# Wytwarzanie amoniaku, kwasu azotowego(V) i nawozow azotowych

Zrodlo: Honorata Zycka, MEN / Instytut Technologii Eksploatacji, Radom 2006
Jednostka modulowa: 311[31].Z5.04

---

## CZESC I — PRODUKCJA AMONIAKU (metoda Habera-Boscha)

### 1. Produkt i jego wlasciwosci

- **Amoniak (NH3)** — bezbarwny gaz o ostrej woni
- Temp. topnienia: -77,7 C; temp. wrzenia: -33,4 C
- Gestosc w war. normalnych: 0,771 g/dm3; w punkcie wrzenia cieczy: 0,682 g/cm3
- Bardzo dobrze rozpuszczalny w wodzie: w 0 C — 1176 obj. NH3 na 1 obj. wody; w 20 C — 702 obj.
- W roztworach wodnych — jonizacja z wytworzeniem roztworu zasadowego (stala dysocjacji 8*10^-5 — slaba zasada), czasteczki NH4OH NIE wystepuja
- Mieszanina **16-27% NH3 z powietrzem** — wybuchowa przy zetkniecieu z plomieniem
- W tlenie spala sie zoltym plomieniem dajac wode i azot
- Powyzej 700 C — silne wlasciwosci redukujace (rozklad termiczny z wydzieleniem H2)
- W obecnosci katalizatora Pt spala sie do NO i H2O

### 2. Zastosowanie amoniaku

- **80%** — produkcja nawozow sztucznych
- Produkcja NO (polprodukt do HNO3) — metoda Ostwalda
- Czynnik chlodniczy (wysokie cieplo parowania 1,3 kJ/g) — wypierane przez freony, ale wraca po odkryciu ich wplywu na ozonosfere
- Produkcja weglanu sodu (metoda Solvaya)
- Materialow wybuchowych, cyjanowodoru, tkanin syntetycznych, barwnikow

### 3. Surowce

- **Gaz ziemny** — ok. 83% swiatowej produkcji NH3
- Polspalanie ciezkich weglowodorow lub zgazowanie wegla/koksu — ok. 16%
- Elektroliza wody — ok. 0,5%
- **Gaz syntezowy**: 75% obj. H2 + 25% obj. N2

### 4. Glowna reakcja syntezy

```
N2 + 3H2 <=> 2NH3     deltaH0 = -92 kJ/mol
```

Reakcja **odwracalna, egzotermiczna**. Wg reguly Le Chateliera — wydajniejsza przy:
- **nizszej temperaturze** (przesuniecie rownowagi w prawo)
- **wyzszym cisnieniu** (zmniejszenie objetosci — 4 mole substratow -> 2 mole produktu)

Reakcja przebiega BARDZO WOLNO — wymaga katalizatora.

---

## 5. ETAPY PROCESU PRODUKCJI AMONIAKU Z GAZU ZIEMNEGO

Cztery zasadnicze etapy:
1. Odsiarczanie gazu ziemnego
2. Otrzymywanie surowego gazu syntezowego (reforming I + II)
3. Oczyszczanie surowego gazu syntezowego (konwersja CO, usuwanie CO2, metanizacja)
4. Wlasciwa synteza amoniaku

Schemat blokowy (Rys. 1):
```
GAZ ZIEMNY -> ODSIARCZANIE (ZnO) -> PIERWSZY REFORMING -> DOPALANIE (powietrze)
-> KONWERSJA CO -> USUWANIE CO2 -> METANIZACJA -> SPREZANIE GAZU -> SYNTEZA NH3
                                                                         |
Produkty uboczne: ZnS, spaliny, kondensat, gaz odpadowy            -> AMONIAK
Wejscia: para wodna, powietrze, cieplo, energia
```

---

### ETAP 1: Odsiarczanie gazu ziemnego

**Cel**: Usuniecie siarki (H2S + zwiazki organiczne S) do poziomu < 0,5 mg S/m3 (z 40 mg S/m3 w gazociagach PGNiG).

**Dlaczego**: Siarka zatruwaja (dezaktywuje) katalizatory ciagu przygotowania gazu i syntezy NH3. H2S wzmaga korozje aparatury i rurociagów.

**Przebieg**:
1. Gaz ziemny podgrzany do ok. **350 C**
2. Kierowany do reaktora z **katalizatorem kobaltowo-molibdenowym** — nastepuje uwodornienie organicznych zwiazkow siarki
3. Nastepnie **adsorpcja H2S** w adsorberach wypelnionych **tlenkiem cynku (ZnO)**:

```
H2S + ZnO -> ZnS + H2O
```

**Uwagi**:
- Powyzej 400 C — moga tworzyc sie produkty krakowania zanieczyszczajace katalizator
- Wodor do uwodornienia pochodzi z recyrkulacji z wezla syntezy
- Zawartosc S po odsiarczeniu spada do **0,1 ppm**

---

### ETAP 2: Otrzymywanie surowego gazu syntezowego

Metoda: **katalityczna konwersja (reforming) z przegrzana para wodna**

Glowna reakcja:
```
CH4 + H2O -> CO + 3H2     deltaH0 = +206 kJ/mol   (ENDOTERMICZNA)
```

Przebiega w **dwoch etapach**: Pierwszy Reforming + Drugi Reforming (Dopalanie)

Schemat instalacji (Rys. 2):
```
1-sprezarka, 2-komora spalin, 3-konwertor-reformer, 4-dopalacz, 5-kociol-utylizator
```

