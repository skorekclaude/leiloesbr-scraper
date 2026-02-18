"""
Generowanie wariantow wyszukiwania z listy artystow.

Automatycznie tworzy warianty nazwisk:
  1. Pelne imie i nazwisko (bez polskich znakow)
  2. Pelne imie i nazwisko (z polskimi znakami jesli inne)
  3. Samo nazwisko (chyba ze fp_risk == "high")
  4. Samo nazwisko z polskimi znakami (jesli inne)

System confidence do redukcji false positives:
  - "low"    = unikalne nazwisko, mozna szukac samym nazwiskiem
  - "medium" = nazwisko moze wystepowac w innych kontekstach
  - "high"   = bardzo popularne, szukaj tylko pelnym imieniem + kontekstem
"""
import json
import os
from config import DATA_DIR

# === TABELA TRANSLITERACJI POLSKICH ZNAKOW ===
_POLISH_MAP = str.maketrans({
    "a": "a", "c": "c", "e": "e", "l": "l", "n": "n",
    "o": "o", "s": "s", "z": "z", "z": "z",
    "A": "A", "C": "C", "E": "E", "L": "L", "N": "N",
    "O": "O", "S": "S", "Z": "Z", "Z": "Z",
    # Specjalne polskie znaki -> ASCII
    "\u0105": "a",  # a ogonek
    "\u0107": "c",  # c kreska
    "\u0119": "e",  # e ogonek
    "\u0142": "l",  # l kreska
    "\u0144": "n",  # n kreska
    "\u00f3": "o",  # o kreska
    "\u015b": "s",  # s kreska
    "\u017a": "z",  # z kreska
    "\u017c": "z",  # z kropka
    "\u0104": "A",  # A ogonek
    "\u0106": "C",  # C kreska
    "\u0118": "E",  # E ogonek
    "\u0141": "L",  # L kreska
    "\u0143": "N",  # N kreska
    "\u00d3": "O",  # O kreska
    "\u015a": "S",  # S kreska
    "\u0179": "Z",  # Z kreska
    "\u017b": "Z",  # Z kropka
})

# === TABELA ODWROTNA: ASCII -> POLSKIE WARIANTY ===
# Dla kazdej litery ASCII, ktora moze byc spolszczona
_POLISH_VARIANTS = {
    "a": ["\u0105"],       # a -> ą
    "c": ["\u0107"],       # c -> ć
    "e": ["\u0119"],       # e -> ę
    "l": ["\u0142"],       # l -> ł
    "n": ["\u0144"],       # n -> ń
    "o": ["\u00f3"],       # o -> ó
    "s": ["\u015b"],       # s -> ś
    "z": ["\u017a", "\u017c"],  # z -> ź, ż
}

# Popularne polskie nazwiska (duzo false positives w brazylijskich aukcjach)
_COMMON_SURNAMES = {
    "brandt", "stern", "weiss", "hartwig", "kossak", "singer",
    "kowalski", "nowak", "majewski", "krawczyk", "pawlak",
    "sobczyk", "tomaszewski", "dominik", "gorka", "sadowski",
    "polska", "zak", "hayden",
}


def strip_polish(text):
    """Usuwa polskie znaki diakrytyczne z tekstu."""
    return text.translate(_POLISH_MAP)


