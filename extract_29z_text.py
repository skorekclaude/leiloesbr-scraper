#!/usr/bin/env python3
"""Extract full text from Seria 29z PDFs."""
import sys, os, fitz
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)

files = [
    r"C:\Users\skore\Downloads\Katalog_Gluchowski_Seria_29z.pdf",
    r"C:\Users\skore\Downloads\Katalog_Gluchowski_Seria_29z_ZDJECIA.pdf",
]

for path in files:
    if not os.path.exists(path):
        continue
    doc = fitz.open(path)
    name = os.path.basename(path)
    print(f"\n{'='*70}")
    print(f"PELNY TEKST: {name} ({len(doc)} stron)")
    print(f"{'='*70}\n")
    for i, page in enumerate(doc):
        text = page.get_text().strip()
        if text:
            print(f"--- STRONA {i+1} ---")
            print(text)
            print()
    doc.close()