#### ETAP 2a: Pierwszy Reforming

**Aparatura — Reformer (piec rurowy)**:
- Wielka liczba rur ze stopu **nikiel-chrom** (stal zaroodporna)
- Srednica wewnetrzna rur: ok. **120 mm**, grubosc scianki: **15-20 mm**
- Rury umieszczone w komorze wylozonej wewnatrz materialem termoizolacyjnym
- Rury wypelnione **katalizatorem niklowym (tlenek niklu)** osadzonym na nosniku glinowym

**Warunki procesowe**:
- Odsiarczony gaz mieszany z para wodna w stosunku **1:3**
- Podgrzanie do **500-600 C** w komorze spalin cieplem gazow spalinowych
- Reakcja konwersji zachodzi w temp. **780-830 C**, cisnienie **3,0-3,5 MPa**

**Ogrzewanie**:
- Cieplo z spalania strumienia gazu ziemnego opalowego w komorze pieca
- System boczny ogrzewania — wielka liczba palnikow w rzedach na kilku wysokosciach pieca
- Cieplo wykorzystane do konwersji = tylko **50-60%** calkowitego ciepla spalania
- Reszta ciepla (gorace spaliny) — zagospodarowanie w sekcji utylizacji:
  - podgrzewanie surowcow
  - wytwarzanie i przegrzewanie pary wysokocisnieniowej
  - podgrzewanie mieszaniny para-gaz do rur katalitycznych
  - podgrzewanie wody kotlowej i innych strumieni
- Spaliny ochladzone do **180-250 C** wyrzucane do atmosfery

**Wyjscie**: Mieszanina H2, CO, CO2 + nieprzereagowany metan (~14% w przeliczeniu na gaz suchy) + para wodna

#### ETAP 2b: Drugi Reforming — Dopalanie

**Cel**: Konwersja resztkowego metanu + wprowadzenie azotu (z powietrza) do strumienia gazu

**Aparatura — Dopalacz**:
- Komora z katalizatorem niklowym ulozonym warstwami

**Przebieg**:
1. Gaz procesowy z I reformera (ok. 14% CH4) -> dopalacz
2. Mieszanie ze strumieniem **powietrza** tloczonego sprezarka pod cisnieniem **3,16 MPa**
3. Ilosc powietrza dobrana tak, aby tlen przereagowdal calkowicie z metanem
4. Powietrze przed dopalaczem ogrzewane w komorze spalin do **550 C**
5. Czesciowe spalenie mieszaniny podnosi temperature do ok. **1000 C**
6. Doprowadzenie konwersji metanu do konca
7. Strumien powietrza wnosi stechiometryczna ilosc **azotu** potrzebna do gazu syntezowego

**Wyjscie**: Gaz procesowy zawierajacy **0,2-0,4% CH4**

Chlodzenie do ok. **350 C** w kotlach — cieplo wykorzystane do produkcji **pary przegrzanej wysokocisnieniowej (11,7 MPa)**

**Sklad surowego gazu syntezowego**:

| Skladnik | H2 | N2 | CO2 | CO | CH4 | O2 |
|----------|----|----|-----|----|-----|----|
| % obj.   | 40-50 | 20-22 | 10-15 | 10-15 | 0,2-0,4 | ok. 0,2 |

---

### ETAP 3: Oczyszczanie surowego gazu syntezowego

#### 3a. Konwersja CO

Reakcja:
```
CO + H2O -> CO2 + H2     deltaH0 = -41,2 kJ/mol   (EGZOTERMICZNA)
```

Przebiega w **dwoch etapach** z miedzystopniowym chlodzeniem:

**Konwersja wysokotemperaturowa**:
- Temperatura: ok. **400 C**
- Katalizator: **tlenkowy zelazowo-chromowy**
- CO spada do ok. **3%**

**Chlodzenie** w szeregu wymiennikow ciepla do **200-220 C**

**Konwersja niskotemperaturowa**:
- Temperatura: **200-220 C**, cisnienie: **2,93 MPa**
- Katalizator: **miedziowo-cynkowy**
- CO spada do **0,2-0,4%**

Po konwersji: chlodzenie w wymiennikach do ok. **100 C** — wydzielanie duzej ilosci kondensatu procesowego (zanieczyszczonego produktami ubocznymi)

#### 3b. Usuwanie CO2

Gaz po konwersji CO zawiera ok. **20% CO2** + nadmiarowa para wodna.

**Metoda**: absorpcja (wymywanie) goracym roztworem **weglanu potasu** aktywowanym **dietanoloamina**.

- CO2 na wylocie spada do **100-1000 ppm**
- Regeneracja roztworu (desorber CO2): temp. ok. **100 C**, cisnienie **0,05 MPa**
- Uwolniony CO2 — czesciowo do produkcji mocznika lub innych celow
- Niezagospodarowany CO2 — zrzucany do atmosfery

#### 3c. Metanizacja

**Cel**: Usuniecie resztkowych ilosci CO i CO2 (trucizny katalizatora syntezy NH3)

**Katalizator**: niklowy
**Temperatura**: **350 C**

Reakcje:
```
CO + 3H2 -> CH4 + H2O
CO2 + 4H2 -> CH4 + 2H2O
```

Suma resztkosci CO + CO2 po metanizacji: **< 10 ppm**

Produkty (metan, woda) — musza byc usuniete przed synteza NH3.

---

### ETAP 3d: Sprezanie i osuszanie gazu syntezowego

