# Przemysl azotowy - Schematy i aparatura

Notatki z materialow pomocniczych do wycieczki technicznej do Z.A. "Pulawy"
Oprac. oryginal: dr B. Chmiel, dr W. Grzegorczyk

---

## 1. SCHEMAT OGOLNY - Otrzymywanie podstawowych zwiazkow azotowych

Schemat blokowy calego lancucha produkcyjnego, wychodzacy od NH3 jako surowca centralnego:

```
                            NH3
                           /    \
                          /      \
            Synteza mocznika    Utlenianie amoniaku
                 |                      |
            Rozprezanie          Absorpcja tlenkow azotu
                 |                      |
         Odparowywanie             HNO3 (kwas azotowy)
           i suszenie                   |
                 |               Zobojetniane (+ NH3)
            CO(NH2)2                    |
           /        \              NH4NO3 (saletra amonowa)
   Topienie i     Mocznik         /          \          + CaCO3
   granulacja   krystaliczny  Granulacja   Mieszanie ---------> Saletrzak
       |                         |
   Mocznik                   Saletra
  granulowany               amonowa
```

**Surowce wejsciowe:** NH3, CO2, powietrze, CaCO3
**Produkty koncowe:** Mocznik (krystal./granul.), Saletra amonowa, Saletrzak, Kwas azotowy

---

## 2. GAZ SYNTEZOWY - Teoria

### 2.1 Definicja
Gaz syntezowy to wieloskladnikowa mieszanina gazowa (glownie CO + H2) przeznaczona do syntez chemicznych. Surowy gaz syntezowy zawiera takze CO2, N2 oraz zanieczyszczenia (H2S, H2O).

**Gaz syntezowy do produkcji NH3:** teoretycznie H2 (75% obj.) + N2 (25% obj.)

### 2.2 Zrodla wodoru
- Zgazowanie paliw stalych (wegiel kamienny, brunatny, koks)
- Zgazowanie paliw cieklych (nafta, ciezkie oleje, odpady porafineryjne)
- Konwersja/rozdzial paliw gazowych (gaz koksowniczy, gaz ziemny, gazy porafineryjne)
- Elektroliza wody (rzadko - duze zuzycie energii)

### 2.3 Zrodla azotu
- Fizycznie: skraplanie (adiabatyczne rozprezanie) + rektyfikacja powietrza
- Chemicznie: zwiazanie tlenu w procesie wytwarzania gazu syntezowego

### 2.4 Metody produkcji gazu syntezowego z gazu ziemnego

| Metoda | Reakcja | Uwagi |
|--------|---------|-------|
| Rozklad termiczny CH4 | CH4 -> C + 2H2 | Glownie do produkcji sadzy |
| Polspalanie CH4 + acetylen | 2CH4 -> C2H2 + 3H2 | Z jednoczesnym otrzymywaniem C2H2 |
| Polspalanie CH4 do CO+H2 | CH4 + 1/2 O2 -> CO + 2H2 | - |
| Konwersja parowa (reforming) | CH4 + H2O -> CO + 3H2 | Rownolegle: CO + H2O -> CO2 + H2 |
| Reforming parowo-tlenowy | CH4 + H2O + O2 (mieszany) | Kombinacja konwersji i polspalania |
| Konwersja z czesciowym utl. powietrzem | CH4 + H2O + powietrze | Tak aby V(H2) = 3 x V(N2) |

### 2.5 Konwersja metanu z para wodna (reforming parowy) - szczegoly

**Reakcja glowna:** CH4 + H2O <=> CO + 3H2 (endotermiczna, dH > 0)
**Reakcja rownlegla:** CH4 + 2H2O <=> CO2 + 4H2

**Warunki procesu:**
- Temperatura: 973-1073 K (700-800 C)
- Cisnienie: 3 - 3,5 MPa
- Katalizator: Ni/Al2O3 (lub spinel glinowo-magnezowy dotowany alkaliami)
- Stosunek H2O:CH4 = 4:1 (2-4 krotny nadmiar H2O zapobiega osadzaniu depozytow weglowych)

**Sklad gazu po konwersji:** H2, CO, CO2, H2O, CH4 (ok. 8% resztkowego!)

**Dalsze kroki:**
- Azot wprowadzany w drugim kroku = DOPALANIE METANU za pomoca powietrza
- Dodatkowe H2 z konwersji CO z para wodna: CO + H2O <=> CO2 + H2 (egzotermiczna, dH < 0)

---

## 3. SCHEMAT IDEOWY - Produkcja surowego gazu syntezowego (ZA Pulawy II)

```
  gaz ziemny ----+
                  |
  para wodna ----+----> [ KONWERSJA PAROWA (reforming parowy) ]
                           T = 973-1073 K
                           Kat.: Ni na nosniku
                                |
                          H2, CH4, CO, CO2
                                |
  powietrze --------> [ DOPALANIE ]
                                |
                                v
                  SUROWY GAZ SYNTEZOWY
           H2 - 56%, N2 - 22%, CO - 16%, CO2 - 6%, CH4 - 0,3%
```

---

## 4. ODSIARCZANIE GAZU ZIEMNEGO

