#!/usr/bin/env python3
"""
translate_collection.py - Tłumaczy tytuły i opisy obiektów kolekcji.

Tłumaczy z portugalskiego (oryginał) na polski i angielski.
Używa Google Translate (free) przez deep_translator.

Użycie:
    python translate_collection.py              # przetłumacz wszystkie brakujące
    python translate_collection.py --dry-run    # pokaż co będzie tłumaczone
    python translate_collection.py --limit 5    # pierwsze 5 obiektów
    python translate_collection.py --object-id 42  # konkretny obiekt
    python translate_collection.py --force      # nadpisz istniejące tłumaczenia
    python translate_collection.py --lang pl    # tylko polski
    python translate_collection.py --lang en    # tylko angielski
"""

import os
import sys
import time
import argparse

# Fix Windows console encoding
import io
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import database

try:
    from deep_translator import GoogleTranslator
except ImportError:
    print("[ERROR] Brak biblioteki deep_translator!")
    print("        Zainstaluj: pip install deep-translator")
    sys.exit(1)

# ============================================================
# CONSTANTS
# ============================================================
TRANSLATE_DELAY = 0.2   # sekund między requestami
MAX_TEXT_LENGTH = 4900   # Google Translate limit ~5000 znaków
BATCH_COMMIT = 10        # commit co N obiektów


# ============================================================
# HELPERS
# ============================================================

def translate_text(text, source='pt', target='pl'):
    """Tłumaczy tekst. Zwraca przetłumaczony tekst lub None przy błędzie."""
    if not text or not text.strip():
        return None

    # Truncate if too long
    if len(text) > MAX_TEXT_LENGTH:
        text = text[:MAX_TEXT_LENGTH]

    try:
        result = GoogleTranslator(source=source, target=target).translate(text)
        return result
    except Exception as e:
        print(f"      [TRANSLATE ERROR] {e}")
        return None


def needs_translation(obj, lang):
    """Sprawdza czy obiekt potrzebuje tłumaczenia dla danego języka."""
    title_col = f"title_{lang}"
    desc_col = f"description_{lang}"

    title_val = obj[title_col] if title_col in obj.keys() else None
    desc_val = obj[desc_col] if desc_col in obj.keys() else None

    # Potrzebuje tłumaczenia jeśli:
    # - tytuł nie jest przetłumaczony (a oryginał istnieje)
    # - LUB opis nie jest przetłumaczony (a oryginał istnieje)
    if obj['title'] and not title_val:
        return True
    if obj['description'] and not desc_val:
        return True
    return False


# ============================================================
# MAIN
# ============================================================

def translate_collection(dry_run=False, limit=None, object_id=None, force=False, lang=None):
    """Tłumaczy tytuły i opisy obiektów kolekcji."""

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

    # Języki do tłumaczenia
    languages = []
    if lang:
        languages = [lang]
    else:
        languages = ['pl', 'en']

    lang_names = {'pl': 'polski', 'en': 'angielski'}
    total = len(objects)
    mode = "[DRY RUN] " if dry_run else ""
    langs_str = ", ".join(lang_names.get(l, l) for l in languages)
    print(f"{mode}Tłumaczenie na: {langs_str}")
    print(f"Obiektów do sprawdzenia: {total}\n")

    # Stats
    translated_titles = {'pl': 0, 'en': 0}
    translated_descs = {'pl': 0, 'en': 0}
    skipped = 0
    errors = 0

    for i, obj in enumerate(objects, 1):
        obj_id = obj['id']
        inv_nr = obj['inventory_number'] or '?'
        title_short = (obj['title'] or '?')[:50]

        # Check if any translation needed
        any_needed = False
        for target_lang in languages:
            if force or needs_translation(obj, target_lang):
                any_needed = True
                break

        if not any_needed:
            skipped += 1
            continue

        print(f"[{i:3d}/{total}] {inv_nr}: {title_short}")

        for target_lang in languages:
            if not force and not needs_translation(obj, target_lang):
                continue

            title_col = f"title_{target_lang}"
            desc_col = f"description_{target_lang}"

            # Translate title
            new_title = None
            if obj['title'] and (force or not (obj[title_col] if title_col in obj.keys() else None)):
                if dry_run:
                    print(f"   [{target_lang}] tytuł: → (would translate)")
                    translated_titles[target_lang] += 1
                else:
                    new_title = translate_text(obj['title'], source='pt', target=target_lang)
                    if new_title:
                        translated_titles[target_lang] += 1
                        print(f"   [{target_lang}] tytuł: {new_title[:60]}")
                    else:
                        errors += 1
                    time.sleep(TRANSLATE_DELAY)

            # Translate description
            new_desc = None
            if obj['description'] and (force or not (obj[desc_col] if desc_col in obj.keys() else None)):
                if dry_run:
                    print(f"   [{target_lang}] opis: → (would translate, {len(obj['description'])} chars)")
                    translated_descs[target_lang] += 1
                else:
                    new_desc = translate_text(obj['description'], source='pt', target=target_lang)
                    if new_desc:
                        translated_descs[target_lang] += 1
                        print(f"   [{target_lang}] opis: {new_desc[:60]}...")
                    else:
                        errors += 1
                    time.sleep(TRANSLATE_DELAY)

            # Update DB
            if not dry_run and (new_title or new_desc):
                updates = []
                params = []
                if new_title:
                    updates.append(f"{title_col} = ?")
                    params.append(new_title)
                if new_desc:
                    updates.append(f"{desc_col} = ?")
                    params.append(new_desc)
                updates.append("updated_at = datetime('now')")
                params.append(obj_id)

                sql = f"UPDATE collection_objects SET {', '.join(updates)} WHERE id = ?"
                conn.execute(sql, params)

                # Commit periodically
                if i % BATCH_COMMIT == 0:
                    conn.commit()

    # Final commit
    if not dry_run:
        conn.commit()
    conn.close()

    # Summary
    print(f"\n{'='*50}")
    print(f"PODSUMOWANIE {mode}")
    print(f"{'='*50}")
    for target_lang in languages:
        ln = lang_names.get(target_lang, target_lang)
        print(f"  [{target_lang}] Tytuły przetłumaczone:  {translated_titles[target_lang]}")
        print(f"  [{target_lang}] Opisy przetłumaczone:   {translated_descs[target_lang]}")
    print(f"  Pominięte (już mają):    {skipped}")
    if errors:
        print(f"  Błędy:                   {errors}")
    print(f"\n[DONE]")


# ============================================================
# CLI
# ============================================================
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Translate collection titles and descriptions")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would be translated without translating")
    parser.add_argument("--limit", type=int, default=None,
                        help="Process only N objects")
    parser.add_argument("--object-id", type=int, default=None,
                        help="Process a single object by ID")
    parser.add_argument("--force", action="store_true",
                        help="Re-translate even if translations exist")
    parser.add_argument("--lang", choices=['pl', 'en'], default=None,
                        help="Translate only to this language (default: both)")
    args = parser.parse_args()

    translate_collection(
        dry_run=args.dry_run,
        limit=args.limit,
        object_id=args.object_id,
        force=args.force,
        lang=args.lang,
    )
