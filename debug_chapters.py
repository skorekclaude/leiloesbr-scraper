#!/usr/bin/env python3
import sys, os
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import database

database.init_db()
conn = database.get_connection()

rows = conn.execute("""
    SELECT inventory_number
    FROM collection_objects
    WHERE inventory_number LIKE 'GL-%'
    ORDER BY inventory_number
""").fetchall()

print(f"Total in DB: {len(rows)}")
for r in rows:
    print(f"  {r['inventory_number']}")
