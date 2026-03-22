"""
Profesjonalna obróbka zdjęć katalogu Głuchowskich
- Styl: katalog aukcyjny (Christie's / Sotheby's)
- Ciemnoszare tło (#2a2a2a)
- Delikatny cień (drop shadow)
- Auto-crop dokumentu (usunięcie tła stołu/sofy)
- Korekcja kontrastu i ostrości
- Zachowanie oryginałów w backup/
"""

import os
import shutil
from PIL import Image, ImageFilter, ImageEnhance, ImageOps
import numpy as np

SRC_DIR = "docs/gluchowski_img"
BACKUP_DIR = "docs/gluchowski_img/originals_backup"
BG_COLOR = (42, 42, 42)  # #2a2a2a - ciemne tło katalogowe
SHADOW_COLOR = (20, 20, 20)
PADDING = 30  # px padding wokół dokumentu
SHADOW_OFFSET = 8
SHADOW_BLUR = 12
QUALITY = 92


def detect_document_bounds(img):
    """Wykryj granice dokumentu na zdjęciu (auto-crop tła)."""
    arr = np.array(img.convert("L"))
    h, w = arr.shape

    # Próg: piksele jaśniejsze niż tło (dokument jest jasny na ciemnym/szarym tle)
    # Oblicz średnią krawędzi jako przybliżenie koloru tła
    edge_pixels = np.concatenate([
        arr[0, :], arr[-1, :],  # góra i dół
        arr[:, 0], arr[:, -1]   # lewo i prawo
    ])
    bg_mean = np.mean(edge_pixels)
    bg_std = np.std(edge_pixels)

    # Jeśli krawędzie są bardzo jednorodne (np. już obcięte), nie cropuj
    if bg_std < 10 and bg_mean < 80:
        # Tło jest ciemne i jednorodne — prawdopodobnie już przetworzone
        return None

    # Jeśli tło jest jasne (dokument na jasnym stole), próg jest inny
    if bg_mean > 200:
        # Jasne tło — szukaj krawędzi dokumentu po ciemniejszych pikselach ramki/tekstu
        # Tutaj lepiej nie cropować agresywnie, bo dokument jest tego samego koloru co tło
        threshold = bg_mean - 40
        mask = arr < threshold
    elif bg_mean > 120:
        # Średnie tło — dokument może być jaśniejszy lub ciemniejszy
        # Nie cropuj
        return None
    else:
        # Ciemne tło — dokument jest jaśniejszy
        threshold = bg_mean + 3 * max(bg_std, 15)
        mask = arr > threshold

    # Znajdź bounding box pikseli dokumentu
    rows = np.any(mask, axis=1)
    cols = np.any(mask, axis=0)

    if not np.any(rows) or not np.any(cols):
        return None

    rmin, rmax = np.where(rows)[0][[0, -1]]
    cmin, cmax = np.where(cols)[0][[0, -1]]

    # Dodaj mały margines
    margin = 5
    rmin = max(0, rmin - margin)
    rmax = min(h - 1, rmax + margin)
    cmin = max(0, cmin - margin)
    cmax = min(w - 1, cmax + margin)

    # Sprawdź czy crop jest sensowny (co najmniej 50% oryginału)
    crop_area = (rmax - rmin) * (cmax - cmin)
    orig_area = h * w
    if crop_area < 0.3 * orig_area:
        return None  # Za agresywny crop
    if crop_area > 0.95 * orig_area:
        return None  # Prawie nic do cropowania

    return (cmin, rmin, cmax, rmax)


def add_shadow(img, offset=SHADOW_OFFSET, blur_radius=SHADOW_BLUR):
    """Dodaj cień pod dokumentem."""
    w, h = img.size
    # Nowy canvas z miejscem na cień
    canvas_w = w + PADDING * 2 + offset
    canvas_h = h + PADDING * 2 + offset

    # Warstwa cienia
    shadow = Image.new("RGB", (canvas_w, canvas_h), BG_COLOR)

    # Tworzymy maskę cienia — prostokąt w rozmiarze dokumentu
    shadow_layer = Image.new("L", (canvas_w, canvas_h), 0)
    shadow_rect = Image.new("L", (w, h), 80)  # intensywność cienia
    shadow_layer.paste(shadow_rect, (PADDING + offset, PADDING + offset))
    shadow_layer = shadow_layer.filter(ImageFilter.GaussianBlur(blur_radius))

    # Nakładamy cień na tło
    shadow_arr = np.array(shadow)
    shadow_mask_arr = np.array(shadow_layer)
    for c in range(3):
        shadow_arr[:, :, c] = np.clip(
            shadow_arr[:, :, c].astype(float) - shadow_mask_arr.astype(float) * 0.6,
            0, 255
        ).astype(np.uint8)

    result = Image.fromarray(shadow_arr)

    # Nakładamy dokument na warstwę z cieniem
    result.paste(img, (PADDING, PADDING))

    return result


def enhance_document(img):
    """Korekcja kontrastu i ostrości dokumentu."""
    # Delikatna poprawa kontrastu
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(1.15)

    # Lekkie wyostrzenie tekstu
    enhancer = ImageEnhance.Sharpness(img)
    img = enhancer.enhance(1.3)

    # Delikatna poprawa jasności (dokumenty bywają ciemne)
    enhancer = ImageEnhance.Brightness(img)
    img = enhancer.enhance(1.05)

    return img


def process_image(filepath):
    """Przetwórz jedno zdjęcie w styl katalogowy."""
    img = Image.open(filepath)

    # 1. Auto-crop (wykryj i przytnij tło)
    bounds = detect_document_bounds(img)
    if bounds:
        img = img.crop(bounds)

    # 2. Korekcja kolorów i ostrości
    img = enhance_document(img)

    # 3. Dodaj ciemne tło + cień
    result = add_shadow(img)

    return result


def main():
    # Utwórz backup
    os.makedirs(BACKUP_DIR, exist_ok=True)

    files = [f for f in os.listdir(SRC_DIR)
             if f.endswith('.jpeg') and os.path.isfile(os.path.join(SRC_DIR, f))]
    files.sort()

    print(f"Przetwarzam {len(files)} zdjęć...")
    print(f"Backup → {BACKUP_DIR}/")
    print(f"Styl: katalog aukcyjny, tło #{BG_COLOR[0]:02x}{BG_COLOR[1]:02x}{BG_COLOR[2]:02x}")
    print()

    processed = 0
    skipped = 0
    errors = 0

    for i, fname in enumerate(files, 1):
        src = os.path.join(SRC_DIR, fname)
        bak = os.path.join(BACKUP_DIR, fname)

        try:
            # Backup (tylko jeśli nie istnieje)
            if not os.path.exists(bak):
                shutil.copy2(src, bak)

            # Przetwarzanie
            result = process_image(src)
            result.save(src, "JPEG", quality=QUALITY, optimize=True)

            processed += 1
            if i % 20 == 0 or i == len(files):
                print(f"  [{i}/{len(files)}] {fname} ✓")

        except Exception as e:
            errors += 1
            print(f"  [{i}/{len(files)}] {fname} ✗ {e}")

    print()
    print(f"Gotowe: {processed} przetworzonych, {skipped} pominiętych, {errors} błędów")
    print(f"Oryginały w: {BACKUP_DIR}/")


if __name__ == "__main__":
    main()
