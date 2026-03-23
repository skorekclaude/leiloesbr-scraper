"""
Profesjonalny crop dokumentów z kolekcji Głuchowskiego.
Usuwa tło (sofę/podkładkę), wykrywa krawędzie dokumentu,
prostuje perspektywę, daje czyste białe tło.
"""

import cv2
import numpy as np
import os
import sys
from pathlib import Path

INPUT_DIR = Path("juras_img")
OUTPUT_DIR = Path("juras_img_clean")
DOCS_IMG_DIR = Path("docs/gluchowski_img")

# Margines wokół dokumentu (piksele)
MARGIN = 15
# Minimalny % powierzchni obrazu, który musi zajmować znaleziony kontur
MIN_AREA_RATIO = 0.10
# Maksymalny % powierzchni (żeby nie brać całego obrazu)
MAX_AREA_RATIO = 0.98

def order_points(pts):
    """Uporządkuj 4 punkty: top-left, top-right, bottom-right, bottom-left."""
    rect = np.zeros((4, 2), dtype="float32")
    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)]      # top-left
    rect[2] = pts[np.argmax(s)]      # bottom-right
    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]   # top-right
    rect[3] = pts[np.argmax(diff)]   # bottom-left
    return rect

def four_point_transform(image, pts):
    """Perspektywiczna transformacja do prostokąta."""
    rect = order_points(pts)
    (tl, tr, br, bl) = rect

    widthA = np.linalg.norm(br - bl)
    widthB = np.linalg.norm(tr - tl)
    maxWidth = max(int(widthA), int(widthB))

    heightA = np.linalg.norm(tr - br)
    heightB = np.linalg.norm(tl - bl)
    maxHeight = max(int(heightA), int(heightB))

    dst = np.array([
        [0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]
    ], dtype="float32")

    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight),
                                  borderMode=cv2.BORDER_CONSTANT,
                                  borderValue=(255, 255, 255))
    return warped

def find_document_contour(image):
    """Znajdź kontur dokumentu na zdjęciu."""
    h, w = image.shape[:2]
    total_area = h * w

    # Konwersja do skali szarości
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Rozmycie Gaussa żeby usunąć szum
    blurred = cv2.GaussianBlur(gray, (7, 7), 0)

    # --- Metoda 1: Detekcja krawędzi Canny ---
    edges = cv2.Canny(blurred, 30, 100)

    # Dylatacja żeby zamknąć przerwy w krawędziach
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    edges = cv2.dilate(edges, kernel, iterations=2)

    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    best_contour = None
    best_area = 0

    for contour in sorted(contours, key=cv2.contourArea, reverse=True)[:10]:
        area = cv2.contourArea(contour)
        if area < total_area * MIN_AREA_RATIO:
            continue
        if area > total_area * MAX_AREA_RATIO:
            continue

        peri = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.02 * peri, True)

        if len(approx) == 4 and area > best_area:
            best_contour = approx
            best_area = area

    if best_contour is not None:
        return best_contour.reshape(4, 2)

    # --- Metoda 2: Threshold adaptacyjny ---
    # Często lepszy dla dokumentów na jasnym tle
    thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                    cv2.THRESH_BINARY_INV, 11, 2)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 9))
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=3)

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in sorted(contours, key=cv2.contourArea, reverse=True)[:5]:
        area = cv2.contourArea(contour)
        if area < total_area * MIN_AREA_RATIO or area > total_area * MAX_AREA_RATIO:
            continue

        peri = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.02 * peri, True)

        if len(approx) == 4:
            return approx.reshape(4, 2)

    # --- Metoda 3: Fallback - bounding rect największego konturu ---
    if contours:
        largest = max(contours, key=cv2.contourArea)
        area = cv2.contourArea(largest)
        if area > total_area * MIN_AREA_RATIO:
            x, y, cw, ch = cv2.boundingRect(largest)
            return np.array([[x, y], [x+cw, y], [x+cw, y+ch], [x, y+ch]], dtype="float32")

    return None

