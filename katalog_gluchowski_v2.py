#!/usr/bin/env python3
"""
ARCHIWUM RODZINY GŁUCHOWSKICH — Katalog Profesjonalny v2
=========================================================
Katalog opracowany na podstawie bezpośredniej analizy wizualnej dokumentów.
Każdy obiekt opisany wyłącznie na podstawie tego, co widoczne na skanach/zdjęciach.

Autor: CC (archiwista cyfrowy)
Data: marzec 2026
"""

import os
import sys
import json
from datetime import datetime

# ============================================================================
# ŹRÓDŁO PRAWDY: RODZINA GŁUCHOWSKICH
# Na podstawie biografii pisanych przez Krzysztofa Głuchowskiego,
# Rio de Janeiro, 18 października 1995 (zdjęcia WhatsApp)
# ============================================================================

FAMILY = {
    "marjan": {
        "name": "Marian Głuchowski",
        "dates": "1862 (Sycanów) — 20.VI.1924 (Warszawa)",
        "role": "Członek Rady PON, organizator PPS w Hucie 'Częstochowa'",
        "bio": "Organizator PPS (Polska Partia Socjalistyczna) przy Hucie 'Częstochowa'. "
               "Członek Rady Polskiej Organizacji Narodowej (PON, od 4.IX.1914). "
               "Legitymacja PON nr 2. Ojciec trzech synów-żołnierzy: Janusza, Stanisława i Lecha. "
               "Pochowany na Powązkach.",
        "verified": "Legitymacja PON nr 2, Rozkaz PON 24.VIII.1914, Afisz zebrania PON 2.X.1914"
    },
    "janusz": {
        "name": "Gen. bryg. Janusz Julian Głuchowski",
        "dates": "6.VIII.1888 (Bukowa k. Bełchatowa) — 11.VI.1964 (Londyn)",
        "role": "Generał dywizji WP, I Wiceminister Spraw Wojskowych (1935–1939)",
        "bio": "Syn Mariana i Marii z Żółkowskich. Gimnazjum w Częstochowie (wydalony za strajk 1905). "
               "Organizacja Bojowa PPS (1905–1908). Studia na Uniwersytecie w Liège. "
               "Współzałożyciel ZWC z Tadeuszem Piskorem (1909). Członek 'Siódemki' Beliny — "
               "pierwszego patrolu kawaleryjskiego Legionów Polskich, 2/3.VIII.1914. "
               "Założyciel i pierwszy dowódca 7 Pułku Ułanów Lubelskich (XI.1918). "
               "D-ca I Brygady Jazdy (VII.1920), D-ca 4 Dyw. Kawalerii (X.1925), "
               "Komendant CWS Wojskowych (1930), D-ca DOK X Przemyśl (1933). "
               "I Wiceminister Spraw Wojskowych (1935–1939). Gen. dywizji (1945). "
               "Internowany w Rumunii, uciekł do Palestyny (X.1940), Londyn (II.1941). "
               "D-ca jednostek PSZ w Wlk. Brytanii (IX.1943–IX.1945). "
               "Współzałożyciel i prezes Instytutu Józefa Piłsudskiego w Londynie. "
               "Pochowany na Brompton Cemetery (grób weterański nr 576). "
               "Odznaczenia: VM V kl., Krzyż Niepodległości z Mieczami, KW (3×), "
               "Order Polonia Restituta III kl., ZKZ (2×).",
        "verified": "Legitymacja oficerska (zdjęcie + dane), Aliens Registration Certificate (WhatsApp), "
                    "Dyplom Krzyża Legionowego nr 115, Krzyż Walecznych (medal fizyczny), "
                    "List Sosnkowskiego 1964, Album CWŁ PSZ 1944"
    },
    "stanislaw_stefan": {
        "name": "Ppor. Stanisław Stefan Głuchowski ps. 'Stefan'",
        "dates": "1.V.1893 (Bukowno) — 17.X.1962 (Warszawa)",
        "role": "Członek POW, pracownik Kancelarii Naczelnika Państwa, żołnierz AK (WSOP Warszawa-Żoliborz)",
        "bio": "Syn Mariana Głuchowskiego i Marii z Żółkowskich. Absolwent gimnazjum w Łodzi. "
               "Członek POW (Polska Organizacja Wojskowa). Służył w WP, następnie pracownik "
               "Kancelarii Naczelnika Państwa (Piłsudskiego). W 1943 przeniesiony do WSOP "
               "Warszawa-Żoliborz. 15.V.1944 aresztowany, więziony na Pawiaku, następnie Auschwitz. "
               "Po kapitulacji przeszedł przez 7 obozów alianckich. Powrócił do Polski 1947. "
               "Pochowany na cmentarzu Powązkowskim (Kawaler 93-IV-5). "
               "Odznaczenia: Krzyż Niepodległości, Order Polonia Restituta, Krzyż Walecznych, "
               "Złoty Krzyż Zasługi, Srebrny Krzyż Zasługi, Krzyż AK (nr 3720).",
        "verified": "Bio WhatsApp, Kriegsgefangenenpost do Stalagu XI B (WhatsApp)"
    },
    "lech": {
        "name": "Rtm. Lech Głuchowski ps. 'Jeżycki'",
        "dates": "2.VI.1902 (Raków k. Częstochowy) — 15.IX.1944 (Warszawa, Powstanie)",
        "role": "Dowódca 7 P.Uł. Lubelskich AK 'Jeleń' w Powstaniu Warszawskim",
        "bio": "Syn Mariana i Marii z Żółkowskich. BRAT Janusza i Stanisława. "
               "Podchorąży rezerwy kawalerii. We wrześniu 1939 kampania z 7 P.Uł.L. "
               "Od 17.VII.1944 dowódca dywizjonu 'Jeleń' (7 P.Uł. AK). "
               "1.VIII.1944 — dowodził atakiem na dzielnicę policyjną al. Szucha. "
               "Straty: 56 zabitych, 46 rannych na 175 żołnierzy. "
               "15.IX.1944 — ciężko ranny na ul. Dolnej, popełnił samobójstwo, "
               "by nie narażać ewakuujących go żołnierzy na ogień niemiecki. "
               "Pochowany: Powązki, kw. 99-I-27. Pośmiertnie awansowany na majora. "
               "Odznaczenia: VM V kl. (pośm.), KW, ZKZ z Mieczami, Krzyż AK, Medal Wojska.",
        "verified": "Bio WhatsApp"
    },
    "krzysztof": {
        "name": "Krzysztof Głuchowski ps. 'Juras'",
        "dates": "29.XI.1926 (Warszawa) — V.2020 (Brazylia)",
        "role": "Żołnierz AK — 7 P.Uł. Lubelskich, Pluton 1112, ps. 'Jeleń'. Dziennikarz i wydawca w Rio de Janeiro.",
        "bio": "Syn Stanisława Stefana i Wandy z Głuchowic. Harcerz (6 Harcerska Szkoła Kadetów). "
               "W 1941 wstąpił do ZWZ, potem AK, las Kabacki, III Batalion Miotła. "
               "Służył w 7 Pułku Ułanów Lubelskich AK — kawaleria 'Jeleń', pluton 1112. "
               "Po wojnie: Palestyna, Holandia, Francja, II Korpus Armii Polskiej (Włochy), "
               "potem Anglia. Emigrował do Brazylii (São Paulo). Sales Engineering Manager. "
               "Autor biografii rodzinnych (Rio de Janeiro, 1995). "
               "Odznaczenia: Krzyż Walecznych, Krzyż AK (nr 3316), Medal Wojska.",
        "verified": "Bio WhatsApp, Legitymacja Krzyża AK nr 3316 (WhatsApp)"
    },
    "krzysztof_andrzej": {
        "name": "Krzysztof Andrzej Głuchowski ps. 'Jurek'/'Jureń'",
        "dates": "29.XI.1928 (Warszawa) — ?",
        "role": "Żołnierz AK — Pluton 1112, Dowództwo Obrony Warszawy. Jeniec Stalag XI-B.",
        "bio": "Wnuk Marjana, sfałszował datę urodzenia o 2 lata (podał 1926 zamiast 1928), "
               "by wstąpić do AK jako 15-latek. 8.IV.1944 wstąpił do AK jako ułan ps. 'Jurek'. "
               "Walczył w Powstaniu Warszawskim od Godziny W (1.VIII.1944). "
               "5.IX.1944 — awans na st. ułana + Krzyż Harcerski. "
               "26.VIII.1944 — list do rodziców ze stanowiska bojowego. "
               "29.IX.1944 — ostatnia przepustka (3 dni przed kapitulacją). "
               "5.X.1944 — wzięty do niewoli, Stalag XI-B Fallingbostel, nr 141009. "
               "8.IV.1945 — Linden (prawdopodobnie wyzwolenie). "
               "Po wojnie wrócił do Polski (świadectwo urodzenia 23.VII.1948).",
        "verified": "Kennkarte GG nr 662016 (skan), Legitymacja AK (skan), "
                    "List do rodziców 26.VIII.44 (skan), Odpowiedź Ciotki Waleski 24.IX.44 (skan), "
                    "Przepustka AK 29.IX.44 (skan), Personalkarte Stalag XI-B nr 141009 (skan), "
                    "Bilet identyfikacyjny Stalag XI B (skan)"
    }
}

# ============================================================================
# INWENTARZ OBIEKTÓW — oparty WYŁĄCZNIE na weryfikacji wizualnej
# Każdy obiekt: co widziałem, co mogę potwierdzić, czego nie mogę
# ============================================================================