- **Kompresory odsrodkowe** — sprezanie do **21 MPa** (cisnienie wezla syntezy)
- Podczas sprezania — niewielkie ilosci zanieczyszczonego kondensatu
- Sprezony gaz (po odseparowaniu kondensatu) mieszany ze strumieniem **gazu obiegowego** z konwertora syntezy
- Para wodna rozpuszcza sie w kondensujacym amoniaku w sekcji chlodzenia — usuwana z obiegu

**Dodatkowe osuszanie** (nowoczesne wytwórnie):
- Technika adsorpcyjna na **sitach molekularnych**
- LUB przemywanie strumieniem cieklego amoniaku / cieklego azotu
- Jednoczesne usuwanie sladowych CO i CO2 po metanizacji

---

### ETAP 4: Wlasciwa synteza amoniaku

#### Klasyfikacja instalacji wg cisnienia:
- **Wysokocisnieniowe**: 70-100 MPa
- **Sredniocisnieniowe**: 20-30 MPa (NAJWIEKSZE ZNACZENIE PRZEMYSLOWE)
- **Niskocisnieniowe**: 8-10 MPa

#### Warunki syntezy:
```
N2 + 3H2 <=> 2NH3     deltaH0 = -92 kJ/mol
```
- Katalizator: **zelazo aktywowane** malym dodatkiem **K2O i Al2O3**
- Temperatura: **350-550 C**
- Cisnienie: **20-30 MPa**

#### Przygotowanie katalizatora (kontaktu):
1. Spalic czyste zelazo w tlenie -> **Fe3O4**
2. Zmieszac Fe3O4 z **tlenkiem glinu i tlenkiem potasu (3-7%)**
3. Stapiac w **piecu elektrycznym**
4. Gotowy kontakt = **granulki stopu o srednicy ziaren 3-8 mm**
5. Redukcja Fe3O4 do zelaza nastepuje **w trakcie procesu** w reaktorze syntezy

#### Zatrucie (dezaktywacja) kontaktu:

**Trucizny trwale**: siarkowodor, weglowodory (z wyjatkiem metanu)
**Trucizny przejsciowe**: para wodna

Mechanizm zatrucia para wodna:
```
Fe + H2O -> FeO + H2
```
FeO nie ma dzialania katalitycznego. Przepuszczenie oczyszczonego gazu syntezowego powoduje redukcje FeO do Fe i przywrocenie aktywnosci (ale bedzie nieco mniejsza).

Jesli gaz zle oczyszczony z CO2/CO -> reakcje CO2/CO z H2 daja pare wodna -> posrednie zatrucie kontaktu.

#### Korozja wodorowa (powazny problem):
- Nasila sie ze wzrostem temperatury i cisnienia
- H2 adsorbuje sie na powierzchni stali -> dyfunduje w glab tworzywa
- Gromadzenie H2 w sieci krystalicznej -> naprezenia -> **kruchosc wodorowa** -> pekanie korozyjne
- Odweglenie stali:
```
Fe3C + 2H2 -> 3Fe + CH4
```
- Stal zubozzona w cementyt (Fe3C) — krucha, mniej plastyczna, mniej odporna na wysokie cisnienia
- Metan i wodor redyfunduja do powierzchni — luszczenie stali

#### Konstrukcja reaktora radialnego (Rys. 4):

Elementy: 1-kosz z kontaktem, 2-zewnetrzny plaszcz cisnieniowy, 4-dolna warstwa kontaktu, 5-rura wymiennika ciepla

**Zasada dzialania — przeplyw radialny**:
1. Gaz syntezowy przeplywaja od osi ku scianom, potem wzdluz scian
2. Strumien przechodzi przez cylindryczna przestrzen miedzy zewnetrznym plaszczem cisnieniowym (2) a sciana wewnetrznego wkladu (kosza) (1)
3. **Temperatura plaszcza < 100 C** — ogranicza korozje wodorowa
4. Gaz nagrzewany w przestrzeni miedzyurowej wymiennika ciepla (5) cieplem gazow poreakcyjnych
5. Przeplyw rura centralna z perforowana scianka -> **gorna warstwa kontaktu (3)**: temp. ok. **400 C**
6. REGULACJA TEMPERATURY: Powyzej 500 C kontakt traci aktywnosc!
7. Gaz opuszczajacy 1. warstwe **chlodzony dostrzykiem zimnego gazu syntezowego**
8. Przez gorna warstwe — przeplyw od rury centralnej do przestrzeni pierscien.
9. Przez dolna warstwe (4) — przeplyw w odwrotnym kierunku

**Wydajnosc jednego przejscia**: tylko **15-20%** gazu przereagowuje do NH3 (niekorzystne warunki rownowagowe)

#### Obieg kolowy (Rys. 5 — schemat Habera-Boscha):

Elementy: 1-konwertor syntezowy, 2-chlodnica wodna, 3-separator, 4-kompresor, 5-filtr, 6-chlodnica amoniakalna, 7-separator, 8-reagenty swieze, 9-reagenty zawracane, 10-odprowadzanie cieklego NH3

**Dzialanie**:
1. Nieprzereagowany gaz po chlodzeniu i **wykropleniu cieklego amoniaku** -> separacja
2. Gaz zawracany do reaktora + uzupelnienie strumieniem gazu swiezego
3. Separacja NH3: chlodzenie amoniakalne -> para NH3 skraplana kompresorem amoniaku chlodniczego
4. Konfiguracje petli: wymienniki ciepla, chlodnice powietrzne/wodne/amoniakalne, separatory

