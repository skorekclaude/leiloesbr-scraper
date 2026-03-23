#!/usr/bin/env python3
"""Mapuje strony PDF do rozdzialow - wypisuje naglowki stron."""
import sys, fitz
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)

path = r"C:\Users\skore\Downloads\Kolekcja_Gluchowski_KATALOG_NAUKOWY.pdf"
doc = fitz.open(path)
for i, page in enumerate(doc):
    text = page.get_text().strip()
    if text:
        lines = [l.strip() for l in text.split('\n') if l.strip()]
        header = ' | '.join(lines[:3])
        print(f"Page {i+1:2d}: {header[:150]}")
doc.close()
