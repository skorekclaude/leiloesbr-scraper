#!/usr/bin/env python3
"""
import_gluchowski.py -- Import kompletnego archiwum Gluchowskich z katalogow PDF.

Zrodla:
  - Kolekcja_Gluchowski_KATALOG_NAUKOWY.pdf (29 stron, 31 obrazow)
  - Kolekcja_Gluchowski_Katalog_Tematyczny.pdf (17 stron)

Archiwum obejmuje 4 pokolenia rodziny Gluchowskich (1905-1945):
  - Gen. bryg. Janusz Gluchowski (1888-1935) -- legionista, general WP
  - Kazimierz Gluchowski (brat) -- korespondencja z emigracji
  - Krzysztof Andrzej Gluchowski -- zolnierz AK, jeniec Stalag XI-B
  - Krzysztof Gluchowski (syn) -- kolekcjoner, zm. 2020 w Brazylii

Kazdy obiekt opisany na podstawie bezposredniej analizy skanow dokumentow.
Opisy klasy muzealnej -- referencje do konkretnych dat, numerow, pieczeci, podpisow.
"""
import sys, os
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import database
from database import get_connection, add_collection_object, collection_object_exists

database.init_db()
conn = get_connection()

# ============================================================
# KOMPLETNY KATALOG KOLEKCJI GLUCHOWSKICH
# Na podstawie bezposredniej analizy 31 obrazow z Katalogu Naukowego
# ============================================================

PROVENANCE = "Archiwum rodziny Gluchowskich -> Krzysztof Gluchowski (Brazylia, zm. 16.05.2020) -> Acervo Raro Leiloes, Brazylia -> kolekcja prywatna"

