import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import fitz

pdf_path = r"C:\Users\skore\Downloads\Kolekcja_Gluchowski_Katalog_Tematyczny.pdf"
doc = fitz.open(pdf_path)

for page_num in range(len(doc)):
    page = doc[page_num]
    text = page.get_text()
    print(f"=== PAGE {page_num + 1} ===")
    print(text)
    print()

print(f"=== TOTAL PAGES: {len(doc)} ===")
doc.close()