#### Gazy obojetne i gaz wydmuchowy:
- Metan i argon wchodza z gazem swiezym -> nagrromadzaja sie w obiegu
- Stale odprowadzanie strumienia **gazu wydmuchowego (resztkowego)**
- Zawartosc inertow w petli: **10-15%**
- Gaz wydmuchowy (H2, N2, CH4, Ar) po przemyciu woda (odzysk NH3) -> na opal
- Nowe instalacje: **rozdestylowanie na frakcje** (wodorowa + azotowa zawracana do procesu, gaz odpadowy na opal)
- Frakcjonowanie — **technika membranowa**

#### Gaz poreakcyjny:
- Zawiera **15-20% NH3**
- Po wielomiesiecznej pracy, gdy aktywnosc spada -> max 10% NH3 = wymiana kontaktu
- Nagle obnizenie = zniszczenie kontaktu (zatrucie lub przegrzanie)

---

### 6. Czynniki wydajnosci produkcji NH3

1. Stopien czystosci gazow + stosunek obj. N2:H2 = **1:3**
2. Aktywnosc katalizatora
3. Optymalna temperatura
4. Mozliwie wysokie cisnienie
5. Obciazenie reaktora
6. Zawartosc NH3 przed i za reaktorem

---

### 7. Samowystarczalnosc energetyczna

- Cieplo z etapow procesu -> produkcja **pary przegrzanej wysokocisnieniowej (>100 atm)**
- Para zasila **turbine parowa** = glowny naped kompresora gazu syntezowego
- Z upustu turbiny: para o cisnieniu zredukowanym -> reforming + turbiny kompresow
- Nowoczesne wytwórnie **nie potrzebuja energii z zewunatrz** — oddaja nadmiar (para/energia elektr.)

---

### 8. Magazynowanie i transport NH3

**Trzy typy zbiornikow**:
1. **Z pelnym chlodzeniem** (ok. -33 C) + system chlodniczy — do wielkich ilosci, maly wyciek przy awarii
2. **Bez chlodzenia** — pod pelnym cisnieniem w temp. otoczenia
3. **Kuliste z niepelnym chlodzeniem** — temp. 0-5 C, cisnienie ok. 5 bar

Zabezpieczenia: alarmy, automatyczne zawory odcinajace, zabezpieczenia przed nadmiernym wzrostem/spadkiem cisnienia, zewnetrzny zbiornik stalowy/betonowy/wal ziemny, system zawracania wycieku, folia polietylenowa/piana.

Transport: cysterny samochodowe, kolejowe, statki, rurociagi przesylowe (cisnieniowe, bez chlodzenia; morskie — cisnieniowe lub chlodzone).

---

### 9. Aparatura cisnieniowa — obsluga i kontrola

- Aparaty gruboscienne, cylindryczne wydluzone, zamkniete plaskimi dnami
- Scianka z jednolitego materialu (wytrzymalosc spawow jest mala)
- Zwykla stal weglowa — dobre wytrzymanie cisnienia i temp., ALE nie odporna na korozje
- Konieczne obliczenia wytrzymalosciowe + kontrola powierzchni narazonych na korozje
- **Urzad Dozoru Technicznego** — przechowuje dokumenty: protokol odbioru, decyzja o dopuszczeniu, protokoly przegladow
- Zagrozenia: rozerwanie aparatu, oderwanie elementow, fala uderzeniowa, kontakt z cieczami/parami/gazami

Schemat instalacji (Rys. 3):
```
1-reformer-konwertor, 2-dopalacz, 3-konwertor wysokotemperaturowy,
4-konwertor niskotemperaturowy, 5-absorber CO2, 6-desorber CO2,
7-metanizator, 8-separator, 9-konwertor syntezowy
```

---

## CZESC II — PRODUKCJA KWASU AZOTOWEGO(V) (metoda Ostwalda)

### 1. Wlasciwosci HNO3

- Gestosc stez. HNO3: 1,50 g/cm3; temp. wrzenia: 86 C
- Mocny kwas — calkowita dysocjacja w roztworach wodnych
- HNO3 i jego sole — silne utleniacze
- Stezony kwas dymi (rozklad):
```
4HNO3 -> 4NO2 + O2 + 2H2O
```
- NO2 — silnie trujacy gaz, nieprzyjemny zapach, brunatne zabarwienie

### 2. Zastosowanie HNO3
- Saletra amonowa, materialy wybuchowe, barwniki
- Przemysl farmaceutyczny
- Oczyszczanie powierzchni metali
- Handel: najczesciej **65% roztwor**

### 3. Trzy etapy metody Ostwalda

1. Utlenienie NH3 tlenem z powietrza do NO (kontakt Pt-Rh)
2. Utlenienie NO do NO2
3. Absorpcja tlenkow azotu w wodzie

**Metody wg cisnienia** (utlenianie / absorpcja):
- Atmosferyczne / atmosferyczne
- Atmosferyczne / podwyzszone (0,4 MPa)
- Podwyzszone / podwyzszone (0,4 lub 0,8 MPa)
- **Kombinowana (0,4 MPa / 0,8 MPa)** — NAJCZESCIEJ STOSOWANA (zasada umiaru technol.)

---

### ETAP 1: Utlenianie amoniaku

Reakcje:
```
4NH3 + 5O2 -> 4NO + 6H2O     deltaH = -905 kJ/mol    (POZADANA)
4NH3 + 3O2 -> 2N2 + 6H2O     deltaH = -1266 kJ/mol   (NIEPOZADANA)
```

