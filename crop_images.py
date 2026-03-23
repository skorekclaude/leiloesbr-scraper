#!/usr/bin/env python3
"""
crop_images.py -- Auto-crop Tematyczny images to remove blue sofa/fabric background.

Specifically targets the blue/gray fabric visible in many Katalog Tematyczny photos.
Uses HSV color space to detect the blue fabric and crop to document content.
"""
import sys, os
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)

from PIL import Image, ImageFilter
import numpy as np

IMG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "docs", "gluchowski_img")
CROP_DIR = os.path.join(IMG_DIR, "cropped")
os.makedirs(CROP_DIR, exist_ok=True)


def rgb_to_hsv(arr):
    """Convert RGB array to HSV."""
    arr = arr.astype(float) / 255.0
    r, g, b = arr[:,:,0], arr[:,:,1], arr[:,:,2]
    maxc = np.maximum(np.maximum(r, g), b)
    minc = np.minimum(np.minimum(r, g), b)
    diff = maxc - minc

    # Hue
    h = np.zeros_like(maxc)
    mask = diff > 0
    rm = mask & (maxc == r)
    gm = mask & (maxc == g)
    bm = mask & (maxc == b)
    h[rm] = (60 * ((g[rm] - b[rm]) / diff[rm]) % 360)
    h[gm] = (60 * ((b[gm] - r[gm]) / diff[gm]) + 120)
    h[bm] = (60 * ((r[bm] - g[bm]) / diff[bm]) + 240)
    h = h % 360

    # Saturation
    s = np.zeros_like(maxc)
    s[maxc > 0] = diff[maxc > 0] / maxc[maxc > 0]

    # Value
    v = maxc

    return h, s, v


def detect_blue_fabric(img):
    """Detect blue/gray sofa fabric in image.

    The Tematyczny photos show documents on blue/steel-gray fabric.
    Returns a boolean mask where True = fabric/background.
    """
    arr = np.array(img.convert("RGB"))
    h, s, v = rgb_to_hsv(arr)

    # Blue fabric characteristics:
    # Hue: 190-250 (blue range)
    # Saturation: 0.08-0.60 (muted blue, not vivid)
    # Value: 0.25-0.75 (medium brightness)
    blue_mask = (
        (h >= 180) & (h <= 260) &
        (s >= 0.05) & (s <= 0.65) &
        (v >= 0.20) & (v <= 0.80)
    )

    # Also catch very dark blue/black areas (shadows on fabric)
    dark_mask = (v < 0.15) & (s < 0.3)

    # Also catch grayish tones near blue
    gray_blue = (
        (h >= 170) & (h <= 270) &
        (s >= 0.02) & (s <= 0.15) &
        (v >= 0.30) & (v <= 0.70)
    )

    return blue_mask | dark_mask | gray_blue


def smart_crop(img, margin=8):
    """Crop image by removing blue fabric from edges.

    Works inward from each edge, removing rows/columns that are mostly fabric.
    """
    arr = np.array(img.convert("RGB"))
    h, w = arr.shape[:2]
    fabric_mask = detect_blue_fabric(img)

    # Find content area by checking row/column fabric density
    # A row/column is "background" if >60% of pixels are fabric
    fabric_threshold = 0.55

    row_fabric = fabric_mask.mean(axis=1)
    col_fabric = fabric_mask.mean(axis=0)

    # Scan from edges inward
    top = 0
    while top < h and row_fabric[top] > fabric_threshold:
        top += 1

    bottom = h
    while bottom > top and row_fabric[bottom-1] > fabric_threshold:
        bottom -= 1

    left = 0
    while left < w and col_fabric[left] > fabric_threshold:
        left += 1

    right = w
    while right > left and col_fabric[right-1] > fabric_threshold:
        right -= 1

    # Apply margin
    top = max(0, top - margin)
    left = max(0, left - margin)
    bottom = min(h, bottom + margin)
    right = min(w, right + margin)

    # Check if we'd remove too much (>50% area) — if so, don't crop
    crop_area = (right - left) * (bottom - top)
    if crop_area < 0.50 * w * h:
        return None, (0, 0, w, h)

    return img.crop((left, top, right, bottom)), (left, top, right, bottom)


def split_multi_object(img, direction="vertical"):
    """Split multi-object photo into separate document regions.

    Uses fabric detection to find gaps between documents.
    direction: 'vertical' (documents stacked top-to-bottom) or
               'horizontal' (documents side-by-side)
    """
    fabric_mask = detect_blue_fabric(img)
    arr = np.array(img.convert("RGB"))
    h, w = arr.shape[:2]

    if direction == "horizontal":
        # Check column-by-column fabric density
        col_density = fabric_mask.mean(axis=0)
        # Find gaps (columns that are mostly fabric)
        gap_threshold = 0.55
        min_gap_width = 8
        min_region_width = 80
    else:
        # Check row-by-row fabric density
        col_density = fabric_mask.mean(axis=1)
        gap_threshold = 0.55
        min_gap_width = 8
        min_region_width = 60

    # Find contiguous content regions
    is_content = col_density < gap_threshold
    regions = []
    in_region = False
    start = 0
    gap_start = 0

    length = w if direction == "horizontal" else h
    min_width = min_region_width

    for i in range(length):
        if is_content[i]:
            if not in_region:
                in_region = True
                start = i
        else:
            if in_region:
                # Check if this gap is wide enough
                if not hasattr(split_multi_object, '_gap_start'):
                    gap_start = i
                gap_end = i
                # Look ahead to see if gap continues
                gap_continues = True
                for j in range(i, min(i + min_gap_width, length)):
                    if is_content[j]:
                        gap_continues = False
                        break
                if gap_continues:
                    if i - start >= min_width:
                        regions.append((start, i))
                    in_region = False

    if in_region and length - start >= min_width:
        regions.append((start, length))

    if len(regions) < 2:
        return []

    # Create cropped images for each region
    results = []
    for r_start, r_end in regions:
        if direction == "horizontal":
            # Find vertical bounds within this horizontal region
            region_fabric = fabric_mask[:, r_start:r_end]
            row_dens = region_fabric.mean(axis=1)
            rows_content = row_dens < 0.55
            if not np.any(rows_content):
                continue
            top = max(0, np.argmax(rows_content) - 5)
            bottom = min(h, h - np.argmax(rows_content[::-1]) + 5)
            bbox = (max(0, r_start-5), top, min(w, r_end+5), bottom)
        else:
            # Find horizontal bounds within this vertical region
            region_fabric = fabric_mask[r_start:r_end, :]
            col_dens = region_fabric.mean(axis=0)
            cols_content = col_dens < 0.55
            if not np.any(cols_content):
                continue
            left = max(0, np.argmax(cols_content) - 5)
            right = min(w, w - np.argmax(cols_content[::-1]) + 5)
            bbox = (left, max(0, r_start-5), right, min(h, r_end+5))

        cropped = img.crop(bbox)
        if cropped.width >= 50 and cropped.height >= 50:
            results.append((cropped, bbox))

    return results