### 4.1 Koniecznosc odsiarczania
Gaz ziemny musi byc odsiarczony do zawartosci S < 5 ppm. Katalizatory niklowe reformingu parowego sa wrazliwe na sladowe ilosci:
- Zwiazkow siarki
- Zwiazki arsenu
- Halogenki

### 4.2 Schemat instalacji odsiarczania (absorpcja etanoloaminowa)

```
 Gaz do                                          Gaz kwasny
 oczyszczania                                   (H2S + CO2)
     |                                               ^
     v                                               |
 +----------+     nasycony r-r     +-------------+   |
 | KOLUMNA  | -----------------> | KOLUMNA       |---+
 | ABSORP-  |   absorbujacy      | REGENERA-     |
 | CYJNA    | <----------------- | CYJNA         |
 +----------+   zregenerowany    +-------------+
     |           r-r absorbujacy       ^    |
     v                                 |    v
  Gaz                              Para   H2O
  oczyszczony                     wodna

Elementy: A - kolumna absorpcyjna (z wypelnieniem)
          B - kolumna regeneracyjna
          1 - wymiennik ciepla u dolu kolumny A
          2 - wymiennik ciepla (podgrzewacz) w kolumnie B
          3 - chlodnica gazu kwasnego na gorze B
          4 - separatory (oddzielacze) - na gorze B i w obiegu
          a - wlot gazu do oczyszczania (dol kolumny A)
```

**Absorbent:** Wodne roztwory (10-25%) etanoloamin: MEA (monoetanoloamina), DEA (dietanoloamina) lub TEA (trietanoloamina)

**Reakcja absorpcji:**
2HO-C2H4-NH2 + H2S + H2O <=> (HO-C2H4-NH3)2S

**Warunki:**
- Absorpcja: T = 300-320 K (tworzenie weglanu i siarczku monoetanoloaminy)
- Regeneracja: obnizenie p + podwyzszenie T do 383 K -> rozklad i uwolnienie H2S

---

## 5. OGOLNY SCHEMAT INSTALACJI OCZYSZCZANIA GAZOW

```
                       woda
                        |     zanieczyszczenia
                        v        gazowe
                     +-----+   +---+
                     | Ch  |   | S |  (separator)
                     +-----+   +---+
                        |        ^
                        v        |
  gaz           +-------------+  |
  oczyszczony<--| KOLUMNA     |--+
                | REGENERA-   |
                | CYJNA       |
                |   T ^       |
                |   p v       |
                +-------------+
   zregenerowany    |    ^   para wodna
   r-r absorbujacy  |    |
         |          v    |
         v        +---+ +---+
  +-----------+   |Ch | | W |  (wymiennik ciepla)
  | KOLUMNA   |   +---+ +---+
  | ABSORP-   |     ^
  | CYJNA     |     | nasycony r-r absorbujacy
  |   T ^     |-----+
  |   p v     |
  +-----------+
       ^
       |
  gaz zanieczyszczony
```

**Oznaczenia:** W - wymiennik ciepla, Ch - chlodnice, S - separator

**Zasada dzialania:** Gaz zanieczyszczony wchodzi od dolu do kolumny absorpcyjnej, kontaktuje sie z roztworem absorbujacym (plynacym z gory). Nasycony roztwor transportowany jest do kolumny regeneracyjnej, gdzie pod dzialaniem pary wodnej i podwyzszonej temperatury zanieczyszczenia sa uwalniane. Zregenerowany roztwor wraca do kolumny absorpcyjnej.

---

## 6. WEZEL WYTWARZANIA SUROWEGO GAZU SYNTEZOWEGO - Schemat aparaturowy

### 6.1 Opis numerowany aparatow

```
  Powietrze ---> [1] ---> [2] ---> [3] <--- Para
                  |        |        |
  Gaz ziemny ----|------> [2]      |
                           |        v
  Gazy spalinowe <--------[3]     [4] <--- Woda zmiekczona
                                    |
                                   [5]
                                    |
                                    v
                           Surowy gaz syntezowy
                           (gaz do konwersji CO)
```

| Nr | Aparat | Funkcja |
|----|--------|---------|
| 1 | Sprezarka powietrza | Sprezanie powietrza do procesu dopalania |
| 2 | Wymiennik ciepla | Podgrzewacz gazu ziemnego i powietrza (odzysk ciepla z gazow spalinowych) |
| 3 | Reformer | Rury z katalizatorem (Ni) + palniki; konwersja parowa CH4; T=973-1073K |
| 4 | Dopalacz | Dopalanie resztkowego CH4 powietrzem (wprowadzenie N2) |
| 5 | Chlodnica | Chlodzenie surowego gazu syntezowego woda zmiekczona |

**Przeplyw:** Gaz ziemny -> podgrzanie w wymienniku (2) -> reformer (3) z para wodna i katalizatorem Ni na rurach -> gaz (H2, CH4, CO, CO2) -> dopalacz (4) z powietrzem -> surowy gaz syntezowy -> chlodnica (5)

---

## 7. OCZYSZCZANIE SUROWEGO GAZU SYNTEZOWEGO (Korekcja skladu)

### 7.1 Usuwanie CO - Konwersja parowa tlenku wegla

**Reakcja:** CO + H2O(g) <=> CO2 + H2 (egzotermiczna, dH < 0)

