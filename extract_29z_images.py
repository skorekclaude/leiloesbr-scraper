#!/usr/bin/env python3
"""Extract images from Seria 29z ZDJECIA PDF."""
import sys, os, fitz
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)

output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "docs", "gluchowski_img")
os.makedirs(output_dir, exist_ok=True)

path = r"C:\Users\skore\Downloads\Katalog_Gluchowski_Seria_29z_ZDJECIA.pdf"
doc = fitz.open(path)
print(f"PDF: {os.path.basename(path)} ({len(doc)} stron)")

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
                if w < 50 or h < 50:
                    continue
                if len(img_bytes) < 5000:
                    continue
                filename = f"Seria_29z_p{page_num+1:02d}_img{img_idx+1:02d}.{ext}"
                filepath = os.path.join(output_dir, filename)
                with open(filepath, "wb") as f:
                    f.write(img_bytes)
                size_kb = len(img_bytes) / 1024
                print(f"  p{page_num+1:2d} | {filename} | {w}x{h} | {size_kb:.0f}KB")
                img_count += 1
        except Exception as e:
            print(f"  p{page_num+1:2d} | ERROR: {e}")

doc.close()
print(f"\nWyciagnieto {img_count} zdjec do {output_dir}")
