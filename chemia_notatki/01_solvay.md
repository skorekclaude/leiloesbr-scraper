# Wytwarzanie sody kalcynowanej -- metoda Solvaya

> Zrodlo: Poradnik MEN, Urszula Zlobinska, Instytut Technologii Eksploatacji, Radom 2006
> Jednostka modulowa 311[31].Z5.05

---

## 1. Produkt i nazwa metody

- **Produkt**: soda kalcynowana = **bezwodny weglan sodu Na2CO3**
- **Metoda**: metoda amoniakalna Solvaya (1872 r., belgijski inzynier Ernest Solvay)
- Zastapila starsza metode Leblanca (1791 r., Francja)

### Nazwy potoczne produktow przemyslu sodowego

| Wzor | Nazwa chemiczna | Nazwa potoczna |
|------|----------------|----------------|
| Na2CO3 | weglan sodu | soda, soda amoniakalna, soda kalcynowana |
| NaHCO3 | wodorweglan sodu | soda oczyszczona, bikarbonat |
| NaOH | wodorotlenek sodu | soda zraca, soda kaustyczna |

### Zastosowania sody

Produkcja soli, farb, srodkow pioracych, klejow, oczyszczanie produktow naftowych, przemysl papierniczy, skorzany, wlokienniczy, metalowy, szklarski, spozywczy.

W polskim przemysle chemicznym przemysl sodowy zajmuje **drugie miejsce** pod wzgledem wielkosci produkcji (po kwasie siarkowym).

---

## 2. Surowce

### Surowce podstawowe

1. **Sol kamienna (NaCl)** -- dostarczana rurociagami jako nasycony roztwor (solanka).
   - Stezenie: **300-315 g NaCl / 1 dm3**
   - Nie moze zawierac jonow Ca2+, Mg2+, SO4(2-)
   - Pozyskiwanie: podziemne rozpuszczanie zloz soli woda (lugowanie)
   - Zaklady sodowe lokalizuje sie w poblizu zloz soli kamiennej

2. **Kamien wapienny (CaCO3)** -- do wypalania (zrodlo CO2 i CaO)
   - Musi zawierac **nie mniej niz 90% CaCO3**
   - Dostarcza dwoch produktow: CO2 (do karbonizacji) i CaO (do gaszenia -> mleko wapienne)

### Surowce pomocnicze

3. **Amoniak (NH3)** -- reagent pomocniczy (nie wchodzi w sklad koncowego produktu)
   - Dostarczany jako 25% woda amoniakalna z zakladow azotowych
   - Krazy w obiegu zamknietym -- straty ok. **2 kg NH3 na tone sody**
   - Uzupelniany tez z regeneracji (z rozkladu NH4Cl)

4. **Woda** -- do gaszenia wapna, plukania, jako rozpuszczalnik

5. **Koks** -- paliwo do pieca wapiennego (spalanie dostarcza ciepla do rozkladu CaCO3)

### Zuzycie surowcow na 1 tone sody kalcynowanej

| Surowiec | Ilosc |
|----------|-------|
| Solanka oczyszczona (310 g NaCl/dm3) | 5,0 m3 |
| Woda amoniakalna (25% NH3) | 10,0 kg |
| Kamien wapienny (100% CaCO3) | 1100 kg |
| Koks (wartosc opalowa 29,3 * 10^3 kJ/kg) | 90 kg |
| Woda | 75 m3 |

Wydajnosc procesu w stosunku do NaCl: **70-75%**

---

## 3. Wszystkie reakcje chemiczne

### Reakcja sumaryczna calego procesu

```
CaCO3 + 2NaCl --> Na2CO3 + CaCl2
```

Z reakcji sumarycznej wynika, ze surowcami sa jedynie wapienie i solanka; amoniak krazy tylko w obiegu.

### Reakcje poszczegolnych etapow

**A) Rozklad termiczny kamienia wapiennego (wypalanie)**
```
CaCO3 --> CaO + CO2          dH = +164 kJ (endotermiczna, odwracalna)
```

**B) Gaszenie wapna**
```
CaO + H2O --> Ca(OH)2         dH = -66,7 kJ (egzotermiczna)
```

