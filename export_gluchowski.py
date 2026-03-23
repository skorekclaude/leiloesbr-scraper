#!/usr/bin/env python3
"""
export_gluchowski.py  - Dedykowany katalog kolekcji Głuchowskich.

Profesjonalny katalog muzealny z podziałem na rozdziały:
  I.   PON (1914)
  II.  Legiony / Siódemka (1914-1918)
  III. II Rzeczpospolita (1918-1939)
  IV.  Gen. Sosnkowski
  V.   Getto Łódzkie (1940-1944)
  VI.  7 Pułk Ułanów Lubelskich
  VII. Scottish Album  - PSZ na Zachodzie
  VIII. Dodatkowe  - odznaczenia, mapy, dokumenty rodzinne
"""
import os, sys, json, glob as globmod
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import database

# ============================================================
# IMAGE MAP - maps chapter keys to catalog page numbers
# ============================================================
# KATALOG_NAUKOWY pages per chapter
_NAUKOWY_PAGES = {
    "I": [4],
    "II": [6],
    "III": [9, 10, 13],
    "IV": [14],
    "V": [17],
    "VI": [19, 20, 21],
    "VII": [23, 24, 25, 26, 27],
    "VIII": [28],
}

# Katalog_Tematyczny pages per chapter
_TEMATYCZNY_PAGES = {
    "I": [2, 3],
    "II": [2, 3, 4, 5],
    "III": [4, 5, 6, 7],
    "IV": [8, 9],
    "V": [10],
    "VI": [11, 12],
    "VII": [13, 14],
    "VIII": [15],
}

# Build IMAGE_MAP by scanning actual files in docs/gluchowski_img/
_img_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "docs", "gluchowski_img")
_all_images = sorted(os.listdir(_img_dir)) if os.path.isdir(_img_dir) else []

IMAGE_MAP = {}
for _ch in ["I", "II", "III", "IV", "V", "VI", "VII", "VIII"]:
    _imgs = []
    for _pg in _NAUKOWY_PAGES.get(_ch, []):
        _prefix = f"Kolekcja_Gluchowski_KATALOG_NAUKOWY_p{_pg:02d}_"
        _imgs.extend([f for f in _all_images if f.startswith(_prefix)])
    for _pg in _TEMATYCZNY_PAGES.get(_ch, []):
        _prefix = f"Kolekcja_Gluchowski_Katalog_Tematyczny_p{_pg:02d}_"
        _imgs.extend([f for f in _all_images if f.startswith(_prefix)])
    # deduplicate preserving order (some pages shared between chapters)
    _seen = set()
    _unique = []
    for _f in _imgs:
        if _f not in _seen:
            _seen.add(_f)
            _unique.append(_f)
    IMAGE_MAP[_ch] = _unique

# Seria 29z pages per chapter
_29Z_PAGES = {
    "IX":  list(range(2, 11)),   # p02-p10
    "X":   list(range(11, 17)),  # p11-p16
    "XI":  list(range(17, 23)),  # p17-p22
    "XII": list(range(23, 38)),  # p23-p37
}
for _ch in ["IX", "X", "XI", "XII"]:
    _imgs = []
    for _pg in _29Z_PAGES.get(_ch, []):
        _prefix = f"Seria_29z_p{_pg:02d}_"
        _imgs.extend([f for f in _all_images if f.startswith(_prefix)])
    _seen = set()
    _unique = []
    for _f in _imgs:
        if _f not in _seen:
            _seen.add(_f)
            _unique.append(_f)
    IMAGE_MAP[_ch] = _unique

_total_imgs = sum(len(v) for v in IMAGE_MAP.values())
print(f"Zaladowano {_total_imgs} obrazow do {len(IMAGE_MAP)} rozdzialow")