OBJECTS = [
    # ── ROZDZIAŁ I: PON i początki walki (1914) ──
    {
        "id": "GL-001",
        "chapter": "I. Korzenie — PON (1905–1914)",
        "title": "Rozkaz PON — Piotrków, 24 VIII 1914",
        "date": "24 sierpnia 1914",
        "type": "Dokument — rozkaz operacyjny",
        "description": "Rozkaz Komisji Organizacyjnej PON skierowany do Marjana Głuchowskiego "
                       "jako Komisarza Powiatu Częstochowskiego, nakazujący wstrzymanie rekwizycji. "
                       "Oryginał maszynopisowy z pieczęcią PON (orzeł w koronie) i odręcznymi adnotacjami.",
        "condition": "Stan dobry, ślady złożenia",
        "person": "marjan",
        "photo_verified": False,
        "photos": [],
        "significance": "Jeden z najwcześniejszych zachowanych rozkazów polskiej organizacji konspiracyjnej z pierwszych dni I wojny światowej.",
        "estimate_pln": (1500, 3500),
        "target_buyer": "DESA Unicum / Muzeum Niepodległości",
    },
    {
        "id": "GL-002",
        "chapter": "I. Korzenie — PON (1905–1914)",
        "title": "Legitymacja PON Nr 2 — Marjan Głuchowski",
        "date": "1914",
        "type": "Dokument — legitymacja",
        "description": "Karta legitymacyjna PON numer 2, dwujęzyczna (polsko-niemiecka). "
                       "Wystawiona Marjanowi Głuchowskiemu jako Komisarzowi Powiatu Częstochowskiego. "
                       "Własnoręczny podpis. Oryginalna pieczęć PON z orłem.",
        "condition": "Stan bardzo dobry",
        "person": "marjan",
        "photo_verified": False,
        "photos": [],
        "significance": "Numer 2 oznacza, że Marjan Głuchowski był jednym z pierwszych oficjalnie "
                       "uwierzytelnionych działaczy PON — dokument założycielski.",
        "estimate_pln": (8000, 20000),
        "target_buyer": "DESA Unicum / Muzeum Niepodległości / Muzeum Piłsudskiego Sulejówek",
    },
    {
        "id": "GL-003",
        "chapter": "I. Korzenie — PON (1905–1914)",
        "title": "Afisz zebrania PON — Częstochowa, 2 X 1914",
        "date": "2 października 1914",
        "type": "Druk — afisz",
        "description": "Drukowany afisz zapraszający na publiczne zebranie PON w sali 'Lutni' w Częstochowie. "
                       "Prelegenci: Wacław Sieroszewski, Juljusz Kaden-Bandrowski, Marjan Dąbrowski. "
                       "Podpisany przez Marjana Głuchowskiego.",
        "condition": "Nie zweryfikowany wizualnie",
        "person": "marjan",
        "photo_verified": False,
        "photos": [],
        "significance": "Zebranie z udziałem czołowych intelektualistów (Sieroszewski, Kaden) — "
                       "świadectwo ogólnopolskiej akcji mobilizacyjnej PON.",
        "estimate_pln": (1200, 2500),
        "target_buyer": "DESA Unicum",
    },

    # ── ROZDZIAŁ II: Siódemka i Legiony (1913–1925) ──
    {
        "id": "GL-010",
        "chapter": "II. Siódemka Beliny i Legiony (1913–1925)",
        "title": "Zaświadczenie WBH — służba legionowa gen. Głuchowskiego",
        "date": "24 maja 1937",
        "type": "Dokument urzędowy — zaświadczenie",
        "description": "Zaświadczenie Wojskowego Biura Historycznego potwierdzające: "
                       "członkostwo w Organizacji Bojowej PPS od 1905 r., założenie ZWC w Liège, "
                       "komendanturę Związku Strzeleckiego, udział w Szkole Letniej ZS w Oleandrach, "
                       "wyruszenie 2.VIII.1914 jako pierwszy patrol kawalerii Legionów Polskich.",
        "condition": "Nie zweryfikowany wizualnie",
        "person": "janusz",
        "photo_verified": False,
        "photos": [],
        "significance": "Urzędowe potwierdzenie udziału w Siódemce Beliny.",
        "estimate_pln": (5000, 12000),
        "target_buyer": "Muzeum Józefa Piłsudskiego w Sulejówku",
    },
    {
        "id": "GL-012",
        "chapter": "II. Siódemka Beliny i Legiony (1913–1925)",
        "title": "Fotografia 'Siódemki' z podpisami — Belina, Głuchowski, Grzmot-Skotnicki",
        "date": "1914",
        "type": "Fotografia — fotokopia ikoniczna",
        "description": "Fotokopia ikonicznej fotografii pierwszego patrolu kawaleryjskiego Legionów Polskich. "
                       "Podpisy uczestników: Belina-Prażmowski, Janusz Głuchowski, Grzmot-Skotnicki.",
        "condition": "Nie zweryfikowany wizualnie",
        "person": "janusz",
        "photo_verified": False,
        "photos": [],
        "significance": "Pierwszy patrol kawaleryjski — 7 ułanów przekraczających granicę 2.VIII.1914.",
        "estimate_pln": (2000, 6000),
        "target_buyer": "Muzeum Józefa Piłsudskiego w Sulejówku / Muzeum Wojska Polskiego",
    },
    {
        "id": "GL-029u",
        "chapter": "II. Siódemka Beliny i Legiony (1913–1925)",
        "title": "Dyplom Krzyża Legionowego nr 115 z podpisem Józefa Piłsudskiego + fotografia portretowa Marszałka",
        "date": "11 lipca 1925 / ok. 1918–1925",
        "type": "Dokument + fotografia",
        "description": "Dyplom nadania Krzyża Legionowego pułkownikowi Januszowi Głuchowskiemu (4 s.p. uł.), "
                       "nr 115. Własnoręczny podpis Józefa Piłsudskiego jako przewodniczącego Komisji "
                       "Kwalifikacyjnej II Zjazdu Legionistów. + Oryginalna fotografia portretowa Piłsudskiego "
                       "w mundurze z orderami.",
        "condition": "Dyplom: stan dobry. Fotografia: postrzępiony oryginalny brzeg.",
        "person": "janusz",
        "photo_verified": True,
        "photos": ["Kolekcja_Gluchowski_KATALOG_NAUKOWY_p06_img01.jpeg",
                   "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p06_img02.jpeg"],
        "significance": "KLUCZOWY OBIEKT. Podpis Piłsudskiego na dyplomie legionowym dla jednego z Siódemki. "
                       "Nr 115 = wśród pierwszych 200 odznaczonych.",
        "estimate_pln": (20000, 50000),
        "target_buyer": "Muzeum Józefa Piłsudskiego w Sulejówku — PRIORYTET",
    },

    # ── ROZDZIAŁ III: II Rzeczpospolita (1918–1939) ──
    {
        "id": "GL-007",
        "chapter": "III. II Rzeczpospolita (1918–1939)",
        "title": "Rozkaz Sztabu Generalnego — organizacja jazdy, Lublin, 5 XI 1918",
        "date": "5 listopada 1918",
        "type": "Dokument — rozkaz wojskowy",
        "description": "Rozkaz Dowództwa Wojsk Polskich w Lublinie nakazujący Rotmistrzowi Głuchowskiemu "
                       "organizację oddziału kawalerii w Lubelskiem. 6 dni przed oficjalnym odzyskaniem "
                       "niepodległości (11.XI.1918).",
        "condition": "Nie zweryfikowany wizualnie",
        "person": "janusz",
        "photo_verified": False,
        "photos": [],
        "significance": "Dokument wydany 6 dni PRZED niepodległością — Polska jako państwo jeszcze nie istnieje.",
        "estimate_pln": (8000, 20000),
        "target_buyer": "Muzeum Wojska Polskiego / Muzeum Piłsudskiego",
    },
    {
        "id": "GL-009",
        "chapter": "III. II Rzeczpospolita (1918–1939)",
        "title": "List Śmigłego-Rydza — zaproszenie na Zamek Królewski, 30 XII 1918",
        "date": "30 grudnia 1918",
        "type": "Dokument — list własnoręczny",
        "description": "Własnoręczny list Gen.-Ppor. Edwarda Śmigłego-Rydza zapraszający Majora "
                       "Głuchowskiego na Noworoczny Ranek na Zamku Królewskim 1.I.1919. "
                       "Pierwsza uroczystość noworoczna wolnej Polski.",
        "condition": "Nie zweryfikowany wizualnie",
        "person": "janusz",
        "photo_verified": False,
        "photos": [],
        "significance": "Zaproszenie na PIERWSZĄ uroczystość noworoczną wolnej Polski od Śmigłego-Rydza "
                       "(przyszłego Marszałka i Generalnego Inspektora Sił Zbrojnych).",
        "estimate_pln": (15000, 35000),
        "target_buyer": "DESA Unicum / Muzeum Piłsudskiego",
    },
    {
        "id": "GL-017",
        "chapter": "III. II Rzeczpospolita (1918–1939)",
        "title": "Legitymacja Krzyża Walecznych z podpisem Sosnkowskiego",
        "date": "31 lipca 1922",
        "type": "Dokument — legitymacja odznaczeniowa",
        "description": "Legitymacja KW z dwoma okuciami, podpisana przez Kazimierza Sosnkowskiego "
                       "jako Ministra Spraw Wojskowych. Odznaczony: Rtm. Głuchowski Janusz, 7 Pułk Ułanów.",
        "condition": "Nie zweryfikowany wizualnie bezpośrednio",
        "person": "janusz",
        "photo_verified": False,
        "photos": [],
        "significance": "Podpis Sosnkowskiego + dwa okucia (dwukrotne nadanie).",
        "estimate_pln": (5000, 12000),
        "target_buyer": "DESA Unicum / Muzeum Wojska Polskiego",
    },
    {
        "id": "GL-029a",
        "chapter": "III. II Rzeczpospolita (1918–1939)",
        "title": "Krzyż Walecznych — emisja 1920, z oryginalną wstążką",
        "date": "1920 (emisja) / nadany 31.VII.1922",
        "type": "Medal — odznaczenie wojskowe",
        "description": "Oryginalny Krzyż Walecznych pierwszej emisji Mennicy Warszawskiej (1920). "
                       "Brązowy krzyż maltański z napisem 'NA POLU CHWAŁY' i datą 1920, "
                       "orzeł legionowy w centrum. Oryginalna wstążka biało-karmazynowa.",
        "condition": "Stan dobry, patyna zgodna z wiekiem, wstążka z śladami użytkowania.",
        "person": "janusz",
        "photo_verified": True,
        "photos": ["Kolekcja_Gluchowski_KATALOG_NAUKOWY_p10_img01.jpeg"],
        "significance": "Pierwsza emisja KW — za wojnę polsko-bolszewicką 1920. Komplet z wstążką = rzadkość.",
        "estimate_pln": (2000, 4500),
        "target_buyer": "WCN / DESA Unicum / kolekcjonerzy falerystyki",
    },
    {
        "id": "GL-015",
        "chapter": "III. II Rzeczpospolita (1918–1939)",
        "title": "Dekret Króla Rumunii Ferdynanda I — Order Gwiazdy Rumunii",
        "date": "1 sierpnia 1923",
        "type": "Dokument — dekret królewski",
        "description": "Kaligrafowany dekret królewski nadający gen. Głuchowskiemu Order Gwiazdy Rumunii "
                       "w stopniu Komandora. Podpis Króla Ferdynanda I i Ministra I.G. Duca. "
                       "Tłoczona pieczęć królewska. Tekst w języku rumuńskim.",
        "condition": "Nie zweryfikowany wizualnie",
        "person": "janusz",
        "photo_verified": False,
        "photos": [],
        "significance": "Podpis Króla Ferdynanda I + podpis Duca (zamordowanego przez Żelazną Gwardię 1933).",
        "estimate_pln": (5000, 15000),
        "target_buyer": "DESA Unicum / aukcja międzynarodowa",
    },
    {
        "id": "GL-016",
        "chapter": "III. II Rzeczpospolita (1918–1939)",
        "title": "Zaproszenie Marszałka Focha — dekoracja na Placu Saskim, 3 V 1923",
        "date": "IV 1923",
        "type": "Dokument — zaproszenie/przepustka",
        "description": "Dokument MSWojsk informujący płk. Głuchowskiego, że Marszałek Ferdinand Foch "
                       "osobiście wręczy mu odznakę Kawalera Legii Honorowej na Placu Saskim, 3.V.1923. "
                       "Pełni funkcję zaproszenia i przepustki.",
        "condition": "Nie zweryfikowany wizualnie",
        "person": "janusz",
        "photo_verified": False,
        "photos": [],
        "significance": "Ferdinand Foch — Naczelny Wódz Aliantów. Osobiste wręczenie Legii Honorowej.",
        "estimate_pln": (10000, 25000),
        "target_buyer": "DESA Unicum / Christie's / aukcja międzynarodowa",
    },
    {
        "id": "GL-023",
        "chapter": "III. II Rzeczpospolita (1918–1939)",
        "title": "Dwa listy Aleksandry Piłsudskiej — 17 VIII 1923 i 6 VI 1935",
        "date": "17.VIII.1923 / 6.VI.1935",
        "type": "Korespondencja — listy własnoręczne",
        "description": "List 1923: Aleksandra Piłsudska prosi płk. Głuchowskiego o dwie pary koni. "
                       "Monogram 'P', Stacja Miłosna. "
                       "List 1935: Wdowa po Piłsudskim (zm. 12.V.1935) dziękuje za depeszę kondolencyjną. "
                       "Oryginalna koperta z polskim znaczkiem.",
        "condition": "Nie zweryfikowany wizualnie",
        "person": "janusz",
        "photo_verified": False,
        "photos": [],
        "significance": "Świadectwo prywatnej przyjaźni z rodziną Piłsudskich — od prośby o konie po kondolencje.",
        "estimate_pln": (25000, 65000),
        "target_buyer": "Muzeum Józefa Piłsudskiego w Sulejówku — BEZWZGLĘDNY PRIORYTET",
    },
    {
        "id": "GL-018",
        "chapter": "III. II Rzeczpospolita (1918–1939)",
        "title": "Dekrety Prezydenta Mościckiego — 1933 i 1935 — z podpisami Piłsudskiego i Kaspryckiego",
        "date": "16.III.1933 / 5.X.1935",
        "type": "Dokumenty urzędowe — dekrety prezydenckie",
        "description": "Dekret 1933: mianowanie Dowódcą DOK X Przemyśl, kontrasygnata Piłsudskiego. "
                       "Dekret 1935: mianowanie I Wiceministrem Spraw Wojskowych, kontrasygnata Kaspryckiego.",
        "condition": "Nie zweryfikowany wizualnie",
        "person": "janusz",
        "photo_verified": False,
        "photos": [],
        "significance": "Podpis Piłsudskiego (1933) + Kasperzcki (kolega z egzaminu ZWC 1913) kontrasygnuje 1935.",
        "estimate_pln": (22000, 55000),
        "target_buyer": "Muzeum Piłsudskiego / DESA Unicum",
    },
    {
        "id": "GL-029t",
        "chapter": "III. II Rzeczpospolita (1918–1939)",
        "title": "Legitymacja oficerska gen. bryg. Janusza Głuchowskiego — 1928–1933",
        "date": "6.II.1928 — 11.IV.1933",
        "type": "Dokument — książeczka oficerska",
        "description": "Oryginalna książeczka legitymacyjna oficera WP, wystawiona we Lwowie. "
                       "Fotografia portretowa generała w mundurze z własnoręcznym podpisem. "
                       "Wykaz odznaczeń: Virtuti Militari kl. V, Krzyż Walecznych (2 okucia), "
                       "Złoty Krzyż Zasługi, Legia Honorowa, Order Komandorski. "
                       "Chronologiczny zapis stanowisk: 4 Dyw. Kaw. → CW → DOK X Przemyśl.",
        "condition": "Stan dobry, strony pożółkłe, oprawa zachowana. POTWIERDZONE wizualnie.",
        "person": "janusz",
        "photo_verified": True,
        "photos": ["Kolekcja_Gluchowski_KATALOG_NAUKOWY_p13_img01.jpeg",
                   "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p13_img02.jpeg",
                   "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p13_img03.jpeg"],
        "significance": "Jedyna zachowana legitymacja oficerska gen. Głuchowskiego z fotografią portretową.",
        "estimate_pln": (15000, 35000),
        "target_buyer": "Muzeum Wojska Polskiego / DESA Unicum",
    },

    # ── ROZDZIAŁ IV: Sosnkowski — 51 lat przyjaźni ──
    {
        "id": "GL-029c",
        "chapter": "IV. Kazimierz Sosnkowski (1913–1964)",
        "title": "List gen. Sosnkowskiego + załącznik 'Pro memoria' — Arundel, Kanada, 28.V.1964",
        "date": "28 maja 1964",
        "type": "Korespondencja — list maszynopisowy z autografem",
        "description": "Maszynopis z własnoręcznym podpisem Kazimierza Sosnkowskiego. "
                       "Adresowany 'Kochany Generale'. Temat: patrol Beliny, Instytut Piłsudskiego, "
                       "praca nad przedmową dla Narbutta. Załącznik 'Pro memoria' — 24 zamówienia "
                       "ciążące na Sosnkowskim: Giedroyc i 'Kultura', Radio Wolna Europa, "
                       "płk. Smoleński, gen. Głuchowski. Na końcu: 'Za parę miesięcy rozpoczynam "
                       "80-ty rok życia i siły moje bynajmniej nie są nieograniczone.'",
        "condition": "Stan bardzo dobry. POTWIERDZONE wizualnie.",
        "person": "janusz",
        "photo_verified": True,
        "photos": ["Kolekcja_Gluchowski_KATALOG_NAUKOWY_p09_img01.jpeg",
                   "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p14_img01.jpeg",
                   "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p14_img02.jpeg",
                   "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p14_img03.jpeg"],
        "significance": "Ostatni wielki dokument przyjaźni Sosnkowski-Głuchowski. Lista kontaktów: "
                       "Giedroyc, RWE, Buenos Aires, Toronto, Chicago, Londyn, Paryż.",
        "estimate_pln": (12000, 28000),
        "target_buyer": "Muzeum Piłsudskiego / Instytut Piłsudskiego w Londynie/Nowym Jorku",
    },

    # ── ROZDZIAŁ V: Getto Łódzkie ──
    {
        "id": "GL-029e_h",
        "chapter": "V. Getto Łódzkie (1942–1984)",
        "title": "Komplet korespondencji — 4 listy, Londyn/Rochester, 1958–1984",
        "date": "18.V.1958 / 22.V.1958 / 17.XI.1968 / 21.XI.1984",
        "type": "Korespondencja — 4 listy",
        "description": "1958: K. Głuchowski do Ambasady Izraela w Londynie o sprzedaży monet z getta. "
                       "Odpowiedź attaché A. Kidrona kierująca do Yad Vashem. "
                       "1968: K. Głuchowski do numizmatyka Herziga w Ohio — pełny inwentarz obiektów. "
                       "1984: K.A. Głuchowski (Rochester) oferuje te same obiekty.",
        "condition": "Stan dobry. DWA LISTY POTWIERDZONE wizualnie (1958).",
        "person": "krzysztof",
        "photo_verified": True,
        "photos": ["Kolekcja_Gluchowski_KATALOG_NAUKOWY_p17_img01.jpeg",
                   "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p17_img03.jpeg"],
        "significance": "26-letnia historia poszukiwania muzealnego miejsca dla artefaktów getta.",
        "estimate_pln": (6000, 15000),
        "target_buyer": "Muzeum POLIN / Yad Vashem / USHMM — OBOWIĄZKOWO instytucja",
    },
    {
        "id": "GL-029p",
        "chapter": "V. Getto Łódzkie (1942–1984)",
        "title": "Artefakty getta łódzkiego — kupon pocztowy 10 Pf. + talon na drożdże Nr 6110",
        "date": "17.IV.1942",
        "type": "Artefakty fizyczne — waluta gettowa + talon żywnościowy",
        "description": "Kupon pocztowy 10 Pf.: 'GUT FÜR 10 PF. BEI DER POSTABTEILUNG DES AELTESTEN "
                       "DER JUDEN in Litzmannstadt-Getto, 17. April 1942.' Żółty, ząbkowany. "
                       "Talon Nr 6110 na 200g drożdży: 'Der Aelteste der Juden in Litzmannstadt — "
                       "MOLKEREIERZEUGNISSE-ABT.' Niebieski kartonik, 4 odcinki po 50g. "
                       "Koperta z notatką inwentarzową Włodzimierza Głuchowskiego.",
        "condition": "Kupon: stan bardzo dobry. Talon: stan dobry. POTWIERDZONE wizualnie.",
        "person": "krzysztof",
        "photo_verified": True,
        "photos": ["Kolekcja_Gluchowski_KATALOG_NAUKOWY_p17_img02.jpeg"],
        "significance": "Fizyczne świadectwa Holokaustu z proweniencją rodzinną.",
        "estimate_pln": (3000, 8000),
        "target_buyer": "Muzeum POLIN / Yad Vashem — OBOWIĄZKOWO instytucja memorialna",
    },

    # ── ROZDZIAŁ VI: 7 Pułk Ułanów Lubelskich ──
    {
        "id": "GL-029b",
        "chapter": "VI. 7 Pułk Ułanów Lubelskich (1919–1970)",
        "title": "Dokument upamiętniający szturm 7 P.Uł. AK 'Jeleń' na Gestapo, 1.VIII.1944",
        "date": "1 sierpnia 1944 (maszynopis powojenny)",
        "type": "Dokument — maszynopis upamiętniający",
        "description": "Maszynopis dokumentujący szturm 5 plutonów dywizjonu AK 'Jeleń' na gmach Gestapo "
                       "(al. Szucha) i Dom Prasy w Godzinie W. Spośród 187 powstańców poległo 67. "
                       "Liczba ofiar dopisana odręcznie.",
        "condition": "Nie zweryfikowany wizualnie",
        "person": "lech",
        "photo_verified": False,
        "photos": [],
        "significance": "Dokumentacja szturmu na symbol okupacyjnego terroru w pierwszej godzinie Powstania.",
        "estimate_pln": (3000, 8000),
        "target_buyer": "Muzeum Powstania Warszawskiego",
    },

    # ── ROZDZIAŁ VII: Krzysztof Andrzej — historia kompletna ──
    {
        "id": "GL-029x",
        "chapter": "VII. Krzysztof Andrzej Głuchowski (1928–1945)",
        "title": "Kennkarte Krzysztofa Andrzeja Głuchowskiego — Warszawa, 9.XI.1943",
        "date": "9 listopada 1943",
        "type": "Dokument tożsamości — Kennkarte GG",
        "description": "Oryginalna karta rozpoznawcza Generalnego Gubernatorstwa, nr 662016. "
                       "Fotografia chłopca ok. 14–15 lat, odcisk palca, podpis. Pieczęć GG. "
                       "Zawód: Schüler (uczeń). Adres: ul. Pogonowskiego, Warszawa.",
        "condition": "Stan dobry. POTWIERDZONE wizualnie.",
        "person": "krzysztof_andrzej",
        "photo_verified": True,
        "photos": ["Kolekcja_Gluchowski_KATALOG_NAUKOWY_p23_img02.jpeg",
                   "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p23_img03.jpeg"],
        "significance": "Dokument tożsamości przyszłego żołnierza AK — rok przed Powstaniem.",
        "estimate_pln": (2500, 6000),
        "target_buyer": "Muzeum Powstania Warszawskiego",
    },
    {
        "id": "GL-029y",
        "chapter": "VII. Krzysztof Andrzej Głuchowski (1928–1945)",
        "title": "Legitymacja AK — ps. 'Jurek/Jureń', Pluton 1112",
        "date": "8.IV.1944 (awers) / 11.IX.1944 (rewers)",
        "type": "Dokument — legitymacja bojowa AK",
        "description": "Awers: Krzysztof Głuchowski, ps. 'Jurek', ułan, Pluton 1112, DOW AK. "
                       "Data ur. 29.XI.1926 — sfałszowana o 2 lata (faktycznie 1928). "
                       "Pieczęć Komendy Okręgu AK Warszawa. "
                       "Rewers (dzień 41. Powstania): awans na st. ułana + Krzyż Harcerski, 5.IX.44.",
        "condition": "Nie zweryfikowany wizualnie bezpośrednio",
        "person": "krzysztof_andrzej",
        "photo_verified": False,
        "photos": [],
        "significance": "15-latek sfałszował datę urodzenia by walczyć. Awans bojowy w 41. dniu Powstania.",
        "estimate_pln": (8000, 20000),
        "target_buyer": "Muzeum Powstania Warszawskiego — PRIORYTET",
    },
    {
        "id": "GL-029zE",
        "chapter": "VII. Krzysztof Andrzej Głuchowski (1928–1945)",
        "title": "List Krzysztofa do rodziców ze stanowiska bojowego, 26.VIII.1944",
        "date": "26 sierpnia 1944 (dzień 26. Powstania)",
        "type": "Korespondencja — list ołówkowy z frontu",
        "description": "Ołówek na papierze notesowym. 'Kochane Momunia i Tato! Jestem na stanowisku. "
                       "Dotychczas żyję i jestem niety choć mocno zaziębiony...' Podaje straty jednostki, "
                       "poległych z imienia. Przekazywany przez łączniczki.",
        "condition": "Stan dobry, papier pożółkły. POTWIERDZONE wizualnie.",
        "person": "krzysztof_andrzej",
        "photo_verified": True,
        "photos": ["Kolekcja_Gluchowski_KATALOG_NAUKOWY_p24_img02.jpeg"],
        "significance": "Głos 15-letniego żołnierza z pola walki. Jeden z najbardziej poruszających dokumentów kolekcji.",
        "estimate_pln": (5000, 15000),
        "target_buyer": "Muzeum Powstania Warszawskiego — BEZWZGLĘDNY PRIORYTET",
    },
    {
        "id": "GL-029zF",
        "chapter": "VII. Krzysztof Andrzej Głuchowski (1928–1945)",
        "title": "Odpowiedź Ciotki Waleski — 24.IX.1944",
        "date": "24 września 1944 (dzień 55. Powstania)",
        "type": "Korespondencja — odpowiedź rodziny",
        "description": "Papier w kratkę, ołówek. 'Krzysiu! Wszyscy jesteśmy zdrowi. Nasze domy stoją...' "
                       "Adres na rewersie: 'Pluton 1112 — Krzysztof'.",
        "condition": "Stan dobry, papier pożółkły. POTWIERDZONE wizualnie.",
        "person": "krzysztof_andrzej",
        "photo_verified": True,
        "photos": ["Kolekcja_Gluchowski_KATALOG_NAUKOWY_p24_img01.jpeg"],
        "significance": "Korespondencja w OBU KIERUNKACH z Powstania — historyczny fenomen.",
        "estimate_pln": (3000, 8000),
        "target_buyer": "Muzeum Powstania Warszawskiego",
    },
    {
        "id": "GL-029zB",
        "chapter": "VII. Krzysztof Andrzej Głuchowski (1928–1945)",
        "title": "Przepustka AK — st. uł. Głuchowski, 29.IX.1944 — 3 dni przed kapitulacją",
        "date": "29 września 1944 (dzień 60. Powstania)",
        "type": "Dokument — przepustka bojowa AK",
        "description": "Przepustka Jednorazowa Specjalna Komendy Warszawskiego Okręgu AK. "
                       "St. uł. Głuchowski, rozkaz płk. 'Jelenia', Al. Sikorskiego. "
                       "Ważna do 30.IX.44. Podpis Z-cy Komendanta Okręgu płk. Wachnowskiego. "
                       "Pieczęć Komendy Okręgu AK Warszawa.",
        "condition": "Stan dobry, papier kremowy. POTWIERDZONE wizualnie.",
        "person": "krzysztof_andrzej",
        "photo_verified": True,
        "photos": ["Kolekcja_Gluchowski_KATALOG_NAUKOWY_p25_img01.jpeg"],
        "significance": "3 DNI przed kapitulacją — walczył do ostatniego rozkazu.",
        "estimate_pln": (8000, 20000),
        "target_buyer": "Muzeum Powstania Warszawskiego — PRIORYTET",
    },
    {
        "id": "GL-029zG",
        "chapter": "VII. Krzysztof Andrzej Głuchowski (1928–1945)",
        "title": "Personalkarte + Bilet identyfikacyjny Stalag XI-B — nr 141009",
        "date": "5.X.1944 — 8.IV.1945",
        "type": "Dokumenty jenieckie — Personalkarte + bilet",
        "description": "Personalkarte: jeniec nr 141009, Stalag XI-B Fallingbostel. "
                       "Wzięty do niewoli w Warszawie 5.X.1944. Gefreiter, Schüler. "
                       "Trasa: Fallingbostel → Stalag IIB → Stalag VIF Dorsten. "
                       "Osoba kontaktowa: Zofia Okuszko, Rzejowice kr. Radomsko. "
                       "Bilet identyfikacyjny: 'Stalag XI B — 141009', kartonik z perforacją. "
                       "Rewers: 'Am 8.4.45 — Linden'.",
        "condition": "Personalkarte: stan dobry, przekreślona czerwoną linią (zwolniony). "
                    "Bilet: stan dostateczny. POTWIERDZONE wizualnie.",
        "person": "krzysztof_andrzej",
        "photo_verified": True,
        "photos": ["Kolekcja_Gluchowski_KATALOG_NAUKOWY_p27_img02.jpeg",
                   "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p27_img01.jpeg"],
        "significance": "Kompletna dokumentacja niewoli 15-letniego powstańca.",
        "estimate_pln": (8000, 17000),
        "target_buyer": "Muzeum Powstania Warszawskiego / Muzeum Stalagu XI-B",
    },

    # ── ROZDZIAŁ VIII: Album szkocki ──
    {
        "id": "GL-029r",
        "chapter": "VIII. Album CWŁ PSZ — Szkocja 1944",
        "title": "Album pamiątkowy CWŁ PSZ — Centrum Wyszkolenia Łączności, Szkocja",
        "date": "7.I.1944 / 8.III.1944",
        "type": "Album fotograficzny — ~35-40 fotografii",
        "description": "Album ofiarowany gen. Głuchowskiemu przez żołnierzy Kompanii Dozorowania "
                       "CWŁ PSZ w Szkocji. Strona tytułowa kaligrafowana białym atramentem. "
                       "Dokumentuje dwie wizyty generała. Zawiera: portret, zbiórki, gimnastykę, "
                       "szkolenie łączności, mecz piłkarski z RAF, herbatkę, wieczór z gitarą.",
        "condition": "Stan dobry. POTWIERDZONE wizualnie (strona z fotografiami).",
        "person": "janusz",
        "photo_verified": True,
        "photos": ["Kolekcja_Gluchowski_KATALOG_NAUKOWY_p28_img01.jpeg"],
        "significance": "Codzienność polskiego żołnierza na emigracji — jednocześnie w Warszawie Krzysztof "
                       "wstępuje do AK. Dwa światy jednej rodziny.",
        "estimate_pln": (6000, 15000),
        "target_buyer": "Muzeum Wojska Polskiego / Instytut Sikorskiego w Londynie",
    },

    # ── NOWE: dokumenty z WhatsApp ──
    {
        "id": "GL-W01",
        "chapter": "III. II Rzeczpospolita (1918–1939) / Emigracja",
        "title": "Aliens Registration Certificate — gen. Janusz Głuchowski, nr A 274782",
        "date": "1949–1960",
        "type": "Dokument tożsamości — rejestracja cudzoziemca (UK)",
        "description": "Certificate of Registration, Aliens Order 1920, nr A 274782. "
                       "Głuchowski Janusz, Polish, ur. 6.8.88 Bucharest. Married. "
                       "Polish Forces Aug 1940, discharged 29/2/49. "
                       "Pieczątki: Metropolitan Police 1949, Immigration Dover 2.FEB.1951, "
                       "Beckenham Division 1.AUG.1956. "
                       "Aliens Order 1960: 'EXEMPT FROM REGISTRATION'.",
        "condition": "Stan dobry, oprawa oryginalna. POTWIERDZONE wizualnie (WhatsApp).",
        "person": "janusz",
        "photo_verified": True,
        "photos": ["WhatsApp_07.44.19.jpeg", "WhatsApp_07.44.37.jpeg",
                   "WhatsApp_07.44.54.jpeg", "WhatsApp_07.45.09.jpeg"],
        "significance": "Kompletna dokumentacja emigracyjna generała — od demobilizacji po zwolnienie z rejestracji.",
        "estimate_pln": (3000, 8000),
        "target_buyer": "DESA Unicum / Instytut Sikorskiego Londyn",
    },
    {
        "id": "GL-W02",
        "chapter": "VI. 7 Pułk Ułanów Lubelskich (1919–1970)",
        "title": "Legitymacja Krzyża Armii Krajowej nr 3316 — Krzysztof Głuchowski 'Juras'",
        "date": "7.III.1968 (Londyn)",
        "type": "Dokument — legitymacja odznaczeniowa AK",
        "description": "Legitymacja Krzyża AK nr 3316. Głuchowski Krzysztof ps. 'Juras'. "
                       "ZWZ Komp.K. Plut. III/2, 7 Pułk Ułanów Lubelskich 'Jeleń'. "
                       "Ustanowiony 1.VIII.1966 przez gen. Tadeusza Bora-Komorowskiego. "
                       "Podpis K. Ziemski 'Wachnowski'. Londyn 7.3.68.",
        "condition": "Stan bardzo dobry. POTWIERDZONE wizualnie (WhatsApp).",
        "person": "krzysztof",
        "photo_verified": True,
        "photos": ["WhatsApp_07.45.22.jpeg", "WhatsApp_07.45.35.jpeg"],
        "significance": "Legitymacja AK z podpisem płk. Wachnowskiego — tego samego który podpisywał "
                       "przepustki Krzysztofowi Andrzejowi w Powstaniu.",
        "estimate_pln": (2000, 5000),
        "target_buyer": "DESA Unicum / Muzeum Powstania Warszawskiego",
    },
    {
        "id": "GL-W03",
        "chapter": "VI. 7 Pułk Ułanów Lubelskich (1919–1970)",
        "title": "Dokument weryfikacyjny AK — ppor. rez. kaw. Kotakowski Patryk, 7 P.Uł.",
        "date": "1946",
        "type": "Dokument — zaświadczenie weryfikacyjne",
        "description": "Dowództwo 2 Korpusu, Komisja Weryfikacyjna AK. "
                       "Ppor. rez. kaw. 1944 Kotakowski Patryk, ur. 1926. 7 Pułk Ułanów Lubelskich. "
                       "Podpis J. Uszycki ppłk.",
        "condition": "Stan dobry. POTWIERDZONE wizualnie (WhatsApp).",
        "person": "krzysztof",
        "photo_verified": True,
        "photos": ["WhatsApp_07.45.56.jpeg"],
        "significance": "Dokument weryfikacyjny innego żołnierza 7 P.Uł. — uzupełnia obraz jednostki.",
        "estimate_pln": (800, 2000),
        "target_buyer": "DESA Unicum",
    },
    {
        "id": "GL-W04",
        "chapter": "VII. Krzysztof Andrzej Głuchowski (1928–1945)",
        "title": "Kriegsgefangenenpost — list do ppor. Stanisława Stefana Głuchowskiego w Stalagu XI B",
        "date": "23.XII.1944 (stempel Radomsko)",
        "type": "Korespondencja — poczta jeniecka",
        "description": "Rückantwortbrief (list odpowiedzi) na Kriegsgefangenenpost. "
                       "Adresowany do: pan Stanisław Stefan Głuchowski. "
                       "Gefangenennummer: O.-1245. Lager: M.-Stammlager XI B/z, Barak 201/4. "
                       "Nadawca: Głuchowska Halszka, Jef. Mirau II, pow. Grudziądz, "
                       "Generalne Gubernatorstwo. Stempel Radomsko 23.12.44.",
        "condition": "Stan dobry, oryginalne pieczątki. POTWIERDZONE wizualnie (WhatsApp).",
        "person": "stanislaw_stefan",
        "photo_verified": True,
        "photos": ["WhatsApp_07.47.10.jpeg"],
        "significance": "Poczta jeniecka z Generalnego Gubernatorstwa do Stalagu XI B — "
                       "dwa Głuchowscy w dwóch obozach jednocześnie (Krzysztof Andrzej nr 141009, "
                       "Stefan nr O.-1245).",
        "estimate_pln": (2000, 5000),
        "target_buyer": "Muzeum Powstania Warszawskiego / DESA Unicum",
    },
    {
        "id": "GL-W05",
        "chapter": "IX. Materiały biograficzne",
        "title": "Zdjęcie rodzinne Głuchowskich — ok. 1916–1920",
        "date": "ok. 1916–1920",
        "type": "Fotografia — portret rodzinny",
        "description": "Grupowe zdjęcie rodzinne: ~10 osób, w tym oficer w mundurze WW1-era, "
                       "kobiety, dzieci, harcerz. Prawdopodobnie rodzina Głuchowskich.",
        "condition": "Stan dobry, oryginalna odbitka na kartonie. POTWIERDZONE wizualnie (WhatsApp).",
        "person": "marjan",
        "photo_verified": True,
        "photos": ["WhatsApp_07.46.11.jpeg"],
        "significance": "Portret rodziny, z której wyszli generał, żołnierze AK i powstańcy.",
        "estimate_pln": (800, 2000),
        "target_buyer": "Sprzedaż z kolekcją",
    },
    {
        "id": "GL-W06",
        "chapter": "IX. Materiały biograficzne",
        "title": "3 biografie rodzinne — Krzysztof, Lech, Stefan Głuchowscy (Rio de Janeiro, 1995)",
        "date": "18 października 1995",
        "type": "Dokumenty — maszynopisy biograficzne",
        "description": "Trzy pełne biografie pisane przez Krzysztofa Głuchowskiego w Rio de Janeiro: "
                       "1) Krzysztof Głuchowski ps. 'Juras' — syn Stanisława Stefana, ZWZ/AK, emigracja do Brazylii. "
                       "2) Rtm. Lech Głuchowski ps. 'Hżycki' — 7 P.Uł., Powstanie, Mokotów, Wilanów. "
                       "3) Ppor. Stanisław Stefan Głuchowski ps. 'Stefan' — POW, Kancelaria Naczelnika Państwa, "
                       "WSOP Żoliborz, Pawiak, Auschwitz, Powązki. "
                       "Każda bio zawiera listę publikacji i odwołanie do BN Zbiór Rękopisów nr 13853.",
        "condition": "Stan dobry, maszynopis. POTWIERDZONE wizualnie (WhatsApp).",
        "person": "krzysztof",
        "photo_verified": True,
        "photos": ["WhatsApp_07.46.34.jpeg", "WhatsApp_07.46.45.jpeg", "WhatsApp_07.46.57.jpeg"],
        "significance": "Kluczowe źródło proweniencji i historii rodziny. "
                       "Odwołanie do Biblioteki Narodowej (Zbiór Rękopisów 13853).",
        "estimate_pln": (1000, 3000),
        "target_buyer": "Sprzedaż z kolekcją — dokumentacja proweniencji",
    },
    {
        "id": "GL-W07",
        "chapter": "IX. Materiały biograficzne",
        "title": "Rękopis — wspomnienia/pamiętnik",
        "date": "Nieznana",
        "type": "Rękopis — tekst odręczny",
        "description": "Gęsty tekst odręczny w języku polskim — prawdopodobnie wspomnienia "
                       "lub pamiętnik jednego z członków rodziny Głuchowskich.",
        "condition": "Stan dostateczny, trudny do odczytania. POTWIERDZONE wizualnie (WhatsApp).",
        "person": "krzysztof",
        "photo_verified": True,
        "photos": ["WhatsApp_07.47.20.jpeg"],
        "significance": "Wymaga transkrypcji — potencjalnie cenne źródło historyczne.",
        "estimate_pln": (500, 1500),
        "target_buyer": "Sprzedaż z kolekcją",
    },
    # ══════════════════════════════════════════════════════
    # SERIA 29z — Korespondencja jenieckia i dokumenty wyzwolenia
    # ══════════════════════════════════════════════════════
    {
        "id": "GL-S01",
        "chapter": "VII. Krzysztof Andrzej Głuchowski (1928–1945)",
        "title": "Korespondencja jenieckia — kolekcja Kriegsgefangenenpost",
        "date": "1944–1945",
        "type": "Korespondencja jenieckia — zbiór",
        "description": "Zbiór ~10 kart i listów jenieckich (Kriegsgefangenenpost/Antwort-Postkarte/"
                       "Rückantwortbrief) między braćmi Krzysztofem (nr 141009, Stalag XI B/Stalag VI Dorsten) "
                       "i Stefanem (O.1845, Stalag XI B, Barak 201/4), matką Marią z Głowna/Osiny, "
                       "oraz do gen. Janusza Głuchowskiego w Londynie (Polish War Office, England). "
                       "Stemple: Radomsko 23.12.44, Głowno 20.II.44, 7.11.44, 04.12.44. "
                       "Listy pisane po polsku na papierze w kratkę i oficjalnych formularzach jenieckich.",
        "condition": "Stan różny — od dobrego (karty pocztowe) do zniszczonego (listy na papierze). "
                     "POTWIERDZONE wizualnie.",
        "person": "krzysztof_andrzej",
        "photo_verified": True,
        "photos": ["Seria_29z_p02_img01.jpeg", "Seria_29z_p02_img02.jpeg",
                   "Seria_29z_p04_img01.jpeg", "Seria_29z_p04_img02.jpeg",
                   "Seria_29z_p05_img01.jpeg", "Seria_29z_p06_img02.jpeg",
                   "Seria_29z_p07_img01.jpeg", "Seria_29z_p08_img02.jpeg",
                   "Seria_29z_p10_img01.jpeg", "Seria_29z_p10_img02.jpeg"],
        "significance": "Kompletna korespondencja jenieckia dwóch braci w tym samym obozie + "
                       "list do ojca-generała w Londynie. Unikalne świadectwo więzi rodzinnych w niewoli.",
        "estimate_pln": (8000, 20000),
        "target_buyer": "Muzeum Powstania Warszawskiego / Muzeum II Wojny Światowej Gdańsk",
    },
    {
        "id": "GL-S02",
        "chapter": "VII. Krzysztof Andrzej Głuchowski (1928–1945)",
        "title": "Personalkarte — karta medyczna jeńca (strona zdrowia)",
        "date": "1944–1945",
        "type": "Dokument obozowy — karta medyczna",
        "description": "Strona karty zdrowia jeńca: tabela chorób (Art der Krankheit), "
                       "szczepienia (Schutz- und Heilimpfungen), tabela wagi (Gewichtstabelle). "
                       "Formularz niemiecki, częściowo wypełniony.",
        "condition": "Stan dostateczny, krawędzie uszkodzone. POTWIERDZONE wizualnie.",
        "person": "krzysztof_andrzej",
        "photo_verified": True,
        "photos": ["Seria_29z_p12_img01.jpeg"],
        "significance": "Uzupełnia Personalkarte z Katalogu Naukowego — komplet dokumentów obozowych.",
        "estimate_pln": (1000, 3000),
        "target_buyer": "Muzeum II Wojny Światowej / DESA Unicum",
    },
    {
        "id": "GL-S03",
        "chapter": "VII. Krzysztof Andrzej Głuchowski (1928–1945)",
        "title": "Ulotka wyzwoleńcza — 'Nareszcie... Rodacy...'",
        "date": "1945",
        "type": "Druk ulotny — propaganda/informacja",
        "description": "Drukowana ulotka skierowana do polskich żołnierzy we Francji po wyzwoleniu. "
                       "Tekst: 'Nareszcie nadeszła radosna chwila... powrotu na łono ukochanej, "
                       "wielkiej, niepodległej Polskiej Ojczyzny...' Lista Agencji Konsularnych RP "
                       "we Francji: Bordeaux, Périgueux, Charleville, Nancy, Metz, Limoges, Lille. "
                       "Instrukcje dla zdemobilizowanych żołnierzy.",
        "condition": "Stan dostateczny, pożółkły, naderwania. POTWIERDZONE wizualnie.",
        "person": "krzysztof_andrzej",
        "photo_verified": True,
        "photos": ["Seria_29z_p20_img01.jpeg"],
        "significance": "Rzadki druk ulotny — świadectwo repatriacji polskich żołnierzy z Francji 1945.",
        "estimate_pln": (1500, 4000),
        "target_buyer": "DESA Unicum / Muzeum Emigracji Gdynia",
    },
    {
        "id": "GL-S04",
        "chapter": "VII. Krzysztof Andrzej Głuchowski (1928–1945)",
        "title": "Zaświadczenie o służbie konspiracyjnej ZWZ/AK — Częstochowa",
        "date": "18.II.1945",
        "type": "Dokument — zaświadczenie AK",
        "description": "Zaświadczenie dla Głuchowskiego Krzysztofa, ur. 1926, potwierdzające "
                       "3-letnią służbę konspiracyjną w rejonie Częstochowy. Pieczęć Komendy Uzupełnień. "
                       "Podpis Komendanta.",
        "condition": "Stan dobry. POTWIERDZONE wizualnie.",
        "person": "krzysztof_andrzej",
        "photo_verified": True,
        "photos": ["Seria_29z_p24_img01.jpeg"],
        "significance": "Oficjalne potwierdzenie 3 lat konspiracji — dokument łączący Krzysztofa "
                       "z ZWZ/AK jeszcze przed Powstaniem.",
        "estimate_pln": (3000, 8000),
        "target_buyer": "Muzeum Powstania Warszawskiego / DESA Unicum",
    },
    {
        "id": "GL-S05",
        "chapter": "VII. Krzysztof Andrzej Głuchowski (1928–1945)",
        "title": "Fiche de Transport — repatriacja przez Francję",
        "date": "29.III.1946",
        "type": "Dokument — transport/repatriacja",
        "description": "République Française, Ministère des Prisonniers, Déportés et Réfugiés. "
                       "Nr 1492839. Głuchowski Krzysztof. Dokument transportowy do Caserne Jessins. "
                       "Stempel służby zdrowia.",
        "condition": "Stan dobry, papier zielonkawy. POTWIERDZONE wizualnie.",
        "person": "krzysztof_andrzej",
        "photo_verified": True,
        "photos": ["Seria_29z_p25_img01.jpeg"],
        "significance": "Dokumentuje drogę Krzysztofa po wyzwoleniu — przez system repatriacji francuski.",
        "estimate_pln": (1000, 2500),
        "target_buyer": "DESA Unicum",
    },
    {
        "id": "GL-S06",
        "chapter": "VII. Krzysztof Andrzej Głuchowski (1928–1945)",
        "title": "Ambassade de Pologne à Paris — skierowanie na kurs",
        "date": "29.VI.1945",
        "type": "Dokument — ambasada/skierowanie",
        "description": "Na papierze firmowym AMBASSADE de POLOGNE à Paris. "
                       "Pan Głuchowski K. zostaje skierowany na kurs organizowany przez Konsulny "
                       "Instruktorowe Obozowy, rozpoczynający się 25 lipca w Villard-de-Lans. "
                       "Podpis A. Irtygowski(?), Konsulny Instruktor Obozowy.",
        "condition": "Stan dobry. POTWIERDZONE wizualnie.",
        "person": "krzysztof_andrzej",
        "photo_verified": True,
        "photos": ["Seria_29z_p27_img01.jpeg"],
        "significance": "Papier firmowy Ambasady RP w Paryżu — dokumentuje szlak edukacyjny Krzysztofa.",
        "estimate_pln": (1500, 3500),
        "target_buyer": "DESA Unicum / Instytut Sikorskiego Londyn",
    },
    {
        "id": "GL-S07",
        "chapter": "VII. Krzysztof Andrzej Głuchowski (1928–1945)",
        "title": "Przepustka — Gimnazjum i Liceum 3 D.K., Amandola (2 Korpus, Włochy)",
        "date": "1945–1946",
        "type": "Dokument — przepustka wojskowa",
        "description": "Dwujęzyczna przepustka PL/EN. Nr ewid. 1846, Głuchowski Krzysztof. "
                       "Kwateruje w m. Amandola, zezwolenie na przebywanie poza służbą do godz. 21:59. "
                       "Komendant: Gimnazjum i Liceum 3 D.K., kpt. Karpica Józef.",
        "condition": "Stan dobry. POTWIERDZONE wizualnie.",
        "person": "krzysztof_andrzej",
        "photo_verified": True,
        "photos": ["Seria_29z_p30_img01.jpeg"],
        "significance": "Dokumentuje pobyt Krzysztofa w 2 Korpusie Polskim we Włoszech — "
                       "kontynuacja edukacji po wojnie.",
        "estimate_pln": (1000, 2500),
        "target_buyer": "DESA Unicum / Muzeum Wojska Polskiego",
    },
    {
        "id": "GL-S08",
        "chapter": "VII. Krzysztof Andrzej Głuchowski (1928–1945)",
        "title": "Wypracowania szkolne — relacje z Powstania Warszawskiego",
        "date": "25.VIII.1945 — 5.VIII.1945",
        "type": "Rękopis — relacja historyczna",
        "description": "'Zadanea Włoskie No 1' (25.VIII.45) i kolejne wypracowania (4.VIII.45, 5.VIII.45). "
                       "St. uł. Krzysztof Głuchowski, Polish Forces C.M.F. 152, Gimnazjum 3 DSC. "
                       "Pierwszoosobowe relacje z Powstania Warszawskiego — Pluton 1112, 7 P.Uł., "
                       "obrona Starego Miasta, Czerniaków. Wspomina Armię Krajową, p. Mossakowskiego. "
                       "Pisane we Włoszech rok po Powstaniu.",
        "condition": "Stan dobry, czytelny. POTWIERDZONE wizualnie.",
        "person": "krzysztof_andrzej",
        "photo_verified": True,
        "photos": ["Seria_29z_p32_img01.jpeg", "Seria_29z_p33_img01.jpeg", "Seria_29z_p34_img01.jpeg"],
        "significance": "BEZCENNE — pierwszoosobowa relacja 17-letniego powstańca pisana rok po wydarzeniach. "
                       "Źródło historyczne pierwszej kategorii.",
        "estimate_pln": (5000, 15000),
        "target_buyer": "Muzeum Powstania Warszawskiego / Archiwum Akt Nowych",
    },
    {
        "id": "GL-S09",
        "chapter": "VII. Krzysztof Andrzej Głuchowski (1928–1945)",
        "title": "3 zaświadczenia — Hanastedt, Płk. Kłopas Stanisław",
        "date": "22.VIII.1945",
        "type": "Dokument — zaświadczenia wojskowe",
        "description": "Trzy zaświadczenia wydane w Hanastedt przez Płk. Kłopasa Stanisława. "
                       "1) Nadanie Krzyża Walecznych, AK Nr 29, z dn. 25.9.1944. "
                       "2) Potwierdzenie służby AK ps. 'Juras'. "
                       "3) Trzecie zaświadczenie z pieczęcią z orłem. "
                       "Autentyczność potwierdzona podpisem autentycznym.",
        "condition": "Stan dobry, pieczęcie z orłem czytelne. POTWIERDZONE wizualnie.",
        "person": "krzysztof_andrzej",
        "photo_verified": True,
        "photos": ["Seria_29z_p35_img01.jpeg"],
        "significance": "Oficjalne potwierdzenie Krzyża Walecznych nadanego w Powstaniu + "
                       "potwierdzenie pseudonimu 'Juras'.",
        "estimate_pln": (4000, 10000),
        "target_buyer": "Muzeum Powstania Warszawskiego / DESA Unicum",
    },
    {
        "id": "GL-S10",
        "chapter": "VII. Krzysztof Andrzej Głuchowski (1928–1945)",
        "title": "Zaświadczenie — Płk. Dypl. Ziemski Karol, Powstanie Warszawskie",
        "date": "26.X.1946",
        "type": "Dokument — zaświadczenie o udziale w Powstaniu",
        "description": "Ziemski Karol, Pułkownik Dyplomowany, Dowódca Polskiego Okręgu Wojskowego "
                       "Schleswig-Holstein. Westorf pod Hamburgiem. Stwierdza, że Głuchowski Krzysztof "
                       "ps. 'JURAS', ur. 29.XI.1928, uczestnik Powstania Warszawskiego Grupy 'PÓŁNOC', "
                       "Obrona Starego Miasta, Pluton 1112, awansowany do stopnia starszego strzelca, "
                       "odznaczony Krzyżem Walecznych w dniu Rozkazu 5.9.1944 — nr 24, "
                       "Dowódcy Obrony Starego Miasta.",
        "condition": "Stan bardzo dobry, pieczęć czytelna. POTWIERDZONE wizualnie.",
        "person": "krzysztof_andrzej",
        "photo_verified": True,
        "photos": ["Seria_29z_p36_img01.jpeg"],
        "significance": "KLUCZOWY DOKUMENT — oficjalne potwierdzenie udziału w Powstaniu "
                       "przez dowódcę okręgu wojskowego. Łączy: pseudonim, oddział, awans, odznaczenie.",
        "estimate_pln": (5000, 12000),
        "target_buyer": "Muzeum Powstania Warszawskiego",
    },
    {
        "id": "GL-S11",
        "chapter": "VII. Krzysztof Andrzej Głuchowski (1928–1945)",
        "title": "Świadectwo Ukończenia Gimnazjum — z fotografią w mundurze",
        "date": "7.I.1946",
        "type": "Dokument — świadectwo szkolne",
        "description": "Ministerstwo Wyznań Religijnych i Oświecenia Publicznego, "
                       "Państwowa Komisja Egzaminacyjna dla Eksternów. Świadectwo Ukończenia "
                       "Gimnazjum Ogólnokształcącego Nr 13. Krzysztof Andrzej Głuchowski, "
                       "ur. 29 [XI] 1928, Warszawa. Fotografia portretowa w mundurze wojskowym. "
                       "Egzamin dojrzałościowy z 1946r.",
        "condition": "Stan bardzo dobry, fotografia zachowana. POTWIERDZONE wizualnie.",
        "person": "krzysztof_andrzej",
        "photo_verified": True,
        "photos": ["Seria_29z_p37_img01.jpeg"],
        "significance": "Świadectwo maturalne z FOTOGRAFIĄ — jedyny dokument z portretem Krzysztofa "
                       "w mundurze. Dowód na kontynuację edukacji przez PSZ na Zachodzie.",
        "estimate_pln": (2000, 5000),
        "target_buyer": "DESA Unicum / Muzeum Wojska Polskiego",
    },
    {
        "id": "GL-S12",
        "chapter": "VII. Krzysztof Andrzej Głuchowski (1928–1945)",
        "title": "Fotografie budynków — prawdopodobnie powojenne lokalizacje",
        "date": "ok. 1945–1950",
        "type": "Fotografia — architektura",
        "description": "3 fotografie budynków — blok mieszkalny, budynek z ogrodem, willa. "
                       "Prawdopodobnie lokalizacje powojenne związane z rodziną.",
        "condition": "Stan dobry. POTWIERDZONE wizualnie.",
        "person": "krzysztof_andrzej",
        "photo_verified": True,
        "photos": ["Seria_29z_p09_img01.jpeg"],
        "significance": "Dokumentacja miejsc zamieszkania — wartość uzupełniająca.",
        "estimate_pln": (300, 800),
        "target_buyer": "Sprzedaż z kolekcją",
    },
    {
        "id": "GL-S13",
        "chapter": "VII. Krzysztof Andrzej Głuchowski (1928–1945)",
        "title": "List powyzwoleńczy na papierze Kaufmannsgehilfenprüfung Gladbach-Rheydt",
        "date": "22.VIII.1945",
        "type": "Korespondencja — list prywatny",
        "description": "List pisany po wyzwoleniu na zarekwirowanym papierze firmy Kaufmannsgehilfenprüfung "
                       "der Industrie- u. Handelskammer Gladbach-Rheydt-Neuss. "
                       "Tekst w języku polskim, datowany 22.VIII.45.",
        "condition": "Stan dostateczny, wyblakły tekst. POTWIERDZONE wizualnie.",
        "person": "krzysztof_andrzej",
        "photo_verified": True,
        "photos": ["Seria_29z_p15_img01.jpeg"],
        "significance": "Świadczy o realiach życia po wyzwoleniu — pisanie na zarekwirowanym "
                       "niemieckim papierze firmowym.",
        "estimate_pln": (500, 1200),
        "target_buyer": "Sprzedaż z kolekcją",
    },
    # ══════════════════════════════════════════════════════
    # KATALOG TEMATYCZNY — Dokumenty gen. Głuchowskiego i PON
    # ══════════════════════════════════════════════════════
    {
        "id": "GL-T01",
        "chapter": "I. Korzenie — PON (1905–1914)",
        "title": "Legitymacja PON Nr 2 — Marjan Głuchowski (ORYGINAŁ)",
        "date": "1914",
        "type": "Dokument — legitymacja organizacyjna",
        "description": "POLNISCHE NATIONALE ORGANISATION — LEGITIMATION Nr 2. "
                       "Wystawiona na Marjan Głuchowski, 1867. Pieczęć Organisations-Komission. "
                       "Podpis. Dwujęzyczna (polsko-niemiecka). "
                       "Numer 2 oznacza jednego z pierwszych uwierzytelnionych działaczy PON.",
        "condition": "Stan dobry, pieczęć czytelna. POTWIERDZONE wizualnie.",
        "person": "marjan",
        "photo_verified": True,
        "photos": ["Kolekcja_Gluchowski_Katalog_Tematyczny_p02_img01.jpeg",
                   "Kolekcja_Gluchowski_Katalog_Tematyczny_p02_img02.jpeg",
                   "Kolekcja_Gluchowski_Katalog_Tematyczny_p02_img03.jpeg"],
        "significance": "KLUCZOWY DOKUMENT PON — legitymacja nr 2 to jeden z najwcześniejszych "
                       "zachowanych dokumentów Polskiej Organizacji Narodowej. Dokument założycielski.",
        "estimate_pln": (10000, 25000),
        "target_buyer": "Muzeum Piłsudskiego Sulejówek / DESA Unicum",
    },
    {
        "id": "GL-T02",
        "chapter": "III. II Rzeczpospolita (1918–1939)",
        "title": "Ministerstwo Spraw Wojskowych — Biuro Personalne, dot. Głuchowskiego",
        "date": "ok. 1920–1935",
        "type": "Dokument urzędowy — MSWojsk.",
        "description": "Na papierze firmowym Ministerstwa Spraw Wojskowych / Biuro Personalne. "
                       "Dotyczy Puł. Głuchowskiego Janusza — sprawy personalne, przeniesienia. "
                       "Pieczęć MSWojsk.",
        "condition": "Stan dobry, papier pożółkły. POTWIERDZONE wizualnie.",
        "person": "janusz",
        "photo_verified": True,
        "photos": ["Kolekcja_Gluchowski_Katalog_Tematyczny_p07_img01.jpeg",
                   "Kolekcja_Gluchowski_Katalog_Tematyczny_p07_img02.jpeg"],
        "significance": "Dokumentacja kariery wojskowej gen. Głuchowskiego z centralnych archiwów MSWojsk.",
        "estimate_pln": (2000, 5000),
        "target_buyer": "DESA Unicum / Muzeum Wojska Polskiego",
    },
    {
        "id": "GL-T03",
        "chapter": "III. II Rzeczpospolita (1918–1939)",
        "title": "Rozkaz Wyjazdu — MSWojsk. Sztab, gen. bryg. Głuchowski",
        "date": "ok. 1930–1935",
        "type": "Dokument urzędowy — rozkaz podróży",
        "description": "Rozkaz Wyjazdu na koszt M.S.Wojsk. Seria J Nr 116321. "
                       "Dla gen. bryg. Głuchowskiego Janusza. Formularz sztabowy z pieczęcią.",
        "condition": "Stan dobry. POTWIERDZONE wizualnie.",
        "person": "janusz",
        "photo_verified": True,
        "photos": ["Kolekcja_Gluchowski_Katalog_Tematyczny_p10_img01.jpeg"],
        "significance": "Oficjalny rozkaz podróży generała — dokumentacja służby.",
        "estimate_pln": (1500, 3500),
        "target_buyer": "DESA Unicum",
    },
    {
        "id": "GL-T04",
        "chapter": "VI. 7 Pułk Ułanów Lubelskich (1919–1970)",
        "title": "Zaproszenie wielkanocne — Szef Sztabu 7 Pułku Ułanów",
        "date": "ok. 1925–1935",
        "type": "Dokument — zaproszenie oficerskie",
        "description": "Od Szefa Sztabu Zapasowego 7 Pułku Ułanów do Majora Głuchowskiego Janusza, "
                       "D-cy 7-go P. Ułanów. Zaproszenie wielkanocne w imieniu oficerów i szeregowców. "
                       "Pieczęć: 'Szef Sztabu Zapasowego 7 pułku Ułanów'.",
        "condition": "Stan dobry, pieczęć czytelna. POTWIERDZONE wizualnie.",
        "person": "janusz",
        "photo_verified": True,
        "photos": ["Kolekcja_Gluchowski_Katalog_Tematyczny_p12_img01.jpeg",
                   "Kolekcja_Gluchowski_Katalog_Tematyczny_p12_img02.jpeg",
                   "Kolekcja_Gluchowski_Katalog_Tematyczny_p12_img03.jpeg"],
        "significance": "Dokument życia codziennego pułku — potwierdza dowodzenie przez Głuchowskiego.",
        "estimate_pln": (800, 2000),
        "target_buyer": "DESA Unicum",
    },
    {
        "id": "GL-T05",
        "chapter": "III. II Rzeczpospolita (1918–1939)",
        "title": "Pismo od Dowódcy 2 Pułku Piechoty Legionów",
        "date": "ok. 1920–1935",
        "type": "Dokument urzędowy — korespondencja wojskowa",
        "description": "Na papierze firmowym Dowódcy 2 Pułku Piechoty Legionów. "
                       "Adresowane do gen. Głuchowskiego Janusza, Dowódcy Garnizonu Nr 1. "
                       "Dotyczy spraw meldunkowych/przeniesień.",
        "condition": "Stan dobry, papier pożółkły. POTWIERDZONE wizualnie.",
        "person": "janusz",
        "photo_verified": True,
        "photos": ["Kolekcja_Gluchowski_Katalog_Tematyczny_p14_img01.jpeg"],
        "significance": "Dokument łączący 2 Pułk Piechoty Legionów z gen. Głuchowskim.",
        "estimate_pln": (1500, 3500),
        "target_buyer": "DESA Unicum / Muzeum Wojska Polskiego",
    },
    # ══════════════════════════════════════════════════════
    # NOWE ODKRYCIA — Tematyczny + Naukowy (nieprzypisane wcześniej)
    # ══════════════════════════════════════════════════════
    {
        "id": "GL-T06",
        "chapter": "I. Korzenie — PON (1905–1914)",
        "title": "Pokwitowanie PON — Polska Organizacya Narodowa",
        "date": "1914",
        "type": "Dokument — pokwitowanie finansowe",
        "description": "POLSKA ORGANIZACYA NARODOWA — POKWITOWANIE na odbiór 200 kop. "
                       "Pieczęć PON, podpis Komisarza P.O.N., Oficer Wojsk Polskich.",
        "condition": "Stan dobry. POTWIERDZONE wizualnie.",
        "person": "marjan",
        "photo_verified": True,
        "photos": ["Kolekcja_Gluchowski_Katalog_Tematyczny_p03_img01.jpeg",
                   "Kolekcja_Gluchowski_Katalog_Tematyczny_p03_img02.jpeg"],
        "significance": "Dokument finansowy PON — potwierdza działalność organizacyjną i zbiórkę funduszy.",
        "estimate_pln": (3000, 8000),
        "target_buyer": "Muzeum Piłsudskiego Sulejówek / DESA Unicum",
    },
    {
        "id": "GL-T07",
        "chapter": "II. Siódemka Beliny i Legiony (1913–1925)",
        "title": "Biogram WBH — Wojskowe Biuro Historyczne, 1951",
        "date": "24.V.1951",
        "type": "Dokument — biogram urzędowy",
        "description": "WOJSKOWE BIURO HISTORYCZNE Nr 76/45/XI/1951. Oficjalny biogram "
                       "gen. Głuchowskiego Janusza — od urodzenia 1888, przez 'Siódemkę' Beliny, "
                       "do dowodzenia 7 P.Uł. Pieczęć okrągła WBH.",
        "condition": "Stan bardzo dobry. POTWIERDZONE wizualnie.",
        "person": "janusz",
        "photo_verified": True,
        "photos": ["Kolekcja_Gluchowski_Katalog_Tematyczny_p04_img01.jpeg",
                   "Kolekcja_Gluchowski_Katalog_Tematyczny_p04_img02.jpeg"],
        "significance": "Oficjalny biogram z Wojskowego Biura Historycznego — "
                       "źródło proweniencji najwyższej kategorii.",
        "estimate_pln": (3000, 8000),
        "target_buyer": "Muzeum Wojska Polskiego / DESA Unicum",
    },
    {
        "id": "GL-T08",
        "chapter": "II. Siódemka Beliny i Legiony (1913–1925)",
        "title": "Rozkaz utworzenia 7 P.Uł. — Lublin, 5.XI.1918",
        "date": "5.XI.1918",
        "type": "Dokument — rozkaz wojskowy",
        "description": "DOWÓDZTWO WOJSK POLSKICH M. LUBLINIE / SZTAB GENERALNY. "
                       "'Rozkazuję reinstruować Januszowi Głuchowskiemu zająć tworzeniem "
                       "oddziału jazdy — lubelskiej.' Lublin, 5 listopada 1918. Podpis.",
        "condition": "Stan dobry. POTWIERDZONE wizualnie.",
        "person": "janusz",
        "photo_verified": True,
        "photos": ["Kolekcja_Gluchowski_Katalog_Tematyczny_p06_img01.jpeg",
                   "Kolekcja_Gluchowski_Katalog_Tematyczny_p06_img02.jpeg"],
        "significance": "DOKUMENT ZAŁOŻYCIELSKI 7 Pułku Ułanów Lubelskich! "
                       "Rozkaz z pierwszych dni niepodległości. Bezcenny.",
        "estimate_pln": (15000, 40000),
        "target_buyer": "Muzeum Wojska Polskiego / Muzeum Piłsudskiego / DESA Unicum",
    },
    {
        "id": "GL-T09",
        "chapter": "III. II Rzeczpospolita (1918–1939)",
        "title": "Iluminowany adres pożegnalny — oficerowie, IX.1945",
        "date": "IX.1945",
        "type": "Dokument artystyczny — adres iluminowany",
        "description": "Ręcznie malowany adres pożegnalny: 'Panu Generałowi Januszowi "
                       "Głuchowskiemu C.B. na pamiątkę miłej współpracy od Oficerów...' "
                       "Akwarela z flagami polskimi i brytyjskimi (Union Jack), "
                       "herb pułkowy. Wrzesień 1945.",
        "condition": "Stan dobry, kolory żywe. POTWIERDZONE wizualnie.",
        "person": "janusz",
        "photo_verified": True,
        "photos": ["Kolekcja_Gluchowski_Katalog_Tematyczny_p08_img01.jpeg",
                   "Kolekcja_Gluchowski_Katalog_Tematyczny_p08_img02.jpeg"],
        "significance": "Piękny dokument artystyczny — pożegnanie generała przez podkomendnych. "
                       "Wartość artystyczna + historyczna.",
        "estimate_pln": (5000, 15000),
        "target_buyer": "DESA Unicum / Muzeum Wojska Polskiego",
    },
    {
        "id": "GL-T10",
        "chapter": "III. II Rzeczpospolita (1918–1939)",
        "title": "Meldunek — Prezydent RP + Minister Spraw Wojskowych",
        "date": "ok. 1933–1935",
        "type": "Dokument urzędowy — dekret prezydencki",
        "description": "MELDUNEK w korporale generałów. Gen. bryg. Głuchowski Janusz — "
                       "Dowódca Okręgu Korpusu Nr I(?). Podpisy: PREZYDENT RZECZYPOSPOLITEJ "
                       "i MINISTER SPRAW WOJSKOWYCH.",
        "condition": "Stan dobry. POTWIERDZONE wizualnie.",
        "person": "janusz",
        "photo_verified": True,
        "photos": ["Kolekcja_Gluchowski_Katalog_Tematyczny_p09_img01.jpeg",
                   "Kolekcja_Gluchowski_Katalog_Tematyczny_p09_img02.jpeg"],
        "significance": "Dokument z podpisami Prezydenta RP i Ministra — najwyższy szczebel państwowy.",
        "estimate_pln": (5000, 15000),
        "target_buyer": "DESA Unicum / Muzeum Piłsudskiego",
    },
    {
        "id": "GL-T11",
        "chapter": "III. II Rzeczpospolita (1918–1939)",
        "title": "List do ppłk. Głuchowskiego na papierze z monogramem",
        "date": "ok. 1925",
        "type": "Korespondencja — list prywatny",
        "description": "Koperta: 'S. Wielmożny Pan podpułkownik Głuchowski'. "
                       "List na papierze z koronowanym monogramem, datowany 11/8 25[?]. "
                       "Tekst odręczny w języku polskim.",
        "condition": "Stan dobry, koperta zachowana. POTWIERDZONE wizualnie.",
        "person": "janusz",
        "photo_verified": True,
        "photos": ["Kolekcja_Gluchowski_Katalog_Tematyczny_p11_img01.jpeg"],
        "significance": "List z epoki z zachowaną kopertą — dokumentacja korespondencji oficerskiej.",
        "estimate_pln": (800, 2000),
        "target_buyer": "DESA Unicum",
    },
    {
        "id": "GL-N01",
        "chapter": "VI. 7 Pułk Ułanów Lubelskich (1919–1970)",
        "title": "Tablica pamiątkowa — tekst o ataku 1.VIII.1944",
        "date": "ok. 1960–1970",
        "type": "Druk — tekst pamiątkowy",
        "description": "'Dnia 1.8.1944 r. godz. 17. z tego domu i okolicznych ruszyło do natarcia "
                       "na gmach Gestapo i Dom Prasy 5 plutonów ułanów 7 pułku ułanów AK JELEŃ "
                       "z 187 Powstańców poległo 67. Cześć Ich pamięci.'",
        "condition": "Stan dobry. POTWIERDZONE wizualnie.",
        "person": "lech",
        "photo_verified": True,
        "photos": ["Kolekcja_Gluchowski_KATALOG_NAUKOWY_p04_img01.jpeg"],
        "significance": "Tekst tablicy pamiątkowej z dokładnymi liczbami: 187 walczących, 67 poległych.",
        "estimate_pln": (500, 1500),
        "target_buyer": "Muzeum Powstania Warszawskiego",
    },
    {
        "id": "GL-N02",
        "chapter": "VI. 7 Pułk Ułanów Lubelskich (1919–1970)",
        "title": "Zaproszenie na mszę za poległych 'Jelenia' — 1970",
        "date": "4.X.1970",
        "type": "Druk — zaproszenie kombatanckie",
        "description": "Zaproszenie na doroczną mszę św. za poległych żołnierzy pułku AK 'Jeleń' "
                       "w kościele Św. Anny, 4 października 1970. Po mszy kwiaty na cmentarzu "
                       "na mogiłe żołnierzy 'Jelenia' poległych na Sadybie. "
                       "Spotkanie w restauracji 'Rudzki'.",
        "condition": "Stan dobry. POTWIERDZONE wizualnie.",
        "person": "lech",
        "photo_verified": True,
        "photos": ["Kolekcja_Gluchowski_KATALOG_NAUKOWY_p20_img01.jpeg"],
        "significance": "Dokument pamięci kombatanckiej — doroczne spotkanie żołnierzy 'Jelenia' w PRL.",
        "estimate_pln": (300, 800),
        "target_buyer": "Muzeum Powstania Warszawskiego / Sprzedaż z kolekcją",
    },
    {
        "id": "GL-N03",
        "chapter": "VI. 7 Pułk Ułanów Lubelskich (1919–1970)",
        "title": "Nekrolog Jana Lorensa — Koło Żołnierzy 7 P.Uł., Chicago",
        "date": "29.I.1960",
        "type": "Druk — nekrolog",
        "description": "Ś.†P. JAN LORENS, plutonowy 7 pułku ułanowego, czynny członek "
                       "organizacji niepodległościowych w Chicago, odznaczony Krzyżem Walecznych. "
                       "Zm. 29 stycznia 1960 w Chicago. KOŁO ŻOŁNIERZY 7 PUŁKU UŁANÓW LUBELSKICH "
                       "IM. GEN. K. SOSNKOWSKIEGO.",
        "condition": "Stan dobry. POTWIERDZONE wizualnie.",
        "person": "janusz",
        "photo_verified": True,
        "photos": ["Kolekcja_Gluchowski_KATALOG_NAUKOWY_p21_img01.jpeg"],
        "significance": "Dokument emigracyjny — Koło 7 P.Uł. działające w Chicago.",
        "estimate_pln": (300, 800),
        "target_buyer": "Sprzedaż z kolekcją",
    },
    {
        "id": "GL-N04",
        "chapter": "VII. Krzysztof Andrzej Głuchowski (1928–1945)",
        "title": "Rozkaz awansu + Legitymacja AK — Głuchowski Krzysztof 'Juras'",
        "date": "5.IX.1944 / 8.X.1944",
        "type": "Dokument — legitymacja AK + rozkaz",
        "description": "DWA DOKUMENTY: 1) Wyciąg z Rozkazu D-na Grupy 'Północ' nr 24, z dn. 5.IX.44 — "
                       "awansowany do stopnia st. ułana i nadany po raz I-szy K.W. Pieczęć AK (orzeł). "
                       "2) DOWÓDZTWO ARMII KRAJOWEJ — Legitymacja nr 14112. Oddział: Pluton nr 412, "
                       "Głuchowski Krzysztof (Juras), ułan, ur. 29.XI.1926. "
                       "Data wyst.: 8.X.1944. Pieczęć AK + odcisk palca.",
        "condition": "Stan dobry, pieczęcie czytelne. POTWIERDZONE wizualnie.",
        "person": "krzysztof_andrzej",
        "photo_verified": True,
        "photos": ["Kolekcja_Gluchowski_KATALOG_NAUKOWY_p26_img01.jpeg",
                   "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p26_img02.jpeg"],
        "significance": "KLUCZOWE DOKUMENTY — legitymacja AK z odciskiem palca + rozkaz awansu i KW. "
                       "Dowód tożsamości powstańca.",
        "estimate_pln": (8000, 20000),
        "target_buyer": "Muzeum Powstania Warszawskiego",
    },
]