**C) Oczyszczanie solanki (metoda sodowo-wapienna)**
```
Mg(2+) + Ca(OH)2 --> Mg(OH)2 (osad) + Ca(2+)
Ca(2+) + Na2CO3 --> CaCO3 (osad) + 2Na(+)
```

**D) Absorpcja amoniaku w solance**
```
2NH3 + 2H2O --> 2NH3*H2O              dH = -35,2 kJ
CO2 + H2O --> H2CO3                    dH = -24,7 kJ
2NH3*H2O + H2CO3 --> (NH4)2CO3 + 2H2O  dH = -92,2 kJ
```
Wszystkie egzotermiczne -- konieczne chlodzenie!

**E) Karbonizacja solanki amoniakalnej (sumaryczna)**
```
NaCl + NH3 + H2O + CO2 --> NaHCO3 + NH4Cl
```

Karbonizacja -- reakcje skladowe:
```
2NH3 + H2O + CO2 --> (NH4)2CO3
(NH4)2CO3 + H2O + CO2 --> 2NH4HCO3
NH4HCO3 + NaCl --> NaHCO3 (krystalizuje) + NH4Cl (zostaje w roztworze)
```

Reakcja karbonizacji jest **odwracalna**:
```
NH4HCO3 + NaCl <=> NaHCO3 + NH4Cl
                <=>
         NH3 + CO2 + H2O
```

**F) Kalcynacja (prazenie) wodorweglanu sodu**
```
2NaHCO3 --> Na2CO3 + H2O + CO2         dH = +67,7 kJ (endotermiczna)
```

Rozklad zanieczyszczen obecnych w osadzie:
```
NH4HCO3 --> NH3 + H2O + CO2            dH = +139 kJ
(NH4)2CO3 --> 2NH3 + H2O + CO2          dH = +207 kJ
```

Reakcja niekorzystna (pogarsza czystosc sody):
```
NH4Cl + NaHCO3 --> NaCl + CO2 + NH3 + H2O   dH = +156 kJ
```

**G) Regeneracja amoniaku (chemiczna)**
```
2NH4Cl + Ca(OH)2 --> 2NH3 + CaCl2 + 2H2O
```
Weglany amonu rozkladaja sie juz termicznie w temp. 50 C (regeneracja termiczna).

### Metoda Leblanca (historyczna, do porownania)
```
2NaCl + H2SO4 --> Na2SO4 + 2HCl
Na2SO4 + 2C + CaCO3 --> Na2CO3 + CaS + 2CO2
```

---

## 4. Etapy procesu -- szczegolowy opis

### ETAP 1: Wypalanie kamienia wapiennego

**Cel**: Otrzymanie CaO (wapna palonego) i CO2 (do karbonizacji)

**Reakcja**:
```
CaCO3 --> CaO + CO2    dH = +164 kJ
```

**Warunki**:
- Reakcja endotermiczna i odwracalna
- Preznosc rownowagowa CO2 nad CaCO3 jest duza juz w 898 C
- Proces prowadzony w **1000-1100 C** (wyzsza temp. zwieksza szybkosc reakcji)
- Temperature osiaga sie przez spalanie koksu
- Wazny: odpowiedni stosunek ilosciowy i granulacja kamienia i koksu

**Aparat: Szybowy piec wapienny z nadmuchem powietrza** (nr 16 na schemacie)

Budowa pieca:
- Sciany z trzech warstw cegiel; wewnetrzna -- **cegla szamotowa** (termoodporna)
- Od gory: **rury wsypowe** z pokrywami i zamknieciami (zapobiegaja wydostawaniu sie gazu przy zaladunku)
- Od dolu: urzadzenie wyladowcze = **zeliwny slimak + karuzela** (rynna zbiorcza) + **lamacz walcowy** (rozdrabnia wapno na kawalki ok. 10 cm srednicy)
- **Dmuchawa** wdmuchuje od dolu powietrze do spalania koksu

Strefy pieca (od gory do dolu):
1. **Strefa podgrzewania** (gora) -- wsad (wapien + koks) wsypany od gory chlodzi gazy odlotowe, sam sie susząc i podgrzewajac (zasada najlepszego wykorzystania energii)
2. **Strefa wypalania** (srodek) -- najwyzsze temperatury, rozklad CaCO3 dzieki cieplu spalania koksu w powietrzu wdmuchiwanym od dolu
3. **Strefa chlodzenia** (dol) -- wapno oddaje cieplo wplywajacemu powietrzu (zasada najlepszego wykorzystania energii)

