"""
Profesjonalny crop dokumentów — V2 z AI background removal (rembg).
Usuwa CAŁE tło: sofę, szkło, odbicia. Zostawia sam dokument na białym tle.
"""

import cv2
import numpy as np
import sys
from pathlib import Path
from PIL import Image
from rembg import remove, new_session
import io

INPUT_DIR = Path("juras_img")
OUTPUT_DIR = Path("juras_img_clean")
DOCS_IMG_DIR = Path("docs/gluchowski_img")

MARGIN = 20  # biała ramka wokół dokumentu

def remove_background(img_path: Path) -> Image.Image | None:
    """Usuń tło za pomocą rembg (U2-Net AI model)."""
    with open(img_path, "rb") as f:
        input_data = f.read()

    # rembg zwraca PNG z przezroczystym tłem
    output_data = remove(input_data)

    # Otwórz jako RGBA
    img_rgba = Image.open(io.BytesIO(output_data)).convert("RGBA")

    return img_rgba


def rgba_to_white_bg(img_rgba: Image.Image) -> Image.Image:
    """Zamień przezroczyste tło na białe."""
    # Stwórz białe tło
    white = Image.new("RGBA", img_rgba.size, (255, 255, 255, 255))
    # Złóż dokument na białym tle
    composite = Image.alpha_composite(white, img_rgba)
    return composite.convert("RGB")


def crop_to_content(img: Image.Image, threshold=240) -> Image.Image:
    """Przytnij do zawartości (usuń białe marginesy)."""
    arr = np.array(img)

    # Maska: piksele które NIE są białe
    gray = cv2.cvtColor(arr, cv2.COLOR_RGB2GRAY)
    mask = gray < threshold

    # Znajdź bounding box zawartości
    coords = np.argwhere(mask)
    if len(coords) < 100:  # Za mało pikseli = coś poszło nie tak
        return img

    y0, x0 = coords.min(axis=0)
    y1, x1 = coords.max(axis=0)

    # Dodaj margines
    h, w = arr.shape[:2]
    y0 = max(0, y0 - MARGIN)
    x0 = max(0, x0 - MARGIN)
    y1 = min(h, y1 + MARGIN)
    x1 = min(w, x1 + MARGIN)

    return img.crop((x0, y0, x1, y1))


def enhance_document(img: Image.Image) -> Image.Image:
    """Lekki boost kontrastu i ostrości."""
    arr = np.array(img)

    # CLAHE na kanale L (LAB)
    lab = cv2.cvtColor(arr, cv2.COLOR_RGB2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=1.5, tileGridSize=(8, 8))
    l = clahe.apply(l)
    lab = cv2.merge([l, a, b])
    result = cv2.cvtColor(lab, cv2.COLOR_LAB2RGB)

    return Image.fromarray(result)


def process_image(input_path: Path, output_path: Path) -> bool:
    """Przetwórz jeden obraz: AI background removal → białe tło → crop → enhance."""
    try:
        # 1. AI background removal
        img_rgba = remove_background(input_path)
        if img_rgba is None:
            print(f"  BŁĄD: rembg nie zadziałał dla {input_path}")
            return False

        # 2. Białe tło zamiast przezroczystego
        img_white = rgba_to_white_bg(img_rgba)

        # 3. Przytnij do zawartości (usuń nadmiar białego)
        img_cropped = crop_to_content(img_white)

        # 4. Lekki enhance
        img_final = enhance_document(img_cropped)

        # 5. Zapisz
        img_final.save(str(output_path), "PNG", optimize=True)
        return True

    except Exception as e:
        print(f"  BŁĄD: {input_path.name}: {e}")
        return False


def main():
    OUTPUT_DIR.mkdir(exist_ok=True)

    files = sorted(INPUT_DIR.glob("juras_*.png"))
    total = len(files)
    success = 0

    print(f"🎨 Przetwarzam {total} zdjęć dokumentów (AI background removal)...")
    print(f"   Input:  {INPUT_DIR}/")
    print(f"   Output: {OUTPUT_DIR}/")
    print(f"   Model: U2-Net (rembg)")
    print("-" * 60)

    # Inicjalizacja modelu (pobierze przy pierwszym użyciu)
    print("Ładuję model AI... (przy pierwszym uruchomieniu pobierze ~170MB)")

    for i, fpath in enumerate(files, 1):
        outpath = OUTPUT_DIR / fpath.name

        ok = process_image(fpath, outpath)
        if ok:
            success += 1
            # Porównaj rozmiary
            orig_size = fpath.stat().st_size
            new_size = outpath.stat().st_size
            ratio = new_size / orig_size * 100
            print(f"[{i:3d}/{total}] ✓ {fpath.name} ({ratio:.0f}% oryginalnego rozmiaru)")
        else:
            print(f"[{i:3d}/{total}] ✗ {fpath.name}")

    print("-" * 60)
    print(f"Gotowe: {success}/{total} zdjęć przetworzonych")

    # Kopiuj do docs/gluchowski_img/
    print(f"\nKopiuję oczyszczone zdjęcia do {DOCS_IMG_DIR}/...")
    import shutil
    copied = 0
    for fpath in OUTPUT_DIR.glob("juras_*.png"):
        dst = DOCS_IMG_DIR / fpath.name
        if dst.exists() or True:  # nadpisz wszystkie
            shutil.copy2(str(fpath), str(dst))
            copied += 1
    print(f"Skopiowano {copied} plików do katalogu docs/")


if __name__ == "__main__":
    main()
