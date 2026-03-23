"""Fix rotation of document images in gluchowski_img/ — v2"""

from PIL import Image
import os

IMG_DIR = r"C:\Users\skore\leiloesbr-scraper\docs\gluchowski_img"

ROTATE_180 = [
    "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p04_img01.jpeg",
    "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p06_img01.jpeg",
    "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p06_img02.jpeg",
    "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p09_img01.jpeg",
    "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p13_img01.jpeg",
    "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p13_img02.jpeg",
    "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p13_img03.jpeg",
    "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p14_img01.jpeg",
    "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p14_img02.jpeg",
    "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p14_img03.jpeg",
    "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p23_img01.jpeg",
    "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p23_img02.jpeg",
    "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p23_img03.jpeg",
    "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p23_img04.jpeg",
    "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p24_img01.jpeg",
    "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p24_img02.jpeg",
    "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p26_img01.jpeg",
    "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p26_img02.jpeg",
    "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p27_img01.jpeg",
    "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p27_img02.jpeg",
    "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p28_img01.jpeg",
    "Kolekcja_Gluchowski_Katalog_Tematyczny_p05_img03.jpeg",
    "Kolekcja_Gluchowski_Katalog_Tematyczny_p13_img01.jpeg",
    "Kolekcja_Gluchowski_Katalog_Tematyczny_p13_img02.jpeg",
    "Seria_29z_p03_img01.jpeg",
    "Seria_29z_p05_img01.jpeg",
    "Seria_29z_p10_img01.jpeg",
    "Seria_29z_p15_img02.jpeg",
    "Seria_29z_p20_img01.jpeg",
]

ROTATE_90CW = [
    "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p17_img02.jpeg",
    "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p17_img03.jpeg",
    "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p25_img01.jpeg",
    "Seria_29z_p02_img01.jpeg",
    "Seria_29z_p04_img01.jpeg",
    "Seria_29z_p04_img02.jpeg",
    "Seria_29z_p05_img02.jpeg",
    "Seria_29z_p06_img01.jpeg",
    "Seria_29z_p06_img02.jpeg",
    "Seria_29z_p07_img01.jpeg",
    "Seria_29z_p08_img01.jpeg",
    "Seria_29z_p08_img02.jpeg",
    "Seria_29z_p09_img01.jpeg",
    "Seria_29z_p10_img02.jpeg",
    "Seria_29z_p11_img01.jpeg",
    "Seria_29z_p11_img02.jpeg",
    "Seria_29z_p12_img01.jpeg",
    "Seria_29z_p12_img02.jpeg",
    "Seria_29z_p13_img01.jpeg",
    "Seria_29z_p13_img02.jpeg",
    "Seria_29z_p13_img03.jpeg",
    "Seria_29z_p13_img04.jpeg",
    "Seria_29z_p14_img01.jpeg",
    "Seria_29z_p14_img02.jpeg",
    "Seria_29z_p14_img03.jpeg",
    "Seria_29z_p15_img01.jpeg",
    "Seria_29z_p15_img03.jpeg",
    "Seria_29z_p16_img01.jpeg",
    "Seria_29z_p16_img02.jpeg",
    "Seria_29z_p17_img01.jpeg",
    "Seria_29z_p18_img01.jpeg",
    "Seria_29z_p18_img02.jpeg",
    "Seria_29z_p19_img01.jpeg",
    "Seria_29z_p19_img02.jpeg",
    "Seria_29z_p21_img01.jpeg",
    "Seria_29z_p22_img01.jpeg",
    "Seria_29z_p22_img02.jpeg",
    "Seria_29z_p23_img01.jpeg",
    "Seria_29z_p23_img02.jpeg",
    "Seria_29z_p24_img01.jpeg",
    "Seria_29z_p25_img01.jpeg",
    "Seria_29z_p26_img01.jpeg",
    "Seria_29z_p27_img01.jpeg",
    "Seria_29z_p28_img01.jpeg",
    "Seria_29z_p28_img02.jpeg",
    "Seria_29z_p29_img01.jpeg",
    "Seria_29z_p29_img02.jpeg",
    "Seria_29z_p30_img01.jpeg",
    "Seria_29z_p31_img01.jpeg",
    "Seria_29z_p32_img01.jpeg",
    "Seria_29z_p32_img02.jpeg",
    "Seria_29z_p32_img03.jpeg",
    "Seria_29z_p32_img04.jpeg",
    "Seria_29z_p32_img05.jpeg",
    "Seria_29z_p33_img01.jpeg",
    "Seria_29z_p34_img01.jpeg",
    "Seria_29z_p35_img01.jpeg",
    "Seria_29z_p36_img01.jpeg",
    "Seria_29z_p37_img01.jpeg",
]


def rotate_file(filepath, transpose_method, label):
    try:
        img = Image.open(filepath)
        rotated = img.transpose(transpose_method)
        rotated.save(filepath, quality=95)
        img.close()
        rotated.close()
        return True, None
    except Exception as e:
        return False, str(e)


ok_count = 0
err_count = 0
missing_count = 0
errors = []

# 180 degree
for fname in ROTATE_180:
    fpath = os.path.join(IMG_DIR, fname)
    if not os.path.exists(fpath):
        print(f"MISSING: {fname}")
        missing_count += 1
        continue
    success, err = rotate_file(fpath, Image.Transpose.ROTATE_180, "180")
    if success:
        ok_count += 1
    else:
        err_count += 1
        errors.append((fname, err))
        print(f"ERROR: {fname} — {err}")

# 90cw (ROTATE_270)
for fname in ROTATE_90CW:
    fpath = os.path.join(IMG_DIR, fname)
    if not os.path.exists(fpath):
        print(f"MISSING: {fname}")
        missing_count += 1
        continue
    success, err = rotate_file(fpath, Image.Transpose.ROTATE_270, "90cw")
    if success:
        ok_count += 1
    else:
        err_count += 1
        errors.append((fname, err))
        print(f"ERROR: {fname} — {err}")

total = len(ROTATE_180) + len(ROTATE_90CW)
print(f"\n=== SUMMARY ===")
print(f"Total files listed: {total}")
print(f"  180 degree: {len(ROTATE_180)}")
print(f"  90cw:       {len(ROTATE_90CW)}")
print(f"Rotated OK:   {ok_count}")
print(f"Missing:      {missing_count}")
print(f"Errors:       {err_count}")
if errors:
    for fname, err in errors:
        print(f"  - {fname}: {err}")
print("Done.")