Czynniki dobrej pracy pieca:
- Wlasciwy stosunek wapienia i koksu we wsadzie + dobre wymieszanie
- Rownomierny zasyp surowca
- Wyladowywanie wapna z odpowiednia predkoscia
- Odpowiedni nadmuch powietrza
- Calkowite napelnienie pieca i wlasciwe polozenie strefy wypalania

---

### ETAP 2: Oczyszczanie gazow z pieca wapiennego

**Aparat: Skruber** (nr 17 na schemacie) -- wypelniony kawalkami koksu

Przebieg:
- Gaz z pieca zawiera pyl i pare wodna (z wody w wapieniu i koksie)
- W skruberze: gaz chlodzi sie i czesciowo odpyla
- Dalsze odpylanie: **filtr trocinowy** (gaz przeciska sie przez warstwy trocin na tkaninie workowej)
- Stosuje sie tez **elektrofiltry**

---

### ETAP 3: Gaszenie wapna

**Reakcja**:
```
CaO + H2O --> Ca(OH)2    dH = -66,7 kJ (egzotermiczna)
```

**Aparat: Aparat bebnowy do lasowania wapna** (nr 18 na schemacie)

Produkt: **mleko wapienne** = zawiesina Ca(OH)2 w wodzie

Zastosowania mleka wapiennego:
- Regeneracja amoniaku z NH4Cl (z przesaczu po filtracji NaHCO3)
- Oczyszczanie solanki
- Ewentualnie do produkcji NaOH

Warunki gaszenia:
- Woda do gaszenia o temperaturze **50-60 C** (wymagane duze stezenie mleka + podwyzszona temp. w procesie regeneracji + latwiejszy transport)

---

### ETAP 4: Oczyszczanie solanki (metoda sodowo-wapienna)

**Cel**: Usuniecie jonow Ca2+, Mg2+ (i Fe) z solanki -- gdyby pozostaly, przy nasycaniu CO2 i NH3 wytracity sie osady CaCO3 i MgCO3 powodujace zarastanie aparatow i rurociag ow.

**Reakcje**:
```
Mg(2+) + Ca(OH)2 --> Mg(OH)2 (osad) + Ca(2+)
Ca(2+) + Na2CO3 --> CaCO3 (osad) + 2Na(+)
```

Jony magnezu usuwane wodorotlenkiem wapnia, jony wapnia -- roztworem sody.

**Aparatura** (numery wg schematu rys. 2):
1. **Mieszalnik** -- przygotowuje stezone roztwory mleka wapiennego i sody
2. **Reaktor (zbiornik reakcyjny, nr 1)** -- mieszanie solanki z reagentami
3. **Odstojnik (nr 2)** -- rozdzial: szlam (odpad) opada, klarowny roztwor solanki z gory
4. **Zbiornik solanki oczyszczonej (nr 3)** -- gotowa solanka idzie dalej do kolumn absorpcyjnych

Szlam = produkt odpadowy

---

### ETAP 5: Absorpcja amoniaku w solance

**Cel**: Nasycenie solanki amoniakiem (CO2 zle rozpuszcza sie w czystej solance, dobrze w solance amoniakalnej)

**Reakcje** (egzotermiczne -- konieczne chlodzenie!):
```
2NH3 + 2H2O --> 2NH3*H2O              dH = -35,2 kJ
CO2 + H2O --> H2CO3                    dH = -24,7 kJ
2NH3*H2O + H2CO3 --> (NH4)2CO3 + 2H2O  dH = -92,2 kJ
```

**Aparat: Kolumna absorpcyjna amoniaku** (nr 4+5 na schemacie) -- zbudowana z **zeliwnych kregow**

Budowa kolumny absorpcyjnej -- dwie czesci:

**A) Czesc gorna (skruber/pluczka)**:
- Wypelnienie koksowe
- Funkcja: odzyskiwanie resztek NH3 z gazow odlotowych z kolumn karbonizacyjnych
- Gazy stykaja sie ze swieza solanka (przeciwprad)
- Solanka splywa nizej przez **zamkniecie syfonowe** do czesci dolnej