| Parametr | WTKCO (wysokotemp.) | NTKCO (niskotemperaturowa) |
|----------|--------------------|-----------------------------|
| Temperatura | 280-450 C (optymalnie 400 C) | 200-250 C (optymalnie 250 C) |
| Cisnienie | 3 MPa | 3 MPa |
| Katalizator | Fe2O3 * 5% Cr2O3 * K2O | Cu/ZnO |
| CO po procesie | 2-3% | 0,2-0,3% |
| Max. zawartosc S w gazie | < 0,5 g/m3 | < 10 ppm |
| Charakter zatrucia kat. | Odwracalne | Nieodwracalne |

**UWAGA:** CO jest TRUCIZNA katalizatora syntezy amoniaku (tworzy polaczenia z Fe). Konieczne glebokie usuwanie.

### 7.2 Konwertor tlenku wegla - budowa aparatu

```
                 +------------------+
                 |    +---------+   |
                 |    | Warstwy |   |   <--- 790 K (gora)
                 |    | kontaktu|   |
                 |    | (kata-  |   |
                 |    | lizator)|   |   <--- 640 K (miedzy warstwami)
    Spaliny z    |    |   [1]   |   |
    palnika ---->|    +---------+   |
    rozruchowego |                  |
                 |  +-----------+   |
                 |  | Wymiennik |   |
                 |  | ciepla    |   |
                 |  |   [2]     |   |
                 |  | (rury)    |   |
                 |  +-----------+   |
                 +------------------+
                   ^              |
                   |              v
           Gaz surowy        Gaz skonwertowany
           z para wodna          490 K
              360 K
```

| Nr | Element | Opis |
|----|---------|------|
| 1 | Warstwy kontaktu (katalizatora) | Zloze katalityczne Fe2O3/Cr2O3 lub Cu/ZnO, umieszczone w gornej czesci konwertora |
| 2 | Wymiennik ciepla | Rury wymiennika w dolnej czesci; chlodzi gaz po reakcji, podgrzewa gaz wejsciowy |

**Temperatury:** Gaz surowy wchodzi od dolu (360 K) -> podgrzewanie w wymienniku -> przeplyw przez warstwy katalizatora (790 K na gorze, 640 K miedzy warstwami) -> skonwertowany gaz wychodzi od dolu (490 K)

### 7.3 Usuwanie CO - Mycie miedziowe

**Absorbent:** Amoniakalny roztwor mrówczanu (lub weglanu) miedzi

**Reakcja:** HCOO-[Cu(NH3)n] + CO <=> HCOO-[Cu(NH3)n*CO]
(kompleks rozklada sie juz w T = 80 C)

**Sklad roztworu [mol/dm3]:** Cu(I) = 1,5; Cu(II) = 0,2; NH3 = 6,0; CO2 = 3,0

**Roztwor wiaze zarowno CO, jak i CO2 oraz O2!**

**Warunki:**
- Sorpcja: p = 10-12 MPa (!!!), T = 278-283 K
- Regeneracja: p = 0,1 MPa, T = 353 K

### 7.4 Usuwanie CO2 - Mycie weglanowe (metoda Bensona-Fielda)

**Reakcja:** K2CO3 + CO2 + H2O <=> 2KHCO3 (dH = -100,5 kJ/mol)

**Warunki absorpcji:**
- p = 2-3 MPa
- T = 373 K
- 2-3 stopnie mycia z 25-35% roztworem K2CO3
- CO2 po procesie < 0,5%
- Aktywatory: 3% DEA lub As2O3

**Warunki regeneracji:**
- p = atmosferyczne
- T = 393 K

### 7.5 Metanizacja (usuwanie resztek CO i CO2)

**Reakcje:**
- CO + 3H2 <=> CH4 + H2O
- CO2 + 4H2 <=> CH4 + 2H2O

**Warunki:**
- Katalizator: wysoko-niklowy Ni/Al2O3
- p = 3 MPa
- T = 553-573 K

---

## 8. SCHEMAT IDEOWY OCZYSZCZANIA GAZU SYNTEZOWEGO (ZA Pulawy II)

```
  SUROWY GAZ SYNTEZOWY ---> Sklad [% obj.]:
  H2 - 56%, CO - 16%, CO2 - 6%, CH4 - 0,3%, N2 - 22%
         |
         v
  [Wysokotemperaturowa konwersja CO (WTKCO)]
    T = 380-450 C, Kat: Fe2O3+Cr2O3+K2O
    CO po procesie: ~3%
         |
         v
  [Niskotemperaturowa konwersja CO (NTKCO)]
    T = 200-250 C, Kat: Cu/ZnO
    CO po procesie: < 0,2%
         |
         v
  [Mycie potasowe (usuwanie CO2)]
    Absorpcja: 25-35% r-r K2CO3, T=95-100 C, cisn. 3 MPa
    Regeneracja: T=120 C, cisn. atm.
    CO2 po procesie: ok. 0,5%
         |
         v
  [Metanizacja (usuwanie CO i CO2)]
    T = 300-400 C, Kat: Ni/Al2O3
    CH4 = 0,8%
    CO i CO2 po procesie: ok. 10 ppm
         |
         v
  OCZYSZCZONY GAZ SYNTEZOWY ---> Sklad [% obj.]:
  H2 - 74%, N2 - 24%, CO i CO2 - po 10 ppm,
  CH4 - 0,8%, Ar i inne inerty - 1,2%
```

