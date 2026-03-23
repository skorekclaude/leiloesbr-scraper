#!/usr/bin/env python3
"""
ARCHIWUM RODZINY GLUCHOWSKICH - Katalog v3
============================================
Kazde zdjecie = 1 karta katalogowa.
Opisy na podstawie bezposredniej analizy wizualnej.
"""

import os

IMG_DIR = "gluchowski_img"

# ============================================================================
# RODZINA
# ============================================================================
FAMILY = {
    "marjan": "Marian Gluchowski (1862-1924), czlonek Rady PON, organizator PPS",
    "janusz": "Gen. bryg. Janusz Julian Gluchowski (1888-1964), I Wiceminister Spraw Wojskowych",
    "stanislaw": "Ppor. Stanislaw Stefan Gluchowski (1897-1977), oficer 7 P.Ul., jeniec Stalag XI B",
    "lech": "Lech Gluchowski ps. 'Jezycki' (1900-1944), polegly w Powstaniu Warszawskim 15.IX.1944",
    "krzysztof_a": "St.ul. Krzysztof Andrzej Gluchowski ps. 'Juras' (1926/1928-), AK plut.1112, jeniec Stalag XI B, Gimnazjum 3DSK",
    "krzysztof_k": "Krzysztof Gluchowski (1926-), syn Stanislawa, ps. 'Juras', Kennkarte GG, legitymacja AK",
}