# ============================================================
# MAPOWANIE ZDJEC DO KONKRETNYCH OBIEKTOW (GL-xxx -> filename)
# Na podstawie analizy zawartosc skanow vs opisy obiektow
# ============================================================
OBJECT_IMAGES = {
    # Ch I - PON (1914)
    "GL-001": ["Kolekcja_Gluchowski_KATALOG_NAUKOWY_p04_img01.jpeg",
               "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p19_img01.jpeg"],
    "GL-002": ["Kolekcja_Gluchowski_Katalog_Tematyczny_p02_img03.jpeg",   # rozkaz PON z pieczecia Orla
               "Kolekcja_Gluchowski_Katalog_Tematyczny_p03_img01.jpeg",   # pokwitowanie PON 200 kop.
               "Kolekcja_Gluchowski_Katalog_Tematyczny_p03_img02.jpeg"],   # koperta urzedowa PON + Karta Polowa (multi-object)
    "GL-003": ["Kolekcja_Gluchowski_Katalog_Tematyczny_p02_img01.jpeg"],   # Legitymacja PON Nr 2
    "GL-004": ["Kolekcja_Gluchowski_Katalog_Tematyczny_p02_img02.jpeg"],   # Afisz zebrania PON, sala Lutni
    # Ch II - Legiony
    "GL-010": ["Kolekcja_Gluchowski_KATALOG_NAUKOWY_p06_img01.jpeg",
               "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p06_img02.jpeg"],      # dyplom + fotografia
    "GL-012": ["Kolekcja_Gluchowski_Katalog_Tematyczny_p04_img01.jpeg"],   # fotokopia Siodemki
    "GL-013": ["Kolekcja_Gluchowski_Katalog_Tematyczny_p04_img02.jpeg",    # zaswiadczenie WBH o sluzbie
               "Kolekcja_Gluchowski_Katalog_Tematyczny_p05_img02.jpeg",    # zaswiadczenie Sosnkowskiego (Inspektor Armii) o PPS
               "Kolekcja_Gluchowski_Katalog_Tematyczny_p05_img04.jpeg"],   # zaswiadczenie DOK o sluzbie
    "GL-014": ["Kolekcja_Gluchowski_Katalog_Tematyczny_p05_img05.jpeg"],   # wlasnorecne wspomnienia gen. (egzamin ZWC)
    "GL-016": ["Kolekcja_Gluchowski_Katalog_Tematyczny_p05_img03.jpeg"],   # fotografia konspiracyjna z Placu Strzeleckiego
    # Ch III - II RP
    "GL-020": ["Kolekcja_Gluchowski_KATALOG_NAUKOWY_p09_img01.jpeg",
               "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p14_img01.jpeg"],
    "GL-021": ["Kolekcja_Gluchowski_KATALOG_NAUKOWY_p10_img01.jpeg"],
    "GL-022": ["Kolekcja_Gluchowski_KATALOG_NAUKOWY_p13_img01.jpeg",
               "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p13_img02.jpeg",
               "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p13_img03.jpeg",      # kompletna legitymacja - 3 strony
               "Kolekcja_Gluchowski_Katalog_Tematyczny_p13_img02.jpeg"],   # portret oficerski w mundurze galowym
    "GL-025": ["Kolekcja_Gluchowski_KATALOG_NAUKOWY_p09_img01.jpeg",
               "Kolekcja_Gluchowski_Katalog_Tematyczny_p09_img01.jpeg"],   # dekret mianowania DOK X
    "GL-026": ["Kolekcja_Gluchowski_KATALOG_NAUKOWY_p09_img01.jpeg",
               "Kolekcja_Gluchowski_Katalog_Tematyczny_p09_img02.jpeg"],   # dekret mianowania I Vice-Ministra
    "GL-027": ["Kolekcja_Gluchowski_Katalog_Tematyczny_p06_img01.jpeg"],   # rozkaz Sztabu Gen. Lublin 5.XI.1918
    "GL-028": ["Kolekcja_Gluchowski_Katalog_Tematyczny_p12_img02.jpeg"],   # pokwitowanie / propusk (multi-object: 3 pozycje)
    "GL-029": ["Kolekcja_Gluchowski_Katalog_Tematyczny_p05_img01.jpeg",    # list na papierze Inspekcji Pulku
               "Kolekcja_Gluchowski_Katalog_Tematyczny_p06_img02.jpeg"],   # list od generala do Chorazego Gluchowskiego
    # Ch IV - Sosnkowski / Emigracja
    "GL-030": ["Kolekcja_Gluchowski_KATALOG_NAUKOWY_p14_img02.jpeg",
               "Kolekcja_Gluchowski_Katalog_Tematyczny_p08_img02.jpeg"],   # pismo MSWojsk o kontrasygnacie Prezydenta
    "GL-031": ["Kolekcja_Gluchowski_KATALOG_NAUKOWY_p14_img03.jpeg"],
    "GL-032": ["Kolekcja_Gluchowski_Katalog_Tematyczny_p07_img02.jpeg"],   # dekret Krola Ferdynanda I Rumunii
    "GL-033": ["Kolekcja_Gluchowski_Katalog_Tematyczny_p07_img01.jpeg"],   # zaproszenie MSWojsk na dekoracje przez Focha
    "GL-034": ["Kolekcja_Gluchowski_Katalog_Tematyczny_p12_img03.jpeg",    # legitymacja Krzyza Walecznych
               "Kolekcja_Gluchowski_Katalog_Tematyczny_p15_img03.jpeg"],   # ta sama legitymacja KW (drugie ujeecie)
    "GL-035": ["Kolekcja_Gluchowski_Katalog_Tematyczny_p10_img01.jpeg"],   # rozkaz wyjazdu na pogrzeb Pilsudskiego
    "GL-036": ["Kolekcja_Gluchowski_Katalog_Tematyczny_p13_img01.jpeg"],   # fotografia z Smidlym-Rydzem 1939
    "GL-037": ["Kolekcja_Gluchowski_Katalog_Tematyczny_p11_img01.jpeg"],   # list Aleksandry Pilsudskiej (koperta + list)
    "GL-038": ["Kolekcja_Gluchowski_Katalog_Tematyczny_p13_img03.jpeg"],   # list wdowy Pilsudskiej po smierci Marszalka
    # Ch V - Getto Lodzkie
    "GL-040": ["Kolekcja_Gluchowski_KATALOG_NAUKOWY_p17_img01.jpeg"],
    "GL-041": ["Kolekcja_Gluchowski_KATALOG_NAUKOWY_p17_img02.jpeg"],
    "GL-042": ["Kolekcja_Gluchowski_KATALOG_NAUKOWY_p17_img02.jpeg"],
    "GL-043": ["Kolekcja_Gluchowski_KATALOG_NAUKOWY_p17_img02.jpeg"],
    "GL-044": ["Kolekcja_Gluchowski_KATALOG_NAUKOWY_p17_img03.jpeg"],
    # GL-045..GL-047 -- brak skanow w PDF (zdjecia z telefonu)
    # Ch VI - 7 Pulk Ulanow (GL-050 usuniety - duplikat GL-001)
    "GL-051": ["Kolekcja_Gluchowski_KATALOG_NAUKOWY_p20_img01.jpeg",
               "Kolekcja_Gluchowski_Katalog_Tematyczny_p12_img01.jpeg"],   # zaproszenie Szwadronu Zapasowego 7 P.Ul.
    "GL-052": ["Kolekcja_Gluchowski_KATALOG_NAUKOWY_p21_img01.jpeg"],
    # GL-053, GL-054 -- brak skanow w PDF (zdjecia z telefonu)
    # Ch VII - Krzysztof Andrzej / AK
    "GL-060": ["Kolekcja_Gluchowski_KATALOG_NAUKOWY_p23_img01.jpeg",
               "Kolekcja_Gluchowski_Katalog_Tematyczny_p14_img01.jpeg"],   # rozkaz dowodcy 2 PP Legionow
    "GL-061": ["Kolekcja_Gluchowski_KATALOG_NAUKOWY_p23_img02.jpeg",
               "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p23_img03.jpeg",
               "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p23_img04.jpeg"],      # Kennkarte - kompletna, 4 strony
    "GL-063": ["Kolekcja_Gluchowski_KATALOG_NAUKOWY_p24_img01.jpeg"],
    "GL-064": ["Kolekcja_Gluchowski_KATALOG_NAUKOWY_p24_img02.jpeg"],
    "GL-065": ["Kolekcja_Gluchowski_KATALOG_NAUKOWY_p25_img01.jpeg"],
    "GL-066": ["Kolekcja_Gluchowski_KATALOG_NAUKOWY_p26_img01.jpeg"],
    "GL-067": ["Kolekcja_Gluchowski_KATALOG_NAUKOWY_p26_img02.jpeg"],
    "GL-068": ["Kolekcja_Gluchowski_KATALOG_NAUKOWY_p27_img01.jpeg"],
    "GL-069": ["Kolekcja_Gluchowski_KATALOG_NAUKOWY_p27_img02.jpeg"],
    # GL-073..GL-078 -- brak skanow w PDF (zdjecia z telefonu)
    # Ch VIII - Szkocja / PSZ na Zachodzie
    "GL-070": ["Kolekcja_Gluchowski_KATALOG_NAUKOWY_p28_img01.jpeg",
               "Kolekcja_Gluchowski_Katalog_Tematyczny_p08_img01.jpeg",    # iluminowany adres pozegnalny od oficerow, IX 1945
               "Kolekcja_Gluchowski_Katalog_Tematyczny_p15_img01.jpeg",    # legitymacja 3 DSK Tobruk
               "Kolekcja_Gluchowski_Katalog_Tematyczny_p15_img02.jpeg"],   # legitymacje odznak pulkowych (7 P.Ul. + 20 P.Ul.)
    "GL-071": ["Kolekcja_Gluchowski_KATALOG_NAUKOWY_p28_img02.jpeg"],
    "GL-072": ["Kolekcja_Gluchowski_KATALOG_NAUKOWY_p28_img03.jpeg"],
    # === SERIA 29z ===
    # Ch IX - Korespondencja jeniecka
    "GL-100": ["Seria_29z_p02_img01.jpeg", "Seria_29z_p02_img02.jpeg"],
    "GL-101": ["Seria_29z_p03_img01.jpeg", "Seria_29z_p03_img02.jpeg"],
    "GL-102": ["Seria_29z_p04_img01.jpeg", "Seria_29z_p04_img02.jpeg"],
    "GL-103": ["Seria_29z_p05_img01.jpeg", "Seria_29z_p05_img02.jpeg"],
    "GL-104": ["Seria_29z_p06_img01.jpeg", "Seria_29z_p06_img02.jpeg"],
    "GL-105": ["Seria_29z_p07_img01.jpeg", "Seria_29z_p07_img02.jpeg"],
    "GL-106": ["Seria_29z_p08_img01.jpeg", "Seria_29z_p08_img02.jpeg"],
    "GL-107": ["Seria_29z_p09_img01.jpeg"],
    "GL-108": ["Seria_29z_p10_img01.jpeg", "Seria_29z_p10_img02.jpeg"],
    # Ch X - Dokumenty obozowe i pamietnik
    "GL-109": ["Seria_29z_p11_img01.jpeg", "Seria_29z_p11_img02.jpeg"],
    "GL-110": ["Seria_29z_p12_img01.jpeg", "Seria_29z_p12_img02.jpeg"],
    "GL-111": ["Seria_29z_p13_img01.jpeg", "Seria_29z_p13_img02.jpeg", "Seria_29z_p13_img03.jpeg", "Seria_29z_p13_img04.jpeg"],
    "GL-112": ["Seria_29z_p14_img01.jpeg", "Seria_29z_p14_img02.jpeg", "Seria_29z_p14_img03.jpeg"],
    "GL-113": ["Seria_29z_p15_img01.jpeg", "Seria_29z_p15_img02.jpeg", "Seria_29z_p15_img03.jpeg"],
    "GL-114": ["Seria_29z_p16_img01.jpeg", "Seria_29z_p16_img02.jpeg"],
    # Ch XI - Wspomnienia i wyzwolenie
    "GL-115": ["Seria_29z_p17_img01.jpeg", "Seria_29z_p17_img02.jpeg"],
    "GL-116": ["Seria_29z_p18_img01.jpeg", "Seria_29z_p18_img02.jpeg"],
    "GL-117": ["Seria_29z_p19_img01.jpeg", "Seria_29z_p19_img02.jpeg"],
    "GL-118": ["Seria_29z_p20_img01.jpeg", "Seria_29z_p20_img02.jpeg"],
    "GL-119": ["Seria_29z_p21_img01.jpeg"],
    "GL-120": ["Seria_29z_p22_img01.jpeg", "Seria_29z_p22_img02.jpeg"],
    # Ch XII - Dokumenty tozsamosci i repatriacja
    "GL-121": ["Seria_29z_p23_img01.jpeg", "Seria_29z_p23_img02.jpeg"],
    "GL-122": ["Seria_29z_p24_img01.jpeg"],
    "GL-123": ["Seria_29z_p25_img01.jpeg"],
    "GL-124": ["Seria_29z_p26_img01.jpeg"],
    "GL-125": ["Seria_29z_p27_img01.jpeg"],
    "GL-126": ["Seria_29z_p28_img01.jpeg", "Seria_29z_p28_img02.jpeg"],
    "GL-127": ["Seria_29z_p29_img01.jpeg", "Seria_29z_p29_img02.jpeg"],
    "GL-128": ["Seria_29z_p30_img01.jpeg"],
    "GL-129": ["Seria_29z_p31_img01.jpeg"],
    "GL-130": ["Seria_29z_p32_img01.jpeg", "Seria_29z_p32_img02.jpeg", "Seria_29z_p32_img03.jpeg", "Seria_29z_p32_img04.jpeg", "Seria_29z_p32_img05.jpeg"],
    "GL-131": ["Seria_29z_p33_img01.jpeg"],
    "GL-132": ["Seria_29z_p34_img01.jpeg"],
    "GL-133": ["Seria_29z_p35_img01.jpeg"],
    "GL-134": ["Seria_29z_p36_img01.jpeg"],
    "GL-135": ["Seria_29z_p37_img01.jpeg"],
}

database.init_db()
conn = database.get_connection()

# Pobierz wszystkie obiekty Głuchowskich
rows = conn.execute("""
    SELECT id, inventory_number, title, category, medium, date_created,
           description, provenance, condition_grade, condition_notes,
           notes, authentication_status, dimensions_notes,
           current_estimated_value, valuation_currency
    FROM collection_objects
    WHERE inventory_number LIKE 'GL-%'
    ORDER BY inventory_number
""").fetchall()

print(f"Znaleziono {len(rows)} obiektów kolekcji Głuchowskich")

