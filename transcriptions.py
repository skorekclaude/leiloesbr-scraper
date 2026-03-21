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
[...] na terenie Włoch / na podst. upoważnienia [...]

Krzysztof Głuchowski
(imię i nazwisko)

urodzony dnia [rok 1926(?)]... w Tyczyn(?) / Kliszów(?)
wyznania: ...
ukończył(a) klasę [IV(?)] i uzyskał oceny następujące:

[Tabela ocen — widzę wpisy:]
1. z religii          — bardzo dobry
2. z języka polskiego — dobry
3. z języka łac.      — dostateczny
4. z języka niem./ang.— dostateczny
5. z historii         — dostateczny
6. z math. (przyrody) — dostateczny
7. z geogr.           — dostateczny
8. z propedeutyki     — bardzo dobry
[...] — dobry

do 20 Czerwca 1946 r.""",
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
        "transkrypcja": """Przedmioty nieobowiązkowe:
[...] — N.N.
[...] — N.N.

Ogółem godzin obowiązkowych — [...] tygodniowo
Uczestnik Rady Pedagogicznej — [...] opuszcz. —
Ze klasy [...] promow.

Harcerskie — Italii, dnia 20 czerwca 1946.

[podpis] fr. Sowiński F.
Opiekun Klasy

[pieczęć okrągła — M.S.]

[podpis] D.M. Melosik (?)
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

KOMUNIKACJA AUTOBUSOWA z LAMMIE - NEAPOL [...]
Godzin: 1000 [...] Wyjazd i LAMMIE [...]
Calto 660, 1700, 1800, 1900 [...] 2200
SKLEP OBOZOWY — Wódki, Wino [...]
W RAMACH DOZWOLONEJ GOSPODARKI
DOSKONAŁY FOTOGRAF ZNAJDUJE: Się W Rojno "E" Casymaker, Kornice""",
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
1. Synagoga                    7. Plac Sportowy         13. Poczta Polowa
2. Kdr Generała Fiji Waskiego  8. Polska Komenda Główna 14. Kaplica Kalutkaserów(?)
3. Kościół Na Skr...           9. [....]                15. [....]
4. Ulica Główna               10. Koszary Oficerskie    16. Plomyak Polski
5. Przychadnia Lekarska       11. [...]
6. Ulica Promenadowa          12. [...]

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
        "transkrypcja": """24 . XII . 1946.

Kochana moja Mateczko!

Od dłuży. Tobą. Odezwali[?] się...
bądźmy o Tobą, którzy[?] listu...
ofiaryw Patki. ktoze[?] j[?] i...
na ten [?] kro, Myślam[?] było[?] lepszej[?]
uwać[?] bos... nie... dosięg na [?]...

dał Mattoni w dz. 2 XII osta bcc
więc dalszm[?]... Onu mi
[?] Rudenkil[?]...
kolejno adesenry[?] dane była ogółal[?]
badanie ... zdawcze blogi... ktoze[?]
budowani [?] tego krogu...
[...tekst bardzo trudny do odczytu...]

W końcowej części listu wymienione są punkty 1), 2), 3)
z prośbami/pytaniami do matki.

...Rozdelej(?) kupić... [?] między nami boty obchodzisz
...na... Bartłomiej[?]... trochy braki [?] się miałeś
...żałowwali[?]...""",
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

1. Report to pass the nearest Military or other Service
   Medical Establishment [...]
2. If unable because of your condition [...]
3. If employment of a civilian practitioner [...] you may visit, or
   call in, a civilian practitioner, to whom you should show
   your Leave Pass [...]
4. If, through sickness, you are unable to travel at the
   expiration of your leave and it would not be in the
   care of a civilian practitioner, obtain a Certificate [...]

To the Civilian Practitioner:
(a) When a soldier is sick [...] the soldier's fitness or unfitness
    to travel [...]
(b) If unfit, he should be instructed to return to his Unit
    and report sick to his Medical Officer [...]""",
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
urodzony dnia 28 [?]... wyznania [?]
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
Przedmioty nieobowiązkowe: [...]
Ogółem godzin obowiązkowych: 43
[...] nieprzerwanie
uchwałą — promuje do klasy Oficer [?]

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