**B) Czesc dolna (wlasciwy absorber)**:
- Aparat polkowy z **polkami passetowymi**
- Solanka (coraz bogatsza w NH3) splywa z polki na polke przez **rurki przelewowe umieszczone na zewnatrz kolumny**
- Stopniowy wzrost temperatury -> solanka chlodzona w **zewnetrznej chlodnicy ociekowej do 30 C** i wracana na nizsze polki
- Na nizszych polkach styka sie z gazem o duzym stezeniu NH3 (wprowadzanym od dolu)

**Chlodnice ociekowe (nr 6, 7)** -- chlodza solanka amoniakalna po opuszczeniu absorbera, przed skierowaniem na kolumny karbonizacyjne

**Parametry pracy**:
- Cisnienie: **zmniejszone, 0,05-0,06 MPa** (proznia)
  - Zwiekszenie cisnienia sprzyja absorpcji, ale zwieksza ulatnianie NH3 przez nieszczelnosci
  - Kompromis: zmniejszone cisnienie = mniejsze straty NH3 + mniejsze zagrozenie srodowiska (zasada umiaru technologicznego)
- Temperatura: chlodzenie do **30 C** (reakcje egzotermiczne podnosza temp., co hamuje absorpcje)
- Stezenie: kontrola stezenia NH3 w solance (miareczkowanie kwasem) -- zbyt duze stezenie NH3 zmniejsza rozpuszczalnosc NaCl -> moze wytrącic staly NaCl ("zasolenie aparatury")
- Stosuje sie solanka **niecalkowicie nasycona NaCl** (zapobieganie zasoleniu)

**Zaklócenia ruchowe**:
- Zla praca pompy prozniowej -> spadek prozni (wzrost cisnienia)
- Nieszczelnosci aparatury
- Przegrzanie absorbera -> zahamowanie absorpcji + wzrost objetosci gazow -> straty NH3
- Wahania stezenia NH3 z powodu zlej pracy kolumny regeneracji (nr 14)
- Zbyt duze stezenie NH3 -> zasolenie absorbera (zatkanie otworow polek passetowych i przelewow, zatkanie rurociag ow)

---

### ETAP 6: Karbonizacja solanki amoniakalnej

**Cel**: Przemiana NaCl w NaHCO3 (polprodukt do otrzymania sody)

**Reakcja sumaryczna karbonizacji**:
```
NaCl + NH3 + H2O + CO2 --> NaHCO3 + NH4Cl
```

**Reakcje skladowe** (kolejnosc):
```
1) 2NH3 + H2O + CO2 --> (NH4)2CO3        (zaczyna sie juz w kolumnie absorpcyjnej)
2) (NH4)2CO3 + H2O + CO2 --> 2NH4HCO3
3) NH4HCO3 + NaCl --> NaHCO3 (krystalizuje) + NH4Cl (zostaje w roztworze)
```

NaHCO3 krystalizuje w dolnej czesci karbonatora (chlodzonego woda), NH4Cl jako lepiej rozpuszczalny zostaje w roztworze.

**Aparat: Kolumna karbonizacyjna (wieza karbonizacyjna Solvaya)** (nr 8-11 na schemacie)

Budowa kolumny karbonizacyjnej:
- Zbudowana z **kilkudziesieciu zeliwnych kregow** o srednicy **1,8-2,8 m**, kazdy z jedna polka
- **Polka passetowa (passeta/paseta)**:
  - Jeden duzy otwor w srodku, nakryty **plaskim dzwonem**
  - Polka i pokrywa maja **kilkaset otworow** (przez nie przeplywaja gazy)
  - Zwieksza kontakt gazow z ciecza
  - Zapobiega osiadaniu krysztalow NaHCO3 na dnie kolumny
- W dolnej czesci: passety podzielone **poziomymi chlodnicami rurowymi**
- Calkowita wysokosc kolumny: **ok. 30 m**
- Kolumna jest aparatem **belkotkowym** (nie zraszanym!) -- do pewnej wysokosci calkowicie wypelniona cieczą

