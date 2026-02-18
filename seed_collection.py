#!/usr/bin/env python3
r"""
seed_collection.py - Import 174 obiektow z Google Sheets CSV do bazy kolekcji.

Zrodlo: leiloesbr_google_sheet.csv
Cel:    artcollection.db -> tabela collection_objects

Uzycie:
    python seed_collection.py
    python seed_collection.py --csv sciezka/do/pliku.csv
    python seed_collection.py --dry-run
"""

import csv
import re
import sys
import os
import argparse
from collections import Counter

# Fix Windows console encoding
import io
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

# Dodaj katalog skryptu do PATH
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import database

# ============================================================
# ŚCIEŻKI
# ============================================================
DEFAULT_CSV = os.path.join(os.path.expanduser("~"), "leiloesbr_google_sheet.csv")

# ============================================================
# ZNANI ARTYŚCI — mapowanie z wariantów na kanoniczne nazwy
# ============================================================
KNOWN_ARTISTS = {
    # Polscy
    "LASAR SEGALL": "Lasar Segall",
    "KAROL KOSSAC": "Karol Kossak",
    "KAROL KOSSAK": "Karol Kossak",
    "CAROL KOSSAK": "Karol Kossak",
    "LEON LEWKOIWICZ": "Leon Lewkowicz",
    "LEON LEWKOWICZ": "Leon Lewkowicz",
    "BRUNO LECHOWSKI": "Bruno Lechowski",
    "AGATA STOMMA": "Agata Stomma",
    "ÁGATA STOMMA": "Agata Stomma",
    "FAYGA OSTROWER": "Fayga Ostrower",

    # Brazylijscy
    "CANDIDO PORTINARI": "Candido Portinari",
    "ALFREDO VOLPI": "Alfredo Volpi",
    "OSCAR NIEMEYER": "Oscar Niemeyer",
    "ATHOS BULCÃO": "Athos Bulcão",
    "FRANS KRAJCBERG": "Frans Krajcberg",
    "HÉRCULES BARSOTTI": "Hércules Barsotti",
    "HERCULES BARSOTTI": "Hércules Barsotti",
    "ANTONIO BANDEIRA": "Antônio Bandeira",
    "ANTÔNIO BANDEIRA": "Antônio Bandeira",
    "TOMOSHIGE KUSUNO": "Tomoshige Kusuno",
    "WESLEY DUKE LEE": "Wesley Duke Lee",
    "EVANDRO TEIXEIRA": "Evandro Teixeira",
    "ELIANE AVELLÁN": "Eliane Avellán",

    # Europejscy awangardziści
    "WASSILY KANDINSKY": "Wassily Kandinsky",
    "W. KANDINSKY": "Wassily Kandinsky",
    "JEAN ARP": "Jean Arp",
    "HANS ARP": "Jean Arp",
    "ALBERT GLEIZES": "Albert Gleizes",
    "THEO VAN DOESBURG": "Theo van Doesburg",
    "VICTOR VASARELY": "Victor Vasarely",
    "SALVADOR DALI": "Salvador Dalí",
    "SALVADOR DALÍ": "Salvador Dalí",
    "ANDY WARHOL": "Andy Warhol",
    "GEORGE BRAQUE": "Georges Braque",
    "GEORGES BRAQUE": "Georges Braque",
    "PICASSO": "Pablo Picasso",
    "PABLO PICASSO": "Pablo Picasso",
    "NICOLAS DE STÄEL": "Nicolas de Staël",
    "NICOLAS DE STAËL": "Nicolas de Staël",

    # Design
    "JORGE ZALSZUPIN": "Jorge Zalszupin",
    "WILLY GUHL": "Willy Guhl",
    "GAETANO PESCE": "Gaetano Pesce",
    "LUDWIG MIES VAN DER ROHE": "Ludwig Mies van der Rohe",
    "CHARLOTTE PERRIAND": "Charlotte Perriand",
    "ANDRIES DIRK COPIER": "Andries Dirk Copier",

    # Inni
    "MANE-KATZ": "Mané-Katz",
    "MANÉ-KATZ": "Mané-Katz",
    "VOLTI": "Antoniucci Volti",
    "ANTON PRINNER": "Anton Prinner",
    "GIORGIO ROSSI": "Giorgio Rossi",
    "OLDRICH KULHÁNEK": "Oldřich Kulhánek",
    "JAN SAUDEK": "Jan Saudek",
    "ZBIGNIEW LIBERA": "Zbigniew Libera",
    "GÉRARD GASIOROWSKI": "Gérard Gasiorowski",
    "ALISON BOOTHROYD": "Alison Boothroyd",
    "ANTOINE VAN DYCK": "Antoine van Dyck",
    "W. MUCHA": "W. Mucha",
    "CRISTOBAL HALFFTER": "Cristóbal Halffter",
    "CRISTÓBAL HALFFTER": "Cristóbal Halffter",
    "H. TRUCI": "H. Truci",
    "BANFI": "Banfi",
    "ANITTA KAUFFAMAN": "Anitta Kauffaman",
    "DAREL": "Darel Valença Lins",
}


