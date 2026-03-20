#!/usr/bin/env python3
"""
sales_intelligence.py — System klasyfikacji sprzedażowej kolekcji.

Automatycznie przypisuje:
  - sales_tier: A (museum-grade), B (gallery), C (decorative/commodity)
  - target_market: PL, BR, INT, EU, US
  - target_buyers: konkretne domy aukcyjne, galerie, instytucje
  - estimated_market_value_eur: szacunkowa wartość rynkowa w EUR
  - sales_notes: uwagi sprzedażowe

Logika:
  Tier A — muzea, poważni kolekcjonerzy. Artyści z historią aukcyjną >$10k.
           Matejko, Boznańska, Fałat, Witkacy, Stażewski, Strzemiński, Segall, Portinari.
  Tier B — galerie, kolekcjonerzy średni. Artyści rozpoznawalni, prace w dobrym stanie.
           Większość polskich modernistów, École de Paris, rzeźba.
  Tier C — dekoracyjne, rzemiosło, drobne grafiki, meble bez proweniencji.
           Druki, pocztówki, dokumenty, drobne obiekty użytkowe.
"""

import sys
import os

# Fix Windows console encoding
import io
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import database


# ============================================================
# ARTIST MARKET DATA — kto jest warty ile i gdzie sprzedawać
# ============================================================

