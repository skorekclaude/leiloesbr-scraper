"""
Scraper aukcji leiloesbr.com.br — celowane wyszukiwanie.

Zamiast skanowac 872 stron, uzywa parametru pesquisa= do celowanego
wyszukiwania kazdego artysty/frazy. ~60 zapytan zamiast ~872.

Funkcje:
  - Wyszukiwanie po wariantach nazwisk
  - Parsowanie cen, dat, domow aukcyjnych
  - Deduplikacja (UNIQUE w bazie)
  - Scoring confidence (false positive reduction)
  - Resume po przerwaniu
  - Pobieranie miniaturek
"""
import sys
import io

# Fix kodowania Windows (cp1252 nie obsluguje polskich znakow)
if sys.stdout.encoding != "utf-8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

import requests
from bs4 import BeautifulSoup
import re
import os
import json
import time
from datetime import datetime
from urllib.parse import quote, urljoin

from config import (
    LEILOESBR_SEARCH_URL, LEILOESBR_FULL_SCAN_URL,
    REQUEST_DELAY, REQUEST_TIMEOUT, MAX_RETRIES, RETRY_DELAY,
    USER_AGENT, DOWNLOAD_IMAGES, AUCTION_IMAGES_DIR, SCRAPER_STATE_PATH,
)
from database import (
    get_connection, upsert_auction_item, get_artist_id_by_name,
    start_scraper_run, finish_scraper_run,
)
from search_terms import get_unique_search_terms