# ============================================================
# MULTI-OBJECT PHOTOS (need splitting)
# ============================================================
MULTI_OBJECT_PHOTOS = {
    # p03_img02: PON envelope (left) + Karta Polowa Legionow (right)
    "Kolekcja_Gluchowski_Katalog_Tematyczny_p03_img02.jpeg": "horizontal",
    # p11_img01: envelope (left) + handwritten letter (right)
    "Kolekcja_Gluchowski_Katalog_Tematyczny_p11_img01.jpeg": "horizontal",
    # p12_img02: 3 items stacked (propusk top, card middle, receipt bottom)
    "Kolekcja_Gluchowski_Katalog_Tematyczny_p12_img02.jpeg": "vertical",
    # p15_img02: 2 legitimation cards side by side
    "Kolekcja_Gluchowski_Katalog_Tematyczny_p15_img02.jpeg": "horizontal",
}


def main():
    tematyczny_files = sorted([
        f for f in os.listdir(IMG_DIR)
        if f.startswith("Kolekcja_Gluchowski_Katalog_Tematyczny_") and f.endswith(".jpeg")
    ])

    print(f"Znaleziono {len(tematyczny_files)} zdjec Tematyczny do przetworzenia")
    print(f"Katalog wyjsciowy: {CROP_DIR}")
    print("=" * 70)

    stats = {"cropped": 0, "copied": 0, "split": 0, "failed": 0}

    for fname in tematyczny_files:
        src_path = os.path.join(IMG_DIR, fname)
        img = Image.open(src_path)
        orig_w, orig_h = img.size

        # Multi-object photo — try splitting
        if fname in MULTI_OBJECT_PHOTOS:
            direction = MULTI_OBJECT_PHOTOS[fname]
            base_name = fname.replace(".jpeg", "")

            results = split_multi_object(img, direction)
            if len(results) >= 2:
                print(f"\n  SPLIT {fname}: {len(results)} obiektow ({direction})")
                for idx, (cropped, bbox) in enumerate(results):
                    out_name = f"{base_name}_obj{idx+1:02d}.jpeg"
                    out_path = os.path.join(CROP_DIR, out_name)
                    cropped.save(out_path, "JPEG", quality=92)
                    print(f"    -> {out_name} ({cropped.width}x{cropped.height})")
                    stats["split"] += 1
                # Also save cropped version of the whole
                cropped_whole, _ = smart_crop(img)
                if cropped_whole:
                    cropped_whole.save(os.path.join(CROP_DIR, fname), "JPEG", quality=92)
                else:
                    img.save(os.path.join(CROP_DIR, fname), "JPEG", quality=92)
            else:
                # Could not split — try regular crop
                cropped, bbox = smart_crop(img)
                out_path = os.path.join(CROP_DIR, fname)
                if cropped and (cropped.width != orig_w or cropped.height != orig_h):
                    cropped.save(out_path, "JPEG", quality=92)
                    print(f"  CROP (no split) {fname}: {orig_w}x{orig_h} -> {cropped.width}x{cropped.height}")
                    stats["cropped"] += 1
                else:
                    img.save(out_path, "JPEG", quality=92)
                    print(f"  COPY (no split) {fname}: {orig_w}x{orig_h}")
                    stats["copied"] += 1
        else:
            # Single-object photo — auto-crop blue fabric edges
            cropped, bbox = smart_crop(img)
            out_path = os.path.join(CROP_DIR, fname)

            if cropped and (cropped.width != orig_w or cropped.height != orig_h):
                reduction = 1 - (cropped.width * cropped.height) / (orig_w * orig_h)
                cropped.save(out_path, "JPEG", quality=92)
                print(f"  CROP {fname}: {orig_w}x{orig_h} -> {cropped.width}x{cropped.height} (-{reduction*100:.0f}%)")
                stats["cropped"] += 1
            else:
                img.save(out_path, "JPEG", quality=92)
                print(f"  COPY {fname}: {orig_w}x{orig_h} (brak niebieskiego tla)")
                stats["copied"] += 1

    print("\n" + "=" * 70)
    print(f"GOTOWE:")
    print(f"  Przyciete:    {stats['cropped']}")
    print(f"  Rozdzielone:  {stats['split']}")
    print(f"  Skopiowane:   {stats['copied']}")
    print(f"\nPliki w: {CROP_DIR}")


if __name__ == "__main__":
    main()
