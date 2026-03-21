"""Generate HTML cards for all documents not yet in transkrypcja_demo.html"""
import sys
import os

# Add project dir to path
sys.path.insert(0, os.path.dirname(__file__))
from transcriptions import TRANSCRIPTIONS

# These 14 are already in the HTML
EXISTING = {
    "juras_001", "juras_009", "juras_010", "juras_024", "juras_026",
    "juras_027", "juras_035", "juras_037", "juras_040", "juras_042",
    "juras_060", "juras_065", "juras_075", "juras_091"
}

# Image mapping
def get_image(key):
    if key.startswith("stefan_"):
        num = key.split("_")[1]
        return f"gluchowski_img/stefan_{num}.jpeg"
    else:
        num = int(key.split("_")[1])
        page = num + 1
        return f"gluchowski_img/juras_{num:03d}_page{page}.png"

def get_sygn(key):
    num = int(key.split("_")[1])
    if key.startswith("stefan_"):
        return f"ARG/S/{num:03d}"
    else:
        return f"ARG/J/{num:03d}"

def escape_html(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def truncate_transcript(text, max_lines=20):
    lines = text.strip().split("\n")
    if len(lines) > max_lines:
        return "\n".join(lines[:max_lines]) + "\n[...]"
    return text.strip()

def get_collection_label(key):
    if key.startswith("stefan_"):
        return "stefan"
    return "juras"

def generate_card(key, doc):
    num = key.split("_")[1]
    collection = get_collection_label(key)
    img = get_image(key)
    sygn = get_sygn(key)

    # Determine if highlight
    highlight_keys = {
        "stefan_028", "stefan_022", "stefan_020", "stefan_023",
        "stefan_002", "stefan_003", "stefan_008", "stefan_006",
        "stefan_031", "stefan_015"
    }
    highlight = " highlight" if key in highlight_keys else ""

    # Collection badge
    if collection == "stefan":
        collection_badge = '<span class="doc-badge" style="background:#8B4513;color:#fff">SERIA STEFAN</span>'
    else:
        collection_badge = '<span class="doc-badge" style="background:#1a5276;color:#fff">SERIA JURAS</span>'

    transcript = escape_html(truncate_transcript(doc.get("transkrypcja", "[brak transkrypcji]")))

    # Persons section
    persons_html = ""
    if doc.get("osoby"):
        persons_items = "\n".join(f"          <li>{escape_html(o)}</li>" for o in doc["osoby"])
        persons_html = f"""
      <div class="doc-meta-block">
        <div class="label label-persons">👤 OSOBY</div>
        <ul>
{persons_items}
        </ul>
      </div>"""

    # Seals section
    seals_html = ""
    if doc.get("pieczecie"):
        seals_items = "\n".join(f"          <li>{escape_html(s)}</li>" for s in doc["pieczecie"])
        seals_html = f"""
      <div class="doc-meta-block">
        <div class="label label-seals">🔴 PIECZĘCIE</div>
        <ul>
{seals_items}
        </ul>
      </div>"""

    # Signs section
    signs_html = ""
    if doc.get("znaki_szczegolne"):
        signs_items = "\n".join(f"          <li>{escape_html(s)}</li>" for s in doc["znaki_szczegolne"])
        signs_html = f"""
      <div class="doc-meta-block">
        <div class="label label-signs">🔍 ZNAKI SZCZEGÓLNE</div>
        <ul>
{signs_items}
        </ul>
      </div>"""

    # Context
    context = escape_html(doc.get("kontekst", ""))

    card = f"""
  <!-- {key} -->
  <div class="doc-card{highlight}" id="doc-{num}-{collection}">
    <div class="doc-img" onclick="openLB(this.querySelector('img').src)">
      <div class="doc-sygn">{sygn}</div>
      <img src="{img}" alt="{escape_html(doc.get('typ', ''))}">
    </div>
    <div class="doc-panel">
      <div class="doc-title">{escape_html(doc.get('typ', ''))}</div>
      <div class="doc-meta">
        <span class="doc-badge date">{escape_html(doc.get('data', 'b.d.'))}</span>
        <span class="doc-badge type">{escape_html(doc.get('typ', ''))}</span>
        <span class="doc-badge lang">{escape_html(doc.get('jezyk', ''))}</span>
        {collection_badge}
      </div>

      <div class="doc-transcript">
        <div class="transcript-header">
          <span class="transcript-label">📝 TRANSKRYPCJA</span>
        </div>
        <pre>{transcript}</pre>
      </div>
{persons_html}
{seals_html}
{signs_html}
      <div class="doc-context">
        <div class="label label-context">📖 KONTEKST HISTORYCZNY</div>
        <span>{context}</span>
      </div>
    </div>
  </div>
"""
    return card

# Sort keys: juras first (by number), then stefan (by number)
def sort_key(k):
    prefix = 0 if k.startswith("juras_") else 1
    num = int(k.split("_")[1])
    return (prefix, num)

missing_keys = sorted(
    [k for k in TRANSCRIPTIONS.keys() if k not in EXISTING],
    key=sort_key
)

print(f"<!-- ============================================ -->")
print(f"<!-- BRAKUJĄCE DOKUMENTY — automatycznie generowane -->")
print(f"<!-- Juras: {sum(1 for k in missing_keys if k.startswith('juras_'))} dokumentów -->")
print(f"<!-- Stefan: {sum(1 for k in missing_keys if k.startswith('stefan_'))} dokumentów -->")
print(f"<!-- ============================================ -->")

# Add Stefan series header before first stefan doc
stefan_header_printed = False
for key in missing_keys:
    if key.startswith("stefan_") and not stefan_header_printed:
        print("""
  <!-- ============================================ -->
  <!-- SERIA STEFAN — Dokumenty Stefana Głuchowskiego -->
  <!-- Urzędnik Kancelarii Cywilnej Prezydenta RP, -->
  <!-- żołnierz AK ps. Radwan, ojciec Krzysztofa -->
  <!-- ============================================ -->
  <div style="margin:40px 0 20px;padding:20px;background:linear-gradient(135deg,#8B4513 0%,#654321 100%);border-radius:12px;text-align:center;">
    <h3 style="color:#f5deb3;margin:0;font-size:1.3em;">📜 SERIA STEFAN — Dokumenty Stefana Głuchowskiego</h3>
    <p style="color:#deb887;margin:8px 0 0;font-size:0.95em;">Urzędnik Kancelarii Cywilnej Prezydenta RP · Żołnierz AK ps. „Radwan" · Ojciec Krzysztofa</p>
  </div>
""")
        stefan_header_printed = True
    print(generate_card(key, TRANSCRIPTIONS[key]))

print(f"\n<!-- Koniec generowanych kart. Łącznie: {len(missing_keys)} nowych dokumentów -->")