**Katalizator platynowo-rodowy**:
- Stop: **93% Pt + 7% Rh**
- Siatki plecione z drutu o grubosci **0,06-0,07 mm**
- Gestosc: **1024 oczka na 1 cm2**
- Stosuje sie **2-4 siatki** prostopadle do kierunku przeplywu (wiecej przy wyzszym cisnieniu)
- Podczas pracy: zmniejszenie wytrzymalosci mechanicznej, unoszenie Pt z gazami, powierzchnia staje sie chropowata (narosla, szczeliny)
- Wrazliwe na: **zwiazki siarki, fluorowodor, acetylen, pyl**
- Czyszczenie: przemywanie rozcienczonym **HCl lub HNO3**
- Wymiana siatek gdy uniesione **1/3 czesci platyny**

**Optymalne parametry** (do 98% wydajnosci utlenienia do NO):
- Temperatura siatki Pt-Rh: **750-850 C**
- Czas zetknięcia gazu z kontaktem: **nie dluzszy niz 0,0003 s**
- Zawartosc NH3 w mieszaninie amoniakalno-powietrznej: **10-11%**

Przy dluzszym czasie lub wyzszej temperaturze -> wieksza reakcja do N2 (niepozadana).

**Aparat kontaktowy (Rys. 10)**:
- Elementy: 1-wkladka ceramiczna, 2-katalizator, 3-kociol parowy (chlodnice)
- Gorna czesc = mieszalnik: sprezarka tloczy powietrze + amoniak
- Cisnienie mieszalnika: **0,4 MPa**
- Mieszanina przeplywaja przez siatki Pt-Rh (pionowo) w temp. **800 C**
- Gazy nitrozowe chlodza sie przeplywajac przez rury kotla parowego (3) — dolna czesc reaktora
- Dalsze chlodzenie: wymiennik + chlodnica wodna

---

### ETAP 2: Utlenianie NO do NO2

```
2NO + O2 -> 2NO2     deltaH = -133 kJ/mol
```

Gaz po utlenieniu NH3: ok. 10% NO, 6% O2, 16% H2O, reszta N2.

**Wazne**: szybkosc utlenienia NO do NO2 **ROSNIE** z obnizeniem temperatury! (wyjatek w chemii)

Reakcje wtorne: dimeryzacja NO2 do N2O4, redukcja NO2 do N2O3.

Regula Le Chateliera:
- Reakcja ze zmniejszeniem objetosci -> **podwyzszenie cisnienia** zwieksza wydajnosc
- Najkorzystniej: **obnizzona temperatura + zwiekszone cisnienie**

---

### ETAP 3: Absorpcja tlenkow azotu w wodzie

```
3NO2 + H2O <=> 2HNO3 + NO     deltaH = -72 kJ/mol
```

Produkty posrednie: nietrwaly HNO2 -> rozklad na HNO3, NO, H2O

Regula Le Chateliera: wydajnosc duza przy **obnizonej temperaturze** i **podwyzszonym cisnieniu**

**Kolumny absorpcyjne**:
- Na kazdej polce **wezownica z woda chlodzaca**
- Jednoczesnie przebiegaja dwie reakcje: utlenianie NO->NO2 i absorpcja NO2->HNO3
- Najlepiej w wodzie lub rozcienczonym kwasie

---

### 4. Schemat technologiczny (Rys. 9)

Elementy: 1a-1d sprezarki, 2-reaktor, 3-wymiennik ciepla, 4-chlodnica wodna, 5-oddzielacz, 6-kolumna dotleniajaca, 7-kolumna absorpcyjna, 8-kolumna bielaca

**Przebieg procesu kombinowanego (0,4/0,8 MPa)**:

1. Sprezarka tloczy powietrze + NH3 do mieszalnika (0,4 MPa)
2. Mieszanina przez siatki Pt-Rh w reaktorze, temp. 800 C -> gazy nitrozowe
3. Chlodzenie w kotle parowym (dolna czesc reaktora)
4. Dalsze chlodzenie: wymiennik + chlodnica wodna
5. Wykroplenie wody, poczatek utleniania NO -> NO2
6. Czesc HNO3 absorbowana w skroplinach -> **10% HNO3** oddzielany w oddzielaczu
7. Gaz z oddzielacza **sprezony do 0,8 MPa** -> kolumna dotleniajaca
8. Kolumna dotleniajaca: utlenienie NO->NO2 + absorpcja NO2 w wodzie
   - Chlodzona wezownicami na polkach
   - Zraszana kwasem obiegowym (z dna i z oddzielacza)
9. Gaz -> **kolumna absorpcyjna** zraszana woda, przeciwpradowe zetk niecie
10. Z dolu kolumny: **kwas 40-50% HNO3**
11. Kwas ma barwe brunatna (NO2) -> **kolumna bielaca**: przeciwpradowo sprezzone powietrze unosi NO2
12. Gazy odlotowe -> wymiennik (ogrzane cieplem gazow nitrozowych) -> energia rozsprezania napedza sprezarki (turbina)

### 5. Zasada umiaru technologicznego

- Absorpcja: lepiej 0,8 MPa (mniejsze aparaty)
- Utlenianie NH3: lepiej cisn. atmosferyczne (mniejsze straty Pt)
- Kompromis: utlenianie przy **0,4 MPa**, absorpcja przy **0,8 MPa**
- Straty ciepla mniejsze (sprezanie tylko 0,4->0,8 MPa)
- Straty Pt nie tak duze jak przy 0,8 MPa