Elementy kolumny (wg rysunku wieza karbonizacyjna):
1. Doprowadzenie solanki amoniakalnej (gora)
2. Doprowadzenie CO2 -- gaz ubozszy 40% CO2 (z pieca wapiennego) w polowie wysokosci
3. Doprowadzenie CO2 -- gaz bogatszy 70% CO2 (z kalcynacji + piec) od dolu
4. Odprowadzenie roztworu z osadem (dol)
5. Woda chlodzaca (wejscie/wyjscie)
6. Gazy odlotowe (gora)

**Parametry pracy**:

- **Temperatura**:
  - Gorna czesc: wyzsza temp. -> hamuje szybkosc wytracania sie osadu -> tworza sie **grubokrystaliczne zarodki** NaHCO3 (korzystne dla filtracji)
  - Srodkowa czesc: **60 C** (przekroczenie 60 C -> rozklad NH4HCO3 i ulatnianie NH3!)
  - Dolna czesc: chlodzenie woda -> **25-28 C** zawiesiny odbieranej z dolu -> podnosi wydajnosc
- **Cisnienie**: **0,2 MPa**
  - Zapobiega dysocjacji termicznej NH4HCO3
  - Przesuniecie rownowagi w kierunku NaHCO3
  - Wieksze cisnienie nieekonomiczne (koszty tloczenia gazow) -- zasada umiaru technologicznego
- **Stezenia**:
  - Stosunek molowy: **1,1-1,2 czasteczki NH3 na 1 czasteczke NaCl** (optymalny)
  - Zbyt duze stezenie NH3 zmniejsza rozpuszczalnosc NaCl
  - Wzrost stezen NaCl, NH3, CO2 zwieksza wydajnosc NaHCO3

**Prowadzenie ruchu**:
- Po kilkudziesieciu godzinach pracy: opory przeplywu rosna (osadzanie krysztalow) -> **konieczne plukanie**
- Kolumny grupuje sie w **baterie (4-7 sztuk)**, kolejno plukane
- Plukanie: przepuszczanie przez kolumne calej ilosci solanki + gaz z piecow wapiennych (wstepna karbonizacja w kolumnie plukanej = "kolumna-karbonator", nr 8)
- Korki z krysztalow usuwane **przedmuchiwaniem para**
- Zrodla CO2:
  - Gaz z pieca wapiennego: **40% CO2** (do polowy wysokosci kolumny)
  - Gaz z kalcynacji NaHCO3: **~95% CO2**, mieszany z gazem z pieca -> **70% CO2** (do dolu kolumny)

Obowiazki zalogi oddzialu karbonizacji:
- Regulowanie przeplywu cieczy przez karbonator i kolumny produkcyjne
- Regulowanie doplywow gazu do wszystkich kolumn
- Regulowanie chlodzenia kolumn i utrzymanie temperatury

---

### ETAP 7: Filtracja wodorweglanu sodu

**Cel**: Oddzielenie krysztalow NaHCO3 od lugu macierzystego (mleczko bikarbonatowe)

**Aparaty** (alternatywnie):

**A) Obrotowy filtr prozniowy (nr 13)** -- rysunek 6
- Budowa: beben filtru (1), zbiornik zawiesiny (2), mieszadlo (3), rolki wygniatajace osad (4), noz (5)
- 5 stref pracy bebna:
  - I -- saczenie (prozniowa)
  - II -- przemywanie (prozniowa)
  - III -- podsuszanie osadu (prozniowa)
  - IV -- strefa obojetna
  - V -- strefa nadcisnieniowa (oczyszczanie tkaniny filtracyjnej)

**B) Wirowka pozioma o dzialaniu ciaglym** -- rysunek 7
- Budowa: oslona (1), klosz perforowany (2), slimak zbierajacy osad (3), doplyw zawiesiny (4), doplyw wody do przemywania (5), zsyp do wilgotnych krysztalow (6)

**Warunki filtracji**:
- Im grubsze krysztaly, tym lepsza filtracja
- Osad na filtrze plukany woda o temp. **40 C** (wyplukanie zanieczyszczen)
- Woda powyzej 40 C -> rosnie rozpuszczalnosc NaHCO3 (przechodzi do przesaczu -- straty!)
- Rownomierne przedmuchiwanie -- kilkunastominutowa przerwa zatkania pory tkaniny!