# ============================================================================
# OBIEKTY: 1 zdjecie = 1 karta
# ============================================================================
OBJECTS = [
    # ===== KATALOG NAUKOWY =====
    {
        "id": "N-001",
        "photo": "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p04_img01.jpeg",
        "title": "Tablica pamiatkowa akcji 'Jelen'",
        "date": "1.VIII.1944",
        "desc": "Tablica upamietniajaca atak oddzialu AK 'Jelen' (7 Pulk Ulanow Lubelskich AK) na siedzibe Gestapo i Dom Prasy w Krakowie, 1 sierpnia 1944 r.",
        "chapter": "AK i Powstanie",
        "person": "7 P.Ul. AK 'Jelen'"
    },
    {
        "id": "N-002",
        "photo": "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p06_img01.jpeg",
        "title": "Dyplom Krzyza Legionowego - zbliżenie",
        "date": "ok. 1920",
        "desc": "Zbliżenie dyplomu Krzyża Legionowego (Croix de la Légion d'Honneur?) nadanego za służbę w Legionach Polskich. Kaligrafowany tekst na pergaminie.",
        "chapter": "Legiony i I wojna",
        "person": "Janusz Głuchowski"
    },
    {
        "id": "N-003",
        "photo": "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p06_img02.jpeg",
        "title": "Dyplom z portretem Pilsudskiego",
        "date": "ok. 1920",
        "desc": "Pelny widok dyplomu legionowego z portretem Jozefa Pilsudskiego w prawym gornym rogu. Dokument ozdobny, druk okolicznosciowy.",
        "chapter": "Legiony i I wojna",
        "person": "Janusz Głuchowski"
    },
    {
        "id": "N-004",
        "photo": "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p09_img01.jpeg",
        "title": "List z Kanady",
        "date": "ok. 1964",
        "desc": "List odręczny, prawdopodobnie zwiazany z dzialalnoscia emigracyjna gen. Gluchowskiego. Pismo atramentem na papierze listowym.",
        "chapter": "Emigracja",
        "person": "Janusz Głuchowski"
    },
    {
        "id": "N-005",
        "photo": "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p10_img01.jpeg",
        "title": "Krzyz Walecznych - fotografia odznaczenia",
        "date": "1920-1944",
        "desc": "Fotografia Krzyza Walecznych - odznaczenia wojskowego nadawanego za mestwo na polu walki. Krzyz z mieczami na wstazce.",
        "chapter": "Odznaczenia",
        "person": "Rodzina Głuchowskich"
    },
    {
        "id": "N-006",
        "photo": "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p13_img01.jpeg",
        "title": "Legitymacja oficerska Janusza - okladka",
        "date": "lata 30.",
        "desc": "Legitymacja oficerska gen. bryg. Janusza Gluchowskiego - widok okladki/pierwszej strony. Dokument tozsamosci oficera Wojska Polskiego.",
        "chapter": "Dokumenty osobiste",
        "person": "Janusz Głuchowski"
    },
    {
        "id": "N-007",
        "photo": "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p13_img02.jpeg",
        "title": "Legitymacja oficerska Janusza - wnetrze (1)",
        "date": "lata 30.",
        "desc": "Legitymacja oficerska gen. bryg. Janusza Gluchowskiego - rozkladowka z danymi osobowymi, pieczecia i zdjecia.",
        "chapter": "Dokumenty osobiste",
        "person": "Janusz Głuchowski"
    },
    {
        "id": "N-008",
        "photo": "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p13_img03.jpeg",
        "title": "Legitymacja oficerska Janusza - wnetrze (2)",
        "date": "lata 30.",
        "desc": "Legitymacja oficerska gen. bryg. Janusza Gluchowskiego - kolejna rozkladowka z wpisami sluzbowymi.",
        "chapter": "Dokumenty osobiste",
        "person": "Janusz Głuchowski"
    },
    {
        "id": "N-009",
        "photo": "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p14_img01.jpeg",
        "title": "Maszynopis - lista prosb/zamowien (str. 1)",
        "date": "lata 60.",
        "desc": "Maszynopis z lista zamowien/prosb dotyczacych artykulow i obchodow 50-lecia. Strona pierwsza dokumentu organizacyjnego.",
        "chapter": "Emigracja",
        "person": "Janusz Głuchowski"
    },
    {
        "id": "N-010",
        "photo": "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p14_img02.jpeg",
        "title": "Maszynopis - lista prosb/zamowien (str. 2)",
        "date": "lata 60.",
        "desc": "Druga strona maszynopisu organizacyjnego. Kontynuacja listy zamowien i artykulow okolicznosciowych.",
        "chapter": "Emigracja",
        "person": "Janusz Głuchowski"
    },
    {
        "id": "N-011",
        "photo": "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p17_img01.jpeg",
        "title": "List do Ambasady Izraela",
        "date": "18.V.1958",
        "desc": "List Krzysztofa Gluchowskiego do Ambasady Izraela w sprawie sprzedazy walut i monet getta lodzkiego (Litzmannstadt). Pismo urzedowe.",
        "chapter": "Getto lodzkie",
        "person": "Krzysztof Głuchowski"
    },
    {
        "id": "N-012",
        "photo": "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p17_img02.jpeg",
        "title": "Pieniadze getta lodzkiego - bon, talon, koperta",
        "date": "1940-1944",
        "desc": "Trzy przedmioty na jednym zdjeciu: bon 10 Pfennig getta lodzkiego (Litzmannstadt), talon na produkty mleczne (Molkereierzeugnisse), koperta. Numizmaty gettowe.",
        "chapter": "Getto lodzkie",
        "person": "Krzysztof Głuchowski"
    },
    {
        "id": "N-013",
        "photo": "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p17_img03.jpeg",
        "title": "Odpowiedz Ambasady Izraela",
        "date": "22.V.1958",
        "desc": "List z Ambasady Izraela do Krzysztofa Gluchowskiego z sugestia kontaktu z Yad Vashem w sprawie walut gettowych. Oficjalna korespondencja dyplomatyczna.",
        "chapter": "Getto lodzkie",
        "person": "Krzysztof Głuchowski"
    },
    {
        "id": "N-014",
        "photo": "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p20_img01.jpeg",
        "title": "Zaproszenie na msze rocznicowa 7 P.Ul.",
        "date": "1970",
        "desc": "Zaproszenie na msze swieta rocznicowa 7 Pulku Ulanow Lubelskich AK 'Jelen'. Druk okolicznosciowy, emigracja.",
        "chapter": "Emigracja",
        "person": "7 P.Ul. AK"
    },
    {
        "id": "N-015",
        "photo": "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p21_img01.jpeg",
        "title": "Nekrolog Jana Lorensa",
        "date": "29.I.1960",
        "desc": "Nekrolog/klepsydra plutonowego Jana Lorensa, zolnierza 7 Pulku Ulanow, zmarlego 29 stycznia 1960 w Chicago. Druk zalobny.",
        "chapter": "Emigracja",
        "person": "7 P.Ul."
    },
    {
        "id": "N-016",
        "photo": "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p23_img01.jpeg",
        "title": "Galony i wstazki orderowe",
        "date": "1939-1945",
        "desc": "Trzy elementy mundurowe: galony (oznaki stopnia), wstazki orderowe. Elementy umundurowania oficera lub podoficera Wojska Polskiego.",
        "chapter": "Militaria",
        "person": "Rodzina Głuchowskich"
    },
    {
        "id": "N-017",
        "photo": "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p23_img02.jpeg",
        "title": "Kennkarte Generalnego Gubernatorstwa - okladka",
        "date": "1941-1944",
        "desc": "Okladka Kennkarte (karty rozpoznawczej) wydanej w Generalnym Gubernatorstwie. Dokument tozsamosci obowiazujacy Polakow pod okupacja niemiecka.",
        "chapter": "Okupacja",
        "person": "Krzysztof Głuchowski"
    },
    {
        "id": "N-018",
        "photo": "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p23_img03.jpeg",
        "title": "Kennkarte GG - wnetrze ze zdjeciem",
        "date": "1941-1944",
        "desc": "Wnetrze Kennkarte z fotografia legitymacyjna Krzysztofa Gluchowskiego, danymi osobowymi i odciskami palcow. Formularz niemieckojezyczny z pieczecia urzedowa.",
        "chapter": "Okupacja",
        "person": "Krzysztof Głuchowski"
    },
    {
        "id": "N-019",
        "photo": "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p23_img04.jpeg",
        "title": "Legitymacja AK + galony",
        "date": "8.IV.1944",
        "desc": "Legitymacja Armii Krajowej: Krzysztof Gluchowski, ps. 'Juras', Pluton nr 1112, ur. 29.XI.1926, datowana 8.IV.1944. Obok galony i wstazki orderowe.",
        "chapter": "AK i Powstanie",
        "person": "Krzysztof Andrzej Głuchowski"
    },
    {
        "id": "N-020",
        "photo": "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p24_img01.jpeg",
        "title": "List z Powstania - 'Krychu!'",
        "date": "VIII.1944",
        "desc": "List odreczny na papierze w kratke: 'Krychu! Krysiey jestesmy...' — list do Krzysztofa z okresu Powstania Warszawskiego. Pismo oloowkowe, warunki polowe.",
        "chapter": "AK i Powstanie",
        "person": "Krzysztof Andrzej Głuchowski"
    },
    {
        "id": "N-021",
        "photo": "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p24_img02.jpeg",
        "title": "List z Powstania do rodzicow - 26.VIII.1944",
        "date": "26.VIII.1944",
        "desc": "List odreczny: 'Warszawa 26-VIII-44, Kochana Maminko i Tatusiu...' — list Krzysztofa Andrzeja do rodzicow z Powstania Warszawskiego. Dokument o ogromnej wartosci emocjonalnej i historycznej.",
        "chapter": "AK i Powstanie",
        "person": "Krzysztof Andrzej Głuchowski"
    },
    {
        "id": "N-022",
        "photo": "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p25_img01.jpeg",
        "title": "Przepustka Jednorazowa Specjalna AK",
        "date": "29.IX.1944",
        "desc": "Przepustka Jednorazowa Specjalna Armii Krajowej, Warszawa 29 wrzesnia 1944. Pieczec Komendy Okregu Warszawskiego AK. Dokument z ostatnich dni Powstania.",
        "chapter": "AK i Powstanie",
        "person": "Krzysztof Andrzej Głuchowski"
    },
    {
        "id": "N-023",
        "photo": "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p26_img01.jpeg",
        "title": "Rozkaz awansu AK - na stopien st. ulana",
        "date": "29.IX.1944",
        "desc": "Rozkaz D-cy Grupy 'Polnoc' nr 24: awans do stopnia starszego ulana i nagrodzony Krzyzem Walecznych po raz I. Datowany 29 wrzesnia 1944, 11.9.44.",
        "chapter": "AK i Powstanie",
        "person": "Krzysztof Andrzej Głuchowski"
    },
    {
        "id": "N-024",
        "photo": "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p26_img02.jpeg",
        "title": "Legitymacja AK - zbliżenie",
        "date": "1944",
        "desc": "Zbliżenie legitymacji Armii Krajowej Krzysztofa Gluchowskiego z widocznym numerem plutonu 1112 i pseudonimem 'Juras'.",
        "chapter": "AK i Powstanie",
        "person": "Krzysztof Andrzej Głuchowski"
    },
    {
        "id": "N-025",
        "photo": "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p27_img01.jpeg",
        "title": "Bilet identyfikacyjny Stalag XI B",
        "date": "1944-1945",
        "desc": "Bilet identyfikacyjny jenca wojennego: numer 141009, pieczec 'Stalag XI B' (Fallingbostel). Maly kartonowy bilet z perforacja. Identyfikacja obozowa Krzysztofa Andrzeja.",
        "chapter": "Niewola",
        "person": "Krzysztof Andrzej Głuchowski"
    },
    {
        "id": "N-026",
        "photo": "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p27_img02.jpeg",
        "title": "Personalkarte - karta jeniecka",
        "date": "1944",
        "desc": "Personalkarte I (karta osobowa jenca) z obozu Stalag XI B. Dane: Głuchowski Krzysztof, Stanislaw Stefan (ojciec). Formularz niemieckojezyczny z danymi personalnymi, adresem rodziny.",
        "chapter": "Niewola",
        "person": "Krzysztof Andrzej Głuchowski"
    },
    {
        "id": "N-027",
        "photo": "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p28_img01.jpeg",
        "title": "Album fotograficzny CWL PSZ - strona 1",
        "date": "ok. 1944",
        "desc": "Strona albumu fotograficznego na czarnym kartonie: 4 zdjecia z zycia obozowego/wojskowego. Podpisy pod zdjeciami: 'po cwiczeniach sportowych ustawien dawag...' Fotografie grupowe zolnierzy.",
        "chapter": "Album",
        "person": "Rodzina Głuchowskich"
    },
    {
        "id": "N-028",
        "photo": "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p28_img02.jpeg",
        "title": "Album fotograficzny CWL PSZ - strona 2",
        "date": "ok. 1944",
        "desc": "Kolejna strona albumu: 4 zdjecia grupowe zolnierzy, w tym zdjecie z gitara. Scenki z zycia obozowego/koszarowego.",
        "chapter": "Album",
        "person": "Rodzina Głuchowskich"
    },
    {
        "id": "N-029",
        "photo": "Kolekcja_Gluchowski_KATALOG_NAUKOWY_p28_img03.jpeg",
        "title": "Album - okladka z dedykacja",
        "date": "8.III.1944",
        "desc": "Czarna okladka albumu z bialym napisem kaligrafowanym: 'Panu Gen. Gluchowskiemu, Dowodcy Jedn. Wojsk w 19 Brytanii, w okazji pobytu na Wyszkoleniu, Zolnierze Kompanii Dowodzenia, 8 marca 1944.' Album upominkowy od zolnierzy dla generala.",
        "chapter": "Album",
        "person": "Janusz Głuchowski"
    },

    # ===== KATALOG TEMATYCZNY =====
    {
        "id": "T-001",
        "photo": "Kolekcja_Gluchowski_Katalog_Tematyczny_p02_img01.jpeg",
        "title": "Legitymacja PON nr 2 - Marjan Gluchowski",
        "date": "1914",
        "desc": "Legitymacja Polskiej Organizacji Narodowej nr 2, wystawiona na Marjana Gluchowskiego, ur. 1867. Wnetrze otwartej legitymacji z danymi osobowymi i pieczeciami. Jeden z pierwszych czlonkow PON.",
        "chapter": "PON i niepodleglosc",
        "person": "Marian Głuchowski"
    },
    {
        "id": "T-002",
        "photo": "Kolekcja_Gluchowski_Katalog_Tematyczny_p02_img02.jpeg",
        "title": "Afisz/Zawiadomienie PON",
        "date": "2.X.1914",
        "desc": "Drukowane zawiadomienie o zebraniu PON w sali 'Lutni', 2 pazdziernika. Prelegenci: Waclaw Sieroszewski, Juljusz Kaden i Marjan Dabrowski. Podpis: Komisarz PON na powiat Czestochowski — Marjan Gluchowski. Wejscie bezplatne.",
        "chapter": "PON i niepodleglosc",
        "person": "Marian Głuchowski"
    },
    {
        "id": "T-003",
        "photo": "Kolekcja_Gluchowski_Katalog_Tematyczny_p02_img03.jpeg",
        "title": "Rozkaz PON - pismo urzedowe L.145",
        "date": "1914",
        "desc": "Pismo Polskiej Organizacji Narodowej, Komisja Organizacyjna, L.145, do M. Gluchowskiego. Naglowek z pieciatka PON. Odrecznie podpisane.",
        "chapter": "PON i niepodleglosc",
        "person": "Marian Głuchowski"
    },
    {
        "id": "T-004",
        "photo": "Kolekcja_Gluchowski_Katalog_Tematyczny_p03_img01.jpeg",
        "title": "Pokwitowanie PON - 2 szable i bron",
        "date": "1914",
        "desc": "Pokwitowanie Polskiej Organizacyi Narodowej na 200 kop., 2 szable, latarka, reflektor, i inne. Formularz z odrecznie wpisanymi danymi, podpis Oficera Wojsk Polskich.",
        "chapter": "PON i niepodleglosc",
        "person": "Marian Głuchowski"
    },
    {
        "id": "T-005",
        "photo": "Kolekcja_Gluchowski_Katalog_Tematyczny_p03_img02.jpeg",
        "title": "Koperta urzedowa PON + Karta Polowa Legionow",
        "date": "1914-1918",
        "desc": "Dwa przedmioty: koperta 'Urzedowa' adresowana do Gluchowskiego, Komisarza na powiat Czestochowy, oraz Karta Polowa Legionow / Feldpostkarte z orlem legionowym.",
        "chapter": "PON i niepodleglosc",
        "person": "Marian Głuchowski"
    },
    {
        "id": "T-006",
        "photo": "Kolekcja_Gluchowski_Katalog_Tematyczny_p04_img01.jpeg",
        "title": "Biogram WBH - Wojskowe Biuro Historyczne",
        "date": "24.V.1937",
        "desc": "Biogram nr 76/45 z Wojskowego Biura Historycznego, 24 maja 1937. Zaswiadczenie o sluzbie Janusza Gluchowskiego: OB PPS, ZWC w Liege, patrol kawaleryjski 2.VIII.1914 do Krakowa i na Kielce, ZS Oleandry.",
        "chapter": "Kariera wojskowa",
        "person": "Janusz Głuchowski"
    },
    {
        "id": "T-007",
        "photo": "Kolekcja_Gluchowski_Katalog_Tematyczny_p04_img02.jpeg",
        "title": "Fotokopia 'Siodemki' z podpisami",
        "date": "2-3.VIII.1914",
        "desc": "Fotokopia historycznego zdjecia 'Siodemki Beliny' - pierwszego patrolu kawaleryjskiego Legionow Polskich. Podpisy: Belina-Prażmowski, Głuchowski, Grzmot-Skotnicki, Karnacki i inni. Moment zalozycielski polskiej kawalerii odrodzonej.",
        "chapter": "Legiony i I wojna",
        "person": "Janusz Głuchowski"
    },
    {
        "id": "T-008",
        "photo": "Kolekcja_Gluchowski_Katalog_Tematyczny_p05_img01.jpeg",
        "title": "List odreczny na papierze Inspektoratu Armii",
        "date": "lata 30.",
        "desc": "List odreczny na papierze firmowym Inspektoratu Armii (Sosnkowskiego). Pismo kaligraficzne atramentem.",
        "chapter": "Kariera wojskowa",
        "person": "Janusz Głuchowski"
    },
    {
        "id": "T-009",
        "photo": "Kolekcja_Gluchowski_Katalog_Tematyczny_p05_img02.jpeg",
        "title": "Zaswiadczenie o przynaleznosci do OB PPS 1905-1908",
        "date": "I.1935",
        "desc": "Zaswiadczenie ze Gluchowski nalezal do Organizacji Bojowej PPS od roku 1905 do 1908. Podpis: Inspektor Armii (Kazimierz Sosnkowski), Warszawa, styczen 1935. Dokument potwierdzajacy rewolucyjna przeszlosc.",
        "chapter": "Kariera wojskowa",
        "person": "Janusz Głuchowski"
    },
    {
        "id": "T-010",
        "photo": "Kolekcja_Gluchowski_Katalog_Tematyczny_p05_img03.jpeg",
        "title": "Fotografia grupowa oficerow",
        "date": "lata 30.",
        "desc": "Ciemna fotografia grupowa oficerow w mundurach. Trudna do identyfikacji ze wzgledu na slaba jakosc reprodukcji.",
        "chapter": "Kariera wojskowa",
        "person": "Janusz Głuchowski"
    },
    {
        "id": "T-011",
        "photo": "Kolekcja_Gluchowski_Katalog_Tematyczny_p05_img04.jpeg",
        "title": "Zaswiadczenie o zlozeniu broni 1909",
        "date": "10.III.1925",
        "desc": "Zaswiadczenie archiwalne ze Gluchowski zlozyl bron (rewolwer) w roku 1909 na szarze Milosci. Pieczec Archiwum Glownego Akt Dawnych, data 10.III.1925.",
        "chapter": "Kariera wojskowa",
        "person": "Janusz Głuchowski"
    },
    {
        "id": "T-012",
        "photo": "Kolekcja_Gluchowski_Katalog_Tematyczny_p05_img05.jpeg",
        "title": "Notatka o Zwiazku Strzeleckim",
        "date": "ok. 1910-1914",
        "desc": "Notatka odręczna — informacja o oficerach ZS, kompaniach, Krakowie. Lista punktow dot. Zwiazku Strzeleckiego i przygotowania kadr wojskowych.",
        "chapter": "Legiony i I wojna",
        "person": "Janusz Głuchowski"
    },
    {
        "id": "T-013",
        "photo": "Kolekcja_Gluchowski_Katalog_Tematyczny_p06_img01.jpeg",
        "title": "Rozkaz utworzenia oddzialu jazdy - Lublin 5.XI.1918",
        "date": "5.XI.1918",
        "desc": "Rozkaz Sztabu Generalnego, Lublin 5 listopada 1918: Rotmistrzowi Januszowi Gluchowskiemu nakazuje sie organizowac nowo-oddzielony oddzial jazdy w Lubelskiem. Moment zalozycielski 7 Pulku Ulanow!",
        "chapter": "7 Pulk Ulanow",
        "person": "Janusz Głuchowski"
    },
    {
        "id": "T-014",
        "photo": "Kolekcja_Gluchowski_Katalog_Tematyczny_p06_img02.jpeg",
        "title": "List odreczny Smiglego-Rydza do Gluchowskiego",
        "date": "ok. 1935-1939",
        "desc": "List odreczny na papierze firmowym — do Majora/Pulkownika Gluchowskiego. Charakter pisma i kontekst sugeruja autorstwo Marszalka Edwarda Smiglego-Rydza.",
        "chapter": "Kariera wojskowa",
        "person": "Janusz Głuchowski"
    },
    {
        "id": "T-015",
        "photo": "Kolekcja_Gluchowski_Katalog_Tematyczny_p07_img01.jpeg",
        "title": "Pismo Ministerstwa Spraw Wojskowych",
        "date": "lata 30.",
        "desc": "Ministerstwo Spraw Wojskowych, Biuro Personalne — pismo L.97/... do Plk. Gluchowskiego. Oficjalne pismo ministerialne dot. mianowania lub audiencji.",
        "chapter": "Kariera wojskowa",
        "person": "Janusz Głuchowski"
    },
    {
        "id": "T-016",
        "photo": "Kolekcja_Gluchowski_Katalog_Tematyczny_p07_img02.jpeg",
        "title": "Dyplom Krola Rumunii Ferdynanda I",
        "date": "XII.1922",
        "desc": "Dyplom Krola Rumunii Ferdynanda I — nadanie orderu rumunskiego (Ordinul Coroanei Romaniei). Kaligrafowany dokument na pergaminie z pieczecia i podpisem Ferdynanda. Dokument dyplomatyczny o duzej wartosci.",
        "chapter": "Odznaczenia",
        "person": "Janusz Głuchowski"
    },
    {
        "id": "T-017",
        "photo": "Kolekcja_Gluchowski_Katalog_Tematyczny_p08_img01.jpeg",
        "title": "Adres iluminowany - akwarela 1945",
        "date": "IX.1945",
        "desc": "Adres iluminowany (akwarela): 'Panu Generalowi Januszowi Gluchowskiemu C.B. na pamiatke milej wspolpracy od Oficerow A.M.S.i La..., wrzesien 1945.' Kolorowe flagi (brytyjska, polska), herb kawalerii. Piekny dokument artystyczny.",
        "chapter": "PSZ na Zachodzie",
        "person": "Janusz Głuchowski"
    },
    {
        "id": "T-018",
        "photo": "Kolekcja_Gluchowski_Katalog_Tematyczny_p08_img02.jpeg",
        "title": "Dekret Prezydenta RP",
        "date": "lata 30.",
        "desc": "Dekret Prezydenta Rzeczypospolitej Polskiej — Ministerstwo Spraw Wojskowych, kontrasygna Ministra. Oficjalny akt mianowania, na grubym papierze urzedowym.",
        "chapter": "Kariera wojskowa",
        "person": "Janusz Głuchowski"
    },
    {
        "id": "T-019",
        "photo": "Kolekcja_Gluchowski_Katalog_Tematyczny_p09_img01.jpeg",
        "title": "Mianowanie na generala brygady - 1933",
        "date": "26.III.1933",
        "desc": "Akt mianowania w korpusie generalow: Gen.bryg. Gluchowski Janusz — dowodca Okregu Korpusu Nr I(?), 26 marca 1933. Podpisy Prezydenta RP i Ministra Spraw Wojskowych.",
        "chapter": "Kariera wojskowa",
        "person": "Janusz Głuchowski"
    },
    {
        "id": "T-020",
        "photo": "Kolekcja_Gluchowski_Katalog_Tematyczny_p09_img02.jpeg",
        "title": "Mianowanie na I Wiceministra - 1935",
        "date": "5.X.1935",
        "desc": "Akt mianowania w korpusie generalow: Generala brygady Gluchowskiego Janusza, dnia 5 pazdziernika 1935. Prezydent RP + Minister MSWojsk. Pieczec Ministerstwa. Mianowanie na I Wiceministra Spraw Wojskowych!",
        "chapter": "Kariera wojskowa",
        "person": "Janusz Głuchowski"
    },
    {
        "id": "T-021",
        "photo": "Kolekcja_Gluchowski_Katalog_Tematyczny_p10_img01.jpeg",
        "title": "Rozkaz wyjazdu - formularz MSWojsk",
        "date": "lata 30.",
        "desc": "Rozkaz wyjazdu — Ministerstwo Spraw Wojskowych, SZTAB, Seria J nr 116321. General bryg. Gluchowski Janusz, cel podrozy: inspekcja. Formularz sluzbowy z pieczecia.",
        "chapter": "Kariera wojskowa",
        "person": "Janusz Głuchowski"
    },
    {
        "id": "T-022",
        "photo": "Kolekcja_Gluchowski_Katalog_Tematyczny_p11_img01.jpeg",
        "title": "List prywatny do Pulkownika Gluchowskiego",
        "date": "4.VIII.1925",
        "desc": "Koperta 'S. Wielmozny Pan Pulkownik J. Gluchowski' + list odreczny na monogramowanym papierze (inicjaly), datowany 4/8 '25. List prywatny z pieciatka monogramowana.",
        "chapter": "Korespondencja",
        "person": "Janusz Głuchowski"
    },
    {
        "id": "T-023",
        "photo": "Kolekcja_Gluchowski_Katalog_Tematyczny_p12_img01.jpeg",
        "title": "Zyczenia od Samorzadu Zolnierskiego 7 P.Ul.",
        "date": "5.I.",
        "desc": "Zyczenia swiateczne od Samorzadu Zolnierskiego 7 Pulku Ulanow: 'do Majora Gluchowskiego Janusza, D-cy 7-go P.Ulanow, w imieniu oficerow i szeregowych...' Pieczec 7 P.Ul., podpis.",
        "chapter": "7 Pulk Ulanow",
        "person": "Janusz Głuchowski"
    },
    {
        "id": "T-024",
        "photo": "Kolekcja_Gluchowski_Katalog_Tematyczny_p12_img02.jpeg",
        "title": "Propusk w plen + legitymacja + pokwitowanie",
        "date": "1914-1920",
        "desc": "Trzy dokumenty na jednym zdjeciu: 'Propusk w plen' (rosyjski przepustek do niewoli z pieczecia Sztabu), mala zielona legitymacja/bilet, pokwitowanie z podpisem i pieczecia (Lublin).",
        "chapter": "Legiony i I wojna",
        "person": "Janusz Głuchowski"
    },
    {
        "id": "T-025",
        "photo": "Kolekcja_Gluchowski_Katalog_Tematyczny_p12_img03.jpeg",
        "title": "Legitymacja Krzyza Walecznych nr 42888",
        "date": "31.VII.1922",
        "desc": "Legitymacja Krzyza Walecznych: Dowodztwo M.S.Wojsk., Nr leg. 42888. Rtm. Gluchowski Janusz, oddzial 7 P.Ul., uprawnionym do noszenia Krzyza Walecznych, Krzyz z 1 okuciem, Rozkazem Nr 12793/22. Podpis Ministra Spraw Wojskowych.",
        "chapter": "Odznaczenia",
        "person": "Janusz Głuchowski"
    },
    {
        "id": "T-026",
        "photo": "Kolekcja_Gluchowski_Katalog_Tematyczny_p13_img01.jpeg",
        "title": "Fotokopia prasowa - Smigly-Rydz wreca sztandar 17 P.Ul.",
        "date": "ok. 1937",
        "desc": "Fotokopia: Marszalek Edward Smigly-Rydz wrecza sztandar 17 Pulku Ulanow Wielkopolskich. Podpisy: d-ca Brygady gen. Janusz Gluchowski, gen. Roman Abraham, gen. Knoll-Kownacki, plk Kowalczewski.",
        "chapter": "Kariera wojskowa",
        "person": "Janusz Głuchowski"
    },
    {
        "id": "T-027",
        "photo": "Kolekcja_Gluchowski_Katalog_Tematyczny_p13_img02.jpeg",
        "title": "Portret gen. Janusza Gluchowskiego",
        "date": "lata 30.",
        "desc": "Portret fotograficzny gen. Janusza Gluchowskiego w mundurze galowym z orderami i epoletami. Zdjecie studyjne. Jedyne zdjecie portretowe generala w kolekcji.",
        "chapter": "Dokumenty osobiste",
        "person": "Janusz Głuchowski"
    },
    {
        "id": "T-028",
        "photo": "Kolekcja_Gluchowski_Katalog_Tematyczny_p13_img03.jpeg",
        "title": "List do Generala - Londyn 14.IX.1943",
        "date": "14.IX.1943",
        "desc": "List odreczny: 'Szanowny Panie Generale!' — datowany 14.IX.1943, kaligraficzne pismo atramentem. Korespondencja z okresu londynskiego.",
        "chapter": "PSZ na Zachodzie",
        "person": "Janusz Głuchowski"
    },
    {
        "id": "T-029",
        "photo": "Kolekcja_Gluchowski_Katalog_Tematyczny_p14_img01.jpeg",
        "title": "Pismo z 2 Pulku Piechoty Legionowej",
        "date": "20.IX.1943",
        "desc": "Dowodca 2 Pulku Piechoty Legionowej, Zambrow — pismo do Gen.bryg. Gluchowskiego Janusza. Dokument wojskowy PSZ z okresu wojny.",
        "chapter": "PSZ na Zachodzie",
        "person": "Janusz Głuchowski"
    },
    {
        "id": "T-030",
        "photo": "Kolekcja_Gluchowski_Katalog_Tematyczny_p15_img01.jpeg",
        "title": "Legitymacja odznaki 3 Dywizji Strzelcow Karpackich",
        "date": "1945-1946",
        "desc": "Legitymacja nr 21488 — St.ul. Gluchowski upowazniony do posiadania i noszenia Pamiatowej Odznaki 3 Dywizji Strzelcow Karpackich. Pieczec: Tobruk, Cassino, D-ca 3 DSK. Podpis gen.bryg.",
        "chapter": "PSZ na Zachodzie",
        "person": "Krzysztof Andrzej Głuchowski"
    },
    {
        "id": "T-031",
        "photo": "Kolekcja_Gluchowski_Katalog_Tematyczny_p15_img02.jpeg",
        "title": "Dwie legitymacje pulkowe",
        "date": "1946",
        "desc": "Dwie legitymacje: (1) St.ulan Gluchowski Krzysztof — odznaka pamiatkowa 7 Pulku Ulanow Lubelskich, 23.III.1946. (2) Gen.Brygad. Gluchowski Janusz — Znak pulkowy 20 Pulku Ulanow, Rzeszow.",
        "chapter": "Odznaczenia",
        "person": "Rodzina Głuchowskich"
    },

    # ===== SERIA 29z - KORESPONDENCJA OBOZOWA =====
    {
        "id": "S-001",
        "photo": "Seria_29z_p02_img01.jpeg",
        "title": "Stempel cenzora obozowego",
        "date": "1944",
        "desc": "Stempel/pieczatka na papierze w kratke — wyblakly stempel cenzora obozowego lub pocztowego. Fragment korespondencji obozowej.",
        "chapter": "Korespondencja obozowa",
        "person": "Rodzina Głuchowskich"
    },
    {
        "id": "S-002",
        "photo": "Seria_29z_p02_img02.jpeg",
        "title": "List obozowy na papierze w kratke",
        "date": "16.X.1944",
        "desc": "List odreczny na papierze w kratke, bardzo zniszczony, pozolkly, z ubytkami. Datowany '16.X...' Charakter pisma sugeruje warunki obozowe. Pismo olowkowe.",
        "chapter": "Korespondencja obozowa",
        "person": "Stanisław Stefan Głuchowski"
    },
    {
        "id": "S-003",
        "photo": "Seria_29z_p03_img01.jpeg",
        "title": "Adres baraku obozowego",
        "date": "1944-1945",
        "desc": "Adres na kartce/kopercie: 'Ppor. Stefan... Gluchowski... Barak 20 Lind...' — adres baraku w obozie jenieckim. Pismo olowkowe na kartonie.",
        "chapter": "Korespondencja obozowa",
        "person": "Stanisław Stefan Głuchowski"
    },
    {
        "id": "S-004",
        "photo": "Seria_29z_p03_img02.jpeg",
        "title": "List Krzysztofa z obozu - nr 141009",
        "date": "1944-1945",
        "desc": "List odreczny na kartonie: wspomina nr 141009 (numer jeniecki Krzysztofa), Stalag XI B. Konczy sie slowami 'Trzymamy sie do konca!' Wazny dokument morale obozowego.",
        "chapter": "Korespondencja obozowa",
        "person": "Krzysztof Andrzej Głuchowski"
    },
    {
        "id": "S-005",
        "photo": "Seria_29z_p04_img01.jpeg",
        "title": "Kriegsgefangenenpost - kartka jenieca (awers)",
        "date": "20.X.1944",
        "desc": "Karta pocztowa jenca wojennego (Kriegsgefangenenpost / Postkarte). Nadawca: Gluchowski, nr jeniecki 0.1245. Adresat: do Zofii, ul. Pulawska, Kleczew, gmina Brzezowce, powiat Radomsko, Generalgouvernement. Stempel: 20.10.44.",
        "chapter": "Korespondencja obozowa",
        "person": "Stanisław Stefan Głuchowski"
    },
    {
        "id": "S-006",
        "photo": "Seria_29z_p04_img02.jpeg",
        "title": "Kriegsgefangenenpost - kartka jenieca (rewers)",
        "date": "14.X.1944",
        "desc": "Rewers kartki: M.-Stammlager XI B, 14.X.1944. 'Droga Zocha! Jestem w oflagu, Krzysztof w Stalagu...' Pisze z obozu Fallingbostel, pyta o rodzine. Korespondencja miedzy ojcem a zona.",
        "chapter": "Korespondencja obozowa",
        "person": "Stanisław Stefan Głuchowski"
    },
    {
        "id": "S-007",
        "photo": "Seria_29z_p05_img01.jpeg",
        "title": "Antwort-Postkarte - karta odpowiedzi (awers)",
        "date": "XI.1945",
        "desc": "Kriegsgefangenenpost / Antwort-Postkarte. Nadawca: Gluchowski Krzysztof, St.Uf., Stalag VI/3, Dorsten in Westfalen. Adresat: Anna Maria, Glowno, Osiny, Lowicz. Stempel cenzury.",
        "chapter": "Korespondencja obozowa",
        "person": "Krzysztof Andrzej Głuchowski"
    },
    {
        "id": "S-008",
        "photo": "Seria_29z_p05_img02.jpeg",
        "title": "Antwort-Postkarte - karta odpowiedzi (rewers)",
        "date": "1945",
        "desc": "Rewers karty odpowiedzi od rodziny: 'Kochany Krzysiu! ...Marus... Twoja Cioteczka Czestochowa... Lawka i jej coreczka...' List od rodziny do jenca. Podpis Maria.",
        "chapter": "Korespondencja obozowa",
        "person": "Rodzina Głuchowskich"
    },
    {
        "id": "S-009",
        "photo": "Seria_29z_p06_img01.jpeg",
        "title": "List obozowy do Stryja - rewers",
        "date": "19.X.1944",
        "desc": "Kriegsgefangenenlager, 19.X.1944. 'Kochany Stryju i Ciociu! Zostalismy obaj w OP...' — list z obozu do stryja (gen. Janusza?), wspomina 2417 km podrozy. Podpis Krzysztof.",
        "chapter": "Korespondencja obozowa",
        "person": "Krzysztof Andrzej Głuchowski"
    },
    {
        "id": "S-010",
        "photo": "Seria_29z_p06_img02.jpeg",
        "title": "Kartka z obozu do gen. Janusza w Londynie",
        "date": "X.1944",
        "desc": "Kriegsgefangenenpost / Postkarte. Nadawca: St.Uf. Krzysztof Gluchowski, nr 141009, M.-Stammlager XI B. Adresat: GENERAL JANUSZ GLUCHOWSKI, London, Polish War's Office, ENGLAND. Stempel PASSED XII. Korespondencja obozowa do stryja-generala w Londynie!",
        "chapter": "Korespondencja obozowa",
        "person": "Krzysztof Andrzej Głuchowski"
    },
    {
        "id": "S-011",
        "photo": "Seria_29z_p07_img01.jpeg",
        "title": "Korespondencja miedzy dwoma jencami - ojciec do syna",
        "date": "XI.1944",
        "desc": "Kriegsgefangenenpost / Rückantwortbrief. Do: Gluchowski St.Uf. Krzysztof, nr 141009, Stalag VI/3 Dorsten. Nadawca: Ppor. Stefan Gluchowski, nr 0.1845, Stalag XI B. Pieczec cenzury. KORESPONDENCJA MIEDZY DWOMA JENCAMI — ojciec i syn w roznych obozach!",
        "chapter": "Korespondencja obozowa",
        "person": "Stanisław Stefan i Krzysztof Andrzej"
    },
    {
        "id": "S-012",
        "photo": "Seria_29z_p07_img02.jpeg",
        "title": "List ojca do syna - rewers",
        "date": "XI.1944",
        "desc": "Rewers listu Stefana do Krzysztofa. Dlugi list o rodzinie, 'Mama na ul. Howe-Monatkiego w Czestochowie', wspomina wielu krewnych. Podpis 'Stefek'. Intymna korespondencja rodzinna z niewoli.",
        "chapter": "Korespondencja obozowa",
        "person": "Stanisław Stefan Głuchowski"
    },
    {
        "id": "S-013",
        "photo": "Seria_29z_p08_img01.jpeg",
        "title": "Dlugi list obozowy - 2 strony",
        "date": "XI.1944",
        "desc": "Rozlozony list dwustronny (Détachez le long du pointillé / Hier abtrennen!). Obie strony gescie zapisane olowkiem. Szczegoowy opis zycia obozowego, rodziny, 17 punktow.",
        "chapter": "Korespondencja obozowa",
        "person": "Krzysztof Andrzej Głuchowski"
    },
    {
        "id": "S-014",
        "photo": "Seria_29z_p08_img02.jpeg",
        "title": "Koperta Kriegsgefangenenpost - Krzysztof do Stefana",
        "date": "7.XI.1944",
        "desc": "Koperta: Kriegsgefangenenpost, do Ppor. Stefana Gluchowskiego, nr 01245, Stalag XI B. Nadawca: St.Uf. Krzysztof Gluchowski. Stempel cenzury '27 Gepruft Stalag XI B', stempel 7.11.44.",
        "chapter": "Korespondencja obozowa",
        "person": "Krzysztof Andrzej Głuchowski"
    },
    {
        "id": "S-015",
        "photo": "Seria_29z_p09_img01.jpeg",
        "title": "Trzy fotografie obozowe",
        "date": "1944-1945",
        "desc": "Trzy male fotografie: widoki budynkow/osiedli, prawdopodobnie Fallingbostel lub okolice obozu. Budynek mieszkalny, aleja z drzewami, brama wjazdowa. Dokumentacja wizualna miejsca internowania.",
        "chapter": "Niewola",
        "person": "Rodzina Głuchowskich"
    },
    {
        "id": "S-016",
        "photo": "Seria_29z_p10_img01.jpeg",
        "title": "Kartka Stefana z obozu - awers",
        "date": "4.XII.1944",
        "desc": "Kriegsgefangenenpost. Nadawca: Ppor. Stefan Gluchowski, nr 0.1845, M.-Stammlager XI B. Adresat: Pani(?), ul. Piaseczna, Kleczew. Stempel: 04.12.44. Kolejna kartka obozowa ojca.",
        "chapter": "Korespondencja obozowa",
        "person": "Stanisław Stefan Głuchowski"
    },
    {
        "id": "S-017",
        "photo": "Seria_29z_p10_img02.jpeg",
        "title": "Kartka Stefana - rewers 30.X.1944",
        "date": "30.X.1944",
        "desc": "Rewers kartki, datowany 30.X.1944. Dlugi list olowkiem. Wspomina nr 141009 (numer Krzysztofa), pisze o warunkach obozowych. Podpis 'Stefan'.",
        "chapter": "Korespondencja obozowa",
        "person": "Stanisław Stefan Głuchowski"
    },
    {
        "id": "S-018",
        "photo": "Seria_29z_p11_img01.jpeg",
        "title": "Notatki z Powstania Warszawskiego",
        "date": "VIII-X.1944",
        "desc": "Fragmenty notatek z Powstania. Wspomina 'Powstanie', obliczenia numeryczne (45, 1.56, 64.18, 92), 'Krzysiek i Gryfon'. Notatki polowe z walk.",
        "chapter": "AK i Powstanie",
        "person": "Krzysztof Andrzej Głuchowski"
    },
    {
        "id": "S-019",
        "photo": "Seria_29z_p11_img02.jpeg",
        "title": "Tabela/rozklad marszowy jednostki",
        "date": "1944-1945",
        "desc": "Recznie narysowana tabelka z liczbami (kalendarz operacyjny?). '8 DPMK 3 SF Remo 10 Genova 11 Fort 12 Pol 13 Brit.' — rozklad marszowy lub transport jednostki.",
        "chapter": "PSZ na Zachodzie",
        "person": "Krzysztof Andrzej Głuchowski"
    },
    {
        "id": "S-020",
        "photo": "Seria_29z_p12_img01.jpeg",
        "title": "Karta zdrowia obozowa - rewers (Heilimpfungen)",
        "date": "1944-1945",
        "desc": "Karta zdrowia obozowa (Gesundheitskarte) — formularz medyczny jenca: Art der Krankheit, Schutz- und Heilimpfungen, Gewichtstabelle. Tabela szczepien i wagi jenca wojennego.",
        "chapter": "Niewola",
        "person": "Krzysztof Andrzej Głuchowski"
    },
    {
        "id": "S-021",
        "photo": "Seria_29z_p12_img02.jpeg",
        "title": "Karta zdrowia M.-Stammlager VI J - awers",
        "date": "1944",
        "desc": "Awers karty zdrowia: M.-Stammlager VI J, Gesundheitskarte. Dane jenca nieczytelne. Karta z INNEGO obozu niz XI B — swiadczy o przenoszeniu miedzy obozami.",
        "chapter": "Niewola",
        "person": "Krzysztof Andrzej Głuchowski"
    },
    {
        "id": "S-022",
        "photo": "Seria_29z_p13_img01.jpeg",
        "title": "Pamietnik obozowy - strona 1",
        "date": "1944-1945",
        "desc": "Zeszyt wspomnieniowy/pamietnik z okresu obozowego. Gescie zapisana strona. Wspomina 'Gluchowski', 'Powstanie', 'Krakowie', 'Boze Narodzenie', 'Londyn'.",
        "chapter": "Pamietnik",
        "person": "Krzysztof Andrzej Głuchowski"
    },
    {
        "id": "S-023",
        "photo": "Seria_29z_p13_img02.jpeg",
        "title": "Pamietnik obozowy - strona 2",
        "date": "1944-1945",
        "desc": "Kontynuacja pamietnika. 'Jestem w Glenboock(?)... nr 141009 — to...' — wspomina numer obozowy. Pismo olowkowe i atramentem.",
        "chapter": "Pamietnik",
        "person": "Krzysztof Andrzej Głuchowski"
    },
    {
        "id": "S-024",
        "photo": "Seria_29z_p13_img03.jpeg",
        "title": "Pamietnik obozowy - strona 3 (wspomnienia z dziecinstwa)",
        "date": "1944-1945",
        "desc": "'Dziecinstwo moje to szczesliwe...' — wspomnienia autobiograficzne pisane niebieskim atramentem. Fragmenty o dziecinstwie i zyciu przed wojna.",
        "chapter": "Pamietnik",
        "person": "Krzysztof Andrzej Głuchowski"
    },
    {
        "id": "S-025",
        "photo": "Seria_29z_p13_img04.jpeg",
        "title": "Pamietnik obozowy - strona 4",
        "date": "1944-1945",
        "desc": "Kolejna strona wspomnien z pamietnika. Ciepla Halemka(?), daty, wspomnienia rodzinne. Pismo olowkowe na pozolklym papierze.",
        "chapter": "Pamietnik",
        "person": "Krzysztof Andrzej Głuchowski"
    },
    {
        "id": "S-026",
        "photo": "Seria_29z_p14_img01.jpeg",
        "title": "Notatnik na papierze w kratke - Stalag VI/17",
        "date": "1944-1945",
        "desc": "Gesto zapisana strona na papierze w kratke. 'Stalag VI/17' widoczne w srodku. Opis obozow, dat, przerzutow. Bardzo geste, drobne pismo — formalny zapis doswiadczen obozowych.",
        "chapter": "Pamietnik",
        "person": "Krzysztof Andrzej Głuchowski"
    },
    {
        "id": "S-027",
        "photo": "Seria_29z_p14_img02.jpeg",
        "title": "Wspomnienia 1940 - papier w kratke",
        "date": "1944-1945",
        "desc": "'Pamietam, jak w roku 1940 uderzyl mnie...' — wspomnienia wojenne na papierze w kratke. Dwie kolumny tekstu i notatki na marginesach.",
        "chapter": "Pamietnik",
        "person": "Krzysztof Andrzej Głuchowski"
    },
    {
        "id": "S-028",
        "photo": "Seria_29z_p14_img03.jpeg",
        "title": "Notatki na formularzu Kaufmannsgehilfenprüfung",
        "date": "1944-1945",
        "desc": "Formularz egzaminu kupieckiego Izby Przemyslowo-Handlowej Gladbach-Rheydt-Neuss, wykorzystany jako papier do notatek. Rysunki geometryczne i zapisy olowkowe na odwrocie. Typowy recykling papieru w obozie.",
        "chapter": "Pamietnik",
        "person": "Krzysztof Andrzej Głuchowski"
    },
    {
        "id": "S-029",
        "photo": "Seria_29z_p15_img01.jpeg",
        "title": "Formularz kupiecki z notatkami i rysunkiem",
        "date": "1944-1945",
        "desc": "Kolejny formularz Kaufmannsgehilfenprufung z notatkami na odwrocie. Rysunek geometryczny i drobne pismo olowkowe.",
        "chapter": "Pamietnik",
        "person": "Krzysztof Andrzej Głuchowski"
    },
    {
        "id": "S-030",
        "photo": "Seria_29z_p15_img02.jpeg",
        "title": "Mapka taktyczna z kompasem - Wolomin",
        "date": "1944",
        "desc": "Strona z notatkami i mapka/schematem z kompasem (N), 'na Wolominie' widoczne. Opis terenow walk? Mapka taktyczna z okresu Powstania pisana w obozie z pamieci.",
        "chapter": "AK i Powstanie",
        "person": "Krzysztof Andrzej Głuchowski"
    },
    {
        "id": "S-031",
        "photo": "Seria_29z_p15_img03.jpeg",
        "title": "Notatki powojenne - 22.VIII.1945",
        "date": "22.VIII.1945",
        "desc": "Formularz Kaufmannsgehilfenprufung z notatkami datowanymi 22.VIII.1945 — juz PO wyzwoleniu. 'Obecnie jestem juz...' Zapis przejscia od niewoli do wolnosci.",
        "chapter": "Wyzwolenie",
        "person": "Krzysztof Andrzej Głuchowski"
    },
    {
        "id": "S-032",
        "photo": "Seria_29z_p16_img01.jpeg",
        "title": "Pamietnik - Bitwy, rok 1934",
        "date": "1944-1945",
        "desc": "Strona z zeszytu: 'Bitwy i...' — wspomina rok 1934. Notatki na papierze w kratke, atrament i olowek. Kontynuacja pamietnika obozowego.",
        "chapter": "Pamietnik",
        "person": "Krzysztof Andrzej Głuchowski"
    },
    {
        "id": "S-033",
        "photo": "Seria_29z_p16_img02.jpeg",
        "title": "Pamietnik - Leznosc, Stalgow",
        "date": "1944-1945",
        "desc": "Gesto zapisana strona, wspomina 'Leznosc', 'Stalgow', daty. Kontynuacja pamietnika. Pismo atramentem i olowkiem.",
        "chapter": "Pamietnik",
        "person": "Krzysztof Andrzej Głuchowski"
    },
    {
        "id": "S-034",
        "photo": "Seria_29z_p17_img01.jpeg",
        "title": "List powojenny - 6.VII.1945",
        "date": "6.VII.1945",
        "desc": "List odreczny datowany 6.7.1945. Wspomina Bogdana, Palestine, Polske. Kaligraficzne pismo atramentem na bialym papierze. Korespondencja powojenna.",
        "chapter": "Wyzwolenie",
        "person": "Krzysztof Andrzej Głuchowski"
    },
    {
        "id": "S-035",
        "photo": "Seria_29z_p17_img02.jpeg",
        "title": "List na papeterii Emil Schröder & Co - Düsseldorf",
        "date": "23.II.1945",
        "desc": "List odreczny po polsku na papierze firmowym fabryki lakierow Emil Schroder & Co G.M.B.H. z Dusseldorfu-Grafenbergu. Recykling papeterii niemieckiej — typowe dla Displaced Persons. Wspomina Bogdane, Polizei, Warszawa.",
        "chapter": "Wyzwolenie",
        "person": "Krzysztof Andrzej Głuchowski"
    },
    {
        "id": "S-036",
        "photo": "Seria_29z_p18_img01.jpeg",
        "title": "Relacja z Powstania Warszawskiego",
        "date": "1944-1945",
        "desc": "RELACJA Z POWSTANIA WARSZAWSKIEGO — gesto zapisana strona. Wspomina 'Gestapo przy 41 branka', '508 strat', 'gen. Bora Komorowskiego', '3 VIII.44 zginal', '1112 odznacz', 'Kompanii Saperow'. Konkretne daty i straty. DOKUMENT O OGROMNEJ WARTOSCI HISTORYCZNEJ.",
        "chapter": "AK i Powstanie",
        "person": "Krzysztof Andrzej Głuchowski"
    },
    {
        "id": "S-037",
        "photo": "Seria_29z_p18_img02.jpeg",
        "title": "List z Düsseldorfu po wyzwoleniu - 2.VI.1945",
        "date": "2.VI.1945",
        "desc": "Datowany Mowe 2.VI.1945. 'Kochajni Ciociu i Stryju! Jestem obecnie w Dusseldorfie. Oswobodzony z niewoli 24/V przez Amerykanow...' Szczegolowa relacja z Powstania i kampanii. Wspomina V.S.O.P., Bora Komorowskiego, kapitulacje 2.X.44.",
        "chapter": "Wyzwolenie",
        "person": "Krzysztof Andrzej Głuchowski"
    },
    {
        "id": "S-038",
        "photo": "Seria_29z_p19_img01.jpeg",
        "title": "Kontynuacja listu - 2.II.1945",
        "date": "2.II.1945",
        "desc": "Datowany 2.II.1945, podpis Krzysztof. Kontynuacja listu z relacja z doswiadczen obozowych. Wspomina Chrystopza, Stryja.",
        "chapter": "Korespondencja obozowa",
        "person": "Krzysztof Andrzej Głuchowski"
    },
    {
        "id": "S-039",
        "photo": "Seria_29z_p19_img02.jpeg",
        "title": "List na papeterii Emil Schröder - 5.VIII.1949",
        "date": "5.VIII.1949",
        "desc": "List na papierze firmowym Emil Schroder & Co, datowany 5.VIII.1949. Korespondencja powojenna. Wspomina Stalag XI B, Babke, Ludke. Cztery lata po wyzwoleniu — kontynuacja kontaktow z Niemiec.",
        "chapter": "Emigracja",
        "person": "Krzysztof Andrzej Głuchowski"
    },
    {
        "id": "S-040",
        "photo": "Seria_29z_p20_img01.jpeg",
        "title": "Ulotka repatriacyjna 'Nareszcie... RODACY' (awers)",
        "date": "1945",
        "desc": "Drukowana odezwa do polskich jencow we Francji po wyzwoleniu: 'Nareszcie... RODACY — Nareszcie nadeszla radosna chwila... powrotu na lono Ojczyzny...' Z lista konsulatow i agencji PCK we Francji. Cenny druk repatriacyjny.",
        "chapter": "Wyzwolenie",
        "person": "Displaced Persons"
    },
    {
        "id": "S-041",
        "photo": "Seria_29z_p20_img02.jpeg",
        "title": "Ulotka repatriacyjna - lista stacji PCK (rewers)",
        "date": "1945",
        "desc": "Rewers ulotki: pelna lista stacji zbornych PCK, obozow, przedstawicielstw departamentalnych PCK, konsulatow we Francji. 'Punkt Informacyjno-werbunkowy, Paryz 23 rue Surene...' Informator dla Displaced Persons.",
        "chapter": "Wyzwolenie",
        "person": "Displaced Persons"
    },
    {
        "id": "S-042",
        "photo": "Seria_29z_p21_img01.jpeg",
        "title": "Card of Identity - wyzwolony jeniec, Düsseldorf 1945",
        "date": "27.IV.1945",
        "desc": "CARD OF IDENTITY — dwujezyczny (polsko-angielski). 'P.f.c. Gluchowski Krzysztof — is a polish soldier liberated by Allied forces from german captivity... prisoners of war in Dusseldorf, Germany.' Dusseldorf, 27th of April 1945. KARTA TOZSAMOSCI WYZWOLONEGO JENCA!",
        "chapter": "Wyzwolenie",
        "person": "Krzysztof Andrzej Głuchowski"
    },
    {
        "id": "S-043",
        "photo": "Seria_29z_p22_img01.jpeg",
        "title": "Drobiazgi obozowe - karteczki, wizytowka, talon",
        "date": "1944-1945",
        "desc": "Trzy drobne przedmioty: karteczka z nazwiskiem, wizytowka wloska (France. Creco. Luigi), mala karta z numerem G 1118001/9 i rysunkiem. Drobne dokumenty obozowe.",
        "chapter": "Niewola",
        "person": "Krzysztof Andrzej Głuchowski"
    },
    {
        "id": "S-044",
        "photo": "Seria_29z_p22_img02.jpeg",
        "title": "Spis adresow w Paryzu + wizytowka rzezbiarz",
        "date": "1945",
        "desc": "Trzy dokumenty: kartka z adresami (Ambasada RP Paryz, PCK YMCA 23 rue Taitbout, Polska Misja Wojskowa, Konsulat Generalny), wizytowka 'Henri Kolacz, Artiste-Sculpteur, Troyes', kartka z adresem.",
        "chapter": "Wyzwolenie",
        "person": "Krzysztof Andrzej Głuchowski"
    },
    {
        "id": "S-045",
        "photo": "Seria_29z_p23_img01.jpeg",
        "title": "Carte de Rapatrié - karta repatrianta (awers)",
        "date": "27.VI.1945",
        "desc": "CARTE DE RAPATRIE — Republique Francaise, Ministere des Prisonniers, Deportes et Refugies. Nr 1492839. Pieczec 'CENTRE D'ORSAY, 27 JUIN 1945'. Gluchowski Krzysztof, Pologne. KARTA REPATRIANTA Z CENTRUM ORSAY W PARYZU!",
        "chapter": "Wyzwolenie",
        "person": "Krzysztof Andrzej Głuchowski"
    },
    {
        "id": "S-046",
        "photo": "Seria_29z_p24_img01.jpeg",
        "title": "Zaswiadczenie o konspiracji AK",
        "date": "18.II.1945",
        "desc": "ZASWIADCZENIE: Gluchowski Krzysztof, st. ulan, konspiracji przez okres 3 lat w Warszawie, ps. Jurat/Jezyk. Pieczec Komendy UZUP. Datowane 18.2.1945. Potwierdzenie 3-letniej sluzby konspiracyjnej w AK.",
        "chapter": "AK i Powstanie",
        "person": "Krzysztof Andrzej Głuchowski"
    },
    {
        "id": "S-047",
        "photo": "Seria_29z_p25_img01.jpeg",
        "title": "Fiche de Transport - karta transportowa repatrianta",
        "date": "VI.1945",
        "desc": "FICHE DE TRANSPORT — Republique Francaise, Ministere des Prisonniers. Nr 1492839 (ten sam co Carte de Rapatrie). Gluchowski Krzysztof, Caserne Jessina. Ocena zdrowotna: D, R. Karta umozliwiajaca transport repatrianta.",
        "chapter": "Wyzwolenie",
        "person": "Krzysztof Andrzej Głuchowski"
    },
    {
        "id": "S-048",
        "photo": "Seria_29z_p26_img01.jpeg",
        "title": "List z Francji",
        "date": "3.II.1944",
        "desc": "List odreczny atramentem. Wspomina 'Brasserie Garcia, St. Ouen'. Korespondencja z Francji, prawdopodobnie od znajomego do Krzysztofa.",
        "chapter": "Korespondencja",
        "person": "Krzysztof Andrzej Głuchowski"
    },
    {
        "id": "S-049",
        "photo": "Seria_29z_p27_img01.jpeg",
        "title": "Skierowanie z Ambasady RP w Paryzu na kurs",
        "date": "29.VI.1945",
        "desc": "AMBASSADE de POLOGNE a Paris. 'Pan Gluchowski K. zostanie skierowany przez Roseliny Instruktorowe na kurs, ktory rozpocznie sie w dniu 25 Lipca b.r. w Villard-de-Lans.' Paryz, 29 czerwca 1945. OFICJALNE SKIEROWANIE Z AMBASADY RP.",
        "chapter": "Wyzwolenie",
        "person": "Krzysztof Andrzej Głuchowski"
    },
    {
        "id": "S-050",
        "photo": "Seria_29z_p28_img01.jpeg",
        "title": "Krotka notatka odręczna",
        "date": "1945",
        "desc": "Mala kartka z notatka odręczna: 'Znalazlem plan i drugie...' Krotka notatka personalna.",
        "chapter": "Wyzwolenie",
        "person": "Krzysztof Andrzej Głuchowski"
    },
    {
        "id": "S-051",
        "photo": "Seria_29z_p28_img02.jpeg",
        "title": "Mapka Marsylii - Rue de Rome, Canebière",
        "date": "1945",
        "desc": "Odręczna mapka/szkic: 'Rue de Rome 99', 'Canebiere', 'Hotel Saile'. Plan jak dojsc do hotelu/mieszkania w Marsylii. Canebiere to glowna ulica Marsylii. Slad podrozy repatriacyjnej.",
        "chapter": "Wyzwolenie",
        "person": "Krzysztof Andrzej Głuchowski"
    },
    {
        "id": "S-052",
        "photo": "Seria_29z_p29_img01.jpeg",
        "title": "Skierowanie na RTG - 7 Szpital Wojenny",
        "date": "23.VII.1945",
        "desc": "RENTGEN — skierowanie z 7 Pulku Ulanow Lubelskich im. Gen. Gluchowskiego, I.K.A.H. Pieczec: '7 SZPITAL WOJENNY POLISH GEN. HOSP. 23.7.45'. Skierowanie na badanie RTG.",
        "chapter": "PSZ na Zachodzie",
        "person": "Krzysztof Andrzej Głuchowski"
    },
    {
        "id": "S-053",
        "photo": "Seria_29z_p29_img02.jpeg",
        "title": "Formularz administracyjny 23.I.1945",
        "date": "23.I.1945",
        "desc": "Formularz maszynowy z odręczna notatka, datowany 23.1.45. Dokument administracyjny, wyblakly i trudno czytelny.",
        "chapter": "Niewola",
        "person": "Krzysztof Andrzej Głuchowski"
    },
    {
        "id": "S-054",
        "photo": "Seria_29z_p30_img01.jpeg",
        "title": "Przepustka z II Korpusu - Amandola",
        "date": "1946",
        "desc": "PRZEPUSTKA dwujezyczna (polsko-angielska). Nr ewid. 1946, ulan Gluchowski Krzysztof. Kwateruje w m. Amandola, zezwolenie na przebywanie do godz. 2159. Komendant Gimnazjum i Liceum 3 D.K. (3 Dywizja Karpacka). Podpis: kpt. Kapica Jozef. PRZEPUSTKA Z II KORPUSU WE WLOSZECH!",
        "chapter": "PSZ na Zachodzie",
        "person": "Krzysztof Andrzej Głuchowski"
    },
    {
        "id": "S-055",
        "photo": "Seria_29z_p31_img01.jpeg",
        "title": "Przepustka z Bazy Personalnej 2 Korpusu",
        "date": "11.VI.1946",
        "desc": "Przepustka: Baza Personalna Legio 2 Korpusu. Gluchowski Krzysztof, prawo opuscic teren obozu. Podpis Kuclinski ppor. Kolejna przepustka z II Korpusu Polskiego we Wloszech.",
        "chapter": "PSZ na Zachodzie",
        "person": "Krzysztof Andrzej Głuchowski"
    },
    {
        "id": "S-056",
        "photo": "Seria_29z_p32_img01.jpeg",
        "title": "Zeszyt szkolny - 'Zadańca Wlosooe' nr 1, 23.VIII.1945",
        "date": "23.VIII.1945",
        "desc": "Esej szkolny: 'Zadańca Wlosooe No 1', 23.VIII.1945. Temat: tragiczna historia, deszcz. Wspomina 1.VIII.1944, Powstanie, pluton 1112. WSPOMNIENIE SZKOLNE Z POWSTANIA pisane we Wloszech rok pozniej!",
        "chapter": "Gimnazjum 3DSK",
        "person": "Krzysztof Andrzej Głuchowski"
    },
    {
        "id": "S-057",
        "photo": "Seria_29z_p32_img02.jpeg",
        "title": "Zadanie szkolne nr 3 - Wyspianski, 11 Listopada",
        "date": "21.XI.1945",
        "desc": "Zadanie szkolne 21.XI.1945. Tematy: 'Spoleczenstwo polskie u progu XX stulecia (Wesele Wyspianskiego)', 'Upadek nagrobkosci w swietle hist.', 'Dzien 11 Listopada w Polsce Odrodzonej'. Eseje z Gimnazjum 3 DSK.",
        "chapter": "Gimnazjum 3DSK",
        "person": "Krzysztof Andrzej Głuchowski"
    },
    {
        "id": "S-058",
        "photo": "Seria_29z_p32_img03.jpeg",
        "title": "Okladka EXERCISE BOOK - Gimnazjum 3DSK",
        "date": "1945-1946",
        "desc": "Okladka zeszytu: EXERCISE BOOK, Code No. 28-31. School: Gimnazjum 3DSK. Name: St.uf. Gluchowski Krzysztof. Subject: Zadania klasowe z jezyka polskiego. 'Supplied for use in NAVAL & MILITARY SCHOOLS by His Majesty\\'s Stationery Office.' BRYTYJSKI ZESZYT SZKOLNY POLSKIEGO ZOLNIERZA!",
        "chapter": "Gimnazjum 3DSK",
        "person": "Krzysztof Andrzej Głuchowski"
    },
    {
        "id": "S-059",
        "photo": "Seria_29z_p32_img04.jpeg",
        "title": "Zadanie szkolne nr 8 - problemy spoleczne",
        "date": "IX.1945",
        "desc": "Esej szkolny nr 8, datowany IX.1945. Tematy: problem spoleczny w noweli, upadek moralnosci. Analiza literacka na poziomie maturalnym.",
        "chapter": "Gimnazjum 3DSK",
        "person": "Krzysztof Andrzej Głuchowski"
    },
    {
        "id": "S-060",
        "photo": "Seria_29z_p32_img05.jpeg",
        "title": "EXERCISE BOOK - tylna okladka (tabele brytyjskie)",
        "date": "1945-1946",
        "desc": "Tylna okladka zeszytu: tabele przelicznikow brytyjskich (Metric Measures, Liquid Measure, Weight, Length, Money, Troy Weight). Druk His Majesty\\'s Stationery Office. Ciekawy dokument cywilizacyjny.",
        "chapter": "Gimnazjum 3DSK",
        "person": "Krzysztof Andrzej Głuchowski"
    },
    {
        "id": "S-061",
        "photo": "Seria_29z_p33_img01.jpeg",
        "title": "Esej o rocznicy Powstania - 1.VIII.1945",
        "date": "1.VIII.1945",
        "desc": "Esej datowany dokladnie 1.VIII.1945, godz. 15:00. 'St.ul. Krzysztof Gluchowski, Polish Forces C.M.F. 152, Gimnazjum.' Temat: 'Jaka kolosalna sila moralna...' ESEJ O ROCZNICE POWSTANIA — pisany dokladnie rok po wybuchu, w Gimnazjum 3DSK we Wloszech. Wspomina Bora Komorowskiego.",
        "chapter": "Gimnazjum 3DSK",
        "person": "Krzysztof Andrzej Głuchowski"
    },
    {
        "id": "S-062",
        "photo": "Seria_29z_p34_img01.jpeg",
        "title": "Esej o artykulach wuja Gluchowskiego",
        "date": "3.VIII.1945",
        "desc": "'St.ul. Krzysztof Gluchowski, Polish Forces CMF 152, Gimnazjum 3DSK.' 3.VIII.1945. Esej O ARTYKULACH WUJA — gen. Janusza Gluchowskiego — o Powstaniu. Wspomina 'artykuly P. Gluchowskiego', Armie Krajowa. Autoreferencyjny dokument rodzinny.",
        "chapter": "Gimnazjum 3DSK",
        "person": "Krzysztof Andrzej Głuchowski"
    },
    {
        "id": "S-063",
        "photo": "Seria_29z_p35_img01.jpeg",
        "title": "Dwa zaswiadczenia - KW i awans, Hensstedt 1945",
        "date": "22.VIII.1945",
        "desc": "DWA ZASWIADCZENIA na jednym zdjeciu: (1) Plk. Klopacz Stanislaw zaswiadcza nadanie Krzyza Walecznych Gluchowskiemu Krzysztofowi, plut. 1112, 7 P.Ul. AK nr 29, z 25.9.1944. (2) Zaswiadczenie o awansie do stopnia st. ulana z 15.9.1944. Oba z Hensstedt, 22.8.1945.",
        "chapter": "AK i Powstanie",
        "person": "Krzysztof Andrzej Głuchowski"
    },
    {
        "id": "S-064",
        "photo": "Seria_29z_p36_img01.jpeg",
        "title": "Zaswiadczenie plk. Ziemskiego - Dowodca Grupy Polnoc",
        "date": "26.X.1946",
        "desc": "ZASWIADCZENIE — Plk. dypl. ZIEMSKI KAROL, D-ca Polskiego Okregu Wojskowego Schleswig-Holstein. Jako b. Dowodca Grupy 'POLNOC' w Powstaniu Warszawskim zaswiadcza: GLUCHOWSKI Krzysztof, ur. 1928, ps. 'Juras', walczyl w Obronie Starego Miasta, plut. 1112, awansowany na st. strzelca, odznaczony KRZYZEM WALECZNYCH. Wentorf pod Hamburgiem, 26.10.1946. KLUCZOWY DOKUMENT POTWIERDZAJACY UDZIAL W POWSTANIU.",
        "chapter": "AK i Powstanie",
        "person": "Krzysztof Andrzej Głuchowski"
    },
    {
        "id": "S-065",
        "photo": "Seria_29z_p37_img01.jpeg",
        "title": "Swiadectwo Ukonczenia Gimnazjum - matura 1946",
        "date": "7.I.1946",
        "desc": "SWIADECTWO UKONCZENIA GIMNAZJUM OGOLNOKSZTALCACEGO Nr 13. Ministerstwo Wyznan Religijnych i Oswiecenia Publicznego. Krzysztof Andrzej Gluchowski, ur. 29.XI.1926 w Warszawie. Zlozyl egzamin maturalny 9 Lutego 1946. ZDJECIE LEGITYMACYJNE W MUNDURZE. Delegata V.R. i O.P. Matura polskiego zolnierza we Wloszech!",
        "chapter": "Gimnazjum 3DSK",
        "person": "Krzysztof Andrzej Głuchowski"
    },
]