# ============================================================
# KATEGORIE — reguły detekcji (kolejność ma znaczenie!)
# ============================================================
CATEGORY_RULES = [
    # Meble / Design — muszą być przed innymi bo np. "mesa" mogłoby trafić do "Inne"
    (["poltrona", "cadeira", "mesa de centro", "mesa ", "chaise", "sofá",
      "geleira", "rack", "estante", "cadeira de auditório", "day bed",
      "puff", "móvel", "mobiliário", "pétala", "sênior", "ouro preto",
      "chanceler", "andorinha", "envelopada", "barcelona"],
     "Mebel / Design"),

    # Vaso / design obiektowy
    (["vaso ", "floreiro"],
     "Design / Obiekt"),

    # Fotografia
    (["fotografia", "foto ", "fotografias", "fotos ", "foto.", "foto,",
      "fotograficzna", "fotográfico", "conjunto fotográfico", "fotografii"],
     "Fotografia"),

    # Grafika (serigrafie, litografie, gravury)
    (["serigrafia", "litografia", "litogravura", "gravura", "ponta seca",
      "xilogravura", "água-forte", "litograph", "heliogravura",
      "impressão artística", "fine art sobre tela"],
     "Grafika"),

    # Malarstwo
    (["o.s.t.", "óleo sobre tela", "óleo s/ tela", "óleo sobre eucatex",
      "óleo s/ eucatex", "óleo sobre cartão", "acrílica sobre",
      "aquarela sobre", "técnica mista sobre tela", "óleo sobre"],
     "Malarstwo"),

    # Rysunek
    (["desenho s/", "desenho,", "estudo,", "nanquim", "carvão", "crayon",
      "lápis sobre", "guache sobre papel", "guasz"],
     "Rysunek"),

    # Rzeźba
    (["escultura", "sculpture", "budha", "buddha", "bronze com base",
      "bronze,", "terracota", "estátua", "estatueta"],
     "Rzeźba"),

    # Tkanina
    (["tapeçaria", "tapestry", "aubusson"],
     "Tkanina"),

    # Szkło / Ceramika artystyczna
    (["daum nancy", "cameo glass", "cristal de rocha", "cloisonne",
      "celadon", "porcelana chinesa"],
     "Szkło / Ceramika"),

    # Azjatycka sztuka (jade, chiny)
    (["jade", "jadeíta", "jadeita", "disco bi", "dinastia song",
      "dinastia qing", "pedra dura chinesa", "pedra translúcida"],
     "Azjatycka Sztuka"),

    # Sztuka prekolumbijska
    (["pre colombiana", "pré-colombian", "chavin", "totonaca"],
     "Sztuka Prekolumbijska"),

    # Dokument / Militaria
    (["documento", "paszport", "passaporte", "legitymacja", "credencial",
      "carta manuscrita", "boina militar", "insígnia", "jambiya", "medalha"],
     "Dokument / Militaria"),

    # Książka / Album
    (["livro", "livros", "catálogo", "catálogos", "álbum", "livreto",
      "edição", "brochura", "enc edit", "enc. edit", "capa dura",
      "box com", "pranchas", "exemplar"],
     "Książka / Album"),

    # Muzyka
    (["partytura", "preludio para madrid", "cd e um caderno"],
     "Muzyka"),

    # Biżuteria
    (["pulseira", "pingente", "ouro 18k"],
     "Biżuteria"),

    # Numizmatyka / Medalha
    (["medalha em prata"],
     "Numizmatyka"),
]


def detect_category(description):
    """Wykrywa kategorię na podstawie opisu."""
    desc_lower = description.lower()
    for patterns, category in CATEGORY_RULES:
        for pattern in patterns:
            if pattern.lower() in desc_lower:
                return category
    return "Inne"


