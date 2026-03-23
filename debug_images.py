#!/usr/bin/env python3
import sys, os
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import database

database.init_db()
conn = database.get_connection()

rows = conn.execute("""
    SELECT inventory_number, title
    FROM collection_objects
    WHERE inventory_number LIKE 'GL-%'
    ORDER BY inventory_number
""").fetchall()

# OBJECT_IMAGES -- synced with export_gluchowski.py (2026-03-20)
OBJECT_IMAGES = {
    # Ch I - PON
    "GL-001": ["x"], "GL-002": ["x"], "GL-003": ["x"], "GL-004": ["x"],
    # Ch II - Legiony
    "GL-010": ["x"], "GL-012": ["x"], "GL-013": ["x"], "GL-014": ["x"], "GL-016": ["x"],
    # Ch III - II RP
    "GL-020": ["x"], "GL-021": ["x"], "GL-022": ["x"], "GL-025": ["x"], "GL-026": ["x"],
    "GL-027": ["x"], "GL-028": ["x"], "GL-029": ["x"],
    # Ch IV - Sosnkowski
    "GL-030": ["x"], "GL-031": ["x"], "GL-032": ["x"], "GL-033": ["x"],
    "GL-034": ["x"], "GL-035": ["x"], "GL-036": ["x"], "GL-037": ["x"], "GL-038": ["x"],
    # Ch V - Getto
    "GL-040": ["x"], "GL-041": ["x"], "GL-042": ["x"], "GL-043": ["x"], "GL-044": ["x"],
    # Ch VI - 7 Pulk
    "GL-051": ["x"], "GL-052": ["x"],
    # Ch VII - Krzysztof Andrzej
    "GL-060": ["x"], "GL-061": ["x"], "GL-063": ["x"], "GL-064": ["x"],
    "GL-065": ["x"], "GL-066": ["x"], "GL-067": ["x"], "GL-068": ["x"], "GL-069": ["x"],
    # Ch VIII - Szkocja
    "GL-070": ["x"], "GL-071": ["x"], "GL-072": ["x"],
    # Seria 29z - all have images
    "GL-100": ["x"], "GL-101": ["x"], "GL-102": ["x"], "GL-103": ["x"],
    "GL-104": ["x"], "GL-105": ["x"], "GL-106": ["x"], "GL-107": ["x"],
    "GL-108": ["x"], "GL-109": ["x"], "GL-110": ["x"], "GL-111": ["x"],
    "GL-112": ["x"], "GL-113": ["x"], "GL-114": ["x"], "GL-115": ["x"],
    "GL-116": ["x"], "GL-117": ["x"], "GL-118": ["x"], "GL-119": ["x"],
    "GL-120": ["x"], "GL-121": ["x"], "GL-122": ["x"], "GL-123": ["x"],
    "GL-124": ["x"], "GL-125": ["x"], "GL-126": ["x"], "GL-127": ["x"],
    "GL-128": ["x"], "GL-129": ["x"], "GL-130": ["x"], "GL-131": ["x"],
    "GL-132": ["x"], "GL-133": ["x"], "GL-134": ["x"], "GL-135": ["x"],
}

print(f"Obiektow w DB: {len(rows)}")
print(f"Obiektow z przypisanymi zdjeciami: {len(OBJECT_IMAGES)}")
print()

no_img = []
for r in rows:
    inv = r["inventory_number"]
    if inv not in OBJECT_IMAGES:
        no_img.append((inv, r["title"][:80]))

print(f"BRAK ZDJEC ({len(no_img)} obiektow):")
for inv, title in no_img:
    print(f"  {inv}: {title}")

# Check unassigned images from PDFs
img_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "docs", "gluchowski_img")
all_imgs = sorted(os.listdir(img_dir))
assigned = set()
for imgs in OBJECT_IMAGES.values():
    for i in imgs:
        if i != "x":
            assigned.add(i)

# Only check Naukowy and Tematyczny (not 29z which are all assigned)
unassigned = [f for f in all_imgs if f not in assigned and not f.startswith("Seria_29z")]
print(f"\nNIEPRZYPISANE ZDJECIA z Naukowy/Tematyczny ({len(unassigned)}):")
for f in unassigned:
    print(f"  {f}")

conn.close()