---

## 9. POROWNANIE ROZWIAZANIA PULAWY I vs PULAWY II

```
          PULAWY I                    PULAWY II
  gaz ziemny + powietrze      gaz ziemny + para wodna
         |                            |
  Polspalanie (I gruszka)      Konwersja parowa
         |                            |
  H2, CH4, CO, CO2, N2        H2, CH4, CO, CO2
         |                            |
  para wodna + powietrze        powietrze
         |                            |
  Konwersja parowa              Dopalanie
  (II gruszka)                        |
         |                     SUROWY GAZ SYNTEZOWY
  SUROWY GAZ SYNTEZOWY         H2, CH4, CO, CO2, N2
  H2, CH4, CO, CO2, N2               |
         |                     +------+------+
         |                     |             |
       WTKCO                 WTKCO         NTKCO
         |                     |             |
    Mycie potasowe          Mycie potasowe
         |                     |
    Mycie miedziowe         Metanizacja
         |                     |
    Mycie amoniakalne              |
         |                         |
  OCZYSZCZONY GAZ             OCZYSZCZONY GAZ
  SYNTEZOWY - H2, N2          SYNTEZOWY - H2, N2
```

**Roznice:** Pulawy I: polspalanie + konwersja parowa + mycie potasowe/miedziowe/amoniakalne.
Pulawy II: konwersja parowa + dopalanie + WTKCO + NTKCO + mycie potasowe + metanizacja (nowsza, efektywniejsza technologia).

---

## 10. DEZAKTYWACJA KATALIZATOROW - Depozyty weglowe

Problem: Trwale formowanie na powierzchni kontaktu produktow przejsciowych (depozyty weglowe), ktore:
- Blokuja powierzchnie aktywna (zjawisko "zatruwania")
- Tworza struktury objetosciowe utrudniajace dyfuzje wewnetrzna i zewnetrzna
- Zaklocaja dynamike wezla kontaktowego

**Zapobieganie:**
- Stosowanie nadmiaru reagenta (2-4 krotny nadmiar H2O wzgledem CH4)
- Modyfikacja skladu powierzchni aktywnej katalizatora (dotowanie alkaliami, np. K - promotory zgazowania depozytow)

---

## 11. SYNTEZA AMONIAKU

### 11.1 Podstawy termodynamiczne

**Reakcja:** N2 + 3H2 <=> 2NH3, dH = -92,4 kJ (egzotermiczna, z obnizeniem objetosci)

**Wplyw warunkow na rownowage:**
- Wyzsze cisnienie -> wiecej NH3 (przesuniecie rownowagi w strone mniejszej objetosci)
- Nizsza temperatura -> wiecej NH3 (reakcja egzotermiczna)
- Ale: niska temperatura = wolna kinetyka -> potrzebny katalizator

**Zawartosc NH3 w rownowadze (mieszanina stechiometryczna):**

| Cisnienie | 200 C | 300 C | 400 C | 500 C | 600 C |
|-----------|-------|-------|-------|-------|-------|
| 1 MPa | ~50% | ~15% | ~4% | ~1% | <1% |
| 10 MPa | ~80% | ~55% | ~25% | ~10% | ~4% |
| 30 MPa | ~90% | ~70% | ~45% | ~20% | ~8% |
| 60 MPa | ~95% | ~85% | ~65% | ~35% | ~15% |
| 100 MPa | ~98% | ~92% | ~80% | ~55% | ~30% |

### 11.2 Katalizator syntezy amoniaku

**Sklad:** Zelazo (Fe) z promotorami: Al2O3, K2O, CaO
**Zakres pracy:** 380-550 C (przekroczenie gornej granicy zmniejsza aktywnosc)

**Mechanizm reakcji na katalizatorze zelazowym:**
1. N2 + 2Fe <=> 2Fe-N (adsorpcja dysocjatywna azotu)
2. H2 + 2Fe <=> 2Fe-H (adsorpcja dysocjatywna wodoru)
3. N(ads.) + H(ads.) <=> NH(ads.)
4. NH(ads.) + H(ads.) <=> NH2(ads.)
5. NH2(ads.) + H(ads.) <=> NH3(ads.)
6. NH3(ads.) <=> NH3 (desorpcja produktu)

---

## 12. METODA OBIEGOWA PRODUKCJI AMONIAKU - Schemat aparaturowy

```
                    Gaz obiegowy (recyrkulacja)
  +------------------------------------------------------------------+
  |                                                                  |
  |  NH3 gaz                                                        |
  |     +---+                                                       |
  +---->| 8 |  (kondensator amoniakalny)                            |
        +---+                                                       |
          |                                                         |
       NH3 ciecz                                                    |
          |      Swiezy gaz                                         |
          v      do syntezy                                         |
        +---+       |       +---+       +---+       +---+       +---+
  <-----| 7 |<------+------>| 5 |------>| 4 |------>| 3 |------>| 2 |-----> [1]
  NH3   +---+               +---+       +---+       +---+       +---+  konwertor
  ciecz   |                   |           |                       |
          v                   v           |                       v
        H2O               olej           |                      H2O
                                         |
                          Gaz wydmuchowy <+
```