ARTIST_MARKET = {
    # === TIER A — MUSEUM GRADE ===
    "Jan Matejko": {
        "tier": "A", "market_value_eur": "50000-500000+",
        "markets": ["PL", "INT"],
        "buyers": ["Muzeum Narodowe Kraków", "Muzeum Narodowe Warszawa", "DESA Unicum", "Sotheby's", "Christie's"],
        "notes": "Ikona polskiego malarstwa. Każda praca jest wydarzeniem. Kontaktować MNK pierwsze."
    },
    "Olga Boznańska": {
        "tier": "A", "market_value_eur": "20000-200000",
        "markets": ["PL", "EU", "INT"],
        "buyers": ["DESA Unicum", "Muzeum Narodowe Kraków", "Artcurial Paris", "Polswiss Art"],
        "notes": "Polska impresjonistka, École de Paris. Portrety najcenniejsze. Rynek europejski aktywny."
    },
    "Józef Chełmoński": {
        "tier": "A", "market_value_eur": "30000-300000",
        "markets": ["PL", "INT"],
        "buyers": ["DESA Unicum", "Muzeum Narodowe Warszawa", "Agra-Art"],
        "notes": "Sceny rodzajowe, konie, pejzaże polskie. Kolekcjonerzy polscy płacą premium."
    },
    "Julian Fałat": {
        "tier": "A", "market_value_eur": "15000-150000",
        "markets": ["PL"],
        "buyers": ["DESA Unicum", "Agra-Art", "Muzeum Śląskie"],
        "notes": "Akwarele zimowe ikoniczne. Rynek głównie polski."
    },
    "Jacek Malczewski": {
        "tier": "A", "market_value_eur": "20000-300000",
        "markets": ["PL", "INT"],
        "buyers": ["DESA Unicum", "Muzeum Narodowe Kraków", "Polswiss Art"],
        "notes": "Symbolizm polski. Autoportrety i sceny alegoryczne najcenniejsze."
    },
    "Stanisław Wyspiański": {
        "tier": "A", "market_value_eur": "15000-200000",
        "markets": ["PL"],
        "buyers": ["Muzeum Narodowe Kraków", "DESA Unicum"],
        "notes": "Pastele, witraże, rysunki. Każda praca muzealnej jakości."
    },
    "Tadeusz Kantor": {
        "tier": "A", "market_value_eur": "10000-150000",
        "markets": ["PL", "EU", "INT"],
        "buyers": ["DESA Unicum", "Christie's", "Phillips", "Muzeum Sztuki Łódź"],
        "notes": "Awangarda, Cricot 2. Rynek międzynarodowy rośnie. Teatralia = osobna kategoria."
    },
    "Henryk Stażewski": {
        "tier": "A", "market_value_eur": "5000-80000",
        "markets": ["PL", "EU"],
        "buyers": ["DESA Unicum", "Muzeum Sztuki Łódź", "Polswiss Art"],
        "notes": "Konstruktywizm, geometria. Reliefs najcenniejsze."
    },
    "Władysław Strzemiński": {
        "tier": "A", "market_value_eur": "10000-200000",
        "markets": ["PL", "EU", "INT"],
        "buyers": ["Muzeum Sztuki Łódź", "DESA Unicum", "Christie's"],
        "notes": "Unizm. Prace rzadkie = ceny rosną. Muzeum Sztuki Łódź ma największą kolekcję."
    },
    "Lasar Segall": {
        "tier": "A", "market_value_eur": "10000-500000",
        "markets": ["BR", "INT"],
        "buyers": ["Museu Lasar Segall São Paulo", "Christie's Latin America", "Bolsa de Arte"],
        "notes": "Polsko-brazylijski modernista. Rynek brazylijski dominujący. Museu Lasar Segall = pierwsza instytucja."
    },
    "Candido Portinari": {
        "tier": "A", "market_value_eur": "20000-1000000+",
        "markets": ["BR", "INT"],
        "buyers": ["Christie's Latin America", "Sotheby's", "Bolsa de Arte", "James Lisboa"],
        "notes": "Najważniejszy brazylijski artysta XX w. Każda praca = wydarzenie. Ceny 6-7 cyfrowe."
    },
    "Frans Krajcberg": {
        "tier": "A", "market_value_eur": "5000-100000",
        "markets": ["BR", "EU"],
        "buyers": ["Bolsa de Arte", "Artcurial Paris", "Instituto Krajcberg"],
        "notes": "Polsko-brazylijski. Rzeźby z natury. Rynek brazylijski i francuski."
    },
    "Fayga Ostrower": {
        "tier": "A", "market_value_eur": "3000-50000",
        "markets": ["BR", "PL"],
        "buyers": ["Bolsa de Arte", "Gravura Brasileira", "Fundação Fayga Ostrower"],
        "notes": "Grafika abstrakcyjna. Polsko-brazylijska. Biennale di Venezia 1958."
    },
    "Alfredo Volpi": {
        "tier": "A", "market_value_eur": "20000-500000",
        "markets": ["BR"],
        "buyers": ["Bolsa de Arte", "James Lisboa", "Christie's Latin America"],
        "notes": "Ikona brazylijskiego modernizmu. Bandeirinhas ikoniczne."
    },

    # === TIER A-B — STRONG GALLERY / MUSEUM BORDERLINE ===
    "Bruno Lechowski": {
        "tier": "A", "market_value_eur": "5000-80000",
        "markets": ["BR", "PL"],
        "buyers": ["Bolsa de Arte", "DESA Unicum", "Pinakotheke São Paulo"],
        "notes": "Polski malarz w Brazylii. Pejzaże Rio/SP. Rynek brazylijski rośnie."
    },
    "Karol Kossak": {
        "tier": "B+", "market_value_eur": "3000-30000",
        "markets": ["PL"],
        "buyers": ["DESA Unicum", "Agra-Art", "Rempex"],
        "notes": "Konie, sceny batalistyczne. Solidny rynek polski. Syn Juliusza."
    },
    "Antoniucci Volti": {
        "tier": "B+", "market_value_eur": "2000-40000",
        "markets": ["EU", "INT"],
        "buyers": ["Artcurial Paris", "Drouot", "Piasa"],
        "notes": "Rzeźbiarz francuski. Akty kobiece. Rynek francuski główny."
    },
    "Nicolas de Staël": {
        "tier": "A", "market_value_eur": "50000-5000000+",
        "markets": ["EU", "INT"],
        "buyers": ["Christie's", "Sotheby's", "Artcurial"],
        "notes": "UWAGA: prawdopodobnie album/książka, nie oryginał. Zweryfikuj!"
    },
    "Agata Stomma": {
        "tier": "B", "market_value_eur": "500-5000",
        "markets": ["PL", "BR"],
        "buyers": ["Galerie lokalne", "Sprzedaż bezpośrednia"],
        "notes": "Współczesna artystka polska w Brazylii. Rynek jeszcze budujący się."
    },
    "Hércules Barsotti": {
        "tier": "B+", "market_value_eur": "3000-30000",
        "markets": ["BR"],
        "buyers": ["Bolsa de Arte", "Dan Galeria"],
        "notes": "Konkretyzm brazylijski. Grafiki i malarstwo. Rynek stabilny."
    },
    "Antônio Bandeira": {
        "tier": "A", "market_value_eur": "5000-100000",
        "markets": ["BR", "EU"],
        "buyers": ["Bolsa de Arte", "Christie's Latin America"],
        "notes": "Brazylijski abstrakcjonista. École de Paris. Ceny rosną."
    },
    "Athos Bulcão": {
        "tier": "A", "market_value_eur": "3000-50000",
        "markets": ["BR"],
        "buyers": ["Bolsa de Arte", "James Lisboa"],
        "notes": "Azulejos, murale. Współpraca z Niemeyerem. Prace architektoniczne najcenniejsze."
    },
    "Oscar Niemeyer": {
        "tier": "A", "market_value_eur": "5000-100000",
        "markets": ["BR", "INT"],
        "buyers": ["Christie's", "Sotheby's Design", "Wright Auctions"],
        "notes": "Architekt-ikona. Rysunki, meble, obiekty. Każda sygnatura = wartość."
    },
    "Leon Lewkowicz": {
        "tier": "B", "market_value_eur": "1000-10000",
        "markets": ["BR", "PL"],
        "buyers": ["Bolsa de Arte", "Galerie brazylijskie"],
        "notes": "Polski malarz w Brazylii. Rynek niszowy ale stabilny."
    },
}

