"""
Baza danych SQLite — schemat i funkcje pomocnicze.
Standard muzealny dla katalogowania kolekcji.
"""
import sqlite3
import os
from datetime import datetime
from config import DATABASE_PATH

SCHEMA_VERSION = 1


def get_connection():
    """Tworzy polaczenie z baza danych z wlaczonym WAL i foreign keys."""
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row  # dostep po nazwach kolumn
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys=ON")
    return conn


def init_db():
    """Tworzy wszystkie tabele jesli nie istnieja. Bezpieczne do wielokrotnego wywolania."""
    conn = get_connection()
    cursor = conn.cursor()

    # --- Wersjonowanie schematu ---
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS schema_version (
            version INTEGER NOT NULL
        )
    """)
    row = cursor.execute("SELECT version FROM schema_version").fetchone()
    if row is None:
        cursor.execute("INSERT INTO schema_version (version) VALUES (?)", (SCHEMA_VERSION,))

    # --- 1. ARTYSCI ---
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS artists (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            canonical_name  TEXT NOT NULL UNIQUE,
            nationality     TEXT,
            birth_year      INTEGER,
            death_year      INTEGER,
            category        TEXT,
            notes           TEXT,
            created_at      TEXT DEFAULT (datetime('now'))
        )
    """)

    # --- 2. WARIANTY NAZWISK ---
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS artist_name_variants (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            artist_id       INTEGER NOT NULL REFERENCES artists(id),
            variant_name    TEXT NOT NULL,
            is_primary      INTEGER DEFAULT 0,
            UNIQUE(artist_id, variant_name)
        )
    """)

    # --- 3. FRAZY WYSZUKIWANIA ---
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS search_terms (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            term            TEXT NOT NULL UNIQUE,
            category        TEXT NOT NULL,
            notes           TEXT
        )
    """)

    # --- 4. ZNALEZISKA AUKCYJNE ---
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS auction_items (
            id                  INTEGER PRIMARY KEY AUTOINCREMENT,
            site_item_id        TEXT NOT NULL,
            source_site         TEXT NOT NULL DEFAULT 'leiloesbr',
            auction_id          TEXT,
            title               TEXT NOT NULL,
            description         TEXT,
            price_text          TEXT,
            price_brl           REAL,
            currency            TEXT DEFAULT 'BRL',
            image_url           TEXT,
            image_local         TEXT,
            auction_date        TEXT,
            auction_time        TEXT,
            auction_state       TEXT,
            auction_house       TEXT,
            auction_house_url   TEXT,
            catalog_url         TEXT,
            matched_term        TEXT,
            matched_artist_id   INTEGER REFERENCES artists(id),
            match_confidence    TEXT DEFAULT 'high',
            is_false_positive   INTEGER DEFAULT 0,
            first_seen_at       TEXT DEFAULT (datetime('now')),
            last_seen_at        TEXT DEFAULT (datetime('now')),
            status              TEXT DEFAULT 'active',
            notes               TEXT,
            UNIQUE(source_site, site_item_id)
        )
    """)

    # --- 5. KOLEKCJA WLASNA (standard muzealny) ---
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS collection_objects (
            id                      INTEGER PRIMARY KEY AUTOINCREMENT,
            inventory_number        TEXT UNIQUE,
            title                   TEXT NOT NULL,
            artist_id               INTEGER REFERENCES artists(id),
            artist_name_display     TEXT,
            date_created            TEXT,
            category                TEXT NOT NULL,
            medium                  TEXT,
            support                 TEXT,
            height_cm               REAL,
            width_cm                REAL,
            depth_cm                REAL,
            weight_kg               REAL,
            dimensions_notes        TEXT,
            description             TEXT,
            inscription             TEXT,
            provenance              TEXT,
            acquisition_date        TEXT,
            acquisition_source      TEXT,
            acquisition_price       REAL,
            acquisition_currency    TEXT DEFAULT 'BRL',
            condition_grade         TEXT,
            condition_notes         TEXT,
            current_estimated_value REAL,
            valuation_currency      TEXT DEFAULT 'BRL',
            valuation_date          TEXT,
            authentication_status   TEXT DEFAULT 'unverified',
            authenticity_notes      TEXT,
            current_location        TEXT,
            exhibition_history      TEXT,
            literature_references   TEXT,
            created_at              TEXT DEFAULT (datetime('now')),
            updated_at              TEXT DEFAULT (datetime('now')),
            notes                   TEXT
        )
    """)

    # --- 6. ZDJECIA OBIEKTOW ---
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS object_photos (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            object_id   INTEGER NOT NULL REFERENCES collection_objects(id) ON DELETE CASCADE,
            file_path   TEXT NOT NULL,
            caption     TEXT,
            is_primary  INTEGER DEFAULT 0,
            taken_date  TEXT,
            added_at    TEXT DEFAULT (datetime('now'))
        )
    """)

    # --- 7. HISTORIA WYCEN ---
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS valuations (
            id                          INTEGER PRIMARY KEY AUTOINCREMENT,
            object_id                   INTEGER NOT NULL REFERENCES collection_objects(id) ON DELETE CASCADE,
            valuation_date              TEXT NOT NULL,
            estimated_value             REAL NOT NULL,
            currency                    TEXT DEFAULT 'BRL',
            appraiser                   TEXT,
            method                      TEXT,
            comparable_auction_item_id  INTEGER REFERENCES auction_items(id),
            notes                       TEXT,
            created_at                  TEXT DEFAULT (datetime('now'))
        )
    """)

    # --- 8. LOG URUCHOMIEN SCRAPERA ---
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS scraper_runs (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            started_at      TEXT NOT NULL,
            finished_at     TEXT,
            status          TEXT DEFAULT 'running',
            terms_searched  INTEGER DEFAULT 0,
            pages_scraped   INTEGER DEFAULT 0,
            items_found     INTEGER DEFAULT 0,
            new_items       INTEGER DEFAULT 0,
            errors          INTEGER DEFAULT 0,
            error_log       TEXT,
            notes           TEXT
        )
    """)

    # --- INDEKSY ---
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_auction_matched_artist ON auction_items(matched_artist_id)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_auction_matched_term ON auction_items(matched_term)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_auction_first_seen ON auction_items(first_seen_at)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_auction_status ON auction_items(status)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_auction_price ON auction_items(price_brl)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_collection_category ON collection_objects(category)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_collection_artist ON collection_objects(artist_id)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_valuations_object ON valuations(object_id)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_photos_object ON object_photos(object_id)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_variants_name ON artist_name_variants(variant_name)")

    # --- MIGRACJA: Wielojezyczne tytuly i opisy ---
    existing_cols = {row[1] for row in cursor.execute("PRAGMA table_info(collection_objects)").fetchall()}
    for col in ["title_pl", "title_en", "description_pl", "description_en"]:
        if col not in existing_cols:
            cursor.execute(f"ALTER TABLE collection_objects ADD COLUMN {col} TEXT")
            print(f"  [MIGRATION] Dodano kolumne: {col}")

    conn.commit()
    conn.close()
    print(f"Baza danych zainicjalizowana: {DATABASE_PATH}")


# ============================================================
# FUNKCJE POMOCNICZE — ARTYSCI
# ============================================================

def seed_artists(artist_list):
    """Wstawia artystow i ich warianty nazwisk do bazy. Pomija istniejacych."""
    conn = get_connection()
    cursor = conn.cursor()

    for artist in artist_list:
        # Wstaw artystę
        cursor.execute("""
            INSERT OR IGNORE INTO artists (canonical_name, nationality, birth_year, death_year, category)
            VALUES (?, ?, ?, ?, ?)
        """, (
            artist["canonical_name"],
            artist.get("nationality"),
            artist.get("birth_year"),
            artist.get("death_year"),
            artist.get("category"),
        ))

        # Pobierz ID artysty
        row = cursor.execute("SELECT id FROM artists WHERE canonical_name = ?",
                             (artist["canonical_name"],)).fetchone()
        artist_id = row["id"]

        # Wstaw warianty
        for i, variant in enumerate(artist.get("variants", [])):
            cursor.execute("""
                INSERT OR IGNORE INTO artist_name_variants (artist_id, variant_name, is_primary)
                VALUES (?, ?, ?)
            """, (artist_id, variant, 1 if i == 0 else 0))

    conn.commit()
    conn.close()
    print(f"Zaladowano {len(artist_list)} artystow do bazy.")


def seed_search_terms(terms_list):
    """Wstawia frazy wyszukiwania (meble, etc.) do bazy."""
    conn = get_connection()
    cursor = conn.cursor()
    for ft in terms_list:
        cursor.execute("""
            INSERT OR IGNORE INTO search_terms (term, category, notes)
            VALUES (?, ?, ?)
        """, (ft["term"], ft["category"], ft.get("notes", "")))
    conn.commit()
    conn.close()
    print(f"Zaladowano {len(terms_list)} fraz wyszukiwania.")


def get_artist_id_by_name(conn, name):
    """Szuka artysty po wariancie nazwiska. Zwraca ID lub None."""
    row = conn.execute("""
        SELECT a.id FROM artists a
        JOIN artist_name_variants v ON a.id = v.artist_id
        WHERE LOWER(v.variant_name) = LOWER(?)
    """, (name,)).fetchone()
    return row["id"] if row else None


# ============================================================
# FUNKCJE POMOCNICZE — AUCTION ITEMS
# ============================================================

def is_duplicate_auction_item(conn, source_site, site_item_id):
    """Sprawdza czy lot juz istnieje w bazie."""
    row = conn.execute(
        "SELECT id FROM auction_items WHERE source_site = ? AND site_item_id = ?",
        (source_site, site_item_id)
    ).fetchone()
    return row["id"] if row else None


def upsert_auction_item(conn, data):
    """
    Wstawia nowy lot lub aktualizuje last_seen_at jesli juz istnieje.
    data: dict z kluczami odpowiadajacymi kolumnom auction_items.
    Zwraca: (item_id, is_new)
    """
    existing_id = is_duplicate_auction_item(conn, data.get("source_site", "leiloesbr"), data["site_item_id"])

    if existing_id:
        conn.execute(
            "UPDATE auction_items SET last_seen_at = datetime('now') WHERE id = ?",
            (existing_id,)
        )
        return existing_id, False

    cursor = conn.execute("""
        INSERT INTO auction_items (
            site_item_id, source_site, auction_id, title, description,
            price_text, price_brl, currency, image_url, image_local,
            auction_date, auction_time, auction_state, auction_house, auction_house_url,
            catalog_url, matched_term, matched_artist_id, match_confidence
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        data["site_item_id"],
        data.get("source_site", "leiloesbr"),
        data.get("auction_id"),
        data["title"],
        data.get("description"),
        data.get("price_text"),
        data.get("price_brl"),
        data.get("currency", "BRL"),
        data.get("image_url"),
        data.get("image_local"),
        data.get("auction_date"),
        data.get("auction_time"),
        data.get("auction_state"),
        data.get("auction_house"),
        data.get("auction_house_url"),
        data.get("catalog_url"),
        data.get("matched_term"),
        data.get("matched_artist_id"),
        data.get("match_confidence", "high"),
    ))
    return cursor.lastrowid, True