| Nr | Aparat | Funkcja |
|----|--------|---------|
| 1 | Konwertor amoniakalny | Reaktor syntezy NH3; katalizator Fe/Al2O3/K2O/CaO; T=380-550 C |
| 2 | Kondensator wodny | Kondensacja pary wodnej z gazu poreakcyjnego; chlodzenie woda (H2O) |
| 3 | Oddzielacz cieklego amoniaku | Separacja skroplonego NH3 z mieszaniny gazowej |
| 4 | Pompa obiegowa | Recyrkulacja gazu nieskonwertowanego z powrotem do konwertora |
| 5 | Filtr olejowy (oddzielacz oleju) | Usuwanie oleju z gazu obiegowego (z pompy/sprezarki) |
| 6 | Chlodnica | Chlodzenie gazu obiegowego przed dalszym skraplaniem NH3 |
| 7 | Wymiennik ciepla i oddzielacz NH3 | Wymiana ciepla + dodatkowa separacja NH3 cieklego; chlodzenie woda |
| 8 | Kondensator amoniakalny | Koncowe skraplanie NH3 z gazu obiegowego; NH3 ciecz odprowadzany |

**Przeplyw:**
1. Swiezy gaz syntezowy (H2+N2) wchodzi do obiegu
2. Gaz przechodzi przez konwertor [1] - czesciowa konwersja do NH3
3. Gaz poreakcyjny chlodzony w kondensatorze wodnym [2] (H2O)
4. Oddzielenie cieklego NH3 w oddzielaczu [3]
5. Nieskonwertowany gaz -> pompa obiegowa [4] -> filtr oleju [5] -> chlodnica [6]
6. Wymiennik ciepla/oddzielacz NH3 [7] -> kondensator amoniakalny [8]
7. Reszta gazu wraca jako gaz obiegowy do konwertora
8. Czesc gazu usuwana jako gaz wydmuchowy (usuwanie inertow: Ar, CH4)

---

## 13. ROZNE TYPY REAKTOROW SYNTEZY AMONIAKU

### 13.1 Konwertor TVA (Tennessee Valley Authority)

```
        wlot gazu
           |
           v
  +------------------+
  |  +-----------+   |
  |  |           |   |
  |  | Katali-   |   |
  |  | zator [1] |   |
  |  |           |   |
  |  |  [3] rury |   |
  |  |  wymien-  |   |
  |  |  nika w   |   |
  |  |  zlozu    |   |
  |  |           |   |
  |  +-----------+   |
  |                   |
  |  +-----------+   |
  |  | Wymiennik |   |
  |  | ciepla [2]|   |
  |  +-----------+   |
  +------------------+
     |             |
     v             v
  wylot gazu   wylot boczny
               gazu ziemnego
```

| Nr | Element | Opis |
|----|---------|------|
| 1 | Katalizator | Zloze katalityczne (Fe z promotorami) |
| 2 | Wymiennik ciepla | Wymiana ciepla miedzy gazem wejsciowym a poreakcyjnym |
| 3 | Rury wymiennika ciepla | Zanurzone bezposrednio w zlozu katalizatora - odbior ciepla reakcji |

### 13.2 Reaktor z promieniowym przeplywem gazu

```
        wlot gazu do syntezy
              |
              v
  +-----------------------+
  |   [5] izolacja        |
  |     cieplna           |
  |  +----------------+  |
  |  | [3] plaszcz    |  |
  |  |  cisnieniowy   |  |
  |  |                |  |
  |  |   +---------+  |  |
  |  |   |         |  |  |
  |  |   | [1]     |  |  |
  |  | [2]| kata-  |  |  |
  |  | zimny| lizator|  |  |
  |  | gaz  |       |  |  |
  |  |   +---------+  |  |
  |  +----------------+  |
  |                       |
  |  +----------------+  |
  |  | [4] wymiennik  |  |
  |  |     ciepla     |  |
  |  +----------------+  |
  +-----------------------+
     |               |
     v               v
  wylot gazu    wlot zimnego gazu
```

| Nr | Element | Opis |
|----|---------|------|
| 1 | Katalizator | Zloze katalizatora - gaz przepllywa promieniowo (radialnie) |
| 2 | Doplyw zimnego gazu | Chlodzenie miedzy warstwami katalizatora (quench) |
| 3 | Plaszcz cisnieniowy | Obudowa cisnieniowa reaktora |
| 4 | Wymiennik ciepla | Odzyskiwanie ciepla z gazu poreakcyjnego |
| 5 | Izolacja cieplna | Ochrona plaszcza cisnieniowego przed wysoka temperatura |

**Zaleta promieniowego przeplywu:** Mniejszy spadek cisnienia na zlozu niz przy przeplywaniu osiowym.

---

## 14. SCHEMAT KOMPLETNEJ INSTALACJI DO PRODUKCJI AMONIAKU

Schemat procesowy calej linii technologicznej od gazu ziemnego do cieklego NH3:

```
  gaz ziemny      powietrze   para 11,5 MPa, 500 C     woda kotlowa
  (3,8 MPa)           |              |     (procesowa)       |
     |                 |              |         |              |
     v                 v              v         v              v
   [1] ----> [2] ---> [3] -------->[4,5,6]-->[16,17]
    |         |        |              |          |
    |         v        v              v          |
    |    [7,8 WTKCO] [9 NTKCO]                  |
    |         |        |                         |
    |         v        v                         |
    |      [10] absorpcja CO2 w K2CO3            |
    |         | CO2 <------> [11] desorpcja      |
    |         v                                  |
    |      [12] metanizator                      |
    |         |                                  |
    v         v                                  |
   [13] konwertor syntezy NH3                    |
    |         |                                  |
    v         v                                  |
  [14] turbosprezarka swiezego gazu              |
  [15] turbosprezarka gazu obiegowego            |
    |                                            |
    v                                            |
  [18] chlodnica powietrzna                      |
    |                                            |
    v                                            |
  [19,22] oddzielacz amoniaku                    |
    |                                            |
  [20] wymiennik ciepla                          |
    |                                            |
  [21] chlodnica amoniakalna                     |
    |                                            |
  [23] rozprezacz cieklego amoniaku              |
    |                                            |
  [24] wymywanie NH3 z gazu resztkowego          |
    |                                            |
  [25] instalacja chlodnicza -----> NH3 ciecz    |
    |                                            |
  [26] turbosprezarka                            |
```

| Nr | Aparat | Funkcja |
|----|--------|---------|
| 1 | Odsiarczanie gazu | Usuwanie H2S i innych zwiazków siarki z gazu ziemnego (< 5 ppm S) |
| 2 | Reformer (konwersja metanu) | Rury z kat. Ni/Al2O3 + palniki; CH4+H2O->CO+3H2; T=973-1073K, p=3-3,5 MPa |
| 3 | Dopalacz metanu | Dopalanie resztkowego CH4 powietrzem; wprowadzenie N2 do gazu |
| 4,5,6 | Wytwornica i podgrzewacze pary i wody | Odzysk ciepla; produkcja pary procesowej 11,5 MPa/500 C |
| 7,8 | Konwertory WTKCO | Wysokotemperaturowa konwersja CO; kat. Fe2O3/Cr2O3/K2O; T=280-450 C |
| 9 | Konwertor NTKCO | Niskotemperaturowa konwersja CO; kat. Cu/ZnO; T=200-250 C |
| 10 | Kolumna absorpcyjna CO2 | Absorpcja CO2 w roztworze K2CO3 (25-35%); p=2-3 MPa; T=373K |
| 11 | Kolumna desorpcyjna | Regeneracja roztworu K2CO3; uwolnienie CO2; p=atm; T=393K |
| 12 | Metanizator | Usuwanie resztek CO i CO2; kat. Ni/Al2O3; T=553-573K; p=3 MPa |
| 13 | Konwertor syntezy NH3 | Synteza amoniaku; kat. Fe/Al2O3/K2O/CaO; T=380-550 C; p=15-30 MPa |
| 14 | Turbosprezarka swiezego gazu | Sprezanie oczyszczonego gazu syntezowego do cisnienia syntezy |
| 15 | Turbosprezarka gazu obiegowego | Recyrkulacja nieskonwertowanego gazu w obiegu syntezy |
| 16,17 | Kociol parowy i wymiennik ciepla | Produkcja pary z ciepla reakcji syntezy; odzysk energii |
| 18 | Chlodnica powietrzna | Chlodzenie gazu poreakcyjnego powietrzem |
| 19,22 | Oddzielacz amoniaku | Separacja skroplonego NH3 cieklego z mieszaniny gazowej |
| 20 | Wymiennik ciepla | Wymiana ciepla miedzy strumieniami procesowymi |
| 21 | Chlodnica amoniakalna | Chlodzenie gazu do niskiej temperatury za pomoca parujacego NH3 |
| 23 | Rozprezacz cieklego amoniaku | Rozprezanie cieklego NH3 (redukcja cisnienia) |
| 24 | Wymywanie NH3 z gazu resztkowego | Odzysk NH3 z gazu wydmuchowego przed wypuszczeniem |
| 25 | Instalacja chlodnicza | Produkcja zimna do skraplania NH3 |
| 26 | Turbosprezarka | Sprezanie gazu w obiegu chlodniczym |

**Cisnienia w instalacji:**
- Gaz ziemny wejsciowy: 3,8 MPa
- Para procesowa: 11,5 MPa, 500 C
- Synteza NH3: 15-30 MPa (typowo)

---

## 15. PRODUKCJA KWASU AZOTOWEGO Z AMONIAKU

### 15.1 Etapy procesu
1. Katalityczne utlenienie NH3 tlenem z powietrza do NO
2. Utlenianie NO do NO2
3. Absorpcja tlenkow azotu w wodzie

### 15.2 Reakcje utleniania amoniaku

**Reakcja pozadana:**
4NH3 + 5O2 => 4NO + 6H2O, dH = -216 kcal

**Reakcje rownolegle (niepozadane):**
- 4NH3 + 4O2 => 2N2O + 6H2O, dH = -264 kcal
- 4NH3 + 3O2 => 2N2 + 6H2O, dH = -303 kcal

**Reakcja nastecza (niepozadana):**
4NH3 + 6NO => 4N2 + 6H2O, dH = -431,6 kcal

**Reakcje poza katalizatorem:**
- NO + 1/2 O2 => NO2
- 3NO2 + H2O => 2HNO3 + NO

### 15.3 Wplyw warunkow na wydajnosc utleniania NH3 do NO

