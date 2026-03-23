#!/usr/bin/env python3
"""
import_29z.py -- Import Seria 29z: dokumenty Krzysztofa Gluchowskiego
z okresu Powstania Warszawskiego, niewoli i repatriacji (1944-1946).

36 obiektow (GL-100 do GL-135): listy jenieckie, pamietnik obozowy,
sprawozdania wojenne, dokumenty repatriacyjne, zeszyty szkolne.
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
# SERIA 29z -- DOKUMENTY KRZYSZTOFA GLUCHOWSKIEGO
# Powstanie Warszawskie, niewola, repatriacja (1944-1946)
# ============================================================

PROVENANCE = "Archiwum rodziny Gluchowskich -> Krzysztof Gluchowski (Brazylia, zm. 16.05.2020) -> Acervo Raro Leiloes, Brazylia -> kolekcja prywatna"

SERIA_29Z_OBJECTS = [
    # ================================================================
    # 29z(J) -- List po kapitulacji Powstania
    # ================================================================
    {
        "inventory_number": "GL-100",
        "title": "List do st. ul. Jurka po kapitulacji Powstania Warszawskiego, 16.X.1944",
        "category": "document",
        "medium": "kartka, olowek, rekopis",
        "date_created": "16 pazdziernika 1944",
        "description": (
            "Kartka zapisana olowkiem, datowana na 16 pazdziernika 1944 roku -- dwa dni po kapitulacji "
            "Powstania Warszawskiego. Adresowana do starszego ulana o pseudonimie Jurek. Na rewersie "
            "adres: 'Jurek / p. 1112 / Jelen'. Numer 1112 odnosi sie do jednostki w ramach 7 Pulku "
            "Ulanow AK 'Jelen'. Jest to jedyny znany dokument datowany po kapitulacji, ktory byl "
            "kierowany do konkretnej jednostki Armii Krajowej. Swiadczy o probach utrzymania lacznosci "
            "w chaosie po zakonczeniu walk. Dokument o wyjatkowej wartosci historycznej dla badan "
            "nad ostatnimi dniami Powstania i losami zolnierzy AK po kapitulacji."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "fair",
        "condition_notes": "Kartka zapisana olowkiem, pismo czytelne, papier zuzyty",
        "notes": "Seria 29z(J). Jedyny dokument po kapitulacji kierowany do jednostki AK. Estymacja: 3,000--8,000 PLN.",
        "authentication_status": "verified",
    },

    # ================================================================
    # 29z(K) nowy -- List Krzysztofa ze Stalagu
    # ================================================================
    {
        "inventory_number": "GL-101",
        "title": "List Krzysztofa do ojca ze Stalagu XIB, 1944/1945 -- Kochany Tatusiu",
        "category": "document",
        "medium": "karta pocztowa jeniecka, rekopis",
        "date_created": "1944/1945",
        "description": (
            "List Krzysztofa Gluchowskiego do ojca Stefana, pisany ze Stalagu XI B. Zaczyna sie slowami "
            "'Kochany Tatusiu!' -- typowy zwrot w korespondencji jenieckiej miedzy ojcem a synem. "
            "Krzysztof informuje o transporcie do Westfalii i podaje swoj numer jeniecki 141009. "
            "Przesyla pozdrowienia dla oficerow 7 Pulku Ulanow, co swiadczy o utrzymywaniu wiezow "
            "z macierzysta jednostka nawet w niewoli. Numer jeniecki 141009 pozwala sledzic losy "
            "Krzysztofa w systemie obozowym. Dokument jest swiadectwem relacji ojciec-syn w warunkach "
            "niewoli niemieckiej."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "fair",
        "condition_notes": "Karta pocztowa jeniecka, pismo odreczne czytelne, slady cenzury",
        "notes": "Seria 29z(K) nowy. Numer jeniecki 141009. Pozdrowienia dla 7 P.Ul. Estymacja: 2,000--6,000 PLN.",
        "authentication_status": "verified",
    },

    # ================================================================
    # 29z(K) -- Kriegsgefangenenpost ppor. Stefana
    # ================================================================
    {
        "inventory_number": "GL-102",
        "title": "Kriegsgefangenenpost ppor. Stefana do Zofii Okuszkowej, Stalag XIB, 14.X.1944",
        "category": "document",
        "medium": "karta pocztowa jeniecka, formularz drukowany, rekopis",
        "date_created": "14 pazdziernika 1944",
        "description": (
            "Oryginalna karta pocztowa jencow wojennych (Kriegsgefangenenpost) wyslana ze Stalagu XI B, "
            "datowana 14 pazdziernika 1944 roku. Nadawca -- ppor. Stefan Gluchowski, numer jenca 01245. "
            "Adresatka -- Zofia Okuszkowa. Stefan informuje, ze Krzysztof przebywa w stalagu. Przekazuje "
            "tragiczna wiadomosc: Lech zginal 15 wrzesnia na Mokotowie. Smierc Lecha Gluchowskiego "
            "na Mokotowie potwierdza, ze walczyl on w jednym z najciezszych rejoncow Powstania. "
            "Dokument laczy trzy watki: niewole Stefana i Krzysztofa, smierc Lecha, oraz probe "
            "utrzymania kontaktu z rodzina poprzez formularz jeniecki."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "good",
        "condition_notes": "Formularz jeniecki kompletny, stemple czytelne, pismo zachowane",
        "notes": "Seria 29z(K). Nr jenca 01245. Smierc Lecha 15.IX na Mokotowie. Estymacja: 4,000--10,000 PLN.",
        "authentication_status": "verified",
    },

    # ================================================================
    # 29z(L) -- Antwort-Postkarte do Krzysztofa
    # ================================================================
    {
        "inventory_number": "GL-103",
        "title": "Antwort-Postkarte do Krzysztofa, Stalag VIF Dorsten, 29.XI.1944",
        "category": "document",
        "medium": "karta pocztowa, formularz drukowany, rekopis",
        "date_created": "29 listopada 1944",
        "description": (
            "Niemiecka karta odpowiedzi (Antwort-Postkarte) adresowana do Krzysztofa Gluchowskiego "
            "w Stalagu VI F w Dorsten, datowana 29 listopada 1944. Nadawczyni -- Maria Jansz -- "
            "potwierdza transfer Krzysztofa miedzy obozami. Zawiera informacje, ze matka Krzysztofa "
            "przebywa w Czestochowie przy ulicy Hoene-Wronskiego. Jest to pierwszy znany dokument "
            "potwierdzajacy istnienie Stalagu VI F jako miejsca przetrzymywania polskich jencow. "
            "Karta stanowi wazne ogniwo w rekonstrukcji trasy obozowej Krzysztofa: Stalag XI B -> "
            "Stalag VI F Dorsten -> Stalag VI J."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "good",
        "condition_notes": "Karta pocztowa w dobrym stanie, stemple i pismo czytelne",
        "notes": "Seria 29z(L). Pierwszy dokument na Stalag VIF. Matka w Czestochowie. Estymacja: 3,000--8,000 PLN.",
        "authentication_status": "verified",
    },

    # ================================================================
    # 29z(M) -- List do gen. Janusza w Londynie
    # ================================================================
    {
        "inventory_number": "GL-104",
        "title": "Kriegsgefangenenpost Krzysztofa do gen. Janusza, Polish War Office London, 19.X.1944",
        "category": "document",
        "medium": "karta pocztowa jeniecka, rekopis, stemple cenzury",
        "date_created": "19 pazdziernika 1944",
        "description": (
            "Karta pocztowa jeniecka wyslana przez Krzysztofa Gluchowskiego ze Stalagu XI B, "
            "adresowana do generala Janusza Gluchowskiego w Polish War Office w Londynie. Datowana "
            "19 pazdziernika 1944. Stemple: Stalag XI B, PASSED T.150 (cenzura brytyjska), "
            "Polish Post Office. Krzysztof informuje o smierci Stryja Lecha. Jest to jedyny znany "
            "dokument laczacy jenca wojennego z polskim generalem w Londynie. Droga pocztowa -- "
            "przez niemiecki system obozowy, cenzure aliancka i polska poczte polowa -- swiadczy "
            "o funkcjonowaniu kanalow komunikacji miedzy niewola a wolnym swiatem. Dokument "
            "o wyjatkowej wartosci dla badan nad polskim wychodzstwem wojennym."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "good",
        "condition_notes": "Stemple czytelne: Stalag XI B, PASSED T.150, Polish Post Office",
        "notes": "Seria 29z(M). Jedyny dok. jeniec-general Londyn. Estymacja: 8,000--20,000 PLN.",
        "authentication_status": "verified",
    },

    # ================================================================
    # 29z(N) -- Ruckantwortbrief Stefana
    # ================================================================
    {
        "inventory_number": "GL-105",
        "title": "Ruckantwortbrief Stefana do Krzysztofa, Stalag XIB -> VIJ, 8.XI.1944",
        "category": "document",
        "medium": "karta pocztowa jeniecka, formularz drukowany, rekopis",
        "date_created": "8 listopada 1944",
        "description": (
            "List zwrotny (Ruckantwortbrief) od Stefana Gluchowskiego do syna Krzysztofa, wyslany "
            "ze Stalagu XI B do Stalagu VI J, datowany 8 listopada 1944 (stempel 13 grudnia 1944). "
            "Stefan zwraca sie do syna slowem 'Synnu' -- intymny zwrot ojcowski. Przekazuje tragiczna "
            "wiadomosc o smierci Babci 29 wrzesnia podczas ewakuacji Zoliborza. Babcia zostala "
            "pochowana w ogrodku willi pani Maciejskiej. Roznica miedzy data listu (8.XI) a stemplem "
            "(13.XII) wskazuje na miesieczne opoznienia w poczcie jenieckiej. Dokument dokumentuje "
            "zarowno straty cywilne Powstania, jak i emocjonalna wiez ojca z synem w niewoli."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "good",
        "condition_notes": "Formularz kompletny, stemple i pismo czytelne",
        "notes": "Seria 29z(N). Smierc Babci 29.IX, ewakuacja Zoliborza. Estymacja: 5,000--12,000 PLN.",
        "authentication_status": "verified",
    },

    # ================================================================
    # 29z(O) -- Kriegsgefangenenpost z Dorsten
    # ================================================================
    {
        "inventory_number": "GL-106",
        "title": "Kriegsgefangenenpost Krzysztofa do ojca, Dorsten -> XIB, 30.X.1944",
        "category": "document",
        "medium": "formularz jeniecki niemiecko-francuski, rekopis",
        "date_created": "30 pazdziernika 1944",
        "description": (
            "Formularz jeniecki niemiecko-francuski (Kriegsgefangenenpost) wyslany przez Krzysztofa "
            "z Dorsten do Stalagu XI B, datowany 30 pazdziernika 1944. Zaczyna sie slowami "
            "'Kochany Tatusiu!' List opisuje pierwsze dni Krzysztofa w Stalagu VI J, gdzie znalazl "
            "sie wsrod mlodszych jencow. Stefan jest ojcem Krzysztofa. Dwujezyczny formularz "
            "(niemiecko-francuski) byl standardem w korespondencji jenieckiej, wymuszonym przez "
            "konwencje genewska. Dokument pozwala datowac transfer Krzysztofa do systemu obozowego "
            "w Westfalii na przelom pazdziernika i listopada 1944."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "fair",
        "condition_notes": "Formularz zachowany, pismo odreczne czytelne",
        "notes": "Seria 29z(O). Pierwsze dni w VIJ, wsrod mlodszych. Estymacja: 4,000--10,000 PLN.",
        "authentication_status": "verified",
    },

    # ================================================================
    # 29z(P) -- Trzy fotografie dokumentacyjne
    # ================================================================
    {
        "inventory_number": "GL-107",
        "title": "Trzy fotografie dokumentacyjne terenu bylego Stalagu, ok. 1955-1965",
        "category": "photograph",
        "medium": "odbitki fotograficzne czarno-biale, 6x9 cm",
        "date_created": "ok. 1955-1965",
        "description": (
            "Trzy czarno-biale fotografie formatu 6x9 cm, przedstawiajace teren bylego stalagu "
            "w okresie powojennym, okolo 1955-1965. Widoczna architektura barakowa typowa dla "
            "niemieckich obozow jenieckich. Na jednym ze zdjec widoczny Volkswagen Garbus (Kaefer), "
            "co pozwala datowac fotografie na lata 50. lub 60. Zdjecia stanowia swiadectwo powrotu "
            "bylego jenca do miejsca traumy -- praktyka znana w psychologii jako 'revisiting'. "
            "Dokumentacja fotograficzna bylych obozow z tego okresu jest rzadka, poniewaz wiekszosc "
            "barakow zostala rozebrana lub przebudowana. Fotografie maja wartosc zarowno historyczna, "
            "jak i psychologiczna."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "good",
        "condition_notes": "Odbitki czarno-biale w dobrym stanie, obraz ostry",
        "notes": "Seria 29z(P). Powrot do miejsc traumy. VW Garbus datuje na lata 50./60. Estymacja: 800--2,500 PLN.",
        "authentication_status": "verified",
    },

    # ================================================================
    # 29z(Q) -- Fotokopia listu Stefana
    # ================================================================
    {
        "inventory_number": "GL-108",
        "title": "Fotokopia Kriegsgefangenenpost Stefana do Zofii Okuszkowej, 20.XI.1944",
        "category": "document",
        "medium": "fotokopia, papier",
        "date_created": "20 listopada 1944 (fotokopia pozniejsza)",
        "description": (
            "Fotokopia karty pocztowej jenieckiej Stefana Gluchowskiego do Zofii Okuszkowej, "
            "datowanej 20 listopada 1944. Stefan rekonstruuje pelna chronologie wydarzen: on i Krzysztof "
            "wyszli ze Srodmiescia (z apteki), byli razem do 11 pazdziernika. Wspomniana jest zona "
            "Wandzia, ktora pozostala w Warszawie. List stanowi centrum narracyjne calej serii 29z -- "
            "laczy watki rodzinne, wojskowe i topograficzne w spojny obraz. Mimo ze jest to fotokopia, "
            "a nie oryginal, dokument zachowuje pelna wartosc informacyjna jako kluczowe zrodlo "
            "do rekonstrukcji losow rodziny Gluchowskich w ostatnich tygodniach Powstania."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "fair",
        "condition_notes": "Fotokopia, nie oryginal -- tekst czytelny",
        "notes": "Seria 29z(Q). Centrum narracyjne serii. Chronologia: apteka, razem do 11.X. Estymacja: 800--2,000 PLN.",
        "authentication_status": "photocopy",
    },

    # ================================================================
    # 29z(R) -- Kalendarz kampanii wloskiej
    # ================================================================
    {
        "inventory_number": "GL-109",
        "title": "Kalendarz kampanii wloskiej z trasa 7 P.Ul., wiosna-lato 1945",
        "category": "document",
        "medium": "kartka z siatka kalendarza, rekopis",
        "date_created": "1945",
        "description": (
            "Kartka z odreczna siatka kalendarza dokumentujaca trase kampanii wloskiej 7 Pulku "
            "Ulanow Lubelskich wiosna i latem 1945 roku. Trasa obejmuje: St. Remo -> Genova -> "
            "Forli -> 7 P.Ul. Na rewersie notatka: 'Maryska Gluchowska'. Kalendarz stanowi rzadki "
            "przyklad zolnierskiej dokumentacji trasy marszu -- nie oficjalny dziennik bojowy, "
            "lecz prywatna notatka. Trasa potwierdza udzial 7 Pulku Ulanow w kampanii wloskiej "
            "2 Korpusu Polskiego gen. Andersa. Wzmianka o Marysce Gluchowskiej na rewersie "
            "laczy dokument z archiwum rodzinnym."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "fair",
        "condition_notes": "Kartka z zapiskami, pismo odreczne czytelne",
        "notes": "Seria 29z(R). Trasa kampanii wloskiej 7 P.Ul. Rewers: Maryska Gluchowska. Estymacja: 1,500--4,000 PLN.",
        "authentication_status": "verified",
    },

    # ================================================================
    # 29z(S) -- Gesundheitsblatt karta zdrowia
    # ================================================================
    {
        "inventory_number": "GL-110",
        "title": "Gesundheitsblatt -- karta zdrowia jenca, M.-Stammlager VI J, 1944-1945",
        "category": "document",
        "medium": "formularz czterostronicowy, papier szarozielony, rekopis",
        "date_created": "1944-1945",
        "description": (
            "Czterostronicowy formularz karty zdrowia jenca (Gesundheitsblatt) z M.-Stammlager VI J. "
            "Papier szarozielony, typowy dla dokumentacji medycznej obozow jenieckich. Formularz "
            "zawiera rubryki dotyczace zachorowan, szczepien i odwszawiania. Karta zdrowia jenca "
            "byla wymagana przez konwencje genewska i prowadzona przez obozowa sluzbe medyczna. "
            "Dokument swiadczy o warunkach sanitarnych w Stalagu VI J i stanowi rzadki przyklad "
            "zachowanej dokumentacji medycznej z niemieckiego obozu jenieckiego. Szarozielony kolor "
            "papieru jest charakterystyczny dla formularzy wehrmachtowych z lat 1944-1945."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "good",
        "condition_notes": "Formularz czterostronicowy kompletny, papier szarozielony, wpisy czytelne",
        "notes": "Seria 29z(S). Karta zdrowia jenca: zachorowania, szczepienia, odwszawianie. Estymacja: 1,200--3,000 PLN.",
        "authentication_status": "verified",
    },

    # ================================================================
    # 29z(T) -- PAMIETNIK OBOZOWY -- NAJCENNIEJSZY DOKUMENT
    # ================================================================
    {
        "inventory_number": "GL-111",
        "title": "Pamietnik obozowy Krzysztofa, Stalag VIJ / Gladbach, grudzien 1944",
        "category": "document",
        "medium": "rekopis, 15 kart, olowek i atrament",
        "date_created": "grudzien 1944",
        "description": (
            "Oryginalny pamietnik rekopismienny Krzysztofa Gluchowskiego, liczacy 15 kart, pisany "
            "w Stalagu VI J / Gladbach w grudniu 1944 roku. Autor identyfikuje sie slowami: "
            "'gdwzich ktory mozwa sie 141009 -- to ja' -- uzywa numeru jenieckiego jako tozsamosci. "
            "Pamietnik opisuje codzienne zycie obozowe, bombardowania i warunki bytowe. Jest to "
            "najcenniejszy dokument w calej serii 29z -- bezposrednie swiadectwo 15-letniego jenca "
            "wojennego. Pamietniki obozowe pisane przez nastolatkow sa niezwykle rzadkie w zbiorach "
            "muzealnych. Dokument ma wartosc porownywalna z pamietnikami z Auschwitz czy Ravensbrueck, "
            "jako bezposrednie swiadectwo doswiadczenia obozowego."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "good",
        "condition_notes": "15 kart rekopiSmiennych, pismo czytelne, papier zuzyty ale kompletny",
        "notes": "Seria 29z(T). NAJCENNIEJSZY DOK W SERII. Nr 141009. Estymacja: 20,000--50,000 PLN.",
        "authentication_status": "verified",
    },

    # ================================================================
    # 29z(U) -- List wigilijny
    # ================================================================
    {
        "inventory_number": "GL-112",
        "title": "List wigilijny na zeszycie IHK Gladbach, 24.XII.1944",
        "category": "document",
        "medium": "zeszyt egzaminacyjny IHK Gladbach-Rheydt-Neuss, rekopis",
        "date_created": "24 grudnia 1944",
        "description": (
            "List do Matki pisany w Wigilie Bozego Narodzenia 1944 roku, na zeszycie egzaminacyjnym "
            "Kaufmannsgehilfenpruefung IHK Gladbach-Rheydt-Neuss. Ironia historyczna: 15-letni jeniec "
            "wojenny pisze list na papierze instytucji, ktora go wiezi. Zeszyt egzaminacyjny "
            "Izby Przemyslowo-Handlowej (IHK) byl przeznaczony do egzaminow na pomocnika kupieckiego "
            "-- a zostal uzyty przez polskiego nastolanka do listu do matki. Dokument laczy watek "
            "emocjonalny (Wigilia w niewoli) z materialnym (papier wroga jako nosnik pamieci). "
            "Jest to jedno z najbardziej poruszajacych swiadectw w calej kolekcji Gluchowskich."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "good",
        "condition_notes": "Zeszyt egzaminacyjny z nadrukiem IHK, rekopis czytelny",
        "notes": "Seria 29z(U). Wigilia 1944 w niewoli. Papier IHK Gladbach. Estymacja: 5,000--15,000 PLN.",
        "authentication_status": "verified",
    },

    # ================================================================
    # 29z(V) -- List/notatka z planem taktycznym Mokotowa
    # ================================================================
    {
        "inventory_number": "GL-113",
        "title": "List/notatka z planem taktycznym Mokotowa, 22.VIII.1945",
        "category": "document",
        "medium": "zeszyt IHK Gladbach, rekopis, szkic odreczny",
        "date_created": "22 sierpnia 1945",
        "description": (
            "Notatka na zeszycie IHK Gladbach zawierajaca wspomnienia z walk na Mokotowie, "
            "datowana 22 sierpnia 1945 -- rok po wydarzeniach. Zawiera odreczny szkic taktyczny "
            "pozycji bojowych. 16-letni byly jeniec rekonstruuje z pamieci pozycje bojowe "
            "i przebieg walk. Plan taktyczny rysowany z pamieci przez nastolanka ma szczegolna "
            "wartosc -- jest jednoczesnie dokumentem wojskowym i psychologicznym swiadectwem "
            "traumy. Uzycie tego samego zeszytu IHK co w liscie wigilijnym (GL-112) laczy "
            "oba dokumenty materialnie. Szkic moze stanowic cenne uzupelnienie map bojowych "
            "Powstania Warszawskiego."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "good",
        "condition_notes": "Zeszyt IHK z rekopisem i szkicem, pismo i rysunek czytelne",
        "notes": "Seria 29z(V). Szkic taktyczny Mokotowa z pamieci. Na zeszycie IHK. Estymacja: 3,000--8,000 PLN.",
        "authentication_status": "verified",
    },

    # ================================================================
    # 29z(W) -- Wspomnienie posmiertne o Lechu
    # ================================================================
    {
        "inventory_number": "GL-114",
        "title": "Wspomnienie posmiertne 'Stryj' o Lechu Gluchowskim, 1945",
        "category": "document",
        "medium": "rekopis, dwie strony",
        "date_created": "1945",
        "description": (
            "Dwustronicowe wspomnienie posmiertne zatytulowane 'Stryj', poswiecone Lechowi "
            "Gluchowskiemu. Autor opisuje wplyw Lecha od 1934 roku, jego udzial w kampanii "
            "wrzesniowej 1939, dzialalnosc konspiracyjna i prace w ogrodzie zoologicznym. "
            "Jest to jedyne znane swiadectwo o zyciu i smierci Lecha Gluchowskiego. "
            "Tekst napisany z perspektywy bratanka, ktory widzial w Lechu wzor do nasladowania. "
            "Wzmianka o ogrodzie zoologicznym jako miejscu konspiracji AK jest istotna "
            "dla badan nad topografia konspiracji w Warszawie. Dokument wypelnia luke "
            "w wiedzy o jednym z czlonkow rodziny Gluchowskich."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "good",
        "condition_notes": "Dwie strony rekopisu, pismo czytelne",
        "notes": "Seria 29z(W). Jedyne swiadectwo o Lechu. Ogrod zoologiczny = konspiracja. Estymacja: 3,000--8,000 PLN.",
        "authentication_status": "verified",
    },

    # ================================================================
    # 29z(X) -- List z Dusseldorfu
    # ================================================================
    {
        "inventory_number": "GL-115",
        "title": "List z Dusseldorfu 'Zawsze humour', papier firmowy Emil Schroder & Co., 25.V.1945",
        "category": "document",
        "medium": "papier firmowy fabryki lakierow, rekopis",
        "date_created": "25 maja 1945",
        "description": (
            "List pisany na papierze firmowym fabryki lakierow Emil Schroder & Co. w Dusseldorfie, "
            "datowany 25 maja 1945 -- trzy tygodnie po zakonczeniu wojny w Europie. Tytul lub "
            "motto: 'Zawsze humour'. Autor wspomina o ranie w noge. Wzmianka o Bogdanie laczy "
            "list z siecia kontaktow Krzysztofa po wyzwoleniu. Dokument stanowi most miedzy "
            "seria jeniecka a okresem powrotu do wolnosci. Uzycie papieru firmowego niemieckiej "
            "fabryki jest typowe dla korespondencji wyzwolonych jencow, ktorzy korzystali "
            "z dostepnych materialow piSmiennych. Ton 'Zawsze humour' swiadczy o resilience "
            "mlodego autora."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "good",
        "condition_notes": "Papier firmowy Emil Schroder & Co., rekopis czytelny",
        "notes": "Seria 29z(X). Most miedzy niewola a wolnoscia. Rana w noge. Estymacja: 3,000--8,000 PLN.",
        "authentication_status": "verified",
    },

    # ================================================================
    # 29z(Y) -- Sprawozdanie wojenne -- DOKUMENT-KLUCZ
    # ================================================================
    {
        "inventory_number": "GL-116",
        "title": "Sprawozdanie wojenne rodziny Gluchowskich, Dusseldorf, 2.VI.1945",
        "category": "document",
        "medium": "rekopis, kilka stron",
        "date_created": "2 czerwca 1945",
        "description": (
            "Kompletne sprawozdanie wojenne rodziny Gluchowskich, datowane na Dusseldorf, "
            "2 czerwca 1945. Dokument opisuje udzial calej rodziny w konspiracji. Matka zostala "
            "ranna 27 wrzesnia 1943 roku. Krzysztof sluzyl przy Kwaterze Glownej generala Bora "
            "(Komorowskiego). Sprawozdanie jest dokumentem-kluczem calej kolekcji -- laczy "
            "wszystkie watki rodzinne w spojny obraz: konspiracja, Powstanie, niewola, straty. "
            "Fakt, ze 16-latek sluzyl przy Kwaterze Glownej dowodcy Powstania, jest dotad "
            "niebadany. Dokument ma wartosc kluczowa dla rekonstrukcji udzialu rodziny "
            "Gluchowskich w konspiracji i Powstaniu."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "good",
        "condition_notes": "Rekopis wielostronicowy, pismo czytelne, papier w dobrym stanie",
        "notes": "Seria 29z(Y). DOKUMENT-KLUCZ calej kolekcji. KG gen. Bora. Matka ranna 27.IX.1943. Estymacja: 15,000--35,000 PLN.",
        "authentication_status": "verified",
    },

    # ================================================================
    # 29z(Z) -- Ciag dalszy sprawozdania
    # ================================================================
    {
        "inventory_number": "GL-117",
        "title": "Ciag dalszy sprawozdania -- smierc Lecha i rana w Gladbach, 2-3.VI.1945",
        "category": "document",
        "medium": "papier firmowy Emil Schroder, rekopis",
        "date_created": "2-3 czerwca 1945",
        "description": (
            "Kontynuacja sprawozdania wojennego, pisana na papierze firmowym Emil Schroder & Co. "
            "Opisuje smierc Stryja Lecha od artylerii -- cialo pozostalo niepochowane. Ojciec Stefan "
            "przebyl Pawiak. 1 lutego 1945 roku Krzysztof zostal ranny w nalocie lotniczym "
            "w Gladbach. General (Janusz Gluchowski) przebywal w Edynburgu w czerwcu 1945. "
            "Dokument laczy trzy pokolenia rodziny: general w Szkocji, ojciec po Pawiaku, "
            "syn ranny w obozie. Wzmianka o niepochowanym ciele Lecha jest jednym "
            "z najbardziej wstrzasajacych fragmentow calej korespondencji."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "good",
        "condition_notes": "Papier firmowy Emil Schroder, rekopis czytelny",
        "notes": "Seria 29z(Z). Smierc Lecha, Pawiak, rana 1.II.1945, general w Edynburgu. Estymacja: 12,000--30,000 PLN.",
        "authentication_status": "verified",
    },

    # ================================================================
    # 29z(Z2) -- Druk urzedowy "Rodacy!"
    # ================================================================
    {
        "inventory_number": "GL-118",
        "title": "Druk urzedowy 'Rodacy!' -- Rzad RP, Oddzial na France, 1945",
        "category": "document",
        "medium": "druk urzedowy, papier, notatka odreczna na marginesie",
        "date_created": "1945",
        "description": (
            "Proklamacja Rzadu RP, Oddzial na France, adresowana do wyzwolonych jencow wojennych. "
            "Naglowek: 'Rodacy!' Na rewersie katalog polskich placowek we Francji. Na marginesie "
            "odreczna notatka Krzysztofa o rane w noge. Druk jest swiadectwem funkcjonowania "
            "polskich struktur panstwowych na emigracji i ich wyslikow w kierunku opieki "
            "nad wyzwolonymi jenkami. Katalog placowek na rewersie ma wartosc dokumentacyjna "
            "dla badan nad polska diaspora we Francji w 1945 roku. Notatka Krzysztofa "
            "personalizuje dokument urzedowy."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "good",
        "condition_notes": "Druk urzedowy w dobrym stanie, notatka odreczna na marginesie",
        "notes": "Seria 29z(Z2). Proklamacja do jencow. Katalog placowek we Francji. Estymacja: 1,500--4,000 PLN.",
        "authentication_status": "verified",
    },

    # ================================================================
    # 29z(Z3) -- Card of Identity
    # ================================================================
    {
        "inventory_number": "GL-119",
        "title": "Card of Identity, Dusseldorf-Gerresheim, 25.IV.1945",
        "category": "document",
        "medium": "karta tozsamosci dwujezyczna, papier, pieczecie",
        "date_created": "25 kwietnia 1945",
        "description": (
            "Dwujezyczna karta tozsamosci wystawiona w Dusseldorf-Gerresheim 25 kwietnia 1945. "
            "Podpisana przez Lt. Hofmana Jerzego, polskiego lekarza naczelnego (pol. chief-doctor). "
            "Jest to pierwszy dokument wolnego Krzysztofa -- wystawiony 8 dni po wyzwoleniu. "
            "Karta stanowi symboliczne przejscie od Kennkarte (1943, dokument okupacyjny) "
            "do Card of Identity (1945, dokument wolnosci). Dwujezycznosc dokumentu (polsko-angielska) "
            "odzwierciedla nowa rzeczywistosc: wolnosc pod alianckim parasolem. "
            "Dokument ma szczegolna wartosc jako swiadectwo pierwszych dni wolnosci."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "good",
        "condition_notes": "Karta dwujezyczna w dobrym stanie, pieczecie i podpisy czytelne",
        "notes": "Seria 29z(Z3). Pierwszy dokument wolnego Krzysztofa. Kennkarte->Card of Identity. Estymacja: 5,000--12,000 PLN.",
        "authentication_status": "verified",
    },

    # ================================================================
    # 29z(Z4) -- Trzy ephemery repatriacyjne
    # ================================================================
    {
        "inventory_number": "GL-120",
        "title": "Trzy ephemery repatriacyjne, Paryz/Troyes, 1945",
        "category": "document",
        "medium": "kartki, wizytowka, rysunek olowkiem",
        "date_created": "1945",
        "description": (
            "Zestaw trzech ephemer repatriacyjnych z 1945 roku: kartka z adresami centrum "
            "repatriacyjnego w Paryzu, wizytowka Henriego Kolacza z Troyes z rysunkiem orla, "
            "oraz kartka z adresami polskimi. Rysunek orla na wizytowce jest jedyna znana "
            "praca plastyczna Krzysztofa Gluchowskiego. Ephemery dokumentuja trase repatriacyjna "
            "przez Francje i siec kontaktow polskiej diaspory. Wizytowka Henriego Kolacza "
            "z Troyes wskazuje na polsko-francuskie kontakty w okresie repatriacji. "
            "Zestaw ma wartosc jako dokumentacja codziennosci repatrianta."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "fair",
        "condition_notes": "Trzy luczne elementy, papier zuzyty, rysunek orla czytelny",
        "notes": "Seria 29z(Z4). Jedyna praca plastyczna Krzysztofa (rysunek orla). Estymacja: 1,200--3,000 PLN.",
        "authentication_status": "verified",
    },

    # ================================================================
    # 29z(Z5) -- Carte de Rapatrie
    # ================================================================
    {
        "inventory_number": "GL-121",
        "title": "Carte de Rapatrie Krzysztofa, Centre d'Orsay, 27.VI.1945",
        "category": "document",
        "medium": "formularz urzedowy francuski, papier, odciski palcow",
        "date_created": "27 czerwca 1945",
        "description": (
            "Karta repatriacyjna (Carte de Rapatrie) wystawiona w Centre d'Orsay, numer 1492839, "
            "datowana 27 czerwca 1945. Zawiera obserwacje medyczna: 'pied gauche' (lewa noga) -- "
            "slad rany odniesionej w Gladbach. Na karcie odciski palcow Krzysztofa. Jest to czwarty "
            "znany wariant sfalszowanej daty urodzenia Krzysztofa -- praktyka powszechna wsrod "
            "mlodocianych zolnierzy, ktorzy zawyzan wiek aby sluzyc. Dokument Centre d'Orsay "
            "jest wazny dla badan nad francuskim systemem repatriacyjnym 1945 roku. "
            "Odciski palcow sa rzadkim elementem biometrycznym w dokumentach z tego okresu."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "good",
        "condition_notes": "Formularz kompletny, odciski palcow widoczne, pieczecie czytelne",
        "notes": "Seria 29z(Z5). Nr 1492839. Pied gauche. Czwarty wariant daty urodzenia. Estymacja: 4,000--10,000 PLN.",
        "authentication_status": "verified",
    },

    # ================================================================
    # 29z(Z6) -- Zaswiadczenie AK w Paryzu
    # ================================================================
    {
        "inventory_number": "GL-122",
        "title": "Zaswiadczenie AK, Komenda Uzupelnien Nr 11, Paryz, 27.VI.1945",
        "category": "document",
        "medium": "dokument urzedowy, papier, pieczecie, podpisy",
        "date_created": "27 czerwca 1945",
        "description": (
            "Zaswiadczenie wystawione przez Komende Uzupelnien Nr 11 Armii Krajowej w Paryzu, "
            "datowane 27 czerwca 1945. Podpisy: ppor. Radomyski i ppor. Milczynski. Pieczec "
            "ppplk. Hoffauera. Krzysztof legalizuje jednoczesnie swoja tozsamosc wobec Francji "
            "i wobec struktur AK -- podwojne uwiarygodnienie. Istnienie Komendy Uzupelnien AK "
            "w Paryzu w czerwcu 1945 jest swiadectwem funkcjonowania polskich struktur wojskowych "
            "na emigracji. Dokument ma wartosc dla badan nad polska administracja wojskowa "
            "we Francji po zakonczeniu dzialan wojennych."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "good",
        "condition_notes": "Dokument z pieczeciami i podpisami, papier w dobrym stanie",
        "notes": "Seria 29z(Z6). AK Paryz. Ppor. Radomyski, ppor. Milczynski, ppplk. Hoffauer. Estymacja: 6,000--15,000 PLN.",
        "authentication_status": "verified",
    },

    # ================================================================
    # 29z(Z7) -- Fiche de Transport
    # ================================================================
    {
        "inventory_number": "GL-123",
        "title": "Fiche de Transport, Centre d'Orsay -> Caserne Bessieres, 27.VI.1945",
        "category": "document",
        "medium": "formularz transportowy francuski, papier",
        "date_created": "27 czerwca 1945",
        "description": (
            "Karta transportowa (Fiche de Transport) z Centre d'Orsay do Caserne Bessieres, "
            "numer 1492839 (ten sam co Carte de Rapatrie GL-121). Datowana 27 czerwca 1945. "
            "Caserne Bessieres w Paryzu byla centrum mobilizacyjnym Polskich Sil Zbrojnych "
            "na Zachodzie. Krzysztof zostal skierowany do wojska, nie do domu -- 16-letni "
            "repatriant kontynuuje sluzbe zamiast wracac do cywila. Dokument swiadczy "
            "o polityce PSZ wobec mlodocianych zolnierzy AK po wyzwoleniu. "
            "Trasa Centre d'Orsay -> Caserne Bessieres jest typowa dla repatriacji wojskowej."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "good",
        "condition_notes": "Formularz transportowy kompletny, stemple czytelne",
        "notes": "Seria 29z(Z7). Nr 1492839. Caserne Bessieres = centrum PSZ. Do wojska, nie do domu. Estymacja: 2,000--5,000 PLN.",
        "authentication_status": "verified",
    },

    # ================================================================
    # 29z(Z8) -- List ppor. Radomyskiego
    # ================================================================
    {
        "inventory_number": "GL-124",
        "title": "List ppor. Radomyskiego do Krzysztofa, Caserne Bessieres, VII.1945",
        "category": "document",
        "medium": "list odreczny, papier",
        "date_created": "lipiec 1945",
        "description": (
            "List ppor. Radomyskiego do Krzysztofa Gluchowskiego, pisany z Caserne Bessieres "
            "w lipcu 1945. Radomyski przekazuje wiadomosc o ojcu Stefanie, ktory przebywa "
            "w Lubece. Kluczowe zdanie: 'Jestem mi naprawde blizszy niz brat' -- swiadectwo "
            "glebokiej wiezy miedzy oficerem AK a mlodym zolnierzem. Ten sam Radomyski "
            "podpisal zaswiadczenie AK (GL-122), co potwierdza ciaglosc relacji. "
            "List dokumentuje siec kontaktow polskich wojskowych rozrzuconych po Europie "
            "w pierwszych miesiach po wojnie: Krzysztof w Paryzu, Stefan w Lubece, "
            "Radomyski w Caserne Bessieres."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "good",
        "condition_notes": "List odreczny, pismo czytelne, papier w dobrym stanie",
        "notes": "Seria 29z(Z8). Radomyski: 'blizszy niz brat'. Ojciec Stefan w Lubece. Estymacja: 3,000--8,000 PLN.",
        "authentication_status": "verified",
    },

    # ================================================================
    # 29z(Z9) -- Skierowanie na kurs Villard-de-Lans
    # ================================================================
    {
        "inventory_number": "GL-125",
        "title": "Skierowanie Ambasady RP na kurs, Villard-de-Lans, 29.VI.1945",
        "category": "document",
        "medium": "pismo urzedowe Ambasady RP, papier, pieczec",
        "date_created": "29 czerwca 1945",
        "description": (
            "Pismo Ambassade de Pologne a Paris (Ambasady RP w Paryzu) kierujace Krzysztofa "
            "na kurs do Villard-de-Lans, datowane 29 czerwca 1945. Podpis: A. Dragowski, "
            "Naczelny Instruktor Odzwiatowy. 16-letni bylym jeniec wojenny zostaje skierowany "
            "do szkoly -- symboliczne przejscie od wojny do edukacji. Villard-de-Lans "
            "w Alpach francuskich bylo miejscem polskich osrodkow szkoleniowych. "
            "Dokument swiadczy o wysiklach polskiej dyplomacji w zakresie edukacji "
            "mlodych repatriantow. Naczelny Instruktor Odzwiatowy to stanowisko "
            "zwiazane z polska oswita na emigracji."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "good",
        "condition_notes": "Pismo urzedowe Ambasady RP, pieczec i podpis czytelne",
        "notes": "Seria 29z(Z9). Ambasada RP Paryz. 16-letni jeniec idzie do szkoly. Estymacja: 3,000--8,000 PLN.",
        "authentication_status": "verified",
    },

    # ================================================================
    # 29z(Z10) -- Plan Marsylii
    # ================================================================
    {
        "inventory_number": "GL-126",
        "title": "Plan Marsylii z notka Krzysztofa, 1945",
        "category": "document",
        "medium": "plan miasta drukowany, notatka odreczna",
        "date_created": "1945",
        "description": (
            "Plan miasta Marsylii z odreczna notka Krzysztofa: 'Znalazlem plan... na wszelki "
            "wypadek.' Na rewersie plan ulic z zaznaczona trasa: Dworzec -> Canebiere -> "
            "Hotel Scribe. Notatka swiadczy o instynkcie archiwisty -- Krzysztof zachowuje "
            "dokumenty 'na wszelki wypadek', co tlumaczy kompletnosc calego archiwum. "
            "Trasa Dworzec-Canebiere-Hotel Scribe dokumentuje pobyt w Marsylii w drodze "
            "do Wloch. Instynkt straznika archiwum widoczny juz u 16-latka jest kluczem "
            "do zrozumienia, dlaczego ta kolekcja przetrwala do 2020 roku."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "fair",
        "condition_notes": "Plan miasta zuzyty, notatka odreczna czytelna",
        "notes": "Seria 29z(Z10). Instynkt archiwisty juz w 1945. 'Na wszelki wypadek.' Estymacja: 800--2,000 PLN.",
        "authentication_status": "verified",
    },

    # ================================================================
    # 29z(Z11) -- Skierowanie na rentgen pluc
    # ================================================================
    {
        "inventory_number": "GL-127",
        "title": "Skierowanie na rentgen pluc, 7 Pulk Ulanow Lubelskich, 22-23.VII.1945",
        "category": "document",
        "medium": "papier firmowy 7 P.Ul., rekopis/maszynopis",
        "date_created": "22-23 lipca 1945",
        "description": (
            "Skierowanie na rentgen pluc wystawione na papierze firmowym 7 Pulku Ulanow "
            "Lubelskich im. Gen. K. Sosnkowskiego, datowane 22-23 lipca 1945. Rozpoznanie: "
            "Susp. g. Plc. Pulmonum -- podejrzenie gruzlicy pluc. Krzysztof sluzy teraz "
            "w pulku, ktorego tradycje kontynuowal 7 Pulk Ulanow AK 'Jelen'. General "
            "Sosnkowski, patron pulku, byl tym samym generalem, ktory dowodzil pulkiem "
            "od 1919 roku. Podejrzenie gruzlicy bylo czestym nastepstwem pobytu w obozach "
            "jenieckich. Dokument zamyka kolo: od Powstania przez stalag do pulku generala."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "good",
        "condition_notes": "Papier firmowy 7 P.Ul., tekst czytelny",
        "notes": "Seria 29z(Z11). 7 P.Ul. im. Sosnkowskiego. Podejrzenie gruzlicy. Estymacja: 3,000--8,000 PLN.",
        "authentication_status": "verified",
    },

    # ================================================================
    # 29z(Z12) -- Przepustka Gimnazjum 3 DSK
    # ================================================================
    {
        "inventory_number": "GL-128",
        "title": "Przepustka Gimnazjum i Liceum 3 DSK, Amandola (Wlochy), 1945",
        "category": "document",
        "medium": "przepustka polsko-angielska, papier, pieczec",
        "date_created": "1945",
        "description": (
            "Przepustka polsko-angielska wystawiona przez Gimnazjum i Liceum 3 Dywizji Strzelkow "
            "Karpackich w Amandoli (Wlochy), 1945. Wystawiona na: St. ul. Gluchowski Krzysztof, "
            "numer ewidencyjny 1926. Podpis: kpt. Kapica Jozef, Komendant Gimnazjum. "
            "Dwujezycznosc dokumentu (polsko-angielska) odzwierciedla warunki funkcjonowania "
            "polskiej oswiaty pod aliancka administracja we Wloszech. 3 DSK prowadzila "
            "gimnazja i licea dla mlodych zolnierzy, umozliwiajac im kontynuowanie nauki. "
            "Kapitan Kapica pojawia sie takze w swiadectwie ukonczenia (GL-135)."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "good",
        "condition_notes": "Przepustka dwujezyczna, pieczec i podpis czytelne",
        "notes": "Seria 29z(Z12). Gimnazjum 3 DSK Amandola. Kpt. Kapica. Nr ewid. 1926. Estymacja: 2,000--5,000 PLN.",
        "authentication_status": "verified",
    },

    # ================================================================
    # 29z(Z13) -- Przepustka Punktu Przesylkowego Jencow
    # ================================================================
    {
        "inventory_number": "GL-129",
        "title": "Przepustka Punktu Przesylkowego Jencow 2 Korpusu PSZ, VII.1945",
        "category": "document",
        "medium": "przepustka, papier, pieczec",
        "date_created": "lipiec 1945",
        "description": (
            "Przepustka wystawiona przez Punkt Przesylkowy Jencow 2 Korpusu Polskich Sil "
            "Zbrojnych, lipiec 1945. Podpis: ppor. Kucharski, Komendant P.P.J. Dokument "
            "tranzytowy miedzy statusem jenca wojennego a zolnierzem PSZ. Jest to czwarta "
            "przepustka w zyciu Krzysztofa -- kazda z innej fazy: konspiracja, niewola, "
            "repatriacja, sluzba. Punkt Przesylkowy Jencow 2 Korpusu zajmowal sie "
            "przyjmowaniem bylych jencow i wlaczaniem ich w struktury PSZ. "
            "Dokument ma wartosc dla badan nad procesem reintegracji jencow wojennych."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "good",
        "condition_notes": "Przepustka w dobrym stanie, pieczec i podpis czytelne",
        "notes": "Seria 29z(Z13). Ppor. Kucharski. Czwarta przepustka w zyciu. Tranzyt jeniec->zolnierz PSZ. Estymacja: 2,000--5,000 PLN.",
        "authentication_status": "verified",
    },

    # ================================================================
    # 29z(Z14) -- ZESZYT SZKOLNY -- Powstanie jako zadanie szkolne
    # ================================================================
    {
        "inventory_number": "GL-130",
        "title": "Zeszyt szkolny Gimnazjum 3 DSK, Amandola, VIII-XI 1945",
        "category": "document",
        "medium": "Exercise Book His Majesty's Stationery Office, rekopis",
        "date_created": "sierpien-listopad 1945",
        "description": (
            "Zeszyt szkolny (Exercise Book His Majesty's Stationery Office) z Gimnazjum 3 Dywizji "
            "Strzelkow Karpackich w Amandoli, prowadzony od sierpnia do listopada 1945. Zadanie "
            "nr 1: 'Moje najciekawsze przygoda' -- opis pierwszych godzin Powstania Warszawskiego! "
            "16-letni uczen opisuje godzine W i poczatek walk jako 'najciekawsza przygode'. "
            "Powstanie Warszawskie jako zadanie szkolne -- jedyny znany przypadek w literaturze "
            "przedmiotu. Zeszyt brytyjskiego Stationery Office uzywany w polskim gimnazjum "
            "we Wloszech jest sam w sobie swiadectwem wielokulturowej rzeczywistosci PSZ. "
            "Dokument o wyjatkowej wartosci historycznej i edukacyjnej."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "good",
        "condition_notes": "Zeszyt kompletny, rekopis czytelny, okladka zachowana",
        "notes": "Seria 29z(Z14). Powstanie jako zadanie szkolne! Exercise Book HMSO. Estymacja: 15,000--35,000 PLN.",
        "authentication_status": "verified",
    },

    # ================================================================
    # 29z(Z15) -- Esej rocznicowy "Rok temu" (FOTOKOPIA)
    # ================================================================
    {
        "inventory_number": "GL-131",
        "title": "Esej rocznicowy 'Rok temu', 1.VIII.1945 godz. 15:30 (fotokopia)",
        "category": "document",
        "medium": "fotokopia rekopisu",
        "date_created": "1 sierpnia 1945",
        "description": (
            "Fotokopia eseju napisanego w pierwsza rocznice Powstania Warszawskiego, 1 sierpnia "
            "1945 o godzinie 15:30 -- 90 minut przed godzina W (17:00). Esej zatytulowany "
            "'Rok temu' jest najdojrzalsza analiza polityczna w calej serii, napisana przez "
            "16-latka. Autor reflektuje nad przyczynami i skutkami Powstania z perspektywy "
            "roku. Mimo mlodego wieku, analiza wykracza poza osobiste doswiadczenie "
            "i obejmuje kontekst polityczny. Dokument zachowany jedynie jako fotokopia -- "
            "oryginal nieznany. Wartosc informacyjna zachowana w pelni pomimo statusu kopii."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "fair",
        "condition_notes": "Fotokopia, nie oryginal -- tekst czytelny",
        "notes": "Seria 29z(Z15). FOTOKOPIA. Najdojrzalsza analiza polityczna 16-latka. 90 min przed godz. W. Estymacja: 8,000--20,000 PLN.",
        "authentication_status": "photocopy",
    },

    # ================================================================
    # 29z(Z16) -- Esej polemiczny "Czytam artykuly" (FOTOKOPIA)
    # ================================================================
    {
        "inventory_number": "GL-132",
        "title": "Esej polemiczny 'Czytam artykuly', 3.VIII.1945 (fotokopia)",
        "category": "document",
        "medium": "fotokopia rekopisu",
        "date_created": "3 sierpnia 1945",
        "description": (
            "Fotokopia eseju polemicznego datowanego 3 sierpnia 1945, dwa dni po rocznicy "
            "Powstania. Autor polemizuje z artykulem Z. Nowakowskiego. Kluczowa informacja: "
            "Dom Gluchoniemych jako miejsce konspiracji Armii Krajowej -- fakt historyczny "
            "dotad niezbadany. Esej swiadczy o intelektualnej dojrzalosci 16-letniego autora, "
            "ktory podejmuje polemike z uznanym publicysta. Wzmianka o Domu Gluchoniemych "
            "moze stanowic istotne odkrycie dla badan nad topografia konspiracji warszawskiej. "
            "Dokument zachowany jedynie jako fotokopia. Wartosc dokumentacyjna mimo statusu kopii."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "fair",
        "condition_notes": "Fotokopia, nie oryginal -- tekst czytelny",
        "notes": "Seria 29z(Z16). FOTOKOPIA. Dom Gluchoniemych = konspiracja AK. Polemika z Nowakowskim. Estymacja: 5,000--12,000 PLN.",
        "authentication_status": "photocopy",
    },

    # ================================================================
    # 29z(Z17) -- Zaswiadczenia plk. Klepacza
    # ================================================================
    {
        "inventory_number": "GL-133",
        "title": "Dwa zaswiadczenia plk. Klepacza -- KW i awans ps. Juras, 22.VIII.1945",
        "category": "document",
        "medium": "dokumenty urzedowe wojskowe, papier, pieczecie",
        "date_created": "22 sierpnia 1945",
        "description": (
            "Dwa zaswiadczenia wystawione przez plk. Klepacza: nadanie Krzyza Walecznych "
            "oraz awans na starszego ulana, rozkazem Okregu AK Nr 29 z 15 wrzesnia 1944. "
            "Pieczec: Dow. I Zgrupowania Ofic. Pol.Ogr.Wojsk. Lubeck. Pseudonim Krzysztofa "
            "to 'Juras' (nie 'Guras' jak podawano wczesniej). Krzyz Walecznych nadany "
            "rozkazem z 15 wrzesnia 1944 -- w trakcie trwania Powstania -- swiadczy "
            "o wyroznieniu w boju. Korekta pseudonimu z 'Guras' na 'Juras' ma znaczenie "
            "dla badan genealogicznych i ewidencji AK."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "good",
        "condition_notes": "Dwa dokumenty z pieczeciami, podpisy czytelne",
        "notes": "Seria 29z(Z17). KW + awans. Ps. 'Juras' (nie 'Guras'). Rozk. Nr 29, 15.IX.1944. Estymacja: 8,000--20,000 PLN.",
        "authentication_status": "verified",
    },

    # ================================================================
    # 29z(Z18) -- Zaswiadczenie plk. Ziemskiego-Wachnowskiego
    # ================================================================
    {
        "inventory_number": "GL-134",
        "title": "Zaswiadczenie plk. Ziemskiego-Wachnowskiego o KW, Wentorf k. Hamburga, 26.X.1946",
        "category": "document",
        "medium": "dokument urzedowy wojskowy, papier, podpis, pieczec",
        "date_created": "26 pazdziernika 1946",
        "description": (
            "Zaswiadczenie o nadaniu Krzyza Walecznych wystawione przez plk. dypl. Karola "
            "Ziemskiego (Wachnowskiego), bylego Dowodce Grupy Polnoc i Obrony Starego Miasta "
            "w Powstaniu Warszawskim. Datowane na Wentorf kolo Hamburga, 26 pazdziernika 1946. "
            "Krzyz Walecznych nadany rozkazem Nr 24 z 5 wrzesnia 1944. Ten sam Wachnowski "
            "podpisal przepustki bojowe we wrzesniu 1944 -- ciaglosc od rozkazu bojowego "
            "do zaswiadczenia powojennego. Pulkownik Ziemski-Wachnowski jest jedna "
            "z najwazniejszych postaci Powstania -- jego podpis nadaje dokumentowi "
            "wyjatkowa wartosc historyczna."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "very good",
        "condition_notes": "Dokument w bardzo dobrym stanie, podpis Wachnowskiego i pieczec czytelne",
        "notes": "Seria 29z(Z18). Plk. Ziemski-Wachnowski, Dow. Grupy Polnoc. KW rozk. Nr 24, 5.IX.1944. Estymacja: 10,000--25,000 PLN.",
        "authentication_status": "verified",
    },

    # ================================================================
    # 29z(Z19) -- Swiadectwo Ukonczenia Gimnazjum
    # ================================================================
    {
        "inventory_number": "GL-135",
        "title": "Swiadectwo Ukonczenia Gimnazjum Ogolnoksztalcacego, 9.II.1946",
        "category": "document",
        "medium": "swiadectwo szkolne, papier, fotografia, pieczecie",
        "date_created": "9 lutego 1946",
        "description": (
            "Swiadectwo Nr 13 ukonczenia Gimnazjum Ogolnoksztalcacego, wystawione na Krzysztofa "
            "Andrzeja Gluchowskiego, urodzonego w Warszawie. Datowane 9 lutego 1946. Egzaminator: "
            "kpt. Kapica Jozef (ten sam co w przepustce GL-128). Zawiera jedyna znana fotografie "
            "Krzysztofa z podpisem. Dokument zamyka luk biograficzny: od Kennkarte (1943, "
            "dokument okupacyjny) przez Card of Identity (1945, wolnosc) do Swiadectwa (1946, "
            "normalnosc). Jedyna znana fotografia portretowa Krzysztofa ma wyjatkowa wartosc "
            "ikonograficzna dla calej kolekcji."
        ),
        "provenance": PROVENANCE,
        "condition_grade": "very good",
        "condition_notes": "Swiadectwo w bardzo dobrym stanie, fotografia zachowana, pieczecie czytelne",
        "notes": "Seria 29z(Z19). Swiadectwo Nr 13. Jedyna fotografia Krzysztofa z podpisem. Kennkarte->Swiadectwo. Estymacja: 5,000--12,000 PLN.",
        "authentication_status": "verified",
    },
]


# ============================================================
# IMPORT DO BAZY
# ============================================================
print(f"=" * 60)
print(f"IMPORT SERII 29z -- DOKUMENTY KRZYSZTOFA GLUCHOWSKIEGO")
print(f"Obiektow do importu: {len(SERIA_29Z_OBJECTS)}")
print(f"=" * 60)

imported = 0
skipped = 0
errors = 0

for obj in SERIA_29Z_OBJECTS:
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
print(f"  RAZEM:         {len(SERIA_29Z_OBJECTS)}")
print(f"{'=' * 60}")
