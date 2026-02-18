#!/usr/bin/env python3
"""
export_static.py - Eksportuje katalog kolekcji jako statyczną stronę HTML.

Generuje kompletną stronę bez serwera — dane wbudowane w JSON, zdjęcia skopiowane.
Wynik gotowy do GitHub Pages, Netlify, lub dowolnego hostingu statycznego.

Użycie:
    python export_static.py                    # export do ./docs/
    python export_static.py --output ./build   # export do ./build/
    python export_static.py --no-images        # bez zdjęć (lżejszy)
    python export_static.py --thumb-quality 60 # jakość miniatur (1-95)
"""

import os
import sys
import json
import shutil
import argparse

# Fix Windows console encoding
import io
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import database
from config import COLLECTION_IMAGES_DIR


def export_static(output_dir="docs", include_images=True):
    """Eksportuje katalog jako statyczną stronę."""

    database.init_db()
    conn = database.get_connection()

    print(f"Eksport statycznej strony do: {output_dir}/\n")

    # --- 1. Przygotuj katalog wyjściowy ---
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir, exist_ok=True)

    # --- 2. Pobierz dane ---
    objects = conn.execute("SELECT * FROM collection_objects ORDER BY id").fetchall()
    objects_list = [dict(o) for o in objects]

    # Dodaj zdjęcia do każdego obiektu
    for obj in objects_list:
        photos = database.get_object_photos(conn, obj["id"])
        photo_list = []
        for p in photos:
            fname = os.path.basename(p["file_path"])
            photo_list.append({
                "filename": fname,
                "is_primary": p["is_primary"],
                "caption": p["caption"],
            })
        obj["photos"] = photo_list
        primary = [ph for ph in photo_list if ph["is_primary"]]
        obj["primary_photo"] = f"images/{primary[0]['filename']}" if primary else (f"images/{photo_list[0]['filename']}" if photo_list else None)

    # Stats
    stats = database.get_collection_stats(conn)
    stats_dict = dict(stats) if stats else {}

    conn.close()

    print(f"  Obiektów: {len(objects_list)}")
    total_photos = sum(len(o["photos"]) for o in objects_list)
    print(f"  Zdjęć: {total_photos}")

    # --- 3. Kopiuj zdjęcia ---
    if include_images:
        img_out = os.path.join(output_dir, "images")
        os.makedirs(img_out, exist_ok=True)
        copied = 0
        for obj in objects_list:
            for ph in obj["photos"]:
                src = os.path.join(COLLECTION_IMAGES_DIR, ph["filename"])
                if os.path.exists(src):
                    shutil.copy2(src, os.path.join(img_out, ph["filename"]))
                    copied += 1
        print(f"  Skopiowano zdjęć: {copied}")

    # --- 4. Buduj statyczny HTML ---
    categories_breakdown = {}
    for obj in objects_list:
        cat = obj.get("category", "Inne")
        categories_breakdown[cat] = categories_breakdown.get(cat, 0) + 1

    embedded_data = {
        "objects": objects_list,
        "stats": {
            "collection_count": len(objects_list),
            "collection_total_value": sum(o.get("acquisition_price") or 0 for o in objects_list),
            "categories_breakdown": categories_breakdown,
            "total_photos": total_photos,
        },
    }

    # Wczytaj oryginalny index.html i zmodyfikuj
    template_path = os.path.join(os.path.dirname(__file__), "web", "index.html")
    with open(template_path, "r", encoding="utf-8") as f:
        html_template = f.read()

    # Wstrzyknij dane JSON i zamień API na lokalne dane
    json_data = json.dumps(embedded_data, ensure_ascii=False, default=str)

    # Dodaj skrypt z osadzonymi danymi + nadpisz funkcję api()
    inject_script = f"""
<script>
// === STATIC EXPORT: Embedded data ===
const STATIC_DATA = {json_data};
const STATIC_MODE = true;
</script>
"""

    # Wstaw przed </head>
    html_output = html_template.replace("</head>", inject_script + "</head>")

    # Nadpisz funkcje API na lokalne
    api_override = """
// === STATIC MODE: Override API functions ===
if (typeof STATIC_MODE !== 'undefined' && STATIC_MODE) {
    // Override api() - no server needed
    async function api(endpoint, options) {
        // Stats
        if (endpoint === 'stats') {
            return STATIC_DATA.stats;
        }
        // Collection list
        if (endpoint.startsWith('collection') && !endpoint.includes('/')) {
            const url = new URL('http://x/' + endpoint);
            const params = url.searchParams;
            let items = [...STATIC_DATA.objects];

            // Filters
            const cat = params.get('category');
            if (cat) items = items.filter(i => i.category === cat);

            const search = params.get('search');
            if (search) {
                const s = search.toLowerCase();
                items = items.filter(i =>
                    (i.title || '').toLowerCase().includes(s) ||
                    (i.description || '').toLowerCase().includes(s) ||
                    (i.artist_name_display || '').toLowerCase().includes(s) ||
                    (i.inventory_number || '').toLowerCase().includes(s) ||
                    (i.notes || '').toLowerCase().includes(s) ||
                    (i.title_pl || '').toLowerCase().includes(s) ||
                    (i.title_en || '').toLowerCase().includes(s) ||
                    (i.description_pl || '').toLowerCase().includes(s) ||
                    (i.description_en || '').toLowerCase().includes(s)
                );
            }

            const hasPhoto = params.get('has_photo');
            if (hasPhoto === 'yes') items = items.filter(i => i.photos && i.photos.length > 0);
            if (hasPhoto === 'no') items = items.filter(i => !i.photos || i.photos.length === 0);

            // Sort
            const sort = params.get('sort') || 'title';
            const sortFns = {
                'title': (a,b) => (a.title||'').localeCompare(b.title||''),
                'artist': (a,b) => (a.artist_name_display||'').localeCompare(b.artist_name_display||''),
                'date': (a,b) => (b.acquisition_date||'').localeCompare(a.acquisition_date||''),
                'price_desc': (a,b) => (b.acquisition_price||0) - (a.acquisition_price||0),
                'price_asc': (a,b) => (a.acquisition_price||0) - (b.acquisition_price||0),
                'category': (a,b) => (a.category||'').localeCompare(b.category||''),
                'newest': (a,b) => (b.created_at||'').localeCompare(a.created_at||''),
            };
            if (sortFns[sort]) items.sort(sortFns[sort]);

            // Pagination
            const page = parseInt(params.get('page') || '1');
            const perPage = parseInt(params.get('per_page') || '48');
            const total = items.length;
            const start = (page - 1) * perPage;
            const pageItems = items.slice(start, start + perPage);

            // Add photo info
            for (const item of pageItems) {
                item.photo_count = item.photos ? item.photos.length : 0;
            }

            return {
                items: pageItems,
                total: total,
                page: page,
                per_page: perPage,
                pages: Math.max(1, Math.ceil(total / perPage)),
            };
        }
        // Collection detail
        const detailMatch = endpoint.match(/^collection\\/(\\d+)$/);
        if (detailMatch) {
            const id = parseInt(detailMatch[1]);
            const obj = STATIC_DATA.objects.find(o => o.id === id);
            if (!obj) return { error: 'Not found' };
            const result = { ...obj };
            result.photos = (obj.photos || []).map(p => ({
                ...p,
                url: 'images/' + p.filename,
            }));
            result.valuations = [];
            return result;
        }
        // Stats
        if (endpoint === 'stats') return STATIC_DATA.stats;
        // Default
        return { error: 'Not found in static mode' };
    }
}
"""

    # Wstaw override po <script> tagiem (po "// === STATE ===")
    html_output = html_output.replace("// === STATE ===", api_override + "\n// === STATE ===")

    # Ukryj scraper/aukcje tabs w trybie statycznym (bo nie ma tych danych)
    static_css = """
<style>
/* Static mode: hide server-only features */
.nav-tab[data-view="items"], .nav-tab[data-view="runs"] { display: none !important; }
.photo-upload-area { display: none !important; }
.btn-danger { display: none !important; }
button[onclick*="openAddModal"] { display: none !important; }
button[onclick*="openEditModal"] { display: none !important; }
</style>
"""
    html_output = html_output.replace("</head>", static_css + "</head>")

    # Auto-switch do collection view
    html_output = html_output.replace(
        """<button class="nav-tab" data-view="collection" onclick="switchView('collection', this)">Kolekcja</button>""",
        """<button class="nav-tab active" data-view="collection" onclick="switchView('collection', this)">Kolekcja</button>"""
    )
    html_output = html_output.replace(
        """<button class="nav-tab active" data-view="items" onclick="switchView('items', this)">Aukcje</button>""",
        """<button class="nav-tab" data-view="items" onclick="switchView('items', this)">Aukcje</button>"""
    )

    # Zapisz HTML
    out_path = os.path.join(output_dir, "index.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html_output)

    # Oblicz rozmiar
    html_size = os.path.getsize(out_path)
    total_size = html_size
    if include_images:
        img_dir = os.path.join(output_dir, "images")
        for fn in os.listdir(img_dir):
            total_size += os.path.getsize(os.path.join(img_dir, fn))

    print(f"\n  HTML: {html_size/1024:.0f} KB")
    print(f"  Razem: {total_size/(1024*1024):.1f} MB")
    print(f"\n✅ Export gotowy: {os.path.abspath(output_dir)}/")
    print(f"   Otwórz w przeglądarce: {os.path.abspath(out_path)}")

    if include_images:
        print(f"\n📁 Aby wrzucić na GitHub Pages:")
        print(f"   1. git add {output_dir}/")
        print(f"   2. git commit -m 'Static catalog export'")
        print(f"   3. git push")
        print(f"   4. W Settings → Pages → Source: Deploy from branch → folder: /docs")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Export static catalog site")
    parser.add_argument("--output", default="docs",
                        help="Output directory (default: docs)")
    parser.add_argument("--no-images", action="store_true",
                        help="Skip copying images")
    args = parser.parse_args()

    export_static(
        output_dir=args.output,
        include_images=not args.no_images,
    )