# ============================================================
# FUNKCJE POMOCNICZE — COLLECTION OBJECTS
# ============================================================

def add_collection_object(conn, data):
    """Dodaje nowy obiekt do kolekcji. Zwraca ID."""
    cursor = conn.execute("""
        INSERT INTO collection_objects (
            inventory_number, title, artist_id, artist_name_display, date_created,
            category, medium, support,
            height_cm, width_cm, depth_cm, weight_kg, dimensions_notes,
            description, inscription,
            provenance, acquisition_date, acquisition_source, acquisition_price, acquisition_currency,
            condition_grade, condition_notes,
            current_estimated_value, valuation_currency, valuation_date,
            authentication_status, authenticity_notes,
            current_location, exhibition_history, literature_references, notes
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        data.get("inventory_number"),
        data["title"],
        data.get("artist_id"),
        data.get("artist_name_display"),
        data.get("date_created"),
        data["category"],
        data.get("medium"),
        data.get("support"),
        data.get("height_cm"),
        data.get("width_cm"),
        data.get("depth_cm"),
        data.get("weight_kg"),
        data.get("dimensions_notes"),
        data.get("description"),
        data.get("inscription"),
        data.get("provenance"),
        data.get("acquisition_date"),
        data.get("acquisition_source"),
        data.get("acquisition_price"),
        data.get("acquisition_currency", "BRL"),
        data.get("condition_grade"),
        data.get("condition_notes"),
        data.get("current_estimated_value"),
        data.get("valuation_currency", "BRL"),
        data.get("valuation_date"),
        data.get("authentication_status", "unverified"),
        data.get("authenticity_notes"),
        data.get("current_location"),
        data.get("exhibition_history"),
        data.get("literature_references"),
        data.get("notes"),
    ))
    return cursor.lastrowid


def collection_object_exists(conn, inventory_number):
    """Sprawdza czy obiekt o danym inventory_number już istnieje."""
    row = conn.execute(
        "SELECT id FROM collection_objects WHERE inventory_number = ?",
        (inventory_number,)
    ).fetchone()
    return row is not None


def delete_all_collection_objects(conn):
    """Usuwa WSZYSTKIE obiekty z kolekcji. Zwraca liczbę usuniętych."""
    cursor = conn.execute("DELETE FROM collection_objects")
    conn.execute("DELETE FROM object_photos")
    return cursor.rowcount


def get_collection_objects(conn, category=None, artist_id=None, search=None,
                           sort_by="title", limit=50, offset=0, has_photo=None):
    """Pobiera obiekty z kolekcji z filtrami."""
    query = "SELECT co.* FROM collection_objects co"
    params = []

    # JOIN for photo filter
    if has_photo is not None:
        query += " LEFT JOIN (SELECT object_id, COUNT(*) as pc FROM object_photos GROUP BY object_id) ph ON ph.object_id = co.id"

    query += " WHERE 1=1"

    if category:
        query += " AND co.category = ?"
        params.append(category)
    if artist_id:
        query += " AND co.artist_id = ?"
        params.append(artist_id)
    if search:
        query += (" AND (co.title LIKE ? OR co.description LIKE ?"
                   " OR co.artist_name_display LIKE ?"
                   " OR co.inventory_number LIKE ? OR co.notes LIKE ?)")
        like = f"%{search}%"
        params.extend([like, like, like, like, like])
    if has_photo == "yes":
        query += " AND ph.pc > 0"
    elif has_photo == "no":
        query += " AND ph.pc IS NULL"

    allowed_sorts = {
        "title": "co.title",
        "artist": "co.artist_name_display",
        "date": "co.acquisition_date DESC",
        "price_desc": "co.acquisition_price DESC",
        "price_asc": "co.acquisition_price ASC",
        "category": "co.category",
        "newest": "co.created_at DESC",
    }
    order = allowed_sorts.get(sort_by, "co.title")
    query += f" ORDER BY {order} LIMIT ? OFFSET ?"
    params.extend([limit, offset])

    return conn.execute(query, params).fetchall()


def get_auction_items(conn, artist_id=None, term=None, confidence=None,
                      false_positive=False, sort_by="newest", limit=50, offset=0):
    """Pobiera znaleziska aukcyjne z filtrami."""
    query = "SELECT * FROM auction_items WHERE is_false_positive = ?"
    params = [1 if false_positive else 0]

    if artist_id:
        query += " AND matched_artist_id = ?"
        params.append(artist_id)
    if term:
        query += " AND matched_term LIKE ?"
        params.append(f"%{term}%")
    if confidence:
        query += " AND match_confidence = ?"
        params.append(confidence)

    sort_map = {"newest": "first_seen_at DESC", "price_high": "price_brl DESC",
                "price_low": "price_brl ASC", "title": "title"}
    order = sort_map.get(sort_by, "first_seen_at DESC")
    query += f" ORDER BY {order} LIMIT ? OFFSET ?"
    params.extend([limit, offset])

    return conn.execute(query, params).fetchall()


def add_valuation(conn, object_id, data):
    """Dodaje wpis wyceny do historii."""
    cursor = conn.execute("""
        INSERT INTO valuations (object_id, valuation_date, estimated_value, currency,
                                appraiser, method, comparable_auction_item_id, notes)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        object_id,
        data["valuation_date"],
        data["estimated_value"],
        data.get("currency", "BRL"),
        data.get("appraiser"),
        data.get("method"),
        data.get("comparable_auction_item_id"),
        data.get("notes"),
    ))
    # Aktualizuj biezaca wycene w obiekcie
    conn.execute("""
        UPDATE collection_objects
        SET current_estimated_value = ?, valuation_currency = ?, valuation_date = ?, updated_at = datetime('now')
        WHERE id = ?
    """, (data["estimated_value"], data.get("currency", "BRL"), data["valuation_date"], object_id))
    return cursor.lastrowid


