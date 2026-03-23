#!/usr/bin/env python3
"""
import_gluchowski_supplement.py -- Uzupelnienie katalogu o brakujace pozycje z Katalogu Naukowego.

Na podstawie pelnej analizy tekstu Kolekcja_Gluchowski_KATALOG_NAUKOWY.pdf (29 stron).
Katalog opisuje 'ponad 120 pozycji' -- ponizsze obiekty uzupelniaja luki w import_gluchowski.py.
"""
import sys, os
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import database
from database import get_connection, add_collection_object, collection_object_exists

database.init_db()
conn = get_connection()

PROVENANCE = "Archiwum rodziny Gluchowskich -> Krzysztof Gluchowski (Brazylia, zm. 16.05.2020) -> Acervo Raro Leiloes, Brazylia -> kolekcja prywatna"

SUPPLEMENT_OBJECTS = [
    # ================================================================
    # ROZDZIAL I -- PON I POCZATKI (1905-1914)
    # Poz. 1-6 z Katalogu Naukowego
    # ================================================================
    {
        "inventory_number": "GL-002",
        "title": "Rozkaz PON -- Komisja Organizacyjna, Piotrkow 24 VIII 1914, pieczec z Orlem w koronie",
        "category": "document",
        "medium": "maszynopis, papier, pieczec PON z Orlem w koronie, adnotacje odreczne",
        "date_created": "24 sierpnia 1914",
        "description": (
            "Rozkaz Komisji Organizacyjnej Polskiej Organizacji Narodowej (PON), skierowany do Marjana "
            "Gluchowskiego jako Komisarza Powiatu Czestochowskiego, nakazujacy wstrzymanie rekwizycji. "
            "Dokument datowany na 24 sierpnia 1914 roku -- trzeci tydzien po wybuchu I wojny swiatowej, "
            "czas absolutnego chaosu na froncie wschodnim, gdy Legiony Polskie wlasnie ruszyly ku Kielcom. "
            "Nosi wlasnorecza pieczec PON z Orlem w koronie -- symbolem polskiej panstwowosci w czasie "
            "gdy Polska nie istniala na mapie Europy. Nakaz wstrzymania rekwizycji swiadczy o probie "
            "utrzymania dyscypliny w oddzialach formowanych napredce. Jest to jeden z PIERWSZYCH "
            "zachowanych rozkazow operacyjnych polskiej organizacji konspiracyjnej z pierwszych dni "
            "I wojny swiatowej. Stanowi uzupelnienie Legitymacji PON nr 2 (GL-003) i afiszu zebrania (GL-004)."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "good",
        "condition_notes": "Maszynopis czytelny, pieczec PON z Orlem zachowana, slady zlozenia operacyjnego",
        "notes": "Rozdzial I, poz. 1. ROZKAZ PON z pieczecia Orla -- jeden z najwczesniejszych dokumentow polskiej konspiracji 1914. Estymacja: 1,500--3,500 PLN.",
        "authentication_status": "verified",
    },
    {
        "inventory_number": "GL-003",
        "title": "Legitymacja PON Nr 2 -- Marjan Gluchowski, Komisarz Powiatu Czestochowskiego, dwujezyczna polsko-niemiecka",
        "category": "document",
        "medium": "druk dwujezyczny, papier, podpis wlasnorecny, pieczec PON z Orlem",
        "date_created": "1914",
        "description": (
            "Karta legitymacyjna Polskiej Organizacji Narodowej NUMER 2 -- wystawiona Marjanowi Gluchowskiemu "
            "jako Komisarzowi Powiatu Czestochowskiego. Dokument dwujezyczny (polsko-niemiecki) -- przeznaczony "
            "do okazywania zarowno polskim oddzialom, jak i wojskom austro-wegierskim, z ktorymi PON "
            "wspoldzialala. Wlasnorecny podpis Marjana Gluchowskiego. Oryginalna pieczec PON z Orlem. "
            "NUMER 2 tej legitymacji jest faktem o fundamentalnym znaczeniu -- oznacza, ze Marjan Gluchowski "
            "byl jednym z doslownie kilku pierwszych oficjalnie uwierzytelnionych dzialaczy PON w powiecie "
            "czestochowskim, prawdopodobnie jednym z ZALOZYCIELI lokalnej struktury. Dwujezycznosc dokumentu "
            "swiadczy o pragmatycznym podejsciu -- PON operowala na styku dwoch stref okupacyjnych."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "very good",
        "condition_notes": "Dokument w bardzo dobrym stanie, podpis czytelny, pieczec zachowana",
        "notes": "Rozdzial I, poz. 2. LEGITYMACJA NR 2 -- dokument zalozycielski PON. Estymacja: 8,000--20,000 PLN. Niski numer = wartosc kolekcjonerska.",
        "authentication_status": "verified",
    },
    {
        "inventory_number": "GL-004",
        "title": "Afisz zebrania PON -- Czestochowa, sala 'Lutni', 2 X 1914, Sieroszewski i Kaden-Bandrowski",
        "category": "document",
        "medium": "druk oryginalny, papier, podpis Marjana Gluchowskiego",
        "date_created": "2 pazdziernika 1914",
        "description": (
            "Drukowany afisz zapraszajacy na publiczne zebranie Polskiej Organizacji Narodowej w sali 'Lutni' "
            "w Czestochowie. Wymienieni prelegenci: Waclaw Sieroszewski (pisarz, etnograf, posel na Sejm), "
            "Juljusz Kaden (pozniejszy Kaden-Bandrowski, jeden z najwazniejszych pisarzy II RP), Marjan "
            "Dabrowski. Podpisany przez Marjana Gluchowskiego jako organizatora. Afisz z 2 pazdziernika 1914 "
            "-- zaledwie dwa miesiace po wybuchu wojny -- jest swiadectwem niezwyklego zjawiska: w momencie "
            "gdy front przebiegpal przez Polske, w Czestochowie organizowano publiczne spotkania z udzialem "
            "czolowych polskich intelektualistow. Obecnosc Sieroszewskiego i Kadena swiadczy, ze zebranie "
            "bylo czescia ogolnopolskiej akcji mobilizacyjnej PON, nie lokalna improwizacja."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "good",
        "condition_notes": "Druk czytelny, papier pozolkly, podpis organizatora zachowany",
        "notes": "Rozdzial I, poz. 3. AFISZ PON z nazwiskami Sieroszewskiego i Kadena-Bandrowskiego. Estymacja: 1,200--2,500 PLN.",
        "authentication_status": "verified",
    },

    # ================================================================
    # ROZDZIAL II -- SIODEMKA I LEGIONY (1913-1918)
    # Poz. 10-14, 29u, 29s
    # ================================================================
    {
        "inventory_number": "GL-013",
        "title": "Zaswiadczenie WBH o sluzbie legionowej gen. Gluchowskiego -- PPS, ZWC, Szkolba Letnia, patrol Beliny, 24 V 1937",
        "category": "document",
        "medium": "maszynopis urzedowy, pieczec WBH, papier",
        "date_created": "24 maja 1937",
        "description": (
            "Zaswiadczenie Wojskowego Biura Historycznego z 24 maja 1937 roku potwierdzajace urzedowo: "
            "czlonkostwo w Organizacji Bojowej PPS od 1905 roku, zalozenie ZWC (Zwiazku Walki Czynnej) "
            "w Liege w Belgii, komendenture Zwiazku Strzeleckiego w Glons i Verviers, uczestnictwo "
            "w Szkole Letniej ZS w Oleandrach, a przede wszystkim -- wyruszenie 2 VIII 1914 z rozkazu "
            "Pilsudskiego jako PIERWSZY PATROL KAWALERII Legionow Polskich. Dokument urzedowy o "
            "fundamentalnym znaczeniu biograficznym -- potwierdza kompletna sciezke niepodleglosciowa "
            "Janusza Gluchowskiego od PPS (1905) przez ZWC (Belgia) do Siodemki Beliny (1914). "
            "Zaswiadczenie WBH ma charakter oficjalny i urzedowy -- wydane 23 lata po opisywanych wydarzeniach."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "good",
        "condition_notes": "Maszynopis urzedowy, pieczec WBH czytelna, papier w dobrym stanie",
        "notes": "Rozdzial II, poz. 10. ZASWIADCZENIE WBH -- oficjalne potwierdzenie udzialu w Siodemce Beliny. Estymacja: 5,000--12,000 PLN.",
        "authentication_status": "verified",
    },
    {
        "inventory_number": "GL-014",
        "title": "Wlasnorecne wspomnienia gen. Gluchowskiego -- egzamin ZWC w Strozach, Pilsudski i Sosnkowski, 1 III 1960",
        "category": "document",
        "medium": "rekopis odreczny, papier, autograf generala",
        "date_created": "1 marca 1960",
        "description": (
            "Wlasnorecny autograf starzejacego sie generala na emigracji, datowany 1 marca 1960 roku, "
            "opisujacy egzamin ZWC w Strozach (1913): egzaminatorow (Pilsudski i Sosnkowski), towarzysza "
            "Kasprzyckiego oraz odznake 'Parasol'. Notatka pisana przez czlowieka majacego 72 lata, "
            "po 46 latach od opisywanych wydarzen -- jest swiadectwem pamieci bezposredniego uczestnika. "
            "KLUCZOWY FAKT: egzaminatorem Gluchowskiego byl Tadeusz Kasprzycki, ktory 22 lata pozniej -- "
            "w 1935 roku -- jako Minister Spraw Wojskowych kontrasygnuje dekret mianowania Gluchowskiego "
            "I Wiceministrem. Obaj panowie przezyli razem pol wieku historii Polski, zaczynajac od "
            "wspolnego egzaminu wojskowego w galicyjskich Strozach."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "good",
        "condition_notes": "Autograf generala czytelny, papier w dobrym stanie",
        "notes": "Rozdzial II, poz. 13. AUTOGRAF GENERALA -- wspomnienia o Pilsudskim i Sosnkowskim. Estymacja: 5,000--15,000 PLN.",
        "authentication_status": "verified",
    },
    {
        "inventory_number": "GL-015",
        "title": "Wykaz sluchaczy Szkoly Letniej Zwiazku Strzeleckiego w Oleandrach",
        "category": "document",
        "medium": "druk/rekopis, papier",
        "date_created": "ok. 1913-1914",
        "description": (
            "Wykaz sluchaczy Szkoly Letniej Zwiazku Strzeleckiego w Oleandrach (Krakow), gdzie szkolili sie "
            "przyszli oficerowie Legionow Polskich. Oleandry -- park w Krakowie -- byly jednym z glownych "
            "osrodkow szkoleniowych paramilitarnych organizacji polskich przed I wojna swiatowa. "
            "Szkola Letnia ZS byla de facto kursem oficerskim -- jej absolwenci tworzyli kadrI dowodcza "
            "Legionow. Gluchowski jest wymieniony wsrod sluchaczy. Dokument dokumentuje krag ludzi, "
            "z ktorych wyroslna elita wojskowa II Rzeczypospolitej."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "good",
        "condition_notes": "Dokument czytelny, papier pozolkly",
        "notes": "Rozdzial II, poz. 11. Wykaz sluchaczy Szkoly Letniej ZS -- kadra dowodcza Legionow. Estymacja: 3,000--8,000 PLN.",
        "authentication_status": "verified",
    },
    {
        "inventory_number": "GL-016",
        "title": "Fotografia konspiracyjna z Placu Strzeleckiego -- Belina-Prazmowski i Gluchowski",
        "category": "photograph",
        "medium": "odbitka fotograficzna, papier fotograficzny",
        "date_created": "ok. 1913-1914",
        "description": (
            "Fotografia konspiracyjna z Placu Strzeleckiego, przedstawiajaca Wladyslawa Beline-Prazmowskiego "
            "i Janusza Gluchowskiego przed I wojna swiatowa. Belina-Prazmowski -- dowodca legendarnej "
            "Siodemki, pierwszego patrolu kawaleryjskiego Legionow -- jest jednym z najbardziej ikonicznych "
            "oficerpw polskiej historii wojskowej. Fotografia dokumentuje relacje miedzy tymi dwoma ludzmi "
            "PRZED wojna -- przed nocnym patrolem 2 sierpnia 1914. Razem z fotografia Siodemki (GL-012) "
            "tworzy pare dokumentujaca relacje przed i podczas wojny."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "good",
        "condition_notes": "Odbitka czytelna, papier fotograficzny z epoki",
        "notes": "Rozdzial II, poz. 14. FOTOGRAFIA KONSPIRACYJNA -- Belina i Gluchowski przed wojna. Estymacja: 3,000--8,000 PLN.",
        "authentication_status": "verified",
    },
    {
        "inventory_number": "GL-017",
        "title": "Karykatura gen. Gluchowskiego autorstwa Iwankowicza -- rysunek satyryczny",
        "category": "artwork",
        "medium": "rysunek, papier, tusz/olowek",
        "date_created": "ok. 1920-1930",
        "description": (
            "Karykatura generala Janusza Gluchowskiego wykonana przez artystE Iwankowicza. "
            "Rysunek satyryczny ukazujacy generala w sposob humorystyczny -- typowy dla tradycji "
            "karykatur wojskowych II RP. Karykatury oficerpw byly popularna forma zyciar towarzyskiego "
            "w kasynie oficerskim. Iwankowicz byl znany z portretow satyrycznych wyzszych oficerpw WP. "
            "Karykatura koresponduje z fotografia portretowa z legitymacji oficerskiej (GL-022) -- "
            "te dwa wizerunki dzieli 15-20 lat."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "good",
        "condition_notes": "Rysunek zachowany, papier lekko pozolkly",
        "notes": "Rozdzial II, poz. 29s. KARYKATURA GENERALA -- rzadki element zycia towarzyskiego kadry oficerskiej II RP. Estymacja: 2,000--5,000 PLN.",
        "authentication_status": "verified",
    },

    # ================================================================
    # ROZDZIAL III -- II RZECZPOSPOLITA (1918-1939)
    # Poz. 7-9, 15-16, 19, 22-24, 29v
    # ================================================================
    {
        "inventory_number": "GL-027",
        "title": "Rozkaz Sztabu Generalnego -- organizacja jazdy w Lubelskiem, 5 XI 1918 (6 dni przed Niepodlegloscia)",
        "category": "document",
        "medium": "maszynopis urzedowy, pieczec Dowodztwa Wojsk Polskich, papier",
        "date_created": "5 listopada 1918",
        "description": (
            "Rozkaz Dowodztwa Wojsk Polskich w Lublinie (Sztab Generalny) nakazujacy Rotmistrzowi "
            "Gluchowskiemu organizacje oddzialu kawalerii w Lubelskiem. Datowany 5 LISTOPADA 1918 ROKU "
            "-- SZESC DNI PRZED OFICJALNYM ODZYSKANIEM NIEPODLEGLOSCI (11 XI 1918) i trzy dni przed "
            "proklamowaniem Republiki Polskiej w Lublinie przez Tymczasowy Rzad Ludowy Ignacego "
            "Daszynskiego. Polska jako panstwo jeszcze NIE ISTNIEJE gdy wydawany jest ten rozkaz. "
            "Wojsko Polskie formuje sie w chaosie -- rozklad armii austriackiej, rewolucja w Niemczech. "
            "Rozkaz organizacji jazdy wskazuje na doswiadczonego kawalerzste -- Rotmistrz Gluchowski "
            "ma za soba kampanie legionowe. Lublin w tych dniach byl centrum rodzacego sie panstwa "
            "polskiego, zanim Pilsudski przejal wladze w Warszawie 11 listopada."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "good",
        "condition_notes": "Maszynopis czytelny, pieczec Dowodztwa zachowana",
        "notes": "Rozdzial III, poz. 7. ROZKAZ SPRZED NIEPODLEGLOSCI -- 6 DNI PRZED 11 LISTOPADA! Estymacja: 8,000--20,000 PLN.",
        "authentication_status": "verified",
    },
    {
        "inventory_number": "GL-028",
        "title": "Pokwitowanie 600 koron -- Lublin, 7 XI 1918 (4 dni przed Niepodlegloscia)",
        "category": "document",
        "medium": "rekopis/druk, papier, podpis",
        "date_created": "7 listopada 1918",
        "description": (
            "Pokwitowanie odbioru 600 koron (waluta austro-wegierska) wystawione w Lublinie 7 listopada "
            "1918 roku -- cztery dni przed oficjalnym odzyskaniem niepodleglosci. Dokument finansowy "
            "zwiazany z organizacja oddzialow kawalerii w Lubelskiem przez Rotmistrza Gluchowskiego. "
            "Kwota 600 koron -- stosunkowo duza suma -- wskazuje na zakup wyposazenia lub zoldu "
            "dla formowanych oddzialow. Waluta koronowa byla jeszcze w obiegu w bylym zaborze "
            "austriackim. Razem z rozkazem z 5 XI (GL-027) dokumentuje pierwsze tygodnie sluzby "
            "Gluchowskiego w odradzajacym sie Wojsku Polskim."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "good",
        "condition_notes": "Dokument czytelny, papier pozolkly",
        "notes": "Rozdzial III, poz. 8. POKWITOWANIE z ostatnich dni przed Niepodlegloscia. Para z GL-027. Estymacja: 2,000--5,000 PLN.",
        "authentication_status": "verified",
    },
    {
        "inventory_number": "GL-029",
        "title": "List gen. Smidlego-Rydza -- zaproszenie na Noworoczny Ranek na Zamku Krolewskim, 30 XII 1918",
        "category": "document",
        "medium": "rekopis wlasnorecny, papier, autograf Smidlego-Rydza",
        "date_created": "30 grudnia 1918",
        "description": (
            "Wlasnorecny list Generala-Podporucznika Edwarda Smidlego-Rydza zapraszajacy Majora "
            "Gluchowskiego na Noworoczny Ranek na Zamku Krolewskim dnia 1 STYCZNIA 1919 ROKU -- "
            "pierwsza noworoczna uroczystosc WOLNEJ POLSKI po 123 latach zaborow. Smidly-Rydz w "
            "grudniu 1918 roku dopiero stawal sie postacia historyczna -- byl dowodca wojsk na Wolyniu. "
            "Do rangi Marszalka Polski i Generalnego Inspektora Sil Zbrojnych dojdzie dopiero w 1936 roku. "
            "List do Gluchowskiego swiadczy, ze obaj nalezeli do tego samego srodowiska legionowego -- "
            "znali sie i traktowali jako rownorzedni oficerowie. Noworoczny Ranek na Zamku 1 stycznia "
            "1919 roku byl ceremonia o gleboko symbolicznym znaczeniu. Smidly-Rydz pojawi sie w kolekcji "
            "ponownie w 1939 roku (GL-036) -- fotografia z gen. Gluchowskim, cztery miesiace przed "
            "wybuchem II wojny. Dwa dokumenty: prog odrodzonej Polski i jej koniec."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "good",
        "condition_notes": "Autograf Smidlego-Rydza czytelny, papier w dobrym stanie",
        "notes": "Rozdzial III, poz. 9. AUTOGRAF SMIDLEGO-RYDZA -- zaproszenie na Zamek Krolewski 1.I.1919. Estymacja: 15,000--35,000 PLN.",
        "authentication_status": "verified",
    },
    {
        "inventory_number": "GL-032",
        "title": "Dekret Krola Rumunii Ferdynanda I -- Order Gwiazdy Rumunii w stopniu Komandora, 1 VIII 1923",
        "category": "document",
        "medium": "kaligrafia oryginalna, papier czerpany, tloczona pieczec krolewska, podpisy",
        "date_created": "1 sierpnia 1923",
        "description": (
            "Oryginalny, kaligrafowany dekret krolewski nadajacy generalowi Gluchowskiemu Order Gwiazdy "
            "Rumunii w stopniu KOMANDORA (nie zwyklego Kawalera -- Komandora). Wlasnorecny podpis "
            "Krola Ferdynanda I Rumunii oraz Ministra I.G. Ducy (pozniejszego premiera Rumunii, "
            "zamordowanego przez Zelazna Gwardie w 1933). Tloczona pieczec krolewska. Kaligrafowany "
            "tekst w jezyku rumuniskim. Kontekst dyplomatyczny: Rumunia i Polska byly sojusznikami "
            "w ramach Malej Ententy i sojuszu polsko-rumunskiego z 1921 roku, wymierzonego przeciw "
            "Rosji Sowieckiej. Podpis I.G. Ducy czyni ten dokument wyjatkowo tragicznym w perspektywie "
            "historycznej: Duca zostanie zamordowany przez faszystow z Zelaznej Gwardii 29 grudnia 1933, "
            "zaledwie 10 lat po podpisaniu tego dokumentu."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "very good",
        "condition_notes": "Kaligrafia nienaruszona, pieczec tloczona zachowana, podpisy czytelne",
        "notes": "Rozdzial III, poz. 15. DEKRET KROLEWSKI RUMUNII -- Order Gwiazdy Rumunii, Komandor. Podpis krola + zamordowanego premiera. Estymacja: 5,000--15,000 PLN.",
        "authentication_status": "verified",
    },
    {
        "inventory_number": "GL-033",
        "title": "Zaproszenie Marszalka Focha -- dekoracja Legia Honorowa na Placu Saskim, 3 V 1923",
        "category": "document",
        "medium": "druk urzedowy MSWojsk., papier, pieczec",
        "date_created": "kwiecien 1923",
        "description": (
            "Dokument Ministerstwa Spraw Wojskowych informujacy plk. Gluchowskiego, ze Marszalek "
            "Ferdinand Foch -- NACZELNY WODZ ALIANTOW w 1918 roku, ojciec zwyciestwa nad Niemcami -- "
            "osobiscie wreczy mu odznake Kawalera Legii Honorowej na Placu Saskim w Warszawie, "
            "dnia 3 maja 1923 roku (Swieto Konstytucji). Dokument pelni funkcje zarowno zaproszenia, "
            "jak i przepustki na uroczystosc: 'Sluzy jako legitymacja do udzialu w uroczystosci.' "
            "Wizyta Focha w Warszawie w maju 1923 byla wydarzeniem politycznym o pierwszorzednym "
            "znaczeniu -- symbolicznym gestem poparcia Francji dla niepodleglosci Polski. "
            "Dekoracja na Placu Saskim (przed Palacem Saskim, gdzie miescilo sie MSWojsk.) "
            "byla publiczna ceremonia. Legia Honorowa wreczana przez Focha OSOBISCIE -- nie przez "
            "ambasadora -- to dyplomatyczne wyroznienie najwyzszej rangi."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "good",
        "condition_notes": "Druk urzedowy czytelny, pieczec MSWojsk. zachowana",
        "notes": "Rozdzial III, poz. 16. ZAPROSZENIE OD MARSZALKA FOCHA -- Legia Honorowa 3 maja 1923. Estymacja: 10,000--25,000 PLN.",
        "authentication_status": "verified",
    },
    {
        "inventory_number": "GL-034",
        "title": "Legitymacja Krzyza Walecznych z podpisem gen. Sosnkowskiego -- Rtm. Gluchowski, 7 P.Ul., 31 VII 1922",
        "category": "document",
        "medium": "druk urzedowy, papier, podpis wlasnorecny ministra Sosnkowskiego",
        "date_created": "31 lipca 1922",
        "description": (
            "Legitymacja Krzyza Walecznych z DWOMA OKUCIAMI (dwukrotne nadanie), podpisana przez "
            "Kazimierza Sosnkowskiego jako Ministra Spraw Wojskowych. Odznaczony: Rotmistrz Gluchowski "
            "Janusz, 7 Pulk Ulanow. Data: 31 lipca 1922. Zestawienie Sosnkowskiego jako egzaminatora "
            "Gluchowskiego w 1913 roku i teraz, w 1922, jako ministra podpisujacego mu odznaczenie "
            "-- jest metafora calej kariery generala. Sosnkowski to jeden z najwybitniejszych strategow "
            "wojskowych II RP. Fakt, ze podpisuje akurat legitymacje KW Gluchowskiemu, swiadczy "
            "o tym, ze obaj nalezeli do waskigo kregu zaufanych pilsudczykow. Krzyz Walecznych z dwoma "
            "okuciami -- nadany za dwa osobne wyroznienia bojowe -- to odznaczenie dla doswiadczonego "
            "zolnierza. Legitymacja stanowi pare z fizycznym medalem KW (GL-021)."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "good",
        "condition_notes": "Podpis Sosnkowskiego czytelny, druk zachowany",
        "notes": "Rozdzial III, poz. 17. LEGITYMACJA KW Z PODPISEM SOSNKOWSKIEGO. Para z GL-021 (medal fizyczny). Estymacja: 5,000--12,000 PLN (sam) | 12,000--25,000 PLN (z medalem).",
        "authentication_status": "verified",
    },
    {
        "inventory_number": "GL-035",
        "title": "Rozkaz wyjazdu na pogrzeb Jozefa Pilsudskiego -- maj 1935",
        "category": "document",
        "medium": "maszynopis urzedowy, papier, pieczec",
        "date_created": "maj 1935",
        "description": (
            "Rozkaz sluzbowy nakazujacy gen. Gluchowskiemu wyjazd na pogrzeb Marszalka Jozefa "
            "Pilsudskiego, ktory zmarl 12 maja 1935 roku. Pogrzeb Pilsudskiego byl wydarzeniem "
            "o skali bezprecedensowej w historii II Rzeczypospolitej -- na ulice Krakowa wyszly "
            "setki tysiecy ludzi, a delegacje przybyly z calego swiata. Gluchowski jako jeden "
            "z Siodemki -- ostatnich zyjaycych towarzyszy Pilsudskiego z nocnego patrolu 1914 -- "
            "mial w tym pogrzebie znaczenie wyjatkowe. Dokument laczy sie bezposrednio z listem "
            "Aleksandry Pilsudskiej (GL-038), w ktorym wdowa Marszalka dziekuje Gluchowskiemu "
            "za depesze kondolencyjna."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "good",
        "condition_notes": "Maszynopis czytelny, pieczec zachowana",
        "notes": "Rozdzial III, poz. 19. ROZKAZ NA POGRZEB PILSUDSKIEGO. Para z GL-038 (list Pilsudskiej). Estymacja: 5,000--12,000 PLN.",
        "authentication_status": "verified",
    },
    {
        "inventory_number": "GL-036",
        "title": "Fotografia uroczystosci wreczenia sztandaru -- gen. Gluchowski obok Marszalka Smidlego-Rydza, 1939",
        "category": "photograph",
        "medium": "odbitka fotograficzna, papier fotograficzny",
        "date_created": "1939",
        "description": (
            "Fotografia uroczystosci wreczenia sztandaru, na ktorej gen. Gluchowski stoi obok "
            "Marszalka Edwarda Smidlego-Rydza. Datowana na 1939 rok -- CZTERY MIESIACE PRZED "
            "WYBUCHEM II WOJNY SWIATOWEJ. Smidly-Rydz byl w tym czasie Generalnym Inspektorem "
            "Sil Zbrojnych i faktycznym wladca Polski. Fotografia dokumentuje apogeum kariery "
            "obu oficerow -- i zarazem ostatnie miesiace II Rzeczypospolitej. Zestawiona z listem "
            "Smidlego-Rydza z 30 XII 1918 (GL-029) tworzy pare: prog odrodzonej Polski i jej koniec. "
            "Dwadziescia lat i cala epoka dzieli te dwa dokumenty."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "good",
        "condition_notes": "Odbitka fotograficzna w dobrym stanie, twarze rozpoznawalne",
        "notes": "Rozdzial III, poz. 22. FOTOGRAFIA Z SMIDLYM-RYDZEM 1939 -- ostatnie miesiace II RP. Para z GL-029. Estymacja: 5,000--12,000 PLN.",
        "authentication_status": "verified",
    },
    {
        "inventory_number": "GL-037",
        "title": "List Aleksandry Pilsudskiej -- prosba o dwie pary koni, monogram 'P', Stacja Milosna, 17 VIII 1923",
        "category": "document",
        "medium": "rekopis wlasnorecny, papier, monogram P (Pilsudska)",
        "date_created": "17 sierpnia 1923",
        "description": (
            "Wlasnorecny list Aleksandry Pilsudskiej (zony Marszalka) do plk. Gluchowskiego z prosba "
            "o dwie pary koni. Monogram 'P' (Pilsudska). Wyslany ze Stacji Milosnej pod Warszawa. "
            "Ton listu jest bezposredni i naturalny -- swiadczy o zywej, codziennej przyjazni miedzy "
            "rodzinami. Aleksandra Pilsudska pisze do pulkownika, ktorego zna osobiscie, prosi o konie, "
            "nie waha sie, nie ceremoni. Jest to dokument zycia prywatnego elity II RP -- ukazuje "
            "relacje miedzy rodzinami wojskowymi na poziomie codziennosci, daleko od oficjalnych "
            "uroczystosci. Dwanascie lat i cala epoka dzieli ten list od listu kondolencyjnego "
            "po smierci Pilsudskiego (GL-038)."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "good",
        "condition_notes": "Rekopis czytelny, monogram P zachowany",
        "notes": "Rozdzial III, poz. 23. LIST ALEKSANDRY PILSUDSKIEJ -- codzienna przyjan z Gluchowskimi. Estymacja: 8,000--20,000 PLN.",
        "authentication_status": "verified",
    },
    {
        "inventory_number": "GL-038",
        "title": "List wdowy Aleksandry Pilsudskiej -- podziekowanie za depesze kondolencyjna, Warszawa-Przemysl, 6 VI 1935",
        "category": "document",
        "medium": "rekopis wlasnorecny, papier, oryginalna koperta z polskim znaczkiem",
        "date_created": "6 czerwca 1935",
        "description": (
            "List wdowy po Marszalku Pilsudskim -- ktory zmarl 12 maja 1935 roku -- dziekujacy gen. "
            "Gluchowskiemu za depesze kondolencyjna. Data: 6 czerwca 1935. Wyslany z Warszawy do "
            "Przemysla (gdzie Gluchowski byl Dowodca DOK X). Oryginalna koperta z polskim znaczkiem. "
            "Aleksandra Pilsudska wsrod setek depesz kondolencyjnych z calego swiata odpisuje OSOBISCIE "
            "Gluchowskiemu. To jest swiadectwo, ze relacja miedzy tymi rodzinami byla gleboka "
            "i prawdziwa, nie tylko protokolarna. Gluchowski walczyl ramie w ramie z Pilsudskim "
            "od 1914 roku -- dla wdowy byl kims z tamtego swiata, ktory zna jej meza nie ze zdjec, "
            "ale z nocy przekroczenia granicy w 1914 roku. Para z GL-037: od prosby o konie (1923) "
            "po kondolencje (1935)."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "very good",
        "condition_notes": "Rekopis czytelny, koperta z znaczkiem zachowana",
        "notes": "Rozdzial III, poz. 24. LIST WDOWY PO PILSUDSKIM z oryginalna koperta. Para z GL-037. Estymacja: 15,000--40,000 PLN. Para: 25,000--65,000 PLN.",
        "authentication_status": "verified",
    },
    {
        "inventory_number": "GL-039",
        "title": "Pocztowka Jozefa Pilsudskiego z Krynicy -- autograf Marszalka, 1933",
        "category": "document",
        "medium": "pocztowka, rekopis, autograf Pilsudskiego",
        "date_created": "1933",
        "description": (
            "Pocztowka wyslana przez Jozefa Pilsudskiego z Krynicy, gdzie Marszalek wielokrotnie "
            "wypoczywal w latach 30. Wlasnorecny autograf Pilsudskiego. Krynica byla popularnym "
            "kurortem wyzszych sfer II RP -- Pilsudski odwiedzal ja regularnie. Pocztowka z 1933 "
            "roku pochodzi z ostatnich lat zycia Marszalka (zm. 12 V 1935). Wlasnorecny autograf "
            "Pilsudskiego to czwarty dokument z podpisem Marszalka w kolekcji (obok dekretow 1933 "
            "i dyplomu Krzyza Legionowego). Koresponduje z fotografioa portretowa Pilsudskiego "
            "(GL-011) i listami Aleksandry Pilsudskiej (GL-037, GL-038)."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "good",
        "condition_notes": "Pocztowka zachowana, autograf Pilsudskiego czytelny",
        "notes": "Rozdzial III, poz. 29v. POCZTOWKA Z AUTOGRAFEM PILSUDSKIEGO. Estymacja: 8,000--20,000 PLN.",
        "authentication_status": "verified",
    },

    # ================================================================
    # ROZDZIAL V -- GETTO LODZKIE -- UZUPELNIENIA
    # Poz. 29g, 29h, 29i
    # ================================================================
    {
        "inventory_number": "GL-045",
        "title": "List K. Gluchowskiego do numizmatyka Herziga w Ohio -- inwentarz obiektow gettowych, pierscionek Ajzenmana, 17 XI 1968",
        "category": "document",
        "medium": "maszynopis, papier, podpis",
        "date_created": "17 listopada 1968",
        "description": (
            "List K. Gluchowskiego pisany na prosbe wuja Wlodzimierza Gluchowskiego z Lodzi do "
            "numizmatyka Herziga w Ohio (USA). Podaje PELNY INWENTARZ obiektow gettowych: pierscionek "
            "z getta z 5.11.1942 (z monogramem S.A. -- Szymon Ajzenman, przelozony rewiru Marysin), "
            "kupon pocztowy 10 pf., talon 200g drozdy, pokwitowanie, katalog Tychsena 1794. "
            "Notuje, ze Wlodzimierz wczesniej wyslal Herzigowi materialy o martyrologii Zydow. "
            "PIERSCIONEK AJZENMANA jest obiektem szczegolnym: ofiara getta lodzkiego, zamordowanego "
            "przelozonego rewiru Marysin, zachowany przez polska rodzine i przez 40 lat szukajacy "
            "wlasciwego miejsca. Korespondencja z lat 1958-1984 to trwajaca 26 lat historia poszukiwania."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "good",
        "condition_notes": "Maszynopis czytelny, podpis zachowany",
        "notes": "Rozdzial V, poz. 29g. LIST Z INWENTARZEM OBIEKTOW GETTOWYCH -- pierscionek Ajzenmana. Estymacja: 3,000--8,000 PLN.",
        "authentication_status": "verified",
    },
    {
        "inventory_number": "GL-046",
        "title": "List K.A. Gluchowskiego z Rochester do Herziga -- oferta tych samych obiektow gettowych, 21 XI 1984",
        "category": "document",
        "medium": "maszynopis, papier, podpis",
        "date_created": "21 listopada 1984",
        "description": (
            "List K.A. Gluchowskiego (syn lub bratanek) z Rochester w Anglii, oferujacy te same "
            "obiekty gettowe temu samemu numizmatykowi Herzigowi w Ohio -- 16 lat po poprzednim "
            "liscie (GL-045). Fakt, ze przez 26 lat (1958-1984) rodzina Gluchowskich probowala "
            "znalezc godne miejsce dla artefaktow z getta lodzkiego -- najpierw Ambasada Izraela "
            "(1958), potem Yad Vashem, potem Herzig (1968, 1984) -- swiadczy o glebokiej etycznej "
            "wrazliwosci i poczuciu odpowiedzialnosci za te przedmioty. Komplet czterech listow "
            "(GL-040, GL-044, GL-045, GL-046) dokumentuje ta 26-letnia odyseje."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "good",
        "condition_notes": "Maszynopis czytelny, papier w dobrym stanie",
        "notes": "Rozdzial V, poz. 29h. LIST Z 1984 -- 26 lat poszukiwan. Komplet 4 listow: GL-040, GL-044, GL-045, GL-046. Estymacja: 2,000--5,000 PLN.",
        "authentication_status": "verified",
    },
    {
        "inventory_number": "GL-047",
        "title": "Fotokopie katalogu Tychsena 1794 -- numizmatyka gettowa, material porownawczy",
        "category": "document",
        "medium": "fotokopia, papier",
        "date_created": "ok. 1968",
        "description": (
            "Fotokopie katalogu numizmatycznego Tychsena z 1794 roku, stanowiace material "
            "porownawczy do kolekcji monet i banknotow gettowych. Wspomniany w liscie do "
            "Herziga (GL-045) jako czesc dokumentacji przeslanej numizmatykowi. Katalog "
            "Tychsena jest klasycznym dzielem numizmatyki XVIII-wiecznej. Wlodzimierz "
            "Gluchowski zgromadzil ten material jako naukowe uzasadnienie wartosci swoich "
            "obiektow gettowych -- swiadczy to o profesjonalnym podejsciu do kolekcjonerstwa."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "good",
        "condition_notes": "Fotokopia czytelna",
        "notes": "Rozdzial V, poz. 29i. FOTOKOPIE TYCHSENA -- material numizmatyczny. Estymacja: 500--1,500 PLN.",
        "authentication_status": "photocopy",
    },

    # ================================================================
    # ROZDZIAL VI -- 7 PULK ULANOW -- UZUPELNIENIA
    # Poz. 29m, 29o
    # ================================================================
    {
        "inventory_number": "GL-053",
        "title": "Nekrolog plk. Lewandowskiego -- Kolo 7 Pulku Ulanow, 1960",
        "category": "document",
        "medium": "druk, papier",
        "date_created": "1960",
        "description": (
            "Drukowany nekrolog pulkownika Lewandowskiego -- weterana 7 Pulku Ulanow Lubelskich, "
            "zmarlego w 1960 roku. Podpisany przez Kolo Zolnierzy 7 Pulku Ulanow na emigracji. "
            "Rok 1960 to rok wielkich strat srodowiska pulkowego -- w tym samym roku zmarl "
            "rowniez Jan Lorens (GL-052). Oba nekrologi z tego samego Kola, z tego samego roku, "
            "dokumentuja odchodzenie pokolenia weteranow kawalerii II RP. Srodowisko pulkowe "
            "Gluchowskiego obejmowalo trzy kontynenty: Polska, Londyn, Chicago."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "good",
        "condition_notes": "Druk czytelny, papier pozolkly",
        "notes": "Rozdzial VI, poz. 29m. NEKROLOG WETERANA -- para z GL-052 (Lorens). Estymacja: 400--1,000 PLN.",
        "authentication_status": "verified",
    },
    {
        "inventory_number": "GL-054",
        "title": "Oplatek wigilijny 7 Pulku Ulanow w Chicago -- zaproszenie/program, ok. 1950-1960",
        "category": "document",
        "medium": "druk, papier",
        "date_created": "ok. 1950-1960",
        "description": (
            "Zaproszenie lub program Oplattka Wigilijnego Kola Zolnierzy 7 Pulku Ulanow Lubelskich "
            "w Chicago. Tradycja swiateczna kontynuowana na emigracji -- weterani kawalerii II RP "
            "spotykali sie co roku na Wigilii pulkowej, utrzymujac wiezi i tradycje mimo rozproszenia "
            "po swiecie. Chicago bylo jednym z najwiekszych skupisk polskiej emigracji. Oplatek "
            "pulkowy nabiera konkretnego kontekstu w zestawieniu z nekrologiem Jana Lorensa (GL-052), "
            "ktory jako prezes sekcji Kola byl prawdopodobnie jego organizatorem."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "good",
        "condition_notes": "Druk zachowany, papier w dobrym stanie",
        "notes": "Rozdzial VI, poz. 29o. OPLATEK WIGILIJNY -- tradycja pulkowa na emigracji. Estymacja: 500--1,500 PLN.",
        "authentication_status": "verified",
    },

    # ================================================================
    # ROZDZIAL VII -- KRZYSZTOF ANDRZEJ -- UZUPELNIENIA
    # Poz. 29w, 29z(A), 29z(D), 29z(F), 29z(I)
    # ================================================================
    {
        "inventory_number": "GL-073",
        "title": "Trzy swiadectwa urodzenia Krzysztofa Andrzeja Gluchowskiego -- 1942, 1943, 1948 (dokumenty konspiracyjne + powrot)",
        "category": "document",
        "medium": "druk urzedowy, papier, pieczecie GG/RP",
        "date_created": "18 V 1942 / 12 XI 1943 / 23 VII 1948",
        "description": (
            "Trzy odpisy swiadectwa urodzenia Krzysztofa Andrzeja Gluchowskiego wystawione w roznych "
            "momentach: (1) 18 maja 1942 -- pierwsze swiadectwo z okresu Generalnego Gubernatorstwa, "
            "prawdopodobnie przygotowywane na potrzeby konspiracyjne; (2) 12 listopada 1943 -- drugie "
            "swiadectwo GG, wystawione dzien po rocznicy odzyskania niepodleglosci, w tym samym "
            "czasie co Kennkarte (GL-061) -- seria dokumentow tozsamosci przygotowywana na potrzeby "
            "konspiracyjne; (3) 23 lipca 1948 -- trzecie swiadectwo po powrocie do Polski, "
            "potwierdzajace, ze Krzysztof przezyl wojne i wrpcil z niewoli. Seria trzech dokumentow "
            "dokumentuje droge od okupacji przez konspiracje do powrotu."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "good",
        "condition_notes": "Dokumenty urzedowe zachowane, pieczecie czytelne",
        "notes": "Rozdzial VII, poz. 29w. TRZY SWIADECTWA URODZENIA -- droga od okupacji do powrotu. Estymacja: 3,000--8,000 PLN (komplet).",
        "authentication_status": "verified",
    },
    {
        "inventory_number": "GL-074",
        "title": "Przepustka Jednorazowa Specjalna AK -- st. ul. Gluchowski ps. 'Jurek', 18 IX 1944 (dzien 49. Powstania)",
        "category": "document",
        "medium": "druk/rekopis, pieczec Komendy Okregu AK, papier z epoki",
        "date_created": "18 wrzesnia 1944",
        "description": (
            "Pierwsza z trzech zachowanych przepustek jednorazowych specjalnych AK wydanych "
            "Krzysztofowi Gluchowskiemu ps. 'Jurek/Jures'. Datowana 18 wrzesnia 1944 -- dzien 49. "
            "Powstania Warszawskiego. Pieczec Komendy Okregu AK m.st. Warszawy. Seria trzech "
            "przepustek (GL-074, GL-075, GL-065) z 18, 24 i 29 wrzesnia 1944 roku to prawdopodobnie "
            "JEDYNY ZACHOWANY W REKACH PRYWATNYCH komplet przepustek jednej osoby z koncowki "
            "Powstania Warszawskiego. Kapitulacja nastapila 2 pazdziernika -- ostatnia przepustka "
            "jest wystawiona trzy dni wczesniej."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "fair",
        "condition_notes": "Papier kremowy z epoki, pieczec czytelna, zagiecia polowe",
        "notes": "Rozdzial VII, poz. 29z(A). PIERWSZA PRZEPUSTKA AK -- dzien 49. Powstania. Komplet 3 przepustek: GL-074, GL-075, GL-065. Estymacja: 8,000--20,000 PLN.",
        "authentication_status": "verified",
    },
    {
        "inventory_number": "GL-075",
        "title": "Przepustka AK na dwie osoby -- plut. podchor. 'Piotr' i st. ul. 'Jures', rozkaz kpt. 'Adaniros', 24 IX 1944",
        "category": "document",
        "medium": "druk/rekopis, pieczec Komendy Okregu AK, podpis plk. Wachnowskiego",
        "date_created": "24 wrzesnia 1944",
        "description": (
            "Oryginalna przepustka jednorazowa specjalna Komendy Okregu AK m.st. Warszawy. "
            "Na DWIE OSOBY: plut. podchor. 'Piotr' i st. ul. 'Jures' (Gluchowski). Rozkaz "
            "Kapitana ps. 'Adaniros'. Wazna do 25/IX. Pieczec fioletowa KOMENDA OKREGU A.K. "
            "m.st. W-wy. Wlasnorecny podpis Z-cy Kmdta Okr. plk. Wachnowskiego. Przepustka "
            "ujawnia nieznanego towarzysza broni 'Piotra' -- podchorazego, ktory szedl razem "
            "z Krzysztofem. Kapitan 'Adaniros' to inny oficer niz 'Jelen' z pozostalych "
            "przepustek -- wskazuje, ze Krzysztof byl lacznikiem miedzy roznymi dowodcami. "
            "Dzien 55. Powstania -- Stare Miasto padlo juz 2 IX, trwaly walki na Srodmiesciu."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "fair",
        "condition_notes": "Papier kremowy z epoki, pieczec fioletowa czytelna, podpis Wachnowskiego zachowany",
        "notes": "Rozdzial VII, poz. 29z(C). PRZEPUSTKA NA DWIE OSOBY -- towarzysz broni 'Piotr'. Estymacja: 8,000--20,000 PLN.",
        "authentication_status": "verified",
    },
    {
        "inventory_number": "GL-076",
        "title": "Kartka lacznikowa z Powstania Warszawskiego -- system komunikacji miedzy dzielnicami",
        "category": "document",
        "medium": "rekopis, papier",
        "date_created": "wrzesien 1944",
        "description": (
            "Oryginalna kartka lacznikowa z Powstania Warszawskiego -- element systemu lacznosci "
            "cywilnej dzialajacego w oblezonej Warszawie. W Powstaniu dzialal system laczniczek "
            "i goncow, ktorzy przenosili listy i wiadomosci przez linie walk. Kartka dokumentuje "
            "ten sam system, przez ktory list Krzysztofa dotarl do rodziny i odpowiedz Ciotki "
            "Waleski (GL-077) dotarla do Plutonu 1112. Sama kartka jest materialnym swiadectwem "
            "dzialania sieci lacznosci cywilnej w warunkach walki miejskiej."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "fair",
        "condition_notes": "Papier zniszczony, rekopis czesciowo czytelny",
        "notes": "Rozdzial VII, poz. 29z(D). KARTKA LACZNIKOWA -- system komunikacji Powstania. Estymacja: 3,000--8,000 PLN.",
        "authentication_status": "verified",
    },
    {
        "inventory_number": "GL-077",
        "title": "Odpowiedz Ciotki Waleski do Krzysztofa -- 'Krzysiu! Wszyscy jestesmy zdrowi', 24 IX 1944 (dzien 55. Powstania)",
        "category": "document",
        "medium": "rekopis olowkowy, papier w kratke",
        "date_created": "24 wrzesnia 1944",
        "description": (
            "Odreczna odpowiedz Ciotki Waleski na list Krzysztofa z 26 VIII 1944. Papier w kratke, "
            "olowek. 'Krzysiu! Wszyscy jestesmy zdrowi. Nasze domy stoja chociaz poharatane troche, "
            "tylko ciotki Smidki nie mie miedzy nami -- mowia ze jest w aptece. Bardzo cieszymy sie "
            "ze dowiedzielismy sie o Tobie tak dobrych wiesci. Caluje Cie serdecznie i bardzo mocno. "
            "Ucaluj wszystkich swoich i pania Zosie i p. Stanislawa... Ciotka Waleska. 24/IX - 44.' "
            "Rewers: 'Pluton 1112 -- Krzysztof'. Odpowiedz Ciotki Waleski, pisana w dniu 55. "
            "Powstania, jest skrotem cywilnej Warszawy: domy stoja ale poharatane, ciotka gdzies "
            "w aptece, wielka radosc ze chlopiec zyje. ZACHOWANIE KORESPONDENCJI W OBIE STRONY "
            "jest historycznym fenomenem -- ze list dotarl do rodziny, ze rodzina zdolala odpowiedziec "
            "i ze odpowiedz dotarla do Plutonu 1112 -- to seria cudow."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "fair",
        "condition_notes": "Papier w kratke, olowek czesciowo wyblakly ale czytelny",
        "notes": "Rozdzial VII, poz. 29z(F). ODPOWIEDZ CIOTKI WALESKI -- korespondencja w obie strony z Powstania. Para z GL-064. Estymacja: 3,000--8,000 PLN.",
        "authentication_status": "verified",
    },
    {
        "inventory_number": "GL-078",
        "title": "List Krzysztofa z obozu jenieckiego do ojca -- 'Trzymam sie do mnie!', olowek na brazowym papierze obozowym",
        "category": "document",
        "medium": "rekopis olowkowy, brazowy papier obozowy",
        "date_created": "ok. pazdziernik 1944 - kwiecien 1945",
        "description": (
            "Odreczny list Krzysztofa Gluchowskiego z obozu jenieckiego Stalag XI-B do ojca. "
            "Olowek, brazowy papier obozowy. Krzysztof podaje numer jeniecki 141009, informuje "
            "o przeniesieniu do Westfalii (Stalag VIF Dorsten), prosi o listy przez Czerwony Krzyz "
            "w trzech egzemplarzach. Konczy slowami: 'Trzymam sie do mnie!' -- pisany przez "
            "15-latka z obozu jenieckiego, jest jednym z najbardziej poruszajacych dokumentow "
            "kolekcji. List domyka chronologie Krzysztofa po kapitulacji Powstania Warszawskiego "
            "(2 X 1944) -- od ulana AK w Warszawie, przez Powstanie, do niemieckiego obozu "
            "jenieckiego. Komplet trzech dokumentow jenieckich: tag (GL-068), Personalkarte (GL-069) "
            "i ten list."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "fair",
        "condition_notes": "Brazowy papier obozowy, olowek czytelny, slady cenzury obozowej",
        "notes": "Rozdzial VII, poz. 29z(I). LIST Z OBOZU -- 'Trzymam sie do mnie!' Komplet z GL-068 i GL-069. Estymacja: 5,000--12,000 PLN.",
        "authentication_status": "verified",
    },
]


# ============================================================
# IMPORT DO BAZY
# ============================================================
print(f"=" * 60)
print(f"UZUPELNIENIE KATALOGU GLUCHOWSKICH -- {len(SUPPLEMENT_OBJECTS)} nowych obiektow")
print(f"=" * 60)

imported = 0
skipped = 0

for obj in SUPPLEMENT_OBJECTS:
    inv = obj["inventory_number"]
    if collection_object_exists(conn, inv):
        print(f"  SKIP: {inv} (juz istnieje)")
        skipped += 1
    else:
        add_collection_object(conn, obj)
        print(f"  DODANO: {inv} -- {obj['title'][:70]}")
        imported += 1

conn.commit()
conn.close()
print(f"\n{'=' * 60}")
print(f"WYNIK: Dodano {imported}, pominieto {skipped}")
print(f"Lacznie nowych pozycji: {len(SUPPLEMENT_OBJECTS)}")
print(f"{'=' * 60}")
