#!/usr/bin/env python3
r"""
scrape_photos.py - Pobiera zdjecia z CDN aukcji do kolekcji.

Kazdy obiekt w bazie ma URL aukcji w polu notes, np.:
  URL: http://www.acervoraroleiloes.com.br/peca.asp?ID=27842724

Zdjecia sa na CDN CloudFront:
  https://d1o6h00a1h5k7q.cloudfront.net/imagens/img_g/{auction_nr}/{peca_id}.jpg

Skrypt buduje URL bezposrednio z danych w bazie (bez parsowania HTML).
Obsluguje tez mandrillapp redirect URLs (base64 decode).
Opcja --extra probuje pobrac dodatkowe zdjecia (_2, _3...).

Uzycie:
    python scrape_photos.py              # pobierz wszystkie
    python scrape_photos.py --dry-run    # tylko pokaz co by pobral
    python scrape_photos.py --limit 5    # pierwsze 5 obiektow
    python scrape_photos.py --object-id 42  # konkretny obiekt
    python scrape_photos.py --force      # nadpisz istniejace
    python scrape_photos.py --extra      # probuj dodatkowe zdjecia
"""

import os
import re
import sys
import time
import json
import base64
import argparse
import requests
from urllib.parse import urlparse, parse_qs

# Fix Windows console encoding
import io
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

# Add script directory to PATH
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import database
from config import (
    COLLECTION_IMAGES_DIR,
    USER_AGENT,
    REQUEST_TIMEOUT,
    MAX_RETRIES,
    RETRY_DELAY,
)

# ============================================================
# CONSTANTS
# ============================================================
CDN_BASE = "https://d1o6h00a1h5k7q.cloudfront.net/imagens/img_g"
DOWNLOAD_DELAY = 0.3  # seconds between downloads (polite)
MAX_EXTRA_PHOTOS = 10  # max additional photos per object


# ============================================================
# HELPERS
# ============================================================

def extract_peca_id(notes):
    """Wyciaga peca_id z pola notes.

    Szuka: URL: http://...peca.asp?ID=27842724
    Zwraca: '27842724' lub None
    """
    if not notes:
        return None
    m = re.search(r'URL:\s*https?://[^\s]*peca\.asp\?ID=(\d+)', notes)
    if m:
        return m.group(1)
    return None


def decode_mandrillapp_url(notes):
    """Dekoduje mandrillapp redirect URL i wyciaga peca_id.

    Mandrillapp URL: https://mandrillapp.com/track/click/30759385/domain?p={base64}
    Base64 dekoduje sie do JSON: {"p": "{\"url\": \"http://...peca.asp?ID=XXXXX\"}"}

    Zwraca: peca_id (str) lub None
    """
    if not notes:
        return None
    # Wyciagnij URL mandrillapp z notes
    m = re.search(r'URL:\s*(https?://mandrillapp\.com/[^\s]+)', notes)
    if not m:
        return None

    mandrill_url = m.group(1)
    try:
        parsed = urlparse(mandrill_url)
        qs = parse_qs(parsed.query)
        p_value = qs.get('p', [None])[0]
        if not p_value:
            return None

        # Fix base64 padding
        padding = 4 - len(p_value) % 4
        if padding != 4:
            p_value += '=' * padding

        decoded = base64.urlsafe_b64decode(p_value)
        outer = json.loads(decoded)
        inner = json.loads(outer.get('p', '{}'))
        actual_url = inner.get('url', '')

        # Wyciagnij peca_id z actual_url
        m2 = re.search(r'peca\.asp\?ID=(\d+)', actual_url)
        if m2:
            return m2.group(1)
    except Exception as e:
        print(f"      [WARN] mandrillapp decode error: {e}")

    return None


def extract_auction_nr(inventory_number):
    """Wyciaga auction_nr z inventory_number.

    LBR-55909-102 -> '55909'
    """
    if not inventory_number:
        return None
    m = re.match(r'LBR-(\d+)-', inventory_number)
    if m:
        return m.group(1)
    return None


def build_cdn_url(auction_nr, peca_id, suffix=""):
    """Buduje URL do zdjecia na CDN.

    suffix="" -> .../27842724.jpg  (glowne)
    suffix="_2" -> .../27842724_2.jpg  (dodatkowe)
    """
    return f"{CDN_BASE}/{auction_nr}/{peca_id}{suffix}.jpg"