# === CATEGORY-BASED TIER DEFAULTS ===
CATEGORY_DEFAULTS = {
    "Malarstwo": {"default_tier": "B", "base_value_eur": "1000-10000"},
    "Rzeźba": {"default_tier": "B", "base_value_eur": "500-8000"},
    "Grafika": {"default_tier": "C+", "base_value_eur": "100-3000"},
    "Rysunek": {"default_tier": "B", "base_value_eur": "200-5000"},
    "Fotografia": {"default_tier": "C+", "base_value_eur": "100-2000"},
    "Mebel / Design": {"default_tier": "B", "base_value_eur": "500-15000"},
    "Książka / Album": {"default_tier": "C", "base_value_eur": "50-500"},
    "Azjatycka Sztuka": {"default_tier": "B", "base_value_eur": "300-5000"},
    "Design / Obiekt": {"default_tier": "B", "base_value_eur": "200-5000"},
    "Dokument / Militaria": {"default_tier": "C", "base_value_eur": "50-500"},
    "Szkło / Ceramika": {"default_tier": "B", "base_value_eur": "200-3000"},
    "Sztuka Prekolumbijska": {"default_tier": "A", "base_value_eur": "2000-50000"},
    "Tkanina": {"default_tier": "C+", "base_value_eur": "100-2000"},
    "Inne": {"default_tier": "C", "base_value_eur": "50-1000"},
}