**Produkty filtracji**:
- **Osad**: 75-80% NaHCO3, male ilosci NaCl i soli amonowych, wilgotnosc < 15% H2O -> kierowany do kalcynacji
- **Przesacz**: sole amonowe + rozpuszczone gazy (z rozkladu weglanow pod zmniejszonym cisnieniem) -> kierowany do **regeneracji amoniaku**

Kontrola: analiza zawartosci poszczegolnych jonow w przesaczu i w osadzie.

---

### ETAP 8: Kalcynacja (prazenie) wodorweglanu sodu

**Cel**: Termiczny rozklad NaHCO3 do Na2CO3 (soda kalcynowana) -- ostatnia faza procesu

**Reakcja glowna**:
```
2NaHCO3 --> Na2CO3 + H2O + CO2     dH = +67,7 kJ (endotermiczna)
```

**Reakcje towarzyszace** (rozklad zanieczyszczen):
```
NH4HCO3 --> NH3 + H2O + CO2        dH = +139 kJ
(NH4)2CO3 --> 2NH3 + H2O + CO2      dH = +207 kJ
NH4Cl + NaHCO3 --> NaCl + CO2 + NH3 + H2O   dH = +156 kJ  (niekorzystna! pogarsza czystosc sody)
```

Wysoka temperatura sprzyja ostatniej reakcji (szybkie uchodzenie gazow).

**Aparat: Piec obrotowy (nr 19)** -- rysunek 8
- Budowa: mieszalnik (1), rury grzejne (2), naped (3)
- Praca ciagla
- Ogrzewanie **przeponowe** gazami spalinowymi z palenisk weglowych lub gazowych (gazy nie stykaja sie z produktem bezposrednio!)
- Najpierw NaHCO3 sie dosusza, potem ulega rozkladowi termicznemu

**Parametry**:
- Temperatura odbieranej sody: **150 C** (stopien rozkladu NaHCO3 zadowalajacy)
- **Szczelnosc pieca bardzo wazna** -- gaz z pieca powinien zawierac ok. **95% CO2**

**Gaz z kalcynacji** tloczony do kolumn karbonizacyjnych (zawracanie do obiegu -- zasada najlepszego wykorzystania surowcow). Mieszany z gazem z piecow wapiennych -> 70% CO2 -> podawany do dolu kolumn karbonizacyjnych.

**Dodatkowy proces: Soda ciezka**
- Beben/krystalizator (nr 20) do otrzymywania sody bezwodnej o duzym ciezarze nasypowym (soda ciezka)

---

### ETAP 9: Regeneracja amoniaku z lugu pofiltracyjnego

**Cel**: Odzyskanie NH3 z przesaczu pofiltracyjnego (zawiera weglany amonu i NH4Cl)

**Dwie metody**:

**A) Metoda termiczna**: Weglany amonu juz w temp. **50 C** zaczynaja sie rozkladac z wydzieleniem NH3 i CO2

**B) Metoda chemiczna**: Rozklad NH4Cl mlekiem wapiennym:
```
2NH4Cl + Ca(OH)2 --> 2NH3 + CaCl2 + 2H2O
```

**Aparat: Kolumna odpedowa (regeneracyjna) amoniaku (nr 14)**

Budowa i dzialanie:
- **Czesc gorna**: wypelnienie koksowe
  - Przesacz z filtracji kierowany od gory
  - Po drodze ogrzewa sie cieplem uchodzacych z kolumny gazow (NH3, CO2, para wodna)
  - Przeciwpradowe zetknięcie ogrzanej cieczy z oparami z dolnej czesci -> weglany ulegaja rozkladowi, NH3 odpedzany
- **Czesc dolna**: zbudowana jak kolumna absorpcyjna -- polki z dzwonem i boczne przelewy cieczy
  - Goraca ciecz mieszana z mlekiem wapiennym w **mieszalniku (nr 15)** i wprowadzana do dolnej czesci
  - Czynnik grzewczy: **przegrzana para wodna** podawana od dolu (belkotka)
  - Z dolu odbierany **odpadkowy roztwor CaCl2** (z domieszkami NaCl i NH4Cl)