def download_image(url, save_path, session):
    """Pobiera zdjecie z URL i zapisuje do pliku.

    Zwraca (True, filesize) lub (False, 0).
    Obsluguje retry i HTTP errors.
    """
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            resp = session.get(url, timeout=REQUEST_TIMEOUT, stream=True)

            if resp.status_code == 404:
                return False, 0

            if resp.status_code == 200:
                content_type = resp.headers.get('Content-Type', '')
                if 'image' not in content_type and 'octet' not in content_type:
                    return False, 0

                with open(save_path, 'wb') as f:
                    for chunk in resp.iter_content(chunk_size=8192):
                        f.write(chunk)

                filesize = os.path.getsize(save_path)
                if filesize < 1000:
                    # Too small - likely a placeholder/error image
                    os.remove(save_path)
                    return False, 0

                return True, filesize

            if resp.status_code == 429:
                wait = RETRY_DELAY * attempt
                print(f"      [429] Rate limited, waiting {wait}s...")
                time.sleep(wait)
                continue

            # Other HTTP error
            return False, 0

        except requests.exceptions.Timeout:
            if attempt < MAX_RETRIES:
                print(f"      [TIMEOUT] attempt {attempt}/{MAX_RETRIES}, retrying...")
                time.sleep(RETRY_DELAY)
            else:
                return False, 0

        except requests.exceptions.RequestException as e:
            if attempt < MAX_RETRIES:
                print(f"      [ERROR] {e}, retrying...")
                time.sleep(RETRY_DELAY)
            else:
                return False, 0

    return False, 0


def has_mandrillapp_url(notes):
    """Sprawdza czy URL to mandrillapp tracking redirect."""
    if not notes:
        return False
    return 'mandrillapp.com' in notes


# ============================================================
# MAIN
# ============================================================