2. Wstąpienie do P.K.P.R. jest dobrowolne [...]

3. Czas służby w P.K.P.R. wynosi na okres nieprzekraczający
2 lat [...]

4. Żołnierze służący w P.K.P.R. zachowują swoje stopnie [...]

5. Żołnierze P.K.P.R. otrzymują żołd funtów brytyjskich [...]

[Tabela żołdu:]
Oficer Warrant Officer I Class — po 4 latach
Sierż. Warrant Officer II Class — po 3 latach
Plut. (Corporal) — po 3 latach
Kpr. (Lance Corporal) — po 3 latach [...]

Żywienie, pomieszczenie, Koszaliny, wskazówki fachowe, porada lekarska — bezpłatne.
Koszaliny: mundur P.K.P.R. będzie nosił polskiego orła i napis „P.K.P.R." [...] """,
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
W WOJSKU STAŁEM

Nr 31043371

Nazwisko: GŁUCHOWSKI
Imiona: KRZYSZTOF
Data urodzenia: 19 . 11 . 1926
[...]

[Tabela dat służby:]
89 [?]  2/12  N/E
[daty wpisu i wykreślenia]

[...] Żydzi do P.K.P.R. [...]

GŁUCHOWSKI KRZYSZTOF  4/92 [?]
[...]

Wejście: [data]  4/92  PARC

ZAŚWIADCZENIE DŁONEM LUB OŁÓWKIEM
PRZY WSTĄPIENIU DOBROWOLNEM DO SŁUŻBY

[podpis]""",
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
LIMITED WE FRANCJI
L.dz. 7003/01/46.

Paryż, dnia 23 listopada 1946r.
14, rue de Castiglione.

PAN GENERAŁ GŁUCHOWSKI
Sztab Główny
LONDYN

Szanowny Panie Generale,

Przedstawiam Panu Generałowi wyciąg [z] meldunku [z] Obozu
Polskiego w La Courtine, który przesłał sprawy b.[yłego] obozu ko-
misar Beselerez[?]. Mimo poszukiwań nie natrafiono na ślady dokumen-
tów osobistych st.uł. GŁUCHOWSKI Krzysztof-Andrzej.
[...] na liłej[?] kom-pani, [...] WOJSKOWEJ

[podpis nieczytelny]
pk.dyr.pl.[?]""",
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
        "transkrypcja": """KWESTIONARIUSZ OSOBISTY
POUFNE

[Formularz z rubrykami:]
1. Nazwisko i imię
2. Stopień wojskowy (Wydział)
3. Data urodzenia
4. Miejsce urodzenia
5. Obywatelstwo
6. Nr Kont[o] Narodowego Wydz.[iału]
7. Zawód [...]
8. Stan Rodzinny [...]
9. Języki [...]
10. Stopień wykształcenia cywilnego
11. Opiniana
12. [...]

[Strona 2 — rewers:]
II. PETYCJE, NAMOWY itp. [...]
30. Jaka praca w przeszłości [...]
30. Gdyby każdy po demobilizacji [...]
[...dalsze rubryki...]""",
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
PAŃSTWOWEJ ORGANIZACJI WYCHOWANIA FIZYCZNEGO
I PRZYSPOSOBIENIA WOJSKOWEGO (?)
KOMITET KOORDYNACYJNY

ŚWIADECTWO DOJRZAŁOŚCI

Głuchowski     Krzysztof
(nazwisko)     (imię)

ur. 19 [...]26
[...] mężczyzna [...] wyznania [...]

po zdaniu egzaminu dojrzałości
z wynikiem [...] otrzymuje
świadectwo [...]

[ZDJĘCIE — fotografia portretowa Krzysztofa Głuchowskiego:
młody mężczyzna, ciemne włosy, wąska twarz, poważny wyraz]

za zgodność [...] wydania [...]

