#!/usr/bin/env python3
"""
export_sales_catalog.py — Eksportuje kolekcję jako profesjonalny katalog sprzedażowy.

Generuje statyczną stronę HTML z podziałem na:
  - Tiers (A/B/C) — muzeum / galeria / dekoracyjne
  - Rynki docelowe (PL/BR/EU/INT)
  - Kategorie (malarstwo, grafika, rzeźba...)
  - Landing pages per artysta / per kategoria

Galerzysta otwiera link — w 10 sekund wie co jest warte jego czasu.

Użycie:
    python export_sales_catalog.py                    # → ./docs/
    python export_sales_catalog.py --output ./build   # → ./build/
"""

import os
import sys
import json
import shutil
import argparse
from collections import defaultdict

# Fix Windows console encoding
import io
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import database
from config import COLLECTION_IMAGES_DIR
from sales_intelligence import TIER_LABELS, CATEGORY_MARKETS


def export_sales_catalog(output_dir="docs", include_images=True):
    """Eksportuje katalog sprzedażowy jako statyczną stronę."""

    database.init_db()
    conn = database.get_connection()

    print(f"Eksport katalogu sprzedażowego do: {output_dir}/\n")

    # --- 1. Przygotuj katalog ---
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir, exist_ok=True)

    # --- 2. Pobierz dane ---
    objects = conn.execute("""
        SELECT * FROM collection_objects
        ORDER BY sales_priority ASC, sales_tier ASC, artist_name_display ASC
    """).fetchall()
    objects_list = [dict(o) for o in objects]

    # Dodaj zdjęcia
    for obj in objects_list:
        photos = database.get_object_photos(conn, obj["id"])
        photo_list = []
        for p in photos:
            fname = os.path.basename(p["file_path"])
            photo_list.append({
                "filename": fname,
                "is_primary": p["is_primary"],
            })
        obj["photos"] = photo_list
        primary = [ph for ph in photo_list if ph["is_primary"]]
        obj["primary_photo"] = (
            f"images/{primary[0]['filename']}" if primary
            else (f"images/{photo_list[0]['filename']}" if photo_list else None)
        )

    conn.close()

    # --- 3. Oblicz statystyki ---
    tier_counts = defaultdict(int)
    market_counts = defaultdict(int)
    category_counts = defaultdict(int)
    artist_counts = defaultdict(list)

    for obj in objects_list:
        tier = obj.get("sales_tier") or "C"
        tier_counts[tier] += 1
        cat = obj.get("category") or "Inne"
        category_counts[cat] += 1
        artist = obj.get("artist_name_display") or "Unknown"
        if artist and artist != "None":
            artist_counts[artist].append(obj)
        for m in (obj.get("target_markets") or "").split(", "):
            if m.strip():
                market_counts[m.strip()] += 1

    # Tier A artists
    tier_a_artists = defaultdict(list)
    for obj in objects_list:
        if obj.get("sales_tier") == "A" and obj.get("artist_name_display"):
            tier_a_artists[obj["artist_name_display"]].append(obj)

    total_photos = sum(len(o["photos"]) for o in objects_list)
    print(f"  Obiektów: {len(objects_list)}")
    print(f"  Zdjęć: {total_photos}")

    # --- 4. Kopiuj zdjęcia ---
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

    # --- 5. Buduj dane JSON ---
    embedded_data = {
        "objects": objects_list,
        "tier_counts": dict(tier_counts),
        "market_counts": dict(market_counts),
        "category_counts": dict(category_counts),
        "tier_a_artists": {k: len(v) for k, v in tier_a_artists.items()},
        "total": len(objects_list),
        "total_photos": total_photos,
    }

    json_data = json.dumps(embedded_data, ensure_ascii=False, default=str)

    # --- 6. Generuj HTML ---
    html = generate_sales_html(json_data, embedded_data)

    out_path = os.path.join(output_dir, "index.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)

    html_size = os.path.getsize(out_path)
    total_size = html_size
    if include_images:
        img_dir = os.path.join(output_dir, "images")
        if os.path.exists(img_dir):
            for fn in os.listdir(img_dir):
                total_size += os.path.getsize(os.path.join(img_dir, fn))

    print(f"\n  HTML: {html_size/1024:.0f} KB")
    print(f"  Razem: {total_size/(1024*1024):.1f} MB")
    print(f"\n✅ Katalog sprzedażowy gotowy: {os.path.abspath(output_dir)}/")
    print(f"   Otwórz: {os.path.abspath(out_path)}")


def generate_sales_html(json_data, stats):
    """Generuje kompletny HTML katalogu sprzedażowego."""

    return f'''<!DOCTYPE html>
<html lang="pl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Polish & Brazilian Art — Sales Catalog</title>
<meta name="description" content="Curated collection of Polish and Brazilian art: paintings, prints, sculpture, photography. Museum-grade to gallery-level works available for acquisition.">
<style>
/* === RESET === */
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{ font-family: 'Georgia', 'Times New Roman', serif; background: #0c0c0e; color: #d4d0c8; min-height: 100vh; }}
a {{ color: #d4a853; text-decoration: none; }}
a:hover {{ text-decoration: underline; }}

/* === HEADER === */
.header {{
    background: linear-gradient(180deg, #111113 0%, #0c0c0e 100%);
    border-bottom: 1px solid #1e1e22;
    padding: 40px 48px 32px;
    text-align: center;
}}
.header h1 {{
    font-size: 28px;
    font-weight: 300;
    color: #fff;
    letter-spacing: 6px;
    text-transform: uppercase;
    margin-bottom: 8px;
}}
.header h1 em {{
    color: #d4a853;
    font-style: normal;
    font-weight: 400;
}}
.header .subtitle {{
    font-size: 14px;
    color: #666;
    letter-spacing: 3px;
    text-transform: uppercase;
}}
.header .contact {{
    margin-top: 16px;
    font-size: 13px;
    color: #555;
}}

/* === NAV === */
.nav {{
    background: #111113;
    border-bottom: 1px solid #1e1e22;
    padding: 0 48px;
    display: flex;
    gap: 0;
    position: sticky;
    top: 0;
    z-index: 100;
    overflow-x: auto;
}}
.nav button {{
    background: transparent;
    border: none;
    color: #666;
    padding: 14px 24px;
    font-family: inherit;
    font-size: 13px;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    cursor: pointer;
    border-bottom: 2px solid transparent;
    transition: all 0.2s;
    white-space: nowrap;
}}
.nav button:hover {{ color: #d4a853; }}
.nav button.active {{
    color: #d4a853;
    border-bottom-color: #d4a853;
}}

/* === TIER BADGES === */
.tier-badge {{
    display: inline-block;
    padding: 2px 10px;
    border-radius: 3px;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1px;
    font-family: -apple-system, sans-serif;
}}
.tier-A {{ background: #d4a853; color: #000; }}
.tier-A- {{ background: #c4983f; color: #000; }}
.tier-B\\+ {{ background: rgba(139,115,85,0.3); color: #c4a870; border: 1px solid #8B7355; }}
.tier-B {{ background: rgba(107,142,90,0.2); color: #9aba87; border: 1px solid #6B8E5A; }}
.tier-C\\+ {{ background: rgba(91,123,138,0.2); color: #8ab0c0; border: 1px solid #5B7B8A; }}
.tier-C {{ background: rgba(136,136,136,0.15); color: #888; border: 1px solid #555; }}

/* === DASHBOARD === */
.dashboard {{
    padding: 48px;
    max-width: 1400px;
    margin: 0 auto;
}}
.stats-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 20px;
    margin-bottom: 48px;
}}
.stat-card {{
    background: #111113;
    border: 1px solid #1e1e22;
    border-radius: 4px;
    padding: 24px;
    text-align: center;
}}
.stat-card .number {{
    font-size: 36px;
    font-weight: 300;
    color: #d4a853;
}}
.stat-card .label {{
    font-size: 12px;
    color: #666;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-top: 8px;
}}

/* === TIER SECTION === */
.tier-section {{
    margin-bottom: 64px;
}}
.tier-header {{
    display: flex;
    align-items: center;
    gap: 16px;
    margin-bottom: 8px;
    padding-bottom: 12px;
    border-bottom: 1px solid #1e1e22;
}}
.tier-header h2 {{
    font-size: 22px;
    font-weight: 300;
    color: #fff;
    letter-spacing: 2px;
}}
.tier-header .count {{
    color: #555;
    font-size: 14px;
}}
.tier-description {{
    font-size: 14px;
    color: #555;
    margin-bottom: 24px;
    font-style: italic;
}}

/* === ITEMS GRID === */
.items-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 20px;
}}

.item-card {{
    background: #111113;
    border: 1px solid #1e1e22;
    border-radius: 4px;
    overflow: hidden;
    transition: border-color 0.2s, transform 0.2s;
    cursor: pointer;
}}
.item-card:hover {{
    border-color: #d4a853;
    transform: translateY(-3px);
}}
.item-card .thumb {{
    width: 100%;
    height: 220px;
    background: #0a0a0c;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    position: relative;
}}
.item-card .thumb img {{
    max-width: 100%;
    max-height: 100%;
    object-fit: contain;
}}
.item-card .thumb .no-img {{
    color: #222;
    font-size: 48px;
}}
.item-card .thumb .tier-tag {{
    position: absolute;
    top: 8px;
    right: 8px;
}}
.item-card .info {{
    padding: 16px;
}}
.item-card .artist-name {{
    font-size: 13px;
    color: #d4a853;
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-bottom: 4px;
}}
.item-card .title {{
    font-size: 15px;
    color: #e8e4dc;
    line-height: 1.4;
    margin-bottom: 8px;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
}}
.item-card .meta-row {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 4px;
}}
.item-card .category {{
    font-size: 11px;
    color: #666;
    text-transform: uppercase;
    letter-spacing: 1px;
}}
.item-card .value {{
    font-size: 13px;
    color: #8aba87;
    font-family: -apple-system, sans-serif;
}}
.item-card .markets {{
    display: flex;
    gap: 4px;
    margin-top: 8px;
    flex-wrap: wrap;
}}
.market-tag {{
    font-size: 10px;
    padding: 2px 6px;
    border-radius: 2px;
    font-family: -apple-system, sans-serif;
    font-weight: 600;
    letter-spacing: 0.5px;
}}
.market-PL {{ background: rgba(220,53,69,0.15); color: #dc3545; border: 1px solid rgba(220,53,69,0.3); }}
.market-BR {{ background: rgba(40,167,69,0.15); color: #28a745; border: 1px solid rgba(40,167,69,0.3); }}
.market-EU {{ background: rgba(0,123,255,0.15); color: #007bff; border: 1px solid rgba(0,123,255,0.3); }}
.market-INT {{ background: rgba(212,168,83,0.15); color: #d4a853; border: 1px solid rgba(212,168,83,0.3); }}
.market-US {{ background: rgba(111,66,193,0.15); color: #6f42c1; border: 1px solid rgba(111,66,193,0.3); }}

/* === DETAIL MODAL === */
.modal-overlay {{
    display: none;
    position: fixed;
    inset: 0;
    background: rgba(0,0,0,0.85);
    z-index: 1000;
    align-items: center;
    justify-content: center;
    padding: 20px;
}}
.modal-overlay.open {{ display: flex; }}
.modal {{
    background: #111113;
    border: 1px solid #2a2a2e;
    border-radius: 6px;
    max-width: 800px;
    width: 100%;
    max-height: 90vh;
    overflow-y: auto;
    padding: 32px;
}}
.modal .close-btn {{
    float: right;
    background: none;
    border: none;
    color: #666;
    font-size: 24px;
    cursor: pointer;
    padding: 4px 8px;
    line-height: 1;
}}
.modal .close-btn:hover {{ color: #d4a853; }}
.modal h2 {{
    font-size: 20px;
    font-weight: 400;
    color: #fff;
    margin-bottom: 4px;
    padding-right: 40px;
}}
.modal .modal-artist {{
    font-size: 14px;
    color: #d4a853;
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-bottom: 16px;
}}
.modal .detail-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin: 20px 0;
}}
.modal .detail-item {{
    background: #0c0c0e;
    padding: 12px;
    border-radius: 4px;
}}
.modal .detail-item .dl {{
    font-size: 11px;
    color: #555;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 4px;
}}
.modal .detail-item .dv {{
    font-size: 14px;
    color: #d4d0c8;
}}
.modal .sales-box {{
    background: rgba(212,168,83,0.08);
    border: 1px solid rgba(212,168,83,0.2);
    border-radius: 4px;
    padding: 16px;
    margin-top: 20px;
}}
.modal .sales-box h3 {{
    font-size: 14px;
    color: #d4a853;
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-bottom: 12px;
}}
.modal .buyers-list {{
    list-style: none;
    padding: 0;
}}
.modal .buyers-list li {{
    font-size: 13px;
    color: #aaa;
    padding: 4px 0;
    border-bottom: 1px solid #1e1e22;
}}
.modal .buyers-list li:last-child {{ border-bottom: none; }}
.modal .strategy-note {{
    font-size: 13px;
    color: #888;
    font-style: italic;
    margin-top: 12px;
    line-height: 1.5;
}}
.modal .photo-gallery {{
    display: flex;
    gap: 8px;
    margin: 16px 0;
    flex-wrap: wrap;
}}
.modal .photo-gallery img {{
    max-height: 300px;
    max-width: 100%;
    border-radius: 4px;
    object-fit: contain;
    background: #0a0a0c;
}}

/* === SEARCH === */
.search-bar {{
    display: flex;
    gap: 12px;
    margin-bottom: 32px;
    flex-wrap: wrap;
}}
.search-bar input {{
    flex: 1;
    min-width: 200px;
    padding: 12px 16px;
    background: #111113;
    border: 1px solid #1e1e22;
    border-radius: 4px;
    color: #d4d0c8;
    font-family: inherit;
    font-size: 14px;
    outline: none;
}}
.search-bar input:focus {{ border-color: #d4a853; }}
.search-bar input::placeholder {{ color: #444; }}
.search-bar select {{
    padding: 12px 16px;
    background: #111113;
    border: 1px solid #1e1e22;
    border-radius: 4px;
    color: #d4d0c8;
    font-family: inherit;
    font-size: 14px;
    outline: none;
    cursor: pointer;
}}
.search-bar select:focus {{ border-color: #d4a853; }}

/* === SECTION (hidden by default) === */
.section {{ display: none; }}
.section.active {{ display: block; }}

/* === RESPONSIVE === */
@media (max-width: 768px) {{
    .dashboard {{ padding: 24px 16px; }}
    .header {{ padding: 24px 16px; }}
    .nav {{ padding: 0 16px; }}
    .items-grid {{ grid-template-columns: 1fr; }}
    .modal .detail-grid {{ grid-template-columns: 1fr; }}
    .header h1 {{ font-size: 20px; letter-spacing: 3px; }}
}}

/* === PRINT === */
@media print {{
    body {{ background: #fff; color: #000; }}
    .nav, .search-bar {{ display: none; }}
    .item-card {{ break-inside: avoid; border-color: #ddd; }}
    .item-card .artist-name {{ color: #8B7355; }}
    .stat-card {{ border-color: #ddd; }}
    .stat-card .number {{ color: #8B7355; }}
}}
</style>
</head>
<body>

<div class="header">
    <h1>Polish & Brazilian <em>Art</em></h1>
    <div class="subtitle">Private Collection — Sales Catalog</div>
    <div class="contact">Inquiries: contact for details • {stats['total']} works • {stats['total_photos']} photographs</div>
</div>

<div class="nav" id="nav">
    <button class="active" onclick="showSection('overview', this)">Overview</button>
    <button onclick="showSection('tier-a', this)">Museum-Grade ({stats['tier_counts'].get('A', 0)})</button>
    <button onclick="showSection('tier-b', this)">Gallery ({stats['tier_counts'].get('B', 0) + stats['tier_counts'].get('B+', 0)})</button>
    <button onclick="showSection('tier-c', this)">Collectible ({stats['tier_counts'].get('C+', 0) + stats['tier_counts'].get('C', 0)})</button>
    <button onclick="showSection('market-pl', this)">Poland ({stats['market_counts'].get('PL', 0)})</button>
    <button onclick="showSection('market-br', this)">Brazil ({stats['market_counts'].get('BR', 0)})</button>
    <button onclick="showSection('all', this)">All Works</button>
</div>

<div class="dashboard">

    <!-- OVERVIEW -->
    <div class="section active" id="section-overview">
        <div class="stats-grid">
            <div class="stat-card">
                <div class="number">{stats['total']}</div>
                <div class="label">Total Works</div>
            </div>
            <div class="stat-card">
                <div class="number">{stats['tier_counts'].get('A', 0)}</div>
                <div class="label">Museum-Grade</div>
            </div>
            <div class="stat-card">
                <div class="number">{stats['tier_counts'].get('B', 0) + stats['tier_counts'].get('B+', 0)}</div>
                <div class="label">Gallery Level</div>
            </div>
            <div class="stat-card">
                <div class="number">{len(stats['tier_a_artists'])}</div>
                <div class="label">Key Artists</div>
            </div>
            <div class="stat-card">
                <div class="number">{stats['total_photos']}</div>
                <div class="label">Photographs</div>
            </div>
        </div>

        <div class="tier-section">
            <div class="tier-header">
                <h2>Top Artists — Museum Grade</h2>
            </div>
            <div class="tier-description">
                Artists with established auction records. Works suitable for institutional acquisition, major auction houses, and serious private collectors.
            </div>
            <div class="items-grid" id="overview-tier-a-grid"></div>
        </div>
    </div>

    <!-- TIER A -->
    <div class="section" id="section-tier-a">
        <div class="tier-section">
            <div class="tier-header">
                <span class="tier-badge tier-A">TIER A</span>
                <h2>Museum-Grade Works</h2>
                <span class="count" id="tier-a-count"></span>
            </div>
            <div class="tier-description">
                Institutional quality. Artists with auction records exceeding €10,000. Recommended channels: DESA Unicum, Christie's, Sotheby's, Bolsa de Arte, Artcurial.
            </div>
            <div class="search-bar">
                <input type="text" id="search-tier-a" placeholder="Search artist, title..." oninput="filterGrid('tier-a')">
                <select id="cat-tier-a" onchange="filterGrid('tier-a')">
                    <option value="">All categories</option>
                </select>
            </div>
            <div class="items-grid" id="tier-a-grid"></div>
        </div>
    </div>

    <!-- TIER B -->
    <div class="section" id="section-tier-b">
        <div class="tier-section">
            <div class="tier-header">
                <span class="tier-badge tier-B">TIER B</span>
                <h2>Gallery-Level Works</h2>
                <span class="count" id="tier-b-count"></span>
            </div>
            <div class="tier-description">
                Recognized artists with active gallery market. Suitable for mid-range galleries, private collectors, and regional auction houses.
            </div>
            <div class="search-bar">
                <input type="text" id="search-tier-b" placeholder="Search artist, title..." oninput="filterGrid('tier-b')">
                <select id="cat-tier-b" onchange="filterGrid('tier-b')">
                    <option value="">All categories</option>
                </select>
            </div>
            <div class="items-grid" id="tier-b-grid"></div>
        </div>
    </div>

    <!-- TIER C -->
    <div class="section" id="section-tier-c">
        <div class="tier-section">
            <div class="tier-header">
                <span class="tier-badge tier-C\\+">TIER C</span>
                <h2>Collectible & Decorative</h2>
                <span class="count" id="tier-c-count"></span>
            </div>
            <div class="tier-description">
                Decorative objects, prints, ephemera. Local market sales, online platforms, antique dealers.
            </div>
            <div class="search-bar">
                <input type="text" id="search-tier-c" placeholder="Search..." oninput="filterGrid('tier-c')">
            </div>
            <div class="items-grid" id="tier-c-grid"></div>
        </div>
    </div>

    <!-- MARKET PL -->
    <div class="section" id="section-market-pl">
        <div class="tier-section">
            <div class="tier-header">
                <span class="market-tag market-PL">PL</span>
                <h2>Poland Market</h2>
                <span class="count" id="market-pl-count"></span>
            </div>
            <div class="tier-description">
                Works recommended for the Polish market. Key auction houses: DESA Unicum (Warsaw), Agra-Art, Polswiss Art, Rempex, Libra.
            </div>
            <div class="search-bar">
                <input type="text" id="search-market-pl" placeholder="Search..." oninput="filterGrid('market-pl')">
            </div>
            <div class="items-grid" id="market-pl-grid"></div>
        </div>
    </div>

    <!-- MARKET BR -->
    <div class="section" id="section-market-br">
        <div class="tier-section">
            <div class="tier-header">
                <span class="market-tag market-BR">BR</span>
                <h2>Brazil Market</h2>
                <span class="count" id="market-br-count"></span>
            </div>
            <div class="tier-description">
                Works recommended for the Brazilian market. Key buyers: Bolsa de Arte, James Lisboa, Gravura Brasileira, Dan Galeria, Pinakotheke.
            </div>
            <div class="search-bar">
                <input type="text" id="search-market-br" placeholder="Search..." oninput="filterGrid('market-br')">
            </div>
            <div class="items-grid" id="market-br-grid"></div>
        </div>
    </div>

    <!-- ALL WORKS -->
    <div class="section" id="section-all">
        <div class="tier-section">
            <div class="tier-header">
                <h2>Complete Collection</h2>
                <span class="count">{stats['total']} works</span>
            </div>
            <div class="search-bar">
                <input type="text" id="search-all" placeholder="Search artist, title, category..." oninput="filterGrid('all')">
                <select id="cat-all" onchange="filterGrid('all')">
                    <option value="">All categories</option>
                </select>
                <select id="tier-all" onchange="filterGrid('all')">
                    <option value="">All tiers</option>
                    <option value="A">Tier A — Museum</option>
                    <option value="B+">Tier B+ — Strong Gallery</option>
                    <option value="B">Tier B — Gallery</option>
                    <option value="C+">Tier C+ — Collectible</option>
                    <option value="C">Tier C — Decorative</option>
                </select>
                <select id="market-all" onchange="filterGrid('all')">
                    <option value="">All markets</option>
                    <option value="PL">Poland</option>
                    <option value="BR">Brazil</option>
                    <option value="EU">Europe</option>
                    <option value="INT">International</option>
                </select>
            </div>
            <div class="items-grid" id="all-grid"></div>
        </div>
    </div>

</div>

<!-- DETAIL MODAL -->
<div class="modal-overlay" id="detailModal" onclick="if(event.target===this)closeDetail()">
    <div class="modal" id="detailContent"></div>
</div>

<script>
const DATA = {json_data};

// === RENDER CARD ===
function renderCard(obj) {{
    const tier = obj.sales_tier || 'C';
    const tierClass = 'tier-' + tier.replace('+', '\\\\+');
    const photo = obj.primary_photo ? `<img src="${{obj.primary_photo}}" alt="" loading="lazy">` : '<div class="no-img">◈</div>';
    const artist = obj.artist_name_display || '';
    const markets = (obj.target_markets || '').split(', ').filter(Boolean);
    const marketTags = markets.map(m => `<span class="market-tag market-${{m}}">${{m}}</span>`).join('');
    const value = obj.estimated_market_value_eur ? `€${{obj.estimated_market_value_eur}}` : '';
    const title = (obj.title_en || obj.title || '').substring(0, 100);

    return `
        <div class="item-card" onclick="openDetail(${{obj.id}})">
            <div class="thumb">
                ${{photo}}
                <span class="tier-tag tier-badge tier-${{tier}}">${{tier}}</span>
            </div>
            <div class="info">
                ${{artist ? `<div class="artist-name">${{artist}}</div>` : ''}}
                <div class="title">${{title}}</div>
                <div class="meta-row">
                    <span class="category">${{obj.category || ''}}</span>
                    ${{value ? `<span class="value">${{value}}</span>` : ''}}
                </div>
                <div class="markets">${{marketTags}}</div>
            </div>
        </div>
    `;
}}

// === FILTER & RENDER ===
function getFilteredItems(sectionKey) {{
    let items = [...DATA.objects];
    const search = document.getElementById('search-' + sectionKey);
    const catSelect = document.getElementById('cat-' + sectionKey);
    const tierSelect = document.getElementById('tier-' + sectionKey);
    const marketSelect = document.getElementById('market-' + sectionKey);

    // Tier filter by section
    if (sectionKey === 'tier-a') items = items.filter(i => i.sales_tier === 'A');
    if (sectionKey === 'tier-b') items = items.filter(i => ['B', 'B+'].includes(i.sales_tier));
    if (sectionKey === 'tier-c') items = items.filter(i => ['C', 'C+'].includes(i.sales_tier));
    if (sectionKey === 'market-pl') items = items.filter(i => (i.target_markets||'').includes('PL'));
    if (sectionKey === 'market-br') items = items.filter(i => (i.target_markets||'').includes('BR'));

    // Search
    if (search && search.value) {{
        const s = search.value.toLowerCase();
        items = items.filter(i =>
            (i.title||'').toLowerCase().includes(s) ||
            (i.title_en||'').toLowerCase().includes(s) ||
            (i.artist_name_display||'').toLowerCase().includes(s) ||
            (i.description||'').toLowerCase().includes(s) ||
            (i.category||'').toLowerCase().includes(s) ||
            (i.sales_strategy||'').toLowerCase().includes(s)
        );
    }}

    // Category filter
    if (catSelect && catSelect.value) {{
        items = items.filter(i => i.category === catSelect.value);
    }}

    // Tier dropdown (all section)
    if (tierSelect && tierSelect.value) {{
        items = items.filter(i => i.sales_tier === tierSelect.value);
    }}

    // Market dropdown (all section)
    if (marketSelect && marketSelect.value) {{
        items = items.filter(i => (i.target_markets||'').includes(marketSelect.value));
    }}

    return items;
}}

function filterGrid(sectionKey) {{
    const items = getFilteredItems(sectionKey);
    const grid = document.getElementById(sectionKey + '-grid');
    if (!grid) return;
    grid.innerHTML = items.map(renderCard).join('');

    // Update count
    const countEl = document.getElementById(sectionKey + '-count');
    if (countEl) countEl.textContent = items.length + ' works';
}}

// === SECTIONS ===
function showSection(id, btn) {{
    document.querySelectorAll('.section').forEach(s => s.classList.remove('active'));
    document.getElementById('section-' + id).classList.add('active');
    document.querySelectorAll('.nav button').forEach(b => b.classList.remove('active'));
    if (btn) btn.classList.add('active');
    filterGrid(id);
}}

// === DETAIL ===
function openDetail(id) {{
    const obj = DATA.objects.find(o => o.id === id);
    if (!obj) return;

    const photos = (obj.photos || []).map(p =>
        `<img src="images/${{p.filename}}" alt="">`
    ).join('');

    const buyers = (obj.target_buyers || '').split(' | ').filter(Boolean).map(b =>
        `<li>${{b}}</li>`
    ).join('');

    const markets = (obj.target_markets || '').split(', ').filter(Boolean).map(m =>
        `<span class="market-tag market-${{m}}">${{m}}</span>`
    ).join(' ');

    document.getElementById('detailContent').innerHTML = `
        <button class="close-btn" onclick="closeDetail()">&times;</button>
        <div class="modal-artist">${{obj.artist_name_display || 'Unknown Artist'}}</div>
        <h2>${{obj.title_en || obj.title || 'Untitled'}}</h2>

        ${{photos ? `<div class="photo-gallery">${{photos}}</div>` : ''}}

        <div class="detail-grid">
            <div class="detail-item">
                <div class="dl">Category</div>
                <div class="dv">${{obj.category || '—'}}</div>
            </div>
            <div class="detail-item">
                <div class="dl">Tier</div>
                <div class="dv"><span class="tier-badge tier-${{obj.sales_tier || 'C'}}">${{obj.sales_tier || 'C'}}</span></div>
            </div>
            <div class="detail-item">
                <div class="dl">Medium</div>
                <div class="dv">${{obj.medium || '—'}}</div>
            </div>
            <div class="detail-item">
                <div class="dl">Dimensions</div>
                <div class="dv">${{obj.dimensions_notes || (obj.height_cm && obj.width_cm ? obj.height_cm + ' × ' + obj.width_cm + ' cm' : '—')}}</div>
            </div>
            <div class="detail-item">
                <div class="dl">Estimated Value (EUR)</div>
                <div class="dv" style="color:#8aba87;font-weight:600">${{obj.estimated_market_value_eur ? '€' + obj.estimated_market_value_eur : '—'}}</div>
            </div>
            <div class="detail-item">
                <div class="dl">Acquisition Price</div>
                <div class="dv">${{obj.acquisition_price ? 'R$ ' + Number(obj.acquisition_price).toLocaleString('pt-BR') : '—'}}</div>
            </div>
            <div class="detail-item">
                <div class="dl">Condition</div>
                <div class="dv">${{obj.condition_grade || 'Not assessed'}}</div>
            </div>
            <div class="detail-item">
                <div class="dl">Authentication</div>
                <div class="dv">${{obj.authentication_status || 'Unverified'}}</div>
            </div>
        </div>

        ${{obj.provenance ? `<div class="detail-item" style="margin:12px 0"><div class="dl">Provenance</div><div class="dv">${{obj.provenance}}</div></div>` : ''}}
        ${{obj.description ? `<div class="detail-item" style="margin:12px 0"><div class="dl">Description</div><div class="dv">${{obj.description_en || obj.description}}</div></div>` : ''}}

        <div class="sales-box">
            <h3>Sales Intelligence</h3>
            <div class="detail-grid" style="margin:0 0 12px 0">
                <div class="detail-item">
                    <div class="dl">Target Markets</div>
                    <div class="dv">${{markets || '—'}}</div>
                </div>
                <div class="detail-item">
                    <div class="dl">Priority</div>
                    <div class="dv">${{obj.sales_priority === 1 ? '🔴 High — Contact now' : obj.sales_priority === 2 ? '🟡 Medium' : '⚪ Standard'}}</div>
                </div>
            </div>
            ${{buyers ? `<div class="dl" style="font-size:11px;color:#555;text-transform:uppercase;letter-spacing:1px;margin-bottom:8px">Recommended Buyers</div><ul class="buyers-list">${{buyers}}</ul>` : ''}}
            ${{obj.sales_strategy ? `<div class="strategy-note">${{obj.sales_strategy}}</div>` : ''}}
        </div>
    `;

    document.getElementById('detailModal').classList.add('open');
}}

function closeDetail() {{
    document.getElementById('detailModal').classList.remove('open');
}}

// === KEYBOARD ===
document.addEventListener('keydown', e => {{
    if (e.key === 'Escape') closeDetail();
}});

// === INIT ===
(function init() {{
    // Populate category selects
    const cats = [...new Set(DATA.objects.map(o => o.category).filter(Boolean))].sort();
    document.querySelectorAll('select[id^="cat-"]').forEach(sel => {{
        cats.forEach(c => {{
            const opt = document.createElement('option');
            opt.value = c;
            opt.textContent = c;
            sel.appendChild(opt);
        }});
    }});

    // Overview: show top tier A items (first 12)
    const tierAItems = DATA.objects.filter(i => i.sales_tier === 'A').slice(0, 12);
    document.getElementById('overview-tier-a-grid').innerHTML = tierAItems.map(renderCard).join('');

    // Pre-render tier A
    filterGrid('tier-a');
}})();
</script>
</body>
</html>'''


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Export sales catalog")
    parser.add_argument("--output", default="docs", help="Output directory")
    parser.add_argument("--no-images", action="store_true", help="Skip images")
    args = parser.parse_args()

    export_sales_catalog(
        output_dir=args.output,
        include_images=not args.no_images,
    )