### 6. Sterowanie procesem HNO3

- Stezenie NH3 w mieszaninie (max **12%** — zagrozenie wybuchem!)
- Temperatura siatek Pt
- Obciazenie reaktorow
- Sklad, temperatura, cisnienie gazow/kwasow we wszystkich aparatach
- Gazy nitrozowe NIE MOGA ochlodzic sie ponizej **373 K (100 C)** w dolnej czesci reaktora — skroplenie pary -> HNO3 rozcienczony -> zniszczenie kotla (zwykla stal!)

### 7. Oczyszczanie gazow odlotowych

Emisje: tlenki azotu **NOx** + tlenek azotu(I) **N2O**
- NOx — z niepelnej przemiany w HNO3
- N2O — z czesciowej przemiany NH3

Metoda katalitycznej redukcji (gazem ziemnym/metanem):
```
4NO + 4NO2 + 3CH4 -> 4N2 + 3CO2 + 6H2O
```

NOx szkodliwe zwlaszcza drzew iglastych. Lokalizacja zakladow — z dala od lasow iglastych.

### 8. BHP w zakladach HNO3

- Mieszaniny NH3 z powietrzem wybuchowe: **15,5-26,6%** obj.
- Tlenki azotu toksyczne: max **0,005 mg/dm3** w powietrzu
- NH3 i pary HNO3 toksyczne
- Kwasy i gazy dzialaja parzaco

---

## CZESC III — PRODUKCJA NAWOZOW AZOTOWYCH

### 1. Rodzaje nawozow azotowych

| Typ | Przyklad | % azotu | Forma azotu |
|-----|----------|---------|-------------|
| Na bazie azotanow(V) | Saletra amonowa | 34% | azotanowa NO3- + amonowa NH4+ |
| Na bazie azotanow(V) | Saletrzak | 27% | j.w. + wypelniacz |
| Na bazie mocznika | Mocznik nawozowy | 46% | amidowa NH2+ |
| Siarczanowo-amonowe | Siarczan(VI) amonu | 20% | amonowa NH4+ |
| Roztwory azotowe | RSM | 30% | azotanowa + amonowa + amidowa |

Dzialanie: forma azotanowa — szybkie; amonowa/amidowa — wolniejsze (przemiany w glebie do azotanow)

---

### 2. Produkcja saletry amonowej (NH4NO3)

#### Reakcja glowna:
```
HNO3 + NH3 -> NH4NO3     deltaH0 = -146 kJ/mol   (SILNIE EGZOTERMICZNA)
```

Surowce: **gazowy NH3** + **56% HNO3**

#### Rozklad termiczny NH4NO3 (zagrozenie wybuchem!):
```
NH4NO3 -> NH3 + HNO3                                    (endotermiczna)
NH4NO3 -> N2O + 2H2O                     deltaH = 39,7 kJ/mol
2NH4NO3 -> 2N2 + O2 + 4H2O              deltaH = -102,9 kJ/mol
2NH4NO3 -> N2 + 2NO + 4H2O              deltaH = -41,6 kJ/mol
4NH4NO3 -> 3N2 + 2NO2 + 8H2O            deltaH = -89,1 kJ/mol
5NH4NO3 -> 2HNO3 + 4N2 + 9H2O
```

Reakcje egzotermiczne -> nagrzewanie masy -> przyspieszenie rozkladu -> **GWALTOWNY ROZKLAD = EKSPLOZJA**

Przyspieszaja rozklad: chlorki, HNO3
Spowalniaja: amoniak, mocznik, weglany wapnia i magnezu

#### 4 etapy produkcji:

**Schemat (Rys. 12)**: 1-neutralizator, 2-zbiornik rozprezajacy, 3a/3b-wyparka prozniowa z plaszem grzejnym i wezownica, 4-zbiornik posredni, 5-zbiornik homogenizacyjny, 6-pompa, 7-wyparka koncowa, 8-zbiornik z plaszczem grzejnym, 9-zbiornik naporowy, 10-wieza granulacyjna, 11-przenosniki tasmowe, 12-sito wibracyjne, 13-podznosnik, 14-chlodnica fluidyzacyjna, 15-beben obrotowy pudrujacy

**Etap 1 — Neutralizacja**:
- NIE wprowadza sie NH3 bezposrednio do kwasu (cieplo -> rozklad HNO3 i NH4NO3!)
- W kolumnie neutralizacyjnej utrzymywana pewna ilosc roztworu NH4NO3 zawracanego z dalszego procesu
- Mozliwe pod cisnieniem normalnym lub podwyzszonym
- Cisnienie podwyzszone: surowce podgrzewane cieplem procesu, pary jako zrodlo energii
- Cisnienie normalne: energia z zewnatrz
- Produkt: roztwor NH4NO3 + para z niewielkimi ilosciami NH4NO3 i NH3/HNO3

**Etap 2 — Odparowanie**:
- W wyparkach — przygotowanie do granulacji
- Zawartosc wody spada:
  - < **8%** (dla granulacji mechanicznej)
  - < **1%** (dla granulacji wiezowej)
- Po oziebieniu krzepnie na twarda mase

**Etap 3 — Granulacja**:

a) **Granulacja wiezowa**: wytworzenie kropel z saletry, zestalenie w wiezy powietrzem. Wymaga **99,5% NH4NO3**, temp. > 180 C. ZAGROZENIE WYBUCHEM.