def update_collection_object(conn, object_id, data):
    """Aktualizuje obiekt w kolekcji. data = dict z polami do zmiany."""
    allowed_fields = {
        "inventory_number", "title", "artist_id", "artist_name_display", "date_created",
        "category", "medium", "support",
        "height_cm", "width_cm", "depth_cm", "weight_kg", "dimensions_notes",
        "description", "inscription",
        "provenance", "acquisition_date", "acquisition_source", "acquisition_price", "acquisition_currency",
        "condition_grade", "condition_notes",
        "current_estimated_value", "valuation_currency", "valuation_date",
        "authentication_status", "authenticity_notes",
        "current_location", "exhibition_history", "literature_references", "notes",
    }
    sets = []
    params = []
    for key, val in data.items():
        if key in allowed_fields:
            sets.append(f"{key} = ?")
            params.append(val)
    if not sets:
        return False
    sets.append("updated_at = datetime('now')")
    params.append(object_id)
    conn.execute(f"UPDATE collection_objects SET {', '.join(sets)} WHERE id = ?", params)
    return True


def delete_collection_object(conn, object_id):
    """Usuwa obiekt z kolekcji (CASCADE usunie zdjecia i wyceny)."""
    conn.execute("DELETE FROM collection_objects WHERE id = ?", (object_id,))