# === TARGET MARKETS PER CATEGORY ===
CATEGORY_MARKETS = {
    "Malarstwo": {
        "buyers_pl": ["DESA Unicum", "Agra-Art", "Polswiss Art", "Rempex"],
        "buyers_br": ["Bolsa de Arte", "James Lisboa", "Pinacotheque"],
        "buyers_int": ["Christie's", "Sotheby's", "Bonhams", "Dorotheum"],
    },
    "Rzeźba": {
        "buyers_pl": ["DESA Unicum", "Agra-Art"],
        "buyers_br": ["Bolsa de Arte"],
        "buyers_int": ["Christie's", "Sotheby's", "Artcurial"],
    },
    "Grafika": {
        "buyers_pl": ["DESA Unicum", "Rempex", "Libra Aukcje"],
        "buyers_br": ["Gravura Brasileira", "Bolsa de Arte"],
        "buyers_int": ["Swann Galleries NY", "Bonhams Prints"],
    },
    "Fotografia": {
        "buyers_pl": ["DESA Unicum Fotografia", "Rempex"],
        "buyers_br": ["Bolsa de Arte"],
        "buyers_int": ["Phillips Photography", "Christie's Photographs"],
    },
    "Mebel / Design": {
        "buyers_pl": ["DESA Unicum Design", "Libra"],
        "buyers_br": ["Bolsa de Arte Design", "Mercado Livre"],
        "buyers_int": ["Wright Auctions", "Phillips Design", "Artcurial Design"],
    },
    "Książka / Album": {
        "buyers_pl": ["Antykwariat Rara Avis", "Lamus Antykwariat"],
        "buyers_br": ["Livraria Cultura", "Estante Virtual"],
        "buyers_int": ["AbeBooks", "Rare book dealers"],
    },
    "Azjatycka Sztuka": {
        "buyers_pl": ["DESA Unicum"],
        "buyers_br": ["Bolsa de Arte"],
        "buyers_int": ["Christie's Asian Art", "Bonhams Asian Art", "Sotheby's Asia"],
    },
    "Dokument / Militaria": {
        "buyers_pl": ["Antykwariat militarny", "Kolekcjonerzy prywatni"],
        "buyers_br": ["Mercado Livre"],
        "buyers_int": ["Heritage Auctions Militaria"],
    },
    "Sztuka Prekolumbijska": {
        "buyers_pl": [],
        "buyers_br": ["Bolsa de Arte Pre-Colombiana"],
        "buyers_int": ["Christie's Pre-Columbian", "Sotheby's Tribal Art", "Bonhams"],
    },
}


# ============================================================
# CLASSIFICATION ENGINE
# ============================================================

