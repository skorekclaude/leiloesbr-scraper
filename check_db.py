import sys, os
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)
import database
database.init_db()
conn = database.get_connection()
print("Total objects:", conn.execute("SELECT COUNT(*) FROM collection_objects").fetchone()[0])
print("Total artists:", conn.execute("SELECT COUNT(*) FROM artists").fetchone()[0])
rows = conn.execute("SELECT category, COUNT(*) as c FROM collection_objects GROUP BY category ORDER BY c DESC").fetchall()
print("Categories:")
for r in rows:
    print(f"  {r[0]}: {r[1]}")
print("\nSample objects:")
for r in conn.execute("SELECT id, title, artist_name_display, category, acquisition_price FROM collection_objects LIMIT 10").fetchall():
    print(f"  [{r[0]}] {r[1]} | {r[2]} | {r[3]} | R${r[4]}")
print("\nColumns in collection_objects:")
for r in conn.execute("PRAGMA table_info(collection_objects)").fetchall():
    print(f"  {r[1]} ({r[2]})")
conn.close()