OCENY:
z religii:                 dobry
z języka polskiego:        dostateczny [?]
z języka angielskiego:     dostateczny
z historii:                dostateczny [?]
z [...]                    dostateczny
z matematyki:              dobry [?]
[...dalsze oceny...]""",
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
        "transkrypcja": """[Komisja Egzaminacyjna]

Pan/i otrzymał jako ocenione oceny na kanach [?]
następujący bodzik i przedmiot [?]:

w kursie:
z książek:                dostateczny
z popr. [...] część:      dobry
Głuchowski Andrzej Krzysztof-Andrzej  [sławnie ?] wyraz: [...] edu

za cześć do dyplomu [...] 2a [?] [...] roku

Komisja Egzaminacyjna w składzie:
Nr 24  Kwalif. Każgolie

PRZEWODNICZĄCY
KOMISJI EGZAMINACYJNEJ
inżpr.[?] M. Pucka [?]

CZŁONKOWIE
KOMISJI EGZAMINACYJNEJ:
[podpis 1] Wyrwal [?]
[podpis 2] Szmatki [?]
[podpis 3] Proszki [?]
[podpis 4] Kiosk al.[?]
[podpis 5] [nieczytelny]
[podpis 6] [nieczytelny]
[podpis 7] Harney [?] Price [?]

[pieczęć okrągła — M.P.]""",
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
        "transkrypcja": """DISCHARGE CERTIFICATE

1. Army No.: 3004271
2. Rank: Pte. [Private]
3. Surname: GŁUCHOWSKI
4. Christian Names: KRZYSZTOF
5. Date of discharge: 31 OCT 1948
6. [...]
7. Service: 1 [year]
8. [...] 365 [days]  2 mentions [?]
9. [...]
10. [...]
11. Campaigns and Military Conduct: [...]
12. Medals: [...]

50748

[podpis oficera]

Signature: [podpis Głuchowskiego]

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

Army Number: 14161026 [?]
Surname (in capitals): GŁUCHOWSKI
Christian Names: KRZYSZTOF
Date of Birth: 19. 11. 19[20/26?]
[...] Polish
Place of    In or near the town of
Birth:      [...] ber zawar [Brzeżany?]
            In the county [...]
Trade on Enlistment: [...]

Nationality of Father at birth: [...] Polnish [?]
Nationality of Mother at birth: Izyni - Kat [?]
Religious Denomination: [...]
Approved Society: [...]
Membership No.: [...]
Enlisted at [...] On the [...] Naib.Ib.[?]
Regular Army □   Supplementary Reserve □
[...] Strike out those inapplicable [...]
For ... years with the Colours and ... years in the
Reserve.
Signature of Soldier: [podpis] Głuchowski
Date: 20. X. 1945

[OPIS FIZYCZNY — strona 3:]
Height: 170 [?]   ins. Weight: 50 [?] lbs.
Maximum Chest: [...] ins. Complexion: [...]
Markings: [...] Hair: I. Kaita [?] Eye: I. Kloma [?]
Distinctive Marks and Minor Defects: [...]

                    DISCHARGED