**Gaz z kolumny regeneracyjnej** (zawierajacy odzyskany NH3) -> po ochlodzeniu -> **do kolumny absorpcyjnej** (nr 4) -- zamkniecie obiegu amoniaku

**Wspolpraca kolumn**: Kolumna regeneracyjna (14) i absorpcyjna (4) scisle wspolpracuja -- zmiany cisnienia na jednej odczuwalne w calym ukladzie.
- Wzrost cisnienia moze wynikac z przegrzania kolumny regeneracyjnej -> nalezy zmniejszyc ilosc pary do belkotki.

---

## 5. Schemat ideowy procesu -- opis aparatow (numery wg rys. 2)

| Nr | Aparat | Funkcja |
|----|--------|---------|
| 1 | Zbiornik reakcyjny | Mieszanie solanki z reagentami oczyszczajacymi |
| 2 | Odstojnik | Sedymentacja szlamu, klarowanie solanki |
| 3 | Zbiornik solanki oczyszczonej | Magazyn solanki oczyszczonej |
| 4 | Kolumna do plukania gazow z kolumny karbonizacyjnej | Gorna czesc kolumny absorpcyjnej -- skruber/pluczka |
| 5 | Kolumna absorpcyjna amoniaku | Nasycanie solanki amoniakiem |
| 6, 7 | Chlodnice ociekowe solanki amoniakalnej | Chlodzenie solanki amoniakalnej przed karbonizacja |
| 8 | Kolumna karbonizacyjna (karbonator) | Kolumna plukana -- wstepna karbonizacja |
| 9, 10, 11 | Kolumny karbonizacyjne produkcyjne | Wlasciwa karbonizacja -- wytwarzanie NaHCO3 |
| 12 | Sprezarka | Tloczenie gazow |
| 13 | Obrotowy filtr prozniowy | Filtracja NaHCO3 z zawiesiny |
| 14 | Kolumna odpedowa amoniaku | Regeneracja NH3 z lugu pofiltracyjnego |
| 15 | Mieszalnik mleka wapiennego | Mieszanie cieczy z mlekiem wapiennym przed regeneracja |
| 16 | Piec wapienny | Wypalanie CaCO3 -> CaO + CO2 |
| 17 | Skruber | Oczyszczanie gazow z pieca wapiennego |
| 18 | Aparat bebnowy do lasowania wapna | Gaszenie CaO -> Ca(OH)2 (mleko wapienne) |
| 19 | Piec obrotowy do kalcynacji NaHCO3 | Prazenie NaHCO3 -> Na2CO3 |
| 20 | Krystalizator/beben | Otrzymywanie sody ciezkiej (bezwodnej, duzy ciezar nasypowy) |

### 4 zintegrowane wezly technologiczne

1. **Wezel I**: Wypalanie wapienia i gaszenie CaO (piec wapienny + skruber + aparat bebnowy)
2. **Wezel II**: Oczyszczanie solanki i absorpcja amoniaku (reaktor + odstojnik + kolumna absorpcyjna + chlodnice)
3. **Wezel III**: Karbonizacja i kalcynacja (kolumny karbonizacyjne + filtr + piec obrotowy)
4. **Wezel IV**: Regeneracja amoniaku (kolumna odpedowa + mieszalnik mleka wapiennego)

---

## 6. Wazne uwagi, zasady technologiczne i BHP

### Zasady technologiczne stosowane w procesie

1. **Zasada najlepszego wykorzystania energii** -- przeciwprad w piecu wapiennym (wsad chlodzi gazy, powietrze chlodzi wapno); ogrzewanie przesaczu cieplem gazow z kolumny regeneracyjnej
2. **Zasada umiaru technologicznego** -- cisnienie w absorberze zmniejszone (kompromis miedzy wydajnoscia a stratami NH3); cisnienie w karbonizacji 0,2 MPa (wieksze nieekonomiczne)
3. **Zasada najlepszego wykorzystania surowcow** -- obieg zamkniety NH3 i CO2; zawracanie CO2 z kalcynacji do karbonizacji
4. **Zasada najlepszego wykorzystania roznic cisnien i stezen** -- w karbonizacji