**Temperatura:**
- Optimum: 850 C (max. wydajnosc NO)
- Ponizej 850 C: wzrost udzialu N2O (4NH3+4O2 = 2N2O+6H2O)
- Powyzej 850 C: wzrost udzialu rozkladu NO (2NO = N2+O2)

**Czas kontaktu:**
- Optymalny: krotki czas (2-6 x 10^-4 s)
- Zbyt dlugi czas -> wzrost udzialu N2

**Stosunek molowy O2:NH3:**
- Optymalny: ok. 1,7-2,0 (nadmiar tlenu)
- Stechiometrycznie: 1,25 (= 5/4)
- Praktycznie: stosuje sie 10-12,5% NH3 w mieszaninie z powietrzem

### 15.4 Optymalne warunki utleniania na kontakcie platynowym

| Parametr | Metoda atmosf. | Met. kombinowana | Met. cisnieniowa |
|----------|----------------|-----------------|------------------|
| Cisnienie | atmosferyczne | 0,2-0,5 MPa | 0,7-0,9 MPa |
| Temperatura | 810-850 C | 870-890 C | 920-940 C |
| NH3 w mieszaninie | 12,0-12,5% | 10,5-11,0% | 10,3-10,5% |
| Wydajnosc utl. do NO | 97-98% | 96-96,5% | 94,5-95% |
| Straty Pt [g/Mg HNO3] | 0,04-0,05 | 0,10-0,11 | 0,25-0,30 |
| Czas pracy siatek [mies.] | 8-12 | 4-6 | 1,5-3 |

### 15.5 Katalizator utleniania amoniaku

**Sklad:** Pt-Rh (5-10% Rh), siatka z nici o sredniccy 0,06-0,09 mm
**Tkanie:** 1024 oczka na 1 cm2 powierzchni
**Erozja:** Podczas pracy zmniejsza sie wytrzymalosc mechaniczna; czesc Pt unoszona z gazami poreakcyjnymi. Siatki wymienia sie gdy zostanie uniesione ok. 1/3 masy Pt.

---

## 16. REAKTOR UTLENIANIA AMONIAKU - Budowa

```
              Amoniak
                |
                v
          +-----------+
          |    [1]    |  <-- mieszalnik amoniaku i powietrza
  Powie-  |           |
  trze -->|    [2]    |  <-- wzmacniacz (sito)
          |           |
          |    [3]    |  <-- siatka Pt-Rh (katalizator)
          |           |  ___
          |    [3*]   | | W |  <-- wymurówka (widok boczny: pierscien
          |           | |___|      siatek koncentrycznych)
          |           |
          |    [4]    |  <-- kociol parowy (odzysk ciepla)
          |    Woda   |
          |  przegrz. |
          |  (do kotla)|
          |           |
          |    [5]    |  <-- dolna czesc z komorami
          |    Woda-->|
          +-----------+
                |
                v
          Gaz poreakcyjny
```

| Nr | Element | Opis |
|----|---------|------|
| 1 | Mieszalnik amoniaku i powietrza | Gorna czesc reaktora; mieszanie NH3 z powietrzem do jednorodnej mieszaniny |
| 2 | Wzmacniacz (sito) | Wyrownanie przeplywu gazu przez przekroj reaktora |
| 3 | Siatka Pt-Rh | Katalizator platynowo-rodowy; siatka z drobnych nici; 1024 oczka/cm2 |
| 3* | Wymurówka | Izolacja termiczna scian reaktora w strefie reakcji |
| 4 | Kociol parowy | Odzysk ciepla reakcji; produkcja pary; woda przegrzana odprowadzana do kotla |
| 5 | Dolna komora | Zbiornik z woda; dodatkowe chlodzenie |

**Widok z gory (przekroj siatki):** Koncentryczne pierscienie siatek Pt-Rh w cylindrycznym reaktorze, oznaczone "W" (wymurówka na obrzezach).

---

## 17. ABSORPCJA NO2 W WODZIE

**Reakcja:** 3NO2 + H2O => 2HNO3 + NO

Powstaly NO wraca do obiegu i jest ponownie utleniany do NO2, a nastepnie absorbowany.

---

## 18. KLASYFIKACJA INSTALACJI DO PRODUKCJI HNO3

Kryterium: cisnienie utleniania / cisnienie absorpcji

| Typ procesu | Utlenianie/Absorpcja | Liczba instalacji |
|-------------|---------------------|-------------------|
| Dwucisnieniowy nisko/srednio | niskie/srednie | 9 (najstarsze) |
| Dwucisnieniowy srednio/wysoko | srednie/wysokie | 36 (najnowsze) |
| Jednocisnieniowy srednio/srednio | srednie/srednie | 22 |
| Jednocisnieniowy wysoko/wysoko | wysokie/wysokie | 11 |

Typowa wydajnosc instalacji: 1000 t/dobe

---

## 19. INSTALACJA DO PRODUKCJI KWASU AZOTOWEGO - Schemat aparaturowy