# ============================================================
# EKSTRAKCJA ARTYSTY
# ============================================================
def extract_artist(description):
    """Próbuje wyodrębnić artystę z opisu."""
    desc = description.strip()

    # 1) Sprawdź znanych artystów bezpośrednio w opisie
    desc_upper = desc.upper()
    for variant, canonical in KNOWN_ARTISTS.items():
        if variant.upper() in desc_upper:
            return canonical

    # 2) Wzorzec: "IMIĘ NAZWISKO - tytuł" (all caps na początku)
    m = re.match(r'^([A-ZÁÉÍÓÚÀÂÃÊÔÇÑ][A-ZÁÉÍÓÚÀÂÃÊÔÇÑ\s\.]+)\s*[-–—]\s', desc)
    if m:
        name = m.group(1).strip()
        # Odfiltruj fałszywe pozytywne (zbyt ogólne frazy)
        skip = ["SEGUNDA GUERRA", "ARTE PRE", "CHINA", "CONJUNTO",
                "ASSINATURA", "RARA", "FABULOSA", "MAGNIFIC", "GRANDE",
                "MÓVEM", "TAPEÇARIA", "LITOGRAVURA", "LIVRO",
                "POSTER", "ESCOLA", "AUTOR NÃO", "GRAVURA"]
        if not any(s in name.upper() for s in skip) and len(name.split()) <= 5:
            # Capitalize properly
            return name.title()

    # 3) Wzorzec: "Imię Nazwisko - tytuł" (mixed case)
    m = re.match(r'^([A-ZÁÉÍÓÚÀÂÃÊ][a-záéíóúàâãêôçñ]+(?:\s+(?:de\s+|van\s+|di\s+)?[A-ZÁÉÍÓÚÀÂÃÊ][a-záéíóúàâãêôçñ]+)*)\s*[-–—]\s', desc)
    if m:
        name = m.group(1).strip()
        if len(name.split()) >= 2 and len(name) < 40:
            return name

    # 4) Wzorzec "Imię Nazwisko (miasto, rok" na początku
    m = re.match(r'^([A-ZÁÉÍÓÚÀÂÃÊ][a-záéíóúàâãêôçñ]+\s+[A-ZÁÉÍÓÚÀÂÃÊ][a-záéíóúàâãêôçñ]+)\s*\(', desc)
    if m:
        return m.group(1).strip()

    return None


# ============================================================
# EKSTRAKCJA TYTUŁU
# ============================================================
def extract_title(description, artist_name=None):
    """Tworzy krótki tytuł z opisu."""
    desc = description.strip()

    if artist_name:
        # Spróbuj wyciąć artystę z początku i wziąć następny segment
        # Wzorce: "ARTYSTA - Tytuł.", "Artysta - Tytuł -"
        patterns = [
            # "Artysta - Tytuł - reszta" lub "ARTYSTA - Tytuł. reszta"
            re.compile(
                re.escape(artist_name) + r'\s*[-–—]\s*(.+?)(?:\s*[-–—.])',
                re.IGNORECASE
            ),
            # "Artysta (miasto, rok) Tytuł De rok"
            re.compile(
                re.escape(artist_name) + r'\s*\([^)]+\)\s*\.?\s*(.+?)(?:\s*[-–—.])',
                re.IGNORECASE
            ),
        ]
        for pat in patterns:
            m = pat.search(desc)
            if m:
                title = m.group(1).strip().strip('"\'')
                if len(title) > 3:
                    # Skróć do rozsądnej długości
                    if len(title) > 120:
                        title = title[:117] + "..."
                    return title

    # Fallback: weź pierwsze zdanie / fragment (do 120 znaków)
    # Odetnij przy pierwszym kropce, średniku lub przecinku po 20+ znakach
    short = desc[:200]
    for sep in ['. ', '; ', ' - ', ', ']:
        idx = short.find(sep, 20)
        if idx > 0 and idx < 150:
            return short[:idx].strip()

    return short[:120].strip()