def scrape_photos(dry_run=False, limit=None, object_id=None, force=False, extra=False):
    """Pobiera zdjecia z CDN dla obiektow w kolekcji."""

    database.init_db()
    conn = database.get_connection()

    # Pobierz obiekty
    if object_id:
        row = conn.execute(
            "SELECT * FROM collection_objects WHERE id = ?", (object_id,)
        ).fetchone()
        if not row:
            print(f"[ERROR] Obiekt o ID {object_id} nie istnieje!")
            return
        objects = [row]
    else:
        objects = conn.execute(
            "SELECT * FROM collection_objects ORDER BY id"
        ).fetchall()

    if limit:
        objects = objects[:limit]

    total = len(objects)
    mode = "[DRY RUN] " if dry_run else ""
    extra_label = " +EXTRA" if extra else ""
    print(f"{mode}Scrape photos{extra_label} for {total} objects\n")

    # Session
    session = requests.Session()
    session.headers.update({"User-Agent": USER_AGENT})

    # Stats
    downloaded = 0
    downloaded_extra = 0
    skipped_has_photos = 0
    skipped_no_url = 0
    skipped_no_auction_nr = 0
    mandrillapp_decoded = 0
    failed_404 = 0
    total_bytes = 0

    for i, obj in enumerate(objects, 1):
        obj_id = obj['id']
        inv_nr = obj['inventory_number'] or '?'
        title_short = (obj['title'] or '?')[:50]
        notes = obj['notes'] or ''

        # Progress
        print(f"[{i:3d}/{total}] {inv_nr}: {title_short}")

        # Skip if already has photos (unless --force or --extra)
        if not force:
            existing = database.get_object_photos(conn, obj_id)
            if existing:
                if extra:
                    # W trybie extra: sprawdz czy sa juz dodatkowe
                    existing_count = len(existing)
                    if existing_count > 1:
                        print(f"         -> skip (already has {existing_count} photos)")
                        skipped_has_photos += 1
                        continue
                    # Ma 1 zdjecie — sprobuj pobrac dodatkowe
                else:
                    print(f"         -> skip (already has {len(existing)} photo(s))")
                    skipped_has_photos += 1
                    continue

        # Try to get peca_id
        peca_id = None

        # 1. Try direct peca.asp URL
        peca_id = extract_peca_id(notes)

        # 2. If mandrillapp, decode
        if not peca_id and has_mandrillapp_url(notes):
            peca_id = decode_mandrillapp_url(notes)
            if peca_id:
                mandrillapp_decoded += 1
                print(f"         [mandrillapp decoded -> ID={peca_id}]")
            else:
                print(f"         -> skip (mandrillapp decode failed)")
                skipped_no_url += 1
                continue

        if not peca_id:
            print(f"         -> skip (no peca URL in notes)")
            skipped_no_url += 1
            continue

        # Extract auction_nr
        auction_nr = extract_auction_nr(inv_nr)
        if not auction_nr:
            print(f"         -> skip (can't parse auction_nr from {inv_nr})")
            skipped_no_auction_nr += 1
            continue

        # ---- Download main photo ----
        existing_photos = database.get_object_photos(conn, obj_id)
        has_main = len(existing_photos) > 0

        if not has_main:
            cdn_url = build_cdn_url(auction_nr, peca_id)
            filename = f"obj{obj_id}_1.jpg"
            save_path = os.path.join(COLLECTION_IMAGES_DIR, filename)

            if dry_run:
                print(f"         -> would download: {cdn_url}")
                downloaded += 1
            else:
                success, filesize = download_image(cdn_url, save_path, session)
                if success:
                    database.add_object_photo(conn, obj_id, save_path, caption=None, is_primary=1)
                    conn.commit()
                    downloaded += 1
                    total_bytes += filesize
                    size_kb = filesize / 1024
                    print(f"         -> OK ({size_kb:.0f} KB)")
                else:
                    failed_404 += 1
                    print(f"         -> FAIL (404 or error)")

            time.sleep(DOWNLOAD_DELAY)

        # ---- Download extra photos (if --extra) ----
        if extra:
            extra_count = 0
            for n in range(2, MAX_EXTRA_PHOTOS + 2):
                suffix = f"_{n}"
                cdn_url = build_cdn_url(auction_nr, peca_id, suffix)
                filename = f"obj{obj_id}_{n}.jpg"
                save_path = os.path.join(COLLECTION_IMAGES_DIR, filename)

                if dry_run:
                    # Check with HEAD request
                    try:
                        resp = session.head(cdn_url, timeout=REQUEST_TIMEOUT)
                        if resp.status_code == 200:
                            print(f"         -> extra #{n}: EXISTS {cdn_url}")
                            extra_count += 1
                        else:
                            break  # No more photos
                    except Exception:
                        break
                else:
                    success, filesize = download_image(cdn_url, save_path, session)
                    if success:
                        database.add_object_photo(conn, obj_id, save_path, caption=None, is_primary=0)
                        conn.commit()
                        extra_count += 1
                        downloaded_extra += 1
                        total_bytes += filesize
                        size_kb = filesize / 1024
                        print(f"         -> extra #{n}: OK ({size_kb:.0f} KB)")
                    else:
                        break  # No more photos for this object

                time.sleep(DOWNLOAD_DELAY)

            if extra_count > 0:
                print(f"         -> {extra_count} extra photo(s)")

    conn.close()

    # Summary
    print(f"\n{'='*50}")
    print(f"SUMMARY {mode}")
    print(f"{'='*50}")
    print(f"  Downloaded (main):   {downloaded}")
    if extra:
        print(f"  Downloaded (extra):  {downloaded_extra}")
    print(f"  Mandrillapp decoded: {mandrillapp_decoded}")
    print(f"  Skip (has photos):   {skipped_has_photos}")
    print(f"  Skip (no URL):       {skipped_no_url}")
    if skipped_no_auction_nr:
        print(f"  Skip (no auc.nr):    {skipped_no_auction_nr}")
    print(f"  Failed (404/err):    {failed_404}")
    if total_bytes > 0:
        mb = total_bytes / (1024 * 1024)
        print(f"  Total size:          {mb:.1f} MB")
    print(f"\n[DONE]")


# ============================================================
# CLI
# ============================================================
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download photos from auction CDN")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would be downloaded without downloading")
    parser.add_argument("--limit", type=int, default=None,
                        help="Process only N objects")
    parser.add_argument("--object-id", type=int, default=None,
                        help="Process a single object by ID")
    parser.add_argument("--force", action="store_true",
                        help="Re-download even if photos exist")
    parser.add_argument("--extra", action="store_true",
                        help="Try to download additional photos (_2, _3...)")
    args = parser.parse_args()

    scrape_photos(
        dry_run=args.dry_run,
        limit=args.limit,
        object_id=args.object_id,
        force=args.force,
        extra=args.extra,
    )
