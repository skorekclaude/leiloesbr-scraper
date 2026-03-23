import sys, os
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import database
database.init_db()
conn = database.get_connection()
conn.execute("DELETE FROM collection_objects WHERE inventory_number LIKE 'GL-%'")
conn.commit()
print("Deleted all GL objects")
conn.close()