def get_collection_object_by_id(conn, object_id):
    """Pobiera pojedynczy obiekt z kolekcji po ID."""
    return conn.execute("SELECT * FROM collection_objects WHERE id = ?", (object_id,)).fetchone()


# ============================================================
# FUNKCJE POMOCNICZE — PHOTOS
# ============================================================

def add_object_photo(conn, object_id, file_path, caption=None, is_primary=0):
    """Dodaje zdjecie do obiektu. Zwraca photo ID."""
    # Jesli is_primary=1, zdejmij primary z innych
    if is_primary:
        conn.execute("UPDATE object_photos SET is_primary = 0 WHERE object_id = ?", (object_id,))
    cursor = conn.execute("""
        INSERT INTO object_photos (object_id, file_path, caption, is_primary)
        VALUES (?, ?, ?, ?)
    """, (object_id, file_path, caption, is_primary))
    return cursor.lastrowid


def get_object_photos(conn, object_id):
    """Pobiera zdjecia obiektu (primary first)."""
    return conn.execute(
        "SELECT * FROM object_photos WHERE object_id = ? ORDER BY is_primary DESC, id ASC",
        (object_id,)
    ).fetchall()


def delete_object_photo(conn, photo_id):
    """Usuwa zdjecie. Zwraca file_path do skasowania pliku."""
    row = conn.execute("SELECT file_path FROM object_photos WHERE id = ?", (photo_id,)).fetchone()
    if row:
        conn.execute("DELETE FROM object_photos WHERE id = ?", (photo_id,))
        return row["file_path"]
    return None