b) **Granulacja mechaniczna**: uzycie roztworu NH4NO3 (**92-96%**) + surowce stale + zawrot (drobne czasteczki z frakcjonowania). BEZPIECZNIEJSZA.

**Etap 4 — Frakcjonowanie**:
- Oddzielenie granulek niespelniajacych norm (podziarno + nadziarno -> zawrot do granulacji)
- Produkt pelnowartosiowy -> opakowania (worki polietylenowe) -> magazyn

#### Oczyszczanie gazow odlotowych:
- Pyly z granulacji: **cyklony, filtry workowe, filtry swiecowe** -> zawrot do procesu
- Koncowe oczyszczanie: **skrubery** z ciecza absorpcyjna + HNO3 (wylapywanie NH3)

#### Oczyszczanie roztworow odpadowych:
- Opary skraplane -> kondensaty zanieczyszczone NH3/HNO3/NH4NO3
- Oczyszczanie oparow przed skropleniem -> scieki 15-25% NH4NO3
- Wykorzystanie sciekow:
  - Ciecz absorpcyjna w produkcji HNO3
  - Surowiec do nawozow plynnych (RSM)
  - Wymiana jonowa / odwrocona osmoza -> odzysk zwiazkow azotu
  - Przemywanie kwasnym roztworem cyrkulacyjnym

#### Dodatki spowalniajace rozklad (bezpieczenstwo):
```
CaCO3 + 2NH4NO3 -> Ca(NO3)2 + 2NH3 + H2O + CO2
MgCO3 + 2NH4NO3 -> Mg(NO3)2 + 2NH3 + H2O + CO2
```
Wydzielajacy sie NH3 hamuje egzotermiczny rozklad NH4NO3.
W sytuacjach awaryjnych: woda zdemineralizowana / kondensat do rozciencania.

#### Zasady magazynowania saletry:
- Suche, czyste pomieszczenia; zabezpieczenie przed wilgocia i naslonecznieniem
- Temp. max **30 C**
- Worki poziomo, max **12 warstw**; uszkodzone osobno
- Min. 20 cm od scian, 150 cm od urzadzen grzewczych
- Przewody elektryczne zabezpieczone
- Max **300 t** w jednym pomieszczeniu
- Zakaz: palenia tytoniu, otwartego ognia, spawania
- Nie przechowywac z: srodkami ochrony roslin, mocznikiem, supedfosfatem, tlenkami metali, kwasami, metalami sproszkowanymi, materialami palnymi, olejami, sloma, cementem

---

### 3. Produkcja mocznika — CO(NH2)2

Mocznik — **46% azotu** — najwiecej ze wszystkich nawozow azotowych

#### Reakcja glowna:
```
2NH3 + CO2 -> NH2-CO-NH2 + H2O
```

Warunki: cisnienie **10-25 MPa**, temperatura **160-200 C**, surowce w fazie cieklej (w gazowej nie reaguja!)

Surowce: **ciekly NH3** + **CO2** (produkt uboczny wytwórni amoniaku)

#### Dwa rownolegle etapy:

**1) Powstawanie karbaminianu amonu** (szybka, egzotermiczna, do konca):
```
2NH3 + CO2 <=> NH2-CO-ONH4     deltaH = -159 kJ
```

**2) Dehydratacja karbaminianu amonu** (endotermiczna, NIE do konca):
```
NH2-CO-ONH4 -> NH2-CO-NH2 + H2O     deltaH = +26 kJ
```

Tylko **50% CO2** ulega przemianie do mocznika. Wyzsza temperatura -> wiecej konwersji, ALE powyzej **200 C** — reakcje uboczne!

#### Reakcje uboczne:

**Powstawanie biuretu (dimocznika)** — powyzej 200 C:
```
2NH2-CO-NH2 <=> NH2-CO-NH-CO-NH2 + NH3
```

**Powstawanie weglanow amonu**:
```
NH3 + CO2 + H2O -> NH4HCO3
NH2-CO-ONH4 + H2O -> (NH4)2CO3
```

#### Nadmiar amoniaku:
- Stosunek molowy NH3:CO2 = **2-5 razy wiecej NH3**
- Problem: wydzielenie czystego mocznika z mieszaniny + odzysk nadmiaru NH3

#### Odzysk z procesu:
- Scieki zawieraja mocznik + nadmiar NH3 + CO2
- **Hydroliza** w podwyzszonej temp. i cisnieniu -> mocznik rozklada sie do CO2 + NH3
- Kierowanie do absorbera -> oddzielenie NH3 i CO2 od sciekow
- NH3 i CO2 **zawracane do procesu**
- Oczyszczona woda -> zasilanie kotlow
- Czesc sciekow -> nawozy plynne (bez oczyszczania)
- Gazy z granulacji -> oczyszczanie -> odzysk NH3 i pylu mocznika -> zawrot

#### Zastosowanie mocznika (poza nawozem):
- Melamina C3H6N6 -> zywice syntetyczne, srodki ognioochronne, impregnaty
- Zywice mocznikowo-formaldehydowe -> kleje
- Zywice melaminowo-mocznikowo-formaldehydowe -> kleje do materialow drewnopochodnych
- Srodki farmaceutyczne (dolegliwosci neurologiczne, dermatologiczne)
- Dodatki do pasz dla bydla
- Herbicydy (srodki chwastobójcze)

---

### 4. Powiazania surowcowo-produktowe w przemysle azotowym (Rys. 13)