# Organizuj w rozdziały
CHAPTERS = {
    "I": {"title": "PON i korzenie walki niepodleglosciowej", "period": "1905-1914", "prefix": "GL-00", "icon": "🏛️",
           "desc": "Polska Organizacja Narodowa, Czestochowa 1914. Rozkaz PON z pieczecia Orla, Legitymacja nr 2 Marjana Gluchowskiego, Afisz zebrania z Sieroszewskim i Kadenem-Bandrowskim."},
    "II": {"title": "Siodemka i Legiony Polskie", "period": "1913-1925", "prefix": "GL-01", "icon": "⚔️",
            "desc": "Zaswiadczenie WBH, wspomnienia o egzaminie u Pilsudskiego, fotokopia Siodemki Beliny, Dyplom Krzyza Legjonowego nr 115 z autografem Pilsudskiego, karykatura Iwankowicza."},
    "III": {"title": "II Rzeczpospolita -- od narodzin do wiceministra", "period": "1918-1939", "prefix": "GL-02", "icon": "🦅",
             "desc": "Rozkaz sprzed Niepodleglosci (5.XI.1918), list Smidlego-Rydza, Krzyz Walecznych z podpisem Sosnkowskiego, dekrety Pilsudski+Moscicki, Foch, Order Rumunii, legitymacja generalska, listy Aleksandry Pilsudskiej."},
    "IV": {"title": "Gen. Sosnkowski -- 50 lat przyjazni", "period": "1913-1964", "prefix": "GL-03", "icon": "🎖️",
            "desc": "Korespondencja emigracyjna z Arundel (Quebec): SPK Kanada, Chicago, 'Pro memoria' z 24 zamowieniami, prace nad historia patrolu Beliny."},
    "V": {"title": "Getto Lodzkie -- swiadectwo i odpowiedzialnosc", "period": "1942-1984", "prefix": "GL-04", "icon": "✡️",
           "desc": "Waluta gettowa (10 Pf. kupon pocztowy, 17.IV.1942), talon nr 6110, korespondencja z Ambasada Izraela, 26 lat poszukiwan muzeum (1958-1984), pierscionek Ajzenmana."},
    "VI": {"title": "7 Pulk Ulanow Lubelskich", "period": "1919-1970", "prefix": "GL-05", "icon": "🐴",
            "desc": "Od Legionow do emigracji: Msza za Jelenia w Wilanowie (1970), nekrologi weteranow z Chicago (1960), Oplatek wigilijny Kola Pulkowego."},
    "VII": {"title": "Krzysztof Andrzej Gluchowski -- historia kompletna", "period": "1928-1945", "prefix": "GL-06", "icon": "🏴󠁧󠁢󠁳󠁣󠁴󠁿",
             "desc": "3 swiadectwa urodzenia, Kennkarte GG, legitymacja AK nr 1112 ps. Jurek/Jures, 3 przepustki AK, list do rodzicow z Powstania (26.VIII.44), odpowiedz Ciotki Waleski, Stalag XI-B, list z obozu."},
    "VIII": {"title": "Album fotograficzny -- PSZ w Szkocji", "period": "1944", "prefix": "GL-07", "icon": "📜",
              "desc": "Album CWL PSZ ze Szkocji: ~35 fotografii, oficerowie, cwiczenia, mecz z RAF, herbatka z gitara. Ofiarowany gen. Gluchowskiemu przez zolnierzy."},
    # === SERIA 29z ===
    "IX": {"title": "Seria 29z: Korespondencja jeniecka", "period": "X.1944-I.1945", "prefix": "GL-10", "icon": "✉️",
            "desc": "Listy, Kriegsgefangenenpost, kartki lacznikowe. Korespondencja miedzy Stalagami XIB, VIF, VIJ. Ojciec Stefan, syn Krzysztof, Zofia Okuszkowa. 8 pozycji."},
    "X": {"title": "Seria 29z: Dokumenty obozowe i pamietnik", "period": "1944-1945", "prefix": "GL-11", "icon": "📓",
           "desc": "PAMIETNIK OBOZOWY 15-letniego powstanca (15 kart!), Gesundheitsblatt, kalendarz kampanii wloskiej, list wigilijny na zeszycie IHK Gladbach. Najcenniejsze pozycje serii."},
    "XI": {"title": "Seria 29z: Wspomnienia i wyzwolenie", "period": "V-VI.1945", "prefix": "GL-12", "icon": "🕊️",
            "desc": "Wspomnienie o Stryju Lechu, listy z Dusseldorfu na papierze Emil Schroder & Co., sprawozdanie wojenne -- dokument-klucz calej kolekcji. Smierc Lecha, rana w Gladbach."},
    "XII": {"title": "Seria 29z: Dokumenty tozsamosci i repatriacja", "period": "IV-VII.1945", "prefix": "GL-13", "icon": "🪪",
             "desc": "Card of Identity, Carte de Rapatrie, zaswiadczenia AK Paryz, Fiche de Transport, przepustki, skierowania. Droga Krzysztofa z Niemiec przez Francje do Wloch. Zaswiadczenia KW plk. Klepacza i Wachnowskiego. Swiadectwo ukonczenia gimnazjum 1946."},
}

# Mapowanie GL-1xx do rozdzialow Serii 29z
_29Z_CHAPTER_MAP = {
    "IX":  ["GL-100","GL-101","GL-102","GL-103","GL-104","GL-105","GL-106","GL-107","GL-108"],
    "X":   ["GL-109","GL-110","GL-111","GL-112","GL-113","GL-114"],
    "XI":  ["GL-115","GL-116","GL-117","GL-118","GL-119","GL-120"],
    "XII": ["GL-121","GL-122","GL-123","GL-124","GL-125","GL-126","GL-127","GL-128","GL-129","GL-130","GL-131","GL-132","GL-133","GL-134","GL-135"],
}
# GL-073..GL-078 to rozdzial VII (prefix GL-07 kolidowblby z VIII)
_EXPLICIT_CH_MAP = {
    # GL-027..GL-039 to rozdzial III (prefix GL-03 koliduje z IV)
    "GL-027": "III", "GL-028": "III", "GL-029": "III",
    "GL-032": "III", "GL-033": "III", "GL-034": "III",
    "GL-035": "III", "GL-036": "III", "GL-037": "III",
    "GL-038": "III", "GL-039": "III",
    # GL-073..GL-078 to rozdzial VII (prefix GL-07 koliduje z VIII)
    "GL-073": "VII", "GL-074": "VII", "GL-075": "VII",
    "GL-076": "VII", "GL-077": "VII", "GL-078": "VII",
}
_29z_inv_to_ch = {}
for _ch, _invs in _29Z_CHAPTER_MAP.items():
    for _inv in _invs:
        _29z_inv_to_ch[_inv] = _ch

# Mapuj obiekty do rozdzialow
chapter_objects = {k: [] for k in CHAPTERS}
for row in rows:
    inv = row["inventory_number"]
    # Explicit mapping (GL-073..GL-078, Seria 29z)
    if inv in _EXPLICIT_CH_MAP:
        chapter_objects[_EXPLICIT_CH_MAP[inv]].append(dict(row))
        continue
    if inv in _29z_inv_to_ch:
        chapter_objects[_29z_inv_to_ch[inv]].append(dict(row))
        continue
    # Original series -- prefix matching
    for ch_key, ch_data in CHAPTERS.items():
        if inv.startswith(ch_data["prefix"]):
            chapter_objects[ch_key].append(dict(row))
            break

# ============================================================
# BADANIE RYNKU -- DANE REFERENCYJNE Z AUKCJI 2019-2026
# ============================================================
# Zrodla: RR Auction, Heritage Auctions, DESA Unicum, OneBid/WDA-MiM,
#         eMedals, Invaluable, Kedem Auction House, Bonhams, Allegro archiwum,
#         PCGS ValueView, CoinStrail, Numista
#
# KLUCZOWE PUNKTY CENOWE (zrealizowane transakcje):
#
# AUTOGRAFY PILSUDSKIEGO:
#   - RR Auction: fotografia z autografem Pilsudskiego = $963 USD (~4,500 PLN)
#     Maly format 3.75x5", sredni stan. Bylo to DRUGIE w historii RR.
#     Dyplom urzedowy z pelnym podpisem > zdjecie: mnoznik x3-x8.
#     GL-010 (dyplom KL nr 115 + foto): estymacja 25,000-60,000 PLN
#     GL-039 (pocztowka z Krynicy z autografem): 10,000-25,000 PLN
#
# KRZYZ WALECZNYCH (medal fizyczny):
#   - OneBid/WCN: KW 1920 emisja oryginalna = 100-480 PLN (sam medal)
#   - Z legitymacja + proweniencja generala: mnoznik x20-x50
#   - GL-021 (KW + proweniencja): 3,000-8,000 PLN
#   - GL-034 (legitymacja KW z podpisem Sosnkowskiego): 8,000-20,000 PLN
#
# WALUTA GETTA LODZKIEGO:
#   - 10 Pf kupon pocztowy: srednia 960 USD (~4,500 PLN), rekord WDA 17,250 PLN
#   - 10 Mark aluminum 1943: srednia 200 USD (~940 PLN), rekord WDA 11,500 PLN
#   - 20 Mark aluminum 1943: srednia 1,800 USD (~8,400 PLN), rekord Marciniak 20,000 PLN
#   - 5 Mark aluminum 1943: srednia 200 USD, rekord WDA 3,600 PLN
#   - Papierowe kupony/talony: rzadsze niz monety, slabiej wyceniane na rynku
#   - KONTEKST MUZEALNY: komplet z proweniencja + korespondencja = mnoznik x3-x5
#
# KENNKARTE GG:
#   - eBay/Invaluable: zwykla Kennkarte = 50-200 USD
#   - Kennkarte zydowska (zolta) = 500-2,000 USD
#   - Kennkarte z proweniencja AK + Powstanie = mnoznik x5-x10
#   - GL-061 (kompletna 4-stronnicowa, AK-owiec): 3,000-8,000 PLN
#
# DOKUMENTY POWSTANIA WARSZAWSKIEGO:
#   - OneBid: koperta poczty polowej PW 1944 = 800-3,000 PLN
#   - OneBid: list poczty harcerskiej PW = 1,200-4,000 PLN
#   - Legitymacja AK oryginal 1944: 2,000-8,000 PLN (Allegro archiwum)
#   - Przepustka AK oryginal: ekstremalnie rzadka, brak porownawczych transakcji
#   - Muzeum Powstania Warszawskiego kupilo listy na aukcji w Dusseldorfie (2008)
#   - GL-067 (legitymacja AK nr 1112): 50,000-120,000 PLN -- UNIKAT
#
# DOKUMENTY OBOZOWE (Stalag):
#   - eBay: Personalkarte jenca = 30-150 USD (zwykla, bez kontekstu)
#   - Z kontekstem AK + Powstanie: mnoznik x10-x20
#   - Pamietnik obozowy "Great Escape" Stalag Luft III = $17,827 USD (Invaluable)
#   - GL-111 (pamietnik 15-latka, 15 kart): 25,000-60,000 PLN
#
# ORDERY I ODZNACZENIA:
#   - Order Gwiazdy Rumunii (Kawaler): 100-300 EUR na eMedals/Katz
#   - Z dyplomem od Krola Ferdynanda: x5-x10
#   - Legia Honorowa (Kawaler): 200-600 EUR sam order
#   - Z zaproszeniem od Focha na Plac Saski: x10-x20
#
# ARCHIWUM RODZINNE (calosciowe):
#   - Instytut Pilsudskiego (Nowy Jork): aukcje spuscizn generalskich
#   - Hoover Institution: zakup archiwow polskich z II WS
#   - PREMIA ZA KOMPLETNOSC: 30-50% ponad sume jednostkowa
#   - PREMIA ZA CIAGLOSC PROWENIENCJI: dodatkowe 20-30%
#   - 4 generacje, 120+ pozycji, 8 rozdzialow tematycznych: premia 50-80%
# ============================================================