### Zagrozenia BHP -- amoniak

Amoniak (wg Kart Charakterystyki):
- **Wodny stezony roztwor NH3**: R23 (toksyczny przez drogi oddechowe), R34 (powoduje oparzenia), R50 (bardzo toksyczny dla organizmow wodnych)
- **Amoniak bezwodny**: dodatkowo R10 (latwo palny)
- Zagrozenie: dziala toksycznie przez drogi oddechowe, powoduje oparzenia

### Kontrola procesow

- Pomiary: temperatura, cisnienie (w absorberze, kolumnach karbonizacyjnych, piecu)
- Oznaczenia: stezenia roztworow, stosunku NaCl do NH3, zawartosci skladnikow, stopnia przereagowania
- Szybkie analizy ruchowe: miareczkowanie kwasem (stezenie NH3)
- Kontrola skladu gazow (% CO2)
- Analiza jonow w przesaczu i osadzie po filtracji

---

## 7. Produkty uboczne i odpady

### Glowny produkt uboczny: CaCl2 (chlorek wapnia)

Sklad cieczy odplywajaccj z kolumn odpedowych:

| Substancja | Ilosc [kg/m3] |
|------------|---------------|
| NaCl | 56,0 |
| CaCl2 | 112,0 |
| Zawiesiny: Ca(OH)2, CaCO3, CaSO4, SiO2 | 21,0 |

Na 1000 kg sody przypada ok. **10 m3** zasolonych sciekow zawierajacych ok. **1000 kg CaCl2** i **500 kg NaCl**.

### "Biale morza" -- problem historyczny

- Dawniej ciecz kierowano do wielkich osadnikow ziemnych ("biale morza")
- Zawiesiny ulegaly dekantacji, klarowny roztwor soli odprowadzano do odbiorkow wodnych
- Osadniki zajmowaly znaczne obszary -- problem na terenach zaludnionych
- Kierowano tam tez: osady z oczyszczania solanki, osad CaCO3 z kaustyfikacji, inne odpady (~200 kg na 1000 kg sody)

### Wspolczesne zagospodarowanie odpadow

1. **Wapno nawozowe** z zawiesiny:
   - Ciecz z kolumny regeneracyjnej -> odstojniki -> separacja na wirowkach
   - Osad plukany woda (zmniejszenie chlorkow) -> powtorne odwirowanie
   - Suszenie w **suszarniach fluidalnych** -> granulowane wapno nawozowe (~40% CaO)

2. **Chlorek wapnia (CaCl2)**:
   - Z roztworu odpadkowego otrzymuje sie CaCl2 * 2H2O (sol dwuwodna)
   - Proces: roztwor -> odstojniki -> oczyszczanie chemiczne Ca(OH)2 i CaSO4 -> odparowanie w **prozniowych wyparkach wielodzialowych**
   - W miare zate?ania wydziela sie NaCl (oddzielany na wirowkach)
   - Dalsze zatezanie -> stop o zawartosci ok. 25% wody -> mozna platkowac

   Zastosowania CaCl2:
   - Suszenie gazow
   - Pylochlon (wiazanie pylu na drogach)
   - Dodatek do zapraw budowlanych w zimie

3. **Szlam z oczyszczania solanki** -- utylizacja jako:
   - Wapno nawozowe
   - Surowiec do przemyslu cementowego

---

## 8. Bilans ogolny procesu

**Wejscie**: CaCO3 + 2NaCl (+ NH3 w obiegu + woda + koks jako paliwo)

**Wyjscie**: Na2CO3 (produkt glowny) + CaCl2 (produkt uboczny/odpad)

**Zalety metody Solvaya**:
- Surowce w stanie plynnym/gazowym -> transport rurociagami
- Amoniak w obiegu zamknietym (male straty)
- Prostszy proces niz metoda Leblanca
- Brak uciazliwych gazow HCl (jak w metodzie Leblanca)
- Brak odpadow stalych CaS (jak w metodzie Leblanca)

**Wady**:
- Duze ilosci sciekow z CaCl2 i NaCl
- Niepelna wydajnosc (70-75% w stosunku do NaCl)
- Koniecznosc zakladu w poblizu zloz soli