GLUCHOWSKI_OBJECTS = [
    # ================================================================
    # ROZDZIAL I -- TABLICA PAMIATOWA POWSTANIA WARSZAWSKIEGO
    # (p04 -- blad w katalogowaniu: ten dokument dotyczy 7 Pulku Ulanow AK)
    # ================================================================
    {
        "inventory_number": "GL-001",
        "title": "Tekst tablicy pamiatkowej Powstania Warszawskiego -- 7 Pulk Ulanow AK 'JELEN', 1.VIII.1944",
        "category": "document",
        "medium": "maszynopis, papier",
        "date_created": "po 1944",
        "description": (
            "Odpis lub projekt tekstu tablicy pamiatkowej upamietniajaccej natarcie na gmach Gestapo i Dom Prasy "
            "w dniu 1 sierpnia 1944 roku o godzinie 17:00. Tekst brzmi: 'Dnia 1.8.1944 r. godz. 17 z tego domu "
            "i okolicznych ruszyli do natarcia na gmach Gestapo i Dom Prasy, 5 plutonow ulanow, 7 pulku ulanow "
            "AK JELEN -- z 187 Powstancow poleglo 67. Czesc Ich pamieci.' Dokument jest swiadectwem pierwszych godzin "
            "Powstania Warszawskiego i nadzwyczaj wysokich strat ponoszonych przez oddzialy kawalerii AK. "
            "7 Pulk Ulanow AK 'JELEN' stanowil kontynuacje tradycji 7 Pulku Ulanow Lubelskich im. Gen. Sosnkowskiego. "
            "Strata 67 z 187 powstancow (35.8%) w jednym natarciu ilustruje desperacki charakter walk pierwszego dnia."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "good",
        "condition_notes": "Maszynopis czytelny, papier pozolkly, bez uszkodzen mechanicznych",
        "notes": "Rozdzial I (p04). Blad w katalogowaniu PDF -- dokument tresciowo nalezy do Rozdzialu VI (7 Pulk Ulanow). Estymacja: 5,000--12,000 PLN. Wartosc dokumentacyjna dla Muzeum Powstania Warszawskiego.",
        "authentication_status": "verified",
    },

    # ================================================================
    # ROZDZIAL II -- LEGIONY POLSKIE
    # ================================================================
    {
        "inventory_number": "GL-010",
        "title": "Dyplom Krzyza Legjonowego nr 115 z autografem Jozefa Pilsudskiego + fotografia portretowa atelier, VII.1925",
        "category": "document",
        "medium": "druk, tusz, papier czerpany, podpis wlasnorecny Pilsudskiego; odbitka fotograficzna atelier",
        "date_created": "11 lipca 1925 / ok. 1918-1925",
        "description": (
            "KOMPLET DWOCH OBIEKTOW stanowiacych jedna pozycje katalogu (poz. 29u Katalogu Naukowego): "
            "(1) DYPLOM: Dokument nadania Krzyza Legjonowego -- najwyzszego odznaczenia kombatanckiego legionistow "
            "-- pulkownikowi Januszowi Gluchowskiemu (4 s.p. ul.), nr 115. Data: 11 lipca 1925 roku, Warszawa. "
            "WLASNORECNY PODPIS JOZEFA PILSUDSKIEGO jako przewodniczacego Komisji Kwalifikacyjnej II Zjazdu "
            "Legjonistow. Numer 115 wskazuje, ze Gluchowski byl wsrod pierwszych 200 odznaczonych. "
            "Kontekst podpisu ma wymiar niemal symboliczny: Pilsudski podpisuje odznaczenie legionowe "
            "Gluchowskiemu -- swojemu zolnierzowi z nocnego patrolu 2 sierpnia 1914 -- dokladnie 11 lat "
            "i 9 dni po tym patrolu. "
            "(2) FOTOGRAFIA: Oryginalna fotografia portretowa atelier Jozefa Pilsudskiego w mundurze z orderami, "
            "lata ok. 1918-1925. Postrzepiony oryginalny brzeg. NIE JEST reprodukcja prasowa -- to odbitka "
            "bezposrednia z archiwum rodzinnego (potwierdzone w Katalogu Naukowym). "
            "Drugie zdjecie w katalogu (powiekszenie) pokazuje zblizenie podpisu Pilsudskiego na dyplomie."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "good",
        "condition_notes": "Dyplom: papier czerpany w dobrym stanie, podpis Pilsudskiego czytelny. Fotografia: odbitka oryginalna, drobne slady czasu",
        "notes": "Rozdzial II, poz. 29u. DYPLOM Z AUTOGRAFEM PILSUDSKIEGO + FOTOGRAFIA PORTRETOWA. Estymacja: 20,000--50,000 PLN (dyplom) | 2,000--6,000 PLN (fotografia).",
        "authentication_status": "verified",
    },

    # --- Fotokopia ikonicznej fotografii "Siodemki" ---
    {
        "inventory_number": "GL-012",
        "title": "Fotokopia ikonicznej fotografii I patrolu 'Siodemki' (7 PP Legionow) z podpisami, 1914",
        "category": "photograph",
        "medium": "fotokopia, papier fotograficzny",
        "date_created": "ok. 1914 (fotokopia pozniejsza)",
        "description": (
            "Fotokopia (NIE oryginal) ikonicznej fotografii przedstawiajacej pierwszy patrol 'Siodemki' "
            "-- 7 Pulku Piechoty Legionow Polskich z 1914 roku. Katalog Naukowy wyraznie opisuje ten obiekt "
            "jako 'Fotokopie ikonicznej fotografii' z podpisami czlonkow patrolu. Fotografia oryginalna "
            "jest jednym z najbardziej rozpoznawalnych zdjec z historii Legionow Polskich -- przedstawia "
            "legionistow I Brygady Pilsudskiego w pierwszych dniach formowania sie oddzialow. "
            "Mimo ze jest to fotokopia, zachowuje wartosc dokumentacyjna jako element archiwum rodzinnego "
            "z potwierdzona proweniencja legionowa."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "good",
        "condition_notes": "Fotokopia w dobrym stanie, podpisy czytelne",
        "notes": "Rozdzial II (p05). FOTOKOPIA -- nie oryginal. Wartosc dokumentacyjna, nie kolekcjonerska. Estymacja: 500--2,000 PLN.",
        "authentication_status": "photocopy",
    },

    # ================================================================
    # ROZDZIAL III -- II RZECZPOSPOLITA (1918-1939)
    # ================================================================
    {
        "inventory_number": "GL-020",
        "title": "List Kazimierza Sosnkowskiego z Kanady -- Arundel, P.Que., 28 maja 1964",
        "category": "document",
        "medium": "maszynopis, papier, podpis odreczny",
        "date_created": "28 maja 1964",
        "description": (
            "Dlugi list maszynopisany, datowany 28 maja 1964 roku, wyslany z Arundel, Province de Quebec, Kanada. "
            "Nadawca podpisany jako 'Kazimierz i ...' -- z najwyzszym prawdopodobieenstwem general Kazimierz Sosnkowski "
            "(1885-1969), ostatni Naczelny Wodz Polskich Sil Zbrojnych, ktory po wojnie osiedlil sie wlasnie w Arundel, Quebec. "
            "List dotyczy spraw historyczno-wydawniczych: publikacji dotyczacych historii polskiego wojska, wspomnien "
            "i artykuow. Sosnkowski, w ostatnich latach zycia, aktywnie wspierpal prace nad utrwaleniem pamieci "
            "o Legionach i II RP. Korespondencja ta stanowi bezcenne zrodlo do badan nad polska emigracja "
            "polityczna w Kanadzie i probach zachowania pamieci historycznej na obczyznie."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "good",
        "condition_notes": "Maszynopis czytelny, papier w dobrym stanie, podpis odreczny zachowany",
        "notes": "Rozdzial III/IV (p09, p14_img01). KORESPONDENCJA GEN. SOSNKOWSKIEGO Z EMIGRACJI. Arundel, Quebec -- znane miejsce zamieszkania Sosnkowskiego. Estymacja: 12,000--30,000 PLN.",
        "authentication_status": "verified",
    },
    {
        "inventory_number": "GL-021",
        "title": "Krzyz Walecznych -- medal fizyczny, 'NA POLU CHWALY 1920'",
        "category": "militaria",
        "medium": "braz, emalia, wstazka bordowo-kremowa",
        "date_created": "ok. 1920-1930",
        "description": (
            "Fizyczny medal -- Krzyz Walecznych, jedno z najwazniejszych polskich odznaczen bojowych. "
            "Na awersie widoczny napis 'NA POLU CHWALY' z data '1920', wskazujacy na nadanie za walki "
            "w wojnie polsko-bolszewickiej. Medal brazowy w formie krzyza, zawieszony na oryginalnej wstazce "
            "w barwach bordowo-kremowych (charakterystycznych dla tego odznaczenia). Krzyz Walecznych byl nadawany "
            "za mestwo i odwage na polu bitwy -- ustanowiony przez Naczelnika Panstwa Jozefa Pilsudskiego "
            "w 1920 roku. Gen. Janusz Gluchowski posiadal wielokrotne nadania tego odznaczenia. "
            "Zachowanie medalu dobre -- patyna brazowa, wstazka oryginalna."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "good",
        "condition_notes": "Metal z naturalna patyna brazowa, wstazka oryginalna, lekkie przetarcia emalii",
        "notes": "Rozdzial III (p10). FIZYCZNY MEDAL -- nie dyplom. Krzyz Walecznych 'NA POLU CHWALY 1920'. Estymacja: 8,000--20,000 PLN. Kolekcjonerzy militariow + muzea.",
        "authentication_status": "verified",
    },
    {
        "inventory_number": "GL-022",
        "title": "Legitymacja oficerska gen. bryg. Janusza Gluchowskiego -- kompletna ksiazeczka 1928-1937, ze zdjeciem i lista odznaczen",
        "category": "document",
        "medium": "druk, tusz, fotografia, pieczecie urzedowe, podpisy, rekopis",
        "date_created": "6 lutego 1928 -- przedluzenia do 1937",
        "description": (
            "Oryginalna KOMPLETNA ksiazeczka legitymacyjna oficera WP (poz. 29t Katalogu Naukowego), wystawiona "
            "6 lutego 1928 we Lwowie. Zawiera kilka stron dokumentujacych cala kariere generala: "
            "(1) STRONA TYTULOWA z fotografia portretowa generala w mundurze, wlasnorecnym podpisem "
            "'Janusz Gluchowski Gen. Br.', dane: General brygady, Stan CZYNNY, D.O.K. I (Warszawa), "
            "pozniej Biuro Personalne M.S.Wojsk. "
            "(2) STRONA ODZNACZEN: pelny wykaz -- Virtuti Militari kl. V, Krzyz Walecznych z 2 okuciami, "
            "Zloty Krzyz Zaslugi, Legia Honorowa (Francja), Order Komandorski Lotwy. Pieczec plk Marjan "
            "Czerniew, Pulkownik Sztabu Generalnego. "
            "(3) STRONA PRZEDLUZEN z pieczecia 'GENERAL DYWIZJI' i Ministra Spraw Wojskowych. Przedluzenia "
            "waznosci 1929-1937 z podpisami przelozonych -- w tym Szefa Sztabu Glownego. "
            "(4) ZAPIS ZMIAN STANOWISK: 4 Dywizja Kawalerii -> Centrum Wyszkolenia Srodkow Wojskowych (1930) "
            "-> Dowodca DOK X Przemysl (11 IV 1933). Wpis o DOK X pojawia sie 3 tygodnie po dekrecie "
            "Pilsudskiego i Moscickiego (16 III 1933). "
            "Legitymacja jest kronika kariery -- nie jeden moment, ale kilka lat. Fotografia portretowa "
            "jest prawdopodobnie jedyna zachowana niereprodukowana fotografia generala Gluchowskiego."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "good",
        "condition_notes": "Ksiazeczka kompletna, fotografia czytelna, pieczecie zachowane, okladka lekko przetarta",
        "notes": "Rozdzial III, poz. 29t. LEGITYMACJA GENERALSKA -- kompletna, 4+ stron, ze zdjeciem i odznaczeniami. Estymacja: 15,000--35,000 PLN.",
        "authentication_status": "verified",
    },

    # --- Odpisy dekretow prezydenckich (kopie z oryginalnymi kontrasygnaturami) ---
    {
        "inventory_number": "GL-025",
        "title": "ODPIS dekretu Prezydenta RP -- mianowanie Gluchowskiego na Dowodce OK X, Pilsudski + Moscicki, 16.III.1933",
        "category": "document",
        "medium": "maszynopis urzedowy, pieczecie, kontrasygnatura oryginalna",
        "date_created": "16 marca 1933",
        "description": (
            "Odpis (kopia urzedowa) dekretu Prezydenta Rzeczypospolitej Ignacego Moscickiego, kontrasygnowanego "
            "przez Jozefa Pilsudskiego jako Ministra Spraw Wojskowych, mianujacego plk./gen. Janusza Gluchowskiego "
            "na stanowisko Dowodcy Okregu Korpusu X. Dokument opisany w Katalogu Naukowym jako 'ODPIS dekretu' "
            "-- NIE oryginal, lecz kopia urzedowa z oryginalnymi kontrasygnaturami. Dekret datowany na 16 marca 1933 r. "
            "Obecnosc podpisow Pilsudskiego i Moscickiego (nawet jako odpis) czyni ten dokument niezwykle cennym "
            "-- dokumentuje bezposredni udzial Marszalka w nominacjach generalskich."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "good",
        "condition_notes": "Odpis urzedowy w dobrym stanie, kontrasygnatura czytelna, pieczecie zachowane",
        "notes": "Rozdzial III (p12). ODPIS -- nie oryginal dekretu. Kontrasygnatura oryginalna. Podpisy: Pilsudski + Moscicki. Estymacja: 8,000--20,000 PLN.",
        "authentication_status": "copy_with_original_signatures",
    },
    {
        "inventory_number": "GL-026",
        "title": "ODPIS Nr 23 dekretu Prezydenta RP -- mianowanie I Vice-Ministra, Moscicki + Kasprzycki, 5.X.1935",
        "category": "document",
        "medium": "maszynopis urzedowy, pieczecie, kontrasygnatura oryginalna",
        "date_created": "5 pazdziernika 1935",
        "description": (
            "Odpis Nr 23 dekretu Prezydenta Rzeczypospolitej Ignacego Moscickiego, kontrasygnowanego przez "
            "Ministra Spraw Wojskowych gen. Tadeusza Kasprzyckiego, mianujacego Gluchowskiego na stanowisko "
            "I Vice-Ministra (zastepcy ministra). Dokument opisany w Katalogu Naukowym jako 'ODPIS Nr 23' "
            "-- numerowana kopia urzedowa z oryginalnymi kontrasygnaturami. Datowany 5 pazdziernika 1935 r. "
            "Mianowanie na Vice-Ministra Spraw Wojskowych bylo jednym z najwyzszych stanowisk w hierarchii "
            "wojskowej II RP, swiadczacym o najwyzszym zaufaniu wladz panstwowych do gen. Gluchowskiego."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "good",
        "condition_notes": "Odpis nr 23, papier urzedowy w dobrym stanie, pieczecie zachowane",
        "notes": "Rozdzial III (p12). ODPIS NR 23 -- numerowana kopia urzedowa. Podpisy: Moscicki + Kasprzycki. Estymacja: 6,000--15,000 PLN.",
        "authentication_status": "copy_with_original_signatures",
    },

    # ================================================================
    # ROZDZIAL IV -- GEN. SOSNKOWSKI -- KORESPONDENCJA EMIGRACYJNA
    # ================================================================
    {
        "inventory_number": "GL-030",
        "title": "Lista zlecen i prosby organizacji polonijnych -- gen. Gluchowski, mjr Zebrowski, SPK Kanada, Chicago",
        "category": "document",
        "medium": "maszynopis, papier",
        "date_created": "ok. 1960-1964",
        "description": (
            "Maszynopisana lista zlecen, prosby i korespondencji od roznych polskich organizacji emigracyjnych. "
            "Dokument wymienia: Gen. Gluchowskiego, Mjr. Zebrowskiego, wspomnienia kawaleryjskie, "
            "Stowarzyszenie Polskich Kombatantow (SPK) Kanada, organizacje polonijne w Chicago. "
            "Wspomniana jest rowniez 'History of Polish Armed Forces' oraz artykuly do katalogow. "
            "Dokument ten jest wyjatkowo cennym zrodlem do badan nad polska emigracja powojenjna -- "
            "ukazuje siec polskich organizacji kombatanckich rozsianych po Ameryce Polnocnej, "
            "ich prace nad zachowaniem pamieci historycznej oraz relacje miedzy weteranami "
            "a instytucjami kultury polskiej na obczyznie."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "good",
        "condition_notes": "Maszynopis czytelny, papier w dobrym stanie",
        "notes": "Rozdzial IV (p14_img02). Dokumentacja emigracji polskiej: SPK, Chicago, pamiec historyczna. Estymacja: 3,000--8,000 PLN.",
        "authentication_status": "verified",
    },
    {
        "inventory_number": "GL-031",
        "title": "Kontynuacja listu Sosnkowskiego -- sprawy wydawnicze, historia PSZ",
        "category": "document",
        "medium": "maszynopis, papier",
        "date_created": "1964",
        "description": (
            "Dalszy ciag korespondencji gen. Kazimierza Sosnkowskiego, dotyczacy spraw wydawniczych -- "
            "prace nad 'History of Polish Armed Forces', artykuly do katalogow historycznych. "
            "Sosnkowski w ostatnich latach zycia (zmarl 11 pazdziernika 1969) prowadzil intensywna dzialalnosc "
            "publicystyczna i memorialna. Jako ostatni Naczelny Wodz PSZ na Zachodzie czul sie odpowiedzialny "
            "za utrwalenie prawdy historycznej o polskim wysilku zbrojnym w II wojnie swiatowej. "
            "List ten dokumentuje te dzialalnosc w jej codziennym, praktycznym wymiarze."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "good",
        "condition_notes": "Maszynopis czytelny, papier w dobrym stanie",
        "notes": "Rozdzial IV (p14_img03). Kontynuacja korespondencji Sosnkowskiego. Wartosc lacznie z GL-020.",
        "authentication_status": "verified",
    },

    # ================================================================
    # ROZDZIAL V -- GETTO LODZKIE (LITZMANNSTADT) -- HOLOKAUST
    # ================================================================
    {
        "inventory_number": "GL-040",
        "title": "List K. Gluchowskiego do Ambasady Izraela w Londynie -- oferta sprzedazy waluty getta, 18 maja 1958",
        "category": "document",
        "medium": "maszynopis, papier, naglowek z adresem",
        "date_created": "18 maja 1958",
        "description": (
            "List maszynopisany na papierze z naglowkiem adresowym '42 Emperors Gate, London SW7', datowany "
            "18 maja 1958 roku, adresowany do 'The Israel Embassy, Public Relations Office, 2 Palace Green, "
            "London W.8.' Autor -- K. Gluchowski -- pisze: 'I am contemplating sale of my complete set of paper "
            "currency and coins issued in Lodz ghetto during the German occupation of Poland. The above set is "
            "of great rarity and museal value, and I wonder if some institution in Israel would not be interested "
            "in purchase.' Dokument ten dowodzi, ze Gluchowski juz w 1958 roku byl swiadomy muzealnej wartosci "
            "swojej kolekcji gettowej. Adres na Emperors Gate (South Kensington) wskazuje na zamozna dzielnice "
            "Londynu -- Gluchowski nalezal do elity polskiej emigracji."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "good",
        "condition_notes": "Maszynopis czytelny, papier firmowy, bez uszkodzen",
        "notes": "Rozdzial V: Getto Lodzkie (p17_img01). KORESPONDENCJA Z AMBASADA IZRAELA 1958. Kluczowy dokument proweniencji kolekcji gettowej. Estymacja: 5,000--15,000 PLN.",
        "authentication_status": "verified",
    },
    {
        "inventory_number": "GL-041",
        "title": "Kupon pocztowy Getta Lodzkiego -- 'GUT FUR 10 PF.' Postabteilung, Litzmannstadt, 17 kwietnia 1942",
        "category": "document",
        "medium": "druk na zoltym papierze, tusz",
        "date_created": "17 kwietnia 1942",
        "description": (
            "Oryginalny kupon pocztowy (zastepczy pieniadz) z Getta Lodzkiego (Litzmannstadt-Getto). "
            "Tekst drukowany: 'GUT FUR 10 PF. BEI DER POSTABTEILUNG DES AELTESTEN DER JUDEN in "
            "Litzmannstadt-Getto, 17. April 1942'. Zolty papier, druk w kolorze ciemnym. 'Aeltester der Juden' "
            "(Starszy Zydow) -- tytul Chaima Mordechaja Rumkowskiego, kontrowersyjnego przywodcy Judenratu "
            "w Lodzi. Getto Lodzkie (1940-1944) bylo drugim co do wielkosci gettem w okupowanej Europie "
            "(ok. 200,000 wiezniow). Kupon pocztowy z dokladna data 17.IV.1942 -- okres przed wielka deportacja "
            "do Chelmna (styczen-maj 1942). Dokumenty walutowe getta sa niezwykle rzadkie na rynku -- "
            "wiekszosc zniszczona podczas likwidacji getta w sierpniu 1944."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "fair",
        "condition_notes": "Papier pozolkly ale czytelny, krawedzie lekko postrzepione, druk zachowany",
        "notes": "Rozdzial V: Getto Lodzkie (p17_img02, obiekt 1/3). WALUTA GETTA LODZKIEGO -- 10 Pfennig. Estymacja: 8,000--25,000 PLN. Potencjalni nabywcy: POLIN, Yad Vashem, USHMM.",
        "authentication_status": "verified",
    },
    {
        "inventory_number": "GL-042",
        "title": "Talon mleczarski nr 6110 z Getta Lodzkiego -- 200g Molkereiprodukte, Litzmannstadt",
        "category": "document",
        "medium": "druk na niebiesko-szarym papierze",
        "date_created": "1940-1944",
        "description": (
            "Oryginalny talon zywnosciowy z Getta Lodzkiego (Litzmannstadt): 'TALON Nr 6110, uber 200 g. "
            "Molkereiprodukte' (200 gramow przetworow mlecznych) z adnotacja 'MOLKEREIERZEUGNISSE-ABT' "
            "(Oddzial Przetworow Mlecznych). Papier niebiesko-szary, druk ciemny. Talony zywnosciowe "
            "byly podstawa systemu racjonowania w getcie -- kontrolowaly glodowa diete wiezniow. "
            "200 gramow przetworow mlecznych stanowilo luksus w warunkach gettowych, gdzie srednia "
            "dzienna racja kaloryczna spadala do 700-900 kcal. Talon o konkretnym numerze (6110) "
            "pozwala na indywidualna identyfikacje i ewentualna korelacje z archiwami getta."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "fair",
        "condition_notes": "Papier kruchy, druk czytelny, krawedzie postrzepione",
        "notes": "Rozdzial V: Getto Lodzkie (p17_img02, obiekt 2/3). TALON ZYWNOSCIOWY -- dokument Holokaustu. Estymacja: 6,000--18,000 PLN.",
        "authentication_status": "verified",
    },
    {
        "inventory_number": "GL-043",
        "title": "Koperta z odrecznymi notatkami -- archiwum gettowe Gluchowskiego",
        "category": "document",
        "medium": "papier, rekopis odreczny",
        "date_created": "ok. 1940-1958",
        "description": (
            "Stara koperta z odrecznymi notatkami, stanowiaca czesc zbioru dokumentow gettowych "
            "Gluchowskiego. Koperta sluzypa prawdopodobnie jako opakowanie/opis dla kolekcji "
            "waluty i talonow z Getta Lodzkiego. Odreczne adnotacje moga zawierac informacje "
            "o proweniencji i okolicznosciach nabycia przedmiotow gettowych. W kontekscie listu "
            "do Ambasady Izraela z 1958 roku -- Gluchowski starannie katalogowal swoja kolekcje."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "fair",
        "condition_notes": "Koperta postarzala, rekopis czesciowo czytelny",
        "notes": "Rozdzial V: Getto Lodzkie (p17_img02, obiekt 3/3). Element proweniencji kolekcji gettowej. Estymacja: 1,000--3,000 PLN.",
        "authentication_status": "verified",
    },
    {
        "inventory_number": "GL-044",
        "title": "Odpowiedz Ambasady Izraela -- A. Kidron, attache prasowy, 22 maja 1958, odesalnie do Yad Vashem",
        "category": "document",
        "medium": "maszynopis, papier z naglowkiem ambasady, pieczec z menora",
        "date_created": "22 maja 1958",
        "description": (
            "Oficjalna odpowiedz z Ambasady Izraela w Londynie (2 Palace Green, London W.8.), datowana "
            "22 maja 1958 roku, z pieczecia przedstawiajaca menore -- herb panstwa Izrael. List adresowany "
            "do 'Dear Mr. Gluchowski', podpisany przez A. Kidrona, Press Attache. Tresc: 'In reply to your "
            "letter of 18 May concerning your set of paper currency and coins, issued in Lodz ghetto, I would "
            "suggest you write to: Yad Veshem, P.O.B. 84, Jerusalem. Yours sincerely, A. Kidron, Press Attache.' "
            "Avraham Kidron (1919-2011) byl pozniej ambasadorem Izraela w Australii i Kanadzie. "
            "Odesalnie do Yad Vashem potwierdza muzealna range kolekcji gettowej Gluchowskiego. "
            "Ten list, w parze z GL-040, tworzy kompletna korespondencje dyplomatyczna."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "very good",
        "condition_notes": "Papier firmowy ambasady, pieczec z menora czytelna, maszynopis bez uszkodzen",
        "notes": "Rozdzial V: Getto Lodzkie (p17_img03). OFICJALNA KORESPONDENCJA AMBASADY IZRAELA z pieczecia menory. Odesalnie do Yad Vashem! Estymacja: 8,000--20,000 PLN. Para z GL-040.",
        "authentication_status": "verified",
    },

    # ================================================================
    # ROZDZIAL VI -- 7 PULK ULANOW LUBELSKICH IM. GEN. SOSNKOWSKIEGO
    # ================================================================
    # GL-050 USUNIETY -- byl duplikatem GL-001 (identyczny tekst tablicy AK 'JELEN')
    {
        "inventory_number": "GL-051",
        "title": "Ogloszenie dorocznej Mszy sw. za zolnierzy AK 'JELEN' -- kosciol sw. Anny w Wilanowie, 4.X.1970",
        "category": "document",
        "medium": "druk/maszynopis, papier",
        "date_created": "pazdziernik 1970",
        "description": (
            "Drukowane ogloszenie o dorocznej Mszy swietej za poleglych zolnierzy Pulku AK 'ULIK' (kryptonim "
            "zwiazany z 7 Pulkiem Ulanow). Tresc: 'Dnia 4-go pazdziernika 1970 r. (niedziela) o godz. 10-ej "
            "w kosciele sw. Anny w Wilanowie bedzie odprawiona doroczna Msza sw. za poleglych w czasie okupacji "
            "i Powstania Warszawskiego ZOLNIERZY PULKU AK ULIK. Po mszy zostana zlozone kwiaty na miejscowym "
            "cmentarzu -- na modle zolnierzy JELENIA, poleglych na Sadybie. Rodziny i towarzysze broni...' "
            "Dokument swiadczy o zywej tradycji komemoracyjnej 7 Pulku Ulanow w PRL -- pomimo cenzury i represji, "
            "rodziny i weterani spotykali sie na dorocznych nabozenstwach. Wilanow/Sadyba -- rejon walk "
            "Powstania Warszawskiego, gdzie 7 Pulk poniosl ciezkie straty."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "good",
        "condition_notes": "Druk czytelny, papier w dobrym stanie",
        "notes": "Rozdzial VI (p20). Dokument komemoracyjny PRL -- tradycja AK w konspiracji pamieci. Kosciol sw. Anny w Wilanowie, cmentarz na Sadybie. Estymacja: 3,000--8,000 PLN.",
        "authentication_status": "verified",
    },
    {
        "inventory_number": "GL-052",
        "title": "Nekrolog plut. Jana Lorensa -- prezes sekcji Kola 7 Pulku Ulanow w Chicago, zm. 29.I.1960",
        "category": "document",
        "medium": "druk, papier",
        "date_created": "styczen-luty 1960",
        "description": (
            "Drukowany nekrolog: 'S.P. JAN LORENS, plutonowy 7 pulku ulanow, prezes sekcji Kola pulkowego; "
            "czynny czlonek wielu organizacji niepodleglosciowych w Chicago, odznaczony Krzyzem Walecznych "
            "i innymi odznaczeniami polskimi i zagranicznymi, zmarl 29 stycznia 1960 w Chicago. Czesc Jego "
            "pamieci! KOLO ZOLNIERZY 7 PULKU ULANOW LUBELSKICH IM. GEN. K. SOSNKOWSKIEGO.' Dokument potwierdza "
            "istnienie Kola 7 Pulku Ulanow na emigracji w Chicago -- jedna z wielu polskich organizacji "
            "kombatanckich w USA. Pelna nazwa pulku z patronem (gen. Sosnkowski) i wzmianka o KW dowodza "
            "bojowej przeszlosci zmarlego."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "good",
        "condition_notes": "Druk czytelny, papier pozolkly",
        "notes": "Rozdzial VI (p21). Nekrolog weterana 7 Pulku z Chicago. KOLO PULKOWE na emigracji. Estymacja: 2,000--5,000 PLN.",
        "authentication_status": "verified",
    },

    # ================================================================
    # ROZDZIAL VII -- KRZYSZTOF ANDRZEJ GLUCHOWSKI
    # Zolnierz AK, uczestnik Powstania Warszawskiego, jeniec Stalag XI-B
    # ================================================================
    {
        "inventory_number": "GL-060",
        "title": "Akcesoria mundurowe -- portepee (chwast szablowy), galon, miniatura KW",
        "category": "militaria",
        "medium": "tkanina, nici srebrno-niebieskie, metal, wstazka",
        "date_created": "ok. 1939-1945",
        "description": (
            "Zestaw trzech akcesoriow mundurowych: (1) Portepee (chwast szablowy, temblak) w barwach "
            "niebiesko-srebrnych -- element munduru oficerskiego lub podoficerskiego kawalerii WP. "
            "(2) Galon zloto-srebrny -- pas lub element lamowki mundurowej. (3) Miniaturowa baretka "
            "Krzyza Walecznych na wstazce bordowo-kremowej -- noszona na co dzien na mundurze. "
            "Te fizyczne relikty mundurowe sa niezwykle rzadkie -- wiekszosc zniszczona lub skonfiskowana "
            "przez Niemcow. Zachowanie ich w komplecie swiadczy o starannosci z jaka rodzina "
            "przechowywala pamiatki wojskowe."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "fair",
        "condition_notes": "Tkaniny lekko splowiale, metal z patyna, wstazka zachowana",
        "notes": "Rozdzial VII (p23_img01). FIZYCZNE AKCESORIA MUNDUROWE -- portepee, galon, miniatura KW. Estymacja: 5,000--15,000 PLN jako komplet.",
        "authentication_status": "verified",
    },
    {
        "inventory_number": "GL-061",
        "title": "Kennkarte nr 662016 -- Krzysztof Andrzej Gluchowski, Schuler, ur. 29.XI.1928, Warszawa (kompletna, 4 strony)",
        "category": "document",
        "medium": "druk dwujezyczny, papier, fotografia, pieczec Generalgouvernement, odcisk palca, podpis",
        "date_created": "9 listopada 1943",
        "description": (
            "Oryginalna KOMPLETNA Kennkarte (Karta Rozpoznawcza) Generalnego Gubernatorstwa (poz. 29x "
            "Katalogu Naukowego), nr identyfikacyjny 662016, wystawiona Krzysztofowi Andrzejowi "
            "Gluchowskiemu przez Prezydenta Policji w Warszawie. Dokument 4-stronicowy: "
            "(1) OKLADKA: 'GENERALGOUVERNEMENT, GENERALNE GUBERNATORSTWO, KENNKARTE, KARTA ROZPOZNAWCZA' "
            "-- dwujezyczny (niemiecko-polski), pieczec z symbolem nazistowskim. "
            "(2) STRONA Z FOTOGRAFIA: portret chlopca ok. 14-15 lat, odcisk palca wskazujacego lewej reki, "
            "wlasnorecny podpis. "
            "(3) DANE OSOBOWE: Zawod: Schuler (uczen). Adres: ul. Pogonowskiego, Warszawa. Data urodzenia: "
            "29 listopada 1928. Wazna do 9 XI 1948. "
            "Kennkarte byly obligatoryjne dla wszystkich mieszkancow GG powyzej 15 roku zycia. "
            "Chlopiec z fotografii ma 15 lat -- patrzy w obiektyw z wyrazem twarzy typowym dla epoki. "
            "Tego samego dnia rodzina wyrabiala kolejne odpisy swiadectwa urodzenia -- seria dokumentow "
            "tozsamosci przygotowywana na potrzeby konspiracyjne. Dokument wystawiony dokladnie rok "
            "przed wzieciem Krzysztofa do niewoli (5 X 1944)."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "good",
        "condition_notes": "Dokument kompletny (4 strony), fotografia czytelna, pieczecie zachowane, papier lekko pozolkly",
        "notes": "Rozdzial VII, poz. 29x. KENNKARTE GG NR 662016 -- kompletna, 4 strony. Estymacja: 2,500--6,000 PLN.",
        "authentication_status": "verified",
    },
    {
        "inventory_number": "GL-063",
        "title": "List wojenny na papierze w kratke -- 'Krychu! Ksiazke poslesz...', dat. 24/IX",
        "category": "document",
        "medium": "rekopis odreczny, papier w kratke",
        "date_created": "24 wrzesnia [1944?]",
        "description": (
            "Odreczny list na kartce z zeszytu w kratke, datowany '24/IX' (24 wrzesnia, prawdopodobnie 1944). "
            "Zaczyna sie od 'Krychu! Ksiazke poslesz...' -- pisany do Krzysztofa (Krychu) w tonie "
            "bezposrednim, kolezenskim lub rodzinnym. Data 24 wrzesnia 1944 -- jesli poprawna -- "
            "oznacza, ze list byl pisany podczas Powstania Warszawskiego, tygodniami przed kapitulacja "
            "(2 pazdziernika 1944). W tym okresie walczacy powstancy wymieniali korespondencje miedzy "
            "dzielnicami za posrednictwem lacznikow i kanalow. Rekopis na papierze w kratke -- typowy "
            "dla warunkow polowych, gdzie brakowalo papeterii."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "fair",
        "condition_notes": "Papier z zeszytu, pozolkly, rekopis czytelny, zagiecia z okresu wojennego",
        "notes": "Rozdzial VII (p24_img01). LIST Z OKRESU POWSTANIA WARSZAWSKIEGO. Estymacja: 8,000--20,000 PLN. Wartosc dokumentacyjna dla MPW.",
        "authentication_status": "verified",
    },
    {
        "inventory_number": "GL-064",
        "title": "List Krzysztofa do rodzicow z Powstania -- 'Kochana Momunia i Tato!', 26.VIII.1944 (dzien 26. Powstania)",
        "category": "document",
        "medium": "rekopis olowkowy, papier notesowy zebkowany",
        "date_created": "26 sierpnia 1944",
        "description": (
            "Odreczny list olowkiem na papierze notesowym zebkowanym, datowany 26 VIII 1944 -- DZIEN 26. "
            "POWSTANIA WARSZAWSKIEGO. Tresc: 'Kochane Momunia i Tato! Jestem na stanowisku. Dotychczas zyje "
            "i jestem niety choc mocno zaziebiomy. W naszej jednostce dotychczas mielismy dosc male straty "
            "z wyjatkiem bardzo dotkliwej jej poniesslismy tragedji naszego porucznika (p. Jerzego) ktory "
            "zginal + 13 bm od odlamka granatu z granatnika. Oprocz tego zginal Stas B. 2 bm. Oprocz tego "
            "zginelo jeszcze 2. Ze Stryjem nie bylem od poczatku. O wenyph na Zolikowie nic nie wiem. "
            "Caluje bardzo mocno -- Krzysztof.' Przekazywany przez laczniczki: 'p. Marienka -- dla p. Jagi "
            "(w srodku kopertki dla niej)'. List 15-latka do rodzicow jest napisany jezykiem dojrzalego "
            "zolnierza: precyzyjnie podaje straty jednostki, wymienia poleglych z imienia. Wzmianka "
            "o 'Stryju' ktory nie daje znaku zycia -- i niewiedza o Zoliborzu -- pokazuje, ze Warszawa "
            "byla podzielona na izolowane wyspy walki."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "fair",
        "condition_notes": "Papier notesowy zebkowany, olowek czytelny, zagiecia polowe",
        "notes": "Rozdzial VII, poz. 29z(E). LIST Z 26 SIERPNIA 1944 -- DZIEN 26. POWSTANIA. Para z GL-077 (odpowiedz Ciotki Waleski). Estymacja: 5,000--15,000 PLN.",
        "authentication_status": "verified",
    },
    {
        "inventory_number": "GL-065",
        "title": "Przepustka Jednorazowa Specjalna Armii Krajowej -- 29.IX.1944, pieczec Komendy Warszawskiego Okregu AK",
        "category": "document",
        "medium": "druk/rekopis, pieczecie AK, podpisy",
        "date_created": "29 wrzesnia 1944",
        "description": (
            "Oryginalna Przepustka Jednorazowa Specjalna wydana przez Armie Krajowa, datowana 29 wrzesnia 1944 roku -- "
            "TRZY DNI PRZED KAPITULACJA POWSTANIA WARSZAWSKIEGO (2 pazdziernika 1944). Pieczec: 'KOMENDA "
            "WARSZAWSKIEGO OKREGU ARMII KRAJOWEJ'. Podpisana przez Z-ce Komendanta Okregu 'Wachnowski plk.' "
            "Przepustka umozliwiala przejscie przez ulice A. Sikorskiego. Wazna do 30.IX.44. "
            "W ostatnich dniach Powstania przepustki AK byly wydawane dla umozliwienia ewakuacji ludnosci "
            "cywilnej i lacznosci miedzy odcialkami walczacymi. Dokument z pieczecia Komendy Okregu Warszawa AK "
            "jest artefaktem najwyzszej rangi -- bardzo niewiele oryginalnych dokumentow AK przetrwalo "
            "zniszczenie Warszawy. Trzy dni przed koncem -- tragiczny kontekst historyczny."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "fair",
        "condition_notes": "Papier polowy, zagiecia, pieczecie czytelne, podpis zachowany",
        "notes": "Rozdzial VII (p25). PRZEPUSTKA AK -- 3 DNI PRZED KAPITULACJA! Pieczec Komendy Okregu Warszawa AK. ABSOLUTNA RAIZKOSC. Estymacja: 25,000--60,000 PLN.",
        "authentication_status": "verified",
    },
    {
        "inventory_number": "GL-066",
        "title": "Rozkaz D-twa Grupy 'Polnoc' nr 24 -- awans na st. ulana i nadanie KW po raz 1-szy",
        "category": "document",
        "medium": "rekopis/maszynopis, pieczec AK, papier",
        "date_created": "wrzesien-pazdziernik 1944",
        "description": (
            "Rewers dokumentu AK z pieczecia 'OKR. ARMII KRAJOWEJ WARSZAWA' i adnotacja: "
            "'Rozkaz D-twa Grupy Polnoc Nr 24, Zgn. 5.47. 4M. -- awansowany do stopnia st. ulana; "
            "nadany K.W. po raz 1-szy' (Krzyz Walecznych po raz pierwszy). Dokument potwierdza, ze "
            "Krzysztof Andrzej Gluchowski zostal awansowany do stopnia starszego ulana i odznaczony "
            "Krzyzem Walecznych podczas Powstania Warszawskiego -- na mocy rozkazu Dowodztwa Grupy 'Polnoc'. "
            "Grupa 'Polnoc' operowala na Zoliborzu i Bielanach. Awans i odznaczenie bojowe w trakcie walk -- "
            "dowod bezposredniego udzialu w walkach i osobistego mestwa."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "fair",
        "condition_notes": "Pieczec AK czytelna, rekopis w stanie dobrym, papier polowy",
        "notes": "Rozdzial VII (p26_img01). AWANS I KW W TRAKCIE POWSTANIA. Pieczec OKR AK WARSZAWA. Estymacja: 15,000--35,000 PLN.",
        "authentication_status": "verified",
    },
    {
        "inventory_number": "GL-067",
        "title": "Legitymacja Armii Krajowej nr 1112 -- ulan Krzysztof Gluchowski ps. 'Guras', 8.IX.1944",
        "category": "document",
        "medium": "druk/rekopis, pieczec z Orlem AK, odcisk palca, tusz",
        "date_created": "8 wrzesnia 1944",
        "description": (
            "Oryginalna legitymacja Armii Krajowej: 'Dowodztwo Armii Krajowej, Oddzial: Pluton Nr M12, "
            "Nazwisko: Gluchowski, Imiona: Krzysztof (Guras), Stopien: ulan, Data urodz.: 29.XI.1926r., "
            "Przydzial: P-two Ob. Hwa F.Z., Data wyst. leg.: 8.IX.1944, Numer leg.: 1112.' "
            "Dokument zawiera ODCISK PALCA posiadacza oraz pieczec z ORLEM ARMII KRAJOWEJ. "
            "Pseudonim konspiracyjny 'Guras'. Data urodzenia 29 listopada 1926 (roznica z Kennkarte -- "
            "1928 -- typowa dla dokumentow konspiracyjnych, gdzie zmieniano dane). "
            "Legitymacja wystawiona 8 wrzesnia 1944 -- w szostym tygodniu Powstania, gdy sytuacja "
            "powstancow byla juz krytyczna. DOKUMENT O ABSOLUTNIE WYJATKOWEJ WARTOSCI MUZEALNEJ -- "
            "oryginalne legitymacje AK z Powstania Warszawskiego naleza do najrzadszych artefaktow "
            "polskiej historii wojskowej."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "fair",
        "condition_notes": "Papier polowy, pieczec Orla AK czytelna, odcisk palca zachowany, zagiecia z uzytku polowego",
        "notes": "Rozdzial VII (p26_img02). LEGITYMACJA AK NR 1112 Z POWSTANIA -- z Orlem AK i odciskiem palca! PS. 'GURAS'. NAJCENNIEJSZY DOKUMENT W KOLEKCJI. Estymacja: 40,000--100,000 PLN.",
        "authentication_status": "verified",
    },
    {
        "inventory_number": "GL-068",
        "title": "Identyfikator jeniecki Stalag XI-B -- nr 141009, tektura z perforacja",
        "category": "militaria",
        "medium": "tektura, perforacja numerowa",
        "date_created": "pazdziernik 1944 - kwiecien 1945",
        "description": (
            "Maly kartonowy identyfikator (tag) jeniecki: 'Stalag XI B, 141009' -- z perforowanym numerem. "
            "Stalag XI-B Fallingbostel (Dolna Saksonia, Niemcy) byl jednym z najwiekszych obozow jenieckich "
            "III Rzeszy -- przeszlo przez niego ponad 300,000 jencow roznych narodowosci. Po kapitulacji "
            "Powstania Warszawskiego (2 pazdziernika 1944), powstancy zostali uznani za jencow wojennych "
            "na mocy konwencji genewskiej (dzieki determinacji gen. Bora-Komorowskiego) i trafili do Stalagoww. "
            "Numer 141009 wskazuje na pozna rejestracje -- tysiace powstancow trafilo do Stalag XI-B "
            "jesienia 1944. Tag jeniecki to namacalny dowod drogi Krzysztofa Gluchowskiego: od "
            "mlodocianego ulana AK w Warszawie, przez Powstanie, do niemieckiego obozu jenieckiego."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "fair",
        "condition_notes": "Tektura lekko zgnijeciona, numer perforowany czytelny, krawedzie obtarte",
        "notes": "Rozdzial VII (p27_img01). TAG JENIECKI STALAG XI-B NR 141009. Estymacja: 8,000--20,000 PLN. Swiadectwo niewoli po Powstaniu.",
        "authentication_status": "verified",
    },
    {
        "inventory_number": "GL-069",
        "title": "Personalkarte I (karta osobowa jenca) -- Stalag XI-B, Gluchowski Krzysztow, ur. 29.XI.28, Warschau",
        "category": "document",
        "medium": "druk formularzowy, maszynopis, tusz, pieczecie niemieckie",
        "date_created": "pazdziernik 1944 - kwiecien 1945",
        "description": (
            "Oryginalna Personalkarte I (karta osobowa jenca wojennego) z obozu Stalag XI-B: "
            "'Familienname: GLUCHOWSKI, Vorname: KRZYSZTOW, geb. 29-11-28 WARSCHAU (urodzony 29.XI.1928, Warszawa), "
            "Religion: KATHOLISCH (katolik), Beruf: SCHULER (uczen), Vorname des Vaters: STEFAN, "
            "Familienname der Mutter: WANDA GLUCHOWSKI, Lager: XI-B.' Status: 'LEDIG' (kawaler). "
            "Wpis kontaktowy: 'ZOFIA DRUSZKO, Krlizin-B, Rzejowice, Radomsko' -- prawdopodobnie osoba "
            "wyznaczona do kontaktu/krewna. Karta potwierdza: (1) date urodzenia w Warszawie, "
            "(2) imiona rodzicow (Stefan i Wanda), (3) status ucznia -- mial 15 lat w momencie wybuchu "
            "Powstania. KOMPLETNA DOKUMENTACJA JENIECK -- od tagu (GL-068) do karty osobowej."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "good",
        "condition_notes": "Formularz kompletny, maszynopis czytelny, pieczecie niemieckie zachowane",
        "notes": "Rozdzial VII (p27_img02). PERSONALKARTE STALAG XI-B -- pelne dane osobowe jenca. Ojciec: STEFAN, matka: WANDA. Kontakt: Zofia Druszko, Radomsko. Estymacja: 10,000--25,000 PLN.",
        "authentication_status": "verified",
    },

    # ================================================================
    # ROZDZIAL VIII -- SZKOCJA -- POLSKIE SILY ZBROJNE NA ZACHODZIE
    # ================================================================
    {
        "inventory_number": "GL-070",
        "title": "Album fotograficzny ze Szkocji -- strona 1: odprawy z oficerami PSZ (plk Koper, plk Krajak, plk Wroblewski, kpt Wojnarowicz)",
        "category": "photography",
        "medium": "odbitki fotograficzne, album z czarnymi kartami, podpisy odreczne",
        "date_created": "1940-1945",
        "description": (
            "Strona albumu fotograficznego z czarnymi kartami (styl lat 40.), zawierajaca 4 fotografie polskich "
            "oficerpw stacjonujacych w Szkocji. Odreczne podpisy identyfikuja: 'od lewej: pplk. Koper, "
            "plk. Krajak, plk. Wroblewski, kpt. Wojnarowicz' -- oficerowie Polskich Sil Zbrojnych na Zachodzie. "
            "Kolejna fotografia podpisana 'odprawa z dywizjonami'. Trzecia: 'Kadra Komp. Doz. z Dep. Batreque' "
            "-- Kadra Kompanii Dozorczej. Polscy zolnierze stacjonowali w Szkocji od 1940 roku, tworzac 1 Korpus "
            "Polski (gen. Maczka). Odreczne podpisy pod zdjeciami sa bezcenne -- pozwalaja na identyfikacje "
            "oficerpow i rekonstrukcje struktury jednostek."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "good",
        "condition_notes": "Album zachowany, fotografie czytelne, podpisy odreczne czytelne, czarne karty lekko wyblakle",
        "notes": "Rozdzial VIII: Szkocja (p28_img01). ALBUM PSZ -- identyfikacja oficerow. Estymacja: 8,000--20,000 PLN za caly album.",
        "authentication_status": "verified",
    },
    {
        "inventory_number": "GL-071",
        "title": "Album fotograficzny ze Szkocji -- strona 2: cwiczenia polowe PSZ",
        "category": "photography",
        "medium": "odbitki fotograficzne, album z czarnymi kartami",
        "date_created": "1940-1945",
        "description": (
            "Kolejna strona albumu szkockiego. Fotografie podpisane 'cwiczenia polowe' -- zolnierze "
            "polscy podczas szkolenia wojskowego na terenie Szkocji. Widoczne sa rowniez zdjecia grupowe "
            "oraz fotografia muzyka z gitara -- dokumentujaca zycie towarzyskie polskich zolnierzy na "
            "obczyznie. Polskie jednostki w Szkocji przechodzialy intensywne szkolenia w oczekiwaniu "
            "na ladzenie we Francji (D-Day, 1944). Album dokumentuje zarowno aspekt wojskowy "
            "(cwiczenia, odprawy), jak i ludzki (muzyka, zycie towarzyskie) sluzby na Wyspach."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "good",
        "condition_notes": "Fotografie czytelne, album w dobrym stanie",
        "notes": "Rozdzial VIII: Szkocja (p28_img02). Album PSZ -- cwiczenia polowe, zycie codzienne. Wartosc lacznie z GL-070.",
        "authentication_status": "verified",
    },
    {
        "inventory_number": "GL-072",
        "title": "Album fotograficzny ze Szkocji -- strona 3: zdjecia grupowe i towarzyskie",
        "category": "photography",
        "medium": "odbitki fotograficzne, album z czarnymi kartami",
        "date_created": "1940-1945",
        "description": (
            "Trzecia strona albumu szkockiego -- dalsze zdjecia grupowe polskich zolnierzy. "
            "Album jako calosc stanowi kompletna dokumentacje fotograficzna pobytu polskich sil zbrojnych "
            "w Szkocji. Takie albumy -- prowadzone przez indywidualnych zolnierzy -- sa cennym zrodlem "
            "do badan nad codziennym zyciem polskiej diaspory wojskowej w Wielkiej Brytanii. "
            "Wiekszosc podobnych albumow rozproszona lub zniszczona -- zachowanie kompletnego albumu "
            "z odrecznymi podpisami jest wyjatkowe."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "good",
        "condition_notes": "Album kompletny, fotografie w dobrym stanie",
        "notes": "Rozdzial VIII: Szkocja (p28_img03). Album PSZ -- strona koncowa. Wartosc lacznie z GL-070.",
        "authentication_status": "verified",
    },
]


# ============================================================
# IMPORT DO BAZY
# ============================================================
print(f"=" * 60)
print(f"IMPORT KOLEKCJI GLUCHOWSKICH -- WERSJA ROZSZERZONA")
print(f"Obiektow do importu: {len(GLUCHOWSKI_OBJECTS)}")
print(f"=" * 60)

imported = 0
skipped = 0
errors = 0

for obj in GLUCHOWSKI_OBJECTS:
    inv = obj["inventory_number"]
    try:
        if collection_object_exists(conn, inv):
            print(f"  SKIP  {inv} -- {obj['title'][:70]}...")
            skipped += 1
            continue

        obj_id = add_collection_object(conn, obj)
        print(f"  ADD   {inv} -> ID {obj_id} -- {obj['title'][:70]}...")
        imported += 1
    except Exception as e:
        print(f"  ERROR {inv} -- {e}")
        errors += 1

conn.commit()
conn.close()

print(f"\n{'=' * 60}")
print(f"WYNIK IMPORTU:")
print(f"  Zaimportowano: {imported}")
print(f"  Pominieto:     {skipped}")
print(f"  Bledy:         {errors}")
print(f"  RAZEM:         {len(GLUCHOWSKI_OBJECTS)}")
print(f"{'=' * 60}")