def classify_object(obj):
    """
    Klasyfikuje obiekt kolekcji: tier, rynek, rekomendacje.
    obj: dict (row z collection_objects)
    Returns: dict z polami sprzedażowymi
    """
    artist = (obj.get("artist_name_display") or "").strip()
    category = obj.get("category") or "Inne"
    price_brl = obj.get("acquisition_price") or 0
    title = (obj.get("title") or "").strip()
    description = (obj.get("description") or "").strip()
    medium = (obj.get("medium") or "").strip()

    result = {
        "sales_tier": "C",
        "target_markets": [],
        "target_buyers": [],
        "estimated_market_value_eur": "",
        "sales_strategy": "",
        "sales_priority": 3,  # 1=urgent/high value, 2=medium, 3=low
    }

    # --- 1. Check if artist is in our market data ---
    artist_data = None
    if artist and len(artist) > 2:  # Skip empty/trivial artist names
        for known_artist, data in ARTIST_MARKET.items():
            # Require meaningful match — at least last name
            artist_lower = artist.lower()
            known_lower = known_artist.lower()
            # Split to compare last names
            known_parts = known_lower.split()
            artist_parts = artist_lower.split()
            # Match: full name contained, or last name matches
            if (known_lower in artist_lower or artist_lower in known_lower or
                (len(known_parts) >= 2 and known_parts[-1] in artist_parts) or
                (len(artist_parts) >= 2 and artist_parts[-1] in known_parts)):
                artist_data = data
                break

    if artist_data:
        result["sales_tier"] = artist_data["tier"]
        result["target_markets"] = artist_data["markets"]
        result["target_buyers"] = artist_data["buyers"]
        result["estimated_market_value_eur"] = artist_data["market_value_eur"]
        result["sales_strategy"] = artist_data["notes"]
        result["sales_priority"] = 1 if artist_data["tier"] == "A" else 2
    else:
        # --- 2. Category-based defaults ---
        cat_data = CATEGORY_DEFAULTS.get(category, CATEGORY_DEFAULTS["Inne"])
        result["sales_tier"] = cat_data["default_tier"]
        result["estimated_market_value_eur"] = cat_data["base_value_eur"]

        cat_markets = CATEGORY_MARKETS.get(category, {})
        # Determine market based on price and category
        if price_brl and price_brl > 2000:
            result["target_markets"] = ["BR", "PL"]
            result["target_buyers"] = cat_markets.get("buyers_br", [])[:2] + cat_markets.get("buyers_pl", [])[:2]
            result["sales_priority"] = 2
        elif price_brl and price_brl > 500:
            result["target_markets"] = ["BR"]
            result["target_buyers"] = cat_markets.get("buyers_br", [])[:2]
            result["sales_priority"] = 2
        else:
            result["target_markets"] = ["BR"]
            result["target_buyers"] = cat_markets.get("buyers_br", [])[:1]
            result["sales_priority"] = 3

    # --- 3. Adjust tier based on condition and provenance ---
    condition = (obj.get("condition_grade") or "").lower()
    provenance = (obj.get("provenance") or "").strip()

    # Provenance boosts value
    if provenance and len(provenance) > 20:
        result["sales_strategy"] += " Proweniencja udokumentowana — podnosi wartość."

    # Bad condition lowers tier
    if "poor" in condition or "bad" in condition or "damaged" in condition:
        if result["sales_tier"] == "A":
            result["sales_tier"] = "B+"
        elif result["sales_tier"] == "B":
            result["sales_tier"] = "C+"
        result["sales_strategy"] += " UWAGA: Stan wymaga konserwacji."

    # --- 4. Book/album special handling ---
    if category == "Książka / Album":
        # Check if it's actually a catalog raisonné or important publication
        important_keywords = ["catalogue raisonné", "catálogo", "raisonné", "complete works",
                              "retrospective", "museum", "museu", "exposition"]
        if any(kw in title.lower() or kw in description.lower() for kw in important_keywords):
            result["sales_tier"] = "B"
            result["sales_strategy"] += " Publikacja referencyjna — wartość bibliograficzna."

    # --- 5. Signed works get a boost ---
    signed_keywords = ["assinado", "assinada", "signed", "sygnowany", "sygnowana",
                       "a lápis", "a lapis"]
    if any(kw in title.lower() or kw in description.lower() for kw in signed_keywords):
        result["sales_strategy"] += " Sygnatura potwierdzona."

    # --- 6. Edition info for prints ---
    if category == "Grafika":
        import re
        edition_match = re.search(r'(\d+)/(\d+)', title + " " + description)
        if edition_match:
            edition_num = int(edition_match.group(1))
            edition_total = int(edition_match.group(2))
            if edition_total <= 30:
                result["sales_strategy"] += f" Nakład limitowany {edition_total} — premium."
                if result["sales_tier"] == "C+":
                    result["sales_tier"] = "B"
            elif edition_total <= 100:
                result["sales_strategy"] += f" Nakład {edition_total}."

    return result


# ============================================================
# TIER LABELS
# ============================================================

