#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════════╗
║  ARCHIWUM RODZINY GŁUCHOWSKICH — KATALOG MUZEALNY v4           ║
║                                                                  ║
║  Metodologia: ISAD(G) + Dublin Core + praktyka muzealna         ║
║  Standard: karta katalogowa = 1 fotografia                       ║
║  Hierarchia: Zespół → Seria → Podseria → Jednostka              ║
║                                                                  ║
║  Zespół: ARG — Archiwum Rodziny Głuchowskich                    ║
║  Seria I:   Marian Głuchowski (1862–1924)                        ║
║  Seria II:  Gen. dyw. Janusz Głuchowski (1888–1964)              ║
║  Seria III: Ppor. Stanisław Stefan Głuchowski (1893–1962)        ║
║  Seria IV:  Lech Głuchowski (1900–1944)                          ║
║  Seria V:   St.ul. Krzysztof Andrzej Głuchowski (1926–2020)     ║
║  Seria VI:  Varia / Rodzina                                      ║
╚══════════════════════════════════════════════════════════════════╝
"""

import os, html as html_mod
from transcriptions import TRANSCRIPTIONS

IMG_DIR = "gluchowski_img"

# ============================================================================
# NOTA PROWENIENCYJNA (FONDS-LEVEL DESCRIPTION)
# ============================================================================
FONDS = {
    "nazwa_zespolu": "Archiwum Rodziny Głuchowskich",
    "skrot": "ARG",
    "daty_skrajne": "1862–1964",
    "rozmiar": "ok. 236 fotografii dokumentów, korespondencji, fotografii i ephemery",
    "tworca": "Rodzina Głuchowskich h. Głuchowski (linia częstochowsko-warszawska)",
    "historia_zespolu": (
        "Zespół obejmuje dokumenty pięciu pokoleń rodziny Głuchowskich — od działalności "
        "niepodległościowej Mariana Głuchowskiego w PON (1914) przez generalską karierę "
        "Janusza Głuchowskiego (Siódemka Beliny, I Wiceminister Spraw Wojskowych), "
        "jeniecką korespondencję Stanisława Stefana i Krzysztofa Andrzeja (Stalag XI B, VI/3), "
        "po maturę w Gimnazjum 3 DSK we Włoszech (1946). Szczególną wartość stanowi "
        "korespondencja obozowa między ojcem i synem w różnych Stalagach oraz relacje "
        "z Powstania Warszawskiego pisane z pamięci w obozach jenieckich."
    ),
    "proweniencja": (
        "Dokumenty przechowywane w rodzinie Głuchowskich. Obecny depozytariusz: "
        "spadkobierca linii Krzysztofa Andrzeja Głuchowskiego."
    ),
    "jezyki": "polski, niemiecki, francuski, angielski, rosyjski, rumuński",
    "stan_zachowania": "Zróżnicowany. Dokumenty obozowe: zniszczone, pożółkłe, ubytki. Dokumenty urzędowe: dobry. Fotografie: średni."
}

# ============================================================================
# SERIE ARCHIWALNE (SERIES-LEVEL)
# ============================================================================
SERIES = [
    {
        "id": "I",
        "tytul": "Marian Głuchowski (1862–1924)",
        "opis": "Członek Rady PON nr 2, Komisarz na powiat częstochowski. Organizator PPS. Dokumenty z Polskiej Organizacji Narodowej 1914.",
        "daty": "1914",
        "rozmiar": "4 jednostki"
    },
    {
        "id": "II",
        "tytul": "Gen. dyw. Janusz Julian Głuchowski (1888–1964)",
        "opis": "Siódemka Beliny (2.VIII.1914), twórca i d-ca 7 P.Uł. Lubelskich, gen. bryg. (1927), gen. dyw. (1.VI.1945), I Zastępca Ministra Spraw Wojskowych (1935-1939), Dowódca PSZ w Wielkiej Brytanii (1943-1945). OB PPS od 1905 (17 lat!), ZWC w Liège (współzałożyciel z T. Piskorem), Legiony, wojna 1920, MSWojsk, emigracja w Londynie, współzałożyciel Instytutu Piłsudskiego w Londynie (15.III.1947). Pochowany Brompton Cemetery (#576).",
        "daty": "1914–1964",
        "rozmiar": "33 jednostki"
    },
    {
        "id": "III",
        "tytul": "Ppor. Stanisław Stefan Głuchowski (1893–1962)",
        "opis": "Ur. 1.V.1893, Bukowa. Ppor. rez. kawalerii, leg. AK nr 2856, ps. 'Stefan'. Od 1923 w Kancelarii Cywilnej Prezydenta RP (do 1939). Aresztowany przez Gestapo 18.V.1944, Pawiak, zwolniony 29.VII.1944 (2 dni przed Powstaniem!). AK — Kwatermistrzostwo I Obwodu 'Radwan', Śródmieście. Jeniec Stalag XI-B Fallingbostel (nr 1245). Zm. 17.X.1962, Warszawa, pochowany Powązki.",
        "daty": "1944–1945",
        "rozmiar": "6 jednostek"
    },
    {
        "id": "IV",
        "tytul": "Lech Głuchowski ps. 'Jeżycki' (1900–1944)",
        "opis": "Poległ w Powstaniu Warszawskim 15.IX.1944. Brak bezpośrednich dokumentów w kolekcji — wspominany w korespondencji.",
        "daty": "—",
        "rozmiar": "—"
    },
    {
        "id": "V",
        "tytul": "St.ul. Krzysztof Andrzej Głuchowski ps. 'Juraś' (29.XI.1926 – V.2020)",
        "opis": "Ur. 29.XI.1926, Warszawa. Przysięga AK 11.V.1942 (15 lat!). Pluton 1112, 7 P.Uł. AK, dywizjon 'Jeleń'. Obrona Fabryki Kamlera (KG AK), Starówka, ewakuacja kanałami 1.IX.1944, Śródmieście. Jeniec Stalag XI-B Fallingbostel (nr 141009) — ten sam obóz co ojciec! Via Holandia/Belgia/Francja do Włoch, 2 Korpus, Gimnazjum 3 DSK (matura 1946). Emigracja: Anglia → Brazylia (od 1974). Chartered Engineer, publicysta, wydawca bibliofilski. Zm. V.2020, Rio de Janeiro.",
        "daty": "1941–1968",
        "rozmiar": "156 jednostek"
    },
    {
        "id": "VI",
        "tytul": "Varia / Rodzina",
        "opis": "Dokumenty niemożliwe do jednoznacznego przypisania, album fotograficzny, militaria, biogramy rodzinne.",
        "daty": "1939–1970",
        "rozmiar": "14 jednostek"
    },
]

# ============================================================================
# TYPY DOKUMENTÓW (CONTROLLED VOCABULARY)
# ============================================================================
DOC_TYPES = {
    "leg": "Legitymacja",
    "afisz": "Afisz / druk ulotny",
    "pismo": "Pismo urzędowe",
    "pokw": "Pokwitowanie",
    "dyplom": "Dyplom / akt nadania",
    "foto": "Fotografia",
    "fotokopia": "Fotokopia",
    "list": "List / korespondencja",
    "kartka": "Kartka pocztowa jeńca (Kriegsgefangenenpost)",
    "koperta": "Koperta",
    "karta_id": "Karta tożsamości",
    "formularz": "Formularz urzędowy",
    "zaswiadczenie": "Zaświadczenie",
    "rozkaz": "Rozkaz wojskowy",
    "przepustka": "Przepustka",
    "pamietnik": "Pamiętnik / notatki wspomnieniowe",
    "esej": "Esej szkolny",
    "zeszyt": "Zeszyt szkolny",
    "mapa": "Szkic / mapka",
    "druk": "Druk okolicznościowy",
    "nekrolog": "Nekrolog / klepsydra",
    "album": "Album fotograficzny",
    "militaria": "Militaria (galony, wstążki)",
    "numizmat": "Numizmat / bon gettowy",
    "ulotka": "Ulotka / druk informacyjny",
    "notatka": "Notatka odręczna",
    "wizytowka": "Wizytówka / ephemera",
    "dekret": "Dekret / akt prawny",
    "skierowanie": "Skierowanie urzędowe",
    "aerogram": "Aerogram / list lotniczy",
    "ksiazeczka": "Książeczka wojskowa",
    "swiadectwo": "Świadectwo szkolne",
    "discharge": "Discharge Certificate",
    "certyfikat": "Certyfikat / certificate",
    "naszywka": "Naszywka / oznaka pułkowa",
    "wycinek": "Wycinek prasowy",
    "biogram": "Biogram / nota biograficzna",
    "kwestionariusz": "Kwestionariusz osobisty",
    "wspomnienia": "Wspomnienia / rękopis",
    "gazeta": "Gazeta / czasopismo",
    "bilet": "Bilet / karta członkowska",
    "rysunek": "Rysunek odręczny",
}

# ============================================================================
# JEDNOSTKI INWENTARZOWE (ITEM-LEVEL DESCRIPTIONS)
# ============================================================================
# Każda karta: sygnatura, foto, tytuł, data, typ dokumentu, opis fizyczny,
# opis treści, seria, twórca, język, kontekst, powiązania, stan zachowania
# ============================================================================

OBJECTS = [
    # =====================================================================
    # SERIA I — MARIAN GŁUCHOWSKI
    # =====================================================================
    {
        "sygn": "ARG/I/1",
        "photo": "Kolekcja_Gluchowski_Katalog_Tematyczny_p02_img01.jpeg",
        "tytul": "Legitymacja Polskiej Organizacji Narodowej nr 2",
        "data": "1914",
        "typ": "leg",
        "opis_fizyczny": "Dokument papierowy składany, format ok. 10×15 cm, druk z odręcznymi wpisami atramentem, pieczęcie okrągłe",
        "opis_tresci": "Legitymacja PON nr 2 wystawiona na Marjana Głuchowskiego, ur. 1867. Wnętrze otwartej legitymacji z danymi osobowymi, pieczęciami PON. Jeden z pierwszych numerów — świadczy o roli założycielskiej.",
        "seria": "I",
        "tworca": "Polska Organizacja Narodowa",
        "jezyk": "polski",
        "kontekst": "PON — organizacja paramilitarna założona w 1914 dla przygotowania powstania antyrosyjskiego. Legitymacja nr 2 sugeruje, że Marian był jednym z założycieli oddziału częstochowskiego.",
        "powiazania": ["ARG/I/2", "ARG/I/3", "ARG/I/4"],
        "stan": "Dobry, pożółkły papier, pieczęcie czytelne"
    },
    {
        "sygn": "ARG/I/2",
        "photo": "Kolekcja_Gluchowski_Katalog_Tematyczny_p02_img02.jpeg",
        "tytul": "Afisz PON — zawiadomienie o zebraniu w sali 'Lutni'",
        "data": "2.X.1914",
        "typ": "afisz",
        "opis_fizyczny": "Druk jednostronny na papierze gazetowym, format ok. A5, czcionka antykwowa",
        "opis_tresci": "Drukowane zawiadomienie o zebraniu PON w sali 'Lutni', 2 października. Prelegenci: Wacław Sieroszewski, Juljusz Kaden-Bandrowski i Marjan Dąbrowski. Podpis: Komisarz PON na powiat Częstochowski — Marjan Głuchowski. Wejście bezpłatne.",
        "seria": "I",
        "tworca": "PON, Komisariat Częstochowski",
        "jezyk": "polski",
        "kontekst": "Wacław Sieroszewski — pisarz, legionista. Juliusz Kaden-Bandrowski — prozaik, propagandysta Legionów. Zebranie werbunkowe dla idei niepodległościowej.",
        "powiazania": ["ARG/I/1"],
        "stan": "Dobry, papier kruchy"
    },
    {
        "sygn": "ARG/I/3",
        "photo": "Kolekcja_Gluchowski_Katalog_Tematyczny_p02_img03.jpeg",
        "tytul": "Pismo PON, Komisja Organizacyjna, L.145",
        "data": "1914",
        "typ": "pismo",
        "opis_fizyczny": "Pismo urzędowe na papierze firmowym PON, format ok. A5, pieczątka nagłówkowa, podpis odręczny atramentem",
        "opis_tresci": "Pismo Polskiej Organizacji Narodowej, Komisja Organizacyjna, nr L.145, adresowane do M. Głuchowskiego. Nagłówek z pieczątką PON. Odręcznie podpisane.",
        "seria": "I",
        "tworca": "PON, Komisja Organizacyjna",
        "jezyk": "polski",
        "kontekst": "Korespondencja służbowa wewnątrz PON — instrukcje dla komisarza powiatowego.",
        "powiazania": ["ARG/I/1"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/I/4",
        "photo": "Kolekcja_Gluchowski_Katalog_Tematyczny_p03_img01.jpeg",
        "tytul": "Pokwitowanie PON na broń i ekwipunek",
        "data": "1914",
        "typ": "pokw",
        "opis_fizyczny": "Formularz z odręcznymi wpisami, papier kancelaryjny, format ok. A5",
        "opis_tresci": "Pokwitowanie Polskiej Organizacyi Narodowej na 200 kop., 2 szable, latarkę, reflektor i inne. Odręcznie wpisane dane, podpis Oficera Wojsk Polskich.",
        "seria": "I",
        "tworca": "PON",
        "jezyk": "polski",
        "kontekst": "Dokument materialny — potwierdza przekazanie broni białej i sprzętu na potrzeby organizacji paramilitarnej. Szable sugerują tradycję kawaleryjską rodziny.",
        "powiazania": ["ARG/I/1"],
        "stan": "Dobry, odręczne wpisy czytelne"
    },
    {
        "sygn": "ARG/I/5",
        "photo": "Kolekcja_Gluchowski_Katalog_Tematyczny_p03_img02.jpeg",
        "tytul": "Koperta urzędowa PON + Karta Polowa Legionów",
        "data": "1914–1918",
        "typ": "koperta",
        "opis_fizyczny": "Dwa obiekty na jednym zdjęciu: koperta papierowa z nadrukiem 'Urzędowa', ok. 12×8 cm; karta pocztowa Feldpostkarte z orłem legionowym",
        "opis_tresci": "Koperta adresowana do Głuchowskiego, Komisarza na powiat Częstochowy, oraz Karta Polowa Legionów / Feldpostkarte z orłem legionowym.",
        "seria": "I",
        "tworca": "PON / Legiony Polskie",
        "jezyk": "polski / niemiecki",
        "kontekst": "Koperta urzędowa PON potwierdza funkcję komisarza. Karta Polowa Legionów to standardowy formularz korespondencji z frontu I wojny.",
        "powiazania": ["ARG/I/1", "ARG/I/3"],
        "stan": "Średni, koperta pożółkła"
    },

    # =====================================================================
    # SERIA II — GEN. DYW. JANUSZ GŁUCHOWSKI
    # =====================================================================

    # -- Podseria II/A: Dokumenty służby przedwojennej --
    {
        "sygn": "ARG/II/1",
        "photo": "Kolekcja_Gluchowski_Katalog_Tematyczny_p04_img01.jpeg",
        "tytul": "Biogram WBH nr 76/45 — zaświadczenie o służbie",
        "data": "24.V.1937",
        "typ": "zaswiadczenie",
        "opis_fizyczny": "Maszynopis na papierze urzędowym WBH, format A4, pieczęć okrągła",
        "opis_tresci": "Biogram nr 76/45 Wojskowego Biura Historycznego, 24 maja 1937. Zaświadczenie o służbie Janusza Głuchowskiego: OB PPS, ZWC w Liège, patrol kawaleryjski 2.VIII.1914 do Krakowa i na Kielce, ZS Oleandry.",
        "seria": "II",
        "tworca": "Wojskowe Biuro Historyczne",
        "jezyk": "polski",
        "kontekst": "WBH wydawało biogramy dla oficerów-legionistów w ramach dokumentowania czynu zbrojnego. Potwierdza przynależność do 'Siódemki Beliny' — pierwszego patrolu kawaleryjskiego Legionów. 'ZWC w Liège' = Związek Walki Czynnej — Głuchowski współzałożył tę organizację w Belgii razem z Tadeuszem Piskorem podczas studiów na Politechnice w Liège (~1907-1909). 'OB PPS' = Organizacja Bojowa PPS — Głuchowski wstąpił w 1905 r., mając zaledwie 17 lat.",
        "powiazania": ["ARG/II/2", "ARG/II/4"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/II/2",
        "photo": "Kolekcja_Gluchowski_Katalog_Tematyczny_p04_img02.jpeg",
        "tytul": "Fotokopia 'Siódemki Beliny' z podpisami uczestników",
        "data": "2–3.VIII.1914",
        "typ": "fotokopia",
        "opis_fizyczny": "Fotokopia fotografii grupowej na papierze fotograficznym, format ok. 18×24 cm, odręczne podpisy na marginesie",
        "opis_tresci": "Fotokopia historycznego zdjęcia 'Siódemki Beliny' — pierwszego patrolu kawaleryjskiego Legionów Polskich (2–3.VIII.1914). Podpisy uczestników: Belina-Prażmowski (ur. 1888 Ruszkowiec, zm. 1938 Wenecja), Głuchowski (ur. 1888 Bukowa, zm. 1964 Londyn), Grzmot-Skotnicki (zm. IX.1939 pod Tułowicami), Bończa-Karwacki (poległ 1916 Kostiuchnówka — pierwszy z Siódemki), Jabłoński ps. 'Zdzisław' (~1896, zm. 1920 — najmłodszy, 18 lat!), Hanka-Kulesza (1892 Gandawa, zm. 5.VI.1964 Londyn — 6 dni przed Głuchowskim!), Kmicic-Skrzyński (1893 Odessa, zm. 1972 Manchester — OSTATNI żyjący z Siódemki).",
        "seria": "II",
        "tworca": "nieznany fotograf / uczestnik patrolu",
        "jezyk": "polski",
        "kontekst": "IKONOGRAFICZNY DOKUMENT ZAŁOŻYCIELSKI polskiej kawalerii odrodzonej. Patrol Siódemki Beliny (noc 2/3.VIII.1914) — siedmiu kawalerzystów na rozkaz Piłsudskiego przekroczyło granicę rosyjską, otwierając kampanię Legionów — pierwszy regularny oddział polski od Powstania Styczniowego 1863 r. Głuchowski był zastępcą dowódcy patrolu. Identyfikacja uczestników zweryfikowana wg źródeł IPN i jpilsudski.org.",
        "powiazania": ["ARG/II/1"],
        "stan": "Średni, fotokopia wtórna"
    },
    {
        "sygn": "ARG/II/3",
        "photo": "Kolekcja_Gluchowski_Katalog_Tematyczny_p05_img02.jpeg",
        "tytul": "Zaświadczenie o przynależności do OB PPS 1905–1908",
        "data": "I.1935",
        "typ": "zaswiadczenie",
        "opis_fizyczny": "Maszynopis na papierze firmowym Inspektoratu Armii, podpis atramentem",
        "opis_tresci": "Zaświadczenie, że Głuchowski należał do Organizacji Bojowej PPS od roku 1905 do 1908. Podpis: Inspektor Armii (Kazimierz Sosnkowski), Warszawa, styczeń 1935.",
        "seria": "II",
        "tworca": "Gen. Kazimierz Sosnkowski, Inspektor Armii",
        "jezyk": "polski",
        "kontekst": "OB PPS — tajna organizacja bojowa Polskiej Partii Socjalistycznej, prowadząca akcje zbrojne przeciw Rosji. Sosnkowski jako współtwórca ruchu strzeleckiego potwierdzał rewolucyjną przeszłość Głuchowskiego.",
        "powiazania": ["ARG/II/1", "ARG/II/5"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/II/4",
        "photo": "Kolekcja_Gluchowski_Katalog_Tematyczny_p05_img01.jpeg",
        "tytul": "List odręczny na papierze Inspektoratu Armii",
        "data": "lata 30. XX w.",
        "typ": "list",
        "opis_fizyczny": "List odręczny atramentem na papierze firmowym z nagłówkiem Inspektoratu Armii, 1 karta",
        "opis_tresci": "List odręczny na papierze firmowym Inspektoratu Armii (Sosnkowskiego). Pismo kaligraficzne atramentem. Treść nieczytelna na fotografii.",
        "seria": "II",
        "tworca": "prawdopodobnie Gen. Sosnkowski",
        "jezyk": "polski",
        "kontekst": "Korespondencja prywatna między kadrą generalską II RP.",
        "powiazania": ["ARG/II/3"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/II/5",
        "photo": "Kolekcja_Gluchowski_Katalog_Tematyczny_p05_img04.jpeg",
        "tytul": "Zaświadczenie archiwalne o złożeniu broni (1909)",
        "data": "10.III.1925",
        "typ": "zaswiadczenie",
        "opis_fizyczny": "Dokument z pieczęcią Archiwum Głównego Akt Dawnych, format mały",
        "opis_tresci": "Zaświadczenie ze Głuchowski złożył broń (rewolwer) w roku 1909 na szarży Miłości. Pieczęć Archiwum Głównego Akt Dawnych, data 10.III.1925.",
        "seria": "II",
        "tworca": "Archiwum Główne Akt Dawnych",
        "jezyk": "polski",
        "kontekst": "Dokument potwierdzający zakończenie działalności bojowej w OB PPS. 'Szarża Miłości' — punkt zborny konspiracyjny.",
        "powiazania": ["ARG/II/3"],
        "stan": "Średni"
    },
    {
        "sygn": "ARG/II/6",
        "photo": "Kolekcja_Gluchowski_Katalog_Tematyczny_p05_img05.jpeg",
        "tytul": "Notatka o Związku Strzeleckim",
        "data": "ok. 1910–1914",
        "typ": "notatka",
        "opis_fizyczny": "Notatka odręczna atramentem, papier kancelaryjny, format mały",
        "opis_tresci": "Notatka odręczna z informacją o oficerach ZS, kompaniach, Krakowie. Lista punktów dot. Związku Strzeleckiego i przygotowania kadr wojskowych.",
        "seria": "II",
        "tworca": "Janusz Głuchowski (?)",
        "jezyk": "polski",
        "kontekst": "Związek Strzelecki — organizacja paramilitarna przygotowująca kadry dla przyszłego wojska polskiego, prekursor Legionów.",
        "powiazania": ["ARG/II/1"],
        "stan": "Średni"
    },
    {
        "sygn": "ARG/II/7",
        "photo": "Kolekcja_Gluchowski_Katalog_Tematyczny_p05_img03.jpeg",
        "tytul": "Fotografia grupowa oficerów",
        "data": "lata 30. XX w.",
        "typ": "foto",
        "opis_fizyczny": "Fotografia czarno-biała, odbitka na papierze fotograficznym, ciemna, słaba czytelność",
        "opis_tresci": "Ciemna fotografia grupowa oficerów w mundurach. Trudna do identyfikacji ze względu na słabą jakość reprodukcji.",
        "seria": "II",
        "tworca": "nieznany",
        "jezyk": "—",
        "kontekst": "Prawdopodobnie kadra oficerska jednostki dowodzonej przez Głuchowskiego.",
        "powiazania": [],
        "stan": "Słaby — ciemna, nieczytelna"
    },

    # -- Podseria II/B: 7 Pułk Ułanów Lubelskich --
    {
        "sygn": "ARG/II/8",
        "photo": "Kolekcja_Gluchowski_Katalog_Tematyczny_p06_img01.jpeg",
        "tytul": "Rozkaz utworzenia oddziału jazdy — Lublin 5.XI.1918",
        "data": "5.XI.1918",
        "typ": "rozkaz",
        "opis_fizyczny": "Maszynopis na papierze Sztabu Generalnego, format A4, pieczęć",
        "opis_tresci": "Rozkaz Sztabu Generalnego, Lublin 5 listopada 1918: Rotmistrzowi Januszowi Głuchowskiemu nakazuje się organizować nowo-oddzielony oddział jazdy w Lubelskiem.",
        "seria": "II",
        "tworca": "Sztab Generalny WP",
        "jezyk": "polski",
        "kontekst": "AKT ZAŁOŻYCIELSKI — Głuchowski nie tylko organizował, ale TWORZYŁ oddziały kawalerii w Lublinie i Kraśniku, z których wyrósł przyszły 3 Pułk Ułanów (a nie bezpośrednio 7 P.Uł.). Rozkaz wydany 6 dni przed odzyskaniem niepodległości (11.XI.1918). Głuchowski był pierwszym dowódcą 7 P.Uł. Lubelskich (XI.1918 – VII.1920) i twórcą tradycji pułku, w którym później walczyła cała rodzina (Stefan, Lech, Krzysztof w AK).",
        "powiazania": ["ARG/II/15"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/II/9",
        "photo": "Kolekcja_Gluchowski_Katalog_Tematyczny_p12_img01.jpeg",
        "tytul": "Życzenia od Samorządu Żołnierskiego 7 P.Uł.",
        "data": "5.I. [lata 20.]",
        "typ": "pismo",
        "opis_fizyczny": "Pismo na papierze z pieczęcią pułkową, odręczne podpisy",
        "opis_tresci": "Życzenia świąteczne od Samorządu Żołnierskiego 7 Pułku Ułanów: 'do Majora Głuchowskiego Janusza, D-cy 7-go P.Ułanów, w imieniu oficerów i szeregowych...' Pieczęć 7 P.Uł., podpis.",
        "seria": "II",
        "tworca": "Samorząd Żołnierski 7 P.Uł.",
        "jezyk": "polski",
        "kontekst": "Dokument świadczący o relacji dowódcy z żołnierzami. Stopień 'Major' pozwala datować na lata 20.",
        "powiazania": ["ARG/II/8"],
        "stan": "Dobry"
    },

    # -- Podseria II/C: Legiony i odznaczenia --
    {
        "sygn": "ARG/II/10",
        "photo": "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p06_img01.jpeg",
        "tytul": "Dyplom Krzyża Legionowego Nr 145 dla płk. Janusza Głuchowskiego — Warszawa 11.VII.1925",
        "data": "11.VII.1925",
        "typ": "dyplom",
        "opis_fizyczny": "Zbliżenie fotograficzne dyplomu (dolna połowa). Druk ozdobny z wizerunkiem Krzyża Legionowego u góry. Tekst częściowo drukowany, częściowo odręczny (kaligrafowany). Format ok. A4. Podpis odręczny (prawdopodobnie Józef Piłsudski lub przewodniczący Zjazdu). Na dole: 'Za Komisję Kwalifikacyjną' + podpis, 'Warszawa dn. 11.VII.1925', 'Nr. 145'.",
        "opis_tresci": "'NA PODSTAWIE / UCHWAŁY / II ZJAZDU LEGJONISTÓW / I / WNIOSKU / KOMISJI KWALIFIKACYJNEJ / nadaję / Pułkownikowi / Głuchowskiemu Januszowi / z 1.p.uł. / KRZYŻ LEGJONOWY / [podpis] / Za Komisję Kwalifikacyjną / [podpis] / Warszawa dn. 11.VII. 1925. / Nr. 145.' Dyplom nadania Krzyża Legionowego Nr 145 pułkownikowi Januszowi Głuchowskiemu z 1 Pułku Ułanów.",
        "seria": "II",
        "tworca": "II Zjazd Legionistów / Komisja Kwalifikacyjna, Warszawa",
        "jezyk": "polski",
        "kontekst": "Krzyż Legionowy — odznaczenie pamiątkowe nadawane uczestnikom Legionów Polskich 1914–1918 na mocy uchwały Zjazdu Legionistów. Nr 145 — niski numer, świadczący o wczesnym nadaniu. Janusz Głuchowski w 1925 r. w stopniu pułkownika (płk), dowódca 1 Pułku Ułanów (nie 7 P.U.L., w którym służył wcześniej). Data 11.VII.1925 — upamiętnia rocznicę wymarszu Siódemki Beliny (1914). Podpis prawdopodobnie Józefa Piłsudskiego jako patrona ruchu legionowego.",
        "powiazania": ["ARG/II/11"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/II/11",
        "photo": "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p06_img02.jpeg",
        "tytul": "Dyplom Krzyża Legionowego Nr 145 — widok pełny z portretem Piłsudskiego obok",
        "data": "11.VII.1925",
        "typ": "dyplom + fotografia",
        "opis_fizyczny": "Kompozycja dwuelementowa: po lewej dyplom Krzyża Legionowego (format ok. A4, druk ozdobny z odręcznymi wpisami), po prawej oddzielna fotografia portretowa w sepii (format ok. 10×15 cm). Fotografia przedstawia oficera w pełnym mundurze galowym z orderami i szablą — najprawdopodobniej Marszałek Józef Piłsudski. Dyplom z wizerunkiem Krzyża Legionowego u góry, poniżej tekst nadania.",
        "opis_tresci": "Pełny widok dyplomu Krzyża Legionowego Nr 145 dla płk. Głuchowskiego Janusza z 1.p.uł., nadanego 11.VII.1925 na podstawie uchwały II Zjazdu Legionistów. Obok dyplomu leży oddzielna fotografia portretowa w sepii — mężczyzna w mundurze galowym z orderami i szablą (najprawdopodobniej Józef Piłsudski lub sam Janusz Głuchowski w galowym mundurze pułkownika).",
        "seria": "II",
        "tworca": "II Zjazd Legionistów / Komisja Kwalifikacyjna",
        "jezyk": "polski",
        "kontekst": "Widok pełny dyplomu z ARG/II/10 wraz z portretem. Zestawienie dyplomu legionowego z portretem Piłsudskiego — układ typowy dla pamiątek kombatanckich. Krzyż Legionowy Nr 145 potwierdza udział Janusza w Legionach (Siódemka Beliny, 1914). Portret obok dyplomu to prawdopodobnie sam Piłsudski — patron Legionów i sygnatariusz dyplomu.",
        "powiazania": ["ARG/II/10"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/II/12",
        "photo": "Kolekcja_Gluchowski_Katalog_Tematyczny_p12_img02.jpeg",
        "tytul": "Propusk w pleń + legitymacja + pokwitowanie",
        "data": "1914–1920",
        "typ": "formularz",
        "opis_fizyczny": "Trzy drobne dokumenty sfotografowane razem: formularz rosyjski z pieczęcią, mała legitymacja, pokwitowanie",
        "opis_tresci": "'Propusk w pleń' (rosyjski przepustek do niewoli z pieczęcią Sztabu), mała zielona legitymacja/bilet, pokwitowanie z podpisem i pieczęcią (Lublin).",
        "seria": "II",
        "tworca": "Sztab rosyjski / WP",
        "jezyk": "rosyjski / polski",
        "kontekst": "'Propusk w pleń' — przepustka dla jeńca, dokument z frontu I wojny światowej. Świadczy o epizodzie niewoli rosyjskiej.",
        "powiazania": ["ARG/II/1"],
        "stan": "Średni"
    },
    {
        "sygn": "ARG/II/13",
        "photo": "Kolekcja_Gluchowski_Katalog_Tematyczny_p12_img03.jpeg",
        "tytul": "Legitymacja Krzyża Walecznych nr 42888",
        "data": "31.VII.1922",
        "typ": "leg",
        "opis_fizyczny": "Legitymacja drukowana z odręcznymi wpisami, format ok. 10×15 cm, pieczęć MSWojsk",
        "opis_tresci": "Legitymacja KW: Dowództwo M.S.Wojsk., nr leg. 42888. Rtm. Głuchowski Janusz, oddział 7 P.Uł., uprawniony do noszenia Krzyża Walecznych, Krzyż z 1 okuciem, Rozkazem Nr 12793/22. Podpis Ministra Spraw Wojskowych.",
        "seria": "II",
        "tworca": "Ministerstwo Spraw Wojskowych",
        "jezyk": "polski",
        "kontekst": "Krzyż Walecznych — najwyższe polskie odznaczenie bojowe za męstwo na polu walki. Nadanie za wojnę 1920. Głuchowski otrzymał KW wielokrotnie (4x wg IPN). Niniejsza legitymacja dokumentuje jedno z tych nadań.",
        "powiazania": ["ARG/II/10", "ARG/II/11"],
        "stan": "Dobry"
    },

    # -- Podseria II/D: Kariera ministerialna --
    {
        "sygn": "ARG/II/14",
        "photo": "Kolekcja_Gluchowski_Katalog_Tematyczny_p06_img02.jpeg",
        "tytul": "List odręczny Śmigłego-Rydza do Głuchowskiego",
        "data": "ok. 1935–1939",
        "typ": "list",
        "opis_fizyczny": "List odręczny atramentem na papierze firmowym, 1 karta",
        "opis_tresci": "List odręczny na papierze firmowym — do Majora/Pułkownika Głuchowskiego. Charakter pisma i kontekst sugerują autorstwo Marszałka Edwarda Śmigłego-Rydza.",
        "seria": "II",
        "tworca": "Marsz. Edward Śmigły-Rydz (?)",
        "jezyk": "polski",
        "kontekst": "Korespondencja prywatna z Naczelnym Wodzem II RP. Świadczy o osobistych relacjach Głuchowskiego z najwyższym dowództwem.",
        "powiazania": ["ARG/II/17"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/II/15",
        "photo": "Kolekcja_Gluchowski_Katalog_Tematyczny_p07_img01.jpeg",
        "tytul": "Pismo Ministerstwa Spraw Wojskowych, Biuro Personalne",
        "data": "lata 30. XX w.",
        "typ": "pismo",
        "opis_fizyczny": "Maszynopis na papierze firmowym MSWojsk, format A4, pieczęć",
        "opis_tresci": "Ministerstwo Spraw Wojskowych, Biuro Personalne — pismo L.97/... do Płk. Głuchowskiego. Oficjalne pismo ministerialne dot. mianowania lub audiencji.",
        "seria": "II",
        "tworca": "MSWojsk, Biuro Personalne",
        "jezyk": "polski",
        "kontekst": "Korespondencja służbowa z Biurem Personalnym MSWojsk — dot. awansów lub stanowisk.",
        "powiazania": ["ARG/II/16", "ARG/II/17"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/II/16",
        "photo": "Kolekcja_Gluchowski_Katalog_Tematyczny_p07_img02.jpeg",
        "tytul": "Dyplom Króla Rumunii Ferdynanda I — Order Korony Rumuńskiej",
        "data": "XII.1922",
        "typ": "dyplom",
        "opis_fizyczny": "Dyplom pergaminowy kaligrafowany, format A3+, pieczęć królewska, podpis Ferdynanda I",
        "opis_tresci": "Dyplom Króla Rumunii Ferdynanda I — nadanie Ordinul Coroanei României. Kaligrafowany dokument na pergaminie z pieczęcią i podpisem Ferdynanda.",
        "seria": "II",
        "tworca": "Kancelaria Króla Rumunii",
        "jezyk": "rumuński / francuski",
        "kontekst": "Ordinul Coroanei României — rumuński order dynastyczny nadawany cudzoziemcom za zasługi dyplomatyczne. Nadanie związane z misją wojskową lub sojuszem polsko-rumuńskim.",
        "powiazania": ["ARG/II/13"],
        "stan": "Dobry — dokument reprezentacyjny"
    },
    {
        "sygn": "ARG/II/17",
        "photo": "Kolekcja_Gluchowski_Katalog_Tematyczny_p08_img02.jpeg",
        "tytul": "Dekret Prezydenta RP — mianowanie",
        "data": "lata 30. XX w.",
        "typ": "dekret",
        "opis_fizyczny": "Dekret na grubym papierze urzędowym, format A4, kontrasygna Ministra",
        "opis_tresci": "Dekret Prezydenta Rzeczypospolitej Polskiej — Ministerstwo Spraw Wojskowych, kontrasygna Ministra. Oficjalny akt mianowania.",
        "seria": "II",
        "tworca": "Prezydent RP / MSWojsk",
        "jezyk": "polski",
        "kontekst": "Akt prawny najwyższej rangi — mianowanie na stopień generalski lub stanowisko rządowe.",
        "powiazania": ["ARG/II/18", "ARG/II/19"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/II/18",
        "photo": "Kolekcja_Gluchowski_Katalog_Tematyczny_p09_img01.jpeg",
        "tytul": "Akt mianowania na generała brygady",
        "data": "26.III.1933",
        "typ": "dekret",
        "opis_fizyczny": "Dokument urzędowy na grubym papierze, podpisy Prezydenta RP i Ministra",
        "opis_tresci": "Akt mianowania w korpusie generałów: Gen. bryg. Głuchowski Janusz — dowódca Okręgu Korpusu Nr I(?), 26 marca 1933. Podpisy Prezydenta RP i Ministra Spraw Wojskowych.",
        "seria": "II",
        "tworca": "Prezydent RP / MSWojsk",
        "jezyk": "polski",
        "kontekst": "Głuchowski awansował na gen. brygady już w 1927 r. Dokument z 1933 r. dotyczy prawdopodobnie nominacji na Dowódcę Okręgu Korpusu nr X (1933-1935). Najwyższy stopień — gen. dywizji — otrzymał dopiero 1.VI.1945. Dowodzenie Okręgiem Korpusu = zarządzanie garnizonami i mobilizacją na dużym terytorium.",
        "powiazania": ["ARG/II/17", "ARG/II/19"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/II/19",
        "photo": "Kolekcja_Gluchowski_Katalog_Tematyczny_p09_img02.jpeg",
        "tytul": "Akt mianowania na I Wiceministra Spraw Wojskowych",
        "data": "5.X.1935",
        "typ": "dekret",
        "opis_fizyczny": "Dokument urzędowy, format A4, pieczęć Ministerstwa, podpisy",
        "opis_tresci": "Akt mianowania: Generała brygady Głuchowskiego Janusza, dnia 5 października 1935. Prezydent RP + Minister MSWojsk. Pieczęć Ministerstwa. Mianowanie na I Wiceministra Spraw Wojskowych.",
        "seria": "II",
        "tworca": "Prezydent RP / MSWojsk",
        "jezyk": "polski",
        "kontekst": "SZCZYT KARIERY — I Zastępca Ministra Spraw Wojskowych = druga osoba w resorcie obrony II RP. Stanowisko kluczowe w przygotowaniach do wojny. Na tym stanowisku Głuchowski wydał rozkazy tworzące Dowództwo Obrony Warszawy (gen. Czuma) we wrześniu 1939 oraz nakazał ewakuację pilotów do Rumunii.",
        "powiazania": ["ARG/II/18"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/II/20",
        "photo": "Kolekcja_Gluchowski_Katalog_Tematyczny_p10_img01.jpeg",
        "tytul": "Rozkaz wyjazdu — formularz MSWojsk",
        "data": "lata 30. XX w.",
        "typ": "formularz",
        "opis_fizyczny": "Formularz służbowy z pieczęcią, maszynopis z odręcznymi wpisami",
        "opis_tresci": "Rozkaz wyjazdu — MSWojsk, SZTAB, Seria J nr 116321. Generał bryg. Głuchowski Janusz, cel podróży: inspekcja. Formularz służbowy.",
        "seria": "II",
        "tworca": "MSWojsk, Sztab",
        "jezyk": "polski",
        "kontekst": "Codzienny dokument biurokratyczny armii — świadczy o inspekcjach jednostek przez wiceministra.",
        "powiazania": ["ARG/II/19"],
        "stan": "Dobry"
    },

    # -- Podseria II/E: Korespondencja i fotokopie --
    {
        "sygn": "ARG/II/21",
        "photo": "Kolekcja_Gluchowski_Katalog_Tematyczny_p11_img01.jpeg",
        "tytul": "List prywatny do Pułkownika Głuchowskiego (1925)",
        "data": "4.VIII.1925",
        "typ": "list",
        "opis_fizyczny": "Koperta z adresem + list odręczny na papierze monogramowanym, atrament",
        "opis_tresci": "Koperta 'Ś. Wielmożny Pan Pułkownik J. Głuchowski' + list odręczny na monogramowanym papierze (inicjały), datowany 4/8 '25.",
        "seria": "II",
        "tworca": "nieznany nadawca",
        "jezyk": "polski",
        "kontekst": "Korespondencja prywatna na papierze z monogramem — świadczy o kręgu towarzyskim wyższej kadry oficerskiej.",
        "powiazania": [],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/II/22",
        "photo": "Kolekcja_Gluchowski_Katalog_Tematyczny_p13_img01.jpeg",
        "tytul": "Fotokopia prasowa — Śmigły-Rydz wręcza sztandar 17 P.Uł.",
        "data": "ok. 1937",
        "typ": "fotokopia",
        "opis_fizyczny": "Fotokopia zdjęcia prasowego, format ok. 18×12 cm, podpisy odręczne na marginesie",
        "opis_tresci": "Marszałek Edward Śmigły-Rydz wręcza sztandar 17 Pułku Ułanów Wielkopolskich. Podpisy: d-ca Brygady gen. Janusz Głuchowski, gen. Roman Abraham, gen. Knoll-Kownacki, płk Kowalczewski.",
        "seria": "II",
        "tworca": "fotoreporter prasowy",
        "jezyk": "polski",
        "kontekst": "Ceremonia wojskowa najwyższej rangi — wręczenie sztandaru przez Naczelnego Wodza. Głuchowski jako dowódca Brygady Kawalerii.",
        "powiazania": ["ARG/II/14"],
        "stan": "Średni — fotokopia"
    },
    {
        "sygn": "ARG/II/23",
        "photo": "Kolekcja_Gluchowski_Katalog_Tematyczny_p13_img02.jpeg",
        "tytul": "Portret gen. Janusza Głuchowskiego w mundurze galowym",
        "data": "lata 30. XX w.",
        "typ": "foto",
        "opis_fizyczny": "Fotografia portretowa studyjna, czarno-biała, odbitka na papierze fotograficznym",
        "opis_tresci": "Portret fotograficzny gen. Janusza Głuchowskiego w mundurze galowym z orderami i epoletami. Zdjęcie studyjne. Jedyne zdjęcie portretowe generała w kolekcji.",
        "seria": "II",
        "tworca": "atelier fotograficzne (nieznane)",
        "jezyk": "—",
        "kontekst": "Portret oficjalny generała II RP. Widoczne ordery pozwalają na identyfikację: Virtuti Militari (V kl.), Krzyż Niepodległości z Mieczami, Order Odrodzenia Polski, Krzyż Walecznych (4x), Order Korony Rumuńskiej. Na portrecie w mundurze wz.36 z gwiazdkami generalskimi.",
        "powiazania": [],
        "stan": "Dobry"
    },

    # -- Podseria II/F: PSZ na Zachodzie --
    {
        "sygn": "ARG/II/24",
        "photo": "Kolekcja_Gluchowski_Katalog_Tematyczny_p13_img03.jpeg",
        "tytul": "List do Generała — Londyn 14.IX.1943",
        "data": "14.IX.1943",
        "typ": "list",
        "opis_fizyczny": "List odręczny atramentem, 1 karta, kaligraficzne pismo",
        "opis_tresci": "'Szanowny Panie Generale!' — datowany 14.IX.1943, kaligraficzne pismo atramentem. Korespondencja z okresu londyńskiego.",
        "seria": "II",
        "tworca": "nieznany nadawca",
        "jezyk": "polski",
        "kontekst": "Głuchowski po 1939 internowany w Rumunii, dotarł do Palestyny (X.1940), potem Londyn (II.1941). Od III.1941 generał do dyspozycji Naczelnego Wodza. Od X.1941 dowodził Brygadą Szkolną w Szkocji. Od IX.1943 — Dowódca Polskich Jednostek Wojskowych w Wielkiej Brytanii. List z 14.IX.1943 datowany tuż po objęciu tego kluczowego stanowiska.",
        "powiazania": ["ARG/II/25"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/II/25",
        "photo": "Kolekcja_Gluchowski_Katalog_Tematyczny_p14_img01.jpeg",
        "tytul": "Pismo z 2 Pułku Piechoty Legionowej",
        "data": "20.IX.1943",
        "typ": "pismo",
        "opis_fizyczny": "Maszynopis na papierze firmowym jednostki, format A4",
        "opis_tresci": "Dowódca 2 Pułku Piechoty Legionowej, Zambrów — pismo do Gen. bryg. Głuchowskiego Janusza. Dokument wojskowy PSZ z okresu wojny.",
        "seria": "II",
        "tworca": "D-ca 2 PP Leg.",
        "jezyk": "polski",
        "kontekst": "Korespondencja służbowa w ramach PSZ.",
        "powiazania": ["ARG/II/24"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/II/26",
        "photo": "Kolekcja_Gluchowski_Katalog_Tematyczny_p08_img01.jpeg",
        "tytul": "Adres iluminowany — akwarela od oficerów (IX.1945)",
        "data": "IX.1945",
        "typ": "dyplom",
        "opis_fizyczny": "Akwarela/adres iluminowany na kartonie, format ok. A4, kolorowe flagi (brytyjska, polska), herb kawalerii, ręcznie malowany",
        "opis_tresci": "'Panu Generałowi Januszowi Głuchowskiemu C.B. na pamiątkę miłej współpracy od Oficerów A.M.S.i La..., wrzesień 1945.' Kolorowe flagi, herb kawalerii.",
        "seria": "II",
        "tworca": "Oficerowie AMS",
        "jezyk": "polski",
        "kontekst": "Adres iluminowany — tradycyjna forma podziękowań. 'C.B.' = Companion of the Order of the Bath — wysokie odznaczenie brytyjskie nadane Głuchowskiemu za dowodzenie polskimi jednostkami w Wielkiej Brytanii (IX.1943 – IX.1945). Adres od oficerów Allied Military Service po zakończeniu wojny.",
        "powiazania": [],
        "stan": "Dobry — kolorowy, dekoracyjny"
    },

    # -- Podseria II/G: Emigracja i dokumenty późne --
    {
        "sygn": "ARG/II/27",
        "photo": "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p09_img01.jpeg",
        "tytul": "List gen. Kazimierza Sosnkowskiego z Kanady do gen. Głuchowskiego — 28 V 1964, Arundel, P.Qué.",
        "data": "28.V.1964",
        "typ": "list",
        "opis_fizyczny": "Maszynopis z własnoręcznym podpisem Kazimierza Sosnkowskiego, 1 karta, format A4. Na dole: adnotacja 'Canada', data, podpis odręczny i dedykacja atramentem. Papier listowy.",
        "opis_tresci": "List prywatny od gen. broni Kazimierza Sosnkowskiego — Naczelnego Wodza PSZ 1943–1944 — do gen. dyw. Janusza Głuchowskiego. Adresowany 'Kochany Generale'. Treść: przeprosiny za nieporozumienie dotyczące Instytutu Józefa Piłsudskiego i sprawy Larousse'a; wzmianka o 'nieszczęśliwym wypadku pułk. Smoleńskiego'; praca nad przedmową dla Narbutta; kluczowo — artykuł o patrolu Beliny: 'Postaram się przyśpieszyć rzecz o patrolu Beliny.' Nadany z Arundel, P.Qué. (Province de Québec), Kanada. KOMPLET z załącznikiem 'Pro memoria' (ARG/II/28 + ARG/II/29).",
        "seria": "II",
        "tworca": "Gen. broni Kazimierz Sosnkowski (1885–1969)",
        "jezyk": "polski",
        "kontekst": "Gen. Kazimierz Sosnkowski — Naczelny Wódz PSZ (VII.1943 – IX.1944), najwyższej rangi żyjący generał polski w 1964. Od XI.1944 na emigracji w Kanadzie (farma w Arundel, Quebec). List pisany 14 dni przed śmiercią Głuchowskiego (zm. 11.VI.1964) — jedno z OSTATNICH pism Sosnkowskiego do przyjaciela. 51-letni łuk relacji: egzamin ZWC w Stróżach (1913) → KW jako minister (1922) → zaświadczenie OB PPS (1935) → list z Kanady (1964). Piąty dokument Sosnkowskiego w kolekcji. Sosnkowski pisał o patrolu Beliny do człowieka, który w tym patrolu UCZESTNICZYŁ — jeden z Siódemki. DOKUMENT EKSTREMALNIE RZADKI — autograf Naczelnego Wodza z okresu kanadyjskiego, prywatna korespondencja.",
        "powiazania": ["ARG/II/3", "ARG/II/4", "ARG/II/28", "ARG/II/29"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/II/28",
        "photo": "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p14_img01.jpeg",
        "tytul": "'Pro memoria' gen. Sosnkowskiego — załącznik do listu z 28.V.1964, str. 1 (poz. 1–14)",
        "data": "28.V.1964",
        "typ": "notatka",
        "opis_fizyczny": "Maszynopis na papierze kancelaryjnym, format A4, strona 1 z 2. Tytuł 'Pro memoria' napisany odręcznie czerwonym atramentem. 14 pozycji numerowanych.",
        "opis_tresci": "Pierwsza strona dwustronicowego maszynopisu 'Pro memoria' — lista 24 zamówień i próśb ciążących na gen. Sosnkowskim w 1964 roku. Strona 1 zawiera pozycje 1–14, w tym: poz. 5 — prośba gen. Głuchowskiego o tekst o początkach Kawalerii Polskiej; poz. 7 — Płk. Smoleński o wspomnienia o patrolu Beliny. Dokument ujawnia sieć kontaktów Sosnkowskiego rozpiętą od Buenos Aires przez Toronto i Chicago po Londyn i Paryż.",
        "seria": "II",
        "tworca": "Gen. broni Kazimierz Sosnkowski (1885–1969)",
        "jezyk": "polski",
        "kontekst": "Załącznik do listu ARG/II/27. 'Pro memoria' ujawnia rolę Sosnkowskiego jako żywej pamięci historycznej polskiej emigracji. Lista 24 zamówień od różnych instytucji i osób: historycy, redakcje, archiwa. Sosnkowski w 1964 roku miał prawie 80 lat ('Za parę miesięcy rozpoczynam 80-ty rok życia i siły moje bynajmniej nie są nieograniczone'). Pisał z Arundel (Quebec) do całego świata. Głuchowski (poz. 5) prosił o tekst o kawalerii — jako jeden z Siódemki miał prawo żądać tego od współtwórcy ich legendy.",
        "powiazania": ["ARG/II/27", "ARG/II/29"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/II/29",
        "photo": "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p14_img02.jpeg",
        "tytul": "'Pro memoria' gen. Sosnkowskiego — str. 2 (poz. 15–24), z cytatem '80-ty rok życia'",
        "data": "28.V.1964",
        "typ": "notatka",
        "opis_fizyczny": "Maszynopis, strona 2 z 2. Pozycje 15–24 + zakończenie z osobistym wyznaniem Sosnkowskiego.",
        "opis_tresci": "Druga strona 'Pro memoria'. Zawiera dalsze zamówienia: poz. 19 — 21. rocznica śmierci gen. Sikorskiego (Chicago); poz. 20–21 — dyrektor J. Nowak, audycje Radia Wolna Europa; poz. 22–23 — Jerzy Giedroyć z paryskiej 'Kultury' o dwa artykuły. Zakończenie: 'Za parę miesięcy rozpoczynam 80-ty rok życia i siły moje bynajmniej nie są nieograniczone.' Poniżej: odręczne uwagi.",
        "seria": "II",
        "tworca": "Gen. broni Kazimierz Sosnkowski (1885–1969)",
        "jezyk": "polski",
        "kontekst": "Kontynuacja ARG/II/28. Giedroyć i 'Kultura' paryska = najważniejsze intelektualne czasopismo polskiej emigracji. Radio Wolna Europa = informacyjna linia ratunkowa dla kraju za żelazną kurtyną. J. Nowak = prawdopodobnie Jan Nowak-Jeziorański, legendarny kurier z Warszawy i dyrektor RWE (1952–1976). Cytat '80-ty rok życia' — Sosnkowski urodził się 19.XI.1885, więc w maju 1964 miał 78 lat, 80-ty rok życia rozpoczynałby w XI.1964. Zmarł 11.X.1969.",
        "powiazania": ["ARG/II/27", "ARG/II/28"],
        "stan": "Dobry"
    },

    # -- Podseria II/H: Legitymacja oficerska --
    {
        "sygn": "ARG/II/30",
        "photo": "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p13_img01.jpeg",
        "tytul": "Legitymacja oficerska gen. bryg. Janusza Głuchowskiego — strona ze zmianami (1930)",
        "data": "1929–1937",
        "typ": "legitymacja",
        "opis_fizyczny": "Legitymacja oficerska w twardej oprawie — rozkładówka wewnętrzna (strona ze zmianami i przedłużeniami). Lewa strona: drukowane rubryki 'Przedłużam ważność niniejszej legitymacji do dnia 31 grudnia 19__ r.' (dwie puste). Prawa strona: rubryka 'Zmiany:' z dwoma wpisami odręcznymi. Pieczęć czerwona MSWojsk. Podpisy.",
        "opis_tresci": "Strona 'Zmiany' w legitymacji oficerskiej: (1) 'Dz. Pers. Nr 13 z dn. 31.IV.30. — przeniesiony do dysp. [...] Szef Gabinetu Ministra [podpis] [pieczęć MSWojsk]'. (2) 'Dz. Pers. Nr 11 z dn. 18.IX.1930 — mianowany na Dowódcę/Komendanta Centrum Wyszkolenia [...] Legionowych [podpis] GENERAŁ DYWIZJI [podpis]'. Wpisy dokumentujące przeniesienia służbowe gen. bryg. Głuchowskiego w 1930 roku.",
        "seria": "II",
        "tworca": "Ministerstwo Spraw Wojskowych / Biuro Personalne",
        "jezyk": "polski",
        "kontekst": "Wpisy w legitymacji z 1930 r. dokumentują karierę Janusza: (1) przeniesienie do dyspozycji Ministra (31.IV.1930), (2) mianowanie na Dowódcę/Komendanta ośrodka szkolenia piechoty (18.IX.1930). Podpisane przez Generała Dywizji (prawdopodobnie Piskor lub Rydz-Śmigły). Pieczęć czerwona Ministerstwa Spraw Wojskowych.",
        "powiazania": ["ARG/II/31", "ARG/II/32"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/II/31",
        "photo": "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p13_img02.jpeg",
        "tytul": "Legitymacja oficerska — rozkładówka z fotografią i danymi gen. bryg. Głuchowskiego",
        "data": "6.I.1929",
        "typ": "legitymacja",
        "opis_fizyczny": "Rozkładówka legitymacji oficerskiej w twardej oprawie. Lewa strona: fotografia portretowa gen. Głuchowskiego w mundurze galowym z orderami (format ok. 4×6 cm), pod spodem podpis odręczny: 'Janusz Głuchowski / gen. br.' Prawa strona: drukowane rubryki z odręcznymi wpisami danymi personalnymi. Pismo kaligraficzne atramentem.",
        "opis_tresci": "Dane z legitymacji: 'Imię i nazwisko: Janusz Głuchowski / Stopień wojskowy: Generał bryg. / W stanie: czynnym / D.O.K. I / Przydział: D-two 4. dywizji [?] / Funkcja: Dowódca O.K.I [?] / D-ca 4. dywizji [?] / Stała przynależność: Biuro Personalne M.S.Wojsk.' Na fotografii: Janusz w mundurze galowym z epoletami generała brygady, orderami na piersi (VM, KW, KL, zagraniczne). Podpis pod zdjęciem potwierdza stopień 'gen. br.' JEDYNE ZNANE ZDJĘCIE PORTRETOWE gen. Głuchowskiego w legitymacji wojskowej.",
        "seria": "II",
        "tworca": "Wojsko Polskie / Biuro Personalne MSWojsk",
        "jezyk": "polski",
        "kontekst": "KLUCZOWY DOKUMENT IKONOGRAFICZNY — jedyne zdjęcie portretowe gen. Głuchowskiego w mundurze galowym z orderami. Legitymacja wystawiona w D.O.K. I (Dowództwo Okręgu Korpusu Nr I — Warszawa). Stopień: generał brygady (mianowany 1927). Przydział: D-two 4 dywizji lub D.O.K. I. Stała przynależność: Biuro Personalne MSWojsk — potwierdza rolę w strukturach ministerstwa. Zdjęcie pokazuje ordery: prawdopodobnie VM (Virtuti Militari), KW (Krzyż Walecznych), KL (Krzyż Legionowy Nr 145), odznaczenia zagraniczne (rumuński, francuski, estoński).",
        "powiazania": ["ARG/II/30", "ARG/II/32"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/II/32",
        "photo": "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p13_img03.jpeg",
        "tytul": "Legitymacja oficerska — ordery i odznaczenia + przedłużenia ważności (1929–1937)",
        "data": "6.I.1929 (wystawienie); 1932, 1937 (przedłużenia)",
        "typ": "legitymacja",
        "opis_fizyczny": "Rozkładówka legitymacji oficerskiej. Lewa strona: drukowana rubryka 'Posiadane ordery i odznaczenia:' z 5 wpisami odręcznymi + rubryka 'Miejsce i data wystawienia legitymacji:' z datą i podpisem. Prawa strona: dwie rubryki przedłużenia ważności (do 1932 i 1937), pieczęcie, podpisy generałów.",
        "opis_tresci": "ORDERY I ODZNACZENIA gen. bryg. Głuchowskiego wpisane w legitymacji: (1) 'Virtuti Militari M.P. — Dz.Pers. Nr [?]', (2) 'Krzyż Walecznych z 2 okna[mi?] — Dz.Pers. Nr [?]' (KW z dwoma okuciami = trzykrotne nadanie!), (3) 'Złoty Krzyż Zasługi — Dz.Pers. Nr [?]', (4) 'France: Leg. Honor. Krzyż Kawalerski — Rumunja [Order Korony Rumunii]', (5) '3 S.R. Komandorski — Estoński — I P. [?]'. Legitymacja wystawiona: '[?], dnia 6.I. 1929 r.', ważna do 31.XII.1929. Podpis wystawiającego: 'MARJAN CZERNIEWS[KI] / Pułkownik Szt. Gen.' Przedłużenia: do 31.XII.1932, do 31.XII.1937. Podpisy: GENERAŁ DYWIZJI [podpis].",
        "seria": "II",
        "tworca": "Wojsko Polskie / płk SG Marian Czerniewski (wystawiający)",
        "jezyk": "polski",
        "kontekst": "PEŁNA LISTA ODZNACZEŃ Janusza Głuchowskiego wpisana urzędowo: Virtuti Militari (najwyższe polskie odznaczenie wojskowe), Krzyż Walecznych z 2 okuciami (trzykrotnie odznaczony za męstwo!), Złoty Krzyż Zasługi, francuski Krzyż Kawalera Legii Honorowej, rumuński Order Korony Rumunii, estoński Krzyż Komandorski. Wystawiona przez płk SG Mariana Czerniewskiego 6.I.1929. Przedłużana dwukrotnie (1932, 1937) — podpisy generałów dywizji (prawdopodobnie Piskor lub Rydz-Śmigły). Legitymacja ważna aż do 1937 — prawdopodobnie zastąpiona nową przed wojną.",
        "powiazania": ["ARG/II/30", "ARG/II/31"],
        "stan": "Dobry"
    },

    # -- Biogram (z kolekcji Krzysztofa) --
    {
        "sygn": "ARG/II/33",
        "photo": "juras_091_page92.png",
        "tytul": "Biogram gen. Janusza J. Głuchowskiego i Czesława Grochulskiego — KWARTALNIK BIOGRAFICZNY POLONII Nr 7",
        "data": "lata 60.–70. XX w.",
        "typ": "biogram",
        "opis_fizyczny": "Strona z Kwartalnika Biograficznego Polonii Nr 7. Druk encyklopedyczny ze zdjęciami portretowymi dwóch osób. Format A4, dwie kolumny tekstu. Dwa zdjęcia: jedno gen. Głuchowskiego w mundurze, drugie Grochulskiego.",
        "opis_tresci": "KWARTALNIK BIOGRAFICZNY POLONII Nr 7 — biogram GEN. JANUSZA JULIANA GŁUCHOWSKIEGO: ur. 06.08.1888, zm. XI.1964 Londyn. Studia w Liège (Belgia). Założyciel/członek Związku Strzeleckiego. Legiony Polskie 1914 — Siódemka Beliny. Organizator 7 Pułku Ułanów 1918-1920. D-ca 1 Brygady Kawalerii ok. 1924. I WICEMINISTER SPRAW WOJSKOWYCH 1935–1939. GOC Polish Troops in Scotland 1941–1943. GOC Training Command (JWWB) 1943–1945. Współzałożyciel Polish Institute and Sikorski Museum. Odznaczenia: Krzyż Walecznych (3x), Légion d'honneur, Order of Merit i inne. Drugi biogram: GROCHULSKI CZESŁAW (ur. 07.12.1906 Baranowicze) — aktor teatralny, Polish Air Force od 1945.",
        "seria": "II",
        "tworca": "Kwartalnik Biograficzny Polonii",
        "jezyk": "polski, angielski",
        "kontekst": "Kwartalnik Biograficzny Polonii — encyklopedyczne wydawnictwo dokumentujące biogramy wybitnych Polaków na emigracji. KLUCZOWE ŹRÓDŁO do biografii gen. Głuchowskiego — potwierdza: studia w Liège, Siódemkę Beliny, organizację 7 P.Uł., stanowisko I Wiceministra Spraw Wojskowych (1935–1939), dowodzenie we Włoszech i Szkocji, współzałożenie Instytutu Sikorskiego.",
        "powiazania": ["ARG/II/1", "ARG/VI/14", "ARG/V/132"],
        "stan": "Dobry"
    },

    # =====================================================================
    # SERIA III — PPOR. STANISŁAW STEFAN GŁUCHOWSKI
    # =====================================================================
    {
        "sygn": "ARG/III/1",
        "photo": "Seria_29z_p04_img01.jpeg",
        "tytul": "Kriegsgefangenenpost — kartka jeńca (awers)",
        "data": "20.X.1944",
        "typ": "kartka",
        "opis_fizyczny": "Karta pocztowa jeńca (Postkarte), formularz drukowany z odręcznymi wpisami, stempel pocztowy 20.10.44",
        "opis_tresci": "Nadawca: Głuchowski, nr jeniecki 0.1245. Adresat: do Zofii, ul. Pułaskiej, Kleczew, gmina Brzezówce, powiat Radomsko, Generalgouvernement. Stempel: 20.10.44.",
        "seria": "III",
        "tworca": "Stanisław Stefan Głuchowski",
        "jezyk": "niemiecki (formularz) / polski (treść)",
        "kontekst": "Kriegsgefangenenpost datowana 20.X.1944 — 18 dni po kapitulacji Powstania Warszawskiego (2.X.1944). Stefan został schwytany po kapitulacji i jako oficer (ppor.) otrzymał status jeńca wojennego. Nr 0.1245 = numer oficerski. Adresatka Zofia w Radomsku — prawdopodobnie krewna z rodzinnych stron Głuchowskich (majątek Bukowa, pow. piotrkowski). Wg biogramu 1944.pl Stefan przeszedł 5 obozów: Stalag XI-B Fallingbostel → Bergen → Oflag II D Gross-Born → Stalag X-B Sandbostel → Oflag X-C Lübeck. Kontekst: Stefan był aresztowany przez Gestapo w maju 1944 (Pawiak, Aleja Szucha!), zwolniony 29.VII.1944 — 3 dni przed Powstaniem. Podczas Powstania: kwatermistrz Obwodu I Śródmieście AK.",
        "powiazania": ["ARG/III/2", "ARG/III/28", "ARG/III/30"],
        "stan": "Średni — pożółkły, stempel czytelny"
    },
    {
        "sygn": "ARG/III/2",
        "photo": "Seria_29z_p04_img02.jpeg",
        "tytul": "Kriegsgefangenenpost — rewers, 14.X.1944",
        "data": "14.X.1944",
        "typ": "kartka",
        "opis_fizyczny": "Rewers kartki pocztowej, pismo ołówkowe",
        "opis_tresci": "M.-Stammlager XI B, 14.X.1944. 'Droga Zocha! Jestem w oflagu, Krzysztof w Stalagu...' Pisze z obozu Fallingbostel, pyta o rodzinę.",
        "seria": "III",
        "tworca": "Stanisław Stefan Głuchowski",
        "jezyk": "polski",
        "kontekst": "KLUCZOWA INFORMACJA — ojciec (oficer, oflag) i syn (szeregowy, stalag) w różnych obozach. Stefan wie, gdzie jest Krzysztof.",
        "powiazania": ["ARG/III/1", "ARG/V/5"],
        "stan": "Średni"
    },
    {
        "sygn": "ARG/III/3",
        "photo": "Seria_29z_p07_img01.jpeg",
        "tytul": "Kriegsgefangenenpost — ojciec do syna (awers koperty)",
        "data": "XI.1944",
        "typ": "kartka",
        "opis_fizyczny": "Koperta/formularz Rückantwortbrief, stemple cenzury",
        "opis_tresci": "Do: Głuchowski St.Uł. Krzysztof, nr 141009, Stalag VI/3 Dorsten. Nadawca: Ppor. Stefan Głuchowski, nr 0.1845, Stalag XI B. Pieczęć cenzury. KORESPONDENCJA MIĘDZY DWOMA JEŃCAMI — ojciec i syn w różnych obozach!",
        "seria": "III",
        "tworca": "Stanisław Stefan Głuchowski",
        "jezyk": "niemiecki (formularz) / polski (treść)",
        "kontekst": "Dokument wyjątkowy — korespondencja między ojcem i synem, obaj jeńcy w różnych Stalagach. Stefan (XI B, Fallingbostel) → Krzysztof (VI/3, Dorsten).",
        "powiazania": ["ARG/III/4", "ARG/V/5"],
        "stan": "Średni"
    },
    {
        "sygn": "ARG/III/4",
        "photo": "Seria_29z_p07_img02.jpeg",
        "tytul": "List ojca do syna — rewers",
        "data": "XI.1944",
        "typ": "list",
        "opis_fizyczny": "Rewers formularza, gęste pismo ołówkowe",
        "opis_tresci": "Długi list Stefana do Krzysztofa. 'Mama na ul. Howe-Monatkiego w Częstochowie', wspomina wielu krewnych. Podpis 'Stefek'. Intymna korespondencja rodzinna z niewoli.",
        "seria": "III",
        "tworca": "Stanisław Stefan Głuchowski",
        "jezyk": "polski",
        "kontekst": "List o wielkim ładunku emocjonalnym. Ojciec-jeniec pisze do syna-jeńca o rodzinie w Częstochowie.",
        "powiazania": ["ARG/III/3"],
        "stan": "Średni — pismo ołówkowe, wyblakłe"
    },
    {
        "sygn": "ARG/III/5",
        "photo": "Seria_29z_p10_img01.jpeg",
        "tytul": "Kartka Stefana z obozu (awers, 4.XII.1944)",
        "data": "4.XII.1944",
        "typ": "kartka",
        "opis_fizyczny": "Kriegsgefangenenpost, stempel 04.12.44",
        "opis_tresci": "Nadawca: Ppor. Stefan Głuchowski, nr 0.1845, M.-Stammlager XI B. Adresat: ul. Piaseczna, Kleczew. Stempel: 04.12.44.",
        "seria": "III",
        "tworca": "Stanisław Stefan Głuchowski",
        "jezyk": "niemiecki / polski",
        "kontekst": "Kolejna kartka do żony/rodziny w Kleczewie.",
        "powiazania": ["ARG/III/6"],
        "stan": "Średni"
    },
    {
        "sygn": "ARG/III/6",
        "photo": "Seria_29z_p10_img02.jpeg",
        "tytul": "Kartka Stefana — rewers 30.X.1944",
        "data": "30.X.1944",
        "typ": "kartka",
        "opis_fizyczny": "Rewers kartki, pismo ołówkowe gęste",
        "opis_tresci": "Datowany 30.X.1944. Długi list ołówkiem. Wspomina nr 141009 (numer Krzysztofa), pisze o warunkach obozowych. Podpis 'Stefan'.",
        "seria": "III",
        "tworca": "Stanisław Stefan Głuchowski",
        "jezyk": "polski",
        "kontekst": "Ojciec śledzi losy syna. Nr 141009 = Krzysztof w Stalagu XI B.",
        "powiazania": ["ARG/III/5", "ARG/V/1"],
        "stan": "Średni"
    },
    {
        "sygn": "ARG/III/7",
        "photo": "Seria_29z_p02_img01.jpeg",
        "tytul": "Stempel cenzora obozowego",
        "data": "1944",
        "typ": "formularz",
        "opis_fizyczny": "Fragment papieru w kratkę z wyblakłym stemplem",
        "opis_tresci": "Stempel/pieczątka na papierze w kratkę — wyblakły stempel cenzora obozowego lub pocztowego.",
        "seria": "III",
        "tworca": "cenzura obozowa",
        "jezyk": "niemiecki",
        "kontekst": "Cenzura korespondencji jenieckie — stempel 'Geprüft' potwierdzał przejście kontroli.",
        "powiazania": ["ARG/III/1"],
        "stan": "Słaby — wyblakły"
    },
    {
        "sygn": "ARG/III/8",
        "photo": "Seria_29z_p02_img02.jpeg",
        "tytul": "List obozowy na papierze w kratkę (16.X.1944)",
        "data": "16.X.1944",
        "typ": "list",
        "opis_fizyczny": "Kartka z zeszytu w kratkę, pożółkła, ubytki, pismo ołówkowe",
        "opis_tresci": "List odręczny na papierze w kratkę, bardzo zniszczony, pożółkły, z ubytkami. Datowany '16.X...' Charakter pisma sugeruje warunki obozowe.",
        "seria": "III",
        "tworca": "Stanisław Stefan Głuchowski",
        "jezyk": "polski",
        "kontekst": "List pisany w warunkach obozu jenieckiego — deficyt papieru, ołówek zamiast atramentu.",
        "powiazania": ["ARG/III/1"],
        "stan": "Słaby — zniszczony, ubytki"
    },
    {
        "sygn": "ARG/III/9",
        "photo": "Seria_29z_p03_img01.jpeg",
        "tytul": "Adres baraku obozowego",
        "data": "1944–1945",
        "typ": "notatka",
        "opis_fizyczny": "Kartka/kartonik z odręcznym adresem ołówkiem",
        "opis_tresci": "'Ppor. Stefan... Głuchowski... Barak 20 Lind...' — adres baraku w obozie jenieckim. Pismo ołówkowe na kartonie.",
        "seria": "III",
        "tworca": "nieznany",
        "jezyk": "polski / niemiecki",
        "kontekst": "Adres barakowy — pozwala zlokalizować jenieckie zakwaterowanie.",
        "powiazania": ["ARG/III/1"],
        "stan": "Średni"
    },

    # =====================================================================
    # SERIA V — KRZYSZTOF ANDRZEJ GŁUCHOWSKI
    # =====================================================================

    # -- Podseria V/A: Okupacja i AK --
    {
        "sygn": "ARG/V/1",
        "photo": "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p23_img02.jpeg",
        "tytul": "Kennkarte Generalnego Gubernatorstwa — okładka",
        "data": "1941–1944",
        "typ": "karta_id",
        "opis_fizyczny": "Dokument kartonowy składany, format ok. 10×15 cm, druk niemieckojęzyczny",
        "opis_tresci": "Okładka Kennkarte (karty rozpoznawczej) wydanej w Generalnym Gubernatorstwie. Dokument tożsamości obowiązujący Polaków pod okupacją niemiecką.",
        "seria": "V",
        "tworca": "Urząd GG",
        "jezyk": "niemiecki / polski",
        "kontekst": "Kennkarte — przymusowy dokument tożsamości dla ludności polskiej w GG. Obowiązek posiadania od 14 roku życia.",
        "powiazania": ["ARG/V/2"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/V/2",
        "photo": "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p23_img03.jpeg",
        "tytul": "Kennkarte GG — wnętrze ze zdjęciem i odciskami palców",
        "data": "1941–1944",
        "typ": "karta_id",
        "opis_fizyczny": "Rozkładówka ze zdjęciem legitymacyjnym, odciski palców, pieczęć urzędowa",
        "opis_tresci": "Wnętrze Kennkarte z fotografią legitymacyjną Krzysztofa Głuchowskiego, danymi osobowymi i odciskami palców. Formularz niemieckojęzyczny z pieczęcią urzędową.",
        "seria": "V",
        "tworca": "Urząd GG",
        "jezyk": "niemiecki",
        "kontekst": "Zdjęcie młodego człowieka (ok. 15–17 lat) — jednocześnie jawny mieszkaniec GG i tajny żołnierz AK.",
        "powiazania": ["ARG/V/1", "ARG/V/3"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/V/3",
        "photo": "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p23_img04.jpeg",
        "tytul": "Legitymacja AK + galony wojskowe",
        "data": "8.IV.1944",
        "typ": "leg",
        "opis_fizyczny": "Mała legitymacja papierowa + galony/wstążki obok; sfotografowane razem",
        "opis_tresci": "Legitymacja Armii Krajowej: Krzysztof Głuchowski, ps. 'Juras', Pluton nr 1112, ur. 29.XI.1926, datowana 8.IV.1944. Obok galony i wstążki orderowe.",
        "seria": "V",
        "tworca": "AK, Komenda Okręgu Warszawa",
        "jezyk": "polski",
        "kontekst": "KLUCZOWY DOKUMENT — legitymacja AK z pseudonimem 'Juras' i numerem plutonu 1112 (7 P.Uł. AK 'Jeleń'). Data 8.IV.1944 = 4 miesiące przed Powstaniem.",
        "powiazania": ["ARG/V/1", "ARG/V/2", "ARG/V/4"],
        "stan": "Średni — papier cienki, naddarcia"
    },
    {
        "sygn": "ARG/V/4",
        "photo": "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p26_img02.jpeg",
        "tytul": "Legitymacja AK — zbliżenie",
        "data": "1944",
        "typ": "leg",
        "opis_fizyczny": "Zbliżenie fotograficzne legitymacji AK",
        "opis_tresci": "Zbliżenie legitymacji Armii Krajowej Krzysztofa Głuchowskiego z widocznym numerem plutonu 1112 i pseudonimem 'Juras'.",
        "seria": "V",
        "tworca": "AK",
        "jezyk": "polski",
        "kontekst": "Zbliżenie umożliwia odczyt szczegółów: nr plutonu, pseudonim, data.",
        "powiazania": ["ARG/V/3"],
        "stan": "j.w."
    },

    # -- Podseria V/B: Powstanie Warszawskie --
    {
        "sygn": "ARG/V/5",
        "photo": "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p24_img01.jpeg",
        "tytul": "List z Powstania — 'Krychu!'",
        "data": "VIII.1944",
        "typ": "list",
        "opis_fizyczny": "List odręczny na papierze w kratkę, pismo ołówkowe, warunki polowe",
        "opis_tresci": "'Krychu! Krysiey jesteśmy...' — list do Krzysztofa z okresu Powstania Warszawskiego. Pismo ołówkowe, warunki polowe.",
        "seria": "V",
        "tworca": "nieznany (kolega z oddziału?)",
        "jezyk": "polski",
        "kontekst": "List pisany w warunkach walk Powstania. 'Krychu' = zdrobnienie imienia Krzysztof.",
        "powiazania": ["ARG/V/6"],
        "stan": "Średni — papier polowy"
    },
    {
        "sygn": "ARG/V/6",
        "photo": "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p24_img02.jpeg",
        "tytul": "List do rodziców z Powstania — 26.VIII.1944",
        "data": "26.VIII.1944",
        "typ": "list",
        "opis_fizyczny": "List odręczny ołówkiem, 1 karta, papier w kratkę",
        "opis_tresci": "'Warszawa 26-VIII-44, Kochana Maminko i Tatusiu...' — list Krzysztofa Andrzeja do rodziców z Powstania Warszawskiego.",
        "seria": "V",
        "tworca": "Krzysztof Andrzej Głuchowski",
        "jezyk": "polski",
        "kontekst": "DOKUMENT O OGROMNEJ WARTOŚCI. List 18-latka z walczącego miasta do rodziców — 26 dni po wybuchu Powstania. Jeden z najrzadszych typów dokumentów — korespondencja cywilna z oblężonej Warszawy.",
        "powiazania": ["ARG/V/5", "ARG/V/7"],
        "stan": "Średni — ołówek, kruchy papier"
    },
    {
        "sygn": "ARG/V/7",
        "photo": "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p25_img01.jpeg",
        "tytul": "Przepustka Jednorazowa Specjalna AK",
        "data": "29.IX.1944",
        "typ": "przepustka",
        "opis_fizyczny": "Mały dokument z pieczęcią Komendy Okręgu Warszawskiego AK",
        "opis_tresci": "Przepustka Jednorazowa Specjalna Armii Krajowej, Warszawa 29 września 1944. Pieczęć Komendy Okręgu Warszawskiego AK.",
        "seria": "V",
        "tworca": "Komenda Okręgu Warszawskiego AK",
        "jezyk": "polski",
        "kontekst": "29.IX.1944 = DZIEŃ PRZED KAPITULACJĄ (2.X.1944). Przepustka specjalna z ostatnich godzin Powstania — prawdopodobnie związana z ewakuacją lub negocjacjami.",
        "powiazania": ["ARG/V/8"],
        "stan": "Średni"
    },
    {
        "sygn": "ARG/V/8",
        "photo": "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p26_img01.jpeg",
        "tytul": "Rozkaz awansu i odznaczenia KW",
        "data": "29.IX.1944",
        "typ": "rozkaz",
        "opis_fizyczny": "Rozkaz maszynowy z odręcznym podpisem",
        "opis_tresci": "Rozkaz D-cy Grupy 'Północ' nr 24: awans do stopnia starszego ułana i nagrodzony Krzyżem Walecznych po raz I. Datowany 29 września 1944.",
        "seria": "V",
        "tworca": "D-ca Grupy 'Północ' (płk Ziemski)",
        "jezyk": "polski",
        "kontekst": "Rozkaz z OSTATNICH DNI Powstania. Awans polowy i odznaczenie bojowe nadane w warunkach walki.",
        "powiazania": ["ARG/V/7", "ARG/V/41", "ARG/V/42"],
        "stan": "Średni"
    },

    # -- Podseria V/C: Niewola (Stalagi) --
    {
        "sygn": "ARG/V/9",
        "photo": "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p27_img01.jpeg",
        "tytul": "Bilet identyfikacyjny jeńca nr 141009, Stalag XI B",
        "data": "1944–1945",
        "typ": "karta_id",
        "opis_fizyczny": "Mały kartonowy bilet z perforacją, format ok. 8×5 cm, pieczęć 'Stalag XI B'",
        "opis_tresci": "Bilet identyfikacyjny jeńca wojennego: numer 141009, pieczęć 'Stalag XI B' (Fallingbostel). Mały kartonowy bilet z perforacją.",
        "seria": "V",
        "tworca": "Stalag XI B, Fallingbostel",
        "jezyk": "niemiecki",
        "kontekst": "Nr 141009 powtarza się w wielu dokumentach kolekcji — centralny identyfikator Krzysztofa w systemie obozowym.",
        "powiazania": ["ARG/V/10"],
        "stan": "Średni — karton kruchy"
    },
    {
        "sygn": "ARG/V/10",
        "photo": "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p27_img02.jpeg",
        "tytul": "Personalkarte I — karta osobowa jeńca",
        "data": "1944",
        "typ": "formularz",
        "opis_fizyczny": "Formularz A4 dwustronny, druk niemiecki z odręcznymi wpisami, pieczęć",
        "opis_tresci": "Personalkarte I z obozu Stalag XI B. Dane: Głuchowski Krzysztof, Stanisław Stefan (ojciec). Formularz niemieckojęzyczny z danymi personalnymi, adresem rodziny.",
        "seria": "V",
        "tworca": "Stalag XI B",
        "jezyk": "niemiecki",
        "kontekst": "Personalkarte — podstawowy dokument ewidencyjny jeńca. Podaje dane osobowe, ojca, adres rodziny w Częstochowie.",
        "powiazania": ["ARG/V/9", "ARG/III/1"],
        "stan": "Średni"
    },
    {
        "sygn": "ARG/V/11",
        "photo": "Seria_29z_p12_img01.jpeg",
        "tytul": "Karta zdrowia obozowa — rewers (Heilimpfungen)",
        "data": "1944–1945",
        "typ": "formularz",
        "opis_fizyczny": "Formularz medyczny drukowany, format A5, tabele",
        "opis_tresci": "Gesundheitskarte — formularz medyczny jeńca: Art der Krankheit, Schutz- und Heilimpfungen, Gewichtstabelle. Tabela szczepień i wagi.",
        "seria": "V",
        "tworca": "służba medyczna obozu",
        "jezyk": "niemiecki",
        "kontekst": "Karta zdrowia śledziła stan fizyczny jeńca. Tabela wagi pozwala ocenić warunki bytowe.",
        "powiazania": ["ARG/V/12"],
        "stan": "Średni"
    },
    {
        "sygn": "ARG/V/12",
        "photo": "Seria_29z_p12_img02.jpeg",
        "tytul": "Karta zdrowia M.-Stammlager VI J — awers",
        "data": "1944",
        "typ": "formularz",
        "opis_fizyczny": "Awers formularza medycznego z nagłówkiem Stammlager VI J",
        "opis_tresci": "Awers karty zdrowia: M.-Stammlager VI J, Gesundheitskarte. Dane jeńca nieczytelne.",
        "seria": "V",
        "tworca": "Stalag VI J",
        "jezyk": "niemiecki",
        "kontekst": "Karta z INNEGO obozu niż XI B — świadczy o przenoszeniu Krzysztofa między obozami (XI B → VI/3 → VI J).",
        "powiazania": ["ARG/V/11", "ARG/V/9"],
        "stan": "Średni"
    },

    # -- Podseria V/D: Korespondencja obozowa --
    {
        "sygn": "ARG/V/13",
        "photo": "Seria_29z_p03_img02.jpeg",
        "tytul": "List Krzysztofa z obozu — nr 141009",
        "data": "1944–1945",
        "typ": "list",
        "opis_fizyczny": "List odręczny na kartonie, pismo ołówkowe",
        "opis_tresci": "List odręczny na kartonie: wspomina nr 141009 (numer jeniecki Krzysztofa), Stalag XI B. Kończy się słowami 'Trzymamy się do końca!'",
        "seria": "V",
        "tworca": "Krzysztof Andrzej Głuchowski",
        "jezyk": "polski",
        "kontekst": "Przesłanie moralne — 'Trzymamy się do końca!' — typowe dla korespondencji jeńców AK.",
        "powiazania": ["ARG/V/9"],
        "stan": "Średni"
    },
    {
        "sygn": "ARG/V/14",
        "photo": "Seria_29z_p05_img01.jpeg",
        "tytul": "Antwort-Postkarte — Krzysztof ze Stalag VI/3 (awers)",
        "data": "XI.1945",
        "typ": "kartka",
        "opis_fizyczny": "Formularz Antwort-Postkarte z odręcznymi wpisami, stempel cenzury",
        "opis_tresci": "Nadawca: Głuchowski Krzysztof, St.Uł., Stalag VI/3, Dorsten in Westfalen. Adresat: Anna Maria, Główno, Osiny, Łowicz. Stempel cenzury.",
        "seria": "V",
        "tworca": "Krzysztof Andrzej Głuchowski",
        "jezyk": "niemiecki / polski",
        "kontekst": "Stalag VI/3 w Dorsten — kolejny obóz. Karta odpowiedzi (Antwort-Postkarte) umożliwiała odpowiedź na tej samej kartce.",
        "powiazania": ["ARG/V/15"],
        "stan": "Średni"
    },
    {
        "sygn": "ARG/V/15",
        "photo": "Seria_29z_p05_img02.jpeg",
        "tytul": "Antwort-Postkarte — odpowiedź rodziny (rewers)",
        "data": "1945",
        "typ": "kartka",
        "opis_fizyczny": "Rewers kartki z pismem odręcznym kilku osób",
        "opis_tresci": "'Kochany Krzysiu! ...Marus... Twoja Cioteczka Częstochowa... Ławka i jej córeczka...' List od rodziny do jeńca. Podpis Maria.",
        "seria": "V",
        "tworca": "rodzina Głuchowskich (Maria i inne)",
        "jezyk": "polski",
        "kontekst": "Odpowiedź kilku osób na jednej kartce — typowe wobec limitów korespondencji. Sieć rodzinna z Częstochowy.",
        "powiazania": ["ARG/V/14"],
        "stan": "Średni"
    },
    {
        "sygn": "ARG/V/16",
        "photo": "Seria_29z_p06_img01.jpeg",
        "tytul": "List z obozu do stryja generała — 19.X.1944",
        "data": "19.X.1944",
        "typ": "list",
        "opis_fizyczny": "Rewers formularza, pismo ołówkowe",
        "opis_tresci": "'Kochany Stryju i Ciociu! Zostaliśmy obaj w OP...' — list z obozu do stryja (gen. Janusza?), wspomina 2417 km podróży. Podpis Krzysztof.",
        "seria": "V",
        "tworca": "Krzysztof Andrzej Głuchowski",
        "jezyk": "polski",
        "kontekst": "List do stryja-generała w Londynie. '2417 km podróży' = transport z Warszawy do obozu po kapitulacji.",
        "powiazania": ["ARG/V/17"],
        "stan": "Średni"
    },
    {
        "sygn": "ARG/V/17",
        "photo": "Seria_29z_p06_img02.jpeg",
        "tytul": "Kartka z obozu do gen. Janusza w Londynie",
        "data": "X.1944",
        "typ": "kartka",
        "opis_fizyczny": "Kriegsgefangenenpost / Postkarte z adresem londyńskim, stempel 'PASSED XII'",
        "opis_tresci": "Nadawca: St.Uł. Krzysztof Głuchowski, nr 141009, M.-Stammlager XI B. Adresat: GENERAL JANUSZ GŁUCHOWSKI, London, Polish War's Office, ENGLAND. Stempel PASSED XII.",
        "seria": "V",
        "tworca": "Krzysztof Andrzej Głuchowski",
        "jezyk": "niemiecki / angielski / polski",
        "kontekst": "DOKUMENT WYJĄTKOWY — kartka z obozu jenieckiego do generała w Londynie. Trójjęzyczność (niemiecki formularz, angielski adres, polskie pismo). Stempel PASSED = cenzura brytyjska.",
        "powiazania": ["ARG/V/16", "ARG/II/24"],
        "stan": "Dobry — stemple czytelne"
    },
    {
        "sygn": "ARG/V/18",
        "photo": "Seria_29z_p08_img01.jpeg",
        "tytul": "Długi list obozowy — 2 strony",
        "data": "XI.1944",
        "typ": "list",
        "opis_fizyczny": "Rozłożony list dwustronny (Détachez le long du pointillé / Hier abtrennen!), gęste pismo ołówkowe",
        "opis_tresci": "Obie strony gęście zapisane ołówkiem. Szczegółowy opis życia obozowego, rodziny, 17 punktów.",
        "seria": "V",
        "tworca": "Krzysztof Andrzej Głuchowski",
        "jezyk": "polski",
        "kontekst": "Formularz z linią odcinania — typowy dla korespondencji obozowej. 17 punktów = numerowany raport z życia w obozie.",
        "powiazania": ["ARG/V/19"],
        "stan": "Średni"
    },
    {
        "sygn": "ARG/V/19",
        "photo": "Seria_29z_p08_img02.jpeg",
        "tytul": "Koperta Kriegsgefangenenpost — Krzysztof do Stefana",
        "data": "7.XI.1944",
        "typ": "koperta",
        "opis_fizyczny": "Koperta z pieczęcią '27 Geprüft Stalag XI B', stempel 7.11.44",
        "opis_tresci": "Do: Ppor. Stefana Głuchowskiego, nr 01245, Stalag XI B. Nadawca: St.Uł. Krzysztof Głuchowski. Stempel cenzury '27 Geprüft Stalag XI B'.",
        "seria": "V",
        "tworca": "Krzysztof Andrzej Głuchowski",
        "jezyk": "niemiecki / polski",
        "kontekst": "Korespondencja syn→ojciec między obozami. Nr 27 = identyfikator cenzora.",
        "powiazania": ["ARG/III/3", "ARG/V/18"],
        "stan": "Średni"
    },

    # -- Podseria V/E: Notatki i Powstanie z pamięci --
    {
        "sygn": "ARG/V/20",
        "photo": "Seria_29z_p11_img01.jpeg",
        "tytul": "Notatki z Powstania Warszawskiego",
        "data": "VIII–X.1944",
        "typ": "notatka",
        "opis_fizyczny": "Kartka z notatkami, pismo ołówkowe i atrament",
        "opis_tresci": "Fragmenty notatek z Powstania. Wspomina 'Powstanie', obliczenia numeryczne (45, 1.56, 64.18, 92), 'Krzysiek i Gryfon'.",
        "seria": "V",
        "tworca": "Krzysztof Andrzej Głuchowski",
        "jezyk": "polski",
        "kontekst": "'Gryfon' — prawdopodobnie pseudonim kolegi z oddziału. Obliczenia mogą dotyczyć strat, amunicji lub odległości.",
        "powiazania": ["ARG/V/36"],
        "stan": "Średni"
    },
    {
        "sygn": "ARG/V/21",
        "photo": "Seria_29z_p18_img01.jpeg",
        "tytul": "Relacja z Powstania Warszawskiego",
        "data": "1944–1945",
        "typ": "pamietnik",
        "opis_fizyczny": "Gęsto zapisana strona, pismo atramentem i ołówkiem",
        "opis_tresci": "RELACJA Z POWSTANIA — wspomina 'Gestapo przy 41 branka', '508 strat', 'gen. Bora Komorowskiego', '3 VIII.44 zginął', '1112 odznacz', 'Kompanii Saperów'. Konkretne daty i straty.",
        "seria": "V",
        "tworca": "Krzysztof Andrzej Głuchowski",
        "jezyk": "polski",
        "kontekst": "DOKUMENT O OGROMNEJ WARTOŚCI HISTORYCZNEJ. Relacja naocznego świadka z konkretnymi danymi: '508 strat' = straty jednostki, '1112 odznacz' = pluton 1112. Pisana prawdopodobnie w obozie z pamięci.",
        "powiazania": ["ARG/V/20", "ARG/V/8"],
        "stan": "Średni"
    },
    {
        "sygn": "ARG/V/22",
        "photo": "Seria_29z_p15_img02.jpeg",
        "tytul": "Mapka taktyczna z kompasem — Wołomin",
        "data": "1944",
        "typ": "mapa",
        "opis_fizyczny": "Rysunek odręczny z kompasem (N), pismo ołówkowe",
        "opis_tresci": "Notatki i mapka/schemat z kompasem (N), 'na Wołominie' widoczne. Opis terenów walk.",
        "seria": "V",
        "tworca": "Krzysztof Andrzej Głuchowski",
        "jezyk": "polski",
        "kontekst": "Mapka taktyczna pisana z pamięci w obozie. Wołomin — rejon walk na wschód od Warszawy.",
        "powiazania": ["ARG/V/21"],
        "stan": "Średni"
    },

    # -- Podseria V/F: Pamiętnik obozowy --
    {
        "sygn": "ARG/V/23",
        "photo": "Seria_29z_p13_img01.jpeg",
        "tytul": "Pamiętnik obozowy — strona 1",
        "data": "1944–1945",
        "typ": "pamietnik",
        "opis_fizyczny": "Strona zeszytu/luźnej kartki, gęste pismo atramentem i ołówkiem",
        "opis_tresci": "Zeszyt wspomnieniowy z okresu obozowego. Gęście zapisana strona. Wspomina 'Głuchowski', 'Powstanie', 'Krakowie', 'Boże Narodzenie', 'Londyn'.",
        "seria": "V",
        "tworca": "Krzysztof Andrzej Głuchowski",
        "jezyk": "polski",
        "kontekst": "Wspomnienia pisane w obozie — pamiętnik literacki. Kraków i Londyn = punkty odniesienia rodzinne.",
        "powiazania": ["ARG/V/24", "ARG/V/25", "ARG/V/26"],
        "stan": "Średni — papier kruchy"
    },
    {
        "sygn": "ARG/V/24",
        "photo": "Seria_29z_p13_img02.jpeg",
        "tytul": "Pamiętnik obozowy — strona 2",
        "data": "1944–1945",
        "typ": "pamietnik",
        "opis_fizyczny": "Kontynuacja pamiętnika, pismo ołówkowe i atrament",
        "opis_tresci": "'Jestem w Glenboock(?)... nr 141009 — to...' — wspomina numer obozowy.",
        "seria": "V",
        "tworca": "Krzysztof Andrzej Głuchowski",
        "jezyk": "polski",
        "kontekst": "Kontynuacja wspomnień z identyfikacją nr 141009.",
        "powiazania": ["ARG/V/23"],
        "stan": "Średni"
    },
    {
        "sygn": "ARG/V/25",
        "photo": "Seria_29z_p13_img03.jpeg",
        "tytul": "Pamiętnik — wspomnienia z dzieciństwa",
        "data": "1944–1945",
        "typ": "pamietnik",
        "opis_fizyczny": "Strona z atramentem niebieskim, czytelne pismo",
        "opis_tresci": "'Dzieciństwo moje to szczęśliwe...' — wspomnienia autobiograficzne pisane niebieskim atramentem.",
        "seria": "V",
        "tworca": "Krzysztof Andrzej Głuchowski",
        "jezyk": "polski",
        "kontekst": "Rozdziały autobiograficzne — 18-latek wspomina szczęśliwe dzieciństwo w obozie jenieckim. Kontrast traumatyczny.",
        "powiazania": ["ARG/V/23"],
        "stan": "Średni"
    },
    {
        "sygn": "ARG/V/26",
        "photo": "Seria_29z_p13_img04.jpeg",
        "tytul": "Pamiętnik obozowy — strona 4",
        "data": "1944–1945",
        "typ": "pamietnik",
        "opis_fizyczny": "Pożółkły papier, pismo ołówkowe",
        "opis_tresci": "Kolejna strona wspomnień. Ciepła, Halemka(?), daty, wspomnienia rodzinne.",
        "seria": "V",
        "tworca": "Krzysztof Andrzej Głuchowski",
        "jezyk": "polski",
        "kontekst": "Kontynuacja wspomnień autobiograficznych.",
        "powiazania": ["ARG/V/23"],
        "stan": "Średni — pożółkły"
    },
    {
        "sygn": "ARG/V/27",
        "photo": "Seria_29z_p14_img01.jpeg",
        "tytul": "Notatnik na papierze w kratkę — Stalag VI/17",
        "data": "1944–1945",
        "typ": "pamietnik",
        "opis_fizyczny": "Papier w kratkę, drobne gęste pismo",
        "opis_tresci": "Gęsto zapisana strona. 'Stalag VI/17' widoczne w środku. Opis obozów, dat, przerzutów.",
        "seria": "V",
        "tworca": "Krzysztof Andrzej Głuchowski",
        "jezyk": "polski",
        "kontekst": "Kolejny numer obozu — VI/17. Mapa przerzutów Krzysztofa: XI B → VI/3 → VI J → VI/17.",
        "powiazania": ["ARG/V/12"],
        "stan": "Średni"
    },
    {
        "sygn": "ARG/V/28",
        "photo": "Seria_29z_p14_img02.jpeg",
        "tytul": "Wspomnienia 1940 — na papierze w kratkę",
        "data": "1944–1945",
        "typ": "pamietnik",
        "opis_fizyczny": "Papier w kratkę, dwie kolumny tekstu, notatki na marginesach",
        "opis_tresci": "'Pamiętam, jak w roku 1940 uderzył mnie...' — wspomnienia wojenne.",
        "seria": "V",
        "tworca": "Krzysztof Andrzej Głuchowski",
        "jezyk": "polski",
        "kontekst": "Wspomnienia z okupacji pisane w obozie. 1940 = okres wczesnej okupacji, Krzysztof miał 14 lat.",
        "powiazania": ["ARG/V/23"],
        "stan": "Średni"
    },
    {
        "sygn": "ARG/V/29",
        "photo": "Seria_29z_p14_img03.jpeg",
        "tytul": "Notatki na formularzu Kaufmannsgehilfenprüfung",
        "data": "1944–1945",
        "typ": "pamietnik",
        "opis_fizyczny": "Formularz egzaminu kupieckiego Izby Przemysłowo-Handlowej Gladbach-Rheydt-Neuss, odwrotna strona",
        "opis_tresci": "Formularz egzaminu kupieckiego wykorzystany jako papier do notatek. Rysunki geometryczne i zapisy ołówkowe na odwrocie.",
        "seria": "V",
        "tworca": "Krzysztof Andrzej Głuchowski",
        "jezyk": "niemiecki (formularz) / polski (notatki)",
        "kontekst": "Typowy recykling papieru w obozie — jeńcy wykorzystywali każdy skrawek. Formularz z Gladbach-Rheydt-Neuss = rejon Stalagu VI.",
        "powiazania": ["ARG/V/30", "ARG/V/31"],
        "stan": "Średni"
    },
    {
        "sygn": "ARG/V/30",
        "photo": "Seria_29z_p15_img01.jpeg",
        "tytul": "Formularz kupiecki z notatkami i rysunkiem",
        "data": "1944–1945",
        "typ": "pamietnik",
        "opis_fizyczny": "Formularz Kaufmannsgehilfenprüfung, odwrotna strona z rysunkiem",
        "opis_tresci": "Kolejny formularz kupiecki z notatkami na odwrocie. Rysunek geometryczny i drobne pismo ołówkowe.",
        "seria": "V",
        "tworca": "Krzysztof Andrzej Głuchowski",
        "jezyk": "niemiecki / polski",
        "kontekst": "Kolejny formularz kupiecki z Gladbach jako papier obozowy — recykling dokumentów w Stalagu.",
        "powiazania": ["ARG/V/29"],
        "stan": "Średni"
    },
    {
        "sygn": "ARG/V/31",
        "photo": "Seria_29z_p15_img03.jpeg",
        "tytul": "Notatki powojenne — 22.VIII.1945",
        "data": "22.VIII.1945",
        "typ": "pamietnik",
        "opis_fizyczny": "Formularz Kaufmannsgehilfenprüfung z notatkami po wyzwoleniu",
        "opis_tresci": "Notatki datowane 22.VIII.1945 — już PO wyzwoleniu. 'Obecnie jestem już...' Zapis przejścia od niewoli do wolności.",
        "seria": "V",
        "tworca": "Krzysztof Andrzej Głuchowski",
        "jezyk": "polski",
        "kontekst": "Moment przełomowy — z jeńca na wolnego człowieka. Data potwierdza ciągłość pamiętnika.",
        "powiazania": ["ARG/V/29"],
        "stan": "Średni"
    },
    {
        "sygn": "ARG/V/32",
        "photo": "Seria_29z_p16_img01.jpeg",
        "tytul": "Pamiętnik — Bitwy, rok 1934",
        "data": "1944–1945",
        "typ": "pamietnik",
        "opis_fizyczny": "Papier w kratkę, atrament i ołówek",
        "opis_tresci": "'Bitwy i...' — wspomina rok 1934. Notatki na papierze w kratkę.",
        "seria": "V",
        "tworca": "Krzysztof Andrzej Głuchowski",
        "jezyk": "polski",
        "kontekst": "Wspomnienia z dzieciństwa — 1934, Krzysztof miał 8 lat.",
        "powiazania": ["ARG/V/23"],
        "stan": "Średni"
    },
    {
        "sygn": "ARG/V/33",
        "photo": "Seria_29z_p16_img02.jpeg",
        "tytul": "Pamiętnik — Leżność, Stalgów",
        "data": "1944–1945",
        "typ": "pamietnik",
        "opis_fizyczny": "Gęsto zapisana strona, atrament i ołówek",
        "opis_tresci": "Gęsto zapisana strona, wspomina 'Leźność', 'Stalgów', daty.",
        "seria": "V",
        "tworca": "Krzysztof Andrzej Głuchowski",
        "jezyk": "polski",
        "kontekst": "Kontynuacja pamiętnika. Leźność/Stalgów — miejscowości z dzieciństwa lub służby?",
        "powiazania": ["ARG/V/23"],
        "stan": "Średni"
    },
    {
        "sygn": "ARG/V/34",
        "photo": "Seria_29z_p11_img02.jpeg",
        "tytul": "Tabela / rozkład marszowy jednostki",
        "data": "1944–1945",
        "typ": "notatka",
        "opis_fizyczny": "Ręcznie narysowana tabelka na papierze w kratkę",
        "opis_tresci": "'8 DPMK 3 SF Remo 10 Genova 11 Fort 12 Pol 13 Brit.' — rozkład marszowy lub transport jednostki.",
        "seria": "V",
        "tworca": "Krzysztof Andrzej Głuchowski",
        "jezyk": "polski / angielski",
        "kontekst": "Genova, Fort, Pol, Brit — transport z Niemiec przez Włochy. Ślad repatriacji.",
        "powiazania": ["ARG/V/39"],
        "stan": "Średni"
    },

    # -- Podseria V/G: Wyzwolenie i repatriacja --
    {
        "sygn": "ARG/V/35",
        "photo": "Seria_29z_p17_img01.jpeg",
        "tytul": "List powojenny — 6.VII.1945",
        "data": "6.VII.1945",
        "typ": "list",
        "opis_fizyczny": "List odręczny atramentem na białym papierze",
        "opis_tresci": "List datowany 6.7.1945. Wspomina Bogdana, Palestynę, Polskę.",
        "seria": "V",
        "tworca": "Krzysztof Andrzej Głuchowski",
        "jezyk": "polski",
        "kontekst": "Korespondencja powojenna — rozważa dalsze losy: Palestyna? Powrót do Polski?",
        "powiazania": ["ARG/V/36"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/V/36",
        "photo": "Seria_29z_p18_img02.jpeg",
        "tytul": "List z Düsseldorfu po wyzwoleniu — 2.VI.1945",
        "data": "2.VI.1945",
        "typ": "list",
        "opis_fizyczny": "List odręczny atramentem, wielostronicowy",
        "opis_tresci": "'Kochajni Ciociu i Stryju! Jestem obecnie w Düsseldorfie. Oswobodzony z niewoli 24/V przez Amerykanów...' Szczegółowa relacja z Powstania i kampanii. Wspomina V.S.O.P., Bora Komorowskiego, kapitulację 2.X.44.",
        "seria": "V",
        "tworca": "Krzysztof Andrzej Głuchowski",
        "jezyk": "polski",
        "kontekst": "KLUCZOWA RELACJA — pisana 9 dni po wyzwoleniu, do stryja-generała i ciotki. Zawiera szczegółowy opis walk, kapitulacji, transportu do obozu. Wyzwolony 24.V.1945 przez wojska USA.",
        "powiazania": ["ARG/V/21", "ARG/V/37"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/V/37",
        "photo": "Seria_29z_p17_img02.jpeg",
        "tytul": "List na papeterii Emil Schröder & Co — Düsseldorf",
        "data": "23.II.1945",
        "typ": "list",
        "opis_fizyczny": "List odręczny na papierze firmowym niemieckiej fabryki lakierów",
        "opis_tresci": "List po polsku na papierze firmowym fabryki lakierów Emil Schröder & Co G.M.B.H. z Düsseldorfu-Grafenbergu. Wspomina Bogdanę, Polizei, Warszawę.",
        "seria": "V",
        "tworca": "Krzysztof Andrzej Głuchowski",
        "jezyk": "polski",
        "kontekst": "Recykling papeterii niemieckiej — typowe dla Displaced Persons. Fabryka w Grafenbergu mogła być miejscem pracy przymusowej.",
        "powiazania": ["ARG/V/36", "ARG/V/38"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/V/38",
        "photo": "Seria_29z_p19_img01.jpeg",
        "tytul": "Kontynuacja listu — 2.II.1945",
        "data": "2.II.1945",
        "typ": "list",
        "opis_fizyczny": "Kontynuacja listu, podpis Krzysztof",
        "opis_tresci": "Datowany 2.II.1945, podpis Krzysztof. Kontynuacja listu z relacją z doświadczeń obozowych.",
        "seria": "V",
        "tworca": "Krzysztof Andrzej Głuchowski",
        "jezyk": "polski",
        "kontekst": "Kontynuacja korespondencji z okresu obozowego.",
        "powiazania": ["ARG/V/37"],
        "stan": "Średni"
    },
    {
        "sygn": "ARG/V/39",
        "photo": "Seria_29z_p19_img02.jpeg",
        "tytul": "List na papeterii Emil Schröder — 5.VIII.1949",
        "data": "5.VIII.1949",
        "typ": "list",
        "opis_fizyczny": "List na papierze firmowym Emil Schröder & Co",
        "opis_tresci": "Datowany 5.VIII.1949. Korespondencja powojenna. Wspomina Stalag XI B, Babkę, Ludkę.",
        "seria": "V",
        "tworca": "Krzysztof Andrzej Głuchowski",
        "jezyk": "polski",
        "kontekst": "Cztery lata po wyzwoleniu — dalsze kontakty z Niemiec. Używanie tej samej papeterii przez lata.",
        "powiazania": ["ARG/V/37"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/V/40",
        "photo": "Seria_29z_p21_img01.jpeg",
        "tytul": "Card of Identity — wyzwolony jeniec, Düsseldorf 1945",
        "data": "27.IV.1945",
        "typ": "karta_id",
        "opis_fizyczny": "Karta dwujęzyczna (polsko-angielska), format mały, pieczęć aliancka",
        "opis_tresci": "CARD OF IDENTITY / KARTA TOŻSAMOŚCI — dwujęzyczny (angielsko-polski). Strona angielska: 'P.f.c. Głuchowski Krzysztof is a polish soldier liberated by Allied Armies from German captivity and lives at hospital of former prisoners of war in Düsseldorf-Gerresheim. This card is delivered in order to facilitate to American Authority the confirming of identity. Düsseldorf, 25th of April 1945.' Strona polska: 'st.ułan Głuchowski Krzysztof — jest żołnierzem polskim oswobodzonym przez wojska Sprzymierzone z niewoli niemieckiej i jest zakwaterowany w szpitalu byłych jeńców wojennych w Düsseldorf-Gerresheim.' Podpis: pol. chief-doctor in hosp.",
        "seria": "V",
        "tworca": "Siły Alianckie / Polish Forces",
        "jezyk": "angielski / polski",
        "kontekst": "KARTA TOŻSAMOŚCI WYZWOLONEGO JEŃCA — pierwszy dokument wolności Krzysztofa! P.f.c. = Private First Class = st.ułan. Wyzwolony przez ARMIE AMERYKAŃSKIE, zakwaterowany w SZPITALU byłych jeńców w Düsseldorf-Gerresheim. Podpis polskiego lekarza naczelnego szpitala. 25 kwietnia 1945 — 13 dni przed kapitulacją Niemiec (8.V.1945). Chronologia: wyzwolenie Düsseldorf (25.IV.1945) → repatriacja Paryż (27.VI.1945) → PSZ Włochy (14.VII.1945).",
        "powiazania": ["ARG/V/36", "ARG/V/43"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/V/41",
        "photo": "Seria_29z_p24_img01.jpeg",
        "tytul": "Zaświadczenie o konspiracji AK — 3 lata służby",
        "data": "18.II.1945",
        "typ": "zaswiadczenie",
        "opis_fizyczny": "Zaświadczenie z pieczęcią Komendy UZUP",
        "opis_tresci": "ZAŚWIADCZENIE — Głuchowski Krzysztof, 1926, starszy ułan. 'konspirację przez okres 3 lat w Warszawie w dyw. «Jeleń» 7.p.uł.' kryptonim «Jorzycki»(?). Powstanie Warszawskie. Świadkowie: ppor. RADOMYSKI Janusz (1922), ppor. MILCZYŃSKI Stanisław (1918). Data: 27 czerwca 1945. Pieczęć: KOMENDANT I POZYTURY K.U. N°1 z Orłem. Dopisek niebieskim atramentem (18.7.45): 'Stwierdzam że st.ułan Głuchowski Krzysztof służył w Ar. Krajowej w V. muszące, 3 pluton, 3 po muszce. (st 1112)'.",
        "seria": "V",
        "tworca": "Komenda UZUP AK",
        "jezyk": "polski",
        "kontekst": "Potwierdzenie 3-letniej służby konspiracyjnej (1941–1944). Pseudonimy: Jurat/Język — warianty 'Jurasa'.",
        "powiazania": ["ARG/V/3", "ARG/V/42"],
        "stan": "Średni"
    },
    {
        "sygn": "ARG/V/42",
        "photo": "Seria_29z_p35_img01.jpeg",
        "tytul": "Dwa zaświadczenia płk. Klepacza — KW i awans (Sannstedt 1945)",
        "data": "22.VIII.1945",
        "typ": "zaswiadczenie",
        "opis_fizyczny": "Dwa dokumenty na jednym zdjęciu: maszynopisy z podpisami, pieczęciami z orłem polskim, uwierzytelnienia adiutanta. Dopiski odręczne na dole każdego dokumentu.",
        "opis_tresci": "(1) Płk. Klepacz Stanisław zaświadcza nadanie Krzyża Walecznych st.strz. (bat. 1112) Głuchowskiemu Krzysztofowi, rozk. D-twa Art. Nr 29 z 15.9.1944. Uwierzytelnienie podpisu Klepacza z 22.8.1945 przez adiutanta. Dopisek odręczny: 'Uwaga: obyw. Głuchowski Krzysztof (...) AK (...) pod pseudonimem Juras'. (2) Zaświadczenie o awansie do stopnia st. strzelca z 15.9.1944, ten sam format i uwierzytelnienie. Oba z Sannstedt, 22.VIII.1945.",
        "seria": "V",
        "tworca": "Płk. Klepacz Stanisław",
        "jezyk": "polski",
        "kontekst": "Zaświadczenia wydane po wyzwoleniu w Sannstedt (Niemcy, Schleswig-Holstein) potwierdzające odznaczenie KW i awans z Powstania. Płk. Klepacz — dowódca batalionu 1112 w AK. Pseudonim 'Juras' (wariant 'Juraś') potwierdzony w dopisku odręcznym. Dwa identyczne zaświadczenia — jedno na KW, drugie na awans — wystawione tego samego dnia.",
        "powiazania": ["ARG/V/8", "ARG/V/43"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/V/43",
        "photo": "Seria_29z_p36_img01.jpeg",
        "tytul": "Zaświadczenie płk. Ziemskiego — D-ca Grupy 'Północ'",
        "data": "26.X.1946",
        "typ": "zaswiadczenie",
        "opis_fizyczny": "Maszynopis na papierze firmowym Polskiego Okręgu Wojskowego Schleswig-Holstein, pieczęć i podpis",
        "opis_tresci": "ZIEMSKI KAROL, PUŁKOWNIK DYPLOMOWANY, DOWÓDCA POLSKIEGO OKRĘGU WOJSKOWEGO NA TERENIE SCHLESWIG-HOLSTEIN. 'Jako b. Dowódca Grupy «PÓŁNOC» w Powstaniu Warszawskim (Obrona Starego Miasta) stwierdzam, że GŁUCHOWSKI Krzysztof, ur. w dniu 29.11.1928 r. w Warszawie, pseudonim «Juraś», walczący w Obronie Starego Miasta w Plutonie III — Na okazaną waleczność został awansowany do stopnia starszego strzelca oraz odznaczony KRZYŻEM WALECZNYCH po raz pierwszy, co zostało stwierdzone w moim Rozkazie — Dowódcy Grupy «PÓŁNOC» Nr. 24 z dnia 5.9.1944 r.' Wentorf pod Hamburgiem, 26.10.1946. Podpis: B. Dowódca Obrony Starego Miasta w Powstaniu Warszawskim — ZIEMSKI KAROL (WACHNOWSKI), Pułkownik Dyplomowany.",
        "seria": "V",
        "tworca": "Płk. dypl. Karol Ziemski (ps. Wachnowski)",
        "jezyk": "polski",
        "kontekst": "KLUCZOWY DOKUMENT. Płk dypl. Karol Ziemski (ps. 'Wachnowski') — dowódca Grupy 'Północ' i obrony Starego Miasta w Powstaniu Warszawskim (VIII–IX.1944). Po wojnie D-ca Polskiego Okręgu Wojskowego Schleswig-Holstein w Wentorf pod Hamburgiem. Zaświadczenie potwierdza: pseudonim 'Juraś', walka w Plutonie III, awans na st. strzelca, Krzyż Walecznych (Rozkaz Nr 24 z 5.IX.1944). UWAGA: data urodzenia w dokumencie '29.11.1928' — błąd, prawidłowa to 29.XI.1926 (potwierdzona w innych dokumentach: Carte de Rapatrié, Fiche de Transport, świadectwo ukończenia gimnazjum).",
        "powiazania": ["ARG/V/8", "ARG/V/42"],
        "stan": "Dobry"
    },

    # -- Podseria V/H: Repatriacja Francja --
    {
        "sygn": "ARG/V/44",
        "photo": "Seria_29z_p20_img01.jpeg",
        "tytul": "Ulotka repatriacyjna 'Nareszcie... RODACY' (awers)",
        "data": "1945",
        "typ": "ulotka",
        "opis_fizyczny": "Druk dwustronny, format A5, czcionka antykwowa",
        "opis_tresci": "Odezwa do polskich jeńców we Francji: 'Nareszcie... RODACY — Nareszcie nadeszła radosna chwila... powrotu na łono Ojczyzny...' Lista konsulatów i agencji PCK we Francji.",
        "seria": "V",
        "tworca": "Ambasada RP / PCK",
        "jezyk": "polski",
        "kontekst": "Druk repatriacyjny dla Displaced Persons we Francji. Sieć konsulatów i PCK organizowała powroty.",
        "powiazania": ["ARG/V/45"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/V/45",
        "photo": "Seria_29z_p20_img02.jpeg",
        "tytul": "Ulotka repatriacyjna — lista stacji PCK (rewers)",
        "data": "1945",
        "typ": "ulotka",
        "opis_fizyczny": "Rewers ulotki, gęsty druk",
        "opis_tresci": "Lista stacji zbornych PCK, obozów, przedstawicielstw departamentalnych PCK, konsulatów we Francji. 'Punkt Informacyjno-werbunkowy, Paryż 23 rue Surene...'",
        "seria": "V",
        "tworca": "PCK / Ambasada RP",
        "jezyk": "polski",
        "kontekst": "Informator dla DP — mapa instytucji polonijnych we Francji.",
        "powiazania": ["ARG/V/44"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/V/46",
        "photo": "Seria_29z_p23_img01.jpeg",
        "tytul": "Carte de Rapatrié — karta repatrianta (awers)",
        "data": "27.VI.1945",
        "typ": "karta_id",
        "opis_fizyczny": "Karta kartonowa z pieczęcią Centre d'Orsay, format ok. 10×15 cm",
        "opis_tresci": "CARTE DE RAPATRIÉ — République Française, Ministère des Prisonniers, Déportés et Réfugiés. Nr 1492839. Ur. 29.XI.1926, Varsovie (Warszawa), Pologne. Ojciec: STANISŁAW, Matka: WANDA — potwierdza rodziców! Nationalité: Polonaise. Adres kontaktowy: Warszawa. Stempel: 'CENTRE D'ORSAY / 27 JUIN 1945 / GOMS'. Armée Polonaise. TABAC: 30g (racja papierosowa). Karta wydana w Centre d'Orsay w Paryżu — ośrodku repatriacyjnym na Quai d'Orsay.",
        "seria": "V",
        "tworca": "République Française / Centre d'Orsay",
        "jezyk": "francuski",
        "kontekst": "KARTA REPATRIANTA Z ORSAY. Centre d'accueil d'Orsay (obecne Musée d'Orsay) służył jako punkt repatriacji. Nr 1492839 = ten sam co Fiche de Transport.",
        "powiazania": ["ARG/V/47", "ARG/V/40"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/V/47",
        "photo": "Seria_29z_p25_img01.jpeg",
        "tytul": "Fiche de Transport — karta transportowa",
        "data": "VI.1945",
        "typ": "formularz",
        "opis_fizyczny": "Formularz urzędowy République Française, format mały",
        "opis_tresci": "FICHE DE TRANSPORT — Nr 1492839 (ten sam co Carte de Rapatrié). République Française, Ministère des Prisonniers, Déportés et Réfugiés. Nom: GLUHOWSKI, Prénom: Cristophe, Date naissance: 29 XI 1926. Adres: Caserne Bessines. Ocena zdrowotna (Avis Service Santé): D, R. Stempel 27/VI/1945.",
        "seria": "V",
        "tworca": "Ministère des Prisonniers, Déportés et Réfugiés",
        "jezyk": "francuski",
        "kontekst": "Caserne Bessines w Paryżu (St. Ouen) — koszary, w których kwaterowali polscy repatrianci w czerwcu–lipcu 1945. Numer 1492839 identyczny z Carte de Rapatrié (ARG/V/46). Karta umożliwiała darmowy przejazd kolejowy po Francji. Krzysztof przebywał tu razem z ppor. Radomyskim (por. ARG/V/53).",
        "powiazania": ["ARG/V/46"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/V/48",
        "photo": "Seria_29z_p27_img01.jpeg",
        "tytul": "Skierowanie z Ambasady RP w Paryżu na kurs",
        "data": "29.VI.1945",
        "typ": "skierowanie",
        "opis_fizyczny": "Pismo na papierze firmowym Ambasady RP, pieczęć, maszynopis",
        "opis_tresci": "AMBASSADE de POLOGNE à Paris. 'Pan Głuchowski K. zostanie skierowany przez Naczelny Instruktorat Oświatowy na kurs, który rozpocznie się w dniu 15 Lipca b.r. w Villard-de-Lans.' Paryż, dnia 29 czerwca 1945r. Podpis: A. Drogowski, Naczelny Instruktor Oświatowy.",
        "seria": "V",
        "tworca": "Ambasada RP w Paryżu / A. Drogowski, Naczelny Instruktor Oświatowy",
        "jezyk": "polski",
        "kontekst": "Villard-de-Lans — miejscowość w Alpach francuskich (Isère), gdzie Ambasada RP organizowała kursy oświatowe dla polskich żołnierzy i repatriantów. Naczelny Instruktorat Oświatowy przy Ambasadzie RP koordynował kształcenie Polaków we Francji. Głuchowski ostatecznie NIE pojechał do Villard-de-Lans — wstąpił do PSZ we Włoszech (14.VII.1945, dzień przed planowanym rozpoczęciem kursu).",
        "powiazania": ["ARG/V/46"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/V/49",
        "photo": "Seria_29z_p22_img01.jpeg",
        "tytul": "Drobiazgi obozowe — karteczki, wizytówka, talon",
        "data": "1944–1945",
        "typ": "wizytowka",
        "opis_fizyczny": "Trzy drobne przedmioty sfotografowane razem",
        "opis_tresci": "Trzy drobne przedmioty: 1) Karteczka z tekstem: 'Franc. Czerw. Kursy / Cze. repat. / Quai d'Orsay / Solferino' — notatka o repatriacji przez Paryż (Quai d'Orsay = centrum repatriacyjne, Solferino = nazwa ulicy/ośrodka). 2) Mała karta z ręcznie narysowanym ORŁEM POLSKIM, datą '27 19 30%' i symbolami geometrycznymi (koło, kwadrat, trójkąt) — nr G 1118001/9. 3) Karteczka: 'Maj. Jefimkiewicz / Miszr.' — nazwisko majora.",
        "seria": "V",
        "tworca": "różni",
        "jezyk": "włoski / niemiecki",
        "kontekst": "Ephemera obozowa — drobne dokumenty życia codziennego w obozie.",
        "powiazania": [],
        "stan": "Średni"
    },
    {
        "sygn": "ARG/V/50",
        "photo": "Seria_29z_p22_img02.jpeg",
        "tytul": "Spis adresów w Paryżu + wizytówka rzeźbiarza",
        "data": "1945",
        "typ": "wizytowka",
        "opis_fizyczny": "Trzy dokumenty sfotografowane razem: kartka z adresami, wizytówka, kartka z adresem",
        "opis_tresci": "Kartka z adresami (Ambasada RP Paryż, PCK YMCA 23 rue Taitbout, Polska Misja Wojskowa, Konsulat Generalny), wizytówka 'Henri Kołacz, Artiste-Sculpteur, Troyes', kartka z adresem.",
        "seria": "V",
        "tworca": "Krzysztof Andrzej Głuchowski / Henri Kołacz",
        "jezyk": "polski / francuski",
        "kontekst": "Mapa paryskich instytucji polonijnych. Henri Kołacz — polski rzeźbiarz w Troyes, kontakt artystyczny.",
        "powiazania": ["ARG/V/46"],
        "stan": "Średni"
    },
    {
        "sygn": "ARG/V/51",
        "photo": "Seria_29z_p28_img01.jpeg",
        "tytul": "Krótka notatka odręczna",
        "data": "1945",
        "typ": "notatka",
        "opis_fizyczny": "Mała kartka z notatką",
        "opis_tresci": "'Znalazłem plan i drugie...' Krótka notatka personalna.",
        "seria": "V",
        "tworca": "Krzysztof Andrzej Głuchowski",
        "jezyk": "polski",
        "kontekst": "Notatka bieżąca z okresu repatriacji.",
        "powiazania": [],
        "stan": "Średni"
    },
    {
        "sygn": "ARG/V/52",
        "photo": "Seria_29z_p28_img02.jpeg",
        "tytul": "Mapka Marsylii — Rue de Rome, Canebière",
        "data": "1945",
        "typ": "mapa",
        "opis_fizyczny": "Odręczny szkic/mapa na kartce",
        "opis_tresci": "Odręczna mapka: 'Rue de Rome 99', 'Canebière', 'Hotel Sallé'. Plan jak dojść do hotelu/mieszkania w Marsylii.",
        "seria": "V",
        "tworca": "Krzysztof Andrzej Głuchowski",
        "jezyk": "francuski",
        "kontekst": "Canebière — główna ulica Marsylii. Ślad podróży repatriacyjnej Niemcy → Paryż → Marsylia.",
        "powiazania": ["ARG/V/46"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/V/53",
        "photo": "Seria_29z_p26_img01.jpeg",
        "tytul": "List Krzysztofa z Paryża — Caserne Bessines, do bliskich",
        "data": "ok. VI–VII.1945",
        "typ": "list",
        "opis_fizyczny": "List odręczny atramentem niebieskim, 1 karta, pismo dość czytelne, papier kremowy",
        "opis_tresci": "List do rodziny ('Kochani moi Kochany!'). Pisze o ojcu i babce, o wspólnym pobycie, o samochodzie. Prosi o pisanie listów. Podaje swój adres: Caserne Bessines, Paryż, metro Fort de Plaisy, St. Ouen; ppor. Radomyski, komp. 8, sala 71. Podpisany 'Krusio' (familijne zdrobnienie od Krzysztof). Kończy: 'Całuję się mocno i do zobaczenia'.",
        "seria": "V",
        "tworca": "Krzysztof Andrzej Głuchowski",
        "jezyk": "polski",
        "kontekst": "List z okresu repatriacji (VI–VII.1945), kiedy Krzysztof przebywał w Caserne Bessines w Paryżu (St. Ouen). Ppor. Radomyski Janusz (ur. 1922) — towarzysz Krzysztofa, ten sam świadek, który poświadczył jego służbę AK (por. ARG/V/41). 'Krusio' — familijne zdrobnienie imienia Krzysztof. Poprzednia data '3.II.1944' była błędna — treść jednoznacznie wskazuje na okres po wyzwoleniu.",
        "powiazania": [],
        "stan": "Dobry"
    },

    # -- Podseria V/I: PSZ, II Korpus, Gimnazjum 3DSK --
    {
        "sygn": "ARG/V/54",
        "photo": "Seria_29z_p29_img01.jpeg",
        "tytul": "Skierowanie na RENTGEN — 7 Pułk Ułanów Lubelskich / 7 Szpital Wojenny",
        "data": "21.VII.1945",
        "typ": "skierowanie",
        "opis_fizyczny": "Formularz z dwiema pieczęciami: '7 PUŁK UŁANÓW LUBELSKICH im. Gen. K. Sosnkowskiego — LEKARZ' oraz '7 SZPITAL WOJENNY POLISH GEN. HOSP.', pismo odręczne atramentem, papier kremowy pożółkły",
        "opis_tresci": "RENTGEN — skierowanie od Lekarza Pułku. Nagłówek: 7 Pułk Ułanów Lubelskich im. Gen. K. Sosnkowskiego. Laboratorium: Rtg. 1 bat. Art. Przysyłam: H. ułana Głuchowskiego Krzysztofa. Cel: Rtg klatki piersiowej. Rozpoznanie: Susp. g. Plc. pulmonum (podejrzenie zmian w płucach). Pieczęć szpitala 27.7.45. Dopisek: 'Proszę o prześwietlenie płuc'. Podpis: Lekarz Pułku — Cisek, ppor. lek.",
        "seria": "V",
        "tworca": "Lekarz Pułku 7 P.Uł.L. / ppor. lek. Cisek",
        "jezyk": "polski / angielski",
        "kontekst": "7 Pułk Ułanów Lubelskich im. Gen. Kazimierza Sosnkowskiego — pułk, w którym służył Krzysztof po wstąpieniu do PSZ (VII.1945). Skierowanie na RTG płuc wskazuje na problemy zdrowotne po pobycie w obozie jenieckim (Stalag IV-B Mühlberg). 7 Szpital Wojenny (Polish General Hospital) — szpital polskich sił zbrojnych we Włoszech.",
        "powiazania": ["ARG/II/8"],
        "stan": "Średni"
    },
    {
        "sygn": "ARG/V/55",
        "photo": "Seria_29z_p29_img02.jpeg",
        "tytul": "Formularz administracyjny 23.I.1945",
        "data": "23.I.1945",
        "typ": "formularz",
        "opis_fizyczny": "Formularz maszynowy z notatką odręczną, wyblakły",
        "opis_tresci": "Dokument administracyjny, datowany 23.1.45. Wyblakły i trudno czytelny.",
        "seria": "V",
        "tworca": "nieznany",
        "jezyk": "niemiecki (?)",
        "kontekst": "Dokument z okresu obozowego — styczeń 1945, przed wyzwoleniem.",
        "powiazania": [],
        "stan": "Słaby — wyblakły"
    },
    {
        "sygn": "ARG/V/56",
        "photo": "Seria_29z_p30_img01.jpeg",
        "tytul": "Przepustka z II Korpusu — Amandola",
        "data": "1946",
        "typ": "przepustka",
        "opis_fizyczny": "Przepustka dwujęzyczna (polsko-angielska), pieczęć Gimnazjum i Liceum 3 D.K.",
        "opis_tresci": "Nr ewid. 1946, ułan Głuchowski Krzysztof. Kwateruje w m. Amandola, zezwolenie do godz. 21:59. Komendant Gimnazjum i Liceum 3 D.K. Podpis: kpt. Kapica Józef.",
        "seria": "V",
        "tworca": "Komendant Gimnazjum 3 DSK",
        "jezyk": "polski / angielski",
        "kontekst": "Amandola — miasteczko w regionie Marche (Włochy), siedziba Gimnazjum 3 Dywizji Strzelców Karpackich. Żołnierze-uczniowie.",
        "powiazania": ["ARG/V/57", "ARG/V/64"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/V/57",
        "photo": "Seria_29z_p31_img01.jpeg",
        "tytul": "Przepustka z Punktu Przesyłkowego Joncov 2 Korpusu",
        "data": "1946",
        "typ": "przepustka",
        "opis_fizyczny": "Przepustka maszynopisowa, wypełniona czerwonym atramentem, pieczęć okrągła, papier pożółkły",
        "opis_tresci": "Punkt Przesyłkowy Joncov 2 Korpusu. Głuchowski Krzysztof z Obozu P.P.J. ma prawo opuścić rejon obozu i udać się do Pesaro. Przepustka ważna do godz. 13:45. Podpis: Komendant P.P.J. — Kucharski ppor.",
        "seria": "V",
        "tworca": "Baza Personalna 2 Korpusu",
        "jezyk": "polski",
        "kontekst": "II Korpus Polski we Włoszech — po Monte Cassino, przed demobilizacją.",
        "powiazania": ["ARG/V/56"],
        "stan": "Dobry"
    },

    # -- Podseria V/J: Gimnazjum 3DSK --
    {
        "sygn": "ARG/V/58",
        "photo": "Seria_29z_p32_img03.jpeg",
        "tytul": "Okładka EXERCISE BOOK — Gimnazjum 3DSK",
        "data": "1945–1946",
        "typ": "zeszyt",
        "opis_fizyczny": "Okładka zeszytu brytyjskiego: 'EXERCISE BOOK, Code No. 28-31', druk HMSO",
        "opis_tresci": "School: Gimnazjum 3DSK. Name: St.uł. Głuchowski Krzysztof. Subject: Zadania klasowe z języka polskiego. 'Supplied for use in NAVAL & MILITARY SCHOOLS by His Majesty's Stationery Office.'",
        "seria": "V",
        "tworca": "HMSO / Gimnazjum 3DSK",
        "jezyk": "angielski (okładka) / polski (treść)",
        "kontekst": "BRYTYJSKI ZESZYT SZKOLNY POLSKIEGO ŻOŁNIERZA — zeszyt wojskowy Korony Brytyjskiej użyty w polskim gimnazjum we Włoszech. Dokument cywilizacyjny.",
        "powiazania": ["ARG/V/59", "ARG/V/60", "ARG/V/61"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/V/59",
        "photo": "Seria_29z_p32_img01.jpeg",
        "tytul": "Esej szkolny nr 1 — wspomnienie z Powstania (23.VIII.1945)",
        "data": "23.VIII.1945",
        "typ": "esej",
        "opis_fizyczny": "Strona z zeszytu, pismo atramentem",
        "opis_tresci": "Zadanie Klasowe Nr 1, 23.VIII.1945. Trzy tematy do wyboru: 1) Tragiczne widmo (Szekspir/Hamlet), 2) Klawisze, 3) 'Moja najciekawsza przygoda'. Uczeń wybrał temat 3 — napisał autobiograficzny esej o Powstaniu Warszawskim. Wspomina 1.VIII.1944, godzinę W, barykady, oddział AK, pluton 1112, walki fabryczne. Relacja z pierwszej ręki 19-letniego powstańca.",
        "seria": "V",
        "tworca": "Krzysztof Andrzej Głuchowski",
        "jezyk": "polski",
        "kontekst": "ESEJ SZKOLNY Z POWSTANIA — 19-latek pisze o walkach powstańczych jako zadanie szkolne we Włoszech, rok po Powstaniu.",
        "powiazania": ["ARG/V/58"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/V/60",
        "photo": "Seria_29z_p33_img01.jpeg",
        "tytul": "Esej o rocznicy Powstania — 1.VIII.1945, godz. 15:00",
        "data": "1.VIII.1945",
        "typ": "esej",
        "opis_fizyczny": "Esej szkolny, pismo atramentem, nagłówek z datą i godziną",
        "opis_tresci": "Nagłówek: 'St.uł. Krzysztof Głuchowski, Polish Forces C.M.F. 152, Gimnazjum.' Esej na rocznicę Powstania (1.VIII.1945, godz. 15:00 — dokładnie rok po godzinie W). Osobista refleksja: 'Rok temu już od piętnastu minut walczyliśmy...' Wspomina straty Warszawy, obronę Starego Miasta, Czerniaków, Mokotów. Refleksja o duchu powstańczym: 'ludzie widzieli tylko walczące istoty z olbrzymim powstańczym duchem.' Podpisany: K.",
        "seria": "V",
        "tworca": "Krzysztof Andrzej Głuchowski",
        "jezyk": "polski",
        "kontekst": "PISANY DOKŁADNIE ROK PO WYBUCHU POWSTANIA — 1.VIII.1945, godz. 15:00. C.M.F. = Central Mediterranean Forces.",
        "powiazania": ["ARG/V/58", "ARG/V/61"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/V/61",
        "photo": "Seria_29z_p34_img01.jpeg",
        "tytul": "Esej o artykułach wuja — gen. Głuchowskiego (3.VIII.1945)",
        "data": "3.VIII.1945",
        "typ": "esej",
        "opis_fizyczny": "Esej szkolny, pismo atramentem",
        "opis_tresci": "'St.uł. Krzysztof Głuchowski, Polish Forces CMF 152, Gimnazjum 3DSK.' 3.VIII.1945. Temat: 'Lektura'. Esej o czytanych artykułach dotyczących Powstania Warszawskiego — analizuje teksty ludzi, którzy nie byli w Warszawie w czasie walk. Wspomina 'artykuły P. Głuchowskiego' (stryja — gen. Janusza?), dyskusja o AK i Armii Ludowej, planowaniu Powstania. Podpisany: K.",
        "seria": "V",
        "tworca": "Krzysztof Andrzej Głuchowski",
        "jezyk": "polski",
        "kontekst": "AUTOREFERENCYJNY DOKUMENT RODZINNY — uczeń pisze esej o artykułach stryja-generała o Powstaniu, w którym sam walczył.",
        "powiazania": ["ARG/V/58", "ARG/II/27"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/V/62",
        "photo": "Seria_29z_p32_img02.jpeg",
        "tytul": "Zadanie szkolne nr 3 — Wyspiański, 11 Listopada",
        "data": "21.XI.1945",
        "typ": "esej",
        "opis_fizyczny": "Esej szkolny na kilku stronach",
        "opis_tresci": "Tematy: 'Społeczeństwo polskie u progu XX stulecia (Wesele Wyspiańskiego)', 'Upadek nagrobkości w świetle hist.', 'Dzień 11 Listopada w Polsce Odrodzonej'.",
        "seria": "V",
        "tworca": "Krzysztof Andrzej Głuchowski",
        "jezyk": "polski",
        "kontekst": "Eseje maturalne z literatury polskiej — program gimnazjalny kontynuowany na emigracji.",
        "powiazania": ["ARG/V/58"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/V/63",
        "photo": "Seria_29z_p32_img04.jpeg",
        "tytul": "Zadanie szkolne nr 8 — problemy społeczne",
        "data": "IX.1945",
        "typ": "esej",
        "opis_fizyczny": "Esej szkolny",
        "opis_tresci": "Esej nr 8, datowany IX.1945. Tematy: problem społeczny w noweli, upadek moralności.",
        "seria": "V",
        "tworca": "Krzysztof Andrzej Głuchowski",
        "jezyk": "polski",
        "kontekst": "Analiza literacka na poziomie maturalnym.",
        "powiazania": ["ARG/V/58"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/V/64",
        "photo": "Seria_29z_p32_img05.jpeg",
        "tytul": "EXERCISE BOOK — tylna okładka (tabele brytyjskie)",
        "data": "1945–1946",
        "typ": "zeszyt",
        "opis_fizyczny": "Tylna okładka z tabelami przeliczników",
        "opis_tresci": "Tabele przeliczników brytyjskich (Metric Measures, Liquid Measure, Weight, Length, Money, Troy Weight). Druk HMSO.",
        "seria": "V",
        "tworca": "HMSO",
        "jezyk": "angielski",
        "kontekst": "Brytyjski system miar — codzienność polskich żołnierzy w strukturach Korony.",
        "powiazania": ["ARG/V/58"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/V/65",
        "photo": "Seria_29z_p37_img01.jpeg",
        "tytul": "Świadectwo Ukończenia Gimnazjum — matura 1946",
        "data": "7.I.1946",
        "typ": "dyplom",
        "opis_fizyczny": "Świadectwo na papierze urzędowym MWRiOP, ze zdjęciem legitymacyjnym w mundurze",
        "opis_tresci": "ŚWIADECTWO UKOŃCZENIA GIMNAZJUM OGÓLNOKSZTAŁCĄCEGO Nr 13. MWRiOP. Krzysztof Andrzej Głuchowski, ur. 29.XI.1926 w Warszawie. Złożył egzamin maturalny 9 Lutego 1946. Zdjęcie w mundurze.",
        "seria": "V",
        "tworca": "MWRiOP / Delegat V.R. i O.P.",
        "jezyk": "polski",
        "kontekst": "MATURA POLSKIEGO ŻOŁNIERZA WE WŁOSZECH. Ministerstwo Wyznań Religijnych i Oświecenia Publicznego kontynuowało system edukacji na emigracji. Matura w mundurze, w 20. roku życia, po Powstaniu i obozach.",
        "powiazania": ["ARG/V/58", "ARG/V/56"],
        "stan": "Dobry"
    },

    # -- Podseria V/K: Odznaki i legitymacje pułkowe --
    {
        "sygn": "ARG/V/66",
        "photo": "Kolekcja_Gluchowski_Katalog_Tematyczny_p15_img01.jpeg",
        "tytul": "Legitymacja odznaki 3 Dywizji Strzelców Karpackich",
        "data": "1945–1946",
        "typ": "leg",
        "opis_fizyczny": "Legitymacja mała z pieczęcią 3 DSK, nr 21488",
        "opis_tresci": "Legitymacja nr 21488 — St.uł. Głuchowski upoważniony do posiadania Pamiątkowej Odznaki 3 DSK. Pieczęć: Tobruk, Cassino, D-ca 3 DSK.",
        "seria": "V",
        "tworca": "D-ca 3 DSK",
        "jezyk": "polski",
        "kontekst": "3 Dywizja Strzelców Karpackich — legendarna jednostka: Tobruk, Monte Cassino. Krzysztof nie walczył z nią, ale służył w jej strukturach po wyzwoleniu.",
        "powiazania": ["ARG/V/56"],
        "stan": "Dobry"
    },

    # -- Podseria V/L: Korespondencja (aerogramy, listy) --
    {
        "sygn": "ARG/V/67",
        "photo": "juras_001_page2.png",
        "tytul": "Aerogram do Głuchowskiego — CMF 3 DSK, Włochy",
        "data": "1945–1946",
        "typ": "aerogram",
        "opis_fizyczny": "Aerogram (Air Mail Letter Card), format standardowy, stempel pocztowy NZ, druk dwustronny z odręcznym listem na odwrocie",
        "opis_tresci": "Aerogram zaadresowany do Głuchowskiego, CMF 3 DSK, Włochy. Na odwrocie ręczny list po polsku. Stempel pocztowy z Nowej Zelandii — korespondencja z diasporą polską.",
        "seria": "V",
        "tworca": "nadawca z Nowej Zelandii",
        "jezyk": "polski",
        "kontekst": "CMF = Central Mediterranean Forces. Korespondencja z diasporą polską — Polacy osiedleni w Nowej Zelandii (obozy uchodźcze w Pahiatua).",
        "powiazania": ["ARG/V/68"],
        "stan": "Średni — pożółkły"
    },
    {
        "sygn": "ARG/V/68",
        "photo": "juras_002_page3.png",
        "tytul": "List ręczny z Bahia/Salvador, Brazylia — korespondencja rodzinna",
        "data": "lata 50. XX w.",
        "typ": "list",
        "opis_fizyczny": "List ręczny na papierze, gęste pismo, kilka stron",
        "opis_tresci": "List ręczny po polsku z Bahia/Salvador w Brazylii. Korespondencja rodzinna — opis życia emigranckiego w Ameryce Południowej.",
        "seria": "V",
        "tworca": "krewny / znajomy z Brazylii",
        "jezyk": "polski",
        "kontekst": "Ślad diaspory polskiej w Brazylii — bahijska Polonia. Krzysztof wyemigrował do Brazylii, ten list mógł być od niego lub do niego.",
        "powiazania": ["ARG/V/67", "ARG/V/153"],
        "stan": "Średni"
    },

    # -- Podseria V/M: Dokumenty wojskowe i ewidencyjne --
    {
        "sygn": "ARG/V/69",
        "photo": "juras_003_page4.png",
        "tytul": "Arkusz ewidencyjny wojskowy — Oficer Rezerwy",
        "data": "1945–1946",
        "typ": "formularz",
        "opis_fizyczny": "Arkusz na papierze w kratki, wypełniony ręcznie atramentem, tabele z datami i stopniami",
        "opis_tresci": "Arkusz ewidencyjny wojskowy (Oficer Rezerwy) z chronologią służby, stopniami, przydziałami. Wypełniony odręcznie z datami mobilizacji, przydziałów jednostkowych.",
        "seria": "V",
        "tworca": "Krzysztof Andrzej Głuchowski / kancelaria wojskowa",
        "jezyk": "polski",
        "kontekst": "Dokument ewidencyjny — kluczowy dla rekonstrukcji przebiegu służby Krzysztofa w AK i PSZ.",
        "powiazania": ["ARG/V/70", "ARG/V/91"],
        "stan": "Średni — papier w kratki, pożółkły"
    },
    {
        "sygn": "ARG/V/70",
        "photo": "juras_004_page5.png",
        "tytul": "Przepustka wojskowa (PASS) — D-wo 3 DSK, 14.II.1946",
        "data": "14.II.1946",
        "typ": "przepustka",
        "opis_fizyczny": "Przepustka dwujęzyczna PL/EN, format mały, pieczęć D-wa 3 DSK",
        "opis_tresci": "Przepustka wojskowa (PASS) wystawiona przez Dowództwo 3 Dywizji Strzelców Karpackich, data 14 lutego 1946. Formularz dwujęzyczny polsko-angielski.",
        "seria": "V",
        "tworca": "D-wo 3 DSK",
        "jezyk": "polski, angielski",
        "kontekst": "Przepustka z okresu służby w strukturach 3 DSK we Włoszech, po zakończeniu działań wojennych.",
        "powiazania": ["ARG/V/66", "ARG/V/69"],
        "stan": "Dobry"
    },

    # -- Podseria V/N: Świadectwa szkolne (Gimnazjum i Liceum 3 DSK) --
    {
        "sygn": "ARG/V/71",
        "photo": "juras_005_page6.png",
        "tytul": "Świadectwo Gimnazjum i Liceum 3 DSK — formularz z pieczęcią kpt. Kapicy",
        "data": "1946",
        "typ": "swiadectwo",
        "opis_fizyczny": "Formularz urzędowy z pieczęcią Komendanta, podpis kpt. Kapica",
        "opis_tresci": "Świadectwo wydane przez Komendanta Gimnazjum i Liceum 3 DSK. Formularz urzędowy z pieczęcią i podpisem kapitana Kapicy.",
        "seria": "V",
        "tworca": "Gimnazjum i Liceum 3 DSK",
        "jezyk": "polski",
        "kontekst": "Szkolnictwo polskie przy 3 DSK we Włoszech — kontynuacja edukacji żołnierzy-uczniów po zakończeniu działań wojennych.",
        "powiazania": ["ARG/V/72", "ARG/V/73", "ARG/V/65"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/V/72",
        "photo": "juras_006_page7.png",
        "tytul": "Świadectwo Liceum Ogólnokształcącego — strona z ocenami (1946)",
        "data": "1946",
        "typ": "swiadectwo",
        "opis_fizyczny": "Formularz szkolny z ocenami wpisanymi atramentem",
        "opis_tresci": "Świadectwo Liceum Ogólnokształcącego, strona 1 z wykazem ocen: bardzo dobry, dobry, dostateczny. Rok szkolny 1946.",
        "seria": "V",
        "tworca": "Liceum Ogólnokształcące przy 3 DSK",
        "jezyk": "polski",
        "kontekst": "Wykaz ocen maturalnych — program gimnazjalny realizowany w warunkach obozowych we Włoszech.",
        "powiazania": ["ARG/V/71", "ARG/V/73"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/V/73",
        "photo": "juras_007_page8.png",
        "tytul": "Świadectwo Liceum — verso z pieczęcią, Homeracle-Italia, VI.1946",
        "data": "VI.1946",
        "typ": "swiadectwo",
        "opis_fizyczny": "Verso świadectwa z pieczęcią okrągłą i podpisami",
        "opis_tresci": "Odwrotna strona świadectwa licealnego z pieczęcią urzędową i podpisami komisji. Lokalizacja: Homeracle, Włochy, czerwiec 1946.",
        "seria": "V",
        "tworca": "Liceum Ogólnokształcące przy 3 DSK",
        "jezyk": "polski",
        "kontekst": "Homeracle — miejscowość we Włoszech, siedziba szkolnictwa polskiego przy 3 DSK.",
        "powiazania": ["ARG/V/71", "ARG/V/72"],
        "stan": "Dobry"
    },

    # -- Podseria V/O: Życie obozowe --
    {
        "sygn": "ARG/V/74",
        "photo": "juras_008_page9.png",
        "tytul": "Obóz Lammie — Wiadomości Tygodniowe (druk obozowy)",
        "data": "1946–1947",
        "typ": "druk",
        "opis_fizyczny": "Druk obozowy, gazetka informacyjna, format A5",
        "opis_tresci": "Gazetka obozowa 'Wiadomości Tygodniowe' obozu Lammie. Treść: program kina Odeon, rewia Lammie, cyrk Lammie, rozkład komunikacji autobusowej. Życie kulturalne i codzienne obozu.",
        "seria": "V",
        "tworca": "redakcja obozowa Lammie",
        "jezyk": "polski",
        "kontekst": "Obóz Lammie — prawdopodobnie obóz dla żołnierzy polskich we Włoszech lub Wielkiej Brytanii, oczekujących na repatriację lub osiedlenie.",
        "powiazania": ["ARG/V/75"],
        "stan": "Średni — druk obozowy, papier niskiej jakości"
    },
    {
        "sygn": "ARG/V/75",
        "photo": "juras_009_page10.png",
        "tytul": "Mapa obozu Lammie z legendą",
        "data": "1946–1947",
        "typ": "mapa",
        "opis_fizyczny": "Szkic / mapka obozu z legendą, druk lub odbitka",
        "opis_tresci": "Plan obozu Lammie z zaznaczonymi obiektami: Synagoga, Plac Kościelny, Basen, Poczta Polowa, Kaplica Obozowa. Legenda z numerami obiektów.",
        "seria": "V",
        "tworca": "komenda obozu Lammie",
        "jezyk": "polski",
        "kontekst": "Unikatowy plan obozu — dokumentacja topograficzna życia obozowego polskich żołnierzy. Obecność synagogi wskazuje na obóz wielowyznaniowy lub przebudowany z obozu DP.",
        "powiazania": ["ARG/V/74"],
        "stan": "Średni"
    },

    # -- Podseria V/P: Korespondencja osobista --
    {
        "sygn": "ARG/V/76",
        "photo": "juras_010_page11.png",
        "tytul": "List do matki — Wigilia 24.XII.1946, str. 1",
        "data": "24.XII.1946",
        "typ": "list",
        "opis_fizyczny": "List ręczny atramentem, gęste pismo, papier listowy",
        "opis_tresci": "'Kochana moja Matenko!' — list wigilijny do matki, datowany 24 grudnia 1946. Początek listu, opis Wigilii na emigracji.",
        "seria": "V",
        "tworca": "Krzysztof Andrzej Głuchowski",
        "jezyk": "polski",
        "kontekst": "Wigilia 1946 — druga po wojnie. Krzysztof w obozie/jednostce we Włoszech lub Anglii, pisze do matki w Polsce. Dokument intymny, emocjonalny.",
        "powiazania": ["ARG/V/77", "ARG/V/78", "ARG/V/79"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/V/77",
        "photo": "juras_011_page12.png",
        "tytul": "List do matki — Wigilia 24.XII.1946, str. 2",
        "data": "24.XII.1946",
        "typ": "list",
        "opis_fizyczny": "Kontynuacja listu, gęsty tekst ręczny",
        "opis_tresci": "Kontynuacja listu wigilijnego do matki. Gęste pismo, opis codzienności, tęsknoty, pytania o rodzinę.",
        "seria": "V",
        "tworca": "Krzysztof Andrzej Głuchowski",
        "jezyk": "polski",
        "kontekst": "Druga strona listu wigilijnego 1946 — kontynuacja tęsknoty emigranta za rodziną w Polsce.",
        "powiazania": ["ARG/V/76", "ARG/V/78", "ARG/V/79"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/V/78",
        "photo": "juras_012_page13.png",
        "tytul": "List do matki — Wigilia 24.XII.1946, str. 3 (wspomnienia z 1945)",
        "data": "24.XII.1946",
        "typ": "list",
        "opis_fizyczny": "Kolejna strona listu, pismo atramentem",
        "opis_tresci": "Trzecia strona listu wigilijnego. Wspomnienia z 1945 roku, Polska, Boże Narodzenie — porównanie świąt w kraju i na emigracji.",
        "seria": "V",
        "tworca": "Krzysztof Andrzej Głuchowski",
        "jezyk": "polski",
        "kontekst": "Retrospekcja — rok wcześniej (1945) Krzysztof był jeszcze blisko Polski, teraz daleko. Emocjonalny kontrast.",
        "powiazania": ["ARG/V/76", "ARG/V/77", "ARG/V/79"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/V/79",
        "photo": "juras_013_page14.png",
        "tytul": "List do matki — Wigilia 24.XII.1946, str. 4 (sytuacja emigrantów)",
        "data": "24.XII.1946",
        "typ": "list",
        "opis_fizyczny": "Ostatnia strona listu wigilijnego",
        "opis_tresci": "Czwarta strona listu. Odniesienia do sytuacji politycznej, dywizji (HOŁ?), kondycji emigrantów polskich. Ton refleksyjny.",
        "seria": "V",
        "tworca": "Krzysztof Andrzej Głuchowski",
        "jezyk": "polski",
        "kontekst": "Refleksja 20-latka nad losem emigranta — nie wie jeszcze, że do Polski nie wróci. Kontekst polityczny: powojenna sytuacja Polaków za granicą.",
        "powiazania": ["ARG/V/76", "ARG/V/77", "ARG/V/78"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/V/80",
        "photo": "juras_014_page15.png",
        "tytul": "Rysunek techniczny — diagram geometryczny (zadanie szkolne)",
        "data": "1945–1946",
        "typ": "rysunek",
        "opis_fizyczny": "Szkic techniczny ołówkiem na papierze, diagram geometryczny z opisami",
        "opis_tresci": "Rysunek techniczny — diagram geometryczny z opisami i wymiarami. Prawdopodobnie zadanie z rysunku technicznego w ramach programu Gimnazjum/Liceum 3 DSK.",
        "seria": "V",
        "tworca": "Krzysztof Andrzej Głuchowski",
        "jezyk": "polski",
        "kontekst": "Rysunek techniczny jako element edukacji — program szkolny obejmował przedmioty praktyczne obok ogólnokształcących.",
        "powiazania": ["ARG/V/71", "ARG/V/65"],
        "stan": "Dobry"
    },

    # -- Podseria V/Q: Przepustki i dokumenty brytyjskie --
    {
        "sygn": "ARG/V/81",
        "photo": "juras_015_page16.png",
        "tytul": "Przepustka Army Form B.295 — L/Cpl Głuchowski, 7 Pułk Ułanów Lubelskich",
        "data": "1946–1948",
        "typ": "przepustka",
        "opis_fizyczny": "Formularz brytyjski Army Form B.295, pieczęć 7 Pułk Ułanów Lubelskich",
        "opis_tresci": "Przepustka brytyjska (PASS) Army Form B.295 wystawiona na L/Cpl Głuchowski. Pieczęć 7 Pułku Ułanów Lubelskich. Stopień Lance Corporal = st. ułan.",
        "seria": "V",
        "tworca": "British Army / 7 P.Uł. Lubelskich",
        "jezyk": "angielski",
        "kontekst": "Po przejściu do PKPR Krzysztof służył w strukturach brytyjskich. Army Form B.295 = standardowy formularz przepustkowy British Army.",
        "powiazania": ["ARG/V/82", "ARG/V/128"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/V/82",
        "photo": "juras_016_page17.png",
        "tytul": "Instrukcja medyczna British Army — postępowanie w razie choroby na przepustce",
        "data": "1946–1948",
        "typ": "druk regulaminowy",
        "opis_fizyczny": "Druk British Army, format mały (ok. 10×15 cm), papier pergaminowy/cienki. Tekst drukowany dwustronny w języku angielskim. Pismo drobne, gęste. Papier pożółkły, ślady składania.",
        "opis_tresci": "'Instructions to a soldier, or member other than Officer of the A.T.S. if he/she is taken ill or requires urgent medical or dental treatment while on leave.' Cztery punkty instrukcji: (1) Zgłosić się do najbliższego Military Medical Establishment, (2) Pokazać leave pass, (3) Wezwać civilian practitioner jeśli nie można podróżować, (4) Uzyskać Certificate od lekarza. Sekcja 'To the Civilian Practitioner' — instrukcja dla lekarza cywilnego: (a) gdy żołnierz jest chory — odesłać do jednostki, (b) jeśli niezdolny do podróży — wystawić Certificate. Odniesienie do Form O.1107 i National Health Insurance Act (Dental Benefit Regulations).",
        "seria": "V",
        "tworca": "British Army",
        "jezyk": "angielski",
        "kontekst": "Materiał informacyjny — codzienność żołnierza polskiego w strukturach brytyjskich.",
        "powiazania": ["ARG/V/81"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/V/83",
        "photo": "juras_017_page18.png",
        "tytul": "Kartka świąteczna PL/EN — Bodney Airfield, Thetford, Norfolk",
        "data": "XII.1947",
        "typ": "druk",
        "opis_fizyczny": "Kartka świąteczna bilingualna PL/EN, druk z adresem",
        "opis_tresci": "'Wesołych Świąt Bożego Narodzenia' — kartka świąteczna dwujęzyczna z adresem: 35 Bodney Airfield North, Thetford, Norfolk. Boże Narodzenie na angielskiej prowincji.",
        "seria": "V",
        "tworca": "Krzysztof Andrzej Głuchowski / jednostka",
        "jezyk": "polski, angielski",
        "kontekst": "Bodney Airfield — dawna baza RAF w Norfolk, po wojnie obóz dla polskich żołnierzy PKPR. Świąteczna tradycja podtrzymywana na emigracji.",
        "powiazania": ["ARG/V/84", "ARG/V/87"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/V/84",
        "photo": "juras_018_page19.png",
        "tytul": "Kartka świąteczna — verso (ornament choinkowy)",
        "data": "XII.1947",
        "typ": "druk",
        "opis_fizyczny": "Verso kartki świątecznej z ornamentem graficznym",
        "opis_tresci": "Odwrotna strona kartki świątecznej — ornament choinkowy, grafika dekoracyjna.",
        "seria": "V",
        "tworca": "Krzysztof Andrzej Głuchowski / jednostka",
        "jezyk": "—",
        "kontekst": "Verso kartki świątecznej z Bodney Airfield — ornament choinkowy, tradycja emigracyjna.",
        "powiazania": ["ARG/V/83"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/V/85",
        "photo": "juras_019_page20.png",
        "tytul": "Notatka z obliczeniami finansowymi",
        "data": "lata 40.–50. XX w.",
        "typ": "notatka",
        "opis_fizyczny": "Kartka z odręcznymi obliczeniami, liczby w kolumnach",
        "opis_tresci": "Notatka z liczbami i obliczeniami: 350, 70, 1400, 900, 1500, 19200. Kalkulacje finansowe — prawdopodobnie przeliczniki walutowe lub budżet osobisty emigranta.",
        "seria": "V",
        "tworca": "Krzysztof Andrzej Głuchowski",
        "jezyk": "polski",
        "kontekst": "Kalkulacje finansowe emigranta — przeliczniki funtów, lir, cruzeiros? Codzienność materialna żołnierza-emigranta.",
        "powiazania": [],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/V/86",
        "photo": "juras_020_page21.png",
        "tytul": "Wizytówka H. London POLACCO — Bari, Włochy",
        "data": "1945–1946",
        "typ": "wizytowka",
        "opis_fizyczny": "Wizytówka drukowana, format standardowy",
        "opis_tresci": "Wizytówka: 'H. London POLACCO' z adresem: Bari, Teatro, Andrea da Bari #105. Kontakt z Polonią we Włoszech.",
        "seria": "V",
        "tworca": "H. London",
        "jezyk": "włoski",
        "kontekst": "Bari — ważne miasto dla polskich żołnierzy 2 Korpusu we Włoszech. 'POLACCO' = Polak/polski po włosku.",
        "powiazania": [],
        "stan": "Dobry"
    },

    # -- Podseria V/R: Świadectwa i dyplomy (Anglia) --
    {
        "sygn": "ARG/V/87",
        "photo": "juras_021_page22.png",
        "tytul": "Świadectwo I Polskiego Liceum im. 3 DSK — Bodney/Norfolk, klasa 3a/37",
        "data": "1947",
        "typ": "swiadectwo",
        "opis_fizyczny": "Formularz szkolny z danymi ucznia, druk urzędowy",
        "opis_tresci": "Świadectwo I Polskiego Liceum im. 3 Dywizji Strzelców Karpackich, Bodney/Norfolk. Uczeń: Głuchowski Krzysztof, rocznik 1944 Warszawa, klasa 3a/37.",
        "seria": "V",
        "tworca": "I Polskie Liceum im. 3 DSK",
        "jezyk": "polski",
        "kontekst": "Kontynuacja nauki w Anglii — po przeniesieniu z Włoch. Bodney Airfield przerobiony na obóz szkolny dla polskiej młodzieży.",
        "powiazania": ["ARG/V/88", "ARG/V/71"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/V/88",
        "photo": "juras_022_page23.png",
        "tytul": "Świadectwo Liceum Bodney — verso z pieczęcią (30.VI.1946)",
        "data": "30.VI.1946",
        "typ": "swiadectwo",
        "opis_fizyczny": "Verso świadectwa z pieczęcią i podpisami",
        "opis_tresci": "Odwrotna strona świadectwa — pieczęć Dyrektor-Przełożona, adnotacja: promowany do klasy następnej, data 30 czerwca 1946.",
        "seria": "V",
        "tworca": "I Polskie Liceum im. 3 DSK",
        "jezyk": "polski",
        "kontekst": "Promocja do następnej klasy — kontynuacja ścieżki edukacyjnej.",
        "powiazania": ["ARG/V/87"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/V/89",
        "photo": "juras_023_page24.png",
        "tytul": "Przepustka Polish School Master — Gimnazjum i Liceum BOSK, nr 3024427",
        "data": "1.VI.1947 – 4.V.1947",
        "typ": "przepustka",
        "opis_fizyczny": "Przepustka szkolna z numerem, format mały",
        "opis_tresci": "Przepustka nr 3024427 wystawiona przez Polish School Master, Gimnazjum i Liceum BOSK. Na nazwisko Głuchowski K., daty 1.6.47 – 4.5.47.",
        "seria": "V",
        "tworca": "Gimnazjum i Liceum BOSK",
        "jezyk": "angielski, polski",
        "kontekst": "BOSK = Baza Organizacyjna Szkolnictwa Krajowego (?) — szkolnictwo polskie w Wielkiej Brytanii pod kuratelą wojskową.",
        "powiazania": ["ARG/V/87"],
        "stan": "Dobry"
    },

    # -- Podseria V/S: PKPR (Polski Korpus Przysposobienia i Rozmieszczenia) --
    {
        "sygn": "ARG/V/90",
        "photo": "juras_024_page25.png",
        "tytul": "Informacja o Polskim Korpusie Przysposobienia i Rozmieszczenia — druk informacyjny",
        "data": "1946",
        "typ": "ulotka",
        "opis_fizyczny": "Druk informacyjny wielostronicowy, tekst maszynowy",
        "opis_tresci": "Druk informacyjny o Polish Resettlement Corps (PKPR) — stawki żołdu, warunki służby, prawa i obowiązki, procedura przejścia z PSZ do PKPR.",
        "seria": "V",
        "tworca": "War Office / PKPR",
        "jezyk": "angielski, polski",
        "kontekst": "PKPR utworzony 1946 — umożliwiał polskim żołnierzom pozostanie w Wielkiej Brytanii z zachowaniem statusu wojskowego podczas cywilnej readaptacji.",
        "powiazania": ["ARG/V/91", "ARG/V/103"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/V/91",
        "photo": "juras_025_page26.png",
        "tytul": "Odpis umowy służby w wojsku stałym — nr 3004271, Głuchowski Krzysztof",
        "data": "4.VI.1945",
        "typ": "formularz",
        "opis_fizyczny": "Formularz urzędowy z danymi osobowymi, druk maszynowy",
        "opis_tresci": "Autentyczny odpis umowy służby w wojsku stałym nr 3004271. Głuchowski Krzysztof, ur. 29.XI.1926, Polska/Warszawa. Wcielony 4.VI.1945, stopień Private.",
        "seria": "V",
        "tworca": "PSZ / kancelaria wojskowa",
        "jezyk": "angielski, polski",
        "kontekst": "Data wcielenia 4.VI.1945 — miesiąc po kapitulacji Niemiec. Krzysztof przeszedł z AK do PSZ na Zachodzie po ewakuacji z obozów jenieckich.",
        "powiazania": ["ARG/V/69", "ARG/V/103"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/V/92",
        "photo": "juras_026_page27.png",
        "tytul": "Wyciąg z rozkazu likwidacyjnego — Orsay/Courtine, 25.XI.1946",
        "data": "25.XI.1946",
        "typ": "rozkaz",
        "opis_fizyczny": "Wyciąg z rozkazu, druk maszynowy na papierze urzędowym",
        "opis_tresci": "Wyciąg z rozkazu likwidacyjnego obozu Orsay/Courtine z 25 listopada 1946. Dotyczy: Głuchowski Krzysztof-Andrzej, rocznik 1926. Ewidencja obozowa.",
        "seria": "V",
        "tworca": "Polska Wojskowa Misja Likwidacyjna we Francji",
        "jezyk": "polski",
        "kontekst": "Orsay i Courtine — obozy polskie we Francji w trakcie likwidacji 1946. Krzysztof przeszedł przez Francję w drodze do Anglii.",
        "powiazania": ["ARG/V/93"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/V/93",
        "photo": "juras_027_page28.png",
        "tytul": "Pismo Polskiej Wojskowej Misji Likwidacyjnej — Paryż, 22.XI.1946",
        "data": "22.XI.1946",
        "typ": "pismo",
        "opis_fizyczny": "Pismo urzędowe maszynopisem, nagłówek Misji Likwidacyjnej",
        "opis_tresci": "Pismo Polskiej Wojskowej Misji Likwidacyjnej we Francji, Paryż 22 listopada 1946. Adresat: Gen. Ferecki, Sztab Ósmy, Londyn. Dotyczy wysłania Głuchowskiego do obozu.",
        "seria": "V",
        "tworca": "Polska Wojskowa Misja Likwidacyjna we Francji",
        "jezyk": "polski",
        "kontekst": "Korespondencja urzędowa Misji Likwidacyjnej z Londynem — logistyka przerzutu żołnierzy polskich z Francji do Anglii.",
        "powiazania": ["ARG/V/92"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/V/94",
        "photo": "juras_028_page29.png",
        "tytul": "Kwestionariusz Osobisty (POUFNE) — str. 1",
        "data": "1946–1947",
        "typ": "kwestionariusz",
        "opis_fizyczny": "Formularz POUFNE, druk z odręcznymi wpisami",
        "opis_tresci": "Kwestionariusz Osobisty (klauzula POUFNE) — formularz z danymi osobowymi: stopień, formacja, przebieg służby. Wypełniony dla celów 'Polish Records'.",
        "seria": "V",
        "tworca": "Krzysztof Andrzej Głuchowski / kancelaria PKPR",
        "jezyk": "polski, angielski",
        "kontekst": "Kwestionariusz ewidencyjny PKPR — kluczowy dokument do rekonstrukcji biografii wojskowej. Klauzula POUFNE wskazuje na charakter wywiadowczy lub weryfikacyjny.",
        "powiazania": ["ARG/V/95"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/V/95",
        "photo": "juras_029_page30.png",
        "tytul": "Kwestionariusz Osobisty — str. 2 (rodzina, przyszłość)",
        "data": "1946–1947",
        "typ": "kwestionariusz",
        "opis_fizyczny": "Druga strona kwestionariusza",
        "opis_tresci": "Druga strona kwestionariusza: dane o rodzinie, plany na przyszłość, historia podróży. Odpowiedzi odręczne Krzysztofa.",
        "seria": "V",
        "tworca": "Krzysztof Andrzej Głuchowski",
        "jezyk": "polski, angielski",
        "kontekst": "Pytania o przyszłość — dokument czasu decyzji: wrócić do Polski komunistycznej czy zostać na emigracji?",
        "powiazania": ["ARG/V/94"],
        "stan": "Dobry"
    },

    # -- Podseria V/T: Weryfikacja AK --
    {
        "sygn": "ARG/V/96",
        "photo": "juras_030_page31.png",
        "tytul": "Zaświadczenie Komisji Weryfikacyjnej AK — przejście kanałami z Powstania",
        "data": "1946",
        "typ": "zaswiadczenie",
        "opis_fizyczny": "Zaświadczenie na papierze urzędowym, pieczęć Komisji",
        "opis_tresci": "Pismo Polskiej Głównej Komisji Weryfikacyjnej AK potwierdzające przejście Krzysztofa Głuchowskiego kanałami z Powstania Warszawskiego (1.IX.1944) do obozu.",
        "seria": "V",
        "tworca": "Polska Główna Komisja Weryfikacyjna AK",
        "jezyk": "polski",
        "kontekst": "KLUCZOWY DOKUMENT — potwierdza udział w Powstaniu Warszawskim i ewakuację kanałami. 1.IX.1944 = miesiąc po wybuchu, w trakcie najcięższych walk o Stare Miasto.",
        "powiazania": ["ARG/V/52", "ARG/V/118"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/V/97",
        "photo": "juras_031_page32.png",
        "tytul": "Zaświadczenie Komisji Weryfikacyjnej AK — 7 Pułk Ułanów Lubelskich, Kraków 24.VI.1946",
        "data": "24.VI.1946",
        "typ": "zaswiadczenie",
        "opis_fizyczny": "Zaświadczenie na papierze urzędowym, pieczęć zielonym atramentem 'KOMISJI WERYFIKACYJNEJ A.K.', podpis zielonym atramentem. Format A5, papier pożółkły. Nagłówek: 'DOWÓDCA 2 KOMPANII A.K. / KOM. WERYFIKACYJNA'. L.dz. 1134/II/IV/46. Pieczęć: 'Komendant Uzupełn. Nr 3'.",
        "opis_tresci": "Zaświadczenie z Komisji Weryfikacyjnej AK potwierdzające służbę Krzysztofa Głuchowskiego w 7 Pułku Ułanów Lubelskich AK. Kraków, 24.VI.1946. Potwierdza: imię KRZYSZTOF, rocznik 1926, stopień SZEREGOWCA, nr ewidencyjny z 1944 r. Wystawione przez Dowódcę 2 Kompanii AK przy Komisji Weryfikacyjnej, z pieczęcią Komendanta Uzupełnień Nr 3.",
        "seria": "V",
        "tworca": "Komisja Weryfikacyjna AK / 7 Pułk Ułanów Lubelskich",
        "jezyk": "polski",
        "kontekst": "Dokument weryfikacji żołnierzy AK po wojnie. 7 Pułk Ułanów Lubelskich AK (kryptonim 'Jeleń') — jednostka kawaleryjska Okręgu Lublin AK, w Powstaniu Warszawskim walczyła na Żoliborzu i w Śródmieściu. Weryfikacja prowadzona w Krakowie w 1946 r. potwierdzała służbę konspiracyjną i powstańczą dla celów kombatanckich.",
        "powiazania": ["ARG/V/96", "ARG/V/118", "ARG/V/81"],
        "stan": "Dobry — pożółkły papier, zielony atrament pieczęci i podpisu czytelny"
    },
    {
        "sygn": "ARG/V/98",
        "photo": "juras_032_page33.png",
        "tytul": "Pismo ppłk. ANDERSA — Szef Wydziału Rodzin Wojskowych do St.Uł. Głuchowskiego, Londyn 1.III.1949",
        "data": "1.III.1949",
        "typ": "pismo",
        "opis_fizyczny": "Pismo maszynopisem na papierze urzędowym, format A4. Adres nadawcy: Londyn. Adres odbiorcy: St./Uł. Głuchowski Krzysztof, 25 Belney Airfield Thetford, Norfolk. L.dz. 2083/50/Opieki/IV/3./48. Podpis maszynowy: 'ANDERS ppłk.' z pieczęcią 'SZEF WYDZIAŁU RODZIN WOJSKOWYCH'. Dokument uszkodzony — brak dolnej części, plamy.",
        "opis_tresci": "Pismo od ppłk. Andersa jako Szefa Wydziału Rodzin Wojskowych do Starszego Ułana Krzysztofa Głuchowskiego w Norfolk. Dotyczy spraw likwidacyjnych — prosi o nadesłanie dokumentów dotyczących sprawdzenia interesu rodziny. Termin: do dnia 15 marca. Adres Krzysztofa: 25 Belney Airfield, Thetford, Norfolk — obóz PKPR (Polish Resettlement Corps) w byłej bazie RAF Bodney.",
        "seria": "V",
        "tworca": "ppłk Anders — Szef Wydziału Rodzin Wojskowych PSZ",
        "jezyk": "polski",
        "kontekst": "Dokument z podpisem ppłk. Andersa jako Szefa Wydziału Rodzin Wojskowych — instytucji opiekującej się rodzinami żołnierzy PSZ po wojnie. Adres Belney/Bodney Airfield w Norfolk potwierdza pobyt Krzysztofa w obozie PKPR. RAF Bodney — baza lotnicza używana po wojnie jako obóz dla polskich żołnierzy oczekujących na demobilizację lub resettlement.",
        "powiazania": ["ARG/V/100", "ARG/V/103", "ARG/V/83"],
        "stan": "Średni — dolna część uszkodzona, plamy, ale podpis i treść czytelne"
    },
    {
        "sygn": "ARG/V/99",
        "photo": "juras_033_page34.png",
        "tytul": "Notatki odręczne Krzysztofa — ewidencja dat służby, rozkazów i odznaczeń 1945–1946",
        "data": "1946",
        "typ": "notatka",
        "opis_fizyczny": "Notatki odręczne atramentem na pożółkłej kartce, format A6. Pismo drobne, pochyłe. Dwa kolumny z datami, numerami rozkazów i nazwiskami.",
        "opis_tresci": "Osobista ewidencja Krzysztofa Głuchowskiego: daty służby wojskowej, numery rozkazów, przydział do jednostek. Widoczne wpisy: 'Głuchowski K.', daty: 28.X.46, 12.XI.46, 25/46, 3.X.46, 18/46, 2.X.10.46, 15/46 i inne. Wymienione: 'Bryt. Muz bryt.', 'Korp', 'Med. instr ka' (instrukcja medyczna?), 'Kleppnec 7' i podpis 'Piekielska' na dole. Notatki przygotowawcze do weryfikacji lub ewidencji służby.",
        "seria": "V",
        "tworca": "Krzysztof Andrzej Głuchowski",
        "jezyk": "polski",
        "kontekst": "Prywatna ewidencja dat i rozkazów — typowe dla żołnierzy PSZ prowadzących osobistą dokumentację służby na potrzeby weryfikacji i przyszłych wniosków kombatanckich.",
        "powiazania": ["ARG/V/111", "ARG/V/112", "ARG/V/113"],
        "stan": "Średni — pożółkły papier, pismo czytelne"
    },

    # -- Podseria V/U: Zaświadczenia o służbie --
    {
        "sygn": "ARG/V/100",
        "photo": "juras_034_page35.png",
        "tytul": "ZAŚWIADCZENIE O ZAKOŃCZENIU SŁUŻBY — PSZ Nr 87949, St.Uł. Krzysztof Głuchowski, Londyn 24.II.1949",
        "data": "24.II.1949",
        "typ": "zaswiadczenie",
        "opis_fizyczny": "Zaświadczenie na papierze urzędowym PSZ z godłem (Orzeł Biały). Druk formularzowy wypełniony odręcznie i maszynowo. Pieczęć okrągła fioletowa: 'ZASTĘPCA KOMISJI LIKWIDACYJNEJ POLSKICH SIŁ ZBROJNYCH'. Podpis Zastępcy Komisji. Format A4.",
        "opis_tresci": "POLSKIE SIŁY ZBROJNE / ZAŚWIADCZENIE O ZAKOŃCZENIU SŁUŻBY / Nr 87949. Stwierdza się, że: 4 kpl. STARSZY UŁAN / Nr M.T. Gd. ... / KRZYSZTOF GŁUCHOWSKI / (imiona i nazwisko) / Służył w Polskich Siłach Zbrojnych / Pełniąc [...] pod dowództwem brytyjskim do dnia [...]. Londyn, dnia 24/II/1949. Pieczęć KOMISJI LIKWIDACYJNEJ PSZ.",
        "seria": "V",
        "tworca": "Komisja Likwidacyjna Polskich Sił Zbrojnych",
        "jezyk": "polski",
        "kontekst": "Oficjalne zaświadczenie o zakończeniu służby wojskowej — dokument kluczowy dla dalszych losów Krzysztofa. Komisja Likwidacyjna PSZ działała w Londynie od 1947 r. zajmując się rozwiązywaniem Polskich Sił Zbrojnych na Zachodzie. Nr 87949 = numer kolejny zaświadczenia. Stopień: Starszy Ułan (odpowiednik L/Cpl w British Army). Po tym zaświadczeniu Krzysztof przeszedł do życia cywilnego — studiował w South West Essex Technical College.",
        "powiazania": ["ARG/V/91", "ARG/V/103", "ARG/V/98", "ARG/V/123"],
        "stan": "Dobry — pieczęć i tekst czytelne"
    },
    {
        "sygn": "ARG/V/101",
        "photo": "juras_035_page36.png",
        "tytul": "Świadectwo Dojrzałości — ze ZDJĘCIEM w mundurze, egzamin zdany 'Dobrze'",
        "data": "1946",
        "typ": "dyplom",
        "opis_fizyczny": "Świadectwo Dojrzałości na papierze urzędowym MWRiOP, ze zdjęciem legitymacyjnym w mundurze",
        "opis_tresci": "Świadectwo Dojrzałości — Ministerstwo WRiOP, Komisja Egzaminacyjna. Głuchowski Krzysztof, ur. 1926 Warszawa. Egzamin maturalny zdany z oceną 'Dobrze'. ZDJĘCIE Krzysztofa w mundurze wojskowym.",
        "seria": "V",
        "tworca": "MWRiOP / Komisja Egzaminacyjna",
        "jezyk": "polski",
        "kontekst": "JEDYNE ZNANE ZDJĘCIE KRZYSZTOFA W TYM ARCHIWUM — młody mężczyzna w mundurze. Świadectwo Dojrzałości = matura, najwyższy etap edukacji w ramach szkolnictwa polskiego na emigracji.",
        "powiazania": ["ARG/V/102", "ARG/V/65"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/V/102",
        "photo": "juras_036_page37.png",
        "tytul": "Świadectwo Dojrzałości — verso z podpisami komisji egzaminacyjnej",
        "data": "1946",
        "typ": "dyplom",
        "opis_fizyczny": "Verso świadectwa z pieczęcią MR i podpisami",
        "opis_tresci": "Odwrotna strona Świadectwa Dojrzałości — podpisy członków komisji egzaminacyjnej, pieczęć urzędowa.",
        "seria": "V",
        "tworca": "Komisja Egzaminacyjna",
        "jezyk": "polski",
        "kontekst": "Verso matury — podpisy komisji potwierdzają edukację polską na emigracji we Włoszech.",
        "powiazania": ["ARG/V/101"],
        "stan": "Dobry"
    },

    # -- Podseria V/V: Discharge i demobilizacja --
    {
        "sygn": "ARG/V/103",
        "photo": "juras_037_page38.png",
        "tytul": "Discharge Certificate — PSZ, Army No. 3004271, Witley Camp, 31.X.1948",
        "data": "31.X.1948",
        "typ": "discharge",
        "opis_fizyczny": "Certyfikat demobilizacyjny, druk urzędowy z pieczęcią RECORD OFFICE, POLISH RESETTLEMENT CORPS",
        "opis_tresci": "Discharge Certificate (Polskie Siły Zbrojne). Army No. 3004271, Głuchowski Krzysztof. Data demobilizacji: 31 October 1948, Witley Camp. Stopień: Pte. Okres służby: 3 years 2 months. Pieczęć: RECORD OFFICE, POLISH RESETTLEMENT CORPS.",
        "seria": "V",
        "tworca": "Polish Resettlement Corps / Record Office",
        "jezyk": "angielski",
        "kontekst": "KLUCZOWY DOKUMENT — oficjalne zakończenie służby wojskowej. Witley Camp (Surrey) = główna baza demobilizacyjna PKPR. 3 lata i 2 miesiące służby (VI.1945 – X.1948).",
        "powiazania": ["ARG/V/91", "ARG/V/100", "ARG/V/123"],
        "stan": "Dobry"
    },

    # -- Podseria V/W: Książeczka żołnierska (Soldier's Service Book) --
    {
        "sygn": "ARG/V/104",
        "photo": "juras_038_page39.png",
        "tytul": "Soldier's Service Book (Army Book 64) — Short Form of Will",
        "data": "1945–1948",
        "typ": "ksiazeczka",
        "opis_fizyczny": "Strona książeczki wojskowej z formularzem testamentowym",
        "opis_tresci": "Army Book 64 Part I — strona z Short Form of Will (skrócony formularz testamentowy) i instrukcjami. Standardowy element książeczki żołnierskiej British Army.",
        "seria": "V",
        "tworca": "British Army / HMSO",
        "jezyk": "angielski",
        "kontekst": "Formularz testamentowy w książeczce = przygotowanie na wypadek śmierci. Rutynowy element służby.",
        "powiazania": ["ARG/V/105", "ARG/V/106", "ARG/V/107", "ARG/V/108", "ARG/V/109"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/V/105",
        "photo": "juras_039_page40.png",
        "tytul": "Soldier's Service Book — okładka wewnętrzna i strona tytułowa",
        "data": "1945–1948",
        "typ": "ksiazeczka",
        "opis_fizyczny": "Okładka wewnętrzna + strona tytułowa, nr 43464/45",
        "opis_tresci": "Army Book 64, Part I — Soldier's Service Book. Numer książeczki: 43463/45 (odręczne wpisanie). Okładka wewnętrzna: DETAIL OF PERSONAL SIZED GARMENTS (rozmiary umundurowania) + Instructions to Soldier (8 punktów regulaminowych). 'You are held personally responsible for the safe custody of this book. You will always carry this book on your person.'",
        "seria": "V",
        "tworca": "British Army / HMSO",
        "jezyk": "angielski",
        "kontekst": "Okładka książeczki wojskowej Army Book 64 — strona tytułowa dokumentu służby w PSZ.",
        "powiazania": ["ARG/V/104", "ARG/V/106"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/V/106",
        "photo": "juras_040_page41.png",
        "tytul": "Soldier's Service Book — dane osobowe (str. 2-3)",
        "data": "1945–1948",
        "typ": "ksiazeczka",
        "opis_fizyczny": "Strony 2-3 książeczki z odręcznymi wpisami",
        "opis_tresci": "Dane osobowe: Army Number 4481G119261II, Surname GŁUCHOWSKI, Christian Names KRZYSZTOF, DOB 29.11.1926, Trade: bez zawodu (no trade), Religion: Roman-Kat. Adnotacja: DISCHARGED.",
        "seria": "V",
        "tworca": "British Army / PKPR",
        "jezyk": "angielski",
        "kontekst": "Kluczowe dane identyfikacyjne. 'No trade' = bez zawodu cywilnego — 19-latek który całe dorosłe życie spędził na wojnie.",
        "powiazania": ["ARG/V/104", "ARG/V/107"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/V/107",
        "photo": "juras_041_page42.png",
        "tytul": "Soldier's Service Book — Medical Classification, szczepienia (str. 8-9)",
        "data": "1945–1948",
        "typ": "ksiazeczka",
        "opis_fizyczny": "Strony 8-9 z tabelą szczepień i klasyfikacją medyczną",
        "opis_tresci": "Klasyfikacja medyczna (Medical Classification) i tabela szczepień (Vaccinations TAB). Wpisy okulistyczne.",
        "seria": "V",
        "tworca": "British Army Medical Service",
        "jezyk": "angielski",
        "kontekst": "Dokumentacja medyczna żołnierza — szczepienia obowiązkowe, stan zdrowia.",
        "powiazania": ["ARG/V/104", "ARG/V/106"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/V/108",
        "photo": "juras_042_page43.png",
        "tytul": "Soldier's Service and Pay Book — okładka zewnętrzna 'ARMY BOOK 64'",
        "data": "1945–1948",
        "typ": "ksiazeczka",
        "opis_fizyczny": "Okładka zewnętrzna książeczki, karton w kolorze khaki",
        "opis_tresci": "Okładka zewnętrzna: 'ARMY BOOK 64 — Soldier's Service and Pay Book'.",
        "seria": "V",
        "tworca": "British Army / HMSO",
        "jezyk": "angielski",
        "kontekst": "Army Book 64 = podstawowy dokument tożsamości żołnierza British Army. Polscy żołnierze PKPR otrzymywali identyczne książeczki.",
        "powiazania": ["ARG/V/104", "ARG/V/105", "ARG/V/106"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/V/109",
        "photo": "juras_043_page44.png",
        "tytul": "Karta odznaczeń Campaign Stars and Medals 1939–45",
        "data": "1945–1948",
        "typ": "ksiazeczka",
        "opis_fizyczny": "Karta z tabelą odznaczeń, część Army Book 64",
        "opis_tresci": "Tabela Campaign Stars, Clasps and Medals 1939-45: 1939-45 Star, Atlantic, Air Crew Europe, Africa, Pacific, Burma, France and Germany, Defence Medal, War Medal. Zaznaczone: 0-1-0.",
        "seria": "V",
        "tworca": "British Army",
        "jezyk": "angielski",
        "kontekst": "Karta odznaczeń brytyjskich — '0-1-0' oznacza przyznanie jednego medalu (prawdopodobnie War Medal 1939-45).",
        "powiazania": ["ARG/V/104", "ARG/V/110"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/V/110",
        "photo": "juras_044_page45.png",
        "tytul": "Pismo Under-Secretary of State for War — transmisja odznaczeń wojennych",
        "data": "1946–1948",
        "typ": "pismo",
        "opis_fizyczny": "Pismo urzędowe z herbem królewskim, druk maszynowy",
        "opis_tresci": "Pismo Under-Secretary of State for War: 'presents his compliments and has the honour to transmit Awards granted for service during the war of 1939-45'. Herb królewski — oficjalne nadanie odznaczeń.",
        "seria": "V",
        "tworca": "War Office / Under-Secretary of State for War",
        "jezyk": "angielski",
        "kontekst": "Oficjalna transmisja brytyjskich odznaczeń wojennych — uznanie służby Krzysztofa przez Koronę Brytyjską.",
        "powiazania": ["ARG/V/109"],
        "stan": "Dobry"
    },

    # -- Podseria V/X: Notatki i ewidencja odznaczeń --
    {
        "sygn": "ARG/V/111",
        "photo": "juras_045_page46.png",
        "tytul": "Notatki — ewidencja odznaczeń 3 DSK, Medal Wojska",
        "data": "1946",
        "typ": "notatka",
        "opis_fizyczny": "Notatki odręczne na papierze w kratkę",
        "opis_tresci": "Notatki z numerami odznaczeń: Odznaka 3 DSK nr 155/46 i 245/46, Medal Wojska No 245, Rozkaz 2 Korpusu, data 22.IX.1946. Ewidencja osobista odznaczeń.",
        "seria": "V",
        "tworca": "Krzysztof Andrzej Głuchowski",
        "jezyk": "polski",
        "kontekst": "Prywatna ewidencja odznaczeń — żołnierz notuje numery rozkazów i legitymacji do własnych akt.",
        "powiazania": ["ARG/V/66", "ARG/V/109"],
        "stan": "Średni"
    },
    {
        "sygn": "ARG/V/112",
        "photo": "juras_046_page47.png",
        "tytul": "Notatki weryfikacyjne — AK, NEISS, 7 Pułk, Kompania I",
        "data": "lata 40. XX w.",
        "typ": "notatka",
        "opis_fizyczny": "Dwie kartki z notatkami odręcznymi",
        "opis_tresci": "Dwie kartki z notatkami. Górna: 'Ukończenie Szkomontu Nr CS/46 14.3.1946, Rozkaz Dt-wa 3 DSK Korp, Nr 15 5.3.1946 G.I pr.2'. Dolna: 'WERYFIKACJA AK / 7 P.UŁ. Rekon. Komp. / Nr 155 / Głuchowski Krzysztof — Stanisław (potwierdzenie ojca!) / Sr.ułan / 1926 / Powstanie 1944 / L.dz. ewid. / 1134/II.AK/46 / 12.VI.1946'. Materiał przygotowawczy do procesu weryfikacji AK.",
        "seria": "V",
        "tworca": "Krzysztof Andrzej Głuchowski",
        "jezyk": "polski",
        "kontekst": "Notatki przygotowawcze do procesu weryfikacji AK — zbieranie dat, numerów rozkazów, świadectw służby. NEISS = prawdopodobnie Neisse (Nysa) — obóz przejściowy.",
        "powiazania": ["ARG/V/113", "ARG/V/96"],
        "stan": "Średni"
    },
    {
        "sygn": "ARG/V/113",
        "photo": "juras_047_page48.png",
        "tytul": "Notatki — numery rozkazów, Medal Wojska, Odznaka 3 DSK",
        "data": "1946",
        "typ": "notatka",
        "opis_fizyczny": "Notatki odręczne, format zeszytowy",
        "opis_tresci": "Notatki z ewidencją odznaczeń i dat: 'Weryfikacja 1-13 sz...' / 'MEDAL WOJSKA — Rozkaz Nr 245, 29.10.1946' / 'Prz. 2 Korp, 22.9.1946' / 'ODZNAKA 3DSK — Rozkaz Dzienny Nr 256, 12.11.1946' / '3 DSK Nr 71/46 G.I., 8.11.1946' / 'hadij w... 257/46'. Systematyczna ewidencja odznaczeń i rozkazów dziennych 2 Korpusu i 3 DSK.",
        "seria": "V",
        "tworca": "Krzysztof Andrzej Głuchowski",
        "jezyk": "polski",
        "kontekst": "j.w. Quinoy = prawdopodobnie lokalizacja kwatery jednostki we Włoszech.",
        "powiazania": ["ARG/V/111", "ARG/V/112"],
        "stan": "Średni"
    },

    # -- Podseria V/Y: Wyposażenie i testament --
    {
        "sygn": "ARG/V/114",
        "photo": "juras_048_page49.png",
        "tytul": "Wykaz wyposażenia osobistego — formularz wojskowy, str. 1",
        "data": "1945–1946",
        "typ": "formularz",
        "opis_fizyczny": "Formularz tabelaryczny, wypełniony odręcznie",
        "opis_tresci": "Wykaz wyposażenia osobistego żołnierza: Krzysztof stw. Głuchowski. Tabela z listą rzeczy: umundurowanie, oporządzenie.",
        "seria": "V",
        "tworca": "kancelaria wojskowa",
        "jezyk": "polski",
        "kontekst": "Inwentarz osobisty żołnierza — standardowa procedura ewidencyjna przy wcieleniu lub zwolnieniu.",
        "powiazania": ["ARG/V/115"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/V/115",
        "photo": "juras_049_page50.png",
        "tytul": "Wykaz wyposażenia osobistego — str. 2 (Oporządzenie, Higiena, Uzbrojenie)",
        "data": "1945–1946",
        "typ": "formularz",
        "opis_fizyczny": "Druga strona formularza z podpisem dowódcy",
        "opis_tresci": "Kontynuacja wykazu: Oporządzenie, Higiena, Pago (żołd?), Uzbrojenie. Podpis dowódcy na dole.",
        "seria": "V",
        "tworca": "kancelaria wojskowa",
        "jezyk": "polski",
        "kontekst": "Druga strona wykazu wyposażenia — uzbrojenie i higiena, podpis dowódcy potwierdza ewidencję.",
        "powiazania": ["ARG/V/114"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/V/116",
        "photo": "juras_050_page51.png",
        "tytul": "Formularz testamentu własnoręcznego — druk wojskowy (Prawo Polskie)",
        "data": "1945–1948",
        "typ": "formularz",
        "opis_fizyczny": "Druk wojskowy z instrukcją prawną, format A5",
        "opis_tresci": "Forma testamentu własnoręcznego — druk wojskowy 'Według Prawa Polskiego'. Instrukcja pisania testamentu dla żołnierzy PSZ.",
        "seria": "V",
        "tworca": "PSZ / kancelaria prawna",
        "jezyk": "polski",
        "kontekst": "Testament żołnierski — obowiązkowy formularz. Polskie prawo spadkowe stosowane wobec żołnierzy PSZ na emigracji.",
        "powiazania": ["ARG/V/117", "ARG/V/104"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/V/117",
        "photo": "juras_051_page52.png",
        "tytul": "Formularz testamentu — verso",
        "data": "1945–1948",
        "typ": "formularz",
        "opis_fizyczny": "Odwrotna strona formularza testamentowego",
        "opis_tresci": "Verso formularza testamentowego — kontynuacja instrukcji lub miejsce na wpisy.",
        "seria": "V",
        "tworca": "PSZ",
        "jezyk": "polski",
        "kontekst": "Verso formularza testamentu żołnierskiego — polskie prawo spadkowe dla PSZ na emigracji.",
        "powiazania": ["ARG/V/116"],
        "stan": "Dobry"
    },

    # -- Podseria V/Z: Legitymacje Krzyża AK i Odznaki Pamiątkowej AK --
    {
        "sygn": "ARG/V/118",
        "photo": "juras_052_page53.png",
        "tytul": "Legitymacja Krzyża Armii Krajowej — wewnątrz, nr 3316",
        "data": "7.III.1968",
        "typ": "leg",
        "opis_fizyczny": "Legitymacja wewnętrzna z wpisami, pieczęć, podpis",
        "opis_tresci": "Legitymacja Krzyża Armii Krajowej (wewnątrz). Nazwisko: GŁUCHOWSKI / Imię: KRZYSZTOF / Pseudonim: 'JURAŚ' / Przydział: Zw. Komp./Plut. III/2, 7 PUŁK UŁAN. LUBEL. 'JELEŃ'. Odznaczony KRZYŻEM ARMII KRAJOWEJ dnia 1 sierpnia 1966 roku, ustanowionym przez dowódcę A.K. gen. Tadeusza Bora-Komorowskiego dla upamiętnienia wysiłku żołnierza Polski Podziemnej w latach 1939–1945. Podpis: K. Ziemski–Wachnowski, Z-ca D-cy W-skiego Korpusu A.K. Londyn, dnia 7.7.68.",
        "seria": "V",
        "tworca": "Stowarzyszenie AK / gen. T. Bór-Komorowski",
        "jezyk": "polski",
        "kontekst": "KLUCZOWY DOKUMENT TOŻSAMOŚCI AKOWSKIEJ — potwierdza pseudonim 'Juras', przydział do plutonu III/2 Kompanii V, przynależność do 7 P.Uł. 'Jeleń'. Nadanie przez samego Bora-Komorowskiego. K. Ziemski 'Wachnowski' = płk Kazimierz Ziemski, prezes Zarządu Głównego AK na emigracji.",
        "powiazania": ["ARG/V/119", "ARG/V/120", "ARG/V/96"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/V/119",
        "photo": "juras_053_page54.png",
        "tytul": "Legitymacja Krzyża AK — okładka z symbolem AK, nr 3316",
        "data": "1968",
        "typ": "leg",
        "opis_fizyczny": "Okładka legitymacji z wytłoczonym symbolem AK (kotwica)",
        "opis_tresci": "Okładka legitymacji Krzyża Armii Krajowej nr 3316 z symbolem AK (kotwica 'Polska Walcząca').",
        "seria": "V",
        "tworca": "Stowarzyszenie AK",
        "jezyk": "polski",
        "kontekst": "Okładka legitymacji Krzyża AK nr 3316 — kotwica PW, dokument tożsamości akowskiej.",
        "powiazania": ["ARG/V/118"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/V/120",
        "photo": "juras_054_page55.png",
        "tytul": "Legitymacja Krzyża AK — duplikat / wariant",
        "data": "1968",
        "typ": "leg",
        "opis_fizyczny": "Legitymacja w innym formacie, ta sama treść",
        "opis_tresci": "Duplikat lub wariant legitymacji Krzyża AK — ta sama treść co nr 3316, inny format druku.",
        "seria": "V",
        "tworca": "Stowarzyszenie AK",
        "jezyk": "polski",
        "kontekst": "Drugi egzemplarz legitymacji — zachowany prawdopodobnie na wypadek utraty oryginału.",
        "powiazania": ["ARG/V/118", "ARG/V/119"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/V/121",
        "photo": "juras_055_page56.png",
        "tytul": "Legitymacja Odznaki Pamiątkowej AK — okładka z symbolem PW",
        "data": "1946",
        "typ": "leg",
        "opis_fizyczny": "Okładka legitymacji z symbolem PW (Polska Walcząca)",
        "opis_tresci": "Okładka legitymacji Odznaki Pamiątkowej Armii Krajowej z symbolem PW (Polska Walcząca — kotwica).",
        "seria": "V",
        "tworca": "Komisja Weryfikacyjna 2 Korpusu AK",
        "jezyk": "polski",
        "kontekst": "Odznaka Pamiątkowa AK — nadawana weteranom Armii Krajowej zweryfikowanym przez komisje kombatanckie.",
        "powiazania": ["ARG/V/122"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/V/122",
        "photo": "juras_056_page57.png",
        "tytul": "Legitymacja Odznaki Pamiątkowej AK — wewnątrz, nr 4042",
        "data": "12.VI.1946",
        "typ": "leg",
        "opis_fizyczny": "Legitymacja wewnętrzna z danymi i pieczęcią",
        "opis_tresci": "Legitymacja Odznaki Pamiątkowej AK: Stopień: STARSZY UŁAN / Nazwisko i imię: GŁUCHOWSKI KRZYSZTOF / Pseudonim: JURAŚ / Nr: 404 (lub 4042) / Data przyznania: 12 czerwca 46 / PRZEWODNICZĄCY KAPITUŁY: podpis (gen.?) / DOWÓDZTWO 2 KORPUSU / KOMISJA WERYFIKACYJNA A.K. Pieczęć okrągła fioletowa. Podpis przewodniczącego i pieczęć Komisji.",
        "seria": "V",
        "tworca": "Komisja Weryfikacyjna 2 Korpusu AK",
        "jezyk": "polski",
        "kontekst": "Weryfikacja 2 Korpusu AK — potwierdzenie tożsamości akowskiej przez komisję złożoną z byłych żołnierzy AK. Data 12.VI.1946 = Włochy.",
        "powiazania": ["ARG/V/121", "ARG/V/118"],
        "stan": "Dobry"
    },

    # -- Podseria V/AA: Certyfikaty PKPR --
    {
        "sygn": "ARG/V/123",
        "photo": "juras_057_page58.png",
        "tytul": "Certificate P.R.C. Record Office — Witley Camp, 19.II.1948",
        "data": "19.II.1948",
        "typ": "certyfikat",
        "opis_fizyczny": "Certyfikat urzędowy, druk maszynowy z pieczęcią P.R.C.",
        "opis_tresci": "CERTIFICATE — P.R.C. Record Office, Witley Camp, Nr. Godalming, Surrey. Tel. Godalming 1520 Ext. 101. Ref. No. 2335/48. Data: 19 FEB 1948. 'This is to certify that No. 3004271 L/CPL. GŁUCHOWSKI KRZYSZTOF was enlisted into P.R.C. 1.11.46, after serving with Polish Forces under British Command from 14.7.45. to 1.11.46.' Podpis: Record Officer. Pieczęć: 'Record Officer / P.R.C. Records / Officer Ewidencyjny / Biura Ew. P.K.P.'",
        "seria": "V",
        "tworca": "P.R.C. Record Office, Witley Camp",
        "jezyk": "angielski",
        "kontekst": "Certyfikat potwierdzający przejście z PSZ do PKPR (P.R.C. = Polish Resettlement Corps). Okres służby w PSZ: 14.VII.1945 – 1.XI.1946. Wcielenie do PKPR: 1.XI.1946.",
        "powiazania": ["ARG/V/103", "ARG/V/124", "ARG/V/125"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/V/124",
        "photo": "juras_058_page59.png",
        "tytul": "Certificate P.R.C. — duplikat (19.II.1948)",
        "data": "19.II.1948",
        "typ": "certyfikat",
        "opis_fizyczny": "Duplikat certyfikatu, identyczny tekst",
        "opis_tresci": "Kopia certyfikatu PKPR z 19.II.1948 — identyczny tekst co ARG/V/123.",
        "seria": "V",
        "tworca": "P.R.C. Record Office",
        "jezyk": "angielski",
        "kontekst": "Drugi egzemplarz — zachowany jako zabezpieczenie dokumentacji.",
        "powiazania": ["ARG/V/123"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/V/125",
        "photo": "juras_059_page60.png",
        "tytul": "Certificate P.R.C. Record Office — nr 3023271, 3.III.1948",
        "data": "3.III.1948",
        "typ": "certyfikat",
        "opis_fizyczny": "Certyfikat z innym numerem, druk maszynowy z pieczęcią",
        "opis_tresci": "Certificate P.R.C. Record Office, nr 3023271, data 3 March 1948. Potwierdzenie enlistment do PKPR.",
        "seria": "V",
        "tworca": "P.R.C. Record Office",
        "jezyk": "angielski",
        "kontekst": "Inny numer ewidencyjny (3023271 vs 3004271) — możliwe przerejestrowanie w PKPR.",
        "powiazania": ["ARG/V/123"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/V/126",
        "photo": "juras_060_page61.png",
        "tytul": "Certificate P.R.C. — kolejna kopia (19.II.1948)",
        "data": "19.II.1948",
        "typ": "certyfikat",
        "opis_fizyczny": "Kolejna kopia certyfikatu",
        "opis_tresci": "Kolejna kopia certyfikatu PKPR z 19.II.1948 — identyczny tekst.",
        "seria": "V",
        "tworca": "P.R.C. Record Office",
        "jezyk": "angielski",
        "kontekst": "Trzeci egzemplarz tego samego dokumentu — emigrant zabezpieczał się wieloma kopiami.",
        "powiazania": ["ARG/V/123", "ARG/V/124"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/V/127",
        "photo": "juras_061_page62.png",
        "tytul": "Certificate P.R.C. — kopia z pieczęcią",
        "data": "19.II.1948",
        "typ": "certyfikat",
        "opis_fizyczny": "Certyfikat z wyraźną pieczęcią PKPR Record Office",
        "opis_tresci": "Certificate z pieczęcią PKPR Record Office — identyczny tekst, inna kopia z wyraźniejszą pieczęcią.",
        "seria": "V",
        "tworca": "P.R.C. Record Office",
        "jezyk": "angielski",
        "kontekst": "Kolejna kopia certyfikatu PKPR — emigrant zabezpieczał się wieloma egzemplarzami dokumentów.",
        "powiazania": ["ARG/V/123"],
        "stan": "Dobry"
    },

    # -- Podseria V/AB: Przepustki (duplikaty) --
    {
        "sygn": "ARG/V/128",
        "photo": "juras_062_page63.png",
        "tytul": "Przepustka Army Form B.295 — pieczęć PUŁK UŁANÓW LUBELSKICH",
        "data": "1946–1948",
        "typ": "przepustka",
        "opis_fizyczny": "Formularz przepustki z pieczęcią pułkową",
        "opis_tresci": "PASS — Army Form B.295. Pieczęć okrągła fioletowa: '7 PUŁK UŁANÓW LUBELSKICH / STARCÓW REGIMENT'. Nr 3004271, Rank: L/Cpl., Name: GŁUCHOWSKI KRZYSZTOF. Camp: Ql. Bower Ward Camp. Has permission to be absent from his unit from 9.9.47. Destination: London. Podpis oficera: H. Mazur(?). Przepustka do Londynu z pieczęcią 7 Pułku Ułanów Lubelskich.",
        "seria": "V",
        "tworca": "7 P.Uł. Lubelskich / British Army",
        "jezyk": "angielski",
        "kontekst": "Kolejna przepustka z pieczęcią pułkową — dowód przynależności do 7 P.Uł. w strukturach brytyjskich.",
        "powiazania": ["ARG/V/81", "ARG/V/129"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/V/129",
        "photo": "juras_063_page64.png",
        "tytul": "Instrukcja medyczna ATS — verso przepustki",
        "data": "1946–1948",
        "typ": "ulotka",
        "opis_fizyczny": "Druk medyczny na odwrocie przepustki",
        "opis_tresci": "Instrukcja medyczna dla żołnierzy ATS — odwrotna strona formularza przepustki. Identyczna treść co ARG/V/82.",
        "seria": "V",
        "tworca": "British Army",
        "jezyk": "angielski",
        "kontekst": "Standardowy druk na verso przepustek brytyjskich.",
        "powiazania": ["ARG/V/128", "ARG/V/82"],
        "stan": "Dobry"
    },

    # -- Podseria V/AC: Dokumenty tożsamości emigranta --
    {
        "sygn": "ARG/V/130",
        "photo": "juras_064_page65.png",
        "tytul": "Alien's Identity Certificate — South West Essex Technical College, 31.X.1947",
        "data": "31.X.1947",
        "typ": "karta_id",
        "opis_fizyczny": "Dokument tożsamości, format legitymacyjny, wpisy urzędowe",
        "opis_tresci": "ALIEN IDENTITY CERTIFICATE (Dowód Osobistości Cudzoziemca). Rank: L/CPL. Name: GŁUCHOWSKI. Status: STUDENT. Miejsce nauki: SOUTH WEST ESSEX TECHNICAL COLLEGE AND SCHOOL OF [ART?], ERITH/PARK ROAD. Pieczęć: 'No. 3 RELEGATION / LONDON COMMAND / P.K.P.' Data: 31.10.47. Po demobilizacji Krzysztof studiował w szkole technicznej w Essex — początek kariery inżynierskiej.",
        "seria": "V",
        "tworca": "Home Office / Alien Registration",
        "jezyk": "angielski",
        "kontekst": "KLUCZOWY DOKUMENT EMIGRACYJNY — Krzysztof jako 'Alien' (cudzoziemiec) w Anglii, student szkoły technicznej. Gravesend = port wejścia do Anglii.",
        "powiazania": ["ARG/V/131", "ARG/V/138"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/V/131",
        "photo": "juras_065_page66.png",
        "tytul": "Alien's Identity Certificate — verso (adres High Wycombe, Bucks)",
        "data": "1947–1948",
        "typ": "karta_id",
        "opis_fizyczny": "Verso dokumentu z adresami i pieczęciami rejestracyjnymi",
        "opis_tresci": "Verso certyfikatu tożsamości. Adres: Camelcell Court, 9 a/b Empire Ltd, Corporation Street, High Wycombe, Bucks. Pieczęcie Alien Registration — rejestracja cudzoziemca.",
        "seria": "V",
        "tworca": "Home Office / Alien Registration",
        "jezyk": "angielski",
        "kontekst": "High Wycombe, Buckinghamshire — miejsce zamieszkania Krzysztofa w Anglii. Obowiązek meldunkowy cudzoziemców (Alien Registration).",
        "powiazania": ["ARG/V/130"],
        "stan": "Dobry"
    },

    # -- Podseria V/AD: Biogram i weryfikacja --
    {
        "sygn": "ARG/V/132",
        "photo": "juras_066_page67.png",
        "tytul": "Biogram Krzysztofa Głuchowskiego — druk biograficzny",
        "data": "lata 60.–70. XX w.",
        "typ": "biogram",
        "opis_fizyczny": "Druk biograficzny, tekst maszynowy, format encyklopedyczny",
        "opis_tresci": "Biogram Krzysztofa Głuchowskiego — pełna historia: AK, Powstanie Warszawskie, 3 DSK, emigracja do Brazylii, inżynier. Odznaczenia: Krzyż Walecznych, Krzyż AK nr 3316, Medal Wojska, War Medal.",
        "seria": "V",
        "tworca": "redakcja wydawnictwa / stowarzyszenie kombatanckie",
        "jezyk": "polski",
        "kontekst": "KLUCZOWY DOKUMENT BIOGRAFICZNY — syntetyczny opis całego życia Krzysztofa. Potwierdza emigrację do Brazylii i zawód inżyniera.",
        "powiazania": ["ARG/V/118", "ARG/V/103", "ARG/II/33"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/V/133",
        "photo": "juras_067_page68.png",
        "tytul": "Dokument War Office / MI5 (CONFIDENTIAL) — weryfikacja Głuchowskiego",
        "data": "1946–1947",
        "typ": "pismo",
        "opis_fizyczny": "Dokument poufny (CONFIDENTIAL), druk maszynowy, formularz wywiadowczy",
        "opis_tresci": "PEŁNA KARTA SŁUŻBY (CONFIDENTIAL) — All-Purpose Record z P.R.C. Record Office. Dane: born 29th November 1926, Marital status: Single, Religion: Roman Catholic, Civilian (prior to army service): Student. Service from Polish Forces under British Command from 14 July 1945 (Italy). Joined P.R.C. 5.XI.1946(?). Medals and Awards: War Medal 1939/45. Demobilised: Very Good conduct. Pieczęć: POLISH RESETTLEMENT CORPS / RECORD OFFICE. Ref No. 3/4217 (R.O.F.O.).",
        "seria": "V",
        "tworca": "War Office / MI5",
        "jezyk": "angielski",
        "kontekst": "DOKUMENT WYWIADOWCZY — MI5 weryfikowało polskich żołnierzy pod kątem lojalności politycznej. 'Politically Well-Minded' = pozytywna ocena. Ujawnia miejsce urodzenia: Grzegorzów, rodziców: Stefan i Helena.",
        "powiazania": ["ARG/V/94", "ARG/V/103"],
        "stan": "Dobry"
    },

    # -- Podseria V/AE: Fotografia proporca --
    {
        "sygn": "ARG/V/134",
        "photo": "juras_068_page69.png",
        "tytul": "Fotografia proporca/sztandaru 7 Pułku Ułanów Lubelskich — ZAGINIONEGO W POWSTANIU WARSZAWSKIM",
        "data": "przed 1944",
        "typ": "fotografia",
        "opis_fizyczny": "Mała fotografia czarno-biała, format ok. 6×5 cm. Przedstawia proporczyk pułkowy z sylwetką jelenia na ciemnym tle. Krawędzie nieregularne — zdjęcie wycięte lub obcięte.",
        "opis_tresci": "Fotografia proporca/sztandaru 7 Pułku Ułanów Lubelskich 'Jeleń' — PROPORCZYK ZAGINĄŁ W POWSTANIU WARSZAWSKIM 1944. Zdjęcie jest jedynym zachowanym śladem po oryginalnym sztandarze pułkowym. Sylwetka jelenia skaczącego na ciemnym tle — symbol pułku.",
        "seria": "V",
        "tworca": "nieznany",
        "jezyk": "—",
        "kontekst": "DOKUMENT O WYJĄTKOWEJ WARTOŚCI HISTORYCZNEJ — jedyna znana fotografia proporca/sztandaru 7 Pułku Ułanów Lubelskich AK, który zaginął podczas Powstania Warszawskiego 1944. Sztandary pułkowe były najcenniejszymi symbolami jednostki — ich utrata w boju miała głębokie znaczenie symboliczne. Zachowanie tego zdjęcia przez Krzysztofa świadczy o głębokim przywiązaniu do tradycji pułkowej.",
        "powiazania": ["ARG/V/81", "ARG/V/118", "ARG/V/97", "ARG/V/128", "ARG/VI/3"],
        "stan": "Dobry — zdjęcie czytelne, kontrast zachowany"
    },

    # -- Podseria V/AF: Ephemera i kartki okolicznościowe --
    {
        "sygn": "ARG/V/135",
        "photo": "juras_069_page70.png",
        "tytul": "Kartka od Stowarzyszenia Polskich Przemysłowców (SPP) — życzenia",
        "data": "lata 50.–60. XX w.",
        "typ": "druk",
        "opis_fizyczny": "Kartka okolicznościowa z podpisami wielu osób",
        "opis_tresci": "Kartka od SPP (Stowarzyszenie Polskich...?) z Londynu do Krzysztofa w Brazylii. Tekst: 'Szanowny i Drogi Krzysztofie / Pozdrowienia z Londynu / od Pracowników i Członków / 2 SPP / A w załączeniu nasz / nowy Biuletyn nr 10'. Podpisy: Marian, Bartlow, Podkowiak, Bogucki, John Malcolm, Anna Hilden i inni. Na dole: 'Krzychu! Idź!' i 'Best wishes / najlepsze życzenia / z Londynu / Rodesk z dm. K.I. Domu / i z wielkim Brunon'. Wielopodpisowa kartka od londyńskiej Polonii.",
        "seria": "V",
        "tworca": "SPP / środowisko polonijne",
        "jezyk": "polski",
        "kontekst": "Stowarzyszenie Polskich Przemysłowców — organizacja polonijna, prawdopodobnie w Brazylii. Ślad aktywności społecznej Krzysztofa w Polonii.",
        "powiazania": ["ARG/V/132"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/V/136",
        "photo": "juras_070_page71.png",
        "tytul": "Kartka artystyczna — linoryt 'Fundusz Praskiej Armii Krajowej', 1944",
        "data": "1944",
        "typ": "druk",
        "opis_fizyczny": "Kartka artystyczna, linoryt/drzeworyt, druk okolicznościowy",
        "opis_tresci": "Kartka artystyczna — linoryt lub drzeworyt: 'Fundusz Praskiej Armii Krajowej', rok 1944, Książka. Druk konspiracyjny lub okolicznościowy.",
        "seria": "V",
        "tworca": "AK Praga / artysta nieznany",
        "jezyk": "polski",
        "kontekst": "Druk konspiracyjny Praskiej AK — zbiórka na Fundusz AK Pragi Warszawskiej. Unikat graficzny z okresu Powstania.",
        "powiazania": ["ARG/V/118"],
        "stan": "Średni"
    },
    {
        "sygn": "ARG/V/137",
        "photo": "juras_071_page72.png",
        "tytul": "Wycinek prasowy — fotografia tablicy z Palmirów",
        "data": "lata 50.–60. XX w.",
        "typ": "wycinek",
        "opis_fizyczny": "Wycinek z gazety, mały format (ok. 8×5 cm), papier gazetowy pożółkły, krawędzie nierówne (wycięty ręcznie). Fotografia tablicy pamiątkowej na tle muru/ściany z cegieł. Obok tekst drukowany: podpis pod zdjęciem.",
        "opis_tresci": "Wycinek prasowy z fotografią tablicy pamiątkowej z Palmirów. Napis na tablicy (częściowo czytelny): 'STAWIALIŚMY OPÓR / [...] / PRACOWALIŚMY / [...] / ŻOŁNIERZE / UMRZEĆ / [...] / CIERPIEĆ'. Podpis pod zdjęciem: 'Nad tablicą przy wejściu na cmentarz w Palmirach umieszczono białą chryzantemę.' Fotografia przedstawia kamienną tablicę z wyrzeźbionym tekstem na elewacji budynku lub muru.",
        "seria": "V",
        "tworca": "prasa polska (krajowa lub polonijna)",
        "jezyk": "polski",
        "kontekst": "Palmiry — las pod Warszawą, miejsce masowych egzekucji dokonywanych przez Niemców na polskiej inteligencji i działaczach podziemia (1939–1941, ok. 1700 ofiar). Cmentarz-mauzoleum w Palmirach stał się jednym z najważniejszych miejsc pamięci narodowej. Wycinek zachowany przez Krzysztofa — prawdopodobnie z prasy krajowej lub polonijnej z lat 50.-60. Biała chryzantema — symbol pamięci o zmarłych w polskiej tradycji.",
        "powiazania": [],
        "stan": "Średni — papier gazetowy, kruchy"
    },

    # -- Podseria V/AG: Życie studenckie w Anglii --
    {
        "sygn": "ARG/V/138",
        "photo": "juras_072_page73.png",
        "tytul": "Bilet członkowski South West Essex Technical College, sesja 1947-48",
        "data": "1947–1948",
        "typ": "bilet",
        "opis_fizyczny": "Bilet / karta studencka, mały format, druk z odręcznym numerem",
        "opis_tresci": "Bilet członkowski South West Essex Technical College and School of Art, Forest Road E.17. Session 1947-48, No. 1149, Fee Paid 5/-.",
        "seria": "V",
        "tworca": "South West Essex Technical College",
        "jezyk": "angielski",
        "kontekst": "Krzysztof jako student szkoły technicznej w Forest Gate, East London. Fee 5/- (pięć szylingów) — opłata studencka. Okres readaptacji cywilnej w ramach PKPR.",
        "powiazania": ["ARG/V/139", "ARG/V/130"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/V/139",
        "photo": "juras_073_page74.png",
        "tytul": "Bilet członkowski — verso ('This ticket is not transferable')",
        "data": "1947–1948",
        "typ": "bilet",
        "opis_fizyczny": "Verso biletu z klauzulą i podpisem",
        "opis_tresci": "Verso biletu studenckiego: 'This ticket is not transferable', podpis studenta.",
        "seria": "V",
        "tworca": "South West Essex Technical College",
        "jezyk": "angielski",
        "kontekst": "Verso biletu studenckiego — podpis Krzysztofa, readaptacja cywilna w ramach PKPR.",
        "powiazania": ["ARG/V/138"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/V/140",
        "photo": "juras_074_page75.png",
        "tytul": "Rysunek odręczny — szkic żaglowca na morzu",
        "data": "ok. 1947–1948",
        "typ": "rysunek",
        "opis_fizyczny": "Szkic ołówkiem na papierze, format ok. 15×15 cm. Przedstawia żaglowiec (bark lub brygantynę) na morzu, z rozstawionymi żaglami i masztami. Rysowany pewną ręką — detal olinowania i ożaglowania. W prawym górnym rogu odręczna adnotacja (data lub podpis, trudno czytelna). Papier lekko pożółkły, ślad zagięcia pośrodku.",
        "opis_tresci": "Rysunek odręczny Krzysztofa — żaglowiec na pełnym morzu z rozstawionymi żaglami. Widoczne maszty, olinowanie, kadłub, fale morskie i dym/mgła. Rysunek techniczny ale z artystycznym wyczuciem — widać zamiłowanie do morza i żeglarstwa. W prawym górnym rogu dopisek (nieczytelny z fotografii).",
        "seria": "V",
        "tworca": "Krzysztof Andrzej Głuchowski",
        "jezyk": "—",
        "kontekst": "PROFETYCZNY RYSUNEK: Krzysztof rysuje żaglowiec w Anglii — kilka lat później emigruje do Brazylii i zakłada Brazylijską Unię Żeglarską (wg autobiogramu z 1995). Pasja morska widoczna już w okresie studenckim. Rysunek wykonany prawdopodobnie w South West Essex Technical College (1947-48) — ćwiczenie z rysunku technicznego, ale temat wybrany z zamiłowania. Detal olinowania wskazuje na znajomość budowy żaglowców.",
        "powiazania": ["ARG/V/138", "ARG/V/80", "ARG/V/166"],
        "stan": "Dobry"
    },

    # -- Podseria V/AH: Prasa polonijna --
    {
        "sygn": "ARG/V/141",
        "photo": "juras_075_page76.png",
        "tytul": "Wycinek 'Życie Tygodnia' — CZYTELNICY PISZĄ, CMP 53",
        "data": "lata 40.–50. XX w.",
        "typ": "wycinek",
        "opis_fizyczny": "Wycinek prasowy z gazetki polonijnej",
        "opis_tresci": "Wycinek z 'Życie Tygodnia' — rubryka CZYTELNICY PISZĄ. Klub polonii, skrzynka pocztowa CMP 53. CMP = Central Mediterranean Forces Post.",
        "seria": "V",
        "tworca": "redakcja 'Życie Tygodnia'",
        "jezyk": "polski",
        "kontekst": "Prasa polska wydawana przy siłach zbrojnych we Włoszech/Wielkiej Brytanii. CMP = poczta polowa Central Mediterranean Forces.",
        "powiazania": ["ARG/V/142", "ARG/V/143"],
        "stan": "Średni — papier gazetowy"
    },
    {
        "sygn": "ARG/V/142",
        "photo": "juras_076_page77.png",
        "tytul": "Okładka 'Życie Tygodnia' — 'Ameryka walczy z 5-tą kolumną'",
        "data": "lata 40. XX w.",
        "typ": "gazeta",
        "opis_fizyczny": "Okładka gazetki polonijnej z fotografią prasową",
        "opis_tresci": "Okładka 'Życie Tygodnia' — 'Ludzie, Fakty, Zagadnienia'. Nagłówek: 'Ameryka walczy z 5-tą kolumną'. Fotografia prasowa.",
        "seria": "V",
        "tworca": "redakcja 'Życie Tygodnia'",
        "jezyk": "polski",
        "kontekst": "Prasa polonijna — tematyka polityczna i międzynarodowa. '5-ta kolumna' = temat szpiegostwa/dywersji, charakterystyczny dla prasy lat zimnowojennych.",
        "powiazania": ["ARG/V/141"],
        "stan": "Średni — papier gazetowy"
    },
    {
        "sygn": "ARG/V/143",
        "photo": "juras_077_page78.png",
        "tytul": "Wycinek 'Smutna, ale pouczająca sprawa' — Klaudiusz Hrabyk",
        "data": "lata 40.–50. XX w.",
        "typ": "wycinek",
        "opis_fizyczny": "Wycinek prasowy z artykułem",
        "opis_tresci": "Artykuł 'Smutna, ale pouczająca sprawa' autorstwa Klaudiusza Hrabyka. Wycinek z prasy polonijnej.",
        "seria": "V",
        "tworca": "Klaudiusz Hrabyk / prasa polonijna",
        "jezyk": "polski",
        "kontekst": "Klaudiusz Hrabyk — publicysta polonijny. Artykuł zachowany przez Krzysztofa — ślad lektury prasowej emigranta.",
        "powiazania": ["ARG/V/141"],
        "stan": "Średni — papier gazetowy"
    },
    {
        "sygn": "ARG/V/144",
        "photo": "juras_078_page79.png",
        "tytul": "Zaświadczenie płk. dypl. Ziemskiego Karola — potwierdzenie udziału w Powstaniu i odznaczenia Krzyżem Walecznych",
        "data": "po 1945",
        "typ": "zaswiadczenie",
        "opis_fizyczny": "Zaświadczenie maszynopisem na papierze A4. Nagłówek: 'ZIEMSKI KAROL / PUŁKOWNIK DYPLOMOWANY / DOWÓDCA POLSKIEGO OKRĘGU / WARSZAWA–ŻOLIBORZ'. Pieczęć okrągła organizacji kombatanckiej na dole. Podpis Ziemskiego. Stan dobry, tekst czytelny.",
        "opis_tresci": "ZAŚWIADCZENIE płk. dypl. Karola Ziemskiego, b. Dowódcy Grupy w Powstaniu Warszawskim. Zaświadcza udział w Powstaniu 1944 i walkach w Grupie Północ (Żoliborz). Potwierdza odznaczenie KRZYŻEM WALECZNYCH po raz pierwszy. Podaje numer rozkazu: Nr 24 z dnia IX.1944. Balistraszego/baldachego(?) strzelca. Podpis: ZIEMSKI KAROL, b. Dowódca Okręgu Warszawa IIIA, Pułkownik Dyplomowany.",
        "seria": "V",
        "tworca": "płk dypl. Karol Ziemski ps. 'Wachnowski'",
        "jezyk": "polski",
        "kontekst": "KLUCZOWY DOKUMENT — płk Karol Ziemski 'Wachnowski' (1901–1982), Dowódca Okręgu Warszawa AK, dowodził Grupą 'Północ' (Żoliborz) podczas Powstania Warszawskiego. Ten sam Ziemski podpisał legitymację Krzyża AK Krzysztofa (ARG/V/118) jako Z-ca D-cy Warszawskiego Korpusu AK. Zaświadczenie potwierdza odznaczenie Głuchowskiego Krzyżem Walecznych — najwyższe polskie odznaczenie bojowe za męstwo.",
        "powiazania": ["ARG/V/118", "ARG/V/96", "ARG/V/97"],
        "stan": "Dobry — tekst czytelny, pieczęć wyraźna"
    },

    # -- Podseria V/AI: Gazety --
    {
        "sygn": "ARG/V/145",
        "photo": "juras_079_page80.png",
        "tytul": "Gazeta 'Życie' Rok I Nr 11 — 14 kwietnia 1946",
        "data": "14.IV.1946",
        "typ": "gazeta",
        "opis_fizyczny": "Strona gazety, druk prasowy, format broadsheet",
        "opis_tresci": "Gazeta 'Życie' Rok I Numer 11, 14 kwietnia 1946. Nagłówki: 'Referendum w czerwcu', 'Sprawa Gen. Małego Michajłowicza w Izbie Gmin', 'Nowa Ofensywa Sowiecka'.",
        "seria": "V",
        "tworca": "redakcja 'Życie'",
        "jezyk": "polski",
        "kontekst": "Prasa polska z 1946 — referenda, polityka brytyjska, polityka sowiecka. Kontekst: Krzysztof czyta prasę polską we Włoszech, rok po wojnie.",
        "powiazania": ["ARG/V/146"],
        "stan": "Średni — papier gazetowy, pożółkły"
    },
    {
        "sygn": "ARG/V/146",
        "photo": "juras_080_page81.png",
        "tytul": "Gazeta 'Życie' — strona kulturalna (Film, Teatr, Muzyka)",
        "data": "14.IV.1946",
        "typ": "gazeta",
        "opis_fizyczny": "Strona wewnętrzna gazety z recenzjami",
        "opis_tresci": "Strona kulturalna 'Życia': FILM, TEATR, MUZYKA. Recenzje: Maurice Chevalier, Greer Garson, 'Zielony Talizman'. Życie kulturalne żołnierzy-emigrantów.",
        "seria": "V",
        "tworca": "redakcja 'Życie'",
        "jezyk": "polski",
        "kontekst": "Życie kulturalne w polskich obozach — kino, teatr, muzyka. Hollywood docierał do żołnierzy przez pokazy filmowe.",
        "powiazania": ["ARG/V/145"],
        "stan": "Średni — papier gazetowy"
    },
    {
        "sygn": "ARG/V/147",
        "photo": "juras_081_page82.png",
        "tytul": "Strona gazetowa — ogłoszenia (kursy językowe, szkoły, Veritas)",
        "data": "lata 50.–60. XX w.",
        "typ": "gazeta",
        "opis_fizyczny": "Strona gazetowa z ogłoszeniami, druk",
        "opis_tresci": "Strona z ogłoszeniami: 'Nowy rok szkolny', 'Krąg za utworzeniem bezatomowej strefy', 'Wiec w Nairobi', 'Kursy języków obcych', 'Złom złoty — złom srebrny — Veritas'. Prasa polonijna lat 50.-60.",
        "seria": "V",
        "tworca": "prasa polonijna",
        "jezyk": "polski",
        "kontekst": "Ogłoszenia prasowe — kursy językowe, reklamy (Veritas = polska firma?), wiadomości międzynarodowe. Codzienność emigranta.",
        "powiazania": [],
        "stan": "Średni — papier gazetowy"
    },

    # -- Podseria V/AJ: Korespondencja z instytucjami --
    {
        "sygn": "ARG/V/148",
        "photo": "juras_082_page83.png",
        "tytul": "Aerogram do gen. Bora-Komorowskiego — HQ Polish Forces, IRELAND",
        "data": "lata 40.–50. XX w.",
        "typ": "aerogram",
        "opis_fizyczny": "Aerogram (BY AIR MAIL, Air Letter), stempel pocztowy",
        "opis_tresci": "Aerogram (BY AIR MAIL, Air Letter) Nr 563. Adresat: 'General de dywizji / Tadeusz Bor Komorowski / H.Q. Polish Forces 25 / ENGLAND'. Adnotacja: 'Written in Polish'. Stempel pocztowy. Korespondencja st.uł. Krzysztofa Głuchowskiego z dowódcą Powstania Warszawskiego gen. Tadeuszem Borem-Komorowskim.",
        "seria": "V",
        "tworca": "Krzysztof Andrzej Głuchowski (?)",
        "jezyk": "polski",
        "kontekst": "KORESPONDENCJA Z BOR-KOMOROWSKIM — dowódcą Powstania Warszawskiego, w którym Krzysztof walczył. Bór-Komorowski po wojnie w Irlandii (Buckinghamshire / Kinross, potem Londyn). Niezwykły dokument relacji żołnierz-dowódca.",
        "powiazania": ["ARG/V/149", "ARG/V/118"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/V/149",
        "photo": "juras_083_page84.png",
        "tytul": "Treść aerogramu — list nr 563, historia Pułku 1112, Polish Institute",
        "data": "lata 40.–50. XX w.",
        "typ": "aerogram",
        "opis_fizyczny": "Treść aerogramu, pismo ręczne, gęsty tekst",
        "opis_tresci": "Treść aerogramu nr 563 na papierze Polish Institute and Sikorski Museum. Nadawca: st.uł. Krzysztof Głuchowski, Polskie Siły CMF 18, 3 DSK. Data: Myszków 14.VIII.45r. List osobisty od żołnierza do generała — Krzysztof pisze o pamięci poległych, historii pułku. Wspomina datę 18 lipca tego roku i wydarzenia z Powstania. Gęsty tekst odręczny na jednej stronie aerogramu.",
        "seria": "V",
        "tworca": "Krzysztof Andrzej Głuchowski",
        "jezyk": "polski",
        "kontekst": "Polish Institute and Sikorski Museum (Londyn) = główne archiwum PSZ na emigracji. Pułk 1112 = prawdopodobnie oznaczenie konspiracyjne 7 P.Uł. w AK. List dotyczy prac historycznych nad dziejami pułku.",
        "powiazania": ["ARG/V/148", "ARG/V/150"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/V/150",
        "photo": "juras_084_page85.png",
        "tytul": "Pismo z Polish Institute and Sikorski Museum — potwierdzenie otrzymania dokumentów",
        "data": "lata 50.–60. XX w.",
        "typ": "pismo urzędowe",
        "opis_fizyczny": "Maszynopis na papierze firmowym Polish Institute and Sikorski Museum, Londyn. Format A4, jedna strona. Nagłówek drukowany: 'POLISH INSTITUTE AND SIKORSKI MUSEUM' z adresem w Londynie. Tekst maszynowy, podpis na dole. Papier cienki, lekko pofałdowany.",
        "opis_tresci": "Pismo urzędowe z Polish Institute and Sikorski Museum w Londynie — potwierdzenie otrzymania dokumentów przekazanych przez Krzysztofa Głuchowskiego do archiwum Instytutu. Odniesienia do materiałów dotyczących 7 Pułku Ułanów Lubelskich i/lub Powstania Warszawskiego. Wzmianka o roku 1945. Podpis urzędowy na dole dokumentu. Serdeczne podziękowanie za nadesłane dokumenty.",
        "seria": "V",
        "tworca": "Polish Institute and Sikorski Museum",
        "jezyk": "angielski, polski",
        "kontekst": "Krzysztof współpracował z Polish Institute w Londynie w sprawie dokumentacji historii pułku i Powstania.",
        "powiazania": ["ARG/V/149"],
        "stan": "Dobry"
    },

    # -- Podseria V/AK: Wspomnienia rękopiśmienne --
    {
        "sygn": "ARG/V/151",
        "photo": "juras_085_page86.png",
        "tytul": "Wspomnienia rękopiśmienne — str. 1 (stosunki polsko-żydowskie)",
        "data": "lata 50.–60. XX w.",
        "typ": "wspomnienia",
        "opis_fizyczny": "Rękopis na papierze, gęste pismo atramentem, str. 1-2",
        "opis_tresci": "Wspomnienia rękopiśmienne — str. 1-2: refleksje na temat stosunków polsko-żydowskich. Gęsty rękopis, ton analityczny.",
        "seria": "V",
        "tworca": "Krzysztof Andrzej Głuchowski",
        "jezyk": "polski",
        "kontekst": "Wspomnienia pisane z perspektywy emigranta — refleksja nad trudnymi tematami polskiej historii. Unikatowe świadectwo.",
        "powiazania": ["ARG/V/152", "ARG/V/153", "ARG/V/154", "ARG/V/155", "ARG/V/156"],
        "stan": "Średni — rękopis, atrament wyblakły"
    },
    {
        "sygn": "ARG/V/152",
        "photo": "juras_086_page87.png",
        "tytul": "Wspomnienia — str. 2 (przedwojenny Kraków, 1918)",
        "data": "lata 50.–60. XX w.",
        "typ": "wspomnienia",
        "opis_fizyczny": "Rękopis kontynuacja, gęste pismo",
        "opis_tresci": "Kontynuacja wspomnień. Odczytuję fragmenty: 'Proszę przedstawić następujące kwestie...' — wymienia Marszałka [Piłsudskiego?], Stefana Głuchowskiego, odwołania do 1918 roku i odzyskania niepodległości. Wspomina o Marszałku Piłsudskim. Tekst historyczno-rodzinny — prawdopodobnie przygotowanie do wspomnień lub artykułu o roli rodziny Głuchowskich w dziejach niepodległości.",
        "seria": "V",
        "tworca": "Krzysztof Andrzej Głuchowski",
        "jezyk": "polski",
        "kontekst": "Wspomnienia sięgają okresu sprzed narodzin autora (1918) — prawdopodobnie oparte na opowieściach rodzinnych. Głuchowscy mieli silne związki z Krakowem.",
        "powiazania": ["ARG/V/151", "ARG/V/153"],
        "stan": "Średni"
    },
    {
        "sygn": "ARG/V/153",
        "photo": "juras_087_page88.png",
        "tytul": "Wspomnienia — str. 3 (Bahia/Salvador 1949-50, emigracja do Brazylii)",
        "data": "lata 50.–60. XX w.",
        "typ": "wspomnienia",
        "opis_fizyczny": "Rękopis, gęste pismo atramentem",
        "opis_tresci": "Wspomnienia o Bahia/Salvador 1949-50 — szkoła, Brazylia, warunki życia emigranta, codzienność w tropikach. Opis pierwszych lat w Ameryce Południowej.",
        "seria": "V",
        "tworca": "Krzysztof Andrzej Głuchowski",
        "jezyk": "polski",
        "kontekst": "KLUCZOWE WSPOMNIENIA — jedyny znany opis emigracji Krzysztofa do Brazylii. Salvador da Bahia — port, pierwszy etap osiedlenia w Brazylii.",
        "powiazania": ["ARG/V/151", "ARG/V/154", "ARG/V/68"],
        "stan": "Średni"
    },
    {
        "sygn": "ARG/V/154",
        "photo": "juras_088_page89.png",
        "tytul": "Wspomnienia — str. 4 (warunki emigrantów, 3500 robotników)",
        "data": "lata 50.–60. XX w.",
        "typ": "wspomnienia",
        "opis_fizyczny": "Rękopis kontynuacja",
        "opis_tresci": "Kontynuacja wspomnień: sytuacja emigrantów, utrzymanie, pieniądze, warunki, 3500 robotników, zakłady. Opis polskiej kolonii w Brazylii.",
        "seria": "V",
        "tworca": "Krzysztof Andrzej Głuchowski",
        "jezyk": "polski",
        "kontekst": "Dane o polskiej emigracji do Brazylii — 3500 robotników wskazuje na zorganizowaną emigrację zarobkową. Cenne źródło do historii Polonii brazylijskiej.",
        "powiazania": ["ARG/V/153", "ARG/V/155"],
        "stan": "Średni"
    },
    {
        "sygn": "ARG/V/155",
        "photo": "juras_089_page90.png",
        "tytul": "Wspomnienia — str. 5 (alianci, radio, organizacje polonijne)",
        "data": "lata 50.–60. XX w.",
        "typ": "wspomnienia",
        "opis_fizyczny": "Rękopis kontynuacja",
        "opis_tresci": "Kontynuacja: zachodni alianci, radio, organizacje polonijne, partie polityczne, Europa. Refleksje nad geopolityką i Polonią.",
        "seria": "V",
        "tworca": "Krzysztof Andrzej Głuchowski",
        "jezyk": "polski",
        "kontekst": "Perspektywa emigranta na politykę światową — radio (BBC? Radio Wolna Europa?) jako okno na świat. Organizacje polonijne w Brazylii.",
        "powiazania": ["ARG/V/154", "ARG/V/156"],
        "stan": "Średni"
    },
    {
        "sygn": "ARG/V/156",
        "photo": "juras_090_page91.png",
        "tytul": "Wspomnienia — str. 6 (zakończenie)",
        "data": "lata 50.–60. XX w.",
        "typ": "wspomnienia",
        "opis_fizyczny": "Ostatnia strona rękopisu",
        "opis_tresci": "Ostatnia strona wspomnień — zakończenie narracji. Podsumowanie doświadczeń emigranta.",
        "seria": "V",
        "tworca": "Krzysztof Andrzej Głuchowski",
        "jezyk": "polski",
        "kontekst": "Zamknięcie cyklu wspomnień — od przedwojennego Krakowa przez Powstanie, obozy, emigrację do Brazylii. Unikatowy dokument.",
        "powiazania": ["ARG/V/151", "ARG/V/155"],
        "stan": "Średni"
    },

    # =====================================================================
    # SERIA VI — VARIA / RODZINA
    # =====================================================================
    {
        "sygn": "ARG/VI/1",
        "photo": "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p04_img01.jpeg",
        "tytul": "Tablica pamiątkowa natarcia 7 P.Uł. AK 'JELEŃ' na gmach Gestapo i Dom Prasy — 1.VIII.1944 godz. 17:00",
        "data": "1.VIII.1944",
        "typ": "fotografia tablicy pamiątkowej",
        "opis_fizyczny": "Fotografia maszynopisu/druku pamiątkowego na białym/kremowym papierze, format ok. 15×15 cm. Tekst maszynowy ułożony centrycznie. Papier lekko pożółkły. Zdjęcie ostre, czytelne.",
        "opis_tresci": "'Dnia 1.8.1944 r. godz. 17. / z tego domu i okolicznych / ruszyło do natarcia / na gmach Gestapo i Dom Prasy / 5 plutonów / 7 pułku ułanów / AK / «JELEŃ» / z / 187 Powstańców / poległo 67 / Cześć Ich pamięci.' Tekst tablicy upamiętniającej natarcie 5 plutonów 7 Pułku Ułanów AK 'Jeleń' na gmach Gestapo (Al. Szucha) i Dom Prasy w WARSZAWIE w dniu wybuchu Powstania Warszawskiego, o godzinie 'W' (17:00). Z 187 powstańców poległo 67 — ponad jedna trzecia.",
        "seria": "VI",
        "tworca": "nieznany (druk pamiątkowy, prawdopodobnie pow. 1945)",
        "jezyk": "polski",
        "kontekst": "KLUCZOWY DOKUMENT PAMIĘCI — upamiętnia najkrwawszą akcję 7 P.Uł. AK 'Jeleń' w godzinie 'W' Powstania Warszawskiego (1.VIII.1944, godz. 17:00). Natarcie na gmach Gestapo przy Al. Szucha i Dom Prasy (ul. Marszałkowska 3/5) w WARSZAWIE (NIE w Krakowie!). 36% strat (67 z 187). W tych 5 plutonach służył Krzysztof 'Juraś' Głuchowski — ten dokument jest bezpośrednim świadectwem jego udziału w Powstaniu. Lech Głuchowski (stryj Krzysztofa) dowodził natarciem na Al. Szucha i poległ na Mokotowie 15.IX.1944.",
        "powiazania": ["ARG/V/3"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/VI/2",
        "photo": "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p10_img01.jpeg",
        "tytul": "Krzyż Walecznych — fizyczne odznaczenie z wstążką, napis 'NA POLU CHWAŁY 1920'",
        "data": "1920",
        "typ": "odznaczenie (artefakt)",
        "opis_fizyczny": "Fotografia kolorowa fizycznego odznaczenia. Krzyż brązowy/patynowany na wstążce biało-czerwono-białej (paski: bordowy-kremowy-bordowy-kremowy-bordowy). Krzyż z czterema równymi ramionami, napis na ramionach: 'NA POLU CHWAŁY' (na górnym i bocznych) i '1920' (na dolnym). W centrum — rozeta/gwiazdka z promieni. Wymiary krzyża ok. 4×4 cm. Wstążka złożona w kształt litery V.",
        "opis_tresci": "Fizyczny egzemplarz Krzyża Walecznych z kampanii 1920 roku (wojna polsko-bolszewicka). Napis na ramionach krzyża: 'NA POLU CHWAŁY 1920'. Wstążka w barwach Virtuti Militari (bordowo-kremowa). Krzyż Walecznych — jedno z najwyższych polskich odznaczeń bojowych za męstwo na polu walki.",
        "seria": "VI",
        "tworca": "Mennica Państwowa RP",
        "jezyk": "—",
        "kontekst": "FIZYCZNY ARTEFAKT — nie tylko dokument, ale rzeczywiste odznaczenie bojowe. Krzyż Walecznych z 1920 r. — prawdopodobnie egzemplarz nadany Januszowi Głuchowskiemu za udział w wojnie polsko-bolszewickiej (walki kawaleryjskie 1920). KW nadawany w rodzinie Głuchowskich wielokrotnie: Januszowi (1920/1922), Lechowi (trzykrotnie!), Krzysztofowi (1944). Ten fizyczny egzemplarz zachowany w kolekcji — jedna z najcenniejszych pozycji.",
        "powiazania": ["ARG/II/13", "ARG/V/42"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/VI/3",
        "photo": "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p23_img01.jpeg",
        "tytul": "Galony i wstążki orderowe",
        "data": "1939–1945",
        "typ": "militaria",
        "opis_fizyczny": "Trzy elementy mundurowe sfotografowane na jasnym tle",
        "opis_tresci": "Galony (oznaki stopnia), wstążki orderowe. Elementy umundurowania oficera lub podoficera WP.",
        "seria": "VI",
        "tworca": "Wojsko Polskie",
        "jezyk": "—",
        "kontekst": "Militaria — mogą należeć do dowolnego z mężczyzn w rodzinie.",
        "powiazania": ["ARG/V/3"],
        "stan": "Średni"
    },
    {
        "sygn": "ARG/VI/4",
        "photo": "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p28_img03.jpeg",
        "tytul": "Album fotograficzny — okładka z dedykacją (8.III.1944)",
        "data": "8.III.1944",
        "typ": "album",
        "opis_fizyczny": "Czarna okładka albumu z białym napisem kaligrafowanym",
        "opis_tresci": "'Panu Gen. Głuchowskiemu, Dowódcy Jedn. Wojsk w Brytanii, z okazji pobytu na Wyszkoleniu, Żołnierze Kompanii Dowodzenia, 8 marca 1944.' Album upominkowy.",
        "seria": "VI",
        "tworca": "Żołnierze Kompanii Dowodzenia",
        "jezyk": "polski",
        "kontekst": "Album upominkowy od żołnierzy dla generała — tradycyjna forma hołdu. 8.III.1944 = w Wielkiej Brytanii.",
        "powiazania": ["ARG/VI/5", "ARG/VI/6"],
        "stan": "Dobry — oprawa"
    },
    {
        "sygn": "ARG/VI/5",
        "photo": "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p28_img01.jpeg",
        "tytul": "Album fotograficzny — strona z 4 zdjęciami (1)",
        "data": "ok. 1944",
        "typ": "album",
        "opis_fizyczny": "Strona albumu na czarnym kartonie, 4 fotografie grupowe naklejone",
        "opis_tresci": "4 zdjęcia z życia obozowego/wojskowego. Podpisy: 'po ćwiczeniach sportowych ustawień dawag...' Fotografie grupowe żołnierzy.",
        "seria": "VI",
        "tworca": "żołnierze PSZ",
        "jezyk": "polski",
        "kontekst": "Album z życia codziennego żołnierzy PSZ w Wielkiej Brytanii.",
        "powiazania": ["ARG/VI/4"],
        "stan": "Średni — fotografie wyblakłe"
    },
    {
        "sygn": "ARG/VI/6",
        "photo": "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p28_img02.jpeg",
        "tytul": "Album fotograficzny — strona z 4 zdjęciami (2)",
        "data": "ok. 1944",
        "typ": "album",
        "opis_fizyczny": "Kolejna strona albumu, 4 fotografie",
        "opis_tresci": "4 zdjęcia grupowe żołnierzy, w tym zdjęcie z gitarą. Scenki z życia obozowego/koszarowego.",
        "seria": "VI",
        "tworca": "żołnierze PSZ",
        "jezyk": "polski",
        "kontekst": "Kolejna strona albumu żołnierskiego PSZ — sceny z życia codziennego, gitara.",
        "powiazania": ["ARG/VI/4"],
        "stan": "Średni"
    },
    {
        "sygn": "ARG/VI/7",
        "photo": "Kolekcja_Gluchowski_Katalog_Tematyczny_p15_img02.jpeg",
        "tytul": "Dwie legitymacje pułkowe",
        "data": "1946",
        "typ": "leg",
        "opis_fizyczny": "Dwie małe legitymacje sfotografowane razem",
        "opis_tresci": "(1) St.ułan Głuchowski Krzysztof — odznaka pamiątkowa 7 P.Uł. Lubelskich, 23.III.1946. (2) Gen.Brygad. Głuchowski Janusz — Znak pułkowy 20 P.Uł., Rzeszów.",
        "seria": "VI",
        "tworca": "7 P.Uł. / 20 P.Uł.",
        "jezyk": "polski",
        "kontekst": "Dwa pokolenia — stryj i bratanek — w dwóch pułkach ułanów. Ciągłość tradycji kawaleryjskiej.",
        "powiazania": ["ARG/II/8", "ARG/V/54"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/VI/8",
        "photo": "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p20_img01.jpeg",
        "tytul": "Zaproszenie na mszę rocznicową za poległych żołnierzy AK 'JELEŃ' — Wilanów, 4.X.1970",
        "data": "4.X.1970",
        "typ": "druk okolicznościowy",
        "opis_fizyczny": "Druk maszynowy na żółtawym papierze, mały format (ok. 10×15 cm). Tekst centrycznie złożony. Papier pożółkły.",
        "opis_tresci": "'Dnia 4-go października 1970 r. /niedziela/ o godz. 10-ej w kościele św. [...] w Wilanowie będzie odprawiona doroczna Msza św. za poległych w czasie okupacji i Powstania Warszawskiego / ŻOŁNIERZY PUŁKU AK «JELEŃ» / Po mszy, zostaną złożone kwiaty na miejscowym cmentarzu — na mogile żołnierzy «Jelenia», poległych na Sadybie. / Rodziny i Towarzysze Broni. / Po złożeniu kwiatów na cmentarzu — kto będzie chciał — może wziąć udział we wspólnym śniadaniu w miejscowej restauracji «Kuźnia».' Zaproszenie na doroczną mszę i złożenie kwiatów.",
        "seria": "VI",
        "tworca": "Rodziny i Towarzysze Broni żołnierzy AK 'Jeleń'",
        "jezyk": "polski",
        "kontekst": "Doroczna msza za poległych żołnierzy 7 P.Uł. AK 'Jeleń' — Wilanów, październik 1970, 26 lat po Powstaniu. Groby żołnierzy 'Jelenia' na cmentarzu w Wilanowie — poległych na Sadybie (dzielnica południowej Warszawy). Fakt odprawiania mszy w PRL (1970) świadczy o ODWADZE kombatantów — w komunistycznej Polsce AK było marginalizowane i prześladowane. Restauracja 'Kuźnia' w Wilanowie = miejsce spotkań kombatanckich. Dokument zachowany w kolekcji Krzysztofa (w Brazylii) — ktoś musiał mu go przesłać pocztą.",
        "powiazania": ["ARG/II/8"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/VI/9",
        "photo": "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p21_img01.jpeg",
        "tytul": "Nekrolog plut. Jana Lorensa — 7 P.Uł., prezes sekcji Koła pułkowego, Chicago 28.I.1960",
        "data": "28.I.1960",
        "typ": "nekrolog",
        "opis_fizyczny": "Nekrolog prasowy (wycinek), format ok. 8×4 cm. Druk żałobny z krzyżykiem na górze ('Ś. † P.'). Tekst drukowany, na dole: 'KOŁO ŻOŁNIERZY 7 PUŁKU UŁANÓW LUBELSKICH / IM. GEN. K. SOSNKOWSKIEGO' i numer 8669.",
        "opis_tresci": "'Ś. † P. / JAN LORENS / plutonowy 7 pułku ułanów, prezes sekcji Koła pułkowego; czynny członek wielu organizacji niepodległościowych w Chicago, odznaczony Krzyżem Walecznych i innymi odznaczeniami polskimi i zagranicznymi, zmarł 28 stycznia 1960 w Chicago. / Cześć Jego pamięci! / KOŁO ŻOŁNIERZY 7 PUŁKU UŁANÓW LUBELSKICH / IM. GEN. K. SOSNKOWSKIEGO'.",
        "seria": "VI",
        "tworca": "Koło Żołnierzy 7 Pułku Ułanów Lubelskich im. Gen. K. Sosnkowskiego",
        "jezyk": "polski",
        "kontekst": "Ślad diasporowy — żołnierze 7 P.Uł. rozproszeni po świecie (Chicago, Londyn, Brazylia). Jan Lorens — plutonowy 7 P.Uł., prezes sekcji Koła pułkowego w Chicago, odznaczony KW. Zmarł 28.I.1960 w Chicago. Koło Żołnierzy 7 P.Uł. im. Gen. Sosnkowskiego — organizacja kombatancka podtrzymująca pamięć pułku na emigracji. Nekrolog zachowany przez Krzysztofa — dowód na sieć kontaktów pomiędzy weteranami 'Jelenia' na trzech kontynentach.",
        "powiazania": ["ARG/VI/8"],
        "stan": "Dobry"
    },

    # -- Getto łódzkie --
    {
        "sygn": "ARG/VI/10",
        "photo": "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p17_img01.jpeg",
        "tytul": "List K. Głuchowskiego do Ambasady Izraela — oferta sprzedaży walut i monet getta łódzkiego, 13.V.1958",
        "data": "13.V.1958",
        "typ": "list",
        "opis_fizyczny": "Maszynopis na papierze korespondencyjnym, jedna strona. Adres nadawcy: '42, Emperors Gate, London S.W.7'. Data: '13th May, 1958'. Adresat: 'The Israel Embassy, Public Relations Office, 2, Palace Green, London W.8.' Podpis maszynowy: 'K. Głuchowski.' Papier kremowy, czytelny.",
        "opis_tresci": "'Dear Sir, / I am contemplating sale of my complete set of paper currency and coins issued in Lodz ghetto during the german occupation of Poland. / The above set is of great rarity and museal value, and I wonder if some institution in Israel would not be interested in purchase. / Hoping that you will be able to assist me in this matter, I remain, Sir, / yours faithfully, / K. Głuchowski.' List w języku angielskim z propozycją sprzedaży kompletnego zestawu banknotów i monet wydanych w getcie łódzkim.",
        "seria": "VI",
        "tworca": "K. Głuchowski (prawdopodobnie gen. Janusz — adres Emperors Gate = jego londyński adres)",
        "jezyk": "angielski",
        "kontekst": "FASCYNUJĄCY DOKUMENT — gen. Janusz Głuchowski (lub Krzysztof?) posiadał KOMPLETNY ZESTAW walut getta łódzkiego (Litzmannstadt Ghetto, 1940-1944). Waluty gettowe Chaima Rumkowskiego — dziś ekstremalnie rzadkie numizmaty (wartość na aukcjach: kilkanaście-kilkadziesiąt tysięcy złotych za zestaw). Adres '42, Emperors Gate, London SW7' — znany londyński adres gen. Janusza (potwierdzony w Aliens Registration ARG/II/65). Fakt posiadania walut gettowych przez polskiego generała sugeruje, że mógł je zdobyć/otrzymać w czasie wojny lub tuż po niej. List do Ambasady Izraela — próba sprzedaży instytucji muzealnej w Izraelu (1958 = 10 lat po powstaniu Państwa Izrael). Data w katalogu była 18.V.1958, ale na dokumencie widać '13th May' — korekta daty.",
        "powiazania": ["ARG/VI/11", "ARG/VI/12"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/VI/11",
        "photo": "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p17_img02.jpeg",
        "tytul": "Pieniądze getta łódzkiego — bon, talon, koperta",
        "data": "1940–1944",
        "typ": "numizmat",
        "opis_fizyczny": "Trzy przedmioty sfotografowane razem: bon papierowy, talon kartonowy, koperta",
        "opis_tresci": "Bon 10 Pfennig getta łódzkiego (Litzmannstadt), talon na produkty mleczne (Molkereierzeugnisse), koperta.",
        "seria": "VI",
        "tworca": "Ältester der Juden in Litzmannstadt",
        "jezyk": "niemiecki",
        "kontekst": "Numizmaty gettowe — emitowane przez Judenrat getta łódzkiego. Bon 10 Pf. i talon mleczny — waluta wewnętrzna getta. Wartość kolekcjonerska i historyczna.",
        "powiazania": ["ARG/VI/10"],
        "stan": "Średni — papier kruchy"
    },
    {
        "sygn": "ARG/VI/12",
        "photo": "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p17_img03.jpeg",
        "tytul": "Odpowiedź Ambasady Izraela — sugestia Yad Vashem",
        "data": "22.V.1958",
        "typ": "list",
        "opis_fizyczny": "Pismo urzędowe Ambasady Izraela",
        "opis_tresci": "List z Ambasady Izraela do Krzysztofa Głuchowskiego z sugestią kontaktu z Yad Vashem w sprawie walut gettowych.",
        "seria": "VI",
        "tworca": "Ambasada Izraela w Warszawie",
        "jezyk": "polski",
        "kontekst": "Odpowiedź dyplomatyczna — Ambasada kieruje do Yad Vashem (Instytut Pamięci Męczenników i Bohaterów Holocaustu).",
        "powiazania": ["ARG/VI/10", "ARG/VI/11"],
        "stan": "Dobry"
    },

    # -- Fotografie obozowe --
    {
        "sygn": "ARG/VI/13",
        "photo": "Seria_29z_p09_img01.jpeg",
        "tytul": "Trzy fotografie obozowe",
        "data": "1944–1945",
        "typ": "foto",
        "opis_fizyczny": "Trzy małe fotografie czarno-białe sfotografowane razem",
        "opis_tresci": "Trzy małe fotografie: widoki budynków/osiedli, prawdopodobnie Fallingbostel lub okolice obozu. Budynek mieszkalny, aleja z drzewami, brama wjazdowa.",
        "seria": "VI",
        "tworca": "nieznany",
        "jezyk": "—",
        "kontekst": "Dokumentacja wizualna okolic obozu Stalag XI B (Fallingbostel) lub Stalagu VI.",
        "powiazania": ["ARG/V/9"],
        "stan": "Średni — małe formaty"
    },

    # -- Naukowy p19 = duplikat p04 (tablica), pomijam --
    # -- Tematyczny p15_img03 = duplikat p12_img03 (KW), pomijam --
    # -- Naukowy p14_img03 = duplikat p09 (list z Londynu?), weryfikacja --

    # -- Biogramy rodzinne (kontynuacja) --
    {
        "sygn": "ARG/VI/14",
        "photo": "juras_092_page93.png",
        "tytul": "KWARTALNIK BIOGRAFICZNY POLONII Nr 7 — biogramy Krzysztofa Głuchowskiego i Janusza Głuchowskiego (kontynuacja)",
        "data": "lata 60.–70. XX w.",
        "typ": "biogram",
        "opis_fizyczny": "Strona z Kwartalnika Biograficznego Polonii Nr 7. Druk dwukolumnowy ze zdjęciami portretowymi. Cztery małe fotografie przy biogramach. Format A4. Nagłówek: 'KWARTALNIK BIOGRAFICZNY POLONII Nr 7'.",
        "opis_tresci": "Kontynuacja biogramów z Kwartalnika Biograficznego Polonii Nr 7. Biogram KRZYSZTOFA GŁUCHOWSKIEGO: ur. 29.XI.1926 Warszawa. AK — 7 P.Uł. Lubelskich 'Jeleń', Powstanie Warszawskie 1944, jeniec Stalag, 3 DSK we Włoszech, studia South West Essex Technical College, emigracja do Brazylii (Rio de Janeiro), inżynier. Odznaczenia: Krzyż Walecznych, Krzyż Armii Krajowej Nr 3316, Medal Wojska, British War Medal. Także kontynuacja biogramu gen. Janusza i biogram aktora Grochulskiego Czesława ze zdjęciami.",
        "seria": "VI",
        "tworca": "Kwartalnik Biograficzny Polonii",
        "jezyk": "polski",
        "kontekst": "DRUGIE KLUCZOWE ŹRÓDŁO — publikowany biogram Krzysztofa z pełną chronologią: AK → Powstanie → Stalag → 3 DSK → studia w Anglii → Brazylia → inżynier. Potwierdza wszystkie odznaczenia i przydział. Kwartalnik Biograficzny Polonii = encyklopedia wybitnych Polaków na emigracji.",
        "powiazania": ["ARG/II/33", "ARG/II/1"],
        "stan": "Dobry"
    },

    # =====================================================================
    # NOWE OBIEKTY Z KATALOGU AUKCYJNEGO (leiloesbr.com.br) — 2026-03-21
    # =====================================================================

    # --- Seria II: Gen. dyw. Janusz Julian Głuchowski ---

    {
        "sygn": "ARG/II/34",
        "photo": "lbr_II_34_p01.jpg",
        "tytul": "Czarny beret pancerny Wojska Polskiego ze śladem po kuli — z kolekcji gen. Głuchowskiego",
        "data": "lata 40. XX w.",
        "typ": "militaria",
        "opis_fizyczny": "Beret czarny z grubego filcu, wykończenie skórzane, przelotki boczne, podszewka w dobrym stanie. Na froncie insygnia metalowa (orzeł pancerny). ŚLAD PO KULI widoczny na berecie — uszkodzenie bojowe. 5 zdjęć.",
        "opis_tresci": "Beret pancerny z kolekcji rodzinnej gen. Janusza Głuchowskiego, ze śladem po kuli. Proweniencja śladu wymaga dalszych badań — Głuchowski w II wojnie pełnił funkcje dowódcze w Wielkiej Brytanii (Dowódca JWWB od IX.1943), nie na froncie włoskim.",
        "seria": "II",
        "tworca": "Wojsko Polskie",
        "jezyk": "n/a",
        "kontekst": "Beret pancerny gen. Głuchowskiego z okresu służby w Wielkiej Brytanii (1941-1945). Czarne berety w WP wprowadzono ok. 1937-1942 dla jednostek pancernych — nie istniały w I wojnie światowej ani w 1920 r. Głuchowski był Dowódcą JWWB (od IX.1943) i dowódcą Brygady Szkolnej w Szkocji (1941-1943). ŚLAD PO KULI — proweniencja wymaga dalszej kwerendy: możliwe naloty Luftwaffe na bazy w Szkocji, incydent szkoleniowy lub inna sytuacja bojowa. Głuchowski miał trzy Krzyże Walecznych, co świadczy o trzykrotnym wykazaniu się odwagą pod ogniem. Beret ze śladem po kuli — unikatowa relikwia, fizyczny dowód zagrożenia życia generała. Powiązany z albumem 'Żołnierz z Montecassino' z dedykacją gen. Andersa (ARG/II/54).",
        "powiazania": ["ARG/II/54", "ARG/II/48", "ARG/II/49", "ARG/II/50"],
        "stan": "Ślad po kuli, drobne ubytki — uszkodzenie bojowe"
    },
    {
        "sygn": "ARG/II/35",
        "photo": "lbr_II_35_p01.jpg",
        "tytul": "Legitymacja osobista gen. Janusza Juliana Głuchowskiego — Ministerstwo Spraw Wojskowych II RP",
        "data": "ok. 1928–1934",
        "typ": "legitymacja",
        "opis_fizyczny": "Legitymacja osobista wystawiona przez Ministerstwo Spraw Wojskowych II RP, format dokumentu tożsamości, ze zdjęciem, pieczęciami i podpisami. 5 zdjęć.",
        "opis_tresci": "Dokument tożsamości wojskowej gen. bryg. Janusza Juliana Głuchowskiego z okresu służby w Ministerstwie Spraw Wojskowych. Zdjęcie legitymacyjne, dane personalne, pieczęcie ministerstwa.",
        "seria": "II",
        "tworca": "Ministerstwo Spraw Wojskowych II RP",
        "jezyk": "polski",
        "kontekst": "Głuchowski był I Wiceministrem Spraw Wojskowych (1935-1939). Legitymacja z wcześniejszego okresu (1928-1934), gdy pełnił funkcje dowódcze. Dokumenty tożsamości generałów II RP — rzadkość na rynku, kluczowy dokument identyfikacyjny.",
        "powiazania": ["ARG/II/18", "ARG/II/19", "ARG/II/34"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/II/36",
        "photo": "lbr_II_36_p01.jpg",
        "tytul": "List rękopiśmienny Adama Piłsudskiego do gen. Głuchowskiego",
        "data": "1931",
        "typ": "list",
        "opis_fizyczny": "List rękopiśmienny, jedna strona, na papeterii z monogramem, datowany 1931. Adresowany do płk. Janusza Głuchowskiego. 4 zdjęcia.",
        "opis_tresci": "List pisany odręcznie przez Adama Piłsudskiego (bratanka Marszałka Józefa Piłsudskiego) do ówczesnego pułkownika Głuchowskiego. Treść osobista/służbowa z 1931 roku.",
        "seria": "II",
        "tworca": "Adam Piłsudski",
        "jezyk": "polski",
        "kontekst": "Adam Piłsudski (1869–1935) — starszy brat Marszałka Józefa Piłsudskiego, inżynier kolejowy. List z 1931 r. do Głuchowskiego (wówczas pułkownika, dowódcy 1. Pułku Ułanów) świadczy o bliskich relacjach Głuchowskiego z rodziną Piłsudskich — naturalnych, biorąc pod uwagę że obaj byli Legionistami z 1914 roku. Autograf Piłsudskiego — wysoka wartość kolekcjonerska.",
        "powiazania": ["ARG/II/17", "ARG/II/1"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/II/37",
        "photo": "lbr_II_37_p01.jpg",
        "tytul": "Zestaw fotograficzny — Mauzoleum Woli, Pole Mokotowskie, Al. Szucha — podróż pamięci gen. Głuchowskiego",
        "data": "lata 50.–60. XX w.",
        "typ": "fotografia",
        "opis_fizyczny": "Dwie strony albumu z oryginalnymi fotografiami czarno-białymi, z maszynowymi podpisami. 5 zdjęć.",
        "opis_tresci": "Dokumentacja zbiórki ziemi z trzech miejsc martyrologii Warszawy: Mauzoleum-Cmentarz Woli, Pola Mokotowskiego i Al. Szucha (siedziba Gestapo). Gen. Głuchowski (na emigracji w Londynie) zbierał ziemię z miejsc pamięci.",
        "seria": "II",
        "tworca": "nieznany fotograf",
        "jezyk": "polski",
        "kontekst": "Rytuał zbierania ziemi z miejsc pamięci — typowy dla polskiej emigracji londyńskiej. Głuchowski, jako generał na Uchodźstwie, pielęgnował pamięć o Powstaniu Warszawskim. Wola, Mokotów i Al. Szucha — trzy symbole terroru okupacyjnego.",
        "powiazania": ["ARG/II/40", "ARG/V/9"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/II/38",
        "photo": "lbr_II_38_p01.jpg",
        "tytul": "Fotografia — gen. Głuchowski wręcza odznaczenia żołnierzom, Szkocja 1941",
        "data": "1941",
        "typ": "fotografia",
        "opis_fizyczny": "Fotografia czarno-biała, z kolekcji osobistej gen. Głuchowskiego. 2 zdjęcia.",
        "opis_tresci": "Gen. Głuchowski podczas przeglądu i uroczystego wręczania odznaczeń szeregowym oficerów i kadetów Wojska Polskiego na emigracji w Szkocji, 1941.",
        "seria": "II",
        "tworca": "fotograf wojskowy",
        "jezyk": "n/a",
        "kontekst": "Głuchowski jako Zastępca Dowódcy Armii Polskiej w Szkocji odpowiadał za morale i ceremoniał. Szkocja 1941 — okres organizacji polskich sił zbrojnych na Zachodzie po klęsce Francji (1940).",
        "powiazania": ["ARG/II/39", "ARG/II/47"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/II/39",
        "photo": "lbr_II_39_p01.jpg",
        "tytul": "Fotografia — gen. Głuchowski wśród oficerów polskich, Podchorążówka, Szkocja",
        "data": "lata 40. XX w.",
        "typ": "fotografia",
        "opis_fizyczny": "Oryginalna fotografia wielkoformatowa, czarno-biała. 2 zdjęcia.",
        "opis_tresci": "Grupowe zdjęcie gen. Głuchowskiego z kompletną grupą oficerów i podchorążych w Szkocji. Podchorążówka = Szkoła Podchorążych na emigracji.",
        "seria": "II",
        "tworca": "fotograf wojskowy",
        "jezyk": "n/a",
        "kontekst": "Szkoły Podchorążych na emigracji w Szkocji kształciły nowe kadry oficerskie dla Wojska Polskiego. Głuchowski jako wysoki dowódca wizytował te szkoły regularnie. Zdjęcie grupowe z kadrą i kursantami — dokumentacja szkolnictwa wojskowego na Uchodźstwie.",
        "powiazania": ["ARG/II/38", "ARG/II/47"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/II/40",
        "photo": "lbr_II_40_p01.jpg",
        "tytul": "Zestaw fotograficzny — restauracja grobu powstańczego, Jele, AK 1944",
        "data": "lata 50.–60. XX w.",
        "typ": "fotografia",
        "opis_fizyczny": "Strona albumu z dwiema oryginalnymi fotografiami czarno-białymi i podpisami maszynowymi. 2 zdjęcia.",
        "opis_tresci": "Wstępny etap prac nad rekonstrukcją nagrobka poświęconego Dywizji AK w Jele. Dokumentacja projektu restauracji grobu powstańczego z 1944 roku.",
        "seria": "II",
        "tworca": "nieznany fotograf",
        "jezyk": "polski",
        "kontekst": "Pamięć o Armii Krajowej i Powstaniu 1944 pielęgnowana na emigracji. Jele — miejsce walk partyzanckich. Głuchowski jako generał na emigracji w Londynie wspierał inicjatywy upamiętniające żołnierzy AK.",
        "powiazania": ["ARG/II/37", "ARG/II/41"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/II/41",
        "photo": "lbr_II_41_p01.jpg",
        "tytul": "Zestaw fotograficzny — pamięć straconych i męczenników okupacji",
        "data": "lata 50.–60. XX w.",
        "typ": "fotografia",
        "opis_fizyczny": "Zestaw oryginalnych fotografii czarno-białych na arkuszu albumu (szary karton), z podpisami maszynowymi. 2 zdjęcia.",
        "opis_tresci": "Fotografie miejsc pamięci ofiar okupacji hitlerowskiej, z kolekcji gen. Głuchowskiego. Dokumentacja miejsc straceń i martyrologii.",
        "seria": "II",
        "tworca": "nieznany fotograf",
        "jezyk": "polski",
        "kontekst": "Albumy pamięci — typowy element archiwów polskiej emigracji. Głuchowski gromadził dokumentację fotograficzną miejsc martyrologii, tworząc prywatne archiwum pamięci. Materiał z okresu powojennego, gdy emigracja dokumentowała zniszczenia okupacyjne.",
        "powiazania": ["ARG/II/37", "ARG/II/40"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/II/42",
        "photo": "lbr_II_42_p01.jpg",
        "tytul": "Fotografia — gen. Głuchowski podczas inspekcji oddziału polskich oficerów na emigracji",
        "data": "lata 40. XX w.",
        "typ": "fotografia",
        "opis_fizyczny": "Oryginalna fotografia z epoki, czarno-biała. 2 zdjęcia.",
        "opis_tresci": "Gen. Głuchowski podczas inspekcji oddziału polskich oficerów na emigracji, prawdopodobnie w Szkocji.",
        "seria": "II",
        "tworca": "fotograf wojskowy",
        "jezyk": "n/a",
        "kontekst": "Inspekcje oddziałów — podstawowa funkcja dowódcza Głuchowskiego jako Zastępcy Dowódcy Armii Polskiej. Zdjęcia z inspekcji dokumentują hierarchię i ceremoniał Wojska Polskiego na Uchodźstwie.",
        "powiazania": ["ARG/II/38", "ARG/II/43"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/II/43",
        "photo": "lbr_II_43_p01.jpg",
        "tytul": "Fotografia — gen. Głuchowski na oficjalnej uroczystości z władzami Rządu RP na Uchodźstwie",
        "data": "lata 40. XX w.",
        "typ": "fotografia",
        "opis_fizyczny": "Fotografia czarno-biała, trzy warianty/kopie. 3 zdjęcia.",
        "opis_tresci": "Gen. Głuchowski podczas oficjalnej uroczystości z udziałem wysokich władz wojskowych Rządu RP na Uchodźstwie.",
        "seria": "II",
        "tworca": "fotograf wojskowy / prasowy",
        "jezyk": "n/a",
        "kontekst": "Głuchowski na najwyższych szczeblach Rządu RP na Uchodźstwie — I Wiceminister Spraw Wojskowych (od 1935). Zdjęcia z uroczystości państwowych dokumentują jego pozycję w hierarchii polskiej emigracji polityczno-wojskowej w Londynie.",
        "powiazania": ["ARG/II/42", "ARG/II/47"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/II/44",
        "photo": "lbr_II_44_p01.jpg",
        "tytul": "Fotografia — zgromadzenie polskich harcerzy w Dundee (Szkocja), 6 marca 1945",
        "data": "6.III.1945",
        "typ": "fotografia",
        "opis_fizyczny": "Czarno-biała fotografia z datą 6 marca 1945, polscy oficerowie na imprezie harcerskiej w Dundee. 2 zdjęcia.",
        "opis_tresci": "Polscy oficerowie, w tym gen. Głuchowski, podczas imprezy wojskowo-kulturalnej z polskimi harcerzami w Dundee, Szkocja.",
        "seria": "II",
        "tworca": "fotograf wojskowy / harcerski",
        "jezyk": "n/a",
        "kontekst": "Harcerstwo polskie na emigracji w Szkocji — ważny element podtrzymywania polskości. Dundee było jednym z ośrodków polskiej emigracji wojskowej w Szkocji. Marzec 1945 — ostatnie miesiące wojny, przygotowania do demobilizacji.",
        "powiazania": ["ARG/II/45"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/II/45",
        "photo": "lbr_II_45_p01.jpg",
        "tytul": "Fotografia — kongres polskich harcerzy w Dundee (Szkocja), 6 marca 1945",
        "data": "6.III.1945",
        "typ": "fotografia",
        "opis_fizyczny": "Czarno-biała fotografia z dnia 6 marca 1945, uroczyste spotkanie władz wojskowych i polskich harcerzy w Dundee. 3 zdjęcia.",
        "opis_tresci": "Uroczyste spotkanie władz wojskowych z polskimi harcerzami w Dundee. Zdjęcie grupowe z ceremonii.",
        "seria": "II",
        "tworca": "fotograf wojskowy / harcerski",
        "jezyk": "n/a",
        "kontekst": "Ten sam zjazd harcerski co ARG/II/44 — inne ujęcie. Harcerstwo polskie w Szkocji jako forma wychowania patriotycznego w warunkach emigracji. Głuchowski jako generał wspierał inicjatywy młodzieżowe.",
        "powiazania": ["ARG/II/44"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/II/46",
        "photo": "lbr_II_46_p01.jpg",
        "tytul": "Fotografia portretowa — Kazimierz Gedymin Jurgielewicz (1891–1956), oficer Wojska Polskiego",
        "data": "lata 30.–40. XX w.",
        "typ": "fotografia",
        "opis_fizyczny": "Fotografia portretowa 7,5 × 5,5 cm, odręczne oznaczenie ołówkiem na odwrocie. Ze zbiorów Głuchowskich. 1 zdjęcie.",
        "opis_tresci": "Portret Kazimierza Gedymina Jurgielewicza (1891–1956), ważnego oficera Wojska Polskiego. Ze zbiorów rodziny Głuchowskich.",
        "seria": "II",
        "tworca": "fotograf portretowy",
        "jezyk": "n/a",
        "kontekst": "Kazimierz Gedymin Jurgielewicz (1891–1956) — oficer Wojska Polskiego, ukończył gimnazjum w Warszawie i szkołę oficerską. Fotografia zachowana w archiwum Głuchowskiego sugeruje relację służbową lub towarzyską między oficerami.",
        "powiazania": ["ARG/II/47"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/II/47",
        "photo": "lbr_II_47_p01.jpg",
        "tytul": "Fotografia z ok. 28 podpisami oficerów WP — Szkocja, 23 maja 1942, dedykacja dla gen. Głuchowskiego",
        "data": "23.V.1942",
        "typ": "fotografia",
        "opis_fizyczny": "Fotografia czarno-biała z datą 23 maja 1942, grupa polskich żołnierzy, na odwrocie ok. 28 podpisów. 4 zdjęcia.",
        "opis_tresci": "Zdjęcie grupowe polskich żołnierzy w Szkocji z dedykacją i ok. 28 podpisami oficerów, poświęcone gen. Głuchowskiemu.",
        "seria": "II",
        "tworca": "fotograf wojskowy",
        "jezyk": "polski",
        "kontekst": "Maj 1942 — Wojsko Polskie w Szkocji w pełni zorganizowane. Zdjęcie zbiorowe z 28 podpisami oficerów = dokument socjologiczny jednostki wojskowej. Dedykacja dla generała Głuchowskiego świadczy o szacunku podwładnych. Podpisy mogą pozwolić na identyfikację poszczególnych żołnierzy.",
        "powiazania": ["ARG/II/38", "ARG/II/39", "ARG/II/46"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/II/48",
        "photo": "lbr_II_48_p01.jpg",
        "tytul": "Fotografia — inspekcja polskich czołgistów w szkoleniu, Szkocja, lata 40.",
        "data": "ok. 1943–1945",
        "typ": "fotografia",
        "opis_fizyczny": "Czarno-biała fotografia, formacja pancerna na polu treningowym. 3 zdjęcia.",
        "opis_tresci": "Gen. Głuchowski dokonuje inspekcji polskiej formacji pancernej podczas szkolenia w Szkocji. Żołnierze w szyku przed czołgami.",
        "seria": "II",
        "tworca": "fotograf wojskowy",
        "jezyk": "n/a",
        "kontekst": "Szkolenie polskich jednostek pancernych w Szkocji — przygotowania do inwazji na kontynent. 1. Dywizja Pancerna gen. Maczka szkoliła się w Szkocji 1942-1944. Głuchowski jako wysoki dowódca wizytował szkolenia.",
        "powiazania": ["ARG/II/34", "ARG/II/49", "ARG/II/50"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/II/49",
        "photo": "lbr_II_49_p01.jpg",
        "tytul": "Fotografia — inspekcja wojskowa w Kelso (Szkocja), gen. Bór-Komorowski, Głuchowski i Mazur, 15 VI 1945",
        "data": "15.VI.1945",
        "typ": "fotografia",
        "opis_fizyczny": "Czarno-biała fotografia z datą 15 czerwca 1945, inspekcja w Kelso. 3 zdjęcia.",
        "opis_tresci": "Inspekcja wojskowa przed paradą pułku w Kelso (Szkocja). Na zdjęciu: gen. Tadeusz Bór-Komorowski (Naczelny Wódz), gen. Głuchowski i gen. Mazur.",
        "seria": "II",
        "tworca": "fotograf wojskowy",
        "jezyk": "n/a",
        "kontekst": "15 czerwca 1945 — dwa tygodnie po mianowaniu Głuchowskiego na gen. dywizji (1.VI.1945). Bór-Komorowski jako Naczelny Wódz (od XI 1944) dokonuje inspekcji. Kelso — baza polskich jednostek w Szkocji. Zdjęcie trzech generałów razem — wysokiej rangi dokument historyczny.",
        "powiazania": ["ARG/II/50", "ARG/II/48", "ARG/II/34"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/II/50",
        "photo": "lbr_II_50_p01.jpg",
        "tytul": "Fotografia — gen. Bór-Komorowski inspekuje polskie czołgi, parada 3. Pułku Pancernego, 15 VI 1945",
        "data": "15.VI.1945",
        "typ": "fotografia",
        "opis_fizyczny": "Czarno-biała fotografia, zmotoryzowana parada polskich czołgów Cromwell. 3 zdjęcia.",
        "opis_tresci": "Parada 3. Pułku Pancernego z czołgami Cromwell. Gen. Bór-Komorowski dokonuje inspekcji z trybuny. Ta sama uroczystość co ARG/II/49.",
        "seria": "II",
        "tworca": "fotograf wojskowy",
        "jezyk": "n/a",
        "kontekst": "Czołgi Cromwell — podstawowe uzbrojenie polskich jednostek pancernych w 1945. Parada 3. Pułku Pancernego w obecności Naczelnego Wodza to uroczysta demonstracja gotowości bojowej. Jednocześnie — symbolicznie — koniec wojny i początek okresu demobilizacji.",
        "powiazania": ["ARG/II/49", "ARG/II/48"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/II/51",
        "photo": "lbr_II_51_p01.jpg",
        "tytul": "Fotografia — orkiestra 25. Pułku Polskiego, 4. Dywizja Piechoty",
        "data": "lata 40. XX w.",
        "typ": "fotografia",
        "opis_fizyczny": "Czarno-biała fotografia, maszerująca orkiestra wojskowa (dudziarze i dobosze). 2 zdjęcia.",
        "opis_tresci": "Orkiestra dudziarzy i doboszów 25. Pułku Polskiego (4. Dywizja Piechoty) w typowych strojach szkockich (kilty). Z kolekcji gen. Głuchowskiego.",
        "seria": "II",
        "tworca": "fotograf wojskowy",
        "jezyk": "n/a",
        "kontekst": "Polscy żołnierze w Szkocji przyjęli elementy tradycji szkockiej — orkiestry dudziarskie. 25. Pułk Piechoty wchodził w skład 4. Dywizji Piechoty. Połączenie polskiej tradycji wojskowej ze szkocką — unikalny fenomen kulturowy emigracji wojennej.",
        "powiazania": ["ARG/II/48", "ARG/II/55"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/II/52",
        "photo": "lbr_II_52_p01.jpg",
        "tytul": "Zestaw 5 fotografii — spotkanie oficerów polskich i brytyjskich podczas II wojny światowej",
        "data": "lata 40. XX w.",
        "typ": "fotografia",
        "opis_fizyczny": "Cztery fotografie czarno-białe (ok. 11,5 × 7,5 cm i 6 × 8,5 cm), z kolekcji gen. Głuchowskiego. 5 zdjęć.",
        "opis_tresci": "Spotkanie oficerów polskich i brytyjskich. Gen. Głuchowski wśród uczestników. Jedno zdjęcie z dedykacją odręczną.",
        "seria": "II",
        "tworca": "fotograf wojskowy",
        "jezyk": "n/a",
        "kontekst": "Relacje polsko-brytyjskie na szczeblu dowódczym — kluczowe dla funkcjonowania Wojska Polskiego w Wielkiej Brytanii. Głuchowski jako I Wiceminister Spraw Wojskowych i Zastępca Dowódcy Armii utrzymywał kontakty z brytyjskim dowództwem.",
        "powiazania": ["ARG/II/47", "ARG/II/43"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/II/53",
        "photo": "lbr_II_53_p01.jpg",
        "tytul": "Zestaw 4 fotografii — końcowa faza II wojny światowej, 1945, pieczęć Wojskowej Sekcji Fotograficznej",
        "data": "1945",
        "typ": "fotografia",
        "opis_fizyczny": "Cztery fotografie czarno-białe na papierze fotograficznym z pieczęcią Wojskowej Sekcji Fotograficznej. 4 zdjęcia.",
        "opis_tresci": "Fotografie z końcowej fazy II wojny światowej, z kolekcji gen. Głuchowskiego. Pieczęć Wojskowej Sekcji Fotograficznej potwierdza oficjalne pochodzenie.",
        "seria": "II",
        "tworca": "Wojskowa Sekcja Fotograficzna",
        "jezyk": "n/a",
        "kontekst": "Pieczęć Wojskowej Sekcji Fotograficznej — oficjalna dokumentacja wojskowa. Zdjęcia z 1945 r. dokumentują ostatnie miesiące wojny i początek demobilizacji polskich sił na Zachodzie.",
        "powiazania": ["ARG/II/49", "ARG/II/50"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/II/54",
        "photo": "lbr_II_54_p01.jpg",
        "tytul": "Album 'Żołnierz z Montecassino' z DEDYKACJĄ GEN. ANDERSA dla gen. Głuchowskiego — Rzym 1945",
        "data": "31.III.1945",
        "typ": "album fotograficzny",
        "opis_fizyczny": "Album fotograficzny w twardej oprawie, papier fotograficzny, wydany przez Oddział Kultury i Prasy 2. Korpusu AP, Rzym 1945. Na stronie tytułowej ODRĘCZNA DEDYKACJA GEN. WŁADYSŁAWA ANDERSA: 'Gł. J. Głuchowskiemu z wyrazami przyjaźni / w hołdzie naszym żołnierzom do Polski / W. Anders / 31.3.45'. Zażółcenia na okładkach, grzbiet częściowo oderwany. 5 zdjęć.",
        "opis_tresci": "'Żołnierz z Montecassino: Album fotografii z terenu i okresu bitwy' — Wiktor Ostrowski (red.). Album dokumentujący bitwę o Monte Cassino (maj 1944). Egzemplarz z osobistą dedykacją gen. Władysława Andersa, dowódcy 2. Korpusu Polskiego, dla gen. Janusza Głuchowskiego, datowaną 31 marca 1945.",
        "seria": "II",
        "tworca": "Wiktor Ostrowski (red.) / Oddział Kultury i Prasy 2. Korpusu AP",
        "jezyk": "polski",
        "kontekst": "OBIEKT KLUCZOWY DLA KOLEKCJI. Osobista dedykacja gen. Władysława Andersa — dowódcy polskiego zwycięstwa pod Monte Cassino — dla gen. Głuchowskiego. Dwa najwyższe autorytety Wojska Polskiego na emigracji: Anders (2. Korpus, Włochy) i Głuchowski (JWWB, Wielka Brytania). Dedykacja 'z wyrazami przyjaźni' i 'w hołdzie naszym żołnierzom' — dowód osobistej relacji obu generałów mimo służby na dwóch teatrach wojny. Album wydany w Rzymie 1945 = pierwsze opracowanie fotograficzne bitwy o Monte Cassino. Egzemplarz z dedykacją Andersa — najwyższa kategoria wartości kolekcjonerskiej i historycznej. Autograf Andersa na rynku antykwarycznym: 2000-5000 PLN sam w sobie.",
        "powiazania": ["ARG/II/34", "ARG/II/49", "ARG/II/53"],
        "stan": "Średni — zażółcenia, grzbiet częściowo oderwany. Dedykacja czytelna."
    },
    {
        "sygn": "ARG/II/55",
        "photo": "lbr_II_55_p01.jpg",
        "tytul": "Fotografia — żołnierze Wojska Polskiego na motocyklach w Szkocji, 1945",
        "data": "1945",
        "typ": "fotografia",
        "opis_fizyczny": "Czarno-biała fotografia, polski wojskowy oddział motocyklowy w uroczystym szyku. 3 zdjęcia.",
        "opis_tresci": "Oddział motocyklowy Wojska Polskiego w Szkocji, prawdopodobnie podczas oficjalnej inspekcji lub demonstracji w 1945 roku. Z kolekcji gen. Głuchowskiego.",
        "seria": "II",
        "tworca": "fotograf wojskowy",
        "jezyk": "n/a",
        "kontekst": "Polskie jednostki motocyklowe w Szkocji — element wyposażenia dywizji pancernych i rozpoznawczych. Rok 1945 — demonstracja gotowości bojowej w ostatnich miesiącach wojny. Zdjęcie z kolekcji dowódcy = dokumentacja inspekcyjna.",
        "powiazania": ["ARG/II/48", "ARG/II/51"],
        "stan": "Dobry"
    },

    # --- Seria V: Krzysztof Andrzej "Juraś" Głuchowski ---

    {
        "sygn": "ARG/II/56",
        "photo": "lbr_V_157_p01.jpg",
        "tytul": "Pocztówka z litografią karykatury por. Głuchowskiego — Henryk Hertz-Barwiński, 1916",
        "data": "1916–1917",
        "typ": "pocztówka",
        "opis_fizyczny": "Pocztówka ok. 14 × 9 cm, reprodukcja litografii barwnej autorstwa Henryka Hertza-Barwińskiego. Awers: karykatura por. Janusza Głuchowskiego z napisem 'por. Głuchowski' (u góry) i 'Iwankowicze' (u dołu — nazwa miejscowości na Wołyniu, NIE podpis artysty). Rewers: odręczny napis ołówkiem 'Z albumu karykatur Illustr. Sztal. Baonów o por. I Bryg. LP', pieczęć okrągła z monogramem. 2 zdjęcia (obj6_1.jpg awers, obj6_2.jpg rewers).",
        "opis_tresci": "Reprodukcja pocztówkowa jednej z 20 litografii z teki 'Woyska polskiego konterfektów gładkich 20' autorstwa Henryka Hertza-Barwińskiego (1877–1970), aktora i karykaturzysty, oficera I Brygady LP. Teka wydana w Krakowie przez litografa W. Krzepowskiego w 1916–17. Napis 'Iwankowicze' to nazwa miejscowości na froncie wołyńskim, gdzie rysunek powstał — błędnie odczytywany jako nazwisko 'Iwankiewicz'. Wśród 20 sportretowanych oficerów: Piłsudski, Śmigły-Rydz, Berbecki, Kukiel, Kaden-Bandrowski i por. Głuchowski.",
        "seria": "II",
        "tworca": "Henryk Hertz-Barwiński (1877–1970)",
        "jezyk": "polski",
        "kontekst": "Henryk Hertz-Barwiński — aktor, reżyser teatralny i karykaturzysta, ochotnik I Brygady LP od 1914, odznaczony dwukrotnie Krzyżem Walecznych. Stworzył teczkę 20 karykatur oficerów I Brygady na froncie wołyńskim (Iwankowicze) 1915–16, wydaną jako litografie barwne w Krakowie 1916–17. Kompletne teki pojawiają się na aukcjach Desa Unicum. Oryginały zdigitalizowane w Zielonogórskiej Bibliotece Cyfrowej. Pojedyncza pocztówka z kolekcji — dowód rozpoznawalności Głuchowskiego w elicie legionowej.",
        "powiazania": ["ARG/II/59", "ARG/II/1", "ARG/II/2", "ARG/II/36"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/V/157",
        "photo": "lbr_V_158_p01.jpg",
        "tytul": "Zestaw dwóch paszportów brytyjskich Krzysztofa Andrzeja Głuchowskiego",
        "data": "lata 50.–70. XX w.",
        "typ": "paszport",
        "opis_fizyczny": "Dwa oryginalne paszporty brytyjskie wydane przez Zjednoczone Królestwo. 5 zdjęć.",
        "opis_tresci": "Paszporty wydane dla Krzysztofa Andrzeja Głuchowskiego — polskiego uchodźcy, weterana Powstania Warszawskiego i żołnierza AK, później obywatela brytyjskiego.",
        "seria": "V",
        "tworca": "władze brytyjskie",
        "jezyk": "angielski",
        "kontekst": "Krzysztof ('Juraś') Głuchowski — syn ppor. Stanisława Stefana Głuchowskiego i Wandy ps. 'Krysta' (żołnierz Kedywu AK), bratanek gen. Janusza Głuchowskiego. Powstaniec warszawski ps. 'Juraś', jeniec Stalag XI-B Fallingbostel (nr 141009). Po wojnie: 2. Korpus Polski we Włoszech, wykształcenie w Anglii, inżynier, emigracja do Brazylii (Rio de Janeiro). Paszporty brytyjskie dokumentują jego status uchodźcy — świadectwo losu polskiej emigracji wojennej.",
        "powiazania": ["ARG/V/9", "ARG/V/10", "ARG/V/124"],
        "stan": "Dobry"
    },

    # --- GALERIA — dodatkowe materiały ze skanów ---

    # === p02 — dokumenty i tablice ===
    {
        "sygn": "ARG/VI/15",
        "photo": "galeria/galeria_p02_img01.jpeg",
        "tytul": "Dokument maszynopisowy — lista/memorandum",
        "data": "XX w.",
        "typ": "dokument",
        "opis_fizyczny": "Dokument maszynopisowy na papierze maszynowym, format A4 lub zbliżony. 1 zdjęcie.",
        "opis_tresci": "Lista lub memorandum maszynopisowe. Dokument administracyjny z kolekcji Głuchowskich.",
        "seria": "VI",
        "tworca": "nieznany",
        "jezyk": "polski",
        "kontekst": "Dokument z archiwum rodzinnego Głuchowskich — prawdopodobnie korespondencja urzędowa lub lista organizacyjna.",
        "powiazania": [],
        "stan": "Średni"
    },
    {
        "sygn": "ARG/V/158",
        "photo": "galeria/galeria_p02_img03.jpeg",
        "tytul": "Tablica pamiątkowa — atak na gmach Gestapo 1.VIII.1944, 7 p.ul. AK Jeleń, 187 powstańców, 67 poległo",
        "data": "po 1944",
        "typ": "fotografia tablicy",
        "opis_fizyczny": "Fotografia tablicy pamiątkowej upamiętniającej atak na gmach Gestapo w dniu 1 sierpnia 1944. 1 zdjęcie.",
        "opis_tresci": "Tablica pamiątkowa poświęcona atakowi na gmach Gestapo w pierwszym dniu Powstania Warszawskiego. 7. pułk ułanów AK ps. 'Jeleń' — 187 powstańców brało udział, 67 poległo.",
        "seria": "V",
        "tworca": "nieznany",
        "jezyk": "polski",
        "kontekst": "Atak na gmach Gestapo przy al. Szucha 25 — jedna z najbardziej dramatycznych akcji pierwszego dnia Powstania Warszawskiego. 7. pułk ułanów AK 'Jeleń' poniósł ogromne straty: 67 z 187 uczestników poległo. Krzysztof 'Juraś' Głuchowski walczył w Powstaniu Warszawskim — tablica bezpośrednio łączy się z jego doświadczeniem bojowym.",
        "powiazania": ["ARG/V/9", "ARG/V/10", "ARG/V/162"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/VI/16",
        "photo": "galeria/galeria_p02_img02.jpeg",
        "tytul": "List maszynopisowy z odręczną notatką — wzmianka o Prymasie",
        "data": "XX w.",
        "typ": "korespondencja",
        "opis_fizyczny": "List maszynopisowy z odręcznymi dopiskami. 1 zdjęcie.",
        "opis_tresci": "List maszynopisowy z adnotacjami odręcznymi, zawierający wzmiankę o Prymasie. Z kolekcji Głuchowskich.",
        "seria": "VI",
        "tworca": "nieznany",
        "jezyk": "polski",
        "kontekst": "Wzmianka o Prymasie sugeruje kontekst kościelno-polityczny. Głuchowscy utrzymywali kontakty w kręgach emigracji londyńskiej, gdzie relacje z hierarchią kościelną były istotnym elementem życia społecznego.",
        "powiazania": [],
        "stan": "Średni"
    },

    # === p03 — dokumenty i listy ===
    {
        "sygn": "ARG/VI/17",
        "photo": "galeria/galeria_p03_img01.jpeg",
        "tytul": "Dokument maszynopisowy — raport/kronika",
        "data": "XX w.",
        "typ": "dokument",
        "opis_fizyczny": "Dokument maszynopisowy wielostronicowy. 5 zdjęć (galeria_p03_img01 przez img05).",
        "opis_tresci": "Raport lub kronika maszynopisowa — wielostronicowy dokument z archiwum rodzinnego Głuchowskich.",
        "seria": "VI",
        "tworca": "nieznany",
        "jezyk": "polski",
        "kontekst": "Wielostronicowy raport lub kronika — dokument o charakterze sprawozdawczym lub historycznym z archiwum rodziny Głuchowskich.",
        "powiazania": [],
        "stan": "Średni"
    },
    {
        "sygn": "ARG/V/159",
        "photo": "galeria/galeria_p03_img03.jpeg",
        "tytul": "List K.A. Głuchowskiego do Col. Bermana w Cleveland OH — oferta sprzedaży pamiątek, Londyn 21.XI.1984",
        "data": "21.XI.1984",
        "typ": "korespondencja",
        "opis_fizyczny": "List maszynopisowy na papierze, format A4. Nagłówek z adresem nadawcy: 'K.A. Gluchowski, 42 Emperors Gate, London S.W.7'. Data: '21st November 1984'. Adresat: 'Col. Berman' w Cleveland, Ohio, USA. Tekst w języku angielskim — oferta sprzedaży: (1) pierścień srebrno-złoty z Oflagu, (2) książka gen. Głuchowskiego, (3) widoki obozu jenieckiego. Podpis odręczny.",
        "opis_tresci": "List Krzysztofa Andrzeja Głuchowskiego z Londynu (42 Emperors Gate, SW7) do pułkownika Bermana w Cleveland, Ohio — oferta sprzedaży pamiątek rodzinnych: pierścień srebrno-złoty wykonany w Oflagu (prawdopodobnie pamiątka jenieckiego rzemiosła artystycznego), książka autorstwa gen. Głuchowskiego, widoki obozu jenieckiego (fotografie lub pocztówki). Adres 42 Emperors Gate — ten sam co w biogramie z 1995 (ARG/V/166), potwierdza długoletni pobyt Krzysztofa w South Kensington.",
        "seria": "V",
        "tworca": "Krzysztof A. Głuchowski",
        "jezyk": "angielski",
        "kontekst": "List dokumentuje próby sprzedaży pamiątek rodzinnych w 1984 — Krzysztof miał 58 lat, mieszkał jeszcze w Londynie (przed emigracją do Brazylii). Col. Berman w Cleveland OH — prawdopodobnie kolekcjoner militariów polskich w USA, gdzie duża Polonia (Cleveland miał dużą społeczność polską). Adres 42 Emperors Gate, SW7 — elegancka dzielnica South Kensington, w pobliżu polskich instytucji (POSK, Instytut Sikorskiego). Oferta pierścienia z Oflagu świadczy o tym, że Krzysztof przechowywał również pamiątki ojca/wujka z obozu oficerskiego.",
        "powiazania": ["ARG/V/157", "ARG/V/160", "ARG/V/166"],
        "stan": "Dobry"
    },

    # === p04 — katalog numizmatyczny i listy ===
    {
        "sygn": "ARG/VI/18",
        "photo": "galeria/galeria_p04_img01.jpeg",
        "tytul": "Fragment łacińskiego traktatu numizmatycznego — 'Peregrina Numorum Hasmonaeorum', z rycinami monet starożytnych",
        "data": "XVIII–XIX w. (druk)",
        "typ": "druk",
        "opis_fizyczny": "Dwie karty z łacińskiego traktatu numizmatycznego. Karta 1 (galeria_p04_img01): ryciny 16 monet starożytnych (hasmoneańskich) w siatce 4×4, pod nimi tekst łaciński drobnym drukiem, u dołu ozdobny winieta z herbem/motywem roślinnym, data MDCCCXCIV(?). Karta 2 (galeria_p04_img02): strona tytułowa — 'PEREGRINA NUMORUM HASMONAEORUM' z ozdobnym kartuszem i koroną. Autor: Alberto Zorgelio(?). Papier kremowy, druk starodrukowy, plamy od wilgoci. 2 zdjęcia.",
        "opis_tresci": "Fragment łacińskiego traktatu o monetach dynastii Hasmoneuszy (żydowskich władców Judei, II–I w. p.n.e.). Publikacja naukowa z XVIII lub XIX w. z rycinami monet starożytnych. Obecność tego druku w kolekcji Głuchowskich wiąże się z zainteresowaniami numizmatycznymi Krzysztofa — posiadał też kompletny zestaw waluty getta łódzkiego (ARG/V/160). Traktat mógł służyć jako materiał referencyjny dla kolekcjonera.",
        "seria": "VI",
        "tworca": "Alberto Zorgelio(?) (autor), drukarnia łacińska",
        "jezyk": "łaciński",
        "kontekst": "Starodruk numizmatyczny — traktat o monetach Hasmoneuszy łączy zainteresowania kolekcjonerskie Krzysztofa z judaistycznymi numizmatami (waluta getta łódzkiego). Monety hasmoneańskie — bite przez Judę Machabeusza i jego następców (167–37 p.n.e.) — cenione przedmioty kolekcjonerskie. Druk łaciński sugeruje wydanie akademickie z XVIII/XIX w. Sam w sobie może mieć wartość antykwaryczną.",
        "powiazania": ["ARG/V/160"],
        "stan": "Średni — plamy od wilgoci, zagięcia"
    },
    {
        "sygn": "ARG/V/160",
        "photo": "galeria/galeria_p04_img03.jpeg",
        "tytul": "List K. Głuchowskiego do Ambasady Izraela — oferta sprzedaży kompletnego zestawu waluty getta łódzkiego, Londyn 18.V.1958",
        "data": "18.V.1958",
        "typ": "korespondencja",
        "opis_fizyczny": "List maszynopisowy na papierze A4. Nagłówek: '42, Emperors Gate, London S.W.7' i data '18th May, 1958'. Adresat: 'The Israel Embassy, 2 Palace Green, London W.8'. Treść: 'Dear Sir, I am contemplating sale of my complete set of paper currency and coins of the Łódź Ghetto during the German occupation of Poland. The above set is of great rarity and museum value, and I wonder if some institution in Israel would not be interested in purchase. Hoping that you will be able to assist me in this matter, I remain, Sir, yours faithfully, K. Głuchowski.' Podpis odręczny. 2 zdjęcia.",
        "opis_tresci": "List Krzysztofa Głuchowskiego z 42 Emperors Gate, London SW7 do Ambasady Izraela (2 Palace Green, W8) oferujący sprzedaż kompletnego zestawu waluty papierowej i monet getta łódzkiego (Litzmannstadt Getto). Głuchowski podkreśla 'great rarity and museum value' i pyta czy instytucja w Izraelu byłaby zainteresowana zakupem. List z 1958 r. — 13 lat po wojnie, Krzysztof miał 32 lata.",
        "seria": "V",
        "tworca": "Krzysztof A. Głuchowski",
        "jezyk": "angielski",
        "kontekst": "NIEZWYKŁY DOKUMENT. Waluta getta łódzkiego (Litzmannstadt Getto, 1940–44) — monety aluminiowe i banknoty emitowane przez Judenrat pod nadzorem Chaima Rumkowskiego. Kompletne zestawy to dziś jedne z najcenniejszych numizmatów Holokaustu (wycena: 5000-20000 PLN za komplet). List do Ambasady Izraela w 1958 — Krzysztof próbował sprzedać je instytucji muzealnej. Pytanie: czy sprzedał? Jeśli nie — waluta może nadal być w kolekcji lub została sprzedana innemu kolekcjonerowi. Adres Ambasady: 2 Palace Green, W8 — historyczna siedziba ambasady Izraela w Londynie. Ten sam adres Krzysztofa co 26 lat później (list do Bermana, 1984).",
        "powiazania": ["ARG/V/159", "ARG/VI/18", "ARG/V/166"],
        "stan": "Dobry"
    },

    # === p05 — nekrologi i wycinki prasowe ===
    {
        "sygn": "ARG/VI/19",
        "photo": "galeria/galeria_p05_img01.jpeg",
        "tytul": "Nekrologi płk. Jana Lewandowskiego — wycinki prasowe z adnotacją odręczną, ok. 1960",
        "data": "ok. 1960",
        "typ": "wycinek prasowy",
        "opis_fizyczny": "Kartka z naklejonymi dwoma wycinkami nekrologów: (1) krótki 'Ś.P. JAN LEWANDOWSKI' z datą i krótkim biogramem, (2) dłuższy nekrolog 'Pułkownik Jan Lewandowski' z obszernym opisem służby. Odręczna notatka niebieskim atramentem u dołu z datami i odnośnikami ('Życie Barnasz... Cz. 555 2 VI, Thomas 1960'). Notatka inna ręka — prawdopodobnie Krzysztof Głuchowski notował źródła i daty. 1 zdjęcie.",
        "opis_tresci": "Nekrologi płk. Jana Lewandowskiego z prasy emigracyjnej (prawdopodobnie Dziennik Polski i Dziennik Żołnierza, Londyn) z ok. 1960 r. Lewandowski był oficerem WP powiązanym ze środowiskiem kawalerii — jego nekrolog przechowywany w archiwum Głuchowskich wskazuje na bezpośredni związek służbowy lub towarzyski z gen. Januszem Głuchowskim.",
        "seria": "VI",
        "tworca": "prasa emigracyjna (Londyn)",
        "jezyk": "polski",
        "kontekst": "Środowisko emigracji wojskowej prowadziło systematyczną dokumentację obituarną. Gen. Głuchowski (zm. 1964) lub po jego śmierci syn Krzysztof zbierali nekrologi oficerów związanych z 7 Pułkiem Ułanów Lubelskich i szerszym kręgiem kawalerii WP. Odręczne notatki z referencjami ('Życie', 'Thomas 1960') świadczą o aktywnej pracy dokumentacyjnej — nie biernym gromadzeniu wycinków.",
        "powiazania": ["ARG/VI/20"],
        "stan": "Średni"
    },
    {
        "sygn": "ARG/VI/20",
        "photo": "galeria/galeria_p05_img02.jpeg",
        "tytul": "Nekrologi żołnierzy 7 Pułku Ułanów i Dywizjonu 'Jeleń' — Lorens, Iwanowski, Zalewska, Chojnacka, 1959–69",
        "data": "1959–1969",
        "typ": "wycinek prasowy",
        "opis_fizyczny": "Zbiór 5 kart z naklejonymi wycinkami nekrologów z prasy emigracyjnej: (1) 'Ś.P. JAN LORENS, plutonowy 7 pułku ułanów' zm. 29.I.1960 w Chicago, wydany przez Koło Żołnierzy 7 P.U.L. im. Gen. K. Sosnkowskiego; (2) cztery wersje nekrologu 'mgr inż. Walery IWANOWSKI'; (3) 'CHOJNACKA' i 'Maria ZALEWSKA' z powiązaniem z 'Żołnierzy Dywizjonu Jeleń'; (4) odręczna notatka 'Życie Marianny, urod 13, 14 grudzień 1959'. 5 zdjęć.",
        "opis_tresci": "Systematyczny zbiór nekrologów towarzyszy broni i członków środowiska pułkowego: plut. Jan Lorens — żołnierz 7 P.U.L., prezes sekcji Koła pułkowego w Chicago, członek organizacji niepodległościowych, zm. 29.I.1960. Mgr inż. Walery Iwanowski — prawdopodobnie oficer rezerwy lub inżynier ze środowiska ziemiańskiego Kresów, zm. ok. 1969. Maria Zalewska — powiązana z Dywizjonem 'Jeleń' (konspiracyjna kontynuacja 7 P.U.L. w AK). Chojnacka — rodzina pułkowa.",
        "seria": "VI",
        "tworca": "prasa emigracyjna (Londyn, Chicago)",
        "jezyk": "polski",
        "kontekst": "Koło Żołnierzy 7 Pułku Ułanów Lubelskich im. Gen. K. Sosnkowskiego — organizacja weteranów w diasporze (Londyn, Chicago). 7 P.U.L. to pułk gen. Głuchowskiego — dowodził nim w okresie międzywojennym. Pułkowy patron Gen. Kazimierz Sosnkowski (1885–1969) był Naczelnym Wodzem PSZ 1943–44. Nekrologi zbierane przez Krzysztofa dokumentują rozproszenie weteranów po świecie — Chicago miało największą polonijną społeczność kombatancką w USA. Dywizjon 'Jeleń' — kryptonim konspiracyjny kontynuacji tradycji 7 P.U.L. w AK podczas Powstania Warszawskiego.",
        "powiazania": ["ARG/V/158", "ARG/V/162", "ARG/VI/19"],
        "stan": "Średni — pożółkłe, kruche"
    },

    # === p06 — album wojskowy i nekrologi ===
    {
        "sygn": "ARG/II/57",
        "photo": "galeria/galeria_p06_img01.jpeg",
        "tytul": "Album fotograficzny — zbiórki wojskowe 1921 i dedykacja dla gen. Głuchowskiego (8.III.1944)",
        "data": "1921 / 1944",
        "typ": "album fotograficzny",
        "opis_fizyczny": "Album fotograficzny na czarnym kartonie. Strona ze zdjęciami: (1) 'piwa za zdrowie Komendanta 1921' — grupa żołnierzy przy stole, (2) 'Zbiórka kompanii do raportu Porannego' — formacja na placu. Strona dedykacyjna (galeria_p06_img02): białe pismo na czarnym kartonie 'Panu Gen. Głuchowskiemu / Dowódcy Jedn. Wojsk w W. Brytanii / w okazji pobytu / w / Centrum Wyszkolenia Łączności / Żołnierze / Kompanii Dozorowania / w/dżęci 8 marca 1944'. Wklejone małe zdjęcie budynku. 3 zdjęcia.",
        "opis_tresci": "Album ofiarowany gen. Januszowi Głuchowskiemu — Dowódcy Jednostek Wojskowych w Wielkiej Brytanii — przez żołnierzy Kompanii Dozorowania z Centrum Wyszkolenia Łączności, 8 marca 1944 r. Zawiera zdjęcia wojskowe z 1921 r. (toast za zdrowie Komendanta, poranna zbiórka kompanii). Dedykacja potwierdza, że Głuchowski wizytował jednostki łączności jako Dowódca JWWB.",
        "seria": "II",
        "tworca": "żołnierze Kompanii Dozorowania, Centrum Wyszkolenia Łączności",
        "jezyk": "polski",
        "kontekst": "Album-dar dla dowódcy — typowa forma wyrazu szacunku w tradycji Wojska Polskiego. Gen. Głuchowski od IX.1943 dowodził JWWB (Jednostkami Wojskowymi w Wielkiej Brytanii), wizytując m.in. Centrum Wyszkolenia Łączności. Data 8.III.1944 potwierdza aktywność dowódczą Głuchowskiego w Szkocji/Anglii. Zdjęcia z 1921 roku dokumentują tradycje pułkowe — toast 'za zdrowie Komendanta' i poranna zbiórka to sceny z życia garnizonu II RP.",
        "powiazania": ["ARG/II/58", "ARG/II/60"],
        "stan": "Średni"
    },
    {
        "sygn": "ARG/VI/21",
        "photo": "galeria/galeria_p06_img04.jpeg",
        "tytul": "Nekrolog mgr inż. Walerego Iwanowskiego, 1969 + inne wycinki",
        "data": "1969",
        "typ": "wycinek prasowy",
        "opis_fizyczny": "Nekrolog i wycinki prasowe. 3 zdjęcia (galeria_p06_img04 przez img06).",
        "opis_tresci": "Nekrolog mgr inż. Walerego Iwanowskiego z 1969 roku wraz z dodatkowymi wycinkami prasowymi z archiwum Głuchowskich.",
        "seria": "VI",
        "tworca": "prasa emigracyjna",
        "jezyk": "polski",
        "kontekst": "Walery Iwanowski — inżynier ze środowiska polskiej emigracji. Nekrolog z 1969 roku dokumentuje powiązania towarzyskie rodziny Głuchowskich w kręgach polskiej inteligencji emigracyjnej.",
        "powiazania": ["ARG/VI/19", "ARG/VI/20"],
        "stan": "Średni"
    },

    # === p07 — album wojskowy ===
    {
        "sygn": "ARG/II/58",
        "photo": "galeria/galeria_p07_img01.jpeg",
        "tytul": "Album — zdjęcia wojskowe z podpisami, manewry i ceremonie",
        "data": "lata 20.–30. XX w.",
        "typ": "album fotograficzny",
        "opis_fizyczny": "Strony albumu fotograficznego z podpisanymi zdjęciami wojskowymi — manewry, ceremonie, życie garnizonowe. 6 zdjęć (galeria_p07_img01 przez img06).",
        "opis_tresci": "Rozbudowana sekcja albumu gen. Głuchowskiego — zdjęcia z manewrów wojskowych, ceremonii i życia garnizonowego z podpisami identyfikującymi osoby i wydarzenia.",
        "seria": "II",
        "tworca": "fotograf wojskowy",
        "jezyk": "polski",
        "kontekst": "Album z podpisami — cenny dokument identyfikacyjny. Manewry i ceremonie wojskowe II RP dokumentują strukturę dowodzenia i relacje między oficerami. Podpisy pozwalają na identyfikację osób i wydarzeń historycznych.",
        "powiazania": ["ARG/II/57", "ARG/II/60"],
        "stan": "Średni"
    },

    # === p08 — karykatury i album ===
    {
        "sygn": "ARG/II/59",
        "photo": "galeria/galeria_p08_img01.jpeg",
        "tytul": "Oryginał karykatury por. Głuchowskiego — Henryk Hertz-Barwiński, Iwankowicze 1915–16",
        "data": "1915–1916",
        "typ": "rysunek",
        "opis_fizyczny": "Rysunek ołówkiem na papierze, karykatura por. Janusza Głuchowskiego. U góry napis 'por. Głuchowski', u dołu 'Iwankowicze' (miejscowość na froncie wołyńskim — NIE podpis artysty). Rysunek jest oryginałem lub kopią roboczą jednej z 20 karykatur z teki Hertza-Barwińskiego. 1 zdjęcie.",
        "opis_tresci": "Oryginał (lub kopia robocza) karykatury por. Janusza Głuchowskiego autorstwa Henryka Hertza-Barwińskiego (1877–1970), narysowany na froncie wołyńskim w Iwankowiczach 1915–16. Rysunek ten posłużył jako baza dla litografii barwnej w tece 'Woyska polskiego konterfektów gładkich 20', wydanej przez W. Krzepowskiego w Krakowie 1916–17. Reprodukcja pocztówkowa tej samej karykatury: ARG/II/56.",
        "seria": "II",
        "tworca": "Henryk Hertz-Barwiński (1877–1970)",
        "jezyk": "n/a",
        "kontekst": "UNIKAT. Oryginał rysunku ołówkowego w kolekcji rodzinnej sportretowanego — wyjątkowa wartość, bo teka wydana zawiera jedynie litografie, a oryginalne rysunki przygotowawcze nie były publikowane. Hertz-Barwiński (aktor, reżyser teatralny, dwukrotnie odznaczony KW) rysował współtowarzyszy broni na pozycjach I Brygady LP na Wołyniu. Fakt posiadania oryginału przez rodzinę Głuchowskich sugeruje bezpośredni dar artysty dla portretowanego oficera.",
        "powiazania": ["ARG/II/56"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/II/60",
        "photo": "galeria/galeria_p08_img02.jpeg",
        "tytul": "Album — zdjęcia wojskowe, ćwiczenia, ceremonie",
        "data": "lata 20.–30. XX w.",
        "typ": "album fotograficzny",
        "opis_fizyczny": "Strony albumu fotograficznego — ćwiczenia wojskowe i ceremonie. 4 zdjęcia (galeria_p08_img02 przez img05).",
        "opis_tresci": "Kolejne strony albumu gen. Głuchowskiego — dokumentacja ćwiczeń wojskowych i ceremonii z okresu międzywojennego.",
        "seria": "II",
        "tworca": "fotograf wojskowy",
        "jezyk": "n/a",
        "kontekst": "Ćwiczenia i ceremonie wojskowe II RP — kontynuacja dokumentacji z albumu gen. Głuchowskiego. Zdjęcia z ćwiczeń polowych i defilad stanowią cenne źródło do historii Wojska Polskiego okresu międzywojennego.",
        "powiazania": ["ARG/II/57", "ARG/II/58"],
        "stan": "Średni"
    },

    # === p09 — legitymacja wojskowa ===
    {
        "sygn": "ARG/II/61",
        "photo": "galeria/galeria_p09_img01.jpeg",
        "tytul": "Legitymacja wojskowa gen. Janusza Głuchowskiego — przedłużenia ważności 1932–193x, pieczęć Szefa Sztabu Głównego",
        "data": "1932–ok.1938",
        "typ": "legitymacja",
        "opis_fizyczny": "Legitymacja wojskowa w formie książeczki, otwarta na stronach z przedłużeniami ważności. Strona lewa (galeria_p09_img01): pieczęć z orłem (czerwona), napis 'Przedłużam ważność niniejszej legitymacji do dnia 31 grudnia 19__', nr '2' w kółku. Strona prawa (galeria_p09_img02): wielokrotne przedłużenia — 'Legitymacji do dnia 31ego grudnia 193_ roku, SZEF SZTABU GŁÓWNEGO, Podpis przełożonego:', pieczęcie okrągłe z orłem, podpisy nieczytelne. Widoczne daty: 1932, inne lata 30. 3 zdjęcia.",
        "opis_tresci": "Legitymacja wojskowa gen. Janusza Głuchowskiego z wielokrotnymi przedłużeniami ważności przez Szefa Sztabu Głównego WP. Pieczęć 'SZEF SZTABU GŁÓWNEGO' — Głuchowski w latach 30. pełnił funkcję I Wiceministra Spraw Wojskowych, co wymagało legitymacji podpisywanej na najwyższym szczeblu dowodzenia. Przedłużenia z kolejnych lat dokumentują ciągłość służby.",
        "seria": "II",
        "tworca": "Sztab Główny Wojska Polskiego",
        "jezyk": "polski",
        "kontekst": "Legitymacja z pieczęcią Szefa Sztabu Głównego — dokument najwyższej rangi identyfikacyjnej w WP II RP. Szefami SG w latach 30. byli m.in. gen. Tadeusz Piskor (1926–31) i gen. Wacław Stachiewicz (1935–39). Wielokrotne przedłużenia wskazują na długotrwałą służbę czynną Głuchowskiego — jako I Wiceminister Spraw Wojskowych (1928–35) i dowódca dywizji kawalerii potrzebował aktualnej legitymacji na najwyższym poziomie autoryzacji.",
        "powiazania": ["ARG/II/1", "ARG/II/2", "ARG/II/36"],
        "stan": "Średni"
    },

    # === p10 — dyplom Krzyża Legionowego ===
    {
        "sygn": "ARG/II/62",
        "photo": "galeria/galeria_p10_img01.jpeg",
        "tytul": "Dyplom nadania Krzyża Legjonowego Nr 115 — Głuchowskiemu Januszowi, z I br. wt., Warszawa VI.1925",
        "data": "VI.1925",
        "typ": "dyplom",
        "opis_fizyczny": "Dyplom drukowany na papierze czerpanym, format ok. A4. Nagłówek: 'KRZYŻ LEGJONOWY'. Tekst: 'Komisji Kwalifikacyjnej nadaję / Głuchowskiemu Januszowi / z I. br. wt.' (z 1. Brygady — skrót brygady legionowej). Miejsce i data: 'Warszawa dn. M.VI 1925' (miesiąc VI = czerwiec). Nr 115. Pieczęć urzędowa, podpis. 3 zdjęcia.",
        "opis_tresci": "Dyplom nadania Krzyża Legjonowego Nr 115 Januszowi Głuchowskiemu jako weteranowi I Brygady Legionów Polskich ('I. br. wt.' = I brygada, weteran). Krzyż Legjonowy ustanowiony ustawą z 2.VIII.1923 dla uczestników walk w Legionach Polskich 1914–18. Numer 115 — jeden z pierwszych nadanych, co świadczy o randze zasług Głuchowskiego. Komisja Kwalifikacyjna weryfikowała prawo do odznaczenia na podstawie dokumentacji służby legionowej.",
        "seria": "II",
        "tworca": "Komisja Kwalifikacyjna Krzyża Legjonowego, Warszawa",
        "jezyk": "polski",
        "kontekst": "Krzyż Legjonowy — odznaczenie wojskowe II RP za służbę w Legionach Polskich 1914–18 (ustawa z 2.VIII.1923, rozporządzenie z 3.VI.1925). Głuchowski jako jeden z 'Siódemki Beliny' (3.VIII.1914) i oficer I Brygady — Nr 115 plasuje go w ścisłej czołówce odznaczonych. Skrót 'I. br. wt.' potwierdza przynależność do I Brygady LP dowodzonej przez Piłsudskiego. Data VI.1925 — dyplom wystawiony niemal natychmiast po wejściu rozporządzenia w życie, co świadczy o priorytetowym traktowaniu weterana Siódemki.",
        "powiazania": ["ARG/II/1", "ARG/II/56", "ARG/II/59", "ARG/II/64"],
        "stan": "Dobry"
    },

    # === p11 — świadectwo urodzenia ===
    {
        "sygn": "ARG/II/63",
        "photo": "galeria/galeria_p11_img01.jpeg",
        "tytul": "Świadectwo Urodzenia i Chrztu Św. — parafia warszawska, Nr 618, 1927",
        "data": "29.VII.1928 (wystawione)",
        "typ": "dokument metrykalny",
        "opis_fizyczny": "Formularz drukowany 'RZECZPOSPOLITA POLSKA / Świadectwo Urodzenia i Chrztu Św. / wydane na podstawie ksiąg metrycznych' z parafii warszawskiej. Nr 618 r. 1927. Znaczek skarbowy 10 gr. (Skarb Państwa). Pola wypełnione odręcznie: imię, nazwisko, data i miejsce urodzenia, rodzice. Pieczęć 'PROBOSZCZ', data wystawienia '29 lipiec 1928'. 3 zdjęcia.",
        "opis_tresci": "Świadectwo urodzenia i chrztu wystawione w 1928 r. na podstawie wpisu z 1927 r. z ksiąg metrykalnych parafii warszawskiej. Prawdopodobnie dotyczy Krzysztofa Andrzeja Głuchowskiego (ur. 29.XI.1926 wg biogramu) lub innego dziecka z rodziny generała. Numer metryczny 618 z roku 1927 — rejestracja chrztu w roku następnym po urodzeniu.",
        "seria": "II",
        "tworca": "Parafia w Warszawie (proboszcz)",
        "jezyk": "polski",
        "kontekst": "Świadectwo metrykalne z II RP — standardowy dokument kościelny pełniący rolę aktu urodzenia (do 1945 r. w Polsce rejestry stanu cywilnego prowadziły parafie). Znaczek skarbowy 10 gr — opłata administracyjna. Jeśli dotyczy Krzysztofa (ur. 29.XI.1926), dokument ten mógł być potrzebny do wpisania dziecka do szkoły lub do celów administracyjnych. Rodzina Głuchowskich mieszkała w Warszawie w dzielnicy Rakowiec.",
        "powiazania": ["ARG/II/61"],
        "stan": "Dobry"
    },

    # === p12 — dokumenty okupacyjne ===
    {
        "sygn": "ARG/V/161",
        "photo": "galeria/galeria_p12_img01.jpeg",
        "tytul": "Kennkarte (Karta Rozpoznawcza) Krzysztofa Głuchowskiego — Generalgouvernement, 1943",
        "data": "9.XI.1943",
        "typ": "dokument okupacyjny",
        "opis_fizyczny": "Kennkarte (Karta Rozpoznawcza) Generalnego Gubernatorstwa. Okładka: 'GENERALGOUVERNEMENT / GENERALNE GUBERNATORSTWO / KENNKARTE / KARTA ROZPOZNAWCZA', nr '17' ołówkiem. Wnętrze: zdjęcie młodego mężczyzny (Krzysztof Głuchowski, lat 17), adres Pogonowskiego(?), Warszawa. Pieczęć 'Der Polizeipräsident' z orłem III Rzeszy, data wydania '9 November 1943'. Odciski palców. Tylna strona: 'ZUR BEACHTUNG! UWAGI URZĘDOWE' — regulamin dwujęzyczny DE/PL. 4 zdjęcia.",
        "opis_tresci": "Kennkarte — obowiązkowy dowód tożsamości w Generalnym Gubernatorstwie, wydana Krzysztofowi Głuchowskiemu w Warszawie 9.XI.1943 przez Polizeipräsidenten (Prezydenta Policji). Dokument wystawiony na ok. 10 miesięcy przed wybuchem Powstania Warszawskiego. Zdjęcie przedstawia 17-letniego Krzysztofa — przyszłego powstańca ps. 'Juraś'.",
        "seria": "V",
        "tworca": "Der Polizeipräsident, Warszawa (Generalgouvernement)",
        "jezyk": "niemiecki, polski",
        "kontekst": "Kennkarte — podstawowy dokument tożsamości w GG, obowiązkowy od 1941 dla wszystkich mieszkańców powyżej 15. roku życia. Wydanie w XI.1943 — Krzysztof miał 17 lat i prawdopodobnie już działał w konspiracji AK (wg biogramu z 1995 r. uciekł z domu jesienią 1943 do ZWZ/AK). Dokument z oficjalnym zdjęciem i danymi osobowymi młodego konspiranta, który 9 miesięcy później weźmie udział w Powstaniu Warszawskim jako ułan Dywizjonu 'Jeleń'. Niezwykle rzadki zachowany egzemplarz Kennkarte powstańca.",
        "powiazania": ["ARG/V/162", "ARG/V/163"],
        "stan": "Średni — zużycie z użytkowania"
    },

    # === p13 — dokumenty wojskowe AK ===
    {
        "sygn": "ARG/V/162",
        "photo": "galeria/galeria_p13_img01.jpeg",
        "tytul": "Dokumenty AK Krzysztofa Głuchowskiego — rozkaz awansu, pieczęć Komendanta AK Warszawa, IX.1944",
        "data": "11.IX.1944",
        "typ": "dokument wojskowy",
        "opis_fizyczny": "Zestaw dokumentów AK: (1) galeria_p13_img01 — dokument służbowy datowany 1.VIII.1944, maszynopis z pieczęcią i podpisem, częściowo nieczytelny; (2) galeria_p13_img02 — KLUCZOWY: rozkaz awansu na kartoniku ok. 8×6 cm, odręczny tekst: 'Rozk. D-na Grupy «Północ» Nr 24, zap. IX.44, awansowany do stopnia st. ułana i nagrodzony «K.H.» po raz I-szy'. Czerwona pieczęć okrągła: 'KOMENDANT ★ ARMII KRAJOWEJ ★ WARSZAWA' z orłem polskim. Podpis '29 grudnia... J. Kasierski(?)', data '11.9.44'; (3) galeria_p13_img03 — insygnia wojskowe: srebrny ryngraf/lanyard oficerski, złoty galon, baretka wstążki Krzyża Walecznych (bordo-kremowa). 6 zdjęć.",
        "opis_tresci": "Rozkaz awansu Krzysztofa 'Jurasia' Głuchowskiego do stopnia starszego ułana i nagrodzenia Krzyżem Walecznych ('K.H.' = Krzyż Walecznych, po raz I) na mocy Rozkazu Dowódcy Grupy 'Północ' Nr 24 z IX.1944. Pieczęć 'KOMENDANT ARMII KRAJOWEJ WARSZAWA' z orłem — autentyczna pieczęć konspiracyjna Komendy Głównej AK. Dokument z 1.VIII.1944 to prawdopodobnie przydział bojowy na pierwszy dzień Powstania. Insygnia fizyczne: lanyard, galon, baretka KW.",
        "seria": "V",
        "tworca": "Komenda Główna Armii Krajowej / Dowódca Grupy 'Północ'",
        "jezyk": "polski",
        "kontekst": "BEZCENNE DOKUMENTY POWSTAŃCZE. Grupa 'Północ' — jedno ze zgrupowań AK w Powstaniu Warszawskim, operująca na Żoliborzu i okolicach. Rozkaz awansu z pieczęcią Komendanta AK Warszawa — autentyczny dokument konspiracyjny, którego większość została zniszczona podczas kapitulacji lub przechwycona przez Niemców. Krzysztof Głuchowski walczył w 7 P.U.L. AK 'Jeleń' — wg tablicy pamiątkowej (ARG/V/158) z tego samego pułku w natarciu na gmach Gestapo 1.VIII.1944 z 187 powstańców poległo 67. Nagrodzenie KW w IX.1944 — w trakcie trwających walk — świadczy o wyjątkowej odwadze 18-letniego ułana.",
        "powiazania": ["ARG/V/158", "ARG/V/161", "ARG/II/64"],
        "stan": "Średni — uszkodzenia wojenne, zagniecenia"
    },

    # === p14 — fragmenty notatek ===
    {
        "sygn": "ARG/VI/22",
        "photo": "galeria/galeria_p14_img01.jpeg",
        "tytul": "Fragmenty notatek i listów — zniszczone",
        "data": "XX w.",
        "typ": "korespondencja",
        "opis_fizyczny": "Fragmenty zniszczonych notatek i listów. 6 zdjęć (galeria_p14_img01 przez img06).",
        "opis_tresci": "Zbiór zniszczonych fragmentów notatek i listów z archiwum Głuchowskich. Częściowo nieczytelne z powodu uszkodzeń.",
        "seria": "VI",
        "tworca": "nieznany",
        "jezyk": "polski",
        "kontekst": "Zniszczone fragmenty korespondencji — świadectwo trudnych losów archiwum rodzinnego. Częściowa destrukcja dokumentów mogła nastąpić podczas wojny, transportu na emigrację lub w wyniku niewłaściwego przechowywania.",
        "powiazania": [],
        "stan": "Zły — fragmenty zniszczone, częściowo nieczytelne"
    },

    # === p15 — medal fizyczny ===
    {
        "sygn": "ARG/II/64",
        "photo": "galeria/galeria_p15_img01.jpeg",
        "tytul": "Medal 'NA POLU CHWAŁY 1920' (Krzyż Walecznych za Wojnę 1920) + insygnia wojskowe — galon, baretka",
        "data": "po 1920",
        "typ": "medal",
        "opis_fizyczny": "Zestaw insygniów: (1) galeria_p15_img01: brązowy medal krzyżowy z inskrypcją 'NA POLU CHWAŁY 1920', wstążka bordo-kremowa (bordowy środek, kremowe paski boczne) — Krzyż Walecznych lub Medal Pamiątkowy za Wojnę 1919–1921. (2) galeria_p15_img02 (jest to oddzielna karta z zdjęcia galeria_p13_img03): trzy elementy insygniów — długi srebrno-szary ryngraf/lanyard z plecionką diamentową (oficerski), krótszy złoty galon (dystynkcja stopnia), mała baretka wstążki bordo-kremowej (Krzyż Walecznych). 2 zdjęcia.",
        "opis_tresci": "Medal z inskrypcją 'NA POLU CHWAŁY 1920' — fizyczny Krzyż Walecznych lub Medal Pamiątkowy za Wojnę Polsko-Bolszewicką 1919–1921. Gen. Głuchowski jako dowódca szwadronu w 1. Pułku Ułanów w wojnie 1920 r. odznaczony trzykrotnie Krzyżem Walecznych. Medal z oryginalną wstążką bordo-kremową. Insygnia dodatkowe: lanyard oficerski (sznur dystynkcyjny), galon na naramiennik, baretka KW — komplet elementów uniformu generalskiego.",
        "seria": "II",
        "tworca": "Mennica Państwowa, Warszawa",
        "jezyk": "n/a",
        "kontekst": "UNIKALNE ARTEFAKTY TRÓJWYMIAROWE. Krzyż Walecznych — najważniejsze polskie odznaczenie bojowe, nadawane za męstwo w walce. Inskrypcja 'NA POLU CHWAŁY 1920' identyfikuje ten egzemplarz jako nadany za wojnę polsko-bolszewicką. Gen. Głuchowski — trzykrotny kawalerowie KW — dowodził szwadronu 1 P.U. w bitwach 1920 r., w tym w pościgu za armią Budionnego. Sznur dystynkcyjny oficerski (lanyard z plecionką diamentową) i galon to elementy munduru, które przetrwały wraz z medalem — komplet osobistych pamiątek oficerskich najwyższej wartości muzealnej i sentymentalnej.",
        "powiazania": ["ARG/II/62", "ARG/II/1", "ARG/V/162"],
        "stan": "Dobry — wstążka lekko wyblakła, lanyard w dobrym stanie"
    },

    # === p16 — dokumenty jenieckie ===
    {
        "sygn": "ARG/V/163",
        "photo": "galeria/galeria_p16_img01.jpeg",
        "tytul": "Karta ewidencyjna jeńca (Personalkarte) Krzysztofa Głuchowskiego — Stalag XI B Fallingbostel, 1944–45",
        "data": "1944–1945",
        "typ": "dokument jeniecki",
        "opis_fizyczny": "Niemiecka karta ewidencyjna jeńca wojennego (Personalkarte) — formularz drukowany z rubrykami: GEFANGENEN (dane jeńca), Kommando (przydział komanda pracy), dane osobowe, Erkennungsmarke (nr identyfikacyjny). Widoczne wpisy odręczne: imię/nazwisko, data. Formularz na żółtawym papierze, format A4. 4 zdjęcia (galeria_p16_img01 — formularz główny, img02-04 — dodatkowe strony).",
        "opis_tresci": "Personalkarte (karta osobowa jeńca) Krzysztofa Głuchowskiego ze Stalagu XI B w Fallingbostel (Dolna Saksonia). Wg Kriegsgefangenenpost (ARG/V/170) numer jeńca: 0-1245, barak 20/4. Stalag XI B — jeden z największych obozów jenieckich w Niemczech, wyzwolony 16.IV.1945 przez wojska brytyjskie. Karta zawiera dane ewidencyjne, przydział do komanda pracy i historię pobytu w obozie.",
        "seria": "V",
        "tworca": "Wehrmacht / Administracja Stalagu XI B Fallingbostel",
        "jezyk": "niemiecki",
        "kontekst": "Stalag XI B Fallingbostel (NIE Stalag IV-B Mühlberg, jak podawano wcześniej — potwierdzone przez Kriegsgefangenenpost z kolekcji i biogram z 1995 r.). Obóz w Fallingbostel, Dolna Saksonia, mieścił ok. 95 000 jeńców różnych narodowości. Powstańcy warszawscy po kapitulacji (2.X.1944) byli traktowani jako jeńcy wojenni na mocy układu kapitulacyjnego. Krzysztof Głuchowski trafił tam jako 18-letni ułan AK. Karta jeniecka to kluczowy dokument identyfikacyjny — pozwala zweryfikować losy jeńca w niemieckich bazach danych (Arolsen Archives / ITS).",
        "powiazania": ["ARG/V/161", "ARG/V/162", "ARG/V/157"],
        "stan": "Średni"
    },

    # === WhatsApp_new — Aliens Registration gen. Janusza ===
    {
        "sygn": "ARG/II/65",
        "photo": "wa_aliens_reg_janusz_photo.jpeg",
        "tytul": "Aliens Registration gen. Janusza Głuchowskiego — strona ze zdjęciem i danymi osobowymi",
        "data": "ok. 1940–1949",
        "typ": "legitymacja",
        "opis_fizyczny": "Dokument Aliens Registration — strona ze zdjęciem. Zdjęcie na niebieskiej sofie, wymagane rembg.",
        "opis_tresci": "Aliens Registration Certificate A 274782 — strona ze ZDJĘCIEM gen. Głuchowskiego (starszy mężczyzna, łysy, z wąsem). Dane: Nationality: Polish. Born: 6.8.88 (6 sierpnia 1888). Birthplace: Bukowina. Occupation: No occupation. Status: Married. Wife: Elizabeth [?]. Address: [...] College [...]. Previous residence: Palestine [?]. Service: Polish Forces, Aug 1940. PMC [?] 22/6/[?], discharged 29/6/49. Passport: Army Form W.M.06, P 5993. Podpis odręczny: Janusz Głuchowski.",
        "seria": "II",
        "tworca": "Home Office / UK",
        "jezyk": "angielski",
        "kontekst": "JEDYNE ZNALEZIONE ZDJĘCIE gen. Głuchowskiego w kolekcji (poza oficjalnymi). Mężczyzna łysy z wąsem. Dokument rejestracji cudzoziemca w Wielkiej Brytanii. Część kompletu: okładka (wa_aliens_reg_cover.jpeg), pieczątki (wa_aliens_reg_stamps.jpeg), zwolnienie (wa_aliens_reg_exempt.jpeg).",
        "powiazania": ["ARG/II/66", "ARG/II/1"],
        "stan": "Dobry — niebieska sofa w tle, wymaga rembg"
    },
    {
        "sygn": "ARG/II/66",
        "photo": "wa_aliens_reg_cover.jpeg",
        "tytul": "Aliens Registration — okładka, pieczątki i zwolnienie",
        "data": "ok. 1940–1949",
        "typ": "legitymacja",
        "opis_fizyczny": "Okładka dokumentu Aliens Registration + strony z pieczątkami i zwolnieniem. Trzy zdjęcia: wa_aliens_reg_cover.jpeg, wa_aliens_reg_stamps.jpeg, wa_aliens_reg_exempt.jpeg.",
        "opis_tresci": "Okładka: 'A 274782 / Aliens Order, 1920 / CERTIFICATE OF REGISTRATION'. Strona pieczątek: Police serial No. 87[?]2578, pieczęć Metropolitan Police — Aliens Registration, data 2 FEB 1951, notatki z 15/9/55 i 26.9.86 (prowadzony ponad 40 lat!). Strona zwolnienia: 'ALIENS ORDER, 1940. The holder is EXEMPT FROM REGISTRATION with the police but should retain this certificate.' Pieczęć: METROPOLITAN POLICE OFFICE, CHECKED.",
        "seria": "II",
        "tworca": "Home Office / UK",
        "jezyk": "angielski",
        "kontekst": "Komplet dokumentu rejestracji cudzoziemca gen. Janusza Głuchowskiego w Wielkiej Brytanii. Nr A 274782. Pieczątki Metropolitan Police potwierdzają ciągłą rejestrację od 1948 do 1986 (38 lat!). Ostateczne zwolnienie z obowiązku rejestracji (EXEMPT FROM REGISTRATION) — prawdopodobnie po uzyskaniu stałego pobytu. Generał, który dowodził dywizją kawalerii i był I Wiceministrem Spraw Wojskowych, musiał się cyklicznie meldować na policji jako 'alien' — wymowny symbol losu polskiej emigracji.",
        "powiazania": ["ARG/II/65"],
        "stan": "Dobry — niebieska sofa w tle, wymaga rembg"
    },

    # === WhatsApp_new — Krzyż AK Krzysztofa ===
    {
        "sygn": "ARG/V/164",
        "photo": "wa_krzyz_ak_juras.jpeg",
        "tytul": "Legitymacja Krzyża Armii Krajowej — Krzysztof Głuchowski 'Juraś', nr 3316, 7 p.ul. Jeleń",
        "data": "7.III.1968",
        "typ": "legitymacja",
        "opis_fizyczny": "Legitymacja odznaczeniowa, druk z odręcznymi wpisami. Zdjęcie na niebieskiej sofie, wymagane rembg.",
        "opis_tresci": "Legitymacja Krzyża AK nr 3316. Odbiorca: Głuchowski Krzysztof 'Juraś'. Jednostka: Z.W.Z. Komp. K. Plut. III/2, 7 Pułk Ułanów Lubelskich 'Jeleń'. Nadanie 1.VIII.1966, podpis gen. Bór-Komorowskiego. Wydano Londyn 7.III.1968, podpis K. Ziemski 'Wachnowski'.",
        "seria": "V",
        "tworca": "Koło byłych żołnierzy AK / Londyn",
        "jezyk": "polski",
        "kontekst": "Krzyż AK — odznaczenie za służbę w Armii Krajowej. Podpis gen. Bór-Komorowskiego (Naczelny Wódz) podnosi wartość. Nr 3316. 7 Pułk Ułanów 'Jeleń' — jednostka Powstania Warszawskiego, sektor Mokotów. Komplet z okładką: wa_krzyz_ak_okladka.jpeg (symbol PW).",
        "powiazania": ["ARG/V/165", "ARG/V/3", "ARG/V/9"],
        "stan": "Dobry — niebieska sofa w tle, wymaga rembg"
    },
    {
        "sygn": "ARG/V/165",
        "photo": "wa_krzyz_ak_okladka.jpeg",
        "tytul": "Okładka legitymacji Krzyża AK — symbol Polski Walczącej",
        "data": "7.III.1968",
        "typ": "legitymacja",
        "opis_fizyczny": "Okładka legitymacji z symbolem PW (Polska Walcząca). Zdjęcie na niebieskiej sofie.",
        "opis_tresci": "Okładka legitymacji Krzyża Armii Krajowej z symbolem Polski Walczącej. W komplecie z ARG/V/164.",
        "seria": "V",
        "tworca": "Koło byłych żołnierzy AK / Londyn",
        "jezyk": "polski",
        "kontekst": "Symbol PW na okładce — ikonografia Polskiego Państwa Podziemnego.",
        "powiazania": ["ARG/V/164"],
        "stan": "Dobry — niebieska sofa w tle, wymaga rembg"
    },

    # === WhatsApp_new — Weryfikacja AK 1946 ===
    {
        "sygn": "ARG/VI/23",
        "photo": "wa_weryfikacja_ak_1946.jpeg",
        "tytul": "Dokument Komisji Weryfikacyjnej AK, 2 Korpus, 1946",
        "data": "1946",
        "typ": "dokument wojskowy",
        "opis_fizyczny": "Dokument urzędowy, maszynopis. Zdjęcie na niebieskiej sofie, wymagane rembg.",
        "opis_tresci": "7 PUŁK UŁANÓW LUBELSKICH / DOWÓDZTWO 2 KORPUSU / KOMISJA WERYFIKACYJNA A.K. Kp. dnia 18.VII.1946. L.dz. 4/I/X/I/K/V/44. Na podstawie przedstawionych dowodów oraz rozkazu Dowódców Korpusu Nr 57 pkt 314 z dnia 6 maja 1946r., Komisja Weryfikacyjna A.K. przyznała dnia 12.XI.46 tytuł podchorążego: Plut. [...] 1944 NOWAKOWSKI MATEUSZ, rocznik 1926. Komisja Weryfikacyjna A.K. L.dz. 879/II/AK/46 przyznała tytuł podchorążego z zastrzeżeniem 'podlega przeszkoleniu'. Podpis: J. USZYCKI ppłk.",
        "seria": "VI",
        "tworca": "Komisja Weryfikacyjna AK / 2 Korpus / ppłk J. Uszycki",
        "jezyk": "polski",
        "kontekst": "Dokument weryfikacyjny AK dotyczący plut. NOWAKOWSKIEGO MATEUSZA (rocznik 1926) — NIE Głuchowskiego! Znaleziony w kolekcji Głuchowskich jako dokument porównawczy z tego samego procesu weryfikacyjnego. Ten sam 7 P.Uł.L., ta sama Komisja, ten sam okres (VII.1946). Podpisany przez ppłk. J. Uszyckiego — Przewodniczącego Komisji. Nowakowski — współtowarzysz Krzysztofa z plutonu 1112 (obaj rocznik 1926).",
        "powiazania": ["ARG/V/164"],
        "stan": "Dobry — niebieska sofa w tle, wymaga rembg"
    },

    # === WhatsApp_new — Portret rodzinny ===
    {
        "sygn": "ARG/II/67",
        "photo": "wa_portret_rodzinny_1920.jpeg",
        "tytul": "Portret rodzinny Głuchowskich — zdjęcie studyjne, ok. 1916–1920",
        "data": "ok. 1916–1920",
        "typ": "fotografia",
        "opis_fizyczny": "Formalna fotografia rodzinna na kartonie, sepia, format ok. 20×15 cm. Studio fotograficzne. 10 osób w dwóch rzędach: rząd tylny — 4 młodych mężczyzn (w garniturach lub mundurach); rząd przedni siedzący — oficer w mundurze brytyjskim(?) z czapką (lewy), dziewczynka, chłopiec, kobieta w białej bluzce (prawa), chłopiec w stroju harcerskim/skautowskim (skrajnie prawy). Zdjęcie na niebieskiej sofie/tkaninie w tle — wymaga rembg.",
        "opis_tresci": "Portret rodziny Głuchowskich z okresu I wojny światowej lub bezpośrednio po. Oficer w mundurze (siedzący po lewej) — prawdopodobnie Marian Głuchowski (ojciec, Seria I) lub inny mężczyzna z rodziny w mundurze. Kobieta w bieli — żona (Maria z Żółkowskich?). Młodzi mężczyźni z tyłu mogą obejmować: Janusza (ur. 1888, miałby 28–32 lata), Stefana (ur. 1893, 23–27 lat), Lecha (ur. 1918 — ale zbyt mały). Chłopiec w stroju harcerskim — datowanie po 1916 (harcerstwo polskie). Identyfikacja wymaga porównania z innymi zdjęciami w kolekcji.",
        "seria": "II",
        "tworca": "studio fotograficzne (nieznane)",
        "jezyk": "—",
        "kontekst": "Portret rodzinny — kluczowy dokument genealogiczny. Rodzina Głuchowskich: Marian (ojciec, Seria I) + Maria z Żółkowskich + synowie (Janusz, Stefan, Lech, Krzysztof + ewentualne córki). Strój harcerski jednego z chłopców datuje zdjęcie na po 1916 (powstanie polskiego harcerstwa). Mundur oficera sugeruje okres I wojny lub pierwszych lat II RP. Porównanie twarzy z karykaturą Hertza-Barwińskiego (ARG/II/59) mogłoby pomóc zidentyfikować Janusza na zdjęciu.",
        "powiazania": ["ARG/II/65", "ARG/II/1", "ARG/I/1", "ARG/II/59"],
        "stan": "Średni — sepia, niebieska sofa w tle (wymaga rembg)"
    },

    # === WhatsApp_new — Biogram Krzysztofa 1995 ===
    {
        "sygn": "ARG/V/166",
        "photo": "wa_biogram_krzysztof_1995.jpeg",
        "tytul": "Biogram Krzysztofa Głuchowskiego ps. 'Juraś' — autobiografia maszynopisowa, Rio de Janeiro 18.X.1995",
        "data": "18.X.1995",
        "typ": "maszynopis",
        "opis_fizyczny": "Maszynopis na papierze A4, jedna pełna strona gęstego tekstu. Nagłówek: 'KRZYSZTOF GŁUCHOWSKI PSEUDONIM «JURAŚ»'. Podpis na dole: 'Krzysztof Głuchowski, Rio de Janeiro, 18 października 1995'. Treść podzielona na dwa bloki: biografia narracyjna i bibliografia (publikacje i archiwalia). Papier biały, maszynopis czarny.",
        "opis_tresci": "Autobiografia Krzysztofa Głuchowskiego: ur. 29.XI.1926 w Warszawie, syn Stanisława Stefana i Wandy z Głuchowskich. Ukończył 6 klas Szkoły Rodziny Wojskowej (do VI.1939). Jesienią 1943 uciekł z domu do ZWZ/AK. W Armii Krajowej — 7 P.U.L. AK 'Jeleń' kpr. Kadecki. 1.VIII.1944 — natarcie na Kadecką i Mokotów. Dywizjon 'Jeleń' na Starówce, następnie przejście kanałami. Kapitulacja — jeniec Stalagu XI B (Fallingbostel, nr 0-1245). Po wyzwoleniu Anglia. Emigracja do Brazylii: inżynier, Project Engineer, Sales Engineering Manager. W Londynie: Koło Żołnierzy Krzysztof Kierownictwa Starzyczkowa, członek Naczelnej Rady AHP, członek Zarządu Zjednoczenia Polskiego w Brazylii. Bibliografia: 'Ułan Lubelski' (od 1947), Komunikat Informacyjny Koła 7 P.U.L., Bellona, 'Powstanie Warszawskie' (Borkiewicz), 135 Pluton AK.",
        "seria": "V",
        "tworca": "Krzysztof Głuchowski (autobiografia)",
        "jezyk": "polski",
        "kontekst": "KLUCZOWY DOKUMENT ŹRÓDŁOWY — autobiografia napisana przez Krzysztofa na 25 lat przed śmiercią. Weryfikuje fakty: Stalag XI B Fallingbostel (NIE IV-B Mühlberg!), nr jeńca 0-1245, uciekł do AK jesienią 1943 (nie 1942), walczył na Mokotowie i Starówce. Podaje kompletną bibliografię publikacji i archiwaliów (BN Warszawa, Zbiór Rękopisów Nr 13853 — korespondencja z ojcem z Włoch). Adres londyński: 42 Emperors Gate, SW7 — ten sam co na liście do ambasady izraelskiej (ARG/V/159). Rio de Janeiro — ostatni okres życia Krzysztofa przed śmiercią ok. 2020.",
        "powiazania": ["ARG/V/164", "ARG/V/151", "ARG/V/163", "ARG/V/161", "ARG/V/162", "ARG/VI/24", "ARG/VI/25"],
        "stan": "Dobry"
    },

    # === WhatsApp_new — Biogram Lecha 1995 ===
    {
        "sygn": "ARG/VI/24",
        "photo": "wa_biogram_lech_1995.jpeg",
        "tytul": "Biogram rtm. Lecha Głuchowskiego ps. 'Iżycki' (ok. 1902–1944) — maszynopis Krzysztofa, Rio de Janeiro 18.X.1995",
        "data": "18.X.1995",
        "typ": "maszynopis",
        "opis_fizyczny": "Maszynopis A4, jedna pełna strona. Nagłówek: 'ROTMISTRZ LECH GŁUCHOWSKI PSEUDONIM «IŻYCKI»'. Podpis: 'Przygotował Krzysztof Głuchowski / Rio de Janeiro, 18 października 1995'. Dwa bloki: biografia narracyjna (~25 linii) + bibliografia (16 pozycji). Na dole przypis gwiazdkowy o gen. Januszu.",
        "opis_tresci": "Biogram Lecha Głuchowskiego (ur. ok. 1902 w Rakowcu, syn Mariana Głuchowskiego i Marty z Żółkiewskich). W 1918 roku miał 16 lat — uczestnik P.W. (pracy wolnościowej?). Szkoły średnie w Radomsku. Ukończył Akademię Rolniczą w Bydgoszczy (ok. 1932). We IX.1939 zmobilizowany do 7 P.U.L., kampania wrześniowa, walki nad Pilicą. We Francji — 10. Brygada Kawalerii Pancernej. W Anglii — AK kryptonim 'Jeleń', konspiracja w Londynie. Wrócił do okupowanej Polski. W 1944 dowódca plutonu/kompanii Dywizjon 'Jeleń' na Al. Szucha, następnie w grupie powstańczej na Mokotowie. 15 września 1944 — poległ w obronie pozycji na Mokotowie. Pochowany na cmentarzu parafialnym (tymczasowo), potem ekshumowany do grobu rodzinnego na cmentarzu na Powązkach(?). Awansowany do stopnia majora (pośmiertnie?). Odznaczenia: Krzyż Virtuti Militari, Krzyż Walecznych (×3), Złoty Krzyż Zasługi z Mieczami, Medal Wojska, Krzyż Armii Krajowej (Nr 1 specjalna seria z 6,67 kolejnych podpisem gen. Bora-Komorowskiego i Prezydenta RP). Bibliografia: 16 pozycji, w tym Bellona (Londyn 1953), Borkiewicz 'Powstanie Warszawskie' (1957), 'Łam i Lubelscy' (Londyn 1969), Żołnierze Mokotowa 1944 (MON 1971), 135 Pluton AK (1994), Dziennik Polski (Londyn, 5 not 1991-92). Archiwum: BN Warszawa, Zbiór Rękopisów Nr 13853. Przypis: '*Później I wice minister Spraw Wojskowych, i dowódca Jednostek Wojska w Wielkiej Brytanii, generał dywizji' — dot. gen. Janusza.",
        "seria": "VI",
        "tworca": "Krzysztof Głuchowski",
        "jezyk": "polski",
        "kontekst": "CZWARTY SYN MARIANA: Lech Głuchowski (ok. 1902–15.IX.1944) — brat Janusza (1888) i Stefana (1893), STRYJ Krzysztofa 'Jurasia'. Rotmistrz kawalerii, weteran kampanii wrześniowej (7 P.U.L.), Francji (10. BKP) i Anglii. Wrócił do okupowanej Polski i walczył w AK 'Jeleń'. Poległ na Mokotowie 15 września 1944 w Powstaniu Warszawskim. Odznaczony Krzyżem Virtuti Militari — najwyższe polskie odznaczenie wojskowe. Krzyż AK Nr 1 z podpisem gen. Bora-Komorowskiego. TRZY BRACIA w walce: Janusz (generał PSZ w Anglii), Stefan (AK Żoliborz, Pawiak), Lech (AK Mokotów, poległ). Biogram spisany przez Krzysztofa w tym samym dniu (18.X.1995) co autobiografia i biogram Stefana — systematyczna praca dokumentacyjna w Rio de Janeiro. Dedykacja od Lecha do Stefana zachowana w kolekcji (ARG/VI/28).",
        "powiazania": ["ARG/V/166", "ARG/VI/25", "ARG/I/1"],
        "stan": "Dobry"
    },

    # === WhatsApp_new — Biogram Stefana 1995 ===
    {
        "sygn": "ARG/VI/25",
        "photo": "wa_biogram_stefan_1995.jpeg",
        "tytul": "Biogram ppor. Stanisława Stefana Głuchowskiego ps. 'Stefan' — maszynopis Krzysztofa, Rio de Janeiro 18.X.1995",
        "data": "18.X.1995",
        "typ": "maszynopis",
        "opis_fizyczny": "Maszynopis A4, jedna pełna strona. Nagłówek: 'PPOR STANISŁAW STEFAN GŁUCHOWSKI PSEUDONIM «STEFAN»'. Podpis: 'Krzysztof Głuchowski, Rio de Janeiro, 18 października 1995'. Struktura: biografia + bibliografia + nota archiwalna.",
        "opis_tresci": "Biogram Stefana Głuchowskiego: ur. 1.5.1893 w Bukowcu pow. Piotrków, syn Mariana i Marii z Żółkowskich. Ukończył gimnazjum w Łodzi. PPS — praca podziemna, aresztowany. Ochotnik w 1918, na froncie 1920. Podchorąży Rezerwy Kawalerii. Urzędnik państwowy w Szefostwie Kolejnictwa. W WSOP Warszawa-Żolibork — szef 2-ej kompanii. 18.V.1944 aresztowany, przesłuchiwany na Al. Szucha, więziony na Pawiaku. Powstanie — z Mokotowa przez kanały. Kapitulacja — do Stalagu. Powrót do kraju 1945. Zmarł 17.X.1962 w Warszawie, pochowany na Powązkach (Seria 99-IV). Odznaczenia: Krzyż Niepodległości, Order Polonia Restituta, Krzyż Walecznych, Złoty Krzyż Zasługi, Srebrny Krzyż Zasługi, Krzyż AK (Nr 3720). Nota archiwalna: 'Komplet listów ppor. Stefana Głuchowskiego z Niemiec do syna Krzysztofa znajdującej się w 7 P.U.L. lib. od Siemion gen. Andersa we Włoszech, wraz z odwrotną korespondencją, z łożą się, w dziale 2giej Woj. Światowej w Archiwum Polskiej Akademii Nauk przy Rynku Starego Miasta w Warszawie. Biblioteka Narodowa w Warszawie Zbiór Rękopisów No. 13853.'",
        "seria": "VI",
        "tworca": "Krzysztof Głuchowski",
        "jezyk": "polski",
        "kontekst": "KLUCZOWY DOKUMENT GENEALOGICZNY — biogram Stefana spisany przez jego syna Krzysztofa w 1995. Potwierdza: Stefan (1893) i Janusz (1888) to BRACIA — obaj synowie Mariana i Marii z Ziółkowskich. Krzysztof 'Juraś' jest SYNEM Stefana i Wandy z Głuchowskich ps. 'Krysta' (nie Janusza!). ARCHIWA: korespondencja Stefana zdeponowana w BN Warszawa (Zbiór Rękopisów Nr 13853) i w Archiwum PAN przy Rynku Starego Miasta — te zbiory mogą uzupełnić kolekcję! Stefan aresztowany przez Gestapo 18.V.1944, więziony na Pawiaku, przesłuchiwany na Al. Szucha. Zwolniony 29.VII.1944 — 3 dni przed Powstaniem! W AK: z-ca d-cy kompanii w S.O.P. Warszawa-Żoliborz. Krzyż AK nr 3720. Pochowany na Powązkach kw. 99-IV-19.",
        "powiazania": ["ARG/VI/24", "ARG/V/166", "ARG/III/1"],
        "stan": "Dobry"
    },

    # === WhatsApp_new — Kriegsgefangenenpost (przeniesiony z V/170 → III/38 — dot. Stefana) ===
    {
        "sygn": "ARG/III/38",
        "photo": "wa_kriegsgefangenenpost.jpeg",
        "tytul": "Kriegsgefangenenpost — Rückantwortbrief DO ppor. Stanisława Stefana Głuchowskiego, Stammlager XI B, barak 201/4",
        "data": "5.I.1945",
        "typ": "korespondencja jeniecka",
        "opis_fizyczny": "Formularz Kriegsgefangenenpost (poczta jeniecka) — Rückantwortbrief (odpowiedź zwrotna). Druk z odręcznymi wpisami. Nagłówek: 'Kriegsgefangenenpost / Rückantwortbrief / 5/1/45'. Adresat (An den Kriegsgefangenen): 'epr.[?] Stanisław / Stefan Głuchowski', Gefangenennummer 0-1245, Lager-Bezeichnung M.-Stammlager XI B, Barak 201/4, Deutschland (Allemagne). Stempel pocztowy: RADOMSKO z datą 01.2.45(?). Sekcja nadawcy (Absender, odwrócony): 'Głuchowskiego Wiesława / por. Walerian(?) / kw. Kleczew II / pow. Radomsko'. Pieczęć cenzury okrągła '20'. Format A5.",
        "opis_tresci": "Formularz poczty jenieckiej — odpowiedź zwrotna wysłana DO ppor. Stefana Głuchowskiego (nr jeńca 0-1245) w Stalagu XI B Fallingbostel, barak 201/4. Nadawca z Kleczewa, pow. Radomsko — gmina w pobliżu rodzinnego majątku Głuchowskich (Bukowa, pow. Piotrków). UWAGA: nr jeńca 0-1245 to numer STEFANA (ojca), nie Krzysztofa (syn miał nr 141009). Stempel RADOMSKO potwierdza korespondencję z regionem rodzinnym.",
        "seria": "III",
        "tworca": "rodzina Głuchowskich z Kleczewa/Radomska (nadawca)",
        "jezyk": "niemiecki, polski",
        "kontekst": "Kriegsgefangenenpost — regulaminowa poczta jeniecka. Rückantwortbrief = odpowiedź na list jeńca. Nr jeńca 0-1245 to numer STEFANA (ppor. Stanisław Stefan Głuchowski), co zgadza się z ARG/III/1 (Kriegsgefangenenpost od Stefana z nr 0.1245). Krzysztof (syn) miał inny numer: 141009. Data 5.I.1945 — trzy miesiące przed wyzwoleniem Stalagu XI B (16.IV.1945). Kleczew, pow. Radomsko — gmina w pobliżu Bukowej (majątek rodzinny). Stefan i Krzysztof byli w TYM SAMYM Stalagu XI B Fallingbostel — ojciec w baraku 201/4, syn w innym baraku. Dwa pokolenia jeńców w jednym obozie. PRZENIESIONY z Serii V/170 do III/38 — dokument dotyczy Stefana, nie Krzysztofa.",
        "powiazania": ["ARG/III/1", "ARG/III/5", "ARG/V/163", "ARG/V/166"],
        "stan": "Średni — niebieska sofa w tle, wymaga rembg"
    },

    # === WhatsApp_new — Rękopis wspomnienia ===
    {
        "sygn": "ARG/V/167",
        "photo": "wa_rekopis_wspomnienia.jpeg",
        "tytul": "Rękopis wspomnieniowy Krzysztofa Głuchowskiego — relacja z Powstania Warszawskiego i Stalagu",
        "data": "XX w. (po 1945)",
        "typ": "rękopis",
        "opis_fizyczny": "Rękopis na papierze liniowanym, gęste pismo odręczne w języku polskim, co najmniej jedna strona. Pismo pochyłe, drobne, czytelne z bliska. Tekst narracyjny — wspomnieniowy, z datami i nazwiskami. Brak tytułu i sygnatury na stronie. Papier pożółkły, ślady zagięć.",
        "opis_tresci": "Rękopiśmienna relacja wspomnieniowa — prawdopodobnie autorstwa Krzysztofa Głuchowskiego. Tekst opisuje wydarzenia z okresu WWII — wzmiankowane daty, miejsca, nazwiska. Gęsty zapis narracyjny sugeruje fragment obszerniejszych wspomnień lub materiał przygotowawczy do jednej z publikacji Krzysztofa (np. do 135 Pluton AK lub artykułów w 'Ułanie Lubelskim'). Wymaga pełnej transkrypcji.",
        "seria": "V",
        "tworca": "Krzysztof Głuchowski (prawdopodobnie)",
        "jezyk": "polski",
        "kontekst": "Krzysztof Głuchowski był aktywnym autorem wspomnień i publikacji historycznych — biogram z 1995 (ARG/V/166) wymienia: artykuły w 'Ułanie Lubelskim' (od 1947), materiały do 'Powstanie Warszawskie' (Borkiewicz), współautorstwo '135 Pluton AK'. Ten rękopis może być brudnopisem jednej z tych publikacji lub niepublikowaną relacją. Archiwum PAN i BN (Zbiór Rękopisów Nr 13853) mają inne rękopisy Krzysztofa — porównanie pisma mogłoby potwierdzić autorstwo.",
        "powiazania": ["ARG/V/166", "ARG/V/151"],
        "stan": "Średni — pożółkły, zagięcia"
    },

    # === Downloads/gluchowski — Stefan Głuchowski (stefan_001–019) ===
    {
        "sygn": "ARG/III/10",
        "photo": "stefan_001.jpeg",
        "tytul": "Zarządzenie Prezesa Rady Ministrów — Komisja Dyscyplinarna, 1929",
        "data": "6.III.1929",
        "typ": "dokument urzędowy",
        "opis_fizyczny": "Maszynopis na papierze firmowym 'PREZES RADY MINISTRÓW', format A4, 1 karta. Nagłówek z orłem II RP. Nr 3743. Papier biurowy, pożółkły, ślady zginania.",
        "opis_tresci": "'PREZES RADY MINISTRÓW / Warszawa, dnia 6 marca 1929 r. / Nr 3743 / Wyższa Komisja Dyscyplinarna przy Prezydium Rady Ministrów / ZARZĄDZENIE WSTĘPNE / Do Wyższej Komisji Dyscyplinarnej (...) następujący dla urzędników i funkcjonarjuszów niższych Prezydium Rady Ministrów, Kancelarii Cywilnej Prezydenta Rzeczypospolitej, Drukarni Państwowych (...) powołuję na okres trzech lat.' Lista członków komisji: na przewodniczącego p. Jana Kantego Pietaka, Szefa Biura PRM; członkowie: Władysław Paconni, Dr Irydion Karłowski, Bolesław Naczke, Henryk Turwiński, August Janiecki, Dr Zygmunt Skarszewski, Jan Ruchowski.",
        "seria": "III",
        "tworca": "Prezes Rady Ministrów (Kazimierz Bartel, 1929)",
        "jezyk": "polski",
        "kontekst": "Zarządzenie o powołaniu Komisji Dyscyplinarnej dla urzędników m.in. Kancelarii Cywilnej Prezydenta RP — instytucji, w której pracował Stefan Głuchowski. Prezes RM w III.1929 — prof. Kazimierz Bartel (zaufany Piłsudskiego, zamordowany przez Gestapo w 1941). Dokument potwierdza przynależność instytucjonalną Stefana do najwyższego szczebla administracji II RP — Kancelaria Cywilna Prezydenta Mościcki. Stefan musiał być obecny na liście podległych urzędników.",
        "powiazania": ["ARG/III/1", "ARG/III/11", "ARG/III/12"],
        "stan": "Średni — pożółkły, ślady zginania"
    },
    {
        "sygn": "ARG/III/11",
        "photo": "stefan_002.jpeg",
        "tytul": "Dyplom Brązowego Medalu za Długoletnią Służbę — Stefan Głuchowski, 1938",
        "data": "14.V.1938",
        "typ": "dyplom",
        "opis_fizyczny": "Dyplom urzędowy na papierze firmowym 'KANCELARIA CYWILNA PREZYDENTA RZECZYPOSPOLITEJ', format A4. Druk z odręcznym wpisem imienia i nazwiska, pieczęć urzędowa, podpis Szefa Kancelarii Cywilnej. Papier kremowy, plamy wilgoci u dołu.",
        "opis_tresci": "'KANCELARIA CYWILNA PREZYDENTA RZECZYPOSPOLITEJ / DYPLOM / Na podstawie ustawy z dnia 8 stycznia 1938 roku (Dz. U. R. P. Nr 3, Poz. 11) nadaję P. STEFANOWI GŁUCHOWSKIEMU, Kierownikowi Referatu w Kancelarii Cywilnej Prezydenta Rzeczypospolitej / BRĄZOWY MEDAL ZA DŁUGOLETNIĄ SŁUŻBĘ / Warszawa, dnia 14 maja 1938 r. / [podpis] Szef Kancelarii Cywilnej.'",
        "seria": "III",
        "tworca": "Szef Kancelarii Cywilnej Prezydenta RP",
        "jezyk": "polski",
        "kontekst": "Medal za Długoletnią Służbę — ustanowiony ustawą z 8.I.1938. Brązowy = 10+ lat nienagannej służby. Stefan pracował w Kancelarii Cywilnej od ok. 1921 — w 1938 miał już 17 lat stażu. Tytuł 'Kierownik Referatu' = stanowisko kierownicze w administracji prezydenckiej. Kancelaria Cywilna Prezydenta RP — najwyższy organ administracji cywilnej II RP, obsługujący prezydenta Ignacego Mościckiego (1926–1939). Stefan był bratem gen. Janusza — obaj na szczytach państwa: jeden wojskowy (I Wiceminister), drugi cywilny (Kancelaria Prezydenta).",
        "powiazania": ["ARG/III/10", "ARG/III/12", "ARG/III/1"],
        "stan": "Średni — plamy wilgoci u dołu"
    },
    {
        "sygn": "ARG/III/12",
        "photo": "stefan_003.jpeg",
        "tytul": "Dyplom Złotego Krzyża Zasługi — Stefan Głuchowski, 1936",
        "data": "11.XI.1936",
        "typ": "dyplom",
        "opis_fizyczny": "Ozdobny dyplom dużego formatu, kaligrafia dekoracyjna z inicjałami. Druk na grubym papierze czerpanym. Herb Rzeczypospolitej, pieczęć, podpisy: Prezes Rady Ministrów + Szef Kancelarii Cywilnej. Pożółkły, ślady wilgoci, ale tekst w pełni czytelny.",
        "opis_tresci": "'Rzeczpospolita Polska / PREZYDENT RZECZYPOSPOLITEJ / PREZES RADY MINISTRÓW / STWIERDZA / NADAŁ / STANISŁAWOWI STEFANOWI GŁUCHOWSKIEMU / KIEROWNIKOWI REFERATU KANCELARII CYWILNEJ P.R.P. / ZARZĄDZENIEM Z DNIA 11 LISTOPADA 1936 r. / ZŁOTY KRZYŻ ZASŁUGI / PO RAZ PIERWSZY / ZA ZASŁUGI W SŁUŻBIE PAŃSTWOWEJ / [podpis] Prezes Rady Ministrów / [podpis] Szef Kancelarii Cywilnej.'",
        "seria": "III",
        "tworca": "Prezydent RP Ignacy Mościcki / Prezes RM (Felicjan Sławoj Składkowski, 1936)",
        "jezyk": "polski",
        "kontekst": "Złoty Krzyż Zasługi — jedno z najwyższych odznaczeń cywilnych II RP, nadawany za wybitne zasługi w służbie państwowej. Data 11.XI.1936 — Święto Niepodległości, tradycyjny dzień nadawania odznaczeń. Prezes RM w XI.1936 = gen. Felicjan Sławoj Składkowski. Stefan Głuchowski = 'Kierownik Referatu Kancelarii Cywilnej Prezydenta Rzeczypospolitej Polskiej' — STANOWISKO KIEROWNICZE w osobistym biurze prezydenta Mościckiego. Bracia Głuchowscy — podwójne szczyty II RP: Janusz jako I Wiceminister Spraw Wojskowych (1935–39), Stefan jako Kierownik w Kancelarii Prezydenta. Rodzina u SAMEGO szczytu państwa.",
        "powiazania": ["ARG/III/11", "ARG/III/10", "ARG/III/19"],
        "stan": "Dobry — czytelny, ozdobny"
    },
    {
        "sygn": "ARG/III/13",
        "photo": "stefan_004.jpeg",
        "tytul": "Pismo urzędowe dot. służby Stefana Głuchowskiego, 1933–34",
        "data": "ok. 1933–1934",
        "typ": "dokument urzędowy",
        "opis_fizyczny": "Pismo urzędowe, maszynopis.",
        "opis_tresci": "Pismo urzędowe dotyczące służby Stefana Głuchowskiego w Kancelarii Cywilnej Prezydenta RP, lata 1933–1934.",
        "seria": "III",
        "tworca": "Kancelaria Cywilna Prezydenta RP",
        "jezyk": "polski",
        "kontekst": "Dokumentacja służbowa Stefana Głuchowskiego — element teczki personalnej urzędnika II RP.",
        "powiazania": ["ARG/III/1"],
        "stan": "Średni"
    },
    {
        "sygn": "ARG/III/14",
        "photo": "stefan_005.jpeg",
        "tytul": "Pismo Kancelarii Cywilnej Prezydenta RP do Stefana Głuchowskiego",
        "data": "ok. 1927–1935",
        "typ": "dokument urzędowy",
        "opis_fizyczny": "Maszynopis na papierze firmowym 'KANCELARIA CYWILNA PREZYDENTA RZECZYPOSPOLITEJ'. Format A4, jedna strona. Zdjęcie wykonane odwrócone (do góry nogami). Pismo maszynowe z odręcznym podpisem na dole. Papier pożółkły, ślady zginania.",
        "opis_tresci": "Pismo urzędowe z Kancelarii Cywilnej Prezydenta RP skierowane do Stefana Głuchowskiego. Dotyczy spraw kadrowych — prawdopodobnie nominacja, kwalifikacja lub awans w służbie państwowej. Podpis Szefa Kancelarii na dole dokumentu. Odniesienia do przepisów służbowych i kategorii płacowych. Sfotografowane odwrócone.",
        "seria": "III",
        "tworca": "Kancelaria Cywilna Prezydenta RP",
        "jezyk": "polski",
        "kontekst": "Komisje Kwalifikacyjne oceniały urzędników państwowych II RP pod kątem awansów i dalszego zatrudnienia.",
        "powiazania": ["ARG/III/13"],
        "stan": "Średni"
    },
    {
        "sygn": "ARG/III/15",
        "photo": "stefan_006.jpeg",
        "tytul": "Pismo z Rezydencji Prezydenckiej w Spale — znaczek myśliwski, 1930",
        "data": "2.XI.1930",
        "typ": "dokument urzędowy",
        "opis_fizyczny": "Pismo urzędowe na papierze firmowym 'ZARZĄD REZYDENCJI PREZYDENTA RZECZYPOSPOLITEJ W SPALE', format A4. Maszynopis z pieczęcią okrągłą i podpisem 'Zarządzający'. Numer: 232/109/32(?).",
        "opis_tresci": "'ZARZĄD REZYDENCJI PREZYDENTA RZECZYPOSPOLITEJ W SPALE / Spała, dn. 2 listopada 192[?] / Do Pana Stefana Głuchowskiego, Radcy Min., Kan.Cyw.Prezydenta R.P. / W WARSZAWIE / Zarząd Rezydencji w Spale przesyła Panu jako uczestnikowi w dniu Św. Huberta w Spale w r. 1930, znaczek pamiątkowy, wydany przez Pana Prezydenta Rzeczypospolitej.' Podpis: Zarządzający [rezydencją].",
        "seria": "III",
        "tworca": "Zarząd Rezydencji Prezydenta RP w Spale",
        "jezyk": "polski",
        "kontekst": "STEFAN GŁUCHOWSKI UCZESTNIKIEM POLOWANIA PREZYDENCKIEGO! Polowanie hubertusowe w Spale (Św. Hubert = 3 XI, patron myśliwych) — ekskluzywna impreza prezydencka, zarezerwowana dla najbliższego otoczenia prezydenta Mościckiego. Spała — dawna carskie łowisko, po 1918 rezydencja letnia Prezydenta RP. Stefan tytułowany 'Radca Ministerialny' — wyższy stopień urzędniczy niż 'Kierownik Referatu'. Znaczek pamiątkowy 'wydany przez Pana Prezydenta' = osobisty upominek Mościckiego dla uczestników polowania. Potwierdza BLISKI DOSTĘP Stefana do Prezydenta — nie tylko służbowy, ale i towarzyski.",
        "powiazania": ["ARG/III/1", "ARG/III/10", "ARG/III/11", "ARG/III/12"],
        "stan": "Dobry — czytelny, papier firmowy z nagłówkiem"
    },
    {
        "sygn": "ARG/III/16",
        "photo": "stefan_007.jpeg",
        "tytul": "Zawiadomienie o nadaniu Krzyża Niepodległości — Stefan Głuchowski, 9.XI.1931",
        "data": "9.XI.1931",
        "typ": "dokument urzędowy",
        "opis_fizyczny": "Pismo urzędowe na papierze firmowym 'KOMITET KRZYŻA I MEDALU NIEPODLEGŁOŚCI', format A4. Maszynopis z odręcznym wpisem nazwiska. Nr 3/1062. Podpis: Kierownik Biura Komitetu P. Sygnowski.",
        "opis_tresci": "'KOMITET KRZYŻA I MEDALU NIEPODLEGŁOŚCI / Nr 3/1062 / Pan GŁUCHOWSKI Stefan / w miejscu / Zarządzeniem Pana Prezydenta Rzeczypospolitej Polskiej z dn. 9 Listopada 1931 r. został Pan odznaczony KRZYŻEM NIEPODLEGŁOŚCI.' Dalej: prośba o wpłacenie na PKO wartości odznaczenia i wypełnienie kwestionariusza.",
        "seria": "III",
        "tworca": "Komitet Krzyża i Medalu Niepodległości / Kierownik Biura P. Sygnowski",
        "jezyk": "polski",
        "kontekst": "KRZYŻ NIEPODLEGŁOŚCI — jedno z NAJWYŻSZYCH odznaczeń II RP, nadawane za walkę o niepodległość Polski w latach 1914–1921. Nadawany dekretem Prezydenta RP. Stefan Głuchowski kwalifikował się jako członek PPS i uczestnik walk niepodległościowych. Data 9.XI.1931 = dzień przed Świętem Niepodległości. Stefan odznaczony TEGO SAMEGO DNIA co Order Odrodzenia Polski (ARG/III/17)! Podwójne wyróżnienie w jednym dniu — rzadkość nawet wśród zasłużonych urzędników.",
        "powiazania": ["ARG/III/1", "ARG/III/17", "ARG/III/12", "ARG/VI/25"],
        "stan": "Dobry — czytelny, pieczęć wyraźna"
    },
    {
        "sygn": "ARG/III/17",
        "photo": "stefan_008.jpeg",
        "tytul": "Zawiadomienie o nadaniu Kawalerii Orderu Odrodzenia Polski — Stefan Głuchowski, 1931",
        "data": "12.XI.1931",
        "typ": "dokument urzędowy",
        "opis_fizyczny": "Pismo urzędowe na papierze firmowym 'KANCELARIA ORDERU «ODRODZENIA POLSKI»', format A4. Maszynopis z ozdobnym nagłówkiem, podpis Kanclerza Orderu. Papier kremowy, pożółkły.",
        "opis_tresci": "'KANCELARIA ORDERU «ODRODZENIA POLSKI» / Do Pana STANISŁAWA STEFANA GŁUCHOWSKIEGO / Radcy Ministerialnego w Kancelarii Cywilnej Prezydenta Rzeczypospolitej w Warszawie / Stwierdzam że Prezydent Rzeczypospolitej nadał dnia 9 listopada 1931 r. Panu / Kawalera / Krzyża Odrodzenia [Polski] / orderu / Warszawa, dnia 12 Listopada 1931.' Podpis Kanclerza Orderu.",
        "seria": "III",
        "tworca": "Kancelaria Orderu Odrodzenia Polski",
        "jezyk": "polski",
        "kontekst": "Order Odrodzenia Polski (Polonia Restituta) kl. V — Kawalera. Jedno z NAJWYŻSZYCH odznaczeń cywilnych II RP. Stefan tytułowany 'Radca Ministerialny w Kancelarii Cywilnej Prezydenta RP' — wyższy tytuł niż 'Kierownik Referatu', awans od czasu dyplomu ZKZ (1936). Nadanie 9.XI.1931 = ten sam dzień co Krzyż Niepodległości (ARG/III/16)! ŁAŃCUCH ODZNACZEŃ STEFANA: Srebrny KZ (1929) → Krzyż Niepodległości + Order Odrodzenia Polski (1931) → Złoty KZ (1936) → Brązowy Medal za Długoletnią Służbę (1938). Porównanie z bratem Januszem: obaj odznaczeni najwyżej w swoich sferach — Janusz: VM, KW z 2 okuc., Legia Honorowa; Stefan: Order Odrodzenia Polski, Krzyż Niepodległości, ZKZ.",
        "powiazania": ["ARG/III/12", "ARG/III/16", "ARG/III/19"],
        "stan": "Dobry — czytelny"
    },
    {
        "sygn": "ARG/III/18",
        "photo": "stefan_009.jpeg",
        "tytul": "Pismo Kancelarii Cywilnej Prezydenta — nominacja/awans Stefana, 31 grudnia",
        "data": "31.XII. (ok. 1927–1935)",
        "typ": "dokument urzędowy",
        "opis_fizyczny": "Maszynopis na papierze firmowym 'KANCELARIA CYWILNA PREZYDENTA RZECZYPOSPOLITEJ'. Format A4, jedna strona. Data: '31 grudnia 19[?]'. Zdjęcie odwrócone. Odręczny podpis na dole. Papier pożółkły ale czytelny.",
        "opis_tresci": "Pismo Kancelarii Cywilnej Prezydenta RP datowane 31 grudnia, skierowane do Stefana Głuchowskiego. Formuła 'na mocy postanowienia' — dotyczy oficjalnej nominacji, awansu lub przyznania odznaczenia. Odniesienie do 'zatwierdzenia' i przepisów służby cywilnej. Podpis Szefa Kancelarii.",
        "seria": "III",
        "tworca": "Kancelaria Cywilna Prezydenta RP",
        "jezyk": "polski",
        "kontekst": "Dokumentacja awansów urzędniczych — Stefan przechodził kolejne szczeble kariery w Kancelarii Prezydenta.",
        "powiazania": ["ARG/III/22", "ARG/III/1"],
        "stan": "Średni"
    },
    {
        "sygn": "ARG/III/19",
        "photo": "stefan_010.jpeg",
        "tytul": "Dyplom Srebrnego Krzyża Zasługi — Stanisław Stefan Głuchowski, 1929",
        "data": "6.III.1929",
        "typ": "dyplom",
        "opis_fizyczny": "Dyplom urzędowy na papierze firmowym 'PREZES RADY MINISTRÓW', z pieczęcią państwową. Format A4, maszynopis z odręcznym wpisem nazwiska. Pożółkły, czytelny.",
        "opis_tresci": "'PREZES RADY MINISTRÓW / Na zasadzie art. 5 ustawy z 23 czerwca 1923 r. (Dz. U. R. P. Nr 67, poz. 459) nadaję Panu po raz pierwszy / SREBRNY KRZYŻ ZASŁUGI / za zasługi w służbie państwowej / Do Pana STANISŁAWA STEFANA GŁUCHOWSKIEGO / Sekretarza w Kancelarii Cywilnej Prezydenta Rzeczypospolitej / w Warszawie.' Podpis Prezesa RM.",
        "seria": "III",
        "tworca": "Prezes Rady Ministrów (Kazimierz Bartel, 1929)",
        "jezyk": "polski",
        "kontekst": "Srebrny Krzyż Zasługi — PIERWSZE odznaczenie w łańcuchu odznaczeń Stefana. W 1929 Stefan miał tytuł 'Sekretarz' w Kancelarii Cywilnej — najniższy w jego udokumentowanej ścieżce awansów. PEŁNA KARIERA STEFANA: Sekretarz (1929) → Radca Ministerialny (1931) → Kierownik Referatu (1936–38). ODZNACZENIA: Srebrny KZ (1929) → Krzyż Niepodległości + Order Odrodzenia Polski V kl. (9.XI.1931) → Złoty KZ (11.XI.1936) → Brązowy Medal za Długoletnią Służbę (14.V.1938). Prezes RM w III.1929 = prof. Kazimierz Bartel (zamordowany przez Gestapo VII.1941).",
        "powiazania": ["ARG/III/12", "ARG/III/10", "ARG/III/16", "ARG/III/17"],
        "stan": "Dobry — czytelny"
    },
    {
        "sygn": "ARG/III/20",
        "photo": "stefan_011.jpeg",
        "tytul": "Pismo Kancelarii Cywilnej Prezydenta — dot. służby Stefana, 11 maja",
        "data": "11.V. (ok. 1925–1935)",
        "typ": "dokument urzędowy",
        "opis_fizyczny": "Maszynopis na papierze firmowym 'KANCELARIA CYWILNA PREZYDENTA RZECZYPOSPOLITEJ'. Format A4, jedna strona. Data: '11 maja 19[?]5'. Zdjęcie odwrócone. Odręczny podpis i adnotacje na dole. Papier pożółkły.",
        "opis_tresci": "Pismo Kancelarii Cywilnej Prezydenta RP datowane 11 maja, dotyczące warunków służby Stefana Głuchowskiego — prawdopodobnie zmiana kategorii płac, przeniesienie, lub zatwierdzenie stażu. Formuła urzędowa z powołaniem na przepisy.",
        "seria": "III",
        "tworca": "Kancelaria Cywilna Prezydenta RP",
        "jezyk": "polski",
        "kontekst": "Dokumentacja warunków służby urzędniczej w Kancelarii Prezydenta II RP.",
        "powiazania": ["ARG/III/1"],
        "stan": "Średni"
    },
    {
        "sygn": "ARG/III/21",
        "photo": "stefan_013.jpeg",
        "tytul": "Zatwierdzenie zatrudnienia Stefana Głuchowskiego jako Pomocnika Referenta — zaliczenie służby od 16.XII.1920",
        "data": "16.XI.1921",
        "typ": "dokument urzędowy",
        "opis_fizyczny": "Pismo urzędowe na papierze firmowym 'KANCELARJA CYWILNA NACZELNIKA PAŃSTWA'. Format A4, maszynopis z odręcznym podpisem. Okrągła niebieska pieczęć urzędowa z Orłem po lewej stronie. Papier pożółkły, czytelny mimo drobnych zabrudzeń. Ślady zginania.",
        "opis_tresci": "'KANCELARJA CYWILNA NACZELNIKA PAŃSTWA' — pismo skierowane 'Do Pana Stefana Głuchowskiego (Pomocnika Referenta) w Kancelarji Cywilnej'. Potwierdza postanowienie z dnia 16 listopada 1921 o zaliczeniu do służby państwowej od 16 grudnia 1920 r. z kategorią I. płac urzędników państwowych. Wzmianka o komisji dyscyplinarnej. Pieczęć okrągła, podpis Szefa Kancelarii.",
        "seria": "III",
        "tworca": "Kancelaria Cywilna Naczelnika Państwa",
        "jezyk": "polski",
        "kontekst": "Dokument potwierdza, że Stefan Głuchowski pracował jako 'Pomocnik Referenta' — najniższy szczebel urzędniczy. Służba zaliczona od 16.XII.1920 r. — co oznacza, że Stefan faktycznie rozpoczął pracę jeszcze PRZED formalnym listem zatrudnieniowym z 1.VII.1921 (ARG/III/23), prawdopodobnie na zasadzie wolontariatu lub stażu. To przesuwa początek kariery Stefana o pół roku wcześniej. Naczelnikiem Państwa w 1921 był Józef Piłsudski. Tytuł 'Pomocnik Referenta' odpowiadał kategoriom I-III płac w hierarchii urzędniczej II RP.",
        "powiazania": ["ARG/III/23", "ARG/III/22", "ARG/III/26", "ARG/III/1"],
        "stan": "Średni"
    },
    {
        "sygn": "ARG/III/22",
        "photo": "stefan_014.jpeg",
        "tytul": "Mianowanie Stefana Głuchowskiego urzędnikiem VIII stopnia służby cywilnej przez Prezydenta RP — 20.X.1926",
        "data": "20.X.1926",
        "typ": "nominacja",
        "opis_fizyczny": "Pismo nominacyjne na papierze firmowym 'KANCELARIA CYWILNA PREZYDENTA RZECZYPOSPOLITEJ'. Format A4, maszynopis z odręcznym podpisem Szefa Kancelarii Cywilnej. Duża okrągła pieczęć z czerwonego laku (pieczęć Prezydenta RP) w dolnej części. Papier pożółkły, ślady wilgoci i zabrudzeń, ale tekst czytelny.",
        "opis_tresci": "'KANCELARIA CYWILNA PREZYDENTA RZECZYPOSPOLITEJ' — 'Do Pana Stefana Głuchowskiego, urzędnika VIII-ej st.sł. w Kancelarji Cywilnej.' Pan Prezydent Rzeczypospolitej postanowieniem z dnia 20 października 1926 r. na zasadzie art. 116 ustawy o państwowej służbie cywilnej (Dz.U.R.P. Nr.21, Dz.101 z 1922 r.) mianował Pana w stopniu służby państwowej i zatwierdzeniem w VIII-go st.sł. w Kancelarji Cywilnej. Podpis: 'Szef Kancelarji Cywilnej' [podpis].",
        "seria": "III",
        "tworca": "Kancelaria Cywilna Prezydenta RP",
        "jezyk": "polski",
        "kontekst": "Nominacja na VIII stopień służby cywilnej — awans po 5-6 latach służby (od 1920). Prezydent RP w 1926 to Ignacy Mościcki (zaprzysiężony 4.VI.1926). Stopień VIII odpowiadał stanowisku 'Sekretarza' — co potwierdza ARG/III/19 (Srebrny KZ z 1929 adresowany do 'Sekretarza'). Pieczęć lakowa Prezydenta RP nadaje dokumentowi rangę aktu państwowego. Ustawa o służbie cywilnej z 1922 (Dz.U. Nr 21) regulowała hierarchię 12 stopni — VIII to szczebel średni-wyższy. Stefan awansował: Pomocnik Referenta (1920) → urzędnik VIII st.sł. / Sekretarz (1926) → Radca Ministerialny (1931) → Kierownik Referatu (1936–38).",
        "powiazania": ["ARG/III/23", "ARG/III/21", "ARG/III/19", "ARG/III/18", "ARG/III/17"],
        "stan": "Średni"
    },
    {
        "sygn": "ARG/III/23",
        "photo": "stefan_015.jpeg",
        "tytul": "List zatrudnieniowy — Stefan Głuchowski przyjęty na próbę do Kancelarii Cywilnej Naczelnika Państwa, 1.VII.1921",
        "data": "1.VII.1921",
        "typ": "pismo urzędowe",
        "opis_fizyczny": "Pismo urzędowe na papierze firmowym 'Kancelarja Cywilna Naczelnika Państwa', Nr 4626/21. Format A4, maszynopis z odręcznym podpisem Szefa Kancelarii Cywilnej. Okrągła pieczęć państwowa z Orłem (fioletowy tusz) w lewym dolnym rogu. Papier kremowy, dobry stan zachowania, ślady zginania. Druk u dołu: 'Drukarnia Państwowa Nr 1032, Ark.III. Nr 1000.'",
        "opis_tresci": "'Kancelarja Cywilna / Naczelnika Państwa / Nr 4626/21. / Warszawa, dn. 1.Lipca 1921 r. / Do / Pana Stefana Głuchowskiego / w/m, — Słuszewska 2 m.10. / W odpowiedzi na podanie z dn. 1.Lipca r.b. proszę Pana o objęcie posady w Kancelarji Cywilnej na czas próbny od 1.Lipca do 1.sierpnia 1921 r., z poborami odpowiadającemi kategorji I. płac urzędników państwowych. / Szef Kancelarji Cywilnej: [podpis]'",
        "seria": "III",
        "tworca": "Szef Kancelarii Cywilnej Naczelnika Państwa",
        "jezyk": "polski",
        "kontekst": "NAJWCZEŚNIEJSZY FORMALNY DOKUMENT Stefana Głuchowskiego — zatrudnienie na okres próbny (1 miesiąc: 1.VII–1.VIII.1921) w Kancelarii Cywilnej Naczelnika Państwa. Naczelnikiem był Józef Piłsudski (do 14.XII.1922). Adres Stefana: ul. Słuszewska 2 m.10, Warszawa (Mokotów). Kategoria I płac = najniższa stawka urzędnicza. Zatrudnienie 'na próbę' było standardową praktyką — po pomyślnym okresie próbnym Stefan został 'Pomocnikiem Referenta' (ARG/III/21 potwierdza służbę od 16.XII.1920 — co sugeruje wcześniejszy staż/wolontariat). Od tego dokumentu rozpoczyna się 18-letnia kariera Stefana w Kancelarii: Pomocnik Referenta (1920–21) → urzędnik VIII st.sł. (1926) → Sekretarz (1929) → Radca Ministerialny (1931) → Kierownik Referatu (1936–38). Stefan przetrwał zmianę ustroju: Naczelnik Państwa → Prezydent RP, pracując pod 2 prezydentami (Wojciechowski 1922–26, Mościcki 1926–39).",
        "powiazania": ["ARG/III/21", "ARG/III/22", "ARG/III/26", "ARG/III/24"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/III/24",
        "photo": "stefan_016.jpeg",
        "tytul": "Podwyżka kategorii płac Stefana Głuchowskiego — z kat. I do kat. II, od 1.XI.1921",
        "data": "1921",
        "typ": "pismo urzędowe",
        "opis_fizyczny": "Pismo urzędowe na papierze firmowym 'Kancelarja Cywilna', Nr 4546/21. Format A4, maszynopis z odręcznym podpisem Szefa Kancelarii Cywilnej. Okrągła pieczęć państwowa z Orłem (fioletowy tusz). Papier kremowy, ślady zginania, dobry stan.",
        "opis_tresci": "'Kancelarja Cywilna / Nr 4546/21' — 'Do Pana Stefana Głuchowskiego.' Na podstawie postanowienia Kancelarii Cywilnej... w myśl ustawy Państwa... przyznaje kategorję II według zasady płac od dnia 1.listopada 1921 r. Podpis: Szef Kancelarji Cywilnej.",
        "seria": "III",
        "tworca": "Kancelaria Cywilna Naczelnika Państwa",
        "jezyk": "polski",
        "kontekst": "Podwyżka z kategorii I (najniższej, przyznanej przy zatrudnieniu 1.VII.1921 — ARG/III/23) do kategorii II od 1.XI.1921 — po zaledwie 4 miesiącach służby. Szybki awans płacowy świadczy o dobrych wynikach pracy lub o rosnących obowiązkach. System kategorii płac urzędników II RP miał ok. 16 szczebli — awans z I na II to nadal niski poziom, ale sam fakt szybkiego przesunięcia jest znaczący.",
        "powiazania": ["ARG/III/23", "ARG/III/21"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/III/25",
        "photo": "stefan_017.jpeg",
        "tytul": "Pismo Kancelarii Cywilnej Prezydenta RP dot. uposażenia/stopnia Stefana Głuchowskiego",
        "data": "ok. 1926",
        "typ": "pismo urzędowe",
        "opis_fizyczny": "Pismo urzędowe na papierze firmowym 'KANCELARJA CYWILNA PREZYDENTA RZECZYPOSPOLITEJ'. Format A4, maszynopis z odręcznym podpisem Szefa Kancelarii Cywilnej. Okrągła pieczęć z czerwonego laku (pieczęć Prezydenta RP). Papier pożółkły, silne ślady wilgoci i zabrudzeń (szczególnie po prawej stronie), ślady zginania. Tekst częściowo nieczytelny z powodu uszkodzeń.",
        "opis_tresci": "'KANCELARJA CYWILNA PREZYDENTA RZECZYPOSPOLITEJ' — 'Do Pana Stefana Głuchowskiego, urzędnika w... st.sł. w Kancelarji...' Dotyczy postanowienia przy Kancelarii Cywilnej w sprawie kategorii/pensji. Pieczęć lakowa Prezydenta RP. Podpis Szefa Kancelarii Cywilnej. Dokument silnie uszkodzony — szczegóły treści częściowo nieczytelne.",
        "seria": "III",
        "tworca": "Kancelaria Cywilna Prezydenta RP",
        "jezyk": "polski",
        "kontekst": "Pismo z okresu prezydentury Mościckiego (po VI.1926). Związane z regulacją uposażenia po zmianie ustroju — Kancelaria Naczelnika Państwa (Piłsudski) została przekształcona w Kancelarię Prezydenta RP. Stefan kontynuował służbę bez przerwy. Dokument wymaga lepszego zdjęcia — silne uszkodzenia uniemożliwiają pełną transkrypcję.",
        "powiazania": ["ARG/III/22", "ARG/III/1"],
        "stan": "Średni"
    },
    {
        "sygn": "ARG/III/26",
        "photo": "stefan_018.jpeg",
        "tytul": "Formalne mianowanie Stefana Głuchowskiego Pomocnikiem Referenta Kancelarii Cywilnej — od 1.I.1922",
        "data": "31.XII.1921",
        "typ": "nominacja",
        "opis_fizyczny": "Pismo urzędowe na papierze firmowym 'KANCELARJA CYWILNA NACZELNIKA PAŃSTWA'. Format A4, maszynopis z odręcznym podpisem Szefa Kancelarii Cywilnej. Okrągła pieczęć państwowa z Orłem (fioletowy tusz). Papier kremowy, ślady zginania, dobry stan. Nr sprawy widoczny.",
        "opis_tresci": "'KANCELARJA CYWILNA NACZELNIKA PAŃSTWA' — 'Warszawa, dn. 31. Grudnia [1921] r.' — 'Do Pana STEFANA GŁUCHOWSKIEGO.' 'Na podstawie deczyzji z dnia 11 grudnia [1921] roku mianuję Pana Pomocnikiem Referenta Kancelarji Cywilnej z zaliczeniem do kategorji [?] płac urzędników państwowych od dnia 1 go Stycznia 1922 roku.' Podpis: 'Szef Kancelarji Cywilnej' [podpis].",
        "seria": "III",
        "tworca": "Szef Kancelarii Cywilnej Naczelnika Państwa",
        "jezyk": "polski",
        "kontekst": "Formalne mianowanie na stałe po pomyślnym okresie próbnym. Stefan rozpoczął pracę na próbę 1.VII.1921 (ARG/III/23), a teraz — po 6 miesiącach — otrzymuje stałe stanowisko 'Pomocnika Referenta' od 1.I.1922. Decyzja podjęta 11.XII.1921, pismo wystawione 31.XII.1921. To zamyka okres próbny i otwiera pełną karierę urzędniczą. 'Pomocnik Referenta' = najniższy szczebel hierarchii biurowej, ale w Kancelarii Naczelnika Państwa — to prestiżowa instytucja. Stefan miał wtedy 28 lat (ur. 1893).",
        "powiazania": ["ARG/III/23", "ARG/III/21", "ARG/III/24", "ARG/III/22"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/III/27",
        "photo": "stefan_019.jpeg",
        "tytul": "Przyznanie Medalu Dziesięciolecia Odzyskanej Niepodległości — ppor. Stanisław Stefan Głuchowski, 1929",
        "data": "ok. VI.1929",
        "typ": "pismo urzędowe",
        "opis_fizyczny": "Pismo urzędowe na papierze firmowym 'KANCELARJA CYWILNA PREZYDENTA RZECZYPOSPOLITEJ', Nr [...]/29. Format A4, maszynopis z odręcznym podpisem Szefa Kancelarii Cywilnej. Okrągła pieczęć państwowa z Orłem (czerwony tusz/lak). Papier pożółkły, ślady zginania, czytelny.",
        "opis_tresci": "'KANCELARJA CYWILNA PREZYDENTA RZECZYPOSPOLITEJ / Nr [...]/29' — 'Do Pana Stefana Głuchowskiego, urzędnika w Kancelarji Cywilnej Prezyd. Rzeczyp.' — 'Na podstawie § 6 rozporządzenia Rady Ministrów z dnia 27 września 1928 r. (Monitor Polski Nr 237 poz. 543) przyznaję Panu prawo do Medalu Dziesięciolecia Odzyskanej Niepodległości.' — 'SZEF KANCELARJI CYWILNEJ' [podpis].",
        "seria": "III",
        "tworca": "Szef Kancelarii Cywilnej Prezydenta RP",
        "jezyk": "polski",
        "kontekst": "Medal Dziesięciolecia Odzyskanej Niepodległości — odznaczenie ustanowione rozporządzeniem Rady Ministrów z 27.IX.1928 (Monitor Polski Nr 237, poz. 543). Nadawany urzędnikom i żołnierzom za zasługi w pierwszym dziesięcioleciu niepodległości (1918–1928). Stefan otrzymał go jako urzędnik Kancelarii Cywilnej z ok. 8-letnim stażem. Medal ten był jednym z najczęściej nadawanych odznaczeń II RP — szacuje się, że przyznano go kilkudziesięciu tysiącom osób. Dla Stefana stanowi kolejne potwierdzenie ciągłości służby państwowej. W chronologii odznaczeń: Medal Dziesięciolecia (1929) → Srebrny KZ (1929) → Krzyż Niepodległości + Order Odrodzenia Polski (1931) → Złoty KZ (1936) → Medal za Długoletnią Służbę (1938).",
        "powiazania": ["ARG/III/19", "ARG/III/10", "ARG/III/16", "ARG/III/12"],
        "stan": "Dobry"
    },

    # === Stefan — dokumenty wojenne i powojenne (stefan_020–031) ===
    {
        "sygn": "ARG/I/6",
        "photo": "stefan_020.jpeg",
        "tytul": "Biogram rtm. Lecha Jerzego Głuchowskiego ps. 'Jeżycki' (1902–1944) — dowódca 7 P.UŁ. 'Jeleń', poległ na Mokotowie",
        "data": "18.X.1995",
        "typ": "biogram/maszynopis",
        "opis_fizyczny": "Maszynopis na papierze A4, druk komputerowy. Tekst jednostronny z przypisami bibliograficznymi. Czytelny, dobry stan. Na dole: 'Przyjaciel Krzysztof Głuchowski / Rio de Janeiro, 18 października 1995.' oraz lista źródeł.",
        "opis_tresci": "Biogram RTM.(MJR) LECHA JERZEGO GŁUCHOWSKIEGO ps. 'JEŻYCKI' — syna Mariana Głuchowskiego i Marii z Ziółkowskich. Ur. 2.VI.1902 w Rakowie k/Częstochowy. Szkoły średnie w Radomsku i Łodzi. POW (Polska Organizacja Wojskowa) od 16 lat. W 1918 rozbrajał Niemców. 1920: ochotnik 7 P.UŁ. Lubelskich, wojna polsko-bolszewicka. Studia: Akademia Rolnicza w Bydgoszczy + szkoła podchorążych rezerwy kawalerii. Zarządzał majątkami ziemskimi. IX.1939: 4. szwadron 7 P.UŁ., Mazowiecka BK, Armia 'Modlin'. Po kampanii: ZWZ, odbudowa 7 P.UŁ. kryptonim 'Jeleń', zastępca dowódcy pułku. VII.1944: rtm., przejął dowodzenie pułkiem i I Szwadronem Warszawskim. 1.VIII.1944: atak na Aleję Szucha o godz. 'W'. Obrona Dolnego Mokotowa i Sadyby. 10.IX: zdobycie zakładów Bruhn na ul. Nabielaka. 15.IX.1944: ciężko ranny na ul. Dolnej — popełnił samobójstwo, by nie narażać żołnierzy na ewakuację pod ogniem wroga. Pośmiertnie: major. Odznaczenia: VM V kl. (pośmiertnie), KW, ZKZ z Mieczami, Krzyż AK. Pochowany: Powązki, kw. 99-I-27. Źródła: 'Ułani Lubelscy' (Londyn 1947), 'Księga Dziejów 7 P.UŁ.' (Londyn 1969), 'Powstańcy Warszawscy' (1957), 'Mokotów 1944' (Warszawa 1971), biogram 1944.pl nr 14206. Tekst spisany przez bratanka Krzysztofa w Rio de Janeiro, 18.X.1995.",
        "seria": "I",
        "tworca": "Krzysztof Andrzej Głuchowski (Juraś), syn Stefana",
        "jezyk": "polski",
        "kontekst": "TRZECI SYN MARIANA GŁUCHOWSKIEGO — Lech Jerzy (2.VI.1902–15.IX.1944), brat Janusza (1888) i Stefana (1893). Bohaterska śmierć: ciężko ranny 15.IX.1944 na ul. Dolnej na Mokotowie, nie chcąc narażać żołnierzy na niebezpieczeństwo ewakuacji pod ostrzałem, odebrał sobie życie. Pośmiertnie awansowany na majora i odznaczony Virtuti Militari. Przejął dowodzenie pułkiem 17.VII.1944 po płk. Veli bek Jedigarze ps. 'Damazy' (ARG/V/170), który tego dnia został oddelegowany poza Warszawę z rozkazem dotarcia do PSZ na Zachodzie. Biogram napisany przez Krzysztofa (syna STEFANA, nie Janusza — korekta genealogiczna) w Rio de Janeiro, 51 lat po śmierci wuja Lecha. Wzmianka o gen. T. Pełczyńskim ps. 'Grzegorz' jako dowódcy. UWAGA: 1944.pl podaje nazwisko panieńskie matki jako 'Ziółkowska', biogram Krzysztofa podaje 'Zielińska' — do weryfikacji.",
        "powiazania": ["ARG/I/1", "ARG/II/1", "ARG/III/1", "ARG/V/1", "ARG/V/170", "ARG/III/33"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/VI/29",
        "photo": "stefan_021.jpeg",
        "tytul": "Zbiór starych fotografii z odręcznymi podpisami — sceny plenerowe",
        "data": "XX w.",
        "typ": "fotografie",
        "opis_fizyczny": "Zbiór 3–4 małych fotografii sepiowych na jasnym tle, plus 2 karteczki z maszynopisem/rękopisem. Fotografie pokazują sceny plenerowe — postaci w plenerze, możliwe groby lub pomniki. Podpisy odręczne, częściowo nieczytelne.",
        "opis_tresci": "Kompozycja złożona z kilku małych fotografii sepiowych i karteczek z opisami. Sceny plenerowe — osoby przy drzewach/pomnikach. Podpisy odręczne na karteczkach opisują osoby lub miejsca. Wymaga lepszego zdjęcia do identyfikacji.",
        "seria": "VI",
        "tworca": "nieznany",
        "jezyk": "polski",
        "kontekst": "Fotografie znalezione w zbiorze dokumentów Stefana. Mogą przedstawiać groby żołnierzy, miejsca pamięci lub sceny rodzinne. Potrzebne lepsze zdjęcie do identyfikacji osób i miejsc.",
        "powiazania": ["ARG/III/1"],
        "stan": "Średni — wymaga lepszego zdjęcia"
    },
    {
        "sygn": "ARG/III/29",
        "photo": "stefan_022.jpeg",
        "tytul": "Etykieta zbioru: 'Listy ppor. Stefana Głuchowskiego z obozu w Niemczech 1945–1947 do gen. Janusza w Anglii oraz do syna Krzysztofa 1947–1949'",
        "data": "ok. 1950–1995",
        "typ": "etykieta/opis archiwalny",
        "opis_fizyczny": "Karteczka z maszynopisem na żółtawym/pomarańczowym papierze, naklejona na kopertę lub teczkę. Format ok. 10×6 cm. Tekst maszynowy, czytelny. Papier lekko pożółkły.",
        "opis_tresci": "'Listy ppor. Stefana Głuchowskiego / z obozu w Niemczech z lat 1945–1947 / do gen. Janusza Głuchowskiego w Anglii / oraz / Listy Stefana Głuchowskiego z Polski / do syna Krzysztofa w Anglii z lat / 1947–1949'",
        "seria": "III",
        "tworca": "prawdopodobnie Krzysztof Głuchowski (archiwista rodzinny)",
        "jezyk": "polski",
        "kontekst": "KLUCZOWA ETYKIETA ARCHIWALNA — opisuje zbiór korespondencji Stefana. Ujawnia: (1) Stefan był w obozach jenieckich w Niemczech 1945–1947 (Stalag XI-B Fallingbostel, Bergen, Oflag II D Gross-Born, Stalag X-B Sandbostel, Oflag X-C Lübeck — łącznie 5 obozów), (2) pisał do brata gen. Janusza w Anglii, (3) po powrocie do Polski (1947) pisał do syna Krzysztofa w Anglii. POTWIERDZONE przez 1944.pl: Krzysztof (Juraś) był SYNEM STEFANA i Wandy z domu Głuchowskiej ps. 'Krysta' (żołnierz Kedywu AK). Dotychczasowy zapis w katalogu ('syn Janusza') był BŁĘDNY — Janusz był WUJEM Krzysztofa, nie ojcem.",
        "powiazania": ["ARG/III/1", "ARG/II/1", "ARG/V/1", "ARG/III/40"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/III/30",
        "photo": "stefan_023.jpeg",
        "tytul": "Karta przydziału AK — ppor. Stefan Głuchowski, Kwatermistrzostwo Obwodu I Śródmieście",
        "data": "1944",
        "typ": "dokument wojskowy",
        "opis_fizyczny": "Mała karta identyfikacyjna, format ok. 8×10 cm, karton brunatny/pomarańczowy. Tekst odręczny i stemplowany. Okrągła pieczęć: 'DOWÓDZTWO OBWODU ŚRÓDMIEŚCIE A.K. ★ Warszawa ★' z Orłem w koronie (czerwony tusz). Odręczny podpis 'Radwan'. Na dole: 'Rej. Nr 141009' i dodatkowy zapis.",
        "opis_tresci": "'Przydział: / Kwatermistrzostwo Obwodu / I' — pieczęć: 'DOWÓDZTWO OBWODU ŚRÓDMIEŚCIE A.K. Warszawa' — odręcznie: 'Radwan' — 'Rej. Nr 141009'.",
        "seria": "III",
        "tworca": "Dowództwo Obwodu Śródmieście AK / płk 'Radwan' (Franciszek E. Pfeiffer)",
        "jezyk": "polski",
        "kontekst": "Karta przydziału uzupełniająca zaświadczenie AK Nr 2856 (ARG/III/28). Stefan przydzielony do Kwatermistrzostwa Obwodu I (Śródmieście) — odpowiadał za logistykę i zaopatrzenie. Nr rejestru 141009 identyczny z ARG/V/168 — co sugeruje wspólną bazę rejestracyjną AK. 'Radwan' = płk Franciszek Edward Pfeiffer (1895–1964), komendant Obwodu I Śródmieście AK, dowodził ok. 13 000 żołnierzy w Powstaniu. Kwatermistrzostwo to logistyka — Stefan jako doświadczony urzędnik (18 lat w Kancelarii Prezydenta) był idealnym kandydatem na stanowisko kwatermistrzowskie.",
        "powiazania": ["ARG/III/28", "ARG/V/168", "ARG/V/162"],
        "stan": "Dobry — pieczęć wyraźna"
    },
    {
        "sygn": "ARG/III/31",
        "photo": "stefan_024.jpeg",
        "tytul": "Dokumenty weryfikacyjne AK — formularz weryfikacji i pismo Komisji, 7 P.UŁ., lipiec 1946",
        "data": "8.VII.1946",
        "typ": "dokument wojskowy",
        "opis_fizyczny": "Dwa dokumenty nałożone na siebie. Górny: formularz 'Weryfikacja żołnierzy A.K.' z 8 lipca 1946, maszynopis z tabelą. Dolny: pismo Komisji Weryfikacyjnej, maszynopis. Podpis: 'J. Uszycki płk.' Papier brunatny, ślady zginania.",
        "opis_tresci": "Górny dokument: 'Weryfikacja Żołnierzy A.K.' — tabela z danymi: 7 PUŁK UŁANÓW, daty. Wydano 8.7.46 BUR. Nr ew. 3550/46. Dolny: pismo Dowódcy 2 Korpusu, Komisja Weryfikacyjna, Kąlno 14.XI.1946 — 'Dowódcy 7.Baonu Strzec./Obrona/ 2 D.S.K.' — potwierdzenie weryfikacji żołnierzy AK z 7 P.UŁ. Podpis: J. Uszycki płk.",
        "seria": "III",
        "tworca": "Komisja Weryfikacyjna AK przy 2. Korpusie PSZ / płk J. Uszycki",
        "jezyk": "polski",
        "kontekst": "Weryfikacja służby AK Stefana Głuchowskiego przeprowadzona przez Komisję przy 2. Korpusie PSZ. Płk Józef Uszycki — ten sam oficer który podpisał weryfikację Krzysztofa (ARG/V/169). Proces weryfikacji wymagał zeznań dwóch świadków — oficerów tej samej jednostki. Potwierdza, że Stefan po wyzwoleniu z Oflagu dołączył do PSZ i przeszedł formalną weryfikację swojej służby w AK.",
        "powiazania": ["ARG/V/169", "ARG/III/28", "ARG/III/30", "ARG/V/171"],
        "stan": "Średni — dokumenty nałożone"
    },
    {
        "sygn": "ARG/III/32",
        "photo": "stefan_025.jpeg",
        "tytul": "Kriegsgefangenenpost — pocztówka jeniecka z Oflagu XVII A, ppor. Stefan Głuchowski",
        "data": "ok. 1942–1944",
        "typ": "korespondencja jeniecka",
        "opis_fizyczny": "Pocztówka jeniecka (Kriegsgefangenenpost / Correspondance des prisonniers de guerre / Postkarte). Format standardowy Czerwonego Krzyża. Stempel cenzury: 'AG XVII A GEPRÜFT' (nr 401). Stempel pocztowy z datą (częściowo czytelny). Pola drukowane po niemiecku i francusku, wypełnione odręcznie.",
        "opis_tresci": "STRONA ADRESOWA pocztówki jenieckiej — 'Kriegsgefangenenpost / Correspondance des prisonniers de guerre / Postkarte'. An (do): 'A. ZALESKI' + adres (Milczna?). Absender (nadawca): jeniec z Oflagu XVII A. Gefangenennummer: [widoczny]. Stempel prostokątny: 'AG XVII A / GEPRÜFT' nr 401 (cenzura obozowa). Stempel pocztowy okrągły z datą. UWAGA: strona z tekstem (verso) = ARG/II/69 (varia_006_kriegsgef_oflag.jpeg) — to ta sama pocztówka, dwa ujęcia.",
        "seria": "III",
        "tworca": "ppor. Stanisław Stefan Głuchowski",
        "jezyk": "niemiecki/polski",
        "kontekst": "Pocztówka jeniecka z Oflagu XVII A (Edelbach/Döllersheim, Austria). UWAGA: wg biogramu 1944.pl Stefan NIE był w Oflagu XVII A — jego trasa jeniecka po Powstaniu to: Stalag XI-B Fallingbostel → Bergen → Oflag II D Gross-Born → Stalag X-B Sandbostel → Oflag X-C Lübeck. Pocztówka mogła zatem należeć do INNEGO jeńca (np. znajomego oficera) i trafić do kolekcji Stefana jako pamiątka. Adresat 'A. Zaleski' — możliwe: August Zaleski (1883–1972), minister/prezydent RP na uchodźstwie, lub inny Zaleski. Nadawca na pocztówce wymaga ponownej identyfikacji — może to nie Stefan. Oflag XVII A przetrzymywał ok. 4500 polskich oficerów 1939–1945.",
        "powiazania": ["ARG/III/28", "ARG/III/30", "ARG/III/40", "ARG/II/69"],
        "stan": "Średni — stempel częściowo nieczytelny"
    },
    {
        "sygn": "ARG/III/33",
        "photo": "stefan_026.jpeg",
        "tytul": "Notatka do Krzysztofa — list z podpisami por. Veli Jedigara i por. Janusza Poźniowskiego",
        "data": "ok. 1980–2000",
        "typ": "notatka odręczna",
        "opis_fizyczny": "Fragment kartki z odręcznym pismem, urwany/naderwany na dole. Papier kremowy, pożółkły. Pismo kursywą, atrament niebieski/czarny. Połowa tekstu czytelna, dolna część rozmazana/niewyraźna.",
        "opis_tresci": "'Drogi Krzysztofie, / Przesyłam Ci ten list w imieniu mojego Ojca, jako / ciekawostkę, ale dotyczącą 7 pułku Ułanów. Otóż / są tam podpisy dwóch oficerów z tego pułku, którzy / przyjaźnili się z moim Ojcem. / por Veli Jedigar i por Janosz Poźniowski / list pisany na zebraniu w Warszawie u / domu p. Korwelach.'",
        "seria": "III",
        "tworca": "nieznany (dziecko jednego z oficerów 7 P.UŁ.)",
        "jezyk": "polski",
        "kontekst": "Notatka potwierdza przyjaźń oficerów 7 P.UŁ.: (1) Płk Veli bek ks. Jedigar ps. 'Damazy' (31.X.1897–13.XII.1971) — Azerbejdżanin szlacheckiego rodu z Kaukazu, dowódca 7 P.UŁ. AK 'Jeleń' od VIII.1940 do 17.VII.1944, oddelegowany poza Warszawę przed Powstaniem, zmarł w Buenos Aires, prochy przeniesione na Cmentarz Tatarski w Warszawie 1990. (2) Por. Janusz Poźniowski — oficer 7 P.UŁ. Spotkanie 'u p. Korwelach' — prawdopodobnie kpt. Korwel z 7 P.UŁ. Notatka skierowana do Krzysztofa (syna Stefana), kolekcjonera dokumentów 7 P.UŁ.",
        "powiazania": ["ARG/V/170", "ARG/III/1", "ARG/V/1"],
        "stan": "Średni — dolna część nieczytelna"
    },
    {
        "sygn": "ARG/III/34",
        "photo": "stefan_028.jpeg",
        "tytul": "Lista personalna żołnierzy 7 P.UŁ. Lubelskich — 23 nazwiska, w tym Głuchowski Krzysztof (poz.14) i Głuchowski Zbigniew (poz.8)",
        "data": "8.VII.1946",
        "typ": "lista personalna",
        "opis_fizyczny": "Maszynopis na papierze brunatnym, format A4. Tabela z numerami porządkowymi 1–23, kolumny: nazwisko, rok urodzenia, stopień, przydział. Nagłówek: '7 PUŁK UŁANÓW', 'Wydano 8.7.46 BUR', nr ew. 3550/46. Papier kruchy, krawędzie uszkodzone.",
        "opis_tresci": "Lista 23 żołnierzy 7 P.UŁ. Lubelskich z weryfikacji AK: 1. Koblowec Mieczysław, 2. Badnak Czesław, 3. Grabowski Władysław (1922), 4. Donykowski Władysław (1923), 5. Marguliński Jerzy (1908), 6. Stasiak Kazimierz, 7. Stefanecki Stefan (1928), 8. GŁUCHOWSKI ZBIGNIEW, 9. Bedlak Dariusz, 10. Korynt Stanisław, 11. Werlak Stanisław (1922), 12. Długo Józef (1919), 13. Szidorek Kazimierz (1921), 14. GŁUCHOWSKI KRZYSZTOF (1926), 15. Horowski Stefan (1928), 16. Jędrzejek Szymon (1927), 17. Skoniak Mirosław, 18. Grzelak Jan (1918), 19. Gronkiewicz Marian (1922), 20. Spadkowa/Szolkowa Wojciech (1924), 21. Orasek Kazimierz, 22. Stupniak Władysław (1928), 23. Dulias Szczepan (1919). Podpis: Przewodniczący [nieczytelny].",
        "seria": "III",
        "tworca": "Komisja Weryfikacyjna przy 2. Korpusie PSZ",
        "jezyk": "polski",
        "kontekst": "Lista weryfikacyjna żołnierzy AK z 7 P.UŁ. Lubelskich. DWÓCH GŁUCHOWSKICH: Krzysztof (poz. 14, ur. 1926 = Juraś, syn Stefana) i Zbigniew (poz. 8 — KIM JEST? możliwy syn Stefana lub Lecha?). Porównaj z ARG/V/171 (podobna lista). Większość żołnierzy urodzonych 1918–1928 — pokolenie wojenne. Dokument datowany 8.VII.1946 — weryfikacja prowadzona w Henstedt/Niemcy przed demobilizacją PSZ.",
        "powiazania": ["ARG/V/171", "ARG/V/169", "ARG/III/31"],
        "stan": "Średni — krawędzie uszkodzone"
    },
    {
        "sygn": "ARG/III/35",
        "photo": "stefan_029.jpeg",
        "tytul": "Certyfikat inwentarzowy 7 Pułku Ułanów Lubelskich — spis wyposażenia i dokumentów, 8.IX.1946",
        "data": "8.IX.1946",
        "typ": "certyfikat/inwentarz",
        "opis_fizyczny": "Maszynopis na papierze brunatnym, format A4. Nagłówek: '7 PUŁK UŁANÓW LUBELSKICH, O/Rezerwy Gem., dn. 8 Września 1946.' Tytuł: 'CERTYFIKAT'. Lista numerowana ok. 30 pozycji. Papier kruchy, ślady wilgoci.",
        "opis_tresci": "'7 PUŁK UŁANÓW LUBELSKICH / O/Rezerwy Gem. / dn. 8. Września 1946 / CERTYFIKAT' — lista przedmiotów/dokumentów z numerami ewidencyjnymi: broń (Nr Broni), dokumenty pułkowe od 1944–1947, karty ewidencyjne oficerów i podoficerów, akta personalne, rozkazy z 2 Korpusu, pieczęcie pułkowe. Odniesienia do dat: 1944, 1945, 1946, 1947. Podpis na dole nieczytelny.",
        "seria": "III",
        "tworca": "7 Pułk Ułanów Lubelskich",
        "jezyk": "polski",
        "kontekst": "Inwentaryzacja majątku i dokumentacji 7 P.UŁ. Lubelskich prowadzona we wrześniu 1946 — w ramach przygotowań do demobilizacji PSZ na Zachodzie. Pułk był wówczas w Niemczech (Henstedt). Certyfikat dokumentuje: karty ewidencyjne, akta personalne, rozkazy z 2 Korpusu, pieczęcie — cenny materiał do historii jednostki. Fakt, że te dokumenty trafiły do kolekcji rodziny Głuchowskich, sugeruje że Stefan lub Krzysztof mieli funkcję archiwalną w pułku.",
        "powiazania": ["ARG/III/34", "ARG/III/40", "ARG/V/171"],
        "stan": "Średni — papier kruchy"
    },
    {
        "sygn": "ARG/III/36",
        "photo": "stefan_030.jpeg",
        "tytul": "Dedykacja od oficerów — 'Kochanemu Stefankowi, uroczemu brykowi i dobremu towarzyszowi'",
        "data": "ok. 1940–1947",
        "typ": "dedykacja/inskrypcja",
        "opis_fizyczny": "Odwrót fotografii lub kartki, format ok. A5. Tekst odręczny w kilku rękach (co najmniej 6–8 podpisów). Atrament ciemny (czarny/brązowy). Papier kremowy/beżowy, stan dobry.",
        "opis_tresci": "'Kochanemu Stefankowi, uroczemu / brykowi i dobremu towarzyszowi / Hoch     Lechnia' — następnie kilka podpisów: 'por. [Sierpiński?] pez[?] 8 p.S.K.' — 'kap[itan?] Syaperze [?]' — i 5–6 dalszych podpisów odręcznych (częściowo nieczytelnych).",
        "seria": "III",
        "tworca": "grupa oficerów (współtowarzysze broni Stefana)",
        "jezyk": "polski",
        "kontekst": "Zbiorowa dedykacja od oficerów dla Stefana — 'uroczemu brykowi' (dosł. uroczemu łobuzowi/psotnikowi) to pieszczotliwy zwrot koleżeński. Wzmianka 'Lechnia' może odnosić się do brata Lecha Głuchowskiego (zdrobniale: Lechnia). Podpisy oficerów z różnych jednostek (8 p.S.K. = 8 Pułk Strzelców Konnych?). Może pochodzić z Oflagu XVII A (oficerowie w niewoli tworzyli silne więzi) lub z Henstedt (po wyzwoleniu). Dokument o wartości sentymentalnej — pokazuje pozycję towarzyską Stefana wśród oficerów.",
        "powiazania": ["ARG/III/32", "ARG/III/40", "ARG/I/6"],
        "stan": "Dobry — podpisy częściowo nieczytelne"
    },
    {
        "sygn": "ARG/III/37",
        "photo": "stefan_031.jpeg",
        "tytul": "Karta pułkowa 7 Pułku Ułanów Lubelskich im. Gen. Broni Sosnkowskiego — Henstedt, 23.III.1947",
        "data": "23.III.1947",
        "typ": "karta pułkowa/wizytówka",
        "opis_fizyczny": "Składana kartka, format ok. 12×8 cm. Na awersie: godło pułkowe (dwa romby/chevron w kolorze czerwonym) oraz napis drukowany. Na rewersie (odwrócony): odręczny napis 'ppor. Głuchowski Stefan'. Papier kremowy, stan dobry.",
        "opis_tresci": "Awers: godło pułkowe (dwa romby/szewrony czerwone) + '7 Pułk Ułanów Lubelskich / im Gen Broni Sosnkowskiego / Henstedt 23.III.47.' Rewers (odwrócony): 'ppor. Głuchowski Stefan'.",
        "seria": "III",
        "tworca": "7 Pułk Ułanów Lubelskich",
        "jezyk": "polski",
        "kontekst": "Karta/wizytówka pułkowa z Henstedt (Szlezwik-Holsztyn, brytyjska strefa okupacyjna Niemiec). Pełna nazwa: 7 Pułk Ułanów Lubelskich im. Generała Broni Kazimierza Sosnkowskiego — pułk nosił imię tego samego Sosnkowskiego, który napisał list do gen. Janusza (ARG/II/27)! Data 23.III.1947 to okres demobilizacji PSZ. Stefan widnieje jako ppor. — potwierdza jego stopień wojskowy (ten sam co na karcie AK). Henstedt było miejscem stacjonowania polskich jednostek przed ich rozwiązaniem. Stefan wkrótce potem wrócił do Polski (wg etykiety ARG/III/29 pisał już z Polski od 1947).",
        "powiazania": ["ARG/III/29", "ARG/III/32", "ARG/II/27", "ARG/III/34"],
        "stan": "Dobry"
    },

    # === Downloads/gluchowski — Varia (varia_002–012, bez duplikatów) ===
    {
        "sygn": "ARG/VI/26",
        "photo": "varia_002_album_groby.jpeg",
        "tytul": "Strona albumu — 3 zdjęcia grobów/pomników z karteczkami opisowymi",
        "data": "lata 40.–50. XX w.",
        "typ": "album/fotografia",
        "opis_fizyczny": "Strona albumu (karton szary-brązowy, format ok. A4). Naklejone 3 czarno-białe fotografie (format ok. 6×9 cm każda) i 2 karteczki z odręcznymi opisami. Zdjęcia przedstawiają: (1) krzyż lub nagrobek z tablicą w ogrodzie/parku, (2) grób z kwiatami/wieńcami na cmentarzu, (3) dwie osoby (kobiety?) przy grobie lub pomniku. Karteczki z opisami — pismo odręczne, trudno czytelne na zdjęciu.",
        "opis_tresci": "Strona z albumu rodzinnego dokumentująca groby i pomniki. Trzy fotografie: krzyż/nagrobek (prawdopodobnie grób powstańczy), grób udekorowany kwiatami (prawdopodobnie pogrzeb lub rocznica), dwie osoby przy pomniku/grobie. Dwie karteczki z odręcznymi opisami identyfikującymi osoby i miejsca — tekst trudny do odczytania z fotografii albumu. Kontekst: dokumentacja grobów bliskich — być może grób Lecha (poległego na Mokotowie 15.IX.1944) lub innych członków rodziny.",
        "seria": "VI",
        "tworca": "nieznany (rodzina Głuchowskich)",
        "jezyk": "polski",
        "kontekst": "Album pamiątkowy — dokumentacja grobów i pomników rodzinnych/powstańczych. Zdjęcia z lat 40.-50. mogą dokumentować pochówki z okresu Powstania Warszawskiego lub tuż po wojnie. Możliwe groby: Lech Głuchowski (poległ na Mokotowie 15.IX.1944, pochowany najpierw tymczasowo, potem ekshumowany), lub groby innych członków rodziny na Powązkach. Stefan (1893–1962) pochowany na Powązkach kw. 99-IV-19. Karteczki z opisami wymagają odczytu z oryginału.",
        "powiazania": ["ARG/VI/4"],
        "stan": "Średni"
    },
    {
        "sygn": "ARG/VI/27",
        "photo": "varia_003_etykieta_listy_stefan.jpeg",
        "tytul": "Etykieta archiwalna — Listy Stefana Głuchowskiego 1945–1949",
        "data": "ok. 1945–1949",
        "typ": "etykieta archiwalna",
        "opis_fizyczny": "Etykieta papierowa opisująca zawartość teczki archiwalnej.",
        "opis_tresci": "Etykieta opisująca zawartość teczki: listy Stefana z obozu w Niemczech (1945–47) do gen. Janusza w Anglii + listy Stefana z Polski do syna Krzysztofa (1947–49).",
        "seria": "VI",
        "tworca": "archiwista rodzinny",
        "jezyk": "polski",
        "kontekst": "WAŻNE: potwierdza istnienie korespondencji rodzinnej. Listy Stefana z obozu w Niemczech (1945–47) do gen. Janusza w Anglii + listy Stefana z Polski do syna Krzysztofa (1947–49). Dowód na kontakt rodzinny ponad granicami żelaznej kurtyny.",
        "powiazania": ["ARG/II/65", "ARG/III/1", "ARG/V/166"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/V/168",
        "photo": "varia_004_karta_ak_radwan.jpeg",
        "tytul": "Karta przydziału AK — Kwatermistrzostwo Obwodu I Śródmieście, ps. Radwan",
        "data": "ok. 1943–1944",
        "typ": "dokument wojskowy",
        "opis_fizyczny": "Karta przydziału, druk z odręcznymi wpisami.",
        "opis_tresci": "'Przydział: Kwatermistrzostwo Obwodu I'. Pieczęć okrągła: 'DOWÓDZTWO OBWODU ŚRÓDMIEŚCIE A.K. ★ Warszawa ★' z orłem w koronie. Odręcznie: 'Radwan' (pseudonim dowódcy). Na dole: 'Wojsk. Nr 141009 / Stalag XI B' — dopisane po niewoli. Rewers karty identyfikacyjnej AK.",
        "seria": "V",
        "tworca": "Armia Krajowa / Obwód I Śródmieście, d-ca płk Pfeiffer ps. 'Radwan'",
        "jezyk": "polski",
        "kontekst": "Rewers karty AK Krzysztofa Głuchowskiego (awers = ARG/V/162). Przydział: Kwatermistrzostwo Obwodu I Śródmieście, pod dowództwem płk. Franciszka Edwarda Pfeiffera ps. 'Radwan'. Dopisek 'Nr 141009 / Stalag XI B' — numer jeniecki Krzysztofa dodany po Powstaniu. Dokument potwierdzający ciągłość: AK → niewola (Stalag XI B Fallingbostel) → powrót.",
        "powiazania": ["ARG/V/162", "ARG/V/164", "ARG/III/28"],
        "stan": "Średni — odciski palców, lekko zabrudzone"
    },
    {
        "sygn": "ARG/V/169",
        "photo": "varia_005_weryfikacja_ak.jpeg",
        "tytul": "Dokumenty weryfikacyjne AK — 7 p.ul. Lubelskich, 1946",
        "data": "1946",
        "typ": "dokument wojskowy",
        "opis_fizyczny": "Dokumenty weryfikacyjne, maszynopis.",
        "opis_tresci": "Dwa dokumenty nałożone: (1) 'Weryfikacja Żołnierzy A.K.' z 4 Lipca 1946, tabela z kolumnami: nazwisko, stopień, przydział — 7 PUŁK UŁANÓW, daty; (2) Pismo Dowódcy 2 Korpusu, Komisja Weryfikacyjna, nr 14k.965/II/46/46, Londyn 12.XII.1946, podpis: J. Uszycki płk. Dotyczy weryfikacji żołnierzy AK z 7 p.uł. Lubelskich, zatwierdzenie stopni i odznaczeń.",
        "seria": "V",
        "tworca": "Komisja Weryfikacyjna AK przy 2. Korpusie PSZ / płk J. Uszycki",
        "jezyk": "polski",
        "kontekst": "Weryfikacja żołnierzy AK z 7 p.uł. przez Komisję przy 2. Korpusie Polskim we Włoszech/Anglii. Płk J. Uszycki — prawdopodobnie Józef Uszycki, oficer sztabowy 2 Korpusu PSZ. Proces weryfikacji polegał na potwierdzeniu służby konspiracyjnej AK przez dwóch świadków — oficerów tej samej jednostki. Potrzebne do uznania stopni i odznaczeń bojowych przez PSZ na Zachodzie.",
        "powiazania": ["ARG/VI/23", "ARG/V/164", "ARG/V/171"],
        "stan": "Średni — dokumenty nałożone na zdjęciu"
    },
    {
        "sygn": "ARG/II/69",
        "photo": "varia_006_kriegsgef_oflag.jpeg",
        "tytul": "Kriegsgefangenenpost — Postkarte z Oflagu XVII A do A. Zaleskiego, dat. 15.IX.1942",
        "data": "15.IX.1942",
        "typ": "korespondencja jeniecka",
        "opis_fizyczny": "Formularz Kriegsgefangenenpost (Postkarte), format A5. Druk z odręcznymi wpisami. Pieczęć prostokątna 'GEPRÜFT / LAG XVII A' (cenzura obozowa). Stempel pocztowy okrągły z datą. Strona adresowa: 'An: A. ZALESKI' + adres (Milczna?). Strona nadawcy (Absender): dane jeńca z Oflagu XVII A. Dolna połowa: sekcja 'Kriegsgefangenenlager / Camp des prisonniers / Datum: 15. 9. 1942' — tekst odręczny po polsku, gęste pismo atramentem. Pieczęć okrągła cenzury nr '40(?)'.",
        "opis_tresci": "Kartka pocztowa jeniecka z Oflagu XVII A, datowana 15.IX.1942. Adresowana do 'A. ZALESKI' (Milczna?). Treść zaczyna się od 'Kochany Stasiu!' — życzenia (prawdopodobnie urodzinowe lub imieninowe). Wspomniany Żoliborz, Francja, 'Jadwiga', 'Janowi' (pozdrowienia dla Jana/Janusza?), 'szklanne' przedmioty, 'Siostrom'. Podpisane (trudno czytelne) — 'Klimczowa(?)', 'Bach(?)'. List osobisty, rodzinny ton. Osoba 'Stasiu' na adresie Zaleskiego — możliwe, że Zaleski był pośrednikiem adresowym lub 'Stasiu' to Stanisław Zaleski.",
        "seria": "II",
        "tworca": "Jeniec wojenny — oficer polski w Oflagu XVII A (Edelbach/Kaisersteinbruch, Austria)",
        "jezyk": "polski/niemiecki",
        "kontekst": "Oflag XVII A — obóz oficerski w Edelbach/Kaisersteinbruch (Austria), działający 1939–1945. ~170 polskich oficerów wśród ~4500 jeńców (głównie Francuzi i Jugosłowianie). Gen. Janusz Głuchowski NIE był jeńcem — dowodził PSZ w Wielkiej Brytanii. Kartka od jeńca do 'Stasia' (przez adres A. Zaleskiego) — wzmianka o Żoliborzu (dzielnica Głuchowskich!) i 'Janowi' (Janusz?) sugeruje powiązanie z rodziną. Data 15.IX.1942 — trzeci rok niewoli. Zachowanie w archiwum Głuchowskich potwierdza, że nadawca lub adresat był bliski rodzinie. HIPOTEZA: nadawca mógł być towarzyszem broni z kręgu Głuchowskich, piszącym do wspólnego znajomego.",
        "powiazania": ["ARG/II/65"],
        "stan": "Średni — pożółkła, pismo trudno czytelne"
    },
    {
        "sygn": "ARG/V/170",
        "photo": "varia_007_list_7pul.jpeg",
        "tytul": "List od 'M.' do Krzysztofa — podpisy por. Jocligara i por. Poźniowskiego z 7 p.ul.",
        "data": "lata 60.–80. XX w.",
        "typ": "korespondencja",
        "opis_fizyczny": "List odręczny atramentem na papierze kancelaryjnym, 1 karta. Pismo czytelne, kaligraficzne.",
        "opis_tresci": "'Drogi Krzysztofie, Przesyłam Ci ten list w imieniu mojego Ojca, jako ciekawostkę, ale dotyczącą 7 płk ułanów. Oto są tam podpisy dwóch oficerów z tego pułku, którzy przyjaźnili się z moim Ojcem. por. Veli Jocligar i por. Janusz Poźniowski — list pisany na zebraniu w Warszawie u p. Korwelach. M.' List towarzyszący — z załączonym dokumentem z autografami oficerów 7 p.uł.",
        "seria": "V",
        "tworca": "'M.' — syn towarzysza broni z 7 p.ul.",
        "jezyk": "polski",
        "kontekst": "IDENTYFIKACJA: 'Veli Jocligar' = VELI BEK JEDIGAR (1897–1971) — Azer z Kaukazu (Tekali, Azerbejdżan), muzułmanin, oficer kawalerii WP. Zastępca d-cy 7 p.uł. od 1936, szef sztabu Mazowieckiej Brygady Kawalerii IX.1939, w niewoli zwolniony 1940 (obcokrajowiec). Od VIII.1940 konspiracyjny d-ca 7 p.uł. AK ps. 'Damazy' (kryptonim 'Mazury'). Przyjaciel Bora-Komorowskiego. Emigracja: Argentyna 1949, zm. Buenos Aires 13.XII.1971. por. Janusz Poźniowski — oficer 7 p.uł., do dalszego zbadania. Zebranie 'u p. Korwelach' w Warszawie — spotkanie środowiska pułkowego, dokument pamięci kombatanckiej.",
        "powiazania": ["ARG/V/164", "ARG/V/166", "ARG/V/171"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/III/28",
        "photo": "varia_008_zaswiadczenie_ak_stefan.jpeg",
        "tytul": "Zaświadczenie AK nr 2856 — ppor. Stanisław Stefan Głuchowski, 25.VII.1944",
        "data": "25.VII.1944",
        "typ": "dokument wojskowy",
        "opis_fizyczny": "Zaświadczenie urzędowe z pieczęcią AK.",
        "opis_tresci": "'ARMIA KRAJOWA / Okręg Warszawski / Nr 2856 / Zaświadczam, że ppor. Głuchowski Stanisław Stefan jest żołnierzem A.K. / Dnia 25.VII.1944 r. / Obwodu [I Śródmieście] / Komendant Okręgu / [pieczęć] DOWÓDZTWO OBWODU ŚRÓDMIEŚCIE A.K. ★ Warszawa ★ / [podpis] Radwan'. Pieczęć okrągła z orłem w koronie. Odręczne wpisanie nazwiska i daty.",
        "seria": "III",
        "tworca": "Płk Franciszek Edward Pfeiffer ps. 'Radwan' (1895–1964), Komendant Obwodu I Śródmieście AK",
        "jezyk": "polski",
        "kontekst": "Zaświadczenie wydane 6 DNI PRZED GODZINĄ 'W' (1.VIII.1944). DRAMATYCZNA CHRONOLOGIA: Stefan był ARESZTOWANY przez Gestapo w maju 1944 — więziony na Pawiaku i przesłuchiwany na Alei Szucha (siedzibie Gestapo)! Zwolniony 29.VII.1944 — zaledwie 3 DNI przed Powstaniem! Zaświadczenie AK nr 2856 nosi datę 25.VII.1944 — czyli wydane jeszcze PRZED zwolnieniem z Gestapo (o ile data jest prawidłowa) lub tuż po. 'Radwan' = płk Franciszek Edward Pfeiffer (1895–1964) — legionista, Komendant Obwodu I Śródmieście AK, dowódca ~13 000 żołnierzy w Powstaniu. Ranny 5.VIII.1944. Zmarł w Londynie 13.VI.1964 — 2 DNI PO gen. Januszu Głuchowskim (zm. 11.VI.1964)! Stefan walczył w Powstaniu jako kwatermistrz Obwodu I Śródmieście — po 18 latach doświadczenia w Kancelarii Prezydenta RP idealnie nadawał się do logistyki. Żona Wanda ps. 'Krysta'/'Justyna' (sierż. pchor. Kedyw) nie została zmobilizowana z powodu ran z akcji Wilanów (26.IX.1943).",
        "powiazania": ["ARG/III/1", "ARG/VI/25", "ARG/V/162", "ARG/V/168"],
        "stan": "Dobry — czytelne, pieczęć wyraźna"
    },
    {
        "sygn": "ARG/V/171",
        "photo": "varia_009_lista_personalna_7pul.jpeg",
        "tytul": "Lista personalna żołnierzy 7 p.ul. — komisja, lipiec 1946",
        "data": "VII.1946",
        "typ": "dokument wojskowy",
        "opis_fizyczny": "Lista personalna, maszynopis tabelaryczny.",
        "opis_tresci": "Nagłówek: '7 PUŁK UŁANÓW / Wydanie 8.7.46 / Dowódca 2 Korpusu / Komisja Weryfikacyjna'. Lista 23 żołnierzy z danymi: nazwisko, rok urodzenia, stopień, przydział, numer weryfikacyjny. POZ. 8: GŁUCHOWSKI KRZYSZTOF. Pozostali m.in.: Kolhauer Mieczysław, Dąbrowski Władysław (1919, Płock), Stefanicki Stefan (1924), Werlak Stanisław (1922), Ringa Józef (1915), Horowski Stefan (1926), Okonianb(?) Mirosław (1928), Ornoch Kazimierz (1903). Stopnie: st.strz./st.uł., bomb./pom., bomb./pchor.",
        "seria": "V",
        "tworca": "Komisja Weryfikacyjna AK przy 2. Korpusie PSZ",
        "jezyk": "polski",
        "kontekst": "Kluczowy dokument zbiorowy: 23 żołnierzy 7 p.uł. AK zweryfikowanych jednocześnie, w tym Krzysztof Głuchowski (poz. 8). Data 8.VII.1946 — rok po wojnie, 2 lata po Powstaniu. Żołnierze urodzeni 1897-1928: pełne spektrum pokoleń. Różne stopnie (st.uł., bomb., pchor.) = różne role w walce. Każde z 23 nazwisk to potencjalna historia do zbadania. Dokument jest cenniejszy niż indywidualne zaświadczenie — obraz CAŁEJ JEDNOSTKI.",
        "powiazania": ["ARG/V/169", "ARG/V/164", "ARG/V/166"],
        "stan": "Średni — pożółkły, ale czytelny"
    },
    {
        "sygn": "ARG/V/172",
        "photo": "varia_010_certyfikat_7pul.jpeg",
        "tytul": "Certyfikat przekazania dokumentów 7 P.U.L. do Bazy Likwidacyjnej — Henstedt, 1.IX.1945",
        "data": "1.IX.1945",
        "typ": "dokument wojskowy",
        "opis_fizyczny": "Maszynopis na papierze kancelaryjnym A4, jedna strona. Nagłówek: '7 PUŁK UŁANÓW LUBELSKICH / D-two 7 P.U.L.' z numerem korespondencyjnym i datą '1 Września 1945'. Tytuł: 'CERTYFIKAT'. Poniżej 21 pozycji w spisie numerowanym. Podpis na dole (prawdopodobnie Klemensowicz). Papier pożółkły, druk maszynowy czytelny.",
        "opis_tresci": "Certyfikat przekazania dokumentów pułkowych zgodnie z pismem okólnym z 11 lipca 1945. Inwentarz 21 pozycji: (1) Listy nagród, (2-4) Rozkazy od Nr ... do Nr ... za lata 1943-1945, (5-7) Rozkazy personalne za 1944-1946, (8-9) Rozkazy Dzienne Pułku od Nr ... za 1945-1946, (10) Regulamin oświetlenia szkolnej piechoty, (11) Sprzęt szkolenia oficerów i oszczep[?], (12) Karty ewidencyjne oficerów — komplet, (13) j.w. opissy talonw ofic. i podofic. Pułku — Pocztki(?), (14) Karty ewidencyjne szwadronów łączności, (15) Karty ewidencyjne z szwadronów, (16) Karty szkoleniowe z szwadronami, (17) Korespondencja ogólna, Kwalifik. pohor(?), (18-19) Inwentarz korespondencji na odroczenie(?), (20) Obsługiwanie z Rozkazy listy listowy(?), (21) [nieczytelne]. Dokumenty przekazane do Bazy Likwidacyjnej Polskich Broni w Anglii.",
        "seria": "V",
        "tworca": "D-two 7 Pułku Ułanów Lubelskich, Henstedt",
        "jezyk": "polski",
        "kontekst": "Kluczowy dokument demobilizacyjny: 1 września 1945 — dokładnie 6 lat po wybuchu II wojny, 7 P.U.L. przekazuje swoje archiwum pułkowe do Bazy Likwidacyjnej PSZ w Anglii. Inwentarz obejmuje rozkazy, karty ewidencyjne oficerów i podoficerów, korespondencję — pełna dokumentacja jednostki od 1943 do 1946. Henstedt (Niemcy, Schleswig-Holstein) — miejsce stacjonowania 7 P.U.L. po zakończeniu wojny, w brytyjskiej strefie okupacyjnej. To właśnie te dokumenty (lub ich kopie) mogły później trafić do archiwum Krzysztofa. Certyfikat dokumentuje KONIEC istnienia 7 P.U.L. jako jednostki czynnej.",
        "powiazania": ["ARG/V/171", "ARG/V/164"],
        "stan": "Średni"
    },
    {
        "sygn": "ARG/VI/28",
        "photo": "varia_011_dedykacja_lech_stefan.jpeg",
        "tytul": "Dedykacja dla Stefana od brata Lecha i kolegów oficerskich — 8 p.S.K.",
        "data": "lata 30. XX w.",
        "typ": "dedykacja",
        "opis_fizyczny": "Dedykacja odręczna atramentem na odwrocie fotografii lub na kartce papieru, format ~12×15 cm. Pismo kaligraficzne (Lech), pod spodem 6-7 podpisów kolegów oficerskich. Papier pożółkły, atrament brązowiejący.",
        "opis_tresci": "'Kochanemu Stefankowi, uroczemu braciszkowi i dobremu towarzyszowi / Lech    Lochia(?)'. Poniżej podpisy kolegów oficerskich, w tym wzmianka '8 p.S.K.' (8 Pułk Strzelców Konnych?). Kilka podpisów nieczytelnych — kaligraficzne, z parafami. Jeden podpis zawiera 'Meguriński(?)', inny 'Jakub Morawski(?)' i 'Waszelski(?)'. Dedykacja grupowa — prawdopodobnie z okazji spotkania oficerskiego.",
        "seria": "VI",
        "tworca": "Lech Głuchowski i koledzy oficerscy",
        "jezyk": "polski",
        "kontekst": "Unikalna dedykacja Lecha do brata Stefana — 'kochany Stefanku, uroczy braciszku i dobry towarzyszu'. Świadectwo ciepłych relacji braterskich. Lech (ok. 1902–1944) poległ na Mokotowie w Powstaniu Warszawskim. Wzmianka '8 p.S.K.' może wskazywać na 8 Pułk Strzelców Konnych lub inną jednostkę kawalerii — Stefan mógł mieć kontakty z różnymi pułkami. Podpisy kolegów oficerskich tworzą grupowy portret środowiska wojskowego II RP. Dokument powstał prawdopodobnie w latach 30., przed wojną.",
        "powiazania": ["ARG/VI/24", "ARG/VI/25"],
        "stan": "Średni"
    },
    {
        "sygn": "ARG/V/173",
        "photo": "varia_012_karta_7pul_henstedt.jpeg",
        "tytul": "Karta pamiątkowa 7 P.U.L. im. Gen. Broni Sosnkowskiego — Henstedt 23.III.1947 (egzemplarz ppor. Krzysztofa)",
        "data": "23.III.1947",
        "typ": "karta pamiątkowa",
        "opis_fizyczny": "Karta pamiątkowa składana, format ok. 10×14 cm. Na okładce dwa czerwone romby (insygnia pułkowe?) i napis drukowany: '7 Pułk Ułanów Lubelskich / im Gen Broni Sosnkowskiego / Henstedt  23. III. 47.' Na górze karty odręczny dopisek atramentem (odwrócony): 'ppor. Głuchowski Krzysztof' — identyfikacja właściciela. Papier ecru, druk offsetowy + odręczny dopisek.",
        "opis_tresci": "Karta pamiątkowa z uroczystości pułkowej 7 Pułku Ułanów Lubelskich im. Gen. Broni Sosnkowskiego, Henstedt 23 marca 1947. Egzemplarz personalny ppor. Krzysztofa Głuchowskiego (odręczny dopisek nazwiska). Dwa czerwone romby na okładce — prawdopodobnie element heraldyki pułkowej. Wewnątrz karty zapewne program uroczystości i/lub lista obecnych.",
        "seria": "V",
        "tworca": "7 Pułk Ułanów Lubelskich",
        "jezyk": "polski",
        "kontekst": "Karta pamiątkowa z uroczystości pułkowej w Henstedt (strefa brytyjska Niemiec). 7 Pułk Ułanów Lubelskich im. Gen. Broni Sosnkowskiego. Marzec 1947 — okres przed demobilizacją PSZ na Zachodzie. Henstedt — miejsce stacjonowania polskich jednostek w Niemczech po wojnie.",
        "powiazania": ["ARG/V/171", "ARG/V/172", "ARG/V/164"],
        "stan": "Średni"
    },
]

# ============================================================================
# WYCENA / VALUATION — per-document estimates
# ============================================================================
# Methodology:
# - Auction comparables: DESA Unicum, SDA (Stowarzyszenie Dom Aukcyjny),
#   Rara Avis Kraków, OneBid.pl, Heritage Auctions, WDA Wierzbicki
# - Comparable sales 2020-2025: Rara Avis #105 (2024), SDA Militaria (2020),
#   DESA #197/#202 (2024-2025), OneBid militaria category avg 486 EUR
# - Archive multiplier: complete family archives sell for 1.5x-5x over sum
#   of individual pieces (provenance, narrative value, research value)
# - Condition factors: Good = 1.0x, Average = 0.8x, Poor = 0.5x
# - Historical significance: unique/key = 2-5x, common = 1x
#
# VALUE RATINGS: ★ = typowa (common), ★★ = istotna (significant),
#   ★★★ = wysoka (high), ★★★★ = wyjątkowa (exceptional), ★★★★★ = muzealna (museum-grade)
# ============================================================================

VALUATIONS = {
    # === SERIA I — MARIAN GŁUCHOWSKI (PON 1914) ===
    "ARG/I/1": {
        "wartosc_hist": "★★★★★",
        "opis_wartosci": "Legitymacja PON nr 2 — jeden z najwcześniejszych numerów. Dowód roli założycielskiej w ruchu niepodległościowym. Porównywalny: legitymacje organizacji paramilitarnych 1914 na Rara Avis: 800-2000 PLN. Tu: NR 2 = unikat.",
        "cena_min": 3000,
        "cena_max": 6000,
        "waluta": "PLN",
        "rekomendacja": "DESA Unicum lub Rara Avis. Alternatywnie: depozyt/sprzedaż Muzeum Niepodległości."
    },
    "ARG/I/2": {
        "wartosc_hist": "★★★★",
        "opis_wartosci": "Afisz PON z nazwiskami Sieroszewskiego i Kadena-Bandrowskiego. Druki ulotne 1914 na Rara Avis: 400-1200 PLN. Związek z uznanymi pisarzami podnosi wartość.",
        "cena_min": 1500,
        "cena_max": 3500,
        "waluta": "PLN",
        "rekomendacja": "Rara Avis Kraków (specjalizacja: druki historyczne) lub DESA."
    },
    "ARG/I/3": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Pismo urzędowe PON L.145 — korespondencja służbowa. Porównywalny: pisma organizacji niepodległościowych: 300-800 PLN.",
        "cena_min": 400,
        "cena_max": 1000,
        "waluta": "PLN",
        "rekomendacja": "W zestawie z ARG/I/1-2."
    },
    "ARG/I/4": {
        "wartosc_hist": "★★★★",
        "opis_wartosci": "Pokwitowanie na broń i ekwipunek PON — dokument materialny potwierdzający przekazanie broni. Rzadki typ dokumentu z 1914. Szable, latarka, reflektor.",
        "cena_min": 1000,
        "cena_max": 2500,
        "waluta": "PLN",
        "rekomendacja": "DESA Unicum lub SDA Aukcja Militariów."
    },
    "ARG/I/5": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Koperta PON + Karta Polowa Legionów — dwa obiekty. Ephemera legionowa: 300-800 PLN za każdy.",
        "cena_min": 600,
        "cena_max": 1500,
        "waluta": "PLN",
        "rekomendacja": "W zestawie z Serią I."
    },

    # === SERIA II — GEN. DYW. JANUSZ GŁUCHOWSKI ===
    "ARG/II/1": {
        "wartosc_hist": "★★★★★",
        "opis_wartosci": "Biogram WBH nr 76/45 potwierdzający Siódemkę Beliny. Dokument łączący bezpośrednio z IKONĄ polskiej historii wojskowej. Zaświadczenia WBH: 500-1500 PLN; tu: Siódemka Beliny = unikatowa proweniencja.",
        "cena_min": 3000,
        "cena_max": 8000,
        "waluta": "PLN",
        "rekomendacja": "DESA Unicum — aukcja tematyczna 'Militaria i Historia'. Muzeum Wojska Polskiego jako alternatywa."
    },
    "ARG/II/2": {
        "wartosc_hist": "★★★★★",
        "opis_wartosci": "Fotokopia Siódemki Beliny z podpisami uczestników. IKONOGRAFICZNY DOKUMENT ZAŁOŻYCIELSKI polskiej kawalerii. Nawet jako fotokopia wtórna — podpisy oryginalnych uczestników czynią go unikatem.",
        "cena_min": 5000,
        "cena_max": 15000,
        "waluta": "PLN",
        "rekomendacja": "DESA Unicum lub bezpośrednio Muzeum Wojska Polskiego / Muzeum Kawalerii w Grudziądzu."
    },
    "ARG/II/3": {
        "wartosc_hist": "★★★★",
        "opis_wartosci": "Zaświadczenie OB PPS podpisane przez gen. Sosnkowskiego. Autograf Sosnkowskiego: 2000-5000 PLN sam w sobie. Kontekst OB PPS dodatkowo podnosi wartość.",
        "cena_min": 3000,
        "cena_max": 7000,
        "waluta": "PLN",
        "rekomendacja": "DESA Unicum."
    },
    "ARG/II/4": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "List odręczny na papierze Inspektoratu Armii. Korespondencja generalska: 500-2000 PLN.",
        "cena_min": 800,
        "cena_max": 2000,
        "waluta": "PLN",
        "rekomendacja": "W zestawie z Serią II."
    },
    "ARG/II/5": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Zaświadczenie archiwalne AGAD o złożeniu broni (rewolwer) 1909. Porównywalny: dokumenty AGAD: 300-800 PLN.",
        "cena_min": 400,
        "cena_max": 1000,
        "waluta": "PLN",
        "rekomendacja": "W zestawie."
    },
    "ARG/II/6": {
        "wartosc_hist": "★★",
        "opis_wartosci": "Notatka o Związku Strzeleckim — trudna do jednoznacznej atrybucji. Notatki odręczne: 200-500 PLN.",
        "cena_min": 200,
        "cena_max": 500,
        "waluta": "PLN",
        "rekomendacja": "W zestawie."
    },
    "ARG/II/7": {
        "wartosc_hist": "★",
        "opis_wartosci": "Ciemna, nieczytelna fotografia grupowa. Niska wartość indywidualna: 50-150 PLN.",
        "cena_min": 50,
        "cena_max": 150,
        "waluta": "PLN",
        "rekomendacja": "Tylko w zestawie."
    },
    "ARG/II/8": {
        "wartosc_hist": "★★★★★",
        "opis_wartosci": "AKT ZAŁOŻYCIELSKI 7 Pułku Ułanów Lubelskich — rozkaz z 5.XI.1918, 6 dni przed niepodległością! Rozkazy wojskowe z tego okresu: 2000-5000 PLN. Tu: akt tworzący legendarne pułki — unikat muzealny.",
        "cena_min": 5000,
        "cena_max": 12000,
        "waluta": "PLN",
        "rekomendacja": "DESA Unicum top lot lub depozyt Muzeum Kawalerii Grudziądz / Muzeum Wojska Polskiego."
    },
    "ARG/II/9": {
        "wartosc_hist": "★★",
        "opis_wartosci": "Życzenia od Samorządu Żołnierskiego. Ephemera pułkowa: 200-500 PLN.",
        "cena_min": 200,
        "cena_max": 500,
        "waluta": "PLN",
        "rekomendacja": "W zestawie."
    },
    "ARG/II/10": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Dyplom Krzyża Legionowego — zbliżenie. Dyplomy legionowe: 1000-3000 PLN (Rara Avis #105: dyplom WP sprzedany za 300-650 PLN, ale Krzyż Legionowy rzadszy).",
        "cena_min": 1500,
        "cena_max": 3500,
        "waluta": "PLN",
        "rekomendacja": "DESA lub Rara Avis."
    },
    "ARG/II/11": {
        "wartosc_hist": "★★★★",
        "opis_wartosci": "Dyplom legionowy z portretem Piłsudskiego. Ikonograficzna wartość portretu Komendanta. Dyplomy z wizerunkiem Piłsudskiego: 2000-6000 PLN.",
        "cena_min": 2500,
        "cena_max": 6000,
        "waluta": "PLN",
        "rekomendacja": "DESA Unicum — kolekcjonerzy piłsudczyzny."
    },
    "ARG/II/12": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Propusk w pleń (rosyjski przepustek do niewoli) + legitymacja + pokwitowanie. Trzy dokumenty z I wojny. Łącznie: 600-1500 PLN.",
        "cena_min": 600,
        "cena_max": 1500,
        "waluta": "PLN",
        "rekomendacja": "W zestawie."
    },
    "ARG/II/13": {
        "wartosc_hist": "★★★★",
        "opis_wartosci": "Legitymacja Krzyża Walecznych nr 42888. Leg. KW na Allegro archiwum: 135 PLN (stan zwykły). DESA #197: leg. KW = 800-2000 PLN. Tu: nadanie dla uczestnika Siódemki.",
        "cena_min": 1500,
        "cena_max": 4000,
        "waluta": "PLN",
        "rekomendacja": "DESA lub SDA."
    },
    "ARG/II/14": {
        "wartosc_hist": "★★★★★",
        "opis_wartosci": "List odręczny Śmigłego-Rydza do Głuchowskiego. AUTOGRAF MARSZAŁKA POLSKI / NACZELNEGO WODZA. Autografy Śmigłego-Rydza: 5000-15000 PLN. Kontekst osobisty = premium.",
        "cena_min": 8000,
        "cena_max": 20000,
        "waluta": "PLN",
        "rekomendacja": "DESA Unicum TOP LOT. Alternatywa: sprzedaż prywatna do kolekcjonera piłsudczyzny."
    },
    "ARG/II/15": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Pismo Biura Personalnego MSWojsk. Dokumenty ministerialne: 400-1000 PLN.",
        "cena_min": 400,
        "cena_max": 1000,
        "waluta": "PLN",
        "rekomendacja": "W zestawie."
    },
    "ARG/II/16": {
        "wartosc_hist": "★★★★★",
        "opis_wartosci": "Dyplom Króla Rumunii Ferdynanda I — Order Korony Rumuńskiej. Dyplomy orderów zagranicznych z podpisem monarchy: 3000-10000 PLN. OneBid: Order Korony Rumuńskiej (sam order bez dyplomu) = 1500-4000 PLN. Tu: pełny dyplom z podpisem królewskim.",
        "cena_min": 5000,
        "cena_max": 12000,
        "waluta": "PLN",
        "rekomendacja": "DESA Unicum lub aukcja międzynarodowa (Spink, DNW London). Zainteresowanie: kolekcjonerzy rumuńscy i polscy."
    },
    "ARG/II/17": {
        "wartosc_hist": "★★★★★",
        "opis_wartosci": "Dekret Prezydenta RP — mianowanie. Akty mianowania z podpisem Prezydenta: 3000-8000 PLN.",
        "cena_min": 3000,
        "cena_max": 8000,
        "waluta": "PLN",
        "rekomendacja": "DESA Unicum."
    },
    "ARG/II/18": {
        "wartosc_hist": "★★★★★",
        "opis_wartosci": "AKT MIANOWANIA NA GENERAŁA BRYGADY (26.III.1933). Podpisy Prezydenta RP i Ministra. Akty mianowania generalskie: 5000-15000 PLN.",
        "cena_min": 6000,
        "cena_max": 15000,
        "waluta": "PLN",
        "rekomendacja": "DESA Unicum TOP LOT lub Muzeum Wojska Polskiego."
    },
    "ARG/II/19": {
        "wartosc_hist": "★★★★★",
        "opis_wartosci": "AKT MIANOWANIA NA I WICEMINISTRA SPRAW WOJSKOWYCH (5.X.1935). SZCZYT KARIERY. Unikat — ile było Wiceministrów MSWojsk? Dokument o znaczeniu państwowym.",
        "cena_min": 8000,
        "cena_max": 20000,
        "waluta": "PLN",
        "rekomendacja": "DESA Unicum TOP LOT. Muzeum Wojska Polskiego, IPN."
    },
    "ARG/II/20": {
        "wartosc_hist": "★★",
        "opis_wartosci": "Formularz rozkazu wyjazdu MSWojsk. Dokumenty biurokratyczne: 200-500 PLN.",
        "cena_min": 200,
        "cena_max": 500,
        "waluta": "PLN",
        "rekomendacja": "W zestawie."
    },
    "ARG/II/21": {
        "wartosc_hist": "★★",
        "opis_wartosci": "List prywatny do Pułkownika (1925). Korespondencja prywatna: 300-800 PLN.",
        "cena_min": 300,
        "cena_max": 800,
        "waluta": "PLN",
        "rekomendacja": "W zestawie."
    },
    "ARG/II/22": {
        "wartosc_hist": "★★★★",
        "opis_wartosci": "Fotokopia prasowa — Śmigły-Rydz wręcza sztandar. Podpisane zdjęcia prasowe z identyfikacją osób: 1000-3000 PLN.",
        "cena_min": 1500,
        "cena_max": 3500,
        "waluta": "PLN",
        "rekomendacja": "DESA lub kolekcjoner."
    },
    "ARG/II/23": {
        "wartosc_hist": "★★★★",
        "opis_wartosci": "Portret gen. Głuchowskiego w mundurze galowym. Jedyne zdjęcie portretowe generała. Portrety generałów II RP: 500-2000 PLN.",
        "cena_min": 800,
        "cena_max": 2500,
        "waluta": "PLN",
        "rekomendacja": "W zestawie z aktami mianowania."
    },
    "ARG/II/24": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "List do Generała — Londyn 1943. Korespondencja z PSZ: 300-800 PLN.",
        "cena_min": 300,
        "cena_max": 800,
        "waluta": "PLN",
        "rekomendacja": "W zestawie."
    },
    "ARG/II/25": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Pismo z 2 PP Legionowej. Dokumenty PSZ: 300-700 PLN.",
        "cena_min": 300,
        "cena_max": 700,
        "waluta": "PLN",
        "rekomendacja": "W zestawie."
    },
    "ARG/II/26": {
        "wartosc_hist": "★★★★",
        "opis_wartosci": "Adres iluminowany — akwarela od oficerów IX.1945. Iluminowane adresy: 1500-4000 PLN. Kolorowy, dekoracyjny, z flagami i herbami.",
        "cena_min": 2000,
        "cena_max": 5000,
        "waluta": "PLN",
        "rekomendacja": "DESA Unicum — wartość artystyczna + historyczna."
    },
    "ARG/II/27": {
        "wartosc_hist": "★★★★★",
        "opis_wartosci": "LIST GEN. KAZIMIERZA SOSNKOWSKIEGO Z KANADY do gen. Głuchowskiego — 'Kochany Januszu'. Autograf Naczelnego Wodza PSZ z okresu kanadyjskiego (Arundel, QC). Korespondencja Sosnkowski-Głuchowski na aukcjach: brak porównywalnych transakcji (ekstremalnie rzadkie). Autografy Sosnkowskiego: 3000-8000 PLN. Tu: pełny list prywatny + kontekst OB PPS + Legiony + emigracja = absolutna unikatowość. Porównanie: list Sosnkowskiego do Andersa (DESA 2019) — 12000 PLN.",
        "cena_min": 5000,
        "cena_max": 15000,
        "waluta": "PLN",
        "rekomendacja": "DESA Unicum lub Muzeum Józefa Piłsudskiego w Sulejówku. Alternatywnie: Instytut Piłsudskiego w Londynie (gdzie spoczywają papiery Głuchowskiego). NAJCENNIEJSZY DOKUMENT W KOLEKCJI obok oryginału Hertz-Barwińskiego (ARG/II/59)."
    },
    "ARG/II/28": {
        "wartosc_hist": "★★★★★",
        "opis_wartosci": "'PRO MEMORIA' gen. Sosnkowskiego str. 1 — załącznik do listu z 28.V.1964. Lista 24 zamówień Naczelnego Wodza. Poz. 5: prośba Głuchowskiego o kawalerię. Poz. 7: Smoleński o patrol Beliny. KOMPLET z listem (ARG/II/27) i str. 2 (ARG/II/29): 12 000–28 000 PLN.",
        "cena_min": 3000,
        "cena_max": 8000,
        "waluta": "PLN",
        "rekomendacja": "WYŁĄCZNIE w komplecie z ARG/II/27 i II/29. Instytut Piłsudskiego w Londynie lub Muzeum w Sulejówku."
    },
    "ARG/II/29": {
        "wartosc_hist": "★★★★★",
        "opis_wartosci": "'PRO MEMORIA' str. 2 — Giedroyć/'Kultura', Radio Wolna Europa (J. Nowak-Jeziorański), cytat '80-ty rok życia'. KOMPLET z ARG/II/27 + II/28: 12 000–28 000 PLN.",
        "cena_min": 3000,
        "cena_max": 8000,
        "waluta": "PLN",
        "rekomendacja": "WYŁĄCZNIE w komplecie z ARG/II/27 i II/28. Nigdy nie rozdzielać!"
    },
    "ARG/II/30": {
        "wartosc_hist": "★★★★",
        "opis_wartosci": "Legitymacja oficerska generała — okładka. Leg. oficerskie generałów: 2000-5000 PLN (DESA). Komplet 3 stron: premium.",
        "cena_min": 2000,
        "cena_max": 5000,
        "waluta": "PLN",
        "rekomendacja": "DESA Unicum (sprzedawać ARG/II/30-32 jako komplet)."
    },
    "ARG/II/31": {
        "wartosc_hist": "★★★★",
        "opis_wartosci": "Legitymacja oficerska — rozkładówka z danymi i zdjęciem. Wliczona w komplet ARG/II/30-32.",
        "cena_min": 0,
        "cena_max": 0,
        "waluta": "PLN",
        "rekomendacja": "Sprzedawać z ARG/II/30."
    },
    "ARG/II/32": {
        "wartosc_hist": "★★★★",
        "opis_wartosci": "Legitymacja oficerska — wpisy służbowe. Wliczona w komplet.",
        "cena_min": 0,
        "cena_max": 0,
        "waluta": "PLN",
        "rekomendacja": "Sprzedawać z ARG/II/30."
    },

    # === SERIA III — PPOR. STANISŁAW STEFAN GŁUCHOWSKI ===
    "ARG/III/1": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Kriegsgefangenenpost — kartka jeńca, awers. OneBid: listy z obozów jenieckich: 80-300 PLN za sztukę. Rara Avis #105: dokumenty WP: 120-650 PLN.",
        "cena_min": 150,
        "cena_max": 400,
        "waluta": "PLN",
        "rekomendacja": "W zestawie z całą korespondencją obozową."
    },
    "ARG/III/2": {
        "wartosc_hist": "★★★★",
        "opis_wartosci": "Rewers z KLUCZOWĄ informacją — ojciec i syn w różnych obozach. Wartość narracyjna podnosi cenę: 200-500 PLN.",
        "cena_min": 200,
        "cena_max": 500,
        "waluta": "PLN",
        "rekomendacja": "W zestawie."
    },
    "ARG/III/3": {
        "wartosc_hist": "★★★★★",
        "opis_wartosci": "Korespondencja OJCIEC→SYN między dwoma Stalagami. DOKUMENT WYJĄTKOWY — korespondencja między dwoma jeńcami z tej samej rodziny. Typowe Kriegsgefangenenpost: 80-300 PLN, ale ten: 500-1500 PLN za wyjątkowość.",
        "cena_min": 500,
        "cena_max": 1500,
        "waluta": "PLN",
        "rekomendacja": "W zestawie z Serią III i V — narracja rodzinna."
    },
    "ARG/III/4": {
        "wartosc_hist": "★★★★",
        "opis_wartosci": "Rewers — intymny list ojca do syna. Wspomina adres w Częstochowie. 200-500 PLN.",
        "cena_min": 200,
        "cena_max": 500,
        "waluta": "PLN",
        "rekomendacja": "W zestawie."
    },
    "ARG/III/5": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Kartka 4.XII.1944 do Kleczewa. Kriegsgefangenenpost standardowy: 100-300 PLN.",
        "cena_min": 100,
        "cena_max": 300,
        "waluta": "PLN",
        "rekomendacja": "W zestawie."
    },
    "ARG/III/6": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Rewers 30.X.1944 z numerem Krzysztofa (141009). 100-300 PLN.",
        "cena_min": 100,
        "cena_max": 300,
        "waluta": "PLN",
        "rekomendacja": "W zestawie."
    },
    "ARG/III/7": {
        "wartosc_hist": "★",
        "opis_wartosci": "Wyblakły stempel cenzora. Minimalna wartość indywidualna: 30-80 PLN.",
        "cena_min": 30,
        "cena_max": 80,
        "waluta": "PLN",
        "rekomendacja": "Tylko w zestawie."
    },
    "ARG/III/8": {
        "wartosc_hist": "★★",
        "opis_wartosci": "List obozowy 16.X.1944, zniszczony. Słaby stan obniża cenę: 80-200 PLN.",
        "cena_min": 80,
        "cena_max": 200,
        "waluta": "PLN",
        "rekomendacja": "W zestawie."
    },
    "ARG/III/9": {
        "wartosc_hist": "★★",
        "opis_wartosci": "Adres baraku obozowego. Ephemera: 50-150 PLN.",
        "cena_min": 50,
        "cena_max": 150,
        "waluta": "PLN",
        "rekomendacja": "W zestawie."
    },

    # -- Stefan: dokumenty urzędowe i wojenne (ARG/III/10-37) --
    "ARG/III/10": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Zarządzenie PRM nr 3743 z 1929 — Komisja Dyscyplinarna. Dokumenty urzędowe II RP: 150-400 PLN.",
        "cena_min": 150,
        "cena_max": 400,
        "waluta": "PLN",
        "rekomendacja": "W zestawie z ARG/III/11-19 (dokumenty kariery)."
    },
    "ARG/III/11": {
        "wartosc_hist": "★★★★",
        "opis_wartosci": "Dyplom Brązowego Medalu za Długoletnią Służbę, 1938. Dyplomy medali II RP: 200-600 PLN. Kancelaria Prezydenta = prestiż.",
        "cena_min": 300,
        "cena_max": 700,
        "waluta": "PLN",
        "rekomendacja": "W zestawie."
    },
    "ARG/III/12": {
        "wartosc_hist": "★★★★",
        "opis_wartosci": "Dyplom Złotego KZ, 11.XI.1936. Dyplomy ZKZ II RP: 300-800 PLN. Pieczęć Prezydenta RP podnosi wartość.",
        "cena_min": 400,
        "cena_max": 900,
        "waluta": "PLN",
        "rekomendacja": "W zestawie z odzn. Stefana."
    },
    "ARG/III/13": {
        "wartosc_hist": "★★",
        "opis_wartosci": "Dokument urzędowy, pismo administracyjne. 100-250 PLN.",
        "cena_min": 100,
        "cena_max": 250,
        "waluta": "PLN",
        "rekomendacja": "W zestawie."
    },
    "ARG/III/14": {
        "wartosc_hist": "★★",
        "opis_wartosci": "Dokument urzędowy. 100-250 PLN.",
        "cena_min": 100,
        "cena_max": 250,
        "waluta": "PLN",
        "rekomendacja": "W zestawie."
    },
    "ARG/III/15": {
        "wartosc_hist": "★★★★★",
        "opis_wartosci": "Pismo z Rezydencji w Spale — polowanie prezydenckie na Św. Huberta 1930! Stefan jako uczestnik polowania Prezydenta Mościckiego. RZADKI dokument: dostęp do Prezydenta. 800-2000 PLN.",
        "cena_min": 800,
        "cena_max": 2000,
        "waluta": "PLN",
        "rekomendacja": "UNIKAT — Spała. DESA Unicum lub Rara Avis."
    },
    "ARG/III/16": {
        "wartosc_hist": "★★★★★",
        "opis_wartosci": "Dyplom Krzyża Niepodległości, 9.XI.1931. KN to jedno z najważniejszych odznaczeń II RP — przyznawany za walkę o niepodległość 1914-21. Dyplomy KN: 500-2000 PLN.",
        "cena_min": 800,
        "cena_max": 2500,
        "waluta": "PLN",
        "rekomendacja": "DESA Unicum. Wysokiej rangi odznaczenie."
    },
    "ARG/III/17": {
        "wartosc_hist": "★★★★",
        "opis_wartosci": "Order Odrodzenia Polski V kl. (Kawalera), 1931. Dyplomy OOP: 400-1200 PLN.",
        "cena_min": 500,
        "cena_max": 1500,
        "waluta": "PLN",
        "rekomendacja": "W zestawie z KN."
    },
    "ARG/III/18": {
        "wartosc_hist": "★★",
        "opis_wartosci": "Pismo urzędowe, awans. 100-300 PLN.",
        "cena_min": 100,
        "cena_max": 300,
        "waluta": "PLN",
        "rekomendacja": "W zestawie."
    },
    "ARG/III/19": {
        "wartosc_hist": "★★★★",
        "opis_wartosci": "Dyplom Srebrnego KZ, 1929, podpis Prezesa RM (Kazimierz Bartel). Dyplomy SKZ: 200-600 PLN. Podpis Bartla podnosi wartość.",
        "cena_min": 300,
        "cena_max": 800,
        "waluta": "PLN",
        "rekomendacja": "W zestawie z ARG/III/12."
    },
    "ARG/III/21": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Zatwierdzenie zatrudnienia, Kancelaria Naczelnika Państwa 1921. Pieczęć urzędowa. Dokumenty KNP: 200-500 PLN.",
        "cena_min": 200,
        "cena_max": 500,
        "waluta": "PLN",
        "rekomendacja": "W zestawie chronologicznym kariery Stefana."
    },
    "ARG/III/22": {
        "wartosc_hist": "★★★★",
        "opis_wartosci": "Nominacja na VIII stopień przez Prezydenta RP z pieczęcią LAKOWĄ Prezydenta! Dokumenty z pieczęcią lakową: 500-1500 PLN.",
        "cena_min": 600,
        "cena_max": 1500,
        "waluta": "PLN",
        "rekomendacja": "PIECZĘĆ LAKOWA Prezydenta RP — wysoka wartość kolekcjonerska."
    },
    "ARG/III/23": {
        "wartosc_hist": "★★★★★",
        "opis_wartosci": "NAJWCZEŚNIEJSZY DOKUMENT — zatrudnienie w Kancelarii Naczelnika Państwa (Piłsudski!), 1.VII.1921. Dokumenty z KNP (Piłsudski): 500-2000 PLN. Pieczęć państwowa z Orłem.",
        "cena_min": 800,
        "cena_max": 2500,
        "waluta": "PLN",
        "rekomendacja": "KLUCZOWY DOKUMENT — początek kariery. Piłsudski jako Naczelnik Państwa."
    },
    "ARG/III/24": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Podwyżka kategorii płac, 1921. Dokumenty kadrowe II RP: 100-300 PLN.",
        "cena_min": 100,
        "cena_max": 300,
        "waluta": "PLN",
        "rekomendacja": "W zestawie."
    },
    "ARG/III/25": {
        "wartosc_hist": "★★",
        "opis_wartosci": "Pismo o uposażeniu, silnie uszkodzone. 80-200 PLN.",
        "cena_min": 80,
        "cena_max": 200,
        "waluta": "PLN",
        "rekomendacja": "W zestawie — wymaga lepszego zdjęcia."
    },
    "ARG/III/26": {
        "wartosc_hist": "★★★★",
        "opis_wartosci": "Mianowanie na Pomocnika Referenta KNP, 31.XII.1921. Formalna nominacja z pieczęcią. 300-700 PLN.",
        "cena_min": 300,
        "cena_max": 700,
        "waluta": "PLN",
        "rekomendacja": "W zestawie z ARG/III/23."
    },
    "ARG/III/27": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Medal Dziesięciolecia, 1929. Dyplomy medali masowych: 100-400 PLN.",
        "cena_min": 150,
        "cena_max": 400,
        "waluta": "PLN",
        "rekomendacja": "W zestawie."
    },
    "ARG/III/28": {
        "wartosc_hist": "★★★★★",
        "opis_wartosci": "Zaświadczenie AK nr 2856 z 25.VII.1944 — 6 DNI przed Powstaniem! Pieczęć Obwodu Śródmieście, podpis Radwan. Dokumenty AK z Powstania: 2000-8000 PLN. Stefan aresztowany przez Gestapo w V.1944, zwolniony 29.VII!",
        "cena_min": 3000,
        "cena_max": 8000,
        "waluta": "PLN",
        "rekomendacja": "DESA Unicum — KLUCZOWY DOKUMENT POWSTAŃCZY. Pieczęć + podpis Radwana."
    },
    "ARG/III/29": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Etykieta archiwalna zbioru listów. Wartość kontekstowa: 50-150 PLN.",
        "cena_min": 50,
        "cena_max": 150,
        "waluta": "PLN",
        "rekomendacja": "Razem z korespondencją."
    },
    "ARG/III/30": {
        "wartosc_hist": "★★★★★",
        "opis_wartosci": "Karta przydziału AK — Kwatermistrzostwo Obwodu I Śródmieście, pieczęć + podpis Radwan. UZUPEŁNIA ARG/III/28. Dokumenty AK z pieczęcią: 1500-5000 PLN.",
        "cena_min": 2000,
        "cena_max": 6000,
        "waluta": "PLN",
        "rekomendacja": "W PARZE z ARG/III/28 — zaświadczenie + karta przydziału."
    },
    "ARG/III/31": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Formularz weryfikacji AK, 1946. Dokumenty weryfikacyjne: 200-500 PLN.",
        "cena_min": 200,
        "cena_max": 500,
        "waluta": "PLN",
        "rekomendacja": "W zestawie z ARG/III/28, V/169."
    },
    "ARG/III/32": {
        "wartosc_hist": "★★★★",
        "opis_wartosci": "Kriegsgefangenenpost z Oflagu XVII A — pocztówka jeniecka z cenzurą. 150-400 PLN (standard), ale Oflag + cenzura: 300-800 PLN.",
        "cena_min": 300,
        "cena_max": 800,
        "waluta": "PLN",
        "rekomendacja": "W zestawie z korespondencją obozową."
    },
    "ARG/III/33": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Notatka o Jedigarze i Poźniowskim. Wartość kontekstowa: 100-300 PLN.",
        "cena_min": 100,
        "cena_max": 300,
        "waluta": "PLN",
        "rekomendacja": "W zestawie z dokumentami 7 P.UŁ."
    },
    "ARG/III/34": {
        "wartosc_hist": "★★★★",
        "opis_wartosci": "Lista personalna 7 P.UŁ. z DWOMA Głuchowskimi — Krzysztof i Zbigniew. Listy personalne AK: 300-800 PLN. Wartość narracyjna.",
        "cena_min": 400,
        "cena_max": 1000,
        "waluta": "PLN",
        "rekomendacja": "W zestawie z ARG/V/171."
    },
    "ARG/III/35": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Certyfikat inwentarzowy 7 P.UŁ., 1946. Dokumenty pułkowe: 200-600 PLN.",
        "cena_min": 200,
        "cena_max": 600,
        "waluta": "PLN",
        "rekomendacja": "W zestawie."
    },
    "ARG/III/36": {
        "wartosc_hist": "★★★★",
        "opis_wartosci": "Dedykacja od oficerów dla Stefana — zbiorowe podpisy, wartość sentymentalna i historyczna. 300-800 PLN.",
        "cena_min": 300,
        "cena_max": 800,
        "waluta": "PLN",
        "rekomendacja": "W zestawie."
    },
    "ARG/III/37": {
        "wartosc_hist": "★★★★",
        "opis_wartosci": "Karta pułkowa 7 P.UŁ. im. Sosnkowskiego z Henstedt 1947 z nazwiskiem ppor. Głuchowskiego. Militaria pułkowe: 200-600 PLN.",
        "cena_min": 300,
        "cena_max": 700,
        "waluta": "PLN",
        "rekomendacja": "W zestawie z dokumentami 7 P.UŁ."
    },

    # -- Wycena ARG/I/6 — biogram Lecha --
    "ARG/I/6": {
        "wartosc_hist": "★★★★★",
        "opis_wartosci": "Biogram rtm. Lecha Głuchowskiego 'Jeżycki' (1902-1944) — dowódcy dywizjonu 'Jeleń', POLEGŁEGO na Mokotowie 15.IX.1944. Spisany przez bratanka Krzysztofa w Rio de Janeiro 1995. Biogramy powstańcze z bibliografią: 300-800 PLN. Wartość archiwalna i genealogiczna.",
        "cena_min": 500,
        "cena_max": 1200,
        "waluta": "PLN",
        "rekomendacja": "Kluczowy dokument genealogiczny. Muzeum Powstania Warszawskiego?"
    },

    # === SERIA V — KRZYSZTOF ANDRZEJ GŁUCHOWSKI ===

    # -- Okupacja i AK --
    "ARG/V/1": {
        "wartosc_hist": "★★★★",
        "opis_wartosci": "Kennkarte GG — okładka. OneBid: Kennkarte GG Warszawa = 200-600 PLN. Komplet z ARG/V/2.",
        "cena_min": 400,
        "cena_max": 1000,
        "waluta": "PLN",
        "rekomendacja": "Sprzedawać w parze ARG/V/1-2."
    },
    "ARG/V/2": {
        "wartosc_hist": "★★★★",
        "opis_wartosci": "Kennkarte GG — wnętrze ze zdjęciem żołnierza AK. Wliczona w komplet ARG/V/1-2. Wartość dodana: osoba = żołnierz AK, powstaniec.",
        "cena_min": 0,
        "cena_max": 0,
        "waluta": "PLN",
        "rekomendacja": "W parze z ARG/V/1."
    },
    "ARG/V/3": {
        "wartosc_hist": "★★★★★",
        "opis_wartosci": "LEGITYMACJA AK ps. 'Juras', plut. 1112, 7 P.Uł. 'Jeleń'. KLUCZOWY DOKUMENT. Leg. AK + galony: SDA/DESA: 2000-8000 PLN. Tu: identyfikacja z konkretnym plutonem powstańczym + galony.",
        "cena_min": 4000,
        "cena_max": 10000,
        "waluta": "PLN",
        "rekomendacja": "DESA Unicum lub SDA Aukcja Militariów. TOP LOT serii V."
    },
    "ARG/V/4": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Zbliżenie legitymacji AK. Dokumentacyjne, wliczone w ARG/V/3.",
        "cena_min": 0,
        "cena_max": 0,
        "waluta": "PLN",
        "rekomendacja": "W parze z ARG/V/3."
    },
    "ARG/V/5": {
        "wartosc_hist": "★★★★★",
        "opis_wartosci": "List z Powstania — 'Krychu!'. KORESPONDENCJA Z OBLĘŻONEJ WARSZAWY. Muzeum Powstania Warszawskiego kupiło listy na aukcji w Düsseldorfie (2008). Listy z Powstania: 2000-8000 PLN.",
        "cena_min": 3000,
        "cena_max": 8000,
        "waluta": "PLN",
        "rekomendacja": "Muzeum Powstania Warszawskiego (priorytet!) lub DESA Unicum."
    },
    "ARG/V/6": {
        "wartosc_hist": "★★★★★",
        "opis_wartosci": "LIST DO RODZICÓW Z POWSTANIA — 26.VIII.1944. 'Kochana Maminko i Tatusiu' — 18-latek pisze z walczącego miasta. Jeden z najrzadszych typów dokumentów. Szacunek: 3000-10000 PLN.",
        "cena_min": 4000,
        "cena_max": 12000,
        "waluta": "PLN",
        "rekomendacja": "Muzeum Powstania Warszawskiego — TOP PRIORYTET. To jest dokument muzealny."
    },
    "ARG/V/7": {
        "wartosc_hist": "★★★★★",
        "opis_wartosci": "Przepustka AK z 29.IX.1944 — DZIEŃ PRZED KAPITULACJĄ. Przepustki AK: 1000-3000 PLN. Tu: data czyni go wyjątkowym.",
        "cena_min": 2000,
        "cena_max": 5000,
        "waluta": "PLN",
        "rekomendacja": "MPW lub DESA."
    },
    "ARG/V/8": {
        "wartosc_hist": "★★★★★",
        "opis_wartosci": "Rozkaz awansu i odznaczenia KW z 29.IX.1944. Rozkazy polowe z Powstania: 2000-6000 PLN. DESA #202: Krzyż Walecznych 1944 = 4000 PLN (sam metal).",
        "cena_min": 3000,
        "cena_max": 8000,
        "waluta": "PLN",
        "rekomendacja": "DESA Unicum lub SDA."
    },

    # -- Niewola --
    "ARG/V/9": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Bilet identyfikacyjny jeńca nr 141009, Stalag XI B. Bilety jenieckie: 200-600 PLN.",
        "cena_min": 300,
        "cena_max": 700,
        "waluta": "PLN",
        "rekomendacja": "W zestawie z dokumentami obozowymi."
    },
    "ARG/V/10": {
        "wartosc_hist": "★★★★",
        "opis_wartosci": "Personalkarte I — karta osobowa jeńca. Personalkarten: 300-800 PLN na OneBid/SDA.",
        "cena_min": 400,
        "cena_max": 1000,
        "waluta": "PLN",
        "rekomendacja": "W zestawie."
    },
    "ARG/V/11": {
        "wartosc_hist": "★★",
        "opis_wartosci": "Karta zdrowia obozowa. Formularze medyczne: 100-300 PLN.",
        "cena_min": 100,
        "cena_max": 300,
        "waluta": "PLN",
        "rekomendacja": "W zestawie."
    },
    "ARG/V/12": {
        "wartosc_hist": "★★",
        "opis_wartosci": "Karta zdrowia Stammlager VI J. j.w.: 100-300 PLN.",
        "cena_min": 100,
        "cena_max": 300,
        "waluta": "PLN",
        "rekomendacja": "W zestawie."
    },

    # -- Korespondencja obozowa --
    "ARG/V/13": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "List Krzysztofa — 'Trzymamy się do końca!'. Listy jenieckie: 100-300 PLN.",
        "cena_min": 150,
        "cena_max": 400,
        "waluta": "PLN",
        "rekomendacja": "W zestawie."
    },
    "ARG/V/14": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Antwort-Postkarte Krzysztof ze Stalag VI/3. Kriegsgefangenenpost: 100-300 PLN.",
        "cena_min": 100,
        "cena_max": 300,
        "waluta": "PLN",
        "rekomendacja": "W zestawie."
    },
    "ARG/V/15": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Odpowiedź rodziny — kilka osób na jednej kartce. Wartość narracyjna: 150-400 PLN.",
        "cena_min": 150,
        "cena_max": 400,
        "waluta": "PLN",
        "rekomendacja": "W zestawie."
    },
    "ARG/V/16": {
        "wartosc_hist": "★★★★",
        "opis_wartosci": "List do stryja generała z obozu, wspomina 2417 km podróży. Wartość narracyjna: 300-700 PLN.",
        "cena_min": 300,
        "cena_max": 700,
        "waluta": "PLN",
        "rekomendacja": "W zestawie."
    },
    "ARG/V/17": {
        "wartosc_hist": "★★★★★",
        "opis_wartosci": "Kartka z obozu do GENERAŁA GŁUCHOWSKIEGO w Londynie. Trójjęzyczny dokument (niem./ang./pol.). Adres: Polish War's Office, London. Stempel PASSED XII. DOKUMENT WYJĄTKOWY: jeniec pisze do generała-stryja w Londynie.",
        "cena_min": 800,
        "cena_max": 2000,
        "waluta": "PLN",
        "rekomendacja": "DESA lub MPW — wartość narracyjna i ikonograficzna."
    },
    "ARG/V/18": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Długi list obozowy — 17 punktów. Listy jenieckie z treścią: 200-500 PLN.",
        "cena_min": 200,
        "cena_max": 500,
        "waluta": "PLN",
        "rekomendacja": "W zestawie."
    },
    "ARG/V/19": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Koperta Kriegsgefangenenpost syn→ojciec. Koperty z pieczęcią cenzury: 80-250 PLN.",
        "cena_min": 100,
        "cena_max": 300,
        "waluta": "PLN",
        "rekomendacja": "W zestawie."
    },

    # -- Notatki i Powstanie z pamięci --
    "ARG/V/20": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Notatki z Powstania — pseudonim 'Gryfon'. Notatki z nazwiskami: 200-500 PLN.",
        "cena_min": 200,
        "cena_max": 500,
        "waluta": "PLN",
        "rekomendacja": "W zestawie."
    },
    "ARG/V/21": {
        "wartosc_hist": "★★★★★",
        "opis_wartosci": "RELACJA Z POWSTANIA WARSZAWSKIEGO z konkretnymi danymi: 508 strat, gen. Bór-Komorowski, pluton 1112. DOKUMENT ŹRÓDŁOWY. Relacje naocznych świadków Powstania: 3000-8000 PLN.",
        "cena_min": 3000,
        "cena_max": 8000,
        "waluta": "PLN",
        "rekomendacja": "Muzeum Powstania Warszawskiego lub IPN."
    },
    "ARG/V/22": {
        "wartosc_hist": "★★★★",
        "opis_wartosci": "Mapka taktyczna z kompasem — Wołomin. Szkice taktyczne z Powstania: 500-2000 PLN.",
        "cena_min": 800,
        "cena_max": 2000,
        "waluta": "PLN",
        "rekomendacja": "MPW lub kolekcjoner militariów."
    },

    # -- Pamiętnik obozowy --
    "ARG/V/23": {
        "wartosc_hist": "★★★★",
        "opis_wartosci": "Pamiętnik obozowy — str. 1. Pamiętniki jenieckie: jako komplet (ARG/V/23-33) = 3000-8000 PLN. Jednostkowa str.: 200-500 PLN.",
        "cena_min": 200,
        "cena_max": 500,
        "waluta": "PLN",
        "rekomendacja": "SPRZEDAWAĆ JAKO KOMPLET (11 stron pamiętnika)."
    },
    "ARG/V/24": {"wartosc_hist": "★★★", "opis_wartosci": "Pamiętnik str. 2. W komplecie.", "cena_min": 0, "cena_max": 0, "waluta": "PLN", "rekomendacja": "W komplecie ARG/V/23-33."},
    "ARG/V/25": {"wartosc_hist": "★★★★", "opis_wartosci": "Pamiętnik — wspomnienia z dzieciństwa. Najpiękniejsza strona: 'Dzieciństwo moje to szczęśliwe...' Kontrast z obozem. W komplecie.", "cena_min": 0, "cena_max": 0, "waluta": "PLN", "rekomendacja": "W komplecie."},
    "ARG/V/26": {"wartosc_hist": "★★★", "opis_wartosci": "Pamiętnik str. 4. W komplecie.", "cena_min": 0, "cena_max": 0, "waluta": "PLN", "rekomendacja": "W komplecie."},
    "ARG/V/27": {"wartosc_hist": "★★★", "opis_wartosci": "Notatnik — Stalag VI/17. W komplecie.", "cena_min": 0, "cena_max": 0, "waluta": "PLN", "rekomendacja": "W komplecie."},
    "ARG/V/28": {"wartosc_hist": "★★★", "opis_wartosci": "Wspomnienia 1940. W komplecie.", "cena_min": 0, "cena_max": 0, "waluta": "PLN", "rekomendacja": "W komplecie."},
    "ARG/V/29": {"wartosc_hist": "★★★", "opis_wartosci": "Notatki na formularzu Kaufmannsgehilfenprüfung — recykling papieru. W komplecie.", "cena_min": 0, "cena_max": 0, "waluta": "PLN", "rekomendacja": "W komplecie."},
    "ARG/V/30": {"wartosc_hist": "★★★", "opis_wartosci": "Formularz kupiecki z rysunkiem. W komplecie.", "cena_min": 0, "cena_max": 0, "waluta": "PLN", "rekomendacja": "W komplecie."},
    "ARG/V/31": {"wartosc_hist": "★★★★", "opis_wartosci": "Notatki 22.VIII.1945 — przejście od niewoli do wolności. Kluczowa data. W komplecie.", "cena_min": 0, "cena_max": 0, "waluta": "PLN", "rekomendacja": "W komplecie."},
    "ARG/V/32": {"wartosc_hist": "★★★", "opis_wartosci": "Pamiętnik — Bitwy, 1934. W komplecie.", "cena_min": 0, "cena_max": 0, "waluta": "PLN", "rekomendacja": "W komplecie."},
    "ARG/V/33": {"wartosc_hist": "★★★", "opis_wartosci": "Pamiętnik — Leżność, Stalgów. W komplecie.", "cena_min": 0, "cena_max": 0, "waluta": "PLN", "rekomendacja": "W komplecie."},
    "ARG/V/34": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Tabela / rozkład marszowy: Remo, Genova, Fort. Dokumenty transportowe: 150-400 PLN.",
        "cena_min": 150,
        "cena_max": 400,
        "waluta": "PLN",
        "rekomendacja": "W zestawie."
    },

    # -- Wyzwolenie i repatriacja --
    "ARG/V/35": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "List powojenny 6.VII.1945. Korespondencja powojenna: 150-400 PLN.",
        "cena_min": 150,
        "cena_max": 400,
        "waluta": "PLN",
        "rekomendacja": "W zestawie."
    },
    "ARG/V/36": {
        "wartosc_hist": "★★★★★",
        "opis_wartosci": "KLUCZOWA RELACJA — Düsseldorf 2.VI.1945, 9 dni po wyzwoleniu. Szczegółowy opis walk, kapitulacji, transportu. Wspomina Bora Komorowskiego, V.S.O.P. Relacje z wyzwolenia: 1000-3000 PLN.",
        "cena_min": 1500,
        "cena_max": 4000,
        "waluta": "PLN",
        "rekomendacja": "MPW lub DESA."
    },
    "ARG/V/37": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "List na papeterii Emil Schröder & Co. Wartość dokumentalna + ciekawostka papeterii: 200-500 PLN.",
        "cena_min": 200,
        "cena_max": 500,
        "waluta": "PLN",
        "rekomendacja": "W zestawie."
    },
    "ARG/V/38": {"wartosc_hist": "★★", "opis_wartosci": "Kontynuacja listu 2.II.1945. 100-300 PLN.", "cena_min": 100, "cena_max": 300, "waluta": "PLN", "rekomendacja": "W zestawie."},
    "ARG/V/39": {"wartosc_hist": "★★", "opis_wartosci": "List 5.VIII.1949 na papeterii Schröder. 100-300 PLN.", "cena_min": 100, "cena_max": 300, "waluta": "PLN", "rekomendacja": "W zestawie."},
    "ARG/V/40": {
        "wartosc_hist": "★★★★★",
        "opis_wartosci": "CARD OF IDENTITY — wyzwolony jeniec, 27.IV.1945. Pierwszy dokument wolności. 11 dni przed kapitulacją Niemiec. Karty tożsamości alianckiej: 500-1500 PLN.",
        "cena_min": 800,
        "cena_max": 2000,
        "waluta": "PLN",
        "rekomendacja": "DESA lub SDA."
    },
    "ARG/V/41": {
        "wartosc_hist": "★★★★",
        "opis_wartosci": "Zaświadczenie o konspiracji AK — 3 lata służby, ps. Jurat/Język. Zaświadczenia AK: 800-2500 PLN.",
        "cena_min": 1000,
        "cena_max": 3000,
        "waluta": "PLN",
        "rekomendacja": "DESA lub SDA."
    },
    "ARG/V/42": {
        "wartosc_hist": "★★★★★",
        "opis_wartosci": "Dwa zaświadczenia: KW + awans (Hensstedt 1945). Płk. Kłopacz potwierdza odznaczenie. 1000-3000 PLN.",
        "cena_min": 1500,
        "cena_max": 3500,
        "waluta": "PLN",
        "rekomendacja": "DESA — w zestawie z ARG/V/43."
    },
    "ARG/V/43": {
        "wartosc_hist": "★★★★★",
        "opis_wartosci": "ZAŚWIADCZENIE PŁK. ZIEMSKIEGO — D-ca Grupy 'Północ' potwierdza walkę w Obronie Starego Miasta. Płk. Karol Ziemski — dowódca 5000+ żołnierzy. Zaświadczenia od dowódców Powstania: 2000-6000 PLN.",
        "cena_min": 3000,
        "cena_max": 7000,
        "waluta": "PLN",
        "rekomendacja": "DESA Unicum TOP LOT lub MPW."
    },

    # -- Repatriacja Francja --
    "ARG/V/44": {"wartosc_hist": "★★★", "opis_wartosci": "Ulotka repatriacyjna 'Nareszcie... RODACY'. Druki DP: 200-600 PLN.", "cena_min": 200, "cena_max": 600, "waluta": "PLN", "rekomendacja": "W zestawie."},
    "ARG/V/45": {"wartosc_hist": "★★", "opis_wartosci": "Rewers ulotki — lista stacji PCK. j.w.", "cena_min": 0, "cena_max": 0, "waluta": "PLN", "rekomendacja": "W parze z ARG/V/44."},
    "ARG/V/46": {
        "wartosc_hist": "★★★★",
        "opis_wartosci": "Carte de Rapatrié — karta repatrianta z Centre d'Orsay (obecne Musée d'Orsay). Unikatowa proweniencja. Karty repatriacyjne: 300-800 PLN.",
        "cena_min": 400,
        "cena_max": 1000,
        "waluta": "PLN",
        "rekomendacja": "DESA lub kolekcjoner francuskiego WWII."
    },
    "ARG/V/47": {"wartosc_hist": "★★★", "opis_wartosci": "Fiche de Transport. Formularze repatriacyjne: 150-400 PLN.", "cena_min": 150, "cena_max": 400, "waluta": "PLN", "rekomendacja": "W zestawie."},
    "ARG/V/48": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Skierowanie z Ambasady RP w Paryżu na kurs w Villard-de-Lans. Dokumenty ambasady: 300-700 PLN.",
        "cena_min": 300,
        "cena_max": 700,
        "waluta": "PLN",
        "rekomendacja": "W zestawie."
    },
    "ARG/V/49": {"wartosc_hist": "★", "opis_wartosci": "Drobiazgi obozowe — ephemera. 50-150 PLN.", "cena_min": 50, "cena_max": 150, "waluta": "PLN", "rekomendacja": "W zestawie."},
    "ARG/V/50": {"wartosc_hist": "★★", "opis_wartosci": "Spis adresów + wizytówka rzeźbiarza. 80-250 PLN.", "cena_min": 80, "cena_max": 250, "waluta": "PLN", "rekomendacja": "W zestawie."},
    "ARG/V/51": {"wartosc_hist": "★", "opis_wartosci": "Krótka notatka. 30-80 PLN.", "cena_min": 30, "cena_max": 80, "waluta": "PLN", "rekomendacja": "Tylko w zestawie."},
    "ARG/V/52": {"wartosc_hist": "★★", "opis_wartosci": "Mapka Marsylii — Canebière. Ciekawy ephemera: 80-250 PLN.", "cena_min": 80, "cena_max": 250, "waluta": "PLN", "rekomendacja": "W zestawie."},
    "ARG/V/53": {"wartosc_hist": "★★", "opis_wartosci": "List z Francji. 100-300 PLN.", "cena_min": 100, "cena_max": 300, "waluta": "PLN", "rekomendacja": "W zestawie."},

    # -- PSZ, II Korpus, Gimnazjum 3DSK --
    "ARG/V/54": {
        "wartosc_hist": "★★★★",
        "opis_wartosci": "Skierowanie na RTG z 7 P.Uł. im. Gen. Głuchowskiego. Pułk nosi imię stryja! Dokumenty II Korpusu: 200-600 PLN. Proweniencja: +100%.",
        "cena_min": 400,
        "cena_max": 1000,
        "waluta": "PLN",
        "rekomendacja": "W zestawie."
    },
    "ARG/V/55": {"wartosc_hist": "★", "opis_wartosci": "Formularz administracyjny, wyblakły. 50-150 PLN.", "cena_min": 50, "cena_max": 150, "waluta": "PLN", "rekomendacja": "Tylko w zestawie."},
    "ARG/V/56": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Przepustka z II Korpusu — Amandola. Przepustki wojskowe: 150-400 PLN.",
        "cena_min": 200,
        "cena_max": 500,
        "waluta": "PLN",
        "rekomendacja": "W zestawie."
    },
    "ARG/V/57": {"wartosc_hist": "★★", "opis_wartosci": "Przepustka Baza Personalna 2 Korpusu. 100-300 PLN.", "cena_min": 100, "cena_max": 300, "waluta": "PLN", "rekomendacja": "W zestawie."},
    "ARG/V/58": {
        "wartosc_hist": "★★★★",
        "opis_wartosci": "Okładka EXERCISE BOOK — brytyjski zeszyt szkolny polskiego żołnierza. Zeszyty 3DSK: jako komplet (ARG/V/58-64): 2000-5000 PLN.",
        "cena_min": 300,
        "cena_max": 700,
        "waluta": "PLN",
        "rekomendacja": "SPRZEDAWAĆ JAKO KOMPLET (zeszyt + 6 esejów + tylna okładka)."
    },
    "ARG/V/59": {
        "wartosc_hist": "★★★★★",
        "opis_wartosci": "ESEJ SZKOLNY O POWSTANIU — 19-latek pisze o walkach rok po Powstaniu. Unikatowy dokument edukacyjno-wojskowy. W komplecie zeszytu.",
        "cena_min": 0, "cena_max": 0, "waluta": "PLN", "rekomendacja": "W komplecie ARG/V/58-64."
    },
    "ARG/V/60": {
        "wartosc_hist": "★★★★★",
        "opis_wartosci": "Esej pisany DOKŁADNIE ROK PO WYBUCHU POWSTANIA — 1.VIII.1945, godz. 15:00. Wspomina Bora Komorowskiego. DOKUMENT UNIKATOWY.",
        "cena_min": 0, "cena_max": 0, "waluta": "PLN", "rekomendacja": "W komplecie."
    },
    "ARG/V/61": {
        "wartosc_hist": "★★★★★",
        "opis_wartosci": "Esej o artykułach stryja-generała o Powstaniu. AUTOREFERENCYJNY — uczeń pisze o artykułach stryja o wojnie, w której sam walczył.",
        "cena_min": 0, "cena_max": 0, "waluta": "PLN", "rekomendacja": "W komplecie."
    },
    "ARG/V/62": {"wartosc_hist": "★★★", "opis_wartosci": "Esej — Wyspiański, 11 Listopada. Program maturalny. W komplecie.", "cena_min": 0, "cena_max": 0, "waluta": "PLN", "rekomendacja": "W komplecie."},
    "ARG/V/63": {"wartosc_hist": "★★", "opis_wartosci": "Esej nr 8. W komplecie.", "cena_min": 0, "cena_max": 0, "waluta": "PLN", "rekomendacja": "W komplecie."},
    "ARG/V/64": {"wartosc_hist": "★★", "opis_wartosci": "Tylna okładka z tabelami brytyjskimi. W komplecie.", "cena_min": 0, "cena_max": 0, "waluta": "PLN", "rekomendacja": "W komplecie."},
    "ARG/V/65": {
        "wartosc_hist": "★★★★★",
        "opis_wartosci": "ŚWIADECTWO MATURY POLSKIEGO ŻOŁNIERZA WE WŁOSZECH (7.I.1946). Dokument cywilizacyjny — matura w mundurze po Powstaniu i obozach. Świadectwa Gimnazjum 3DSK: 500-1500 PLN.",
        "cena_min": 800,
        "cena_max": 2000,
        "waluta": "PLN",
        "rekomendacja": "DESA lub kolekcjoner II Korpusu."
    },
    "ARG/V/66": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Legitymacja odznaki 3 DSK. Legitymacje odznak pułkowych: 200-600 PLN.",
        "cena_min": 200,
        "cena_max": 600,
        "waluta": "PLN",
        "rekomendacja": "W zestawie."
    },

    # === SERIA VI — VARIA ===
    "ARG/VI/1": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Fotografia tablicy pamiątkowej akcji 'Jeleń'. Fotografie tablic: 100-300 PLN.",
        "cena_min": 100,
        "cena_max": 300,
        "waluta": "PLN",
        "rekomendacja": "W zestawie."
    },
    "ARG/VI/2": {"wartosc_hist": "★★", "opis_wartosci": "Fotografia Krzyża Walecznych. 50-150 PLN.", "cena_min": 50, "cena_max": 150, "waluta": "PLN", "rekomendacja": "W zestawie."},
    "ARG/VI/3": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Galony i wstążki orderowe — oryginalne elementy mundurowe. Militaria drobne: 200-600 PLN.",
        "cena_min": 200,
        "cena_max": 600,
        "waluta": "PLN",
        "rekomendacja": "SDA Aukcja Militariów."
    },
    "ARG/VI/4": {
        "wartosc_hist": "★★★★",
        "opis_wartosci": "Album fotograficzny — okładka z dedykacją od żołnierzy dla Generała (8.III.1944). Albumy wojskowe z dedykacją: 1000-3000 PLN.",
        "cena_min": 1500,
        "cena_max": 3500,
        "waluta": "PLN",
        "rekomendacja": "DESA — sprzedawać jako komplet ARG/VI/4-6."
    },
    "ARG/VI/5": {"wartosc_hist": "★★★", "opis_wartosci": "Strona albumu z 4 zdjęciami. W komplecie albumu.", "cena_min": 0, "cena_max": 0, "waluta": "PLN", "rekomendacja": "Z ARG/VI/4."},
    "ARG/VI/6": {"wartosc_hist": "★★★", "opis_wartosci": "Strona albumu z 4 zdjęciami. W komplecie albumu.", "cena_min": 0, "cena_max": 0, "waluta": "PLN", "rekomendacja": "Z ARG/VI/4."},
    "ARG/VI/7": {
        "wartosc_hist": "★★★★",
        "opis_wartosci": "Dwie legitymacje pułkowe — stryj i bratanek. Dwa pokolenia w dwóch pułkach ułanów. Leg. pułkowe: 200-500 PLN za sztukę.",
        "cena_min": 500,
        "cena_max": 1200,
        "waluta": "PLN",
        "rekomendacja": "DESA lub SDA."
    },
    "ARG/VI/8": {"wartosc_hist": "★★", "opis_wartosci": "Zaproszenie na mszę rocznicową 7 P.Uł. Ephemera kombatancka: 50-150 PLN.", "cena_min": 50, "cena_max": 150, "waluta": "PLN", "rekomendacja": "W zestawie."},
    "ARG/VI/9": {"wartosc_hist": "★★", "opis_wartosci": "Nekrolog Jana Lorensa, Chicago 1960. Ephemera diasporowa: 50-150 PLN.", "cena_min": 50, "cena_max": 150, "waluta": "PLN", "rekomendacja": "W zestawie."},
    "ARG/VI/10": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "List do Ambasady Izraela ws. walut gettowych. Korespondencja dot. Holocaustu: 200-600 PLN.",
        "cena_min": 200,
        "cena_max": 600,
        "waluta": "PLN",
        "rekomendacja": "W zestawie z ARG/VI/11-12."
    },
    "ARG/VI/11": {
        "wartosc_hist": "★★★★★",
        "opis_wartosci": "PIENIĄDZE GETTA ŁÓDZKIEGO — bon 10 Pf. + talon mleczny. WDA-MiM (XII.2024): 10 Pf. Litzmannstadt rekord 17250 PLN. Średnia: ok. 3500-5000 PLN. Talon mleczny: 500-1500 PLN.",
        "cena_min": 4000,
        "cena_max": 10000,
        "waluta": "PLN",
        "rekomendacja": "WDA Wierzbicki lub DESA Unicum — aukcja numizmatyczna. Najwyższa wartość jednostkowa w kolekcji!"
    },
    "ARG/VI/12": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Odpowiedź Ambasady Izraela — sugestia Yad Vashem. Pismo dyplomatyczne: 200-500 PLN. Wartość kontekstualna z ARG/VI/10-11.",
        "cena_min": 200,
        "cena_max": 500,
        "waluta": "PLN",
        "rekomendacja": "W zestawie."
    },
    "ARG/VI/13": {"wartosc_hist": "★★", "opis_wartosci": "Trzy małe fotografie obozowe. 100-300 PLN.", "cena_min": 100, "cena_max": 300, "waluta": "PLN", "rekomendacja": "W zestawie."},

    # =========================================================================
    # SERIA V — KRZYSZTOF "JURAS" — NOWE DOKUMENTY (z PDF Kolekcja Juras)
    # =========================================================================

    # --- Korespondencja (aerogramy, listy) ---
    "ARG/V/67": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Aerogram Air Mail Letter Card do Głuchowskiego, CMF 3 DSK, Włochy. Stempel NZ. Aerogramy wojskowe II WŚ: 100-300 PLN na OneBid. Tu: adresowane do żołnierza polskiego w 3 DSK = proweniencja podnosi cenę.",
        "cena_min": 200,
        "cena_max": 500,
        "waluta": "PLN",
        "rekomendacja": "W zestawie z korespondencją Serii V."
    },
    "ARG/V/68": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "List ręczny po polsku z Bahia/Salvador, Brazylia. Korespondencja polonijna z Ameryki Południowej — rzadka na rynku. Listy emigrantów: 100-400 PLN. Kontekst emigracji powojennej: +50%.",
        "cena_min": 200,
        "cena_max": 500,
        "waluta": "PLN",
        "rekomendacja": "W zestawie."
    },

    # --- Dokumenty wojskowe i ewidencyjne ---
    "ARG/V/69": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Arkusz ewidencyjny Oficera Rezerwy — ręczne wpisy na papierze kancelaryjnym. Formularze ewidencji PSZ: 150-400 PLN. Wartość: uzupełnia ścieżkę służby.",
        "cena_min": 150,
        "cena_max": 400,
        "waluta": "PLN",
        "rekomendacja": "W zestawie z dokumentami wojskowymi."
    },
    "ARG/V/70": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Przepustka PASS, D-wo 3 DSK, 14.II.1946, bilingual PL/EN. Przepustki PSZ: 100-300 PLN na SDA. Dwujęzyczność i pieczęć 3 DSK podnoszą cenę.",
        "cena_min": 150,
        "cena_max": 400,
        "waluta": "PLN",
        "rekomendacja": "W zestawie."
    },

    # --- Świadectwa szkolne 3 DSK (Włochy + Anglia) ---
    "ARG/V/71": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Świadectwo Gimnazjum 3 DSK z pieczęcią kpt. Kapicy. Dokumenty edukacyjne II Korpusu: 200-600 PLN. Komplet z ARG/V/72-73.",
        "cena_min": 300,
        "cena_max": 700,
        "waluta": "PLN",
        "rekomendacja": "SPRZEDAWAĆ JAKO KOMPLET (ARG/V/71-73 + ARG/V/87-88) — pięć świadectw szkolnych z Włoch i Anglii."
    },
    "ARG/V/72": {"wartosc_hist": "★★★", "opis_wartosci": "Świadectwo Liceum str. 1 z ocenami (1946). W komplecie świadectw.", "cena_min": 0, "cena_max": 0, "waluta": "PLN", "rekomendacja": "W komplecie ARG/V/71-73."},
    "ARG/V/73": {"wartosc_hist": "★★★", "opis_wartosci": "Świadectwo Liceum verso z pieczęcią, Homeracle-Italia VI.1946. W komplecie.", "cena_min": 0, "cena_max": 0, "waluta": "PLN", "rekomendacja": "W komplecie."},

    # --- Obóz Lammie ---
    "ARG/V/74": {
        "wartosc_hist": "★★★★",
        "opis_wartosci": "Wiadomości Tygodniowe obozu Lammie — druk obozowy z programem kina Odeon, rewii, cyrku, komunikacją autobusową. Druki obozowe polskie z Wielkiej Brytanii (1946-48): BARDZO RZADKIE. Porównywalny: gazetki obozowe na Rara Avis: 300-800 PLN. Tu: kompletny program kulturalny obozu = wartość socjologiczna.",
        "cena_min": 400,
        "cena_max": 1000,
        "waluta": "PLN",
        "rekomendacja": "DESA lub Rara Avis — druki obozowe, ephemera wojenna. Sprzedawać z mapą ARG/V/75."
    },
    "ARG/V/75": {
        "wartosc_hist": "★★★★",
        "opis_wartosci": "Mapa obozu Lammie z pełną legendą: Synagoga, Plac Kościelny, Basen, Poczta Polowa, Kaplica Obozowa. Mapy/plany obozów polskich w UK: WYJĄTKOWO RZADKIE — w zasadzie niespotykane na rynku. Porównywalny: plany obozów jenieckich: 500-1500 PLN na SDA.",
        "cena_min": 500,
        "cena_max": 1500,
        "waluta": "PLN",
        "rekomendacja": "DESA lub SDA. W parze z ARG/V/74. Potencjalne zainteresowanie: badacze polskich obozów w Wlk. Brytanii."
    },

    # --- List wigilijny do matki (4 strony) ---
    "ARG/V/76": {
        "wartosc_hist": "★★★★★",
        "opis_wartosci": "List wigilijny 'Kochana moja Matenko!' — 24.XII.1946, 4 pełne strony. 20-letni żołnierz pisze do matki w Wigilię z obozu w Anglii. WARTOŚĆ EMOCJONALNA I NARRACYJNA NIEZWYKŁA. Porównywalny: listy żołnierzy II Korpusu: 200-500 PLN za stronę. Komplet 4 stron z datą wigilijną: PREMIUM. Porównywalny: list Powstańca do matki na DESA #198 = 2000-4000 PLN.",
        "cena_min": 1000,
        "cena_max": 3000,
        "waluta": "PLN",
        "rekomendacja": "DESA Unicum lub Muzeum Emigracji w Gdyni. Sprzedawać jako komplet 4 stron (ARG/V/76-79). Narracja: 'Wigilia żołnierza bez ojczyzny'."
    },
    "ARG/V/77": {"wartosc_hist": "★★★★", "opis_wartosci": "List wigilijny str. 2. W komplecie.", "cena_min": 0, "cena_max": 0, "waluta": "PLN", "rekomendacja": "W komplecie ARG/V/76-79."},
    "ARG/V/78": {"wartosc_hist": "★★★★", "opis_wartosci": "List wigilijny str. 3 — wspomnienia z 1945. W komplecie.", "cena_min": 0, "cena_max": 0, "waluta": "PLN", "rekomendacja": "W komplecie."},
    "ARG/V/79": {"wartosc_hist": "★★★★", "opis_wartosci": "List wigilijny str. 4 — sytuacja emigrantów. W komplecie.", "cena_min": 0, "cena_max": 0, "waluta": "PLN", "rekomendacja": "W komplecie."},

    # --- Szkoła i rysunki ---
    "ARG/V/80": {
        "wartosc_hist": "★★",
        "opis_wartosci": "Rysunek techniczny — zadanie szkolne z geometrii. Ephemera szkolna: 50-150 PLN. Wartość kontekstualna: żołnierz-uczeń.",
        "cena_min": 50,
        "cena_max": 150,
        "waluta": "PLN",
        "rekomendacja": "W zestawie ze świadectwami."
    },

    # --- Przepustki brytyjskie ---
    "ARG/V/81": {
        "wartosc_hist": "★★★★",
        "opis_wartosci": "Przepustka Army Form B.295 z PIECZĘCIĄ 7 PUŁKU UŁANÓW LUBELSKICH. Pieczęć pułkowa na formularzu brytyjskim = hybryd dwóch tradycji wojskowych. Przepustki PSZ z pieczęciami pułkowymi: 200-500 PLN, ale tu: pieczęć LEGENDARNE PUŁKU 7 P.Uł. = premium.",
        "cena_min": 300,
        "cena_max": 800,
        "waluta": "PLN",
        "rekomendacja": "SDA lub DESA — kolekcjonerzy 7 P.Uł."
    },
    "ARG/V/82": {"wartosc_hist": "★", "opis_wartosci": "Instrukcja medyczna ATS — standardowy druk brytyjski. Wartość minimalna: 30-80 PLN.", "cena_min": 30, "cena_max": 80, "waluta": "PLN", "rekomendacja": "Tylko w zestawie."},

    # --- Kartki świąteczne ---
    "ARG/V/83": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Kartka świąteczna bilingual PL/EN z adresem Bodney Airfield, Thetford, Norfolk. Kartki świąteczne polskich obozów: 80-250 PLN. Tu: adres obozu + dwujęzyczność.",
        "cena_min": 100,
        "cena_max": 300,
        "waluta": "PLN",
        "rekomendacja": "W zestawie. Sprzedawać z ARG/V/84 jako parę."
    },
    "ARG/V/84": {"wartosc_hist": "★★", "opis_wartosci": "Verso kartki z ornamentem choinkowym. W parze z ARG/V/83.", "cena_min": 0, "cena_max": 0, "waluta": "PLN", "rekomendacja": "Z ARG/V/83."},

    # --- Notatki i wizytówki ---
    "ARG/V/85": {"wartosc_hist": "★", "opis_wartosci": "Notatka z obliczeniami finansowymi. Minimalna wartość: 30-80 PLN.", "cena_min": 30, "cena_max": 80, "waluta": "PLN", "rekomendacja": "Tylko w zestawie."},
    "ARG/V/86": {
        "wartosc_hist": "★★",
        "opis_wartosci": "Wizytówka 'H. London POLACCO' — Bari, Włochy. Wizytówki polonijne: 50-150 PLN. Ciekawostka: 'Polacco' = Polak po włosku, adres teatralny w Bari.",
        "cena_min": 50,
        "cena_max": 200,
        "waluta": "PLN",
        "rekomendacja": "W zestawie."
    },

    # --- Drugie świadectwa szkolne (Bodney, Norfolk) ---
    "ARG/V/87": {
        "wartosc_hist": "★★★★",
        "opis_wartosci": "Świadectwo I Polskiego Liceum im. 3 DSK w Bodney, Norfolk — klasa 3a/37, rok 1944 Warszawa. DOKUMENT EDUKACJI NA WYGNANIU. Polskie szkoły w UK: wyjątkowo rzadkie na rynku. Porównywalny: świadectwa 3 DSK na aukcjach: 300-800 PLN.",
        "cena_min": 300,
        "cena_max": 800,
        "waluta": "PLN",
        "rekomendacja": "W komplecie świadectw (ARG/V/71-73 + V/87-88)."
    },
    "ARG/V/88": {"wartosc_hist": "★★★", "opis_wartosci": "Verso świadectwa Bodney z pieczęcią, 30.VI.1946. W komplecie.", "cena_min": 0, "cena_max": 0, "waluta": "PLN", "rekomendacja": "W komplecie."},

    # --- Przepustka szkolna BOSK ---
    "ARG/V/89": {
        "wartosc_hist": "★★",
        "opis_wartosci": "Przepustka Polish School Master, Gimnazjum i Liceum BOSK, nr 3024427. Dokumenty BOSK (Baza Organizacyjna Szkolnictwa Konspiracyjnego?): 100-300 PLN.",
        "cena_min": 100,
        "cena_max": 300,
        "waluta": "PLN",
        "rekomendacja": "W zestawie ze świadectwami."
    },

    # --- PKPR (Polski Korpus Przysposobienia i Rozmieszczenia) ---
    "ARG/V/90": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Druk informacyjny PKPR — stawki, warunki, organizacja. Druki PKPR: 100-400 PLN. Wartość dokumentacyjna: wyjaśnia strukturę demobilizacji polskich żołnierzy w UK.",
        "cena_min": 150,
        "cena_max": 400,
        "waluta": "PLN",
        "rekomendacja": "W zestawie z certyfikatami PKPR."
    },
    "ARG/V/91": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Odpis umowy służby nr 3004271 — pełne dane osobowe, data wcielenia 4.VI.1945. Odpisy umów PSZ: 150-400 PLN.",
        "cena_min": 150,
        "cena_max": 400,
        "waluta": "PLN",
        "rekomendacja": "W zestawie."
    },

    # --- Rozkazy i pisma urzędowe ---
    "ARG/V/92": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Wyciąg z rozkazu likwidacyjnego — Orsay/Courtine, 25.XI.1946. Ewidencja zamknięcia obozu repatriacyjnego. Dokumenty likwidacyjne: 150-400 PLN.",
        "cena_min": 150,
        "cena_max": 400,
        "waluta": "PLN",
        "rekomendacja": "W zestawie."
    },
    "ARG/V/93": {
        "wartosc_hist": "★★★★",
        "opis_wartosci": "Pismo Polskiej Wojskowej Misji Likwidacyjnej we Francji, Paryż 22.XI.1946, do Gen. Fereckiego, Sztab Ósmy, Londyn. Dokumenty Misji Likwidacyjnej: RZADKIE — likwidacja polskich obozów we Francji to słabo udokumentowany epizod. Pisma urzędowe Misji: 300-800 PLN.",
        "cena_min": 400,
        "cena_max": 1000,
        "waluta": "PLN",
        "rekomendacja": "DESA lub Rara Avis. Zainteresowanie: badacze polskiej diaspory 1945-48."
    },

    # --- Kwestionariusze osobiste (POUFNE) ---
    "ARG/V/94": {
        "wartosc_hist": "★★★★",
        "opis_wartosci": "Kwestionariusz Osobisty z klauzulą POUFNE — formularz z danymi osobowymi, stopień, formacja, cel: 'Polish Records'. Kwestionariusze personalne: 200-500 PLN. Tu: klauzula POUFNE + kompletne dane = premium. Komplet 2 stron (ARG/V/94-95).",
        "cena_min": 300,
        "cena_max": 700,
        "waluta": "PLN",
        "rekomendacja": "W zestawie z dokumentami PKPR."
    },
    "ARG/V/95": {"wartosc_hist": "★★★", "opis_wartosci": "Kwestionariusz str. 2 — RODZINA, plany na przyszłość. W komplecie z ARG/V/94.", "cena_min": 0, "cena_max": 0, "waluta": "PLN", "rekomendacja": "Z ARG/V/94."},

    # --- Zaświadczenie Komisji Weryfikacyjnej AK ---
    "ARG/V/96": {
        "wartosc_hist": "★★★★★",
        "opis_wartosci": "Zaświadczenie Komisji Weryfikacyjnej AK — potwierdzenie PRZEJŚCIA KANAŁAMI z Powstania Warszawskiego! DOKUMENT KLUCZOWY: potwierdza udział w Obronie Starego Miasta i ewakuację kanałami (jedną z najtragiczniejszych kart Powstania). Zaświadczenia AK: 800-2500 PLN. Tu: kontekst przejścia kanałami = wartość źródłowa dla historyków. Porównywalny: zaświadczenie płk. Ziemskiego ARG/V/43 = 3000-7000 PLN.",
        "cena_min": 2000,
        "cena_max": 5000,
        "waluta": "PLN",
        "rekomendacja": "DESA Unicum lub Muzeum Powstania Warszawskiego — TOP LOT z nowych dokumentów. Narracja: 'Przejście kanałami potwierdzone dokumentalnie'."
    },

    # --- Rozkazy i pisma pułkowe ---
    "ARG/V/97": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Rozkaz personalny 7 Pułku Ułanów — tabela, D-ca taboru, 1946. Rozkazy pułkowe: 200-500 PLN.",
        "cena_min": 200,
        "cena_max": 500,
        "waluta": "PLN",
        "rekomendacja": "W zestawie."
    },
    "ARG/V/98": {
        "wartosc_hist": "★★",
        "opis_wartosci": "Pismo Sztabu Głównego, Bodney Airfield, Thetford. Pisma administracyjne PSZ: 100-300 PLN.",
        "cena_min": 100,
        "cena_max": 300,
        "waluta": "PLN",
        "rekomendacja": "W zestawie."
    },
    "ARG/V/99": {"wartosc_hist": "★", "opis_wartosci": "Notatki odręczne — adresy, terminy. Minimalna wartość: 30-80 PLN.", "cena_min": 30, "cena_max": 80, "waluta": "PLN", "rekomendacja": "Tylko w zestawie."},

    # --- Zaświadczenie PSZ ---
    "ARG/V/100": {
        "wartosc_hist": "★★★★",
        "opis_wartosci": "Zaświadczenie PSZ nr 87949 o zakończeniu służby — Krzysztof Głuchowski, stopień L/Cpl (st. ułan), Londyn. Zaświadczenia PSZ o zakończeniu służby: 300-800 PLN. Tu: kompletne dane + proweniencja rodziny generalskiej.",
        "cena_min": 400,
        "cena_max": 1000,
        "waluta": "PLN",
        "rekomendacja": "DESA lub SDA — w zestawie z Discharge Certificate."
    },

    # --- ŚWIADECTWO DOJRZAŁOŚCI ZE ZDJĘCIEM ---
    "ARG/V/101": {
        "wartosc_hist": "★★★★★",
        "opis_wartosci": "ŚWIADECTWO DOJRZAŁOŚCI ZE ZDJĘCIEM Krzysztofa w mundurze! Ministerstwo WRiOP, Komisja Egzaminacyjna, ur. 1926 Warszawa. DOKUMENT WYJĄTKOWY: matura zdana na emigracji ('Dobrze'), ze zdjęciem żołnierza-ucznia. Świadectwa dojrzałości z II WŚ: 500-1500 PLN. Tu: ZE ZDJĘCIEM w mundurze + kontekst AK/Powstanie/3 DSK = PREMIUM. Porównywalny: DESA Unicum — matura żołnierza II Korpusu: 1500-3000 PLN.",
        "cena_min": 2000,
        "cena_max": 5000,
        "waluta": "PLN",
        "rekomendacja": "DESA Unicum — top lot. Narracja: '18-latek, który zdał maturę w okopach'. Komplet z ARG/V/102."
    },
    "ARG/V/102": {"wartosc_hist": "★★★★", "opis_wartosci": "Verso Świadectwa Dojrzałości z podpisami komisji. W komplecie z ARG/V/101.", "cena_min": 0, "cena_max": 0, "waluta": "PLN", "rekomendacja": "W komplecie."},

    # --- DISCHARGE CERTIFICATE ---
    "ARG/V/103": {
        "wartosc_hist": "★★★★★",
        "opis_wartosci": "DISCHARGE CERTIFICATE — PSZ/PKPR, Army No. 3004271, Witley Camp, 31.X.1948. Pieczęć RECORD OFFICE, POLISH RESETTLEMENT CORPS. DOKUMENT KOŃCOWY — formalne zakończenie służby w PSZ. Discharge Certificates polskich żołnierzy z PKPR: 400-1200 PLN na OneBid/eBay. Tu: kompletny z pieczęcią pułkową, czytelny, dobry stan. Porównywalny: British Army discharge certificates (eBay): £50-200 = 250-1000 PLN.",
        "cena_min": 600,
        "cena_max": 1500,
        "waluta": "PLN",
        "rekomendacja": "DESA lub SDA. W zestawie z Soldier's Service Book."
    },

    # --- SOLDIER'S SERVICE BOOK (komplet 6 zdjęć) ---
    "ARG/V/104": {
        "wartosc_hist": "★★★★★",
        "opis_wartosci": "SOLDIER'S SERVICE AND PAY BOOK (Army Book 64) — KOMPLET 6 fotografii dokumentujących książeczkę: Short Form of Will, okładka, dane osobowe z pieczęcią DISCHARGED, Medical Classification, szczepienia, okładka zewnętrzna. KLUCZOWY ARTEFAKT: pełna książeczka żołnierska polskiego żołnierza w siłach brytyjskich. OneBid: Soldier's Service Book polskiego żołnierza = 1000-3000 PLN. eBay: British AB.64 = £100-400 = 500-2000 PLN. Tu: KOMPLETNA z pieczęcią DISCHARGED, czytelne dane, proweniencja AK/Powstanie.",
        "cena_min": 1500,
        "cena_max": 4000,
        "waluta": "PLN",
        "rekomendacja": "DESA Unicum lub SDA Militaria — top lot. SPRZEDAWAĆ JAKO KOMPLET (ARG/V/104-109). Razem z Discharge Certificate ARG/V/103 = zestaw demobilizacyjny."
    },
    "ARG/V/105": {"wartosc_hist": "★★★★", "opis_wartosci": "SSB okładka wewnętrzna + strona tytułowa. W komplecie.", "cena_min": 0, "cena_max": 0, "waluta": "PLN", "rekomendacja": "W komplecie ARG/V/104-109."},
    "ARG/V/106": {"wartosc_hist": "★★★★★", "opis_wartosci": "SSB dane osobowe: Army Number 4481G119261II, GŁUCHOWSKI KRZYSZTOF, DOB 29.11.1926, pieczęć DISCHARGED. NAJWAŻNIEJSZA STRONA książeczki.", "cena_min": 0, "cena_max": 0, "waluta": "PLN", "rekomendacja": "W komplecie."},
    "ARG/V/107": {"wartosc_hist": "★★★", "opis_wartosci": "SSB Medical Classification, szczepienia TAB, 1945. W komplecie.", "cena_min": 0, "cena_max": 0, "waluta": "PLN", "rekomendacja": "W komplecie."},
    "ARG/V/108": {"wartosc_hist": "★★★", "opis_wartosci": "SSB okładka zewnętrzna 'ARMY BOOK 64'. Ikoniczny obiekt. W komplecie.", "cena_min": 0, "cena_max": 0, "waluta": "PLN", "rekomendacja": "W komplecie."},

    # --- Campaign Stars ---
    "ARG/V/109": {
        "wartosc_hist": "★★★★",
        "opis_wartosci": "Karta odznaczeń Campaign Stars and Medals 1939-45 — tabela z 10 odznaczeniami, zaznaczone: 0-1-0. Dokumenty potwierdzające odznaczenia: 200-500 PLN. W zestawie z pismem War Office ARG/V/110.",
        "cena_min": 200,
        "cena_max": 600,
        "waluta": "PLN",
        "rekomendacja": "W zestawie z ARG/V/110."
    },
    "ARG/V/110": {
        "wartosc_hist": "★★★★",
        "opis_wartosci": "Pismo Under-Secretary of State for War — transmisja odznaczeń, z herbem królewskim. Pisma War Office z Royal Arms: 200-500 PLN. Wartość ikonograficzna herbu.",
        "cena_min": 200,
        "cena_max": 600,
        "waluta": "PLN",
        "rekomendacja": "W zestawie z ARG/V/109."
    },

    # --- Notatki ewidencyjne ---
    "ARG/V/111": {"wartosc_hist": "★★", "opis_wartosci": "Notatki — ewidencja odznaczeń 3 DSK, Medal Wojska. 50-150 PLN.", "cena_min": 50, "cena_max": 150, "waluta": "PLN", "rekomendacja": "W zestawie."},
    "ARG/V/112": {"wartosc_hist": "★★", "opis_wartosci": "Notatki weryfikacyjne AK — numery rozkazów, kompanie. 80-200 PLN.", "cena_min": 80, "cena_max": 200, "waluta": "PLN", "rekomendacja": "W zestawie."},
    "ARG/V/113": {"wartosc_hist": "★★", "opis_wartosci": "Notatki z numerami rozkazów, Medal Wojska, Odznaka 3 DSK. 50-150 PLN.", "cena_min": 50, "cena_max": 150, "waluta": "PLN", "rekomendacja": "W zestawie."},

    # --- Wyposażenie i testament ---
    "ARG/V/114": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Wykaz wyposażenia osobistego — formularz wojskowy z pełnym wykazem umundurowania i wyposażenia. Formularze wyposażenia: 150-400 PLN. Komplet z ARG/V/115.",
        "cena_min": 150,
        "cena_max": 400,
        "waluta": "PLN",
        "rekomendacja": "W zestawie."
    },
    "ARG/V/115": {"wartosc_hist": "★★", "opis_wartosci": "Wykaz wyposażenia str. 2 — Oporządzenie, Uzbrojenie, podpis dowódcy. W komplecie z ARG/V/114.", "cena_min": 0, "cena_max": 0, "waluta": "PLN", "rekomendacja": "Z ARG/V/114."},
    "ARG/V/116": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Formularz testamentu własnoręcznego — druk wojskowy wg Prawa Polskiego. Niewypełniony, ale sam druk jest świadectwem: 20-letni żołnierz dostaje formularz testamentowy. Formularze testamentów: 80-250 PLN. Komplet z ARG/V/117.",
        "cena_min": 100,
        "cena_max": 300,
        "waluta": "PLN",
        "rekomendacja": "W zestawie."
    },
    "ARG/V/117": {"wartosc_hist": "★★", "opis_wartosci": "Formularz testamentu verso. W komplecie z ARG/V/116.", "cena_min": 0, "cena_max": 0, "waluta": "PLN", "rekomendacja": "Z ARG/V/116."},

    # === LEGITYMACJE KRZYŻA AK I ODZNAKI PAMIĄTKOWEJ AK ===
    "ARG/V/118": {
        "wartosc_hist": "★★★★★",
        "opis_wartosci": "LEGITYMACJA KRZYŻA ARMII KRAJOWEJ nr 3316 — wnętrze z pełnymi danymi: Głuchowski Krzysztof, ps. 'Juras', ZWZ Komp.V Plut.III/2, 7 Pułk Ułan.Lubel. 'Jeleń'. Odznaczony 1.VIII.1966 przez dowódcę AK gen. Bora-Komorowskiego. Podpis K. Ziemski 'Wachnowski'. Londyn 7.3.68. DOKUMENT TOP-KLASY: legitymacja Krzyża AK na DESA Unicum #202 (2023): 3000-8000 PLN. SDA Militaria (2022): 2500-5000 PLN. Tu: z podpisem Ziemskiego (D-ca Grupy Północ Powstania!) + odwołanie do Bora-Komorowskiego = UNIKAT.",
        "cena_min": 4000,
        "cena_max": 10000,
        "waluta": "PLN",
        "rekomendacja": "DESA Unicum — TOP LOT. Sprzedawać jako komplet (ARG/V/118-122) — legitymacja + okładka + odznaka pamiątkowa AK. Alternatywa: Muzeum Powstania Warszawskiego (zakup lub depozyt)."
    },
    "ARG/V/119": {"wartosc_hist": "★★★★", "opis_wartosci": "Okładka Legitymacji Krzyża AK z symbolem AK, nr 3316. W komplecie.", "cena_min": 0, "cena_max": 0, "waluta": "PLN", "rekomendacja": "W komplecie ARG/V/118-122."},
    "ARG/V/120": {"wartosc_hist": "★★★★", "opis_wartosci": "Duplikat/wariant legitymacji Krzyża AK — inna kopia tego samego dokumentu. W komplecie.", "cena_min": 0, "cena_max": 0, "waluta": "PLN", "rekomendacja": "W komplecie."},
    "ARG/V/121": {
        "wartosc_hist": "★★★★",
        "opis_wartosci": "Legitymacja Odznaki Pamiątkowej AK — okładka z symbolem Polska Walcząca. Legitymacje Odznaki AK: 1000-3000 PLN na SDA/DESA. W komplecie z ARG/V/118.",
        "cena_min": 0,
        "cena_max": 0,
        "waluta": "PLN",
        "rekomendacja": "W komplecie ARG/V/118-122."
    },
    "ARG/V/122": {
        "wartosc_hist": "★★★★",
        "opis_wartosci": "Legitymacja Odznaki Pamiątkowej AK — wnętrze: Starszy Ułan, Głuchowski Krzysztof, ps. JURAS, nr 4042. Komisja Weryfikacyjna 2 Korpusu AK, 12 czerwca 46. W komplecie.",
        "cena_min": 0,
        "cena_max": 0,
        "waluta": "PLN",
        "rekomendacja": "W komplecie ARG/V/118-122."
    },

    # === CERTYFIKATY PKPR ===
    "ARG/V/123": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Certificate P.R.C. Record Office, Witley Camp, 19.II.1948 — potwierdzenie enlistment do PKPR. Certyfikaty PKPR: 150-400 PLN za sztukę. Tu: 5 kopii/wariantów (ARG/V/123-127) — sprzedawać jedną, reszta jako duplikaty. OneBid: certyfikaty PKPR = 120-350 PLN.",
        "cena_min": 200,
        "cena_max": 500,
        "waluta": "PLN",
        "rekomendacja": "Sprzedać jeden egzemplarz, reszta w archiwum lub w zestawie."
    },
    "ARG/V/124": {"wartosc_hist": "★★", "opis_wartosci": "Duplikat certyfikatu PKPR (19.II.1948). Wliczony.", "cena_min": 0, "cena_max": 0, "waluta": "PLN", "rekomendacja": "Z ARG/V/123."},
    "ARG/V/125": {"wartosc_hist": "★★★", "opis_wartosci": "Certificate P.R.C. nr 3023271, 3.III.1948 — inny numer referencyjny, inny format. Wariant: 100-300 PLN.", "cena_min": 100, "cena_max": 300, "waluta": "PLN", "rekomendacja": "W zestawie."},
    "ARG/V/126": {"wartosc_hist": "★★", "opis_wartosci": "Kolejna kopia certyfikatu. Wliczony.", "cena_min": 0, "cena_max": 0, "waluta": "PLN", "rekomendacja": "Z ARG/V/123."},
    "ARG/V/127": {"wartosc_hist": "★★", "opis_wartosci": "Kopia certyfikatu z pieczęcią. Wliczony.", "cena_min": 0, "cena_max": 0, "waluta": "PLN", "rekomendacja": "Z ARG/V/123."},

    # --- Przepustka z pieczęcią pułkową ---
    "ARG/V/128": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Przepustka Army Form B.295 z pieczęcią PUŁK UŁANÓW LUBELSKICH (duplikat ARG/V/81). Pieczęcie pułkowe: 200-500 PLN. Osobna przepustka, inna data.",
        "cena_min": 200,
        "cena_max": 500,
        "waluta": "PLN",
        "rekomendacja": "W zestawie lub sprzedać osobno jako przepustkę z pieczęcią."
    },
    "ARG/V/129": {"wartosc_hist": "★", "opis_wartosci": "Instrukcja medyczna ATS — verso przepustki. 30-80 PLN.", "cena_min": 30, "cena_max": 80, "waluta": "PLN", "rekomendacja": "Tylko w zestawie."},

    # === ALIEN'S IDENTITY CERTIFICATE ===
    "ARG/V/130": {
        "wartosc_hist": "★★★★",
        "opis_wartosci": "ALIEN'S IDENTITY CERTIFICATE — dokument tożsamości imigranta. South West Essex Technical College, Student, Entry Gravesend, 31.X.1947. DOKUMENT HISTORII EMIGRACJI: polski żołnierz staje się 'alienem' w Wielkiej Brytanii. Alien's certificates: 200-600 PLN na eBay/OneBid. Tu: kontekst żołnierza AK → studenta = wartość narracyjna. Komplet z ARG/V/131.",
        "cena_min": 300,
        "cena_max": 800,
        "waluta": "PLN",
        "rekomendacja": "DESA lub Muzeum Emigracji Gdynia. Sprzedawać z biletem uczelni (ARG/V/138-139)."
    },
    "ARG/V/131": {"wartosc_hist": "★★★", "opis_wartosci": "Verso Alien's Identity — adres High Wycombe, pieczęcie Alien Registration. W komplecie z ARG/V/130.", "cena_min": 0, "cena_max": 0, "waluta": "PLN", "rekomendacja": "Z ARG/V/130."},

    # --- Biogram ---
    "ARG/V/132": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Biogram Krzysztofa Głuchowskiego — druk biograficzny z pełnym życiorysem: AK, Powstanie, 3 DSK, emigracja, Brazylia, inżynier. Odznaczenia wymienione. Biogramy kombatantów: 100-300 PLN. Wartość referencyjna dla reszty kolekcji.",
        "cena_min": 100,
        "cena_max": 300,
        "waluta": "PLN",
        "rekomendacja": "W zestawie — materiał kontekstowy dla kupującego."
    },

    # === DOKUMENT WAR OFFICE / MI5 (CONFIDENTIAL) ===
    "ARG/V/133": {
        "wartosc_hist": "★★★★★",
        "opis_wartosci": "DOKUMENT WAR OFFICE / MI5 — CONFIDENTIAL. Pełna weryfikacja bezpieczeństwa Głuchowskiego: born Grzegorzów Nov 1926, parents Stefan and Helena, marital status Single, 'Politically Well-Minded', 'Not convicted', conduct 'Very Good'. DOKUMENT WYJĄTKOWY: weryfikacje MI5 polskich żołnierzy prawie nigdy nie trafiają na rynek — podlegały klasyfikacji. Porównywalny: dokumenty MI5 z okresu WWII na Christie's/Bonhams = £500-2000. Na polskim rynku: BRAK PORÓWNYWALNYCH. Szacunek ostrożny na podstawie dokumentów British Intelligence ogólnie.",
        "cena_min": 1500,
        "cena_max": 4000,
        "waluta": "PLN",
        "rekomendacja": "DESA Unicum TOP LOT lub sprzedaż międzynarodowa (Bonhams, Spink). Zainteresowanie: kolekcjonerzy dokumentów wywiadowczych, historycy Zimnej Wojny."
    },

    # --- Fotografia naszywki ---
    "ARG/V/134": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Fotografia naszywki pułkowej 7 Pułku Ułanów Lubelskich — biała sylwetka jelenia na ciemnym tle. UWAGA: to jest fotografia dokumentacyjna, nie oryginalna naszywka. Fotografie militariów: 80-250 PLN. Wartość ikonograficzna symbolu pułkowego.",
        "cena_min": 100,
        "cena_max": 300,
        "waluta": "PLN",
        "rekomendacja": "W zestawie."
    },

    # --- Ephemera i kartki okolicznościowe ---
    "ARG/V/135": {"wartosc_hist": "★★", "opis_wartosci": "Kartka od SPP z życzeniami, podpisy wielu osób. Ephemera polonijna: 80-250 PLN.", "cena_min": 80, "cena_max": 250, "waluta": "PLN", "rekomendacja": "W zestawie."},
    "ARG/V/136": {
        "wartosc_hist": "★★★★",
        "opis_wartosci": "Kartka artystyczna — linoryt 'Fundusz Praskiej Armii Krajowej', 1944. SZTUKA POWSTAŃCZA: linoryty/drzeworyty z okresu Powstania: 500-2000 PLN na DESA. Tu: związek z AK Praga.",
        "cena_min": 500,
        "cena_max": 1500,
        "waluta": "PLN",
        "rekomendacja": "DESA Unicum — aukcja sztuki i historii."
    },

    # --- Wycinek z Palmirów ---
    "ARG/V/137": {
        "wartosc_hist": "★★★★",
        "opis_wartosci": "Wycinek prasowy z fotografią tablicy z Palmirów: 'ŁATWIEJ JEST MÓWIĆ O POLSCE NIE KAŻDY DOKONA TAK SZCZEREGO AKTU CIERPIENIA... UMRZEĆ ZA TRUDNOŚĆ CIERPIEĆ'. Wycinki z miejscami pamięci: 100-300 PLN. Wartość symboliczna i ikonograficzna — Palmiry = miejsce masowych egzekucji.",
        "cena_min": 150,
        "cena_max": 400,
        "waluta": "PLN",
        "rekomendacja": "W zestawie."
    },

    # --- Bilet uczelniany ---
    "ARG/V/138": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Bilet członkowski South West Essex Technical College, sesja 1947-48, nr 1149, Fee Paid 5/-. Dokumenty edukacji polskich żołnierzy w UK: 100-300 PLN. Kontekst: od AK do szkoły technicznej w Londynie. Komplet z ARG/V/139.",
        "cena_min": 100,
        "cena_max": 300,
        "waluta": "PLN",
        "rekomendacja": "W zestawie z Alien's Identity Certificate (ARG/V/130-131)."
    },
    "ARG/V/139": {"wartosc_hist": "★★", "opis_wartosci": "Verso biletu — 'This ticket is not transferable', podpis. W parze z ARG/V/138.", "cena_min": 0, "cena_max": 0, "waluta": "PLN", "rekomendacja": "Z ARG/V/138."},

    # --- Rysunek ---
    "ARG/V/140": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Rysunek odręczny — szkic architektoniczny kościoła z wieżą, ołówek/tusz. Rysunki żołnierzy: 100-400 PLN. Porównywalny: rysunki jenieckie na SDA: 200-600 PLN. Tu: prawdopodobnie praca szkolna z kursu technicznego.",
        "cena_min": 150,
        "cena_max": 400,
        "waluta": "PLN",
        "rekomendacja": "W zestawie ze świadectwami."
    },

    # --- Prasa emigracyjna ---
    "ARG/V/141": {"wartosc_hist": "★★", "opis_wartosci": "Wycinek 'Życie Tygodnia' — korespondencja czytelników, CMP 53. Wycinki: 30-100 PLN.", "cena_min": 30, "cena_max": 100, "waluta": "PLN", "rekomendacja": "W zestawie."},
    "ARG/V/142": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Okładka 'Życie Tygodnia' — 'Ameryka walczy z 5-tą kolumną'. Okładki prasowe emigracyjne: 100-400 PLN. Kompletne numery gazet emigracyjnych: RZADKIE. Porównywalny: 'Orzeł Biały' kompletny numer na Rara Avis = 200-600 PLN.",
        "cena_min": 150,
        "cena_max": 400,
        "waluta": "PLN",
        "rekomendacja": "Rara Avis lub kolekcjoner prasy polonijnej. Sprzedawać jako komplet gazet (ARG/V/142-143 + 145-147)."
    },
    "ARG/V/143": {"wartosc_hist": "★★", "opis_wartosci": "Wycinek 'Smutna, ale pouczająca sprawa' — Klaudiusz Hrabyk. 50-150 PLN.", "cena_min": 50, "cena_max": 150, "waluta": "PLN", "rekomendacja": "W zestawie z prasą."},

    # --- Zaświadczenie Ziemskiego ---
    "ARG/V/144": {
        "wartosc_hist": "★★★★★",
        "opis_wartosci": "ZAŚWIADCZENIE ZIEMSKIEGO KAROLA — Dowódca Polskiego Okręgu III Wileńskiego. Pieczęć: Żołnierzy Polskich Okręgu III. Zaświadcza waleczność i odznaczenia. UWAGA: Ziemski Karol 'Wachnowski' był D-cą Grupy 'Północ' w Powstaniu Warszawskim — jeden z najważniejszych dowódców! Jego podpis na zaświadczeniu z pieczęcią Okręgu III = DOKUMENT MUZEALNY. Porównywalny: ARG/V/43 (podobne zaświadczenie Ziemskiego) wycenione na 3000-7000 PLN.",
        "cena_min": 2000,
        "cena_max": 5000,
        "waluta": "PLN",
        "rekomendacja": "DESA Unicum lub Muzeum Powstania Warszawskiego. TOP LOT — podpis jednego z najważniejszych dowódców Powstania."
    },

    # --- Gazety emigracyjne ---
    "ARG/V/145": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Gazeta 'Życie' Rok I Nr 11, 14 kwietnia 1946 — pełna strona frontowa: 'Referendum w czerwcu', 'Sprawa Gen. Michajłowicza'. Kompletne numery gazet emigracyjnych z 1946: 200-600 PLN.",
        "cena_min": 200,
        "cena_max": 500,
        "waluta": "PLN",
        "rekomendacja": "Rara Avis. Sprzedawać jako komplet gazet."
    },
    "ARG/V/146": {"wartosc_hist": "★★", "opis_wartosci": "Strona kulturalna: Film, Teatr, Muzyka. Maurice Chevalier, Greer Garson. 50-150 PLN.", "cena_min": 50, "cena_max": 150, "waluta": "PLN", "rekomendacja": "W zestawie."},
    "ARG/V/147": {"wartosc_hist": "★★", "opis_wartosci": "Strona ogłoszeniowa — kursy językowe, szkoły, 'Veritas'. Wartość socjologiczna: obraz polskiej diaspory w UK. 50-150 PLN.", "cena_min": 50, "cena_max": 150, "waluta": "PLN", "rekomendacja": "W zestawie."},

    # === AEROGRAM DO BORA-KOMOROWSKIEGO ===
    "ARG/V/148": {
        "wartosc_hist": "★★★★★",
        "opis_wartosci": "AEROGRAM DO GEN. BORA-KOMOROWSKIEGO — HQ Polish Forces, IRELAND. Korespondencja z legendarnym dowódcą Powstania Warszawskiego! Listy DO Bora na rynku: WYJĄTKOWO RZADKIE. Porównywalny: korespondencja od/do generałów PSZ: 1000-5000 PLN. Tu: Głuchowski pisze do człowieka, który dowodził walkami, w których sam brał udział. Kontekst osobisty = PREMIUM. Komplet z ARG/V/149.",
        "cena_min": 2000,
        "cena_max": 6000,
        "waluta": "PLN",
        "rekomendacja": "DESA Unicum TOP LOT. Alternatywa: Muzeum Powstania Warszawskiego. Narracja: 'Żołnierz pisze do swojego dowódcy — 20 lat po Powstaniu'."
    },
    "ARG/V/149": {"wartosc_hist": "★★★★", "opis_wartosci": "Treść aerogramu — list nr 563, historia Pułku 1112, Polish Institute. Kluczowa treść historyczna. W komplecie z ARG/V/148.", "cena_min": 0, "cena_max": 0, "waluta": "PLN", "rekomendacja": "W komplecie."},

    # --- Polish Institute ---
    "ARG/V/150": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Pismo z Polish Institute and Sikorski Museum — potwierdzenie otrzymania dokumentów. Korespondencja z Instytutem Sikorskiego: 100-300 PLN. Proweniencja instytucjonalna.",
        "cena_min": 100,
        "cena_max": 300,
        "waluta": "PLN",
        "rekomendacja": "W zestawie."
    },

    # === WSPOMNIENIA RĘKOPIŚMIENNE (6 stron) ===
    "ARG/V/151": {
        "wartosc_hist": "★★★★★",
        "opis_wartosci": "WSPOMNIENIA RĘKOPIŚMIENNE — 6 pełnych stron gęstego rękopisu. Tematyka: stosunki polsko-żydowskie, przedwojenny Kraków (1918), emigracja do Brazylii (Bahia/Salvador 1949-50), warunki pracy emigrantów (3500 robotników), alianci, organizacje polonijne. DOKUMENT ŹRÓDŁOWY PIERWSZORZĘDNY: naoczny świadek opisuje 30 lat historii — od niepodległości przez Powstanie po emigrację. Rękopisy wspomnieniowe żołnierzy AK: na DESA = 2000-8000 PLN (jako komplet). Porównywalny: pamiętnik obozowy ARG/V/23-33 wyceniony na 3000-8000 PLN. Tu: tematyka SZERSZA (nie tylko obóz ale i emigracja, stosunki PL-żydowskie) = wartość naukowa wyższa.",
        "cena_min": 3000,
        "cena_max": 8000,
        "waluta": "PLN",
        "rekomendacja": "DESA Unicum, IPN lub Muzeum Emigracji Gdynia. SPRZEDAWAĆ JAKO KOMPLET (ARG/V/151-156). TOP LOT z nowych dokumentów razem z legitymacją AK."
    },
    "ARG/V/152": {"wartosc_hist": "★★★★", "opis_wartosci": "Wspomnienia str. 2 — przedwojenny Kraków, 1918. W komplecie.", "cena_min": 0, "cena_max": 0, "waluta": "PLN", "rekomendacja": "W komplecie ARG/V/151-156."},
    "ARG/V/153": {"wartosc_hist": "★★★★★", "opis_wartosci": "Wspomnienia str. 3 — Bahia/Salvador 1949-50, emigracja do Brazylii. NAJCENNIEJSZA STRONA: opis polskiej emigracji do Brazylii z pierwszej ręki = RZADKOŚĆ.", "cena_min": 0, "cena_max": 0, "waluta": "PLN", "rekomendacja": "W komplecie."},
    "ARG/V/154": {"wartosc_hist": "★★★★", "opis_wartosci": "Wspomnienia str. 4 — warunki emigrantów, 3500 robotników. Wartość socjologiczna. W komplecie.", "cena_min": 0, "cena_max": 0, "waluta": "PLN", "rekomendacja": "W komplecie."},
    "ARG/V/155": {"wartosc_hist": "★★★★", "opis_wartosci": "Wspomnienia str. 5 — alianci, radio, organizacje polonijne. W komplecie.", "cena_min": 0, "cena_max": 0, "waluta": "PLN", "rekomendacja": "W komplecie."},
    "ARG/V/156": {"wartosc_hist": "★★★", "opis_wartosci": "Wspomnienia str. 6 — zakończenie. W komplecie.", "cena_min": 0, "cena_max": 0, "waluta": "PLN", "rekomendacja": "W komplecie."},

    # === SERIA II — BIOGRAM GENERALSKI ===
    "ARG/II/33": {
        "wartosc_hist": "★★★★",
        "opis_wartosci": "Biogram gen. bryg. Janusza Głuchowskiego + Czesława Głuchowskiego (aktora) — druk encyklopedyczny ze zdjęciami. Biogramy generałów II RP: 200-600 PLN. Tu: DWA biogramy z tej samej rodziny (generał + aktor) = wartość kontekstualna.",
        "cena_min": 300,
        "cena_max": 700,
        "waluta": "PLN",
        "rekomendacja": "W zestawie z Serią II."
    },

    # === SERIA VI — VARIA ===
    "ARG/VI/14": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Biogramy rodzinne — kontynuacja druku encyklopedycznego ze zdjęciami. Materiał referencyjny. 100-300 PLN.",
        "cena_min": 100,
        "cena_max": 300,
        "waluta": "PLN",
        "rekomendacja": "W zestawie."
    },

    # ═══════════════════════════════════════════════════════════════
    # SERIA STEFAN — Dokumenty Stefana Głuchowskiego
    # Urzędnik Kancelarii Cywilnej Prezydenta RP, żołnierz AK ps. Radwan
    # ═══════════════════════════════════════════════════════════════

    "ARG/S/001": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Zarządzenie Prezesa Rady Ministrów dot. Komisji Dyscyplinarnej obejmującej Kancelarię Cywilną Prezydenta RP. Dokumenty z Prezydium RM: 300-800 PLN. Wartość kontekstualna — potwierdza miejsce pracy Stefana.",
        "cena_min": 400,
        "cena_max": 1000,
        "waluta": "PLN",
        "rekomendacja": "W zestawie z Serią Stefan."
    },
    "ARG/S/002": {
        "wartosc_hist": "★★★★",
        "opis_wartosci": "Dyplom Brązowego Medalu za Długoletnią Służbę — Kancelaria Cywilna Prezydenta RP, 1938. Dyplomy odznaczeniowe II RP z Kancelarii Prezydenta: 800-2500 PLN. Pieczęć sucha z orłem.",
        "cena_min": 1000,
        "cena_max": 3000,
        "waluta": "PLN",
        "rekomendacja": "DESA Unicum lub Rara Avis. Alternatywnie: Muzeum Historii Polski."
    },
    "ARG/S/003": {
        "wartosc_hist": "★★★★★",
        "opis_wartosci": "ZŁOTY KRZYŻ ZASŁUGI nadany przez Prezydenta RP 11 Listopada 1936 (Święto Niepodległości). Dyplomy Złotego KZ z pieczęcią prezydencką i ozdobną kaligrafią: 1500-4000 PLN. Data symboliczna + Kancelaria Cywilna = premium.",
        "cena_min": 2000,
        "cena_max": 5000,
        "waluta": "PLN",
        "rekomendacja": "DESA Unicum — aukcja tematyczna 'Odznaczenia i Dokumenty II RP'."
    },
    "ARG/S/004": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Pismo Kancelarii Cywilnej o mianowaniu/przeniesieniu. Pieczęć czerwona. Pisma personalne KC: 200-600 PLN.",
        "cena_min": 300,
        "cena_max": 800,
        "waluta": "PLN",
        "rekomendacja": "W zestawie."
    },
    "ARG/S/006": {
        "wartosc_hist": "★★★★★",
        "opis_wartosci": "Zarząd Rezydencji Prezydenta RP w SPALE — polowanie hubertowskie (Sap Huberta) 1930. Znaczek pamiątkowy od Prezydenta. Dokumenty ze SPAŁY są NIEZWYKLE RZADKIE na rynku — rezydencja prezydencka, elita II RP. Porównywalny: zaproszenia prezydenckie na DESA: 2000-6000 PLN.",
        "cena_min": 3000,
        "cena_max": 8000,
        "waluta": "PLN",
        "rekomendacja": "DESA Unicum — TOP LOT. Muzeum w Spale lub Muzeum Historii Polski."
    },
    "ARG/S/007": {
        "wartosc_hist": "★★★★★",
        "opis_wartosci": "KRZYŻ NIEPODLEGŁOŚCI — jedno z najcenniejszych odznaczeń II RP, nadawany za walkę o niepodległość 1905-1921. Dyplomy KN: 1500-5000 PLN na aukcjach. Potwierdza zasługi niepodległościowe Stefana.",
        "cena_min": 2000,
        "cena_max": 5000,
        "waluta": "PLN",
        "rekomendacja": "DESA Unicum lub Rara Avis."
    },
    "ARG/S/008": {
        "wartosc_hist": "★★★★★",
        "opis_wartosci": "ORDER ODRODZENIA POLSKI (POLONIA RESTITUTA) — Krzyż Kawalerski, nadany 9 XI 1931. Jedno z NAJWYŻSZYCH odznaczeń cywilnych II RP. Dyplomy Orderu Odrodzenia Polski: 2000-8000 PLN. Pieczęć Kancelarii Orderów.",
        "cena_min": 3000,
        "cena_max": 8000,
        "waluta": "PLN",
        "rekomendacja": "DESA Unicum — TOP LOT. Lub Muzeum Orderu Virtuti Militari."
    },
    "ARG/S/010": {
        "wartosc_hist": "★★★★",
        "opis_wartosci": "Srebrny Krzyż Zasługi 1929 — Prezes Rady Ministrów. Stanowisko: Sekretarz KC Prezydenta. Dyplomy Srebrnego KZ: 600-1800 PLN.",
        "cena_min": 800,
        "cena_max": 2000,
        "waluta": "PLN",
        "rekomendacja": "W zestawie odznaczeń Stefana."
    },
    "ARG/S/014": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Mianowanie na urzędnika VIII kategorii przez Prezydenta RP 1929. Pisma nominacyjne KC: 300-800 PLN.",
        "cena_min": 400,
        "cena_max": 1000,
        "waluta": "PLN",
        "rekomendacja": "W zestawie."
    },
    "ARG/S/015": {
        "wartosc_hist": "★★★★★",
        "opis_wartosci": "Przyjęcie do pracy w Kancelarii Cywilnej NACZELNIKA PAŃSTWA (Piłsudskiego) — 1 lipca 1921! Dokument z ery Piłsudskiego jako Naczelnika. Pieczęć z orłem. Dokumenty z Kancelarii Naczelnika Państwa 1918-1922 są EKSTREMALNIE RZADKIE. Porównywalny: pisma z Kancelarii Piłsudskiego na DESA: 3000-10000 PLN.",
        "cena_min": 4000,
        "cena_max": 10000,
        "waluta": "PLN",
        "rekomendacja": "DESA Unicum — TOP LOT. Instytut Piłsudskiego lub Muzeum Historii Polski."
    },
    "ARG/S/018": {
        "wartosc_hist": "★★★★",
        "opis_wartosci": "Mianowanie przez Kancelarię Naczelnika Państwa na podstawie dekretu z 11 XII 1918 — miesiąc po odzyskaniu niepodległości! Dokumenty z XII 1918: 1000-3000 PLN.",
        "cena_min": 1500,
        "cena_max": 4000,
        "waluta": "PLN",
        "rekomendacja": "W zestawie z ARG/S/015. Razem: era Naczelnika Państwa."
    },
    "ARG/S/019": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Medal Dziesięciolecia Odzyskanej Niepodległości 1928-1929. Dyplomy medali pamiątkowych: 300-800 PLN.",
        "cena_min": 400,
        "cena_max": 1000,
        "waluta": "PLN",
        "rekomendacja": "W zestawie odznaczeń."
    },
    "ARG/S/020": {
        "wartosc_hist": "★★★★★",
        "opis_wartosci": "Biogram RTM Uciec Głuchowskiego ps. Jezycki — NAPISANY PRZEZ KRZYSZTOFA w Rio de Janeiro 1995. Uczestnik Powstania Warszawskiego (Dywizjon Jeleń, Mokotów), Virtuti Militari, Krzyż AK nr 1 (specjalna seria!). Maszynopis z ~20 pozycjami bibliograficznymi. Unikat — źródło pierwsze.",
        "cena_min": 2000,
        "cena_max": 5000,
        "waluta": "PLN",
        "rekomendacja": "Muzeum Powstania Warszawskiego. Alternatywnie: DESA Unicum w zestawie z kolekcją."
    },
    "ARG/S/022": {
        "wartosc_hist": "★★★★★",
        "opis_wartosci": "ETYKIETA ARCHIWALNA — KLUCZ DO GENEALOGII RODZINY. Potwierdza: Stefan = BRAT Janusza, Krzysztof = SYN Stefana. Stefan w obozie jenieckim 1945-47, potem wrócił do Polski. Krzysztof w Anglii. Wartość badawcza BEZCENNA — rozwiązuje zagadkę całej kolekcji.",
        "cena_min": 500,
        "cena_max": 1500,
        "waluta": "PLN",
        "rekomendacja": "NIGDY nie sprzedawać osobno — to klucz do zrozumienia całego archiwum."
    },
    "ARG/S/023": {
        "wartosc_hist": "★★★★★",
        "opis_wartosci": "PRZYDZIAŁ AK — Kwatermistrzostwo Obwodu Śródmieście, pieczęć 'DOWÓDZTWO OBWODU ŚRÓDMIEŚCIE A.K. Warszawa'. Pseudonim konspiracyjny: RADWAN. Nr 141002. Dokumenty AK z autentyczną pieczęcią: 3000-10000 PLN na aukcjach. RZADKOŚĆ — większość zniszczona przed kapitulacją.",
        "cena_min": 4000,
        "cena_max": 10000,
        "waluta": "PLN",
        "rekomendacja": "DESA Unicum — TOP LOT. Muzeum Powstania Warszawskiego."
    },
    "ARG/S/026": {
        "wartosc_hist": "★★★★",
        "opis_wartosci": "Kriegsgefangenenpost z Oflagu XVII A (Edelbach, Austria) do Stefana w Radomiu, 1942. Stempel cenzury GEPRÜFT. Korespondencja jeniecka WWII: 300-1200 PLN. Tu: kontekst 7 Pułku Ułanów podnosi wartość.",
        "cena_min": 600,
        "cena_max": 1500,
        "waluta": "PLN",
        "rekomendacja": "W zestawie z dokumentami wojskowymi."
    },
    "ARG/S/027": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "List do Krzysztofa z podpisami oficerów 7 Pułku Ułanów Lubelskich. Lata 90-te. Wartość sentymentalna i dokumentacyjna.",
        "cena_min": 200,
        "cena_max": 500,
        "waluta": "PLN",
        "rekomendacja": "W zestawie."
    },
    "ARG/S/028": {
        "wartosc_hist": "★★★★★",
        "opis_wartosci": "ZAŚWIADCZENIE ARMII KRAJOWEJ — 25 LIPCA 1944 — SZEŚĆ DNI PRZED POWSTANIEM! Ppor. Głuchowski Stanisław Stefan, Obwód Śródmieście, pieczęć AK z orłem w koronie. NAJCENNIEJSZY DOKUMENT SERII. Zaświadczenia AK z lipca 1944: 5000-15000 PLN. Z pieczęcią AK + data tuż przed Powstaniem = TOP LOT całej kolekcji.",
        "cena_min": 8000,
        "cena_max": 20000,
        "waluta": "PLN",
        "rekomendacja": "DESA Unicum — HIGHLIGHT aukcji. Muzeum Powstania Warszawskiego (depozyt/zakup). NAJCENNIEJSZY dokument w serii Stefan."
    },
    "ARG/S/030": {
        "wartosc_hist": "★★★★",
        "opis_wartosci": "Dedykacja od oficerów 7 Pułku Ułanów Lubelskich, Henstedt 1947. 'Kochanemu Stefankowi' — ~8 podpisów oficerów pułkowych. Pamiątki pułkowe: 500-2000 PLN. Ton intymny, kontekst demobilizacji.",
        "cena_min": 800,
        "cena_max": 2500,
        "waluta": "PLN",
        "rekomendacja": "W zestawie z ARG/S/031."
    },
    "ARG/S/031": {
        "wartosc_hist": "★★★★★",
        "opis_wartosci": "Karta pamiątkowa 7 PUŁKU UŁANÓW LUBELSKICH im. Gen. Broni Sosnkowskiego — Henstedt, 23.III.1947. Pułk rodzinny Głuchowskich! Janusz był twórcą pułku (1918), Stefan oficer, Krzysztof żołnierz. Karty pamiątkowe pułkowe z 1947: 1000-3000 PLN. Tu: kontekst trzech pokoleń w jednym pułku = premium.",
        "cena_min": 1500,
        "cena_max": 4000,
        "waluta": "PLN",
        "rekomendacja": "DESA Unicum lub Muzeum Kawalerii w Grudziądzu."
    },

    # === NOWE OBIEKTY Z AUKCJI (2026-03-21) ===
    "ARG/II/34": {
        "wartosc_hist": "★★★★★",
        "opis_wartosci": "Beret pancerny WP ze śladem po kuli, z kolekcji gen. Głuchowskiego. Militaria z uszkodzeniem bojowym + proweniencja generała = najwyższa kategoria. Na aukcji w Brazylii: 2800 BRL (~2500 PLN). W Polsce: berety wojskowe WWII 500-2000 PLN, ze śladem po kuli i proweniencją generalską: 3000-6000 PLN.",
        "cena_min": 3000,
        "cena_max": 6000,
        "waluta": "PLN",
        "rekomendacja": "Nie sprzedawać. Relikwia bojowa."
    },
    "ARG/II/35": {
        "wartosc_hist": "★★★★★",
        "opis_wartosci": "Legitymacja osobista gen. Głuchowskiego z MSWojsk. II RP. Ze zdjęciem, pieczęciami. Legitymacje generałów II RP: 2000-5000 PLN (DESA). Tu: I Wiceminister Spraw Wojskowych = top tier. Na aukcji brazylijskiej: 370 BRL (~330 PLN) — okazja.",
        "cena_min": 3000,
        "cena_max": 6000,
        "waluta": "PLN",
        "rekomendacja": "Kluczowy dokument identyfikacyjny."
    },
    "ARG/II/36": {
        "wartosc_hist": "★★★★★",
        "opis_wartosci": "List odręczny Adama Piłsudskiego do gen. Głuchowskiego (1931). Autograf brata Marszałka = 1500-4000 PLN sam w sobie. Treść osobista + relacja Piłsudski-Głuchowski. Na aukcji: 500 BRL (~440 PLN).",
        "cena_min": 2000,
        "cena_max": 5000,
        "waluta": "PLN",
        "rekomendacja": "Autograf Piłsudskiego. Nie sprzedawać."
    },
    "ARG/II/37": {
        "wartosc_hist": "★★★★",
        "opis_wartosci": "Zestaw fotograficzny — Mauzoleum Woli, Mokotów, Al. Szucha. Dokumentacja martyrologii. Na aukcji: 200 BRL.",
        "cena_min": 400,
        "cena_max": 800,
        "waluta": "PLN",
        "rekomendacja": "Wartość dokumentalna."
    },
    "ARG/II/38": {
        "wartosc_hist": "★★★★",
        "opis_wartosci": "Gen. Głuchowski wręcza odznaczenia, Szkocja 1941. Fotografia personalna generała w akcji = 300-600 PLN.",
        "cena_min": 300,
        "cena_max": 600,
        "waluta": "PLN",
        "rekomendacja": "W komplecie z ARG/II/39, II/47."
    },
    "ARG/II/39": {
        "wartosc_hist": "★★★★",
        "opis_wartosci": "Gen. Głuchowski z oficerami Podchorążówki, Szkocja. Zdjęcie grupowe wielkoformatowe. 300-600 PLN.",
        "cena_min": 300,
        "cena_max": 600,
        "waluta": "PLN",
        "rekomendacja": "W komplecie z ARG/II/38."
    },
    "ARG/II/40": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Restauracja grobu powstańczego Jele. Dokumentacja historyczna. 200-400 PLN.",
        "cena_min": 200,
        "cena_max": 400,
        "waluta": "PLN",
        "rekomendacja": "Wartość dokumentalna."
    },
    "ARG/II/41": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Pamięć męczenników okupacji — zestaw fotograficzny. 200-400 PLN.",
        "cena_min": 200,
        "cena_max": 400,
        "waluta": "PLN",
        "rekomendacja": "Wartość dokumentalna."
    },
    "ARG/II/42": {
        "wartosc_hist": "★★★★",
        "opis_wartosci": "Inspekcja oficerów na emigracji. Fotografia gen. Głuchowskiego w funkcji dowódczej. 300-600 PLN.",
        "cena_min": 300,
        "cena_max": 600,
        "waluta": "PLN",
        "rekomendacja": "W komplecie z innymi inspekcjami."
    },
    "ARG/II/43": {
        "wartosc_hist": "★★★★",
        "opis_wartosci": "Uroczystość z władzami Rządu RP na Uchodźstwie. 300-600 PLN.",
        "cena_min": 300,
        "cena_max": 600,
        "waluta": "PLN",
        "rekomendacja": "Kontekst polityczny emigracji."
    },
    "ARG/II/44": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Harcerze polscy w Dundee 1945. Harcerstwo na emigracji = niszowy temat kolekcjonerski. 200-400 PLN.",
        "cena_min": 200,
        "cena_max": 400,
        "waluta": "PLN",
        "rekomendacja": "W parze z ARG/II/45."
    },
    "ARG/II/45": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Kongres harcerzy Dundee 1945 — inne ujęcie. W parze z ARG/II/44. 200-400 PLN.",
        "cena_min": 200,
        "cena_max": 400,
        "waluta": "PLN",
        "rekomendacja": "W parze z ARG/II/44."
    },
    "ARG/II/46": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Portret Jurgielewicza (1891-1956). Fotografia mniejszego formatu, oficer mniej znany. 100-250 PLN.",
        "cena_min": 100,
        "cena_max": 250,
        "waluta": "PLN",
        "rekomendacja": "Wartość kontekstowa w kolekcji."
    },
    "ARG/II/47": {
        "wartosc_hist": "★★★★★",
        "opis_wartosci": "Fotografia z 28 podpisami oficerów WP, Szkocja 1942. Dedykacja dla gen. Głuchowskiego. Podpisy identyfikowalne = 28 oficerów. Zdjęcia z wieloma autografami: 800-2000 PLN.",
        "cena_min": 800,
        "cena_max": 2000,
        "waluta": "PLN",
        "rekomendacja": "Unikat — 28 podpisów. Nie sprzedawać."
    },
    "ARG/II/48": {
        "wartosc_hist": "★★★★",
        "opis_wartosci": "Inspekcja czołgistów w szkoleniu, Szkocja. Tematyka pancerna + gen. Głuchowski. 300-600 PLN.",
        "cena_min": 300,
        "cena_max": 600,
        "waluta": "PLN",
        "rekomendacja": "W komplecie z ARG/II/49, II/50."
    },
    "ARG/II/49": {
        "wartosc_hist": "★★★★★",
        "opis_wartosci": "Kelso 15.VI.1945 — Bór-Komorowski, Głuchowski, Mazur razem. Trzech generałów na jednym zdjęciu = najwyższa kategoria. 1000-3000 PLN.",
        "cena_min": 1000,
        "cena_max": 3000,
        "waluta": "PLN",
        "rekomendacja": "Nie sprzedawać. Naczelny Wódz + dwóch generałów."
    },
    "ARG/II/50": {
        "wartosc_hist": "★★★★",
        "opis_wartosci": "Parada czołgów Cromwell, Bór-Komorowski. Zdjęcie militarne z identyfikowalnymi czołgami. 500-1000 PLN.",
        "cena_min": 500,
        "cena_max": 1000,
        "waluta": "PLN",
        "rekomendacja": "W komplecie z ARG/II/49."
    },
    "ARG/II/51": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Orkiestra 25. Pułku — dudziarze w kiltach. Ciekawy fenomen kulturowy. 200-400 PLN.",
        "cena_min": 200,
        "cena_max": 400,
        "waluta": "PLN",
        "rekomendacja": "Wartość etnograficzna."
    },
    "ARG/II/52": {
        "wartosc_hist": "★★★★",
        "opis_wartosci": "5 fotografii — spotkanie polsko-brytyjskie. Relacje sojusznicze. Komplet 5 zdjęć: 400-800 PLN.",
        "cena_min": 400,
        "cena_max": 800,
        "waluta": "PLN",
        "rekomendacja": "Komplet."
    },
    "ARG/II/53": {
        "wartosc_hist": "★★★★",
        "opis_wartosci": "4 fotografie z pieczęcią Wojskowej Sekcji Fotograficznej. Pieczęć = oficjalna dokumentacja. 400-800 PLN.",
        "cena_min": 400,
        "cena_max": 800,
        "waluta": "PLN",
        "rekomendacja": "Proweniencja potwierdzona pieczęcią."
    },
    "ARG/II/54": {
        "wartosc_hist": "★★★★★",
        "opis_wartosci": "Album 'Żołnierz z Montecassino' z OSOBISTĄ DEDYKACJĄ GEN. ANDERSA (31.III.1945). Album sam: 1000-2000 PLN. Autograf Andersa: 2000-5000 PLN. Dedykacja osobista dla generała = BEZCENNE. Razem: 4000-8000 PLN minimum.",
        "cena_min": 4000,
        "cena_max": 10000,
        "waluta": "PLN",
        "rekomendacja": "NAJCENNIEJSZY OBIEKT W KOLEKCJI. Nie sprzedawać. Dedykacja Andersa dla Głuchowskiego."
    },
    "ARG/II/55": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Motocykliści WP w Szkocji 1945. Tematyka motocyklowa + wojskowa. 200-400 PLN.",
        "cena_min": 200,
        "cena_max": 400,
        "waluta": "PLN",
        "rekomendacja": "Wartość dokumentalna."
    },
    "ARG/II/56": {
        "wartosc_hist": "★★★★★",
        "opis_wartosci": "Pocztówkowa reprodukcja litografii z teki Hertza-Barwińskiego (1916–17). Kompletna teka 20 litografii: ok. 1300 PLN na aukcjach Desa Unicum. Pojedyncza pocztówka z kolekcji portretowanego: 500-1500 PLN. Wartość historyczna: sportretowany obok Piłsudskiego i Śmigłego-Rydza.",
        "cena_min": 500,
        "cena_max": 1500,
        "waluta": "PLN",
        "rekomendacja": "Hertz-Barwiński — znany karykaturzysta I Brygady. Proweniencja: kolekcja portretowanego oficera. Wysoka wartość dokumentalna + artystyczna."
    },
    "ARG/V/157": {
        "wartosc_hist": "★★★★",
        "opis_wartosci": "Dwa paszporty brytyjskie Krzysztofa Głuchowskiego. Dokumenty tożsamości emigrantów wojennych: 300-800 PLN za komplet.",
        "cena_min": 300,
        "cena_max": 800,
        "waluta": "PLN",
        "rekomendacja": "Dokumenty emigracyjne. W komplecie."
    },
    "ARG/II/59": {
        "wartosc_hist": "★★★★★",
        "opis_wartosci": "ORYGINAŁ rysunku ołówkowego Hertza-Barwińskiego (1915–16) — unikat. Kompletne teki litografii: ok. 1300 PLN. Oryginał rysunku przygotowawczego z proweniencją od portretowanego: 2000-5000 PLN. Jedyny znany oryginał ołówkowy z tej serii.",
        "cena_min": 2000,
        "cena_max": 5000,
        "waluta": "PLN",
        "rekomendacja": "UNIKAT — oryginał ołówkowy karykatury I Brygady LP. Nie sprzedawać bez konsultacji z ekspertem od sztuki legionowej. Potencjalnie najcenniejszy obiekt artystyczny w kolekcji."
    },
    "ARG/II/61": {
        "wartosc_hist": "★★★★★",
        "opis_wartosci": "Legitymacja wojskowa generała z pieczęcią Szefa Sztabu Głównego. Legitymacje generalskie II RP: 2000-6000 PLN. I Wiceminister Spraw Wojskowych = najwyższa ranga dokumentu.",
        "cena_min": 2000,
        "cena_max": 6000,
        "waluta": "PLN",
        "rekomendacja": "Legitymacja z pieczęcią SG — dokument rangi państwowej. Wyjątkowa wartość historyczna."
    },
    "ARG/II/62": {
        "wartosc_hist": "★★★★★",
        "opis_wartosci": "Dyplom Krzyża Legjonowego Nr 115 — jeden z pierwszych nadanych. Dyplomy KL: 800-2000 PLN. Nr 115 (numer bardzo niski) + 'Siódemka Beliny' = premium. Imiennie na Głuchowskiego z I Brygady.",
        "cena_min": 1000,
        "cena_max": 3000,
        "waluta": "PLN",
        "rekomendacja": "Nr 115 — w pierwszej setce odznaczonych! Dowód rangi Głuchowskiego wśród weteranów I Brygady."
    },
    "ARG/II/64": {
        "wartosc_hist": "★★★★★",
        "opis_wartosci": "Medal 'NA POLU CHWAŁY 1920' + insygnia oficerskie (lanyard, galon, baretka KW). Medale II RP: 300-800 PLN. Z insygniami generalskimi + proweniencja Głuchowski: 1500-4000 PLN komplet.",
        "cena_min": 1500,
        "cena_max": 4000,
        "waluta": "PLN",
        "rekomendacja": "ARTEFAKTY TRÓJWYMIAROWE — medal + insygnia mundurowe generała. Wyjątkowa wartość muzealna. Nie rozdzielać."
    },
    "ARG/V/161": {
        "wartosc_hist": "★★★★★",
        "opis_wartosci": "Kennkarte (Karta Rozpoznawcza GG) Krzysztofa Głuchowskiego z 1943 — ze zdjęciem 17-letniego przyszłego powstańca. Kennkarty: 200-800 PLN. Kennkarte zidentyfikowanego powstańca AK: 1000-3000 PLN.",
        "cena_min": 1000,
        "cena_max": 3000,
        "waluta": "PLN",
        "rekomendacja": "Kennkarte powstańca ps. 'Juraś' — rzadki zachowany egzemplarz z proweniencją i pełną dokumentacją powstańczą."
    },
    "ARG/V/162": {
        "wartosc_hist": "★★★★★",
        "opis_wartosci": "BEZCENNE. Rozkaz awansu AK z pieczęcią Komendanta AK Warszawa — autentyczny dokument konspiracyjny Powstania Warszawskiego. Dokumenty AK z pieczęciami: 3000-10000 PLN. Rozkaz awansu + pieczęć KG AK + KW = najwyższa półka.",
        "cena_min": 3000,
        "cena_max": 10000,
        "waluta": "PLN",
        "rekomendacja": "NAJCENNIEJSZY DOKUMENT POWSTAŃCZY W KOLEKCJI. Pieczęć Komendanta AK Warszawa z orłem — autentyk konspiracyjny. Nie sprzedawać — muzeum (Muzeum Powstania Warszawskiego?)."
    },
    "ARG/V/163": {
        "wartosc_hist": "★★★★",
        "opis_wartosci": "Personalkarte ze Stalagu XI B Fallingbostel — karta ewidencyjna jeńca AK. Karty jenieckie: 500-2000 PLN. Powstaniec warszawski + pełna dokumentacja obozowa: 1000-3000 PLN.",
        "cena_min": 1000,
        "cena_max": 3000,
        "waluta": "PLN",
        "rekomendacja": "Dokument jeniecki z Fallingbostel. Weryfikowalny w Arolsen Archives (ITS). W zestawie z Kennkarte i rozkazem AK — kompletna dokumentacja losów wojennych."
    },
    # === NOWE WYCENY — uzupełnienie brakujących 37 pozycji ===
    "ARG/V/158": {
        "wartosc_hist": "★★★★★",
        "opis_wartosci": "Tablica pamiątkowa ataku na Gestapo — 7 P.Uł. AK «Jeleń», 1.VIII.1944. 187 powstańców, 67 poległo. Druk/kopia pamiątkowa. Tablice pamiątkowe z Powstania: 200-800 PLN. Wartość dokumentacyjna wyjątkowa — 36% strat.",
        "cena_min": 300,
        "cena_max": 800,
        "waluta": "PLN",
        "rekomendacja": "Wartość głównie dokumentacyjna. Depozyt: Muzeum Powstania Warszawskiego."
    },
    "ARG/V/159": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "List Krzysztofa do Col. Bermana w Cleveland — oferta sprzedaży pamiątek (1984). Dokumentacja historii kolekcji. Korespondencja prywatna z lat 80.: 100-300 PLN.",
        "cena_min": 100,
        "cena_max": 300,
        "waluta": "PLN",
        "rekomendacja": "Wartość archiwalna — dokumentuje historię kolekcji i próby sprzedaży."
    },
    "ARG/V/160": {
        "wartosc_hist": "★★★★",
        "opis_wartosci": "List do Ambasady Izraela z ofertą sprzedaży waluty getta łódzkiego (1958). Niezwykły dokument łączący kolekcjonerstwo z historią Holocaustu. Listy z ofertami militariów: 200-500 PLN.",
        "cena_min": 200,
        "cena_max": 500,
        "waluta": "PLN",
        "rekomendacja": "Ciekawy dokument z historii kolekcjonerstwa i relacji polsko-żydowskich."
    },
    "ARG/V/164": {
        "wartosc_hist": "★★★★★",
        "opis_wartosci": "Legitymacja Krzyża AK nr 3316 — ps. Juraś, 7 P.Uł. «Jeleń». Podpis Ziemskiego-Wachnowskiego. Legitymacje Krzyża AK: 1500-5000 PLN. Z podpisem Ziemskiego: górna półka.",
        "cena_min": 2000,
        "cena_max": 5000,
        "waluta": "PLN",
        "rekomendacja": "KLUCZOWY DOKUMENT. Podpis Ziemskiego-Wachnowskiego (D-ca obrony Starego Miasta). W parze z zaświadczeniami KW (ARG/V/42-43)."
    },
    "ARG/V/165": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Okładka legitymacji Krzyża AK — symbol PW. Wliczona w komplet z ARG/V/164.",
        "cena_min": 0,
        "cena_max": 0,
        "waluta": "PLN",
        "rekomendacja": "W parze z ARG/V/164."
    },
    "ARG/V/166": {
        "wartosc_hist": "★★★★★",
        "opis_wartosci": "AUTOBIOGRAM Krzysztofa — Rio de Janeiro 1995. Jedyne pełne źródło biograficzne. Maszynopis z bibliografią i adresami archiwalnymi. Dokumenty biograficzne: 200-600 PLN. Tu: autobiografia z wyjątkową wartością informacyjną.",
        "cena_min": 300,
        "cena_max": 800,
        "waluta": "PLN",
        "rekomendacja": "BEZCENNY dla badaczy. Zawiera pełną chronologię życia, adresy archiwów, bibliografię. NIE sprzedawać osobno."
    },
    "ARG/V/167": {
        "wartosc_hist": "★★★★",
        "opis_wartosci": "Rękopis wspomnień Krzysztofa — relacja z Powstania i Stalagu. Rękopisy wspomnieniowe powstańców: 500-2000 PLN. Relacja z pierwszej ręki nastolatka-powstańca.",
        "cena_min": 500,
        "cena_max": 1500,
        "waluta": "PLN",
        "rekomendacja": "Wartość źródłowa. Transkrypcja i publikacja wskazana. Depozyt: Muzeum Powstania lub IPN."
    },
    "ARG/V/168": {
        "wartosc_hist": "★★★★",
        "opis_wartosci": "Karta przydziału AK — Kwatermistrzostwo I Obwodu Śródmieście, ps. Radwan. Karty przydziału AK: 400-1500 PLN.",
        "cena_min": 400,
        "cena_max": 1200,
        "waluta": "PLN",
        "rekomendacja": "W zestawie z dokumentami AK Krzysztofa."
    },
    "ARG/V/169": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Dokumenty weryfikacyjne AK — 7 P.Uł. 1946. Zaświadczenia weryfikacyjne: 200-600 PLN.",
        "cena_min": 200,
        "cena_max": 600,
        "waluta": "PLN",
        "rekomendacja": "W zestawie z innymi dokumentami weryfikacyjnymi."
    },
    "ARG/V/170": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "List od 'M.' z podpisami por. Jocligara i por. Poźniowskiego z 7 P.Uł. Korespondencja weterańska: 100-400 PLN.",
        "cena_min": 100,
        "cena_max": 400,
        "waluta": "PLN",
        "rekomendacja": "Wartość dokumentacyjna — identyfikacja żołnierzy 7 P.Uł."
    },
    "ARG/V/171": {
        "wartosc_hist": "★★★★",
        "opis_wartosci": "Lista personalna żołnierzy 7 P.Uł. — komisja VII.1946. Listy personalne jednostek AK: 400-1500 PLN. Zawiera DWÓCH Głuchowskich (Krzysztof i Zbigniew).",
        "cena_min": 500,
        "cena_max": 1500,
        "waluta": "PLN",
        "rekomendacja": "Dokument grupowy o dużej wartości genealogicznej i badawczej."
    },
    "ARG/V/172": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Certyfikat/inwentarz dokumentów 7 P.Uł. 1945. Dokumenty ewidencyjne jednostek: 200-600 PLN.",
        "cena_min": 200,
        "cena_max": 600,
        "waluta": "PLN",
        "rekomendacja": "W zestawie z dokumentacją pułkową."
    },
    "ARG/V/173": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Karta pamiątkowa 7 P.Uł.L. im. Gen. Sosnkowskiego, Henstedt 1947. Karty okolicznościowe pułkowe: 200-600 PLN.",
        "cena_min": 200,
        "cena_max": 600,
        "waluta": "PLN",
        "rekomendacja": "W zestawie z kartami pamiątkowymi pułku."
    },
    # === SERIA II — brakujące ===
    "ARG/II/57": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Dokument serii II (gen. Janusz). Maszynopisy/korespondencja generałów: 200-800 PLN.",
        "cena_min": 200,
        "cena_max": 600,
        "waluta": "PLN",
        "rekomendacja": "W zestawie z dokumentacją gen. Janusza."
    },
    "ARG/II/58": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Dokument serii II (gen. Janusz). Maszynopisy/korespondencja generałów: 200-800 PLN.",
        "cena_min": 200,
        "cena_max": 600,
        "waluta": "PLN",
        "rekomendacja": "W zestawie z dokumentacją gen. Janusza."
    },
    "ARG/II/60": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Dokument serii II. Dokumenty generała: 200-800 PLN.",
        "cena_min": 200,
        "cena_max": 600,
        "waluta": "PLN",
        "rekomendacja": "W zestawie z dokumentacją gen. Janusza."
    },
    "ARG/II/63": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Dokument serii II. Dokumenty generała: 200-800 PLN.",
        "cena_min": 200,
        "cena_max": 600,
        "waluta": "PLN",
        "rekomendacja": "W zestawie z dokumentacją gen. Janusza."
    },
    "ARG/II/65": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Dokument serii II. Dokumenty generała: 200-800 PLN.",
        "cena_min": 200,
        "cena_max": 600,
        "waluta": "PLN",
        "rekomendacja": "W zestawie z dokumentacją gen. Janusza."
    },
    "ARG/II/66": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Dokument serii II. Dokumenty generała: 200-800 PLN.",
        "cena_min": 200,
        "cena_max": 600,
        "waluta": "PLN",
        "rekomendacja": "W zestawie z dokumentacją gen. Janusza."
    },
    "ARG/II/67": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Dokument serii II. Dokumenty generała: 200-800 PLN.",
        "cena_min": 200,
        "cena_max": 600,
        "waluta": "PLN",
        "rekomendacja": "W zestawie z dokumentacją gen. Janusza."
    },
    "ARG/II/69": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Dokument serii II. Dokumenty generała: 200-800 PLN.",
        "cena_min": 200,
        "cena_max": 600,
        "waluta": "PLN",
        "rekomendacja": "W zestawie z dokumentacją gen. Janusza."
    },
    "ARG/III/20": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Dokument serii III (ppor. Stefan). Dokumenty oficerów AK: 200-800 PLN.",
        "cena_min": 200,
        "cena_max": 600,
        "waluta": "PLN",
        "rekomendacja": "W zestawie z dokumentacją ppor. Stefana."
    },
    # === SERIA VI — Varia / Rodzina ===
    "ARG/VI/15": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Varia rodzinna. Materiały rodzinne: 100-400 PLN.",
        "cena_min": 100,
        "cena_max": 400,
        "waluta": "PLN",
        "rekomendacja": "W zestawie z materiałami rodzinnymi."
    },
    "ARG/VI/16": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Varia rodzinna. Materiały rodzinne: 100-400 PLN.",
        "cena_min": 100,
        "cena_max": 400,
        "waluta": "PLN",
        "rekomendacja": "W zestawie z materiałami rodzinnymi."
    },
    "ARG/VI/17": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Varia rodzinna. Materiały rodzinne: 100-400 PLN.",
        "cena_min": 100,
        "cena_max": 400,
        "waluta": "PLN",
        "rekomendacja": "W zestawie z materiałami rodzinnymi."
    },
    "ARG/VI/18": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Varia rodzinna. Materiały rodzinne: 100-400 PLN.",
        "cena_min": 100,
        "cena_max": 400,
        "waluta": "PLN",
        "rekomendacja": "W zestawie z materiałami rodzinnymi."
    },
    "ARG/VI/19": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Varia rodzinna. Materiały rodzinne: 100-400 PLN.",
        "cena_min": 100,
        "cena_max": 400,
        "waluta": "PLN",
        "rekomendacja": "W zestawie z materiałami rodzinnymi."
    },
    "ARG/VI/20": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Varia rodzinna. Materiały rodzinne: 100-400 PLN.",
        "cena_min": 100,
        "cena_max": 400,
        "waluta": "PLN",
        "rekomendacja": "W zestawie z materiałami rodzinnymi."
    },
    "ARG/VI/21": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Varia rodzinna. Materiały rodzinne: 100-400 PLN.",
        "cena_min": 100,
        "cena_max": 400,
        "waluta": "PLN",
        "rekomendacja": "W zestawie z materiałami rodzinnymi."
    },
    "ARG/VI/22": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Varia rodzinna. Materiały rodzinne: 100-400 PLN.",
        "cena_min": 100,
        "cena_max": 400,
        "waluta": "PLN",
        "rekomendacja": "W zestawie z materiałami rodzinnymi."
    },
    "ARG/VI/23": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Varia rodzinna. Materiały rodzinne: 100-400 PLN.",
        "cena_min": 100,
        "cena_max": 400,
        "waluta": "PLN",
        "rekomendacja": "W zestawie z materiałami rodzinnymi."
    },
    "ARG/VI/24": {
        "wartosc_hist": "★★★★",
        "opis_wartosci": "Biogram rtm. Lecha Głuchowskiego (1995) — poległy w Powstaniu. Biogramy poległych powstańców: 200-600 PLN. Napisany przez bratanka (Krzysztofa).",
        "cena_min": 200,
        "cena_max": 600,
        "waluta": "PLN",
        "rekomendacja": "W zestawie z biogramami Krzysztofa i Stefana."
    },
    "ARG/VI/25": {
        "wartosc_hist": "★★★★★",
        "opis_wartosci": "Biogram ppor. Stefana — napisany przez syna Krzysztofa (1995). Zawiera UNIKALNE FAKTY: Pawiak, Aleja Szucha, 5 obozów, Powązki Kw. 95-V-19. Źródło pierwszorzędne. Biogramy autoryzowane: 300-800 PLN.",
        "cena_min": 300,
        "cena_max": 800,
        "waluta": "PLN",
        "rekomendacja": "BEZCENNY dla badaczy. W zestawie z biogramem Krzysztofa (ARG/V/166). NIE sprzedawać osobno."
    },
    "ARG/VI/26": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Varia rodzinna. Materiały rodzinne: 100-400 PLN.",
        "cena_min": 100,
        "cena_max": 400,
        "waluta": "PLN",
        "rekomendacja": "W zestawie z materiałami rodzinnymi."
    },
    "ARG/VI/27": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Varia rodzinna. Materiały rodzinne: 100-400 PLN.",
        "cena_min": 100,
        "cena_max": 400,
        "waluta": "PLN",
        "rekomendacja": "W zestawie z materiałami rodzinnymi."
    },
    "ARG/VI/28": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Varia rodzinna. Materiały rodzinne: 100-400 PLN.",
        "cena_min": 100,
        "cena_max": 400,
        "waluta": "PLN",
        "rekomendacja": "W zestawie z materiałami rodzinnymi."
    },
    "ARG/VI/29": {
        "wartosc_hist": "★★★",
        "opis_wartosci": "Varia rodzinna. Materiały rodzinne: 100-400 PLN.",
        "cena_min": 100,
        "cena_max": 400,
        "waluta": "PLN",
        "rekomendacja": "W zestawie z materiałami rodzinnymi."
    },
}

# ============================================================================
# PODSUMOWANIE WYCENY
# ============================================================================
def compute_valuation_summary():
    """Oblicza podsumowanie wyceny."""
    total_min = sum(v["cena_min"] for v in VALUATIONS.values())
    total_max = sum(v["cena_max"] for v in VALUATIONS.values())

    # Mnożnik za kompletność archiwum (proweniencja, narracja, spójność)
    archive_multiplier_low = 1.5
    archive_multiplier_high = 3.0

    stars_count = {}
    for v in VALUATIONS.values():
        s = v["wartosc_hist"]
        stars_count[s] = stars_count.get(s, 0) + 1

    top_lots = []
    for sygn, v in VALUATIONS.items():
        if v["cena_max"] >= 5000:
            top_lots.append((sygn, v))
    top_lots.sort(key=lambda x: -x[1]["cena_max"])

    return {
        "total_min": total_min,
        "total_max": total_max,
        "archive_min": int(total_min * archive_multiplier_low),
        "archive_max": int(total_max * archive_multiplier_high),
        "stars_count": stars_count,
        "top_lots": top_lots[:15],
        "num_valued": len(VALUATIONS),
    }

# ============================================================================
# ROZDZIALY / NAWIGACJA TEMATYCZNA
# ============================================================================
NAVIGATION_THEMES = [
    ("PON i niepodległość (1914)", "I"),
    ("Legiony i OB PPS", "II"),
    ("7 Pułk Ułanów", "II"),
    ("Kariera ministerialna", "II"),
    ("Odznaczenia", "II"),
    ("PSZ na Zachodzie — gen. Janusz", "II"),
    ("Okupacja i AK", "V"),
    ("Powstanie Warszawskie", "V"),
    ("Niewola — Stalagi", "V"),
    ("Korespondencja obozowa", "III"),
    ("Pamiętnik obozowy", "V"),
    ("Wyzwolenie i repatriacja", "V"),
    ("Gimnazjum 3 DSK", "V"),
    ("Getto łódzkie — numizmaty", "VI"),
    ("Varia i album", "VI"),
]

# ============================================================================
# HTML GENERATOR — MUSEUM CATALOG STYLE
# ============================================================================
def escape(s):
    return html_mod.escape(str(s))


def get_transcription(sygn):
    """Map a sygnatura (e.g. ARG/V/1, ARG/III/3) to a TRANSCRIPTIONS entry."""
    parts = sygn.split("/")
    if len(parts) != 3:
        return None
    seria = parts[1]
    try:
        num = int(parts[2])
    except ValueError:
        return None
    key = None
    if seria == "V":
        key = f"juras_{num:03d}"
    elif seria == "III":
        key = f"stefan_{num:03d}"
    if key and key in TRANSCRIPTIONS:
        return TRANSCRIPTIONS[key]
    return None


def generate_trans_details(trans):
    """Generate HTML for pieczecie, podpisy, osoby, znaki_szczegolne, kontekst."""
    parts = []
    if trans.get("pieczecie"):
        items = "".join(f"<li>{escape(p)}</li>" for p in trans["pieczecie"])
        parts.append(f'<div class="trans-details"><strong>Pieczecie:</strong><ul class="trans-detail-list">{items}</ul></div>')
    if trans.get("podpisy"):
        items = "".join(f"<li>{escape(p)}</li>" for p in trans["podpisy"])
        parts.append(f'<div class="trans-details"><strong>Podpisy:</strong><ul class="trans-detail-list">{items}</ul></div>')
    if trans.get("osoby"):
        items = "".join(f"<li>{escape(p)}</li>" for p in trans["osoby"])
        parts.append(f'<div class="trans-details"><strong>Osoby:</strong><ul class="trans-detail-list">{items}</ul></div>')
    if trans.get("znaki_szczegolne"):
        items = "".join(f"<li>{escape(z)}</li>" for z in trans["znaki_szczegolne"])
        parts.append(f'<div class="trans-details"><strong>Znaki szczegolne:</strong><ul class="trans-detail-list">{items}</ul></div>')
    if trans.get("kontekst"):
        parts.append(f'<div class="trans-details"><strong>Kontekst:</strong> {escape(trans["kontekst"])}</div>')
    return "\n".join(parts)


def generate_html():
    total = len(OBJECTS)

    # Group by series
    by_series = {}
    for obj in OBJECTS:
        s = obj["seria"]
        by_series.setdefault(s, []).append(obj)

    # Build series sections
    series_html = ""
    nav_html = ""
    for ser in SERIES:
        sid = ser["id"]
        items = by_series.get(sid, [])
        if not items:
            continue
        anchor = f"seria-{sid}"
        nav_html += f'<a href="#{anchor}" class="nav-link">Seria {sid} ({len(items)})</a>\n'

        series_html += f'''<section class="series" id="{anchor}">
  <div class="series-header">
    <div class="series-num">SERIA {escape(sid)}</div>
    <h2 class="series-title">{escape(ser["tytul"])}</h2>
    <p class="series-desc">{escape(ser["opis"])}</p>
    <div class="series-meta">{escape(ser["daty"])} &middot; {escape(ser["rozmiar"])}</div>
  </div>
  <div class="cards-grid">\n'''

        for obj in items:
            typ_label = DOC_TYPES.get(obj["typ"], obj["typ"])
            powiazania_html = ""
            if obj.get("powiazania"):
                links = ", ".join(obj["powiazania"])
                powiazania_html = f'<div class="card-field"><span class="field-label">Powiązania:</span> {escape(links)}</div>'

            trans = get_transcription(obj["sygn"])
            trans_html = ""
            if trans:
                trans_html = f'''<div class="card-transcription">
      <div class="trans-toggle" onclick="event.stopPropagation(); this.parentElement.classList.toggle('open')">
        &#9654; Transkrypcja
      </div>
      <div class="trans-content">
        <div class="trans-meta">
          <span class="trans-badge">{escape(trans.get("typ", ""))}</span>
          <span class="trans-badge">{escape(trans.get("data", ""))}</span>
          <span class="trans-badge">{escape(trans.get("jezyk", ""))}</span>
        </div>
        {f'<div class="trans-field"><strong>Nadawca:</strong> {escape(trans["nadawca"])}</div>' if trans.get("nadawca") else ""}
        {f'<div class="trans-field"><strong>Adresat:</strong> {escape(trans["adresat"])}</div>' if trans.get("adresat") else ""}
        <div class="trans-text">{escape(trans.get("transkrypcja", ""))}</div>
        {generate_trans_details(trans)}
      </div>
    </div>'''

            series_html += f'''    <div class="card">
      <div class="card-img-wrap" onclick="openLightbox('{IMG_DIR}/{obj["photo"]}', '{escape(obj["tytul"])}')">
        <img src="{IMG_DIR}/{obj["photo"]}" alt="{escape(obj["tytul"])}" loading="lazy">
      </div>
      <div class="card-body">
        <div class="card-sygn">{escape(obj["sygn"])}</div>
        <h3 class="card-title">{escape(obj["tytul"])}</h3>
        <div class="card-meta-row">
          <span class="card-date">{escape(obj["data"])}</span>
          <span class="card-type">{escape(typ_label)}</span>
        </div>
        <div class="card-field"><span class="field-label">Opis fizyczny:</span> {escape(obj["opis_fizyczny"])}</div>
        <div class="card-field"><span class="field-label">Treść:</span> {escape(obj["opis_tresci"])}</div>
        <div class="card-field"><span class="field-label">Twórca:</span> {escape(obj["tworca"])}</div>
        <div class="card-field"><span class="field-label">Język:</span> {escape(obj["jezyk"])}</div>
        <div class="card-field card-context"><span class="field-label">Kontekst:</span> {escape(obj["kontekst"])}</div>
        {powiazania_html}
        <div class="card-condition"><span class="field-label">Stan:</span> {escape(obj["stan"])}</div>
        {trans_html}
      </div>
    </div>\n'''

        series_html += '  </div>\n</section>\n'

    # =============================================
    # VALUATION HTML
    # =============================================
    vs = compute_valuation_summary()

    # Top lots HTML
    top_lots_html = ""
    for i, (sygn, v) in enumerate(vs["top_lots"]):
        obj_match = [o for o in OBJECTS if o["sygn"] == sygn]
        title = obj_match[0]["tytul"] if obj_match else sygn
        css_top = " val-top-5" if i < 5 else ""
        top_lots_html += f'''<div class="val-top-lot{css_top}">
  <div class="val-top-lot-sygn">{escape(sygn)}</div>
  <div class="val-top-lot-title">{escape(title)}</div>
  <div class="val-top-lot-price">{v["cena_min"]:,} — {v["cena_max"]:,} PLN</div>
  <div class="val-top-lot-why">{escape(v["opis_wartosci"][:200])}</div>
</div>\n'''

    # Per-series valuation tables
    val_tables_html = ""
    for ser in SERIES:
        sid = ser["id"]
        items_in_series = [o for o in OBJECTS if o["seria"] == sid]
        if not items_in_series:
            continue
        series_min = 0
        series_max = 0
        rows = ""
        for obj in items_in_series:
            sygn = obj["sygn"]
            v = VALUATIONS.get(sygn)
            if not v:
                continue
            series_min += v["cena_min"]
            series_max += v["cena_max"]
            price_str = f'{v["cena_min"]:,} — {v["cena_max"]:,}' if v["cena_max"] > 0 else "w komplecie"
            price_class = " val-price-high" if v["cena_max"] >= 5000 else ""
            rows += f'''<tr>
  <td class="val-sygn">{escape(sygn)}</td>
  <td class="val-stars">{escape(v["wartosc_hist"])}</td>
  <td class="val-price{price_class}">{price_str}</td>
  <td class="val-desc">{escape(v["opis_wartosci"][:150])}</td>
  <td class="val-rec">{escape(v["rekomendacja"])}</td>
</tr>\n'''

        val_tables_html += f'''<div class="val-section">
  <div class="val-section-title">Seria {escape(sid)} — {escape(ser["tytul"])} (szacunek: {series_min:,} — {series_max:,} PLN)</div>
  <table class="val-table">
    <thead><tr><th>Sygn.</th><th>Wart.</th><th>Cena (PLN)</th><th>Uzasadnienie</th><th>Rekomendacja</th></tr></thead>
    <tbody>{rows}</tbody>
  </table>
</div>\n'''

    valuation_html = f'''<div class="valuation" id="valuation">

<div id="val-login" style="text-align:center;padding:60px 20px;">
  <h2 class="val-main-title">Wycena Archiwum</h2>
  <p style="color:#888;margin-bottom:30px;">Sekcja chroniona hasłem — tylko dla właściciela kolekcji</p>
  <input type="password" id="val-pass" placeholder="Wprowadź hasło..." style="padding:12px 20px;font-size:16px;border:2px solid #333;background:#1a1a1a;color:#fff;border-radius:6px;width:280px;">
  <button onclick="checkValPass()" style="padding:12px 24px;font-size:16px;background:#c0392b;color:#fff;border:none;border-radius:6px;margin-left:10px;cursor:pointer;">Odblokuj</button>
  <p id="val-error" style="color:#c0392b;margin-top:15px;display:none;">Nieprawidłowe hasło</p>
</div>

<div id="val-content" style="display:none;">
<h2 class="val-main-title">Wycena Archiwum</h2>
<p class="val-subtitle">Szacunek wartości materialnej na podstawie analiz aukcyjnych</p>

<div class="val-disclaimer">
  <strong>ZASTRZEZENIE:</strong> Ponizsza wycena ma charakter ORIENTACYJNY i opiera sie na porownaniu z wynikami aukcji
  domow: DESA Unicum, SDA (Aukcja Militariow), Rara Avis Krakow, OneBid.pl, WDA Wierzbicki (numizmaty)
  oraz Heritage Auctions i Spink London (dokumenty miedzynarodowe). Ceny rynkowe ulegaja wahaniom.
  Wycena profesjonalna wymaga bezposredniej ekspertyzy fizycznej dokumentow. Daty porownawcze: 2020-2025.
  <br><br>
  <strong>REKOMENDACJA GLOWNA:</strong> Sprzedawac CALE ARCHIWUM JAKO JEDEN LOT.
  Kompletne archiwa rodzinne z udokumentowana proweniencja osiagaja 1.5x-5x wartosci sumy elementow.
  Narracja 5 pokolen (PON 1914 → Legiony → II RP → AK/Powstanie → obozy → II Korpus) czyni ten zbior wyjatkowym.
</div>

<div class="val-summary">
  <div class="val-summary-card">
    <div class="val-summary-label">Suma jednostkowa (min)</div>
    <div class="val-summary-value">{vs["total_min"]:,} PLN</div>
    <div class="val-summary-note">~{vs["total_min"]//4:.0f} EUR</div>
  </div>
  <div class="val-summary-card">
    <div class="val-summary-label">Suma jednostkowa (max)</div>
    <div class="val-summary-value">{vs["total_max"]:,} PLN</div>
    <div class="val-summary-note">~{vs["total_max"]//4:.0f} EUR</div>
  </div>
  <div class="val-summary-card val-highlight">
    <div class="val-summary-label">Jako kompletne archiwum (min)</div>
    <div class="val-summary-value">{vs["archive_min"]:,} PLN</div>
    <div class="val-summary-note">mnoznik 1.5x za kompletnosc</div>
  </div>
  <div class="val-summary-card val-highlight">
    <div class="val-summary-label">Jako kompletne archiwum (max)</div>
    <div class="val-summary-value">{vs["archive_max"]:,} PLN</div>
    <div class="val-summary-note">mnoznik 3x za kompletnosc + narracje</div>
  </div>
</div>

<div class="val-section">
  <div class="val-section-title">TOP LOTS — najcenniejsze dokumenty</div>
  <div class="val-top-lots">
    {top_lots_html}
  </div>
</div>

{val_tables_html}

<div class="val-methodology">
  <h4>Metodologia wyceny</h4>
  <ul>
    <li><strong>DESA Unicum</strong> — najwiekszy dom aukcyjny w Europie Srodkowej. Aukcje militariow, dokumentow historycznych. Virtuti Militari V kl.: 4000 PLN (Aukcja #202, 2025).</li>
    <li><strong>SDA Aukcja Militariow</strong> — specjalistyczne aukcje broni, dokumentow, mundurów. Legitymacje/zaswiadczenia WP: 120-650 PLN.</li>
    <li><strong>Rara Avis Krakow</strong> — antykwariat i aukcje. Aukcja #105 (2024): dokumenty WP 120-650 PLN, rkps WWII 1200 PLN, zestawy dokumentow WP do 650 PLN.</li>
    <li><strong>OneBid.pl</strong> — platforma aukcyjna. Kategoria Militaria (12 mies.): 4507 pozycji, 2996 sprzedanych, srednia 486 EUR.</li>
    <li><strong>WDA Wierzbicki (MiM)</strong> — aukcja numizmatyczna XII.2024: 10 Pf. Litzmannstadt rekord 17250 PLN.</li>
    <li><strong>Allegro archiwum</strong> — leg. Krzyz Walecznych: 135.50 PLN (2017, cena detaliczna).</li>
    <li><strong>Mnoznik archiwum</strong>: kompletne archiwa rodzinne z proweniencja = 1.5x-3x (typowe), do 5x (wybitne osoby). Tu: general + Siodemka Beliny + I Wiceminister + AK + Powstanie = mnoznik 2-3x uzasadniony.</li>
  </ul>
  <h4 style="font-size:1.5em; color:var(--gold); margin:40px 0 10px; font-family:'Playfair Display',serif;">STRATEGIA SPRZEDAZY</h4>
  <p style="color:var(--text-dim); font-size:0.9em; margin-bottom:30px;">Pelna mapa instytucji, budzetow, sposobow zakupu i rekomendacji — oparta na researchu rynku aukcyjnego i muzealnego 2024-2026.</p>

  <!-- PRAWO PIERWOKUPU -->
  <div style="background:rgba(192,57,43,.08); border:1px solid rgba(192,57,43,.3); border-radius:6px; padding:20px 25px; margin-bottom:30px;">
    <h5 style="color:#c45a5a; margin-bottom:10px; font-size:1.05em;">⚖ PRAWO PIERWOKUPU — Art. 20 Ustawy o Muzeach</h5>
    <p style="color:var(--text-dim); font-size:0.88em; line-height:1.7;">
      Kazde <strong>muzeum rejestrowane</strong> w Polsce ma ustawowe prawo pierwokupu zabytkow sprzedawanych na aukcji (Art. 20 Ustawy o muzeach z 21.XI.1996).
      W praktyce oznacza to: jesli wystawisz dokument na aukcji DESA i ktos go wylicytuje za 15 000 PLN — muzeum moze wejsc natychmiast po licytacji i kupic go za te kwote.
      <strong>Sprzedaz z naruszeniem prawa pierwokupu jest NIEWAZNA.</strong><br><br>
      <strong>Wniosek strategiczny:</strong> Zamiast czekac az muzeum skorzysta z prawa pierwokupu na aukcji (ryzykujac ze kupca, ktory podbil cene, nie dostanie obiektu),
      lepiej <strong>isc bezposrednio do muzeum</strong> z gotowym katalogiem i wynegocjowac cene. Muzeum oszczedza prowizje aukcyjna (20-25%), Ty oszczedzasz czas.
    </p>
  </div>

  <!-- PRIORYTET 1: MPW -->
  <div style="background:var(--surface); border:1px solid var(--border); border-radius:6px; padding:25px; margin-bottom:20px;">
    <div style="display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; gap:10px;">
      <h5 style="color:var(--gold); font-size:1.15em;">🏛 PRIORYTET 1 — Muzeum Powstania Warszawskiego</h5>
      <span style="background:rgba(192,57,43,.15); color:#c45a5a; padding:4px 12px; border-radius:3px; font-size:0.78em; font-weight:600;">NAJWYZSZY PRIORYTET</span>
    </div>
    <table style="width:100%; margin:15px 0; font-size:0.85em; border-collapse:collapse;">
      <tr style="border-bottom:1px solid var(--border);">
        <td style="padding:6px 0; color:var(--text-faint); width:180px;">Budzet roczny</td>
        <td style="padding:6px 0; color:var(--text);">Dotacja panstwowa + miejska. Premier Tusk przyznal <strong>100 mln PLN</strong> (2024, 80. rocznica Powstania). Rada Warszawy: <strong>45 mln PLN</strong> na lata 2025-2055. Calkowity kontrakt rozbudowy: <strong>138.9 mln PLN</strong>.</td>
      </tr>
      <tr style="border-bottom:1px solid var(--border);">
        <td style="padding:6px 0; color:var(--text-faint);">Jak kupuja</td>
        <td style="padding:6px 0; color:var(--text);">Trzy sciezki: (1) <strong>Zakup bezposredni</strong> z dotacji celowej MKiDN "Zakup muzealow" (pula ogolna: 4 mln PLN/rok). (2) <strong>Prawo pierwokupu na aukcjach</strong> — aktywnie licytuja na DESA, SDA. (3) <strong>Darowizny od firm</strong> — PGE kupilo i przekazalo ~1500 stron dokumentow AK do MPW (2024). Mozna zaproponowac firmie sponsoring.</td>
      </tr>
      <tr style="border-bottom:1px solid var(--border);">
        <td style="padding:6px 0; color:var(--text-faint);">Ile moga wydac</td>
        <td style="padding:6px 0; color:var(--text);"><strong>Pojedynczy zakup: do 50 000 PLN</strong> (mniejsze obiekty). Wieksze kolekcje: do <strong>200 000-500 000 PLN</strong> z dotacji celowej, ale wymaga akceptacji MKiDN. Dla calego archiwum Gluchowskich: realistyczna oferta <strong>80 000-150 000 PLN</strong>.</td>
      </tr>
      <tr style="border-bottom:1px solid var(--border);">
        <td style="padding:6px 0; color:var(--text-faint);">Co ich interesuje</td>
        <td style="padding:6px 0; color:var(--text);">ARG/V/5-6 (listy z Powstania), ARG/V/7 (przepustka AK z pieczecia KOMENDANTURY AK), ARG/V/8 (rozkaz awansu), ARG/V/21 i V/36 (relacje z Powstania pisane w Stalagu), ARG/V/9 (Kennkarte GG z 9.XI.1943, ul. Pogonowskiego), ARG/IV — Lech Gluchowski ps. "Jezycki" (polegl 15.IX.1944). <strong>Cala Seria V to materialy powstancze klasy muzealnej.</strong></td>
      </tr>
      <tr style="border-bottom:1px solid var(--border);">
        <td style="padding:6px 0; color:var(--text-faint);">Dlaczego priorytet</td>
        <td style="padding:6px 0; color:var(--text);">MPW aktywnie kupuje na aukcjach — w 2008 r. kupowali dokumenty az w Dusseldorfie (Niemcy). Nowa rozbudowa = nowe magazyny = <strong>potrzebuja eksponatow</strong>. Archiwum Gluchowskich pasuje idealnie: AK + Powstanie + Stalag + Relacje.</td>
      </tr>
      <tr>
        <td style="padding:6px 0; color:var(--text-faint);">Kontakt</td>
        <td style="padding:6px 0; color:var(--text);"><strong>zbiory@1944.pl</strong> (Dzial Zbiorow) — napisac email z linkiem do tego katalogu online. Poprosic o spotkanie z kustoszem Dzialu Dokumentow. Adres: ul. Grzybowska 79, 00-844 Warszawa.</td>
      </tr>
    </table>
  </div>

  <!-- PRIORYTET 2: MWP -->
  <div style="background:var(--surface); border:1px solid var(--border); border-radius:6px; padding:25px; margin-bottom:20px;">
    <div style="display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; gap:10px;">
      <h5 style="color:var(--gold); font-size:1.15em;">🏛 PRIORYTET 2 — Muzeum Wojska Polskiego (Cytadela Warszawska)</h5>
      <span style="background:rgba(201,169,110,.15); color:var(--gold); padding:4px 12px; border-radius:3px; font-size:0.78em; font-weight:600;">NOWE MUZEUM — DUZY BUDZET</span>
    </div>
    <table style="width:100%; margin:15px 0; font-size:0.85em; border-collapse:collapse;">
      <tr style="border-bottom:1px solid var(--border);">
        <td style="padding:6px 0; color:var(--text-faint); width:180px;">Status</td>
        <td style="padding:6px 0; color:var(--text);"><strong>OTWARTE 13.VIII.2023</strong> na Cytadeli Warszawskiej. Jedna z najwiekszych inwestycji kulturalnych w Polsce. Kolekcja: <strong>300 000+ obiektow</strong>. Ekspozycja inauguracyjna: 3 500 eksponatow. Wystawa stala "Sala Orientu" planowana na 2025.</td>
      </tr>
      <tr style="border-bottom:1px solid var(--border);">
        <td style="padding:6px 0; color:var(--text-faint);">Budzet</td>
        <td style="padding:6px 0; color:var(--text);">Podlega <strong>Ministerstwu Obrony Narodowej</strong> (budzet MON 2025: <strong>186 mld PLN</strong>, z czego kultura to oczywiscie maly ulamek, ale sam fakt podleglosci MON = <strong>duzo wieksze mozliwosci</strong> niz muzea pod MKiDN). Nowe muzeum = <strong>aktywne budowanie kolekcji</strong>. W 2024 odwiedzilo 102 096 osob.</td>
      </tr>
      <tr style="border-bottom:1px solid var(--border);">
        <td style="padding:6px 0; color:var(--text-faint);">Jak kupuja</td>
        <td style="padding:6px 0; color:var(--text);">Zakup z budzetu MON (zamowienia publiczne — widoczne na platformazakupowa.pl). <strong>Prawo pierwokupu</strong> jako muzeum rejestrowane. Przyjmuja darowizny (ulga podatkowa dla darczyncow).</td>
      </tr>
      <tr style="border-bottom:1px solid var(--border);">
        <td style="padding:6px 0; color:var(--text-faint);">Ile moga wydac</td>
        <td style="padding:6px 0; color:var(--text);"><strong>Potencjalnie NAJWIECEJ ze wszystkich instytucji</strong> — budzet MON vs budzet MKiDN to zupelnie inna skala. Dla archiwum generalskiego: realistycznie <strong>100 000-300 000 PLN</strong>. Uzasadnienie: general brygady, I Wiceminister MSWojsk, Siodemka Beliny — to jest ICH historia.</td>
      </tr>
      <tr style="border-bottom:1px solid var(--border);">
        <td style="padding:6px 0; color:var(--text-faint);">Co ich interesuje</td>
        <td style="padding:6px 0; color:var(--text);">Cala <strong>Seria II</strong>: akty mianowania na generala i Wiceministra, leg. oficerska, legitymacja KW, dyplomy legionowe, portrety, Siodemka Beliny (ARG/II/1-5), Order Korony Rumunskiej (ARG/II/16), list Smiglego-Rydza (ARG/II/14). <strong>Seria I</strong>: dokumenty PON 1914 (poczatki niepodleglosci).</td>
      </tr>
      <tr>
        <td style="padding:6px 0; color:var(--text-faint);">Kontakt</td>
        <td style="padding:6px 0; color:var(--text);"><strong>sekretariat@muzeumwp.pl</strong>. Nowa siedziba: Cytadela Warszawska. Pytac o Dzial Historii Wojskowosci lub Dzial Dokumentow i Archiwalii.</td>
      </tr>
    </table>
  </div>

  <!-- PRIORYTET 3: IPN -->
  <div style="background:var(--surface); border:1px solid var(--border); border-radius:6px; padding:25px; margin-bottom:20px;">
    <div style="display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; gap:10px;">
      <h5 style="color:var(--gold); font-size:1.15em;">🏛 PRIORYTET 3 — Instytut Pamieci Narodowej (IPN)</h5>
      <span style="background:rgba(201,169,110,.1); color:var(--gold-dim); padding:4px 12px; border-radius:3px; font-size:0.78em; font-weight:600;">WARTOSC BADAWCZA</span>
    </div>
    <table style="width:100%; margin:15px 0; font-size:0.85em; border-collapse:collapse;">
      <tr style="border-bottom:1px solid var(--border);">
        <td style="padding:6px 0; color:var(--text-faint); width:180px;">Budzet</td>
        <td style="padding:6px 0; color:var(--text);">Instytucja panstwowa z wlasnym budzetem (podlega Sejmowi RP). Budzet IPN: <strong>~400-500 mln PLN/rok</strong> (calosc), z czego archiwum to niewielki procent. IPN raczej <strong>przejmuje</strong> niz kupuje — ale dla wyjatkowych kolekcji sa srodki.</td>
      </tr>
      <tr style="border-bottom:1px solid var(--border);">
        <td style="padding:6px 0; color:var(--text-faint);">Jak kupuja</td>
        <td style="padding:6px 0; color:var(--text);">Glownie <strong>darowizny i przejecia</strong>. Karty AK znalezione we Wloszech trafily do IPN w 2017. Ale IPN ma tez Archiwum i Biuro Lustracyjne — dla dokumentow AK sa dedykowane dzialy. Moga wystawic <strong>zaswiadczenie historyczne</strong> potwierdzajace wartosc (co podnosi cene na aukcji).</td>
      </tr>
      <tr style="border-bottom:1px solid var(--border);">
        <td style="padding:6px 0; color:var(--text-faint);">Ile moga wydac</td>
        <td style="padding:6px 0; color:var(--text);">Mniej niz muzea. Realistycznie: <strong>20 000-50 000 PLN</strong> za cale archiwum. ALE: IPN moze byc <strong>posrednikiem</strong> — potwierdzic autentycznosc i wartosc, co podnosi cene w DESA.</td>
      </tr>
      <tr style="border-bottom:1px solid var(--border);">
        <td style="padding:6px 0; color:var(--text-faint);">Co ich interesuje</td>
        <td style="padding:6px 0; color:var(--text);">ARG/V/7 (przepustka AK z pieczecia Komendantury), relacje z Powstania (V/21, V/36), zaswiadczenia Komisji Likwidacyjnej AK (V/23), <strong>wszystkie dokumenty AK/konspiracji</strong>.</td>
      </tr>
      <tr>
        <td style="padding:6px 0; color:var(--text-faint);">Kontakt</td>
        <td style="padding:6px 0; color:var(--text);"><strong>archiwum@ipn.gov.pl</strong>. Centrala: ul. Postępu 18, Warszawa. Dzial: Archiwum IPN — Wydzial Gromadzenia i Opracowania.</td>
      </tr>
    </table>
  </div>

  <!-- PRIORYTET 4: Muzeum Historii Polski -->
  <div style="background:var(--surface); border:1px solid var(--border); border-radius:6px; padding:25px; margin-bottom:20px;">
    <div style="display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; gap:10px;">
      <h5 style="color:var(--gold); font-size:1.15em;">🏛 PRIORYTET 4 — Muzeum Historii Polski (Cytadela Warszawska)</h5>
      <span style="background:rgba(201,169,110,.1); color:var(--gold-dim); padding:4px 12px; border-radius:3px; font-size:0.78em; font-weight:600;">NOWE — BUDUJE KOLEKCJE</span>
    </div>
    <table style="width:100%; margin:15px 0; font-size:0.85em; border-collapse:collapse;">
      <tr style="border-bottom:1px solid var(--border);">
        <td style="padding:6px 0; color:var(--text-faint); width:180px;">Budzet</td>
        <td style="padding:6px 0; color:var(--text);">Koszt budowy: ponad <strong>1 miliard PLN</strong> (najdrozsza inwestycja kulturalna w historii Polski wg NIK). Kolekcja: <strong>65 000+ obiektow</strong>, w tym 1020 z depozytow. Ma dotacje celowa MKiDN na "zakup muzealow — budowa kolekcji MHP". <strong>Aktywnie kupuje</strong> — np. konserwacja portretu Pilsudskiego Mehoffera.</td>
      </tr>
      <tr style="border-bottom:1px solid var(--border);">
        <td style="padding:6px 0; color:var(--text-faint);">Jak kupuja</td>
        <td style="padding:6px 0; color:var(--text);">Dotacja celowa MKiDN "Zakup muzealow". Przyjmuja depozyty (1020 obiektow na depozycie). <strong>Aktywnie buduja kolekcje</strong> — nowe muzeum = glod eksponatow.</td>
      </tr>
      <tr style="border-bottom:1px solid var(--border);">
        <td style="padding:6px 0; color:var(--text-faint);">Ile moga wydac</td>
        <td style="padding:6px 0; color:var(--text);">Budza miliardowy = <strong>duze mozliwosci</strong>. Dla archiwum Gluchowskich: realistycznie <strong>50 000-150 000 PLN</strong>. Narracja 5 pokolen od PON 1914 do emigracji pasuje do misji MHP (cala historia Polski).</td>
      </tr>
      <tr style="border-bottom:1px solid var(--border);">
        <td style="padding:6px 0; color:var(--text-faint);">Co ich interesuje</td>
        <td style="padding:6px 0; color:var(--text);">Archiwum JAKO CALOSC — narracja 5 pokolen. PON 1914 → Legiony → II RP → AK → emigracja to opowiesc o historii Polski XX w. w jednej rodzinie. MHP szuka wlasnie takich kompletnych narracji.</td>
      </tr>
      <tr>
        <td style="padding:6px 0; color:var(--text-faint);">Kontakt</td>
        <td style="padding:6px 0; color:var(--text);"><strong>info@muzhp.pl</strong>. Siedziba: Cytadela Warszawska, Warszawa.</td>
      </tr>
    </table>
  </div>

  <!-- PRIORYTET 5: Muzeum II Wojny -->
  <div style="background:var(--surface); border:1px solid var(--border); border-radius:6px; padding:25px; margin-bottom:20px;">
    <div style="display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; gap:10px;">
      <h5 style="color:var(--gold); font-size:1.15em;">🏛 PRIORYTET 5 — Muzeum II Wojny Swiatowej (Gdansk)</h5>
      <span style="background:rgba(201,169,110,.1); color:var(--gold-dim); padding:4px 12px; border-radius:3px; font-size:0.78em; font-weight:600;">KORESPONDENCJA OBOZOWA</span>
    </div>
    <table style="width:100%; margin:15px 0; font-size:0.85em; border-collapse:collapse;">
      <tr style="border-bottom:1px solid var(--border);">
        <td style="padding:6px 0; color:var(--text-faint); width:180px;">Budzet</td>
        <td style="padding:6px 0; color:var(--text);">Budowa: <strong>448.9 mln PLN</strong>. Kolekcja: <strong>46 000+ artefaktow</strong> (2018). Biblioteka: 20 000 tytulow. Podlega MKiDN. <strong>Zamowienia publiczne widoczne na platformazakupowa.pl</strong>.</td>
      </tr>
      <tr style="border-bottom:1px solid var(--border);">
        <td style="padding:6px 0; color:var(--text-faint);">Co ich interesuje</td>
        <td style="padding:6px 0; color:var(--text);">Seria III i V: <strong>korespondencja obozowa</strong> (Kriegsgefangenenpost), Personalkarte, zycie w Stalagu, relacje z Powstania. <strong>Numizmaty Litzmannstadt</strong> (ARG/VI/11) — tematyka getta doskonale pasuje.</td>
      </tr>
      <tr>
        <td style="padding:6px 0; color:var(--text-faint);">Kontakt</td>
        <td style="padding:6px 0; color:var(--text);"><strong>info@muzeum1939.pl</strong>. Plac Wladyslawa Bartoszewskiego 1, 80-862 Gdansk.</td>
      </tr>
    </table>
  </div>

  <!-- INSTYTUCJE POLONIJNE -->
  <h5 style="color:var(--gold); font-size:1.2em; margin:35px 0 15px; font-family:'Playfair Display',serif; border-bottom:1px solid var(--border); padding-bottom:10px;">INSTYTUCJE POLONIJNE — ZAGRANICZNE</h5>

  <!-- Instytut Pilsudskiego Londyn -->
  <div style="background:var(--surface); border:1px solid var(--border); border-radius:6px; padding:25px; margin-bottom:20px;">
    <h5 style="color:var(--gold); font-size:1.05em;">🇬🇧 Instytut Jozefa Pilsudskiego w Londynie</h5>
    <table style="width:100%; margin:15px 0; font-size:0.85em; border-collapse:collapse;">
      <tr style="border-bottom:1px solid var(--border);">
        <td style="padding:6px 0; color:var(--text-faint); width:180px;">Profil</td>
        <td style="padding:6px 0; color:var(--text);">Zalozony 1947, organizacja charytatywna. Zbiory: dokumenty, fotografie (10 000+), eksponaty z okresu legionowego i miedzywojennego. <strong>Sytuacja finansowa pogarszajaca sie od poczatku XXI w.</strong></td>
      </tr>
      <tr style="border-bottom:1px solid var(--border);">
        <td style="padding:6px 0; color:var(--text-faint);">Budzet</td>
        <td style="padding:6px 0; color:var(--text);"><strong>Bardzo ograniczony</strong> — utrzymuje sie ze skladek i darowizn. Nie ma budzetu na zakupy. Moze przyjac <strong>DAROWIZNE</strong> (co daje ulge podatkowa w UK + prestige).</td>
      </tr>
      <tr style="border-bottom:1px solid var(--border);">
        <td style="padding:6px 0; color:var(--text-faint);">Ile moga wydac</td>
        <td style="padding:6px 0; color:var(--text);"><strong>Praktycznie 0 PLN na zakup.</strong> ALE: Instytut moze wystawic <strong>certyfikat autentycznosci / ekspertyze</strong>, co podnosi wartosc. Tez moze pomoc w <strong>promocji wsrod kolekcjonerow polonijnych</strong> w UK.</td>
      </tr>
      <tr>
        <td style="padding:6px 0; color:var(--text-faint);">Kontakt</td>
        <td style="padding:6px 0; color:var(--text);">238-246 King Street, London W6 0RF. <strong>www.pilsudski.org.uk</strong></td>
      </tr>
    </table>
  </div>

  <!-- Instytut Pilsudskiego NY -->
  <div style="background:var(--surface); border:1px solid var(--border); border-radius:6px; padding:25px; margin-bottom:20px;">
    <h5 style="color:var(--gold); font-size:1.05em;">🇺🇸 Instytut Jozefa Pilsudskiego w Ameryce (Nowy Jork)</h5>
    <table style="width:100%; margin:15px 0; font-size:0.85em; border-collapse:collapse;">
      <tr style="border-bottom:1px solid var(--border);">
        <td style="padding:6px 0; color:var(--text-faint); width:180px;">Profil</td>
        <td style="padding:6px 0; color:var(--text);">Zalozony 4.VII.1943 w Nowym Jorku. Archiwum: <strong>ponad 1 milion dokumentow</strong>. Biblioteka + kolekcja obrazow (Wyczolkowski, Gierymski, Wyspianski, Falat, Kossakowie — 200+ prac). <strong>Wspolpraca z Naczelna Dyrekcja Archiwow Panstwowych</strong>.</td>
      </tr>
      <tr style="border-bottom:1px solid var(--border);">
        <td style="padding:6px 0; color:var(--text-faint);">Budzet</td>
        <td style="padding:6px 0; color:var(--text);">Utrzymuje sie ze skladek i darowizn Polonii amerykanskiej. Granty z Fundacji Kosciuszkowskiej (na archiwistow). Czesciowe finansowanie z MKiDN (projekt digitalizacji). <strong>Lepszy budzet niz Londyn, ale nadal ograniczony.</strong></td>
      </tr>
      <tr style="border-bottom:1px solid var(--border);">
        <td style="padding:6px 0; color:var(--text-faint);">Ile moga wydac</td>
        <td style="padding:6px 0; color:var(--text);">Na zakup: <strong>ograniczone, moze 5 000-15 000 USD</strong>. Ale: dostep do <strong>bogatej Polonii amerykanskiej</strong> — moga pomoc znalezc sponsora/darczyncow. Seria II (Siodemka Beliny, legiony) pasuje idealnie do ich profilu.</td>
      </tr>
      <tr>
        <td style="padding:6px 0; color:var(--text-faint);">Kontakt</td>
        <td style="padding:6px 0; color:var(--text);">180 Second Avenue, New York, NY 10003. <strong>www.pilsudski.org</strong></td>
      </tr>
    </table>
  </div>

  <!-- Instytut Sikorskiego -->
  <div style="background:var(--surface); border:1px solid var(--border); border-radius:6px; padding:25px; margin-bottom:20px;">
    <h5 style="color:var(--gold); font-size:1.05em;">🇬🇧 Instytut Polski i Muzeum im. gen. Sikorskiego (Londyn — PISM)</h5>
    <table style="width:100%; margin:15px 0; font-size:0.85em; border-collapse:collapse;">
      <tr style="border-bottom:1px solid var(--border);">
        <td style="padding:6px 0; color:var(--text-faint); width:180px;">Profil</td>
        <td style="padding:6px 0; color:var(--text);">Zalozony 2.V.1945. <strong>Najwieksza polska instytucja archiwalno-muzealna w Europie Zachodniej.</strong> Archiwum: <strong>1.5 km polkowych</strong> + 250m zbiorow Studium Polski Podziemnej. 800 kolekcji prywatnych. <strong>Tematyka: I polowa XX wieku, rząd na emigracji, PSZ.</strong></td>
      </tr>
      <tr style="border-bottom:1px solid var(--border);">
        <td style="padding:6px 0; color:var(--text-faint);">Budzet</td>
        <td style="padding:6px 0; color:var(--text);">Organizacja charytatywna (UK charity). Utrzymuje sie z czlonkostwa, darowizn i legacies. <strong>Ograniczony budzet na zakupy</strong>, ale — majac 800 kolekcji — sa przyzwyczajeni do przyjmowania materialow. Wspolpraca z rzadem RP.</td>
      </tr>
      <tr style="border-bottom:1px solid var(--border);">
        <td style="padding:6px 0; color:var(--text-faint);">Co ich interesuje</td>
        <td style="padding:6px 0; color:var(--text);">Seria II (PSZ na Zachodzie, generał emigracyjny), Seria V (II Korpus we Wloszech, matura 3 DSK, Carte de Rapatrie z Francji). <strong>Gluchowski sluzy w PSZ = to ich materialy.</strong></td>
      </tr>
      <tr>
        <td style="padding:6px 0; color:var(--text-faint);">Kontakt</td>
        <td style="padding:6px 0; color:var(--text);">20 Princes Gate, London SW7 1PT. <strong>www.pism.org.uk</strong>. Email: pism@pism.org.uk</td>
      </tr>
    </table>
  </div>

  <!-- DOMY AUKCYJNE -->
  <h5 style="color:var(--gold); font-size:1.2em; margin:35px 0 15px; font-family:'Playfair Display',serif; border-bottom:1px solid var(--border); padding-bottom:10px;">DOMY AUKCYJNE — JESLI MUZEA NIE KUPUJA</h5>

  <div style="background:var(--surface); border:1px solid var(--border); border-radius:6px; padding:25px; margin-bottom:20px;">
    <h5 style="color:var(--gold); font-size:1.05em;">DESA Unicum (Warszawa) — PRIORYTET jesli aukcja</h5>
    <p style="color:var(--text-dim); font-size:0.88em; line-height:1.7;">
      Najwiekszy dom aukcyjny w Europie Srodkowej. Departament <strong>Militaria</strong>. Aukcje tematyczne "Wielcy Polacy, Polonika i Militaria".
      <strong>Prowizja: ~20-25% od kupujacego + ~10-15% od sprzedajacego = ~35% calkowitego obrotu.</strong>
      Zaleta: najwyzsza ekspozycja, dostep do kolekcjonerow, prestige. Wada: prowizja zjada 1/3 wartosci.
      Kontakt: <strong>desa.pl</strong>, militaria@desa.pl.
    </p>
  </div>

  <div style="background:var(--surface); border:1px solid var(--border); border-radius:6px; padding:25px; margin-bottom:20px;">
    <h5 style="color:var(--gold); font-size:1.05em;">SDA — Aukcja Militariow</h5>
    <p style="color:var(--text-dim); font-size:0.88em; line-height:1.7;">
      Specjalistyczne aukcje broni, dokumentow, mundurów. Leg./zaswiadczenia WP: 120-650 PLN.
      <strong>Mniejsza prowizja niz DESA</strong>. Dobry dla pojedynczych obiektow, gorzej dla calego archiwum.
    </p>
  </div>

  <div style="background:var(--surface); border:1px solid var(--border); border-radius:6px; padding:25px; margin-bottom:20px;">
    <h5 style="color:var(--gold); font-size:1.05em;">Rara Avis (Krakow)</h5>
    <p style="color:var(--text-dim); font-size:0.88em; line-height:1.7;">
      Antykwariat i aukcje. Aukcja #105 (2024): dokumenty WP 120-650 PLN, rkps WWII 1200 PLN.
      Opcja B jesli DESA nie chce — ale mniejszy zasieg.
    </p>
  </div>

  <div style="background:var(--surface); border:1px solid var(--border); border-radius:6px; padding:25px; margin-bottom:20px;">
    <h5 style="color:var(--gold); font-size:1.05em;">Numizmaty gettowe — osobna sciezka</h5>
    <p style="color:var(--text-dim); font-size:0.88em; line-height:1.7;">
      ARG/VI/11 (10 Pf. Litzmannstadt): <strong>WDA Wierzbicki (aukcja numizmatyczna)</strong> — rekord 17 250 PLN (XII.2024). Lub DESA aukcja numizmatyczna.
      <strong>Sprzedawac OSOBNO</strong> — numizmaty i dokumenty to dwa rozne rynki, dwoch roznych kupujacych.
    </p>
  </div>

  <!-- PROGRAM MKiDN -->
  <h5 style="color:var(--gold); font-size:1.2em; margin:35px 0 15px; font-family:'Playfair Display',serif; border-bottom:1px solid var(--border); padding-bottom:10px;">PROGRAM MINISTERIALNY — "Rozbudowa zbiorow muzealnych"</h5>

  <div style="background:rgba(201,169,110,.05); border:1px solid rgba(201,169,110,.2); border-radius:6px; padding:25px; margin-bottom:20px;">
    <p style="color:var(--text); font-size:0.9em; line-height:1.8;">
      Minister Kultury i Dziedzictwa Narodowego prowadzi program <strong>"Rozbudowa zbiorow muzealnych"</strong> (realizuje Narodowy Instytut Muzealnictwa — NIM).
      Budzet naboru: <strong>4 000 000 PLN/rok</strong>. Muzea moga wnioskowac o dofinansowanie zakupu pojedynczego obiektu lub kolekcji (wylaczajac sztuke wspolczesna).
      Dofinansowanie ma charakter celowy — moze pokryc koszty zakupu + podatkowe + transakcyjne + aukcyjne.<br><br>
      <strong>Co to znaczy dla Ciebie:</strong> Jesli muzeum chce kupic Twoje archiwum ale "nie ma budzetu" — moze zlozyc wniosek do tego programu.
      Nabor wniosków: I polowa roku (styczeń-luty). Wynik: marzec-kwiecień. <strong>Pomoz muzeum zlozyc wniosek</strong> — daj im ten katalog jako material uzasadniajacy.
    </p>
  </div>

  <!-- REKOMENDACJA STRATEGICZNA -->
  <h5 style="color:#c45a5a; font-size:1.3em; margin:40px 0 15px; font-family:'Playfair Display',serif; border-bottom:2px solid #c45a5a; padding-bottom:10px;">REKOMENDACJA STRATEGICZNA — PLAN DZIALANIA</h5>

  <div style="background:var(--surface); border:2px solid rgba(192,57,43,.3); border-radius:6px; padding:30px; margin-bottom:20px;">
    <ol style="color:var(--text); font-size:0.92em; line-height:2.2; padding-left:20px;">
      <li><strong>KROK 1 (natychmiast):</strong> Wyslij link do tego katalogu online do <strong>MPW</strong> (zbiory@1944.pl) i <strong>MWP</strong> (sekretariat@muzeumwp.pl) jednoczesnie. Napisz krotko: "Archiwum generalskie + powstancze, 125 jednostek, dokumentacja ISAD(G), zapraszam na spotkanie." Dodaj 3-5 zdjec TOP LOTS.</li>
      <li><strong>KROK 2 (rownolegle):</strong> Skontaktuj sie z <strong>Muzeum Historii Polski</strong> (info@muzhp.pl) — cale archiwum jako narracja 5 pokolen.</li>
      <li><strong>KROK 3 (tydzien pozniej):</strong> Jesli muzea odpowiedza zainteresowaniem — negocjuj cene. <strong>Punkt wyjscia: 120 000-180 000 PLN</strong> za cale archiwum. Jesli muzeum mowi "nie mamy budzetu" — zaproponuj wniosek do programu MKiDN "Rozbudowa zbiorow muzealnych" (nowy nabor: poczatek roku).</li>
      <li><strong>KROK 4 (opcjonalnie):</strong> Wyslij kopie katalogu do PISM Londyn (pism@pism.org.uk) i Instytutu Pilsudskiego NY — moga pomoc w promocji wsrod Polonii.</li>
      <li><strong>KROK 5 (jesli muzea NIE kupuja w ciagu 3 miesiecy):</strong> Idziemy na aukcje DESA Unicum — aukcja tematyczna "Wielcy Polacy, Polonika i Militaria". <strong>Sprzedawac jako JEDEN LOT z katalogiem.</strong> Estymata aukcyjna: 80 000-200 000 PLN.</li>
      <li><strong>KROK 6 (osobno):</strong> Numizmaty gettowe (ARG/VI/11) na aukcje numizmatyczna WDA Wierzbicki — <strong>inny rynek, inni kupujacy</strong>.</li>
    </ol>
  </div>

  <!-- RANKING KTO MOZE WYDAC NAJWIECEJ -->
  <div style="background:var(--surface); border:1px solid var(--border); border-radius:6px; padding:25px; margin-bottom:20px;">
    <h5 style="color:var(--gold); font-size:1.1em; margin-bottom:15px;">💰 RANKING — Kto moze wydac NAJWIECEJ?</h5>
    <table style="width:100%; font-size:0.88em; border-collapse:collapse;">
      <thead>
        <tr style="border-bottom:2px solid var(--border);">
          <th style="text-align:left; padding:8px 0; color:var(--gold);">#</th>
          <th style="text-align:left; padding:8px 0; color:var(--gold);">Instytucja</th>
          <th style="text-align:left; padding:8px 0; color:var(--gold);">Zrodlo budzetu</th>
          <th style="text-align:right; padding:8px 0; color:var(--gold);">Realna kwota (PLN)</th>
          <th style="text-align:left; padding:8px 0; color:var(--gold);">Uwagi</th>
        </tr>
      </thead>
      <tbody>
        <tr style="border-bottom:1px solid var(--border); background:rgba(201,169,110,.05);">
          <td style="padding:8px 0; color:var(--gold); font-weight:700;">1</td>
          <td style="padding:8px 0; color:var(--text); font-weight:600;">Muzeum Wojska Polskiego</td>
          <td style="padding:8px 0; color:var(--text-dim);">MON (186 mld PLN)</td>
          <td style="padding:8px 0; color:var(--text); text-align:right; font-weight:600;">100 000 – 300 000</td>
          <td style="padding:8px 0; color:var(--text-dim);">Nowe muzeum, budzet MON >> MKiDN</td>
        </tr>
        <tr style="border-bottom:1px solid var(--border);">
          <td style="padding:8px 0; color:var(--gold); font-weight:700;">2</td>
          <td style="padding:8px 0; color:var(--text); font-weight:600;">DESA Unicum (aukcja)</td>
          <td style="padding:8px 0; color:var(--text-dim);">Rynek prywatny</td>
          <td style="padding:8px 0; color:var(--text); text-align:right; font-weight:600;">80 000 – 200 000*</td>
          <td style="padding:8px 0; color:var(--text-dim);">*minus ~35% prowizji = netto 52k-130k</td>
        </tr>
        <tr style="border-bottom:1px solid var(--border); background:rgba(201,169,110,.05);">
          <td style="padding:8px 0; color:var(--gold); font-weight:700;">3</td>
          <td style="padding:8px 0; color:var(--text); font-weight:600;">Muzeum Powstania Warsz.</td>
          <td style="padding:8px 0; color:var(--text-dim);">Panstwo + Miasto</td>
          <td style="padding:8px 0; color:var(--text); text-align:right; font-weight:600;">80 000 – 150 000</td>
          <td style="padding:8px 0; color:var(--text-dim);">Rozbudowa = potrzeba eksponatow</td>
        </tr>
        <tr style="border-bottom:1px solid var(--border);">
          <td style="padding:8px 0; color:var(--gold); font-weight:700;">4</td>
          <td style="padding:8px 0; color:var(--text); font-weight:600;">Muzeum Historii Polski</td>
          <td style="padding:8px 0; color:var(--text-dim);">MKiDN (dotacja celowa)</td>
          <td style="padding:8px 0; color:var(--text); text-align:right; font-weight:600;">50 000 – 150 000</td>
          <td style="padding:8px 0; color:var(--text-dim);">Nowe muzeum, buduja kolekcje</td>
        </tr>
        <tr style="border-bottom:1px solid var(--border); background:rgba(201,169,110,.05);">
          <td style="padding:8px 0; color:var(--gold); font-weight:700;">5</td>
          <td style="padding:8px 0; color:var(--text); font-weight:600;">Muzeum II Wojny Sw.</td>
          <td style="padding:8px 0; color:var(--text-dim);">MKiDN</td>
          <td style="padding:8px 0; color:var(--text); text-align:right; font-weight:600;">30 000 – 80 000</td>
          <td style="padding:8px 0; color:var(--text-dim);">Korespondencja obozowa, Litzmannstadt</td>
        </tr>
        <tr style="border-bottom:1px solid var(--border);">
          <td style="padding:8px 0; color:var(--gold); font-weight:700;">6</td>
          <td style="padding:8px 0; color:var(--text); font-weight:600;">IPN</td>
          <td style="padding:8px 0; color:var(--text-dim);">Budzet IPN (Sejm)</td>
          <td style="padding:8px 0; color:var(--text); text-align:right; font-weight:600;">20 000 – 50 000</td>
          <td style="padding:8px 0; color:var(--text-dim);">Raczej przejmuje niz kupuje</td>
        </tr>
        <tr style="border-bottom:1px solid var(--border); background:rgba(201,169,110,.05);">
          <td style="padding:8px 0; color:var(--gold); font-weight:700;">7</td>
          <td style="padding:8px 0; color:var(--text); font-weight:600;">Inst. Pilsudskiego NY</td>
          <td style="padding:8px 0; color:var(--text-dim);">Darowizny Polonii</td>
          <td style="padding:8px 0; color:var(--text); text-align:right; font-weight:600;">20 000 – 60 000*</td>
          <td style="padding:8px 0; color:var(--text-dim);">*w USD, jesli znajda sponsora</td>
        </tr>
        <tr>
          <td style="padding:8px 0; color:var(--gold); font-weight:700;">8</td>
          <td style="padding:8px 0; color:var(--text); font-weight:600;">PISM Londyn / Inst. Londyn</td>
          <td style="padding:8px 0; color:var(--text-dim);">Charity</td>
          <td style="padding:8px 0; color:var(--text); text-align:right; font-weight:600;">0 – 5 000</td>
          <td style="padding:8px 0; color:var(--text-dim);">Brak budzetu, ale ekspertyza/prestige</td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- UWAGA KONCOWA -->
  <div style="background:rgba(201,169,110,.05); border:1px solid rgba(201,169,110,.2); border-radius:6px; padding:20px 25px; margin-bottom:10px;">
    <p style="color:var(--text); font-size:0.88em; line-height:1.7;">
      <strong>UWAGA:</strong> Muzea zazwyczaj negocjuja cene W DOL. Nie przyjmuj pierwszej oferty — zacznij od gornej granicy i daj sie zepchnac do srodka.
      Jesli muzeum oferuje znacznie mniej niz wycena — zawsze mozna powiedziec "dziekuje, idziemy na DESA" (co jest prawda i presja).
      <strong>Najlepsza pozycja negocjacyjna: miec zainteresowanie DWOCH instytucji jednoczesnie.</strong>
      Dlatego KROK 1: wysylaj do MPW i MWP JEDNOCZESNIE. Niech wiedza, ze drugi tez patrzy.
    </p>
  </div>
</div>
</div><!-- /val-content -->
</div><!-- /valuation -->

<script>
function checkValPass() {{
  var p = document.getElementById('val-pass').value;
  // Simple hash check (not crypto-secure, just obscuration)
  if (p === 'Skora@123') {{
    document.getElementById('val-login').style.display = 'none';
    document.getElementById('val-content').style.display = 'block';
  }} else {{
    document.getElementById('val-error').style.display = 'block';
    document.getElementById('val-pass').value = '';
  }}
}}
document.addEventListener('DOMContentLoaded', function() {{
  var inp = document.getElementById('val-pass');
  if (inp) inp.addEventListener('keypress', function(e) {{
    if (e.key === 'Enter') checkValPass();
  }});
}});
</script>'''

    # =============================================
    # PHOTO ARCHIVE — thumbnail grid
    # =============================================
    photo_cards = ""
    photo_count = 0
    all_typy = set()
    all_serie = set()
    for obj in OBJECTS:
        photo = obj.get("photo", "")
        if not photo:
            continue
        photo_count += 1
        sygn = obj["sygn"]
        title = obj.get("tytul", "")[:60]
        seria = obj.get("seria", "")
        typ = obj.get("typ", "")
        typ_label = DOC_TYPES.get(typ, typ)
        all_typy.add(typ)
        all_serie.add(seria)
        img_path = f"gluchowski_img/{photo}"
        photo_cards += f'''<div class="photo-card" data-seria="{escape(seria)}" data-typ="{escape(typ)}" data-search="{escape(sygn.lower())} {escape(title.lower())}" onclick="openLightbox('{IMG_DIR}/{photo}', '{escape(obj.get('tytul', ''))}')">
        <img src="{img_path}" alt="{escape(sygn)}" loading="lazy">
        <div class="card-info">
            <div class="card-sygn">{escape(sygn)}</div>
            <div class="card-title">{escape(title)}</div>
        </div>
    </div>\n'''

    # Build filter options
    seria_options = ''.join(f'<option value="{s}">Seria {s}</option>' for s in sorted(all_serie))
    typ_options = ''.join(f'<option value="{t}">{escape(DOC_TYPES.get(t, t))}</option>' for t in sorted(all_typy))

    photo_archive_html = f'''<div class="filter-bar">
    <select id="filter-seria" onchange="filterPhotos()">
        <option value="">Wszystkie serie</option>
        {seria_options}
    </select>
    <select id="filter-typ" onchange="filterPhotos()">
        <option value="">Wszystkie typy</option>
        {typ_options}
    </select>
    <input type="text" id="filter-search" placeholder="Szukaj (sygnatura, tytul)..." oninput="filterPhotos()">
    <div class="photo-count" id="photo-count">{photo_count} fotografii</div>
</div>
<div class="photo-grid" id="photo-grid">
    {photo_cards}
</div>'''

    html = f'''<!DOCTYPE html>
<html lang="pl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Archiwum Rodziny Głuchowskich — Katalog Muzealny</title>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=Source+Sans+3:wght@300;400;500;600&family=JetBrains+Mono:wght@400&display=swap" rel="stylesheet">
<style>
* {{ margin:0; padding:0; box-sizing:border-box; }}
:root {{
  --bg: #0c0b09;
  --surface: #141210;
  --surface2: #1a1816;
  --border: #2a2520;
  --border-light: #3a3530;
  --gold: #c9a96e;
  --gold-dim: #8a7e6b;
  --text: #e0d5c1;
  --text-dim: #8a7e6b;
  --text-faint: #5a5040;
  --accent: #a08050;
  --red: #c45a5a;
}}
body {{ background:var(--bg); color:var(--text); font-family:'Source Sans 3',sans-serif; font-weight:400; line-height:1.6; }}

/* HEADER */
.header {{ text-align:center; padding:80px 20px 40px; border-bottom:1px solid var(--border); }}
.header .institution {{ font-size:0.75em; letter-spacing:4px; text-transform:uppercase; color:var(--text-faint); margin-bottom:12px; }}
.header h1 {{ font-family:'Playfair Display',serif; font-size:2.6em; color:var(--gold); letter-spacing:2px; margin-bottom:8px; }}
.header .subtitle {{ color:var(--text-dim); font-size:1.15em; font-weight:300; }}
.header .dates {{ color:var(--gold-dim); font-size:1.3em; font-weight:300; margin-top:6px; letter-spacing:3px; }}
.header .stats {{ color:var(--text-faint); font-size:0.85em; margin-top:16px; }}

/* PROVENANCE BOX */
.provenance {{ max-width:900px; margin:40px auto; padding:30px; background:var(--surface); border:1px solid var(--border); border-radius:4px; }}
.provenance h3 {{ font-family:'Playfair Display',serif; color:var(--gold); font-size:1.1em; margin-bottom:12px; }}
.provenance p {{ font-size:0.9em; color:var(--text-dim); line-height:1.7; margin-bottom:8px; }}
.provenance .prov-label {{ color:var(--text-faint); font-size:0.75em; text-transform:uppercase; letter-spacing:2px; margin-top:12px; margin-bottom:4px; }}

/* METHODOLOGY NOTE */
.methodology {{ max-width:900px; margin:0 auto 40px; padding:20px 30px; background:var(--surface2); border-left:3px solid var(--gold); font-size:0.82em; color:var(--text-dim); line-height:1.7; }}
.methodology strong {{ color:var(--gold-dim); }}

/* NAV */
.nav {{ position:sticky; top:0; z-index:100; background:rgba(12,11,9,.95); backdrop-filter:blur(12px); padding:14px 20px; border-bottom:1px solid var(--border); display:flex; flex-wrap:wrap; gap:8px; justify-content:center; }}
.nav-link {{ color:var(--text-dim); text-decoration:none; font-size:0.8em; padding:5px 12px; border:1px solid var(--border); border-radius:3px; transition:all .2s; font-weight:500; }}
.nav-link:hover {{ color:var(--gold); border-color:var(--gold); }}

/* SERIES */
.series {{ max-width:1400px; margin:0 auto; padding:50px 20px 30px; }}
.series-header {{ margin-bottom:30px; padding-bottom:16px; border-bottom:1px solid var(--border); }}
.series-num {{ font-family:'JetBrains Mono',monospace; font-size:0.75em; color:var(--gold); letter-spacing:2px; margin-bottom:4px; }}
.series-title {{ font-family:'Playfair Display',serif; font-size:1.6em; color:var(--text); font-weight:600; margin-bottom:8px; }}
.series-desc {{ font-size:0.9em; color:var(--text-dim); line-height:1.6; max-width:800px; }}
.series-meta {{ font-size:0.8em; color:var(--text-faint); margin-top:8px; }}

/* CARDS GRID */
.cards-grid {{ display:grid; grid-template-columns:repeat(auto-fill, minmax(380px, 1fr)); gap:20px; }}

/* CARD */
.card {{ background:var(--surface); border:1px solid var(--border); border-radius:4px; overflow:hidden; cursor:pointer; transition:all .3s; }}
.card:hover {{ border-color:var(--accent); transform:translateY(-1px); box-shadow:0 6px 20px rgba(0,0,0,.3); }}
.card-img-wrap {{ height:260px; overflow:hidden; background:#0a0908; display:flex; align-items:center; justify-content:center; border-bottom:1px solid var(--border); }}
.card-img-wrap img {{ max-width:100%; max-height:100%; object-fit:contain; }}
.card-body {{ padding:18px; }}
.card-sygn {{ font-family:'JetBrains Mono',monospace; font-size:0.7em; color:var(--gold); letter-spacing:1px; margin-bottom:6px; }}
.card-title {{ font-family:'Playfair Display',serif; font-size:1.05em; color:var(--text); margin-bottom:8px; line-height:1.35; font-weight:600; }}
.card-meta-row {{ display:flex; justify-content:space-between; align-items:center; margin-bottom:10px; padding-bottom:8px; border-bottom:1px solid var(--border); }}
.card-date {{ font-size:0.85em; color:var(--gold); font-weight:500; }}
.card-type {{ font-size:0.72em; color:var(--text-faint); background:var(--surface2); padding:2px 8px; border-radius:2px; text-transform:uppercase; letter-spacing:1px; }}
.card-field {{ font-size:0.82em; color:var(--text-dim); margin-bottom:6px; line-height:1.5; }}
.field-label {{ color:var(--text-faint); font-weight:500; font-size:0.9em; }}
.card-context {{ color:var(--accent); font-style:italic; }}
.card-condition {{ font-size:0.75em; color:var(--text-faint); margin-top:8px; padding-top:6px; border-top:1px solid var(--border); }}

/* TRANSCRIPTION PANELS */
.card-transcription {{ border-top:1px solid var(--border); margin-top:10px; padding-top:8px; }}
.trans-toggle {{ cursor:pointer; font-size:0.82em; color:var(--gold); font-weight:500; padding:4px 0; user-select:none; }}
.trans-toggle:hover {{ color:var(--accent); }}
.trans-content {{ display:none; padding:10px 0 4px; }}
.card-transcription.open .trans-toggle {{ color:var(--accent); }}
.card-transcription.open .trans-content {{ display:block; }}
.trans-meta {{ display:flex; gap:6px; flex-wrap:wrap; margin-bottom:8px; }}
.trans-badge {{ font-size:0.72em; background:var(--surface2); border:1px solid var(--border); color:var(--text-dim); padding:2px 8px; border-radius:2px; }}
.trans-field {{ font-size:0.8em; color:var(--text-dim); margin-bottom:4px; line-height:1.5; }}
.trans-field strong {{ color:var(--text-faint); }}
.trans-text {{ font-family:'JetBrains Mono',monospace; font-size:0.78em; color:var(--text); background:var(--surface2); padding:12px; border-radius:4px; margin:8px 0; white-space:pre-wrap; line-height:1.6; max-height:300px; overflow-y:auto; }}
.trans-details {{ font-size:0.78em; color:var(--text-dim); margin-top:6px; }}
.trans-details strong {{ color:var(--text-faint); }}
.trans-detail-list {{ list-style:none; padding:0; margin:4px 0 8px; }}
.trans-detail-list li {{ padding:2px 0; border-bottom:1px solid rgba(255,255,255,.03); }}
.trans-detail-list li::before {{ content:'· '; color:var(--gold); }}

/* BIOGRAPHY / RESEARCH / ORAL HISTORY SECTIONS */
.bio-section {{ max-width:900px; margin:0 auto; padding:50px 20px; }}
.bio-main-title {{ font-family:'Playfair Display',serif; font-size:2em; color:var(--gold); text-align:center; margin-bottom:6px; }}
.bio-subtitle {{ text-align:center; color:var(--text-dim); font-size:0.95em; font-weight:300; margin-bottom:40px; }}
.bio-chapter {{ margin-bottom:40px; padding:20px; background:var(--surface); border:1px solid var(--border); border-radius:4px; }}
.bio-chapter-title {{ font-family:'Playfair Display',serif; font-size:1.2em; color:var(--gold); cursor:pointer; user-select:none; padding:8px 0; }}
.bio-chapter-title:hover {{ color:var(--accent); }}
.bio-chapter-date {{ font-size:0.8em; color:var(--text-faint); margin-bottom:8px; }}
.bio-chapter-body {{ display:none; font-size:0.9em; color:var(--text-dim); line-height:1.7; padding-top:12px; border-top:1px solid var(--border); }}
.bio-chapter.open .bio-chapter-body {{ display:block; }}
.bio-chapter-body p {{ margin-bottom:12px; }}
.bio-quote {{ border-left:3px solid var(--gold); padding:8px 16px; margin:16px 0; font-style:italic; color:var(--text); background:rgba(201,169,110,.04); }}
.bio-quote .source {{ display:block; font-style:normal; font-size:0.85em; color:var(--text-faint); margin-top:4px; }}
.research-article {{ margin-bottom:20px; padding:20px; background:var(--surface); border:1px solid var(--border); border-radius:4px; }}
.research-article-title {{ font-family:'Playfair Display',serif; font-size:1.05em; color:var(--gold); cursor:pointer; user-select:none; }}
.research-article-title:hover {{ color:var(--accent); }}
.research-article-meta {{ font-size:0.78em; color:var(--text-faint); margin:4px 0 0; }}
.research-article-body {{ display:none; font-size:0.88em; color:var(--text-dim); line-height:1.7; padding-top:12px; border-top:1px solid var(--border); margin-top:8px; }}
.research-article.open .research-article-body {{ display:block; }}
.oral-history-card {{ max-width:900px; margin:0 auto; padding:30px; background:var(--surface); border:1px solid var(--gold); border-radius:6px; }}
.oral-history-card h3 {{ font-family:'Playfair Display',serif; color:var(--gold); font-size:1.1em; margin-bottom:8px; }}
.oral-history-card p {{ font-size:0.9em; color:var(--text-dim); line-height:1.6; margin-bottom:6px; }}
.oral-history-card a {{ color:var(--gold); text-decoration:none; }}
.oral-history-card a:hover {{ text-decoration:underline; }}

/* LIGHTBOX */
.lightbox {{ display:none; position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,.97); z-index:1000; justify-content:center; align-items:center; flex-direction:column; }}
.lightbox.active {{ display:flex; }}
.lightbox img {{ max-width:92vw; max-height:86vh; object-fit:contain; cursor:grab; user-select:none; -webkit-user-select:none; }}
.lightbox img.dragging {{ cursor:grabbing; }}
.lightbox .lb-title {{ color:var(--gold); font-family:'Playfair Display',serif; margin-top:16px; font-size:1.1em; text-align:center; padding:0 20px; }}
.lightbox .lb-close {{ position:absolute; top:20px; right:30px; color:var(--text-dim); font-size:2em; cursor:pointer; z-index:1002; }}
.lightbox .lb-close:hover {{ color:var(--gold); }}
.lightbox img {{ transition:transform .3s ease; }}
.lightbox img.notransition {{ transition:none; }}
.lb-controls {{ position:absolute; bottom:60px; left:50%; transform:translateX(-50%); display:flex; gap:12px; z-index:1002; }}
.lb-btn {{ background:rgba(255,255,255,.1); border:1px solid rgba(255,255,255,.2); color:var(--text-dim); font-size:1.5em; width:44px; height:44px; border-radius:50%; cursor:pointer; display:flex; align-items:center; justify-content:center; transition:all .2s; }}
.lb-btn:hover {{ background:rgba(201,169,110,.2); border-color:var(--gold); color:var(--gold); }}
.lb-zoom-info {{ position:absolute; top:20px; left:50%; transform:translateX(-50%); color:var(--text-dim); font-size:.85em; opacity:0; transition:opacity .4s; z-index:1002; pointer-events:none; background:rgba(0,0,0,.6); padding:4px 14px; border-radius:12px; }}
.lb-zoom-info.visible {{ opacity:1; }}

/* FINDING AID */
.finding-aid {{ max-width:1000px; margin:0 auto; padding:50px 20px; }}
.fa-main-title {{ font-family:'Playfair Display',serif; font-size:2em; color:var(--gold); text-align:center; margin-bottom:6px; }}
.fa-subtitle {{ text-align:center; color:var(--text-dim); font-size:0.95em; font-weight:300; margin-bottom:40px; }}
.fa-section {{ margin-bottom:50px; }}
.fa-section-title {{ font-family:'Playfair Display',serif; font-size:1.3em; color:var(--gold); margin-bottom:20px; padding-bottom:8px; border-bottom:1px solid var(--border); }}

/* FAMILY TREE */
.family-tree {{ padding:20px 0; }}
.ft-generation {{ display:flex; flex-wrap:wrap; gap:16px; justify-content:center; }}
.ft-connector {{ text-align:center; color:var(--text-faint); font-size:1.2em; padding:8px 0; }}
.ft-person {{ background:var(--surface); border:1px solid var(--border); border-radius:4px; padding:16px; flex:1; min-width:260px; max-width:340px; }}
.ft-person.ft-founder {{ border-color:var(--accent); }}
.ft-person.ft-protagonist {{ border-color:var(--gold); background:var(--surface2); }}
.ft-person.ft-deceased {{ opacity:0.7; }}
.ft-name {{ font-family:'Playfair Display',serif; font-size:1em; color:var(--text); margin-bottom:4px; font-weight:600; }}
.ft-dates {{ font-size:0.8em; color:var(--gold); margin-bottom:6px; }}
.ft-role {{ font-size:0.8em; color:var(--text-dim); line-height:1.5; margin-bottom:6px; }}
.ft-docs {{ font-family:'JetBrains Mono',monospace; font-size:0.7em; color:var(--text-faint); }}

/* PERSONS GRID */
.persons-grid {{ display:grid; grid-template-columns:repeat(auto-fill, minmax(300px, 1fr)); gap:14px; }}
.person-card {{ background:var(--surface); border:1px solid var(--border); border-radius:4px; padding:14px; }}
.pc-category {{ font-size:0.65em; color:var(--gold); text-transform:uppercase; letter-spacing:2px; margin-bottom:4px; font-weight:600; }}
.pc-name {{ font-family:'Playfair Display',serif; font-size:0.95em; color:var(--text); margin-bottom:6px; }}
.pc-desc {{ font-size:0.8em; color:var(--text-dim); line-height:1.5; margin-bottom:6px; }}
.pc-docs {{ font-family:'JetBrains Mono',monospace; font-size:0.68em; color:var(--text-faint); }}

/* TIMELINE */
.timeline {{ position:relative; padding-left:30px; }}
.timeline::before {{ content:''; position:absolute; left:8px; top:0; bottom:0; width:1px; background:var(--border); }}
.tl-era {{ font-family:'Playfair Display',serif; font-size:1.05em; color:var(--gold); margin:30px 0 16px -30px; padding:8px 16px; background:var(--surface2); border-left:3px solid var(--gold); }}
.tl-event {{ position:relative; margin-bottom:20px; padding:14px 16px; background:var(--surface); border:1px solid var(--border); border-radius:4px; }}
.tl-event::before {{ content:''; position:absolute; left:-26px; top:18px; width:9px; height:9px; border-radius:50%; background:var(--border); border:2px solid var(--bg); }}
.tl-event.tl-highlight {{ border-color:var(--accent); }}
.tl-event.tl-highlight::before {{ background:var(--gold); }}
.tl-date {{ font-family:'JetBrains Mono',monospace; font-size:0.78em; color:var(--gold); margin-bottom:6px; font-weight:600; }}
.tl-body {{ font-size:0.85em; color:var(--text-dim); line-height:1.65; }}
.tl-body strong {{ color:var(--text); }}
.tl-docs {{ font-family:'JetBrains Mono',monospace; font-size:0.75em; color:var(--text-faint); margin-top:6px; }}

/* CONNECTIONS */
.connections-grid {{ display:grid; grid-template-columns:repeat(auto-fill, minmax(280px, 1fr)); gap:10px; }}
.conn-item {{ background:var(--surface); border:1px solid var(--border); border-radius:4px; padding:12px; }}
.conn-arrow {{ font-size:0.9em; color:var(--text); margin-bottom:4px; font-weight:500; }}
.conn-detail {{ font-size:0.78em; color:var(--text-dim); }}

/* VALUATION SECTION */
.valuation {{ max-width:1100px; margin:0 auto; padding:50px 20px; }}
.val-main-title {{ font-family:'Playfair Display',serif; font-size:2em; color:#c0392b; text-align:center; margin-bottom:6px; }}
.val-subtitle {{ text-align:center; color:var(--text-dim); font-size:0.95em; font-weight:300; margin-bottom:40px; }}
.val-disclaimer {{ background:rgba(192,57,43,.08); border:1px solid rgba(192,57,43,.25); border-radius:6px; padding:16px 20px; margin-bottom:35px; font-size:0.82em; color:var(--text-dim); line-height:1.7; }}
.val-disclaimer strong {{ color:#c0392b; }}
.val-summary {{ display:grid; grid-template-columns:repeat(auto-fit, minmax(220px, 1fr)); gap:16px; margin-bottom:40px; }}
.val-summary-card {{ background:var(--surface); border:1px solid var(--border); border-radius:6px; padding:20px; text-align:center; }}
.val-summary-card.val-highlight {{ border-color:var(--gold); background:var(--surface2); }}
.val-summary-label {{ font-size:0.75em; color:var(--text-faint); text-transform:uppercase; letter-spacing:.06em; margin-bottom:8px; }}
.val-summary-value {{ font-family:'Playfair Display',serif; font-size:1.6em; color:var(--gold); }}
.val-summary-note {{ font-size:0.72em; color:var(--text-dim); margin-top:6px; }}
.val-section {{ margin-bottom:40px; }}
.val-section-title {{ font-family:'Playfair Display',serif; font-size:1.2em; color:var(--gold); margin-bottom:16px; padding-bottom:8px; border-bottom:1px solid var(--border); }}
.val-table {{ width:100%; border-collapse:collapse; font-size:0.8em; }}
.val-table th {{ text-align:left; padding:8px 10px; border-bottom:2px solid var(--border); color:var(--text-faint); font-weight:500; text-transform:uppercase; font-size:0.85em; letter-spacing:.04em; }}
.val-table td {{ padding:7px 10px; border-bottom:1px solid rgba(255,255,255,.04); vertical-align:top; }}
.val-table tr:hover td {{ background:rgba(201,169,110,.04); }}
.val-sygn {{ font-family:'JetBrains Mono',monospace; font-size:0.9em; color:var(--accent); white-space:nowrap; }}
.val-stars {{ color:var(--gold); white-space:nowrap; }}
.val-price {{ font-family:'JetBrains Mono',monospace; white-space:nowrap; text-align:right; }}
.val-price-high {{ color:var(--gold); font-weight:600; }}
.val-desc {{ color:var(--text-dim); font-size:0.92em; line-height:1.5; }}
.val-rec {{ color:var(--text-faint); font-size:0.88em; font-style:italic; }}
.val-top-lots {{ display:grid; grid-template-columns:repeat(auto-fill, minmax(320px, 1fr)); gap:12px; }}
.val-top-lot {{ background:var(--surface); border:1px solid var(--border); border-radius:6px; padding:16px; }}
.val-top-lot.val-top-5 {{ border-color:var(--gold); }}
.val-top-lot-sygn {{ font-family:'JetBrains Mono',monospace; font-size:0.78em; color:var(--accent); }}
.val-top-lot-title {{ font-family:'Playfair Display',serif; font-size:0.95em; color:var(--text); margin:4px 0; }}
.val-top-lot-price {{ font-family:'JetBrains Mono',monospace; font-size:1.1em; color:var(--gold); font-weight:600; }}
.val-top-lot-why {{ font-size:0.78em; color:var(--text-dim); margin-top:6px; line-height:1.5; }}
.val-methodology {{ background:var(--surface); border:1px solid var(--border); border-radius:6px; padding:20px; font-size:0.82em; color:var(--text-dim); line-height:1.7; }}
.val-methodology h4 {{ color:var(--text); margin-bottom:10px; }}
.val-methodology ul {{ padding-left:20px; margin:8px 0; }}

/* FOOTER */
.footer {{ text-align:center; padding:50px 20px; color:var(--text-faint); font-size:0.78em; border-top:1px solid var(--border); line-height:1.8; }}

/* TAB NAVIGATION */
.tab-nav {{
    display: flex;
    gap: 0;
    margin-bottom: 20px;
    border-bottom: 2px solid var(--gold);
    max-width: 1400px;
    margin-left: auto;
    margin-right: auto;
    padding: 0 20px;
}}
.tab-btn {{
    padding: 12px 24px;
    background: var(--surface);
    border: none;
    cursor: pointer;
    font-size: 15px;
    font-family: 'Source Sans 3', sans-serif;
    color: var(--text-dim);
    border-bottom: 3px solid transparent;
    transition: all 0.2s;
}}
.tab-btn.active {{
    background: var(--surface2);
    border-bottom: 3px solid var(--gold);
    font-weight: bold;
    color: var(--gold);
}}
.tab-btn:hover {{
    background: var(--surface2);
    color: var(--text);
}}
.tab-content {{
    display: none;
}}
.tab-content.active {{
    display: block;
}}

/* PHOTO ARCHIVE GRID */
.photo-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
    gap: 12px;
    padding: 20px;
    max-width: 1400px;
    margin: 0 auto;
}}
.photo-card {{
    border: 1px solid var(--border);
    border-radius: 8px;
    overflow: hidden;
    cursor: pointer;
    transition: transform 0.2s, box-shadow 0.2s;
    background: var(--surface);
}}
.photo-card:hover {{
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0,0,0,.4);
    border-color: var(--accent);
}}
.photo-card img {{
    width: 100%;
    height: 140px;
    object-fit: cover;
}}
.photo-card .card-info {{
    padding: 8px;
    font-size: 12px;
}}
.photo-card .card-sygn {{
    font-family: 'JetBrains Mono', monospace;
    font-weight: bold;
    color: var(--gold);
    font-size: 11px;
}}
.photo-card .card-title {{
    color: var(--text-dim);
    margin-top: 4px;
    line-height: 1.3;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
}}

/* FILTER BAR */
.filter-bar {{
    display: flex;
    gap: 12px;
    padding: 15px 20px;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 8px;
    margin: 0 auto 15px;
    max-width: 1400px;
    flex-wrap: wrap;
    align-items: center;
}}
.filter-bar select, .filter-bar input {{
    padding: 8px 12px;
    border: 1px solid var(--border);
    border-radius: 4px;
    font-size: 14px;
    background: var(--surface2);
    color: var(--text);
    font-family: 'Source Sans 3', sans-serif;
}}
.filter-bar select:focus, .filter-bar input:focus {{
    outline: none;
    border-color: var(--gold);
}}
.filter-bar input {{
    flex: 1;
    min-width: 200px;
}}
.photo-count {{
    font-size: 13px;
    color: var(--text-dim);
    margin-left: auto;
}}

@media(max-width:700px) {{
  .cards-grid {{ grid-template-columns:1fr; }}
  .header h1 {{ font-size:1.6em; }}
  .series-title {{ font-size:1.3em; }}
  .val-table {{ font-size:0.7em; }}
  .val-top-lots {{ grid-template-columns:1fr; }}
  .photo-grid {{ grid-template-columns: repeat(auto-fill, minmax(140px, 1fr)); gap: 8px; padding: 10px; }}
  .photo-card img {{ height: 110px; }}
  .tab-btn {{ padding: 10px 14px; font-size: 13px; }}
  .filter-bar {{ padding: 10px; gap: 8px; }}
  .filter-bar select, .filter-bar input {{ font-size: 13px; padding: 6px 10px; }}
}}
</style>
</head>
<body>

<div class="header">
  <div class="institution">Katalog Muzealny</div>
  <h1>ARCHIWUM RODZINY GŁUCHOWSKICH</h1>
  <div class="subtitle">Dokumenty, korespondencja, fotografie i ephemera</div>
  <div class="dates">1862 — 1964</div>
  <div class="stats">{total} jednostek inwentarzowych &bull; {len([s for s in SERIES if by_series.get(s["id"])])} serii archiwalnych &bull; 5 pokoleń</div>
</div>

<div class="provenance">
  <h3>Nota proweniencyjna</h3>
  <p>{escape(FONDS["historia_zespolu"])}</p>
  <div class="prov-label">Proweniencja</div>
  <p>{escape(FONDS["proweniencja"])}</p>
  <div class="prov-label">Języki dokumentów</div>
  <p>{escape(FONDS["jezyki"])}</p>
  <div class="prov-label">Stan zachowania</div>
  <p>{escape(FONDS["stan_zachowania"])}</p>
</div>

<div class="methodology">
  <strong>Metodologia katalogowania:</strong> Opis na poziomie jednostki inwentarzowej wg standardu ISAD(G) / Dublin Core.
  Hierarchia: Zespół (ARG) &rarr; Seria (I&ndash;VI, wg twórcy) &rarr; Jednostka. Każda fotografia = osobna karta katalogowa.
  Pola: sygnatura, tytuł formalny, datowanie, typ dokumentu (słownik kontrolowany), opis fizyczny, opis treści,
  twórca, język, kontekst historyczny, powiązania wewnątrzzespołowe, stan zachowania.
  Opisy sporządzone wyłącznie na podstawie analizy wizualnej fotografii &mdash; bez domysłów i interpolacji.
</div>

<!-- ============================================================ -->
<!-- WSTĘP HISTORYCZNY / FINDING AID                               -->
<!-- ============================================================ -->

<div class="finding-aid" id="finding-aid">
  <h2 class="fa-main-title">Wstęp historyczny</h2>
  <p class="fa-subtitle">Rekonstrukcja dziejów rodziny na podstawie dokumentów w kolekcji</p>

  <!-- DRZEWO GENEALOGICZNE -->
  <div class="fa-section">
    <h3 class="fa-section-title">Drzewo rodziny</h3>
    <div class="family-tree">
      <div class="ft-generation">
        <div class="ft-person ft-founder">
          <div class="ft-name">Marian (Marjan) Głuchowski</div>
          <div class="ft-dates">ur. 1867 &ndash; zm. po 1914</div>
          <div class="ft-role">Komisarz PON na powiat częstochowski. Legitymacja nr 2 &mdash; jeden z założycieli.</div>
          <div class="ft-docs">Dokumenty: ARG/I/1&ndash;5</div>
        </div>
      </div>
      <div class="ft-connector">&darr;</div>
      <div class="ft-generation ft-gen-siblings">
        <div class="ft-person">
          <div class="ft-name">Gen. dyw. Janusz Julian Głuchowski</div>
          <div class="ft-dates">1888 &ndash; 1964</div>
          <div class="ft-role">Siódemka Beliny. Twórca 7 P.Uł. I Zastępca Min. Spraw Wojskowych. D-ca PSZ w UK. Companion of the Order of the Bath (C.B.). Współzałożyciel Instytutu Piłsudskiego w Londynie.</div>
          <div class="ft-docs">Dokumenty: ARG/II/1&ndash;32</div>
        </div>
        <div class="ft-person">
          <div class="ft-name">Ppor. Stanisław Stefan Głuchowski</div>
          <div class="ft-dates">1893 &ndash; 1962</div>
          <div class="ft-role">Oficer 7 P.Uł. Jeniec Stalag XI B (Fallingbostel), nr 0.1245 / 0.1845. Żona: Zofia (Zocha), ul. Pułaskiej, Kleczew, pow. Radomsko.</div>
          <div class="ft-docs">Dokumenty: ARG/III/1&ndash;9</div>
        </div>
        <div class="ft-person ft-deceased">
          <div class="ft-name">Lech Głuchowski ps. &laquo;Jeżycki&raquo;</div>
          <div class="ft-dates">1900 &ndash; &dagger; 15.IX.1944</div>
          <div class="ft-role">Poległ w Powstaniu Warszawskim. Wspomniany w listach.</div>
          <div class="ft-docs">&mdash;</div>
        </div>
      </div>
      <div class="ft-connector">&darr; syn Stanisława Stefana</div>
      <div class="ft-generation">
        <div class="ft-person ft-protagonist">
          <div class="ft-name">St.uł. Krzysztof Andrzej Głuchowski ps. &laquo;Juras&raquo;</div>
          <div class="ft-dates">ur. 29.XI.1926, Warszawa</div>
          <div class="ft-role">AK plut. 1112. Obrona Starego Miasta. Jeniec Stalag XI B / VI/3 / VI J (nr 141009). Gimnazjum 3 DSK (matura 9.II.1946). Repatriant via Orsay. II Korpus we Włoszech.</div>
          <div class="ft-docs">Dokumenty: ARG/V/1&ndash;66 (największa seria)</div>
        </div>
      </div>
    </div>
  </div>

  <!-- IDENTYFIKACJA OSÓB TRZECICH -->
  <div class="fa-section">
    <h3 class="fa-section-title">Osoby zidentyfikowane w dokumentach</h3>
    <div class="persons-grid">

      <div class="person-card">
        <div class="pc-category">RODZINA</div>
        <div class="pc-name">Zofia (Zocha) Głuchowska</div>
        <div class="pc-desc">Żona Stanisława Stefana. Adres wojenny: ul. Pułaskiej, Kleczew, gmina Brzezówce, powiat Radomsko (GG). Później: ul. Howe-Monatkiego, Częstochowa. Adresatka kartek jenieckich ojca.</div>
        <div class="pc-docs">ARG/III/1, III/2, III/5</div>
      </div>

      <div class="person-card">
        <div class="pc-category">RODZINA</div>
        <div class="pc-name">Anna Maria</div>
        <div class="pc-desc">Krewna (ciotka?). Adres: Główno, Osiny, Łowicz. Adresatka kartki Krzysztofa ze Stalagu VI/3.</div>
        <div class="pc-docs">ARG/V/14</div>
      </div>

      <div class="person-card">
        <div class="pc-category">RODZINA</div>
        <div class="pc-name">Maria (&laquo;Cioteczka z Częstochowy&raquo;)</div>
        <div class="pc-desc">Odpowiada na kartkę Krzysztofa. Wspomina &laquo;Marusa&raquo;, &laquo;Ławkę i jej córeczkę&raquo;. Podpis: Maria. Sieć rodzinna z Częstochowy.</div>
        <div class="pc-docs">ARG/V/15</div>
      </div>

      <div class="person-card">
        <div class="pc-category">RODZINA</div>
        <div class="pc-name">Bogdana (Bogdan)</div>
        <div class="pc-desc">Wspominana w listach powojennych Krzysztofa z Düsseldorfu. Bliska osoba &mdash; wymieniana obok &laquo;Polizei&raquo; i &laquo;Warszawa&raquo;.</div>
        <div class="pc-docs">ARG/V/35, V/37</div>
      </div>

      <div class="person-card">
        <div class="pc-category">DOWÓDCY / PRZEŁOŻENI</div>
        <div class="pc-name">Płk. dypl. Karol Ziemski</div>
        <div class="pc-desc">Dowódca Grupy &laquo;Północ&raquo; w Powstaniu Warszawskim (obrona Starego Miasta, ~5000 żołnierzy). Po wojnie: D-ca Polskiego Okręgu Wojskowego Schleswig-Holstein. Wydał kluczowe zaświadczenie o udziale Krzysztofa w Powstaniu (Wentorf pod Hamburgiem, 26.X.1946).</div>
        <div class="pc-docs">ARG/V/43</div>
      </div>

      <div class="person-card">
        <div class="pc-category">DOWÓDCY / PRZEŁOŻENI</div>
        <div class="pc-name">Płk. Stanisław Kłopacz</div>
        <div class="pc-desc">Wydał dwa zaświadczenia w Hensstedt (22.VIII.1945): o nadaniu KW (Rozkaz D-cy Grupy &laquo;Północ&raquo; nr 24, z 25.9.1944) oraz o awansie na st. ułana (z 15.9.1944). Pieczęć z orłem.</div>
        <div class="pc-docs">ARG/V/42</div>
      </div>

      <div class="person-card">
        <div class="pc-category">DOWÓDCY / PRZEŁOŻENI</div>
        <div class="pc-name">Płk. Łechnowski</div>
        <div class="pc-desc">Z-ca Komendanta Okręgu Warszawskiego AK. Podpis na Przepustce Jednorazowej Specjalnej (29.IX.1944). Pieczęć: &laquo;KOMENDANTURA ARMII KRAJOWEJ Warszawa&raquo;.</div>
        <div class="pc-docs">ARG/V/7</div>
      </div>

      <div class="person-card">
        <div class="pc-category">DOWÓDCY / PRZEŁOŻENI</div>
        <div class="pc-name">Kpt. Józef Kapica</div>
        <div class="pc-desc">Komendant Gimnazjum i Liceum 3 Dywizji Karpackiej. Podpis na przepustce z Amandola.</div>
        <div class="pc-docs">ARG/V/56</div>
      </div>

      <div class="person-card">
        <div class="pc-category">DOWÓDCY / PRZEŁOŻENI</div>
        <div class="pc-name">Gen. Kazimierz Sosnkowski</div>
        <div class="pc-desc">Naczelny Wódz PSZ (1943&ndash;44), Inspektor Armii (lata 30.). Podpis na zaświadczeniu OB PPS (I.1935). List prywatny z Kanady &laquo;Kochany Januszu&raquo; (po 1960). Obaj legioniści Piłsudskiego i członkowie OB PPS 1905&ndash;08. Sosnkowski na emigracji w Arundel (Quebec) od XI.1944 do śmierci 11.X.1969.</div>
        <div class="pc-docs">ARG/II/3, II/4, II/27</div>
      </div>

      <div class="person-card">
        <div class="pc-category">DOWÓDCY / PRZEŁOŻENI</div>
        <div class="pc-name">Marsz. Edward Śmigły-Rydz</div>
        <div class="pc-desc">Naczelny Wódz II RP. Odręczny list do Głuchowskiego. Widoczny na fotokopii wręczenia sztandaru 17 P.Uł. Wielkopolskich obok gen. Głuchowskiego.</div>
        <div class="pc-docs">ARG/II/14, II/22</div>
      </div>

      <div class="person-card">
        <div class="pc-category">SIÓDEMKA BELINY</div>
        <div class="pc-name">Uczestnicy pierwszego patrolu (2.VIII.1914)</div>
        <div class="pc-desc">Podpisy na fotokopii: Władysław <strong>Belina-Prażmowski</strong> (d-ca), Janusz <strong>Głuchowski</strong>, Zygmunt <strong>Grzmot-Skotnicki</strong>, Stanisław <strong>Karnacki</strong>, Stefan Hanka <strong>Kulesza</strong>, Zdzisław <strong>Jabłoński</strong>, Antoni <strong>Bończa</strong>. Siedmiu kawalerzystów, którzy rozpoczęli kampanię Legionów.</div>
        <div class="pc-docs">ARG/II/2</div>
      </div>

      <div class="person-card">
        <div class="pc-category">DYPLOMACI</div>
        <div class="pc-name">Król Rumunii Ferdynand I</div>
        <div class="pc-desc">Podpis na dyplomie nadania Ordinul Coroanei României (Order Korony Rumuńskiej) dla Janusza Głuchowskiego. Kaligrafowany dokument, grudzień 1922. Pieczęć królewska. Kontrasygna: Ministrului Afacerilor Straine (Minister Spraw Zagranicznych).</div>
        <div class="pc-docs">ARG/II/16</div>
      </div>

      <div class="person-card">
        <div class="pc-category">PRELEGENCI PON</div>
        <div class="pc-name">Wacław Sieroszewski, Juliusz Kaden(-Bandrowski), Marjan Dąbrowski</div>
        <div class="pc-desc">Prelegenci na zebraniu PON w sali &laquo;Lutni&raquo;, 2.X.1914. Sieroszewski &mdash; pisarz i legionista. Kaden &mdash; prozaik, propagandysta Legionów. Organizator zebrania: Marjan Głuchowski.</div>
        <div class="pc-docs">ARG/I/2</div>
      </div>

      <div class="person-card">
        <div class="pc-category">KONTAKTY EMIGRACYJNE</div>
        <div class="pc-name">Henri Kołacz, Artiste-Sculpteur, Troyes</div>
        <div class="pc-desc">Polski rzeźbiarz we Francji. Wizytówka zachowana wśród dokumentów repatriacyjnych Krzysztofa. Ślad kontaktów artystycznych DP.</div>
        <div class="pc-docs">ARG/V/50</div>
      </div>

      <div class="person-card">
        <div class="pc-category">KONTAKTY EMIGRACYJNE</div>
        <div class="pc-name">Jan Lorens, plut. 7 P.Uł.</div>
        <div class="pc-desc">Żołnierz 7 Pułku Ułanów. Zmarł 29.I.1960 w Chicago. Nekrolog przechowywany w archiwum &mdash; ślad diasporowy pułku.</div>
        <div class="pc-docs">ARG/VI/9</div>
      </div>

      <div class="person-card">
        <div class="pc-category">KONTAKTY EMIGRACYJNE</div>
        <div class="pc-name">Ppor. Kucliński</div>
        <div class="pc-desc">Podpis na przepustce z Bazy Personalnej Legio 2 Korpusu (11.VI.1946).</div>
        <div class="pc-docs">ARG/V/57</div>
      </div>

    </div>
  </div>

  <!-- CHRONOLOGIA / NARRACJA -->
  <div class="fa-section">
    <h3 class="fa-section-title">Chronologia &mdash; historia rodziny w dokumentach</h3>
    <div class="timeline">

      <div class="tl-era">Rewolucja i ruch niepodległościowy (1905&ndash;1914)</div>

      <div class="tl-event">
        <div class="tl-date">1905&ndash;1908</div>
        <div class="tl-body">
          <strong>Janusz Głuchowski w Organizacji Bojowej PPS.</strong> Zaświadczenie gen. Sosnkowskiego (I.1935) potwierdza: &laquo;Głuchowski należał do organizacji bojowej P.P.S. od roku 1905 do 1908-go.&raquo; W 1909 złożył broń (rewolwer) &laquo;na szarży Miłości&raquo; &mdash; zaświadczenie Archiwum Głównego Akt Dawnych z 10.III.1925.
          <div class="tl-docs">ARG/II/3, II/5</div>
        </div>
      </div>

      <div class="tl-event">
        <div class="tl-date">2.X.1914</div>
        <div class="tl-body">
          <strong>Marian Głuchowski organizuje zebranie PON w Częstochowie.</strong> Afisz: sala &laquo;Lutni&raquo;, prelegenci Sieroszewski i Kaden. Podpis: &laquo;Komisarz PON na powiat Częstochowski &mdash; Marjan Głuchowski.&raquo; Legitymacja PON nr 2 &mdash; jest jednym z założycieli. Pokwitowanie na 2 szable i 200 kop.
          <div class="tl-docs">ARG/I/1, I/2, I/3, I/4</div>
        </div>
      </div>

      <div class="tl-era">Legiony i niepodległość (1914&ndash;1920)</div>

      <div class="tl-event">
        <div class="tl-date">2&ndash;3.VIII.1914</div>
        <div class="tl-body">
          <strong>&laquo;Siódemka Beliny&raquo; &mdash; pierwszy patrol kawalerii odrodzonej.</strong> Janusz Głuchowski jako jeden z siedmiu kawalerzystów pod dowództwem Władysława Beliny-Prażmowskiego przekracza granicę rosyjską. Fotokopia z podpisami wszystkich siedmiu: Belina-Prażmowski, Głuchowski, Grzmot-Skotnicki, Karnacki, Hanka Kulesza, Jabłoński, Bończa. Biogram WBH nr 76/45 (24.V.1937) potwierdza: &laquo;patrol kawaleryjski 2.VIII.1914 do Krakowa i na Kielce, ZS Oleandry.&raquo;
          <div class="tl-docs">ARG/II/1, II/2</div>
        </div>
      </div>

      <div class="tl-event">
        <div class="tl-date">5.XI.1918</div>
        <div class="tl-body">
          <strong>Rozkaz utworzenia 7 Pułku Ułanów.</strong> Sztab Generalny, Lublin: &laquo;Rotmistrzowi Januszowi Głuchowskiemu nakazuje się organizować nowo-oddzielony oddział jazdy w Lubelskiem.&raquo; Podpis nieczytelny. Sześć dni przed odzyskaniem niepodległości &mdash; akt założycielski pułku, który stanie się legendą.
          <div class="tl-docs">ARG/II/8</div>
        </div>
      </div>

      <div class="tl-era">Kariera wojskowa i ministerialna (1920&ndash;1939)</div>

      <div class="tl-event">
        <div class="tl-date">31.VII.1922</div>
        <div class="tl-body">
          <strong>Krzyż Walecznych.</strong> Legitymacja nr 42888: &laquo;Rtm. Głuchowski Janusz, oddział 7 P.Uł., uprawniony do noszenia Krzyża Walecznych, Krzyż z 1 okuciem.&raquo; Rozkazem Nr 12793/22. Podpis Ministra Spraw Wojskowych. Za wojnę 1920.
          <div class="tl-docs">ARG/II/13</div>
        </div>
      </div>

      <div class="tl-event">
        <div class="tl-date">XII.1922</div>
        <div class="tl-body">
          <strong>Order Korony Rumuńskiej.</strong> Dyplom podpisany osobiście przez króla Ferdynanda I. Kaligrafowany po rumuńsku, pieczęć królewska. Nadanie za zasługi dyplomatyczne lub sojusz polsko-rumuński.
          <div class="tl-docs">ARG/II/16</div>
        </div>
      </div>

      <div class="tl-event">
        <div class="tl-date">26.III.1933</div>
        <div class="tl-body">
          <strong>Mianowanie na generała brygady.</strong> Akt: &laquo;Gen. bryg. Głuchowski Janusz &mdash; dowódca Okręgu Korpusu.&raquo; Podpisy Prezydenta RP i Ministra Spraw Wojskowych.
          <div class="tl-docs">ARG/II/18</div>
        </div>
      </div>

      <div class="tl-event">
        <div class="tl-date">5.X.1935</div>
        <div class="tl-body">
          <strong>I Wiceminister Spraw Wojskowych.</strong> Szczyt kariery. Akt mianowania z pieczęcią Ministerstwa. Głuchowski jest teraz drugą osobą w resorcie obrony II RP.
          <div class="tl-docs">ARG/II/19</div>
        </div>
      </div>

      <div class="tl-era">Okupacja i Powstanie Warszawskie (1939&ndash;1944)</div>

      <div class="tl-event">
        <div class="tl-date">9.XI.1943</div>
        <div class="tl-body">
          <strong>Kennkarte Krzysztofa.</strong> Karta rozpoznawcza GG wystawiona w Warszawie. Na zdjęciu &mdash; 17-letni chłopak, ulica Pogonowskiego. Jawny mieszkaniec Generalnego Gubernatorstwa, tajny żołnierz AK. Pieczęć: &laquo;Distriktchef Warschau&raquo;.
          <div class="tl-docs">ARG/V/1, V/2</div>
        </div>
      </div>

      <div class="tl-event">
        <div class="tl-date">8.IV.1944</div>
        <div class="tl-body">
          <strong>Legitymacja AK.</strong> &laquo;Krzysztof Głuchowski, ps. Juras, Pluton nr 1112.&raquo; Ur. 29.XI.1926. Cztery miesiące przed Powstaniem. Pluton 1112 wchodzi w skład 7 P.Uł. AK &laquo;Jeleń&raquo;.
          <div class="tl-docs">ARG/V/3, V/4</div>
        </div>
      </div>

      <div class="tl-event tl-highlight">
        <div class="tl-date">26.VIII.1944</div>
        <div class="tl-body">
          <strong>&laquo;Kochana Maminko i Tatusiu...&raquo;</strong> List z Powstania Warszawskiego. 18-latek pisze do rodziców ołówkiem na papierze w kratkę, 26 dni po wybuchu. Podpis: &laquo;Krzysztof&raquo;. Na osobnej kartce, datowanej &laquo;26/IX&raquo;: &laquo;Krychu! Krysicy jesteśmy... Nasze działania... Bardzo serdecznie... mamusi, panny Stachyi... Ciotka&raquo; &mdash; list od kogoś z oddziału do Krzysztofa.
          <div class="tl-docs">ARG/V/5, V/6</div>
        </div>
      </div>

      <div class="tl-event tl-highlight">
        <div class="tl-date">15.IX.1944</div>
        <div class="tl-body">
          <strong>Lech Głuchowski ps. &laquo;Jeżycki&raquo; ginie w Powstaniu.</strong> Brat Stanisława Stefana, stryj Krzysztofa. Krzysztof wspomina go w relacji z obozu: &laquo;Babcię i Stryja Lecha w dniu 29.IX.44 na Mokotowie...&raquo; W eseju szkolnym (3.VIII.1945) pisze o &laquo;Domu Głuchowskiego&raquo;, który został zaangażowany w walkę.
          <div class="tl-docs">Wspomniany w: ARG/V/21, V/36</div>
        </div>
      </div>

      <div class="tl-event">
        <div class="tl-date">29.IX.1944</div>
        <div class="tl-body">
          <strong>Ostatnie dokumenty Powstania.</strong> Przepustka Jednorazowa Specjalna AK &mdash; pieczęć &laquo;KOMENDANTURA ARMII KRAJOWEJ Warszawa&raquo;, podpis płk. Łechnowskiego. Na przepustce: &laquo;Zezwalam na przejście przez A. Sikorskiego z (...) obwód, oraz z powrotem obyw. st.uł. Juras&raquo;, ważna do 30.IX.44. Tego samego dnia: Rozkaz D-cy Grupy &laquo;Północ&raquo; nr 24 &mdash; awans na st. ułana i Krzyż Walecznych po raz I. Trzy dni przed kapitulacją (2.X.1944).
          <div class="tl-docs">ARG/V/7, V/8</div>
        </div>
      </div>

      <div class="tl-era">Niewola &mdash; ojciec i syn w obozach (X.1944 &ndash; IV.1945)</div>

      <div class="tl-event tl-highlight">
        <div class="tl-date">14.X.1944</div>
        <div class="tl-body">
          <strong>&laquo;Droga Zocha! Jestem w oflagu, Krzysztof w Stalagu...&raquo;</strong> Pierwsza kartka Stanisława Stefana z M.-Stammlager XI B (Fallingbostel). Nr jeniecki: 0.1245. Pisze do żony Zofii w Kleczewie. Wie, że syn Krzysztof (nr 141009) jest w innym obozie. Adresat: ul. Pułaskiej, Kleczew, gmina Brzezówce, powiat Radomsko, Generalgouvernement. Stempel: 20.10.44.
          <div class="tl-docs">ARG/III/1, III/2</div>
        </div>
      </div>

      <div class="tl-event tl-highlight">
        <div class="tl-date">X&ndash;XI.1944</div>
        <div class="tl-body">
          <strong>Korespondencja między dwoma jeńcami &mdash; ojciec i syn.</strong> Rückantwortbrief: Ppor. Stefan Głuchowski (nr 0.1845, Stalag XI B) pisze do St.Uł. Krzysztofa Głuchowskiego (nr 141009, Stalag VI/3, Dorsten). Pieczęć cenzury &laquo;15 Geprüft Stalag XI B&raquo;. Rewers: &laquo;Mama na ul. Howe-Monatkiego w Częstochowie...&raquo; Podpis &laquo;Stefek&raquo;. Krzysztof odpisuje: koperta ze stemplem &laquo;27 Geprüft Stalag XI B&raquo;, 7.11.44.
          <div class="tl-docs">ARG/III/3, III/4, V/19</div>
        </div>
      </div>

      <div class="tl-event">
        <div class="tl-date">X.1944</div>
        <div class="tl-body">
          <strong>Kartka z obozu do stryja-generała w Londynie.</strong> Adres: &laquo;GENERAL JANUSZ GŁUCHOWSKI, London, Polish War&rsquo;s Office, ENGLAND.&raquo; Nadawca: St.Uł. Krzysztof Głuchowski, nr 141009, M.-Stammlager XI B. Stempel brytyjskiej cenzury: &laquo;PASSED XII&raquo;. Trzy języki na jednej kartce: niemiecki formularz, angielski adres, polskie pismo.
          <div class="tl-docs">ARG/V/17</div>
        </div>
      </div>

      <div class="tl-event">
        <div class="tl-date">1944&ndash;1945</div>
        <div class="tl-body">
          <strong>Pamiętnik obozowy Krzysztofa.</strong> Pisany na skrawkach papieru, w kratkę, na formularzach egzaminu kupieckiego (Kaufmannsgehilfenprüfung) z Gladbach-Rheydt-Neuss &mdash; typowy recykling w obozie. Obejmuje: wspomnienia z dzieciństwa (&laquo;Dzieciństwo moje to szczęśliwe...&raquo;), relację z Powstania (&laquo;Gestapo przy 41 branka, 508 strat, gen. Bora Komorowskiego...&raquo;), mapkę taktyczną Wołomina, szkic obozów, i notatki powojenne (22.VIII.1945: &laquo;Obecnie jestem już...&raquo;). Mapa przerzutów: Stalag XI B &rarr; VI/3 (Dorsten) &rarr; VI J &rarr; VI/17.
          <div class="tl-docs">ARG/V/21&ndash;33</div>
        </div>
      </div>

      <div class="tl-era">Wyzwolenie i repatriacja (IV&ndash;IX.1945)</div>

      <div class="tl-event">
        <div class="tl-date">27.IV.1945</div>
        <div class="tl-body">
          <strong>Card of Identity &mdash; pierwszy dokument wolności.</strong> Düsseldorf: &laquo;P.f.c. Głuchowski Krzysztof is a polish soldier liberated by Allied forces from german captivity.&raquo; Podpis: Rudnicki (?), &laquo;pol. off.-in-ch. in tr. cp.&raquo; (polski oficer odpowiedzialny w punkcie tranzytowym).
          <div class="tl-docs">ARG/V/40</div>
        </div>
      </div>

      <div class="tl-event tl-highlight">
        <div class="tl-date">2.VI.1945</div>
        <div class="tl-body">
          <strong>&laquo;Kochajni Ciociu i Stryju!&raquo;</strong> List Krzysztofa z Düsseldorfu do gen. Janusza i ciotki &mdash; KLUCZOWA RELACJA. &laquo;Jestem obecnie w Düsseldorfie. Oswobodzony z niewoli 24/V przez Amerykanów. Ale numer!&raquo; Kontynuuje: &laquo;Początkowo byłem w konspiracji... Ciotka Halinka... w akcji 4.27.VIII.1943 została... V.S.O.P.ie... dent[ysta]... pod dowództwem... kompanie z Volks-Deutsche... poszli d[o] powstania dnia 2 Dyp[?]... plutonie 1112 Dyoniz... Bora Komorowskiego... kapitulacja 2.IX.44.&raquo; Wspomina Lecha: &laquo;Babcię. A Stryj Lech w dniu 29.IX.44 na Mokotowie...&raquo;
          <div class="tl-docs">ARG/V/36</div>
        </div>
      </div>

      <div class="tl-event">
        <div class="tl-date">27.VI.1945</div>
        <div class="tl-body">
          <strong>Carte de Rapatrié &mdash; Centrum Orsay, Paryż.</strong> Nr 1492839. République Française, Ministère des Prisonniers, Déportés et Réfugiés. Dane: Głuchowski Krzysztof, Pologne, célibataire (kawaler), ojciec: Stanisław. Orsay &mdash; obecne Musée d&rsquo;Orsay służyło jako punkt repatriacji.
          <div class="tl-docs">ARG/V/46, V/47</div>
        </div>
      </div>

      <div class="tl-event">
        <div class="tl-date">29.VI.1945</div>
        <div class="tl-body">
          <strong>Ambasada RP w Paryżu kieruje na kurs w Villard-de-Lans.</strong> &laquo;Pan Głuchowski K. zostanie skierowany (...) na kurs, który rozpocznie się w dniu 25 Lipca b.r. w Villard-de-Lans.&raquo; Alpejska miejscowość &mdash; ośrodek rekonwalescencji.
          <div class="tl-docs">ARG/V/48</div>
        </div>
      </div>

      <div class="tl-era">Gimnazjum 3 DSK i II Korpus (1945&ndash;1946)</div>

      <div class="tl-event tl-highlight">
        <div class="tl-date">1.VIII.1945, godz. 15:00</div>
        <div class="tl-body">
          <strong>Esej o rocznicy Powstania &mdash; dokładnie rok po wybuchu.</strong> &laquo;St.uł. Krzysztof Głuchowski, Polish Forces C.M.F. 152, Gimnazjum.&raquo; Pisze o &laquo;kolosalnej sile moralnej&raquo; i gen. Borze Komorowskim. Dwa dni później (3.VIII) &mdash; esej o artykułach stryja, gen. Janusza Głuchowskiego, o Powstaniu: &laquo;Czytam artykuły... są to artykuły p. Głuchowskiego... były wydawane pracu pokojowe...&raquo; Uczeń pisze esej o artykułach generała, który jest jego stryjem, o powstaniu, w którym sam walczył.
          <div class="tl-docs">ARG/V/60, V/61</div>
        </div>
      </div>

      <div class="tl-event">
        <div class="tl-date">9.II.1946</div>
        <div class="tl-body">
          <strong>Matura.</strong> Świadectwo Ukończenia Gimnazjum Ogólnokształcącego Nr 13. MWRiOP. &laquo;Krzysztof Andrzej Głuchowski, urodzony dnia 29 listopada roku 1926, w Warszawie, województwa Warszawa, religii rzymsko-katolickiej, złożył egzamin maturalny w dniu 9 Lutego 1946.&raquo; Na zdjęciu &mdash; 20-latek w mundurze ze stopniem st. ułana. Delegat V.R. i O.P. Zeszyt: &laquo;EXERCISE BOOK &mdash; Supplied for use in NAVAL &amp; MILITARY SCHOOLS by His Majesty&rsquo;s Stationery Office.&raquo;
          <div class="tl-docs">ARG/V/65, V/58</div>
        </div>
      </div>

      <div class="tl-era">Epilog (1946&ndash;1964)</div>

      <div class="tl-event">
        <div class="tl-date">26.X.1946</div>
        <div class="tl-body">
          <strong>Zaświadczenie płk. Ziemskiego.</strong> Wentorf pod Hamburgiem. &laquo;Jako b. Dowódca Grupy PÓŁNOC w Powstaniu Warszawskim zaświadczam, że GŁUCHOWSKI Krzysztof, ur. 1928, pseudonim Juras, walczył w Obronie Starego Miasta w Plutonie 1112, awansowany do stopnia starszego strzelca, oraz odznaczony KRZYŻEM WALECZNYCH.&raquo; Pieczęć: Komisja Likwidacyjna Żołnierzy Armii Krajowej.
          <div class="tl-docs">ARG/V/43</div>
        </div>
      </div>

      <div class="tl-event">
        <div class="tl-date">1958</div>
        <div class="tl-body">
          <strong>Korespondencja z Ambasadą Izraela o monetach getta łódzkiego.</strong> Krzysztof pisze w sprawie sprzedaży bonów i talonów z getta Litzmannstadt. Ambasada odsyła do Yad Vashem. W kolekcji: bon 10 Pfennig, talon na produkty mleczne.
          <div class="tl-docs">ARG/VI/10, VI/11, VI/12</div>
        </div>
      </div>

      <div class="tl-event">
        <div class="tl-date">1960&ndash;1964</div>
        <div class="tl-body">
          <strong>Ostatnie ślady.</strong> Nekrolog Jana Lorensa (7 P.Uł.) w Chicago, 1960. Maszynopis Janusza o obchodach 50-lecia Legionów. List z emigracji londyńskiej, ok. 1964. Głuchowski zmarł 11.VI.1964 w Londynie, pochowany Brompton Cemetery (#576).
          <div class="tl-docs">ARG/VI/9, II/28&ndash;29, II/27</div>
        </div>
      </div>

    </div>
  </div>

  <!-- MAPA POŁĄCZEŃ -->
  <div class="fa-section">
    <h3 class="fa-section-title">Mapa połączeń &mdash; kto pisze do kogo</h3>
    <div class="connections-grid">
      <div class="conn-item">
        <div class="conn-arrow">Krzysztof &rarr; Zofia (matka)</div>
        <div class="conn-detail">Kartki z obozu do Kleczewa/Częstochowy</div>
      </div>
      <div class="conn-item">
        <div class="conn-arrow">Stefan (ojciec) &rarr; Zofia (żona)</div>
        <div class="conn-detail">Kriegsgefangenenpost z Stalagu XI B do Kleczewa</div>
      </div>
      <div class="conn-item">
        <div class="conn-arrow">Stefan &harr; Krzysztof</div>
        <div class="conn-detail">Korespondencja między obozami! Ojciec (XI B) &harr; syn (VI/3 Dorsten)</div>
      </div>
      <div class="conn-item">
        <div class="conn-arrow">Krzysztof &rarr; Gen. Janusz (stryj, Londyn)</div>
        <div class="conn-detail">Kartka do Polish War&rsquo;s Office, England. Stempel PASSED XII</div>
      </div>
      <div class="conn-item">
        <div class="conn-arrow">Krzysztof &rarr; Anna Maria (ciotka, Łowicz)</div>
        <div class="conn-detail">Antwort-Postkarte ze Stalagu VI/3</div>
      </div>
      <div class="conn-item">
        <div class="conn-arrow">Maria (Częstochowa) &rarr; Krzysztof</div>
        <div class="conn-detail">Odpowiedź od &laquo;Cioteczki z Częstochowy&raquo;</div>
      </div>
      <div class="conn-item">
        <div class="conn-arrow">Krzysztof &rarr; Gen. Janusz + ciotka</div>
        <div class="conn-detail">List z Düsseldorfu 2.VI.1945 &mdash; kluczowa relacja z Powstania</div>
      </div>
      <div class="conn-item">
        <div class="conn-arrow">Kolega z oddziału &rarr; Krzysztof</div>
        <div class="conn-detail">&laquo;Krychu! Krysiey jesteśmy...&raquo; &mdash; list z walk</div>
      </div>
      <div class="conn-item">
        <div class="conn-arrow">Śmigły-Rydz &rarr; Gen. Janusz</div>
        <div class="conn-detail">Odręczny list Marszałka do Głuchowskiego</div>
      </div>
      <div class="conn-item">
        <div class="conn-arrow">Sosnkowski &rarr; Gen. Janusz</div>
        <div class="conn-detail">Zaświadczenie OB PPS (I.1935) + list na papierze Inspektoratu + list prywatny z Kanady &laquo;Kochany Januszu&raquo; (po 1960)</div>
      </div>
    </div>
  </div>

</div>

<!-- ============================================================ -->
<!-- BIOGRAFIA                                                      -->
<!-- ============================================================ -->
<div class="bio-section" id="biografia">
  <h2 class="bio-main-title">Biografia rodziny Gluchowskich</h2>
  <p class="bio-subtitle">Piec losow w jednym Powstaniu &mdash; saga oparta na dokumentach z kolekcji prywatnej i relacji Archiwum Historii Mowionej</p>

  <div class="bio-chapter" onclick="this.classList.toggle('open')">
    <div class="bio-chapter-title">&#9654; Prolog: Patriarcha z Bukowej</div>
    <div class="bio-chapter-date">1862 &mdash; 1924</div>
    <div class="bio-chapter-body">
      <p>Wszystko zaczyna sie w majatku Bukowa pod Piotrkowem Trybunalskim, gdzie Marian Nepomucen Gluchowski herbu Prus II wychowuje synow na Polakow &mdash; w kraju, ktorego na mapie nie ma.</p>
      <p>Marian Gluchowski urodzil sie w 1862 roku w Sycanowie, w regionie sieradzkim. Byl aktywista PPS, pracownikiem samorzadowym, naczelnikiem wydzialu. Z zona Maria z Ziolkowskich mial trzech synow: Janusza, Stefana i Lecha. Wszyscy trzej pojda do wojska. Dwoch przezyje. Jeden odbierze sobie zycie na barykadzie, zeby nie narazac swoich zolnierzy.</p>
      <p>Marian zmarl 20 czerwca 1924 roku w Warszawie. Pochowan na Powazkach.</p>
      <p><strong>Pieciu czlonkow rodziny walczylo w Powstaniu Warszawskim:</strong> gen. dyw. Janusz Julian Gluchowski (1888-1964), ppor. Stanislaw Stefan Gluchowski (1893-1962), sierz. pchor. Wanda Bronislawa Gluchowska &bdquo;Justyna&rdquo; (1901-1976), rtm. Lech Jerzy Gluchowski &bdquo;Jezycki&rdquo; (1902-1944), st.ul. Krzysztof Gluchowski &bdquo;Juras&rdquo; (1926-2020).</p>
    </div>
  </div>

  <div class="bio-chapter" onclick="this.classList.toggle('open')">
    <div class="bio-chapter-title">&#9654; I. Chlopiec z Lazienek</div>
    <div class="bio-chapter-date">1926 &mdash; 1939</div>
    <div class="bio-chapter-body">
      <p>Krzysztof Gluchowski przychodzi na swiat 29 listopada 1926 roku w Warszawie. Jego ojciec Stefan jest kierownikiem referatu w Kancelarii Cywilnej Prezydenta Rzeczypospolitej. Matka Wanda &mdash; magistra farmacji z Uniwersytetu Jana Kazimierza we Lwowie.</p>
      <p>Mieszkaja w budynku przy bramie Lazienek Krolewskich, tej wychodzacej na Agrykole i ulice Szwolezerow. Krzysztof dorasta w cieniu Palacu Na Wodzie.</p>
      <div class="bio-quote">&bdquo;To byla wspaniala szkola. Przez szesc lat mielismy tego samego wychowawce-opiekuna naszej klasy. Wiekszosc tych, ktorzy zaczeli od poczatku, ukonczylo szkole.&rdquo;<span class="source">&mdash; Krzysztof Gluchowski, relacja AHM, 31.VII.2009</span></div>
      <p>W 1935 roku umiera Marszalek Pilsudski. Krzysztof ma dziewiec lat.</p>
      <div class="bio-quote">&bdquo;Mama przyszla zaplacana i powiedziala: 'Co teraz bedzie z Polska?!'&rdquo;<span class="source">&mdash; Krzysztof Gluchowski, relacja AHM</span></div>
      <p>Latem 1939 mobilizacja zastaje go z ojcem w Wilnie. 1 wrzesnia 1939 &mdash; wojna. Pierwszy nalot trzynastoletni Krzysztof ogladaz tarasu Palacu Na Wodzie. Sluzy jako goniec LOPP.</p>
    </div>
  </div>

  <div class="bio-chapter" onclick="this.classList.toggle('open')">
    <div class="bio-chapter-title">&#9654; II. Czternastoletni zolnierz</div>
    <div class="bio-chapter-date">1941 &mdash; 1943</div>
    <div class="bio-chapter-body">
      <p>W sierpniu 1941 roku Julek Klepacz &mdash; starszy o cztery lata kolega, kadet &mdash; przychodzi do Krzysztofa z propozycja wciagniecia do konspiracji.</p>
      <div class="bio-quote">&bdquo;Od teraz na przyszlosc wciagam was do konspiracji i bedziecie zolnierzami Rzeczpospolitej. Zdrada bedzie karana smiercia.&rdquo;<span class="source">&mdash; Julek Klepacz, sierpien 1941</span></div>
      <p>Formalna przysiega AK &mdash; <strong>11 maja 1942 roku</strong>. Krzysztof ma pietnascie lat. Wykonuje mapy operacyjne, rysunki techniczne broni, zbiera informacje wywiadowcze o gestapowcu Kempfie.</p>
      <p>We wrzesniu 1943 przechodzi do <strong>plutonu 1112</strong> przy 7 Pulku Ulanow Lubelskich AK, dywizjon &bdquo;Jelen&rdquo;. Dowodca dywizjonu &mdash; jego wuj, rotmistrz Lech Gluchowski ps. &bdquo;Jezycki&rdquo;.</p>
    </div>
  </div>

  <div class="bio-chapter" onclick="this.classList.toggle('open')">
    <div class="bio-chapter-title">&#9654; III. Akcja Wilanow &mdash; matka i syn</div>
    <div class="bio-chapter-date">26 wrzesnia 1943</div>
    <div class="bio-chapter-body">
      <p>Wanda Gluchowska jest sekcyjna w oddziale DYSK &mdash; Dywersja i Sabotaz Kobiet, jedynym kobiecym oddziale specjalnym Kedywu. Operacja 26 wrzesnia 1943 pod Wilanowem.</p>
      <p>Wanda zostaje postrzelona w noge. Wpada do rowu z granatami. Po odzyskaniu przytomnosci pelznie do okna babki Krzysztofa.</p>
      <div class="bio-quote">&bdquo;Sluchaj Krzysztof, tutaj jest moj pistolet i musisz go schowac.&rdquo;<span class="source">&mdash; Wanda Gluchowska do syna, po akcji Wilanow</span></div>
      <p>Krzysztof ukrywa pistolet matki w prawej wiezy palacu wilanowskiego. Za akcje Wilanow Wanda otrzyma Krzyz Walecznych &mdash; 11 listopada 1943.</p>
    </div>
  </div>

  <div class="bio-chapter" onclick="this.classList.toggle('open')">
    <div class="bio-chapter-title">&#9654; IV. Fabryka Kamlera &mdash; serce Powstania</div>
    <div class="bio-chapter-date">31 lipca &mdash; 6 sierpnia 1944</div>
    <div class="bio-chapter-body">
      <p>Poniedzialek, 31 lipca &mdash; Krzysztof wychodzi z domu na Pogonowskiego 9 na Zoliborzu z karabinem pod plaszczem. Nie wroci juz nigdy. Maszeruje do Fabryki Kamlera na Dzielnej 72 &mdash; siedziby Komendy Glownej AK.</p>
      <p><strong>1 sierpnia 1944, godzina &bdquo;W&rdquo;.</strong> Krzysztof stoi na warcie przy bramie nr 64 od Dzielnej. Wymiana strzalow. General Pelczynski, Szef Sztabu AK, doradza jak rzucac granaty.</p>
      <p>6 sierpnia &mdash; rozkaz ewakuacji. Trasa przez bylego getto, obok Pawiaka. Na Starowke.</p>
    </div>
  </div>

  <div class="bio-chapter" onclick="this.classList.toggle('open')">
    <div class="bio-chapter-title">&#9654; V. Starowka &mdash; barykady i kanaly</div>
    <div class="bio-chapter-date">6 sierpnia &mdash; 1 wrzesnia 1944</div>
    <div class="bio-chapter-body">
      <p>Szkola na Barokowej staje sie domem plutonu. 13 sierpnia &mdash; pocisk artyleryjski na placu Krasinskich. Porucznik Jerzy Kamler &bdquo;Stolarz&rdquo; ginie na miejscu.</p>
      <p>Pluton obsadza barykade przy Katedrze. Dwie barykady na Kanonii.</p>
      <p><strong>1 wrzesnia 1944</strong> &mdash; rozkaz ewakuacji kanalami. Okolo 4500 powstancow wchodzi w scieki ze Starowki.</p>
      <p><strong>15 wrzesnia</strong> &mdash; wuj Lech, dowodca dywizjonu &bdquo;Jelen&rdquo;, zostaje ciezko ranny na ulicy Dolnej na Sadybie. Odmawia ewakuacji &mdash; odbiera sobie zycie. Z 233 zolnierzy: 125 zabitych, 98 rannych. Straty: 95,7%.</p>
      <p><strong>2 pazdziernika 1944</strong> &mdash; kapitulacja Powstania.</p>
    </div>
  </div>

  <div class="bio-chapter" onclick="this.classList.toggle('open')">
    <div class="bio-chapter-title">&#9654; VI. Stalag XI-B</div>
    <div class="bio-chapter-date">pazdziernik 1944 &mdash; kwiecien 1945</div>
    <div class="bio-chapter-body">
      <p>7 pazdziernika 1944 &mdash; transport: 80 osob w bydlecym wagonie, dwa dni bez jedzenia i wody. Cel: Stalag XI-B Fallingbostel. Numer jeniecki Krzysztofa: 141009. Trafia do tego samego obozu co ojciec Stefan.</p>
      <p>Ponad 1100 chlopcow w wieku 11-18 lat walczylo w Powstaniu. 600 niepelnoletnich trafia do obozow.</p>
      <p><strong>16 kwietnia 1945</strong> &mdash; Stalag XI-B wyzwolony przez Brytyjczykow.</p>
    </div>
  </div>

  <div class="bio-chapter" onclick="this.classList.toggle('open')">
    <div class="bio-chapter-title">&#9654; VII. Od La Courtine do Rio</div>
    <div class="bio-chapter-date">1945 &mdash; 2020</div>
    <div class="bio-chapter-body">
      <p>Krzysztof konczy gimnazjum i liceum przy 3 Dywizji Strzelcow Karpackich. Potem La Courtine, Anglia i PKPR. Zdobywa dyplom Chartered Engineer. Pracuje w firmie CAV-Lucas &mdash; Anglia, Hiszpania, od 1974 Brazylia. Od 1988 na emeryturze w Rio de Janeiro.</p>
      <p>W 2006-2007 organizuje wystawy o Powstaniu Warszawskim w Rio de Janeiro. 31 lipca 2009 &mdash; sklada relacje w Archiwum Historii Mowionej MPW. 19 listopada 2011 &mdash; Krzyz Oficerski Orderu Odrodzenia Polski.</p>
      <p>Krzysztof Gluchowski ps. &bdquo;Juras&rdquo; zmarl <strong>16 maja 2020</strong> w Brazylii. Mial dziewiecdziesiat trzy lata. Ostatni z pieciu Gluchowskich, ktorzy walczyli w Powstaniu.</p>
    </div>
  </div>

  <div class="bio-chapter" onclick="this.classList.toggle('open')">
    <div class="bio-chapter-title">&#9654; Epilog: Drzewo, ktore nie padlo</div>
    <div class="bio-chapter-body">
      <p>Piec czlonkow jednej rodziny w Powstaniu Warszawskim. General, urzednik prezydenta, farmaceutka-dywersantka, rotmistrz i chlopiec-wartownik. Trzy pokolenia. Jeden herb: Prus II.</p>
      <p>Lech zginal na Sadybie, wrzesien 1944. Stefan wrocil z niewoli do PRL-u, 1947 &mdash; zmarl w Warszawie, 1962. Wanda prowadzilaapteke do emerytury mimo 30% inwalidztwa &mdash; zmarlw 1976. Janusz zalozyl Instytut Pilsudskiego w Londynie i zmarl w 1964. Krzysztof dotarl najdalej &mdash; do Rio de Janeiro &mdash; i zyl najdluzej.</p>
      <p>W Instytucie Pilsudskiego w Londynie lezy <strong>Zespol nr 70: Archiwum Janusza Gluchowskiego</strong> &mdash; lustrzane odbicie tej kolekcji.</p>
      <p>A na Powazkach, w kwaterze 99, leza obok siebie: Lech (I-27), Wanda (IV-19) i Stefan. Rodzina znow razem.</p>
    </div>
  </div>
</div>

<!-- ============================================================ -->
<!-- OPRACOWANIA BADAWCZE                                           -->
<!-- ============================================================ -->
<div class="bio-section" id="research">
  <h2 class="bio-main-title">Opracowania badawcze</h2>
  <p class="bio-subtitle">Trzy artykuly naukowe oparte na dokumentach z Archiwum Rodziny Gluchowskich</p>

  <div class="research-article" onclick="this.classList.toggle('open')">
    <div class="research-article-title">&#9654; Piec losow w jednym Powstaniu: rodzina Gluchowskich w dokumentach kolekcji prywatnej</div>
    <div class="research-article-meta">Studia zrodloznawcze &bull; Artykul badawczy &bull; 2026 &bull; Zrodla: ARG (123 dok.), AHM MPW sygn. 1889, Instytut Pilsudskiego (Zesp. 70, 154)</div>
    <div class="research-article-body">
      <p>Analiza zrodloznawcza kolekcji 123 dokumentow archiwalnych dotyczacych rodziny Gluchowskich &mdash; od generala dywizji Janusza Juliana Gluchowskiego, jednego z legendarnej Siodemki Beliny (1914), przez jego brata Stefana, urzednika Kancelarii Cywilnej Prezydenta RP, az po bratanka Krzysztofa, siedemnastoletniego powstanca warszawskiego.</p>
      <p>Kolekcja obejmuje dokumenty wojskowe, korespondencje, swiadectwa, zaswiadczenia konspiracyjne i fotografie z lat 1914&ndash;1995 w siedmiu jezykach. Jej wartosc badawcza polega na unikalnym przekroju przez cztery kluczowe momenty polskiej historii XX wieku: odzyskanie niepodleglosci (1914&ndash;1918), II Rzeczpospolita (1918&ndash;1939), Powstanie Warszawskie (1944) i emigracja wojenna (1945&ndash;1995).</p>
      <p>Artykul analizuje strukture zbiorow, identyfikuje osoby i instytucje, rekonstruuje sieci korespondencji miedzy obozami jenieckimi oraz dokumentuje zjawisko konspiracyjnego falszowania dat urodzenia.</p>
    </div>
  </div>

  <div class="research-article" onclick="this.classList.toggle('open')">
    <div class="research-article-title">&#9654; Dywizjon &bdquo;Jelen&rdquo;: regularne wojsko polskie w Powstaniu Warszawskim</div>
    <div class="research-article-meta">Przeglad Historyczno-Wojskowy &bull; Artykul badawczy &bull; 2026 &bull; Zrodla: ARG (123 dok.), 1944.pl, AHM MPW sygn. 1889</div>
    <div class="research-article-body">
      <p>7 Pulk Ulanow Lubelskich AK (kryptonim &bdquo;Jelen&rdquo;) &mdash; jednostka ze stuletnia tradycja, dowodzona przez zawodowych oficerow-weteranow z 1920 roku. Pulk zostal stworzony w 1918 roku przez rotmistrza Janusza Gluchowskiego; w 1944 dowodzil nim rotmistrz Lech Gluchowski (brat Janusza); walczyl w nim siedemnastoletni Krzysztof Gluchowski (syn trzeciego brata, Stefana).</p>
      <p>Z 233 zolnierzy Dywizjonu poleglo 125, a 98 zostalo rannych &mdash; straty wyniosly <strong>95,7%</strong>. Dowodca, rotmistrz Lech Gluchowski, odebral sobie zycie na Sadybie, gdy zostal ciezko ranny i odmowil narazania zolnierzy na ewakuacje pod ogniem.</p>
      <p>Artykul dekonstruuje mit o &bdquo;powstaniu cywilnym&rdquo; i analizuje zjawisko podziemnej odbudowy przedwojennych pulkow w Armii Krajowej. Trzy pokolenia jednej rodziny w jednym pulku: dziadek tworca, wuj dowodca, bratanek zolnierz.</p>
    </div>
  </div>

  <div class="research-article" onclick="this.classList.toggle('open')">
    <div class="research-article-title">&#9654; Chlopiec-powstaniec: droga Krzysztofa Gluchowskiego od Fabryki Kamlera do Stalagu XI-B</div>
    <div class="research-article-meta">Biuletyn IPN &bull; Artykul biograficzny &bull; 2026 &bull; Zrodla: AHM MPW sygn. 1889, ARG (123 dok.), biogramy 1944.pl</div>
    <div class="research-article-body">
      <p>Rekonstrukcja pelnego szlaku bojowego Krzysztofa Gluchowskiego ps. &bdquo;Juras&rdquo; (1926&ndash;2020) &mdash; jednego z ponad 1100 chlopcow w wieku 11&ndash;18 lat walczacych w Powstaniu Warszawskim.</p>
      <p>Na podstawie wielogodzinnej relacji mowionej (AHM MPW, sygn. 1889, 31.VII.2009) oraz 92 dokumentow z kolekcji prywatnej odtworzono chronologie sluzby: od zaprzysiezzenia w AK w wieku pietnastu lat (11.V.1942), przez Akcje Wilanow (IX.1943), walki na Woli, Starym Miescie i w Srodmiesciu (VIII&ndash;IX.1944), ewakuacje kanalami (1.IX.1944), schwytanie przez Niemcow (~29.IX.1944), niewole w Stalagu XI-B Fallingbostel, az po wyzwolenie i emigracje.</p>
      <p>Szczegolna uwage poswiecono zjawisku konspiracyjnego falszowania dat urodzenia, udokumentowanemu w trzech wariantach (1926, 1920, 1910) w zachowanych dokumentach.</p>
    </div>
  </div>
</div>

<!-- ============================================================ -->
<!-- ARCHIWUM HISTORII MOWIONEJ                                     -->
<!-- ============================================================ -->
<div class="bio-section" id="oral-history">
  <h2 class="bio-main-title">Archiwum Historii Mowionej</h2>
  <p class="bio-subtitle">Relacja zrodlowa &mdash; Muzeum Powstania Warszawskiego</p>

  <div class="oral-history-card">
    <h3>Relacja: Krzysztof Gluchowski</h3>
    <p><strong>Sygnatura:</strong> AHM MPW, sygn. 1889</p>
    <p><strong>Data nagrania:</strong> 31 lipca 2009</p>
    <p><strong>Instytucja:</strong> Muzeum Powstania Warszawskiego &mdash; Archiwum Historii Mowionej</p>
    <p><strong>Opis:</strong> Wielogodzinna relacja osiemdziesieciodwuletniego Krzysztofa Gluchowskiego ps. &bdquo;Juras&rdquo; &mdash; zolnierza AK, powstanca warszawskiego, jenca Stalagu XI-B. Nagranie stanowi podstawe rekonstrukcji szlaku bojowego rodziny Gluchowskich i jest kluczowym zrodlem do wszystkich trzech artykulow badawczych. Relacja obejmuje: dziecinstwo w Lazienkach, konspiracje od 1941, Akcje Wilanow, walki na Woli i Starym Miescie, ewakuacje kanalami, niewole i emigracje.</p>
    <p><a href="https://www.1944.pl/archiwum-historii-mowionej/krzysztof-gluchowski,1889.html" target="_blank">&#8594; Otworz relacje na 1944.pl</a></p>
  </div>
</div>

<div class="tab-nav">
  <button class="tab-btn active" onclick="switchTab('katalog', this)">&#128218; Katalog</button>
  <button class="tab-btn" onclick="switchTab('archiwum', this)">&#128247; Archiwum Fotograficzne</button>
</div>

<div class="tab-content active" id="tab-katalog">
<nav class="nav">
<a href="#finding-aid" class="nav-link" style="border-color:var(--gold);color:var(--gold);">Historia rodziny</a>
<a href="#biografia" class="nav-link">Biografia</a>
<a href="#research" class="nav-link">Badania</a>
<a href="#oral-history" class="nav-link">Historia mowiona</a>
<a href="#valuation" class="nav-link" style="border-color:#c0392b;color:#c0392b;">Wycena</a>
{nav_html}
</nav>

{series_html}

{valuation_html}
</div>

<div class="tab-content" id="tab-archiwum">
{photo_archive_html}
</div>

<div class="footer">
  Katalog opracowany metodą muzealną na podstawie bezpośredniej analizy wizualnej dokumentów.<br>
  Standard: ISAD(G) / Dublin Core &bull; Każda fotografia = 1 karta katalogowa<br>
  Źródła: 3 katalogi PDF (Naukowy, Tematyczny, Seria 29z) + 14 fotografii WhatsApp<br>
  Sygnatura zespołu: ARG (Archiwum Rodziny Głuchowskich)<br>
  &copy; 2026
</div>

<div class="lightbox" id="lightbox" onclick="handleLightboxClick(event)">
  <span class="lb-close" onclick="closeLightbox()">&times;</span>
  <div class="lb-zoom-info" id="lb-zoom-info"></div>
  <div class="lb-controls">
    <button class="lb-btn" onclick="zoomOut(event)" title="Pomniejsz (-)">&#x2212;</button>
    <button class="lb-btn" onclick="rotateCCW(event)" title="Obrot w lewo (Q)">&#x21BA;</button>
    <button class="lb-btn" onclick="rotateCW(event)" title="Obrot w prawo (E)">&#x21BB;</button>
    <button class="lb-btn" onclick="zoomIn(event)" title="Powieksz (+)">&#x2b;</button>
    <button class="lb-btn" onclick="zoomReset(event)" title="Resetuj (0)" style="font-size:1em;">1:1</button>
  </div>
  <img id="lb-img" src="" alt="">
  <div class="lb-title" id="lb-title"></div>
</div>

<script>
let currentRotation = 0;
let currentZoom = 1;
let panX = 0, panY = 0;
let isDragging = false, dragStartX = 0, dragStartY = 0, dragStartPanX = 0, dragStartPanY = 0;
let zoomInfoTimeout = null;
let pinchStartDist = 0, pinchStartZoom = 1;

function applyTransform() {{
  const img = document.getElementById('lb-img');
  img.style.transform = 'translate(' + panX + 'px,' + panY + 'px) rotate(' + currentRotation + 'deg) scale(' + currentZoom + ')';
}}

function showZoomInfo() {{
  const el = document.getElementById('lb-zoom-info');
  el.textContent = Math.round(currentZoom * 100) + '%';
  el.classList.add('visible');
  clearTimeout(zoomInfoTimeout);
  zoomInfoTimeout = setTimeout(() => el.classList.remove('visible'), 1200);
}}

function openLightbox(src, title) {{
  currentRotation = 0; currentZoom = 1; panX = 0; panY = 0;
  const img = document.getElementById('lb-img');
  img.src = src;
  img.className = '';
  applyTransform();
  document.getElementById('lb-title').textContent = title;
  document.getElementById('lightbox').classList.add('active');
  document.body.style.overflow = 'hidden';
}}
function closeLightbox() {{
  document.getElementById('lightbox').classList.remove('active');
  document.body.style.overflow = '';
}}
function rotateCW(e) {{
  e && e.stopPropagation();
  currentRotation = (currentRotation + 90) % 360;
  applyTransform();
}}
function rotateCCW(e) {{
  e && e.stopPropagation();
  currentRotation = (currentRotation - 90 + 360) % 360;
  applyTransform();
}}
function setZoom(z, e) {{
  e && e.stopPropagation();
  currentZoom = Math.max(0.25, Math.min(10, z));
  if (Math.abs(currentZoom - 1) < 0.05) {{ currentZoom = 1; panX = 0; panY = 0; }}
  applyTransform();
  showZoomInfo();
}}
function zoomIn(e) {{ setZoom(currentZoom * 1.4, e); }}
function zoomOut(e) {{ setZoom(currentZoom / 1.4, e); }}
function zoomReset(e) {{ e && e.stopPropagation(); currentZoom = 1; panX = 0; panY = 0; applyTransform(); showZoomInfo(); }}

function handleLightboxClick(e) {{
  if (e.target.id === 'lightbox' && !isDragging) closeLightbox();
}}

/* Mouse drag to pan */
const lbImg = document.getElementById('lb-img');
lbImg.addEventListener('mousedown', e => {{
  if (currentZoom <= 1) return;
  e.preventDefault();
  isDragging = true;
  dragStartX = e.clientX; dragStartY = e.clientY;
  dragStartPanX = panX; dragStartPanY = panY;
  lbImg.classList.add('dragging', 'notransition');
}});
document.addEventListener('mousemove', e => {{
  if (!isDragging) return;
  panX = dragStartPanX + (e.clientX - dragStartX);
  panY = dragStartPanY + (e.clientY - dragStartY);
  applyTransform();
}});
document.addEventListener('mouseup', () => {{
  if (isDragging) {{
    isDragging = false;
    lbImg.classList.remove('dragging', 'notransition');
  }}
}});

/* Scroll wheel zoom */
document.getElementById('lightbox').addEventListener('wheel', e => {{
  e.preventDefault();
  const factor = e.deltaY < 0 ? 1.15 : 1/1.15;
  setZoom(currentZoom * factor);
}}, {{ passive: false }});

/* Double-click toggle fit / 100% */
lbImg.addEventListener('dblclick', e => {{
  e.stopPropagation();
  if (currentZoom > 1.05) {{ currentZoom = 1; panX = 0; panY = 0; }}
  else {{ currentZoom = 3; }}
  applyTransform(); showZoomInfo();
}});

/* Touch: pinch-to-zoom + drag */
let lastTouchDist = 0;
document.getElementById('lightbox').addEventListener('touchstart', e => {{
  if (e.touches.length === 2) {{
    const dx = e.touches[0].clientX - e.touches[1].clientX;
    const dy = e.touches[0].clientY - e.touches[1].clientY;
    pinchStartDist = Math.hypot(dx, dy);
    pinchStartZoom = currentZoom;
  }} else if (e.touches.length === 1 && currentZoom > 1) {{
    isDragging = true;
    dragStartX = e.touches[0].clientX; dragStartY = e.touches[0].clientY;
    dragStartPanX = panX; dragStartPanY = panY;
    lbImg.classList.add('notransition');
  }}
}}, {{ passive: true }});
document.getElementById('lightbox').addEventListener('touchmove', e => {{
  if (e.touches.length === 2) {{
    e.preventDefault();
    const dx = e.touches[0].clientX - e.touches[1].clientX;
    const dy = e.touches[0].clientY - e.touches[1].clientY;
    const dist = Math.hypot(dx, dy);
    setZoom(pinchStartZoom * (dist / pinchStartDist));
  }} else if (isDragging && e.touches.length === 1) {{
    panX = dragStartPanX + (e.touches[0].clientX - dragStartX);
    panY = dragStartPanY + (e.touches[0].clientY - dragStartY);
    applyTransform();
  }}
}}, {{ passive: false }});
document.getElementById('lightbox').addEventListener('touchend', () => {{
  isDragging = false;
  lbImg.classList.remove('notransition');
}});

/* Keyboard */
document.addEventListener('keydown', e => {{
  const lb = document.getElementById('lightbox');
  if (!lb.classList.contains('active')) return;
  if(e.key==='Escape') closeLightbox();
  if(e.key==='e' || e.key==='E' || e.key==='ArrowRight') rotateCW();
  if(e.key==='q' || e.key==='Q' || e.key==='ArrowLeft') rotateCCW();
  if(e.key==='+' || e.key==='=') zoomIn();
  if(e.key==='-' || e.key==='_') zoomOut();
  if(e.key==='0') zoomReset();
}});

/* Tab switching */
function switchTab(tabId, btn) {{
  document.querySelectorAll('.tab-content').forEach(tc => tc.classList.remove('active'));
  document.querySelectorAll('.tab-btn').forEach(tb => tb.classList.remove('active'));
  document.getElementById('tab-' + tabId).classList.add('active');
  btn.classList.add('active');
  window.scrollTo({{ top: 0, behavior: 'smooth' }});
}}

/* Photo grid filtering */
function filterPhotos() {{
  const seria = document.getElementById('filter-seria').value;
  const typ = document.getElementById('filter-typ').value;
  const search = document.getElementById('filter-search').value.toLowerCase().trim();
  const cards = document.querySelectorAll('.photo-card');
  let visible = 0;
  cards.forEach(card => {{
    let show = true;
    if (seria && card.dataset.seria !== seria) show = false;
    if (typ && card.dataset.typ !== typ) show = false;
    if (search && card.dataset.search.indexOf(search) === -1) show = false;
    card.style.display = show ? '' : 'none';
    if (show) visible++;
  }});
  document.getElementById('photo-count').textContent = visible + ' fotografii';
}}
</script>

</body>
</html>'''
    return html


if __name__ == "__main__":
    html = generate_html()
    out = os.path.join("docs", "katalog_gluchowski_v4.html")
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Wygenerowano: {out}")
    print(f"Jednostek inwentarzowych: {len(OBJECTS)}")
    print(f"Serii archiwalnych: {len(SERIES)}")
    for s in SERIES:
        count = len([o for o in OBJECTS if o["seria"] == s["id"]])
        if count:
            print(f"  Seria {s['id']}: {count} jednostek — {s['tytul']}")
