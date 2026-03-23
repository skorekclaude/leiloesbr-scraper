#!/usr/bin/env python3
"""Assemble 4 chemistry chapter HTML files into one unified document."""

import os, re, sys, io, html as html_mod

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

CHAPTER_FILES = [
    ("final_01_solvay.html", "chapter-1", "Rozdział 1"),
    ("final_02_kwas_siarkowy.html", "chapter-2", "Rozdział 2"),
    ("final_03_kwas_fosforowy.html", "chapter-3", "Rozdział 3"),
    ("final_04_amoniak.html", "chapter-4", "Rozdział 4"),
]

OUTPUT_FILE = os.path.join(BASE_DIR, "METODY_TECHNOLOGICZNE_FINAL.html")


def extract_title_and_subtitle(html_content):
    header_area = html_content[:5000]
    h1_pat = r"<h1[^>]*>(.*?)</h1>"
    h2_pat = r"<h2[^>]*>(.*?)</h2>"
    h1_match = re.search(h1_pat, header_area, re.DOTALL)
    h2_match = re.search(h2_pat, header_area, re.DOTALL)
    tag_pat = r"<[^>]+>"
    title = html_mod.unescape(re.sub(tag_pat, "", h1_match.group(1)).strip()) if h1_match else "Rozdzial"
    subtitle = html_mod.unescape(re.sub(tag_pat, "", h2_match.group(1)).strip()) if h2_match else ""
    return title, subtitle


def strip_inline_font_family(html_content):
    pat = r'(<div class="chapter" style="[^"]*?)font-family:\s*[^;]+;\s*'
    html_content = re.sub(pat, r'\1', html_content, count=1)
    # Remove any leading raw CSS text before the first HTML tag (broken div extraction)
    html_content = re.sub(r'^[^<]+(?=<)', '', html_content.strip())
    return html_content