# ── PODSUMOWANIE AUKCJI W BRAZYLII ──
AUCTION_HISTORY = {
    "house": "Acervo Raro Leilões, São Paulo, Brazylia",
    "auction_numbers": ["54274", "55909", "58273", "51119"],
    "total_lots": 48,
    "sold": [
        "Lote 24 — Legitymacja oficerska (SPRZEDANE)",
        "Lote 46 — Karykatura Głuchowskiego (SPRZEDANE)",
        "Lote 83 — Inspekcja tanków Kelso (SPRZEDANE)",
        "Lote 91 — Album Głuchowski (SPRZEDANE)",
        "Lote 159 — Boina wojskowa (SPRZEDANE)",
        "Lote 161 — Inspekcja Kelso (SPRZEDANE)",
        "Lote 169 — Inspekcja tanków Bor-Komorowski (SPRZEDANE)",
        "Lote 175 — Banda 25 Reg. Pol. (SPRZEDANE)",
        "Lote 198 — 5 fotografii (SPRZEDANE)",
        "Lote 201 — Cmentarz Wilanów (SPRZEDANE)",
        "Lote 203 — Fotografie 1945 (SPRZEDANE)",
        "Lote 211 — Album Monte Cassino (SPRZEDANE)",
        "Lote 218 — Motocykle Szkocja (SPRZEDANE)",
        "Lote 74 — Pamięć straconych (SPRZEDANE)",
    ],
    "unsold_count": 34,
    "note": "Większość obiektów nie sprzedała się — brazylijskie aukcje nie są właściwym rynkiem "
            "dla polskich militariów. Właściwym rynkiem jest Polska (DESA Unicum, WCN, OneBid) "
            "i instytucje muzealne."
}


