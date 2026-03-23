#!/usr/bin/env python3
import sys, sqlite3
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)
conn = sqlite3.connect('leiloes.db')
cur = conn.cursor()
# List all tables
cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cur.fetchall()
print(f"Tables: {[t[0] for t in tables]}")
for t in tables:
    tname = t[0]
    cur.execute(f"SELECT COUNT(*) FROM [{tname}]")
    cnt = cur.fetchone()[0]
    if cnt > 0:
        print(f"  {tname}: {cnt} rows")
        cur.execute(f"SELECT * FROM [{tname}] LIMIT 1")
        cols = [d[0] for d in cur.description]
        print(f"    cols: {cols}")
        # Check for GL- entries
        for col in cols:
            try:
                cur.execute(f"SELECT COUNT(*) FROM [{tname}] WHERE [{col}] LIKE 'GL-%'")
                gc = cur.fetchone()[0]
                if gc > 0:
                    print(f"    -> {col} has {gc} GL- entries")
            except:
                pass
conn.close()
