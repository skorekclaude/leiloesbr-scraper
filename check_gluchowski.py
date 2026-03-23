import sys, os
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import database
database.init_db()
conn = database.get_connection()
rows = conn.execute("""
    SELECT id, title, category, description, medium, acquisition_price, provenance, notes, dimensions_notes
    FROM collection_objects
    WHERE title LIKE '%GLUCHOWSKI%' OR title LIKE '%Gluchowski%' OR title LIKE '%gluchowski%'
       OR description LIKE '%Gluchowski%' OR notes LIKE '%Gluchowski%'
       OR title LIKE '%MILITAR%' OR title LIKE '%GENERAL%'
    ORDER BY id
""").fetchall()
print(f"Obiekty Gluchowski / militaria: {len(rows)}")
for r in rows:
    print("---")
    print(f"ID: {r[0]}")
    t = r[1] or "-"
    print(f"Title: {t[:250]}")
    print(f"Category: {r[2]}")
    d = r[3] or "-"
    print(f"Description: {d[:400]}")
    print(f"Medium: {r[4]}")
    print(f"Price: R${r[5]}")
    print(f"Provenance: {r[6]}")
    print(f"Notes: {r[7]}")
    print(f"Dimensions: {r[8]}")

# Also check photos
for r in rows:
    photos = conn.execute("SELECT file_path FROM object_photos WHERE object_id = ?", (r[0],)).fetchall()
    if photos:
        print(f"\nPhotos for ID {r[0]}:")
        for p in photos:
            print(f"  {p[0]}")

conn.close()