# Wyceny (na podstawie badania rynku -- indywidualne per dokument)
VALUATIONS = {
    # Ch I -- PON (1914)
    # Dokumenty PON z 1914 to absolutna rzadkosc -- pierwsze tygodnie I WS.
    # Brak bezposrednich comparables na rynku. Wycena muzealna.
    "GL-001": {"min_pln": 5000, "max_pln": 12000, "tier": "A"},   # tablica pamiatkowa AK Jelen -- kontekst pulkowy
    "GL-002": {"min_pln": 2000, "max_pln": 5000, "tier": "B+"},   # rozkaz PON z pieczecia Orla -- unikat, brak comparables
    "GL-003": {"min_pln": 10000, "max_pln": 25000, "tier": "A"},  # Legitymacja PON nr 2 -- JEDEN Z PIERWSZYCH w historii
    "GL-004": {"min_pln": 1500, "max_pln": 3500, "tier": "B"},    # afisz zebrania -- druk, mniejsza rzadkosc

    # Ch II -- Legiony
    # Ref: RR Auction -- foto Pilsudskiego z podpisem = $963 (maly format, sredni stan)
    # Dyplom urzedowy z pelnym podpisem Pilsudskiego >> zdjecie portretowe
    "GL-010": {"min_pln": 25000, "max_pln": 60000, "tier": "A"},  # dyplom KL nr 115 + podpis Pilsudskiego + foto atelier
    "GL-012": {"min_pln": 2000, "max_pln": 6000, "tier": "B"},    # fotokopia Siodemki -- reprodukcja, nie oryginal
    "GL-013": {"min_pln": 5000, "max_pln": 12000, "tier": "A"},   # zaswiadczenie WBH -- dokument sluzby legionowej
    "GL-014": {"min_pln": 6000, "max_pln": 18000, "tier": "A"},   # wspomnienia o egzaminie u Pilsudskiego -- manuskrypt
    "GL-015": {"min_pln": 3000, "max_pln": 8000, "tier": "B+"},   # wykaz sluchaczy Szkoly Strzeleckiego
    "GL-016": {"min_pln": 4000, "max_pln": 10000, "tier": "B+"},  # foto konspiracyjna Belina -- ikonografia legionowa
    "GL-017": {"min_pln": 2000, "max_pln": 5000, "tier": "B"},    # karykatura Iwankowicza

    # Ch III -- II RP
    # Ref: Sosnkowski -- brak comparables na rynku (korespondencja prywatna generala)
    # Ref: Smigly-Rydz, Pilsudska -- listy osob z najblizszego kregu Pilsudskiego
    "GL-020": {"min_pln": 12000, "max_pln": 30000, "tier": "A"},  # list Sosnkowskiego z Kanady
    "GL-021": {"min_pln": 3000, "max_pln": 8000, "tier": "B+"},   # KW medal -- ref: WCN 100-480 PLN sam medal, +proweniencja
    "GL-022": {"min_pln": 18000, "max_pln": 45000, "tier": "A"},  # legitymacja generalska kompletna 1928-1937 -- UNIKAT
    "GL-025": {"min_pln": 10000, "max_pln": 25000, "tier": "A"},  # dekret Prezydenta -- mianowanie d-cy OK
    "GL-026": {"min_pln": 8000, "max_pln": 20000, "tier": "A"},   # dekret -- mianowanie I Wiceministra
    "GL-027": {"min_pln": 10000, "max_pln": 25000, "tier": "A"},  # rozkaz 5.XI.1918 -- DZIEN PRZED Niepodlegloscia!
    "GL-028": {"min_pln": 2000, "max_pln": 5000, "tier": "B"},    # pokwitowanie 600 koron
    "GL-029": {"min_pln": 15000, "max_pln": 35000, "tier": "A"},  # list Smidlego-Rydza -- Zamek Krolewski
    "GL-032": {"min_pln": 8000, "max_pln": 20000, "tier": "A"},   # Order Gwiazdy Rumunii -- ref: Katz 100-300 EUR + dyplom
    "GL-033": {"min_pln": 12000, "max_pln": 30000, "tier": "A"},  # zaproszenie Focha -- Legia Honorowa, Plac Saski
    "GL-034": {"min_pln": 8000, "max_pln": 20000, "tier": "A"},   # legitymacja KW z podpisem Sosnkowskiego
    "GL-035": {"min_pln": 5000, "max_pln": 12000, "tier": "B+"},  # rozkaz pogrzeb Pilsudskiego
    "GL-036": {"min_pln": 5000, "max_pln": 12000, "tier": "B+"},  # foto uroczystosc sztandaru + Smigly-Rydz
    "GL-037": {"min_pln": 10000, "max_pln": 25000, "tier": "A"},  # list Aleksandry Pilsudskiej -- monogram P
    "GL-038": {"min_pln": 18000, "max_pln": 45000, "tier": "A"},  # list wdowy Pilsudskiej 1935 -- kondolencje
    "GL-039": {"min_pln": 10000, "max_pln": 25000, "tier": "A"},  # pocztowka Pilsudskiego z Krynicy -- AUTOGRAF

    # Ch IV -- Sosnkowski / Emigracja
    "GL-030": {"min_pln": 3000, "max_pln": 8000, "tier": "B+"},   # lista zlecen organizacji polonijnych
    "GL-031": {"min_pln": 3000, "max_pln": 8000, "tier": "B+"},   # kontynuacja listu -- sprawy wydawnicze

    # Ch V -- Getto Lodzkie
    # Ref: 10 Pf kupon pocztowy srednia 960 USD / rekord 17,250 PLN (WDA-MiM)
    # Ref: 20 Mark aluminum srednia 1,800 USD / rekord 20,000 PLN (Marciniak)
    # Ref: talony papierowe -- rzadsze niz monety, mniej comparables
    "GL-040": {"min_pln": 5000, "max_pln": 15000, "tier": "A"},   # list do Ambasady Izraela -- kontekst historyczny
    "GL-041": {"min_pln": 5000, "max_pln": 15000, "tier": "A"},   # kupon pocztowy 10 Pf -- ref: srednia 4,500 PLN
    "GL-042": {"min_pln": 3000, "max_pln": 8000, "tier": "B+"},   # talon mleczarski -- papierowy, rzadszy niz monety
    "GL-043": {"min_pln": 800, "max_pln": 2000, "tier": "B"},     # koperta z notatkami -- material archiwalny
    "GL-044": {"min_pln": 8000, "max_pln": 20000, "tier": "A"},   # odpowiedz Ambasady Izraela -- Kidron, 1958
    "GL-045": {"min_pln": 3000, "max_pln": 8000, "tier": "B+"},   # list do Herziga Ohio -- inwentarz
    "GL-046": {"min_pln": 2000, "max_pln": 5000, "tier": "B"},    # list z Rochester 1984
    "GL-047": {"min_pln": 500, "max_pln": 1500, "tier": "B"},     # fotokopie Tychsena -- reprodukcje

    # Ch VI -- 7 Pulk Ulanow (GL-050 usuniety)
    "GL-051": {"min_pln": 2000, "max_pln": 5000, "tier": "B+"},   # Msza za Jelenia Wilanow 1970
    "GL-052": {"min_pln": 1500, "max_pln": 4000, "tier": "B"},    # nekrolog Lorensa -- Chicago
    "GL-053": {"min_pln": 500, "max_pln": 1500, "tier": "B"},     # nekrolog Lewandowskiego
    "GL-054": {"min_pln": 500, "max_pln": 1500, "tier": "B"},     # oplatek wigilijny

    # Ch VII -- Krzysztof Andrzej / AK / Powstanie / Stalag
    # Ref: koperta poczty polowej PW = 800-3,000 PLN (OneBid)
    # Ref: legitymacja AK 1944 = 2,000-8,000 PLN (Allegro archiwum)
    # Ref: Kennkarte zwykla = 50-200 USD; z kontekstem AK = x5-x10
    # Ref: Personalkarte zwykla = 30-150 USD; z kontekstem AK = x10-x20
    "GL-060": {"min_pln": 5000, "max_pln": 15000, "tier": "A"},   # akcesoria mundurowe -- portepee, galon, miniatura
    "GL-061": {"min_pln": 3000, "max_pln": 8000, "tier": "B+"},   # Kennkarte kompletna -- ref: 50-200 USD zwykla, +AK kontekst
    "GL-063": {"min_pln": 8000, "max_pln": 20000, "tier": "A"},   # list wojenny -- Krychu, kartka w kratke
    "GL-064": {"min_pln": 8000, "max_pln": 20000, "tier": "A"},   # list z Powstania 26.VIII.1944 -- dzien 26.
    "GL-065": {"min_pln": 25000, "max_pln": 60000, "tier": "A"},  # przepustka AK 29.IX -- 3 dni przed kapitulacja
    "GL-066": {"min_pln": 15000, "max_pln": 35000, "tier": "A"},  # rozkaz awansu + KW -- Grupa Polnoc nr 24
    "GL-067": {"min_pln": 50000, "max_pln": 120000, "tier": "A"}, # legitymacja AK nr 1112 -- ABSOLUTNY UNIKAT
    "GL-068": {"min_pln": 5000, "max_pln": 12000, "tier": "A"},   # tag jeniecki Stalag XI-B -- ref: 30-150 USD + AK kontekst
    "GL-069": {"min_pln": 8000, "max_pln": 20000, "tier": "A"},   # Personalkarte -- ref: 30-150 USD + AK + Powstanie
    "GL-073": {"min_pln": 3000, "max_pln": 8000, "tier": "B+"},   # 3 swiadectwa urodzenia -- GG + RP, serie konspiracyjna
    "GL-074": {"min_pln": 8000, "max_pln": 20000, "tier": "A"},   # przepustka AK 18.IX -- dzien 49. Powstania
    "GL-075": {"min_pln": 10000, "max_pln": 25000, "tier": "A"},  # przepustka AK na 2 osoby -- towarzysz Piotr
    "GL-076": {"min_pln": 3000, "max_pln": 8000, "tier": "B+"},   # kartka lacznikowa -- system komunikacji PW
    "GL-077": {"min_pln": 5000, "max_pln": 12000, "tier": "A"},   # odpowiedz Ciotki Waleski -- KORESPONDENCJA W OBIE STRONY
    "GL-078": {"min_pln": 5000, "max_pln": 12000, "tier": "A"},   # list z obozu -- 'Trzymam sie do mnie!'

    # Ch VIII -- Album Szkocja
    # Ref: albumy fotograficzne PSZ -- brak bezposrednich comparables
    # Albumy wojskowe z epoki: 2,000-10,000 PLN na DESA/Rara Avis
    "GL-070": {"min_pln": 8000, "max_pln": 20000, "tier": "A"},   # album str. 1 -- odprawy oficerskie
    "GL-071": {"min_pln": 4000, "max_pln": 10000, "tier": "B+"},  # album str. 2 -- cwiczenia polowe
    "GL-072": {"min_pln": 3000, "max_pln": 8000, "tier": "B+"},   # album str. 3 -- zdjecia grupowe

    # === SERIA 29z ===
    # Ch IX -- Korespondencja jeniecka
    # Ref: Kriegsgefangenenpost polskich jencow -- niszowy rynek, 200-800 PLN per karta
    # Z kontekstem AK + Powstanie + rodzina generala: x5-x10
    "GL-100": {"min_pln": 3000, "max_pln": 8000, "tier": "B+"},
    "GL-101": {"min_pln": 2000, "max_pln": 6000, "tier": "B+"},
    "GL-102": {"min_pln": 4000, "max_pln": 10000, "tier": "A"},
    "GL-103": {"min_pln": 3000, "max_pln": 8000, "tier": "B+"},
    "GL-104": {"min_pln": 8000, "max_pln": 20000, "tier": "A"},   # list do Polish War Office London
    "GL-105": {"min_pln": 5000, "max_pln": 12000, "tier": "A"},
    "GL-106": {"min_pln": 4000, "max_pln": 10000, "tier": "B+"},
    "GL-107": {"min_pln": 800, "max_pln": 2500, "tier": "B"},     # fotografie terenu Stalagu
    "GL-108": {"min_pln": 800, "max_pln": 2000, "tier": "B"},     # fotokopia

    # Ch X -- Dokumenty obozowe i pamietnik
    # Ref: pamietnik "Great Escape" Stalag Luft III = $17,827 (Invaluable/Bonhams)
    # Pamietnik 15-letniego powstanca (!) -- jeszcze rzadszy kontekst
    "GL-109": {"min_pln": 1500, "max_pln": 4000, "tier": "B+"},   # kalendarz kampanii wloskiej
    "GL-110": {"min_pln": 1200, "max_pln": 3000, "tier": "B"},    # Gesundheitsblatt
    "GL-111": {"min_pln": 30000, "max_pln": 70000, "tier": "A"},  # PAMIETNIK OBOZOWY 15 kart -- ref: $17,827 Great Escape
    "GL-112": {"min_pln": 6000, "max_pln": 15000, "tier": "A"},   # list wigilijny na zeszycie IHK
    "GL-113": {"min_pln": 3000, "max_pln": 8000, "tier": "A"},    # plan taktyczny Mokotowa
    "GL-114": {"min_pln": 3000, "max_pln": 8000, "tier": "B+"},   # wspomnienie o Stryju Lechu

    # Ch XI -- Wspomnienia i wyzwolenie
    "GL-115": {"min_pln": 3000, "max_pln": 8000, "tier": "B+"},
    "GL-116": {"min_pln": 18000, "max_pln": 40000, "tier": "A"},  # sprawozdanie wojenne -- dokument-klucz
    "GL-117": {"min_pln": 15000, "max_pln": 35000, "tier": "A"},  # cd. sprawozdania -- smierc Lecha
    "GL-118": {"min_pln": 1500, "max_pln": 4000, "tier": "B"},    # druk Rodacy
    "GL-119": {"min_pln": 5000, "max_pln": 12000, "tier": "A"},   # Card of Identity
    "GL-120": {"min_pln": 1200, "max_pln": 3000, "tier": "B"},    # ephemery repatriacyjne

    # Ch XII -- Dokumenty tozsamosci i repatriacja
    "GL-121": {"min_pln": 4000, "max_pln": 10000, "tier": "A"},   # Carte de Rapatrie
    "GL-122": {"min_pln": 8000, "max_pln": 20000, "tier": "A"},   # zaswiadczenie AK Paryz
    "GL-123": {"min_pln": 2000, "max_pln": 5000, "tier": "B+"},   # Fiche de Transport
    "GL-124": {"min_pln": 3000, "max_pln": 8000, "tier": "B+"},   # list Radomyskiego
    "GL-125": {"min_pln": 3000, "max_pln": 8000, "tier": "B+"},   # skierowanie Ambasady RP
    "GL-126": {"min_pln": 800, "max_pln": 2000, "tier": "B"},     # plan Marsylii
    "GL-127": {"min_pln": 3000, "max_pln": 8000, "tier": "B+"},   # skierowanie na rentgen
    "GL-128": {"min_pln": 2000, "max_pln": 5000, "tier": "B"},    # przepustka Gimnazjum 3 DSK
    "GL-129": {"min_pln": 2000, "max_pln": 5000, "tier": "B"},    # przepustka Punktu Przesylkowego
    "GL-130": {"min_pln": 18000, "max_pln": 40000, "tier": "A"},  # zeszyt szkolny -- komplet materialow edukacyjnych
    "GL-131": {"min_pln": 8000, "max_pln": 20000, "tier": "A"},   # esej rocznicowy 'Rok temu'
    "GL-132": {"min_pln": 5000, "max_pln": 12000, "tier": "A"},   # esej polemiczny
    "GL-133": {"min_pln": 10000, "max_pln": 25000, "tier": "A"},  # zaswiadczenia KW plk. Klepacza
    "GL-134": {"min_pln": 12000, "max_pln": 30000, "tier": "A"},  # zaswiadczenie plk. Wachnowskiego
    "GL-135": {"min_pln": 5000, "max_pln": 12000, "tier": "A"},   # swiadectwo ukonczenia gimnazjum 1946
}