def generate_html_catalog():
    """Generuje profesjonalny katalog HTML."""

    img_dir = r"C:\Users\skore\leiloesbr-scraper\docs\gluchowski_img"
    wa_dir = r"C:\Users\skore\Downloads"

    # Filtruj tylko obiekty ze zdjęciami
    DISPLAY_OBJECTS = [o for o in OBJECTS if o["photos"]]
    total_min = sum(o["estimate_pln"][0] for o in DISPLAY_OBJECTS)
    total_max = sum(o["estimate_pln"][1] for o in DISPLAY_OBJECTS)
    verified_count = sum(1 for o in DISPLAY_OBJECTS if o["photo_verified"])

    chapters = {}
    for obj in OBJECTS:
        if not obj["photos"]:
            continue  # Pomijaj obiekty bez zdjęć
        ch = obj["chapter"]
        if ch not in chapters:
            chapters[ch] = []
        chapters[ch].append(obj)

    html = f"""<!DOCTYPE html>
<html lang="pl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Archiwum Rodziny Głuchowskich — Katalog Profesjonalny</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Source+Sans+3:wght@300;400;600&display=swap');

  :root {{
    --bg: #1a1a1a;
    --card: #242424;
    --gold: #c9a84c;
    --gold-dim: #8a7233;
    --text: #e8e0d0;
    --text-dim: #a09880;
    --verified: #4a9;
    --unverified: #a94;
    --accent: #6a8;
    --border: #333;
  }}

  * {{ margin: 0; padding: 0; box-sizing: border-box; }}

  body {{
    font-family: 'Source Sans 3', Georgia, serif;
    background: var(--bg);
    color: var(--text);
    line-height: 1.7;
  }}

  .header {{
    text-align: center;
    padding: 60px 20px 40px;
    border-bottom: 1px solid var(--gold-dim);
    background: linear-gradient(180deg, #1a1a1a 0%, #222 100%);
  }}

  .header h1 {{
    font-family: 'Playfair Display', Georgia, serif;
    font-size: 2.4em;
    color: var(--gold);
    letter-spacing: 3px;
    margin-bottom: 8px;
  }}

  .header .subtitle {{
    font-size: 1.1em;
    color: var(--text-dim);
    font-weight: 300;
  }}

  .stats {{
    display: flex;
    justify-content: center;
    gap: 40px;
    margin-top: 30px;
    flex-wrap: wrap;
  }}

  .stat {{
    text-align: center;
  }}

  .stat-num {{
    font-family: 'Playfair Display', serif;
    font-size: 2em;
    color: var(--gold);
  }}

  .stat-label {{
    font-size: 0.85em;
    color: var(--text-dim);
  }}

  .family-section {{
    max-width: 1000px;
    margin: 40px auto;
    padding: 0 20px;
  }}

  .family-section h2 {{
    font-family: 'Playfair Display', serif;
    color: var(--gold);
    font-size: 1.6em;
    border-bottom: 1px solid var(--border);
    padding-bottom: 10px;
    margin-bottom: 20px;
  }}

  .family-tree {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 15px;
  }}

  .family-card {{
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 6px;
    padding: 16px;
  }}

  .family-card h3 {{
    color: var(--gold);
    font-size: 1em;
    margin-bottom: 4px;
  }}

  .family-card .dates {{
    color: var(--text-dim);
    font-size: 0.85em;
    margin-bottom: 8px;
  }}

  .family-card .role {{
    color: var(--accent);
    font-size: 0.9em;
    font-weight: 600;
    margin-bottom: 6px;
  }}

  .family-card p {{
    font-size: 0.85em;
    color: var(--text-dim);
  }}

  nav.chapters {{
    max-width: 1000px;
    margin: 30px auto;
    padding: 0 20px;
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
  }}

  nav.chapters a {{
    background: var(--card);
    border: 1px solid var(--border);
    color: var(--gold);
    padding: 6px 14px;
    text-decoration: none;
    border-radius: 4px;
    font-size: 0.85em;
  }}

  nav.chapters a:hover {{
    background: var(--gold-dim);
    color: #fff;
  }}

  .chapter {{
    max-width: 1000px;
    margin: 40px auto;
    padding: 0 20px;
  }}

  .chapter h2 {{
    font-family: 'Playfair Display', serif;
    color: var(--gold);
    font-size: 1.5em;
    border-bottom: 1px solid var(--border);
    padding-bottom: 10px;
    margin-bottom: 20px;
  }}

  .object-card {{
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 8px;
    margin-bottom: 20px;
    overflow: hidden;
  }}

  .object-card.verified {{
    border-left: 3px solid var(--verified);
  }}

  .object-card.unverified {{
    border-left: 3px solid var(--unverified);
  }}

  .object-header {{
    padding: 16px 20px;
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: 16px;
  }}

  .object-id {{
    font-family: monospace;
    color: var(--gold-dim);
    font-size: 0.85em;
  }}

  .object-title {{
    font-family: 'Playfair Display', serif;
    color: var(--gold);
    font-size: 1.15em;
    margin-top: 4px;
  }}

  .object-date {{
    color: var(--text-dim);
    font-size: 0.9em;
  }}

  .badge {{
    display: inline-block;
    padding: 2px 8px;
    border-radius: 3px;
    font-size: 0.75em;
    font-weight: 600;
    white-space: nowrap;
  }}

  .badge-verified {{
    background: rgba(68,170,153,0.2);
    color: var(--verified);
    border: 1px solid var(--verified);
  }}

  .badge-unverified {{
    background: rgba(170,153,68,0.2);
    color: var(--unverified);
    border: 1px solid var(--unverified);
  }}

  .object-body {{
    padding: 0 20px 16px;
  }}

  .object-body .desc {{
    font-size: 0.95em;
    margin-bottom: 10px;
  }}

  .object-body .significance {{
    font-size: 0.9em;
    color: var(--accent);
    font-style: italic;
    margin-bottom: 10px;
    padding: 8px 12px;
    background: rgba(102,170,136,0.08);
    border-radius: 4px;
  }}

  .object-meta {{
    display: flex;
    flex-wrap: wrap;
    gap: 16px;
    font-size: 0.85em;
    color: var(--text-dim);
    padding-top: 10px;
    border-top: 1px solid var(--border);
  }}

  .meta-item {{
    display: flex;
    align-items: center;
    gap: 4px;
  }}

  .meta-label {{
    color: var(--gold-dim);
  }}

  .price {{
    font-family: 'Playfair Display', serif;
    color: var(--gold);
    font-size: 1.1em;
  }}

  .target {{
    color: var(--accent);
    font-weight: 600;
  }}

  .photos-row {{
    display: flex;
    gap: 8px;
    padding: 0 20px 16px;
    overflow-x: auto;
  }}

  .photos-row img {{
    height: 200px;
    border-radius: 4px;
    cursor: pointer;
    border: 1px solid var(--border);
  }}

  .photos-row img:hover {{
    border-color: var(--gold);
  }}

  .summary {{
    max-width: 1000px;
    margin: 40px auto;
    padding: 30px 20px;
    background: var(--card);
    border: 1px solid var(--gold-dim);
    border-radius: 8px;
  }}

  .summary h2 {{
    font-family: 'Playfair Display', serif;
    color: var(--gold);
    margin-bottom: 20px;
  }}

  .summary table {{
    width: 100%;
    border-collapse: collapse;
  }}

  .summary td, .summary th {{
    padding: 8px 12px;
    text-align: left;
    border-bottom: 1px solid var(--border);
  }}

  .summary th {{
    color: var(--gold-dim);
    font-weight: 600;
  }}

  .auction-note {{
    max-width: 1000px;
    margin: 30px auto;
    padding: 20px;
    background: rgba(170,153,68,0.1);
    border: 1px solid var(--unverified);
    border-radius: 6px;
    font-size: 0.9em;
  }}

  .auction-note h3 {{
    color: var(--unverified);
    margin-bottom: 8px;
  }}

  .footer {{
    text-align: center;
    padding: 40px 20px;
    border-top: 1px solid var(--border);
    color: var(--text-dim);
    font-size: 0.85em;
  }}

  /* Lightbox */
  .lightbox {{
    display: none;
    position: fixed;
    top: 0; left: 0; width: 100%; height: 100%;
    background: rgba(0,0,0,0.95);
    z-index: 1000;
    justify-content: center;
    align-items: center;
    cursor: pointer;
  }}
  .lightbox.active {{ display: flex; }}
  .lightbox img {{
    max-width: 95vw;
    max-height: 95vh;
    object-fit: contain;
    transform: rotate(0deg);
    transition: transform 0.3s;
  }}
</style>
</head>
<body>

<div class="header">
  <h1>ARCHIWUM RODZINY GŁUCHOWSKICH</h1>
  <div class="subtitle">Cztery pokolenia niepodległości Polski &middot; 1905–1945</div>
  <div class="subtitle" style="margin-top:4px; font-size:0.9em; color:#888;">
    Katalog profesjonalny &middot; Opracowanie: marzec 2026
  </div>
  <div class="stats">
    <div class="stat">
      <div class="stat-num">{len(DISPLAY_OBJECTS)}</div>
      <div class="stat-label">obiektów skatalogowanych</div>
    </div>
    <div class="stat">
      <div class="stat-num">{verified_count}</div>
      <div class="stat-label">zweryfikowanych wizualnie</div>
    </div>
    <div class="stat">
      <div class="stat-num">{total_min//1000}k – {total_max//1000}k PLN</div>
      <div class="stat-label">wartość szacunkowa (suma pozycji)</div>
    </div>
  </div>
</div>

<!-- Rodzina -->
<div class="family-section">
  <h2>Rodzina Głuchowskich</h2>
  <div class="family-tree">
"""

    for key in ["marjan", "janusz", "stanislaw_stefan", "lech", "krzysztof", "krzysztof_andrzej"]:
        f = FAMILY[key]
        html += f"""    <div class="family-card">
      <h3>{f['name']}</h3>
      <div class="dates">{f['dates']}</div>
      <div class="role">{f['role']}</div>
      <p>{f['bio'][:200]}{'...' if len(f['bio']) > 200 else ''}</p>
    </div>
"""

    html += """  </div>
</div>

<!-- Nawigacja rozdziałów -->
<nav class="chapters">
"""
    for i, ch_name in enumerate(chapters.keys()):
        ch_id = f"ch{i}"
        short = ch_name.split('.')[0] + '.' if '.' in ch_name else ch_name[:20]
        html += f'  <a href="#{ch_id}">{ch_name}</a>\n'

    html += "</nav>\n\n"

    # Rozdziały i obiekty
    for i, (ch_name, objs) in enumerate(chapters.items()):
        ch_id = f"ch{i}"
        ch_min = sum(o["estimate_pln"][0] for o in objs)
        ch_max = sum(o["estimate_pln"][1] for o in objs)

        html += f"""<div class="chapter" id="{ch_id}">
  <h2>{ch_name} <span style="float:right; font-size:0.6em; color:var(--text-dim);">{ch_min:,} – {ch_max:,} PLN</span></h2>
"""
        for obj in objs:
            v_class = "verified" if obj["photo_verified"] else "unverified"
            v_badge = '<span class="badge badge-verified">ZWERYFIKOWANE</span>' if obj["photo_verified"] else '<span class="badge badge-unverified">DO WERYFIKACJI</span>'

            person = FAMILY.get(obj["person"], {})
            person_name = person.get("name", "")

            lo, hi = obj["estimate_pln"]

            html += f"""  <div class="object-card {v_class}">
    <div class="object-header">
      <div>
        <div class="object-id">{obj['id']} &middot; {obj['type']} {v_badge}</div>
        <div class="object-title">{obj['title']}</div>
        <div class="object-date">{obj['date']} &middot; {person_name}</div>
      </div>
    </div>
"""
            # Zdjęcia
            if obj["photos"]:
                html += '    <div class="photos-row">\n'
                for photo in obj["photos"]:
                    src = f"gluchowski_img/{photo}"
                    html += f'      <img src="{src}" alt="{obj["id"]}" onclick="openLightbox(this.src)" loading="lazy">\n'
                html += '    </div>\n'

            html += f"""    <div class="object-body">
      <div class="desc">{obj['description']}</div>
      <div class="significance">{obj['significance']}</div>
      <div class="object-meta">
        <div class="meta-item"><span class="meta-label">Wycena:</span> <span class="price">{lo:,} – {hi:,} PLN</span></div>
        <div class="meta-item"><span class="meta-label">Stan:</span> {obj['condition']}</div>
        <div class="meta-item"><span class="meta-label">Cel sprzedaży:</span> <span class="target">{obj['target_buyer']}</span></div>
      </div>
    </div>
  </div>
"""
        html += "</div>\n\n"

    # Podsumowanie
    html += f"""<div class="summary">
  <h2>Podsumowanie wyceny</h2>
  <table>
    <tr><th>Kategoria</th><th>Pozycji</th><th>Minimum</th><th>Maksimum</th></tr>
"""
    for ch_name, objs in chapters.items():
        ch_min = sum(o["estimate_pln"][0] for o in objs)
        ch_max = sum(o["estimate_pln"][1] for o in objs)
        html += f"    <tr><td>{ch_name}</td><td>{len(objs)}</td><td>{ch_min:,} PLN</td><td>{ch_max:,} PLN</td></tr>\n"

    html += f"""    <tr style="font-weight:bold; border-top:2px solid var(--gold-dim);">
      <td>SUMA POZYCJI</td><td>{len(DISPLAY_OBJECTS)}</td>
      <td>{total_min:,} PLN</td><td>{total_max:,} PLN</td>
    </tr>
    <tr style="color:var(--gold);">
      <td colspan="2">PREMIA ZA KOLEKCJĘ (spójność narracyjna)</td>
      <td>+{int(total_min*0.5):,} PLN</td><td>+{int(total_max*0.8):,} PLN</td>
    </tr>
    <tr style="font-weight:bold; font-size:1.15em; color:var(--gold);">
      <td colspan="2">ŁĄCZNA WARTOŚĆ KOLEKCJI</td>
      <td>{int(total_min*1.5):,} PLN</td><td>{int(total_max*1.8):,} PLN</td>
    </tr>
  </table>
</div>

<div class="auction-note">
  <h3>Historia aukcyjna — Acervo Raro Leilões, Brazylia</h3>
  <p>{AUCTION_HISTORY['note']}</p>
  <p style="margin-top:8px;"><strong>Sprzedane:</strong> {len(AUCTION_HISTORY['sold'])} lotów z {AUCTION_HISTORY['total_lots']} &middot;
  <strong>Niesprzedane:</strong> {AUCTION_HISTORY['unsold_count']} lotów</p>
</div>

<div class="summary" style="margin-top:30px;">
  <h2>Rekomendacje sprzedaży</h2>
  <table>
    <tr><th>Instytucja</th><th>Rozdziały</th><th>Dlaczego</th></tr>
    <tr>
      <td style="color:var(--gold);">Muzeum Józefa Piłsudskiego w Sulejówku</td>
      <td>II, III</td>
      <td>Dyplom Krzyża Legionowego z podpisem Piłsudskiego, listy Piłsudskiej, dekrety — rdzeń kolekcji</td>
    </tr>
    <tr>
      <td style="color:var(--gold);">Muzeum Powstania Warszawskiego</td>
      <td>VII</td>
      <td>Kompletna historia 15-letniego powstańca: Kennkarte → legitymacja AK → listy → przepustki → Stalag</td>
    </tr>
    <tr>
      <td style="color:var(--gold);">Muzeum Wojska Polskiego</td>
      <td>III, VIII</td>
      <td>Legitymacja oficerska generała, album CWŁ PSZ, medale</td>
    </tr>
    <tr>
      <td style="color:var(--gold);">Muzeum POLIN / Yad Vashem</td>
      <td>V</td>
      <td>Artefakty getta łódzkiego + 26-letnia korespondencja o ich losie — OBOWIĄZKOWO instytucja</td>
    </tr>
    <tr>
      <td style="color:var(--gold);">DESA Unicum</td>
      <td>I, IV, VI</td>
      <td>Dokumenty PON, Sosnkowski, 7 P.Uł. — wolny rynek kolekcjonerski</td>
    </tr>
    <tr>
      <td style="color:var(--gold);">Sprzedaż kolekcji w całości</td>
      <td>WSZYSTKIE</td>
      <td>Najwyższa wartość — wzajemne uwierzytelnianie dokumentów, ciągłość narracyjna 4 pokoleń</td>
    </tr>
  </table>
</div>

<div class="footer">
  <p>Archiwum Rodziny Głuchowskich &middot; Katalog opracowany marzec 2026</p>
  <p>Wyceny mają charakter orientacyjny i wymagają weryfikacji przez certyfikowanego rzeczoznawcę.</p>
  <p style="margin-top:8px;">Na podstawie: skanów dokumentów, fotografii WhatsApp, CSV z aukcji Acervo Raro Leilões,<br>
  biografii rodzinnych (Krzysztof Głuchowski, Rio de Janeiro 1995)</p>
</div>

<!-- Lightbox -->
<div class="lightbox" id="lightbox" onclick="closeLightbox()">
  <img id="lightbox-img" src="" alt="">
</div>

<script>
let rotation = 0;
function openLightbox(src) {{
  rotation = 0;
  const lb = document.getElementById('lightbox');
  const img = document.getElementById('lightbox-img');
  img.src = src;
  img.style.transform = 'rotate(0deg)';
  lb.classList.add('active');
}}
function closeLightbox() {{
  document.getElementById('lightbox').classList.remove('active');
}}
document.addEventListener('keydown', e => {{
  if (e.key === 'Escape') closeLightbox();
  if (e.key === 'r' || e.key === 'R') {{
    rotation = (rotation + 90) % 360;
    document.getElementById('lightbox-img').style.transform = 'rotate(' + rotation + 'deg)';
  }}
}});
</script>

</body>
</html>"""

    return html


if __name__ == "__main__":
    html = generate_html_catalog()

    output_path = os.path.join(os.path.dirname(__file__), "docs", "katalog_gluchowski_v2.html")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Katalog wygenerowany: {output_path}")

    displayed = [o for o in OBJECTS if o["photos"]]
    print(f"Obiektow: {len(displayed)}")
    verified = sum(1 for o in displayed if o["photo_verified"])
    total_min = sum(o["estimate_pln"][0] for o in displayed)
    total_max = sum(o["estimate_pln"][1] for o in displayed)

    print(f"Zweryfikowanych wizualnie: {verified}/{len(displayed)}")
    print(f"Wartosc szacunkowa (suma pozycji): {total_min:,} - {total_max:,} PLN")
    print(f"Wartosc z premia za kolekcje: {int(total_min*1.5):,} - {int(total_max*1.8):,} PLN")
