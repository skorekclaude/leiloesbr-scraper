import sys, fitz
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)

files = [
    r"C:\Users\skore\Downloads\Kolekcja_Gluchowski_KATALOG_NAUKOWY.pdf",
    r"C:\Users\skore\Downloads\Kolekcja_Gluchowski_Katalog_Tematyczny.pdf",
]

for path in files:
    doc = fitz.open(path)
    print(f"\n{'='*80}")
    print(f"FILE: {path}")
    print(f"Pages: {len(doc)}")
    print(f"{'='*80}")
    for i, page in enumerate(doc):
        if i >= 20:  # limit to 20 pages
            print(f"\n... (truncated, {len(doc)} pages total)")
            break
        text = page.get_text()
        if text.strip():
            print(f"\n--- Page {i+1} ---")
            print(text[:3000])
    doc.close()