def build_unified_css():
    return """
    *, *::before, *::after { box-sizing: border-box; }
    html { font-size: 16px; scroll-behavior: smooth; }
    body {
        font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
        color: #1a1a1a; background: #f5f5f0;
        margin: 0; padding: 0; line-height: 1.7;
        -webkit-font-smoothing: antialiased;
    }
    .cover-page {
        min-height: 100vh; display: flex; flex-direction: column;
        justify-content: center; align-items: center; text-align: center;
        background: linear-gradient(160deg, #1a365d 0%, #2c5282 40%, #3182ce 100%);
        color: #fff; padding: 60px 40px;
    }
    .cover-page h1 {
        font-family: Georgia, 'Times New Roman', serif;
        font-size: 2.8rem; font-weight: 700; letter-spacing: 2px;
        margin: 0 0 16px 0; max-width: 800px; line-height: 1.2;
        text-shadow: 0 2px 8px rgba(0,0,0,0.3);
    }
    .cover-page .subtitle {
        font-size: 1.2rem; font-weight: 300; opacity: 0.85;
        max-width: 600px; margin: 0 0 40px 0; line-height: 1.5;
    }
    .cover-page .date {
        font-size: 1rem; opacity: 0.6; letter-spacing: 3px;
        text-transform: uppercase; margin-top: 20px;
    }
    .cover-page .divider {
        width: 120px; height: 2px; background: rgba(255,255,255,0.4); margin: 30px auto;
    }
    .toc-page {
        max-width: 800px; margin: 0 auto; padding: 60px 40px 80px; background: #fff;
    }
    .toc-page h2 {
        font-family: Georgia, 'Times New Roman', serif;
        font-size: 2rem; color: #1a365d; text-align: center;
        margin: 0 0 40px 0; padding-bottom: 16px; border-bottom: 3px solid #1a365d;
    }
    .toc-list { list-style: none; padding: 0; margin: 0; }
    .toc-list li { margin: 0; border-bottom: 1px solid #e2e8f0; }
    .toc-list li:last-child { border-bottom: none; }
    .toc-list a {
        display: flex; align-items: baseline; padding: 18px 16px;
        text-decoration: none; color: #2d3748; transition: all 0.2s; border-radius: 6px;
    }
    .toc-list a:hover { background: #edf2f7; color: #1a365d; }
    .toc-chapter-num {
        font-family: Georgia, 'Times New Roman', serif;
        font-size: 1.1rem; font-weight: 700; color: #2c5282;
        min-width: 120px; flex-shrink: 0;
    }
    .toc-chapter-info { flex: 1; }
    .toc-chapter-title {
        font-family: Georgia, 'Times New Roman', serif;
        font-size: 1.15rem; font-weight: 600; color: #1a365d; display: block;
    }
    .toc-chapter-subtitle { font-size: 0.9rem; color: #718096; margin-top: 2px; display: block; }
    .chapter-wrapper {
        max-width: 960px; margin: 0 auto; padding: 0 20px 60px; background: #fff;
    }
    .chapter-wrapper .chapter { padding-top: 40px; }
    .chapter-wrapper h1 {
        font-family: Georgia, 'Times New Roman', serif !important;
        color: #1a365d !important; font-size: 2rem !important; letter-spacing: 1.5px !important;
    }
    .chapter-wrapper h2 {
        font-family: Georgia, 'Times New Roman', serif !important; font-size: 1.4rem !important;
    }
    .chapter-wrapper h3 {
        font-family: Georgia, 'Times New Roman', serif !important; color: #2c5282 !important;
    }
    .chapter-wrapper h4 { font-family: Georgia, 'Times New Roman', serif !important; }
    .chapter-wrapper table {
        width: 100%; border-collapse: collapse; margin: 18px 0; font-size: 0.92rem;
    }
    .chapter-wrapper th {
        background: #1a365d !important; color: #fff !important;
        padding: 10px 12px !important; text-align: left; font-weight: 600;
        border: 1px solid #2c5282 !important;
    }
    .chapter-wrapper td {
        padding: 8px 12px !important; border: 1px solid #cbd5e0 !important;
    }
    .chapter-wrapper tr:nth-child(even) td { background: #f7fafc; }
    .chapter-wrapper tr:nth-child(odd) td { background: #fff; }
    .chapter-wrapper tr:hover td { background: #edf2f7; }
    .back-to-toc {
        display: inline-block; margin-top: 30px; padding: 8px 20px;
        font-size: 0.85rem; color: #2c5282; text-decoration: none;
        border: 1px solid #cbd5e0; border-radius: 4px; transition: all 0.2s;
    }
    .back-to-toc:hover { background: #edf2f7; border-color: #2c5282; }
    .chapter-separator {
        border: none; height: 3px;
        background: linear-gradient(90deg, transparent, #2c5282, transparent);
        margin: 60px auto 0; max-width: 400px;
    }
    .doc-footer {
        text-align: center; padding: 40px 20px; font-size: 0.85rem;
        background: #1a365d; color: rgba(255,255,255,0.5);
    }
    @media print {
        html { font-size: 11pt; }
        body { background: #fff; color: #000; }
        .cover-page {
            min-height: auto; height: 100vh;
            background: #fff !important; color: #1a365d !important;
            page-break-after: always;
        }
        .cover-page h1 { text-shadow: none; color: #1a365d; }
        .cover-page .subtitle, .cover-page .date { color: #4a5568; opacity: 1; }
        .cover-page .divider { background: #1a365d; }
        .toc-page { page-break-after: always; }
        .toc-list a { color: #000; }
        .chapter-wrapper { padding: 0; }
        .chapter-wrapper .chapter { page-break-before: always; }
        .chapter-wrapper .chapter:first-child { page-break-before: auto; }
        .chapter-wrapper h1, .chapter-wrapper h2, .chapter-wrapper h3 { page-break-after: avoid; }
        .chapter-wrapper table { page-break-inside: avoid; }
        .back-to-toc { display: none !important; }
        .chapter-separator { display: none; }
        .doc-footer { display: none; }
        @page { size: A4; margin: 20mm 18mm; }
    }
    """