def add_polish_diacritics(name):
    """
    Probuje dodac polskie znaki diakrytyczne do nazwy.
    Zwraca wariant z polskimi znakami lub None jesli identyczny.

    Uzywa slownika znanych zamian w polskich nazwiskach.
    """
    # Znane zamiany w popularnych fragmentach polskich nazwisk
    known_replacements = {
        # Nazwiska
        "Wyspianski": "Wyspia\u0144ski",
        "Beksinski": "Beksi\u0144ski",
        "Chelmonski": "Che\u0142mo\u0144ski",
        "Strzeminski": "Strzemi\u0144ski",
        "Stryjenska": "Stryje\u0144ska",
        "Slewinski": "Slewi\u0144ski",
        "Slendzinski": "Slendzi\u0144ski",
        "Witkiewicz": "Witkiewicz",  # bez zmian
        "Malczewski": "Malczewski",  # bez zmian
        "Kossak": "Kossak",
        "Matejko": "Matejko",
        "Mehoffer": "Mehoffer",
        "Siemiradzki": "Siemiradzki",
        "Pankiewicz": "Pankiewicz",
        "Boznanska": "Bozna\u0144ska",
        "Podkowinski": "Podkowi\u0144ski",
        "Wyczolkowski": "Wycz\u00f3\u0142kowski",
        "Tetmajer": "Tetmajer",
        "Axentowicz": "Axentowicz",
        "Chelmonski": "Che\u0142mo\u0144ski",
        "Gierymski": "Gierymski",
        "Dunikowski": "Dunikowski",
        "Sienkiewicz": "Sienkiewicz",
        "Szymborska": "Szymborska",
        "Milosz": "Mi\u0142osz",
        # Imiona
        "Jozef": "J\u00f3zef",
        "Stanislaw": "Stanis\u0142aw",
        "Wladyslaw": "W\u0142adys\u0142aw",
        "Zdzislaw": "Zdzis\u0142aw",
        "Wojciech": "Wojciech",
        "Tadeusz": "Tadeusz",
        "Czeslaw": "Czes\u0142aw",
        "Wislawa": "Wis\u0142awa",
        "Wlodzimierz": "W\u0142odzimierz",
        "Jozefa": "J\u00f3zefa",
        "Kazimierz": "Kazimierz",
        "Bronislaw": "Bronis\u0142aw",
        "Zbigniew": "Zbigniew",
        "Franciszek": "Franciszek",
        "Konrad": "Konrad",
        "Ludomir": "Ludomir",
        "Aleksander": "Aleksander",
        "Maksymilian": "Maksymilian",
        "Felicjan": "Felicjan",
        "Ferdynand": "Ferdynand",
        "Henryk": "Henryk",
        "Tymon": "Tymon",
        "Eugeniusz": "Eugeniusz",
        "Waclaw": "Wac\u0142aw",
        "Rafal": "Rafa\u0142",
        "Miroslaw": "Miros\u0142aw",
        "Jaroslaw": "Jaros\u0142aw",
        "Przemyslaw": "Przemys\u0142aw",
        "Pawel": "Pawe\u0142",
        "Krzysztof": "Krzysztof",
        # Ogólne zamiany
        "Olbinski": "Olbi\u0144ski",
        "Fijalkowski": "Fija\u0142kowski",
        "Krzyzanowski": "Krzy\u017canowski",
        "Niesiolowski": "Niesi\u00f3\u0142owski",
        "Cieslewicz": "Cieslewicz",  # Cie\u015blewicz
        "Mlodozeniec": "M\u0142odo\u017ceniec",
        "Modzelewski": "Modzelewski",
        "Stanislawski": "Stanis\u0142awski",
        "Srzednicki": "Srzednicki",
        "Pagowska": "Pag\u00f3wska",
        "Wlodarski": "W\u0142odarski",
        "Tchorzewski": "Tcz\u00f3rzewski",
        "Strumiłło": "Strumi\u0142\u0142o",
        "Duda-Gracz": "Duda-Gracz",
        "Swierzy": "\u015awierzy",
        "Gorka": "G\u00f3rka",
        "Walkuski": "Wa\u0142kuski",
        "Zebrowski": "\u017bebrowski",
        "Mrozewski": "Mrozewski",
        "Suberlak": "Suberlak",
        "Lewczynski": "Lewczy\u0144ski",
    }

    # Sprobuj zamienic znane fragmenty
    result = name
    for ascii_form, polish_form in known_replacements.items():
        if ascii_form in result and ascii_form != polish_form:
            result = result.replace(ascii_form, polish_form)

    return result if result != name else None


def generate_name_variants(canonical_name, fp_risk="low"):
    """
    Generuje warianty wyszukiwania dla artysty.

    Zwraca liste unikalnych terminow do szukania na leiloesbr.
    """
    variants = set()
    name = canonical_name.strip()

    # 1. Pelne imie i nazwisko (ASCII)
    ascii_name = strip_polish(name)
    variants.add(ascii_name)

    # 2. Pelne imie z polskimi znakami
    polish_name = add_polish_diacritics(ascii_name)
    if polish_name and polish_name != ascii_name:
        variants.add(polish_name)

    # 3. Samo nazwisko (chyba ze high risk)
    parts = ascii_name.split()
    if len(parts) >= 2 and fp_risk != "high":
        surname = parts[-1]
        # Obsluga nazwisk zlozonych (np. "Duda-Gracz", "Nacht-Samborski")
        if "-" in name:
            surname = parts[-1]  # Calosc z myslnikiem
        variants.add(surname)

        # Nazwisko z polskimi znakami
        polish_surname = add_polish_diacritics(surname)
        if polish_surname and polish_surname != surname:
            variants.add(polish_surname)

    # 4. Specjalne warianty
    # Witkacy
    if "Witkiewicz" in name and "Ignacy" in name:
        variants.add("Witkacy")

    # Nikifor
    if "Nikifor" in name:
        variants.add("Nikifor")

    # Mela Muter (Mutermilch)
    if "Muter" in name:
        variants.add("Mutermilch")

    # Marcoussis / Markus
    if "Marcoussis" in name:
        variants.add("Markus")
        variants.add("Ludwik Markus")

    # Lempicka
    if "Lempicka" in name:
        variants.add("Lempicka")
        variants.add("\u0141empicka")

    # Mondzain / Mondszajn
    if "Mondzain" in name:
        variants.add("Mondszajn")

    return sorted(variants)


