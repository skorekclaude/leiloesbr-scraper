#!/usr/bin/env python3
"""Extract text from TRANSKRYPT ROZMOWY PDF."""
import sys, os, fitz
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)

path = r"C:\Users\skore\Downloads\Kolekcja_Gluchowski_TRANSKRYPT_ROZMOWY.pdf"
doc = fitz.open(path)
print(f"PDF: {os.path.basename(path)} ({len(doc)} stron)")
print("=" * 80)

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "transkrypt_text.txt")
with open(out_path, "w", encoding="utf-8") as f:
    for page_num in range(len(doc)):
        text = doc[page_num].get_text()
        header = f"\n--- STRONA {page_num+1} ---\n"
        print(header)
        print(text[:500])
        if len(text) > 500:
            print(f"  ... ({len(text)} znakow)")
        f.write(header)
        f.write(text)
        f.write("\n")

doc.close()
print(f"\nZapisano pelny tekst do: {out_path}")
