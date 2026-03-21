"""Quick test: rembg on 3 sample images."""
from pathlib import Path
from PIL import Image
from rembg import remove
import io
import cv2
import numpy as np

INPUT_DIR = Path("juras_img")
OUTPUT_DIR = Path("juras_img_clean")
OUTPUT_DIR.mkdir(exist_ok=True)

MARGIN = 20
test_files = ["juras_001_page2.png", "juras_030_page31.png", "juras_060_page61.png"]

for fname in test_files:
    fpath = INPUT_DIR / fname
    print(f"Processing {fname}...")

    with open(fpath, "rb") as f:
        input_data = f.read()

    output_data = remove(input_data)
    img_rgba = Image.open(io.BytesIO(output_data)).convert("RGBA")

    # White bg
    white = Image.new("RGBA", img_rgba.size, (255, 255, 255, 255))
    composite = Image.alpha_composite(white, img_rgba).convert("RGB")

    # Crop to content
    arr = np.array(composite)
    gray = cv2.cvtColor(arr, cv2.COLOR_RGB2GRAY)
    mask = gray < 240
    coords = np.argwhere(mask)
    if len(coords) > 100:
        y0, x0 = coords.min(axis=0)
        y1, x1 = coords.max(axis=0)
        h, w = arr.shape[:2]
        y0 = max(0, y0 - MARGIN)
        x0 = max(0, x0 - MARGIN)
        y1 = min(h, y1 + MARGIN)
        x1 = min(w, x1 + MARGIN)
        composite = composite.crop((x0, y0, x1, y1))

    outpath = OUTPUT_DIR / fname
    composite.save(str(outpath), "PNG")
    print(f"  ✓ Saved to {outpath}")

print("Done! Check juras_img_clean/")