def get_object_valuations(conn, object_id):
    """Pobiera historię wycen obiektu."""
    return conn.execute(
        "SELECT * FROM valuations WHERE object_id = ? ORDER BY valuation_date DESC",
        (object_id,)
    ).fetchall()


def get_collection_stats(conn):
    """Statystyki kolekcji: count, value, categories."""
    stats = {}
    stats["collection_count"] = conn.execute(
        "SELECT COUNT(*) as c FROM collection_objects"
    ).fetchone()["c"]
    row = conn.execute(
        "SELECT COALESCE(SUM(acquisition_price), 0) as v FROM collection_objects"
    ).fetchone()
    stats["collection_total_value"] = row["v"]
    rows = conn.execute(
        "SELECT category, COUNT(*) as c FROM collection_objects GROUP BY category ORDER BY c DESC"
    ).fetchall()
    stats["categories_breakdown"] = {r["category"]: r["c"] for r in rows}
    return stats


def start_scraper_run(conn):
    """Rejestruje rozpoczecie sesji scrapera. Zwraca run_id."""
    cursor = conn.execute(
        "INSERT INTO scraper_runs (started_at) VALUES (?)",
        (datetime.now().isoformat(),)
    )
    conn.commit()
    return cursor.lastrowid


def finish_scraper_run(conn, run_id, stats):
    """Aktualizuje rekord po zakonczeniu scrapowania."""
    conn.execute("""
        UPDATE scraper_runs
        SET finished_at = ?, status = ?, terms_searched = ?, pages_scraped = ?,
            items_found = ?, new_items = ?, errors = ?, error_log = ?
        WHERE id = ?
    """, (
        datetime.now().isoformat(),
        stats.get("status", "completed"),
        stats.get("terms_searched", 0),
        stats.get("pages_scraped", 0),
        stats.get("items_found", 0),
        stats.get("new_items", 0),
        stats.get("errors", 0),
        stats.get("error_log"),
        run_id,
    ))
    conn.commit()