# === DODATKOWE FRAZY (nie-artystyczne) ===
FURNITURE_TERMS = [
    {"term": "Zalszupin", "category": "furniture", "notes": "Jorge Zalszupin — polski projektant w Brazylii"},
    {"term": "Jorge Zalszupin", "category": "furniture", "notes": "Pelne imie i nazwisko"},
    {"term": "Zalszupina", "category": "furniture", "notes": "Wariant odmieniony (portugalski)"},
    {"term": "L'Atelier", "category": "furniture", "notes": "Firma Zalszupina — L'Atelier Moveis"},
]


def get_all_search_variants():
    """
    Generuje kompletna liste wariantow do wyszukiwania.

    Laczy artystow z artists_data.py + dodatkowe frazy (meble).
    Kazdy element:
      {
        "term": str,
        "artist_canonical": str|None,
        "category": str,
        "risk": str,
        "context": list[str],
      }
    """
    from artists_data import ARTISTS

    variants = []
    seen_terms = set()

    for artist in ARTISTS:
        name = artist["canonical_name"]
        fp_risk = artist.get("fp_risk", "low")
        context = artist.get("context", [])
        category = artist.get("category", "painter")

        # Generuj warianty nazw
        name_variants = generate_name_variants(name, fp_risk)

        for term in name_variants:
            key = term.lower()
            if key in seen_terms:
                continue
            seen_terms.add(key)

            variants.append({
                "term": term,
                "artist_canonical": name,
                "category": category,
                "risk": fp_risk,
                "context": context,
            })

    # Dodaj frazy meblowe
    for ft in FURNITURE_TERMS:
        key = ft["term"].lower()
        if key in seen_terms:
            continue
        seen_terms.add(key)
        variants.append({
            "term": ft["term"],
            "artist_canonical": None,
            "category": ft["category"],
            "risk": "low",
            "context": [],
        })

    return variants


def get_unique_search_terms():
    """
    Zwraca zredukowana liste unikalnych terminow do wyszukiwania.
    Wrapper na get_all_search_variants() — deduplikacja case-insensitive.
    """
    seen = set()
    unique = []
    for v in get_all_search_variants():
        key = v["term"].lower()
        if key not in seen:
            seen.add(key)
            unique.append(v)
    return unique


# === EKSPORT STARYCH STALYCH DLA KOMPATYBILNOSCI Z database.py ===
# database.py uzywa POLISH_ARTISTS i FURNITURE_TERMS do seedowania

def _build_polish_artists_for_db():
    """Buduje liste artystow w formacie wymaganym przez database.seed_artists()."""
    from artists_data import ARTISTS

    result = []
    for artist in ARTISTS:
        name = artist["canonical_name"]
        fp_risk = artist.get("fp_risk", "low")

        entry = {
            "canonical_name": name,
            "variants": generate_name_variants(name, fp_risk),
            "nationality": "Polish",
            "birth_year": artist.get("birth_year"),
            "death_year": artist.get("death_year"),
            "category": artist.get("category", "painter"),
        }
        result.append(entry)
    return result


# Lazy-loaded
_POLISH_ARTISTS_CACHE = None

def get_polish_artists():
    """Zwraca liste artystow w formacie kompatybilnym z database.seed_artists()."""
    global _POLISH_ARTISTS_CACHE
    if _POLISH_ARTISTS_CACHE is None:
        _POLISH_ARTISTS_CACHE = _build_polish_artists_for_db()
    return _POLISH_ARTISTS_CACHE


# ============================================================
# MAIN — diagnostyka
# ============================================================
if __name__ == "__main__":
    import sys, io
    if sys.stdout.encoding != "utf-8":
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

    terms = get_unique_search_terms()
    artists = get_polish_artists()

    print("=" * 70)
    print("SEARCH TERMS — DIAGNOSTYKA")
    print("=" * 70)
    print(f"Artystow w bazie:     {len(artists)}")
    print(f"Terminow wyszukiwania: {len(terms)}")
    print()

    # Statystyki po kategoriach
    cats = {}
    for a in artists:
        c = a.get("category", "?")
        cats[c] = cats.get(c, 0) + 1
    print("Kategorie artystow:")
    for c, n in sorted(cats.items(), key=lambda x: -x[1]):
        print(f"  {c}: {n}")

    # Statystyki po ryzyku
    risks = {"low": 0, "medium": 0, "high": 0}
    for t in terms:
        risks[t["risk"]] = risks.get(t["risk"], 0) + 1
    print(f"\nRyzyko false positive w terminach:")
    for r, n in risks.items():
        print(f"  {r}: {n}")

    # Przykladowe warianty
    print(f"\nPrzykladowe warianty:")
    examples = ["Stanislaw Wyspianski", "Tamara de Lempicka", "Jozef Chelmonski",
                 "Mojzesz Kisling", "Frans Krajcberg"]
    from artists_data import ARTISTS as ALL
    for ex_name in examples:
        artist = next((a for a in ALL if a["canonical_name"] == ex_name), None)
        if artist:
            fp = artist.get("fp_risk", "low")
            vs = generate_name_variants(ex_name, fp)
            print(f"  {ex_name}: {vs}")
