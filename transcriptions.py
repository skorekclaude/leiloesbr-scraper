"""
Transkrypcje dokumentów z Kolekcji Głuchowskich (seria Juras).
Każdy dokument ma: transkrypcję, osoby, pieczęcie, podpisy, znaki szczególne.

Format: TRANSCRIPTIONS[sygnatura] = { ... }
"""

TRANSCRIPTIONS = {

    # ═══════════════════════════════════════════════════════════════
    # juras_001 — Aerogram z Nowej Zelandii
    # ═══════════════════════════════════════════════════════════════
    "juras_001": {
        "typ": "Aerogram (N.Z. Air Mail Letter Card)",
        "data": "ok. 1946-1948",
        "jezyk": "polski",
        "nadawca": "Danka (prawdopodobnie Danuta Głuchowska lub krewna)",
        "adresat": "Krzysztof Głuchowski, Polish Forces, C.M.F. 105 (Central Mediterranean Forces), Italia",
        "transkrypcja": """Uszymy się tu też nadrabiając straty ubiegłych lat
i ciągle szyjemy od rana do wieczora. Po długich latach tułaczki
ością i niedoli będziemy mogli przesiąść nad odnowieniem
i odbudowaniem Rodnej Polski.
Ale przy tym musisz skończyć mój list. Myślę, że Pan
będzie łaskawym odpisać na pewnie łacinym pozdrawia
mia dla Pana Kolegio.
        Danka.""",
        "pieczecie": ["Stempel pocztowy N.Z. (Nowa Zelandia)", "Cenzura wojskowa ITALIA"],
        "podpisy": ["Danka"],
        "osoby": ["Krzysztof Głuchowski", "Danka (nadawczyni)"],
        "znaki_szczegolne": [
            "Aerogram wojskowy BY AIR MAIL — N.Z. Air Mail Letter Card",
            "Adres: C.M.F. 105 = Central Mediterranean Forces (Włochy)",
            "Tekst odwrócony (zdjęcie do góry nogami)",
            "Czerwony dopisek ołówkiem: 'Italia'",
            "Ton listu nostalgiczny — wspomnienia o tułaczce, nadzieja na odbudowę Polski"
        ],
        "kontekst": "List z Nowej Zelandii do żołnierza PSZ we Włoszech. Nadawczyni Danka pisze o szyciu i nadrabianiu strat wojennych. Wspomina o tułaczce i nadziei na odbudowę Polski."
    },

    # ═══════════════════════════════════════════════════════════════
    # juras_002 — List odręczny (strona z aerogramu lub oddzielny list)
    # ═══════════════════════════════════════════════════════════════
    "juras_002": {
        "typ": "List odręczny",
        "data": "ok. 1946-1948",
        "jezyk": "polski",
        "nadawca": "Nieustalony (prawdopodobnie Danka lub inna krewna)",
        "adresat": "Brak widocznego adresata (kontynuacja listu?)",
        "transkrypcja": """Drogi Salusiu...
Kochany rodziny sprawd na Boże... bo ubiego roku
historia ojbydwlm na Boże list... bo pabysgo do
Armia Ewakuacyjna dowcieliom...
Chocia i rozerwij, kolekcja do... tej...
[...tekst trudny do odczytu ze względu na charakter pisma...]
...o biedę i... nie zapas...
...do siebie zabiernieci przyb...
...Niestety Bożego opłatku
...na ile drugie cieki Bożego po remiśce
do obos zebrdzimy
...dziele piękne tego krok
[...dalszy tekst nieczytelny...]""",
        "pieczecie": [],
        "podpisy": [],
        "osoby": ["Saluś (adresat — zdrobnienie)", "Krzysztof Głuchowski (prawdopodobny odbiorca)"],
        "znaki_szczegolne": [
            "Pismo odręczne atramentem niebieskim",
            "Bardzo trudny do odczytu charakter pisma",
            "Wspomnienie o Bożym Narodzeniu — opłatek, życzenia",
            "Ton emocjonalny — tęsknota za rodziną",
            "Wspomnienie 'Armia Ewakuacyjna' — kontekst wojskowy"
        ],
        "kontekst": "List prywatny, prawdopodobnie świąteczny (Boże Narodzenie). Nadawca zwraca się do 'Salusia'. Wspomina o Armii Ewakuacyjnej i rozłące rodzinnej."
    },

    # ═══════════════════════════════════════════════════════════════
    # juras_003 — Arkusz rachunkowy / Oficerska Składnica Mundurowa
    # ═══════════════════════════════════════════════════════════════
    "juras_003": {
        "typ": "Arkusz rachunkowy wojskowy",
        "data": "1945-1946",
        "jezyk": "polski",
        "nadawca": "Oficerska Składnica Mundurowa (Oficerska Składnica Gospoldarzcza?)",
        "adresat": "Głuchowski Krzysztof",
        "transkrypcja": """OFICERSKA SKŁADNICA MUNDUROWA/GOSPOLARCZA
MAGAZYN E.I.

Głuchowski Krzysztof

[Tabela z datami i kwotami:]
19.I.46    £ 14.0    Gum. Lola
10.I.46    £ 14.0       —
7.I.46     £ 14.0       —
1.I.46     £ 14.0       —
            £ 14.0
            N/P

[Daty w lewej kolumnie:]
19.II.46
10.II.46
1.II.46
29.I.46
[...dalsze wpisy...]""",
        "pieczecie": ["Pieczątka OFICERSKA SKŁADNICA MUNDUROWA (częściowo nieczytelna)"],
        "podpisy": ["Podpisy nieczytelne przy poszczególnych wpisach"],
        "osoby": ["Krzysztof Głuchowski"],
        "znaki_szczegolne": [
            "Papier kancelaryjny w kratkę (formularz rachunkowy)",
            "Kwoty w funtach brytyjskich (£14.0)",
            "Daty: styczeń-luty 1946",
            "Magazyn E.I. — kontekst: zaopatrzenie wojskowe PSZ",
            "Prawdopodobnie lista pobrań mundurowych/ekwipunku",
            "Adnotacja 'Gum. Lola' — prawdopodobnie gumowa peleryna/buty"
        ],
        "kontekst": "Dokument rachunkowy z Oficerskiej Składnicy Mundurowej PSZ. Dokumentuje pobrania ekwipunku przez kpr. Krzysztofa Głuchowskiego w styczniu-lutym 1946. Kwoty w funtach — jednostka stacjonowana w Wielkiej Brytanii lub Włoszech pod dowództwem brytyjskim."
    },

    # ═══════════════════════════════════════════════════════════════
    # juras_004 — Przepustka / Pass (dwujęzyczny)
    # ═══════════════════════════════════════════════════════════════
    "juras_004": {
        "typ": "Przepustka wojskowa (PRZEPUSTKA / PASS)",
        "data": "14.II.1946",
        "jezyk": "polski / angielski",
        "nadawca": "Dowództwo jednostki wojskowej PSZ",
        "adresat": "Sierż. [Sierżant] Manelko (?), Batl. [Batalion]",
        "transkrypcja": """PRZEPUSTKA
PASS

Data: 14.II.1946 r.
Nazwisko: Sierż... Manelko (?) E. Batl...

has permission to be absent from his unit
from ... 14.II.1946
to ... [data powrotu]

for the purpose of proceeding to
...Ostia Wislanów (?)...

[podpis oficera]""",
        "pieczecie": ["Pieczątka okrągła jednostki — nieczytelna", "Stempel D-TWO 3 D.S.K. (3 Dywizja Strzelców Karpackich?)"],
        "podpisy": ["Podpis oficera wydającego (nieczytelny)"],
        "osoby": ["Sierżant Manelko (lub Głuchowski?) — posiadacz przepustki"],
        "znaki_szczegolne": [
            "Formularz dwujęzyczny: polski + angielski",
            "Data: 14 lutego 1946",
            "D-TWO 3 D.S.K. — prawdopodobnie 3 Dywizja Strzelców Karpackich",
            "Cel podróży: Ostia (Włochy? — blisko Rzymu)",
            "Dokument wyblakły, trudny do odczytu w wielu miejscach",
            "Pieczątka fioletowa (atrament urzędowy)"
        ],
        "kontekst": "Przepustka wojskowa wydana żołnierzowi PSZ we Włoszech. 3 Dywizja Strzelców Karpackich (3 DSK) walczyła pod Monte Cassino i po wojnie stacjonowała we Włoszech do demobilizacji."
    },

    # ═══════════════════════════════════════════════════════════════
    # juras_005 — Zaświadczenie / Poświadczenie (D-TWO 3 DSK)
    # ═══════════════════════════════════════════════════════════════
    "juras_005": {
        "typ": "Zaświadczenie wojskowe",
        "data": "ok. 1945-1946",
        "jezyk": "polski",
        "nadawca": "Dowództwo 3 D.S.K. (3 Dywizja Strzelców Karpackich)",
        "adresat": "Kpr. [Kapral] Głuchowski Krzysztof",
        "transkrypcja": """D-TWO 3 D.S.K.
DEMOBILIZACJA
L.dz. .../.../46

Data: ......1946 r.

ZAŚWIADCZENIE

Zaświadcza się, że kpr. Głuchowski Krzysztof
...niniejszym służył (...) rejonowy
w okresie od dnia ... 1945 r. do dnia ... 1946 r.
do dnia ... lunch ... 1946 r. służb ... r.

Komendant
Obóz/Ośrodek I Liceum 3 DSK.
[podpis] Kapica Józef
kapitan""",
        "pieczecie": ["Pieczątka D-TWO 3 D.S.K. DEMOBILIZACJA"],
        "podpisy": ["Kpt. Kapica Józef — Komendant Obozu/Ośrodka I Liceum 3 DSK"],
        "osoby": ["Krzysztof Głuchowski (kapral)", "Józef Kapica (kapitan, komendant)"],
        "znaki_szczegolne": [
            "Pieczątka DEMOBILIZACJA — dokument z okresu rozwiązywania PSZ",
            "Komendant: kpt. Józef Kapica",
            "Ośrodek I Liceum 3 DSK — liceum polskie przy dywizji (edukacja żołnierzy)",
            "Głuchowski miał stopień KAPRALA",
            "Atrament fioletowy — pieczątka + podpis"
        ],
        "kontekst": "Zaświadczenie o służbie wydane przez Ośrodek I Liceum przy 3 Dywizji Strzelców Karpackich. Świadczy o tym, że Krzysztof Głuchowski po walkach uczęszczał do liceum wojskowego — typowa ścieżka młodych żołnierzy PSZ uzupełniających wykształcenie po wojnie."
    },

    # ═══════════════════════════════════════════════════════════════
    # juras_006 — Świadectwo Liceum Ogólnokształcącego
    # ═══════════════════════════════════════════════════════════════
    "juras_006": {
        "typ": "Świadectwo szkolne",
        "data": "20 czerwca 1946",
        "jezyk": "polski",
        "nadawca": "Liceum Ogólnokształcące Nr 9 przy 3 Dywizji Strzelców Karpackich",
        "adresat": "Głuchowski Krzysztof",
        "transkrypcja": """ŚWIADECTWO LICEUM
OGÓLNOKSZTAŁCĄCEGO

Nr 9

Liceum Ogólnokształcące 3 Dywizji Strzelców
Karpackich 2 Korpusu z prawami szkół państwowych
(Zarządzenie Oddziału Wych. W.P./O.T. mo. 2 Korpusu
d.d. 1829/Wdz./46, dat. L/6.19)

matem.-fizyc.
(typ)

Krzysztof Głuchowski
(imię i nazwisko)

urodzony dnia 29.XI. roku 1926 m. Warszawa
województwo — wyznania rzym.-kat.
uczęszczał do klasy I-fce — Pierwsza Licealna
i uczył się w roku szkolnym od 1 Kwiecień 1946
do 30 Czerwca 1946 oceny następujące:

z zachowania się        — bardzo dobry
z religii               — dobry
z języka polskiego      — dobry
z języka angielskiego   — dobry
z języka włoskiego      — dostateczny
z historii              — dobry
z zagadnień życia współczesnego — dostateczny
z geografii i geologii  —
z fizyki z astronomią   — dobry
z chemii                — dobry
z matematyki            — dostateczny
z propedeutyki filozofii — bardzo dobry
z ćwiczeń cielesnych    — dobry
z biologii              — dobry""",
        "pieczecie": [],
        "podpisy": ["Podpisy pedagogów (na stronie 2)"],
        "osoby": ["Krzysztof Głuchowski (uczeń)"],
        "znaki_szczegolne": [
            "Świadectwo z ORŁEM POLSKIM (godło) w nagłówku",
            "Liceum Nr 9 przy 3 DSK — szkoła polonijna we Włoszech",
            "Data ukończenia: 20 czerwca 1946",
            "Oceny: głównie dostateczne i dobre, religia i propedeutyka — bardzo dobre",
            "Formularz drukowany z odręcznymi wpisami",
            "Dokument formalny edukacji w warunkach emigracyjnych"
        ],
        "kontekst": "Świadectwo szkolne z Liceum Ogólnokształcącego Nr 9, działającego przy 3 DSK we Włoszech. Polskie szkoły przy PSZ umożliwiały młodym żołnierzom uzupełnienie wykształcenia przerwanego przez wojnę. Głuchowski ukończył klasę z przeciętnymi ocenami."
    },

    # ═══════════════════════════════════════════════════════════════
    # juras_007 — Świadectwo Liceum — strona 2 (pieczęć + podpisy)
    # ═══════════════════════════════════════════════════════════════
    "juras_007": {
        "typ": "Świadectwo szkolne — strona 2 (rewers)",
        "data": "20 czerwca 1946",
        "jezyk": "polski",
        "nadawca": "Liceum Ogólnokształcące Nr 9 przy 3 DSK",
        "adresat": "Głuchowski Krzysztof",
        "transkrypcja": """Przedmioty nadobowiązkowe:
[przekreślone — brak wpisów]

Opuścił godzin szkolnych 10 w tym nieusprawiedliwiono
Uchwałą Rady Pedagogicznej otrzymał promocję
do klasy

Amandola — Italia dnia 30 czerwca 1946 r.

[podpis] Mirowski F.
Opiekun klasy

[pieczęć okrągła — MINISTERSTWA WYZNAŃ RELIGIJNYCH I OŚWIECENIA PUBLICZNEGO — M.P.]

[podpis] Dr H. Polczynizo
Dyrektor""",
        "pieczecie": ["Pieczęć okrągła szkoły (czerwona, z orłem)", "M.S. — inicjały?"],
        "podpisy": ["Fr. Sowiński F. — Opiekun Klasy", "D.M. Melosik (?) — Dyrektor"],
        "osoby": ["Krzysztof Głuchowski (uczeń)", "Fr. Sowiński F. (opiekun klasy)", "Dyrektor Melosik (?)"],
        "znaki_szczegolne": [
            "Pieczęć okrągła CZERWONA — pieczęć urzędowa szkoły",
            "Podpisy dwóch osób: opiekun klasy + dyrektor",
            "Miejsce wydania: Italia (Włochy)",
            "Zachowana w dobrym stanie — czytelne podpisy"
        ],
        "kontekst": "Rewers świadectwa z podpisami kadry pedagogicznej i pieczęcią szkoły. Potwierdza autentyczność dokumentu."
    },

    # ═══════════════════════════════════════════════════════════════
    # juras_008 — Gazeta obozowa "OBÓZ LAMMIE — Wiadomości Tygodniowe"
    # ═══════════════════════════════════════════════════════════════
    "juras_008": {
        "typ": "Gazeta obozowa / Informator",
        "data": "ok. 1946-1948",
        "jezyk": "polski",
        "nadawca": "Redakcja obozowa, Obóz Lammie",
        "adresat": "Mieszkańcy obozu",
        "transkrypcja": """OBÓZ LAMMIE
WIADOMOŚCI TYGODNIOWE
ROZRYWKI OBOZOWE

─── TEATR NA OTWARTYM POWIETRZU ───
PON. WTOR. ŚRODA i CZWART. PIĄTEK
Szalone i Calsi: ok. 2000 hr.

─── KINO ODEON ───
KSC Poniedz.
PON. WTOR./ ŚRODA
Ceny Biletów: NIEUSTALONY

PROGRAM NIEUSTALONY

─── "REWIA LAMMIE" ───
Odwiedziny Roma z odk. Okazji
299 kwarteru Numerowo
                    Założone w Lirze

CZWARTEK, SOBOTA I NIEDZIELA
Ceny biletów 120 i 200
PROGRAM NIEUSTALONY

─── CYRK LAMMIE ───
Niepowtarzalny Teatr Ciekaw
Otwarty do Dyspozycji
Ceny biletów: ...Założone 60 Lirze

CO DO DALSZYCH SZCZEGÓŁÓW ZAPRZECZAMY SŁUŻYWO
GOŚCIOM DLA PAŃ

KOMUNIKACJA AUTOBUSOWA — LAMMIE - NEAPOL
Odjazd z przed Gospody Red Lion w Godz: 1330, 1500, 1600, 1700, 1800, 1900 i 2030
Powrót z przed Pałac Neapol o Godz: 1400, 1500, 1630, 1730, 1830, 1930 i 2230.
SKLEPOBOZOWY: — Wielki Wybór Towarów, Rękawiczki, Kamee, Pończochy, Zegarki, Walizki
Wszelkich Rozmiarów, Orzechy, Rodzynki, i t. p. Na miejscu Znajdują Się robotnice
Które Naszalenie Haftuję Monogramy i Napisy Na jedwab Nych Materiałach.
DOSKONAŁY FOTOGRAF ZNAJDUJE: — Się W Rejonie "E" Cenyyumiar, Kowane,
Otwarty W Godz. 0900 - 1230 i 1400 - 1630.""",
        "pieczecie": [],
        "podpisy": [],
        "osoby": [],
        "znaki_szczegolne": [
            "Druk obozowy — informator tygodniowy",
            "Obóz Lammie — obóz przejściowy/demobilizacyjny PSZ we Włoszech (okolice Neapolu)",
            "Program rozrywkowy: teatr, kino Odeon, rewia, cyrk",
            "Ceny w LIRACH włoskich",
            "Komunikacja autobusowa Lammie–Neapol",
            "Sklep obozowy — alkohol, artykuły",
            "Fotograf obozowy",
            "Świadectwo życia kulturalnego polskich żołnierzy po wojnie"
        ],
        "kontekst": "Informator tygodniowy obozu Lammie pod Neapolem — jednego z obozów dla żołnierzy PSZ po zakończeniu wojny. Dokument unikatowy, świadczący o bogatym życiu kulturalnym: teatr, kino, cyrk, rewia. Ceny w lirach. Komunikacja autobusowa do Neapolu."
    },

    # ═══════════════════════════════════════════════════════════════
    # juras_009 — Mapa obozu Lammie
    # ═══════════════════════════════════════════════════════════════
    "juras_009": {
        "typ": "Mapa / Plan obozu",
        "data": "ok. 1946-1948",
        "jezyk": "polski / angielski",
        "nadawca": "Administracja obozu Lammie",
        "adresat": "Mieszkańcy obozu",
        "transkrypcja": """[LEGENDA MAPY:]
1. Fotograf                    7. Teren Sportowy        13. Poczta Polowa
2. D-two Generała plk Wielskiego 8. Polska Komenda Obozowa 14. Kasyno Podoficerskie
3. Kościół                     9. Kino Odeon            15. Pralnia Przyczółki
4. Główna Ulica               10. Polska Komenda Obozowa 16. Planty Polskie
5. Przychodnia Lekarska       11. Teatr Gaiety
6. Odcinek Transportowy       12. Kasyno Oficerskie

[MAPA POKAZUJE:]
— Sektory: C, D, E
— Alexander Road (główna droga)
— NAPLES (kierunek Neapol)
— Budynki, drzewa, place
— Base + Print [AR/PIR?]""",
        "pieczecie": [],
        "podpisy": [],
        "osoby": ["Generał Fiji Waski (?) — nazwa ulicy/kwatery"],
        "znaki_szczegolne": [
            "Drukowana mapa obozu z legendą po polsku",
            "Sektory C, D, E — podział administracyjny",
            "Alexander Road — główna arteria",
            "Kierunek: Neapol (Naples)",
            "Synagoga, kościół, kaplica — wielowyznaniowość",
            "Poczta Polowa, Polska Komenda Główna",
            "Plac sportowy, promenada — infrastruktura rekreacyjna",
            "Przychodnia lekarska — opieka medyczna",
            "NIEZWYKLE RZADKI DOKUMENT — mapy obozów PSZ są bardzo cenione przez kolekcjonerów"
        ],
        "kontekst": "Plan obozu Lammie pod Neapolem. Niezwykle rzadki dokument kartograficzny. Pokazuje pełną infrastrukturę: sektory mieszkalne, obiekty religijne (synagoga, kościół, kaplica), rekreacyjne (plac sportowy, promenada), administracyjne (Polska Komenda Główna, Poczta Polowa). Droga na Neapol. Świadectwo organizacji życia kilku tysięcy polskich żołnierzy."
    },

    # ═══════════════════════════════════════════════════════════════
    # juras_010 — List do matki (24.XII.1946 — Wigilia)
    # ═══════════════════════════════════════════════════════════════
    "juras_010": {
        "typ": "List odręczny (Wigilia 1946)",
        "data": "24 grudnia 1946",
        "jezyk": "polski",
        "nadawca": "Krzysztof Głuchowski",
        "adresat": "Matka (Kochana moja Mateczko!)",
        "transkrypcja": """24-XII-1946r.

Kochana moja Mateńko!

Myślę o Tobie. Ciekawy jestem gdzie w tej chwili jesteś. Wiem że i Ty Mateńko myślisz o nas obu. Myślami więc jesteśmy wszyscy troje razem, choć dzielą nas góry, rzeki i morza.

List Mateńki z dn. 2-XII otrzymałem już kilka dni temu. Chcę nań odpisać. Przede wszystkim odpowiadam na pytania:

Typ szkoły do której chodzę jest ogólnokształcący. Zdałem obecnie z wynikiem dostatecznym do klasy drugiej liceum matematyczno-fizycznego. Poziom szkoły jest wysoki. Do dużej matury pozostało mi od 6 do 8 miesięcy.

Mieszkam w obozie, gdzie mieści się nasza szkoła adres jej Mateńka zna. W baraku jest nas dwudziestu. Jest w baraku czysto.

Klimat nie przeszkadza mi zupełnie. Poprzednio byłem w górach gdzie był też ostry klimat, więc zmiana nie była taka straszna.

Ciepłych rzeczy do ubrania mam dosyć a nawet sporo. Również i bieliznę mam ciepłą wełnianą. Ubrań mam aż trzy w tym jedno zupełnie eleganckie.

[Strona 2:]

Pod tym względem zupełnie się Matuś nie potrzebuje martwić. Np. mam dwie pary butów i dwie pary półbucików.

Papierosów nie palę. Pijałem tylko Ojcu. Alkohol piję tylko wtedy, gdy jest jakaś przygrywka, ale nie ciągnie mnie do tego.

Z zębami gorzej, gdyż nie mam zupełnie wewnętrznych od wewnątrz. Jeden wyrwałem pół roku temu (prawy, dolny, pierwszy trzonowy). Obecnie mam bardzo popsute oba przedtrzonowe górne. Będę starał się je leczyć.

Z językiem tak sobie. Wprawdzie znam z angielskiego b. dobrze, ale rozmawiać jeszcze nie mogę, ani czytać książek. Mówię jako tako natomiast biegle po włosku.

Wódka fucha już nie jest na dawnej posadzie, ale w dalszym ciągu pracuje w tym samym biurze.

Co do towarzystwa to femmel nie może być liczony w ogóle. Jest dobrym kolegą i też współmilczkiem, ale jest dość ograniczony. Zresztą o takie towarzystwo jak jego mi nie chodzi. Chodzi mi przede wszystkim o towarzystwo kobiece, a na drugim miejscu kulturalne i inteligentne. Kolegów mam dosyć. Żyję przecież z nimi. Życie zbiorowe jest dobre ale w miarę.

[Strona 4:]

Co do tego że niewdzięczna Mama może sypać głowę popiołem, to znów mylisz się całkowicie. Bomby niestety nie były podporządkowane jej życzeniom. Zresztą przez ostatnie najcięższe dwa dni nie było już nikogo na stanowisku. Aby żyć trzeba mieć więcej szczęścia niż rozumu. Zresztą wcale nie dziwię się, bo w Niemczech byłem bardzo bliski do śmierci, ale też miałem szczęście. Nie wiem czy Mateńka wie. Pracując w niewoli w M. Gladbach przy umacnianiu gruzów, przeszedłem wiele nalotów Anglo-Amerykańskich. Podczas jednego z nich dnia 1-lutego 1945 bomba uderzyła w piwnicę sąsiedniego domu (~3-4 m odemnie). Wypchnęła ona ścianę do naszej piwnicy i postawiła mnie na nogi. Oparzyła ona nogę. Oparzenie było III stopnia. Dokładnie miałem oparzoną lewą stopę od wewnątrz. Pojechałem do szpitala w Gerresheimie pod Düsseldorfem. Wyleczyli mnie tam i teraz mam jedynie bliznę, która nie przeszkadza ani nie dokucza. (wymiary 7 cm x 2 cm)

Przesyłkę dostałem, ale proszę Cię Mateńko nie przysyłaj mi więcej, gdyż mam ich dosyć. Zresztą dostałem 9 zł co odpowiada mojej półtora miesięcznej pensji. A co nie jest wcale wielką sumą. Zresztą po przeliczeniu powinienem od nich dostać 12 zł

[Strona 3 — częściowo odczytana z enhancowanego skanu:]

aż 3£ kontaktu, ta cała opłata, a przyszły, grosze, dobrze. Mam oszczędzone 40£ (Długi teraz, że nie podam). Nie pomyślisz ni się mądrzyć. Dotąd nie wręczyli bo i dalej się żądam. Jak dotąd to i nadal tak w Bolonii.

12) z panią Joanną korespondentką.

Oto moje krótkie odpowiedzi na wszystkie pytania.

Obecną sytuację — trochę. Na Wigilię byłem w mieście, dostałem bilet na przejazd. Pociągi klinem nabite, dnia twarze[?], nieba[?], poruszyłaś[?] i studiem. Kierunek na kochanie. Mam jeszcze dorzucić pieniędzy, wszystko będą do 2 konta[?]. Obiecuję robić dobrze. Darzy Boga pięknie stare i mają interes.

A propos korespondencję, ma Mateńka pozdrowić od komendy, jest to moja korespondentka z Italii. Pisze ona daje Mateńki od razu pozdrowić i powiedzieć że bardzo ona Mateńkę kocha gdyż jest moją mamą. Bardzo jest miła i kocha owa Mateńkę. Bardzo miła jest i ja mam korespondentką. Kupię[?] [...]""",
        "pieczecie": [],
        "podpisy": ["Krzysztof (domyślnie — list do matki)"],
        "osoby": ["Krzysztof Głuchowski (nadawca)", "Matka Głuchowska (adresatka)", "Mattoni (?)", "Rudenko (?)"],
        "znaki_szczegolne": [
            "Data: Wigilia 1946 — list świąteczny",
            "Zwrot 'Kochana moja Mateczko!' — głęboki szacunek i czułość",
            "Pismo odręczne czarnym atramentem, drobne, trudne do odczytu",
            "Wymienione punkty numerowane (1, 2, 3) — prośby lub pytania",
            "Ton emocjonalny — tęsknota za matką w Wigilię",
            "List pisany prawdopodobnie z obozu we Włoszech",
            "Wspomnienie osoby 'Mattoni' — może kolega z jednostki"
        ],
        "kontekst": "Wigilijny list Krzysztofa Głuchowskiego do matki, pisany 24 grudnia 1946 r. z obozu we Włoszech. Niezwykle osobisty dokument — młody żołnierz spędza kolejne święta z dala od rodziny. Ton listu pełen tęsknoty. Wymienia konkretne osoby i prośby."
    },

    # ═══════════════════════════════════════════════════════════════
    # juras_015 — Formularz urlopowy / Leave Pass (brytyjski)
    # ═══════════════════════════════════════════════════════════════
    "juras_015": {
        "typ": "Formularz urlopowy (Leave Pass)",
        "data": "ok. 1946",
        "jezyk": "angielski",
        "nadawca": "Dowództwo brytyjskie",
        "adresat": "Żołnierz PSZ (Głuchowski?)",
        "strony": ["juras_015_page16.png", "juras_016_page17.png"],
        "transkrypcja": """[Formularz brytyjski — Leave Pass / ZASS]

[Strona 1: Dane przepustki — pola częściowo wypełnione]

[Strona 2: Instrukcja po angielsku]
Instructions to a soldier, or member other than Officer
of the A.T.S. if he/she is taken ill or requires urgent
medical or dental treatment while on leave.

1. Report in person to the nearest Military or other Service
   Medical Establishment or Emergency Medical Services Hospital.
   (Such an establishment is shown on the front of this leave pass.)
2. If unable, because of your illness, to report in person, you must
   send a message to the nearest Military Medical Unit and ask for instructions.
3. If unable to do either (1) or (2), because of distance involved (over 2 miles)
   you may visit, or call in, a Civilian Medical or Dental Practitioner, to whom
   you will show this pass. You will at once report the employment of a civilian
   practitioner to your Commanding Officer.
4. If, through sickness, you are unable to travel at the expiration of your leave
   and are under the care of a Civilian Doctor, you must obtain a Certificate to
   that effect from the Doctor and forward it at once to your Commanding Officer.

To the Civilian Practitioner.
(a) When a soldier is sick at the expiration of his leave and a Civilian Medical
    Practitioner is in attendance, the latter should be guided, in the action he
    takes, solely by the soldier's fitness or unfitness to travel.
(b) If fit to travel he should be instructed to return to his Unit and report sick
    to his Medical Officer. If unfit, he should be furnished with a Certificate to
    that effect to be forwarded to his Commanding Officer, and at the same time be
    instructed to notify the nearest Military Medical Establishment.""",
        "pieczecie": [],
        "podpisy": [],
        "osoby": ["Krzysztof Głuchowski (domniemany posiadacz)"],
        "znaki_szczegolne": [
            "Formularz brytyjski — żołnierze PSZ podlegali dowództwu brytyjskiemu",
            "Druk dwustronny z instrukcją medyczną",
            "A.T.S. = Auxiliary Territorial Service",
            "Świadectwo integracji PSZ z brytyjskim systemem wojskowym"
        ],
        "kontekst": "Formularz urlopowy wydawany żołnierzom pod dowództwem brytyjskim. Żołnierze PSZ, choć polscy, otrzymywali dokumenty brytyjskie. Instrukcja dotyczy postępowania w razie choroby na urlopie."
    },

    # ═══════════════════════════════════════════════════════════════
    # juras_017 — Kartka świąteczna z Liceum Polskiego
    # ═══════════════════════════════════════════════════════════════
    "juras_017": {
        "typ": "Kartka świąteczna",
        "data": "grudzień 1946",
        "jezyk": "polski / angielski",
        "nadawca": "Polskie Liceum (3 DSK?)",
        "adresat": "Krzysztof Głuchowski (domyślnie)",
        "strony": ["juras_017_page18.png", "juras_018_page19.png"],
        "transkrypcja": """[Strona tytułowa — ozdobna grafika z gałązką ostrokrzewu:]

Wesołych Świąt
Bożego Narodzenia

Compliments
of the Season

The Soldier Medical Society
at Thomas's Norfolk

[Strona wewnętrzna:]
With
Best Wishes
for
Xmas and
the New Year

[Grafika: gałązka ostrokrzewu z jagodami, zielony druk]""",
        "pieczecie": [],
        "podpisy": [],
        "osoby": ["Krzysztof Głuchowski (domniemany adresat)"],
        "znaki_szczegolne": [
            "Kartka dwujęzyczna: polsko-angielska",
            "Ozdobna grafika — gałązka ostrokrzewu (holly)",
            "The Soldier Medical Society at Thomas's Norfolk",
            "Zachowana w dobrym stanie — kolory żywe",
            "Świadectwo życia towarzyskiego żołnierzy polskich"
        ],
        "kontekst": "Kartka świąteczna z okazji Bożego Narodzenia, prawdopodobnie 1946 r. Dwujęzyczny tekst (polski + angielski) odzwierciedla środowisko polsko-brytyjskie."
    },

    # ═══════════════════════════════════════════════════════════════
    # juras_021 — Świadectwo Liceum (drugie, pełniejsze)
    # ═══════════════════════════════════════════════════════════════
    "juras_021": {
        "typ": "Świadectwo szkolne (I Polskie Liceum)",
        "data": "30 XI 1946",
        "jezyk": "polski",
        "nadawca": "I. Polskie Liceum im. 3 Dywizji Strzelców Karpackich w Barletta (Włochy)",
        "adresat": "Głuchowski Krzysztof",
        "strony": ["juras_021_page22.png", "juras_022_page23.png"],
        "transkrypcja": """I. POLSKIE LICEUM im.
3 Dywizji Strzelców Karpackich
w Barletta [Włochy]

Rok szkolny 1944...
Nr S.E. 1946

ŚWIADECTWO LICEUM

Nr 9

Głuchowski Krzysztof   mężczyzna
urodzony dnia 29.VI roku 1926 w Warszawa
województwo — wyznania rzym.-kat.
do klasy następnej:

OCENY NASTĘPUJĄCE:
z zachowania się:          bardzo dobre
z religii:                 bardzo dobry
z języka polskiego:        dobry
z języka angielskiego:     dostateczny
z historii:                dostateczny
z zagadn. życia współcz.:  dostateczny
z geografii i astronomii:  dostateczny
z fizyki z astronomią:     oceny
z chemii:                  dostateczny
z matematyki:              dobry
z propedeutyki:            dostateczny
z ćwiczeń cielesnych:      dobry
z rysunków:                dostateczny

[Strona 2 — rewers:]
Przedmioty nadobowiązkowe: [przekreślone — brak wpisów]
Opuścił godzin szkolnych 43 w tym nieusprawiedliwiono
Uchwałą Rady Pedagogicznej otrzymał promocję do klasy drugiej

Dnia 30 XI 1946.

Nr 2       Bol/ej

[podpis] Klimowska F.
Opiekun Klasy

[pieczęć okrągła szkoły — M.P.]

[podpis] D. Budzik
DYREKTOR I PRZEŁOŻONA""",
        "pieczecie": ["Pieczęć okrągła szkoły (M.P.)", "Pieczątka szkoły w nagłówku"],
        "podpisy": ["Klimowska F. — Opiekun Klasy", "D. Budzik — Dyrektor i Przełożona"],
        "osoby": ["Krzysztof Głuchowski (uczeń)", "Klimowska F. (opiekun klasy)", "D. Budzik (dyrektor)"],
        "znaki_szczegolne": [
            "I. Polskie Liceum w BARLETTA — miasto w Apulii, Włochy",
            "Szkoła im. 3 Dywizji Strzelców Karpackich",
            "Data: 30 XI 1946 (= 30 listopada 1946)",
            "Zachowanie: BARDZO DOBRE",
            "43 godziny obowiązkowe tygodniowo — intensywny program",
            "Dyrektor: D. Budzik (kobieta — 'Przełożona')",
            "Opiekun klasy: Klimowska F. (kobieta)",
            "Oceny lepsze niż na wcześniejszym świadectwie (czerwiec 1946)"
        ],
        "kontekst": "Drugie świadectwo z Polskiego Liceum przy 3 DSK, tym razem z Barletta (Apulia). Szkoła przeniosła się z innej lokalizacji lub powstała nowa. Dyrekcja kobieca (D. Budzik, Klimowska) — w PSZ pracowało wiele Polek jako nauczycielki. Głuchowski poprawił oceny w porównaniu z czerwcem."
    },

    # ═══════════════════════════════════════════════════════════════
    # juras_024 — Informator PKPR (Polish Resettlement Corps)
    # ═══════════════════════════════════════════════════════════════
    "juras_024": {
        "typ": "Broszura informacyjna PKPR",
        "data": "1946",
        "jezyk": "polski",
        "nadawca": "Polski Korpus Przysposobienia i Rozmieszczenia",
        "adresat": "Żołnierze PSZ",
        "transkrypcja": """POLSKI KORPUS PRZYSPOSOBIENIA
I ROZMIESZCZENIA
(POLISH RESETTLEMENT CORPS)

1. Polski Korpus Przysposobienia i Rozmieszczenia, nazywany skrótowo
P.K.P.R., został utworzony przez Rząd Brytyjski w celu ułatwienia
żołnierzom Polskich Sił Zbrojnych osiedlenia się w życiu cywilnym.

2. Przy wstąpieniu do P.K.P.R. będziecie musieli podpisać specjalny formularz, tzw.
Attestation Form. Formularz ten jest w języku polskim, przy czym każdy otrzyma 1 egzem-
plarz, będzie zatem widział dokładnie co należy uczynić.

3. Będziecie przyjmowani do służby w P.K.P.R. na okres dwóch lat. Nie oznacza to,
że będziecie musieli spędzić dwa lata w obozie wojskowym, gdyż w razie znalezienia
dla Was pracy w zawodzie cywilnym przed upływem tego terminu, lub jeśli sami
znajdziecie tego rodzaju zajęcie, będziecie mogli przejść do rezerwy.

4. Z chwilą wstąpienia do P.K.P.R. staniecie się żołnierzami Armii Brytyjskiej i będziecie
podlegali normalnym brytyjskim przepisom dyscyplinarnym. W razie popełnienia poważnego
wykroczenia będziecie sądzeni przez Brytyjski Sąd Wojskowy, na podstawie przepisów brytyjskich.

5. Będziecie przyjmowani do P.K.P.R. w stopniu szeregowca, gdyż prawo brytyjskie nie
pozwala na przyjmowanie do armii kogokolwiek powyżej tego stopnia, jednakże odrazu
otrzymacie tzw. płatny stopień lokalny (paid local rank), równy stopniowi według którego
otrzymywaliście żołd w Armii Polskiej.

6. Dzienne stawki żołdu będą wynosiły:
                        żołd     po 3 latach  po 4 latach
Chor. (Warrant Officer I Class)   14s 6d    15s 6d    16s 0d
St.sierż. (Warrant Officer II)    11s 6d    12s 6d    13s 6d
Sierż. (Staff Sergeant)           10s 6d    11s 0d    11s 0d
Plut. (Sergeant)                    6s 8d     7s 9d     8s 0d
Kpl. (Corporal)                     5s 0d     6s 0d       —
St.szer. (Lance Corporal)           4s 3d     5s 0d     5s 4d
Szer. (Private)                     3s 6d     4s 0d     4s 6d

7. Żonom i rodzinom żonatych oficerów i szeregowych P.K.P.R., które przebywają w
Zjednoczonym Królestwie, będzie przysługiwało zaopatrzenie, mieszkanie i wyżywienie w
naturze, albo dodatek rodzinny w gotówce.""",
        "pieczecie": ["Godło PKPR w nagłówku"],
        "podpisy": [],
        "osoby": [],
        "znaki_szczegolne": [
            "Oficjalna broszura informacyjna PKPR",
            "Wyjaśnia warunki służby, żołd, uprawnienia",
            "Tabela żołdu w funtach brytyjskich wg stopni",
            "Mundur z polskim orłem i napisem P.K.P.R.",
            "Służba max 2 lata — program reintegracji cywilnej",
            "NIEZWYKLE WAŻNY dokument historyczny — jeden z niewielu zachowanych informatorów PKPR"
        ],
        "kontekst": "Broszura informacyjna Polskiego Korpusu Przysposobienia i Rozmieszczenia (PKPR/PRC). Utworzony w 1946 r. przez rząd brytyjski dla ~250 000 polskich żołnierzy, którzy nie chcieli wracać do komunistycznej Polski. Oferował 2 lata służby, szkolenie zawodowe i pomoc w osiedleniu. Głuchowski wstąpił do PKPR 1.11.1946."
    },

    # ═══════════════════════════════════════════════════════════════
    # juras_025 — Autentyczny odpis umowy służby
    # ═══════════════════════════════════════════════════════════════
    "juras_025": {
        "typ": "Odpis umowy służby wojskowej",
        "data": "ok. 1946",
        "jezyk": "polski / angielski",
        "nadawca": "P.K.P.R. (Polish Resettlement Corps)",
        "adresat": "Głuchowski Krzysztof",
        "transkrypcja": """AUTENTYCZNY ODPIS UMOWY SŁUŻBY
W WOJSKU STAŁYM

Nr 30043271

Nazwisko: GŁUCHOWSKI
Korpus: Polski Korpus Przysposobienia (Resettlement Corps)

1. Imiona: KRZYSZTOF ANDRZEJ
   Nazwisko: GŁUCHOWSKI
2. Gmina: Hamrawa, Powiat: Hamsawa, Województwo: Warszawa
3. (a) Czy jest Pan obywatelem brytyjskim: NIE
   (b) Narodowość rodziców: ojciec — polska, matka — polska
4. Jaki jest Pana zawód: Uczeń
5. (a) Ile Pan miał lat: 19
   (b) dzień, miesiąc, rok urodzenia: 29-11-1926
6. (a) Czy Pan jest żonaty: NIE
7. Czy Pan obecnie służy w Royal Navy, Royal Air Force: NIE
9. Czy podał Pan zgodnie z prawdą wszystkie dane: Tak
10. Czy chce Pan poddać się szczepieniu ochronnym: Tak
11. Czy chce Pan służyć w Polskim Korpusie Przysposobienia: Tak
12. Czy chce Pan służyć przez okres 2 lat: Tak
13. Czy otrzymał Pan pisemnie pouczenie o zobowiązaniach: Tak

Nazwisko WYCIGA, Rodzaj Wojska PRC
GŁUCHOWSKI KRZYSZTOF d/opl. uroczyście oświadczam...

[podpis] Głuchowski (Podpis zgłaszającego się)
[podpis] Wycig ppor. (Podpis świadka)

ZAŚWIADCZENIE URZĘDNIKA LUB OFICERA
PRZYJMUJĄCEGO ZOBOWIĄZANIE DO SŁUŻBY""",
        "pieczecie": ["Pieczątka PARC (Polish Army Records Centre?)"],
        "podpisy": ["Podpis Głuchowskiego przy zaciągu"],
        "osoby": ["Krzysztof Głuchowski (ur. 19.11.1926, nr 31043371)"],
        "znaki_szczegolne": [
            "Numer służbowy: 31043371",
            "Data urodzenia POTWIERDZONA: 19 listopada 1926",
            "Formularz dwujęzyczny (polsko-angielski)",
            "Pieczątka PARC — Polish Army Records Centre",
            "Dokument potwierdzający dobrowolne wstąpienie do służby"
        ],
        "kontekst": "Odpis umowy o dobrowolną służbę w PKPR. Potwierdza datę urodzenia Krzysztofa: 19 listopada 1926 r. Numer służbowy 31043371. Dokument przejściowy między PSZ a PKPR."
    },

    # ═══════════════════════════════════════════════════════════════
    # juras_026 — Wyciąg z La Courtine (Francja)
    # ═══════════════════════════════════════════════════════════════
    "juras_026": {
        "typ": "Wyciąg z akt wojskowych",
        "data": "15 listopada 1946",
        "jezyk": "polski",
        "nadawca": "Szef Polskiej Wojskowej Misji Likwidacyjnej we Francji",
        "adresat": "Obóz Wojska Polskiego, La Courtine",
        "transkrypcja": """WYCIĄG

La Courtine, dnia 15.11.46.

OBÓZ WOJSKA POLSKIEGO
L.dz.8916/bw/46.

Głuchowski pohr.—

SZEF POLSKICH WOJSKOWYCH MISJI
LIKWIDACYJNEJ WE FRANCJI

PART.

Na rozkaz L.dz.7003/96/46 z dnia 18.10.46 melduję, że

1. st.ułan Głuchowski Krzysztof-Andrzej, r.1926, skreślony
   ze stanu Obozu z dniem 10.7.46.
2. ..........
3. ..........

wymienieni nie posiadają w tut. obozie żadnych dokumentów
osobistych.

                                    Dowódca Obozu
                                    (-) Kotarba
                                    pułkownik.

Za zgodność wyciągu:
szef okręgowego
J. Szmoczynski [podpis]""",
        "pieczecie": [],
        "podpisy": ["Pułkownik Kotarba — Dowódca Obozu La Courtine", "J. Szmoczynski — szef okręgowy"],
        "osoby": [
            "Krzysztof-Andrzej Głuchowski (st. ułan, r. 1926, skreślony z obozu)",
            "Pułkownik Kotarba (dowódca obozu La Courtine)",
            "J. Szmoczynski (szef okręgowy)"
        ],
        "znaki_szczegolne": [
            "Stopień wojskowy: STARSZY UŁAN — kawaleria!",
            "Pełne imię: Krzysztof-Andrzej",
            "Rok urodzenia potwierdzony: 1926",
            "Skreślony ze stanu obozu: 10 lipca 1946",
            "NIE POSIADA dokumentów osobistych — utracone podczas wojny!",
            "La Courtine — obóz likwidacyjny we Francji (departament Creuse)",
            "Polska Misja Wojskowa Likwidacyjna — instytucja zamykająca sprawy PSZ we Francji"
        ],
        "kontekst": "Wyciąg z akt obozu polskiego w La Courtine (Francja, departament Creuse). Głuchowski miał stopień STARSZEGO UŁANA — czyli służył w kawalerii. Został skreślony ze stanu obozu 10.07.1946, co oznacza przeniesienie (prawdopodobnie do Włoch lub Wielkiej Brytanii). Kluczowa informacja: NIE POSIADA dokumentów osobistych — utracone podczas wojny. To wyjaśnia, dlaczego w kolekcji jest tak wiele duplikatów zaświadczeń."
    },

    # ═══════════════════════════════════════════════════════════════
    # juras_027 — List z Polskiej Misji Wojskowej w Paryżu
    # do Generała Głuchowskiego w Londynie
    # ═══════════════════════════════════════════════════════════════
    "juras_027": {
        "typ": "Pismo urzędowe (Misja Wojskowa → Generał)",
        "data": "23 listopada 1946",
        "jezyk": "polski",
        "nadawca": "Polska Misja Wojskowa, Paryż (14, rue de Castiglione)",
        "adresat": "Pan Gen. dyw. Janusz Głuchowski, Sztab Główny, LONDYN",
        "transkrypcja": """POLSKA MISJA WOJSKOWA
LIKWID. WE FRANCJI
L.dz. 7003/01/46.

Paryż, dnia 23 listopada 1946r.
14, Rue de Castiglione.

PAN GENERAŁ GŁUCHOWSKI
Sztab Główny
LONDYN

Szanowny Panie Generale,

Przedstawiam Panu Generałowi wyciąg z meldunku Dcy Obozu
Polskiego w La Courtine, który przejął sprawy b. Obozu ko-
misarz Bessieres. Mimo poszukiwań nie natrafiono na ślady dokumen-
tów osobistych st.uł. GŁUCHOWSKI Krzysztof-Andrzej.

                    Szef Misji Wojskowej
[podpis] A. Szymański
płk.dypl.""",
        "pieczecie": ["Pieczątka POLSKA MISJA WOJSKOWA LIMITED WE FRANCJI"],
        "podpisy": ["Podpis oficera Misji Wojskowej (nieczytelny)"],
        "osoby": [
            "Gen. dyw. Janusz Głuchowski (adresat — Sztab Główny, Londyn)",
            "Krzysztof-Andrzej Głuchowski (starszy ułan — przedmiot pisma)",
            "Komisarz Beselerez (?) — prowadził sprawy obozu La Courtine"
        ],
        "znaki_szczegolne": [
            "KLUCZOWY DOKUMENT — potwierdza POKREWIEŃSTWO",
            "Gen. dyw. Janusz Głuchowski w Sztabie Głównym w Londynie szuka dokumentów Krzysztofa-Andrzeja",
            "Polska Misja Wojskowa w Paryżu — 14, rue de Castiglione (prestiżowy adres)",
            "Dowód, że GENERAŁ osobiście interweniował w sprawie zaginionych dokumentów krewnego",
            "Wyjaśnia kontekst rodzinny: Krzysztof jest prawdopodobnie SYNEM lub BRATANKIEM generała",
            "Pieczątka: 'POLSKA MISJA WOJSKOWA LIMITED WE FRANCJI'",
            "Ton pisma oficjalny ale z szacunkiem ('Szanowny Panie Generale')"
        ],
        "kontekst": "Pismo z Polskiej Misji Wojskowej w Paryżu do Generała Głuchowskiego w Londynie. Generał Juliusz Głuchowski (1888–1964) — generał brygady, szef sztabu, wiceminister spraw wojskowych 1935–1939 — prawdopodobnie ojciec lub bliski krewny Krzysztofa-Andrzeja. Generał interweniuje w sprawie zaginionych dokumentów osobistych młodego żołnierza z obozu La Courtine. Dokument potwierdza, że Krzysztof był pod opieką wysoko postawionego krewnego."
    },

    # ═══════════════════════════════════════════════════════════════
    # juras_028-029 — Kwestionariusz osobisty (pusty formularz)
    # ═══════════════════════════════════════════════════════════════
    "juras_028": {
        "typ": "Kwestionariusz osobisty (formularz POUFNE)",
        "data": "ok. 1946-1948",
        "jezyk": "polski",
        "nadawca": "Administracja wojskowa",
        "adresat": "Żołnierz PSZ / PKPR",
        "strony": ["juras_028_page29.png", "juras_029_page30.png"],
        "transkrypcja": """KWESTIONARIUSZ OSOBISTY    QUESTIONNAIRE FOR POLISH RECORDS    POUFNE

A. DANE OSOBISTE:
1. Nazwisko / Imiona
2a. Imię Ojca / Panieńskie Nazwisko Matki
4. Mężczyzna / Kobieta
5. Stopień Wojskowy: Polski / Brytyjski / Kod
6. Nr Ewidencyjny/Wojsk.: Polski / Brytyjski
7. Stosunek do Służby Wojskowej / Kod
8. Data Urodzenia (Dzień/Miesiąc/Rok) / Miejsce Urodzenia i Kraj
9. Obywatelstwo
10. Kawaler/Panna / Żonaty/Zamężna / Rozwiedziony/na / Wdowiec/wa / Ilość Dzieci
11. Kategoria Zdrowia
12. Czy jesteś Członkiem Stowarzyszenia Polskich Kombatantów
13. Podaj numer twego koła Stowarzyszenia Polskich Kombatantów
14. Nr poczty polowej oddziału
15. Prywatny stały Adres

B. WYKSZTAŁCENIE CYWILNE:
16. Podaj datę opuszczenia ostatniej szkoły lub uczelni wyższej
    [Tabela: Nazwa szkoły | Przedmiot główny | Uzyskane świadectwo | Uczęszczał od-do]
17. Kursy dokształcające
    [Tabela: Czego uczył się | Nazwa kursu i instytucji | Uzyskane świadectwo | Czas]

[Formularz niewypełniony]""",
        "pieczecie": [],
        "podpisy": [],
        "osoby": [],
        "znaki_szczegolne": [
            "Formularz POUFNE — dane osobowe żołnierzy",
            "Rubryki o zawodzie, wykształceniu, rodzinie, językach",
            "Część II: petycje, plany po demobilizacji",
            "Formularz drukowany, niewypełniony lub słabo czytelny",
            "Dokument procesu demobilizacyjnego PSZ"
        ],
        "kontekst": "Standardowy kwestionariusz osobisty używany przy demobilizacji PSZ. Zbierał dane potrzebne do osiedlenia żołnierzy: wykształcenie, zawód, języki, plany na przyszłość."
    },

    # ═══════════════════════════════════════════════════════════════
    # juras_035 — ŚWIADECTWO DOJRZAŁOŚCI (Matura) ze zdjęciem!
    # ═══════════════════════════════════════════════════════════════
    "juras_035": {
        "typ": "Świadectwo dojrzałości (Matura)",
        "data": "ok. 1947-1948",
        "jezyk": "polski",
        "nadawca": "Dział Oświaty, Komitet Koordynacyjny (?)",
        "adresat": "Głuchowski Krzysztof",
        "transkrypcja": """DZIAŁ OŚWIATY
Komitetu dla Spraw Oświaty Polaków w W. Brytanii
TYMCZASOWEGO KOMITETU TREASURY DLA SPRAW POLSKICH

KOMISJA EGZAMINACYJNA

ŚWIADECTWO DOJRZAŁOŚCI

Głuchowski     Krzysztof
(imię i nazwisko)

urodzony d. dnia 29 miesiąca listopada
roku 1926 w m. Hamrawa
województwa Warszawskiego
wyznania rzym.-kat.
po ukończeniu nauki w Gimnazjum

[ZDJĘCIE — fotografia portretowa Krzysztofa Głuchowskiego:
młody mężczyzna, ciemne włosy, wąska twarz, poważny wyraz]

z Liceum S.W.P.N.
do którego był przyjęty w 1945 roku
zdawał w terminie 16 Lipca 1947

zwyczajny egzamin dojrzałości wydziału matematyczno-fizycznego
wobec Komisji Egzaminacyjnej, powołanej Komitet do Spraw Oświaty
Polaków w W. Brytanii pismem
L.dz. II/10/05/97 dnia 4 Lipca 1947r. otrzymuję następujące
oceny ostateczne z przedmiotów egzaminacyjnych:

z religii:                              dobry
z języka polskiego:                     bardzo dobry
z języka łacińskiego:                   —
z języka angielskiego:                  dobry
z historii wraz z nauką o Polsce współczesnej: dostateczny
z matematyki:                           dobry
z fizyki wraz z chemią:                 dostateczny""",
        "pieczecie": ["Pieczęć Działu Oświaty"],
        "podpisy": ["Podpisy komisji egzaminacyjnej"],
        "osoby": ["Krzysztof Głuchowski (ur. 1926, maturzysta)"],
        "znaki_szczegolne": [
            "ZAWIERA FOTOGRAFIĘ KRZYSZTOFA GŁUCHOWSKIEGO — jedyne zdjęcie w kolekcji!",
            "Świadectwo DOJRZAŁOŚCI = polska MATURA",
            "Data urodzenia potwierdzona: 1926",
            "Matura zdana na emigracji — prawdopodobnie w ramach PKPR lub przy 3 DSK",
            "Zdjęcie: młody mężczyzna, ciemne włosy, poważny",
            "Dokument kluczowy — potwierdzenie pełnego wykształcenia średniego"
        ],
        "kontekst": "Świadectwo dojrzałości (matura) Krzysztofa Głuchowskiego. JEDYNY dokument w kolekcji zawierający jego fotografię. Matura zdana na emigracji, prawdopodobnie w ramach programu edukacyjnego PKPR lub przy liceum 3 DSK. Zdjęcie pokazuje młodego mężczyznę, ok. 20-22 lat."
    },

    # ═══════════════════════════════════════════════════════════════
    # juras_036 — Wynik egzaminu komisji egzaminacyjnej
    # ═══════════════════════════════════════════════════════════════
    "juras_036": {
        "typ": "Protokół egzaminu",
        "data": "ok. 1947",
        "jezyk": "polski",
        "nadawca": "Komisja Egzaminacyjna",
        "adresat": "Głuchowski Krzysztof-Andrzej",
        "transkrypcja": """[Strona 2 Świadectwa Dojrzałości — verso]

Poza tym uzyskał jako ostatnie oceny roczne w klasach I-III
(lub odpowiednie oceny na egzaminie wstępnym do wymienionego liceum)
z przedmiotów następujących:

z biologii:                    dostateczny
z propedeutyki filozofii:      dobry
z zagadnień życia współczesnego: dobry
z ćwiczeń cielesnych:          dobry

Komisja Egzaminacyjna uznała Głuchowskiego Krzysztofa
za dojrzałego do studiów wyższych i wydaje niniejsze świadectwo.
Bodney, Anglia dnia 16 Lipca 1947 roku.
Nr 29

PRZEWODNICZĄCY
KOMISJI EGZAMINACYJNEJ
mgr D. Raciborski

[pieczęć okrągła — I POLSKIE LICEUM... M.P.]

CZŁONKOWIE
KOMISJI EGZAMINACYJNEJ:
[podpis 1] K. [nieczytelny]
[podpis 2] A. Amara
[podpis 3] J. Turczyk
[podpis 4] G.H. Fink R.
[podpis 5] J.S. Eddy B.Sc(hons)
[podpis 6] Kleyszolski
[podpis 7] Fm. Mirowski F.
[podpis 8] Wodziński W.
[podpis 9] Henry Piotrkó""",
        "pieczecie": ["Pieczęć okrągła komisji egzaminacyjnej (M.P.)"],
        "podpisy": ["Przewodniczący komisji + 7 członków"],
        "osoby": ["Krzysztof-Andrzej Głuchowski (egzaminowany)"],
        "znaki_szczegolne": [
            "Pełna komisja egzaminacyjna — przewodniczący + 7 członków",
            "Pieczęć urzędowa M.P.",
            "Nazwiska komisji trudne do odczytu",
            "Wynik: dostateczny / dobry",
            "Powiązany ze świadectwem dojrzałości (juras_035)"
        ],
        "kontekst": "Protokół egzaminu dojrzałości z wynikami i podpisami pełnej komisji egzaminacyjnej. Powiązany ze świadectwem juras_035."
    },

    # ═══════════════════════════════════════════════════════════════
    # juras_037 — DISCHARGE CERTIFICATE (Zwolnienie z PKPR)
    # ═══════════════════════════════════════════════════════════════
    "juras_037": {
        "typ": "Certyfikat zwolnienia ze służby (Discharge Certificate)",
        "data": "31 października 1948",
        "jezyk": "angielski",
        "nadawca": "Polish Resettlement Corps, Record Office, Witley Camp",
        "adresat": "Głuchowski Krzysztof",
        "transkrypcja": """DISCHARGE CERTIFICATE.    Army Form B108J
(If this Certificate is lost no duplicate can be obtained.)

1. Army No.: 30043271
2. Surname: GŁUCHOWSKI
3. First Names: KRZYSZTOF
4. Effective Date of Discharge: 31 OCT 1948
5. Corps from which Discharged: P.R.C.
6. Rank on Discharge: L/Cpl. (Lance Corporal)
7. Service with the Colours: Years 3, Days —
8. Service on Class W(T) Reserve: Years —, 363 Days, 2
9. Total Service: [puste]
10. Cause of Discharge: K.R. 3097 para XIX(b) His services being no
    longer required on completion of contract
11. Campaigns and Military Conduct: Service Abroad
12. Medals: [puste]
13. Military Conduct: [puste]

50748

[podpis] A. Montwice [?]
Signature and Rank, Officer i/c Records.

Date: 31 OCT 1948

[Pieczątka:]
POLISH RESETTLEMENT CORPS
RECORD OFFICE
WITLEY CAMP
31 OCT 1948""",
        "pieczecie": [
            "POLISH RESETTLEMENT CORPS RECORD OFFICE WITLEY CAMP — pieczątka z datą 31 OCT 1948"
        ],
        "podpisy": ["Podpis oficera zwalniającego", "Podpis Głuchowskiego"],
        "osoby": ["Krzysztof Głuchowski (nr 3004271, Private, zwolniony 31.10.1948)"],
        "znaki_szczegolne": [
            "KONIEC SŁUŻBY WOJSKOWEJ — 31 października 1948",
            "Nr służbowy: 3004271 (ten sam co na certyfikacie PKPR juras_060)",
            "Stopień: PRIVATE (Pte.) — odpowiednik szeregowego",
            "Witley Camp, Surrey — główny obóz demobilizacyjny PKPR",
            "Nr dokumentu: 50748",
            "Formularz w okładce skórzanej (książeczka wojskowa)"
        ],
        "kontekst": "Certyfikat zwolnienia ze służby w PKPR. Data 31.10.1948 oznacza koniec drogi wojskowej Krzysztofa — dokładnie 2 lata po wstąpieniu do PKPR (1.11.1946). Od tego momentu Głuchowski jest cywilnym rezydentem Wielkiej Brytanii. Witley Camp w Surrey służył jako centrum demobilizacyjne dla tysięcy polskich żołnierzy."
    },

    # ═══════════════════════════════════════════════════════════════
    # juras_040 — Brytyjska książeczka wojskowa (Soldier's Pay Book)
    # ═══════════════════════════════════════════════════════════════
    "juras_040": {
        "typ": "Soldier's Pay Book / Service Book (brytyjski)",
        "data": "1945-1948",
        "jezyk": "angielski",
        "nadawca": "British Army / Polish Forces under British Command",
        "adresat": "Głuchowski Krzysztof",
        "transkrypcja": """[Strony 2-3 otwartej książeczki:]

2                                    3
(1) SOLDIER'S NAME and DESCRIPTION on ATTESTATION.

Army Number: 14161026 [nieczytelne]
Surname (in capitals): GŁUCHOWSKI
Christian Names: KRZYSZTOF
Date of Birth: 19. 11. 19[20/26?]
[puste] Polish
Place of    In or near the town of
Birth:      [puste] ber zawar [Brzeżany?]
            In the county [puste]
Trade on Enlistment: [puste]

Nationality of Father at birth: [puste] Polnish [nieczytelne]
Nationality of Mother at birth: Izyni - Kat [nieczytelne]
Religious Denomination: [puste]
Approved Society: [puste]
Membership No.: [puste]
Enlisted at [puste] On the [puste] Naib.Ib.[nieczytelne]
Regular Army □   Supplementary Reserve □
[puste] Strike out those inapplicable [puste]
For ... years with the Colours and ... years in the
Reserve.
Signature of Soldier: [podpis] Głuchowski
Date: 20. X. 1945

[OPIS FIZYCZNY — strona 3:]
Height: 170 [nieczytelne]   ins. Weight: 50 [nieczytelne] lbs.
Maximum Chest: [puste] ins. Complexion: [puste]
Markings: [puste] Hair: I. Kaita [nieczytelne] Eye: I. Kloma [nieczytelne]
Distinctive Marks and Minor Defects: [puste]

                    DISCHARGED

CONDITION ON TRANSFER TO RESERVE: [puste]""",
        "pieczecie": ["Stempel DISCHARGED (duży, niebieski)"],
        "podpisy": ["Podpis Krzysztofa Głuchowskiego (20.X.1945)"],
        "osoby": ["Krzysztof Głuchowski (nr 14161026?, ur. 19.11, miejsce: Brzeżany?)"],
        "znaki_szczegolne": [
            "BRYTYJSKA KSIĄŻECZKA WOJSKOWA — Soldier's Pay Book",
            "Dwie daty: zaciąg 20.X.1945, stempel DISCHARGED (późniejszy)",
            "Wzrost: ok. 170 cm, waga: ok. 50 lbs (23 kg? — chyba błędny wpis lub 150 lbs)",
            "Miejsce urodzenia: 'ber zawar' — prawdopodobnie BRZEŻANY (dziś Bereżany, Ukraina)",
            "Ojciec — narodowość polska",
            "Matka — 'Izyni-Kat' — być może Iżyna z Kut? (nazwisko panieńskie i miejsce?)",
            "Dokument BARDZO ważny biograficznie — dane fizyczne + miejsca urodzenia"
        ],
        "kontekst": "Brytyjska książeczka wojskowa (Soldier's Pay Book) Krzysztofa Głuchowskiego. Miejsce urodzenia 'ber zawar' to prawdopodobnie BRZEŻANY — miasto w województwie tarnopolskim (Kresy Wschodnie, dziś Ukraina). To wyjaśnia losy rodziny: Kresy → ewakuacja → armia → emigracja. Data zaciągu 20.X.1945 — tuż po zakończeniu wojny."
    },

    # ═══════════════════════════════════════════════════════════════
    # juras_040-044 — Soldier's Service and Pay Book (komplet)
    # ═══════════════════════════════════════════════════════════════
    "juras_041": {
        "typ": "Książeczka wojskowa — strony medyczne",
        "data": "1945-1948",
        "jezyk": "angielski",
        "nadawca": "British Army",
        "adresat": "Głuchowski Krzysztof",
        "strony": ["juras_041_page42.png"],
        "transkrypcja": """[Strony 8-9: Medical Classification & Vaccinations]

MEDICAL CLASSIFICATION:
Category: A1
Date: 10.11.45

PRESCRIPTION FOR GLASSES: [puste]

VACCINATIONS:
S.P.E. / S.P.T. [daty]

PROTECTIVE INOCULATIONS:
T.A.B. [tyfus-paratyfus]:
  Dates: 1945
  [wpisy medyczne z datami]

Name of Vaccine: T.A.B.
Army Form: T.P.9""",
        "pieczecie": [],
        "podpisy": ["Podpisy lekarzy wojskowych"],
        "osoby": ["Krzysztof Głuchowski"],
        "znaki_szczegolne": [
            "Kategoria medyczna A1 — pełna zdolność do służby",
            "Szczepienia: T.A.B. (tyfus) — obowiązkowe w armii",
            "Daty medyczne: grudzień 1945",
            "Wpisy czytelne — dokumentacja medyczna zachowana"
        ],
        "kontekst": "Strony medyczne książeczki — szczepienia i klasyfikacja zdrowotna. Kategoria A1 = pełna zdolność. Szczepienia T.A.B. przeciw tyfusowi — standard w armii."
    },

    "juras_042": {
        "typ": "Okładka książeczki wojskowej",
        "data": "1945-1948",
        "jezyk": "angielski",
        "nadawca": "British Army",
        "adresat": "Głuchowski Krzysztof",
        "transkrypcja": """ARMY BOOK 64.

SOLDIER'S SERVICE
AND
PAY BOOK.""",
        "pieczecie": [],
        "podpisy": [],
        "osoby": ["Krzysztof Głuchowski"],
        "znaki_szczegolne": [
            "Okładka ARMY BOOK 64 — standardowa książeczka brytyjska",
            "Skórzana oprawa, zużyta — noszony przy sobie przez lata",
            "Najważniejszy dokument identyfikacyjny żołnierza"
        ],
        "kontekst": "Okładka standardowej brytyjskiej książeczki wojskowej Army Book 64."
    },

    "juras_043": {
        "typ": "Tabela odznaczeń wojennych (Campaign Stars & Medals)",
        "data": "1945-1948",
        "jezyk": "angielski",
        "nadawca": "British Army",
        "adresat": "Głuchowski Krzysztof",
        "transkrypcja": """Campaign Stars, Clasps and Medals
instituted in recognition of service
in the war of 1939-45

NUMBER OF STARS, MEDALS,
CLASPS & EMBLEMS ENCLOSED: 0 - 1 - 0

[Tabela odznaczeń:]
1. 1939-45 Star
2. Atlantic Star
3. Air Crew Europe Star
4. Africa Star (incl. France and Germany clasp)
5. Pacific Star (8th Army or 1st Army or North Africa 1942-43)
6. Burma Star
7. Italy Star
8. France and Germany Star
9. Defence Medal
10. War Medal 1939-45

[Opis wstążek i kolorów dla każdego odznaczenia]
Oak Leaf — dla wyróżnionych w rozkazach""",
        "pieczecie": [],
        "podpisy": [],
        "osoby": ["Krzysztof Głuchowski"],
        "znaki_szczegolne": [
            "TABELA ODZNACZEŃ — druk w książeczce wojskowej",
            "Wpis 0-1-0: Krzysztof otrzymał JEDNO odznaczenie/klamerka",
            "Prawdopodobnie ITALY STAR lub DEFENCE MEDAL",
            "Pełna lista Campaign Stars z II WŚ",
            "Kolorowe opisy wstążek (tekst czerwony + czarny)"
        ],
        "kontekst": "Tabela odznaczeń wojennych z książeczki. Wpis '0-1-0' oznacza jedno odznaczenie — prawdopodobnie Italy Star (za służbę we Włoszech) lub Defence Medal."
    },

    "juras_044": {
        "typ": "Odznaka / Emblemat wojskowy",
        "data": "ok. 1945-1948",
        "jezyk": "—",
        "nadawca": "—",
        "adresat": "—",
        "transkrypcja": """[Fotografia odznaki/emblematu:
Brązowa odznaka z herbem lub orłem polskim,
ozdobny wzór, prawdopodobnie metalowa wpinka mundurowa]""",
        "pieczecie": [],
        "podpisy": [],
        "osoby": [],
        "znaki_szczegolne": [
            "Metalowa odznaka/emblemat — brąz/miedź",
            "Prawdopodobnie Orzeł Polski lub herb jednostki",
            "Wpinka mundurowa — noszona na klapie lub czapce",
            "Zachowana osobno od munduru"
        ],
        "kontekst": "Odznaka mundurowa — prawdopodobnie orzeł polski lub emblemat jednostki. Żołnierze PSZ nosili polskie emblematy na brytyjskich mundurach."
    },

    # ═══════════════════════════════════════════════════════════════
    # juras_065 — Alien Registration Certificate (Wielka Brytania)
    # ═══════════════════════════════════════════════════════════════
    "juras_065": {
        "typ": "Alien Registration Certificate (rejestracja cudzoziemca)",
        "data": "ok. 1948-1950",
        "jezyk": "angielski",
        "nadawca": "Buckinghamshire Police / Home Office",
        "adresat": "Głuchowski Krzysztof",
        "transkrypcja": """[Formularz brytyjski — Alien Registration]

ALIEN REGISTRATION CERTIFICATE
No. 247254 [?]

[...] Corporation Street, High Wycombe, Bucks.

[Pieczątka okrągła:]
BUCKINGHAMSHIRE POLICE
ALIENS REGISTRATION

[...daty i adnotacje...]

[Tekst formularza:]
This Order is to be in your possession at all times [...]
Under the Aliens Order [...] and National Service Acts [...]
[...] Polish Resettlement Corps [...] or Polish [...] Forces [...]""",
        "pieczecie": [
            "Pieczątka BUCKINGHAMSHIRE POLICE — ALIENS REGISTRATION",
            "Pieczątka Home Office / urzędu rejestracji"
        ],
        "podpisy": ["Podpis urzędnika rejestracyjnego"],
        "osoby": ["Krzysztof Głuchowski (zarejestrowany jako alien / cudzoziemiec)"],
        "znaki_szczegolne": [
            "ALIEN REGISTRATION — dokument potwierdzający status cudzoziemca w UK",
            "Adres: Corporation Street, HIGH WYCOMBE, Buckinghamshire",
            "Nr rejestracji: 247254",
            "High Wycombe — miasto ok. 50 km od Londynu",
            "Po zwolnieniu z PKPR Krzysztof zamieszkał w High Wycombe",
            "Pieczątka policyjna — obowiązek rejestracji cudzoziemców",
            "Wzmianka o Polish Resettlement Corps i Polish Forces"
        ],
        "kontekst": "Certyfikat rejestracji cudzoziemca (Alien Registration) wydany przez policję Buckinghamshire. Po zwolnieniu z PKPR (31.10.1948), Krzysztof zamieszkał w HIGH WYCOMBE koło Londynu jako zarejestrowany cudzoziemiec. Polscy żołnierze musieli rejestrować się jako 'aliens' — mimo walki za Wielką Brytanię. High Wycombe — tam też stacjonowały jednostki RAF, w tym polskie dywizjony."
    },

    # ═══════════════════════════════════════════════════════════════
    # juras_075 — Gazeta "Życie Tygodnia" (strona obozowa)
    # ═══════════════════════════════════════════════════════════════
    "juras_075": {
        "typ": "Gazeta obozowa 'Życie Tygodnia'",
        "data": "ok. 1946-1947",
        "jezyk": "polski",
        "nadawca": "Redakcja 'Życie Tygodnia'",
        "adresat": "Żołnierze PSZ",
        "transkrypcja": """ŻYCIE TYGODNIA   [numer] KWIECIEŃ 194[6/7]

CZYTELNICY PISZĄ
[...] Andrew Mackie 1st Bn Borders [...] Polish Forces [...]

[Zdjęcie: kobieta w ujęciu filmowym/teatralnym]

Jak można się do niej zgłosić [...]
Obetris [?] Fot. [fotografia]

WĘDROWI[?] RZĄD POLSKI
[...artykuł o rządzie polskim na emigracji...]

SKRZYNKA POCZTOWA
[Adresy korespondencyjne:]
Do Spo- [?] sęsno Tygodnie 12 sąd [...]
[m in?] Odpowiedzia [...] Ter. 13838

Żydki, Głuchowski, Stołls, Polish
Forces C. M.[?] Strath [?]
[...adresy wojskowe...]

GDZIE JEST TWA BAZA?
[...artykuł lub ogłoszenie...]

C.M.F. 501 [Central Mediterranean Forces]""",
        "pieczecie": [],
        "podpisy": [],
        "osoby": ["Głuchowski (wymieniony w skrzynce pocztowej!)"],
        "znaki_szczegolne": [
            "GAZETA 'ŻYCIE TYGODNIA' — tygodnik obozowy",
            "GŁUCHOWSKI wymieniony w skrzynce pocztowej — szukał korespondencji!",
            "C.M.F. 501 — Central Mediterranean Forces (Włochy)",
            "Zdjęcia — druk ilustrowany",
            "Sekcja CZYTELNICY PISZĄ — interaktywna gazeta",
            "Data: KWIECIEŃ — wiosna 1946 lub 1947",
            "Andrew Mackie 1st Bn Borders — żołnierz brytyjski, kontakt"
        ],
        "kontekst": "Gazeta obozowa 'Życie Tygodnia'. NAZWISKO GŁUCHOWSKI pojawia się w skrzynce pocztowej — Krzysztof szukał kontaktu z innymi lub odpowiadał na ogłoszenia. C.M.F. 501 — ten sam rejon co C.M.F. 105 z aerogramu (dok. 001). Gazeta świadczy o aktywnym życiu intelektualnym w obozach."
    },

    # ═══════════════════════════════════════════════════════════════
    # juras_085 — List po francusku (z okresu La Courtine?)
    # ═══════════════════════════════════════════════════════════════
    "juras_085": {
        "typ": "List odręczny (po francusku lub polsku)",
        "data": "ok. 1946",
        "jezyk": "polski (z elementami francuskimi?)",
        "nadawca": "Krzysztof Głuchowski (?)",
        "adresat": "Nieustalony",
        "transkrypcja": """[Notatka odręczna, 2 strony:]

Stożyque de Granceków [?]
Opodas w moay, a w telize poki to eleria

[...tekst odręczny, trudny do odczytu...]

Główczyn [?] wiezy takich prasza, leistyr przekrosenin
Głuchidzy [...] stely przero, viechis[?] czekotanin yar [?]

[...dalszy tekst...]

Do naszn unarnd poch ś łeg praklekh ile racij umazieln
[...]

[Druga strona:]
[...] Powichylanie [?] o przesyferenoi [...] be duostape
[...]
Latcyz [?] a Buxky Maszino o polscz przeckownosc naj bogan
Gody et de Moszowskyo stołbosn walischeszn[?]
[...]
Subse pel siebiś lisze [...] nieczyrzenki i stopach e[...]
ne 1550 [...] niesszaknein [...]""",
        "pieczecie": [],
        "podpisy": [],
        "osoby": [],
        "znaki_szczegolne": [
            "Pismo odręczne — bardzo trudne do odczytu",
            "Możliwe elementy francuskie (okres La Courtine?)",
            "Wymieniona cyfra 1550 — może kwota lub numer",
            "Notatka o charakterze osobistym lub biznesowym",
            "Wymaga profesjonalnej transkrypcji HTR"
        ],
        "kontekst": "Notatka odręczna, prawdopodobnie z okresu pobytu Krzysztofa we Francji (La Courtine). Elementy językowe sugerują mieszankę polskiego z wpływami francuskimi — typowe dla żołnierzy polskich stacjonujących we Francji."
    },

    # ═══════════════════════════════════════════════════════════════
    # juras_045 — Notatki (daty służby i numery)
    # ═══════════════════════════════════════════════════════════════
    "juras_045": {
        "typ": "Notatki odręczne (daty służby)",
        "data": "ok. 1946",
        "jezyk": "polski",
        "nadawca": "Krzysztof Głuchowski (prawdopodobnie)",
        "adresat": "—",
        "transkrypcja": """[Notatki na papierze w kratkę, charakter odręczny:]

[Lewa strona:]
54/7533
94/46

Ryt. 19-VII-46

D. [dywizja?] 3 DSK
12. XI. 46

[Prawa strona:]
155/46

Wauty[?] skontro[?]:
    uj li żwo Mandavi[?] 1944
    1134/II AK./46
    [data] 12 VI 1946

Mali wolna:
    [...]

Rospi. [?] pro Ditvo 2 Kopr.[?]

22. IX. 1946""",
        "pieczecie": [],
        "podpisy": [],
        "osoby": ["Krzysztof Głuchowski (pisał notatki)"],
        "znaki_szczegolne": [
            "Notatki osobiste — numery dokumentów i daty",
            "Daty: 19.VII.46, 12.XI.46, 12.VI.1946, 22.IX.1946",
            "3 DSK — 3 Dywizja Strzelców Karpackich",
            "Numery akt: 54/7533, 94/46, 155/46, 1134/II AK./46",
            "Papier w kratkę — notatnik żołnierski",
            "Prawdopodobnie spis dokumentów potrzebnych do akt osobowych"
        ],
        "kontekst": "Notatki Krzysztofa z numerami dokumentów wojskowych i datami. Prawdopodobnie spisywał numery potrzebne do odtworzenia akt osobowych (które zaginęły w La Courtine)."
    },

    # ═══════════════════════════════════════════════════════════════
    # juras_050 — Dokument prawny (prawo polskie, testamenty)
    # ═══════════════════════════════════════════════════════════════
    "juras_050": {
        "typ": "Informator prawny (prawo spadkowe)",
        "data": "ok. 1946-1948",
        "jezyk": "polski",
        "nadawca": "Wydawnictwo prawne (druk urzędowy)",
        "adresat": "Żołnierze PSZ / PKPR",
        "transkrypcja": """WEDŁUG PRAWA POLSKIEGO

Żołnierze znajdujący się w czynnej służbie wojskowej — na terenie
państwowego kraju lub poza [...] do postaćenia
kategorji [...]

1. Według prawa polskiego żołnierze w czynnej służbie wojskowej
   uprawnieni są do praw i obowiązków [...]
   i Rzeczpospolita
2. [...]
3. Kto może być wezwany jako świadek testamentu [...]
   [...] osoby porażone [...] w zakresie Konsulatu [...]
   i mogą porządkować mianą wojskową
4. Kto[?] ma uprawnienie do Marynarki Wojennej [...]
   osoby wchodzące w charakterze kadukarzy[?]
   [...]
5. Testament to pismo, jakch jest sporządzony [...]
   do dokumentu jest główny [...]
   a) każdy wypadek po dobremu [...]
   b) będzie czuło [...] dochodzenie [...] p. 1...
   c) [...]
   d) [...]

P.A.S. 2.17/WB3.41/44""",
        "pieczecie": [],
        "podpisy": [],
        "osoby": [],
        "znaki_szczegolne": [
            "Druk urzędowy — informator o PRAWIE POLSKIM",
            "Dotyczy testamentów wojskowych i prawa spadkowego",
            "Przeznaczony dla żołnierzy na emigracji",
            "Numer druku: P.A.S. 2.17/WB3.41/44",
            "Świadectwo organizacji prawnej emigracji polskiej"
        ],
        "kontekst": "Informator prawny dla żołnierzy polskich na emigracji, dotyczący prawa testamentowego i spadkowego. Żołnierze PSZ potrzebowali regulacji prawnych w sytuacji, gdy nie mogli wrócić do Polski."
    },

    # ═══════════════════════════════════════════════════════════════
    # juras_060 — Certyfikat PRC (Polish Resettlement Corps)
    # ═══════════════════════════════════════════════════════════════
    "juras_060": {
        "typ": "Certyfikat służby PRC",
        "data": "19 lutego 1948",
        "jezyk": "angielski",
        "nadawca": "P.R.C. Record Office, Witley Camp, Surrey",
        "adresat": "Głuchowski Krzysztof",
        "transkrypcja": """P.R.C. Record Office
Witley Camp
nr. Godalming, Surrey
Tel. Godalming 1520 Ext.108

Ref.No. 2135 / 48

                                        19 FEB 1948

                    CERTIFICATE

This is to certify that No. 3004271
L/Cpl. GŁUCHOWSKI KRZYSZTOF was enlisted into
P.R.C. 1.11.46, after serving with Polish Forces
under British Command from 14.7.45 — 1.11.46.

                                        Record Officer
                                        [podpis]
                                        O.P.G.R. Colling[?]
                                        Biuro Ew. P.K.P.""",
        "pieczecie": ["Pieczątka Record Office P.R.C. Witley Camp"],
        "podpisy": ["Record Officer — O.P.G.R. Colling (?)"],
        "osoby": ["Krzysztof Głuchowski (L/Cpl = Lance Corporal, nr 3004271)"],
        "znaki_szczegolne": [
            "KLUCZOWY DOKUMENT CHRONOLOGICZNY:",
            "14.7.1945 — początek służby w Polish Forces under British Command",
            "1.11.1946 — wstąpienie do PKPR (Polish Resettlement Corps)",
            "Stopień: L/Cpl (Lance Corporal = starszy szeregowy / kapral)",
            "Nr służbowy: 3004271",
            "Witley Camp, Godalming, Surrey — centrum administracyjne PKPR",
            "Data certyfikatu: 19 lutego 1948",
            "Biuro Ew. P.K.P. = Biuro Ewidencyjne Polskiego Korpusu Przysposobienia"
        ],
        "kontekst": "Oficjalny certyfikat potwierdzający przebieg służby Krzysztofa Głuchowskiego. Chronologia: Polish Forces (14.7.1945 – 1.11.1946) → P.R.C. (od 1.11.1946, zwolniony 31.10.1948). Witley Camp pod Godalming w Surrey — główne biuro ewidencyjne PKPR, przez które przeszły dziesiątki tysięcy polskich żołnierzy."
    },

    # ═══════════════════════════════════════════════════════════════
    # juras_070 — Fundusz Inwalidów Armii Krajowej (Londyn 1984)
    # ═══════════════════════════════════════════════════════════════
    "juras_070": {
        "typ": "Druk graficzny / Karta okolicznościowa",
        "data": "1984",
        "jezyk": "polski",
        "nadawca": "Fundusz Inwalidów Armii Krajowej, Londyn",
        "adresat": "—",
        "transkrypcja": """FUNDUSZ INWALIDÓW ARMII KRAJOWEJ
KO.O. A.K. LONDYN 1984

[Grafika: Linoryt przedstawiający postać rycerza/żołnierza
w dynamicznej pozie — styl ekspresjonistyczny]

Grafika — Zielma Starkiewicz[?], kombinacja
Drukarz: Arloma[?] Seriografia w Sztuce[?]

KOŁO A.K.""",
        "pieczecie": [],
        "podpisy": ["Zielma Starkiewicz (?) — autorka grafiki"],
        "osoby": ["Gen. dyw. Janusz Głuchowski (prawdopodobny odbiorca / członek)"],
        "znaki_szczegolne": [
            "Fundusz Inwalidów Armii Krajowej — organizacja emigracyjna",
            "Londyn 1984 — wciąż aktywna polska społeczność",
            "Grafika: LINORYT ekspresjonistyczny — wysoka jakość artystyczna",
            "Dowód na kontynuację więzi z AK na emigracji",
            "Kolekcja Głuchowskich sięga aż do lat 80."
        ],
        "kontekst": "Druk graficzny Funduszu Inwalidów Armii Krajowej z Londynu, 1984. Świadczy o tym, że rodzina Głuchowskich utrzymywała więzi z organizacjami kombatanckimi przez dziesięciolecia. Linoryt wykonany w technice serigrafii."
    },

    # ═══════════════════════════════════════════════════════════════
    # juras_080 — Gazeta obozowa (strona kulturalna)
    # ═══════════════════════════════════════════════════════════════
    "juras_080": {
        "typ": "Gazeta obozowa (strona kulturalna)",
        "data": "ok. 1946-1947",
        "jezyk": "polski",
        "nadawca": "Redakcja gazety obozowej",
        "adresat": "Mieszkańcy obozu",
        "transkrypcja": """[Strona gazety obozowej — sekcje:]

MUZYKA
SZEŚCIASTOLENI KOMPOZYTOR
[...] muzyka Oda [...] Gra [...]
Maryna Omas [...] W...

FILM
Co robi Maurice Chevalier
[...]
Greto Garbo jest w Sztocholmie [Sztokholmie]
[artykuł] artystce Hollywoodu [...]

TEATR
[...] SZCLODNERZ I KOMISJA [?]
[artykuł o teatrze]

NOTATKI WYDAWNICZE
CARLOS NOLOMI [?]
[recenzja] Paryż [...] Brazylia [...]

[Zdjęcia: 4 fotografie — Maurice Chevalier,
Greta Garbo (?), aktor teatralny, postać]""",
        "pieczecie": [],
        "podpisy": [],
        "osoby": ["Maurice Chevalier (wspomniany)", "Greta Garbo (wspomniana)"],
        "znaki_szczegolne": [
            "Strona KULTURALNA gazety obozowej",
            "Sekcje: Muzyka, Film, Teatr, Notatki Wydawnicze",
            "Maurice Chevalier i Greta Garbo — gwiazdy tamtej epoki",
            "4 fotografie — druk ilustrowany",
            "Świadectwo kultury masowej w obozach polskich",
            "Żołnierze śledzili kino i teatr światowy"
        ],
        "kontekst": "Strona kulturalna gazety obozowej. Żołnierze polscy w obozach włoskich/brytyjskich śledzili światową kulturę — kino (Chevalier, Garbo), teatr, muzykę. Gazety obozowe pełniły funkcję łącznika ze światem zewnętrznym."
    },

    # ═══════════════════════════════════════════════════════════════
    # juras_088-090 — Kontynuacja listu (strony 3, 4, 5)
    # Część tego samego listu co juras_010 (list wigilijny)
    # ═══════════════════════════════════════════════════════════════
    "juras_088": {
        "typ": "Memorandum polityczne — apel do emigracji polskiej",
        "data": "ok. 1950-te",
        "jezyk": "polski",
        "nadawca": "Krzysztof Głuchowski (lub Stefan/Janusz Głuchowski)",
        "adresat": "Emigracja polska / diaspora",
        "strony": ["juras_088_page89.png", "juras_089_page90.png", "juras_090_page91.png"],
        "transkrypcja": """[Strona 3:]
Obecnie zachodzi, muszę się skarżyć i ani
z ruchami Rządu Rzeczyposp[olitej] z Londynu, ani nie
zapewnia nas do [?] wojska Polskiego.

Wzór[?] powiedzieć!
Krytykę komisji mi na drobne!

Z te[?] ustawy amerykańskie, [?] ostatnio,
to pod tym względem ci [na]większe.

Na mocy jednej ustawy amerykańs[kiej] melduje na te-
ren Niemiec 2500 Ochotników z ponad uchodźców
z poza „Żelaznej kurtyny" do [służby?] [?] [werbunek?]

Bo oddali[?] o fałszywym [?]. —
                                         Ktoś mógłby tu [?]
na mocy tej ustawy imigranci od 18-35 lat
do służby w korpach amer. Czy ja [?] dos, czy
nie chce, czy [?] ja ustawy do emigracji [?],
legalnej by zawiodło; czy zamierza kiedyś ubiegać
się o obywatelstwo amerykańskie, czy też nie.

Na ostatni[?] również muszę[?] zachodzę dobrze
nas [?] ogony, wszak na [?] Kon[?], jedno jest
ma [?] dzieło widoczne całego świata, a
następnie koniecnym[?] która prowadzą [?]
do „Osady" [?]. Nieraz czyta wzrost t.zw. [?]—

[Strona 4:]
[?] „uciśnionych"; a na Zachodzie ciągle pomi-
nięta[?] Aby dogadanie[?] z Kremlem końcem na-
rodów oddalonych z niołu[?].

Nie gnijà również myśleć o [?] Narodu
Polskiego [?] narzędzie[?] porodzie[?] polityczne
doradcy[?]; z porodó być mówić o tych sprawach,
trzeba ani [?], ani patrzenie[?] sytuacja
nie jest dostatnia[?]?

'I jednak!'

Osoba[?] i ty starsi na emigracji [?]
[?] Polskiego; czy to wśród partji politycznych,
czy to wśród organizacji społecznych, których
zagadnienia Narodu Polskiego nie [?].
Dlaczego?

Bo organu[?] wszyscy ze sto [?], że jest
nie porozumienie[?] obecnie nad tó [?], [?]
[?] byli nadżywę[?], że [?] koś[?] i i
[?] nieprawdopodobne zupełnie i jest i to[?]
[może?] nie oczekujemy powrotku[?] Psychicznego[?],
i natchni[ął?] [?] tu [?] [?]—

[Strona 5:]
Która będzie mogła narazić na nas nadcho-
dzących wydarzeń — inni będą [?] forty
[?]; inni będą decydowali o nasz los
nás, o na Polskiejm[?] społeczeństw[ie], który i jak
wiadomo, nigdy nie, [mają?] racji. —

Kiedy, na [?] nasze[?] [?] ulegnie napra-
wę wobec [?] niebezpieczeństwa. — Polacy
muszą [?] jedności i obliczu niebezpieczeństwa.

[Żeby?] także, ów [?] zachodnie będą musiały
robili[?] całe sprawy, o jednym i tych celou i na
[?] zatknie będzie wolności uparolowanych[?] na-
PolsCe[?].

Dlatego postawiłem sobie memoriał do Was
[?].

Dlatego, że nam [?], że należy do reko-
lekcji, która [?]. Być może że i tych [?]
przedstawi[eni]e obejdą[?] [?] [?].

Ale ten wyraz na tó [?] czy polityce, czy [?]-
[?]; czy rzeczywis[tości], czy obywatel, czy nawet
[?] — Polszczyk[?] musisz podjąć pracę i prz-
yjąć odpowiedzialność za losy Narodu.""",
        "pieczecie": [],
        "podpisy": [],
        "osoby": ["Krzysztof Głuchowski (lub Stefan/Janusz Głuchowski) — autor memorandum"],
        "znaki_szczegolne": [
            "MEMORANDUM POLITYCZNE — nie list osobisty! (poprzednia transkrypcja błędna)",
            "Skan obrócony o 270° — tekst napisany pionowo na kartkach",
            "Krytyka Rządu RP na Uchodźstwie z Londynu",
            "Omówienie ustaw amerykańskich o imigracji — 2500 ochotników",
            "Wspomniana 'Żelazna kurtyna' — kontekst zimnowojennej",
            "Werbunek imigrantów 18-35 lat do służby w korpusach amerykańskich",
            "Kwestia obywatelstwa amerykańskiego dla Polaków",
            "Krytyka braku jedności emigracji polskiej",
            "Apel końcowy: 'Polak musisz podjąć pracę i przyjąć odpowiedzialność za losy Narodu'",
            "'Dlatego postawiłem sobie memoriał do Was' — dokument adresowany do organizacji",
            "Strony numerowane 3, 4, 5 — istniały wcześniejsze strony (1-2)"
        ],
        "kontekst": "Memorandum polityczne (strony 3-5, brak stron 1-2) adresowane do polskiej emigracji. Autor krytykuje bierność Rządu RP z Londynu i brak jedności wśród organizacji emigracyjnych. Omawia amerykańskie ustawy imigracyjne i rekrutację uchodźców zza Żelaznej kurtyny do służby wojskowej w USA. Kończy apelem o podjęcie odpowiedzialności za losy Narodu. Datowanie: lata 50-te (kontekst zimnowojennej, ustawy imigracyjne USA, Żelazna kurtyna). Charakter pisma sugeruje Krzysztofa, ale ton i wiedza polityczna mogą wskazywać na gen. Janusza."
    },

    # ═══════════════════════════════════════════════════════════════
    # juras_091-092 — Kwartalnik Biograficzny Polonii (biogramy)
    # ═══════════════════════════════════════════════════════════════
    "juras_091": {
        "typ": "Kwartalnik Biograficzny Polonii — biogramy",
        "data": "ok. 1990-te",
        "jezyk": "polski / angielski",
        "nadawca": "Kwartalnik Biograficzny Polonii",
        "adresat": "—",
        "strony": ["juras_091_page92.png", "juras_092_page93.png"],
        "transkrypcja": """[Strona 1 — biogramy po angielsku, Nr 7:]

GŁUCHOWSKI Janusz Julian (06.08.1888 estate of Bukowa in the Piotrkowski
County – 11.06.1964 London) Lt.-General. Studied at the Polytechnic
of Liège in Belgium. Founder of the Liège branch of the "Active Armed
Struggle Association" in 1909. In 1912 he graduated in Stróże near Cracow
from the officers' course of the Riflemen's Association. 1914-1917 he was
a member of the Polish Legions and took part in the whole campaign fought
by the 1st Brigade. After the "Oath Crisis" in 1917, he was interned in
Beniaminów, then he was transferred to the prison of Werl in Germany.
Between 1918-1920 he was the organiser and commanding officer of the 3rd
Lancers Regiment, renamed the 7th Lublin Lancers Regiment. 1920-1924 he
commanded the 1st Cavalry Brigade and shortly the 4th Cavalry Division.
He was promoted major-general in 1927. Commandant of the Academy of War
Studies 1930-1933; GOC X Military District of Przemyśl 1933-1935; 1st
Vice-Minister of Military Affairs 1935-1939. After the September Campaign,
he reached France through Romania. He was Special G.O.C. Officer to the
Polish Commander-in-Chief in 1940-1941; GOC Training Brigade in Scotland
1941-1943; GOC Polish Troops in Great Britain, promoted lieut.-general
in 1945. After demobilisation he settled in London, where he was a founder
and chairman of the Generals, Colonels and Senior Commanding Officers
Association. He was co-founder of the Regimental Association of the 1st
Belina Lancers; founder member and from 1963 chairman of the Council of
the Piłsudski Institute in London; Inspector of Training of the "Pogoń"
Youth Brigade. He was the author of numerous articles published in
"Belinak" in London. Decorations: Order of Virtuti Militari (V class),
Cross of Valour (3x), Gold Cross of Merit (2x), British Order of Bath
(III class), French Legion d'Honneur (III class), the Estonian Order of
Freedom (II class), Latvian Order of the Conquerer of the Bear (II class),
Crown of Romania (II class), Star of Romania (II class), Hungarian Cross
for Merit (II class).

[FOTO: Portret gen. Głuchowskiego w mundurze — starszy mężczyzna, dystyngowany]

───────────────────────────────────

GROCHOBIŃSKI Czesław (born 07.12.1906 Baranowicze) actor. Education
grammar school. Actor in theatres of Warsaw, Wilno, Cracow and Poznań
1929-39. He has lived in Great Britain since 1943. Member of the Polish
Air Force Theatre Group. Has acted on stage, in films, on television and
radio from 1945 till present day. He took part in a Royal Command
Performance in the Victoria Theatre in 1951. He has acted in many British
and American films, as well as in the Polish emigre theatre. ZASP,
"Syrena" and "Proarte". Member of the Association of Polish Artists of
the Stage in London, British Actors Equity Association.

[FOTO: Portret Grochobińskiego]

═══════════════════════════════════

[Strona 2 — biogramy po polsku, Nr 7:]

GŁUCHOWSKI Janusz Julian, generał dywizji, ur. 6 sierpnia 1888
w majątku Bukowa (pow. piotrkowski), zm. 11 czerwca 1964 w Londynie.
Syn Macieja i Marii Zdanowskiej. Studia na politechnice w Liège (Belgia).
Założył oddział Związku Walki Czynnej w Liège (1909). W 1912 ukończył
oficerski kurs Związku Strzeleckiego w Stróży pod Krakowem. W latach
1914-1917 w Legionach Polskich (czteroletni szlak kampanii I Brygady).
Po kryzysie przysięgowym w 1917 internowany w Beniaminowie (twierdza
Werl). Organizator i dowódca 3 Pułku Ułanów, a następnie 7 Pułku Ułanów
Lubelskich i I Brygady Kawalerii (1920-1924), generał brygady 1927.
Komendant Wyższych Studiów Wojskowych 1930-1933; DOK X Przemyśl 1933-
1935; I wiceminister Spraw Wojskowych 1935-1939. Po kampanii wrześniowej
przeszedł przez Rumunię do Francji i następnie do Anglii. (1940-41) —
Specjalny Oficer do dyspozycji Naczelnego Wodza; (1941-43) GOC Brygady
Szkolnej w Szkocji; GOC Polish Troops in Great Britain, promowany do
generała dywizji w 1945. Po demobilizacji osiedlił się w Londynie.
Założyciel i prezes Związku Kół Pułkowych Kawalerii 1953-1964; inicjator
i prezes Koła Generałów i Pułkowników b. Wyższych Dowództw; współzałożyciel
i od 1963 przewodniczący Rady Instytutu J. Piłsudskiego w Londynie; prezes
Koła 7. Pułku Ułanów; członek Rady Naczelnej Ligi Niepodległości Polski;
inspektor wyszkolenia brygady drużyn «Pogoń». Autor licznych artykułów
opublikowanych w «Belinaku» w Londynie.
Odznaczenia: Virtuti Militari (V), Krzyż Niepodległości z Mieczami,
Order Odrodzenia Polski (III), Walecznych (3x), Złoty Krzyż Zasługi (2x),
Order Łaźni (III), Legia Honorowa (III), estoński Order Krzyża Wolności (II),
łotewski Order Pogromcy Niedźwiedzia, Korona Rumunii (II), Gwiazda
Rumunii (II), węgierski Krzyż Zasługi (II).

(źr.: Arch. KBFP; Cygon W.K. Słownik biograficzny oficerów Legionów
Polskich, Warszawa 1992, s. 54; Kto jest kim. Generałowie z Kartotekami,
Warszawa 1999, s. 131-142.)

[FOTO: Portret gen. Głuchowskiego — zdjęcie w mundurze z odznaczeniami]

───────────────────────────────────

GŁUCHOWSKI Krzysztof, inżynier, ur. 29 listopada 1926 Warszawa, syn
Stanisława (Stefana) i Wandy Głuchowskiej. Żołnierz ZWZ, a następnie
Armii Krajowej (Kompania Kadeci, 17 Pułku Ułanów Lubelskich AK
1943-1944). Uczestnik Powstania Warszawskiego. AK i Delegatury Rządu
na Kraj, a następnie Dowództwa Okręgu Warszawskiego. Po kapitulacji
w niewoli w Fallingbostel i Dorsten, a następnie w München Gladbach.
7 Pułk Ułanów Lubelskich 1945. Studia inżynierskie w Londynie,
inżynier (specjalista od systemów wychładzających). Stanowisko
pracownicze w Hiszpanii i Brazylii. Od 1978 odpowiedzialny w CAV —
firmy Francji Feria i Pola. Po przejściu na emeryturę osiedla się
w Brazylii. Autor licznych artykułów w prasie polonijnej,
w «Dzienniku Polskim» (Londyn). Członek Rady Instytutu im. Piłsudskiego,
członek Zarządu Polskiego Ośrodka Społeczno-Kulturalnego w Londynie.

[FOTO: Portret Krzysztofa Głuchowskiego w okularach]

───────────────────────────────────

GROCHOBIŃSKI Czesław, aktor, ur. 7 grudnia 1906 w Baranowiczach,
syn Franciszka i Marii Otałowicz. Wykształcenie średnie. Aktor teatralny
w Warszawie, Wilnie, Krakowie i Poznaniu 1926-1939. W Wielkiej Brytanii
od 1943. Członek Lotniczego Ośrodka Teatralnego w Londynie. Aktor
teatralny, filmowy, telewizyjny i radiowy od 1945. Brał udział w Royal
Command Performance w Victoria Theatre 1951. Grał w wielu angielskich
i amerykańskich filmach. Aktor Teatru Polskiego ZASP i teatru «Syrena»
oraz Pro Arte. Członek Związku Artystów Scen Polskich w Londynie,
Stowarzyszenia Lotników Polskich w Londynie, British Actors Equity
Association.

[FOTO: Portret Grochobińskiego]""",
        "pieczecie": [],
        "podpisy": [],
        "osoby": [
            "Gen. dyw. Janusz Julian Głuchowski (ur. 06.08.1888 Bukowa pow. piotrkowski, zm. 11.06.1964 Londyn) — syn Macieja i Marii Zdanowskiej",
            "Krzysztof Głuchowski (ur. 29.11.1926 Warszawa) — inżynier, syn Stefana i Wandy",
            "Czesław Grochobiński (ur. 07.12.1906 Baranowicze) — aktor, syn Franciszka i Marii Otałowicz"
        ],
        "znaki_szczegolne": [
            "KLUCZOWY DOKUMENT — 3 biogramy: gen. Janusz, Krzysztof, Grochobiński",
            "Dwujęzyczne (EN/PL) — strona 1 po angielsku, strona 2 po polsku",
            "BIOGRAM KRZYSZTOFA — potwierdza: ZWZ/AK, Kompania Kadeci, 17 PUL, Powstanie",
            "Krzysztof: niewola w Fallingbostel, Dorsten, München Gladbach; ucieczka",
            "Krzysztof: inżynier systemów wychładzających, Hiszpania, Brazylia, CAV",
            "Gen. Janusz: Związek Walki Czynnej 1909, I Brygada Legionów 1914-17",
            "Gen. Janusz: I wiceminister Spraw Wojskowych 1935-1939",
            "Gen. Janusz: GOC Polish Troops in Great Britain, gen. dyw. 1945",
            "Odznaczenia gen. Janusza: VM (V), KN z Mieczami, Order Łaźni (III), Legia Honorowa (III)",
            "Źródło: Arch. KBFP; Cygon W.K. Słownik biogr. oficerów Legionów, 1992",
            "3 FOTO: gen. Janusz w mundurze, Krzysztof w okularach, Grochobiński"
        ],
        "kontekst": "Kwartalnik Biograficzny Polonii, Nr 7. TRZY biogramy: (1) Gen. dyw. Janusz Julian Głuchowski (1888-1964) — legionista, dowódca 7 PUŁ, I wiceminister SW, GOC w Szkocji i W. Brytanii. (2) Krzysztof Głuchowski (ur. 1926) — syn Stefana, żołnierz AK/Powstaniec, inżynier w Brazylii, działacz POSK i Instytutu Piłsudskiego. (3) Czesław Grochobiński — aktor polski w Londynie. Biogram Krzysztofa POTWIERDZA: ur. 1926 (nie 1928!), syn STEFANA (nie Janusza), ZWZ → AK → Kompania Kadeci 17 PUL → Powstanie → niewola → 7 PUL 1945 → Londyn → Brazylia."
    },

    # ═══════════════════════════════════════════════════════════════
    # SERIA STEFAN — Dokumenty Stefana Głuchowskiego
    # (brat gen. Janusza, urzędnik Kancelarii Cywilnej Prezydenta RP,
    #  żołnierz AK, ojciec Krzysztofa)
    # ═══════════════════════════════════════════════════════════════

    # stefan_001 — Zarządzenie Prezesa Rady Ministrów
    "stefan_001": {
        "typ": "Zarządzenie urzędowe",
        "data": "8 marca 1929",
        "jezyk": "polski",
        "nadawca": "Prezes Rady Ministrów",
        "adresat": "Wyższa Komisja Dyscyplinarna przy Prezydium Rady Ministrów",
        "transkrypcja": """PREZES RADY MINISTRÓW
Nr. 3743                    Warszawa, dnia 8 marca 1929 r.

Wyższa Komisja Dyscyplinarna,
przy Prezydium Rady Ministrów.

ZARZĄDZENIE WEWNĘTRZNE.

Do Wyższej Komisji Dyscyplinarnej przy Prezydium
Rady Ministrów, następujacą dla urzędników i
funkcjonarjuszów niższych Prezydium Rady Ministrów,
Kancelarii Cywilnej Prezydenta Rzeczypospolitej,
Drukarni Państwowych, Urzędu Patentowych oraz
Polskiej Agencji Telegraficznej, powołuję na okres
trzech lat:
na przewodniczącego: p. Jana Kantego Pietaka, Szefa
    Biura Prawnego Prezydium Rady
    Ministrów,
na zastępcę przewod.: p.Dr Bronisława Krzyżanowskiego
    [...]
na członków:
    p.P.: Władysława Racpoński [...]
    Dr Ireneusza Karłińskiego [...]
    Bolesław Rezera [...]
    Henryka Turulskiego [...]
    Augusta Janiczkiego [...]
    Dr Zygmunta Skwarczyńskiego [...]
    St. Jana Kuchowskiego [...]""",
        "pieczecie": ["Nagłówek Prezes Rady Ministrów"],
        "podpisy": [],
        "osoby": ["Stefan Głuchowski (kontekst — dokument z jego akt)", "Jan Kanty Pietak", "Dr Bronisław Krzyżanowski"],
        "znaki_szczegolne": [
            "Dokument z akt osobowych Stefana Głuchowskiego",
            "Komisja Dyscyplinarna dla Kancelarii Cywilnej Prezydenta RP",
            "Wymienia kluczowe instytucje: Prezydium RM, Kancelaria Cywilna, PAT"
        ],
        "kontekst": "Zarządzenie o powołaniu komisji dyscyplinarnej obejmującej m.in. Kancelarię Cywilną Prezydenta RP, gdzie pracował Stefan Głuchowski. Dokument zachowany w jego aktach osobowych."
    },

    # stefan_002 — Dyplom: Brązowy Medal za Długoletnią Służbę
    "stefan_002": {
        "typ": "Dyplom odznaczeniowy",
        "data": "14 maja 1938",
        "jezyk": "polski",
        "nadawca": "Kancelaria Cywilna Prezydenta Rzeczypospolitej",
        "adresat": "Stefan Głuchowski",
        "transkrypcja": """DYPLOM

Na podstawie ustawy z dnia 8 stycznia 1938 roku
(Dz. U. R. P. Nr 3, Poz. 11) nadaję

P. STEFANOWI GŁUCHOWSKIEMU,
Kierownikowi Referatu w Kancelarii Cywilnej Prezydenta Rzeczypospolitej

BRĄZOWY
MEDAL ZA DŁUGOLETNIĄ SŁUŻBĘ

Warszawa, dnia 14 maja 1938 r.

[podpis]
SZEF KANCELARJI CYWILNEJ""",
        "pieczecie": ["Kancelaria Cywilna Prezydenta Rzeczypospolitej (sucha pieczęć)"],
        "podpisy": ["Szef Kancelarii Cywilnej"],
        "osoby": ["Stefan Głuchowski"],
        "znaki_szczegolne": [
            "Stanowisko: Kierownik Referatu w Kancelarii Cywilnej Prezydenta RP",
            "Brązowy Medal za Długoletnią Służbę — ustawa z 8.01.1938",
            "Pieczęć sucha z orłem"
        ],
        "kontekst": "Stefan Głuchowski pracował jako Kierownik Referatu w Kancelarii Cywilnej Prezydenta RP Ignacego Mościckiego. Medal za długoletnią służbę (od 1918/1921 do 1938 = ~17-20 lat pracy)."
    },

    # stefan_003 — Złoty Krzyż Zasługi
    "stefan_003": {
        "typ": "Dyplom odznaczeniowy",
        "data": "11 listopada 1936",
        "jezyk": "polski",
        "nadawca": "Prezydent Rzeczypospolitej / Prezes Rady Ministrów",
        "adresat": "Stefan Głuchowski",
        "transkrypcja": """Rzeczpospolita Polska

PREZYDENT RZECZYPOSPOLITEJ
za zgodą
PREZESA RADY MINISTRÓW

stwierdza, że
zarządzeniem z dnia 11 Listopada 1936 r.

NADAŁ

STEFANOWI GŁUCHOWSKIEMU
Kierownikowi Referatu Kancelarii Cywilnej P.R.P.

ZŁOTY KRZYŻ ZASŁUGI

PO RAZ PIERWSZY

[podpis] PREZES RADY MINISTRÓW
[podpis] SZEF KANCELARJI""",
        "pieczecie": ["Orzeł RP (pieczęć ozdobna)"],
        "podpisy": ["Prezes Rady Ministrów", "Szef Kancelarii"],
        "osoby": ["Stefan Głuchowski", "Prezydent RP (Ignacy Mościcki)"],
        "znaki_szczegolne": [
            "ZŁOTY Krzyż Zasługi — 3. stopień (brązowy→srebrny→złoty)",
            "Data symboliczna: 11 Listopada — Święto Niepodległości",
            "Ozdobna kaligrafia, pieczęć z orłem",
            "Zdobyty PO RAZ PIERWSZY — formularz przewiduje powtórzenia"
        ],
        "kontekst": "Złoty Krzyż Zasługi nadany 11 listopada 1936 r. (Święto Niepodległości). Stefan Głuchowski wspinał się po szczeblach odznaczeń: Srebrny Krzyż Zasługi (1929) → Złoty Krzyż Zasługi (1936). Równolegle brat Janusz był już I Zastępcą Ministra Spraw Wojskowych."
    },

    # stefan_004 — Pismo Kancelarii Cywilnej, mianowanie/przeniesienie
    "stefan_004": {
        "typ": "Pismo urzędowe",
        "data": "ok. 1933-1934",
        "jezyk": "polski",
        "nadawca": "Kancelaria Cywilna Prezydenta Rzeczypospolitej",
        "adresat": "Stefan Głuchowski",
        "transkrypcja": """[Dokument obrócony — pismo Kancelarii Cywilnej Prezydenta RP
dotyczące mianowania lub przeniesienia Stefana Głuchowskiego.
Data: prawdopodobnie XII.1933 lub I.1934.
Widoczna pieczęć Kancelarii Cywilnej (okrągła, czerwona).]""",
        "pieczecie": ["Kancelaria Cywilna Prezydenta RP (okrągła, czerwona)"],
        "podpisy": ["Szef Kancelarii Cywilnej"],
        "osoby": ["Stefan Głuchowski"],
        "znaki_szczegolne": ["Dokument obrócony o 180°", "Pieczęć czerwona"],
        "kontekst": "Jedno z wielu pism personalnych w aktach Stefana — awanse i przeniesienia w Kancelarii Cywilnej."
    },

    # stefan_006 — Zarząd Rezydencji Prezydenta RP w Spale
    "stefan_006": {
        "typ": "Pismo urzędowe / zaproszenie",
        "data": "2 listopada 1930",
        "jezyk": "polski",
        "nadawca": "Zarząd Rezydencji Prezydenta Rzeczypospolitej w Spale",
        "adresat": "Stefan Głuchowski, Radca Min., Kanc.Cyw.Prezydenta",
        "transkrypcja": """ZARZĄD REZYDENCJI
PREZYDENTA RZECZYPOSPOLITEJ
W SPALE

Spała, dn. 2 listopada 1930.
Nr. 210/109/30

Do
Pana Stefana Głuchowskiego
Radcy Min., Kanc.Cyw.Prezydenta

Zarząd Rezydencji w Spale przesyła Panu jako uczestnikowi
corocznego myśliwskiego w dniu Sap Huberta w Spale w r. 1930, znaczek
pamiątkowy, wydany przez Pana Prezydenta.

[podpis]
Zarządzający""",
        "pieczecie": ["Zarząd Rezydencji Prezydenta RP w Spale (okrągła, niebieska)"],
        "podpisy": ["Zarządzający Rezydencją"],
        "osoby": ["Stefan Głuchowski", "Prezydent RP (Ignacy Mościcki)"],
        "znaki_szczegolne": [
            "SPAŁA — letnia rezydencja Prezydenta RP (pałac myśliwski Romanowów, potem RP)",
            "Sap Huberta — tradycyjne polowanie hubertowskie, 3 listopada",
            "Stefan jako RADCA MINISTERIALNY — wysoki urzędnik",
            "Znaczek pamiątkowy od Prezydenta — osobisty prezent"
        ],
        "kontekst": "Stefan Głuchowski uczestniczył w polowaniu hubertowskim (Sap Huberta) w rezydencji prezydenckiej w Spale. To dowodzi jego wysokiej pozycji — do Spały zapraszano elitę urzędniczą i wojskową II RP. Prezydent Mościcki osobiście wydawał pamiątkowe znaczki. Spała była jedną z najważniejszych rezydencji — Piłsudski i Mościcki regularnie tam przebywali."
    },

    # stefan_007 — Komitet Krzyża i Medalu Niepodległości
    "stefan_007": {
        "typ": "Wezwanie urzędowe",
        "data": "9 listopada [1931?]",
        "jezyk": "polski",
        "nadawca": "Komitet Krzyża i Medalu Niepodległości",
        "adresat": "Głuchowski Stefan",
        "transkrypcja": """KOMITET
KRZYŻA I MEDALU NIEPODLEGŁOŚCI
Konto P.K.O. Nr 29.860.

N. 3/1062.

Pan GŁUCHOWSKI Stefan
w miejscu

Zarządzeniem Pana Prezydenta Rzeczypospolitej
Polskiej z dn. 9 Listopada
odznaczony 7 KRZYŻEM NIEPODLEGŁOŚCI

Proszę o wypełnienie do K.K.O. według załączonego
wzoru kat. 10 — (dziesięciogresz) na konto Ko-
mitetu wraz z 10 — [...]
składam Panu potwierdzenie, proszę po wypłoszeni
Biura Biuro Komitetu [...]

KIEROWNIK BIURA KOMITETU
Fr. Sygnowski ppłk.""",
        "pieczecie": ["Komitet Krzyża i Medalu Niepodległości"],
        "podpisy": ["Fr. Sygnowski ppłk."],
        "osoby": ["Stefan Głuchowski", "Ppłk. Fr. Sygnowski"],
        "znaki_szczegolne": [
            "KRZYŻ NIEPODLEGŁOŚCI — jedno z najcenniejszych odznaczeń II RP",
            "Nadawany za działalność w walce o niepodległość 1905-1921",
            "Stefan musiał mieć zasługi niepodległościowe (jak brat Janusz)"
        ],
        "kontekst": "Krzyż Niepodległości nadawany na mocy ustawy z 1930 za czyn zbrojny lub pracę niepodległościową w okresie 1905-1921. Stefan musiał mieć udokumentowane zasługi — prawdopodobnie za działalność konspiracyjną lub służbę w wojnie polsko-bolszewickiej."
    },

    # stefan_008 — Order Odrodzenia Polski, Krzyż Kawalerski
    "stefan_008": {
        "typ": "Dyplom odznaczeniowy",
        "data": "9 listopada 1931",
        "jezyk": "polski",
        "nadawca": "Kancelaria Odznaczenia / Prezydent RP",
        "adresat": "Stefan Głuchowski",
        "transkrypcja": """KANCELARIA ORDERÓW
„ODRODZENIA POLSKI"

Do
Pana STEFANA GŁUCHOWSKIEGO, URZĘDNIKA
Kancelarii Cywilnej Prezydenta Rzeczypospolitej
w Warszawie

Stwierdzam, że Prezydent Rzeczypospolitej
dnia 9 Listopada 1931 r. raczył
odznaczony Pana
KRZYŻEM KAWALERSKIM

orderu
ODRODZENIA POLSKI

Warszawa, dnia 12 Listopada 1931 r.    Kanclerz
[podpis]""",
        "pieczecie": ["Kancelaria Orderów Odrodzenia Polski"],
        "podpisy": ["Kanclerz"],
        "osoby": ["Stefan Głuchowski", "Prezydent RP (Ignacy Mościcki)"],
        "znaki_szczegolne": [
            "ORDER ODRODZENIA POLSKI (POLONIA RESTITUTA) — Krzyż Kawalerski (V klasa)",
            "To BARDZO wysokie odznaczenie dla urzędnika cywilnego!",
            "Data: 9 Listopada — Święto Niepodległości",
            "Brat Janusz z pewnością miał wyższą klasę tego orderu"
        ],
        "kontekst": "Order Odrodzenia Polski (Polonia Restituta) w klasie V (Krzyż Kawalerski) — jedno z najwyższych odznaczeń cywilnych II RP. Nadany 9 listopada 1931 r. (wigilia Święta Niepodległości). Potwierdza wysoką pozycję Stefana w aparacie państwowym."
    },

    # stefan_010 — Srebrny Krzyż Zasługi
    "stefan_010": {
        "typ": "Dyplom odznaczeniowy",
        "data": "8 czerwca 1929",
        "jezyk": "polski",
        "nadawca": "Prezes Rady Ministrów",
        "adresat": "Stefan Głuchowski",
        "transkrypcja": """KRZYŻ ZASŁUGI
Nr. 6109/1021.

Do
Pana STEFANA GŁUCHOWSKIEGO
Sekretarza Kancelarii Cywilnej
Prezydenta Rzeczypospolitej
w Warszawie

SREBRNY KRZYŻ ZASŁUGI

Na zasadzie art. 5 ustawy z 23 Czerwca 1923 r. (Dz.U.R.P.
Nr. 62 poz. 458) nadaję Panu — po raz pierwszy

Prezes Rady Ministrów
Warszawa, dn. 8 Czerwca 1929 r.

[podpis]""",
        "pieczecie": ["Prezes Rady Ministrów (pieczęć okrągła)"],
        "podpisy": ["Prezes Rady Ministrów"],
        "osoby": ["Stefan Głuchowski"],
        "znaki_szczegolne": [
            "Srebrny Krzyż Zasługi — II stopień odznaczenia",
            "Stanowisko: SEKRETARZ Kancelarii Cywilnej (1929) — potem awansował na Kierownika Referatu",
            "Po raz pierwszy — można było otrzymać wielokrotnie"
        ],
        "kontekst": "Ścieżka odznaczeń Stefana: Srebrny KZ (1929) → Złoty KZ (1936). W 1929 był jeszcze Sekretarzem, do 1936 awansował na Kierownika Referatu."
    },

    # stefan_014 — Mianowanie na urzędnika VIII kategorii
    "stefan_014": {
        "typ": "Pismo nominacyjne",
        "data": "ok. październik 1929",
        "jezyk": "polski",
        "nadawca": "Kancelaria Cywilna Prezydenta Rzeczypospolitej",
        "adresat": "Stefan Głuchowski",
        "transkrypcja": """KANCELARIA CYWILNA
PREZYDENTA RZECZYPOSPOLITEJ
Nr. [...]

Do
Pana Stefana Głuchowskiego
urzędnika VIII-ej kat.st. w Kancelarii Cywilnej

Pan Prezydent Rzeczypospolitej postanowił
dnia dn. 20 Października 1929 r. na zasadzie art.
11b ustawy o państwowej służbie cywilnej (Dz.Ust.R.P.
Gr.61,dec.104 i 1925 r.) mianić Pana w stopniu
państwowej.

Jednocześnie Pan Prezydent Rzeczypospolitej
ley mianować Pan zatrudnionym w VIII-ej kat.st.
w Kancelarii Cywilnej.

Szef Kancelacji Cywilnej:
[podpis]""",
        "pieczecie": ["Kancelaria Cywilna Prezydenta RP (okrągła, czerwona)"],
        "podpisy": ["Szef Kancelarii Cywilnej"],
        "osoby": ["Stefan Głuchowski", "Prezydent RP (Ignacy Mościcki)"],
        "znaki_szczegolne": [
            "Urzędnik VIII kategorii — średni szczebel służby cywilnej",
            "Mianowanie przez samego Prezydenta RP (dla pracowników Kancelarii)",
            "Pieczęć czerwona z orłem"
        ],
        "kontekst": "Mianowanie na stałego urzędnika państwowego VIII kategorii. W Kancelarii Cywilnej nawet takie formalne akty wymagały podpisu Prezydenta."
    },

    # stefan_015 — Przyjęcie do pracy w Kancelarii Cywilnej (1921)
    "stefan_015": {
        "typ": "Pismo o zatrudnieniu",
        "data": "1 lipca 1921",
        "jezyk": "polski",
        "nadawca": "Kancelaria Cywilna Naczelnika Państwa",
        "adresat": "Stefan Głuchowski",
        "transkrypcja": """Kancelaria Cywilna
Naczelnika Państwa
Nr 4626/21.

Do
Pana Stefana Głuchowskiego
w/m. — Słuzewska 2 m.10.

W odpowiedzi na podanie z dn. 1.Lipca r.b.
proszę Pana o objęcie posady w Kancelarii Cy-
wilnej na czas próbny od 1.Lipca do 1 Sierpnia
1921 r. z poborami odpowiadającemi kategorji
I. płac urzędników państwo-wych.

Szef Kancelacji Cywilnej:
[podpis]""",
        "pieczecie": ["Kancelaria Cywilna Naczelnika Państwa (orzeł, okrągła niebieska)"],
        "podpisy": ["Szef Kancelarii Cywilnej"],
        "osoby": ["Stefan Głuchowski"],
        "znaki_szczegolne": [
            "NACZELNIK PAŃSTWA — to jeszcze era Piłsudskiego jako Naczelnika (1918-1922)!",
            "Adres: Słuzewska 2 m.10, Warszawa",
            "Zatrudnienie na okres próbny — 1 miesiąc",
            "Kategoria I płac — najniższa (początek kariery)",
            "DATA: 1 lipca 1921 — Stefan zaczął pracę w Kancelarii Cywilnej"
        ],
        "kontekst": "Pierwsze zatrudnienie Stefana Głuchowskiego w Kancelarii Cywilnej Naczelnika Państwa (Józefa Piłsudskiego). Data: lipiec 1921 — jeszcze przed uchwaleniem Konstytucji marcowej! Stefan zaczynał od najniższej kategorii płac. Piłsudski był Naczelnikiem Państwa do 14 XII 1922."
    },

    # stefan_018 — Mianowanie przez Kancelarię Naczelnika Państwa
    "stefan_018": {
        "typ": "Pismo nominacyjne",
        "data": "31 grudnia 1918 lub 1922",
        "jezyk": "polski",
        "nadawca": "Kancelaria Cywilna Naczelnika Państwa",
        "adresat": "Stefan Głuchowski",
        "transkrypcja": """Kancelaria Cywilna
Naczelnika Państwa
Nr 5834

Do
Pana STEFANA GŁUCHOWSKIEGO

Na podstawie dekretu z dnia 11 Grudnia 1918
roku mianuje Pana Ponomocnik Referenta Kancelarii Cy-
wilnej Kancelarii Pełnpraw z odłączeniem do kategoryi
[...] pienc urzednika Pańsn. od kategorji n- kasy
masowej od dnia 1 po Stycznia 1922 roku.

Szef Kancelarii Cywilnej:
[podpis]""",
        "pieczecie": ["Kancelaria Cywilna Naczelnika Państwa (orzeł, okrągła niebieska)"],
        "podpisy": ["Szef Kancelarii Cywilnej"],
        "osoby": ["Stefan Głuchowski"],
        "znaki_szczegolne": [
            "Dekret z 11 XII 1918 — jeden z pierwszych aktów prawnych odrodzonej Polski!",
            "Mianowanie na Pomocnika Referenta — awans z kategorii I",
            "Pieczęć z orłem Naczelnika Państwa"
        ],
        "kontekst": "Dokument potwierdzający awans w strukturze Kancelarii Cywilnej. Powołanie na dekret z 11 XII 1918 — to zaledwie miesiąc po odzyskaniu niepodległości!"
    },

    # stefan_019 — Medal Dziesięciolecia Odzyskanej Niepodległości
    "stefan_019": {
        "typ": "Dyplom odznaczeniowy",
        "data": "ok. 1929",
        "jezyk": "polski",
        "nadawca": "Kancelaria Cywilna Prezydenta Rzeczypospolitej",
        "adresat": "Stefan Głuchowski",
        "transkrypcja": """KANCELARIA CYWILNA
PREZYDENTA RZECZYPOSPOLITEJ
Nr. [...]

Do
Pana Stefana Głuchowskiego
urzędnika w Kancelarii Cywilnej
[...] Prezydenta Rzeczypospolitej

Na podstawie § 6 rozporządzenia Rady Ministrów z dnia
27 września 1928 r. (Monitor Polski Nr 237 poz. 543) przyznaję
Panu prawo do Medalu Dziesięciolecia Odzyskanej Niepodległości.

SZEF KANCELARJI CYWILNEJ
[podpis]""",
        "pieczecie": ["Kancelaria Cywilna Prezydenta RP (orzeł)"],
        "podpisy": ["Szef Kancelarii Cywilnej"],
        "osoby": ["Stefan Głuchowski"],
        "znaki_szczegolne": [
            "Medal Dziesięciolecia Odzyskanej Niepodległości (1918-1928)",
            "Rozporządzenie z 27.09.1928 (Monitor Polski Nr 237, poz. 543)",
            "Przyznawany urzędnikom państwowym w 10. rocznicę niepodległości"
        ],
        "kontekst": "Medal pamiątkowy z okazji 10-lecia odzyskania niepodległości. Stefan pracował w służbie państwowej od ~1918/1921, więc kwalifikował się."
    },

    # stefan_020 — Biogram RTM. UCIECH GŁUCHOWSKI ps. "Jezycki"
    "stefan_020": {
        "typ": "Biogram / maszynopis historyczny",
        "data": "ok. 1995 (opracowanie)",
        "jezyk": "polski",
        "nadawca": "autor biogramu (nieznany)",
        "adresat": "—",
        "transkrypcja": """RTM.(UCIECH) GŁUCHOWSKI pseudonim „JEZYCKI"

syn Mariana Głuchowskiego i Marii z Zielikowskich. Urodzony w 1902 roku w Radomiu pod
Częstochową. Szkoły średnie w Radomsku, a maturę w Łodzi. Ochotnik P.W.-IV
[...] służył w kawalerii warszawskiej. W międzyczasie służył również na funkcjach w ro-
zeszły 7 Pułku Ułanów Lubelskich, dowodzonych przez brata majora
Głuchowskiego. W roku 1930 roku po odbyciu służby w P.W. i końcem zdjęty na maturze
zafascynowany zagadnieniami na polu Medzyn [...] jednych lat hydrografizm.
W 4 września dobrze znając od Piłssy i Narew realia kampanii poinformator [...]
do obrony n 1922 roku moto rozpoczął studia na Akademii Rolniczej w Bydgoszczy. Po stu-
diach Praktykant Rolniczy Karnicza. Po zakończeni prak. politycznego dyrektor krajoznaw-
czego [...] administrowanie gdzie redokując 6 Brumisło w marg.Pław

[...] we Wrześniu 1939 mobilizacyjnie, odbywa czas kampanię w 4 szwadronie 7 P.Uł.Lab, który to szwa-
dron [...] od szeregowca do st.wachmistrza [...] O Roli Krakowskiej partyzantów, z Nowogrodzkem w „Romb" oddziale i
dostał z połączeniu [...]

W październiku 1944 obrany natrakciam Dywizjonu „Jelen" na Aleje Szucha, a nastepnie [...] a grupa pozosto-
stałych przy życiu [...]
1 Dywizja [...] o następnym szlaku od Mokotowa. 21 sierpnia dopiecznia dezertera Dywisjonu [...]
1 Sierpnia [...] to razem otarty [...] zniszczone po tum koniku strasnie ulary.
15 Października 1944 w czasie obrony trzeciej ranni zamiast odesłane do oddziału zamiast w [...] od uderzenia na Mokotów,
odniesieniu ranie i aby nie narazać pragmatycz ży wobec żołnierzey, podslania się bycia czlnrak ze strzcl-
[...] Po wyzwoleniu na gmin szlachetnem ze strony zdroumym obozu czasu [...]

Pozostalemu awansowani do stopnia majora i odznaczany między innymi: Virtuti Militari, innee odznaczeni-
Krzyż Walecznych, Krzyż Krzyża Zasluge z Mieczami, Krzyż Armii Krajowej (No. 1. Specjalna seria z
I.5.8.67, kapitulacja podpiona przez gen. Tadeusza Pełczyńskiego „Grzegorz")

W muzech u mąż pan Lecho Gloebowskich znaleźli sa w nastepujących wydrukowanych i zródłach-
[...] Londyn str 120 50 3 1946 na str.148 94.5 do 100
Ułani Lubelscy. Zeszty wydawane od 1947 przez Koło 7 P.Uł.Lubelskich London
[...] 35(41)2, 8.56 Warszawa
Redakcja Znaki nr 3.4.(6), London 1953 (artyku Plt plyp.G.Lewczowskiego)
Powstanie Warszawskie; Adam Borkiewicz, Pax Warszawa 1957
Powstanie Warszawskie w Bialoszek; Stelko Warszawa 1937
[...]
Dziennik Polski 2.4.91, 29.4.91, 24.6.91, 30.7.92, 23.9.92, London
[...]
Moskiny 1944: Leslam M.Barlticki MON Warszawa 1971
[...]
Wydano w czesc oficjalnych materiałow 1939-1945 Bialoszova Nomokiewicza Szczepańczkiw Warszawa 1992
[...] Film: Mc. Oczekul Anders (I lumos) Warszawa 1994
Biblioteka Narodowa w Warszawie Zbior Rekoposow No. 13853

Przedstawiony I Vice minister Spraw Wojskowych i dowódca Jednostek Wojska w Wielkiej Brytanii,
generał dywizji.

Przypomnienie Krzysztof Głuchowski
Rio de Janeiro, 18 Października 1995""",
        "pieczecie": [],
        "podpisy": ["Krzysztof Głuchowski (autor przypomnenia, Rio de Janeiro)"],
        "osoby": ["RTM Uciech Głuchowski ps. Jezycki", "Marian Głuchowski (ojciec Uciec)", "Maria z Zielikowskich (matka)", "Krzysztof Głuchowski (autor)", "Gen. dyw. Janusz Głuchowski (wspomniany)", "Gen. Tadeusz Pełczyński ps. Grzegorz"],
        "znaki_szczegolne": [
            "NOWY CZŁONEK RODZINY: RTM Uciech Głuchowski, ur. 1902 Radom",
            "Syn MARIANA Głuchowskiego (nie Janusza i nie Stefana!) — TRZECIA gałąź rodziny?",
            "Służył w 7 Pułku Ułanów Lubelskich",
            "Uczestnik POWSTANIA WARSZAWSKIEGO — Dywizjon 'Jeleń', Aleje Szucha, Mokotów",
            "Odznaczenia: Virtuti Militari, Krzyż Walecznych, KZ z Mieczami, Krzyż AK (nr 1, specjalna seria!)",
            "Ranny 15 X 1944 na Mokotowie",
            "Autor biogramu: KRZYSZTOF GŁUCHOWSKI, Rio de Janeiro, 18 X 1995",
            "Maszynopis wspomina Janusza jako 'I Vice minister Spraw Wojskowych i dowódca Jednostek Wojska w WB, generał dywizji'",
            "Bibliografia: ~20 pozycji, London + Warszawa"
        ],
        "kontekst": "KLUCZOWY DOKUMENT GENEALOGICZNY. Biogram Uciec Głuchowskiego (ur. 1902, syn Mariana) napisany przez Krzysztofa Głuchowskiego w Rio de Janeiro w 1995. Uciech służył w 7 Pułku Ułanów Lubelskich, walczył w Powstaniu Warszawskim (Mokotów), odznaczony Virtuti Militari i Krzyżem AK nr 1 (specjalna seria). Krzysztof potwierdza Janusza jako generała dywizji i I Zastępcę Ministra. PYTANIE: jaka relacja między Marianem (ojcem Uciec) a Januszem i Stefanem?"
    },

    # stefan_022 — Etykieta: listy z obozu do generała i syna
    "stefan_022": {
        "typ": "Etykieta archiwalna / opis zawartości",
        "data": "ok. 1945-1949 (opisywany okres)",
        "jezyk": "polski",
        "nadawca": "—",
        "adresat": "—",
        "transkrypcja": """Listy ppor. Stefana Głuchowskiego
z obozu w Niemczech z lat 1945-1947
do gen. Janusza Głuchowskiego w Anglii
oraz
Listy Stefana Głuchowskiego z Polski
do syna Krzysztofa w Anglii z lat
1947-1949""",
        "pieczecie": [],
        "podpisy": [],
        "osoby": ["ppor. Stefan Głuchowski", "gen. Janusz Głuchowski", "Krzysztof Głuchowski"],
        "znaki_szczegolne": [
            "KLUCZOWY DOKUMENT GENEALOGICZNY!",
            "Stefan = BRAT Janusza (pisze z obozu jenieckiego DO GENERAŁA)",
            "Krzysztof = SYN STEFANA (Stefan pisze z Polski DO SYNA w Anglii)",
            "Stefan miał stopień PODPORUCZNIKA (ppor.)",
            "Stefan był w OBOZIE JENIECKIM w Niemczech 1945-1947",
            "Po uwolnieniu wrócił do POLSKI (nie na Zachód)",
            "Krzysztof był w ANGLII (prawdopodobnie PKPR/PSZ)"
        ],
        "kontekst": "REWOLUCYJNE ODKRYCIE DLA KOLEKCJI. Ta etykieta archiwalna rozwiązuje zagadkę rodzinną: Stefan Głuchowski (ppor. AK, urzędnik Kancelarii Prezydenta) był BRATEM gen. Janusza Głuchowskiego, a OJCEM Krzysztofa. Stefan po wojnie wrócił do Polski komunistycznej (1947+), natomiast jego syn Krzysztof pozostał na Zachodzie (Anglia → Brazylia). To wyjaśnia, dlaczego Krzysztof miał dokumenty zarówno Stefana (ojca) jak i Janusza (wuja-generała)."
    },

    # stefan_023 — Przydział AK: Kwatermistrzostwo Obwodu Śródmieście
    "stefan_023": {
        "typ": "Dokument konspiracyjny / przydział AK",
        "data": "ok. 1943-1944",
        "jezyk": "polski",
        "nadawca": "Armia Krajowa, Obwód Śródmieście",
        "adresat": "Stefan Głuchowski",
        "transkrypcja": """Przydział:
Kwatermistrzostwo Obwodu
I

[pieczęć okrągła: DOWÓDZTWO OBWODU ŚRÓDMIEŚCIE A.K. Warszawa]

Radwan [pseudonim konspiracyjny]

[nr] Wyd.Nr 141002
[...] y R.""",
        "pieczecie": ["DOWÓDZTWO OBWODU ŚRÓDMIEŚCIE A.K. Warszawa (okrągła, czerwona)"],
        "podpisy": [],
        "osoby": ["Stefan Głuchowski ps. Radwan"],
        "znaki_szczegolne": [
            "PSEUDONIM KONSPIRACYJNY STEFANA: RADWAN",
            "Przydział: Kwatermistrzostwo Obwodu I (Śródmieście)",
            "Pieczęć DOWÓDZTWO OBWODU ŚRÓDMIEŚCIE A.K. — autentyczna!",
            "Nr ewidencyjny 141002",
            "Obwód I Śródmieście — serce Powstania Warszawskiego"
        ],
        "kontekst": "Dokument konspiracyjny przydzielający Stefana Głuchowskiego (ps. Radwan) do Kwatermistrzostwa Obwodu I Śródmieście AK. Obwód Śródmieście był jednym z najważniejszych w strukturze AK Okręgu Warszawskiego — tu toczyły się najcięższe walki Powstania."
    },

    # stefan_026 — Kriegsgefangenenpost — karta jeniecka
    "stefan_026": {
        "typ": "Kriegsgefangenenpost (poczta jeniecka)",
        "data": "15 września 1942",
        "jezyk": "polski/niemiecki",
        "nadawca": "Zaleski (?), Oflag XVII A",
        "adresat": "Stefan Głuchowski, Radom",
        "transkrypcja": """Kriegsgefangenenpost
Correspondance des prisonniers de guerre
Postkarte

An: A. ZALESKI    [stempel: GEPRÜFT / STALAG XVII A]
     gebir. [...]  Radom     14.12.41

Absender / Expéditeur:
Vor- und Zuname: [...]
Gefangenennummer: [...]
Lager-Bez. (pays): Oflag XVII A    Straße: [...]
                                    Land: Galizien
Oflag XVII.A. Unterlager: [...]
Deutschland (Allemagne)

Kriegsgefangenenlager           Datum: 15. 9. 1942
Camp des prisonniers            date

Kochany Stasio i Rodzino [...] napisałem [...] Grusz [...] wa
[...] i ciągle szwaranc się i o rodzinne moje [...]
[...] Brud [...]
[...] Kościuszko Polowanie a dzisięe Lubelszczyznw [...]
[...] Krzyszego Powiernik sędzkowie wizuam [...]
[...] wiele [...] prosby [...]
[...] Stalo to w lepszej [...] i cieszenia [...] i wiele nowej [...] [...]
Serdeczni Czi/Serdeczni Boh.    Twój Kowalow [...]
                                 Etwac""",
        "pieczecie": ["GEPRÜFT / STALAG XVII A (stempel cenzury)", "Stempel pocztowy 14.12.41"],
        "podpisy": ["Zaleski (?)"],
        "osoby": ["Stefan Głuchowski (adresat 'Stasio')", "Zaleski (nadawca, jeniec Oflag XVII A)"],
        "znaki_szczegolne": [
            "OFLAG XVII A — obóz jeniecki dla oficerów w Edelbach (Austria)",
            "Adres Stefana: RADOM — to potwierdza radomskie korzenie rodziny",
            "Cenzura wojskowa (GEPRÜFT)",
            "Nadawca zwraca się 'Kochany Stasio' — bliska znajomość",
            "Wspomina Lubelszyznę i Kościuszkę — prawdopodobnie 7 Pułk Ułanów Lubelskich",
            "Data: 15.IX.1942 — w środku okupacji"
        ],
        "kontekst": "Karta jeniecka z Oflagu XVII A (Edelbach, Austria) wysłana do Stefana Głuchowskiego w Radomiu. Nadawca (Zaleski?) to prawdopodobnie współsłużący z 7 Pułku Ułanów Lubelskich, jeniec wojenny od 1939. Stefan w tym czasie był jeszcze w Radomiu/Warszawie — dopiero później dołączył do AK."
    },

    # stefan_027 — List do Krzysztofa z podpisami oficerów 7 pułku
    "stefan_027": {
        "typ": "List osobisty",
        "data": "ok. 1990s",
        "jezyk": "polski",
        "nadawca": "N. (autor listu, syn oficera?)",
        "adresat": "Krzysztof Głuchowski",
        "transkrypcja": """Drogi Krzysztofie,
Posyłam Ci ten list w imieniu mojego Ojca, jako
ciekawostkę, ale dotyczącą 7 płk ułanów. Oto
są tam podpisy dwóch oficerów z tego pułku, którzy
przyjaźnili się z moim Ojcem:
por. Vol. Jocigar   i por. Janusz Pornatowski
list pisany na zebraniu w Warszawie u
p. domu P. Korolcbuk.

N.""",
        "pieczecie": [],
        "podpisy": ["N. (autor)"],
        "osoby": ["Krzysztof Głuchowski (adresat)", "por. Vol. Jocigar", "por. Janusz Pornatowski", "P. Korolcbuk"],
        "znaki_szczegolne": [
            "Dotyczy 7 PUŁKU UŁANÓW LUBELSKICH",
            "Podpisy dwóch oficerów pułku",
            "Zebranie w Warszawie — prawdopodobnie przedwojenne",
            "Krzysztof zbierał materiały o 7 pułku (rodzinnym pułku)"
        ],
        "kontekst": "List do Krzysztofa z materiałami dotyczącymi 7 Pułku Ułanów Lubelskich. Krzysztof aktywnie zbierał wspomnienia i dokumenty pułkowe — to on napisał biogram Uciec w 1995."
    },

    # stefan_028 — ZAŚWIADCZENIE ARMII KRAJOWEJ
    "stefan_028": {
        "typ": "Zaświadczenie wojskowe / dokument konspiracyjny",
        "data": "25 lipca 1944",
        "jezyk": "polski",
        "nadawca": "Armia Krajowa, Okręg Warszawski",
        "adresat": "ppor. Głuchowski Stanisław Stefan",
        "transkrypcja": """ARMIA KRAJOWA
Okręg Warszawski

Nr 2856

Zaświadczam, że

stopień wojsk. (pseudonim i imię)
ppor. Głuchowski Stanisław Stefan jest
nazwisko
żołnierzem A. K.
Dnia 25.VII.1944 r.

Obwod [Śródmieście]
Komendant Okręgu:
[podpis] Radwan

[pieczęć: DOWÓDZTWO OBWODU ŚRÓDMIEŚCIE A.K. Warszawa]""",
        "pieczecie": ["DOWÓDZTWO OBWODU ŚRÓDMIEŚCIE A.K. Warszawa (pieczęć okrągła, czerwona z orłem)"],
        "podpisy": ["Komendant Okręgu (podpis nieczytelny)"],
        "osoby": ["ppor. Głuchowski Stanisław Stefan"],
        "znaki_szczegolne": [
            "🔴 DOKUMENT NAJWYŻSZEJ WAGI HISTORYCZNEJ!",
            "Pełne imiona: STANISŁAW STEFAN Głuchowski — dwa imiona!",
            "Data: 25 LIPCA 1944 — 6 DNI PRZED POWSTANIEM WARSZAWSKIM (1 VIII 1944)!",
            "Stopień: podporucznik (ppor.)",
            "Obwód Śródmieście — serce walki powstańczej",
            "Pieczęć autentyczna AK z orłem w koronie",
            "Nr zaświadczenia: 2856",
            "To ten sam 'Radwan' co na dokumencie stefan_023!"
        ],
        "kontekst": "NAJCENNIEJSZY DOKUMENT W NOWEJ SERII. Zaświadczenie Armii Krajowej wystawione ppor. Stanisławowi Stefanowi Głuchowskiemu 25 lipca 1944 — SZEŚĆ DNI przed wybuchem Powstania Warszawskiego. Dokument potwierdza jego przynależność do AK, stopień podporucznika, przydział do Obwodu Śródmieście. Stefan (ps. Radwan) walczył w Powstaniu Warszawskim — przeżył i trafił do obozu jenieckiego w Niemczech (1945-1947)."
    },

    # stefan_030 — Dedykacja od oficerów 7 Pułku Ułanów
    "stefan_030": {
        "typ": "Dedykacja / wpis pamiątkowy",
        "data": "ok. 1947 (Henstedt)",
        "jezyk": "polski",
        "nadawca": "Oficerowie 7 Pułku Ułanów Lubelskich",
        "adresat": "Stefan Głuchowski",
        "transkrypcja": """Kochanemu Stefankowi, wrocenu
brykisci i dobremu towarzyszowi
Hoch     Lochwia
[podpis] przelożeni pst. 8 p.S.R. [?]
[podpis] Karpiński [?]
[podpis] KaZimierz [?]
R. Małgorzata po Rym [?]
[podpis]       [podpis]       [podpis]
[podpis] Jack Morocoski [?]    Ktoszczelcen""",
        "pieczecie": [],
        "podpisy": ["~8 podpisów oficerów pułkowych"],
        "osoby": ["Stefan Głuchowski (adresat dedykacji)", "oficerowie 7 Pułku Ułanów Lubelskich"],
        "znaki_szczegolne": [
            "Dedykacja od kolegow pulkowych - intymny, ciepły ton",
            "'Kochanemu Stefankowi, wrocemu brykisci' - zdrobnienie!",
            "~8 podpisow - proba identyfikacji: Karpinski, Malgorzata(?), Morocoski(?)",
            "Prawdopodobnie z okazji demobilizacji lub pożegnania w Henstedt (1947)"
        ],
        "kontekst": "Dedykacja na karcie pamiątkowej 7 Pułku Ułanów Lubelskich z Henstedt (Niemcy, 1947). Oficerowie żegnają Stefana ciepłymi słowami. Stefan prawdopodobnie wracał do Polski (jako jeden z nielicznych), podczas gdy koło pułkowe kontynuowało działalność w Londynie."
    },

    # stefan_031 — Karta pamiątkowa 7 Pułku Ułanów Lubelskich
    "stefan_031": {
        "typ": "Karta pamiątkowa / okolicznościowa",
        "data": "23 marca 1947",
        "jezyk": "polski",
        "nadawca": "7 Pułk Ułanów Lubelskich im. Gen. Broni Sosnkowskiego",
        "adresat": "ppor. Głuchowski (Stefan)",
        "transkrypcja": """ppor. Głuchowski [odręcznie na górze, odwrócone]

7 Pułk Ułanów Lubelskich
im Gen Broni Sosnkowskiego

Henstedt  23. III. 47.""",
        "pieczecie": [],
        "podpisy": [],
        "osoby": ["ppor. Stefan Głuchowski", "Gen. Broni Kazimierz Sosnkowski (patron)"],
        "znaki_szczegolne": [
            "7 PUŁK UŁANÓW LUBELSKICH — pułk rodzinny Głuchowskich!",
            "Patron: Gen. Broni Kazimierz Sosnkowski",
            "Henstedt (Niemcy) — miejsce stacjonowania pułku po wojnie",
            "23 marca 1947 — demobilizacja w toku",
            "Czerwony romb — znak rozpoznawczy pułku",
            "Stefan przypisany jako ppor. (porucznik)"
        ],
        "kontekst": "Karta pamiątkowa 7 Pułku Ułanów Lubelskich im. Gen. Sosnkowskiego. Henstedt — obóz w Niemczech, gdzie pułk stacjonował po zakończeniu wojny (1945-1947). 23 marca 1947 to okres demobilizacji — żołnierze wybierali między Polską a emigracją. Stefan wybrał powrót do Polski."
    },

    # ═══════════════════════════════════════════════════════════════
    # juras_039 — Soldier's Service Book (Army Book 64) (ARG/V/105)
    # ═══════════════════════════════════════════════════════════════
    "juras_039": {
        "typ": "Książeczka wojskowa — Army Book 64",
        "data": "1945–1948",
        "jezyk": "angielski",
        "nadawca": "British Army / War Office",
        "adresat": "Głuchowski Krzysztof",
        "transkrypcja": """Army Book 64 (Part I)

43463/45

Soldier's Service Book.

(Soldier's Pay Book, Army Book 64 (Part II), will be
issued for active service.)

Entries in this book (other than those connected with the
marking of a Soldier's Kit and insertion of the names of
relatives) are to be made under the superintendence of an
Officer.

Instructions to Soldier.

1. You are held personally responsible for the safe
   custody of this book.
2. You will always carry this book on your person.
3. You must produce this book when called upon
   to do so by the Civil Police or by a com-petent military
   authority, viz., Officer, Warrant Officer, N.C.O. or Military
   Policeman.
[...]

[Lewa strona — DETAIL OF PERSONAL SIZED GARMENTS:]
ARTICLE / SIZE No.
Athletic, Web / Blouse, B.D. / Boots, ankle /
Cap, Bonnet or Helmet / Drawers / Greatcoat /
Jersey, pullover / Shirts / Shoes / Socks, worsted /
Trousers, B.D., S.D. or Shorts, K.D. / Vests, woollen

ALL RANKS
REMEMBER — Never discuss military, naval or air
matters, at meals or with strangers [...]
BE ON YOUR GUARD and report any suspicious individual.""",
        "pieczecie": [],
        "podpisy": [],
        "osoby": ["Krzysztof Głuchowski"],
        "znaki_szczegolne": [
            "Nr książeczki: 43463/45",
            "Army Book 64 Part I — standardowa książeczka brytyjska",
            "Okładka skórzana, mocno zużyta — noszona przy sobie przez lata",
            "Lewa strona: tabela rozmiarów umundurowania (pusta)",
            "Prawa strona: instrukcje dla żołnierza — obowiązek noszenia przy sobie"
        ],
        "kontekst": "Standardowa książeczka wojskowa Army Book 64 wydawana żołnierzom służącym pod dowództwem brytyjskim. Nr 43463/45. Zawierała dane osobowe, przebieg służby, odznaczenia i informacje o najbliższej rodzinie. Obowiązkowa do noszenia przy sobie — żołnierz był personalnie odpowiedzialny za jej bezpieczeństwo."
    },

    # ═══════════════════════════════════════════════════════════════
    # juras_047_odznaczenia — Notatki o odznaczeniach (ARG/V/113)
    # ═══════════════════════════════════════════════════════════════
    "juras_047_odznaczenia": {
        "typ": "Notatki odręczne — rejestr odznaczeń",
        "data": "XI.1946",
        "jezyk": "polski",
        "nadawca": "Krzysztof Głuchowski (notatki własne)",
        "adresat": "dokumentacja osobista",
        "transkrypcja": """[Notatki na kartce z notatnika, pismo odręczne:]

[...] — 13 [...] [...]
[...] odznaczenie [...] [...]
W [...] odznaczenie [...] [...]
[...] przyznane na dnia [...]

MEDAL WOJSKA
Rozkaz Nr 245    29.10.1946
Poz.    2 komp.    22.9.1946

ODZNAKA 3DSK
Rozkaz Dzienny Nr 256    12.11.1946
3DSK Nr 71/46 G.I.    8.11.1946
[...]    257/46""",
        "pieczecie": [],
        "podpisy": [],
        "osoby": ["Krzysztof Głuchowski"],
        "znaki_szczegolne": [
            "MEDAL WOJSKA — Rozkaz Nr 245, 29.10.1946 (2 kompania, 22.9.1946)",
            "ODZNAKA 3DSK — Rozkaz Dzienny Nr 256, 12.11.1946",
            "3DSK Nr 71/46 G.I. — numer ewidencyjny odznaki",
            "Notatki na kartce z notatnika z dziurkami",
            "Pismo atramentem, częściowo trudne do odczytu"
        ],
        "kontekst": "Notatki Krzysztofa rejestrujące jego odznaczenia: Medal Wojska (Rozkaz Nr 245 z 29.X.1946) i Odznaka 3 Dywizji Strzelców Karpackich (Rozkaz Dzienny Nr 256 z 12.XI.1946). Medal Wojska — polskie odznaczenie za udział w walkach 1939–1945. Odznaka 3DSK — odznaka dywizji, w której służył Krzysztof (Gimnazjum i Liceum 3 DSK)."
    },

    # ═══════════════════════════════════════════════════════════════
    # juras_056_odznaka_ak — Odznaka Pamiątkowa AK Nr 404 (ARG/V/122)
    # ═══════════════════════════════════════════════════════════════
    "juras_056_odznaka_ak": {
        "typ": "Legitymacja Odznaki Pamiątkowej AK",
        "data": "12.VI.1946",
        "jezyk": "polski",
        "nadawca": "Komisja Weryfikacyjna AK, Dowództwo 2 Korpusu",
        "adresat": "Głuchowski Krzysztof",
        "transkrypcja": """starszy ułan
(stopień)

GŁUCHOWSKI    KRZYSZTOF
(nazwisko i imię)

JURAS
(pseudonim)

Nr 404

Data przyznania 12 czerwca 46

PRZEWODNICZĄCY KAPITUŁY
[pieczęć]
[podpis: Leszczyński (?)]

DOWÓDZTWO 2 KORPUSU
KOMISJA WERYFIKACYJNA A.K.
[podpis]""",
        "pieczecie": ["Pieczęć okrągła — Dowództwo 2 Korpusu / Komisja Weryfikacyjna AK"],
        "podpisy": ["Przewodniczący Kapituły (Leszczyński?)", "Komisja Weryfikacyjna AK"],
        "osoby": ["Krzysztof Głuchowski (ps. Juras, st. ułan)"],
        "znaki_szczegolne": [
            "Odznaka Pamiątkowa AK Nr 404",
            "Pseudonim: JURAS (wariant zapisu — bez ś)",
            "Stopień: starszy ułan",
            "Data przyznania: 12 czerwca 1946",
            "Pieczęć i dwa podpisy — Przewodniczący Kapituły i Komisja Weryfikacyjna",
            "Format małej legitymacji / karteczki"
        ],
        "kontekst": "Legitymacja Odznaki Pamiątkowej Armii Krajowej Nr 404, wydana przez Komisję Weryfikacyjną AK przy Dowództwie 2 Korpusu Polskiego. Data 12 czerwca 1946 — ta sama co weryfikacja AK (ARG/V/112). Pseudonim 'Juras' bez znaku diakrytycznego (w innych dokumentach: 'Juraś'). Odznaka pamiątkowa AK — odróżniać od Krzyża AK (ARG/V/118), który został nadany w 1968 r."
    },

    # ═══════════════════════════════════════════════════════════════
    # juras_046 — WERYFIKACJA AK — notatki weryfikacyjne (ARG/V/112)
    # ═══════════════════════════════════════════════════════════════
    "juras_046": {
        "typ": "Notatki weryfikacyjne AK (dwie kartki)",
        "data": "12.VI.1946",
        "jezyk": "polski",
        "nadawca": "Komisja Weryfikacyjna AK, 7 P.Uł., Kraków",
        "adresat": "akta weryfikacyjne Głuchowskiego",
        "transkrypcja": """[Kartka górna:]
Ukończył Gymnasium
Nr 65/46  15.3.1946
Rozkaz Dnia 335 [...]
Nr 15  5.3.1946. G.I. prt.2

[Kartka dolna:]
WERYFIKACJA AK    Nr 155
7 P.Uł. [?] Kraków [?]
Część I & [?]

Głuchowski Krzysztof — Stanisław

[...] Bat. 1112 [...] 2 Komp.
w 45/46 [...] AK [...]

1°) Narożański [...] St.[?]...
     Szeregowiec   1926   Rocznik 1944
     [...] [...]

     1134/II.AK/46
     12.VI.1946""",
        "pieczecie": [],
        "podpisy": [],
        "osoby": ["Krzysztof Głuchowski (syn Stanisława)", "Narożański (świadek weryfikacji)"],
        "znaki_szczegolne": [
            "Nr weryfikacji 155 — numer w rejestrze Komisji",
            "Głuchowski Krzysztof — Stanisław = imię ojca (potwierdza: ojciec = Stanisław)",
            "Bat. 1112, 2 Komp. — przydział AK",
            "Narożański — świadek weryfikacji, szeregowiec, rocznik 1926",
            "Numer akt: 1134/II.AK/46 — ten sam co zaświadczenie ARG/V/97",
            "Dwie kartki z notatnika z dziurkami — notatki robocze komisji",
            "Wzmianka o ukończeniu Gimnazjum (Nr 65/46)"
        ],
        "kontekst": "Notatki robocze Komisji Weryfikacyjnej AK z Krakowa. Potwierdzają: Krzysztof syn Stanisława, Bat. 1112, 2 Kompania. Narożański jako świadek. Numer akt 1134/II.AK/46 identyczny z zaświadczeniem ARG/V/97 (juras_031) — są częścią tego samego procesu weryfikacyjnego."
    },

    # ═══════════════════════════════════════════════════════════════
    # juras_052 — Legitymacja Krzyża Armii Krajowej (ARG/V/118)
    # KLUCZOWY DOKUMENT — pseudonim, przydział, podpis Ziemskiego
    # ═══════════════════════════════════════════════════════════════
    "juras_052": {
        "typ": "Legitymacja odznaczenia — Krzyż Armii Krajowej",
        "data": "7.III.1968",
        "jezyk": "polski",
        "nadawca": "K. Ziemski — «Wachnowski», Z-ca D-cy W-skiego Korpusu A.K.",
        "adresat": "Głuchowski Krzysztof",
        "transkrypcja": """Nazwisko: GŁUCHOWSKI
Imię: KRZYSZTOF
Pseudonim: «JURAŚ»
Przydział: Zw.Komp./Plut.III/2.
7 PUŁK UŁAN.LUBEL. «JELEŃ»

Odznaczony został

KRZYŻEM ARMII KRAJOWEJ

ustanowionym dnia 1 sierpnia 1966 roku
przez dowódcę A.K. gen. Tadeusza Bora-
Komorowskiego dla upamiętnienia wysiłku
żołnierza Polski Podziemnej w latach
1939 — 1945.

                              Podpis:
K. Ziemski — «Wachnowski»
Z-ca D-cy W-skiego Korpusu A.K.

Londyn, dnia
7.3.68""",
        "pieczecie": [],
        "podpisy": ["K. Ziemski — «Wachnowski», Z-ca D-cy Warszawskiego Korpusu AK"],
        "osoby": ["Krzysztof Głuchowski (ps. Juraś)", "K. Ziemski (ps. Wachnowski)", "gen. Tadeusz Bór-Komorowski"],
        "znaki_szczegolne": [
            "PSEUDONIM «JURAŚ» — oficjalnie potwierdzone",
            "Przydział: Zw.Komp./Plut.III/2 — Związkowa Kompania, Pluton III, sekcja 2",
            "7 PUŁK UŁAN.LUBEL. «JELEŃ» — pełna nazwa pułku z kryptonimem",
            "Podpisana przez Ziemskiego-Wachnowskiego — tego samego co zaświadczenie ARG/V/43",
            "Londyn, 7 marca 1968 — 24 lata po Powstaniu",
            "Odznaczenie ustanowione 1.VIII.1966 przez Bora-Komorowskiego",
            "Druk z odręcznymi wpisami atramentem niebieskim"
        ],
        "kontekst": "Legitymacja Krzyża Armii Krajowej — odznaczenia ustanowionego 1 sierpnia 1966 r. przez gen. Tadeusza Bora-Komorowskiego dla żołnierzy Polski Podziemnej. Podpisana przez płk. Karola Ziemskiego (ps. Wachnowski) — Zastępcę Dowódcy Warszawskiego Korpusu AK, tego samego oficera, który zaświadczał o służbie Krzysztofa w 1946 (ARG/V/43). Dokument potwierdza: pseudonim JURAŚ, przydział do Plutonu III/sekcja 2 Związkowej Kompanii 7 Pułku Ułanów Lubelskich «Jeleń»."
    },

    # ═══════════════════════════════════════════════════════════════
    # juras_057_prc — Certyfikat P.R.C. (ARG/V/123)
    # ═══════════════════════════════════════════════════════════════
    "juras_057_prc": {
        "typ": "Certyfikat służby — Polish Resettlement Corps",
        "data": "19.II.1948",
        "jezyk": "angielski",
        "nadawca": "P.R.C. Record Office, Watley Camp, Godalming, Surrey",
        "adresat": "Głuchowski Krzysztof",
        "transkrypcja": """P.R.C. Record Office
Watley Camp
nr. Godalming, Surrey
Tel. Godalming 1520 Ext.101
Ref.No. 2335/  /48

19 FEB 1948

CERTIFICATE

This is to certify that No. 3004271
L/CPL GLUCHOWSKI KRZYSZTOF was enlisted into
P.R.C. 1.11.46, after serving with Polish Forces
under British Command from 14.7.45 to 1.11.46.

                              Record Officer
                              [podpis]
                              Biuro Ew. PKPR""",
        "pieczecie": [],
        "podpisy": ["Record Officer, Biuro Ewidencji PKPR"],
        "osoby": ["Krzysztof Głuchowski (L/CPL, No. 3004271)"],
        "znaki_szczegolne": [
            "Numer wojskowy: 3004271",
            "Stopień: L/CPL (Lance Corporal = starszy ułan)",
            "Służba w Polish Forces: 14.7.45 — 1.11.46",
            "Zaciąg do P.R.C.: 1.11.46",
            "Watley Camp, Godalming, Surrey — siedziba biura PRC",
            "Ref.No. 2335/  /48",
            "Dwujęzyczny podpis: Record Officer / Biuro Ew. PKPR"
        ],
        "kontekst": "Certyfikat potwierdzający przebieg służby: Polish Forces pod dowództwem brytyjskim od 14 lipca 1945 do 1 listopada 1946, następnie zaciąg do Polish Resettlement Corps (PKPR/PRC) od 1 listopada 1946. Numer 3004271. Watley Camp w Godalming (Surrey) — centralne biuro ewidencji PRC. PKPR = Polski Korpus Przysposobienia i Rozmieszczenia — organizacja pośrednia między demobilizacją a cywilnym osiedleniem w Wielkiej Brytanii."
    },

    # ═══════════════════════════════════════════════════════════════
    # juras_031 — Zaświadczenie Komisji Weryfikacyjnej AK (ARG/V/97)
    # ═══════════════════════════════════════════════════════════════
    "juras_031": {
        "typ": "Zaświadczenie Komisji Weryfikacyjnej AK",
        "data": "24.VI.1946",
        "jezyk": "polski",
        "nadawca": "Komisja Weryfikacyjna AK, Kraków",
        "adresat": "Głuchowski Krzysztof",
        "transkrypcja": """DOWÓDCA
7 Pułku Uł. Lubelskich

Kp. dnia 24.VI.1946.

L.dz. 1134/II/IV/46

Na skutek przedstawionych dowodów i to jako Dowódcy z Krakowa
Komisja weryfikacyjna A.K. stwierdza, że

GŁUCHOWSKI KRZYSZTOF    rocznik 1926
(imię i nazwisko, rocznik i Nr ewid.)

w stopniu szeregowca
(stopień boku szeregowca.)

z pozostawieniem dotychczas-
owego boku szeregowca.

PRZEWODNICZĄCY
KOMISJI WERYFIKACYJNEJ A.K.
(urzędnik pieczęć)

Komendant Napędowy Nr 3""",
        "pieczecie": ["Komisja Weryfikacyjna AK — pieczęć okrągła"],
        "podpisy": ["Przewodniczący Komisji Weryfikacyjnej AK", "Komendant Napędowy Nr 3"],
        "osoby": ["Krzysztof Głuchowski"],
        "znaki_szczegolne": [
            "L.dz. 1134/II/IV/46 — numer dziennika podawczego",
            "7 Pułk Ułanów Lubelskich — potwierdzenie przynależności",
            "Rocznik 1926 — potwierdzony rok urodzenia",
            "Stopień: szeregowiec (w AK, przed awansem na st. strzelca)",
            "Kraków, 24 czerwca 1946 — weryfikacja w Polsce"
        ],
        "kontekst": "Zaświadczenie Komisji Weryfikacyjnej AK potwierdzające służbę Krzysztofa Głuchowskiego w stopniu szeregowca w 7 Pułku Ułanów Lubelskich AK. Komisje weryfikacyjne działały po wojnie, potwierdzając tożsamość i służbę żołnierzy AK na podstawie zeznań świadków i dokumentów."
    },

    # ═══════════════════════════════════════════════════════════════
    # juras_032 — Pismo ppłk. Andersa — Szef Wydziału Rodzin Wojskowych (ARG/V/98)
    # ═══════════════════════════════════════════════════════════════
    "juras_032": {
        "typ": "Pismo urzędowe — Wydział Rodzin Wojskowych",
        "data": "1.III.1949",
        "jezyk": "polski",
        "nadawca": "ppłk ANDERS, Szef Wydziału Rodzin Wojskowych",
        "adresat": "St.Uł. Głuchowski Krzysztof Andrzej, 25 Belney Airfield, Thetford, Norfolk",
        "transkrypcja": """Szef Sztabu Opieki nad Żołnierzem
L.dz. 2083/50/Opieki/IV/3./48
Londyn, dnia 1 marca 1949 r.
Żołnierz pozostający na [...]

St.Uł. Głuchowski Krzysztof Andrzej
25 Belney Airfield Thetford
Norfolk

W nawiązaniu do [rozmowy?] odpowiadamy na zapytanie [...]
w sprawie [...] Kolekcji [...] także Pan
[...] ok. dnia [...] świadczeniu, do
[Ministerialnego?] [...] w Instrukcji [...] sprawdzeniu rodzin z Kontynentu

[...] likwidację interes[ów]. [...] od dnia
[...] Ministeriat [...] z wniosków [...] do dnia 15 marca 19[...]
[...] należeć nadzieję na [...] [...]
[...] list naprawiony dla [...] opr.

SZEF WYDZIAŁU RODZIN WOJSKOWYCH

ANDERS    ppłk.""",
        "pieczecie": [],
        "podpisy": ["ANDERS ppłk., Szef Wydziału Rodzin Wojskowych"],
        "osoby": ["Krzysztof Głuchowski", "ppłk Anders (Szef Wydziału Rodzin Wojskowych)"],
        "znaki_szczegolne": [
            "Podpisany: ANDERS ppłk. — Szef Wydziału Rodzin Wojskowych (NIE gen. Władysław Anders!)",
            "Adres Krzysztofa: 25 Belney Airfield, Thetford, Norfolk — baza RAF/PRC",
            "L.dz. 2083/50/Opieki/IV/3./48 — numer korespondencji",
            "Dotyczy spraw rodzinnych — łączność z rodziną na Kontynencie",
            "Maszynopis na papierze urzędowym, częściowo nieczytelny (zagniecenia)"
        ],
        "kontekst": "Pismo od ppłk. Andersa (Szefa Wydziału Rodzin Wojskowych, NIE gen. Władysława Andersa) do st.uł. Głuchowskiego w sprawie kontaktu z rodziną na Kontynencie. Adres 25 Belney Airfield, Thetford, Norfolk — baza RAF, gdzie stacjonowali polscy żołnierze PRC. Wydział Rodzin Wojskowych pomagał żołnierzom PSZ w utrzymaniu kontaktu z rodzinami w Polsce i na emigracji."
    },

    # ═══════════════════════════════════════════════════════════════
    # juras_034 — Zaświadczenie o zakończeniu służby PSZ (ARG/V/100)
    # ═══════════════════════════════════════════════════════════════
    "juras_034": {
        "typ": "Zaświadczenie o zakończeniu służby wojskowej",
        "data": "24.II.1949",
        "jezyk": "polski",
        "nadawca": "Komisja Likwidacyjna Polskich Sił Zbrojnych",
        "adresat": "Głuchowski Krzysztof",
        "transkrypcja": """POLSKIE SIŁY ZBROJNE

ZAŚWIADCZENIE
O ZAKOŃCZENIU SŁUŻBY

Nr 87949

Stwierdzam, że

Krzysztof    Głuchowski
(imię i imiona)    (nazwisko)

4 [?]    starszy ułan
R.N.S. [...]    (stopień)

Służył w Polskich Siłach Zbrojnych
[Począwszy?] [...] pod Dowództwem Brytyjskim do dnia...

Londyn, dnia 24/II/1949

[pieczęć okrągła]
KOMISJA LIKWIDACYJNA
POLSKICH SIŁ ZBROJNYCH

[podpis]""",
        "pieczecie": ["KOMISJA LIKWIDACYJNA POLSKICH SIŁ ZBROJNYCH (pieczęć okrągła)"],
        "podpisy": ["Przewodniczący Komisji Likwidacyjnej PSZ"],
        "osoby": ["Krzysztof Głuchowski"],
        "znaki_szczegolne": [
            "Nr 87949 — numer zaświadczenia PSZ",
            "Stopień: starszy ułan — ostateczny stopień w PSZ",
            "Londyn, 24.II.1949 — oficjalna data zakończenia służby",
            "Pieczęć Komisji Likwidacyjnej PSZ",
            "Orzeł polski w nagłówku",
            "Druk urzędowy z odręcznymi wpisami"
        ],
        "kontekst": "Oficjalne zaświadczenie o zakończeniu służby w Polskich Siłach Zbrojnych. Nr 87949. Krzysztof Głuchowski, starszy ułan, zakończył służbę 24 lutego 1949 w Londynie. Komisja Likwidacyjna PSZ — organ powołany do formalnego rozwiązania Polskich Sił Zbrojnych na Zachodzie po II wojnie światowej."
    },

    # ═══════════════════════════════════════════════════════════════
    # juras_047 — Fiche de Transport (ARG/V/47, Seria_29z_p25)
    # ═══════════════════════════════════════════════════════════════
    "juras_047": {
        "typ": "Karta transportowa (Fiche de Transport)",
        "data": "27.VI.1945",
        "jezyk": "francuski",
        "nadawca": "Ministère des Prisonniers, Déportés et Réfugiés",
        "adresat": "Głuchowski Krzysztof",
        "transkrypcja": """RÉPUBLIQUE FRANÇAISE
Ministère des Prisonniers, Déportés et Réfugiés

FICHE DE TRANSPORT   1492839

Nom: GLUHOWSKI   Prénom: Cristophe
Date naissance: 29 XI 1926
Adresse: Caserne Bessines

AVIS SERVICE SANTÉ: D   R

[stempel] 27/VI/1945""",
        "pieczecie": ["Stempel datowy 27/VI/1945"],
        "podpisy": [],
        "osoby": ["Krzysztof Głuchowski"],
        "znaki_szczegolne": [
            "Nr 1492839 — identyczny z Carte de Rapatrié (ARG/V/46)",
            "Nazwisko w pisowni francuskiej: GLUHOWSKI",
            "Imię: Cristophe (fonetyczna transkrypcja Krzysztof)",
            "Data urodzenia: 29 XI 1926 — potwierdza rok 1926",
            "Caserne Bessines — koszary w St. Ouen pod Paryżem"
        ],
        "kontekst": "Karta transportowa repatrianta uprawniająca do darmowego przejazdu kolejowego po Francji. Wydana przez Ministère des Prisonniers, Déportés et Réfugiés. Caserne Bessines w St. Ouen — miejsce kwaterowania polskich repatriantów."
    },

    # ═══════════════════════════════════════════════════════════════
    # juras_048 — Skierowanie z Ambasady RP na kurs (ARG/V/48, Seria_29z_p27)
    # ═══════════════════════════════════════════════════════════════
    "juras_048": {
        "typ": "Skierowanie urzędowe",
        "data": "29.VI.1945",
        "jezyk": "polski",
        "nadawca": "A. Drogowski, Naczelny Instruktor Oświatowy, Ambasada RP w Paryżu",
        "adresat": "Głuchowski K.",
        "transkrypcja": """AMBASSADE de POLOGNE
à Paris

Pan Głuchowski K. zostanie skierowany
przez Naczelny Instruktorat Oświatowy na kurs, który rozpocznie się
w dniu 15 Lipca b.r. w Villard-de-Lans.

A. Drogowski
Naczelny Instruktor Oświatowy

Paryż, dnia 29 czerwca 1945r.""",
        "pieczecie": [],
        "podpisy": ["A. Drogowski, Naczelny Instruktor Oświatowy"],
        "osoby": ["Krzysztof Głuchowski", "A. Drogowski"],
        "znaki_szczegolne": [
            "Papier firmowy Ambasady RP w Paryżu",
            "Villard-de-Lans — ośrodek kursów oświatowych w Alpach (Isère)",
            "Kurs miał zacząć się 15 lipca — Krzysztof NIE pojechał (wstąpił do PSZ 14.VII.1945)"
        ],
        "kontekst": "Skierowanie na kurs oświatowy we Francji, którego Krzysztof ostatecznie nie odbył — dzień przed planowanym początkiem kursu (15.VII) wstąpił do Polskich Sił Zbrojnych we Włoszech (14.VII.1945)."
    },

    # ═══════════════════════════════════════════════════════════════
    # juras_053 — List Krzysztofa z Paryża (ARG/V/53, Seria_29z_p26)
    # ═══════════════════════════════════════════════════════════════
    "juras_053": {
        "typ": "List prywatny",
        "data": "ok. VI–VII.1945",
        "jezyk": "polski",
        "nadawca": "Krzysztof Andrzej Głuchowski ('Krusio')",
        "adresat": "Rodzina (bliscy)",
        "transkrypcja": """Kochani moi Kochany! Przyjeżdżajcie za mną gdy ja
jadę. Ojciec [...] o babce jest razem z [...].
[...] Krzysztof [...] być w [...] adresie jest [...]
Nie [...] My [...] obecnie
razem z [...] w Paryżu. [...] samochodem
[...] brak dalej.
[...] pomocy. [...]
Kochany nie wiem jak bardzo tu [...]
ale [...] garażu nie chciałbym się
[...] starci [...] niż brat. Mój adres obecnie

Caserne Bessines Paryż
metro Fort de Plaisy St. Ouen
ppor. Radomyski komp. 8 sala 71

Całuję się mocno i do zobaczenia
Krusio""",
        "pieczecie": [],
        "podpisy": ["Krusio (Krzysztof Głuchowski)"],
        "osoby": ["Krzysztof Głuchowski", "ppor. Radomyski Janusz", "ojciec (Stanisław Głuchowski)", "babka"],
        "znaki_szczegolne": [
            "Podpisany 'Krusio' — familijne zdrobnienie od Krzysztof",
            "Adres: Caserne Bessines, metro Fort de Plaisy, St. Ouen",
            "Ppor. Radomyski — towarzysz i późniejszy świadek służby AK",
            "Atrament niebieski, pismo odręczne",
            "Wiele fragmentów trudnych do odczytania"
        ],
        "kontekst": "List do rodziny z okresu pobytu w Caserne Bessines w Paryżu (VI–VII.1945). Wspomina ojca (Stanisława) i babkę. Ppor. Radomyski Janusz (ur. 1922) — ten sam świadek, który poświadczył służbę AK Krzysztofa (por. ARG/V/41). Poprzednio błędnie datowany na '3.II.1944'."
    },

    # ═══════════════════════════════════════════════════════════════
    # juras_054 — Skierowanie na RENTGEN (ARG/V/54, Seria_29z_p29)
    # ═══════════════════════════════════════════════════════════════
    "juras_054": {
        "typ": "Skierowanie medyczne",
        "data": "21.VII.1945",
        "jezyk": "polski",
        "nadawca": "Lekarz Pułku 7 P.Uł.L., ppor. lek. Cisek",
        "adresat": "7 Szpital Wojenny Polish Gen. Hosp.",
        "transkrypcja": """RENTGEN

7 PUŁK UŁANÓW LUBELSKICH
im. Gen. K. Sosnkowskiego
LEKARZ

M.p., dnia 21/7 1945 r.

Laboratorium: Rtg. 1 bat. Art.
Przysyłam: H. ułana Głuchowskiego Krzysztofa
Celem: Rtg klatki piersiowej
Rozpoznanie: Susp. g. Plc. pulmonum

[pieczęć] 7 SZPITAL WOJENNY POLISH GEN. HOSP.
27.7.45

Proszę o prześwietlenie płuc.

Lekarz Pułku
Cisek
ppor. lek.""",
        "pieczecie": ["7 PUŁK UŁANÓW LUBELSKICH im. Gen. K. Sosnkowskiego — LEKARZ", "7 SZPITAL WOJENNY POLISH GEN. HOSP."],
        "podpisy": ["ppor. lek. Cisek, Lekarz Pułku"],
        "osoby": ["Krzysztof Głuchowski", "ppor. lek. Cisek"],
        "znaki_szczegolne": [
            "Nagłówek: 7 Pułk Ułanów Lubelskich im. Gen. K. Sosnkowskiego",
            "Rozpoznanie: Susp. Plc. pulmonum — podejrzenie zmian w płucach",
            "Pieczęć szpitalna z datą 27.7.45 — RTG wykonane 6 dni po skierowaniu",
            "Papier kremowy, pożółkły, pismo odręczne atramentem"
        ],
        "kontekst": "Skierowanie na RTG płuc — wskazuje na problemy zdrowotne po pobycie w obozie jenieckim (Stalag IV-B Mühlberg). 7 Pułk Ułanów Lubelskich im. Gen. Kazimierza Sosnkowskiego — pułk, w którym służył Krzysztof po wstąpieniu do PSZ."
    },

    # ═══════════════════════════════════════════════════════════════
    # juras_056 — Przepustka z Amandola (ARG/V/56, Seria_29z_p30)
    # ═══════════════════════════════════════════════════════════════
    "juras_056": {
        "typ": "Przepustka wojskowa",
        "data": "1946",
        "jezyk": "polski / angielski",
        "nadawca": "Komendant Gimnazjum i Liceum 3 D.K., kpt. Kapica Józef",
        "adresat": "Głuchowski Krzysztof",
        "transkrypcja": """PRZEPUSTKA

Nr ewid. 1846
Stopień: [...]
Nazwisko i imię: Głuchowski Krzysztof
z Gimnazjum i Liceum 3 D.K. / Oddz.

Kwateruje w m. Amandola
i ma zezwolenie przebywania poza służbą w tejże
miejscowości codziennie do godz. 2159

and is permitted to be absent from his quarters in that
town when off duty until 2159 hrs daily.

Komendant
Kapica Józef, kapitan

UWAGA: Podoficerowie od plutonowego w górę do g. 2359.""",
        "pieczecie": ["Gimnazjum i Liceum 3 D.K. (pieczęć okrągła)"],
        "podpisy": ["kpt. Kapica Józef, Komendant"],
        "osoby": ["Krzysztof Głuchowski", "kpt. Kapica Józef"],
        "znaki_szczegolne": [
            "Formularz dwujęzyczny (polsko-angielski)",
            "Amandola — miasteczko we Włoszech, siedziba Gimnazjum 3 DSK",
            "Godzina powrotu: 21:59 (podoficerowie do 23:59)"
        ],
        "kontekst": "Przepustka z Gimnazjum i Liceum 3. Dywizji Strzelców Karpackich w Amandola (Włochy). Krzysztof uczył się tu w ramach systemu oświaty PSZ, przygotowując się do matury (zdanej 9.II.1946)."
    },

    # ═══════════════════════════════════════════════════════════════
    # juras_057_ppj — Przepustka z Punktu Przesyłkowego Joncov (ARG/V/57, Seria_29z_p31)
    # ═══════════════════════════════════════════════════════════════
    "juras_057_ppj": {
        "typ": "Przepustka obozowa",
        "data": "1946",
        "jezyk": "polski",
        "nadawca": "Komendant P.P.J. — ppor. Kucharski",
        "adresat": "Głuchowski Krzysztof",
        "transkrypcja": """Punkt Przesyłkowy Joncov 2 Korpusu

M.p. [...] 194[...]

Przepustka

Głuchowski Krzysztof z Obozu P.P.J.
ma prawo opuścić rejon obozu i udać się do: Pesaro.
Przepustka ważna na dzień [...] do godz. 13:45.

Komendant P.P.J.
Kucharski ppor.""",
        "pieczecie": ["Punkt Przesyłkowy Joncov 2 Korpusu (pieczęć okrągła)"],
        "podpisy": ["ppor. Kucharski, Komendant P.P.J."],
        "osoby": ["Krzysztof Głuchowski", "ppor. Kucharski"],
        "znaki_szczegolne": [
            "Wypełniona czerwonym atramentem",
            "Papier pożółkły, częściowo nieczytelny",
            "Pesaro — miasto na Adriatyku, cel wyjścia z obozu"
        ],
        "kontekst": "Przepustka z Punktu Przesyłkowego Joncov 2. Korpusu Polskiego we Włoszech. Pesaro — miasto portowe na Adriatyku, odwiedzane przez żołnierzy w wolnym czasie."
    },

    # ═══════════════════════════════════════════════════════════════
    # juras_065_gimn — Świadectwo Ukończenia Gimnazjum (ARG/V/65, Seria_29z_p37)
    # ═══════════════════════════════════════════════════════════════
    "juras_065_gimn": {
        "typ": "Świadectwo szkolne",
        "data": "7.I.1946",
        "jezyk": "polski",
        "nadawca": "MWRiOP / Państwowa Komisja Egzaminacyjna dla Eksternów",
        "adresat": "Głuchowski Krzysztof Andrzej",
        "transkrypcja": """MINISTERSTWO WYZNAŃ RELIGIJNYCH I OŚWIECENIA PUBLICZNEGO
PAŃSTWOWA KOMISJA EGZAMINACYJNA DLA EKSTERNÓW

Nr 43

ŚWIADECTWO UKOŃCZENIA
GIMNAZJUM OGÓLNOKSZTAŁCĄCEGO

Krzysztof Andrzej Głuchowski
urodzony dnia 29 listopada [1926]
w Warszawa, województwo Warszawa
wyznania rzym.-kat.

złożył nadzwyczajny egzamin [...]
dnia 9 Lutego 1946 roku

L. Dz. 32/Edn/46, dnia 7 Stycznia 1946""",
        "pieczecie": ["Orzeł Polski (nagłówek)", "Pieczęć M.P. na zdjęciu"],
        "podpisy": ["Delegat W.R. i O.P."],
        "osoby": ["Krzysztof Andrzej Głuchowski"],
        "znaki_szczegolne": [
            "Ze zdjęciem legitymacyjnym w mundurze",
            "Egzamin eksternistyczny — zdawany poza normalnym trybem szkolnym",
            "Druk urzędowy z herbem Polski",
            "Pieczęć 'M.P.' na zdjęciu"
        ],
        "kontekst": "Świadectwo ukończenia gimnazjum ogólnokształcącego zdane eksternistycznie w ramach systemu oświaty PSZ we Włoszech. Komisja egzaminacyjna działała przy Gimnazjum i Liceum 3 DSK w Amandola. Krzysztof zdał maturę gimnazjalną 9 lutego 1946 — miał wtedy 19 lat."
    },

    # ═══════════════════════════════════════════════════════════════
    # wa_aliens_reg — Aliens Registration gen. Janusza Głuchowskiego (ARG/II/65-66)
    # ═══════════════════════════════════════════════════════════════
    "wa_aliens_reg": {
        "typ": "Certyfikat rejestracji cudzoziemca",
        "data": "1940–1986",
        "jezyk": "angielski",
        "nadawca": "Home Office / Metropolitan Police",
        "adresat": "Gen. Janusz Głuchowski",
        "transkrypcja": """[OKŁADKA:]
A 274782
Aliens Order, 1920.
CERTIFICATE OF REGISTRATION
You must produce this certificate if required to do so by any Police
Officer, Immigration Officer, or member of His Majesty's forces
acting in the course of his duty.

[STRONA ZE ZDJĘCIEM:]
Registration Certificate No. [...] 79 [...]
Name: GŁUCHOWSKI Janusz
Date: 28/2/[49?]
[Zdjęcie: starszy mężczyzna, łysy, z wąsem]
Signature: Janusz Głuchowski [odręcznie]

[DANE OSOBOWE:]
Nationality: Polish
Born on: 6.8.88    Bukowina
Nationality of wife: [?]
Profession or Occupation: No occupation
Single or Married: Married
Name of [...]: Elizabeth [?]
Address: [...] College [...] F[?]
[...] in United Kingdom: [...] Palestine [?]
[...]: Polish Forces, Aug 1940
[...] PMC 22/6/[?]    discharged 29/6/49
Passport: Army Form W.M.06.
[...] P 5993 [...]

[PIECZĄTKI:]
Police serial No. 87[?]2578
[Pieczęć:] ALIENS REGISTRATION / METROPOLITAN POLICE
[Data:] 2 FEB 1951
[...] Kensington [...]
15/9/55
26.9.86

[ZWOLNIENIE:]
ALIENS ORDER, 1940.
The holder is
EXEMPT FROM REGISTRATION
with the police but should retain
this certificate.
[Pieczęć:] CHECKED
[Pieczęć:] METROPOLITAN POLICE OFFICE""",
        "pieczecie": [
            "ALIENS REGISTRATION / METROPOLITAN POLICE",
            "METROPOLITAN POLICE OFFICE",
            "CHECKED"
        ],
        "podpisy": ["Janusz Głuchowski (odręcznie)"],
        "osoby": ["Gen. dyw. Janusz Głuchowski", "Elizabeth (żona?)"],
        "znaki_szczegolne": [
            "A 274782 — numer rejestracji",
            "JEDYNE ZNANE ZDJĘCIE gen. Głuchowskiego w kolekcji",
            "Ur. 6.8.1888 Bukowina — potwierdzenie",
            "Żona: Elizabeth (nie Maria Bukowska jak w niektórych źródłach?)",
            "Polish Forces od VIII.1940, discharged 29.VI.1949",
            "Dokument prowadzony od 1940 do 1986 — 46 LAT!",
            "Ostatecznie EXEMPT FROM REGISTRATION",
            "Kensington — dzielnica Londynu, adres Głuchowskiego",
            "Army Form W.M.06, P 5993 — numer paszportu wojskowego"
        ],
        "kontekst": "Certyfikat rejestracji cudzoziemca gen. dyw. Janusza Głuchowskiego — Aliens Order 1920. Nr A 274782. Dokument prowadzony przez Metropolitan Police od 1940 do 1986 (pieczątki z 1951, 1955, 1986). Generał, I Wiceminister Spraw Wojskowych RP, Dowódca JWWB, musiał cyklicznie meldować się na policji jako 'alien'. Ostatecznie zwolniony z obowiązku rejestracji (EXEMPT). Zdjęcie: starszy mężczyzna, łysy, z wąsem. UWAGA: żona zapisana jako 'Elizabeth' — wymaga weryfikacji (Maria Bukowska? Elizabeth to angielskie imię Elżbiety?)."
    },

    # ═══════════════════════════════════════════════════════════════
    # wa_biogram_krzysztof — AUTOBIOGRAM Krzysztofa (ARG/VI/14 lub powiązany)
    # KLUCZOWY DOKUMENT — NAPISANY PRZEZ SAMEGO KRZYSZTOFA W 1995!
    # ═══════════════════════════════════════════════════════════════
    "wa_biogram_krzysztof": {
        "typ": "Biogram / autobiografia",
        "data": "18.X.1995",
        "jezyk": "polski",
        "nadawca": "Krzysztof Głuchowski",
        "adresat": "publikacja / archiwum",
        "transkrypcja": """KRZYSZTOF GŁUCHOWSKI PSEUDONIM «JURAŚ»

Syn Stanisława Stefana Głuchowskiego i Wandy z Głuchowskich ur. 29.11.1926 w Warszawie. Uczęszczał do
6 klasowej Szkoły Rodziny Wojskowej, którą skończył w czerwcu 1939 roku po czym zdał egzamin [...]
[...] Na I wojnę [...]

W czasie okupacji jest uczniem szkół handlowych / [...] Korporacja [...] III [...]
[...] Służył [...]
część powojennych [...] do cywilnego [...]

U kompanii brał udział od sierpień 1941 roku [wstąpieniu] do ZWZ a następnie w Armii Krajowej, początkowo w
Kompanii Kadeci a od 1943 roku w [...] Pułku Ułanów Lubelskich AK — kryptonim «Jeleń», na przydział w plutonie 1112.
[...] Okręgu Warszawskiego na terenie [Włoch?].

W Powstaniu [...] płk. dypl. Karol [...] Dowódca [...]
[...] do rejonu Walk [...] teren [...] stanowisko [...] obronie
z [...] na Kamczatce [...] do [...]
[...] dowodzi [...] Wachnowski [...] do obrony [...]
w budynku [...] Wola [...] Cmentarz [...] Kaplicy Matki [...] Powązki [...]
Czerniaków. Ok. 41 żołnierzy [...] widzieliśmy [...]
[...] Dowódcami Okręgu Warszawskiego «Monter» - Chruściel.
[...] Krzysztof [...] Głuchowski [...] do stopnia starszego strzelca. Po kapitulacji
wzięty jako jeniec do Niemiec, gdzie przechodzi przez obozy w Fallingbostel [...] Dorsten [...]
do [...] Mándler [...] [...]
[...] statkiem [...] do Francji. [...]

[...] Holandii, Belgii i Francji przedostaje się do [...] Korpusu Armii Polskiej gen. Andersa do Włoszech
[...] 7 Pułku Ułanów Lubelskich, I [...] dywizja [...]
Dywizji Strzelców Karpackich, zdaje małą, a [...] jest w Anglii matur[ę].
[...] na rachunkach angielskich dyplom [...] Chartered Engineer. Po [...]
[...] prywatną firmą V.I.[...] [...] Jest
kierownikiem [...] Project Engineer, Coordinator for East Europe and Spain. Sales Engineering Manager [...] fili[i]
[...] w Brazylii [...] São Paulo [...] jako [...] Project Manager. [...]
aplikacji jest odpowiedzialny [...] za łącznik z filią firmy w Blois i La Rochelle we Francji w związku z
[...] pomieszczeń [...] CV [...] na samochodach okładowych Perkins France
[...] Emerytuje w Londynie na Krzyżownickim Krzyż [...] Starostwo [...], członkiem Kuratorium
[...] Harcerstwa [...] członkiem Naczelnej Rady AHP [...], członkiem Zarządu Zjednoczenia Polskiego w
[...] Brazylii [...], członkiem [...] Rady Koła Armii Krajowej, [...]
[...] Polskich [...] długoletnim skarbnikiem Polskiego
Ośrodka [...] Kulturalnej — POSK w Londynie.
[...] Brazylia i [...] domu Barbara [...] emigrantów osiedla się w Rio de Janeiro,
[...] drukarką [...] do pracy [...] 2 Dziennika Polskim w Londynie i
Nowym Dziennikiem w Nowym Jorku. Jest członkiem Stowarzyszenia Kronikarzy Prasy [...]
[...] w Brazylii [...] założył [...] Brazylijska Unia Sportu Żeglarz[y]. Jest
też członkiem Związku Pisarzy Polskich na Obczyźnie.

Odznaczenia: Krzyż Walecznych, Krzyż Armii Krajowej (No 3316), Medal Wojska, British War Medal
[...] Krzysztof Głuchowski [...] w następujących wydawnictwach i źródłach —
Powstanie Warszawskie: Adam Borkiewicz, Pax Warszawa 1957
Wiadomości POSK, London 1964-70
Dziesięciolecie Powstania 1954 Warszawa 1989
Ułani Lubelscy: Księga Dziejów 7 P.Uł.Lubelskich, Londyn 1969
[...] nad Tamizą, Opracował Józef Garliński POSK, Londyn 1989
[...], Anna Branicka-Wolska Iskry Warszawa 1990, (II wydanie Tenten Warszawa 1993)
[...] Królewska w Czasach Drugiej Rzeczypospolitej: Warszawa 1993
Dziennik Polski masowy 2.4.91, 18.4.91, 27.5.91, 25.8.92, 10.9.92. Londyn

Biblioteka Narodowa w Warszawie Zbiór Rękopisów No. 13853

Komplet listów Krzysztofa Głuchowskiego z Włoch, do ojca w Niemczech wraz z odwrotną korespondencją, złożone są w
dziale 2giej Wojny Światowej w Archiwum Polskiej Akademii Nauk przy Rynku Starego
Miasta w Warszawie

Przygotował Krzysztof Głuchowski
Rio de Janeiro, 18 października 1995""",
        "pieczecie": [],
        "podpisy": ["Krzysztof Głuchowski, Rio de Janeiro, 18.X.1995"],
        "osoby": [
            "Krzysztof Głuchowski (ps. Juraś, autor)",
            "Stanisław Stefan Głuchowski (ojciec)",
            "Wanda z Głuchowskich (matka)",
            "Gen. Władysław Anders",
            "Płk. dypl. Karol Ziemski (Wachnowski)",
            "Gen. Antoni Chruściel (Monter)",
            "Adam Borkiewicz (historyk)",
            "Józef Garliński",
            "Anna Branicka-Wolska",
            "Barbara (żona Krzysztofa)"
        ],
        "znaki_szczegolne": [
            "AUTOBIOGRAM — napisany przez samego Krzysztofa w 1995 roku!",
            "Rio de Janeiro, 18 października 1995",
            "PEŁNA CHRONOLOGIA ŻYCIA: szkoła → AK (1941) → Powstanie → obozy → Francja → Włochy → Anglia → Brazylia",
            "Krzyż AK Nr 3316 — numer potwierdzony",
            "Chartered Engineer — kwalifikacja inżynierska",
            "Project Engineer, Coordinator for East Europe and Spain",
            "Sales Engineering Manager, Project Manager",
            "Praca z Perkins France (silniki) w Blois i La Rochelle",
            "Żona: Barbara",
            "Osiedlił się w Rio de Janeiro",
            "Członek: POSK (skarbnik!), AHP, Koło AK, Związek Pisarzy Polskich na Obczyźnie",
            "Założył Brazylijską Unię Sportu Żeglarzy",
            "Dziennikarz: Dziennik Polski (Londyn), Nowy Dziennik (NY)",
            "Listy w Bibliotece Narodowej: Zbiór Rękopisów No. 13853",
            "Listy w Archiwum PAN przy Rynku Starego Miasta"
        ],
        "kontekst": "NAJWAŻNIEJSZY DOKUMENT BIOGRAFICZNY — autobiogram napisany przez samego Krzysztofa Głuchowskiego w Rio de Janeiro 18 października 1995 roku. Zawiera pełną chronologię życia: od Szkoły Rodziny Wojskowej (1939), przez ZWZ/AK (od VIII.1941), pluton 1112, 7 P.Uł. «Jeleń», Powstanie Warszawskie (Stare Miasto, Czerniaków), obozy jenieckie (Fallingbostel, Dorsten), repatriację przez Francję, służbę w 2 Korpusie we Włoszech, maturę w Anglii, dyplom Chartered Engineer, karierę inżynierską (Perkins France), emigrację do Brazylii (São Paulo → Rio). Aktywny w organizacjach: POSK (skarbnik), AHP, Koło AK, Związek Pisarzy na Obczyźnie. Żonaty z Barbarą. Listy archiwalne w Bibliotece Narodowej (nr 13853) i Archiwum PAN."
    },

    # ═══════════════════════════════════════════════════════════════
    # wa_biogram_stefan — Biogram ppor. Stefana (przygotowany przez Krzysztofa 1995)
    # ═══════════════════════════════════════════════════════════════
    "wa_biogram_stefan": {
        "typ": "Biogram",
        "data": "18.X.1995",
        "jezyk": "polski",
        "nadawca": "Krzysztof Głuchowski (autor biogramu)",
        "adresat": "publikacja / archiwum",
        "transkrypcja": """PPOR. STANISŁAW STEFAN GŁUCHOWSKI PSEUDONIM «STEFAN»

syn Mariana Głuchowskiego i Marii z Ziółkowskich. Ur. 1.5.1893 w Mąj Bukowo pow. Piotrków. [...]
[...] w gimnazjum [...] w Łodzi. Pracą [...] w sierpniu PPS a maturalnie [...]
[...] studenckim na wydziale [...] do 7 pułku [...] Piłsudskiego [...]
Warszawskim. W roku 1918 [...] na ochotnika zgłasza się do 7 P.Uł.[...] na front.
[...] 1919 od[komenderowany] [...] do [...] Podchorążych Piechoty.
Podchorążych uzyskawszy [...] na [...] oficerów [...] służb [...] I Pułk
Podchorążych Rezerwy Kawalerii [...] jako [...] rezerwowy przydzielony [...] do II [...]
[...] — [...] Kompanii [...] do [...] do 1933 [...]
[...] Piłsudskiego Rzeczpospolitej [...] do stanowiska [...] Kuźmewicza [...]
Kolekcja. W [...] 1939 [...] przydziały [...] do [...] mobilizowanej [...]
odrzucone powołania [...]. Warsztat [...] przybrał się do walczących [...] 1940
oddziałów. Po zakończeniu [...] [...] i powrócił do Warszawy. [...] między [...] 1940
[...] organizacji [...] Kompanii [...] K. [...] Nowamber 1943 zostaje
następnikiem w W.S.O.P. Warszawa-Żoliborz jako z-ca d-cy kompanii. 18.5.1944 aresztowany i więziony
na Pawiaku, przesłuchiwany na Alei Szucha. Zwolniony 29 lipca 1944.
Powstanie [...] na Śródmieście, [...] przydział [...] i dołącza [...] i [...] pracuje w
kwatermistrzostwie I Obwodu. Do kapitulacji idzie do niewoli przechodzi przez obozy 2 Fallingbostel,
Bergen, Gross-Born, Sandbostel i Lübeck. Po wyzwoleniu w Niemczech [...] 1947 [...] następnie
powraca do kraju. Zmarł 17.10.1962 w Warszawie. Pochowany na cmentarzu cywilnym na Powązkach
(Kwatera 95-V-19)

Odznaczenia: Krzyż Niepodległości, Order Polonia Restituta, Krzyż Walecznych, Złoty Krzyż Zasługi,
Srebrny Krzyż Zasługi, Krzyż Armii Krajowej (No. 3720)

Wzmianki o ppor. Stefanie Głuchowskim znajdują się w następujących wydawnictwach i źródłach –
- Ułani Lubelscy. Zeszyty wydawane od 1947 przez Koło 7 P.Uł.Lubelskich Londyn
- Komunikat Informacyjny Koła 7 P.Uł.Lubelskich No.38 I Londyn 1962
- Ułani Lubelscy: Księga Dziejów 7 P.Uł.Lubelskich I, Londyn 1969
- Listy niezwykłe, Anna Branicka-Wolska Iskry Warszawa 1990, (II wydanie Tenten Warszawa 1993)
- Zamek Królewski w Czasach Drugiej Rzeczypospolitej: Warszawa 1993
- Dziennik Polski masowy 2.4.91, 18.4.91, 27.5.91, 25.8.92, 10.9.92 Londyn
135 Pluton (AK...) Opracował Andrzej Drawkowski Warszawa 1994

Komplet listów ppor. Stefana Głuchowskiego z Niemiec do syna Krzysztofa znajdującego się w 7 P.Uł.Lubl.
i do [...] gen. Andersa we Włoszech, wraz z odwrotną korespondencją, złożone są w
dziale 2giej Wojny Światowej w Archiwum Polskiej Akademii Nauk przy Rynku Starego Miasta w
Warszawie
Biblioteka Narodowa w Warszawie Zbiór Rękopisów No. 13853

Przygotował Krzysztof Głuchowski
Rio de Janeiro, 18 października 1995""",
        "pieczecie": [],
        "podpisy": ["Krzysztof Głuchowski, Rio de Janeiro, 18.X.1995"],
        "osoby": [
            "ppor. Stanisław Stefan Głuchowski (ps. Stefan, ur. 1.V.1893)",
            "Marian Głuchowski (ojciec Stefana)",
            "Maria z Ziółkowskich (matka Stefana)",
            "Krzysztof Głuchowski (syn, autor biogramu)",
            "Gen. Władysław Anders"
        ],
        "znaki_szczegolne": [
            "Biogram napisany przez SYNA (Krzysztofa) w 1995 roku — źródło pierwszorzędne",
            "Stefan ur. 1.V.1893 w Mąj Bukowo pow. Piotrków (NIE 1893 Warszawa!)",
            "Pseudonim «Stefan» — prosty, od imienia",
            "Gimnazjum w Łodzi, członek PPS",
            "1918: ochotnik do 7 P.Uł. na front",
            "W.S.O.P. Warszawa-Żoliborz: z-ca d-cy kompanii (XI.1943)",
            "18.V.1944: ARESZTOWANY — Pawiak + przesłuchania na Alei Szucha!",
            "29.VII.1944: ZWOLNIONY — 3 dni przed Powstaniem!",
            "Powstanie: kwatermistrzostwo I Obwodu Śródmieście",
            "5 obozów: Fallingbostel, Bergen, Gross-Born, Sandbostel, Lübeck",
            "1947: powrót do Polski",
            "Zmarł 17.X.1962 w Warszawie",
            "Pochowany: Powązki, Kwatera 95-V-19",
            "Odznaczenia: Krzyż Niepodległości, Order Polonia Restituta, KW, Złoty KZ, Srebrny KZ, Krzyż AK (No. 3720)",
            "Bibliografia: 8 publikacji + archiwalia w BN i PAN"
        ],
        "kontekst": "Biogram ppor. Stefana Głuchowskiego przygotowany przez jego syna Krzysztofa w Rio de Janeiro (18.X.1995). KLUCZOWE NOWE FAKTY: Stefan urodził się w Mąj Bukowo pow. Piotrków (nie Warszawa). Był członkiem PPS. W 1943 został z-ca d-cy kompanii W.S.O.P. Warszawa-Żoliborz. 18.V.1944 aresztowany przez Gestapo — więziony na Pawiaku, przesłuchiwany na Alei Szucha (siedziba Gestapo). Zwolniony 29.VII.1944 — zaledwie 3 DNI przed wybuchem Powstania! W Powstaniu: kwatermistrz I Obwodu (Śródmieście). Po kapitulacji: 5 obozów jenieckich. 1947: powrót do Polski (nie emigracja). Zmarł 17.X.1962, pochowany na Powązkach (Kw. 95-V-19). Odznaczenia obejmują Krzyż Niepodległości i Order Polonia Restituta — najwyższe odznaczenia państwowe."
    },

    # ═══════════════════════════════════════════════════════════════
    # juras_033 — Notatki służbowe — rejestr dat i numerów (ARG/V/99)
    # ═══════════════════════════════════════════════════════════════
    "juras_033": {
        "typ": "Notatki służbowe — rejestr odznaczeń i rozkazów",
        "data": "1946",
        "jezyk": "polski",
        "nadawca": "Krzysztof Głuchowski (notatki własne)",
        "adresat": "dokumentacja osobista",
        "transkrypcja": """Głuchowski K.
[...] 14[?].45    149/46

Medal [Wojska?]
28 X 46    245/46

Odznaka 3DSK
12 XI 46    256/46

Bryt. [Medal?]    13 X 46    257/46
[...] 12/46
[...] 155/46

Medal [...] [?]
2.X.10.46    [...]/46

[...]
30 X [?]    [...] 263/[?]
[Med.] [...] [?]    [...]/46

[...]
6 [...] [?]

[Na dole:]
Klopotki [?]
Pożecznek [?]""",
        "pieczecie": [],
        "podpisy": [],
        "osoby": ["Krzysztof Głuchowski"],
        "znaki_szczegolne": [
            "Chronologiczny rejestr rozkazów i numerów akt",
            "Medal Wojska — 28 X 46, Rozkaz 245/46",
            "Odznaka 3DSK — 12 XI 46, Rozkaz 256/46",
            "Brytyjski Medal — 13 X 46, 257/46",
            "Numer 149/46, 155/46, 263/[?] — numery rozkazów dziennych",
            "Klopotki, Pożecznek — prawdopodobnie nazwiska świadków lub oficerów",
            "Pismo ołówkiem, trudno czytelne"
        ],
        "kontekst": "Notatki robocze Krzysztofa rejestrujące daty i numery rozkazów dotyczących jego odznaczeń i przebiegu służby. Stanowią uzupełnienie do notatek z ARG/V/113 (juras_047). Potwierdzone odznaczenia: Medal Wojska (28.X.46), Odznaka 3DSK (12.XI.46), medal brytyjski (13.X.46)."
    },

    # ═══════════════════════════════════════════════════════════════
    # juras_083 — List Krzysztofa z Myszkowa (ARG/V/149)
    # ═══════════════════════════════════════════════════════════════
    "juras_083": {
        "typ": "List / aerogram",
        "data": "14.VIII.1945",
        "jezyk": "polski",
        "nadawca": "Krzysztof Głuchowski (st.uł.)",
        "adresat": "nieustalony (rodzina?)",
        "transkrypcja": """st.Uł. Krzysztof Głuchowski
Polish Forces CMF 152
Gimnazjum 3 DSK

Myszków 14 VIII 45r.

[...] kochanej [...] posyłam
z [...] drodzy [...] Ostatnio [...]
tęsknię [...] [...]

W obecnej [chwili] pomagam [...] Pana Generała [zbierać?]
pluton 1112 [...] do [...] [...]
[...] [przy każdym?] pluton [...]
[...] do Generała [...] najcenniejszej
[...] Odnalazły [...] [...]
[...]
18 [...] list [...] Powstania [...]
[...] w wielkim szacunkiem [...]

[Na prawo — stempel:]
POLISH INSTITUTE AND SIKORSKI MUSEUM
[adres]

[Nr formularza:] 563""",
        "pieczecie": ["Stempel POLISH INSTITUTE AND SIKORSKI MUSEUM"],
        "podpisy": ["Krzysztof Głuchowski"],
        "osoby": ["Krzysztof Głuchowski", "Pan Generał (Janusz Głuchowski?)"],
        "znaki_szczegolne": [
            "Myszków 14.VIII.1945 — pisany z Myszkowa (miasto w woj. śląskim)",
            "Wspomina 'pluton 1112' — nr batalionu AK",
            "Wspomina 'Pana Generała' — prawdopodobnie stryj Janusz Głuchowski",
            "Stempel Instytutu Polskiego i Muzeum Sikorskiego w Londynie",
            "Aerogram nr 563 — ten sam format co list do Bora (ARG/V/148)",
            "Tekst trudno czytelny — wyblakły, niski kontrast"
        ],
        "kontekst": "List z Myszkowa (14.VIII.1945) — Myszków to miasto w woj. śląskim, przez które mogła przechodzić trasa repatriacyjna. Krzysztof wspomina pomaganie 'Panu Generałowi' (prawdopodobnie stryj Janusz) w zbieraniu informacji o plutonie 1112 z Powstania. Stempel Instytutu Polskiego i Muzeum Sikorskiego sugeruje, że list trafił do archiwum muzealnego."
    },

    # ═══════════════════════════════════════════════════════════════
    # juras_086 — Rękopis wspomnień — Piłsudski i 1918 (ARG/V/152)
    # ═══════════════════════════════════════════════════════════════
    "juras_086": {
        "typ": "Rękopis — wspomnienia historyczne",
        "data": "ok. 1960–1970",
        "jezyk": "polski",
        "nadawca": "Krzysztof Głuchowski (?)",
        "adresat": "notatki własne / wspomnienia",
        "transkrypcja": """                                        1
                    gen. Głuch.

Pragnę przedstawić pokrótce Karierę
stryja St. Marszałka ze szczególnym naciskiem
Służby w Kawalerii. Stryjo[?] Marszałka i przedsta-
wić [tu?] dzieje jak oficer. Pragnę poznać karierę [?]
naszej Matki[?], jak bardzo szybko sam sobie [kasę?]-
rię prowadzić de Ko[?].
Było ze tego powody.

Pamiętam powodów jest kilka, ze od wielu lat
angażował świadomości w mieście i w wszystko
Co lat Marszałka — lat Piłsud[skiego], dawno właściwie
prawo.

„Bitwa [Cóże?]" „Orzysz" to jest raczej dość
znane, a było to [wiąże?] bardziej czę i ciężko obej-
muje i główną [?] ku manewrowi, nasze zwycięskie
marsze.

Ciągle powodów jest kilka, i [Morowie?] podwody
od różnego wydarzenia w dzień rewolucyjnym do
dnia koniec[?] wiernie i 1918 roku, nasze podst[awy?] [polit?]-""",
        "pieczecie": [],
        "podpisy": [],
        "osoby": ["Marszałek (Józef Piłsudski)", "Stefan Głuchowski (?)"],
        "znaki_szczegolne": [
            "Nagłówek: 'gen. Głuch.' — wspomnienia o karierze Gen. Janusza Głuchowskiego",
            "'Pragnę przedstawić pokrótce Karierę stryja' — Krzysztof pisze o STRYJU (nie ojcu!)",
            "Nacisk na służbę w Kawalerii i związek z Marszałkiem Piłsudskim",
            "Wspomina Bitwę pod Orzyszem (1914/1920?) — manewry kawaleryjskie",
            "Odniesienie do 1918 roku — odzyskanie niepodległości",
            "Pismo odręczne atramentem na kremowym papierze, wyblakłe",
            "Strona numerowana '1' — istniała dalsza część"
        ],
        "kontekst": "Rękopis wspomnień Krzysztofa o karierze stryja — gen. Janusza Głuchowskiego. Krzysztof podkreśla kawaleryjski charakter służby stryja i jego związki z Marszałkiem Piłsudskim. Wspomina 'Bitwę pod Orzyszem' i wydarzenia 1918 roku. WAŻNE: Krzysztof nazywa Janusza 'stryjem' — potwierdza, że jest synem STEFANA (brata Janusza). Nagłówek 'gen. Głuch.' i numeracja '1' sugerują, że to początek dłuższego tekstu o historii rodziny."
    },

    # ═══════════════════════════════════════════════════════════════
    # juras_069 — Karta pozdrowień z SPP Londyn (ARG/V/135)
    # ═══════════════════════════════════════════════════════════════
    "juras_069": {
        "typ": "Karta pozdrowień / życzenia",
        "data": "ok. 1960–1970",
        "jezyk": "polski / angielski",
        "nadawca": "Pracownicy SPP w Londynie",
        "adresat": "Krzysztof Głuchowski",
        "transkrypcja": """Szanowny i Drogi Krzysztofie!

Pozdrowienia z Londynu
od Pracowników Koleżanek
i [Kolegów?]
z SPP

A w zastępstwie nasz
mamy Biuletyn nr 10

[podpis] Zofija [?]
Pracownik [?] pozdrowieniami
[...] SPP [...]
Elżbieta [?]
[...] Bogusław [?]

[Na dole, innym pismem:]
Best wishes
[?] najlepsze życzenia z Londynu, [...]
Rozkel z [?] K[?]
i najlepszych Bracie[m]

Krzysztofie! [?] [?]
[...] Irene [?]""",
        "pieczecie": [],
        "podpisy": ["Zofija", "Elżbieta", "Bogusław", "Irene", "i inni"],
        "osoby": ["Krzysztof Głuchowski", "Zofija", "Elżbieta", "Bogusław", "Irene"],
        "znaki_szczegolne": [
            "SPP — Stowarzyszenie Polskich Kombatantów (?)  lub Skarb Polskich Pracowników",
            "Biuletyn nr 10 — wspomniany jako zastępstwo za wizytę",
            "Wiele podpisów — koleżanki i koledzy z SPP",
            "Dwujęzyczna — 'Best wishes' po angielsku",
            "Pismo niebieskim atramentem na szarym papierze"
        ],
        "kontekst": "Karta pozdrowień od współpracowników z SPP (Stowarzyszenie Polskich Kombatantów?) w Londynie do Krzysztofa, prawdopodobnie w Brazylii. Wspomina Biuletyn nr 10 — periodyk organizacji. Wielokrotne podpisy — Krzysztof utrzymywał kontakty z polską emigracją londyńską."
    },

    # ═══════════════════════════════════════════════════════════════
    # juras_078 — Zaświadczenie Ziemskiego o KW — wariant (ARG/V/144)
    # ═══════════════════════════════════════════════════════════════
    "juras_078": {
        "typ": "Zaświadczenie wojskowe — Krzyż Walecznych",
        "data": "26.X.1946",
        "jezyk": "polski",
        "nadawca": "Płk. dypl. Karol Ziemski (ps. Wachnowski)",
        "adresat": "poświadczenie służby Krzysztofa Głuchowskiego",
        "transkrypcja": """ZIEMSKI KAROL
PUŁKOWNIK DYPLOMOWANY
DOWÓDCA POLSKIEGO OKRĘGU [WOJSKOWEGO]
[...] SCHLESWIG-HOLSTEIN

Wentorf [pod Hamburgiem]
[...]

ZAŚWIADCZENIE

Jako b. Dowódca Grupy «PÓŁNOC» w Powstaniu Warszaw-
skim (Obrona Starego Miasta) [stwierdzam, że] [...]
Krzysztof, ur. [...] w Warszawie, pseudonim [...]
walczący w Obronie Starego Miasta [w Plutonie III]

[awansowany do stopnia]

starszego strzelca

oraz odznaczony

KRZYŻEM WALECZNYCH po raz pierwszy

co zostało stwierdzone w moim Rozkazie — Dowódcy Grupy
«PÓŁNOC» Nr. 24 z dnia 5.9.1944 —

B. DOWÓDCA OBRONY STAREGO MIASTA

[podpis]

ZIEMSKI KAROL
PUŁKOWNIK DYPLOMOWANY

[pieczęć okrągła na dole]""",
        "pieczecie": ["Pieczęć okrągła Polskiego Okręgu Wojskowego"],
        "podpisy": ["Ziemski Karol, Pułkownik Dyplomowany"],
        "osoby": ["Krzysztof Głuchowski", "Płk. dypl. Karol Ziemski (ps. Wachnowski)"],
        "znaki_szczegolne": [
            "Duplikat/wariant zaświadczenia ARG/V/43 (Seria_29z_p36)",
            "Ten sam tekst i podpis — inna kopia dokumentu",
            "Pieczęć okrągła na dole — uwierzytelnienie",
            "Dokument pożółkły, lekko uszkodzony"
        ],
        "kontekst": "Wariant/duplikat zaświadczenia płk. Ziemskiego (por. ARG/V/43). Krzysztof posiadał dwie kopie tego kluczowego dokumentu — potwierdzenie udziału w obronie Starego Miasta, pseudonim Juraś, awans na st. strzelca i Krzyż Walecznych."
    },

    # ═══════════════════════════════════════════════════════════════
    # juras_082 — Aerogram do gen. Bora-Komorowskiego (ARG/V/148)
    # ═══════════════════════════════════════════════════════════════
    "juras_082": {
        "typ": "Aerogram (Air Letter)",
        "data": "ok. 1946–1948",
        "jezyk": "polski",
        "nadawca": "Krzysztof Głuchowski (?)",
        "adresat": "Generał de dywizji Tadeusz Bor Komorowski, H.Q. Polish Forces 25, ENGLAND",
        "transkrypcja": """BY AIR MAIL
AIR LETTER

563

[Stempele pocztowe — dwa okrągłe]

Generał de dywizji
Tadeusz Bor Komorowski
H.Q. Polish Forces 25
ENGLAND

Written in Polish.

[Odwrotna strona — treść listu nieczytelna na zdjęciu]""",
        "pieczecie": ["Stempele pocztowe (dwa okrągłe, częściowo czytelne)"],
        "podpisy": [],
        "osoby": ["Krzysztof Głuchowski (nadawca?)", "Gen. dyw. Tadeusz Bór-Komorowski (adresat)"],
        "znaki_szczegolne": [
            "ADRESAT: Generał de dywizji Tadeusz Bor Komorowski!",
            "H.Q. Polish Forces 25 — Kwatera Główna Polskich Sił Zbrojnych",
            "Nr 563 — numer formularza aerogramu",
            "Dopisek 'Written in Polish' — cenzura pocztowa",
            "Treść na odwrocie nieczytelna na zdjęciu",
            "Stempele pocztowe wymagają odrębnej analizy"
        ],
        "kontekst": "Aerogram zaadresowany do gen. dyw. Tadeusza Bora-Komorowskiego — Dowódcy Armii Krajowej i Powstania Warszawskiego! Bór-Komorowski po wojnie przebywał w Londynie jako Naczelny Wódz PSZ (1946–1947). H.Q. Polish Forces 25 — kwatera główna. Ten sam Bór-Komorowski, który ustanowił Krzyż AK (1966), którym odznaczono Krzysztofa. Dokument pokazuje bezpośredni kontakt młodego powstańca z najwyższym dowódcą."
    },

    # ═══════════════════════════════════════════════════════════════
    # juras_062 — PASS z 7 Pułku Ułanów Lubelskich (ARG/V/128)
    # ═══════════════════════════════════════════════════════════════
    "juras_062": {
        "typ": "Przepustka wojskowa — Army Form B.295",
        "data": "9.IX.1947",
        "jezyk": "angielski",
        "nadawca": "7 Pułk Ułanów Lubelskich / Commanding Officer",
        "adresat": "Głuchowski Krzysztof",
        "transkrypcja": """PASS
Army Form B.295

[Pieczęć okrągła:] 7 PUŁK UŁANÓW LUBELSKICH

Regt. [?] Bower Ward Camp
No. 3004271    Rank: L/Cpl
Name: GLUCHOWSKI Krzysztof
has permission to absent from his unit
from 9.9.47

[podpis] Commanding [Officer]

1. From London District
2. To London
3. Through London

7. Ration Card Issued
8. For use of C.M.P.
9. Valid only with A.B.64""",
        "pieczecie": ["7 PUŁK UŁANÓW LUBELSKICH (pieczęć okrągła niebieska)"],
        "podpisy": ["Commanding Officer"],
        "osoby": ["Krzysztof Głuchowski (L/Cpl, No. 3004271)"],
        "znaki_szczegolne": [
            "Nr 3004271 — ten sam numer co w certyfikacie PRC",
            "Stopień: L/Cpl (Lance Corporal = starszy ułan)",
            "Pieczęć 7 PUŁKU UŁANÓW LUBELSKICH — pułk rodzinny",
            "Data: 9.9.47 — przepustka do Londynu",
            "Bower Ward Camp — obóz wojskowy",
            "Valid only with A.B.64 — ważna tylko z książeczką wojskową"
        ],
        "kontekst": "Przepustka z 7 Pułku Ułanów Lubelskich zezwalająca L/Cpl Głuchowskiemu na wyjazd do Londynu z Bower Ward Camp (9.IX.1947). Pieczęć z polską nazwą pułku na brytyjskim formularzu — symbol polskiej tożsamości w ramach struktur brytyjskich."
    },

    # ═══════════════════════════════════════════════════════════════
    # juras_064 — ALIEN IDENTITY CERTIFICATE (ARG/V/130)
    # ═══════════════════════════════════════════════════════════════
    "juras_064": {
        "typ": "Certyfikat tożsamości cudzoziemca",
        "data": "31.X.1947",
        "jezyk": "angielski",
        "nadawca": "Polish Resettlement Corps / Ministry of Labour",
        "adresat": "Głuchowski Krzysztof",
        "transkrypcja": """ALIEN IDENTITY CERTIFICATE
Army Form E.D.A. [?]

POLISH RESETTLEMENT CORPS [...]
MINISTRY OF LABOUR [...]

Surname: GLUCHOWSKI
[Christian Names: Krzysztof]
Rank: L.CPL.
Date of Birth: 29.11.1926
[...]

SOUTH WEST ESSEX TECHNICAL COLLEGE
AND SCHOOL OF
[...] STREET ROAD
ERITH / PARK ROAD

Occupation: STUDENT

[...] 31.10.[47]

[Pieczęć:] No. 3 RELEGATION
EASTERN COMMAND
P.R.C.

[podpisy]""",
        "pieczecie": ["No. 3 RELEGATION, EASTERN COMMAND, P.R.C."],
        "podpisy": ["Officer Commanding", "Record Officer"],
        "osoby": ["Krzysztof Głuchowski (L.CPL, student)"],
        "znaki_szczegolne": [
            "STUDENT at South West Essex Technical College",
            "Adres: Erith / Park Road — w hrabstwie Kent",
            "Stopień: L.CPL (Lance Corporal)",
            "Data urodzenia: 29.11.1926 — potwierdzona",
            "No. 3 Relegation, Eastern Command, P.R.C. — pieczęć jednostki",
            "Dokument duży, pożółkły, z wieloma wpisami odręcznymi"
        ],
        "kontekst": "Certyfikat tożsamości cudzoziemca wydany Głuchowskiemu jako żołnierzowi PRC skierowanemu na studia. South West Essex Technical College w Erith (Kent) — szkoła techniczna, gdzie Krzysztof studiował po demobilizacji. Erith leży na południowo-wschodnim obrzeżu Londynu. Studenci-żołnierze PRC mogli kontynuować naukę w ramach programu resettlement."
    },

    # ═══════════════════════════════════════════════════════════════
    # juras_067 — Pełna karta służby (ARG/V/133)
    # KLUCZOWY DOKUMENT — WSZYSTKIE DANE PERSONALNE
    # ═══════════════════════════════════════════════════════════════
    "juras_067": {
        "typ": "Karta służby — Polish All-British Record Centre",
        "data": "ok. 1949",
        "jezyk": "angielski",
        "nadawca": "All-British Record Centre (Polish), Bayrs Barracks, Middlesex",
        "adresat": "zapytanie o dane służbowe",
        "transkrypcja": """THE ALL-BRITISH RECORD CENTRE (POLISH)
BAYRS BARRACKS
[...] MIDDLESEX

Ref. No. 34477 (R.O.R.C.)

CONFIDENTIAL

[...] the following are the particulars of the
above named:

Army No.: 3004271
Date of Birth: 29th November 1926
Born in: [Warsaw?]
Marital Status: Single
Religion: Roman Catholic
Parents: Stefan and Wanda
Civilian Occupation (prior to army service): Student

Service: with the Polish Forces under British Command —
    From 14th July 1945 (Italy)
    [...] the Polish (Resettlement) Corps on [1.11.1946?]
    Discharged: 31.10.[1948]

Polish [Decorations]:
    Polish Medal [...] 5.11.1947
    [...]

Medals and Awards:
    War Medal 1939/45

Conduct: Very Good.

[pieczęć:] POLISH ALL-BRITISH RECORD CENTRE
[...] MIDDLESEX

[podpis]
P.O.R.B. 35
[...] LONDON W.5.""",
        "pieczecie": ["POLISH ALL-BRITISH RECORD CENTRE, Middlesex"],
        "podpisy": ["Officer, P.O.R.B. 35"],
        "osoby": ["Krzysztof Głuchowski", "Stefan Głuchowski (ojciec)", "Wanda Głuchowska (matka)"],
        "znaki_szczegolne": [
            "KLUCZOWY DOKUMENT — pełna karta służby z WSZYSTKIMI danymi personalnymi",
            "Army No.: 3004271",
            "Ur. 29 listopada 1926",
            "Stan cywilny: Single (kawaler)",
            "Wyznanie: Roman Catholic",
            "Rodzice: STEFAN i WANDA — oficjalne potwierdzenie",
            "Zawód cywilny: Student",
            "Służba: od 14 lipca 1945 (Włochy) do 31.10.1948",
            "Medal: War Medal 1939/45",
            "Conduct: Very Good",
            "CONFIDENTIAL — dokument poufny",
            "Bayrs Barracks, Middlesex — centralne archiwum wojskowe polskie w UK"
        ],
        "kontekst": "Pełna karta służby z centralnego archiwum polskiego w Wielkiej Brytanii (All-British Record Centre w Bayrs Barracks, Middlesex). POTWIERDZA DEFINITYWNIE: rodzice Stefan i Wanda, ur. 29.XI.1926, kawaler, rzymski katolik, student, służba od 14.VII.1945 (Włochy) przez PRC do zwolnienia 31.X.1948. War Medal 1939/45. Conduct: Very Good. Dokument poufny (CONFIDENTIAL) — odpowiedź na zapytanie urzędowe o dane służbowe."
    },

    # ═══════════════════════════════════════════════════════════════
    # juras_059 — Esej szkolny nr 1: "Moja najciekawsza przygoda" (ARG/V/59, Seria_29z_p32_img01)
    # RELACJA Z PIERWSZEJ RĘKI Z POWSTANIA WARSZAWSKIEGO
    # ═══════════════════════════════════════════════════════════════
    "juras_059": {
        "typ": "Esej szkolny — relacja osobista z Powstania Warszawskiego",
        "data": "23.VIII.1945",
        "jezyk": "polski",
        "nadawca": "Krzysztof Andrzej Głuchowski (uczeń Gimnazjum 3 DSK)",
        "adresat": "Nauczyciel języka polskiego, Gimnazjum 3 DSK",
        "transkrypcja": """Zadanie Klasowe No 1                    23 VIII 45r.

Tematy:
1) Tragiczne widmo: fenho (fenho Montyken[?])
2) Klawisze (kości i zagadki)
3) Moja najciekawsza przygoda.

[Uczeń wybrał temat 3]

3. Gdy myślę to moich przygodach, biorę poważnie te. W każd-
ej[?] razie było to jedną z moich większych przygód. Potem miałem, muszę
uczciwie dodać, ale ja jednak nie upadła na mnie takiego wra-
żenia.

Było to dnia 1 Sierpnia 1944 roku — w Warszawie. Armia Kra-
jowa przygotowywała się na koncentrację. Patrzejąc placówki i daw-
niej bawiliśmy się w nasz[e] przesłać czujnością.

Nasz pluton miał numer 1112. Był osiem[?]/jedenastu[?] jeden-
nastu uzbrojonych żołnierzy[?]. „Falk"[?]: PP. kilku [w] bluzie mundurach.

Umieszczenie naszego plutonu przeniesiono wreszcie w fabrykę
mebli, tyi[?] ul. Belwed[erska?]/Piękna, o godzinie 15:00.

Około godziny 16:30 po otrzymaniu rozkazu — aparat[?] na Bole[sław?]
Śl[?] do broni chodziliśmy — chodziliśmy cały łanem szturmowym[?]
[mieliśmy?] tej fabrykę; ogień fabryki [?] budynki były w otoczeniu[?]
naszego obsuchy[?]. Spr. oficer Jerzego Konieczn[y] (Warzon.?), rozejdawali
się. Podtem kontowaliśmy[?], forma „Odkowan[ie?]": forma — Srodolski[?].

Było nas dwudziestu osiem. Uzbrojenie: jako na warunki AK —
średnie i dobre. Składało się z 2 dwóch R.K.M., osiem[?] jedenastu sztuk,
z nich karabinów w strzela podschodząc. Amunicji do potrzebności prawie nie
było. Rozkaz komunikować — nam było, żebyś[my] na Belweder[?] (granaty
podejśli[?]).

Ja nadstawiałem się w boju strzeleckim[?] podaniem[?], w jedne[?]...""",
        "pieczecie": [],
        "podpisy": [],
        "osoby": ["Krzysztof Głuchowski", "Spr. Jerzy Konieczny (oficer)"],
        "znaki_szczegolne": [
            "BEZCENNA RELACJA Z PIERWSZEJ RĘKI — 19-letni powstaniec pisze o 1.VIII.1944",
            "Zadanie klasowe w Gimnazjum 3 DSK we Włoszech, rok po Powstaniu",
            "EXERCISE BOOK — okładka: 'Gimnazjum 3 DSK, St.uł. Głuchowski Krzysztof, Zadania Klasowe z języka polskiego'",
            "Pluton nr 1112 — potwierdzony w innych dokumentach",
            "28 żołnierzy, uzbrojenie: 2 R.K.M. (ręczne karabiny maszynowe), kilkanaście karabinów",
            "Amunicji 'do potrzebności prawie nie było'",
            "Fabryka mebli przy ul. Belwederskiej/Pięknej — punkt zborny",
            "Godzina 15:00 — koncentracja, 16:30 — otrzymanie rozkazu do walki",
            "Spr. oficer Jerzy Konieczny — dowódca na miejscu",
            "Forma 'Odkowań' — forma 'Srodolski' — nazwy kompanii/ugrupowań?",
            "Skan z Seria_29z_p32_img01 (Exercise Book)"
        ],
        "kontekst": "Esej szkolny napisany 23 sierpnia 1945 — dokładnie rok i 23 dni po wybuchu Powstania. Krzysztof, wówczas 19-letni uczeń Gimnazjum 3 DSK we Włoszech, wybrał temat 'Moja najciekawsza przygoda' i opisał swoje przeżycia z 1 sierpnia 1944. Relacja z pierwszej ręki: placówka 1112, 28 żołnierzy, 8 petard szkolnych, zbiórka o 15:00, fabryka mebli jako punkt wyjścia. Dokument o wyjątkowej wartości historycznej — bezpośrednie świadectwo nastolatka-powstańca."
    },

    # ═══════════════════════════════════════════════════════════════
    # juras_060_esej — Esej na rocznicę Powstania (ARG/V/60, Seria_29z_p33)
    # REFLEKSJA W PIERWSZĄ ROCZNICĘ — DOKŁADNIE O GODZ. 15:55
    # ═══════════════════════════════════════════════════════════════
    "juras_060_esej": {
        "typ": "Esej szkolny — refleksja na rocznicę Powstania Warszawskiego",
        "data": "1.VIII.1945",
        "jezyk": "polski",
        "nadawca": "Krzysztof Andrzej Głuchowski",
        "adresat": "Nauczyciel języka polskiego, Gimnazjum 3 DSK",
        "transkrypcja": """St. uł. Krzysztof Głuchowski        Mp. [...] VIII 1945r.
Polish Forces C.M.F. 152             godz. 15.55
Gimnazjum

Rok temu już od piętnastu minut walczyliśmy
z [...] jako Żołnierze ale [miasto] [...] z [...]
[...] do walki [...] starsze i straszniejsze [...]

Powstanie do którego byliśmy osobno wszyscy i moralnie
przygotowani udało się. Dawno to miało [swój] koniec [...]
gdy Warszawa [...] zginęło 3.000.000 ludzi.

A jednak ja sobie mówię i mówię, o Powstanie [...]
Nie [...] to nie tylko Warszawa, do któr[ej] [...]
Polskie [...] walczyły. [...]
[...] tego cel: [Wpadnie?] Warszawa, [...]
[...] walki Niemca [ujęły?] [...]

[...] Czerniaków. Armia [...] wolna.
Pozostaje tylko [...] [...]
[...] na Czerniakow. Armia. Niestety [pozostali]: [...]
[...] Miany [myśleli?] o Bolszewiku
[...]. [Ale] [...]  dwóch [...]
[...] Warszawa walczyło 63 [...]. I [dzisiaj] [...]
[...] walczymy [...] walki [...]

[...] W Powstani[u] [...] w Warszawie...
Czerwony [...] piękności o bohater[ach] walecznych powstańców
[...]

Wśród powstańców duch był: ludzie widzieli tylko [walczące] isto-
ty[?] z olbrzymim powstańczym duchem.

K.""",
        "pieczecie": [],
        "podpisy": ["K. (Krzysztof Głuchowski)"],
        "osoby": ["Krzysztof Głuchowski"],
        "znaki_szczegolne": [
            "NAPISANY DOKŁADNIE W ROCZNICĘ — 1.VIII.1945 godz. 15:55",
            "Godzina 15:55 = minutę przed godziną W (16:00 wg planu, 17:00 faktycznie)",
            "Wspomina 3.000.000 ofiar — zawyżona liczba, ale oddaje traumę",
            "Czerniaków, Armia — wspomina kluczowe punkty walk",
            "Odniesienie do Bolszewików — krytyka braku pomocy sowieckiej",
            "63 [dni?] walki Warszawy",
            "Końcowe zdanie o 'olbrzymim powstańczym duchu'",
            "Nagłówek: Polish Forces C.M.F. 152 (Central Mediterranean Forces)"
        ],
        "kontekst": "Esej napisany 1 sierpnia 1945 o godz. 15:55 — dokładnie w pierwszą rocznicę Powstania Warszawskiego, minutę przed godziną W. Krzysztof, 19-letni uczeń Gimnazjum 3 DSK we Włoszech, pisze emocjonalną refleksję o walce, stratach i duchu powstańczym. Wspomina Czerniaków, krytykuje brak pomocy sowieckiej ('Bolszewik'), podaje (zawyżoną) liczbę ofiar. Kończy słowami o 'olbrzymim powstańczym duchu' — zdanie, które definiuje jego pokolenie."
    },

    # ═══════════════════════════════════════════════════════════════
    # juras_061 — Esej "Lektura" o artykułach o Powstaniu (ARG/V/61, Seria_29z_p34)
    # ═══════════════════════════════════════════════════════════════
    "juras_061": {
        "typ": "Esej szkolny — analiza artykułów o Powstaniu Warszawskim",
        "data": "3.VIII.1945",
        "jezyk": "polski",
        "nadawca": "Krzysztof Andrzej Głuchowski",
        "adresat": "Nauczyciel języka polskiego, Gimnazjum 3 DSK",
        "transkrypcja": """St.uł. Krzysztof Głuchowski         Mp. 3 VIII '45r.
Polish Forces CMF 152
Gimnazjum 3DSK.

Lektura.

Czytam artykuły różnych ludzi o Powsta-
niu Warszawskim. Porównuję je bo artykuły ludzi, którzy
nie brali w nim udziału. Wyjść ci nie rozumieją istoty
rzeczy w Warszawie. Wydaje się mówić o bohaterstwie py-
taniu[?] ludzi w Warszawie, znaleźć o pracy, o organizacji. A poco[?]
jest to dużo ważniejsze. W Warszawie wspaniale wal-
czyła Armia, Armia która posiadała swoją organizację
i dobre społeczne[?]. To nie byli, ci sobie prostacze[?], któ-
ry spontanicznie chcący do walce — to był żołnierz,
który w ciężkich warunkach okupacji i nieustająco przygoto-
wał się, mozolną pracę podzieloną do Powstania.
Warszawskiej Armii brakowało tylko sprzętu[?] — odpo-
wiadalny[ch] na[?] pod każdym względem. — Z kompasem[?].

Czytając jeden z artykułów p. Nowakowskiego —
spotkać się ze słowami „Głuchowscy wszyscy
pośli do Powstania i [walki] o kraj". Widocznie pan
Nowakowski nie pisał to[?]. Pan Głuchowski[?] wielka
praca konspiracyjna; że właśnie Głuchowscy byli
jednym[i] z żołnierzy Armii Krajowej. Plutonem, który
miał swoje wyznaczone zadania w planie opanowa-
nia Warszawy.

W Warszawie, trochę dmusze[?] na szalkę na dorobek
detali — obroty[?] wykonała wielka, największą[?] była praca
organizacyjna: obronna a ludna — jej też Polacy. —

K.""",
        "pieczecie": [],
        "podpisy": ["K. (Krzysztof Głuchowski)"],
        "osoby": ["Krzysztof Głuchowski", "p. Nowakowski (autor artykułów)", "rodzina Głuchowskich"],
        "znaki_szczegolne": [
            "Esej krytyczny — powstaniec polemizuje z publicystami, którzy nie walczyli",
            "GŁUCHOWSCY WYMIENIENI Z NAZWISKA — Nowakowski pisał o nich: 'Głuchowscy wszyscy pośli do Powstania'",
            "Krzysztof odpowiada: Głuchowscy nie byli spontanicznymi ochotnikami — byli żołnierzami AK",
            "'To nie byli ci sobie prostacze, którzy spontanicznie chcący do walce — to był żołnierz'",
            "'Plutonem, który miał swoje wyznaczone zadania w planie opanowania Warszawy'",
            "'W ciężkich warunkach okupacji nieustająco przygotowywał się, mozolną pracę podzieloną'",
            "Nagłówek: Polish Forces CMF 152, Gimnazjum 3DSK",
            "Skan z Seria_29z_p34_img01 (Exercise Book)"
        ],
        "kontekst": "Esej analityczny napisany 3 sierpnia 1945. 19-letni Krzysztof czyta artykuły o Powstaniu i polemizuje z autorami, którzy nie brali w nim udziału. KLUCZOWE ODKRYCIE: cytuje p. Nowakowskiego, który WYMIENIŁ GŁUCHOWSKICH Z NAZWISKA — 'Głuchowscy wszyscy pośli do Powstania i walki o kraj'. Krzysztof broni honoru rodziny: Głuchowscy nie byli spontanicznymi ochotnikami, ale żołnierzami AK z wyznaczonymi zadaniami w planie opanowania Warszawy. Podkreśla profesjonalizm: 'to nie byli ci sobie prostacze — to był żołnierz, który w ciężkich warunkach okupacji nieustająco przygotowywał się'. Fascynujący dokument — głos 19-latka, który SAM walczył, wobec publicystów, którzy PISALI o walce."
    },

    # ═══════════════════════════════════════════════════════════════
    # juras_043_ziemski — Zaświadczenie płk. Ziemskiego (ARG/V/43, Seria_29z_p36)
    # ═══════════════════════════════════════════════════════════════
    "juras_043_ziemski": {
        "typ": "Zaświadczenie wojskowe",
        "data": "26.X.1946",
        "jezyk": "polski",
        "nadawca": "Płk. dypl. Karol Ziemski (ps. Wachnowski)",
        "adresat": "dokument poświadczający służbę Krzysztofa Głuchowskiego",
        "transkrypcja": """ZIEMSKI KAROL
PUŁKOWNIK DYPLOMOWANY

DOWÓDCA POLSKIEGO OKRĘGU
WOJSKOWEGO NA TERENIE
SCHLESWIG - HOLSTEIN

Wentorf pod Hamburgiem
Dnia 26.10.1946 R.

ZAŚWIADCZENIE

Jako b. Dowódca Grupy «PÓŁNOC» w Powstaniu Warszaw-
skim (Obrona Starego Miasta) stwierdzam, że GŁUCHOWSKI
Krzysztof, ur. w dniu 29.11.1928 r. w Warszawie, pseudonim
«Juraś», walczący w Obronie Starego Miasta w Plutonie III

Na okazaną waleczność został awansowany do stopnia

starszego strzelca

oraz odznaczony

KRZYŻEM WALECZNYCH po raz pierwszy,

co zostało stwierdzone w moim Rozkazie — Dowódcy Grupy
«PÓŁNOC» Nr. 24 z dnia 5.9.1944 r.

B. DOWÓDCA OBRONY STAREGO MIASTA
W POWSTANIU WARSZAWSKIM

[podpis]

ZIEMSKI KAROL
(WACHNOWSKI)
PUŁKOWNIK DYPLOMOWANY""",
        "pieczecie": [],
        "podpisy": ["Ziemski Karol (Wachnowski), Pułkownik Dyplomowany"],
        "osoby": ["Krzysztof Głuchowski (ps. Juraś)", "Płk. dypl. Karol Ziemski (ps. Wachnowski)"],
        "znaki_szczegolne": [
            "KLUCZOWY DOKUMENT — zaświadczenie od dowódcy obrony Starego Miasta",
            "Pseudonim «Juraś» — potwierdzone oficjalnie",
            "Grupa «PÓŁNOC» — oddział obrony Starego Miasta w Powstaniu",
            "Rozkaz Nr 24 z 5.IX.1944 — nadanie KW i awansu",
            "Data urodzenia 29.11.1928 — BŁĄD w dokumencie (prawidłowa: 29.XI.1926)",
            "Papier firmowy Polskiego Okręgu Wojskowego Schleswig-Holstein",
            "Wentorf pod Hamburgiem — siedziba dowództwa"
        ],
        "kontekst": "Zaświadczenie od płk. dypl. Karola Ziemskiego (ps. Wachnowski) — dowódcy Grupy 'Północ' i obrony Starego Miasta w Powstaniu Warszawskim. Potwierdza udział Krzysztofa w Plutonie III obrony Starego Miasta, pseudonim 'Juraś', awans na st. strzelca i odznaczenie Krzyżem Walecznych (Rozkaz Nr 24 z 5.IX.1944). Ziemski po wojnie dowodził Polskim Okręgiem Wojskowym w Schleswig-Holstein."
    },

    # ═══════════════════════════════════════════════════════════════
    # lbr_II_54 — Dedykacja gen. Andersa na albumie
    # ═══════════════════════════════════════════════════════════════
    "lbr_II_54": {
        "typ": "dedykacja",
        "data": "31.III.1945",
        "jezyk": "pl",
        "nadawca": "Gen. Władysław Anders",
        "adresat": "Gen. Janusz Głuchowski",
        "transkrypcja": "Gł. J. Głuchowskiemu z wyrazami przyjaźni\nw hołdzie naszym żołnierzom do Polski\nW. Anders\n31.3.45",
        "pieczecie": [],
        "podpisy": ["W. Anders"],
        "osoby": ["Władysław Anders", "Janusz Głuchowski"],
        "znaki_szczegolne": "Dedykacja odręczna na stronie tytułowej albumu 'Żołnierz z Montecassino'. Atrament czarny, pismo kaligraficzne.",
        "kontekst": "Osobista dedykacja gen. Andersa — dowódcy 2. Korpusu Polskiego i zwycięzcy spod Monte Cassino — dla gen. Głuchowskiego, Dowódcy JWWB. Datowana 31 marca 1945, gdy Anders był jeszcze we Włoszech. Dokument przyjaźni dwóch najwyższych generałów polskiej emigracji."
    },

    # ═══════════════════════════════════════════════════════════════
    # wa_krzyz_ak — Legitymacja Krzyża Armii Krajowej (Krzysztof)
    # ═══════════════════════════════════════════════════════════════
    "wa_krzyz_ak": {
        "typ": "Legitymacja odznaczenia wojskowego",
        "data": "7.3.1968",
        "jezyk": "polski",
        "nadawca": "K. Ziemski «Wachnowski», Z-ca D-cy W-skiego Korpusu A.K.",
        "adresat": "Krzysztof Głuchowski ps. «Juras»",
        "transkrypcja": """Nazwisko  GŁUCHOWSKI
Imię  Krzysztof
Pseudonim  „JURAS"
Przydział  Z.W.Z. KOMP. K. PLUT. III2
7 PUŁK UŁAN. LUBEL. „JELEŃ"

Odznaczony został
KRZYŻEM ARMII KRAJOWEJ
ustanowionym dnia 1 sierpnia 1966 roku
przez dowódcę A.K. gen. Tadeusza Bora-
Komorowskiego dla upamiętnienia wysiłku
żołnierza Polski Podziemnej w latach
1939 — 1945.

Podpis:
K. Ziemski — „Wachnowski"
Z-CA D-CY W-SKIEGO KORPUSU A.K.

Londyn, dnia 7.3.68""",
        "pieczecie": [],
        "podpisy": ["K. Ziemski «Wachnowski»"],
        "osoby": [
            "Krzysztof Głuchowski ps. «Juras»",
            "K. Ziemski ps. «Wachnowski» (Z-ca D-cy Warszawskiego Korpusu AK)",
            "Gen. Tadeusz Bór-Komorowski (ustanowienie odznaczenia)"
        ],
        "znaki_szczegolne": [
            "Legitymacja Krzyża Armii Krajowej — odznaczenie ustanowione 1.VIII.1966",
            "Pseudonim «Juras» — od niego nazwa serii kolekcji",
            "Przydział: ZWZ, Kompania K, Pluton III/2, 7 Pułk Ułanów Lubelskich «Jeleń»",
            "Podpisana w Londynie 7 marca 1968",
            "Podpis K. Ziemskiego «Wachnowskiego» — Zastępcy Dowódcy Warszawskiego Korpusu AK",
            "Dokument drukowany z odręcznymi wpisami danymi i podpisem"
        ],
        "kontekst": "Legitymacja potwierdzająca nadanie Krzyżowi Armii Krajowej Krzysztofowi Głuchowskiemu ps. «Juras». Odznaczenie ustanowione przez gen. Bora-Komorowskiego 1 sierpnia 1966 r. dla upamiętnienia żołnierzy Polski Podziemnej 1939-1945. Krzysztof służył w ZWZ, a następnie w 7 Pułku Ułanów Lubelskich «Jeleń» — tym samym pułku co jego brat Stefan. Legitymacja wydana w Londynie w 1968 r."
    },

    # ═══════════════════════════════════════════════════════════════
    # galeria_tablica_gestapo — Tablica pamiątkowa ataku na Gestapo
    # ═══════════════════════════════════════════════════════════════
    "galeria_tablica_gestapo": {
        "typ": "Tablica pamiątkowa / inskrypcja",
        "data": "1.VIII.1944",
        "jezyk": "polski",
        "nadawca": "brak (tablica upamiętniająca)",
        "adresat": "brak",
        "transkrypcja": """Dnia 1.8.1944 r. godz. 17.
z tego domu i okolicznych
ruszyło do natarcia
na gmach Gestapo i Dom Prasy
5 plutonów
7 pułku ułanów AK
„JELEŃ"
z 187 Powstańców
poległo 67
Cześć Ich pamięci.""",
        "pieczecie": [],
        "podpisy": [],
        "osoby": [
            "Żołnierze 7 Pułku Ułanów AK «Jeleń»",
            "187 Powstańców (uczestników natarcia)",
            "67 poległych"
        ],
        "znaki_szczegolne": [
            "Tablica pamiątkowa z Powstania Warszawskiego",
            "1 sierpnia 1944 godz. 17:00 — godzina «W», początek Powstania",
            "Natarcie na gmach Gestapo i Dom Prasy",
            "5 plutonów 7 Pułku Ułanów AK «Jeleń»",
            "187 powstańców ruszyło do ataku, 67 poległo (36% strat)",
            "Papier maszynowy, prawdopodobnie kopia lub druk pamiątkowy",
            "Tekst ułożony pionowo na kartce"
        ],
        "kontekst": "Tablica upamiętniająca atak 7 Pułku Ułanów AK «Jeleń» na gmach Gestapo i Dom Prasy w pierwszych minutach Powstania Warszawskiego, 1 sierpnia 1944 o godz. 17:00 (godzina «W»). Z 187 powstańców poległo 67 — ponad jedna trzecia. To ten sam pułk, w którym służyli Krzysztof («Juras») i Stefan Głuchowscy. Dokument łączy kolekcję z najkrwawszymi chwilami Powstania."
    },

    # ═══════════════════════════════════════════════════════════════
    # wa_biogram_lech — Biogram rtm. Lecha Głuchowskiego ps. "Iżycki"
    # ARG/VI/24 — maszynopis Krzysztofa, Rio de Janeiro 18.X.1995
    # ═══════════════════════════════════════════════════════════════
    "wa_biogram_lech": {
        "typ": "maszynopis/biogram",
        "data": "18.X.1995",
        "jezyk": "pl",
        "nadawca": "Krzysztof Głuchowski (autor biogramu)",
        "adresat": "archiwum rodzinne / instytucje pamięci",
        "transkrypcja": """ROTMISTRZ LECH GŁUCHOWSKI PSEUDONIM «IŻYCKI»

[w Rakowcu pod nr...] Marian Głuchowski i Marta z Żółkiewskich.
Urodzony w [...] roku. P.W. W 1918 roku 16 lat [...] Ciągnionej.
Szkoły średnie w Radomsku a następnie w [...] roku spółka celulozowa jako [...]
[...] broni, będąc już [...]
W [...] roku [...] rozpoczął naukę na Akademii Rolniczej w Bydgoszczy [...] 7 Pułku
Małych Podlaskich Bożymów Krakowskiich [...] w oficielskim [...] rok pierwszy
[...] nad Słochem, a następnie w roku 1930 administrację dość obrończą w Branicach w [...]

We wrześniu 1939 zmobilizowany, odbywał kampanię w 7 P.U.L., który to stworzył
[...] broni pod Sochaczewem, później w ko[szarach?] walk w Warszawy, [...]
do pułqów [...] Kliczkę na [...] stronę Wisły [...] za [...]
[...] ewakuowano na południe od Pilicy, gdzie zwalczał [...] oddział [...] został [...]
[...] do 10[.] Brygady Kawalerii [...] Francji [...]

[...] w 1944 dowodził natarciem Dywizjonu «Jeleń» na Al. Szucha, następnie w grupie powstańczej
[...] przy życiu ułanów, przenosząc się na Mokotów.
[...] dowodził rozdziałem Dywizjonu, biorąc miejsca martwych
ułanów [...] matarcia na szkoły [...] W [...] 21 [...] września obronnie dowódczym [...]
«Jeleń» ułanów obwody, a w każdej checie mostu prowadził strzały. Przez przerzucenie się na Mokotowie
15 września 1944 w czasie obrony pozycji nacierających [...] Niemcach [...] zdobywanych w okolicach [...]
[...] tam gdzie umarłech, po pochwaniu i wieczorze, pochwany jak za życia
[...] w tymczasowej mogile, po ekshumacji spoczął w grobie rodzinnym na cywilnym cmentarzu
na Powązkach Dywizyjnych [...]

[...] do stopnia majora i (odznaczony) Krzyżem Virtuti Militari. Inne odznaczenia —
Krzyż Walecznych, Złoty Krzyż Zasługi z Mieczami, Krzyż Armii Krajowej (No. I specjalna seria
z 6,67 [...] podpisem gen. [...] Polskiego-Sosnnego(?)

Wzmianki o rtm. I Lechu Głuchowskim następujących w następujących wydawnictwach i rozkazach
/ Gazeta Ludowa nr 138 20.5.19[46?] i nr 14.8.19[46?]
/ «Łam i Lubelscy» — wydawane od 1947 przez Koło 7 P.U.Ł. Lubelskich w Londyn
/ Bellona/Zesz III str 43-44, London 1953 (artykuł płk. dypl. G. I.czworniaczukowa)
/ Powstanie Warszawskie, Adam Borkiewicz, Pax Warszawa 1957
/ Tatar: Warszawski w [...] / Bieliński: Stolica 1957
/ Powstanie Warszawskie, M. Bartnicka etc. Warszawa 1957
/ «A Przyszło to» Nr 32(177) 7.8.60 Warszawa
/ i Nr [...] I do nr 15270(1) 15.8.66 Warszawa
/ Powstanie Warszawskie, t.dzieło M. Bartnicka [...] Warszawa 1967
/ «Łam i Lubelscy» Księga Dziejów 7 P.U.Ł Lubelskich, Londyn 1969
/ Żołnierze Mokotowa 1944, t. dzieło M. Bartnicka MON Warszawa 1971
/ Jałmużny, Praca zbiorowa PIW Warszawa 1989
/ Dziennik Polski 2.4.91, 29.8.91, 24.6.91, 30.7.92, 23.9.92, London
/ Żołnierze w cieniu słusznego oponentka 1939-1945 Bożena Niemurzycka-Szczepanik, Warszawa 1992
/ 135 Pluton AK...; Opracował Andrzej Dławicki/ski Warszawa 1994
/ Biblioteka Narodowa w Warszawie Zbiór Rękopisów No. 13853

*Później I wice minister Spraw Wojskowych, i dowódca Jednostek Wojska w Wielkiej Brytanii,
generał dywizji.

Przygotował Krzysztof Głuchowski
Rio de Janeiro, 18 października 1995""",
        "pieczecie": [],
        "podpisy": ["Krzysztof Głuchowski"],
        "osoby": [
            "Rtm. Lech Głuchowski ps. «Iżycki» (ok. 1902–15.IX.1944, poległ na Mokotowie)",
            "Marian Głuchowski (ojciec Lecha)",
            "Marta z Żółkiewskich Głuchowska (matka Lecha)",
            "Gen. dyw. Janusz Głuchowski (brat Lecha — przypis o I Wiceministrze)",
            "Gen. Bór-Komorowski (kontrasygnat Krzyża AK Nr 1)",
            "Krzysztof Głuchowski (autor biogramu, bratanek Lecha)",
            "Adam Borkiewicz (autor «Powstania Warszawskiego», cytowany)",
            "M. Bartnicka (autorka kilku prac o Powstaniu i Mokotowie)"
        ],
        "znaki_szczegolne": [
            "Maszynopis A4, jedna pełna strona — identyczny format jak biogramy Stefana i Krzysztofa",
            "Sporządzony tego samego dnia (18.X.1995) co pozostałe biogramy — systematyczna praca dokumentacyjna",
            "Bibliografia 16 pozycji — Lech wzmiankowany w wielu publikacjach o Powstaniu",
            "Krzyż AK Nr 1 specjalna seria — najwyższe odznaczenie AK",
            "Pochowany na Powązkach Dywizyjnych po ekshumacji z grobu tymczasowego",
            "Lech poległ na Mokotowie 15.IX.1944 — ten sam dzień co kapitulacja Mokotowa",
            "Awansowany pośmiertnie do stopnia majora",
            "16 lat w 1918 — brał udział w odzyskaniu niepodległości",
            "Przypis gwiazdkowy o gen. Januszu = potwierdzenie braterstwa Lecha i Janusza"
        ],
        "kontekst": "Trzeci z serii biogramów spisanych przez Krzysztofa Głuchowskiego w Rio de Janeiro 18 października 1995 (razem z autobiogramem i biogramem Stefana). Lech Głuchowski — brat Janusza (1888) i Stefana (1893), syn Mariana i Marty z Żółkiewskich. Rotmistrz kawalerii, weteran kampanii wrześniowej 1939 (7 P.U.L.), Francji (10. Brygada Kawalerii Pancernej) i AK. Dowodził natarciem na gmach Gestapo przy Al. Szucha. Poległ 15 września 1944 na Mokotowie — w dniu kapitulacji tej dzielnicy. Odznaczony Krzyżem Virtuti Militari i Krzyżem AK Nr 1. Pochowany na Powązkach. TRZY BRACIA GŁUCHOWSCY w wojnie: Janusz (generał PSZ w Wielkiej Brytanii), Stefan (AK Żoliborz, aresztowany na Pawiaku), Lech (AK Mokotów, poległ). Archiwum w BN Warszawa: Zbiór Rękopisów Nr 13853."
    },

    # ═══════════════════════════════════════════════════════════════
    # wa_etykieta_stefan — Etykieta archiwalna: Listy Stefana 1945–1949
    # ARG/VI/27
    # ═══════════════════════════════════════════════════════════════
    "wa_etykieta_stefan": {
        "typ": "etykieta archiwalna",
        "data": "ok. 1945-1949",
        "jezyk": "pl",
        "nadawca": "archiwista rodzinny (Krzysztof Głuchowski?)",
        "adresat": "archiwum rodzinne",
        "transkrypcja": """Listy ppor. Stefana Głuchowskiego
z obozu w Niemczech z lat 1945-1947
do gen. Janusza Głuchowskiego w Anglii
oraz
Listy Stefana Głuchowskiego z Polski
do syna Krzysztofa w Anglii z lat
1947-1949""",
        "pieczecie": [],
        "podpisy": [],
        "osoby": [
            "Ppor. Stefan Głuchowski (nadawca listów z obozu i Polski)",
            "Gen. Janusz Głuchowski (adresat listów 1945-1947)",
            "Krzysztof Głuchowski (adresat listów 1947-1949, syn Stefana)"
        ],
        "znaki_szczegolne": [
            "Etykieta na pomarańczowym papierze, pismo maszynowe",
            "Opisuje zawartość teczki archiwalnej — dwie serie listów",
            "Potwierdza korespondencję Stefana z obozu jenieckiego w Niemczech (1945-47) do brata Janusza w Anglii",
            "Listy z Polski (1947-49) do syna Krzysztofa — po powrocie Stefana do kraju",
            "Dowód kontaktu rodzinnego ponad granicami żelaznej kurtyny"
        ],
        "kontekst": "Etykieta dokumentująca dwie serie listów Stefana Głuchowskiego: (1) z obozu jenieckiego w Niemczech (1945-47) do brata gen. Janusza w Anglii, (2) z Polski (1947-49) do syna Krzysztofa w Anglii. Potwierdza ciągłość kontaktu rodzinnego mimo podziału na dwie strony żelaznej kurtyny. Stefan po powrocie z obozu wrócił do Polski, Krzysztof został w Anglii (potem emigrował do Brazylii). Archiwa listów zdeponowane prawdopodobnie w BN Warszawa, Zbiór Rękopisów Nr 13853."
    },

    # ═══════════════════════════════════════════════════════════════
    # wa_dedykacja_lech_stefan — Dedykacja Lecha dla brata Stefana
    # ARG/VI/28
    # ═══════════════════════════════════════════════════════════════
    # ═══════════════════════════════════════════════════════════════
    # krzyz_legionowy — Dyplom Krzyża Legionowego Nr 145
    # ARG/II/10 — dla płk. Janusza Głuchowskiego, 11.VII.1925
    # ═══════════════════════════════════════════════════════════════
    "krzyz_legionowy": {
        "typ": "dyplom",
        "data": "11.VII.1925",
        "jezyk": "pl",
        "nadawca": "II Zjazd Legionistów / Komisja Kwalifikacyjna",
        "adresat": "Płk Janusz Głuchowski",
        "transkrypcja": """NA PODSTAWIE
UCHWAŁY
II ZJAZDU LEGJONISTÓW
I
WNIOSKU
KOMISJI KWALIFIKACYJNEJ
nadaję
Pułkownikowi
Głuchowskiemu Januszowi
z 1.p.uł.
KRZYŻ LEGJONOWY
[podpis]
Za Komisję
Kwalifikacyjną
[podpis]
Warszawa
dn. 11.VII. 1925.
Nr. 145.""",
        "pieczecie": [],
        "podpisy": ["Podpis sygnatariusza (Piłsudski?)", "Podpis Za Komisję Kwalifikacyjną"],
        "osoby": [
            "Płk Janusz Głuchowski (odznaczony)",
            "Józef Piłsudski (prawdopodobny sygnatariusz)"
        ],
        "znaki_szczegolne": [
            "Druk ozdobny z wizerunkiem Krzyża Legionowego u góry",
            "Nr 145 — niski numer nadania",
            "Stopień: pułkownik (płk) — w 1925 Janusz był już pułkownikiem",
            "Jednostka: 1 Pułk Ułanów (z 1.p.uł.)",
            "Data 11.VII.1925 — rocznica wymarszu Siódemki Beliny (1914)"
        ],
        "kontekst": "Krzyż Legionowy — odznaczenie pamiątkowe nadawane uczestnikom Legionów Polskich 1914–1918. Janusz Głuchowski był jednym z Siódemki Beliny — pierwszych 7 zwiadowców Legionów (6.VIII.1914). Nr 145 potwierdza wczesne nadanie. W 1925 Janusz w stopniu pułkownika, dowódca 1 Pułku Ułanów."
    },

    # ═══════════════════════════════════════════════════════════════
    # list_ambasada_izrael — List do Ambasady Izraela, waluty gettowe
    # ARG/VI/10 — 13.V.1958, Londyn
    # ═══════════════════════════════════════════════════════════════
    "list_ambasada_izrael": {
        "typ": "list",
        "data": "13.V.1958",
        "jezyk": "en",
        "nadawca": "K. Głuchowski (42, Emperors Gate, London S.W.7)",
        "adresat": "The Israel Embassy, Public Relations Office, 2 Palace Green, London W.8.",
        "transkrypcja": """42, Emperors Gate,
London S.W.7

13th May, 1958.

The Israel Embassy,
Public Relations Office,
2, Palace Green,
London W.8.

Dear Sir,

I am contemplating sale of my complete set of paper currency and coins issued in Lodz ghetto during the german occupation of Poland.

The above set is of great rarity and museal value, and I wonder if some institution in Israel would not be interested in purchase.

Hoping that you will be able to assist me in this matter, I remain, Sir,

yours faithfully,

K. Głuchowski.""",
        "pieczecie": [],
        "podpisy": ["K. Głuchowski"],
        "osoby": [
            "K. Głuchowski (nadawca — prawdopodobnie gen. Janusz, adres Emperors Gate)",
            "Ambasada Izraela w Londynie (adresat)"
        ],
        "znaki_szczegolne": [
            "List w języku angielskim",
            "Adres 42 Emperors Gate, London SW7 = znany adres gen. Janusza",
            "Kompletny zestaw walut i monet getta łódzkiego",
            "'great rarity and museal value' — świadomość wartości muzealnej",
            "Rok 1958 — 10 lat po powstaniu Państwa Izrael"
        ],
        "kontekst": "Fascynujący dokument — gen. Janusz (lub Krzysztof?) posiadał kompletny zestaw walut getta łódzkiego (Litzmannstadt Ghetto, 1940-44) i chciał go sprzedać instytucji muzealnej w Izraelu. Waluty gettowe Chaima Rumkowskiego — dziś ekstremalnie rzadkie numizmaty. Adres Emperors Gate potwierdza, że nadawcą jest gen. Janusz."
    },

    # ═══════════════════════════════════════════════════════════════
    # nekrolog_lorens — Nekrolog plut. Jana Lorensa, 7 P.Uł.
    # ARG/VI/9 — zmarł 28.I.1960, Chicago
    # ═══════════════════════════════════════════════════════════════
    "nekrolog_lorens": {
        "typ": "nekrolog",
        "data": "28.I.1960",
        "jezyk": "pl",
        "nadawca": "Koło Żołnierzy 7 Pułku Ułanów Lubelskich im. Gen. K. Sosnkowskiego",
        "adresat": "ogół kombatantów / prasa polonijna",
        "transkrypcja": """Ś. † P.
JAN LORENS
plutonowy 7 pułku ułanów, prezes sekcji Koła pułkowego;
czynny członek wielu organizacji niepodległościowych w Chicago,
odznaczony Krzyżem Walecznych i innymi odznaczeniami polskimi
i zagranicznymi, zmarł 28 stycznia 1960 w Chicago.
Cześć Jego pamięci!
KOŁO ŻOŁNIERZY 7 PUŁKU UŁANÓW LUBELSKICH
IM. GEN. K. SOSNKOWSKIEGO""",
        "pieczecie": [],
        "podpisy": [],
        "osoby": [
            "Plut. Jan Lorens (zmarły, 7 P.Uł., odznaczony KW)",
            "Gen. K. Sosnkowski (patron Koła)"
        ],
        "znaki_szczegolne": [
            "Nekrolog prasowy, numer 8669",
            "Prezes sekcji Koła pułkowego w Chicago",
            "Czynny w organizacjach niepodległościowych",
            "Odznaczony KW i innymi odznaczeniami polskimi i zagranicznymi"
        ],
        "kontekst": "Jan Lorens — plutonowy 7 P.Uł. Lubelskich, prezes sekcji Koła pułkowego w Chicago. Zmarł 28.I.1960. Koło im. Gen. Sosnkowskiego — organizacja kombatancka na emigracji. Nekrolog zachowany przez Krzysztofa w Brazylii."
    },

    # ═══════════════════════════════════════════════════════════════
    # msza_jelen_1970 — Zaproszenie na mszę za poległych AK «Jeleń»
    # ARG/VI/8 — Wilanów, 4.X.1970
    # ═══════════════════════════════════════════════════════════════
    "msza_jelen_1970": {
        "typ": "druk okolicznościowy",
        "data": "4.X.1970",
        "jezyk": "pl",
        "nadawca": "Rodziny i Towarzysze Broni żołnierzy AK «Jeleń»",
        "adresat": "kombatanci i rodziny",
        "transkrypcja": """Dnia 4-go października 1970 r. /niedziela/ o godz. 10-ej w kościele
św. [...] w Wilanowie będzie odprawiona doroczna Msza św. za poległych
w czasie okupacji i Powstania Warszawskiego
ŻOŁNIERZY PUŁKU AK «JELEŃ»
Po mszy, zostaną złożone kwiaty na miejscowym cmentarzu — na mogile
żołnierzy «Jelenia», poległych na Sadybie.
Rodziny i Towarzysze Broni.
Po złożeniu kwiatów na cmentarzu — kto będzie chciał — może wziąć udział
we wspólnym śniadaniu w miejscowej restauracji «Kuźnia».""",
        "pieczecie": [],
        "podpisy": [],
        "osoby": [
            "Żołnierze AK «Jeleń» polegli na Sadybie",
            "Rodziny i Towarzysze Broni (organizatorzy)"
        ],
        "znaki_szczegolne": [
            "Doroczna msza — tradycja kontynuowana mimo PRL",
            "Wilanów — groby na cmentarzu lokalnym",
            "Sadyba — dzielnica Warszawy, miejsce walk AK",
            "Restauracja «Kuźnia» — miejsce spotkań kombatanckich",
            "Druk maszynowy na żółtawym papierze"
        ],
        "kontekst": "Doroczna msza za poległych żołnierzy 7 P.Uł. AK «Jeleń» — Wilanów, październik 1970, 26 lat po Powstaniu. W PRL pamięć o AK była marginalizowana i prześladowana — fakt odprawiania mszy świadczy o odwadze kombatantów. Groby na Sadybie. Dokument zachowany w kolekcji Krzysztofa w Brazylii."
    },

    "wa_dedykacja_lech_stefan": {
        "typ": "dedykacja",
        "data": "lata 30. XX w.",
        "jezyk": "pl",
        "nadawca": "Lech Głuchowski i koledzy oficerscy",
        "adresat": "Stefan Głuchowski",
        "transkrypcja": """Kochanemu Stefankowi, uroczemu
braciszkowi i dobremu towarzyszowi
Lech       Lochia(?)
[podpisy kolegów oficerskich — 8 p.S.K.]
[...] p.[?]
[...] Morawski(?) [...]
[...] Meguriński(?)
[...] Waszelski(?)""",
        "pieczecie": [],
        "podpisy": ["Lech Głuchowski", "Lochia(?)", "5-6 nieczytelnych podpisów oficerskich"],
        "osoby": [
            "Lech Głuchowski (autor dedykacji, brat Stefana)",
            "Stefan Głuchowski (adresat — 'kochany Stefanku')",
            "Koledzy oficerscy z 8 p.S.K. (podpisy)"
        ],
        "znaki_szczegolne": [
            "Pismo kaligraficzne atramentem (Lech)",
            "Serdeczny ton: 'kochany Stefanku, uroczy braciszku'",
            "Wzmianka '8 p.S.K.' — 8 Pułk Strzelców Konnych?",
            "Grupowa dedykacja — podpisy kolegów oficerskich",
            "Papier pożółkły, atrament brązowiejący"
        ],
        "kontekst": "Unikalna dedykacja Lecha Głuchowskiego do brata Stefana — świadectwo ciepłych relacji braterskich w okresie międzywojennym. Lech (ok. 1902–1944) poległ na Mokotowie w Powstaniu Warszawskim. Wzmianka '8 p.S.K.' może wskazywać na 8 Pułk Strzelców Konnych lub inną formację kawalerii. Dedykacja grupowa z podpisami kolegów oficerskich — portret środowiska wojskowego II RP."
    },

    # ── Korespondencja 1946 ─────────────────────────────────────────

    "juras_174": {
        "typ": "list",
        "data": "3.VIII.1946",
        "jezyk": "pl",
        "nadawca": "Aleksander Flejszer",
        "adresat": "Krzysztof Głuchowski",
        "transkrypcja": """Sierż.-mgr. Aleksander Flejszer, Polish Forces, C.M.F. 509.
M.p., dn. 3/8/46 r.

Szanowny Panie!

Otrzymałem list z miasta Łodzi od mojej żony. W liście tym żona prosi mnie, w imieniu matki Pańskiej, Pani Wandy, o skomunikowanie się z Panem, podając mi adres Pana — C.M.F. 105.

Matka Pańska serdecznie Pana pozdrawia i prosi Pana o napisanie do niej kilku słów. Pisać powinien Pan nie podając ani miejsca pobytu, ani daty. List ten proszę wysłać na następujący adres:

Władysław Goldman,
1 rue du Docteur Labbé,
Paris 20e,
France

Stamtąd list zostanie skierowany do mojej żony, która przyjaźni się z Panią Wandą i bodaj codziennie ją widuje. Tą drogą ja komunikuję się z żoną i listy z jednej i drugiej strony przychodzą. Do wybuchu wojny ja pracowałem w aptece Włodzimierza Gruchowskiego.

Gruchowscy wszyscy żyją i mieszkają w Łodzi: Pani Ludmiła od czasu do czasu choruje na płuca, a córka ich — Irusia — jest po doktoracie.

Bardzo byłbym rad, gdybym od Pana otrzymał kilka słów.

Przesyłam serdeczne pozdrowienia
A. Flejszer""",
        "osoby": ["Aleksander Flejszer", "Wanda Głuchowska", "Krzysztof Głuchowski", "Władysław Goldman", "Ludmiła Gruchowska", "Irusia Gruchowska", "Włodzimierz Gruchowski"],
        "znaki_szczegolne": [
            "Nagłówek drukowany z danymi wojskowymi",
            "Konspiracyjna droga pocztowa: CMF → Paryż (Goldman) → Łódź → Wanda",
            "Wzmianka o aptece Gruchowskiego — przedwojenny kontekst zawodowy"
        ],
        "kontekst": "Sierpień 1946. Flejszer pośredniczy w nawiązaniu kontaktu między Wandą (Łódź/Warszawa) a Krzysztofem (Włochy). Droga pocztowa: żołnierz → Paryż (Goldman) → żona Flejszera (Łódź) → Wanda. Pisanie bez podawania miejsca i daty — środek ostrożności wobec cenzury komunistycznej."
    },

    "juras_175": {
        "typ": "list",
        "data": "13.VIII.1946",
        "jezyk": "pl",
        "nadawca": "Wanda Głuchowska",
        "adresat": "Krzysztof Głuchowski",
        "transkrypcja": """Drogi Kochany Synku!

Czekam od Ciebie znaku życia, ale jak dotąd bezowocnie. —

U nas w rodzinie trochę nowości, bo Grażynę z rodziną wuj Karik nareszcie odebrał do nas. Grażynka urocze dziecko u matki, to znaczy na Żoliborzu, a mąż jej pojechał do Prus Wschodnich objąć posadę inspektora rolnego. Wuj Karik jeszcze się nie ustalił; a na razie jest w Łodzi, bo tam mieszka Sławka. U Witoldów wielkie nieszczęście, bo ciotka b. ciężko na płuca.

Ja jestem zdrowa i otworzyłam aptekę na drugiej stronie, tam gdzie była Cysia Cukiernia. Komora jest zupełnie zniszczona, ale dolne sklepienie i dolne [są tu?].

Synku Kochany napisz do mnie choćby kilka słów i całuję Cię

Wandy

Ł. 13/VIII 46 r.""",
        "osoby": ["Wanda Głuchowska", "Krzysztof Głuchowski", "Grażyna", "Karik (wuj)", "Sławka", "Witoldowie"],
        "znaki_szczegolne": [
            "Pismo odręczne Wandy — atrament niebieski, papier w linie",
            "Podpis 'Wandy' (dopełniacz — 'od Wandy')",
            "Data 'Ł.' = Łódź",
            "Wzmianka o aptece na rogu Kruczej i Hożej (dawna cukiernia Paciorkowskiego/Cysia)",
            "Fragment nieczytelny: 'ale dolne sklepienie i dolne [są tu?]'"
        ],
        "kontekst": "Pierwszy znany list Wandy Głuchowskiej do syna Krzysztofa na emigracji. Wanda — żona gen. Janusza Głuchowskiego, matka Krzysztofa. Aresztowana po wojnie, wywieziona do Rosji, obóz w Rembertowie — ale w tym liście o represjach nie pisze. Odbudowała aptekę w Warszawie na rogu Kruczej i Hożej. List szedł konspiracyjną drogą przez Paryż."
    },

    "juras_176": {
        "typ": "list",
        "data": "25.VIII.1946",
        "jezyk": "pl",
        "nadawca": "Henryk Łabędzki",
        "adresat": "Krzysztof Głuchowski",
        "transkrypcja": """Szanowny Panie Krzysztofie!

Matka Pana, pani Wanda wręczyła mi list, celem przesłania Panu. Jednocześnie prosiła mnie o przesłanie Panu co pewien czas pieniędzy, by Pan nie był skrępowany zanadto w swoich wydatkach. Zechce Pan wobec tego podać mi odwrotną pocztą, jak mam ten przekaz uskutecznić, a niezwłocznie tak postąpię.

Niezależnie od tego zechce Pan zakomunikować ojcu swemu w imieniu p. Wandy, że w Polsce wydano ustawę, iż wszyscy co byli urzędnicy państwowi są obowiązani w ciągu krótkiego czasu (jeszcze jakieś 2 miesiące) wrócić do kraju i zameldować swoje przybycie, pod groźbą całkowitej utraty praw do ewentualnej emerytury. Prócz tego prosiła p. Wanda o zakomunikowanie, że aptekarz Bukowski od trzech miesięcy siedzi w więzieniu. Przyczyna aresztowania bliżej nieznana.

Załączam również 2 fotografie które p. Wanda mi wręczyła.

Odpowiedzi na przyszłość zechce Pan kierować pod adresem:
Jules Schwob, Genève, Suisse
Quai Charles Page 37.

W Genewie przebywam od 2–3 tygodni i o ile odpowiedź od Pana nadejdzie do tego czasu, osobiście ją zawiozę do W-wy; o ile później, zostanie przesłana matce przez wyżej wymienioną osobę.

Łączę pozdrowienia
Łabędzki Henryk

Genewa, 25 sierpnia 1946""",
        "osoby": ["Henryk Łabędzki", "Wanda Głuchowska", "Krzysztof Głuchowski", "Jules Schwob", "Bukowski (aptekarz)"],
        "znaki_szczegolne": [
            "Trzecia droga pocztowa: Genewa (Schwob) → Warszawa",
            "Wzmianka o ustawie nakazującej powrót urzędników",
            "Aresztowanie aptekarza Bukowskiego",
            "2 fotografie załączone przez Wandę (niezidentyfikowane)",
            "Pismo pochyłe, atrament czarny"
        ],
        "kontekst": "Łabędzki pośredniczy z Genewy. Ustawa o powrocie urzędników — komunistyczny nacisk na emigrację. Bukowski aresztowany — represje wobec inteligencji. Droga pocztowa przez Jules Schwob (Genewa) — niezależna od kanału paryskiego (Goldman)."
    },

    "juras_177": {
        "typ": "list",
        "data": "1.XII.1946",
        "jezyk": "pl",
        "nadawca": "Wanda Głuchowska",
        "adresat": "Krzysztof Głuchowski",
        "transkrypcja": """[POCZĄTEK LISTU BRAKUJE — pierwsza strona zaginęła]

...jest w Krynicy, gdzie jest jeszcze jakiś doktór, który stosuje nowe metody, u nas dotąd nie stosowane.

Krysieńku czy czasem nie słyszałeś nic o Twoim Rodzeństwiem — Josiek zginął na Starówce, a ojczka — nie ma. Kosterlitz — również że nie żyje. Pani Londyńszczerowa miota się w rozpaczy, żeby coś o niej się dowiedzieć. Wogóle jeśli chodzi o Twoich kolegów ze szkoły powszechnej, to prawie wszyscy wyginęli.

Jak bardzo jestem Ciebie ciekawa, Krysieńku — przecież już jesteś dorosłym mężczyzną. Pewnego spotkanego młodego mężczyznę przyjmiesz w myśli z Tobą od serca całuję i ściskam serdecznie mocno

Wandy

Swego czasu posłałam Ci plakietkę Batorego. Czy ją dostałeś i ile masz wzrostu? Napisz mi.

W. 1/12 46 r.""",
        "osoby": ["Wanda Głuchowska", "Krzysztof Głuchowski", "Josiek", "Kosterlitz", "Pani Londyńszczerowa"],
        "znaki_szczegolne": [
            "NIEKOMPLETNY — brak pierwszej strony",
            "Zdrobnienie 'Krysieńku'",
            "Lista poległych kolegów ze szkoły powszechnej",
            "Pytanie o wzrost syna — matka nie widziała go 2 lata",
            "Plakietka Batorego — symbol polskości",
            "Papier pomarszczony, atrament ciemny"
        ],
        "kontekst": "Grudzień 1946. Wanda wylicza poległych kolegów syna — Josiek na Starówce, Kosterlitz, 'prawie wszyscy wyginęli.' Matka nie widziała 18-letniego syna od ewakuacji z Warszawy (1944). Pytanie 'ile masz wzrostu' — nie wie jak wygląda jej dorosły syn."
    },

    # ── Korespondencja 1945-1947 (starszy PDF) ──────────────────

    "juras_207c": {
        "typ": "list",
        "data": "5.II.1947",
        "jezyk": "pl",
        "nadawca": "Janusz Kamiński",
        "adresat": "Krzysztof Głuchowski",
        "transkrypcja": """Brownings Camp, Billingshurst, Sussex, 5/II/46 [prawdopodobnie 1947]

Kochany Panie Krzysiu.

Niezmiernie mi przykro, że nasze spotkanie w Londynie nie doszło do skutku.

Z listu żony, pisanego 25/I br. przepisuję ustęp dotyczący Pana Matki:

'Wanda prosi być przytulić do serca Krzysia — bardzo się ponieważ w W-wie — mieszka przy aptece, którą z wielkim nakładem wysiłku i pieniędzy odbudowała (tylko parter rogowy w zupełnie zrujnowanym domu), na razie idzie stało. To tam gdzie poprzednio była cukiernia Paciorkowskiego — róg Kruczej i Hożej!'

Adres cioci Staśki: Staśka Armatysowa, ul. Żwirki 1 d m 12.

Tak p. Wanda była aresztowana, wywieziona do Rosji, potem siedziała w obozie w Rembertowie. Ale to dawne czasy, teraz nie powinno Jej nic grozić. Ale napewno jest pod obserwacją, i lepiej do Niej wprost nie pisywać! Najlepiej do p. Staśki!

Oddany Janusz K.""",
        "osoby": ["Janusz Kamiński", "Wanda Głuchowska", "Krzysztof Głuchowski", "Staśka Armatysowa"],
        "znaki_szczegolne": [
            "KLUCZOWY: deportacja Wandy do Rosji + obóz Rembertów",
            "Apteka róg Kruczej i Hożej — trzecie potwierdzenie",
            "Wanda pod obserwacją"
        ],
        "kontekst": "Najważniejszy dokument o represjach wobec Wandy Głuchowskiej. Jedyne pisemne potwierdzenie deportacji do Rosji i obozu w Rembertowie."
    },

    "juras_178": {
        "typ": "list",
        "data": "ok. 1946",
        "jezyk": "pl",
        "nadawca": "nieznany",
        "adresat": "Krzysztof Głuchowski",
        "transkrypcja": """Drogi Krysiu! Od Matki Twojej z Warszawy przesyłam Ci najserdeczniejsze pozdrowienia. Matka Twoja ma aptekę w Warszawie i nieźle jej się powodzi. Tylko, że jeden z Twoich stryjków jest zaaresztowany.

Pozdrowienia przesyłam
[podpis nieczytelny]""",
        "osoby": ["Wanda Głuchowska", "Krzysztof Głuchowski"],
        "znaki_szczegolne": [
            "Bilecik — mały karteczek ok. 8×12 cm",
            "Podpis nieczytelny — pośrednik anonimowy",
            "Wzmianka o aresztowaniu stryjka"
        ],
        "kontekst": "Anonimowy bilecik z pozdrowieniami od Wandy. Pośrednik — prawdopodobnie okazyjny podróżny. Stryjek aresztowany — represje."
    },

    "juras_179": {
        "typ": "list",
        "data": "12.X.1946",
        "jezyk": "pl",
        "nadawca": "Henryk Łabędzki",
        "adresat": "Krzysztof Głuchowski",
        "transkrypcja": """Genewa, 12 paźdz. 1946

Szanowny Panie!

Potwierdzam odbiór listu Pana z 23 września b.r. i odpowiadam również z poważnym opóźnieniem, gdyż dotychczas leżałem w szpitalu w Zurichu i przytem nic nie widziałem, po operacji ocznej.

Odnośnie pieniędzy przesyłam Panu przy niniejszym trzy funty, załączone w kopertę, i proszę Pana w Jego interesie o odwrotne potwierdzenie odbioru wymienionej sumy. Po otrzymaniu potwierdzenia przyślę Panu jeszcze dwukrotnie takie same sumy w pewnych odstępach czasu.

Co dotyczy korespondencji zechce Pan na wymieniony adres przesyłać listy, które następnie będą przesłane do kraju.

Ja osobiście wracam jutro do kraju i w ciągu najbliższych dni osobiście porozumiem się z Mamusią Pana.

Łączę pozdrowienia i życzenia pomyślnej nauki
H. Łabędzki""",
        "osoby": ["Henryk Łabędzki", "Krzysztof Głuchowski", "Wanda Głuchowska", "Jules Schwob"],
        "znaki_szczegolne": [
            "Operacja oczna w Zurychu",
            "3 funty w kopercie — pomoc finansowa",
            "Wraca do Polski — 'osobiście porozumiem się z Mamusią'",
            "Adres: Jules Schwob, Quai Charles Page 37, Genève"
        ],
        "kontekst": "Łabędzki wraca do komunistycznej Polski z Genewy. Obiecuje osobisty kontakt z Wandą. Pieniądze dla Krzysztofa — realna pomoc."
    },

    "juras_180": {
        "typ": "list",
        "data": "21.X.1946",
        "jezyk": "pl",
        "nadawca": "Rose Schwok",
        "adresat": "Krzysztof Głuchowski",
        "transkrypcja": """Genève, le 21/X. 46.

Szanowny Panie!

Przed chwilą otrzymałam liścik Sz. Pana, w którym potwierdza Pan odbiór 3ch f., które szwagier posłał Panu przed swym wyjazdem do Polski.

Pozostawił mi 6 f., które w tym liście załączam Panu, no i za kilka dni resztę 3 f. znów załączę Sz. Panu.

Liścik dla matki Pana, przesłałam natychmiast wraz z mym listem do brata mego, który wręczy szwagrowi, a ten doręczy Pani Głuchowskiej.

Załączam pozdrowienia
R. Schwok""",
        "osoby": ["Rose Schwok", "Krzysztof Głuchowski", "Henryk Łabędzki", "Wanda Głuchowska"],
        "znaki_szczegolne": ["6 funtów w kopercie", "Łańcuch: Schwok → brat → Łabędzki → Wanda"],
        "kontekst": "Schwok pośredniczy finansowo i pocztowo z Genewy."
    },

    "juras_181": {
        "typ": "list",
        "data": "3.XI.1946",
        "jezyk": "pl",
        "nadawca": "Rose Schwok",
        "adresat": "Krzysztof Głuchowski",
        "transkrypcja": """Genève, le 3/XI. 46.

Szanowny Panie!

Otrzymałam Pański liścik z dn. 30/X. 46, w którym potwierdza Pan odbiór 3ch f. dn. 21/X. 46 z drugiej przesyłki.

W tym liście załączam ostatnie 3 trzy f., które te dwie przesyłki zostały mi powierzone. Jak zrozumiałam z listu Sz. Pana chce mi Pan przysłać liścik dla Matki Pańskiej, który przez Genewę/Szwajcarię mam posłać do Polski. Z przyjemnością mogę oddać przysługę Panu, lecz listy polecone z Anglji dochodzą do Polski. Myślę, że łatwiejsza droga jest wprost od Pana do Warszawy, nieprawdaż?

W każdym bądź razie, jeśli cokolwiek Sz. Pan będzie potrzebował, oddać będę mogła przysługę, byle ile jest w mej możliwości.

Z poważaniem
Rose Schwok
z domu Zimnowoda""",
        "osoby": ["Rose Schwok", "Krzysztof Głuchowski", "Wanda Głuchowska"],
        "znaki_szczegolne": ["Ostatnie 3 funty", "Rada: listy polecone z Anglii dochodzą do Polski", "Nazwisko panieńskie: Zimnowoda"],
        "kontekst": "Schwok sugeruje bezpośrednią korespondencję. Przełom — konspiracyjna droga przez Genewę może nie być konieczna."
    },

    "juras_182": {
        "typ": "list",
        "data": "13.XII.1946",
        "jezyk": "pl",
        "nadawca": "Wanda Głuchowska",
        "adresat": "Krzysztof Głuchowski",
        "transkrypcja": """Warszawa 13/XII 46 r.

Kochany Synku!

Wysłałam już kilka listów, ale nie wiem czy cokolwiek dojdzie do Was — nieszczególnie jestem pewna obawy czy dojdą przez do Stefka. Synku kochany zbliżają się Święta i znów nie będziemy razem, bardzo to jest trujące dla nas. Liczyłam więc tylko ślę Ci życzenia żebyśmy mogli się jakoś prędko zobaczyć, do eras się tyle.

Wielką to dla mnie radością są Twoje listy i od czasu kiedy dostałam pierwszy Twój list, żyję w oczekiwaniu. Pisz na Paryż.

Krysieńku pamiętaj że sprawa Twoich stryjków jest najważniejszą sprawą dla nas obydwojga i że utrudniające wobec jej tylko Stefka. Oczywiście że nie możesz o nim zapominać, ale z czystym sumieniem z żadnych możliwości na korzyść jego nie rezygnuj. —

U nas zima w pełni, mamy dziś 13 stopni, ale na antresoli ciepło, a ponieważ mam zastępstwo (zwykle pracuję po obiedzie) bo przyuczam jedną z pań żeby mnie mogła zastępić, a ja chcę jechać na kilka dni w okresie świątecznym na wyjazd, więc się zabrałam do pisania listu. Na Święta chcę jechać z Wandą S. do Selesia do rodziny, a później do Jadzi do Wrocławia.

Co rodzinie Węgiernowskiej to od powiadania to bardzo dużo zmian nastąpiło bo: — stary pan Węgiernow umarł jeszcze w 44 r. Zygmuś wrócił z niewoli i ożenił się ze Stefcią Kuralczycówną, to przedszkolanką z Łanuch. Następnie wyszła za mąż Jadia za inż. Gmowskiego b. sympatycznego i pod każdym względem na poziomu pana, następnie ożenił się Adaś z nowo poznaną młodą panienką i nakoniec najsmutniejsza zmiana, umarła Ilżynka Januowa.

Do Łodzi nie jadę choć bardzo na to naręczaj, ale jakoś tak chcę się przewietrzyć po 7-miu latach.

Wczoraj był w aptece p. Trebińskiej bardzo mu się ucieszyłam, bo nie wiadomo tam dokąd czy żyje. Jest obecnie w Porumie i dorobił się córki. Dawałam mu do przeczytania Twoje listy i b. był z nich zadowolony.

Tyle listów do Ciebie w ostatku dni napisałam że już nie wiesz co już wiesz, a co jeszcze nie.

Syneczku — ogromnie wzrosło moje zainteresowanie mężczyznami, bo przecież chcę znaleźć takiego kto by na Twój wzrost. A teraz napisz ile ważysz i ile masz cm szerokości w barkach?

Kończę już, całuję i ściskam mocno serdecznie
Wandy""",
        "osoby": ["Wanda Głuchowska", "Krzysztof Głuchowski", "Wanda S.", "Jadia", "Węgiernowscy", "Zygmuś", "Stefcia Kuralczycówna", "Adaś", "Ilżynka Januowa", "p. Trebiński"],
        "znaki_szczegolne": ["Bezpośrednia poczta Warszawa→Anglia", "Sprawa stryjków — represje", "Chce się 'przewietrzyć po 7-miu latach'", "Pytanie o wzrost, wagę, barki syna"],
        "kontekst": "Grudzień 1946, Warszawa. Wanda pisze bezpośrednio. Tęsknota za synem na Święta. Relacjonuje zmiany w rodzinie Węgiernowskich. 'Po 7-miu latach' — od 1939, bez przerwy w Warszawie/Polsce."
    },

    "juras_183": {
        "typ": "list",
        "data": "2.VII.1946",
        "jezyk": "pl",
        "nadawca": "Wanda Głuchowska",
        "adresat": "Krzysztof Głuchowski",
        "transkrypcja": """Warszawa 2/VII. 1946 r.

Moje Drogie Kochane Drogie Dziecko!

Jak bardzo cieszę się Twemi listami odczytując je po kilka razy dziennie, szukam w nich Ciebie takiego jakiego Cię znam — takiego jakiego jesteś dziś nie mam Cię, bo przecież dzieci nas mogą okropliwości zmienić. To też daleko drogi Synku jestem Ciebie taka ciekawa, bardzo bardzo się cieszę że nareszcie nawiązaliśmy korespondencję, a przyznajesz jak nam piszę tysiąc korespondencji, więc mnie i ja będę mogła bardzo pracę z Twoich listów:

Jaki jest typ szkoły do której chodzisz?
Jak mieszkacie — ilu przychodzi, czy też piszą w baraki?
Czy nie dokucza Ci klimat, tymczasem to przyjechałeś z ciepła?
Czy masz ciepłe rzeczy do ubrania?
Czy palisz papierosy? Czy pijesz alkohol?
Czy reperują zęby?
Jak idzie Ci przyswajanie języka?
Czy ojciec jakoś już nie pracuje?

Pisz dziecenko że pod względem towarzyskim jesteś strona podle, więc tak się zastanawiam czy z Januszkiem Klep. stosunki nie są zbyt serdeczni. Bardzo mi chciała żebyście naprawdę byli przyjaciółmi. Myślę że wiele zawdzięczamy Losi Kl. jeśli chodzi o Starówkę — Czasem to mi się wydaje że to że żyjem to jej opieka.

To że jesteś w takiej przyjaźni z G.D. bardzo mnie cieszy, bo to bardzo przyjemny chłopiec. W zeszłym tygodniu spotkałam p. Lewię ślicznie wyglądała i była doskonale ubrana — przyjechała z Berlina na dwa dni samochodem po żywność bo mówi że tam nic nie można dostać. A u nas wszystkiego wbród.

Bez ograniczeń a można dostać żeby tylko były pieniądze. Gorzej jest z wełną, skórą, lekami — wszystko się kończy. W tej chwili dolar stoi 700 zł (papierowy), ale jakieś dwa tygodnie temu to stał 1400 zł.

Dla orjentacji podaję ceny:
Cukier 180 zł. Masło 480. Mąka pszenna 90 zł. Bułka biała kajzerka 5 zł. Chleb 50 zł. Szynka 500 zł. Kiełbasa 350. Pończochy / buciki damskie półbuty 15 tyś. Wysokie buty oficerskie 40 tyś. Dobra wełna na ubranie 10 do 15 tyś. Proszek od bólu głowy 12 zł 50 gr. Magister farmacji zarabia 18 tysięcy, ale zwykły urzędnik państwowy 16 kategorii 4 500 zł.""",
        "osoby": ["Wanda Głuchowska", "Krzysztof Głuchowski", "Januszek Klep.", "Losia Kl.", "G.D.", "p. Lewia"],
        "znaki_szczegolne": [
            "Najdłuższy list Wandy — 4 strony",
            "Lista cen Warszawy VII.1946 — dokument ekonomiczny",
            "Dolar 700 zł (spadł z 1400)",
            "8 pytań matki do syna",
            "'Czy palisz papierosy? Czy pijesz alkohol?'",
            "Wzmianka o Starówce — 'że żyjem to jej opieka' (Losia Kl.)",
            "Berlin: 'nic nie można dostać', Warszawa: 'wszystkiego wbród'"
        ],
        "kontekst": "Lipiec 1946 — chronologicznie NAJWCZEŚNIEJSZY list Wandy. Bezcenny dokument: ceny, kursy walut, warunki życia w Warszawie. Matka czyta listy syna 'po kilka razy dziennie.' 8 pytań — od szkoły przez papierosy po zęby. Wzmianka o Losi Kl. i Starówce — ktoś kto ich uratował w Powstaniu."
    },

    "juras_201": {
        "typ": "list",
        "data": "",
        "jezyk": "pl",
        "transkrypcja": """Reims, 15.IX.1945 → Krzysztof Głuchowski (CMF, Włochy) | 1 arkusz, dwustronnie, atrament niebiesko-szary
Reims, 15.IX.45.
Panie Krzysiu!
Dziękuję uprzejmie za otrzymany list, który sprawił mi wielką radość. Ucieszyłem się, 
dowiedziawszy się, że Pan dotarł do swego oddziału. Jak się Pan powodzi? Jak jest z 
nożką? Czy klimat odpowiada? Co porabiają d[...]? Jakie są proszę [...] Nawiązałem 
kontakt z bratem, który eme[?] przebywa w okoliczy Hamburga. Do Rot. Borowskiego 
pisać nie mogę, gdyż ten nie posiada
adresu wojskowego. Pisałem na adres Gerersheim, lecz listy wróciły. Obecnie 
otrzymuję listy od brata. Pragnę go odwiedzić, poczem wyruszę w dalszą podróż. 
Sądzę, że wkrótce się zobaczymy. Co słychać o powrocie do Kraju? Jestem nadal w 
Reims. Powodzi mi się dobrze. Nie będę się rozwodziś, gdyż praca moja jest Panu 
dostatecznie znana. Amerykanie przystąpili do przesłuchany[?] samolotów A.j.[?] na 
system zimowy. Otwarci[?] pogłoski, że oddziały wartownicze pozostaną do wiosny.
Inna plotka głosi że przeniosą nas na teren Niemiec, by tam pełnić służbę. Krótkich 
chwil można zauważyć wielcy ruch na terenie Francji. Jednym słowem Francja 
obudziła się z letargu. Obrady[?] żywnościowe i tekstylne napełniają się towarami. 
Skocki[?] chlebowe zniesiono zostaną w przyszłym miesiącu. Ostatnio przeprowadzono
 
u nas ankietę kto chce w ciągu najbliższych 30 dni wrócić do Kraju. Za powrotem 
wypowiedziało się 30%. Amerykanie wyrazili swoje zdziwienie. Co porabia ppor. 
Domyśli[?]?
W przyszłym tygodniu wybieram się do Paryża, by uzyskać zezwolenia na przejazd do 
Niemiec. Panie Krzysiu!! Nie będę Pana zamęczał, gdyż będzie Pan miał trudności w 
odcyfrowaniu mego pisma, dlatego kończę rozsyłając moc uścisków i serdeczny 
żołnierski uścisk dłoni
Kpt Przybyszewski Jan.""",
        "kontekst": "List kpt. Jana Przybyszewskiego"
    },

    "juras_202a": {
        "typ": "list",
        "data": "",
        "jezyk": "pl",
        "transkrypcja": """CMF, 30.XII.1945 → Krzysztof Głuchowski (Liceum 3 DSK) | Nagłówek: Stw. Ostrowski Zygmunt / Polish Forces CMF 
16633/2
Wp. 30.XII.45.
Panie Krzysztofie!
Dowiedziałem się iż jest Pan w Liceum 3 DSK, o sposób przypadkowy informowano też
 
mnie, iż Ojciec Pana jest w Lubece.
Panie Krzysztofie proszę przesłać mi adres Ojca i parę słów o sobie. Ja pragnę 
wiedzieć, jakim samolotem[?] dostał się Pan do Włoch, czy ma Pan wiadomości o 
Matce?
Ja dostałem się do niewoli niemieckiej po kapitulacji O-y[?] z grupą... Choroby 2" (15 
pp.), obecnie jestem w Szkole Podchorążych.
Z okazji Nowego Roku przesyłam Panu najserdeczniejsze życzenia a w szczególności 
osiągnięcia jak najlepszych rezultatów w Liceum.
Łączę mocy uścisk dłoni
Z. Ostrowski
P.S. B[ardzo] załóżmy[?] mi na adresie Ojca.""",
        "kontekst": "List stw. Zygmunta Ostrowskiego (I)"
    },

    "juras_202b": {
        "typ": "list",
        "data": "",
        "jezyk": "pl",
        "transkrypcja": """CMF, 16.III.1946 → Krzysztof Głuchowski | Nagłówek: U.S. Podch. stw. Ostrowski Zygmunt / Polish Forces CMF 16633/2
Wp. 16.III.1946r.
Drogi Panie Kolego!
W poprzednim liście pisał mi Pan, iż w lutym zdaje Pan małą maturę. Jak się Panu 
powiedło? Czy mogę pogratulować?
Obecnie ukończyliśmy Podchorążówkę i z przyjemnością Pana odwiedzę, 
porozmawiamy sobie o wszystkim obszernie, tematów jest dużo... Obecnie jestem 
b[ardzo] skorowany[?], okres egzaminów...
Wczoraj otrzymałem list od Pańskiego Ojca, sprawił mi dużą radość... Nawiązanie 
kontaktu po koszmarnych przeżyciach ostatnich czasów, nawet w drodze listownej 
daje dużą satysfakcję...
Panie Krzysztofie, ponieważ jest Pan na terenie Włoch sam, Ojciec jest od Pana 
stosunkowo daleko, proszę przyjąć do wiadomości iż opiekuję się[?] b. mało[?], i żebym
 
mógł być Panu w czynnościach pomocny. Proszę mnie traktować jako swego starego 
kolegę, czuję do Pana dużo sympatji i życzliwości.
Oczekuję na odpowiedź.
Zygmunt Ostrowski""",
        "kontekst": "List u.s. podch. Zygmunta Ostrowskiego (II)"
    },

    "juras_203": {
        "typ": "list",
        "data": "",
        "jezyk": "pl",
        "transkrypcja": """1944–1947 | Krzysztof Głuchowski | 1 arkusz w linie, atrament fioletowy + ołówek
AWERS — Lista miejscowości z datami
Warszawa 5-X-1944 ✓
Ożarów 5-7-X-1944 ✓
Ożarów – Fallingbostel 7–9-X-1944
— Fallingbostel 9–
Fallingbostel – Dorsten 24–27 X 1944
Dorsten 22-X — XI 1944 ✓
Glagbach XI – 1944 II 1945 ✓
Gerresheim  / Düsseldorf 
✓
✓
Düsseldorf – Reims [strzałka, "H.D."]
Reims  / Troyes  / Paryż  1
✓
✓
✱
[...] Sorgue / Avignon / Marsylia ✓
S. Remo 9 VII / Genova 10 VII / Forlì 11 VII
S. Giorgio 12 VII / M. Rubiano 13 VII — Ancona
Petritoli — Giulianova / Amendola
Rzym  28-VII-1945
✱
Amendola 1-XI-1945
Forlì / Bologna / Ferrara / Rovigo / Padova / Mestre / Treviso / Vittorio Veneto
[Prawa kolumna:] Pescara, Bevi, Trento, Gallipoli, Trani, Barletta, Vittorio, Belluno,
 
Bolzano, Amendola, Grotta Mare , S. Benedetto , Meldola , Ravenna — 
✓
✓
✓
Pedaso, Monteluce, Este , Wenecja , Martinsicuro, Civitanova, Rzym, 
✓
✓
Neapol [podkreślony], Liverpool, Brandon, Bodney, London , Welton, Thetford, 
✱
Ingham, Reading...
[Marginesy:] Horsham, Worcester, Longbridge, Norwich, Swaffham, Liphook / London
 
– Gravesend – Dover – Boulogne – Etaples – Stella Plage – Dover – Ramsgate / Witley – 
Oxford – Loughborough – Leicester – Brighton – Maidenhead / [...] Ameryka
REWERS — Notatki z fizyki, Liceum 3 DSK
L = F·s·cosα
Ek = mv²/2    Ep = mgh
Moc... 1 HP = 736 Watt, 1 kWh = ...
[Rysunek geometryczny — prostopadłościan z wektorami]
BB'/AB = tgα... tg = α
p = α·K... α = P/R
Wyznaczenie modułu Younga
l cm, s cm², F kg, Δl... A = Δl/l, E = F/σ
n = 1000, V = 80 m/s, h = 2...
g·t... Vt = at, S = gt²/2
S = at²/2, V = at, 80 m/s... g = 981
h = ½ Vt[?]
[Na dole — lista osobista:]
Aparat fotograficzny  / Buty  / Zegarek / Rowerek  / ...pamiątkę dla Gosi
✓
✓
✓
[Prawy górny róg:] Ozdobny rysunek geometryczny — trzy koła wpisane w trójkąt 
odwrócony, gęsto zakreskowane.""",
        "kontekst": "Itinerarium wojenne (awers) + notatki z fizyki (rewers)"
    },

    "juras_204": {
        "typ": "list",
        "data": "",
        "jezyk": "pl",
        "transkrypcja": """CMF 154/12, 5.II.1946 → Krzysztof Głuchowski | 1 kartka, dwustronnie, atrament czarny
Kochany Krzysiu!
Przepraszam Cię za dość długą zwłokę w odpowiedzi na Twój list, a mianowice mi list 
ale właściwie kilka słów. W przyszłości postaram się, iż napiszę obszerniej. W 
pierwszym rzędzie przesyłam Ci adres Januma[Janusza?], o który prosiłeś: R.J. Pol. 
Forc. CMF 460. U mnie stara bieda. Zapewne wiesz od Leszka, że jestem na służbie 
wartowniczej. Pracy nie mam dużo, co traci dzień służba. Wyobraź sobie, że dziś 
otrzymałem list od Jurka i to jest z terenu „Italii"
Nic wiem co mu strzeliło do głowy, żeby wyjechać z Anglii, gdyż w dodatku musi[ał] 
studiować. Piszan[?] aby Ci opisać nasze przeżycia w Niemczech.
Na dnie[?] było przejść i ociało[?] byłoby napisanie[?], aby to wszystko opisać, a Sam 
widzisz na jakich warunkach piszę. Przy najbliższej jeśli[?] okazji podzielimy się 
wrażeniami.
Tymczasem ściskam Cię
Tadek
d. 5/II.46""",
        "kontekst": "List pdo. Tadeusza Bystydżeńskiego"
    },

    "juras_206a": {
        "typ": "list",
        "data": "",
        "jezyk": "pl",
        "transkrypcja": """CMF 125 (5 KDP), 22.I.1946 → Krzysztof Głuchowski | Winieta: choinka na tarczy biało-czerwonej
C.M.F. Polsh Forces 125 — 22/I.46
[Winieta 5. Kresowej Dywizji Piechoty]
Kochany Krzysiu!
U nas wszystko jest takie same, jak było przedtem. Właściwie nie ma żadnych zmian 
chyba to tylko, że jestem więcej zajęty jako wykładowca na kursie motorowym, co 
mnie zupełnie nie bawi, ze względu na to, że już kilka takich kursów odmawiałem[?]. 
Nelli wyjechał i mieszka obecnie nad morzem. Byłem u niego w niedzielę i wybieram 
się znowu. Jest dla mnie b. serdeczny.
[...] Podchorążowie Biglasek[?] i Kossalsk[?] otoczył[?] zapytujem nie to w 7. P. 
Ułanów. [...]
Czy dostam[?] dostałeś uwierzytelnione odpisy tych świadczeń[?], o które mię prosił. 
Zrobiłem to i wysłałem na drugi dzień po Twoim odjezdzie do gimnazjum z pocztą 
służbową.
Ściskam Cię serdecznie
wt swoje Joanna Skrobecki""",
        "kontekst": "List Jana Skrobeckiego (I) — winieta 5 KDP"
    },

    "juras_206b": {
        "typ": "list",
        "data": "",
        "jezyk": "pl",
        "transkrypcja": """CMF (5 KDP), 16.IV.1946 → Krzysztof Głuchowski i Janusz
16/IV 46.
Kochany Krzysztofie!
Bardzo nieswetułem[?] mi[?] decyzji Nowych[?] władz byciu nie wyjeżdżać[?] w czas 
synu[?]. Żałuję że nie mogę dla Was uczynić wszystku[?], ale nie wypada mi wpływ 
bać[?] na władze Pólk[?] by zmienić decyzji w stosunku do Was dwóch[?]. [...]
Mam nadzieję że odwiedzenne mnie później wykorzyst- uje z profuli widzimi[?] na / 
byle nie 28/ü bo mnie nie będzie/. Życzę Wam serdecznie Kochani chłopcy Tobie i 
Januszowi żakoń[?] mielnia[?] i fest Wielkanocnych Świąt, mele szczęścia.
Świąteczni życzeń i pozdrowień. Decyzja Twoja Krzysztofie co do wszystko tych 
wysiłku w nauce podoba mi się. Masz wrodzone zdolności i warto je wykorzystać przy 
zdobywaniu wiedzy.
Ściskam Cię serdecznie jako też Janusza
Skrobecki.""",
        "kontekst": "List Jana Skrobeckiego (II)"
    },

    "juras_207a": {
        "typ": "list",
        "data": "",
        "jezyk": "pl",
        "transkrypcja": """Brownings Camp, Billingshurst, Sussex, 19.IX.1946 → Krzysztof Głuchowski (Bodney) | 2 karty jasnoniebieskie
Brownings Camp / Billingshurst / Sussex / 19.9.1946.
Kochany Panie Krzysiu.
Bardzo mnie ucieszył list Pana i wiadomość że jest Pan już w Anglii, a do tego uczy się,
 
co jest najlepsze z tego co mógłby Pan robić.
Ostatnią wiadomość o Matce Pana miałem od swego syna Marka. Tę ostatnią 
wiadomość przesłał Panu pan Janusz. Oczywiście znaczy to oby[?] poszedł na aptekę w
 
Łodzi. Jeśli Marek to pisał to dlatego /moim zdaniem/ że o napisanie tego prosiła 
Matka Pana.
Pytam Pan czy pisał wprost do Matki i czy podał adres na Bodney.
Na moje wyczucie lepiej pisać do osób w Łodzi — wuja Włodka czy innego członka 
rodziny — oni już bezpiecznie dostarczą Pani Wandzie. Adres musi być Bodney, 
nigdz[ie] nie inny.
Co się dzieje z p. Stefanem — Pana Ojcem — od dłuższego czasu nie mam od niego ani
 
o nim wiadomości. Czy jest nadal w Niemczech, czy zdołał dostać się do Anglii?
Istotnie mało się znamy. Pamiętam Pana jako 10–11 letniego chłopca. Mam wrażenie, 
że jest Pan w wieku mego starszego syna — on jest 1927 rocznik, ale może się mylę.
Bardzo bym chciał poznać Pana bliżej Panie Krzysiu, więc jeśli Pan będzie w Londynie 
w czasie jakiegoś week-endu, proszę mnie zawiadomić, a postaram się z Panem 
skontaktować.
Dziękuję serdecznie za list i proszę o mnie nie zapominać!
Janusz Kamiński""",
        "kontekst": "List Janusza Kamińskiego (I) — konspiracja pocztowa"
    },

    "juras_207b": {
        "typ": "list",
        "data": "",
        "jezyk": "pl",
        "transkrypcja": """Brownings Camp, 28.X.1946 → Krzysztof Głuchowski | 1 kartka jasnoniebieska, dwustronnie
Brownings Camp / Billingshurst / Sussex / 28/10/46.
Kochany Panie Krzysiu.
Marek został aresztowany przez Bezpiekę 9 września i bardzo się z tego powodu 
martwiłem.
Ale dzisiaj dostałem od niego list z 16 paźdz. że znów jest na wolności i udało mu się 
tym razem wykręcić. Nie wiem oczywiście z jakiego powodu i co od niego chcieli.
Jeśli pisze — cześć[?] się znów pewnie. Marek pisze że wiadomości o Panu, /które mu 
posłałem/ przekazał Matce Pana. Niestety nie podaje żadnych dodatkowych 
wiadomości tyle aby Pan pisał jak najczęściej na adres
Pani Staśki, który Pan zapewno ma.
Co u Pana słychać: Jak się Panu powodzi, i jak idzie nauka.
Wiem, że Matka Pana prowadzi aptekę i daje się na wolnej czy Kruczej w 
odrestaurowanym budynku.
Jest Jej podobno ciężko i nie czuje się zbyt bezpieczona w Warszawie.
Kilka tygodni temu p. Janusz z żoną byli w naszym obozie i rozmawialiśmy o Panu.
Serdeczne pozdrowienia Twój i uściski rozsyłam
Janusz Kamiński
Czy ma Pan wiadomości od Ojca. Czy przyjechał[?].""",
        "kontekst": "List Janusza Kamińskiego (II) — aresztowanie Marka"
    },

    "juras_209a": {
        "typ": "list",
        "data": "",
        "jezyk": "pl",
        "transkrypcja": """55 Bolton Gardens, Londyn SW5, 26.XI.1946 → St. Uł. Głuchowski, 25 Bodney Airfield F/105 | Maszynopis
TERENOWE KOŁO B. ŻOŁNIERZY AK
W ANGLII
55, Bolton Gardens
London SW 5
L.dz. 403/Sekr/46
Londyn 26.11.46.
St. Uł. Głuchowski Krzysztof
25, Boaney Airfield
F/105
Thetford — Norfolk
W odpowiedzi na list Kolegi z dnia 20.10.46., zawiadamiam, że przed wstąpieniem do 
Koła b. Żołnierzy AK, należy przeprowadzić weryfikację przebiegu służby, w AK. W 
tym celu proszę zwrócić się do Komisji Weryfikacyjnej II Korpusu — adres:
Polish Camp Wynstay — Park, Ruabon n/Chester.
Po przeprowadzeniu weryfikacji proszę do nas napisać ponownie, wtedy prześlemy 
Koledze deklarację członkowską, statut Koła, oraz wszelkie informacje dot. 
działalności i organizacji Koła.
Z koleżeńskimi pozdrowieniami
Sekretarz
z.u. J. Więckowski""",
        "kontekst": "Pismo Koła b. Żołnierzy AK w Anglii (I)"
    },

    "juras_209b": {
        "typ": "list",
        "data": "",
        "jezyk": "pl",
        "transkrypcja": """Londyn, 7.XII.1946 → Stquł. Głuchowski, 25 Bodney Airfield/F/105 | Maszynopis
Terenowe Koło b. Żołnierzy A.K. w Anglii
L.Dz. 555/Sekr/46
Londyn 7 grudnia 46r.
W poprzedniej swej kartce z dn. 20.X.46 nie podał Kolega żadnych danych o swej 
weryfikacji stąd to nieporozumienie.
W załączeniu przesyłam statut Koła oraz deklarację na członka Koła z prośbą o 
dokładne wypełnienie tej ostatniej o ile Kolega zechce przystąpić do naszego Koła.
Z koleżeńskim pozdrowieniem
Sekretarz z.u. J. Więckowski""",
        "kontekst": "Pismo Koła b. Żołnierzy AK w Anglii (II)"
    },

    "juras_210": {
        "typ": "list",
        "data": "",
        "jezyk": "pl",
        "transkrypcja": """Witley Camp, 30.X.1946 → Krzysztof Głuchowski (Bodney) | 1 kartka, dwustronnie, atrament fioletowy
Witley Camp / 30.10.46.
Drogi Krzysiu!
Z wielką radością dowiedziałem się że jesteś w Anglii. Adres Twój podał mi Krzysz Sz. 
Bardzo ciekawy jestem jak przeszedłeś Powstanie. W jakich obozach byłeś w niewoli, 
gdzie się obracałeś we Włoszech i ostatecznie kiedy przyjechałeś do W. Brytanii. 
Napisz mi co robisz obecnie i jak sobie ułożyłeś tu życie.
Ja podczas Powstania prawie cały czas byłem na Poczcie Dworcowej. Byłem ranny, 
lecz obecnie jestem zupełnie zdrowy. Ze znajomych widuję tu tylko Ciocię Z. Horyńską
 
i Renę B. Odwiedzili mnie[?] w szpitalu. Leżałem na Marszałkowskiej pod 8. Po 
kapitulacji dostałem się przez Lamsdorf do VII Stalagu do Markt-pongau. 12 maja 
oswobodzili nas Amerykanie. Do Włoch przyjechałem w sierpniu 1945 i tam zostałem 
przydzielony do 16 Pomorskiej Brygady Piech. Jedyną osobą jaką spotkałem w II 
Korpusie był Bysiek Żukowski, kolega Lenka. Przyjechał on do Italii prosto z Polski w 
45 roku i wiele mi opowiadał o wszystkich i o stosunkach panujących obecnie w Kraju.
Drogi Krzysiu jeśli byś miał być w Londynie i chciał mnie zobaczyć to daj mi znać. 
Znajduję się obecnie w Witley camp o 40 mil od Londynu. Jest to główne biuro P.K.P.R.
 
Odpisz mi w każdym razie prędko.
Kończę i ściskam Cię mocno
Józek Dynowski""",
        "kontekst": "List Józka Dynowskiego — Poczta Dworcowa"
    },

    "juras_211a": {
        "typ": "list",
        "data": "",
        "jezyk": "pl",
        "transkrypcja": """CMF 153, 9.VIII.1945 (plut. pchor. Krahelski Lech. / Polish Forces. C.M.F. 153. — 9.VIII.45.
Kochany Krzysiu!
U nas wszystko jest takie same, jak było przedtem. Właściwie nie ma żadnych zmian 
chyba to tylko, że jestem więcej zajęty jako wykładowca na kursie motorowym, co 
mnie zupełnie nie bawi, ze względu na to, że już kilka takich kursów odmawiałem[?]. 
Nelli wyjechał i mieszka obecnie nad morzem. Byłem u niego w niedzielę i wybieram 
się znowu. Jest dla mnie b. serdeczny.
Jeśli byś mógł przyjechać na sobotę i niedzielę, jak to zresztą wielu robi, to przyjedź bo
 
tam musi być Ci trochę nudno. U nas też nie ma nic specjalnego ale zawsze coś można 
urządzić.
Przyjechał teraz jeszcze Jurek Mayer niestety nie jest tu. Widuję się z nim co drugi 
dzień, ale on jak tam zupełnie sam[?] i to jest niewesołe.
Napisz mi jak Ci tam leci w szkole i czy wybierasz się na podchorążówkę. Moim 
zdaniem warto.
Marian przesyła Ci pozdrowienia, ja mam nadzieję, że jeszcze do nas napiszesz.
Ściskam
Lesiek""",
        "kontekst": "Air Letter Krahelskiego (I)"
    },

    "juras_211b": {
        "typ": "list",
        "data": "",
        "jezyk": "pl",
        "transkrypcja": """CMF 153 / Poczta Polowa 122, 27.VIII.1945 (stemple 28+31.VIII.45, cenzura 564) → Gimnazjum 3 DSK (klasa IV)
plut. pchor. Krahelski Lech. / Polish Forces, C.M.F. 153. — 27.VIII.45
Kochany Krzysiu!
U nas nic nowego. Jak zwykle stara bieda, nic ciekawego się nie dzieje. Dobrze wiesz 
jak to wszystko wygląda. Czy nie masz możności zdobycia dla mnie tam w szkole 
samouczka języka angielskiego. Jeśli możesz, to mi przyślij. Pozatem mógłbyś nas 
kiedyś odwiedzić, tylko zdaje się za dobrze Ci się tam powodzi i już nie potrzebujesz 
starych kolegów.
„Jelenia" rysuję poniżej, nie mogę Ci przysłać szablonu, bo mam tylko jeden, a 
Nałęcz jeszcze mi mojej Barwy nie oddał. W dalszym ciągu uważam, że to wyjątkowy 
bałen[?].
[RYSUNEK: odręczna sylwetka jelenia z porożem — odznaka 7 P.Uł. Lubelskich]
/powinien być trochę ciemny, ale inaczej nie mogłem dokładnie odrysować, rysuję po 
zewnętrznej stronie linii. L.J./
Mam nadzieję że napiszesz do mnie, bo napewno nowego się coś u Ciebie uzbierało.
Przesyłam pozdrowienie od Mariana, Ciebie ściskam
Lesiek""",
        "kontekst": "Air Letter Krahelskiego (II) — RYSUNEK JELENIA"
    },

    "juras_213a": {
        "typ": "list",
        "data": "",
        "jezyk": "pl",
        "transkrypcja": """High Wycombe, 3.II.1947 → Krzysztof Głuchowski | 1 kartka, dwustronnie, atrament fioletowy
High Wycombe 3.II.47r.
Kochany Krzysiu!
Z wielką radością dowiedziałem się, że żyjesz i jesteś również jak ja na tej „wybornej" 
wyspie. Doniósł mi o tem mój Tatuś, który widział się z Twoją Mamunią w Warszawie i 
która dała mu Twój obecny adres.
Dowiedziałem się również, że zamierzasz wyjechać do Argentyny i Mamusia Twoja 
prosiła, długi[?] tego gd[?]-uprzednia nie wolni[?]: jeśli nie możliwe[?] tutaj warunków 
do nauki wrucać do Kraju.
Bardzo ciekawy jestem gdzie byłeś i co robiłeś podczas tych długich ciężkich lat. Ja od 
września 1939r. do grudnia 1944 byłem na Węgrzech, następnie od grudnia 1944 do 
końca wojny siedziałem w niemieckiej niewoli najpierw pod Wiedniem a poźniej pod 
Berlinem. Uwolniony zostałem nie, rosjan[?] 25 kwietnia 45r. a następnie siedziałem ci
 
do miesiąca[?] w Berlinie /w ros. a poźniej ameryk. Zonie/. W końcu miesiąca[?] 45r. 
wyjechałem do Włoch gdzie początkowo siedziałem pod Taranto — a od grudnia 45r. 
do października u.r. z przerwami wakacyjnymi w Rzymie gdzie studiowałem chemie. 
Od listopada u.r. do dnia dzisiejszy ciężko w chłodniskim[?] obozie niedaleko 
Londynu /2 g. jazdy koleją/ w High Wycombe. [...]
Całuję Cię serdecznie
W. Tudek.""",
        "kontekst": "List W. Tudka (I) — ARGENTYNA"
    },

    "juras_216b": {
        "typ": "list",
        "data": "",
        "jezyk": "pl",
        "transkrypcja": """Coventry, 2.X.1947 → Krzysztof Głuchowski | 4 kartki
Coventry 2.10.47
Kochany Krzysiu!
[...] Ok, że Kosio dostał Stypendium! W przyszłości jak będziecie inżynierami chyba 
weźmiecie prostego Kolegę do pracy — co? [...]
dzisiaj dostałem pierwszą wypłatę /za końce ubiegłego tygodnia/ oto jak wygląda 
rachunek:
44 godz. a 1-11½ ......... 4-6-2
— Insurance /ubezpieczenie/ ... 3s 8d
Hospital .......................... 4d
Income tax /podatki/ .......... 6d[?]
Nett Wages   3.17.1.
Podobnie będzie do grudnia — potem zobaczymy!
[...] Co słychać u Twoich rodziców? U mnie /tzn. u ojca/ wszystko w porządku, chcą 
żebym wracał i obiecują mi grunki na wiosnę w ja jednak otwarcie napisałem [...]
Ściskam Cię
Marian
ARG/V/216-tel — Telegram na 21. urodziny
Keresley → Walthamstow E17, 29.XI.1947 | Formularz GPO, paski teleksowe
KRZYSZTOF GLUCHOWSKI C/O MRS WHITTLE 12
KENILWORTH AVE WALTHAMSTOW LONDON-E 17 =
ZOKAZJI UKONCZENIA 21 LAT SERD UCZNE ZYCZENIA
MARIAN + C
[Stempel: WALTHAMSTOW E17 — 29 NOV 47]
[Nadanie: E D 40 11.50 KERESLEY 19]""",
        "kontekst": "List Mariana (II) — PASEK WYPŁATY"
    },

    "juras_217": {
        "typ": "list",
        "data": "",
        "jezyk": "pl",
        "transkrypcja": """24.IV.1947 → Krzysztof Głuchowski i Janusz | 2 kartki kremowe, atrament niebieski
24.IV.47r.
Kochany i miły Krzysztofku!
Dziękuję Ci za pamięć i miłe liściki, które otrzymaliśmy. Cierzy[?] się bardzo, że 
jesteście razem z Januszem. Cokolwiek Was w ewolucji[?] czasem rozdzieliło — to 
zawsze Tęczę[?] Was będą przejście wspólnie ogółki[?], a najradośniejsze rasy i wierzę
 
Julkę w Wany[?] wierną przyjażni[?] o czem obadwaj wiecie. Cos Was znów złączy 
razem — ustępujcie sobie nawzajem, bo wysiłek jednej strony na nic się nie zda. Dobra
 
wola utrzymania najlepszego stosunku i harmonii musi być obustronna. Zresztą 
wierzę, że będzie Wam z sobą dobrze i trochę rodzinnie.
Miło mi, że bądą się teraz troszyłą i myślatą o Was razem. Napiw Krysieńku miły jak Ci
 
klimat służy? Jaką macie pogodę? Czy są pomarańcze? /To najbardziej interesuje 
Hanię/ Czy stołujecie się u tej Wronki u której mieszkacie? co jadacie na śniad[anie], 
obiady i kol[ację]? Czy macie ubrania, obuwie, pościel, i bieliznę? Ciekawam co Ci 
poradzi mij Janusiu, bo ja na Waszym miejsc kończyłabym liceum — jeśliw są po temu 
warunki.
Czy Ty lub Januszek widział się z gen. Rakowskim [...]
Całuję Cię Krysieńku mocno i serdecznie
„Kochajcie się"
Ciotka Kochana.
ARCHIWUM RODZINY GŁUCHOWSKICH — Transkrypcje korespondencji ARG/V/201–217
Opracowanie: sesja katalogowa 24.III.2026 | Opisy na podstawie analizy wizualnej fotografii""",
        "kontekst": "List Cioci Kochanej"
    },

    # listy_wanda_2.pdf

    "juras_218": {
        "typ": "list",
        "jezyk": "pl",
        "nadawca": "Wanda Głuchowska",
        "transkrypcja": """...napisz, to mu oddam list. Kłodzio jest gdzieś pod Paryżem chodzi na akademię szlak
pięknych, na zapisy literackie. Symusiu napisz mi czy dostałaś pieniądze dałam 50 dolarów
do Szwajcarii, — nie mogę zaszyć obaw co do tego czy ci przesłe ale ciekawa jestem ile
funków to jest i jaką tu ma walutę siłę Kapota. Myślę że w najbliższym czasie będzie ktoś co
ci zawiezie znów list, gdzie mógł wziąć swobodnie odpowiedź, proszę cię tego rynku napisz
mi wszystko dokładnie z jakich funduszów teraz żyjesz i jakie masz możliwości, na
przyszłość. Tylko jedyną napisz też o cioci Hance dlaczego tak jest, jak jest, co robi...""",
        "kontekst": "Fragment listu (brak daty)"
    },

    "juras_219": {
        "typ": "list",
        "jezyk": "pl",
        "nadawca": "Wanda Głuchowska",
        "transkrypcja": """Penley, 9.I.1948.
Panie Krzysztofie!
Przyjechałam niedawno do Anglii, a ponieważ w Polsce bardzo często przebywałam z Jego
rodziną, może Pan zechce zobaczyć się ze mną, aby dowiedzieć się szczegółów.
My znamy się jeszcze z Warszawy. Często przychodziłam do Państwa na Żoliborz, i
przeważnie reperowałam tam Pana garderobę. Obecnie jestem razem z mężem na terenie
trzeciego szpitala wojennego.

Łasijam pozdrowienia
Hanna Flejsner<BRTAG>(Janina Ryszewska)
Przesyłam Panu najserdeczniejsze pozdrowienia oraz (mego późniejsze) życzenia z okazji
Nowego Roku
H. Flejsner""",
        "kontekst": "Penley, 9.I.1948"
    },

    "juras_220": {
        "typ": "list",
        "jezyk": "pl",
        "nadawca": "Wanda Głuchowska",
        "transkrypcja": """SERENA HÔTEL-PENSION, NORRMALMSTORG 4, STOCKHOLM den 23.2. 1947
Wielce szanowny Panie – Pozwalam sobie zwrócić do Sz. Pana z polecenia Pani Wandy, z
którą żyjemy ostatnio bardzo blisko, jako że jest ona najbliższą znajomą mojej najlepszej
przyjaciół Stefanów Jezierskich. Pani Wanda odwanyła Imienne temu Aptekę na rogu
Kruczej [...] w zburzonym domu, z którego zostały tylko mury. [...] wybudowała sobie pani
Wanda antresolę [...] „bocianie gniazdo" gdzie mieszka [...] Jedyną jej największą troską to
brak wiadomości o synu [...]
prosiła mnie abym napisała do Pana [...] Jak jej chłopiec się wodzi, czego żyje, czy ją tczy [...]
jakie jego plany na przyszłość i czy radzi ją z Panem, jako jego najbliższym opiekunem. [...]
Pozatem miałam Państwu jeszcze podać krótko wiadomość o panu Stanisławie Bukowskim,
który rok temu zdali zarekwirowany [...]
Maria Grafowa.""",
        "kontekst": "Sztokholm, 23.II.1947"
    },

    "juras_221": {
        "typ": "list",
        "jezyk": "pl",
        "nadawca": "Wanda Głuchowska",
        "transkrypcja": """Jerzy Graff<BRTAG>Londyn 26/4 47<BRTAG>27, Crespigny Rd. N.W.4<BRTAG>tel.
Hendon 2725
Szanowny Panie,
Z polecenia Pani Wandy Głuchowskiej przywiozłem paczkę dla p. Krzysztofa Głuchowskiego.
Ponieważ nie posiadam numeru telefonu Sz. Pana, uprzejmie proszę o skomunikowanie się
ze mną telefonicznie każdego dnia do godz 9³⁰ rano, lub o godz. 7 wieczorem.
Zaznaczam że pozostanę w Londynie ok. 1 tygodnia. –

Z poważaniem<BRTAG>[podpis]""",
        "kontekst": "Londyn, 26.IV.1947"
    },

    "juras_222": {
        "typ": "list",
        "jezyk": "pl",
        "nadawca": "Wanda Głuchowska",
        "transkrypcja": """Synku Malutki!
Dostałam 
dwa 
Twoje 
listy, 
dzień 
po 
dniu.<BRTAG>Odpiszę 
w 
najbliższych
dniach<BRTAG>a dziś do serca Cię tulę
Wawa""",
        "kontekst": "Liścik (brak daty)"
    },

    "juras_223": {
        "typ": "list",
        "jezyk": "pl",
        "nadawca": "Wanda Głuchowska",
        "transkrypcja": """Młody Głuchowski<BRTAG>wizje p. Janowy dn. 20/- 47.
Synku Kochany!
Tak czekam na wiadomości od Ciebie. Pisz koniecznie na adres paryski. U nas bez zmian.
Czy dostałeś przesyłkę? Ściskam Was wszystkich b. b. serdecznie [...] ja dobrze do ucałuj.
Wawa
[Na 
odwrocie 
adres:]<BRTAG>Krzysztof 
Głuchowski<BRTAG>25 
Bodney 
Airfield
P/105<BRTAG>Thetford – Norfolk""",
        "kontekst": "ok. 20.-.1947"
    },

    "juras_224": {
        "typ": "list",
        "jezyk": "pl",
        "nadawca": "Wanda Głuchowska",
        "transkrypcja": """W-wa 13.I.1947 r.
Synisku Mój Malutki!
Dostałam list od Sofki [...] chcę ci wysłać trochę zdjęć [...] Tak czekam listu od Ciebie,
synku. – Ja na okres wiatreczny wyjechałam z W-wy [...] z Wandą S. [...] Na Żoliborzu [...]
zjechało aż 5-iu panów – Szumark, Patek, 3 panów Korbolskich. [...] Paniunk upadł i złamał
obie ręki i pękła aż w 4-ech miejscach. [...]
U mnie na mojej antresoli coraz przyjemniej [...] Mamy tu już dwa spania, stolik okrągły, 2
kresła, lustro, dywanik a ostatnio [...] radio i dwie śliczne przysułki. [...]
Wawa""",
        "kontekst": "Warszawa, 13.I.1947"
    },

    "juras_225": {
        "typ": "list",
        "jezyk": "pl",
        "nadawca": "Wanda Głuchowska",
        "transkrypcja": """W. 19.XII.46 r.
Kochany Synu!
[...] wybieram się do Marysi R. do Leśniarówki i następnie do Wrocławia i do Łodzi – jadę
razem z Wandą S. [...]
Krysiuku jeśli Malek nie wróci do żony to staraj się go skomunikować z Bronkiem [...]
Przecie byli w wielkiej przyjaźni. [...]
Synecku malutki! Takin bardzo ciekawa czy paczki doszły do Ciebie [...] przesłam Ci
kalendarzyk żeby mu posłał tylko Krysiuku nalep, bo mi kleja zabrakło [...] jeśli będzie się do

Ciebie wracać ktokolwiek z rodziny Klendjana to możesz mieć do nich zaufanie i nie unikaj
kontaktu z nimi.
Ściskam mocno, mocno Twoja matka""",
        "kontekst": "Warszawa, 19.XII.1946"
    },

    "juras_226": {
        "typ": "list",
        "jezyk": "pl",
        "nadawca": "Wanda Głuchowska",
        "transkrypcja": """Krysieku Kochany! Zrobiłam aż już taka prawdziwa histeryczka, wprost z apteki nie chce mi
się wychodzić, bo zdaje mi się że właśnie jak wyjdę list od Ciebie przyjdzie. – Tak Synecku
jesteś jedyną wygraną pozycją w moim życiu i to wygraną podwójnie, bo po pierwne to że
wogóle istniejesz, a po drugie że powstanie czy inne katastrofy nie zabrało mi Ciebie. [...]
Kocham Cię Malutki i tęsknię za Tobą. A jak pomyślę sobie że świat tak prachtonie i już do
mnie nie wróci to obraca mi się krojc. [...] Wczoraj spotkałam P. Hygrosierorcz z jednym z
synistki pod rękę i wiec Synecku wprost fizycznie poczułam zazdrość [...]
W. 9/III 47r. Wawa""",
        "kontekst": "Warszawa, 9.III.1947"
    },

    "juras_227": {
        "typ": "list",
        "jezyk": "pl",
        "nadawca": "Wanda Głuchowska",
        "transkrypcja": """W-wa 10/II -47
Synku Kochany! List Twój z 19-go dostałam. Malutki pisz do mnie częściej. U nas bez zmian.
– straszne mrozy. [...] Czy dostałeś moskotki wysłane lotem przez Szwedów było ich
kilkanaście?
Wawa
---
Krysieku Kochany! [...] koło Norfolk góra Londonu się ukazała – że ciągle się martwię czy Ci
tam nie jest zimno. – U nas wielkie mrozy, ale węgla jest dość [...] pojechałam do Łozi to
przez dwa dni apteka była zamknięta, bo ja nie mogłam wrócić bo pociągi i autobusy nie
mog [...] Posyłam Ci znaczki [...] Wszystkie zdjęcia robione na ślubie Adasia [...] Adaś
obecnie jest nadleśniczym w Ostromecku koło Torunia. – Synecku moly pisz i nie jedź do
Argentyny [...]
Wawa""",
        "kontekst": "Warszawa, 10.II.1947 + list bez daty"
    },

    "juras_228": {
        "typ": "list",
        "jezyk": "pl",
        "nadawca": "Wanda Głuchowska",
        "transkrypcja": """Synku Kochany! Pytam czy dostałam list z 16.I. Otóż Synku listów od Ciebie dostałam pięć z
22.X.46r. z 25.XI.46r. 19.I.47. 5.II.23.I [...] Czytam je tam jakie raz myślce i będę Ci chciała
odpowiedzieć na wszystkie zasadne w nich pytania. –
[O zdjęciach:] zdjęć się naliniarlo, bo istrawda było ine darzio, bo przecień oprócz naszych
była cała skrzynia fotografji Stanki, ale synecku się w tak opłakanym stanie [...] Dach był
przecie zerwany, więc przez kilka miesięcy woda zalewała wszystko.
[O kolegach:] Jakoś synecku do tej pory nie zdosarann się nie dowiedzieć [...]
[O lekarstwach:] Żusofnylisin proszek [...] wyślij na adres Stawki Żwirki 1 d. mieszkania 12 –
Łódź.
[O domu na Żoliborzu:] Jak widzisz na zdjęciu dom stoi, ale [...] Dach został zerwany a desci
i śnieg [...] Ciotka Halenkę w okresie kiedy ja jeszcze byłam w więzieniu (7 miesięcy) zrobiła
umowę [...]
[O meblach:] Fotel mahoniowy, sofecka mahoniowe [...] Twoja Biblioteka [...] ani porcelany,
ani garderoi ani recy osobistych nie się nie uralowało [...]
Przyjaźnicn Twoja jest [...] Warszawa 5.VI.42

Wawa W. 19/II 47r.""",
        "kontekst": "Warszawa, 19.II.1947"
    },

    "juras_229": {
        "typ": "list",
        "jezyk": "pl",
        "nadawca": "Wanda Głuchowska",
        "transkrypcja": """W. 18/III.47r.
Syneku Kochany! Dziś w dziś B.B.C. mówi o tych którzy nie zapisali się do Korpsu
przysposobienia lub nie wracają do Kraju [...] właśnie nie rozumiem co z Tobą. Właściwie co
skłania Cię do tego żeby jechać [...] w tak daleki świat. [...]
proszę Cię ureguluj swoje sprawy w naszej placówce [...] metryki twoje [...] więc koniecznie
ureguluj te sprawy. –
[O pieniądzach:] na wszystkie strony kombinuję jakby tu zrobić żeby [...] przesłać Ci trochę
gotówki. [...]
[O towarach na sprzedaż:] krawaty z prawdziwego milanowskiego jedwabiu [...] szaliki i
chusteczki [...] kapcie 3½ m. [...] O bardzo pięknym wronie, ręczenie malowanym [...]
Pororum się w tej sprawie z Kłodkiem on ma rodzinę w Anglji [...]
[O Stefku:] Pisałeś Synku że Stefek zdecydował się wracać, ja myślę że pewnie dobrze robi
[...] los tych wszystkich wymigrców to jest lepiej być z nami. –
Tulę Cię Synku do serca i mocno całuję Wawa""",
        "kontekst": "Warszawa, 18.III.1947"
    },

    "juras_230": {
        "typ": "list",
        "jezyk": "pl",
        "nadawca": "Wanda Głuchowska",
        "transkrypcja": """Synku! Jesteś już dorosłym mężczyzną a ja ciągle nie mogę się z tym pogodzić [...] Pisałeś mi
że nie zakochałeś się jeszcze, oczywiście jak wszystkie matki i ja chciałabym jak najdalej ten
moment odsunąć [...]
Synecku piszen że korespondujez z czterema Dziewczynkami – napisz mi jakie i kto one [...]
Wczoraj byłam w teatrze i tam spotkałam pp. Piałkow i Violett. Violett straciła matkę a dom
ich dostał zepsutie rozbity [...]
Na Skaryszce powoleli zaczynają się ekshumacje [...]
[...] Krysieku apteka natomiast jest b. b. przyjemna, jasna i zupełnie estetyceme, i b. ją lubię
[...]
[...] antresola jest b. przyjemna i jest mi tu b. dobrze [...]
[O planach syna:] jeśli chodziostujo wyzen [...] raczej studiował w Anglji [...] ale jeśli ta
Argutyna to mi zupełnie mi odpowiacle [...]
19.IV.47r. [...] Posyłam Ci 2 chusteczki. Jest to czysty jedwab. Milanówek – ręczne
malowanie. Cena 1 sztuki 400 zł [...]

Wawa""",
        "kontekst": "Warszawa (wielostronicowy, bez jednolitej"
    },

    "juras_231": {
        "typ": "list",
        "jezyk": "pl",
        "nadawca": "Wanda Głuchowska",
        "transkrypcja": """W. 30/III 47r.
Kochany Synku! [...] Jeśli Ci napisałam że nie przedstawiam tych wartości jakie
przedstawiają inne matki, to dlatego że tych wartości istholie nie mami [...] nie Ciebie, a
siebie winię. – [...] a że nie jesteśmy razem toć tylko losowi urgan. [...]
Dzięki Bogu że skończyła się zima. [...]
[O poszukiwaniu syna po wojnie:] Jakiś rok temu był na Żoliborzu jakiś chłopiec [...] i
opowiadał że [...] byłeś bardzo zdepresjonowany. – To pewno był okres francuski. – [...]
dopiero [...] spotkałam jedną panią która była sekretarką w Grenobli i zapowniła mnie że [...]
pisała listy uczniów do Gimnazjum i że Twoje nazwisko tam było. To był pierwszy ślad że
żyjesz. –
Krysieku patrzę na wszystkie posiadane fotografie Twoje [...] masz b. smutny wyraz twarzy –
martui mnie to bardzo [...]
[O kontaktach:] posyłam ci adres p. Kirkora [...] który jakoby decyduje o [...] stypudiojach
[...] p. Bronisław Chrerpińskiego, on jest przecier prezesem związku Polaków [...]
Wawa""",
        "kontekst": "Warszawa, 30.III.1947"
    },

    "juras_232": {
        "typ": "list",
        "jezyk": "pl",
        "nadawca": "Wanda Głuchowska",
        "transkrypcja": """Drogi Kochany Synku!
Święta się zbliżają i znów jesteśmy daleko od Siebie. [...] znów tylko w pośpiechu [...] Mocno
mocno całuję Cię i tulę do sana i życzę Ci Wesołych Świąt
Wawa
W 31/III 47r.
---
Bardzo chciałabym widzieć dokładnie kiedy ojciec kupuje i jaką drogą [...] Dobraby było
żeby Stefek [...] Mocno całuję Wawa.""",
        "kontekst": "Życzenia wielkanocne, 31.III.1947 +"
    },

    "juras_233": {
        "typ": "list",
        "jezyk": "pl",
        "nadawca": "Wanda Głuchowska",
        "transkrypcja": """Warszawa, 4/IV.47r.
Najdroższe moje Dziecko.
Wielki Piątek [...] Stanelka z całą rotyji pojechała wczoraj do Kożnicy, bo doktor Hance
zalecił koniecznie wyjazd na 2 miesiące. [...]
Józek już pojechał, był kilka dni w Warinwie, ale [...] wybrał sobie w niedzielę ugotowało bię
zupi z pomilorów z panki amerykańskiej, tak że [...] pradie prytomnośó Trocii [...]
Ostatnio jest konserwatorem rynku w Kazimierzu z ramienia ministerstwa [...] Możliwe że
dostanie pozwolenie na wysyłkę swoich medali [...] I „Majdanek" II „Bolesław Chrobry" i III
– plakietka [...] robione jeszcze w okresie okupacji niemieckiej.
Maznie porsiałam Ci baraneczka. [...]
Wawa""",
        "kontekst": "Warszawa, 4.IV.1947"
    },

    "juras_234": {
        "typ": "list",
        "jezyk": "pl",
        "nadawca": "Wanda Głuchowska",
        "transkrypcja": """Łódź 8.IV.47r.
Najdroższe moje Krysiulko!
A więc na święta zjechałam do Łodzi. [...] Cały dzień spędziliśmy w domu. [...] był i baranek i
babki i wiśodek [...] Tylko nas była taka mała garstka [...]
Włodeczek miał co oglądać [medale Józka] – Bardzo mu się podobały [...] Włodek jest w
wielkiej przyjaźni numizmatycznej z dyrektorem mennicy p. Toleckim [...]
Włodek b. jest przygnębiony tą chorobą Ludki [...] położenie jest beznadziejne [...]
Na moji dzień Ewa zrobiła mi wielką przyjemność [...] przygotowała wannę gorącej wody i
wykąpałam się [...]
9/IV. Dziś raciuko przyjechałam autobusem do Warszawy [...] pojechać na Powązki, koło dris
imieniny Babci. – [...] z myślą o Tobie postawiłam niebieską cynerarię [...]
Wawa.
Synku jakie Ty marki zbierasz, czy tylko stemplowane, czy też mogę być i niestemplowane?
–""",
        "kontekst": "Łódź, 8-9.IV.1947"
    },

    "juras_235": {
        "typ": "list",
        "jezyk": "pl",
        "nadawca": "Wanda Głuchowska",
        "transkrypcja": """W-wa 11/IV 1947r.
Synku Mój Malutki!
Zbliżają się Twoje imieniny, życzę Ci więc dziecisko jaknajwięcej jasnych i promiennych
chwil w życiu i do serca Cię tulę. [...]
Ten przedświąteczny okres, kiedy dostałam kilka listów jeden po drugim był dla mnie b.
regiśtiwy [...] Synecku a już najwięcej – Dziękuję Ci za ten list z Niemiec. [...]
12/IV [...] Pierone wiadomości dotarły do minie dopiero jesienią – był to list od Stefka
wysłany przez jakiegoś powracającego oficera.
13/IV Dowiedziałam się że żyjesz. [...]
Wawa
Czy masz jakiś adres w Londynie gdzie mogna by coś przesłać, może Cioci Marysi? [...]
Operacja jej [...] była miesiąc temu, ale [...] do tej pory jeszcze jest chora.
Wawa""",
        "kontekst": "Warszawa, 11-13.IV.1947"
    },

    "juras_236": {
        "typ": "list",
        "jezyk": "pl",
        "nadawca": "Wanda Głuchowska",
        "transkrypcja": """W. 15.IV.47r.
Synku Drogi!
Wczoraj dostałam Twój list z Longbridge [...] Bardzo ucieszyłam się nim [...]
[O pieniądzach:] ja napewno będę Ci mogła jakoś przekazać trochę groszy [...] przeciętne
stypendium wynosi do funtów miesięcznie [...] jest tu naprzykład jedna starsza Pani której
wnuk chce przesyłać 10 funtów miesięcznie [...]
[...] bardzo chciała żebyś nawiązał kontakt z p. Bronisławem Chełerpińskim [...] albo Janusz
Rowiński [...]
O Synku mój dzięki Bogu że ta Argentyna nie jest taką uko dwoalnicj bo tak mnie to
przerażało –
[...] Krysieniujalt imieninowy upominek mam dla Ciebie aparat fotograficzny. – [...] Jest to
niemiecki. Włodek go kupował i uwara go za dobry. Nie jest Leika ale w tym typie. [...]
Wysłałam [...] trochę pisanek [...]
Wawa""",
        "kontekst": "Warszawa, 15.IV.1947"
    },

    "juras_237": {
        "typ": "list",
        "jezyk": "pl",
        "nadawca": "Wanda Głuchowska",
        "transkrypcja": """W. 16.IV.47r.
Krysieku Synecku Mój!
U nas jest w cołej pełni wiosna, bardzo ciepło się zrobiło. [...] kto wejdzie do apteki to [...]
Wszyscy się dopytują o Was obydwuch – kiedy wracacie. –
[...] Stefan Keropiński [...] opowiadał mi o sonier Zygmuncie. Niestety biedaczysko jest
chory i siedzi w Salatoriun na Dolnym Śląsku [...]
[...] Tadeun Buranowski jest w Londynie – p. Zagiełkowski jest również w Londynie. [...]
Boranowska Hala zginęła w pociągu [...] z Pruszkowa do obozów, podczas nalotu
aljanckiego. –
[...] Zaczynam żyć pod wrażeniem ewenalnego powrotu ojca [...] Mam już [...] 3 tomy
„Popiołów" [...] oddałam do reperacji koparai ten na którym sypiał ojciec jeszcze w
barakach. [...]
Synecku a dla Ciebie – mam [...] śliczne plumeau [...]
Dostałam dziś nacanki od Janeczki [...]""",
        "kontekst": "Warszawa, 16.IV.1947"
    },

    "juras_238": {
        "typ": "list",
        "jezyk": "pl",
        "nadawca": "Wanda Głuchowska",
        "transkrypcja": """W. 17.IV – 47r.
Krychu Kochany!
Dziś dostałam pierwszy list przesłany normalną pocztą od ojca. Pisze mi że ma zamiar w
końce kwietnia wrócić do Kraju. [...] sprawa pełnomocnictwa od ciotki na dom [...] ojciec w
liście pyta jakie artykuły aptekarskie są w Kraju potrzebne [...] przesyłam Tobie dzieciako
spis, a Ty bądź tak dobry i prześlij ojcu. –
[...] przesyłam zdjęcie dziadka z ojcem [...] robione w listopadzie 1944 w Krakowie. [...]
Wawa
SPIS LEKARSTW (45 pozycji):<BRTAG>1) Campolon 2 i 5, 2) Testoviron 10 mg i 25 mg, 3)
Cortison 10 mg, 4) Cibasol tabl., 5) Lacarnol amp., 6) Pyramidon pulv., 7) Eshetonin tabl., 8)
Euphyllin ampułki i pulv., 9) Tonophosphan „forte", 10) Pilocarpin pulv., 11) Papaverin
pulv., 12) Pereninyl „forte", 13) Proluton 20 mg 5 mg, 14) Felamin, 15) Iminol, 16)
Bronchisan, 17) Calcium Sandoz, 18) Jod-Calcium-Diuretin, 19) Calcium Diuretin, 20)
Diacolin pulv. i tabl., 21) Adalin tabl., 22) Butolate, 23) Hegeminal, 24) Coramin amp 5 cc i
pryguel, 25) Cardianol pulv., 26) Cebion 5 i 2 amp., 27) Progynon 10 i 50 tys. jednostek, 28)
Dolantin amp., 29) Eldoform, 30) Euflawin, 31) Ewin tabl. i amp., 32) Yatren Casein, 33)
Carostidin, 34) Lutren 5 mg amp., 35) Noralgin amp/tabl./pulv./eliksir, 36) Paralin amp., 37)
Sympatol liq., 38) Thyreoidee tabl., 39) Thyroxin, 40) Validol, 41) Vogin""",
        "kontekst": "Warszawa, 17.IV.1947"
    },

    # ═══════════════════════════════════════════════════════════════
    # SERIA II — Gen. dyw. Janusz Julian Głuchowski (1888–1964)
    # ═══════════════════════════════════════════════════════════════

    # ═══════════════════════════════════════════════════════════════
    # SERIA V — Priorytet 2: Korespondencja jeniecka / wojenna
    # ═══════════════════════════════════════════════════════════════

    # ARG/V/13 — List Krzysztofa z obozu — nr 141009
    "juras_013": {
        "typ": "List z obozu jenieckiego",
        "data": "21.X.1944",
        "jezyk": "polski",
        "nadawca": "Krzysztof Głuchowski (nr 141009)",
        "adresat": "Ojciec (Stefan Głuchowski)",
        "strony": ["Seria_29z_p03_img02.jpeg"],
        "transkrypcja": """Kochany Tatusiu! Wyjechałem z [nieczytelne]
podróż podobnie do Westfalii. Myślę
że panno[?] tu niedługo [nieczytelne] pomieszczeni[?]
Głód jest[?] [nieczytelne] jedzenie napływa[?]. Od [nieczytelne]
dostałem tylko [?] kaszę. Mój numer jest
141009 (jest dotąd XIB) Plany do Francji
w kilku egzemplarzach myśl[?] [nieczytelne]
dopiero[?]. Całej Victorii b[ardzo?] [nieczytelne]
i myślę że nie niedługo[?]
21.X.44. [nieczytelne]
[nieczytelne] p. Ratkowsk[iego?]
i ojcowi z 7 p.uł. [?]

Trzymamy się do końca!""",
        "pieczecie": [],
        "podpisy": [],
        "osoby": ["Krzysztof Głuchowski (nr jeniecki 141009)", "Stefan Głuchowski (adresat — ojciec)", "p. Ratkowski[?] (wspomniany)"],
        "znaki_szczegolne": [
            "NR JENIECKI 141009 — potwierdza numer z innych dokumentów",
            "Stalag XI B — obóz w Fallingbostel",
            "Data 21.X.1944 — 3 tygodnie po kapitulacji Starówki",
            "'Trzymamy się do końca!' — 18-letni jeniec",
            "Pismo ołówkowe na kartonie, stan średni — trudne do odczytu",
            "Wspomina plany do Francji — ewakuacja?",
            "Głód w obozie — 'dostałem tylko kaszę'"
        ],
        "kontekst": "Pierwszy list Krzysztofa z obozu jenieckiego Stalag XI B (Fallingbostel), datowany 21.X.1944 — zaledwie 3 tygodnie po kapitulacji Starówki. 18-letni jeniec nr 141009 pisze do ojca (też jeniec, nr 01245). Pismo ołówkowe na kartonie, bardzo trudne do odczytu. Kończy heroicznym 'Trzymamy się do końca!'"
    },

    # ARG/V/16 — List z obozu do stryja generała — 19.X.1944
    "juras_016": {
        "typ": "Formularz Kriegsgefangenenlager",
        "data": "19.X.1944",
        "jezyk": "polski / niemiecki",
        "nadawca": "St.uł. Krzysztof Głuchowski (nr 141009, M.-Stammlager XI B)",
        "adresat": "General Janusz Głuchowski, London, Polish War's Office, ENGLAND",
        "strony": ["Seria_29z_p06_img01.jpeg"],
        "transkrypcja": """Kriegsgefangenenlager                  Datum 19 - X - 1944

Kochany Stryju i Cioci! Jesteśmy dumni[?] wciąż w obie[?]
w obozie[?]. Niestety nie mam  Od Babci (Hotel[?] Wanda[?] i W[nieczytelne])
który[a?] był[a?] na Żoliborzu ostatni[e] wiadomości dostałem dnia 24/IX[?]. Dwunastu[?]
porobiton[?] się po Kapit[ulacji?] łekcji[?] gdzie zabrano aby dowieźli[?] nas [do?]
[nieczytelne] Stryj Lech poległ 15-tego [na] Mokotowie. [ZAKREŚLONE/OCENZUROWANE] Będziemy żyć[?]
[nieczytelne] Pacho[?] prosi Stryja i Ciocię[?] [nieczytelne]
i [nieczytelne] łagier — paczki. Całuję bardzo kocham mocno Krzysztof""",
        "pieczecie": ["Stempel PASSED XII (cenzura brytyjska)"],
        "podpisy": ["Krzysztof"],
        "osoby": [
            "Krzysztof Głuchowski (nadawca, jeniec nr 141009)",
            "Gen. Janusz Głuchowski (adresat — stryj w Londynie)",
            "Ciocia (żona gen. Janusza)",
            "Babcia (Hotel[?], Żoliborz)",
            "Rtm. Lech Głuchowski — POLEGŁ 15-tego na Mokotowie!"
        ],
        "znaki_szczegolne": [
            "KLUCZOWY DOKUMENT — pierwsza wzmianka o ŚMIERCI LECHA: 'Stryj Lech poległ 15-tego Mokotowie'",
            "Potwierdza datę śmierci Lecha: 15.IX.1944 na Mokotowie",
            "Krzysztof pisze DO STRYJA generała w Londynie — potwierdza relację rodzinną",
            "Babcia na Żoliborzu — nieznany dotąd szczegół genealogiczny",
            "Fragment OCENZUROWANY (zakreślony czarnym) — informacja wojskowa?",
            "Formularz Kriegsgefangenenlager z datą ręczną 19.X.1944",
            "Stempel PASSED XII — cenzura brytyjska po stronie odbiorcy",
            "Trójjęzyczny: formularz niem., adres ang., treść pol."
        ],
        "kontekst": "List z obozu jenieckiego do gen. Janusza Głuchowskiego w Londynie, 19.X.1944. NAJWAŻNIEJSZY DOKUMENT JENIECKI W KOLEKCJI — zawiera pierwszą wiadomość o śmierci rtm. Lecha Głuchowskiego na Mokotowie 15.IX.1944. Krzysztof nazywa Janusza 'Stryjem' — potwierdza relację bratanek-stryj. Wspomina babcię na Żoliborzu. Fragment ocenzurowany przez obóz (informacja wojskowa?)."
    },

    # ARG/V/18 — List do ojca Stefana z obozu — 'Kochany Tatuśku!', XI.1944
    "juras_018": {
        "typ": "List jeniecki dwustronny na formularzu",
        "data": "XI.1944",
        "jezyk": "polski",
        "nadawca": "Krzysztof Głuchowski (jeniec)",
        "adresat": "Ppor. Stefan Głuchowski (jeniec nr 01245, Stalag XI B Bergen)",
        "strony": ["Seria_29z_p08_img01.jpeg"],
        "transkrypcja": """Kochany Tatuśku! Jest mi[?] już rad[?] dla tu czemu[?]
[za?] dawać[?] [?] tu duże[?]. Mamy [?] [?] i [?]
dolar już[?] ajenci i[?] zamojo[?] rata
dom opr[?] ajent[?] ma czat[?] [nieczytelne] Ojciem
jak o ojce[?] opiekł[?] ogród[?] [nieczytelne] Bydło[?]
jest o opl[?] [?] około[?] czy[?] [do] doplat-
[?] jest [?] tak[?] 25[?] centy[?] pokań(?) co wielk [nieczytelne]
12 jest roje[?] po opis[?] daleki[?] Mimy[?] kto[?]
[nieczytelne dalszy tekst — pismo bardzo gęste, ołówkowe, częściowo zatarte]

[...] i dużo[?]. Coś[?] o rodzonej[?] byli[?]
siłą[?] nie naszej[?] fajnie[?] do czeka[?] głód[?] na
nas[?] nagminy[?] na potrzeba[?] przez tu na
razów[?] [nieczytelne]
[...] w Polskę[?] o Bożena[?] Upadała[?] dal[?] dłu[?]g

[...] a[?] my mirzio[?] do domu naprzód[?] a potem w
ile[?] medyczni[?] na do pewnie[?] lub Obóz jest[?]
[?] i dobrze[?]. Najmariam[?] daleka[?] ale[?] [nieczytelne]
reszta[?] książkę[?] Bazylko[?]. Siren[?] w osobowi[?] całych[?]
I[?] Iren[?] badanie[?] [do?] pomiaru[?] Sluszny[?] [?] i każdej[?]
w Mon[?] Teren[?] dawno[?] wto[?] nim radziwiłł(?)n[?]
kiedyś[?] Poli Maryśko[?] główko[?] adres[?] Krustofd[?] [nieczytelne]""",
        "pieczecie": ["Détachez le long du pointillé / Hier abtrennen! (nadruk formularza)"],
        "podpisy": [],
        "osoby": ["Krzysztof Głuchowski (nadawca)", "Stefan Głuchowski (adresat — ojciec, jeniec nr 01245)"],
        "znaki_szczegolne": [
            "'Kochany Tatuśku!' — 18-letni syn pisze do ojca w innym obozie",
            "Pismo ołówkowe BARDZO gęste, częściowo zatarte — wymaga profesjonalnego HTR",
            "Formularz z linią odcinania (niem./franc.)",
            "Rozłożony list dwustronny, format ok. A4",
            "Wiele fragmentów nieczytelnych — stan średni",
            "Koperta: ARG/V/19"
        ],
        "kontekst": "List syn→ojciec między obozami jenieckimi (XI.1944). Krzysztof (18 lat) pisze do Stefana (jeniec nr 01245, Stalag XI B Bergen). Pismo ołówkowe, niezwykle gęste — transkrypcja wysoce niepewna. Wymaga profesjonalnego narzędzia HTR (Transkribus). Koperta zachowana osobno (ARG/V/19)."
    },

    # ARG/V/19 — Koperta Kriegsgefangenenpost — Krzysztof do Stefana
    "juras_019": {
        "typ": "Koperta-formularz Kriegsgefangenenpost",
        "data": "7.XI.1944",
        "jezyk": "niemiecki / francuski",
        "nadawca": "Krzysztof Głuchowski (jeniec)",
        "adresat": "Ppor. Stefan Głuchowski (nr 01245, Stalag XI B, Bergen)",
        "strony": ["Seria_29z_p08_img02.jpeg"],
        "transkrypcja": """[STRONA ADRESOWA:]
Kriegsgefangenenpost
Correspondance des prisonnier de guerre

An: ppor. Stefan Głuchow[ski]
Gefangenennummer: 01245
Empfangsort: Stalag XI B
Straße: Bergen

[Stempel okrągły:] -7.11.44 -6N
[Stempel prostokątny:] 27 Geprüft [cenzura]

Besetztes Gebiet | Südfrankreich
Territoire occupé | France méridionale
Nichtzutreffendes streichen / Biffer les mentions inutiles

Gebührenfrei! Franc de port!

[STRONA NADAWCY — odwrócona:]
Deutschland (Allemagne)
Lager-Bezeichnung: [nieczytelne]
Gefangenennummer: [nr Krzysztofa]
Vor- und Zuname: [Głuchowski Krzysztof]
Absender:

M. St.""",
        "pieczecie": ["27 Geprüft (cenzura obozowa)", "Datownik okrągły 7.11.44"],
        "podpisy": [],
        "osoby": ["Krzysztof Głuchowski (nadawca)", "Ppor. Stefan Głuchowski (adresat, nr 01245)"],
        "znaki_szczegolne": [
            "KOPERTA JENIECA DO JENIECA — syn do ojca w tym samym Stalagu!",
            "Stefan = ppor. (porucznik) — potwierdza stopień oficerski",
            "Numer jeniecki Stefana: 01245 — niski numer = wcześniej wzięty do niewoli",
            "Stempel 27 Geprüft = cenzor nr 27",
            "Datownik 7.XI.1944 — dopełnia list ARG/V/18",
            "Dwujęzyczny formularz niem./franc.",
            "M. St. — Mannschafts-Stammlager?"
        ],
        "kontekst": "Koperta jenieckiego listu Krzysztofa do ojca Stefana (ARG/V/18). Obaj w Stalagu XI B, ale Stefan w podlagierze Bergen (nr 01245), Krzysztof pod innym numerem (141009). Stempel cenzury 27 Geprüft i datownik 7.XI.1944. Formularz dwujęzyczny (niem./franc.) z nadrukiem 'Besetztes Gebiet/Territoire occupé'."
    },

    # ARG/V/38 — List Krzysztofa z Hilden bei Düsseldorf — wieści o Stryju w Edynburgu
    "juras_038": {
        "typ": "List odręczny",
        "data": "2.VI.1945",
        "jezyk": "polski",
        "nadawca": "Krzysztof Głuchowski",
        "adresat": "Rodzina / Ciotka",
        "strony": ["Seria_29z_p19_img01.jpeg"],
        "transkrypcja": """[przekreślone:] Czysz[?] w Ilangu[?] ja tu  [?]
1.II '45 ustała[?] [nieczytelne] strzelano[?] godne[?] wszystk[ie?] na Śląch[?].
Dostanie się do apteki, a w jej prawi[e]
[nieczytelne] [nieczytelne] [zniszczenie?]
[nieczytelne] Jest tutaj w Hilden pod
Düsseldorf[em] Phon[?] [?] i w[?] ustalano[?]-
tam i dowiedziałem się od Niego że Stryj
jest w Edynburgu. Pań[?] podpatkowanie[?]
ma[?] w najbliższ[ym?] [nieczytelne] przegrupowani[e?]
obóz o polskich Janów w[spółpracuj?ą?]cych do [kraju?]
go mamy zwol[nieni?] z pułtania[?] pytanie co będzii[e?]
dalej nie wiem. O Ojcu obecnie nic nie wi[em].
Chrystus[ie?] [jak?] jak najszybciej zobaczyli z
Ciotką[?] co Stryjan[?] Narzeczy[?] Całuję mocno

2/VI '45

Krzysztof""",
        "pieczecie": [],
        "podpisy": ["Krzysztof"],
        "osoby": [
            "Krzysztof Głuchowski (nadawca)",
            "Gen. Janusz Głuchowski ('Stryj jest w Edynburgu')",
            "Stefan Głuchowski ('O Ojcu obecnie nic nie wiem')",
            "Ciotka (adresatka?)"
        ],
        "znaki_szczegolne": [
            "LOKALIZACJA: Hilden pod Düsseldorfem — wyzwolony jeniec",
            "Data 2.VI.1945 — miesiąc po kapitulacji Niemiec",
            "'Stryj jest w Edynburgu' — potwierdza gen. Janusza w Szkocji",
            "'O Ojcu obecnie nic nie wiem' — Stefan jeszcze w niewoli/zagubiony",
            "Obóz przegrupowania polskich żołnierzy",
            "Pytanie 'co będzie dalej' — niepewność o przyszłość",
            "Papier zniszczony, ubytki na brzegach, atrament niebieski"
        ],
        "kontekst": "List wyzwolonego jenieca z Hilden pod Düsseldorfem, datowany 2.VI.1945 — miesiąc po kapitulacji. Krzysztof dowiedział się, że stryj gen. Janusz jest w Edynburgu, ale o ojcu Stefanie 'obecnie nic nie wie'. Pisze o przegrupowaniu obozu polskich żołnierzy. Dokument ilustruje chaos pierwszych tygodni po wyzwoleniu — żołnierze szukają rodzin rozrzuconych po Europie."
    },

    # ARG/V/77 — List do matki — Wigilia 24.XII.1946, str. 2
    "juras_077": {
        "typ": "List odręczny — str. 2 listu wigilijnego",
        "data": "24.XII.1946",
        "jezyk": "polski",
        "nadawca": "Krzysztof Głuchowski",
        "adresat": "Wanda Głuchowska (matka)",
        "strony": ["juras_011_page12.jpeg"],
        "transkrypcja": """[...] tak[?] w ogólnym ustaleniu jest Anglia
na co[?] ile dalszy[?] Zachęcaj[?] mu[?] też[?]. Gdy[?] wiem, daw
i[?] u Ciebie jest dużo[?] inaczej[?]. Byli Polacy bo
w Filipinach nie do Anglii[?] jest oficjal-
nie[?] już w kolejcy[?] nie i Filipiny[?] oficjal[?]
w ogóle[?] dom[?] Korowaj[?] nie wiem[?]
właśnie[?] on odwag[?] przyjaznie[?]
[nieczytelne — pismo bardzo gęste i drobne]

[...] Polkownik[?] grize[?] fajka[?] znakomit[y?] w str.
F3[?] regularnie kto nie w obiekcj(?) moimi
zaczynaj[?] i kiedzy[?] się wciąż[?] nie
[nieczytelne]

[...] tata[?] pojazd[?] fajno w nie korzysta[?] dość[?]
ale[?] że dalszej szypy panu i[?] a dopa[?]-
[?] na
o ile do nas tego w[?] upraszali i coś[?] wiem[?]
to[?] nie spał[?] dobrze o tak daleko[?] to
[?] się Ojciec Puls[?] Guty[?] Alutij[?] albo[?]
na dole[?] tyle co[?] dadzą[?] wszelako[?] i dalszych[?]
nie sami[?] [?] tutaj? i idgałkiem[?]
[nieczytelne — końcówka strony]""",
        "pieczecie": [],
        "podpisy": [],
        "osoby": ["Krzysztof Głuchowski (nadawca)", "Wanda Głuchowska (adresatka — matka)"],
        "znaki_szczegolne": [
            "Wigilia 1946 — 20-letni żołnierz pisze do matki w Warszawie",
            "Strona 2 listu cztrostronicowego (str. 1 = ARG/V/76, str. 3 = V/78, str. 4 = V/79)",
            "Pismo BARDZO drobne i gęste — skan mały, odczyt wysoce niepewny",
            "Wspomina Anglię, Filipiny — sytuacja emigrantów polskich",
            "Wspomina Ojca — Stefan Głuchowski (repatriacja?)",
            "Wymaga profesjonalnego HTR (Transkribus) i skanu w wyższej rozdzielczości"
        ],
        "kontekst": "Strona 2 wigilijnego listu do matki Wandy (24.XII.1946). Krzysztof pisze z Anglii — opisuje sytuację Polaków na emigracji (Filipiny, Anglia). Pismo niezwykle drobne, skan w niskiej rozdzielczości — transkrypcja wysoce niepewna. Pełny list: str. 1 (V/76), str. 2 (V/77), str. 3 (V/78), str. 4 (V/79)."
    },

    # ARG/V/79 — List do matki — Wigilia 24.XII.1946, str. 4 (sytuacja emigrantów)
    "juras_079": {
        "typ": "List odręczny — str. 4 listu wigilijnego",
        "data": "24.XII.1946",
        "jezyk": "polski",
        "nadawca": "Krzysztof Głuchowski",
        "adresat": "Wanda Głuchowska (matka)",
        "strony": ["juras_013_page14.jpeg"],
        "transkrypcja": """[...] ist[?] Grabowska tu minie specjalnie[?]
i[?] ogi[?] zaklejonych[?] Pani[?] wszyst[?]
Kieda[?] (Popo[?] nie o to[?] co[?] tamte[?]) bo[?] po
stanie[?] w ten wymach[?]. Dlatego czek żeby[?] no
o dalej [?] jąć[?] dobl[?] to jest[?] na dachy[?]
do[?] przejm[?] samol[?]. Wigorek[?]

Od Stryja dużej[?] informacje[?] nie
mający[?] chwiów[?].

Czesto nie dupli[?] [?]na[?]
o lepina[?] wsłać[?] prawdopodob[?] Przy[?] nie[?]
żołnierz[?], wobec[?] jest[?] koniecz[nia?] udział[?] posta-
wili[?] niie[?] widoczniii[?] udział[?] które jest[?]
nie swoby[?] kompo[?] na domy[?] warto być[?] do
i o pięć[?]. Następuje[?] więce[?] zwarta[?] że[?]
[nieczytelne]

[...] że dalszego[?] ich dalj(?) [nieczytelne] pragnącemu[?]
o zapowiedzianej[?] się podwod[?] w[?] pul[?] co[?] mają[?]
prezen(?)wiosna[?] pomi[?] pracę[?] jest a[?] mi[?] moja
zwolnioni[?] Bezliwy[?] emisi[?] pozycje[?] wszech[?] nai[?]
i[?] o bożen Pasfra(?) [?] i przech[?] jak[?]
na krytma[?] obronu Pacfory[?] o[?] i dalin [?]
wiosna[?] Bandung[?] widwn[?] się patrzy[?] na
z[?] przem[?] w czarnom[?] wypiera [?] w a dalins [?]""",
        "pieczecie": [],
        "podpisy": [],
        "osoby": ["Krzysztof Głuchowski (nadawca)", "Wanda Głuchowska (adresatka)", "Grabowska (wspomniana)", "Stryj (gen. Janusz Głuchowski)"],
        "znaki_szczegolne": [
            "Strona 4 (ostatnia) listu wigilijnego 24.XII.1946",
            "'Od Stryja dużej informacje nie mające' — brak wieści od gen. Janusza",
            "Pismo BARDZO drobne — skan w niskiej rozdzielczości",
            "Odczyt wysoce niepewny — wymaga HTR",
            "Wspomina Grabowską — nieznana postać",
            "Kontekst: sytuacja emigrantów, demobilizacja, przyszłość"
        ],
        "kontekst": "Ostatnia strona (4 z 4) wigilijnego listu Krzysztofa do matki Wandy, 24.XII.1946. Wspomina stryja gen. Janusza (brak informacji od niego), Grabowską, sytuację emigrantów. Pismo niezwykle drobne, skan zbyt mały dla rzetelnego odczytu — transkrypcja orientacyjna, wymaga weryfikacji z oryginałem."
    },

    # ═══════════════════════════════════════════════════════════════
    # SERIA V — Priorytet 3: Listy kolegów (V/201-218)
    # ═══════════════════════════════════════════════════════════════

    # ARG/V/202a — List 'Józefa P.S.' — wieści rodzinne
    "juras_202a": {
        "typ": "List odręczny",
        "data": "ok. 1946",
        "jezyk": "polski",
        "nadawca": "Józef P.S.",
        "adresat": "Krzysztof Głuchowski",
        "strony": ["originals_201_217/20260324_1735536699334025058410662_rot.jpg"],
        "transkrypcja": """[Kartka niebieska — lewa strona:]
[?] Polish Forces [?]
Polish Forces NAAFI[?]

[?] Styczeń 1946[?]

Kochany Panie Rudy[?]:

W pierwszych dniach piszę do Pana [?] o kilku
[?] do Anglii. Jak dno. Pana pozdać[?] z
tego[?] [?] postanowieniom.
Właśnie tedeś[?] Podstyriąd[?] i z przyjemnością
być odeślę[?] poruszona[?] czeka i pozostałe słoniecz[?]
Siostra jest dość[?]. Ogłoś jedną do obsługiwanej[?]
olśnie sprawie[?].
[...] [nieczytelne] [?] Wskazując fajne[?] sprzedą
na biela[?] całkiem[?] Sobieskiego bońdo tu konneksjach[?]
przesyłam wsłodze[?] cenę, czer o boskie listonosz ciągle
dalej czytanie[?]

Pani Kroplidłą[?] pomiesi[?] pył[?] Pana tu bowd-
ś dość wol[?] fajnie jest jelo na ulicznikowi
[...]  fajne o do dostwier co dobrami z fajne[?]
w fajnie przyleci[?] ku do Pana w Anglii we
w [nieczytelne dalszy tekst]

Ściskaj a zawięziś[?]

[podpis nieczytelny]

[Kartka kremowa — prawa strona:]
[?] Polish [?] Szpital[?]
Polish Forces CMF 112[?]                   Gdynia [?] 12. 46[?]

Panie Krzysztofie[?],

Upozostałem się do pis[?] [?] do nikogo
3 DSK[?], a poza mogą[?] informacyj nic
[nieczytelne]

Pana Kraińskiego[?] znasz pewnie[?] w mańka Wion[?]
[?] [?] stru o edice[?] [?] [?] cukierki[?]
jabłko ciasteczka dlatego dać! Pan tu Wil[?].

Ja dośliźnie do ze mnych [?] rozmawiać nai[?]
Podleśnym[?] Morg[?] i szprę obudzi! C. [?]
downy[?] z bodu[?] Podleśn[?].

J olacy obnaj[?] Pola rozmawiasz[?] Pan
przystrzelonymi[?] życiem[?] z zaparciem[?] narzuca
ich najbujacz[?] podwołań[?] o odzieżowo.

[Łącze?] nowy niśri dkien[?]

A. Wólanow[?]

P.S. z polowy[?] za ze sobaz[?] kolon[?].""",
        "pieczecie": [],
        "podpisy": ["Józef P.S. (?)", "A. Wólanow[?]"],
        "osoby": ["Józef P.S. (nadawca)", "Krzysztof Głuchowski (adresat)", "A. Wólanow[?]"],
        "znaki_szczegolne": [
            "DWA LISTY na jednym skanie — kartka niebieska i kremowa",
            "CMF 112 — Central Mediterranean Forces",
            "Wymieniony 3 DSK (Dywizja Strzelców Karpackich)",
            "Pismo trudne do odczytu — wymaga HTR"
        ],
        "kontekst": "Dwa listy sfotografowane razem na jednym skanie. Korespondencja z kolegami z wojska (CMF, 3 DSK). Odczyt wysoce niepewny — pismo odręczne, atrament wyblakły."
    },

    # ARG/V/202b — List do 'Pana Wincentego' — życzenia noworoczne
    "juras_202b": {
        "typ": "List odręczny",
        "data": "8.I.1946",
        "jezyk": "polski",
        "nadawca": "P.J. Wilczem (?)",
        "adresat": "Pan Wincenty",
        "strony": ["originals_201_217/20260324_1735536699334025058410662_rot.jpg"],
        "transkrypcja": """[Na tym samym skanie co V/202a — kartka kremowa, prawa strona]
[Transkrypcja łączona z V/202a — patrz juras_202a]""",
        "pieczecie": [],
        "podpisy": [],
        "osoby": ["P.J. Wilczem[?] (nadawca)", "Pan Wincenty (adresat)"],
        "znaki_szczegolne": [
            "Na tym samym skanie co V/202a",
            "Życzenia noworoczne 8.I.1946"
        ],
        "kontekst": "Noworoczna korespondencja 1946. Dwie jednostki sfotografowane razem na jednym skanie — patrz juras_202a."
    },

    # ARG/V/205 — List — fotografie i Gen. Strelczyński
    "juras_205": {
        "typ": "List odręczny",
        "data": "ok. I.1946[?]",
        "jezyk": "polski",
        "nadawca": "Nieustalony",
        "adresat": "Krzysztof Głuchowski",
        "strony": ["originals_201_217/20260324_1746587960714446524300966_rot.jpg"],
        "transkrypcja": """[nagłówek nieczytelny — tekst odwrócony u góry]
kochani najlepsi[?] [nieczytelne] serdeczn[ie?]

[?] I. [?]

z przybyciem tam dłuszej[?], że jeszcze
nie przynosili ciężki[?] brogi[?], a ó ciupki[?]
z tego[?] mierem powole kochani o Waszym
przeniesieniu do Żimarzynu[?]. Zaidy[?] tylko
tu przyjdą, to zaraz dam polok[?]
odkąd bożek tu P[an] znalazłem w pólnocym[?]
Odbłononym[?] chustik[?] do 15-ty id. Galeria[?]
byłem u pole Stóleckiego[?].

W Londynie chciałem być u Gen. Strelczyńskiego
świstowi[?] mierrze Kelepcin[?] nagrodzon[?] z prośbę
o rządfundowani[e?] do mnie celi[?] i kiedyś mają
priklu[?]. Przypuszczam[?] tu List[?] nie  nic wobec
nikogo, gdzie[?] niedotkniętem rospostroich[?]
Co odpiksie[?] w dno. Jadąc że niesłusano[?]
wspatrzę[?], a Januszowi bardzo prosy o przybych[ie?]
nic zbieranych fotografij. Jednak to bordowe[?]
to bardzo też porcy[?] o[?] przysłaniu do 25 ka[?].

Przy robotomidni[?] do Pocz[ty?] kochani[?]""",
        "pieczecie": [],
        "podpisy": [],
        "osoby": ["Nadawca nieustalony", "Gen. Strelczyński (wspomniany)", "Janusz (wspomniany — gen. Głuchowski?)"],
        "znaki_szczegolne": [
            "Wspomina Gen. Strelczyńskiego — wizyta w Londynie",
            "Januszowi prosi o przysłanie fotografii — gen. Głuchowski?",
            "Wymiana fotografii między żołnierzami",
            "Pismo trudne — wymaga HTR"
        ],
        "kontekst": "List od niezidentyfikowanego kolegi. Wspomina wizytę u Gen. Strelczyńskiego w Londynie i prośbę o fotografie od Janusza (prawdopodobnie gen. Głuchowskiego). Dokumentacja wymiany fotografii w środowisku PSZ."
    },

    # ARG/V/206a — List z CMF Polish Forces 125
    "juras_206a": {
        "typ": "List odręczny",
        "data": "24.I.1946",
        "jezyk": "polski",
        "nadawca": "Nieustalony (podpis 'G...')",
        "adresat": "Krzysztof Głuchowski",
        "strony": ["originals_201_217/20260324_1748223633272231402712281_rot.jpg"],
        "transkrypcja": """C.M.F. Polish Forces 125
24/I 46

Kochany Krzysiu!

Otrzymałem Twój list poleca, bo
dopiero po powrocie z ćwczeń[?]
tygo dniowego[?] w poniedziałek 21/I
10 jutro mniej dość[?] na tydzień
prz ćwiczeniu[?] do Bolonii[?]. Poza
tożłam[?] że subiektywu boletou Toyot[?]
to lista informacja fajne[?] podołaniu[?]
wiadomości o „ufaniu mas[?]". Ogarzni[?]
nie damy letnim obroty[?], bo[?] każd tyło[?],
bo Jaśki i Leszakóch[?] bo tańczek i ka-
dudzi[?] — ok chwiłowe nadzieję mieniem że
plany roboczenie się w czego, w reszta
kursami warantu[?] ich finiszem.
Toteż jeszcze wielki[?] zwolni[?] no
tu pojad[?] do klarine[?] ale na Polary[?]
leczo[?] kilka tysię[cy?] i zwolnienie
more następne w bardzie[?] wam obiąt[?]
tu podchol[e?] — w reszta oba[?]. Cu pal[?]
1945 – na Paprozka – osiem miozn[?]
ty – o wczoraj którogo nie wydał[?] jeszcze[?]
od roku. Osiem roturmam olma[?]""",
        "pieczecie": [],
        "podpisy": ["G... (podpis nieczytelny)"],
        "osoby": ["Nadawca G... (nieustalony)", "Krzysztof Głuchowski (adresat)", "Jaśko (wspomniany)", "Leszek (wspomniany)"],
        "znaki_szczegolne": [
            "Logo choinka (5 KDP?) na papierze",
            "CMF Polish Forces 125 — Włochy",
            "Data 24.I.1946 — demobilizacja i reorganizacja 2 Korpusu",
            "Wspomina ćwiczenia w Bolonii",
            "Wspomina Jaśka i Leszka — koledzy z jednostki"
        ],
        "kontekst": "Styczeń 1946, CMF (Włochy). Nadawca opisuje demobilizację i reorganizację 2 Korpusu Polskiego. Logo 5 KDP na papierze. Wspomina ćwiczenia tygodniowe i plany zwolnień."
    },

    # ARG/V/206b — List 'Słobusia K.' — decyzje o wyjeździe, Bolonia
    "juras_206b": {
        "typ": "List odręczny",
        "data": "16.IV.1946",
        "jezyk": "polski",
        "nadawca": "Słobuś K.",
        "adresat": "Krzysztof Głuchowski",
        "strony": ["originals_201_217/20260324_1811564265226715002790673_rot.jpg"],
        "transkrypcja": """16/IV '46.

Kochany Krzysztofku!

Bardzo niestanowieńi[e?]
Ty olecisz Korzył władn[ie?]
Życie nie wyjeżdżali
w końce srypt[?]. Żałuję
że nie mocy dla Nas
uszczyc Występka[?], ale
nie wybędno owi wyjdę.
Tak ka władek[?] ktoś[?]
by nieusty olecis w
Stosunki[?] dla Nas dom.
Coprawda to i ja bę-
dę unoś „republice" Pola[?]""",
        "pieczecie": [],
        "podpisy": ["Słobuś K."],
        "osoby": ["Słobuś K. (nadawca — bliski znajomy)", "Krzysztof Głuchowski (adresat)"],
        "znaki_szczegolne": [
            "Kwiecień 1946 — decyzje o wyjeździe",
            "Nadawca zna Krzysztofa bardzo blisko ('Krzysztofku')",
            "Temat: emigracja vs. pozostanie"
        ],
        "kontekst": "Kwiecień 1946. Nadawca zna Krzysztofa bardzo blisko. Temat listu: decyzje o wyjeździe i emigracji — kluczowy moment w życiu żołnierzy PSZ."
    },

    # ARG/V/207a — List Janusza Ramińskiego (I) — wieści o Wandzie
    "juras_207a": {
        "typ": "List odręczny",
        "data": "19.IX.1946",
        "jezyk": "polski",
        "nadawca": "Janusz Ramiński",
        "adresat": "Krzysztof Głuchowski",
        "strony": ["originals_201_217/20260324_1813377748033720388689926_rot.jpg"],
        "transkrypcja": """[Strona 1 — niebieska kartka lewa:]
Szlachetna Pani Mandzie[?] okocen[?] moim Pol[?]
Bulwą[?] pola[?] wszet[?]. Tu jest nie pracyw[?]
Co bli dzieje[?] z p. Stefanem Panem
Ojcem — od dłuższego czasu nie mam
od niego nic o nim wiadomości[?] czy
jest nadal w Niemczech[?] czy zdążył
bodnej[?] co do Anglii.
Istnieje mało co znaczy Pamiętn[?] z
Pana jakoś 10-11 letniego chłopca Mam[?]
wrazenia[?] że jest Pan w siódło Mego wnuczka[?]
typu — co jest 1927 rocznik ale
nie to myślę[?].
Brodziszu[?] chciał sprawić Pan bo
gdy[?] Panie Krzyśko nie jest Pan bydnie
i w dłubiąc[?] w czasie zakażone[?] nich-może[?]
proszę zmi[?] zamówide[?] o postarow[?] o[?]
Panina[?] Komunikatów[?]

Każdy[?] wcielmni[?] ze List [?]
o mnie nie zapomniał[?].

Janusz Ramiński

[Strona 2 — kremowa kartka prawa:]
                    Brownings Camp
                    Billingshurst
                    Sussex
                    19/9 1946

Kochany Panie Krysiu.

Bardzo mnie ucieszyć List Pana
i wiadomość że jest Pan jeszcze[?] w Anglii,
a do tego nowy ów[?], co jest najlepsze
z tego co mógłby Pan zrobić.

Ostatnie wiadomości o Matce Pana
należały od mojgo syna Marka. Ty
ostatnie wiadomości przesłał Panu pan
Janusz. Bezpiecznie znacie[?] to oby pisz[?]-
my na aptekę w Łodzi[?] żebyś Marka
to przede[?] to dlatego (mama odziumierz[?]
o nagrommi[?] lęgu porodź[?]). Matka Pana
Pyta Pan czy poroty uprować[?] do
Matki i czy podaj[?] adres na Bodney.
Na myślę najbardziej przejście[?]
niech w Łodzi — użyj Matka coś miesiąc[?]
stałan rolaną[?] — nim ich bieprzeczenia[?]""",
        "pieczecie": [],
        "podpisy": ["Janusz Ramiński"],
        "osoby": [
            "Janusz Ramiński (nadawca, Brownings Camp, Sussex)",
            "Krzysztof Głuchowski (adresat)",
            "Wanda Głuchowska (Matka — apteka)",
            "Stefan Głuchowski (Pan Ojciec — brak wiadomości)",
            "Marek (syn Ramińskiego — pośrednik)"
        ],
        "znaki_szczegolne": [
            "Brownings Camp, Billingshurst, Sussex — obóz polski",
            "Ramiński pamięta Krzysztofa jako 10-11 letniego chłopca ('rocznik 1927')",
            "Pyta o Stefana ('od dłuższego czasu nie mam o nim wiadomości')",
            "Apteka Wandy — przekazanie wiadomości przez Marka",
            "Rada: pisać na adres Bodney",
            "List dwustronny na niebieskiej i kremowej kartce"
        ],
        "kontekst": "Wrzesień 1946. Ramiński w Brownings Camp (obóz polski w Sussex) pośredniczy między Krzysztofem a rodziną w Polsce. Zna rodzinę od lat — pamięta Krzysztofa jako chłopca. Pyta o Stefana (brak wiadomości). Wanda prowadzi aptekę."
    },

    # ARG/V/207b — List Ramińskiego (II) — aresztowanie Marka
    "juras_207b": {
        "typ": "List odręczny",
        "data": "28.X.1946",
        "jezyk": "polski",
        "nadawca": "Janusz Ramiński",
        "adresat": "Krzysztof Głuchowski",
        "strony": ["originals_201_217/20260324_1820364793131874182220755_rot.jpg"],
        "transkrypcja": """Brownings Camp
Billingshurst
Sussex
28/10/'46.

Kochany Panie Krzysiu.

Marek został aresztowany przez
Bezpiekę 9 września i bardzo bij[?] z tego
powodu markotau[?].

Ale dzisiaj dostałem od niego
list z 16 paźdz. że znów jest na wol-
ności i udało mu bij fymi[?] razen
wykręcić. Nie wiem niestymcji[?] z ja-
kiego powodu i co od niego chcieli.

Jeśli pitre — rzecz[?] bij znów pewnie[?].

Marek pnia[?] mi wiadomość o Panu,
(które mu postałem) przekazał Matce
Pana. Niestety nie podaje żadnych
dodatkowych wiadomości tylko aby
Pan pisał jaknajprędzej na adros""",
        "pieczecie": [],
        "podpisy": ["Janusz Ramiński"],
        "osoby": [
            "Janusz Ramiński (nadawca)",
            "Krzysztof Głuchowski (adresat)",
            "Marek Ramiński (aresztowany przez Bezpiekę 9.IX.1946)",
            "Wanda Głuchowska (Matka Pana — przekazano wiadomości)"
        ],
        "znaki_szczegolne": [
            "MAREK ARESZTOWANY PRZEZ BEZPIEKĘ 9 WRZEŚNIA 1946!",
            "Zwolniony — list z 16.X potwierdzający wolność",
            "Bezpieka = UB (Urząd Bezpieczeństwa)",
            "Marek przekazał wiadomości od Krzysztofa Matce (Wandzie)",
            "Brownings Camp, 28.X.1946"
        ],
        "kontekst": "KLUCZOWY: aresztowanie syna Ramińskiego (Marka) przez UB 9.IX.1946 — świadectwo represji wobec pośredników w korespondencji z emigracją. Marek wypuszczony (list z 16.X). Ramiński nie wie za co aresztowano. Marek zdążył wcześniej przekazać wiadomości Wandzie."
    },

    # ARG/V/208 — List 'Czesława J.' z obozu w Walii
    "juras_208": {
        "typ": "List odręczny",
        "data": "ok. 1946",
        "jezyk": "polski",
        "nadawca": "Czesław J.",
        "adresat": "Krzysztof Głuchowski",
        "strony": ["originals_201_217/20260324_1824362851036695023960408_rot.jpg"],
        "transkrypcja": """[Lewa kartka:]
52

to Stochłowe Łorew[?] i oddo[?]—
sić[?] na ushinwał[?] nie uzlodayn[?]
a przez poganiową opo[?] oddo[?]
uwszystka[?] jesarśćisz[?] jest us
jedme polebini[?] tu olna osa
wrocił by Gdyńsk[?] razjędr[?].
Zbaprólu[?] Pan be[?] ów szniesz[?]
od o gazet[?] bez N. Chrop[?]
jest i nieistonami. Panim[?]
łowaj skatlujaj[?] się w ogólnym
opr[?] unig C jeśmni[?] ko A.K.N[?].pl[?]
jużka[?] za olody[?]. Być W.D.kobap[?]
plus w ajhonania minik[?] wa
[?] upoślenie przygrowak[?] łaps[?]
a pruszk, babien osz c I d[?]
Świdczki[?] uż aw oficerskie[?]
proda[?] tu my uzgadla pru-
[nieczytelne]

[Prawa kartka:]
                        18. X. 46[?]

Drogi mój Krzysiu!

Upewni[?] się w rozumiam forji[?]
kochani[?]. Win[?] chyba robi[?] co za
moim czasu[?] reble[?] w Łągó[?]. Solidy[?]
rozumiesz potaje[?] co[?] i [?] [?]
a doby uwydziła[?] w Gale Gwi[?].
Wiedy[?] moty jeszcze mity obwata[?]
stabucki[?] Polsce a Linia[?] dlatego[?]
wada[?] nic[?] ty, no[?] list do obody[?]
więci[?] pamięci[?] do jasałełem[?]. O
po bu[?] tumilek[?], a chrzestne[?]
ponytnik[?] nie[?] go[?] rusło[?] Sofon[?]
boku[?], kol ze wołoni[?] ofkolina[?]
inna miasfomaist[?]. Widocz-
nami[?] moty muta. Port[?] moj[?]""",
        "pieczecie": [],
        "podpisy": ["Czesław J."],
        "osoby": ["Czesław J. (nadawca)", "Krzysztof Głuchowski (adresat)"],
        "znaki_szczegolne": [
            "Data 18.X.1946[?]",
            "Dwie kartki sfotografowane razem",
            "Pismo BARDZO trudne do odczytu",
            "Wspomina AK",
            "Wymaga profesjonalnego HTR"
        ],
        "kontekst": "List Czesława J. do Krzysztofa. Pismo niezwykle trudne do odczytu — transkrypcja orientacyjna. Wymaga profesjonalnego narzędzia HTR."
    },

    # ARG/V/211a — List Krahelskiego 'Leszka' z CMF 153
    "juras_211a": {
        "typ": "List odręczny",
        "data": "9.VIII.1946[?]",
        "jezyk": "polski",
        "nadawca": "Plut. pchor. Krahelski Lech (Leszek)",
        "adresat": "Krzysztof Głuchowski",
        "strony": ["originals_201_217/20260324_1931188855098837933167592_rot.jpg"],
        "transkrypcja": """plut. pchor. Krahelski Lech.              9 VIII 46[?]
Polish Forces. C.M.F. 153.

Kochany Krzysiu!

U nas wszystko jest teraz takie same jak było
przedtem. Właściwie nie ma żadnych zmian,
chyba to tylko, że jestem więcej zapety[?] jako
brygato donos[?] na kursie motorowym, co
mnie zupełnie nie bawi, ze względu na to że już
kilka takich kursów odrobiałem. Mihi[?] więcejchat
i mieszła[?] obecnie nad morzem. By-
łem u niego w niedzielę i wyborowi się[?]
znowu jest dla mnie i serdeczny.

Jeżeli[?] być mogi[?] przyjechar na sobotę i nie-
dzielę, jak to znaczy wiele raki[?], to przyjedzii[?]
bo tam musi być Ci trochę nudno. Okre-
ślić[?] mia[?] też nic specjalnego ale zawsze
coś można zagadek[?].

Przyjechał teraz Jurekc[?] Major nie
stety nie jest tu. Widuję się z nim co
drugi dzień, ale on jest tam zupełnie
temu i to jest niewiele.

Napisz mi jak Ci tam iść w szkole i
czy wybierasz się na podchorążówkę. Moim
zdaniem warto.

Marian przesyła Ci pozdrowienie, ja mam
nadzieję, że jeszcze do nas napiszesz.

Ściskam        Leszek""",
        "pieczecie": [],
        "podpisy": ["Leszek (Krahelski Lech)"],
        "osoby": [
            "Plut. pchor. Krahelski Lech / Leszek (nadawca, CMF 153)",
            "Krzysztof Głuchowski (adresat)",
            "Jurek Major (wspomniany)",
            "Marian (przesyła pozdrowienia)",
            "Mihi[?] (mieszka nad morzem)"
        ],
        "znaki_szczegolne": [
            "CMF 153 — Włochy",
            "Kursy motorowe — szkolenie żołnierzy",
            "Pyta o podchorążówkę — doradza Krzysztofowi",
            "Marian przesyła pozdrowienia — ten sam co w V/211b i V/216b?",
            "Pismo czytelne, atrament niebieski"
        ],
        "kontekst": "List Krahelskiego (plut. pchor., CMF 153) do Krzysztofa. Sierpień 1946 — Krahelski na kursach motorowych, radzi Krzysztofowi iść na podchorążówkę. Ton koleżeński, serdeczny. Marian przesyła pozdrowienia."
    },

    # ARG/V/211b — List Krahelskiego z RYSUNKIEM JELENIA
    "juras_211b": {
        "typ": "List odręczny z rysunkiem",
        "data": "29.VIII.1946[?]",
        "jezyk": "polski",
        "nadawca": "Plut. pchor. Krahelski Lech (Leszek)",
        "adresat": "Krzysztof Głuchowski",
        "strony": ["originals_201_217/20260324_1949561247533166282117318_rot.jpg"],
        "transkrypcja": """plut. pchor. Krahelski Lech.     29. VIII. 46[?]
Polish Forces. P.M.F.[?] 153

Kochany Krzysiu!

U nas nie wionpa[?] Nie zandz[?] olwa
cmdżo[?] mie[?] jub[?] w dalszych wzglę-
du. Dobra[?] moje zaś ile ostrzejsza napręd[?]
dy nie [?] masz miejsce jakiegoś[?]
dls mnie ikon[?] o kole[?] więzności[?]
około[?] napokora[?]. Idzie również to
ma[?] pracędy[?] i dwóch[?] po miodycin tu[?]
[?] fajna nie każdzio się na dóbr[?]
był fajma[?] ale[?] nie od[?] i wta-
takidajko[?] długi kolakjce[?] „Jeleń" ry-
sujs[?] „ponirzej" kto mogę to przysłac też
doli(?) Kraków. też[?] jest Moreygo[?]
Ferencie[?] omi moisi[?]. Tum to nieco[?]
dalanym zieja[?] musialem[?] się co wyjat-
kono[?]  bazek[?].

Wiem podobizszie ze napisziesz do mnie,
ho napywną[?] kurga waw av Grobni[?] i
jebróta[?].

Pozdrowienia od Mariana,
Polski olkóam[?]

Leszek

[RYSUNEK — jeleń narysowany ołówkiem, pod spodem tekst:]
(propozycja bys[?] doable
pomnik[?] ile stary[?] nie rozpoznaj[?]
aby i obronie[?] odkazano[?] myśl mi[?] pon-
nowy/dolejaj[?] chca nie olni[?]
K[?])""",
        "pieczecie": [],
        "podpisy": ["Leszek"],
        "osoby": ["Krahelski Lech (nadawca)", "Krzysztof Głuchowski (adresat)", "Marian (pozdrowienia)"],
        "znaki_szczegolne": [
            "RYSUNEK JELENIA — symbol 7 Pułku Ułanów Lubelskich!",
            "Wspomina 'kolakjce[?] Jeleń' -- kryptonim pułku",
            "Propozycja pomnika? — pod rysunkiem",
            "Marian ponownie przesyła pozdrowienia",
            "Unikat — rysunek jelenia w liście żołnierskim"
        ],
        "kontekst": "List z rysunkiem jelenia — symbolu 7 Pułku Ułanów Lubelskich «Jeleń». Krahelski rysuje jelenia i wspomina kolekcję/projekt związany z pułkiem. Unikatowy dokument łączący korespondencję z ikonografią pułkową."
    },

    # ARG/V/212a — List Jaśka Leoniuka z Troyes (I)
    "juras_212a": {
        "typ": "List odręczny",
        "data": "12.IX.1945[?]",
        "jezyk": "polski",
        "nadawca": "Jaśko Leoniuk",
        "adresat": "Krzysztof Głuchowski",
        "strony": ["originals_201_217/20260324_1938481997225877696633528_rot.jpg"],
        "transkrypcja": """Troyes 12. IX '45[?].

Drogi Krysiu!

Przepraszam Cię bardzo, że
tak długo nie odpisywałem
na doli[?] Twój list Który otrzy-
małem dopiero 30. VIII b.r., ale
wierz mi że to nie moja wina.
My f.j. Jurek i ja z znajduje-
my[?] z powrotem w Troyes i pra-
cujemy tak jak na początku. Sto-
sunek władz zwierchnik do
nas pracowników, zmienił się
z umienię[?] na lepsze. Mimo to
nie ciekawy zamimam porostki[?] tu
na zimę. Krysiek napisz nam
co u Ciebie Tychar[?], a pre-""",
        "pieczecie": [],
        "podpisy": ["Jaśko (Leoniuk)"],
        "osoby": ["Jaśko Leoniuk (nadawca, Troyes, Francja)", "Jurek (kolega w Troyes)", "Krzysztof Głuchowski (adresat)"],
        "znaki_szczegolne": [
            "Troyes (Francja) — Polacy pracujący we Francji po wojnie",
            "Wrzesień 1945 — poprawa stosunków z pracodawcami",
            "Jurek i Jaśko razem w Troyes",
            "Pismo czytelne, ołówek na żółtawym papierze"
        ],
        "kontekst": "List Jaśka Leoniuka z Troyes (Francja), wrzesień 1945. Polacy pracujący we Francji po wojnie — stosunek władz 'zmienił się na lepsze'. Jaśko i Jurek razem. Pyta o Krzysztofa. Kontynuacja w V/212b."
    },

    # ARG/V/212b -- List Jaska Leoniuka z Troyes (II)
    "juras_212b": {
        "typ": "List odreczny",
        "data": "15.IX.1945[?]",
        "jezyk": "polski",
        "nadawca": "Jasek Leoniuk",
        "adresat": "Krzysztof Gluchowski",
        "strony": ["originals_201_217/20260324_194747769693003963708055_rot.jpg"],
        "transkrypcja": """[Lewa kartka:]
na granatowo ize duro kolegow
wyjechalo do kraju, wszystko po sla-
wieniu. Ja dostalem list z Kraju,
rodzina zyje. Na tym Koniec, bo
musze isc na sluzbe, czekami na
odpowiedzi. Sciska Cie

Janek

[Prawa kartka:]
                Drogi Krysiu!    Troyes 15.IX '45[?]

List Twoj otrzymalem za ktory
bardzo dziekuje. Przyjechali on na czas,
bo wybieralam sie do Ciebie dajmeno[?]
po pierwsyem. To u Ciebie slychac no-
wego, czy otrzymales paczke? Za
nieco cos piszke[?] kabanory[?], pod
kuruzutel[?], i kursule sielnigk[?] i krawat[?]
W wypadku gdyby paczka zginela,
to jest ona ozaczone[?] na poczcie
w cenie 2000 Fr. Spodnie nie bucty[?]-
nie miema gdzie, ale postaram
sie kupic, za firek[?] od Bogdana.
Dostane od niego 1000 fr. gdyz do-
lary dawno sprzedat[?] w tej cenie.
Spodnie bede kupowal[?] okolo
700 fr. (prawie nowe, lub nowe). Ubrau
postalyze[?] za premiumdarystyjem[?] nas""",
        "pieczecie": [],
        "podpisy": ["Janek (Leoniuk)"],
        "osoby": ["Jasek/Janek Leoniuk (nadawca, Troyes)", "Krzysztof Gluchowski (adresat)", "Bogdan (wspomniany)"],
        "znaki_szczegolne": [
            "Paczka z ubraniami za 2000 fr. -- pomoc materialna",
            "Dolary sprzedane -- wymiana walut wsrod emigrantow",
            "Spodnie za 700 fr. -- ceny we Francji 1945",
            "Koledzy wyjezdzaja do Kraju -- repatriacja"
        ],
        "kontekst": "Kontynuacja korespondencji z Troyes. Jasek wysyla Krzysztofowi paczke z ubraniami (kabanory, koszule, krawat). Ceny: paczka ubezpieczona na 2000 fr., spodnie ~700 fr. Koledzy wyjezdzaja do kraju -- repatriacja trwa."
    },

    # ARG/V/213a -- List Tudka z High Wycombe
    "juras_213a": {
        "typ": "List odreczny",
        "data": "3.II.1947",
        "jezyk": "polski",
        "nadawca": "Tudek",
        "adresat": "Krzysztof Gluchowski",
        "strony": ["originals_201_217/20260324_1847475149231012056091582_rot.jpg"],
        "transkrypcja": """High Wycombe 3 II '47r.

Kochany Krzysiu!

Z wielka radoscia dowiedzialem sie, ze
zipen[?] i jest[es?] rozumni jake[?] fa na
tej 'woldonej' wyspie. Donosi mi
o tym wuj Totis[?], ktory widzial
sie z Twoja ciamami[?] w Warszawie
i blisa data na Twoj obeny[?] adres.
Dowiedzialem sie rowno,z[?] ze zamierzasz
wyjechal do Trypolifimy[?] i dumowi[?] Twoja
posela[?], soly[?] klep[?] Staniszuwa nie robi[?],
jesli nie wladz[?] kiedys warunkow
do nawej[?] wracal do Kraju. Jestem
bardzo ciekawy pline kuzles[?] i co robisz
podczas kich[?] oblysich[?] siedem lut[?]
ja od wrzesnia 1939-go do grudnia
1944 bylem w Warszawie, nastepnie
od grudzien 1944 do komica wojny
pod Wiednia a pierwy pod Berlinem""",
        "pieczecie": [],
        "podpisy": ["Tudek"],
        "osoby": ["Tudek (nadawca, High Wycombe)", "Krzysztof Gluchowski (adresat)", "Wuj Totis[?] (posrednik)"],
        "znaki_szczegolne": [
            "High Wycombe -- miasto w Buckinghamshire, baza RAF/polskie osrodki",
            "Tudek w Warszawie 1939-1944, potem pod Wiedniem i Berlinem",
            "Wuj widzial sie z rodzina Krzysztofa w Warszawie",
            "Pismo czytelne, atrament niebieski"
        ],
        "kontekst": "Luty 1947. Tudek (kolega z Warszawy?) pisze z High Wycombe. Byl w Warszawie 1939-1944, potem walczyl pod Wiedniem i Berlinem. Wuj Totis posredniczy -- widzial sie z rodzina Krzysztofa w Warszawie i przekazal adres."
    },

    # ARG/V/213b -- List Tudka z Sudbury -- PKPR, R.A.S.T.
    "juras_213b": {
        "typ": "List odreczny",
        "data": "29.II.1947[?]",
        "jezyk": "polski",
        "nadawca": "Tudek",
        "adresat": "Krzysztof Gluchowski",
        "strony": ["originals_201_217/20260324_1848331174709311799573626_rot.jpg"],
        "transkrypcja": """Sudbury 29. II. 47[?].

Drogi Krysiu!

Dziekuje Ci za odpowiedzi, ktora otrzymalem
w blisz[?] naszego przenoszenia w St. Johns do
nowego oboru chudnokniaje[?]. Jest un Sudbury,
dbs. znajduje co o 3 mile od miasteczka,
doblednego[?] zwor wlasnych mal nie na i schody[?]
innej lokomosci[?]. Koszulik naklukowane na was[?]
burde typan[?], gdzie[?] zamiast 12 miesiace w 8
gdyznie jest niezabezp[ieczaj?]oce, te ku dolszejewan[?]
moznahy[?] umrec z glodu. Ale i moy[?] mie[?] od
dzisiaj wpisy do P.K.P.R., ale z niewiadamyld[?]
blizej prowodlaw[?] zostala odrodzona[?]. Jest nas
tu z wszystkich dwiedzy[?], ugro[?] glówne[?] gdzie[?]
chcie[?] wszeprzaie[?] do P.R.P.R. natomiast 2/3 prosila
o odwolenie. Ja rownisz jestem w lej grupe[?]
obecnie wraz z inzeni dyrektorjag[?] wspadkow
mozliwosci oplawy[?] i nieuy[?] entygrojac[?] i prowadz[?].
Ostatnio jest[?] mozliwosci dostania sie do
Londyn na R.A.S.T. gdzie[?] 120 naszypartner[?]
szpadowi[?] prowadka i prawdopodobaltie narze-
dzimgi[?] masa 150[?] oburom[?], hody[?] uczic[?]
sie fajpiolesza, a od poiniedzu[?]ko[?] moge sie
naprawic najtrudcy[?] z mat. ksiki, slom
i slowowi. Dobrze rowniez olszymac[?] pannie i
szpitalnego Cambridge.

Co Stydwi[?] w tebie, jak Ci idzie nauka i""",
        "pieczecie": [],
        "podpisy": ["Tudek"],
        "osoby": ["Tudek (nadawca, Sudbury)", "Krzysztof Gluchowski (adresat)"],
        "znaki_szczegolne": [
            "Sudbury -- przeniesienie z St. Johns",
            "PKPR -- Polski Korpus Przysposobienia i Rozmieszczenia",
            "R.A.S.T. -- kurs w Londynie, 120 uczestnikow",
            "150 obcokrajowcow -- Cambridge",
            "2/3 prosilo o odwolenie z PKPR"
        ],
        "kontekst": "Tudek przeniesiony z St. Johns do Sudbury. Opisuje warunki (zamkniete, 3 mile od miasta, brak transportu). Wpisy do PKPR. Kurs R.A.S.T. w Londynie dla 120 osob. 2/3 zolnierzy prosi o odwolanie -- niechec do PKPR."
    },

    # ARG/V/214 -- List posrednika z Bodney (I) -- list polecony od Mamusi
    "juras_214": {
        "typ": "List odreczny",
        "data": "9.II.1947[?]",
        "jezyk": "polski",
        "nadawca": "Nieustalony (posrednik z Bodney)",
        "adresat": "Krzysztof Gluchowski",
        "strony": ["originals_201_217/20260324_1944201555232293354009694_rot.jpg"],
        "transkrypcja": """Bodney 9. II. 47[?]

Kochany Krzysiu!

Przed chwila odebralem z po-
czty list polecony dla Ciebie
(od Mamusi) i wysylajac go,
przy okazji -- pisze troszke.
Zasadniczo nie wiem jaki orabic,
bo list ten jest otworamy (obozn[?]
si, ze jest bos[?] w srodku) -- i nie
wiem czy go doslyc[?], czy odklac[?]
i dolopno wladac w koperte
do Ciebie! Chyba zrole to ostar-
nie -- uwylo[?] ze man do mnie
na tyle zaufania, ze mie
posodzisz mnie oto ze wya[?]

Wczoraj odbylo sie tu zebra-
niu Kola (ja na minie jednak-
nie bylem, bo nie zaprostan[?]
ale obdalem ponedaycs poleg[?]""",
        "pieczecie": [],
        "podpisy": [],
        "osoby": ["Posrednik z Bodney (nadawca)", "Krzysztof Gluchowski (adresat)", "Mamusia (Wanda Gluchowska -- nadawca listu poleconego)"],
        "znaki_szczegolne": [
            "LIST POLECONY OD MAMUSI przekazany przez posrednika",
            "Bodney Airfield -- baza RAF, oboz polski",
            "List otwarty -- posrednik zastanawia sie czy doklac koperte",
            "Zebranie Kola -- organizacja zolnierska na Bodney"
        ],
        "kontekst": "Posrednik z Bodney przekazuje Krzysztofowi list polecony od matki (Wandy). List przyszedl otwarty -- posrednik zastanawia sie nad etyka dalszego przekazywania. Wspomniane zebranie Kola na Bodney."
    },

    # ARG/V/215 -- List posrednika z Bodney (II) -- stypendium Erentz
    "juras_215": {
        "typ": "List odreczny",
        "data": "13.IX.1947[?]",
        "jezyk": "polski",
        "nadawca": "Nieustalony (posrednik z Bodney)",
        "adresat": "Krzysztof Gluchowski",
        "strony": ["originals_201_217/20260324_1944532316727053919767412_rot.jpg"],
        "transkrypcja": """Bodney 13. IX. 47

Drogi Krzysiu!

Zasyłam Ci serdeczne gratulacje
z okazji otrzymania stypendium
Erentz -- to bylo jasne, ze Ty go
dostaniesz i odram[?] nie twierdzisz --
Poza listem do Ciebie od Litegyo[?],
wystalem jeszcze 2 (oba od Mamusi)
takowze, nie odklejajac ale ze
porada poczumeista naklejajac
nowej adres. Tak lepie[?].
Napisz Mamusi by zwierla[?]
adreatke[?] przy wysylaniu gazet
bo przyklodnaz[?] tutaj nadal
-- zupelnie niepotrzebnie!

Janusz Klepesz wrocil prost[?]
chory ze szpitala i cufa[?] sie
dosc dobrze, natomiast Koptek
i Janusz zostali tam nadal.""",
        "pieczecie": [],
        "podpisy": [],
        "osoby": ["Posrednik z Bodney (nadawca)", "Krzysztof Gluchowski (adresat)", "Mamusia (Wanda)", "Janusz Klepesz (chory)", "Koptek", "Janusz"],
        "znaki_szczegolne": [
            "STYPENDIUM ERENTZ -- Krzysztof je otrzymal!",
            "Dwa listy od Mamusi przekazane dalej",
            "Rada: niech Mamusia zmieni adres na gazetach",
            "Janusz Klepesz chory, ze szpitala",
            "Bodney wrzesien 1947"
        ],
        "kontekst": "Posrednik gratuluje Krzysztofowi stypendium Erentz. Przekazuje 2 listy od Wandy. Radzi zmienic adres na gazetach (przychodza na Bodney, niepotrzebnie). Janusz Klepesz wrócil ze szpitala."
    },

    # ARG/V/216a -- List Debskiego 'Koniusia' -- mundury, Keresley Hostel
    "juras_216a": {
        "typ": "List odreczny",
        "data": "ok. 1947",
        "jezyk": "polski",
        "nadawca": "Debski 'Koniuś'",
        "adresat": "Krzysztof Gluchowski",
        "strony": ["originals_201_217/20260324_1952556443212415006740829.jpg"],
        "transkrypcja": """[tekst obrócony -- czytany od dolu do gory:]
efekt to olize. uczni[?] imp[?]
stanu 'koniec' a eseno Koncu[?]
dane 'party' do Ciebie.
i ide do tego operanta. Ak-
i poniec że lerivie 14 luty[?]
dr. pna M.[?] chyba podany 4
5 lit. postde otecou(usi 292975)
Ciebie jo otoonji do otecanie[?]
(osoba po Irrancji) do II korp.
placowej. 9 Band Re caly sa
dla mnie po 2 (łyniatecenie[?])
kaldego. Bo dobri[?] Padlcunin[?]

No to rocy
Korny
zainy mnie serdeczna
pozdrowienie
Marian""",
        "pieczecie": [],
        "podpisy": ["Koniuś (Dębski)", "Marian"],
        "osoby": ["Debski Koniuś (nadawca)", "Marian (wspolnadawca)", "Krzysztof Gluchowski (adresat)"],
        "znaki_szczegolne": [
            "Tekst obrócony -- czytany od dolu",
            "Numer 292975 -- identyfikator?",
            "Marian przesyla pozdrowienia -- ten sam co u Krahelskiego?",
            "Wspomina II Korpus i Francje"
        ],
        "kontekst": "List Debskiego z pozdrowieniam od Mariana. Tekst obrócony, trudny do odczytu. Wspomina II Korpus i Francje."
    },

    # ARG/V/216b -- List Mariana -- zjazd, 11 5 KDP, Lucy
    "juras_216b": {
        "typ": "List odreczny",
        "data": "ok. 1947",
        "jezyk": "polski",
        "nadawca": "Marian",
        "adresat": "Krzysztof Gluchowski",
        "strony": ["originals_201_217/20260324_1943446872492370937293977_rot.jpg"],
        "transkrypcja": """i wszystkie papierzy Heckorii[?])
obelaych byto 18 (dlingsza[?]
7 maszyn' -- 11 5 KDP). Prze-
sesem wybreno owy wstine[?]
Kapt Inui[?], V-przesem -- Wocke[?]
Skolosikim[?] a serzem Sektecurm[?]
Kogos z 5-ej.

Janusz ani Wojtek, jeszcze
sie ospitola nie wrocili i jest im
dosliwie sam i nudze sie
okrobenie.

Lucy -- przysila przeprosiny
(na 10 stronicach). Poza tym
nic nowego. Muszie wrocic sialo-
fóm z podtrazemiymi dayoma[?]
-- powod znany...

Koniuś
zalytem serdeczne
pozdrowienie
Marian""",
        "pieczecie": [],
        "podpisy": ["Koniuś", "Marian"],
        "osoby": ["Marian (nadawca)", "Krzysztof Gluchowski (adresat)", "Janusz (w szpitalu)", "Wojtek (w szpitalu)", "Lucy (przysyla przeprosiny)", "Kapt. Inui[?] (wybrany przesem)"],
        "znaki_szczegolne": [
            "11 5 KDP -- 11 kompania 5 Kresowej Dywizji Piechoty",
            "18 osob na zjeżdzie",
            "Lucy przysyla przeprosiny na 10 stronach!",
            "Janusz i Wojtek w szpitalu",
            "Podpisy Koniusia i Mariana"
        ],
        "kontekst": "List Mariana o zjezdzie organizacyjnym (18 osob, 7 maszyn, 11 5 KDP). Wybrali zarząd. Janusz i Wojtek w szpitalu. Lucy przesyla 10-stronicowe przeprosiny. Podpisany przez Koniusia i Mariana."
    },

    # ARG/V/218a -- List Debskiego z Coventry (I) -- Constructional Engineers
    "juras_218a": {
        "typ": "List odreczny",
        "data": "27.9.1947[?]",
        "jezyk": "polski",
        "nadawca": "Debski (Koniuś)",
        "adresat": "Krzysztof Gluchowski",
        "strony": ["originals_201_217/20260324_195422208538623440374049_rot.jpg"],
        "transkrypcja": """Coventry, 27. 9. 47.

Drogi Krzysiu!

W pierwszym rzedzie materialow[?] Cie
podkuszic[?] za to, ze nie odpowiedziales
na moj list z 13 b.m. pisany jeszcze
z Bodney Airfield. 15 b.m. dostalem
Twoj telegram (z 13) i od sam pominne[?]
na poczt[e?]. Lego jednak jeszcze nie bylo
jest i w ciagu z najblizszych dni -- dapoki[?]
nie wyjasnieni[?].

Mieszkam w hostelu dosc dobrze
urzadzonym i jedynym moze bolesnie[?]
jest brak towarzystwa gdyz poradtike[?]
Kieletowi i Antkim w hostelu oraz
kilku podchodrazejnim[?] w pracy mioma[?]
my tu do kogo obdimaci[?]. Reszta
towarzystwa jest bowiem wiova[?], ale pod
typu 'tary z boku' i 'podrygca wrosnieki[?]
ghekliowya[?] drolemo golne treba i gali[?]
nie lubio. Jeli Ci wiadomo odumyj jam[?]""",
        "pieczecie": [],
        "podpisy": ["Koniuś (Dębski)"],
        "osoby": ["Debski Koniuś (nadawca, Coventry)", "Krzysztof Gluchowski (adresat)", "Kielet (kolega w hostelu)", "Antek (kolega w hostelu)"],
        "znaki_szczegolne": [
            "Coventry -- Debski przeniesiony z Bodney",
            "Hostel dla Polakow -- Keresley Hostel?",
            "Brak towarzystwa -- tylko kilku Polakow",
            "Telegram od Krzysztofa z 13 wrzesnia"
        ],
        "kontekst": "Wrzesien 1947. Debski przeniesiony z Bodney Airfield do Coventry. Mieszka w hostelu, brak towarzystwa polskiego -- tylko Kielet, Antek i kilku podchorazych. Czeka na telegram od Krzysztofa."
    },

    # ARG/V/218b -- List Debskiego z Coventry (II) -- 'materyjal na to i na owszem'
    "juras_218b": {
        "typ": "List odreczny",
        "data": "22.10.1947[?]",
        "jezyk": "polski",
        "nadawca": "Debski (Koniuś)",
        "adresat": "Krzysztof Gluchowski",
        "strony": ["originals_201_217/20260324_2013095723694821932849249_rot.jpg"],
        "transkrypcja": """Coventry 22. 10. 47

Kochany Krzysiu!

Slomia to trochy i jeszes[?] ale znow
mi takie wrazenie -- widzialem jes
gorse! Co z Ciebie wyrosnie -- zobaczymy.

Dobre, ze pamietain o moich spra-
wach, postaraj sie jednak umi misc
na[?] 'na glowie' ma i zacac jeli-
mopfrodlej[?]! Nien jeli jest!

U mnie takin 'z tym co i
ownern' spragestovo i mie zanosi sie
na popracz z mojej wylicumi wi-
my, bo materyał 'na to' i na --
ownern 'jest pierwszorzedny i wlosni[?]
i jaksciosa...

W Koidelom jedneli wypodło[?]
co zamordazmayn[?]...""",
        "pieczecie": [],
        "podpisy": ["Koniuś"],
        "osoby": ["Debski Koniuś (nadawca)", "Krzysztof Gluchowski (adresat)"],
        "znaki_szczegolne": [
            "Coventry, 22.X.1947",
            "Ton serdeczno-zartobliwy: 'Co z Ciebie wyrosnie -- zobaczymy'",
            "'Materyjal na to i na owszem jest pierwszorzedny'",
            "Debski o swoich sprawach -- praca?"
        ],
        "kontekst": "Październik 1947. Debski pisze z humorem -- komentuje przyszlosc Krzysztofa. Wspomina swoje sprawy zawodowe ('materyjal pierwszorzedny')."
    },

    # ARG/V/218c -- List Debskiego z Coventry (III) -- Maryla Czechowiczowna
    "juras_218c": {
        "typ": "List odreczny",
        "data": "26.10.1947[?]",
        "jezyk": "polski",
        "nadawca": "Debski (Koniuś)",
        "adresat": "Krzysztof Gluchowski",
        "strony": ["originals_201_217/20260324_2014558418007150941536046_rot.jpg"],
        "transkrypcja": """Coventry 26. 10. 47

Drogi Krzysiu!

Wielka niespodzianka bylo dla
mnie to, ze zapisales sie do kasarni
i jest[es?] juz miedzy 'drabniami
z drabinimi' (to drugie wazniejsze!)
Mysliz, ze ile na tym nie wyjedizes
bo panna oporo nowych 'trasy' a
moze bgdni miedzy mimi mas
interesujacego...

Dziekuje ze tojez 'zaduost' 'posd
pos rejganeli -- i bez dresti'
wierze, ze w pars dni dostane
list od tego 'chrzesty-debelin'!

Tek, tek! To samo nas uszzy!
Je te bobe miegramotny i oko lego
nie sie nie uczyc (w tym beamsie[?]
do konca zycia nie bede umial""",
        "pieczecie": [],
        "podpisy": ["Koniuś"],
        "osoby": ["Debski Koniuś (nadawca)", "Krzysztof Gluchowski (adresat)"],
        "znaki_szczegolne": [
            "Coventry, 26.X.1947",
            "Krzysztof 'zapisal sie do kasarni' -- szkola/kurs?",
            "'Drabnie z drabiniami' -- zartobliwy ton o kobietach?",
            "Debski o nauce -- 'nie bede umial do konca zycia'"
        ],
        "kontekst": "Debski reaguje z humorem na wiadomosc ze Krzysztof 'zapisal sie do kasarni'. Zartuje o 'drabniach' i o wlasnym braku wyksztalcenia."
    },

    # ARG/V/218d -- List Debskiego z Coventry (IV) -- Kolo AK, Jurci Fiodorow
    "juras_218d": {
        "typ": "List odreczny",
        "data": "30.11.1947[?]",
        "jezyk": "polski",
        "nadawca": "Debski (Koniuś)",
        "adresat": "Krzysztof Gluchowski",
        "strony": ["originals_201_217/20260324_2019567151651057515116939_rot.jpg"],
        "transkrypcja": """Coventry 30. 11. 47

Kochany Krzysiu!

Musisz mi nanblizszej przy
najblizszym sproebenim i
najchoudzij[?] ordynesnym[?]
sposobem ze to, ze jestem taki
'jesulła' i Twoj list lety
juz u mnie ok. 1 i typodam[?]
aczkolwisz na odpowiedzi!

Z Kolem AK nie juz nie[?]
zalatwiaj, gdyz przewody
z nimi dosc obfiwne korres-
pondencje i slem sobie wszystko
'poring' i natomiast ciekawe[?]
jestem czy wydrosi to
ksiazke swojej 'kochany
Marylu' ?

Leszek otrzymalem -- nudzi[?]""",
        "pieczecie": [],
        "podpisy": ["Koniuś"],
        "osoby": ["Debski Koniuś (nadawca)", "Krzysztof Gluchowski (adresat)", "Leszek (Krahelski -- wspomniany)", "Maryla (kochana Krzysztofa?)"],
        "znaki_szczegolne": [
            "Coventry, 30.XI.1947",
            "KOLO AK -- Debski prowadzi korespondencje z Kolem",
            "'Kochana Marylu' -- Krzysztof ma dziewczyne?",
            "Leszek (Krahelski) -- 'nudzi'",
            "Debski przeprasza za opoznienie w odpowiedzi"
        ],
        "kontekst": "Listopad 1947. Debski pisze o Kole AK (prowadzi korespondencje, radzi Krzysztofowi nie zalatwiać). Pyta o 'kochana Maryle' -- Krzysztof ma dziewczyne? Wspomina Leszka (Krahelskiego)."
    },

    # ═══════════════════════════════════════════════════════════════
    # SERIA II — Gen. dyw. Janusz Julian Głuchowski (1888-1964)
    # ═══════════════════════════════════════════════════════════════

    # ARG/II/14 — List odręczny Śmigłego-Rydza do Głuchowskiego
    "janusz_014": {
        "typ": "List odręczny",
        "data": "30.XII.1919",
        "jezyk": "polski",
        "nadawca": "Generał-porucznik [Edward Śmigły-Rydz?]",
        "adresat": "Major Głuchowski",
        "strony": ["Kolekcja_Gluchowski_Katalog_Tematyczny_p06_img02.jpeg"],
        "transkrypcja": """Warszawa, dn. 30 Grudnia 1919[?]

Do
J.W.P. Majora Głuchowskiego

Korpus Oficerski Ministerstwa Wojny
przysłał zaproszenie dla mnie i oficerów
artylerii obozujących[?] w Kursarni[?] na poranek noworoczny w
Zamku.
Ze mej strony proszę Pana Majora
o przybycie na Zamek wraz z pozostałymi oficerami pułku o godz.[?]
dn. 1 Stycznia 1919[sic? 1920?] roku.

[podpis nieczytelny]
Generał – porucznik[?]""",
        "pieczecie": [],
        "podpisy": ["Generał-porucznik [podpis nieczytelny — Śmigły-Rydz?]"],
        "osoby": ["Maj. Janusz Głuchowski (adresat)", "Generał-porucznik [Śmigły-Rydz?] (nadawca)"],
        "znaki_szczegolne": [
            "AUTOGRAF GENERAŁA — zaproszenie na poranek noworoczny na Zamku Królewskim",
            "Data 30.XII.1919 — poranek noworoczny na 1.I.1920",
            "Głuchowski jako Major — przed awansem na pułkownika",
            "Zamek Królewski w Warszawie — siedziba władz państwowych",
            "Korpus Oficerski Ministerstwa Wojny — najwyższy szczebel",
            "UWAGA: Katalog datuje ten list na 1935-1939, ale data na dokumencie wygląda na 1919. Do weryfikacji"
        ],
        "kontekst": "Zaproszenie na poranek noworoczny na Zamku Królewskim w Warszawie. Nadawca — generał-porucznik (podpis trudny do odczytu, katalog identyfikuje jako Śmigłego-Rydza). Głuchowski nosi stopień majora, co odpowiada okresowi 1918-1920 (dowódca 3/7 Pułku Ułanów). UWAGA: data na dokumencie (30.XII.1919) nie zgadza się z datowaniem katalogowym (ok. 1935-1939) — wymaga weryfikacji. Jeśli data 1919 jest poprawna, nadawcą może być inny generał."
    },

    # ARG/II/27 — List gen. Sosnkowskiego z Kanady
    "janusz_027": {
        "typ": "List maszynopisowy z odręcznym podpisem",
        "data": "28.V.1964",
        "jezyk": "polski",
        "nadawca": "Gen. broni Kazimierz Sosnkowski",
        "adresat": "Gen. dyw. Janusz Głuchowski",
        "strony": ["Kolekcja_Gluchowski_KATALOG_NAUKOWY_p09_img01.jpeg"],
        "transkrypcja": """Kochany Januszu,

Twój list z dnia 18-go maja (polecony, ale nie listonosz) otrzymałem
dopiero [?] temu, po przyjeździe do Kanady. Odwlekałem z trochę odpowiedzią
na list, bo chciałem zebrać parę informacyj[?] i [nieczytelne].

[...] kto przedwojennych, kto ma dziś Gazetę haków[?] nikt, ani niektó-
rych[?] poszukiwanych. Poruszyło mnie[?] wielce podrzuconym,
że dywizja naszych polskich pod[?] Łosicach. [nieczytelne] poza osiągnięć-
mi, na Komorowski[?][?] Pana Prezydenta Barfasya[?] [?]. List z Londynu od
Generała w Liście pochwytnych[?] pismo na dwie strony[?] — [nieczytelne]
jako jedna biała nieprzystępna piśma, a ta dawana pisałem miesiąc temu

Bardzo zmartwia mnie wiadomość o chorowaniu sytuacji p[ułkownika?][nieczytelne]-
wskiego. [?] Pan go proszę [?] bardzo serdecznie[?] pozdrawiam.

Prosiło mnie o przysłonięcie[?] „trudu swojej" matki[?]. Poprawa
własna[?], że nie dla chcenia[?]. Rzeczywiście od hr[abiego?] Stefana de Roz-
niatowskiego[?] z Austrii[?], nic przeczytane [nieczytelne]
Pragmatyczni, udało stało[?] złożonego[?] wyboru p[ułkowni?]ko[nieczytelne]-
 czego[?], cała[?] mała dóbr[?] świata[?] 500 abonnés[?]. Ale było tylko jednego[?]
artykuł[?] poświęcony przeżyciach[?]. Aby wyciągnąć coś do obiegu (przecież
wydawcy tylko fragmenty i materiały, które dóbr stanie się wystawionych przeżyć) zawarli
 szczególnie wyjaśnień dotyczyło sprzed i wydarzeń.

Prosiłem o przypadku[?] lepiej z patrolu Beliny. Ale wiesz mi powiem-
my[?]. Jadzio każden[?] chciwy z mamy godnej z wyrozmaiłem.

[podpis odręczny]
Kazimierz Sosnkowski

Arundel, P.Qué.
28 maja 1964.""",
        "pieczecie": [],
        "podpisy": ["Kazimierz Sosnkowski (podpis odręczny)"],
        "osoby": [
            "Gen. broni Kazimierz Sosnkowski (1885–1969) — nadawca, Naczelny Wódz PSZ 1943-44",
            "Gen. dyw. Janusz Głuchowski — adresat",
            "Hrabia Stefan de Rozniatowski[?] (wspomniany)"
        ],
        "znaki_szczegolne": [
            "AUTOGRAF NACZELNEGO WODZA PSZ — list prywatny 'Kochany Januszu'",
            "Arundel, Province de Québec — Sosnkowski na emigracji w Kanadzie",
            "28 maja 1964 — 7 miesięcy przed śmiercią Janusza (11.VI.1964 Londyn)",
            "Wspomina patrol Beliny — Siódemka z 2.VIII.1914",
            "Maszynopis z odręcznym podpisem — Sosnkowski miał 78 lat",
            "UWAGA: obraz mały, tekst środkowy trudny do odczytu — wymaga weryfikacji z oryginałem",
            "Porównanie z ARG/II/28-29 (Pro memoria) — ten sam okres korespondencji"
        ],
        "kontekst": "List prywatny gen. Sosnkowskiego do gen. Głuchowskiego, pisany z Arundel w Quebeku 28 maja 1964 — zaledwie kilka miesięcy przed śmiercią Janusza. Sosnkowski (Naczelny Wódz PSZ 1943-44, OB PPS, towarzysz z Legionów) wspomina patrol Beliny i prosi o informacje. Ekstremalnie rzadki autograf — korespondencja Sosnkowski-Głuchowski nieznana na rynku aukcyjnym."
    },

    # ARG/II/36 — List Adama Piłsudskiego do płk. Głuchowskiego
    "janusz_036": {
        "typ": "List odręczny na papeterii z monogramem",
        "data": "17.VIII.1931",
        "jezyk": "polski",
        "nadawca": "Adam Piłsudski",
        "adresat": "Płk. Janusz Głuchowski",
        "strony": ["lbr_II_36_p01.jpg", "lbr_II_36_p02.jpg", "lbr_II_36_p03.jpg", "lbr_II_36_p04.jpg"],
        "transkrypcja": """17/8 '31.

Szanowny Panie Pułkowniku!

Zwracam się do Sz. Pana z
uprzejmą prośbą o pana[?], czy nie
mógłbym otrzymać 2 par koni
do ćwiczenia wogóle[?] dość czasu, bo
jutka[?] samu[?].

W tej chwili otrzymałam[sic] zawia-
domienie iż wagon 12 myśli[?]
jest na st. Morena i że na-
tychmiast wszedł[?] musi być
zebrany.

O ile jest to możliwe proszę będę
o odpowiedź przez ordynansa.

Łączę wyrazie[?] pozdrowienia[?]

A. Piłsudski

[Na kopercie/odwrocie:]
Wielmożny Pan
Pułkownik J. Głuchowski""",
        "pieczecie": [],
        "podpisy": ["A. Piłsudski (podpis odręczny)"],
        "osoby": [
            "Adam Piłsudski (brat Marszałka Józefa Piłsudskiego) — nadawca",
            "Płk. Janusz Głuchowski — adresat"
        ],
        "znaki_szczegolne": [
            "AUTOGRAF BRATA MARSZAŁKA PIŁSUDSKIEGO",
            "Papeteria z wytłoczonym monogramem 'P' (niebieskim) — Piłsudscy",
            "Data: 17 sierpnia 1931",
            "Dotyczy koni do ćwiczeń — kontekst kawaleryjski",
            "Stacja Morena — wagon z końmi",
            "Koperta zaadresowana: 'Wielmożny Pan Pułkownik J. Głuchowski'",
            "4 skany: list, zbliżenie podpisu, monogram P, koperta"
        ],
        "kontekst": "List Adama Piłsudskiego (1869-1935), starszego brata Marszałka Józefa Piłsudskiego, do płk. Głuchowskiego. Adam prosi o użyczenie 2 par koni do ćwiczeń i informuje o wagonie na stacji Morena. Kontekst kawaleryjski — Głuchowski jako dowódca I Brygady Kawalerii (1920-1924) i komendant Wyższych Studiów Wojskowych (1930-1933) dysponował końmi służbowymi. Monogram 'P' na papeterii potwierdza proweniencję od rodziny Piłsudskich."
    },

}

# ═══════════════════════════════════════════════════════════════
# INDEKS OSÓB — automatycznie generowany z transkrypcji
# ═══════════════════════════════════════════════════════════════

def build_person_index():
    """Zbuduj indeks osób ze wszystkich transkrypcji."""
    index = {}
    for sig, data in TRANSCRIPTIONS.items():
        for osoba in data.get("osoby", []):
            # Normalizuj imię (usuń opisy w nawiasach)
            name_clean = osoba.split("(")[0].strip()
            if name_clean not in index:
                index[name_clean] = []
            index[name_clean].append({
                "sygnatura": sig,
                "rola": osoba,
                "data": data.get("data", ""),
                "typ": data.get("typ", ""),
            })
    return index

def build_timeline():
    """Zbuduj oś czasu z dokumentów."""
    timeline = []
    for sig, data in TRANSCRIPTIONS.items():
        timeline.append({
            "sygnatura": sig,
            "data": data.get("data", "brak daty"),
            "typ": data.get("typ", ""),
            "kontekst": data.get("kontekst", ""),
        })
    # Sortuj po dacie (przybliżone)
    return timeline


if __name__ == "__main__":
    print(f"Transkrypcje: {len(TRANSCRIPTIONS)} dokumentów")
    idx = build_person_index()
    print(f"Indeks osób: {len(idx)} unikalnych osób")
    for name, docs in sorted(idx.items()):
        print(f"  {name}: {len(docs)} dok. — {', '.join(d['sygnatura'] for d in docs)}")