class LeiloesBrScraper:
    """Scraper dla leiloesbr.com.br z celowanym wyszukiwaniem."""

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": USER_AGENT})
        self.conn = get_connection()
        self.search_terms = get_unique_search_terms()

        # Statystyki
        self.stats = {
            "terms_searched": 0,
            "pages_scraped": 0,
            "items_found": 0,
            "new_items": 0,
            "errors": 0,
            "error_log": "",
        }

        # Resume state
        self.state = self._load_state()

    # ============================================================
    # GLOWNA PETLA
    # ============================================================

    def run(self):
        """Uruchamia pelne skanowanie."""
        print("=" * 70)
        print("LEILOESBR ART SCRAPER — CELOWANE WYSZUKIWANIE")
        print("=" * 70)
        print(f"Terminy do przeszukania: {len(self.search_terms)}")
        print(f"Start: {datetime.now().strftime('%H:%M:%S')}")
        print("=" * 70)

        run_id = start_scraper_run(self.conn)
        start_time = time.time()

        completed_terms = set(self.state.get("completed_terms", []))

        for i, sv in enumerate(self.search_terms):
            term = sv["term"]

            # Pomin juz przeszukane terminy (resume)
            if term in completed_terms:
                continue

            print(f"\n[{i+1}/{len(self.search_terms)}] Szukam: \"{term}\" ({sv['category']})")

            try:
                found = self._search_term(sv)
                self.stats["terms_searched"] += 1
                completed_terms.add(term)
                self._save_state(list(completed_terms))

                if found > 0:
                    print(f"  -> Znaleziono {found} lotow")

            except KeyboardInterrupt:
                print("\n\nPrzerwane przez uzytkownika. Stan zapisany — mozna wznowic.")
                self._save_state(list(completed_terms))
                self.stats["status"] = "interrupted"
                finish_scraper_run(self.conn, run_id, self.stats)
                self.conn.close()
                return self.stats

            except Exception as e:
                self.stats["errors"] += 1
                self.stats["error_log"] += f"[{term}] {str(e)}\n"
                print(f"  BLAD: {e}")

            time.sleep(REQUEST_DELAY)

        # Zakonczenie
        elapsed = (time.time() - start_time) / 60
        self.stats["status"] = "completed"
        finish_scraper_run(self.conn, run_id, self.stats)

        # Wyczysc state (zakonczono wszystko)
        self._clear_state()

        print("\n" + "=" * 70)
        print("ZAKONCZONE!")
        print(f"  Terminy:    {self.stats['terms_searched']}")
        print(f"  Strony:     {self.stats['pages_scraped']}")
        print(f"  Znalezione: {self.stats['items_found']}")
        print(f"  Nowe:       {self.stats['new_items']}")
        print(f"  Bledy:      {self.stats['errors']}")
        print(f"  Czas:       {elapsed:.1f} min")
        print("=" * 70)

        self.conn.close()
        return self.stats

    # ============================================================
    # WYSZUKIWANIE JEDNEGO TERMINU
    # ============================================================

    def _search_term(self, search_variant):
        """Przeszukuje strony wynikow dla jednego terminu. Zwraca liczbe znalezisk."""
        term = search_variant["term"]
        total_found = 0
        page = 1

        while True:
            url = LEILOESBR_SEARCH_URL.format(term=quote(term), page=page)
            html = self._fetch_page(url)
            if html is None:
                break

            soup = BeautifulSoup(html, "html.parser")
            products = soup.find_all("div", class_="product")

            if not products:
                break  # Brak wynikow na tej stronie

            for product_div in products:
                item_data = self._parse_product(product_div, search_variant)
                if item_data:
                    item_id, is_new = upsert_auction_item(self.conn, item_data)
                    self.stats["items_found"] += 1
                    total_found += 1
                    if is_new:
                        self.stats["new_items"] += 1
                        confidence = item_data.get("match_confidence", "high")
                        emoji = {"high": "🎯", "medium": "🟡", "low": "🔴"}.get(confidence, "")
                        print(f"  {emoji} NOWY: {item_data['title'][:60]}...")
                        if item_data.get("price_text"):
                            print(f"       Cena: {item_data['price_text']}")

            self.conn.commit()
            self.stats["pages_scraped"] += 1

            # Sprawdz czy jest nastepna strona
            next_link = soup.find("a", href=re.compile(rf"pag={page+1}"))
            if next_link and len(products) >= 10:
                page += 1
                time.sleep(REQUEST_DELAY)
            else:
                break

        return total_found

    # ============================================================
    # FETCH Z RETRY
    # ============================================================

    def _fetch_page(self, url):
        """Pobiera strone z retry. Zwraca HTML lub None."""
        for attempt in range(MAX_RETRIES):
            try:
                response = self.session.get(url, timeout=REQUEST_TIMEOUT)
                response.encoding = "utf-8"

                if response.status_code == 200:
                    return response.text
                elif response.status_code == 429:
                    wait = RETRY_DELAY * (attempt + 2)
                    print(f"  Rate limited (429), czekam {wait}s...")
                    time.sleep(wait)
                else:
                    print(f"  HTTP {response.status_code} dla {url}")
                    return None

            except requests.exceptions.Timeout:
                print(f"  Timeout (proba {attempt+1}/{MAX_RETRIES})")
                time.sleep(RETRY_DELAY)
            except requests.exceptions.RequestException as e:
                print(f"  Blad sieci: {e} (proba {attempt+1}/{MAX_RETRIES})")
                time.sleep(RETRY_DELAY)

        return None

    # ============================================================
    # PARSOWANIE PRODUKTU
    # ============================================================

    def _parse_product(self, div, search_variant):
        """
        Parsuje jeden div.product i zwraca dict danych.
        Zwraca None jesli nie mozna sparsowac.
        """
        try:
            # Tytul — szukamy linka do katalogu (abre_catalogo)
            catalog_links = div.find_all("a", href=re.compile(r"abre_catalogo"))
            title_el = None
            for cl in catalog_links:
                text = cl.get_text(strip=True)
                if text:  # Bierz pierwszy link z tekstem
                    title_el = cl
                    break
            if not title_el and catalog_links:
                title_el = catalog_links[0]  # fallback na pierwszy link
            if not title_el:
                return None

            title = title_el.get_text(strip=True)
            # Jesli tytul pusty, uzyj alt z obrazka
            if not title:
                img_el = div.find("img")
                title = img_el.get("alt", "") if img_el else ""
            if not title:
                return None

            # Link katalogowy
            href = title_el.get("href", "")
            catalog_url = href if href.startswith("http") else f"https://www.leiloesbr.com.br/{href}"

            # Parsuj link: abre_catalogo.asp?t=1|site_url|auction_id|item_id
            site_item_id = None
            auction_id = None
            auction_house_url = None

            match = re.search(r"abre_catalogo\.asp\?t=([^|]*)\|([^|]*)\|([^|]*)\|([^|&]*)", href)
            if match:
                auction_house_url = match.group(2)
                auction_id = match.group(3)
                site_item_id = match.group(4)
            else:
                # Fallback — uzyj hash tytulu
                site_item_id = str(hash(title + href))

            # Opis z alt obrazka
            img_el = div.find("img")
            description = img_el.get("alt", "") if img_el else ""
            image_url = img_el.get("src", "") if img_el else ""

            # Cena
            price_el = div.find("div", class_=re.compile(r"product-price|venda-price"))
            price_text = price_el.get_text(strip=True) if price_el else ""
            price_brl = self._parse_price(price_text)

            # Data i stan (lokalizacja)
            info_divs = div.find_all("div", class_="mostbidded__info")
            auction_date = None
            auction_time = None
            auction_state = None
            auction_house = None

            if info_divs:
                # Pierwszy info: data i lokalizacja
                date_text = info_divs[0].get_text(strip=True)
                auction_date, auction_time, auction_state = self._parse_date_location(date_text)

                # Ostatni info: dom aukcyjny
                if len(info_divs) > 1:
                    house_el = info_divs[-1].find("a")
                    if house_el:
                        auction_house = house_el.get_text(strip=True)
                    else:
                        auction_house = info_divs[-1].get_text(strip=True)

            # Confidence scoring
            confidence = self._assess_confidence(title, description, search_variant)

            # Pobierz miniaturke
            image_local = None
            if DOWNLOAD_IMAGES and image_url and site_item_id:
                image_local = self._download_image(image_url, site_item_id)

            # Znajdz artist_id
            artist_id = None
            if search_variant.get("artist_canonical"):
                artist_id = get_artist_id_by_name(self.conn, search_variant["artist_canonical"])

            return {
                "site_item_id": str(site_item_id),
                "source_site": "leiloesbr",
                "auction_id": str(auction_id) if auction_id else None,
                "title": title,
                "description": description,
                "price_text": price_text,
                "price_brl": price_brl,
                "currency": "BRL",
                "image_url": image_url,
                "image_local": image_local,
                "auction_date": auction_date,
                "auction_time": auction_time,
                "auction_state": auction_state,
                "auction_house": auction_house,
                "auction_house_url": auction_house_url,
                "catalog_url": catalog_url,
                "matched_term": search_variant["term"],
                "matched_artist_id": artist_id,
                "match_confidence": confidence,
            }

        except Exception as e:
            self.stats["errors"] += 1
            self.stats["error_log"] += f"[parse] {str(e)}\n"
            return None

    # ============================================================
    # PARSOWANIE DANYCH
    # ============================================================

    def _parse_price(self, text):
        """Parsuje 'R$ 16.000,00' -> 16000.00. Zwraca None jesli nie da sie."""
        if not text:
            return None
        try:
            # Usun wszystko poza cyframi, kropkami i przecinkami
            cleaned = re.sub(r"[^\d.,]", "", text)
            if not cleaned:
                return None
            # Brazylijski format: 16.000,00 -> 16000.00
            cleaned = cleaned.replace(".", "").replace(",", ".")
            return float(cleaned)
        except (ValueError, TypeError):
            return None

    def _parse_date_location(self, text):
        """
        Parsuje '27/2/2026 - 19h -RJ' -> ('2026-02-27', '19:00', 'RJ').
        Zwraca (date, time, state) — kazde moze byc None.
        """
        date_str = None
        time_str = None
        state_str = None

        if not text:
            return None, None, None

        # Data: dd/mm/yyyy
        date_match = re.search(r"(\d{1,2})/(\d{1,2})/(\d{4})", text)
        if date_match:
            day, month, year = date_match.groups()
            date_str = f"{year}-{int(month):02d}-{int(day):02d}"

        # Czas: 19h lub 19:00
        time_match = re.search(r"(\d{1,2})h(\d{2})?", text)
        if time_match:
            hour = time_match.group(1)
            minute = time_match.group(2) or "00"
            time_str = f"{int(hour):02d}:{minute}"

        # Stan: -RJ, -SP, -MG (2-literowy kod po myslniku)
        state_match = re.search(r"-\s*([A-Z]{2})\s*$", text)
        if state_match:
            state_str = state_match.group(1)

        return date_str, time_str, state_str

    def _assess_confidence(self, title, description, search_variant):
        """
        Ocenia pewnosc dopasowania.
        - high: unikalne nazwisko, pewne trafienie
        - medium: mozliwe trafienie, wymaga uwagi
        - low: prawdopodobnie false positive
        """
        risk = search_variant.get("risk", "low")

        if risk == "low":
            return "high"

        # Dla medium/high risk: sprawdz kontekst
        context_words = search_variant.get("context", [])
        if not context_words:
            return "medium" if risk == "medium" else "low"

        # Szukaj slow kontekstowych w tytule i opisie
        combined = (title + " " + description).lower()
        for word in context_words:
            if word.lower() in combined:
                return "high" if risk == "medium" else "medium"

        # Brak kontekstu
        return "medium" if risk == "medium" else "low"

    # ============================================================
    # POBIERANIE OBRAZKOW
    # ============================================================

    def _download_image(self, url, item_id):
        """Pobiera miniaturke. Zwraca lokalna sciezke lub None."""
        if not url or not item_id:
            return None

        filename = f"{item_id}.jpg"
        local_path = os.path.join(AUCTION_IMAGES_DIR, filename)

        if os.path.exists(local_path):
            return local_path  # Juz pobrano

        try:
            response = self.session.get(url, timeout=10, stream=True)
            if response.status_code == 200:
                with open(local_path, "wb") as f:
                    for chunk in response.iter_content(1024):
                        f.write(chunk)
                return local_path
        except Exception:
            pass

        return None

    # ============================================================
    # RESUME / STATE
    # ============================================================

    def _load_state(self):
        """Wczytuje stan z pliku (do wznawiania)."""
        if os.path.exists(SCRAPER_STATE_PATH):
            try:
                with open(SCRAPER_STATE_PATH, "r") as f:
                    state = json.load(f)
                # Sprawdz czy state jest z dzisiaj
                if state.get("date") == datetime.now().strftime("%Y-%m-%d"):
                    print(f"Wznawiam z {len(state.get('completed_terms', []))} ukonczonych terminow")
                    return state
            except (json.JSONDecodeError, KeyError):
                pass
        return {"date": datetime.now().strftime("%Y-%m-%d"), "completed_terms": []}

    def _save_state(self, completed_terms):
        """Zapisuje stan do pliku."""
        state = {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "completed_terms": completed_terms,
            "saved_at": datetime.now().isoformat(),
        }
        with open(SCRAPER_STATE_PATH, "w") as f:
            json.dump(state, f, indent=2)

    def _clear_state(self):
        """Usuwa plik stanu po pomyslnym zakonczeniu."""
        if os.path.exists(SCRAPER_STATE_PATH):
            os.remove(SCRAPER_STATE_PATH)


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    from database import init_db
    from search_terms import get_polish_artists, FURNITURE_TERMS
    from database import seed_artists, seed_search_terms

    init_db()
    seed_artists(get_polish_artists())
    seed_search_terms(FURNITURE_TERMS)

    scraper = LeiloesBrScraper()
    stats = scraper.run()

    print(f"\nGotowe! Nowe znaleziska: {stats['new_items']}")