```
  Amoniak     Para
    |          |
    v          v
  [1] ------> [2] ---------> Do komina
   NH3        reaktor          |
   |         utleniania        |
   v          NH3              v
  [Mieszanie]   |          [Woda elektr.]
   |             v              |
   v          Powietrze         v
  [Filtr]        |         [Kolumny absorpcyjne
   |             v          6,7 - wielopolkowe]
   |          [3] --------> H2O |
   |          wymiennik         |
   |          ciepla            v
   |             |          [Kolumna koncowa]
   |             v              |
   |          [4] H2O           v
   |          chlodnica    43-50% HNO3
   |             |
   v             v
  [5] ------> Gaz zawierajacy tlenki azotu ------>
               Gaz odlotowy (do komina po oczyszczeniu)
```

**Opis przeplywu:**
1. Amoniak (gazowy) + powietrze mieszane -> reaktor utleniania [2] z siatka Pt-Rh
2. Gazy poreakcyjne (NO, H2O, N2) -> wymienniki ciepla [3] (odzysk ciepla, produkcja pary)
3. Chlodzenie gazow -> utlenianie NO do NO2
4. NO2 + H2O -> absorpcja w kolumnach absorpcyjnych [6,7] (wielopolkowe, z woda)
5. H2O podawana od gory, gaz od dolu (przeciwprad)
6. Produkt: 43-50% HNO3 (stezony kwas azotowy)
7. Gaz odlotowy -> do komina (po oczyszczeniu z resztek NOx)

---

## 20. SALETRA AMONOWA (NH4NO3)

### 20.1 Wlasciwosci
- Zawartosc azotu: 35% (dwie formy: amonowa + azotanowa)
- Nawoz uniwersalny
- Temperatura topnienia: 169,6 C

**Otrzymywanie:** HNO3 + NH3 => NH4NO3, dH = -146 kJ (silnie egzotermiczna)

**Rozklad termiczny:** 2NH4NO3 => 2N2 + O2 + 4H2O, dH = -146 kJ

### 20.2 Surowce
- Gazowy amoniak (NH3)
- 56,5% kwas azotowy (HNO3)

### 20.3 Problem technologiczny
Cieplo egzotermicznej reakcji zobojętniania moze spowodowac wzrost temperatury prowadzacy do rozkladu HNO3 i NH4NO3. Nie mozna bezposrednio wprowadzac NH3 do kwasu! Utrzymuje sie w obiegu pewna ilosc azotanu amonu, do ktorego dozuje sie odpowiednie ilosci NH3 i HNO3.

---

## 21. KOLUMNA NEUTRALIZACYJNA HOBLERA - Schemat aparaturowy

```
                    powietrze +
                    para wodna
                        ^
                        |   75 C
                     +------+
                     |Satu- |
                     |rator |
                     +------+
                        |
   skruber              |
     |                  |   80 C
     v                  |
  +------+           +------+
  |Absor-|   NH3 --->|Strefa|   105 C
  |ber   |           |neutr.|
  |natry-|           | XXXX |<----- lug kwasny (60 C)
  |skowy |           +------+
  +------+              |
     ^                  |
     |                  v
  HNO3             lug amoniakalny (60 C)
  woda                  |
  amoniakalna           |
                        v
  dozowniki ---> [neutralizator koncowy] <--- pompa
                        |                       ^
                        v                       |
                  lug zobojetniiony        60 C |
                  do wyparek          <---------+
```

| Element | Temperatura | Funkcja |
|---------|-------------|---------|
| Dozowniki | - | Precyzyjne dozowanie NH3 i HNO3 |
| Strefa neutralizacji (XXXX) | 105 C | Glowna reakcja zobojętniania NH3+HNO3 |
| Saturator | 75 C | Nasycanie powietrza para wodna (odbior ciepla) |
| Skruber | - | Oczyszczanie gazow wylotowych |
| Absorber natryskowy | - | Absorpcja resztek NH3 z powietrza (roztworem HNO3 + woda amoniakalna) |
| Neutralizator koncowy | 60 C | Dokladne doregulowanie pH/skladau roztworu |
| Pompa | - | Recyrkulacja lugu zobojetnionego |

**Przeplyw materialow:**
1. HNO3 (kwas) wplywa z boku (60 C) jako "lug kwasny"
2. NH3 (gazowy) wplywa do strefy neutralizacji (80 C)
3. Reakcja egzotermiczna podnosi T do 105 C
4. Lug amoniakalny (60 C) odbierany od dolu
5. Powietrze + para wodna wychodza gora przez saturator (75 C)
6. Lug zobojetniiony odprowadzany do wyparek (produkcja stalej saletry)
7. Skruber i absorber natryskowy oczyszczaja gazy wylotowe z resztek NH3

---

## 22. ZAKLADY AZOTOWE W PULAWACH - Zdolnosci produkcyjne

| Produkt | Roczna zdolnosc produkcyjna |
|---------|---------------------------|
| Saletra amonowa ogolem (roztwor) | 1 103 850 ton/rok |
| Saletra amonowa granulowana | 919 875 ton/rok |
| Roztwor saletrzano-mocznikowy (RSM) | 1 000 000 ton/rok |
| Mocznik ogolem | 924 000 ton/rok |
| Mocznik granulowany | 600 000 ton/rok |
| Melamina | 92 000 ton/rok |
| Kaprolaktam | 65 000 ton/rok |
| Siarczan amonu | 156 000 ton/rok |
| Nadtlenek wodoru (w przelicz. na 100%) | 10 000 ton/rok |
| Skroplony CO2 | 74 250 ton/rok |
