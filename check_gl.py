import sys, os
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import database
database.init_db()
conn = database.get_connection()
rows = conn.execute("SELECT inventory_number, title, description FROM collection_objects WHERE inventory_number LIKE 'GL-%' ORDER BY inventory_number").fetchall()
print(f"Obiekty GL: {len(rows)}\n")
for r in rows:
    desc = (r[2] or "")[:200]
    print(f"[{r[0]}] {r[1]}")
    print(f"  {desc}...")
    print()
conn.close()