def crop_with_color_mask(image):
    """
    Alternatywna metoda: maskuj tło po kolorze (beż/błękit sofy).
    Używana gdy detekcja konturów zawiedzie.
    """
    h, w = image.shape[:2]
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Maska na jasne/beżowe tło (sofa)
    # HSV: H=0-30 (beż/żółty), S=10-80 (lekko nasycony), V=150-255 (jasny)
    lower_beige = np.array([0, 10, 140])
    upper_beige = np.array([35, 100, 255])
    mask_beige = cv2.inRange(hsv, lower_beige, upper_beige)

    # Maska na błękitne tło
    lower_blue = np.array([90, 20, 100])
    upper_blue = np.array([130, 100, 255])
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)

    # Połącz maski tła
    bg_mask = cv2.bitwise_or(mask_beige, mask_blue)

    # Inwersja = maska dokumentu
    doc_mask = cv2.bitwise_not(bg_mask)

    # Morphologia - wyczyść
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 15))
    doc_mask = cv2.morphologyEx(doc_mask, cv2.MORPH_CLOSE, kernel, iterations=3)
    doc_mask = cv2.morphologyEx(doc_mask, cv2.MORPH_OPEN, kernel, iterations=1)

    # Znajdź bounding rect
    contours, _ = cv2.findContours(doc_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        largest = max(contours, key=cv2.contourArea)
        if cv2.contourArea(largest) > h * w * MIN_AREA_RATIO:
            x, y, cw, ch = cv2.boundingRect(largest)
            return image[y:y+ch, x:x+cw]

    return None

def add_white_border(image, border=MARGIN):
    """Dodaj białą ramkę wokół dokumentu."""
    return cv2.copyMakeBorder(image, border, border, border, border,
                               cv2.BORDER_CONSTANT, value=(255, 255, 255))

def enhance_document(image):
    """Lekkie wzmocnienie kontrastu dokumentu."""
    # CLAHE na kanale L (LAB colorspace)
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=1.5, tileGridSize=(8, 8))
    l = clahe.apply(l)
    lab = cv2.merge([l, a, b])
    return cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)

def process_image(input_path, output_path):
    """Przetwórz jeden obraz: wykryj dokument, wytnij, wyprostuj."""
    image = cv2.imread(str(input_path))
    if image is None:
        print(f"  BŁĄD: Nie mogę wczytać {input_path}")
        return False

    h, w = image.shape[:2]
    original = image.copy()

    # Próba 1: Detekcja konturu 4-punktowego
    contour = find_document_contour(image)

    if contour is not None:
        # Sprawdź czy kontur ma sensowny kształt (nie za wąski/szeroki)
        rect = order_points(contour.astype("float32"))
        widthA = np.linalg.norm(rect[2] - rect[3])
        widthB = np.linalg.norm(rect[1] - rect[0])
        heightA = np.linalg.norm(rect[1] - rect[2])
        heightB = np.linalg.norm(rect[0] - rect[3])
        avg_w = (widthA + widthB) / 2
        avg_h = (heightA + heightB) / 2

        aspect = max(avg_w, avg_h) / max(min(avg_w, avg_h), 1)

        if aspect < 5:  # Sensowny stosunek boków (nie cienki pasek)
            result = four_point_transform(original, contour.astype("float32"))
            result = enhance_document(result)
            result = add_white_border(result)
            cv2.imwrite(str(output_path), result, [cv2.IMWRITE_PNG_COMPRESSION, 6])
            return True

    # Próba 2: Crop po kolorze
    result = crop_with_color_mask(original)
    if result is not None:
        rh, rw = result.shape[:2]
        if rh > 100 and rw > 100:  # Sensowny rozmiar
            result = enhance_document(result)
            result = add_white_border(result)
            cv2.imwrite(str(output_path), result, [cv2.IMWRITE_PNG_COMPRESSION, 6])
            return True

    # Próba 3: Proste przycięcie marginesów (5% z każdej strony)
    margin_y = int(h * 0.04)
    margin_x = int(w * 0.04)
    result = original[margin_y:h-margin_y, margin_x:w-margin_x]
    result = enhance_document(result)
    result = add_white_border(result, border=5)
    cv2.imwrite(str(output_path), result, [cv2.IMWRITE_PNG_COMPRESSION, 6])
    return True  # Fallback zawsze "działa"

def main():
    OUTPUT_DIR.mkdir(exist_ok=True)

    files = sorted(INPUT_DIR.glob("juras_*.png"))
    total = len(files)
    success = 0
    fallback = 0

    print(f"Przetwarzam {total} zdjęć dokumentów...")
    print(f"Input:  {INPUT_DIR}/")
    print(f"Output: {OUTPUT_DIR}/")
    print("-" * 60)

    for i, fpath in enumerate(files, 1):
        outpath = OUTPUT_DIR / fpath.name

        # Sprawdź którą metodą poszło
        image = cv2.imread(str(fpath))
        if image is None:
            print(f"[{i:3d}/{total}] BŁĄD: {fpath.name}")
            continue

        contour = find_document_contour(image)
        method = "kontur" if contour is not None else "kolor/fallback"

        ok = process_image(fpath, outpath)
        if ok:
            success += 1
            status = "✓"
        else:
            status = "✗"

        print(f"[{i:3d}/{total}] {status} {fpath.name} ({method})")

    print("-" * 60)
    print(f"Gotowe: {success}/{total} zdjęć przetworzonych")
    print(f"Wyniki w: {OUTPUT_DIR}/")

    # Kopiuj do docs/gluchowski_img/ (nadpisz oryginały)
    print(f"\nKopiuję oczyszczone zdjęcia do {DOCS_IMG_DIR}/...")
    copied = 0
    for fpath in OUTPUT_DIR.glob("juras_*.png"):
        dst = DOCS_IMG_DIR / fpath.name
        if dst.exists():
            import shutil
            shutil.copy2(str(fpath), str(dst))
            copied += 1
    print(f"Skopiowano {copied} plików do katalogu docs/")

if __name__ == "__main__":
    main()
