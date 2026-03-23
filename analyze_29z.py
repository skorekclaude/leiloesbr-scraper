#!/usr/bin/env python3
"""Analyze Seria 29z PDFs - count pages, images, extract text structure."""
import sys, os, fitz
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)

files = [
    r"C:\Users\skore\Downloads\Katalog_Gluchowski_Seria_29z.pdf",
    r"C:\Users\skore\Downloads\Katalog_Gluchowski_Seria_29z_ZDJECIA.pdf",
]

for path in files:
    if not os.path.exists(path):
        print(f"BRAK: {path}")
        continue

    doc = fitz.open(path)
    name = os.path.basename(path)
    print(f"\n{'='*70}")
    print(f"PDF: {name}")
    print(f"Stron: {len(doc)}")
    print(f"Rozmiar: {os.path.getsize(path)/1024/1024:.1f} MB")
    print(f"{'='*70}")

    total_images = 0
    for i, page in enumerate(doc):
        images = page.get_images(full=True)
        big_images = [img for img in images if True]  # count all
        total_images += len(big_images)

        text = page.get_text().strip()
        if text:
            lines = [l.strip() for l in text.split('\n') if l.strip()]
            header = ' | '.join(lines[:4])
            print(f"  p{i+1:2d}: {len(big_images):2d} img | {header[:130]}")
        else:
            print(f"  p{i+1:2d}: {len(big_images):2d} img | [brak tekstu]")

    print(f"\nRAZEM: {total_images} obrazow na {len(doc)} stronach")
    doc.close()