TIER_LABELS = {
    "A": {"name": "Museum-Grade", "color": "#d4a853", "icon": "🏛️",
           "description": "Klasa muzealna. Artyści z historią aukcyjną >€10k. Kontakt z domami aukcyjnymi i instytucjami."},
    "A-": {"name": "Museum / Top Gallery", "color": "#c4983f", "icon": "🏛️",
            "description": "Graniczny muzeum/galeria. Silni artyści, prace wymagające weryfikacji."},
    "B+": {"name": "Strong Gallery", "color": "#8B7355", "icon": "🖼️",
            "description": "Silna galeria. Rozpoznawalni artyści, solidny rynek wtórny."},
    "B": {"name": "Gallery", "color": "#6B8E5A", "icon": "🖼️",
           "description": "Poziom galeryjny. Artyści z rynkiem, prace w dobrym stanie."},
    "C+": {"name": "Collectible", "color": "#5B7B8A", "icon": "📦",
            "description": "Kolekcjonerskie. Grafiki, fotografie, obiekty z potencjałem."},
    "C": {"name": "Decorative", "color": "#888", "icon": "📦",
           "description": "Dekoracyjne / użytkowe. Sprzedaż lokalna, Mercado Livre, antykwariaty."},
}


# ============================================================
# RUN CLASSIFICATION ON ENTIRE COLLECTION
# ============================================================

def classify_all():
    """Klasyfikuje wszystkie obiekty w kolekcji i zapisuje wyniki."""
    database.init_db()
    conn = database.get_connection()

    # Ensure sales columns exist
    existing_cols = {row[1] for row in conn.execute("PRAGMA table_info(collection_objects)").fetchall()}
    new_cols = {
        "sales_tier": "TEXT DEFAULT 'C'",
        "target_markets": "TEXT",
        "target_buyers": "TEXT",
        "estimated_market_value_eur": "TEXT",
        "sales_strategy": "TEXT",
        "sales_priority": "INTEGER DEFAULT 3",
    }
    for col, typedef in new_cols.items():
        if col not in existing_cols:
            conn.execute(f"ALTER TABLE collection_objects ADD COLUMN {col} {typedef}")
            print(f"  [MIGRATION] Added column: {col}")

    conn.commit()

    # Classify each object
    objects = conn.execute("SELECT * FROM collection_objects").fetchall()
    stats = {"A": 0, "A-": 0, "B+": 0, "B": 0, "C+": 0, "C": 0}
    market_stats = {}

    for obj in objects:
        obj_dict = dict(obj)
        classification = classify_object(obj_dict)

        # Update DB
        conn.execute("""
            UPDATE collection_objects SET
                sales_tier = ?,
                target_markets = ?,
                target_buyers = ?,
                estimated_market_value_eur = ?,
                sales_strategy = ?,
                sales_priority = ?,
                updated_at = datetime('now')
            WHERE id = ?
        """, (
            classification["sales_tier"],
            ", ".join(classification["target_markets"]),
            " | ".join(classification["target_buyers"]),
            classification["estimated_market_value_eur"],
            classification["sales_strategy"].strip(),
            classification["sales_priority"],
            obj_dict["id"],
        ))

        tier = classification["sales_tier"]
        stats[tier] = stats.get(tier, 0) + 1
        for m in classification["target_markets"]:
            market_stats[m] = market_stats.get(m, 0) + 1

    conn.commit()
    conn.close()

    print(f"\n{'='*50}")
    print(f"KLASYFIKACJA SPRZEDAŻOWA — {len(objects)} obiektów")
    print(f"{'='*50}")
    print(f"\n📊 Tiers:")
    for tier, label in TIER_LABELS.items():
        count = stats.get(tier, 0)
        if count > 0:
            print(f"  {label['icon']} {tier} ({label['name']}): {count}")

    print(f"\n🌍 Rynki docelowe:")
    for market, count in sorted(market_stats.items(), key=lambda x: -x[1]):
        names = {"PL": "Polska", "BR": "Brazylia", "EU": "Europa", "INT": "Międzynarodowy", "US": "USA"}
        print(f"  {names.get(market, market)}: {count}")

    print(f"\n✅ Klasyfikacja zakończona.")
    return stats


if __name__ == "__main__":
    classify_all()
