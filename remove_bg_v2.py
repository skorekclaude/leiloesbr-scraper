"""Remove blue sofa/fabric backgrounds from document images using rembg."""

from pathlib import Path
from PIL import Image
from rembg import remove
import time

IMG_DIR = Path(r"C:\Users\skore\leiloesbr-scraper\docs\gluchowski_img")

FILES = [
    "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p25_img01.jpeg",
    "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p28_img02.jpeg",
    "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p28_img03.jpeg",
    "Kolekcja_Gluchowski_Katalog_Tematyczny_p05_img04.jpeg",
    "Seria_29z_p07_img02.jpeg",
    "Seria_29z_p20_img02.jpeg",
    "Seria_29z_p22_img01.jpeg",
    "Seria_29z_p22_img02.jpeg",
    "Seria_29z_p23_img01.jpeg",
    "Seria_29z_p23_img02.jpeg",
    "Seria_29z_p35_img01.jpeg",
    "Seria_29z_p36_img01.jpeg",
]

def process_image(filepath: Path) -> bool:
    """Remove background, composite on white, save as JPEG quality=90."""
    img = Image.open(filepath).convert("RGB")
    # rembg returns RGBA with transparent background
    rgba = remove(img)
    # Create white background and composite
    white_bg = Image.new("RGBA", rgba.size, (255, 255, 255, 255))
    composite = Image.alpha_composite(white_bg, rgba)
    # Convert to RGB and save as JPEG
    composite.convert("RGB").save(filepath, "JPEG", quality=90)
    return True

def main():
    print(f"Processing {len(FILES)} images from {IMG_DIR}\n")
    success = 0
    failed = 0
    t0 = time.time()

    for i, fname in enumerate(FILES, 1):
        fpath = IMG_DIR / fname
        if not fpath.exists():
            print(f"[{i:2d}/{len(FILES)}] MISSING: {fname}")
            failed += 1
            continue
        try:
            t1 = time.time()
            process_image(fpath)
            elapsed = time.time() - t1
            print(f"[{i:2d}/{len(FILES)}] OK ({elapsed:.1f}s): {fname}")
            success += 1
        except Exception as e:
            print(f"[{i:2d}/{len(FILES)}] FAILED: {fname} — {e}")
            failed += 1

    total_time = time.time() - t0
    print(f"\nDone in {total_time:.1f}s — {success} success, {failed} failed")

if __name__ == "__main__":
    main()