# Potencjalni nabywcy
BUYERS = {
    "museums": [
        {"name": "Muzeum Jozefa Pilsudskiego w Sulejowku", "interest": "Legiony, Krzyz Legjonowy, II RP", "chapters": ["II", "III"]},
        {"name": "Muzeum Wojska Polskiego, Warszawa", "interest": "Cala kolekcja wojskowa: legitymacja generalska, KW, akcesoria mundurowe", "chapters": ["I", "II", "III", "IV", "VI", "VII", "VIII"]},
        {"name": "Muzeum Powstania Warszawskiego", "interest": "Legitymacja AK, przepustka AK, listy z Powstania, Kennkarte, Stalag XI-B", "chapters": ["I", "VII"]},
        {"name": "Muzeum POLIN, Warszawa", "interest": "Waluta gettowa, talony zywnosciowe, korespondencja z Ambasada Izraela", "chapters": ["V"]},
        {"name": "Yad Vashem, Jerozolima", "interest": "Dokumenty Getta Lodzkiego -- wskazani przez Ambasade Izraela w 1958!", "chapters": ["V"]},
        {"name": "USHMM (US Holocaust Memorial Museum), Waszyngton", "interest": "Kupon pocztowy 10 Pf., talon mleczarski, korespondencja Gluchowski-Kidron", "chapters": ["V"]},
        {"name": "Muzeum Tradycji 7 Pulku Ulanow Lubelskich", "interest": "Tablica Powstania, Msza sw. Wilanow, nekrolog plut. Lorensa", "chapters": ["I", "VI"]},
        {"name": "Muzeum Kawalerii, Grudziadz", "interest": "7 Pulk Ulanow, portepee, dokumenty kawaleryjskie", "chapters": ["VI"]},
        {"name": "Instytut Pamieci Narodowej (IPN)", "interest": "Legitymacja AK, przepustka AK, rozkazy Grupy Polnoc, Kennkarte GG", "chapters": ["III", "IV", "V", "VII"]},
        {"name": "Centralne Archiwum Wojskowe, Warszawa", "interest": "Legitymacja oficerska gen. bryg., Krzyz Legjonowy, dokumenty sluzby", "chapters": ["II", "III", "IV", "VI"]},
        {"name": "Muzeum Historii Lodzi", "interest": "Kupon pocztowy getta, talon mleczarski nr 6110, Litzmannstadt-Getto", "chapters": ["V"]},
        {"name": "National War Museum Scotland, Edinburgh", "interest": "Album fotograficzny PSZ w Szkocji: plk Koper, Krajak, Wroblewski", "chapters": ["VIII"]},
    ],
    "auction_houses": [
        {"name": "DESA Unicum, Warszawa", "type": "Największy dom aukcyjny w Polsce  - militaria, dokumenty historyczne"},
        {"name": "Antykwariat Rara Avis, Kraków", "type": "Specjalizacja: stare druki, rękopisy, dokumenty historyczne"},
        {"name": "Dom Aukcyjny Libra, Kraków", "type": "Militaria, odznaczenia, dokumenty wojskowe"},
        {"name": "Sopocki Dom Aukcyjny", "type": "Militaria, fotografia historyczna"},
        {"name": "Rempex / Abbey House", "type": "Dokumenty historyczne, autografy"},
    ],
}

# ============================================================
# GENEROWANIE HTML
# ============================================================

total_min = sum(v["min_pln"] for v in VALUATIONS.values())
total_max = sum(v["max_pln"] for v in VALUATIONS.values())
tier_a_count = sum(1 for v in VALUATIONS.values() if v["tier"] == "A")

