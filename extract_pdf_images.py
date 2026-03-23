#!/usr/bin/env python3
"""
Wyciaga zdjecia z PDF-ow katalogow Gluchowskich.
"""
import sys, os, fitz
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)

output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images", "gluchowski")
os.makedirs(output_dir, exist_ok=True)

files = [
    r"C:\Users\skore\Downloads\Kolekcja_Gluchowski_KATALOG_NAUKOWY.pdf",
    r"C:\Users\skore\Downloads\Kolekcja_Gluchowski_Katalog_Tematyczny.pdf",
]

total = 0
for path in files:
    if not os.path.exists(path):
        print(f"SKIP - nie znaleziono: {path}")
        continue

    doc = fitz.open(path)
    pdf_name = os.path.splitext(os.path.basename(path))[0]
    print(f"\n{'='*60}")
    print(f"PDF: {pdf_name} ({len(doc)} stron)")
    print(f"{'='*60}")

    img_count = 0
    for page_num in range(len(doc)):
        page = doc[page_num]
        images = page.get_images(full=True)

        for img_idx, img_info in enumerate(images):
            xref = img_info[0]
            try:
                base_image = doc.extract_image(xref)
                if base_image:
                    ext = base_image["ext"]
                    img_bytes = base_image["image"]
                    w = base_image.get("width", 0)
                    h = base_image.get("height", 0)

                    # Pomijaj male ikony i artefakty
                    if w < 50 or h < 50:
                        continue
                    if len(img_bytes) < 5000:  # < 5KB = prawdopodobnie ikona
                        continue

                    filename = f"{pdf_name}_p{page_num+1:02d}_img{img_idx+1:02d}.{ext}"
                    filepath = os.path.join(output_dir, filename)

                    with open(filepath, "wb") as f:
                        f.write(img_bytes)

                    size_kb = len(img_bytes) / 1024
                    print(f"  Page {page_num+1:2d} | {filename} | {w}x{h} | {size_kb:.0f}KB")
                    img_count += 1
            except Exception as e:
                print(f"  Page {page_num+1:2d} | ERROR: {e}")

    doc.close()
    print(f"\nWyciagnieto {img_count} zdjec z {pdf_name}")
    total += img_count

print(f"\n{'='*60}")
print(f"RAZEM: {total} zdjec w {output_dir}")
print(f"{'='*60}")
