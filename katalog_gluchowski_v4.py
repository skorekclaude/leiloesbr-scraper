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
        "tytul": "Dyplom Krzyża Legionowego — zbliżenie",
        "data": "ok. 1920",
        "typ": "dyplom",
        "opis_fizyczny": "Dokument pergaminowy, kaligrafowany ręcznie, zbliżenie fotograficzne fragmentu",
        "opis_tresci": "Zbliżenie dyplomu Krzyża Legionowego nadanego za służbę w Legionach Polskich. Kaligrafowany tekst na pergaminie.",
        "seria": "II",
        "tworca": "Ministerstwo Spraw Wojskowych (?)",
        "jezyk": "polski",
        "kontekst": "Krzyż Legionowy — odznaczenie pamiątkowe nadawane uczestnikom Legionów Polskich 1914–1918.",
        "powiazania": ["ARG/II/11"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/II/11",
        "photo": "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p06_img02.jpeg",
        "tytul": "Dyplom legionowy z portretem Piłsudskiego",
        "data": "ok. 1920",
        "typ": "dyplom",
        "opis_fizyczny": "Dokument ozdobny wielkoformatowy z portretem litografowanym, format ok. A3",
        "opis_tresci": "Pełny widok dyplomu legionowego z portretem Józefa Piłsudskiego w prawym górnym rogu. Druk okolicznościowy, ozdobna typografia.",
        "seria": "II",
        "tworca": "Legiony Polskie / MSWojsk",
        "jezyk": "polski",
        "kontekst": "Dyplomy legionowe z wizerunkiem Komendanta wydawane kombatantom. Portret Piłsudskiego nadaje dokumentowi wymiar ikonograficzny.",
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
        "tytul": "List z emigracji londyńskiej",
        "data": "ok. 1964",
        "typ": "list",
        "opis_fizyczny": "List odręczny atramentem na papierze listowym, 1 karta",
        "opis_tresci": "List odręczny, prawdopodobnie związany z działalnością emigracyjną gen. Głuchowskiego. Pismo atramentem na papierze listowym.",
        "seria": "II",
        "tworca": "nieznany",
        "jezyk": "polski",
        "kontekst": "Głuchowski na emigracji w Londynie (NIE w Kanadzie!). Zmarł 11.VI.1964 w Londynie, pochowany na Brompton Cemetery (nr 576). 15.III.1947 współzałożył Instytut Józefa Piłsudskiego w Londynie — jego papiery stanowią jedną z najważniejszych kolekcji tej instytucji.",
        "powiazania": [],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/II/28",
        "photo": "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p14_img01.jpeg",
        "tytul": "Maszynopis — lista artykułów / obchody 50-lecia (str. 1)",
        "data": "lata 60. XX w.",
        "typ": "notatka",
        "opis_fizyczny": "Maszynopis na papierze kancelaryjnym, format A4, str. 1",
        "opis_tresci": "Maszynopis z listą zamówień/próśb dotyczących artykułów i obchodów 50-lecia. Strona pierwsza dokumentu organizacyjnego.",
        "seria": "II",
        "tworca": "Janusz Głuchowski (?)",
        "jezyk": "polski",
        "kontekst": "50-lecie Legionów = 1964. Głuchowski zmarł 11.VI.1964, zaledwie kilka tygodni przed rocznicą (6.VIII.1964). Hanka-Kulesza (inny z Siódemki Beliny) zmarł 5.VI.1964 — sześć dni wcześniej! Kmicic-Skrzyński (ostatni żyjący z Siódemki) zmarł dopiero w 1972 w Manchesterze.",
        "powiazania": ["ARG/II/29"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/II/29",
        "photo": "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p14_img02.jpeg",
        "tytul": "Maszynopis — lista artykułów / obchody 50-lecia (str. 2)",
        "data": "lata 60. XX w.",
        "typ": "notatka",
        "opis_fizyczny": "Maszynopis, strona 2, kontynuacja",
        "opis_tresci": "Druga strona maszynopisu organizacyjnego. Kontynuacja listy zamówień i artykułów okolicznościowych.",
        "seria": "II",
        "tworca": "Janusz Głuchowski (?)",
        "jezyk": "polski",
        "kontekst": "Kontynuacja ARG/II/28. 50-lecie Legionów — Głuchowski organizował obchody na emigracji, ale nie dożył rocznicy (zm. 11.VI.1964, rocznica 6.VIII.1964). Hanka-Kulesza zmarł 5.VI.1964, sześć dni przed Głuchowskim.",
        "powiazania": ["ARG/II/28"],
        "stan": "Dobry"
    },

    # -- Podseria II/H: Legitymacja oficerska --
    {
        "sygn": "ARG/II/30",
        "photo": "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p13_img01.jpeg",
        "tytul": "Legitymacja oficerska — okładka",
        "data": "lata 30. XX w.",
        "typ": "leg",
        "opis_fizyczny": "Dokument wielostronicowy w twardej oprawie, widok okładki",
        "opis_tresci": "Legitymacja oficerska gen. bryg. Janusza Głuchowskiego — widok okładki/pierwszej strony. Dokument tożsamości oficera Wojska Polskiego.",
        "seria": "II",
        "tworca": "Wojsko Polskie",
        "jezyk": "polski",
        "kontekst": "Legitymacja oficerska — podstawowy dokument tożsamości wojskowej w II RP.",
        "powiazania": ["ARG/II/31", "ARG/II/32"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/II/31",
        "photo": "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p13_img02.jpeg",
        "tytul": "Legitymacja oficerska — rozkładówka z danymi i zdjęciem",
        "data": "lata 30. XX w.",
        "typ": "leg",
        "opis_fizyczny": "Rozkładówka legitymacji z fotografią legitymacyjną, pieczęciami, odręcznymi wpisami",
        "opis_tresci": "Wnętrze legitymacji: dane osobowe, fotografia, pieczęcie.",
        "seria": "II",
        "tworca": "Wojsko Polskie",
        "jezyk": "polski",
        "kontekst": "Rozkładówka legitymacji oficerskiej — dane personalne i foto gen. Głuchowskiego.",
        "powiazania": ["ARG/II/30", "ARG/II/32"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/II/32",
        "photo": "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p13_img03.jpeg",
        "tytul": "Legitymacja oficerska — wpisy służbowe",
        "data": "lata 30. XX w.",
        "typ": "leg",
        "opis_fizyczny": "Kolejna rozkładówka z wpisami atramentem",
        "opis_tresci": "Kolejna rozkładówka legitymacji z wpisami służbowymi.",
        "seria": "II",
        "tworca": "Wojsko Polskie",
        "jezyk": "polski",
        "kontekst": "Kolejna strona legitymacji oficerskiej — wpisy o przebiegu służby wojskowej.",
        "powiazania": ["ARG/II/30", "ARG/II/31"],
        "stan": "Dobry"
    },

    # -- Biogram (z kolekcji Krzysztofa) --
    {
        "sygn": "ARG/II/33",
        "photo": "juras_091_page92.png",
        "tytul": "Biogram gen. bryg. Janusza Głuchowskiego i Czesława Głuchowskiego — druk encyklopedyczny",
        "data": "lata 60.–70. XX w.",
        "typ": "biogram",
        "opis_fizyczny": "Druk encyklopedyczny / słownikowy ze zdjęciami, format książkowy",
        "opis_tresci": "Biogram generała brygady Janusza Juliana Głuchowskiego (1888–1964) oraz aktora Czesława Głuchowskiego — z encyklopedii lub słownika biograficznego. Ze zdjęciami portretowymi.",
        "seria": "II",
        "tworca": "redakcja wydawnictwa encyklopedycznego",
        "jezyk": "polski",
        "kontekst": "Druk słownikowy zachowany przez Krzysztofa jako dokumentacja historii rodziny. Janusz = stryj Krzysztofa, Czesław = brat ojca.",
        "powiazania": ["ARG/II/1", "ARG/VI/14"],
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
        "kontekst": "Kriegsgefangenenpost — jedyna dozwolona forma korespondencji jeńców. Formularz cenzurowany. Nr 0.1245 = numer oficerski.",
        "powiazania": ["ARG/III/2"],
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
        "opis_tresci": "CARD OF IDENTITY — 'P.f.c. Głuchowski Krzysztof — is a polish soldier liberated by Allied forces from german captivity... prisoners of war in Düsseldorf, Germany.' 27th of April 1945.",
        "seria": "V",
        "tworca": "Siły Alianckie / Polish Forces",
        "jezyk": "angielski / polski",
        "kontekst": "KARTA TOŻSAMOŚCI WYZWOLONEGO JEŃCA. Pierwszy dokument wolności. P.f.c. = Private First Class. Düsseldorf, 27 kwietnia 1945 — 11 dni przed kapitulacją Niemiec.",
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
        "opis_tresci": "Głuchowski Krzysztof, st. ułan, konspiracji przez okres 3 lat w Warszawie, ps. Jurat/Język. Pieczęć Komendy UZUP. Datowane 18.2.1945.",
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
        "tytul": "Dwa zaświadczenia — KW i awans (Hensstedt 1945)",
        "data": "22.VIII.1945",
        "typ": "zaswiadczenie",
        "opis_fizyczny": "Dwa dokumenty na jednym zdjęciu: maszynopisy z podpisami i pieczęciami",
        "opis_tresci": "(1) Płk. Kłopacz Stanisław zaświadcza nadanie Krzyża Walecznych Głuchowskiemu Krzysztofowi, plut. 1112, 7 P.Uł. AK nr 29, z 25.9.1944. (2) Zaświadczenie o awansie do stopnia st. ułana z 15.9.1944. Oba z Hensstedt, 22.8.1945.",
        "seria": "V",
        "tworca": "Płk. Kłopacz Stanisław",
        "jezyk": "polski",
        "kontekst": "Zaświadczenia wydane w obozie/po wyzwoleniu potwierdzające odznaczenie i awans z Powstania. Hensstedt — punkt zborny żołnierzy polskich w Niemczech.",
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
        "opis_tresci": "Płk. dypl. ZIEMSKI KAROL, D-ca Polskiego Okręgu Wojskowego Schleswig-Holstein. Jako b. Dowódca Grupy 'PÓŁNOC' w Powstaniu Warszawskim zaświadcza: GŁUCHOWSKI Krzysztof, ur. 1928, ps. 'Juras', walczył w Obronie Starego Miasta, plut. 1112, awansowany na st. strzelca, odznaczony KRZYŻEM WALECZNYCH.",
        "seria": "V",
        "tworca": "Płk. dypl. Karol Ziemski",
        "jezyk": "polski",
        "kontekst": "KLUCZOWY DOKUMENT — zaświadczenie od dowódcy Grupy 'Północ' w Powstaniu. Płk Ziemski dowodził obroną Starego Miasta (5000+ żołnierzy). Wentorf pod Hamburgiem, 26.10.1946.",
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
        "opis_tresci": "CARTE DE RAPATRIÉ — République Française, Ministère des Prisonniers, Déportés et Réfugiés. Nr 1492839. Pieczęć 'CENTRE D'ORSAY, 27 JUIN 1945'. Głuchowski Krzysztof, Pologne.",
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
        "opis_tresci": "FICHE DE TRANSPORT — Nr 1492839 (ten sam co Carte de Rapatrié). Głuchowski Krzysztof, Caserne Jessina. Ocena zdrowotna: D, R.",
        "seria": "V",
        "tworca": "Ministère des Prisonniers",
        "jezyk": "francuski",
        "kontekst": "Karta transportowa repatrianta — umożliwiała darmowy przejazd kolejowy. Caserne Jessina = koszary zbiorcze.",
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
        "opis_tresci": "AMBASSADE de POLOGNE à Paris. 'Pan Głuchowski K. zostanie skierowany (...) na kurs, który rozpocznie się w dniu 25 Lipca b.r. w Villard-de-Lans.' Paryż, 29 czerwca 1945.",
        "seria": "V",
        "tworca": "Ambasada RP w Paryżu",
        "jezyk": "polski",
        "kontekst": "Villard-de-Lans — miejscowość w Alpach, ośrodek rekonwalescencji i kursów dla polskich żołnierzy we Francji.",
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
        "opis_tresci": "Karteczka z nazwiskiem, wizytówka włoska (France. Creco. Luigi), mała karta z numerem G 1118001/9 i rysunkiem.",
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
        "tytul": "List z Francji",
        "data": "3.II.1944",
        "typ": "list",
        "opis_fizyczny": "List odręczny atramentem, 1 karta",
        "opis_tresci": "List odręczny atramentem. Wspomina 'Brasserie Garcia, St. Ouen'. Korespondencja z Francji.",
        "seria": "V",
        "tworca": "nieznany",
        "jezyk": "polski / francuski",
        "kontekst": "Korespondencja z Francji. St. Ouen — gmina pod Paryżem.",
        "powiazania": [],
        "stan": "Dobry"
    },

    # -- Podseria V/I: PSZ, II Korpus, Gimnazjum 3DSK --
    {
        "sygn": "ARG/V/54",
        "photo": "Seria_29z_p29_img01.jpeg",
        "tytul": "Skierowanie na RTG — 7 Szpital Wojenny Polish Gen. Hosp.",
        "data": "23.VII.1945",
        "typ": "skierowanie",
        "opis_fizyczny": "Formularz z pieczęcią '7 SZPITAL WOJENNY POLISH GEN. HOSP.'",
        "opis_tresci": "RENTGEN — skierowanie z 7 Pułku Ułanów Lubelskich im. Gen. Głuchowskiego, I.K.A.H. Pieczęć szpitala.",
        "seria": "V",
        "tworca": "7 P.Uł. / 7 Szpital Wojenny",
        "jezyk": "polski / angielski",
        "kontekst": "7 Pułk Ułanów 'im. Gen. Głuchowskiego' — pułk noszący imię stryja Krzysztofa! Krzysztof służy w pułku upamiętniającym stryja.",
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
        "tytul": "Przepustka z Bazy Personalnej 2 Korpusu",
        "data": "11.VI.1946",
        "typ": "przepustka",
        "opis_fizyczny": "Przepustka z pieczęcią, podpis ppor. Kuclińskiego",
        "opis_tresci": "Baza Personalna Legio 2 Korpusu. Głuchowski Krzysztof, prawo opuścić teren obozu. Podpis Kucliński ppor.",
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
        "opis_tresci": "'Zadańca Włosooe No 1', 23.VIII.1945. Temat: tragiczna historia, deszcz. Wspomina 1.VIII.1944, Powstanie, pluton 1112.",
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
        "opis_tresci": "'St.uł. Krzysztof Głuchowski, Polish Forces C.M.F. 152, Gimnazjum.' Temat: 'Jaka kolosalna siła moralna...' Wspomina Bora Komorowskiego.",
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
        "opis_tresci": "'St.uł. Krzysztof Głuchowski, Polish Forces CMF 152, Gimnazjum 3DSK.' Esej o artykułach wuja — gen. Janusza Głuchowskiego — o Powstaniu. Wspomina 'artykuły P. Głuchowskiego', Armię Krajową.",
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
        "tytul": "Instrukcja medyczna A.T.S. — druk brytyjski dla żołnierzy",
        "data": "1946–1948",
        "typ": "ulotka",
        "opis_fizyczny": "Druk informacyjny brytyjski, format mały",
        "opis_tresci": "Instrukcja medyczna A.T.S. (Auxiliary Territorial Service) — zasady leczenia i higieny dla żołnierzy. Druk brytyjski standardowy.",
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
        "tytul": "Rozkaz personalny 7 Pułk Ułanów — tabela, D-ca taboru, 1946",
        "data": "1946",
        "typ": "rozkaz",
        "opis_fizyczny": "Tabela personalna, druk maszynowy",
        "opis_tresci": "Rozkaz personalny 7 Pułku Ułanów w formie tabeli. Dotyczy D-cy taboru/laboratoriów, rok 1946. Ewidencja personalna jednostki.",
        "seria": "V",
        "tworca": "D-wo 7 Pułku Ułanów",
        "jezyk": "polski",
        "kontekst": "7 Pułk Ułanów Lubelskich — jednostka macierzysta Krzysztofa. Rozkaz personalny dokumentuje strukturę organizacyjną.",
        "powiazania": ["ARG/V/81"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/V/98",
        "photo": "juras_032_page33.png",
        "tytul": "Pismo Sztabu Głównego — Bodney Airfield, Thetford",
        "data": "1947",
        "typ": "pismo",
        "opis_fizyczny": "Pismo urzędowe maszynopisem, nagłówek Sztabu",
        "opis_tresci": "Pismo Sztabu Głównego z Bodney Airfield, Thetford — prośba o list napędzający do Komisji Skarbu. Korespondencja administracyjna.",
        "seria": "V",
        "tworca": "Sztab Główny PSZ",
        "jezyk": "polski",
        "kontekst": "Bodney Airfield, Thetford = baza PKPR w Norfolk. Korespondencja administracyjna dotycząca spraw finansowych.",
        "powiazania": ["ARG/V/83"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/V/99",
        "photo": "juras_033_page34.png",
        "tytul": "Notatki odręczne — adresy, terminy, lista spraw",
        "data": "lata 40. XX w.",
        "typ": "notatka",
        "opis_fizyczny": "Notatki odręczne na kartce, pismo ołówkiem i atramentem",
        "opis_tresci": "Notatki z datami i adresami: Pidlaseki, nogi/herpes, Omicella Nowe, Port maal harp, Bach, koszule. Lista adresów, terminów, spraw do załatwienia.",
        "seria": "V",
        "tworca": "Krzysztof Andrzej Głuchowski",
        "jezyk": "polski",
        "kontekst": "Notatki codzienne emigranta — sprawy zdrowotne, adresy, lista zakupów. Okruchy życia codziennego.",
        "powiazania": [],
        "stan": "Średni"
    },

    # -- Podseria V/U: Zaświadczenia o służbie --
    {
        "sygn": "ARG/V/100",
        "photo": "juras_034_page35.png",
        "tytul": "Zaświadczenie PSZ nr 87949 — zakończenie służby",
        "data": "1948",
        "typ": "zaswiadczenie",
        "opis_fizyczny": "Zaświadczenie urzędowe PSZ, druk z pieczęcią, London",
        "opis_tresci": "Zaświadczenie Polskich Sił Zbrojnych nr 87949 o zakończeniu służby. Krzysztof Głuchowski, stopień L/Cpl (st.uł.). Wystawione w Londynie.",
        "seria": "V",
        "tworca": "Polskie Siły Zbrojne",
        "jezyk": "polski",
        "kontekst": "Koniec służby wojskowej — przejście do życia cywilnego. L/Cpl = Lance Corporal = starszy ułan.",
        "powiazania": ["ARG/V/91", "ARG/V/103"],
        "stan": "Dobry"
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
        "opis_tresci": "Army Book 64, Part I — okładka wewnętrzna i strona tytułowa. Numer druku: 43464/45.",
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
        "opis_tresci": "Notatki: WERYFIKACJA AK, NEISS, Kompania I, Głuchowski szef sekcji, 7 Pułk, Grupa I Bo. Daty i numery rozkazów — materiał przygotowawczy do weryfikacji.",
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
        "opis_tresci": "Notatki: Wkładczysko 1-13, Medal Cześć Wojska, Rozkaz No 245, Odznaka 3 DSK, Rozkaz Quinoy No 256, 3 DSK Nr 77/46. Systematyczna ewidencja odznaczeń i rozkazów.",
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
        "opis_tresci": "Legitymacja Krzyża Armii Krajowej (wewnątrz). Głuchowski Krzysztof, ps. 'Juras'. Przydział: ZWZ Komp.V Plut.III/2, 7 Pułk Ułan. Lubel. 'Jeleń'. Odznaczony 1 sierpnia 1966 przez gen. Bora-Komorowskiego. Londyn 7.III.1968, podpis K. Ziemski 'Wachnowski'.",
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
        "opis_tresci": "Legitymacja Odznaki Pamiątkowej AK: Starszy Ułan Głuchowski Krzysztof, ps. JURAS, nr 4042. Data: 12 czerwca 1946. Komisja Weryfikacyjna 2 Korpusu AK.",
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
        "opis_tresci": "Certificate P.R.C. Record Office, Witley Camp, Godalming, Surrey, 19 FEB 1948. Treść: 'GŁUCHOWSKI KRZYSZTOF was enlisted into P.R.C. 1.11.46 after serving with Polish Forces under British Command from 14.7.45 to 1.11.46.'",
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
        "opis_tresci": "Przepustka (PASS) Army Form B.295 z pieczęcią PUŁK UŁANÓW LUBELSKICH. Inny egzemplarz niż ARG/V/81.",
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
        "opis_tresci": "Alien's Identity Certificate — dokument tożsamości cudzoziemca. Student, South West Essex Technical College. Entry: Gravesend, 31.10.47. Status: Alien (cudzoziemiec).",
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
        "opis_tresci": "Dokument War Office / MI5 (CONFIDENTIAL) — weryfikacja: born Grzegorzów Nov 1926, parents Stefan and Helena, marital status Single. Service history. Ocena: 'Politically Well-Minded', 'Not convicted of any offence', conduct 'Very Good'.",
        "seria": "V",
        "tworca": "War Office / MI5",
        "jezyk": "angielski",
        "kontekst": "DOKUMENT WYWIADOWCZY — MI5 weryfikowało polskich żołnierzy pod kątem lojalności politycznej. 'Politically Well-Minded' = pozytywna ocena. Ujawnia miejsce urodzenia: Grzegorzów, rodziców: Stefan i Helena.",
        "powiazania": ["ARG/V/94", "ARG/V/103"],
        "stan": "Dobry"
    },

    # -- Podseria V/AE: Fotografia naszywki pułkowej --
    {
        "sygn": "ARG/V/134",
        "photo": "juras_068_page69.png",
        "tytul": "Fotografia naszywki pułkowej 7 Pułku Ułanów Lubelskich — 'Jeleń'",
        "data": "1944–1948",
        "typ": "foto",
        "opis_fizyczny": "Fotografia czarno-biała na papierze, format ok. 10×7 cm, naklejona na białe podłoże",
        "opis_tresci": "Fotografia dokumentująca naszywkę pułkową — biała sylwetka jelenia na ciemnym tle. Oznaka 7 Pułku Ułanów Lubelskich ('Jeleń'). Zdjęcie oryginalnej oznaki mundurowej, nie sam tekstyl.",
        "seria": "V",
        "tworca": "nieznany",
        "jezyk": "—",
        "kontekst": "Fotografia dokumentująca oznakę pułkową 7 P.Uł. 'Jeleń'. Jeleń = symbol pułku od 1918. Fotograficzna pamiątka przynależności do jednostki.",
        "powiazania": ["ARG/V/81", "ARG/V/118", "ARG/VI/3"],
        "stan": "Dobry"
    },

    # -- Podseria V/AF: Ephemera i kartki okolicznościowe --
    {
        "sygn": "ARG/V/135",
        "photo": "juras_069_page70.png",
        "tytul": "Kartka od Stowarzyszenia Polskich Przemysłowców (SPP) — życzenia",
        "data": "lata 50.–60. XX w.",
        "typ": "druk",
        "opis_fizyczny": "Kartka okolicznościowa z podpisami wielu osób",
        "opis_tresci": "Kartka od Stowarzyszenia Polskich Przemysłowców (SPP) — życzenia z wieloma podpisami. Środowisko polonijne.",
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
        "opis_fizyczny": "Wycinek z gazety, fotografia, papier gazetowy",
        "opis_tresci": "Wycinek prasowy z fotografią tablicy pamiątkowej z Palmirów: 'ŁATWIEJ JEST MÓWIĆ O POLSCE NIE KAŻDY DOKONA TAK SZCZEREGO AKTU CIERPIENIA... UMRZEĆ ZA TRUDNOŚĆ CIERPIEĆ'.",
        "seria": "V",
        "tworca": "prasa polonijna",
        "jezyk": "polski",
        "kontekst": "Palmiry — miejsce masowych egzekucji dokonywanych przez Niemców na polskiej inteligencji (1939–1941). Wycinek zachowany jako pamiątka patriotyczna.",
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
        "tytul": "Rysunek odręczny — szkic architektoniczny (kościół z wieżą)",
        "data": "1947–1948",
        "typ": "rysunek",
        "opis_fizyczny": "Szkic architektoniczny, ołówek/tusz na papierze",
        "opis_tresci": "Rysunek odręczny — szkic architektoniczny budynku z wieżą (kościół?). Ołówek lub tusz. Prawdopodobnie zadanie z rysunku technicznego na South West Essex Technical College.",
        "seria": "V",
        "tworca": "Krzysztof Andrzej Głuchowski",
        "jezyk": "—",
        "kontekst": "Prace studenckie z rysunku technicznego/architektonicznego — przygotowanie do zawodu inżyniera.",
        "powiazania": ["ARG/V/138", "ARG/V/80"],
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
        "tytul": "Zaświadczenie Ziemskiego Karola — Dowódca Polskiego Okręgu III Wileńskiego",
        "data": "lata 40.–60. XX w.",
        "typ": "zaswiadczenie",
        "opis_fizyczny": "Zaświadczenie urzędowe z pieczęcią",
        "opis_tresci": "Zaświadczenie Karola Ziemskiego, Dowódcy Polskiego Okręgu III Wileńskiego — zaświadcza służbę ochotnika Waldemara, odznaczenie Krzyżem. Pieczęć: Żołnierzy Polskich Okręgu III.",
        "seria": "V",
        "tworca": "Karol Ziemski / Okręg III Wileński AK",
        "jezyk": "polski",
        "kontekst": "K. Ziemski 'Wachnowski' = ten sam, który podpisał legitymację Krzyża AK Krzysztofa (ARG/V/118). Zaświadczenie dotyczy innej osoby (Waldemar) — zachowane przez Krzysztofa jako dokument pułkowy.",
        "powiazania": ["ARG/V/118"],
        "stan": "Dobry"
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
        "opis_tresci": "Aerogram zaadresowany do Gen. dywizji Tadeusz Bór-Komorowski, HQ Polish Forces, IRELAND. Stempel pocztowy — korespondencja z dowódcą Powstania Warszawskiego.",
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
        "opis_tresci": "List ręczny nr 563, dot. historii Pułku 1112, sprawy patrocji, rozkazy. Nagłówek: Polish Institute and Sikorski Museum.",
        "seria": "V",
        "tworca": "nadawca z kręgu kombatanckiego",
        "jezyk": "polski",
        "kontekst": "Polish Institute and Sikorski Museum (Londyn) = główne archiwum PSZ na emigracji. Pułk 1112 = prawdopodobnie oznaczenie konspiracyjne 7 P.Uł. w AK. List dotyczy prac historycznych nad dziejami pułku.",
        "powiazania": ["ARG/V/148", "ARG/V/150"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/V/150",
        "photo": "juras_084_page85.png",
        "tytul": "Pismo z Polish Institute — potwierdzenie otrzymania dokumentów",
        "data": "lata 50.–60. XX w.",
        "typ": "pismo",
        "opis_fizyczny": "Pismo maszynopisem na papierze instytutowym",
        "opis_tresci": "Pismo z Polish Institute and Sikorski Museum — maszynopis, potwierdzenie otrzymania dokumentów. Korespondencja archiwalna.",
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
        "opis_tresci": "Kontynuacja wspomnień: opis przedwojennego Krakowa, sytuacja polityczna roku 1918. Perspektywa historyczna.",
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
        "tytul": "Tablica pamiątkowa akcji 'Jeleń' (1.VIII.1944)",
        "data": "1.VIII.1944",
        "typ": "foto",
        "opis_fizyczny": "Fotografia tablicy pamiątkowej",
        "opis_tresci": "Tablica upamiętniająca atak oddziału AK 'Jeleń' (7 Pułk Ułanów Lubelskich AK) na siedzibę Gestapo i Dom Prasy w Krakowie, 1 sierpnia 1944.",
        "seria": "VI",
        "tworca": "nieznany",
        "jezyk": "polski",
        "kontekst": "7 P.Uł. AK 'Jeleń' — oddział, w którym służył Krzysztof (plut. 1112). Kraków, nie Warszawa — inna kompania.",
        "powiazania": ["ARG/V/3"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/VI/2",
        "photo": "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p10_img01.jpeg",
        "tytul": "Krzyż Walecznych — fotografia odznaczenia",
        "data": "1920–1944",
        "typ": "foto",
        "opis_fizyczny": "Fotografia czarno-biała odznaczenia metalowego",
        "opis_tresci": "Fotografia Krzyża Walecznych — odznaczenia wojskowego. Krzyż z mieczami na wstążce.",
        "seria": "VI",
        "tworca": "nieznany fotograf",
        "jezyk": "—",
        "kontekst": "KW nadany w rodzinie wielokrotnie — Januszowi (1922) i Krzysztofowi (1944).",
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
        "tytul": "Zaproszenie na mszę rocznicową 7 P.Uł.",
        "data": "1970",
        "typ": "druk",
        "opis_fizyczny": "Druk okolicznościowy, format mały",
        "opis_tresci": "Zaproszenie na mszę świętą rocznicową 7 Pułku Ułanów Lubelskich AK 'Jeleń'. Druk okolicznościowy, emigracja.",
        "seria": "VI",
        "tworca": "Koło Kombatantów 7 P.Uł.",
        "jezyk": "polski",
        "kontekst": "Działalność kombatancka na emigracji — podtrzymywanie tradycji pułkowej.",
        "powiazania": ["ARG/II/8"],
        "stan": "Dobry"
    },
    {
        "sygn": "ARG/VI/9",
        "photo": "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p21_img01.jpeg",
        "tytul": "Nekrolog Jana Lorensa — 7 P.Uł., Chicago 1960",
        "data": "29.I.1960",
        "typ": "nekrolog",
        "opis_fizyczny": "Druk żałobny / klepsydra",
        "opis_tresci": "Nekrolog plutonowego Jana Lorensa, żołnierza 7 P.Uł., zmarłego 29 stycznia 1960 w Chicago.",
        "seria": "VI",
        "tworca": "rodzina Lorensów / 7 P.Uł.",
        "jezyk": "polski",
        "kontekst": "Ślad diasporowy — żołnierze 7 P.Uł. rozproszeni po świecie (Chicago, Kanada). Głuchowski przechowywał nekrolog kolegi z pułku.",
        "powiazania": ["ARG/VI/8"],
        "stan": "Dobry"
    },

    # -- Getto łódzkie --
    {
        "sygn": "ARG/VI/10",
        "photo": "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p17_img01.jpeg",
        "tytul": "List do Ambasady Izraela — waluta gettowa",
        "data": "18.V.1958",
        "typ": "list",
        "opis_fizyczny": "List maszynopisem na papierze korespondencyjnym",
        "opis_tresci": "List Krzysztofa Głuchowskiego do Ambasady Izraela w sprawie sprzedaży walut i monet getta łódzkiego (Litzmannstadt).",
        "seria": "VI",
        "tworca": "Krzysztof Głuchowski",
        "jezyk": "polski",
        "kontekst": "Próba sprzedaży numizmatów gettowych — pamiątki znalezione lub nabyte. Łódź = Litzmannstadt pod okupacją.",
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
        "tytul": "Biogramy rodzinne — kontynuacja druku encyklopedycznego",
        "data": "lata 60.–70. XX w.",
        "typ": "biogram",
        "opis_fizyczny": "Druk encyklopedyczny / słownikowy ze zdjęciami, kontynuacja",
        "opis_tresci": "Dalsza część biogramów rodziny Głuchowskich z encyklopedii lub słownika biograficznego. Zdjęcia portretowe członków rodziny.",
        "seria": "VI",
        "tworca": "redakcja wydawnictwa encyklopedycznego",
        "jezyk": "polski",
        "kontekst": "Kontynuacja biogramów z juras_091. Dokumentacja genealogiczna rodziny Głuchowskich zachowana przez Krzysztofa.",
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
        "tytul": "Pocztówka z karykaturą gen. Głuchowskiego — z kolekcji Krzysztofa",
        "data": "lata 20.–30. XX w.",
        "typ": "pocztówka",
        "opis_fizyczny": "Pocztówka ok. 14 × 9 cm, reprodukcja karykatury gen. Głuchowskiego. Na odwrocie odręczne napisy ołówkiem: 'Z albumu karikatur [...] ppor 1 Bryg. LP'. 2 zdjęcia.",
        "opis_tresci": "Karykatura gen. Janusza Głuchowskiego na pocztówce. Odręczny napis nawiązuje do albumu karykatur podchorążego z 1. Brygady Legionów Polskich.",
        "seria": "II",
        "tworca": "nieznany karykaturzysta / środowisko legionowe",
        "jezyk": "polski",
        "kontekst": "Karykatury oficerów Legionów Polskich — popularna forma artystyczna w środowisku legionowym. 1. Brygada Legionów — formacja Piłsudskiego, w której Głuchowski służył od 1914 jako jeden z 'Siódemki Beliny'. Pocztówka dokumentuje rozpoznawalność Głuchowskiego w kręgach legionowych.",
        "powiazania": ["ARG/II/1", "ARG/II/2", "ARG/II/36"],
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
        "kontekst": "Krzysztof ('Juraś') Głuchowski — syn gen. Janusza Głuchowskiego, powstaniec warszawski ps. 'Juraś', jeniec Stalagu IV-B Mühlberg. Po wojnie emigracja do Wielkiej Brytanii, następnie Brazylia. Paszporty brytyjskie dokumentują jego status uchodźcy i późniejsze obywatelstwo — świadectwo losu polskiej emigracji wojennej.",
        "powiazania": ["ARG/V/9", "ARG/V/10", "ARG/V/124"],
        "stan": "Dobry"
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
        "wartosc_hist": "★★",
        "opis_wartosci": "List z emigracji londyńskiej. Korespondencja emigracyjna: 200-500 PLN.",
        "cena_min": 200,
        "cena_max": 500,
        "waluta": "PLN",
        "rekomendacja": "W zestawie."
    },
    "ARG/II/28": {
        "wartosc_hist": "★★",
        "opis_wartosci": "Maszynopis — lista obchody 50-lecia, str. 1. Dokumenty organizacyjne emigracji: 150-400 PLN.",
        "cena_min": 150,
        "cena_max": 400,
        "waluta": "PLN",
        "rekomendacja": "W zestawie."
    },
    "ARG/II/29": {
        "wartosc_hist": "★★",
        "opis_wartosci": "Maszynopis str. 2. j.w.",
        "cena_min": 100,
        "cena_max": 250,
        "waluta": "PLN",
        "rekomendacja": "W zestawie."
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

@media(max-width:700px) {{
  .cards-grid {{ grid-template-columns:1fr; }}
  .header h1 {{ font-size:1.6em; }}
  .series-title {{ font-size:1.3em; }}
  .val-table {{ font-size:0.7em; }}
  .val-top-lots {{ grid-template-columns:1fr; }}
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
        <div class="pc-desc">Inspektor Armii. Podpis na zaświadczeniu o przynależności Janusza do OB PPS (1905&ndash;1908). Papier firmowy Inspektoratu Armii. Współtwórca ruchu strzeleckiego.</div>
        <div class="pc-docs">ARG/II/3, II/4</div>
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
        <div class="conn-detail">Zaświadczenie + list na papierze Inspektoratu Armii</div>
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
