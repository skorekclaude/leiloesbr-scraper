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
        "kontekst": "Biogram z Kwartalnika Biograficznego Polonii. POTWIERDZA: Gen. dyw. Janusz Julian Głuchowski (1888-1964) — jedna z najważniejszych postaci polskiego wychodźstwa wojskowego. I Zastępca Ministra Spraw Wojskowych przed wojną, dowódca jednostek polskich w Szkocji, po wojnie aktywny w Londynie. BRAT Stefana Głuchowskiego (urzędnika Kancelarii Cywilnej Prezydenta RP). Krzysztof to SYN STEFANA."
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
        "transkrypcja": """[...] Ojczyzny

Pragnę przedstawić [opis?] [...] Kiedat[?]
[...] [St.] Marszałka [...] na [...]
[...] w [...] gdzie [...] Marszałka na [...]
[...] generał [...] [rajony?] [...]
moje [...] na [...] co [...]

[...] ze 100
[...] to [...] [...]

[Dwa?] [...] posiadały [...] [plk?] [...] od [...]
[...] [...]
[...] w [...] i w [...]
[...] [piłka?] [polu?] [...]
— i Polska kogo — [...] nie jest [...] dnia
[...] a [...] bo u [...] [...]

[...] bo [...] byli [...] [dalekich] polityków

od Marszałka [...] w [...] [...]
po tej pierwszej walcze[niu] w 1918 [...] [kupił?] polsk[ie]""",
        "pieczecie": [],
        "podpisy": [],
        "osoby": ["Marszałek (Józef Piłsudski)", "Stefan Głuchowski (?)"],
        "znaki_szczegolne": [
            "Wspomnienia o Marszałku Piłsudskim i wydarzeniach z 1918 roku",
            "Pismo odręczne atramentem na kremowym papierze",
            "Wiele fragmentów nieczytelnych — wyblakły atrament",
            "Wspomina 'Pierwszą walkę w 1918' — odzyskanie niepodległości",
            "Kontekst: rodzina Głuchowskich i Piłsudski — Siódemka Beliny"
        ],
        "kontekst": "Fragment wspomnień dotyczących Marszałka Piłsudskiego i wydarzeń z 1918 roku — odzyskania niepodległości. Gen. Janusz Głuchowski był jednym z Siódemki Beliny (1914) i bliskim współpracownikiem Piłsudskiego. Rękopis prawdopodobnie sporządzony przez Krzysztofa na podstawie opowieści rodzinnych lub jako próba spisania historii rodziny."
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
1) Tragiczne widmo — fenho [Szekspir?/Wyspiański?]
2) Klawisze (kości z ogniskami)
3) Moja najciekawsza przygoda.

[Uczeń wybrał temat 3]

Gdy [myślę] o moich przygodach, biorę poważnie [...]. W kształ-
cie ich bo jedna z moich większych przygód. Było to moim pierw-
szym [przeżyciem] [dwóch] lat już [...]

Było to dnia 1 sierpnia 1944r. w Warszawie. Armia Kra-
jowa przygotowywała się do [walki]. Pamiętam [jak] [...] i do-
bry [...] w moim [oddziale]. Pamiętam najdokładniej.

Moja placówka miał numer 1112. Był [ok.] 16 [ludzi] [...]
umundurowanych. [...] w [blokach/blankietach] [...]
na ostatnich chwili moja placówka przeniesiona została do fabryki
mebli przy ul. [Pięknej?]. O godzinie 15:00.

O[koło] godziny 16:30 po ukonczeniu bram — [...] w [...]
jako do boju [...]  — obowiązki [...] bram [...]
[w bloku.] [w] fabryki, oficerzy fabryki [...]
[...] obudzony. [Spr.?] Jerzy [Konieczn?] [...]
[...] Podtem [...]

[...] w [...] było możliwości, [...] po warunki AK
[...] przystali. Składała się z 28 dwóch [żołnierzy] i jednego [...]
[...] karabinów z 8 szkolny[mi] petardami. [Amunicja?] [...]
było. Rozkaz [komunikować] [...]  ludzi co [byli] za [...]