html = f"""<!DOCTYPE html>
<html lang="pl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Kolekcja Głuchowskich  - Katalog Archiwum Wojskowego 1905-1945</title>
<style>
:root {{
    --bg: #0a0a0f;
    --surface: #12121a;
    --card: #1a1a25;
    --border: #2a2a3a;
    --gold: #d4a853;
    --gold-dim: #8b7335;
    --text: #e8e6e3;
    --text-dim: #9a9a9a;
    --red: #c0392b;
    --green: #27ae60;
    --blue: #2980b9;
    --purple: #8e44ad;
}}
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{
    font-family: Georgia, 'Times New Roman', serif;
    background: var(--bg);
    color: var(--text);
    line-height: 1.7;
}}
.container {{ max-width: 1200px; margin: 0 auto; padding: 20px; }}

/* HEADER */
.hero {{
    text-align: center;
    padding: 60px 20px;
    background: linear-gradient(180deg, #151520 0%, var(--bg) 100%);
    border-bottom: 2px solid var(--gold);
    margin-bottom: 40px;
}}
.hero h1 {{
    font-size: 2.4em;
    color: var(--gold);
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-bottom: 10px;
}}
.hero .subtitle {{
    font-size: 1.2em;
    color: var(--text-dim);
    font-style: italic;
    margin-bottom: 20px;
}}
.hero .family-line {{
    font-size: 0.95em;
    color: var(--text-dim);
    max-width: 800px;
    margin: 0 auto;
    line-height: 1.8;
}}

/* STATS BAR */
.stats-bar {{
    display: flex;
    justify-content: center;
    gap: 40px;
    padding: 25px;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 8px;
    margin-bottom: 40px;
    flex-wrap: wrap;
}}
.stat {{ text-align: center; }}
.stat-number {{ font-size: 2em; color: var(--gold); font-weight: bold; }}
.stat-label {{ font-size: 0.85em; color: var(--text-dim); text-transform: uppercase; letter-spacing: 1px; }}

/* NAV */
.chapter-nav {{
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-bottom: 40px;
    justify-content: center;
}}
.chapter-nav a {{
    padding: 8px 16px;
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 6px;
    color: var(--text);
    text-decoration: none;
    font-size: 0.9em;
    transition: all 0.2s;
}}
.chapter-nav a:hover {{ border-color: var(--gold); color: var(--gold); }}

/* CHAPTER */
.chapter {{
    margin-bottom: 50px;
    border: 1px solid var(--border);
    border-radius: 10px;
    overflow: hidden;
}}
.chapter-header {{
    padding: 25px 30px;
    background: linear-gradient(135deg, #1a1a28 0%, #15152a 100%);
    border-bottom: 2px solid var(--gold-dim);
}}
.chapter-header h2 {{
    font-size: 1.5em;
    color: var(--gold);
    margin-bottom: 5px;
}}
.chapter-header .period {{
    font-size: 0.95em;
    color: var(--text-dim);
    font-style: italic;
}}
.chapter-header .chapter-desc {{
    font-size: 0.9em;
    color: var(--text-dim);
    margin-top: 10px;
    line-height: 1.6;
}}
.chapter-body {{ padding: 20px; }}

/* OBJECT CARD */
.object-card {{
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 20px 25px;
    margin-bottom: 15px;
    transition: border-color 0.2s;
}}
.object-card:hover {{ border-color: var(--gold-dim); }}
.object-card .obj-header {{
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    margin-bottom: 10px;
    flex-wrap: wrap;
    gap: 10px;
}}
.object-card .inv-number {{
    font-family: 'Courier New', monospace;
    color: var(--gold);
    font-size: 0.85em;
    background: rgba(212,168,83,0.1);
    padding: 2px 8px;
    border-radius: 4px;
}}
.object-card .obj-title {{
    font-size: 1.15em;
    color: var(--text);
    font-weight: bold;
    flex: 1;
    min-width: 300px;
}}
.object-card .tier-badge {{
    padding: 3px 10px;
    border-radius: 4px;
    font-size: 0.8em;
    font-weight: bold;
    text-transform: uppercase;
}}
.tier-A {{ background: rgba(192,57,43,0.2); color: #e74c3c; border: 1px solid #c0392b; }}
.tier-Bplus {{ background: rgba(41,128,185,0.2); color: #3498db; border: 1px solid #2980b9; }}
.tier-B {{ background: rgba(39,174,96,0.2); color: #2ecc71; border: 1px solid #27ae60; }}

.object-card .obj-meta {{
    display: flex;
    gap: 20px;
    flex-wrap: wrap;
    font-size: 0.85em;
    color: var(--text-dim);
    margin-bottom: 10px;
}}
.object-card .obj-meta span {{ white-space: nowrap; }}
.object-card .obj-desc {{
    font-size: 0.92em;
    color: var(--text-dim);
    line-height: 1.7;
    margin-bottom: 10px;
}}
.object-card .obj-value {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-top: 10px;
    border-top: 1px solid var(--border);
    flex-wrap: wrap;
    gap: 10px;
}}
.object-card .price-range {{
    font-size: 1.1em;
    color: var(--gold);
    font-weight: bold;
}}
.object-card .condition {{
    font-size: 0.8em;
    padding: 2px 8px;
    border-radius: 4px;
    text-transform: uppercase;
}}
.cond-very-good {{ background: rgba(39,174,96,0.2); color: #2ecc71; }}
.cond-good {{ background: rgba(41,128,185,0.2); color: #3498db; }}
.cond-fair {{ background: rgba(243,156,18,0.2); color: #f39c12; }}

.object-card .notes-box {{
    margin-top: 8px;
    padding: 8px 12px;
    background: rgba(212,168,83,0.05);
    border-left: 3px solid var(--gold-dim);
    font-size: 0.85em;
    color: var(--text-dim);
    font-style: italic;
}}

/* OBJECT IMAGES (per-card) */
.obj-content {{
    display: flex;
    gap: 20px;
    align-items: flex-start;
}}
.obj-images {{
    flex: 0 0 auto;
    display: flex;
    flex-direction: column;
    gap: 8px;
}}
.obj-images img {{
    width: 220px;
    height: auto;
    max-height: 280px;
    object-fit: cover;
    border-radius: 6px;
    border: 1px solid var(--border);
    cursor: pointer;
    transition: border-color 0.2s, transform 0.2s;
}}
.obj-images img:hover {{
    border-color: var(--gold);
    transform: scale(1.02);
}}
.obj-text {{
    flex: 1;
    min-width: 0;
}}
@media (max-width: 768px) {{
    .obj-content {{ flex-direction: column; }}
    .obj-images img {{ width: 100%; max-height: 200px; }}
}}

/* BUYERS SECTION */
.buyers-section {{
    margin-top: 50px;
    border: 1px solid var(--border);
    border-radius: 10px;
    overflow: hidden;
}}
.buyers-section h2 {{
    padding: 20px 30px;
    background: linear-gradient(135deg, #1a1a28 0%, #15152a 100%);
    color: var(--gold);
    border-bottom: 2px solid var(--gold-dim);
    font-size: 1.4em;
}}
.buyers-body {{ padding: 20px; }}
.buyer-card {{
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 15px 20px;
    margin-bottom: 10px;
}}
.buyer-card h3 {{ color: var(--text); font-size: 1.05em; margin-bottom: 5px; }}
.buyer-card .interest {{ font-size: 0.88em; color: var(--text-dim); }}
.buyer-card .chapters-tags {{ margin-top: 8px; display: flex; gap: 5px; flex-wrap: wrap; }}
.buyer-card .ch-tag {{
    padding: 2px 8px;
    background: rgba(212,168,83,0.1);
    border: 1px solid var(--gold-dim);
    border-radius: 4px;
    font-size: 0.75em;
    color: var(--gold);
}}

/* SUMMARY */
.summary-section {{
    margin-top: 50px;
    padding: 30px;
    background: var(--surface);
    border: 2px solid var(--gold-dim);
    border-radius: 10px;
    text-align: center;
}}
.summary-section h2 {{ color: var(--gold); font-size: 1.4em; margin-bottom: 15px; }}
.summary-section .total-value {{
    font-size: 2em;
    color: var(--gold);
    font-weight: bold;
    margin: 15px 0;
}}
.summary-section .disclaimer {{
    font-size: 0.85em;
    color: var(--text-dim);
    font-style: italic;
    max-width: 600px;
    margin: 15px auto 0;
}}

/* PROVENANCE */
.provenance-box {{
    margin-top: 50px;
    padding: 30px;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 10px;
}}
.provenance-box h2 {{ color: var(--gold); font-size: 1.3em; margin-bottom: 15px; }}
.provenance-box p {{ color: var(--text-dim); font-size: 0.95em; margin-bottom: 10px; line-height: 1.7; }}
.timeline {{
    margin-top: 20px;
    padding-left: 30px;
    border-left: 2px solid var(--gold-dim);
}}
.timeline-item {{
    position: relative;
    padding: 10px 0 10px 20px;
}}
.timeline-item::before {{
    content: '';
    position: absolute;
    left: -26px;
    top: 16px;
    width: 10px;
    height: 10px;
    background: var(--gold);
    border-radius: 50%;
}}
.timeline-item .year {{ color: var(--gold); font-weight: bold; }}
.timeline-item .event {{ color: var(--text-dim); font-size: 0.9em; }}

/* FOOTER */
.footer {{
    margin-top: 60px;
    padding: 20px;
    text-align: center;
    border-top: 1px solid var(--border);
    color: var(--text-dim);
    font-size: 0.85em;
}}

/* IMAGE GALLERY */
.chapter-gallery {{
    display: flex;
    gap: 10px;
    overflow-x: auto;
    padding: 15px 0 20px;
    margin-bottom: 10px;
    scrollbar-width: thin;
    scrollbar-color: var(--gold-dim) var(--surface);
}}
.chapter-gallery::-webkit-scrollbar {{ height: 6px; }}
.chapter-gallery::-webkit-scrollbar-track {{ background: var(--surface); border-radius: 3px; }}
.chapter-gallery::-webkit-scrollbar-thumb {{ background: var(--gold-dim); border-radius: 3px; }}
.gallery-thumb {{
    flex: 0 0 auto;
    width: 180px;
    height: 130px;
    border-radius: 6px;
    object-fit: cover;
    border: 1px solid var(--border);
    cursor: pointer;
    transition: border-color 0.2s, transform 0.2s;
}}
.gallery-thumb:hover {{
    border-color: var(--gold);
    transform: scale(1.03);
}}

/* LIGHTBOX */
.lightbox-overlay {{
    display: none;
    position: fixed;
    inset: 0;
    background: rgba(0,0,0,0.92);
    z-index: 9999;
    justify-content: center;
    align-items: center;
    cursor: pointer;
}}
.lightbox-overlay.active {{
    display: flex;
}}
.lightbox-overlay img {{
    max-width: 90vw;
    max-height: 90vh;
    border-radius: 8px;
    box-shadow: 0 0 40px rgba(212,168,83,0.3);
}}
.lightbox-close {{
    position: fixed;
    top: 20px;
    right: 30px;
    font-size: 2em;
    color: var(--gold);
    cursor: pointer;
    z-index: 10000;
    font-family: sans-serif;
    line-height: 1;
}}
.lightbox-rotate {{
    position: fixed;
    bottom: 30px;
    right: 30px;
    font-size: 1.5em;
    color: var(--gold);
    cursor: pointer;
    z-index: 10000;
    background: rgba(0,0,0,0.6);
    border: 1px solid var(--gold);
    border-radius: 8px;
    padding: 8px 16px;
    font-family: sans-serif;
}}
.lightbox-rotate:hover {{
    background: rgba(212,168,83,0.2);
}}

@media print {{
    body {{ background: white; color: black; }}
    .chapter-nav {{ display: none; }}
    .object-card {{ break-inside: avoid; border: 1px solid #ccc; }}
    .lightbox-overlay {{ display: none !important; }}
}}
@media (max-width: 768px) {{
    .hero h1 {{ font-size: 1.5em; }}
    .stats-bar {{ gap: 20px; }}
    .object-card .obj-header {{ flex-direction: column; }}
    .gallery-thumb {{ width: 140px; height: 100px; }}
}}
</style>
</head>
<body>

<div class="hero">
    <h1>Kolekcja Głuchowskich</h1>
    <div class="subtitle">Archiwum Wojskowe Rodziny Głuchowskich • 1905-1945</div>
    <div class="family-line">
        Cztery pokolenia polskiej historii wojskowej  - od Polskiej Organizacji Narodowej (1914),
        przez Legiony Piłsudskiego, II Rzeczpospolitą, aż po Polskie Siły Zbrojne na Zachodzie.<br>
        <strong>Gen. bryg. Janusz Głuchowski (1888-1935)</strong>  - legionista, generał WP, kawaler Virtuti Militari.<br>
        Archiwum z podpisami: <em>Józefa Piłsudskiego, Ignacego Mościckiego, Marszałka Focha, Króla Ferdynanda I Rumunii, Gen. Sosnkowskiego</em>
    </div>
</div>

<div class="container">

<div class="stats-bar">
    <div class="stat">
        <div class="stat-number">{len(rows)}</div>
        <div class="stat-label">Obiektów</div>
    </div>
    <div class="stat">
        <div class="stat-number">{len(CHAPTERS)}</div>
        <div class="stat-label">Rozdziałów</div>
    </div>
    <div class="stat">
        <div class="stat-number">{tier_a_count}</div>
        <div class="stat-label">Klasa A (muzealna)</div>
    </div>
    <div class="stat">
        <div class="stat-number">{total_min//1000}k-{total_max//1000}k PLN</div>
        <div class="stat-label">Estymacja całości</div>
    </div>
</div>

<div class="chapter-nav">
"""