# ============================================================================
# ROZDZIALY
# ============================================================================
CHAPTERS = [
    "PON i niepodleglosc",
    "Legiony i I wojna",
    "7 Pulk Ulanow",
    "Kariera wojskowa",
    "Odznaczenia",
    "Dokumenty osobiste",
    "Korespondencja",
    "Okupacja",
    "AK i Powstanie",
    "Niewola",
    "Korespondencja obozowa",
    "Pamietnik",
    "Wyzwolenie",
    "PSZ na Zachodzie",
    "Gimnazjum 3DSK",
    "Getto lodzkie",
    "Album",
    "Emigracja",
]

# ============================================================================
# HTML GENERATOR
# ============================================================================
def generate_html():
    cards_by_chapter = {}
    for obj in OBJECTS:
        ch = obj["chapter"]
        if ch not in cards_by_chapter:
            cards_by_chapter[ch] = []
        cards_by_chapter[ch].append(obj)

    total = len(OBJECTS)

    nav_html = ""
    chapters_html = ""
    for ch in CHAPTERS:
        items = cards_by_chapter.get(ch, [])
        if not items:
            continue
        ch_id = ch.replace(" ", "-").replace("/", "-")
        nav_html += f'<a href="#{ch_id}" class="nav-link">{ch} ({len(items)})</a>\n'

        chapters_html += f'<div class="chapter" id="{ch_id}">\n'
        chapters_html += f'<h2 class="chapter-title">{ch}</h2>\n'
        chapters_html += '<div class="cards-grid">\n'
        for obj in items:
            chapters_html += f'''<div class="card" onclick="openLightbox('{IMG_DIR}/{obj["photo"]}', '{obj["title"].replace("'", "&#39;")}')" >
  <div class="card-img-wrap">
    <img src="{IMG_DIR}/{obj["photo"]}" alt="{obj["title"]}" loading="lazy">
  </div>
  <div class="card-body">
    <div class="card-id">{obj["id"]}</div>
    <h3 class="card-title">{obj["title"]}</h3>
    <div class="card-date">{obj["date"]}</div>
    <p class="card-desc">{obj["desc"]}</p>
    <div class="card-person">{obj["person"]}</div>
  </div>
</div>
'''
        chapters_html += '</div></div>\n'

    html = f'''<!DOCTYPE html>
<html lang="pl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Archiwum Rodziny Gluchowskich — Katalog</title>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Source+Sans+3:wght@300;400;600&display=swap" rel="stylesheet">
<style>
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{ background:#0a0a0a; color:#e0d5c1; font-family:'Source Sans 3',sans-serif; }}
.header {{ text-align:center; padding:60px 20px 30px; border-bottom:1px solid #2a2520; }}
.header h1 {{ font-family:'Playfair Display',serif; font-size:2.4em; color:#c9a96e; letter-spacing:2px; }}
.header .subtitle {{ color:#8a7e6b; font-size:1.1em; margin-top:8px; }}
.header .stats {{ color:#6b5f4e; font-size:0.9em; margin-top:12px; }}
.nav {{ position:sticky; top:0; z-index:100; background:#0a0a0aee; backdrop-filter:blur(10px); padding:12px 20px; border-bottom:1px solid #1a1815; display:flex; flex-wrap:wrap; gap:8px; justify-content:center; }}
.nav-link {{ color:#8a7e6b; text-decoration:none; font-size:0.82em; padding:4px 10px; border:1px solid #2a2520; border-radius:3px; transition:all .2s; }}
.nav-link:hover {{ color:#c9a96e; border-color:#c9a96e; }}
.chapter {{ padding:40px 20px; max-width:1400px; margin:0 auto; }}
.chapter-title {{ font-family:'Playfair Display',serif; font-size:1.8em; color:#c9a96e; margin-bottom:24px; padding-bottom:8px; border-bottom:1px solid #2a2520; }}
.cards-grid {{ display:grid; grid-template-columns:repeat(auto-fill, minmax(320px, 1fr)); gap:20px; }}
.card {{ background:#141210; border:1px solid #2a2520; border-radius:6px; overflow:hidden; cursor:pointer; transition:all .3s; }}
.card:hover {{ border-color:#c9a96e; transform:translateY(-2px); box-shadow:0 8px 24px rgba(0,0,0,.4); }}
.card-img-wrap {{ height:240px; overflow:hidden; background:#0d0c0a; display:flex; align-items:center; justify-content:center; }}
.card-img-wrap img {{ max-width:100%; max-height:100%; object-fit:contain; }}
.card-body {{ padding:16px; }}
.card-id {{ font-size:0.75em; color:#6b5f4e; font-family:monospace; margin-bottom:4px; }}
.card-title {{ font-family:'Playfair Display',serif; font-size:1.05em; color:#d4c5a9; margin-bottom:6px; line-height:1.3; }}
.card-date {{ font-size:0.8em; color:#c9a96e; margin-bottom:8px; }}
.card-desc {{ font-size:0.85em; color:#8a7e6b; line-height:1.5; margin-bottom:8px; }}
.card-person {{ font-size:0.75em; color:#5a5040; font-style:italic; }}
.lightbox {{ display:none; position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,.95); z-index:1000; justify-content:center; align-items:center; flex-direction:column; }}
.lightbox.active {{ display:flex; }}
.lightbox img {{ max-width:90vw; max-height:85vh; object-fit:contain; }}
.lightbox .lb-title {{ color:#c9a96e; font-family:'Playfair Display',serif; margin-top:16px; font-size:1.1em; }}
.lightbox .lb-close {{ position:absolute; top:20px; right:30px; color:#8a7e6b; font-size:2em; cursor:pointer; }}
.footer {{ text-align:center; padding:40px; color:#3a3530; font-size:0.8em; border-top:1px solid #1a1815; }}
@media(max-width:700px) {{ .cards-grid {{ grid-template-columns:1fr; }} .header h1 {{ font-size:1.6em; }} }}
</style>
</head>
<body>
<div class="header">
  <h1>ARCHIWUM RODZINY GLUCHOWSKICH</h1>
  <div class="subtitle">Kolekcja dokumentow, korespondencji i fotografii 1862-1964</div>
  <div class="stats">{total} obiektow w {len([ch for ch in CHAPTERS if cards_by_chapter.get(ch)])} rozdzialach &bull; Marian &bull; Janusz &bull; Stanislaw Stefan &bull; Lech &bull; Krzysztof Andrzej</div>
</div>
<nav class="nav">
{nav_html}
</nav>
{chapters_html}
<div class="footer">
  Katalog opracowany na podstawie bezposredniej analizy wizualnej dokumentow.<br>
  Kazde zdjecie = 1 karta katalogowa. Zrodla: 3 katalogi PDF + 14 zdjec WhatsApp.<br>
  &copy; 2026 — Archiwum Rodziny Gluchowskich
</div>
<div class="lightbox" id="lightbox" onclick="closeLightbox()">
  <span class="lb-close">&times;</span>
  <img id="lb-img" src="" alt="">
  <div class="lb-title" id="lb-title"></div>
</div>
<script>
function openLightbox(src, title) {{
  document.getElementById('lb-img').src = src;
  document.getElementById('lb-title').textContent = title;
  document.getElementById('lightbox').classList.add('active');
}}
function closeLightbox() {{
  document.getElementById('lightbox').classList.remove('active');
}}
document.addEventListener('keydown', e => {{ if(e.key==='Escape') closeLightbox(); }});
</script>
</body>
</html>'''
    return html

if __name__ == "__main__":
    html = generate_html()
    out = os.path.join("docs", "katalog_gluchowski_v3.html")
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Wygenerowano: {out}")
    print(f"Obiektow: {len(OBJECTS)}")