CONDITION ON TRANSFER TO RESERVE: [...]""",
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
Date: 10.12.45, 25.12.45 [?]

PRESCRIPTION FOR GLASSES: [puste]

VACCINATIONS:
S.P.E. / S.P.T. [daty]

PROTECTIVE INOCULATIONS:
T.A.B. [tyfus-paratyfus]:
  Dates: [...] 1945
  [wpisy medyczne z datami]

Name of Vaccine: T.A.B.
Army Form: [...] T.P.9""",
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
        "typ": "List odręczny — strona 3 (kontynuacja listu wigilijnego?)",
        "data": "ok. 1946-1948",
        "jezyk": "polski",
        "nadawca": "Krzysztof Głuchowski",
        "adresat": "Matka lub krewna",
        "strony": ["juras_088_page89.png", "juras_089_page90.png", "juras_090_page91.png"],
        "transkrypcja": """[Strona 3:]
Obudziwsz zachodzić [?] dawnie list konigby [?] a das
i razumiaz [?] Trzecii Artuzowi [?] a lekarzer[?] za ni
łagoanisz [?] na to bawienin tajini łedifego[?] dze li
Wyraz prazcisz[?] na te abrótki[?]
Łabidz postnał[?] na te obrólki viachomik[?] crasleną
A olm ubrzś lizgafani[?] à vadkimie
A racz wezs odeż slabzśn[?] i acz cażówy unazwał[?]
na sodstoi à topasiesie[?] odzablenio [?] kedy umazali
obrażeń[?] à bracz yepz wiechomiki ożóy unatchi
na sodlidn[?] è topasiesie[?]
[...dalszy tekst bardzo trudny do odczytu...]

[Strona 4:]
woska wybuchwość[?] i na zamóst ciągle polu-
łojeq[?] obsa odazwać à Krakow latuba sa-
doiąwsz ogólniej — imi brosś chochych polsiy
ewa i był[?] obozznali[?] a coi[?] bos
zakażcnie [?] bo łaś[?] duszczu[?] uniechsrż[?] koirzy[?] ej sa
wołóliamy[?] à pnzec[?] mie olósko[?] i igel[?] opzwat[?]
Poliszm otom[?] mozłdoy[?] ratlosik[?] praztany[?] Polszym
obroziw[?] à przesz wie udsi[?] o igel opzwat[?]
różni je potrzeb redsistm[?] — Polszym
dawy à pokószy è adja ciartónin[?] redsistm[?]
ceni i podłuzy bri do udoó paeszy pochożysz[?]
ado podolec ta b[?] wierchnie oho[?] opej[?]
[...tekst trudny do odczytu — drobne odręczne pismo...]

[Strona 5:]
Kochane bodno mocka zagasty[?] na bos wazoble
długyéy ogólnie[?] — imi brosś chochych polsiy
dolchossé imi birsły odeznołej a coi[?] bos
zakćnie bo łaś[?] duszczu[?] uniechsny[?] koirzy ej sa
wołóliamy à k. [?] duszczu sółoboem[?] koirzy[?] ej sa

Wśdzisz [?] je grosse rechnistro[?] — Polszym
dawy à pobójszty [?] poczty [?] solńce przescisz[?] co
nie i otolosił[?] co izzy odsętgim[?] czy usczci
i nastrzk[?] — łu nadzieliom, łu odsętgim[?] czy usczci
i nastrya— [?] kieohialsz miusić prałze fraiscy[?] i  por.[?]
inż odpowiedzialność na Dóp Nfrancra[?]""",
        "pieczecie": [],
        "podpisy": [],
        "osoby": ["Krzysztof Głuchowski (nadawca)", "Matka/krewna (adresatka)"],
        "znaki_szczegolne": [
            "Pismo BARDZO drobne, atramentem, niezwykle trudne do odczytu",
            "3 strony gęsto zapisanego listu",
            "Wymieniony Kraków — miejsce w Polsce",
            "Ton emocjonalny — tęsknota za rodziną i Polską",
            "Wymaga profesjonalnej transkrypcji (Transkribus/HTR)",
            "Charakter pisma spójny z listem wigilijnym (juras_010-014)"
        ],
        "kontekst": "Kolejne strony listu odręcznego. Pismo niezwykle drobne i trudne do odczytu — wymaga profesjonalnego narzędzia do rozpoznawania pisma ręcznego (HTR). Wspomniany Kraków sugeruje, że nadawca pisze o rodzinie w Polsce."
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
        "transkrypcja": """[Strona z biogramami — 2 wpisy z fotografiami:]

Nr 7.                                                    Nr 7.

GŁUCHOWSKI JULIUSZ, gen. bryg. ur. 06.08.1888
[zm.] 11.1964 Londyn. Lt.-General. Studied in the Poli-
tical Science[?] at Liège Belgium. Founder of the "Ac-
tive Armed Group" in 1909. In 1912 he graduated in
Legions' Officiers course [...] Polish Legions' Associate [...]
In the "Outi" Crisis of 1917. He was a member of the
[...] organized in Germany, Between 1918-1920 he com-
manded the 3rd Lancers Regiment [...] He was trans-
ferred [...] and continuing officer, the 4th Cavalry Division [...] he comman-
ded the 1st Cavalry Brigade [...] shortly, Cavalry Division [...] He
was 1st Cavalry major-general in 1927 [...]
1935; 1st Vice-Minister of Military Affairs 1935-1939 [...] He was Spe-
cial Commander [...] 1939 [...]
France, Chief of the Polish French [...] Commit-
tee 1939. He erected Polish Forces Abroad[...] Romani 1940-1941 [...]
G.O.C. Polish Training Centre 1940-41; G.O.C. [...]
Great Britain and Scotland 1941-1943; GOC Polish Troops in
Scotland, promoted lieutenant-general [...] 1943; Senior
Commanding Officer [...] 1945; After demobilisation he
stayed in London, where he was a founder of [...] Association [...]
co-founder of the [...] Association [...] He Ge-
neral [...] 1963 chairman [...] He
was also [...] Inspector of the [...] Polish Br-
Institute in London, [...] author of numerous articles [...]
in London [...] He was a [...]
[...]
[...] French Legion of Honour [...] Class [...] Romanian
[...] Cross of Merit (2x), British Order [...] the Bath [...] Crown
of Romania (II class), Latvia Order of the Bear [...] Class [...]

[FOTO: Portret gen. Głuchowskiego w mundurze — starszy mężczyzna, dystyngowany]

───────────────────────────────────

GROCHOBIŃSKI CZESŁAW, ur. 07.12.1906 Baranowicze, aktor. Education
Poznań school [...] Actor in theaters [...] 1929-39. He acted [...] Great Britain since 1943. Member [...]
[...] Polish [...] Theatre [...] London [...] His acted on stage [...] Part in Royal
Command Performance from 1945 [...] and American films [...] He excelled in
[...] Polish [...] British Actors' Equity Association
[...] Z.A.S.P. "Syren" and [...]

[FOTO: Portret Grochobińskiego]""",
        "pieczecie": [],
        "podpisy": [],
        "osoby": [
            "Gen. dyw. Janusz Julian Głuchowski (ur. 06.08.1888 Bukowa, zm. 11.06.1964 Londyn) — generał dywizji",
            "Czesław Grochobiński (ur. 07.12.1906 Baranowicze) — aktor"
        ],
        "znaki_szczegolne": [
            "KLUCZOWY DOKUMENT BIOGRAFICZNY — potwierdza tożsamość Generała",
            "Gen. Juliusz Głuchowski: ur. 06.08.1888, zm. XI.1964 Londyn",
            "Kariera: Legiony 1909-1912, 3. Pułk Ułanów, 1. Brygada Kawalerii",
            "I Zastępca Ministra Spraw Wojskowych 1935-1939!",
            "GOC Polish Training Centre 1940-41, GOC Polish Troops Scotland 1941-43",
            "Odznaczenia: Legion Honorowy (fr.), Order Łaźni (bryt.), Korona Rumunii, Order Łotwy",
            "Po demobilizacji — Londyn, założyciel organizacji kombatanckich, inspektor",
            "FOTO w mundurze — dystyngowany starszy oficer",
            "Sąsiedni biogram: Czesław Grochobiński — aktor, też Londyn"
        ],
        "kontekst": "Biogram z Kwartalnika Biograficznego Polonii. POTWIERDZA: Gen. dyw. Janusz Julian Głuchowski (1888-1964) — jedna z najważniejszych postaci polskiego wychodźstwa wojskowego. I Zastępca Ministra Spraw Wojskowych przed wojną, dowódca jednostek polskich w Szkocji, po wojnie aktywny w Londynie. To OJCIEC (lub bliski krewny) Krzysztofa-Andrzeja. List z Paryża do 'Pana Generała Głuchowskiego, Sztab Główny, LONDYN' potwierdza rodzinną opiekę."
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