# ============================================================
# EKSTRAKCJA MEDIUM (technika)
# ============================================================
MEDIUM_PATTERNS = [
    (r'serigrafia\b', "Serigrafia"),
    (r'litografia\b', "Litografia"),
    (r'litogravura\b', "Litogravura"),
    (r'gravura\s+(?:em\s+)?ponta\s+seca', "Gravura ponta seca"),
    (r'gravura\s+em\s+metal', "Gravura em metal"),
    (r'gravura\b', "Gravura"),
    (r'xilogravura', "Xilogravura"),
    (r'heliogravura', "Heliogravura"),
    (r'água[- ]forte', "Água-forte"),
    (r'impressão artística', "Impressão artística"),
    (r'fine art sobre tela', "Fine art sobre tela"),
    (r'litografia offset', "Litografia offset"),
    (r'o\.s\.t\.', "Óleo sobre tela"),
    (r'óleo s(?:obre|\/) tela', "Óleo sobre tela"),
    (r'óleo s(?:obre|\/) eucatex', "Óleo sobre eucatex"),
    (r'óleo s(?:obre|\/) cartão', "Óleo sobre cartão"),
    (r'óleo sobre papel', "Óleo sobre papel"),
    (r'acrílica sobre', "Acrílica"),
    (r'aquarela sobre', "Aquarela"),
    (r'técnica mista sobre tela', "Técnica mista sobre tela"),
    (r'guache sobre papel', "Guache sobre papel"),
    (r'guasz', "Guache"),
    (r'desenho s\/', "Desenho"),
    (r'nanquim', "Nanquim"),
    (r'fotografia\b', "Fotografia"),
    (r'foto\b', "Fotografia"),
    (r'impressão em gelatina', "Impressão em gelatina"),
    (r'bronze\b', "Bronze"),
    (r'terracota', "Terracota"),
    (r'madeira policromada', "Madeira policromada"),
    (r'estuque', "Estuque"),
    (r'cameo glass', "Cameo glass"),
    (r'fibrocimento', "Fibrocimento"),
]


def extract_medium(description):
    """Wykrywa technikę z opisu."""
    desc_lower = description.lower()
    for pattern, medium in MEDIUM_PATTERNS:
        if re.search(pattern, desc_lower):
            return medium
    return None


# ============================================================
# EKSTRAKCJA WYMIARÓW
# ============================================================
def extract_dimensions(description):
    """Wyciąga wymiary z opisu (cm, m)."""
    # Wzorce: "56 x 77 cm", "0.637 m x 0.49 m", "Med. 35x20 cm", itd.
    patterns = [
        r'(?:med(?:idas)?[.:]\s*)?(\d+(?:[.,]\d+)?\s*x\s*\d+(?:[.,]\d+)?(?:\s*x\s*\d+(?:[.,]\d+)?)?)\s*cm',
        r'(?:med(?:idas)?[.:]\s*)?(\d+(?:[.,]\d+)?\s*x\s*\d+(?:[.,]\d+)?)\s*(?:cm|m\b)',
        r'(\d+\s*cm\s*(?:de\s+)?(?:altura|alt))',
    ]
    for pat in patterns:
        m = re.search(pat, description, re.IGNORECASE)
        if m:
            return m.group(0).strip()
    return None


# ============================================================
# EKSTRAKCJA NAZWY DOMU AUKCYJNEGO
# ============================================================
def clean_auction_house(dom_aukcyjny, tytul_csv):
    """Czyści nazwę domu aukcyjnego."""
    name = dom_aukcyjny.strip()

    # Specjalne przypadki — gdy kolumna ma dziwne wartości
    if name.lower() in ("oficial", "público", "10%", "de 5 %.",
                        "é deposito.", "leilões br"):
        # Spróbuj wyciągnąć z tytułu
        # "Cartela 246259 - Lotes arrematados - Nº XXXXX: NAZWA AUKCJI"
        m = re.search(r'Nº\s*\d+:\s*(.+?)(?:\s*-\s*Envio|\s*$)', tytul_csv)
        if m:
            auction_name = m.group(1).strip()
            # Skróć do 80 znaków
            if len(auction_name) > 80:
                auction_name = auction_name[:77] + "..."
            return auction_name

    # Usuń "www." i ".com.br" z nazwy
    name = re.sub(r'^www\.', '', name)
    name = re.sub(r'\.com\.br$', '', name)
    name = re.sub(r'\.lel\.br$', '', name)
    name = re.sub(r'\.net\.br$', '', name)

    return name if name else "Nieznany"