def build_html(chapters_data):
    LT = chr(60)
    GT = chr(62)
    AMP = chr(38)
    toc_items = ""
    for ch in chapters_data:
        toc_items += LT + "li" + GT
        toc_items += LT + "a href=" + chr(34) + "#" + ch["id"] + chr(34) + GT
        toc_items += LT + "span class=" + chr(34) + "toc-chapter-num" + chr(34) + GT + ch["label"] + LT + "/span" + GT
        toc_items += LT + "span class=" + chr(34) + "toc-chapter-info" + chr(34) + GT
        toc_items += LT + "span class=" + chr(34) + "toc-chapter-title" + chr(34) + GT + ch["title"] + LT + "/span" + GT
        toc_items += LT + "span class=" + chr(34) + "toc-chapter-subtitle" + chr(34) + GT + ch["subtitle"] + LT + "/span" + GT
        toc_items += LT + "/span" + GT + LT + "/a" + GT + LT + "/li" + GT + chr(10)

    chapter_sections = ""
    for i, ch in enumerate(chapters_data):
        if i > 0:
            chapter_sections += LT + "hr class=" + chr(34) + "chapter-separator" + chr(34) + GT + chr(10)
        chapter_sections += LT + "div id=" + chr(34) + ch["id"] + chr(34) + " class=" + chr(34) + "chapter-wrapper" + chr(34) + GT + chr(10)
        chapter_sections += ch["content"] + chr(10)
        chapter_sections += LT + "a href=" + chr(34) + "#toc" + chr(34) + " class=" + chr(34) + "back-to-toc" + chr(34) + GT
        chapter_sections += AMP + "uarr; Spis treści" + LT + "/a" + GT + chr(10)
        chapter_sections += LT + "/div" + GT + chr(10)

    css = build_unified_css()

    h = LT + "!DOCTYPE html" + GT + chr(10)
    h += LT + "html lang=" + chr(34) + "pl" + chr(34) + GT + chr(10)
    h += LT + "head" + GT + chr(10)
    h += LT + "meta charset=" + chr(34) + "UTF-8" + chr(34) + GT + chr(10)
    h += LT + "meta name=" + chr(34) + "viewport" + chr(34) + " content=" + chr(34) + "width=device-width, initial-scale=1.0" + chr(34) + GT + chr(10)
    h += LT + "title" + GT + "Metody technologiczne w przemyśle chemicznym" + LT + "/title" + GT + chr(10)
    h += LT + "style" + GT + css + LT + "/style" + GT + chr(10)
    h += LT + "/head" + GT + chr(10)
    h += LT + "body" + GT + chr(10) + chr(10)

    # Cover page
    h += LT + "div class=" + chr(34) + "cover-page" + chr(34) + GT + chr(10)
    h += LT + "div style=" + chr(34) + "font-size:72px;margin-bottom:30px;opacity:0.9" + chr(34) + GT + AMP + "#9883;" + LT + "/div" + GT + chr(10)
    h += LT + "h1" + GT + "METODY TECHNOLOGICZNE" + LT + "br" + GT + "W PRZEMYŚLE CHEMICZNYM" + LT + "/h1" + GT + chr(10)
    h += LT + "div class=" + chr(34) + "divider" + chr(34) + GT + LT + "/div" + GT + chr(10)
    h += LT + "p class=" + chr(34) + "subtitle" + chr(34) + GT + "Szczegółowy opis metod produkcji kluczowych związków chemicznych" + LT + "/p" + GT + chr(10)
    h += LT + "p class=" + chr(34) + "date" + chr(34) + GT + "Luty 2026" + LT + "/p" + GT + chr(10)
    h += LT + "/div" + GT + chr(10) + chr(10)

    # TOC
    h += LT + "div id=" + chr(34) + "toc" + chr(34) + " class=" + chr(34) + "toc-page" + chr(34) + GT + chr(10)
    h += LT + "h2" + GT + "Spis treści" + LT + "/h2" + GT + chr(10)
    h += LT + "ul class=" + chr(34) + "toc-list" + chr(34) + GT + chr(10) + toc_items + LT + "/ul" + GT + chr(10)
    h += LT + "/div" + GT + chr(10) + chr(10)

    # Chapters
    h += chapter_sections + chr(10)

    # Footer
    h += LT + "div class=" + chr(34) + "doc-footer" + chr(34) + GT + chr(10)
    h += "Metody technologiczne w przemyśle chemicznym " + AMP + "mdash; Opracowanie do celów egzaminacyjnych " + AMP + "mdash; Luty 2026" + chr(10)
    h += LT + "/div" + GT + chr(10) + chr(10)
    h += LT + "/body" + GT + chr(10) + LT + "/html" + GT
    return h

def main():
    chapters_data = []
    for filename, chapter_id, label in CHAPTER_FILES:
        filepath = os.path.join(BASE_DIR, filename)
        if not os.path.exists(filepath):
            print("ERROR: File not found: " + filepath, file=sys.stderr)
            sys.exit(1)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        # Check for body tags (these files are div fragments, but just in case)
        body_pat = r"(?si)" + chr(60) + "body[^" + chr(62) + "]*" + chr(62) + "(.*?)" + chr(60) + "/body" + chr(62)
        body_match = re.search(body_pat, content)
        if body_match:
            content = body_match.group(1).strip()
        title, subtitle = extract_title_and_subtitle(content)
        content = strip_inline_font_family(content)
        chapters_data.append({
            "id": chapter_id,
            "label": label,
            "title": title,
            "subtitle": subtitle,
            "content": content,
        })
        print("  Loaded " + filename + " (" + str(len(content)) + " chars) -> " + title)
    html = build_html(chapters_data)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(html)
    print("")
    print("Written " + str(len(html)) + " chars to " + OUTPUT_FILE)


if __name__ == "__main__":
    main()