def get_stats(conn):
    """Zwraca statystyki systemu."""
    stats = {}
    stats["total_collection"] = conn.execute("SELECT COUNT(*) as c FROM collection_objects").fetchone()["c"]
    stats["total_auction_items"] = conn.execute("SELECT COUNT(*) as c FROM auction_items WHERE is_false_positive=0").fetchone()["c"]
    stats["total_artists"] = conn.execute("SELECT COUNT(*) as c FROM artists").fetchone()["c"]
    stats["new_today"] = conn.execute(
        "SELECT COUNT(*) as c FROM auction_items WHERE DATE(first_seen_at) = DATE('now') AND is_false_positive=0"
    ).fetchone()["c"]

    # Obiekt po kategoriach
    rows = conn.execute(
        "SELECT category, COUNT(*) as c FROM collection_objects GROUP BY category ORDER BY c DESC"
    ).fetchall()
    stats["collection_by_category"] = {r["category"]: r["c"] for r in rows}

    # Top artysci w aukcjach
    rows = conn.execute("""
        SELECT a.canonical_name, COUNT(*) as c
        FROM auction_items ai
        JOIN artists a ON ai.matched_artist_id = a.id
        WHERE ai.is_false_positive = 0
        GROUP BY a.id ORDER BY c DESC LIMIT 10
    """).fetchall()
    stats["top_auction_artists"] = {r["canonical_name"]: r["c"] for r in rows}

    return stats


# ============================================================
# MAIN — uruchom zeby zainicjalizowac baze
# ============================================================
if __name__ == "__main__":
    init_db()

    # Zaladuj artystow z search_terms.py
    from search_terms import get_polish_artists, FURNITURE_TERMS
    seed_artists(get_polish_artists())
    seed_search_terms(FURNITURE_TERMS)

    # Statystyki
    conn = get_connection()
    artists_count = conn.execute("SELECT COUNT(*) as c FROM artists").fetchone()["c"]
    variants_count = conn.execute("SELECT COUNT(*) as c FROM artist_name_variants").fetchone()["c"]
    terms_count = conn.execute("SELECT COUNT(*) as c FROM search_terms").fetchone()["c"]
    conn.close()

    print(f"\nPodsumowanie:")
    print(f"  Artysci:   {artists_count}")
    print(f"  Warianty:  {variants_count}")
    print(f"  Frazy:     {terms_count}")
    print(f"\nBaza gotowa!")