# ============================================================
# GŁÓWNA FUNKCJA IMPORTU
# ============================================================
def import_from_csv(csv_path, dry_run=False):
    """Importuje obiekty z CSV do bazy danych."""

    if not os.path.exists(csv_path):
        print(f"❌ Plik CSV nie istnieje: {csv_path}")
        return

    # Czytaj CSV
    rows = []
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)

    print(f"[IMPORT] z CSV: {os.path.basename(csv_path)}")
    print(f"   {len(rows)} wierszy wczytanych\n")

    if not rows:
        print("[ERROR] Brak danych w pliku CSV!")
        return

    # Połącz z bazą
    conn = database.get_connection()

    # Usuń stare testowe obiekty (jeśli istnieją)
    if not dry_run:
        deleted = database.delete_all_collection_objects(conn)
        conn.commit()
        if deleted > 0:
            print(f"[DEL] Usunieto {deleted} istniejacych obiektow\n")

    added = 0
    skipped = 0
    errors = 0
    total_value = 0.0
    categories = Counter()

    for i, row in enumerate(rows, 1):
        try:
            # Parsuj pola CSV
            data_csv = row.get("Data", "").strip()
            auction_nr = row.get("Leilão Nr", "").strip()
            tytul_csv = row.get("Tytuł", "").strip()
            dom_aukcyjny = row.get("Dom Aukcyjny", "").strip()
            lot_nr = row.get("Lot Nr", "").strip()
            cena_str = row.get("Cena (R$)", "0").strip()
            opis = row.get("Opis", "").strip()
            status = row.get("Status", "").strip()
            fracht = row.get("Fracht (R$)", "").strip()
            link = row.get("Link", "").strip()

            # Parsuj cenę
            try:
                cena = float(cena_str.replace(",", "."))
            except (ValueError, TypeError):
                cena = 0.0

            # Inventory number
            inv_nr = f"LBR-{auction_nr}-{lot_nr}"

            # Sprawdź duplikat
            if not dry_run and database.collection_object_exists(conn, inv_nr):
                skipped += 1
                continue

            # Ekstrakcja danych
            artist = extract_artist(opis)
            title = extract_title(opis, artist)
            category = detect_category(opis)
            medium = extract_medium(opis)
            dimensions = extract_dimensions(opis)
            auction_house = clean_auction_house(dom_aukcyjny, tytul_csv)

            # Buduj notatki
            notes_parts = []
            if link:
                notes_parts.append(f"URL: {link}")
            if status:
                notes_parts.append(f"Status: {status}")
            if fracht:
                notes_parts.append(f"Fracht: R$ {fracht}")
            notes = "\n".join(notes_parts)

            # Buduj dict
            obj_data = {
                "inventory_number": inv_nr,
                "title": title,
                "artist_name_display": artist,
                "category": category,
                "medium": medium,
                "dimensions_notes": dimensions,
                "description": opis[:1000] if opis else None,
                "acquisition_date": data_csv,
                "acquisition_source": f"leiloesbr.com.br - {auction_house}",
                "acquisition_price": cena,
                "acquisition_currency": "BRL",
                "provenance": f"Leilão Nº {auction_nr}, Lot {lot_nr}",
                "notes": notes if notes else None,
            }

            if dry_run:
                artist_str = f" ({artist})" if artist else ""
                print(f"  [{i:3d}] {inv_nr}: {title[:60]}{artist_str}")
                print(f"        Cat: {category} | R$ {cena:,.2f} | {medium or '-'}")
            else:
                database.add_collection_object(conn, obj_data)

            added += 1
            total_value += cena
            categories[category] += 1

        except Exception as e:
            errors += 1
            print(f"  [WARN] Blad w wierszu {i} (Lot {lot_nr}): {e}")

    # Commit
    if not dry_run:
        conn.commit()

    # Podsumowanie
    print(f"\n{'='*50}")
    print(f"PODSUMOWANIE {'(DRY RUN) ' if dry_run else ''}")
    print(f"{'='*50}")
    print(f"  [OK]   Dodano:    {added}")
    print(f"  [SKIP] Pominieto: {skipped}")
    if errors:
        print(f"  [WARN] Bledow:    {errors}")
    print(f"  [VAL]  Wartosc:   R$ {total_value:,.2f}")
    print(f"\n  Kategorie:")
    for cat, count in categories.most_common():
        print(f"     {cat:25s} -- {count:3d} obiektow")

    conn.close()
    print(f"\n[DONE] {'Symulacja zakonczona' if dry_run else 'Import zakonczony pomyslnie!'}")


# ============================================================
# CLI
# ============================================================
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Import kolekcji z CSV do bazy")
    parser.add_argument("--csv", default=DEFAULT_CSV,
                        help="Path to CSV file (default: ~/leiloesbr_google_sheet.csv)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Dry run - don't write to database")
    args = parser.parse_args()

    import_from_csv(args.csv, dry_run=args.dry_run)