for ch_key, ch_data in CHAPTERS.items():
    count = len(chapter_objects.get(ch_key, []))
    html += f'    <a href="#ch-{ch_key}">{ch_data["icon"]} {ch_key}. {ch_data["title"]} ({count})</a>\n'

html += '    <a href="#buyers">🏛️ Potencjalni nabywcy</a>\n'
html += '    <a href="#provenance">📜 Proweniencja</a>\n'
html += '    <a href="#market-research">📊 Badanie rynku</a>\n'
html += '</div>\n\n'

# Rozdziały
for ch_key, ch_data in CHAPTERS.items():
    objects = chapter_objects.get(ch_key, [])
    ch_min = sum(VALUATIONS.get(o["inventory_number"], {}).get("min_pln", 0) for o in objects)
    ch_max = sum(VALUATIONS.get(o["inventory_number"], {}).get("max_pln", 0) for o in objects)

    # Build gallery HTML for this chapter
    ch_images = IMAGE_MAP.get(ch_key, [])
    gallery_html = ""
    if ch_images:
        gallery_html = '    <div class="chapter-gallery">\n'
        for img_file in ch_images:
            gallery_html += f'        <img class="gallery-thumb" src="gluchowski_img/{img_file}" alt="{img_file}" onclick="openLightbox(this.src)">\n'
        gallery_html += '    </div>\n'

    html += f"""
<div class="chapter" id="ch-{ch_key}">
    <div class="chapter-header">
        <h2>{ch_data["icon"]} Rozdzia\u0142 {ch_key}  - {ch_data["title"]}</h2>
        <div class="period">{ch_data["period"]} | {len(objects)} obiekt\u00f3w | {len(ch_images)} zdj\u0119\u0107 | Estymacja: {ch_min:,} - {ch_max:,} PLN</div>
        <div class="chapter-desc">{ch_data["desc"]}</div>
    </div>
    <div class="chapter-body">
{gallery_html}"""
    for obj in objects:
        inv = obj["inventory_number"]
        val = VALUATIONS.get(inv, {})
        tier = val.get("tier", "B")
        tier_css = tier.replace("+", "plus")
        min_v = val.get("min_pln", 0)
        max_v = val.get("max_pln", 0)
        cond = obj.get("condition_grade", "good") or "good"
        cond_css = cond.replace(" ", "-")

        # Per-object images (prefer cropped versions when available)
        obj_imgs = OBJECT_IMAGES.get(inv, [])
        imgs_html = ""
        if obj_imgs:
            imgs_html = '            <div class="obj-images">\n'
            for img_file in obj_imgs:
                # Use cropped version if it exists
                cropped_path = os.path.join(_img_dir, "cropped", img_file)
                if os.path.exists(cropped_path):
                    img_src = f"gluchowski_img/cropped/{img_file}"
                else:
                    img_src = f"gluchowski_img/{img_file}"
                imgs_html += f'                <img src="{img_src}" alt="{inv}" onclick="openLightbox(this.src)">\n'
            imgs_html += '            </div>\n'

        html += f"""
        <div class="object-card">
            <div class="obj-header">
                <span class="inv-number">{inv}</span>
                <span class="obj-title">{obj["title"]}</span>
                <span class="tier-badge tier-{tier_css}">Tier {tier}</span>
            </div>
            <div class="obj-meta">
                <span>📁 {obj.get("category", "document")}</span>
                <span>📅 {obj.get("date_created", " -")}</span>
                <span>🎨 {obj.get("medium", " -")}</span>
            </div>
            <div class="obj-content">
{imgs_html}                <div class="obj-text">
                    <div class="obj-desc">{obj.get("description", "")}</div>
                    <div class="obj-value">
                        <span class="price-range">{min_v:,} - {max_v:,} PLN</span>
                        <span class="condition cond-{cond_css}">{cond}</span>
                    </div>
"""
        # Specjalne notatki
        notes = obj.get("notes", "")
        if "PODPIS" in (notes or "").upper() or "KOMPLET" in (notes or "").upper() or "HOLOKAUST" in (notes or "").upper():
            highlight = notes.split(".")[-2] if "." in notes else notes
            html += f'                    <div class="notes-box">⚠️ {highlight.strip()}</div>\n'

        html += "                </div>\n"  # close obj-text
        html += "            </div>\n"  # close obj-content
        html += "        </div>\n"  # close object-card

    html += "    </div>\n</div>\n"

# BUYERS SECTION
html += """
<div class="buyers-section" id="buyers">
    <h2>🏛️ Potencjalni nabywcy instytucjonalni</h2>
    <div class="buyers-body">
"""

for buyer in BUYERS["museums"]:
    html += f"""
        <div class="buyer-card">
            <h3>{buyer["name"]}</h3>
            <div class="interest">{buyer["interest"]}</div>
            <div class="chapters-tags">
"""
    for ch in buyer["chapters"]:
        ch_title = CHAPTERS[ch]["title"].split(" -")[0].split("(")[0].strip()
        html += f'                <span class="ch-tag">{ch}. {ch_title}</span>\n'
    html += "            </div>\n        </div>\n"

html += """
        <h3 style="color: var(--gold); margin: 25px 0 15px; font-size: 1.2em;">🔨 Domy aukcyjne (jeśli sprzedaż komercyjna)</h3>
"""
for ah in BUYERS["auction_houses"]:
    html += f"""
        <div class="buyer-card">
            <h3>{ah["name"]}</h3>
            <div class="interest">{ah["type"]}</div>
        </div>
"""
html += "    </div>\n</div>\n"

# PROVENANCE
html += """
<div class="provenance-box" id="provenance">
    <h2>📜 Proweniencja archiwum</h2>
    <p>Archiwum rodziny Głuchowskich  - kompletna dokumentacja czterech pokoleń polskiej rodziny wojskowej.
       Zbiór przechowywany przez rodzinę, następnie przez Krzysztofa Głuchowskiego (syna brata generała),
       który wyemigrował do Brazylii, gdzie zmarł 16 maja 2020 roku. Po jego śmierci archiwum trafiło na
       aukcje w Brazylii (Acervo Raro Leilões).</p>

    <div class="timeline">
        <div class="timeline-item">
            <span class="year">1888</span>
            <span class="event">  - Narodziny Janusza Głuchowskiego</span>
        </div>
        <div class="timeline-item">
            <span class="year">1914</span>
            <span class="event">  - PON, początek działalności niepodległościowej, wstąpienie do Legionów</span>
        </div>
        <div class="timeline-item">
            <span class="year">1914-1918</span>
            <span class="event">  - Służba w 7 Pułku Piechoty Legionów ("Siódemka"), I Brygada Piłsudskiego</span>
        </div>
        <div class="timeline-item">
            <span class="year">1920</span>
            <span class="event">  - Wojna polsko-bolszewicka, walki kawaleryjskie</span>
        </div>
        <div class="timeline-item">
            <span class="year">1918-1935</span>
            <span class="event">  - Kariera w II RP: Sztab Generalny, nominacja na generała, ordery od Piłsudskiego, Mościckiego, Focha</span>
        </div>
        <div class="timeline-item">
            <span class="year">1935</span>
            <span class="event">  - Śmierć gen. Janusza Głuchowskiego</span>
        </div>
        <div class="timeline-item">
            <span class="year">1940-1944</span>
            <span class="event">  - Dokumenty z Getta Łódzkiego trafiają do archiwum rodzinnego</span>
        </div>
        <div class="timeline-item">
            <span class="year">1940-1945</span>
            <span class="event">  - Krzysztof Andrzej Głuchowski w Szkocji  - Scottish Album</span>
        </div>
        <div class="timeline-item">
            <span class="year">~1950-2020</span>
            <span class="event">  - Archiwum przechowywane przez Krzysztofa Głuchowskiego w Brazylii</span>
        </div>
        <div class="timeline-item">
            <span class="year">16.05.2020</span>
            <span class="event">  - Śmierć Krzysztofa Głuchowskiego w Brazylii</span>
        </div>
        <div class="timeline-item">
            <span class="year">2024-2025</span>
            <span class="event">  - Archiwum na aukcjach Acervo Raro Leilões, Brazylia  - zakupione</span>
        </div>
    </div>
</div>
"""

