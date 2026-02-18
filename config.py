"""
Konfiguracja systemu kolekcjonerskiego.
Wszystkie stale i sciezki w jednym miejscu.
"""
import os

# === SCIEZKI ===
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
IMAGES_DIR = os.path.join(BASE_DIR, "images")
AUCTION_IMAGES_DIR = os.path.join(IMAGES_DIR, "auction")
COLLECTION_IMAGES_DIR = os.path.join(IMAGES_DIR, "collection")
REPORTS_DIR = os.path.join(BASE_DIR, "reports")
DAILY_REPORTS_DIR = os.path.join(REPORTS_DIR, "daily")
EXPORTS_DIR = os.path.join(REPORTS_DIR, "exports")
WEB_DIR = os.path.join(BASE_DIR, "web")

# === BAZA DANYCH ===
DATABASE_PATH = os.path.join(DATA_DIR, "artcollection.db")

# === SCRAPER ===
SCRAPER_STATE_PATH = os.path.join(DATA_DIR, "scraper_state.json")
SCRAPER_LOG_PATH = os.path.join(DATA_DIR, "scraper_log.txt")

# LeiloesBR
LEILOESBR_BASE_URL = "https://www.leiloesbr.com.br/busca_andamento.asp"
LEILOESBR_SEARCH_URL = LEILOESBR_BASE_URL + "?pesquisa={term}&op=1&v=126&tp=|&b=0&pag={page}"
LEILOESBR_FULL_SCAN_URL = LEILOESBR_BASE_URL + "?pesquisa=&op=1&v=126&tp=|&b=0&pag={page}"

# Ustawienia requestow
REQUEST_DELAY = 0.8          # sekundy miedzy zapytaniami
REQUEST_TIMEOUT = 15         # timeout na zapytanie
MAX_RETRIES = 3              # ile razy ponowic po bledzie
RETRY_DELAY = 5              # sekundy czekania po bledzie
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"

# Pobieranie obrazkow
DOWNLOAD_IMAGES = True       # czy pobierac miniaturki z aukcji

# === SERWER ===
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 8080

# === TWORZENIE KATALOGOW ===
for d in [DATA_DIR, AUCTION_IMAGES_DIR, COLLECTION_IMAGES_DIR, DAILY_REPORTS_DIR, EXPORTS_DIR]:
    os.makedirs(d, exist_ok=True)