Ja nadstawiałem [...] w [...]""",
        "pieczecie": [],
        "podpisy": [],
        "osoby": ["Krzysztof Głuchowski", "Spr. Jerzy Konieczny (?)"],
        "znaki_szczegolne": [
            "BEZCENNA RELACJA Z PIERWSZEJ RĘKI — 19-letni powstaniec pisze o 1.VIII.1944",
            "Zadanie klasowe w Gimnazjum 3 DSK we Włoszech, rok po Powstaniu",
            "Placówka nr 1112 — ten sam numer batalionu potwierdzony w innych dokumentach",
            "28 żołnierzy, 8 petard szkolnych — skromne uzbrojenie",
            "Fabryka mebli przy ul. Pięknej (?) — punkt zborny przed godziną W",
            "Godzina 15:00 — zbiórka, 16:30 — przygotowania do walki",
            "Pismo atramentem na papierze liniowanym (EXERCISE BOOK)",
            "Wiele fragmentów trudnych do odczytania — pismo drobne, gęste"
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
Gimnazjum 3DSK

Lektura.

Czytam artykuły różnych ludzi o Powsta-
niu Warszawskim... Porównuję [je] bo artykuły ludzi, którzy
nie byli w nim [nie brali?] udziału. [Wejście?] się [w niuanse?] rze-
czy w Warszawie. Wydaje [się?] [...] o [...] [wszystkim?] [...]
nie mieli, Warszaw[a] [...] o pracy [...] artystycznego, ale
nie twórczej i informacji. W Warszawie [...]
[...] Armia Krajowa posiadała swoją organizaj[cję]
i dolne społeczne. To nie był[y?] [...] sobie [...]
[...] [spontanicznie] chcący do [walki] — to był żołnierz,
który w ciężkich [warunkach] [...] [przygotow-]
ał się, i [mundur?] [...] prac[ował] do Powstania.
Warszawskiej Armii [...] tylko [spotykali?] [ludzi?]
[wiadomy?] był pod każdym względem. Z [każdej strony?] [...]

Czytaj[ąc] jeden z artykuł[ów] p. Nowakowskiego
[...] — [między?] [...] danymi. Chłodnym [warszaw?]
przyszli do Powstania [...] nie [walczyli?] o [...]  ale [...] pan
Nowakowski nie [pisał?] [tak]. [P. Nowakowski?] [uważa?] [...]
[...] nie [współuczestnik?]; że właśnie [ludzie?] [...]
[...]  z żołnierzy Armii Krajowej. Pluton[ów] które
miały nasze [wyznac?][zone?] [zadani?]a w plana[ch] opanowa[nia]
Warszawy.

W Warszawie, [w] tych chwilach [...] [na] [...]
[...] szalona [wymiana?] wielka, [...] praca
organizacyjna i [zakończona?] [...]  — [...] Polacy. —

K.""",
        "pieczecie": [],
        "podpisy": ["K. (Krzysztof Głuchowski)"],
        "osoby": ["Krzysztof Głuchowski", "p. Nowakowski (autor artykułów)"],
        "znaki_szczegolne": [
            "Esej krytyczny — powstaniec polemizuje z publicystami, którzy nie walczyli",
            "Wspomina p. Nowakowskiego — prawdopodobnie Tadeusz Nowakowski (pisarz emigracyjny)",
            "Podkreśla profesjonalizm AK: 'to nie byli spontanicznie chcący do walki — to był żołnierz'",
            "Krytykuje autorów piszących o Powstaniu bez osobistego udziału",
            "Wspomina plany opanowania Warszawy i organizację plutonów AK",
            "Nagłówek: Polish Forces CMF 152, Gimnazjum 3DSK"
        ],
        "kontekst": "Esej analityczny napisany 3 sierpnia 1945. 19-letni Krzysztof czyta artykuły o Powstaniu i polemizuje z autorami, którzy nie brali w nim udziału. Broni profesjonalizmu Armii Krajowej — podkreśla, że żołnierze AK nie byli spontanicznym tłumem, lecz wyszkolonymi żołnierzami z planami i organizacją. Krytykuje p. Nowakowskiego (prawdopodobnie Tadeusza Nowakowskiego, pisarza emigracyjnego) za błędne przedstawienie motywacji powstańców. Fascynujący dokument — głos 19-latka, który SAM walczył, wobec publicystów, którzy PISALI o walce."
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