# SUMMARY
html += f"""
<div class="summary-section">
    <h2>Podsumowanie wyceny</h2>
    <div class="total-value">{total_min:,} - {total_max:,} PLN</div>
    <p style="color: var(--text-dim);">
        ({total_min//4.3:.0f} - {total_max//4.3:.0f} EUR  •  {total_min//4.7:.0f} - {total_max//4.7:.0f} USD)
    </p>
    <p style="color: var(--text-dim); margin-top: 10px;">
        <strong>{tier_a_count} obiektów klasy A</strong> (muzealna) •
        {sum(1 for v in VALUATIONS.values() if v['tier']=='B+' or v['tier']=='B')} obiektów klasy B/B+
    </p>
    <div class="disclaimer">
        Wyceny oparte na analizie rynku antykwarycznego w Polsce i Europie (DESA Unicum, Rara Avis, Libra, Onebid).
        Rzeczywista wartosc zalezy od: stanu zachowania, kompletnosci, autentykacji eksperckiej, i aktualnego popytu rynkowego.
        Archiwum sprzedawane jako komplet moze osiagnac premie 30-50% ponad sume jednostkowa.
    </div>
</div>

<div class="provenance-box" id="market-research" style="margin-top: 30px;">
    <h2>📊 Metodologia wyceny -- badanie rynku</h2>
    <p><strong>Niezalezna wycena</strong> oparta na zrealizowanych transakcjach aukcyjnych 2019-2026.
       Przebadano platformy: RR Auction (USA), Heritage Auctions (USA), DESA Unicum (PL), OneBid/WDA-MiM (PL),
       eMedals (CA), Invaluable (USA), Kedem Auction House (IL), Bonhams (UK), Allegro archiwum (PL),
       PCGS ValueView, CoinStrail, Numista.</p>

    <h3 style="color: var(--gold); margin-top: 20px;">Kluczowe punkty cenowe (zrealizowane):</h3>

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 15px; margin-top: 15px;">
        <div style="background: var(--card); padding: 15px; border-radius: 8px; border-left: 3px solid #c0392b;">
            <strong style="color: #e74c3c;">Autografy Pilsudskiego</strong><br>
            <span style="color: var(--gold);">$963 USD</span> -- fotografia z podpisem (RR Auction, maly format 3.75x5")<br>
            <span style="color: var(--text-dim); font-size: 0.85em;">
                Bylo to DRUGIE podpisane zdjecie Pilsudskiego w historii RR Auction.
                Dyplom urzedowy z pelnym podpisem > fotografia: mnoznik x3-x8.
            </span>
        </div>
        <div style="background: var(--card); padding: 15px; border-radius: 8px; border-left: 3px solid #2980b9;">
            <strong style="color: #3498db;">Waluta Getta Lodzkiego</strong><br>
            <span style="color: var(--gold);">10 Pf kupon: sr. 960 USD / rekord 17,250 PLN</span><br>
            <span style="color: var(--gold);">20 Mk aluminum: sr. 1,800 USD / rekord 20,000 PLN</span><br>
            <span style="color: var(--text-dim); font-size: 0.85em;">
                WDA-MiM, Marciniak Dom Aukcyjny. Kupony pocztowe rzadsze niz monety.
                Komplet z proweniencja = mnoznik x3-x5.
            </span>
        </div>
        <div style="background: var(--card); padding: 15px; border-radius: 8px; border-left: 3px solid #27ae60;">
            <strong style="color: #2ecc71;">Dokumenty Powstania Warszawskiego</strong><br>
            <span style="color: var(--gold);">Koperta poczty polowej: 800-3,000 PLN</span><br>
            <span style="color: var(--gold);">Legitymacja AK oryginal: 2,000-8,000 PLN</span><br>
            <span style="color: var(--text-dim); font-size: 0.85em;">
                OneBid, Allegro archiwum. Przepustki AK -- ekstremalnie rzadkie,
                brak porownawczych transakcji. Muzeum PW kupowalo listy na aukcjach (Dusseldorf 2008).
            </span>
        </div>
        <div style="background: var(--card); padding: 15px; border-radius: 8px; border-left: 3px solid #8e44ad;">
            <strong style="color: #9b59b6;">Pamietniki obozowe</strong><br>
            <span style="color: var(--gold);">$17,827 USD</span> -- pamietnik RAF z Stalag Luft III (Invaluable)<br>
            <span style="color: var(--text-dim); font-size: 0.85em;">
                Pamietnik 15-letniego AK-owca (GL-111) -- jeszcze rzadszy kontekst niz Stalag Luft III.
                15 kart obozowych, Stalag VIJ, grudzien 1944.
            </span>
        </div>
        <div style="background: var(--card); padding: 15px; border-radius: 8px; border-left: 3px solid #d4a853;">
            <strong style="color: var(--gold);">Krzyz Walecznych</strong><br>
            <span style="color: var(--gold);">100-480 PLN</span> -- sam medal (WCN e-aukcje)<br>
            <span style="color: var(--text-dim); font-size: 0.85em;">
                Z legitymacja + proweniencja generala = mnoznik x20-x50.
                GL-021 (KW generala) = 3,000-8,000 PLN.
            </span>
        </div>
        <div style="background: var(--card); padding: 15px; border-radius: 8px; border-left: 3px solid #e67e22;">
            <strong style="color: #e67e22;">Premia za kompletnosc archiwum</strong><br>
            <span style="color: var(--gold);">+50-80%</span> ponad sume jednostkowa<br>
            <span style="color: var(--text-dim); font-size: 0.85em;">
                4 generacje, 95 obiektow, 12 rozdzialow, ciagla proweniencja od 1914 do 1946.
                Instytut Pilsudskiego (NY), Hoover Institution -- precedensy zakupu archiwow.
            </span>
        </div>
    </div>

    <h3 style="color: var(--gold); margin-top: 20px;">Dlaczego te ceny?</h3>
    <p style="margin-top: 10px;">
        <strong>1. Autograf Pilsudskiego (GL-010, GL-039)</strong> -- Pilsudski prawie nigdy nie podpisywal dokumentow
        dla osob prywatnych. RR Auction sprzedalo tylko DWIE pozycje z jego podpisem w historii firmy.
        Dyplom Krzyza Legjonowego nr 115 z pelnym podpisem na dokumencie urzedowym jest wart wielokrotnosc
        zdjecia portretowego ($963). Estymacja 25,000-60,000 PLN odzwierciedla ekstremalnie ograniczona podaz.
    </p>
    <p style="margin-top: 10px;">
        <strong>2. Legitymacja AK nr 1112 (GL-067)</strong> -- Oryginalna legitymacja AK z Powstania Warszawskiego
        to obiekt klasy muzealnej. Na rynku pojawiaja sie glownie wtorniki i kopie z archiwow ZBOWID.
        Oryginal z pieczecia, pseudonimem i przydzialem do plutonu -- w rekach prywatnych -- jest UNIKATEM.
        Muzeum Powstania Warszawskiego posiada ok. 400 legitymacji, ale wiekszosc z powojennych archiwow.
        Estymacja 50,000-120,000 PLN.
    </p>
    <p style="margin-top: 10px;">
        <strong>3. Pamietnik obozowy (GL-111)</strong> -- Pamietnik prowadzony przez 15-letniego jenca w Stalagu VIJ,
        15 kart zagestego pisma olowkiem. Porownanie: pamietnik RAF z Stalag Luft III sprzedany za $17,827 USD
        (~84,000 PLN). Pamietnik dziecka-zolnierza AK jest jeszcze rzadszy. Estymacja 30,000-70,000 PLN.
    </p>
    <p style="margin-top: 10px;">
        <strong>4. Getto Lodzkie (GL-041)</strong> -- Kupon pocztowy 10 Pf to fizyczny relikt Holocaustu.
        Srednia cena na rynku numizmatycznym: 960 USD. Rekord WDA-MiM: 17,250 PLN. ALE: ten kupon
        ma udokumentowana proweniencje (rodzina Gluchowskich od lat 40.), 26 lat poszukiwan muzeum (1958-1984),
        i korespondencje z Ambasada Izraela. To nie jest moneta bez historii -- to dokument-swiadectwo.
    </p>
</div>

<div class="summary-section" style="margin-top: 30px;">
    <h2>Wartosc archiwum jako calosci</h2>
    <p style="color: var(--text-dim);">
        Suma jednostkowa: <strong style="color: var(--gold);">{total_min:,} - {total_max:,} PLN</strong>
    </p>
    <p style="color: var(--text-dim);">
        Z premia za kompletnosc (+50-80%):
    </p>
    <div class="total-value">{int(total_min*1.5):,} - {int(total_max*1.8):,} PLN</div>
    <p style="color: var(--text-dim);">
        ({int(total_min*1.5/4.3):,} - {int(total_max*1.8/4.3):,} EUR  &bull;
        {int(total_min*1.5/4.7):,} - {int(total_max*1.8/4.7):,} USD)
    </p>
    <p style="color: var(--text-dim); margin-top: 10px;">
        Katalog Naukowy szacowal: <strong>600,000 - 1,200,000+ PLN</strong>
    </p>
</div>

<div class="footer">
    <p>Katalog wygenerowany automatycznie • {len(rows)} obiektów • {len(CHAPTERS)} rozdziałów</p>
    <p>Kolekcja Głuchowskich  - Archiwum Wojskowe 1905-1945</p>
    <p style="margin-top: 10px; font-style: italic;">Dokument poufny  - nie do dystrybucji publicznej</p>
</div>

</div>

<!-- Lightbox -->
<div class="lightbox-overlay" id="lightbox" onclick="closeLightbox(event)">
    <span class="lightbox-close" onclick="closeLightbox(event)">&times;</span>
    <img id="lightbox-img" src="" alt="Full size" style="transition: transform 0.3s;">
    <span class="lightbox-rotate" onclick="rotateLightbox(event)">&#x21BB; Obroc 90&deg;</span>
</div>

<script>
var _lbRotation = 0;
function openLightbox(src) {{
    _lbRotation = 0;
    var overlay = document.getElementById('lightbox');
    var img = document.getElementById('lightbox-img');
    img.src = src;
    img.style.transform = 'rotate(0deg)';
    overlay.classList.add('active');
}}
function closeLightbox(e) {{
    if (e) e.stopPropagation();
    document.getElementById('lightbox').classList.remove('active');
}}
function rotateLightbox(e) {{
    if (e) e.stopPropagation();
    _lbRotation = (_lbRotation + 90) % 360;
    document.getElementById('lightbox-img').style.transform = 'rotate(' + _lbRotation + 'deg)';
}}
document.addEventListener('keydown', function(e) {{
    if (e.key === 'Escape') closeLightbox(e);
    if (e.key === 'r' || e.key === 'R') rotateLightbox(e);
}});
</script>

</body>
</html>
"""

# Zapisz
output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "docs")
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "gluchowski.html")

with open(output_path, "w", encoding="utf-8") as f:
    f.write(html)

print(f"\n✅ Katalog Głuchowskich wygenerowany: {output_path}")
print(f"   {len(rows)} obiektów w {len(CHAPTERS)} rozdziałach")
print(f"   Estymacja: {total_min:,} - {total_max:,} PLN")
print(f"   Otwórz: http://localhost:8091/gluchowski.html")

conn.close()