```
Surowce: biomasa, woda, powietrze, gaz ziemny, gaz rafineryjny, nafta, wegiel

-> Wytwórnia amoniaku -> NH3 (techniczny + nawozowy)
   |-> CO2 (produkt uboczny) -> wytwórnia cieklego CO2
   |-> NH3 + CO2 -> wytwórnia mocznika -> mocznik nawozowy/techniczny
   |-> NH3 + powietrze -> wytwórnia HNO3 -> techniczny HNO3
       |-> HNO3 + NH3 -> wytwórnia saletry amonowej -> saletra amonowa
       |-> roztwor NH4NO3 + dolomit -> saletrzak (azotan amonu z wypelniaczem)
       |-> roztwory: RMA, RSM, RSA -> nawozy plynne
       |-> HNO3 + NH3 -> wytwórnia nitrofosfatow -> NP
```

RMA = roztwor mocznikowo-amoniakalny
RSM = roztwor saletrzano-mocznikowy
RSA = roztwor saletrzano-amoniakalny

---

## PODSUMOWANIE — KLUCZOWE REAKCJE CHEMICZNE

| Nr | Reakcja | Warunki | deltaH |
|----|---------|---------|--------|
| 1 | N2 + 3H2 <=> 2NH3 | 350-550 C, 20-30 MPa, kat. Fe/K2O/Al2O3 | -92 kJ/mol |
| 2 | CH4 + H2O -> CO + 3H2 | 780-830 C, 3-3,5 MPa, kat. Ni | +206 kJ/mol |
| 3 | H2S + ZnO -> ZnS + H2O | 350 C | — |
| 4 | CO + H2O -> CO2 + H2 | 400 C (wysoko), 200-220 C (nisko) | -41,2 kJ/mol |
| 5 | CO + 3H2 -> CH4 + H2O | 350 C, kat. Ni | — |
| 6 | CO2 + 4H2 -> CH4 + 2H2O | 350 C, kat. Ni | — |
| 7 | Fe + H2O -> FeO + H2 | (zatrucie kontaktu) | — |
| 8 | Fe3C + 2H2 -> 3Fe + CH4 | (korozja wodorowa) | — |
| 9 | 4NH3 + 5O2 -> 4NO + 6H2O | 750-850 C, kat. Pt-Rh | -905 kJ/mol |
| 10 | 4NH3 + 3O2 -> 2N2 + 6H2O | (niepozadana) | -1266 kJ/mol |
| 11 | 2NO + O2 -> 2NO2 | niska temp, wys. cisn. | -133 kJ/mol |
| 12 | 3NO2 + H2O <=> 2HNO3 + NO | niska temp, wys. cisn. | -72 kJ/mol |
| 13 | 4HNO3 -> 4NO2 + O2 + 2H2O | (rozklad stez. HNO3) | — |
| 14 | HNO3 + NH3 -> NH4NO3 | — | -146 kJ/mol |
| 15 | 2NH3 + CO2 -> NH2-CO-NH2 + H2O | 160-200 C, 10-25 MPa | — |
| 16 | 2NH3 + CO2 <=> NH2-CO-ONH4 | etap 1 syntezy mocznika | -159 kJ |
| 17 | NH2-CO-ONH4 -> NH2-CO-NH2 + H2O | etap 2 (dehydratacja) | +26 kJ |
| 18 | 4NO + 4NO2 + 3CH4 -> 4N2 + 3CO2 + 6H2O | oczyszczanie gazow | — |
| 19 | CaCO3 + 2NH4NO3 -> Ca(NO3)2 + 2NH3 + H2O + CO2 | stabilizacja saletry | — |

## PODSUMOWANIE — KATALIZATORY

| Etap | Katalizator | Nosnik/Dodatki |
|------|-------------|----------------|
| Odsiarczanie (uwodornienie) | Kobaltowo-molibdenowy | — |
| Adsorpcja H2S | Tlenek cynku (ZnO) | — |
| Reforming I i II | Niklowy (tlenek Ni) | Nosnik glinowy |
| Konwersja CO (wysoka T) | Tlenkowy zelazowo-chromowy | — |
| Konwersja CO (niska T) | Miedziowo-cynkowy | — |
| Metanizacja | Niklowy | — |
| Synteza NH3 | Zelazo (Fe z Fe3O4) | K2O + Al2O3 (3-7%), granulki 3-8mm |
| Utlenianie NH3 | Stop Pt-Rh (93%/7%) | Siatki, drut 0,06-0,07mm, 1024 oczka/cm2 |

## PRODUKTY UBOCZNE I ODPADY

- **ZnS** — z odsiarczania (zuzyty adsorbent)
- **Spaliny** — z pieca reformera (180-250 C, do atmosfery)
- **Kondensat procesowy** — zanieczyszczony produktami ubocznymi (po konwersji CO)
- **CO2** — z usuwania CO2, czesciowo do mocznika, reszta do atmosfery
- **Gaz wydmuchowy** — H2, N2, CH4, Ar (na opal lub frakcjonowanie)
- **NOx i N2O** — gazy odlotowe z wytwórni HNO3 (redukcja katalityczna)
- **Straty platyny** — unoszenie z siatek (odzysk, wymiana po 1/3 ubytku)
- **Kondensat z oparow NH4NO3** — scieki 15-25% NH4NO3 (odzysk)
- **Pyl z granulacji** — cyklony, filtry, skrubery -> zawrot
- **Biuret** — niepozadany produkt uboczny syntezy mocznika (> 200 C)
