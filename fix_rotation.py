"""Fix rotation of document images in gluchowski_img/"""
from PIL import Image
import os

IMG_DIR = os.path.join("docs", "gluchowski_img")

# Rotation map based on visual inspection
# 90cw = rotate 90° clockwise (PIL: transpose ROTATE_270)
# 90ccw = rotate 90° counter-clockwise (PIL: transpose ROTATE_90)
# 180 = rotate 180° (PIL: transpose ROTATE_180)
ROTATIONS = {
    # Tematyczny images
    "Kolekcja_Gluchowski_Katalog_Tematyczny_p02_img02.jpeg": "90cw",
    "Kolekcja_Gluchowski_Katalog_Tematyczny_p02_img03.jpeg": "90cw",
    "Kolekcja_Gluchowski_Katalog_Tematyczny_p03_img01.jpeg": "90cw",
    "Kolekcja_Gluchowski_Katalog_Tematyczny_p03_img02.jpeg": "90cw",
    "Kolekcja_Gluchowski_Katalog_Tematyczny_p04_img01.jpeg": "90cw",
    "Kolekcja_Gluchowski_Katalog_Tematyczny_p04_img02.jpeg": "90cw",
    "Kolekcja_Gluchowski_Katalog_Tematyczny_p05_img01.jpeg": "90cw",
    "Kolekcja_Gluchowski_Katalog_Tematyczny_p05_img02.jpeg": "90cw",
    "Kolekcja_Gluchowski_Katalog_Tematyczny_p05_img03.jpeg": "90ccw",
    "Kolekcja_Gluchowski_Katalog_Tematyczny_p05_img04.jpeg": "90cw",
    "Kolekcja_Gluchowski_Katalog_Tematyczny_p05_img05.jpeg": "90cw",
    "Kolekcja_Gluchowski_Katalog_Tematyczny_p06_img01.jpeg": "90cw",
    "Kolekcja_Gluchowski_Katalog_Tematyczny_p06_img02.jpeg": "90cw",
    "Kolekcja_Gluchowski_Katalog_Tematyczny_p07_img01.jpeg": "90cw",
    "Kolekcja_Gluchowski_Katalog_Tematyczny_p07_img02.jpeg": "90cw",
    "Kolekcja_Gluchowski_Katalog_Tematyczny_p08_img01.jpeg": "90cw",
    "Kolekcja_Gluchowski_Katalog_Tematyczny_p08_img02.jpeg": "90cw",
    "Kolekcja_Gluchowski_Katalog_Tematyczny_p09_img01.jpeg": "180",
    "Kolekcja_Gluchowski_Katalog_Tematyczny_p09_img02.jpeg": "180",
    "Kolekcja_Gluchowski_Katalog_Tematyczny_p10_img01.jpeg": "90cw",
    "Kolekcja_Gluchowski_Katalog_Tematyczny_p11_img01.jpeg": "90cw",
    "Kolekcja_Gluchowski_Katalog_Tematyczny_p12_img01.jpeg": "90cw",
    "Kolekcja_Gluchowski_Katalog_Tematyczny_p12_img03.jpeg": "90cw",
    "Kolekcja_Gluchowski_Katalog_Tematyczny_p13_img01.jpeg": "90ccw",
    "Kolekcja_Gluchowski_Katalog_Tematyczny_p13_img02.jpeg": "90ccw",
    "Kolekcja_Gluchowski_Katalog_Tematyczny_p13_img03.jpeg": "90cw",
    "Kolekcja_Gluchowski_Katalog_Tematyczny_p14_img01.jpeg": "90cw",
    "Kolekcja_Gluchowski_Katalog_Tematyczny_p15_img01.jpeg": "90cw",
    "Kolekcja_Gluchowski_Katalog_Tematyczny_p15_img02.jpeg": "90cw",
    "Kolekcja_Gluchowski_Katalog_Tematyczny_p15_img03.jpeg": "90cw",
    # Naukowy images
    "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p04_img01.jpeg": "90ccw",
    "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p06_img01.jpeg": "90ccw",
    "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p06_img02.jpeg": "90ccw",
    "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p09_img01.jpeg": "90ccw",
    "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p13_img01.jpeg": "90ccw",
    "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p13_img02.jpeg": "90ccw",
    "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p13_img03.jpeg": "90ccw",
    "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p14_img01.jpeg": "90ccw",
    "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p14_img02.jpeg": "90ccw",
    # Seria 29z
    "Seria_29z_p03_img01.jpeg": "90ccw",
    "Seria_29z_p05_img01.jpeg": "90ccw",
    "Seria_29z_p10_img01.jpeg": "90ccw",
    "Seria_29z_p15_img01.jpeg": "90ccw",
    "Seria_29z_p20_img01.jpeg": "90ccw",
}

PIL_ROTATIONS = {
    "90cw": Image.Transpose.ROTATE_270,
    "90ccw": Image.Transpose.ROTATE_90,
    "180": Image.Transpose.ROTATE_180,
}

fixed = 0
errors = 0

for fname, direction in ROTATIONS.items():
    path = os.path.join(IMG_DIR, fname)
    if not os.path.exists(path):
        # Check in cropped/ subfolder
        path = os.path.join(IMG_DIR, "cropped", fname)
        if not os.path.exists(path):
            print(f"SKIP (not found): {fname}")
            continue

    try:
        img = Image.open(path)
        rotated = img.transpose(PIL_ROTATIONS[direction])
        rotated.save(path, quality=90)
        fixed += 1
        print(f"FIXED ({direction}): {fname}")
    except Exception as e:
        print(f"ERROR: {fname} — {e}")
        errors += 1

print(f"\nDone: {fixed} fixed, {errors} errors, {len(ROTATIONS)} total")
