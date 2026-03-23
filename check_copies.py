#!/usr/bin/env python3
"""
check_copies.py -- Scan both Gluchowski PDF catalogs for copy/original indicators.

Searches for words like: copia, cópia, kopia, reprodukcja, reprodução,
original, oryginal, odpis, faksymile, fac-simile, xerox, fotokopia, etc.
"""
import fitz  # PyMuPDF
import re
import sys

sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)

PDFS = [
    r"C:\Users\skore\Downloads\Kolekcja_Gluchowski_KATALOG_NAUKOWY.pdf",
    r"C:\Users\skore\Downloads\Kolekcja_Gluchowski_Katalog_Tematyczny.pdf",
]

# Keywords to search (case-insensitive)
COPY_KEYWORDS = [
    r'\bcopi[aã]\b',
    r'\bcópi[aã]\b',
    r'\bkopi[aã]\b',
    r'\breprodu[kcç][çcaã]\w*\b',
    r'\bodpis\b',
    r'\bfaksymil\w*\b',
    r'\bfac[\-\s]?simil\w*\b',
    r'\bxero[xk]\w*\b',
    r'\bfotokopi\w*\b',
    r'\bkserokopi\w*\b',
    r'\bduplikat\w*\b',
    r'\bdublet\w*\b',
    r'\bprzedruk\w*\b',
    r'\breprint\w*\b',
]

ORIGINAL_KEYWORDS = [
    r'\boryginał\w*\b',
    r'\boryginal\w*\b',
    r'\boriginal\w*\b',
    r'\bautentycz\w*\b',
    r'\bautentic\w*\b',
    r'\bautograf\w*\b',
]

def search_page(text, patterns):
    """Return list of (keyword, context) matches."""
    results = []
    for pat in patterns:
        for m in re.finditer(pat, text, re.IGNORECASE):
            start = max(0, m.start() - 80)
            end = min(len(text), m.end() + 80)
            context = text[start:end].replace('\n', ' ').strip()
            results.append((m.group(), context))
    return results


def main():
    for pdf_path in PDFS:
        print(f"\n{'='*80}")
        print(f"PDF: {pdf_path.split(chr(92))[-1]}")
        print(f"{'='*80}")

        try:
            doc = fitz.open(pdf_path)
        except Exception as e:
            print(f"  ERROR opening: {e}")
            continue

        print(f"  Pages: {len(doc)}")

        copy_found_any = False
        original_found_any = False

        for page_num in range(len(doc)):
            page = doc[page_num]
            text = page.get_text()

            if not text.strip():
                continue

            copy_matches = search_page(text, COPY_KEYWORDS)
            orig_matches = search_page(text, ORIGINAL_KEYWORDS)

            if copy_matches or orig_matches:
                print(f"\n  --- Page {page_num + 1} ---")

                if copy_matches:
                    copy_found_any = True
                    for kw, ctx in copy_matches:
                        print(f"    [COPY] '{kw}' -> ...{ctx}...")

                if orig_matches:
                    original_found_any = True
                    for kw, ctx in orig_matches:
                        print(f"    [ORIG] '{kw}' -> ...{ctx}...")

        doc.close()

        if not copy_found_any and not original_found_any:
            print("  No copy/original keywords found in text layer.")
            print("  (PDF may be image-only or use different terminology)")

    # Also dump full text of a few key pages for manual review
    print(f"\n\n{'='*80}")
    print("FULL TEXT DUMP -- KATALOG NAUKOWY (first 10 pages with text)")
    print(f"{'='*80}")

    doc = fitz.open(PDFS[0])
    pages_with_text = 0
    for page_num in range(len(doc)):
        text = doc[page_num].get_text().strip()
        if text and pages_with_text < 29:  # dump all pages
            pages_with_text += 1
            print(f"\n--- NAUKOWY Page {page_num + 1} ---")
            print(text[:2000])
            if len(text) > 2000:
                print(f"  ... [truncated, {len(text)} chars total]")
    doc.close()

    print(f"\n\n{'='*80}")
    print("FULL TEXT DUMP -- KATALOG TEMATYCZNY (all pages with text)")
    print(f"{'='*80}")

    doc = fitz.open(PDFS[1])
    for page_num in range(len(doc)):
        text = doc[page_num].get_text().strip()
        if text:
            print(f"\n--- TEMATYCZNY Page {page_num + 1} ---")
            print(text[:2000])
            if len(text) > 2000:
                print(f"  ... [truncated, {len(text)} chars total]")
    doc.close()


if __name__ == "__main__":
    main()
