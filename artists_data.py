"""
Baza polskich artystow wizualnych urodzonych po 1840.
250+ artystow: malarze, rzezbiarz, graficy, fotografowie, plakacisci, konceptualisci.
Obejmuje emigrantow (Ecole de Paris, USA, Brazylia, etc.)

Kazdy artysta ma:
  - canonical_name: bez polskich znakow (do wyszukiwania w brazylijskiej bazie)
  - birth_year / death_year
  - category: painter, sculptor, graphic_artist, poster_artist, photographer,
               conceptual_artist, installation_artist, textile_artist, ceramist
  - fp_risk: false positive risk (low/medium/high) — jak ryzykowne jest szukanie samym nazwiskiem
  - context: slowa potwierdzajace trafienie (dla medium/high risk)
  - notes: dodatkowe info

UWAGA: warianty nazwisk generowane automatycznie w search_terms.py
"""

ARTISTS = [
    # ====================================================================
    # MALARSTWO — MLODA POLSKA / ART NOUVEAU (1840-1920)
    # ====================================================================
    {"canonical_name": "Jan Matejko", "birth_year": 1838, "death_year": 1893, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Jozef Chelmonski", "birth_year": 1849, "death_year": 1914, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Aleksander Gierymski", "birth_year": 1850, "death_year": 1901, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Maksymilian Gierymski", "birth_year": 1846, "death_year": 1874, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Henryk Siemiradzki", "birth_year": 1843, "death_year": 1902, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Jozef Brandt", "birth_year": 1841, "death_year": 1915, "category": "painter",
     "fp_risk": "high", "context": ["pintura", "quadro", "oleo", "tela", "painting", "cavalo", "batalha", "polish", "polonesa"]},
    {"canonical_name": "Artur Grottger", "birth_year": 1837, "death_year": 1867, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Stanislaw Wyspianski", "birth_year": 1869, "death_year": 1907, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Jacek Malczewski", "birth_year": 1854, "death_year": 1929, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Jozef Mehoffer", "birth_year": 1869, "death_year": 1946, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Wojciech Kossak", "birth_year": 1856, "death_year": 1942, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Juliusz Kossak", "birth_year": 1824, "death_year": 1899, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Jerzy Kossak", "birth_year": 1886, "death_year": 1955, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Leon Wyczolkowski", "birth_year": 1852, "death_year": 1936, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Wlodzimierz Tetmajer", "birth_year": 1861, "death_year": 1923, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Jozef Pankiewicz", "birth_year": 1866, "death_year": 1940, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Olga Boznanska", "birth_year": 1865, "death_year": 1940, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Wladyslaw Podkowinski", "birth_year": 1866, "death_year": 1895, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Ferdynand Ruszczyc", "birth_year": 1870, "death_year": 1936, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Witold Pruszkowski", "birth_year": 1846, "death_year": 1896, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Teodor Axentowicz", "birth_year": 1859, "death_year": 1938, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Julian Falat", "birth_year": 1853, "death_year": 1929, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Wlodzimierz Przerwa-Tetmajer", "birth_year": 1861, "death_year": 1923, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Kazimierz Stabrowski", "birth_year": 1869, "death_year": 1929, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Konrad Krzyzanowski", "birth_year": 1872, "death_year": 1922, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Henryk Uziemblo", "birth_year": 1879, "death_year": 1949, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Kazimierz Sichulski", "birth_year": 1879, "death_year": 1942, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Wlastimil Hofman", "birth_year": 1881, "death_year": 1970, "category": "painter", "fp_risk": "low"},

    # ====================================================================
    # MALARSTWO — FORMISCI / AWANGARDA (1910-1939)
    # ====================================================================
    {"canonical_name": "Stanislaw Ignacy Witkiewicz", "birth_year": 1885, "death_year": 1939, "category": "painter",
     "fp_risk": "low", "notes": "Witkacy"},
    {"canonical_name": "Wladyslaw Strzeminski", "birth_year": 1893, "death_year": 1952, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Leon Chwistek", "birth_year": 1884, "death_year": 1944, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Tytus Czyzewski", "birth_year": 1880, "death_year": 1945, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Zbigniew Pronaszko", "birth_year": 1885, "death_year": 1958, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Andrzej Pronaszko", "birth_year": 1888, "death_year": 1961, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Stanislaw Kubicki", "birth_year": 1889, "death_year": 1942, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Henryk Berlewi", "birth_year": 1894, "death_year": 1967, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Henryk Stazewski", "birth_year": 1894, "death_year": 1988, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Zofia Stryjenska", "birth_year": 1891, "death_year": 1976, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Rafal Malczewski", "birth_year": 1892, "death_year": 1965, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Jan Cybis", "birth_year": 1897, "death_year": 1972, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Artur Nacht-Samborski", "birth_year": 1898, "death_year": 1974, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Zygmunt Waliszewski", "birth_year": 1897, "death_year": 1936, "category": "painter", "fp_risk": "low"},

    # ====================================================================
    # ECOLE DE PARIS — POLSCY ARTYSCI W PARYZU
    # ====================================================================
    {"canonical_name": "Tamara de Lempicka", "birth_year": 1898, "death_year": 1980, "category": "painter",
     "fp_risk": "low", "notes": "Art Deco, emigracja USA"},
    {"canonical_name": "Mojzesz Kisling", "birth_year": 1891, "death_year": 1953, "category": "painter",
     "fp_risk": "low", "notes": "Ecole de Paris"},
    {"canonical_name": "Eugeniusz Zak", "birth_year": 1884, "death_year": 1926, "category": "painter",
     "fp_risk": "high", "context": ["pintura", "quadro", "oleo", "arte", "painting", "ecole", "paris"],
     "notes": "Ecole de Paris"},
    {"canonical_name": "Mela Muter", "birth_year": 1876, "death_year": 1967, "category": "painter",
     "fp_risk": "low", "notes": "Ecole de Paris, Maria Melania Mutermilch"},
    {"canonical_name": "Louis Marcoussis", "birth_year": 1878, "death_year": 1941, "category": "painter",
     "fp_risk": "low", "notes": "Ludwik Kazimierz Wladyslaw Markus, kubizm"},
    {"canonical_name": "Marek Szwarc", "birth_year": 1892, "death_year": 1958, "category": "painter",
     "fp_risk": "low", "notes": "Ecole de Paris, rzezba tez"},
    {"canonical_name": "Zygmunt Menkes", "birth_year": 1896, "death_year": 1986, "category": "painter",
     "fp_risk": "low", "notes": "Ecole de Paris, potem USA"},
    {"canonical_name": "Henryk Hayden", "birth_year": 1883, "death_year": 1970, "category": "painter",
     "fp_risk": "medium", "context": ["pintura", "quadro", "cubisme", "cubismo", "ecole", "paris", "arte"],
     "notes": "Ecole de Paris, kubizm"},
    {"canonical_name": "Simon Mondzain", "birth_year": 1888, "death_year": 1979, "category": "painter",
     "fp_risk": "low", "notes": "Szymon Mondszajn, Ecole de Paris"},
    {"canonical_name": "Sonia Delaunay", "birth_year": 1885, "death_year": 1979, "category": "painter",
     "fp_risk": "low", "notes": "Urodzona Sara Iliniczna Stern w Hradyzku (Ukraina/Polska)"},
    {"canonical_name": "Roman Kramsztyk", "birth_year": 1885, "death_year": 1942, "category": "painter",
     "fp_risk": "low", "notes": "Ecole de Paris"},
    {"canonical_name": "Joachim Weingart", "birth_year": 1895, "death_year": 1942, "category": "painter",
     "fp_risk": "low", "notes": "Ecole de Paris"},
    {"canonical_name": "Leopold Gottlieb", "birth_year": 1879, "death_year": 1934, "category": "painter",
     "fp_risk": "medium", "context": ["pintura", "quadro", "arte", "ecole", "paris", "painting"],
     "notes": "Ecole de Paris"},
    {"canonical_name": "Maurycy Gottlieb", "birth_year": 1856, "death_year": 1879, "category": "painter",
     "fp_risk": "medium", "context": ["pintura", "quadro", "arte", "painting", "judaico", "jewish"],
     "notes": "Malarstwo historyczne i judaica"},
    {"canonical_name": "Samuel Hirszenberg", "birth_year": 1865, "death_year": 1908, "category": "painter",
     "fp_risk": "low", "notes": "Malarstwo historyczne"},
    {"canonical_name": "Alicja Halicka", "birth_year": 1894, "death_year": 1975, "category": "painter",
     "fp_risk": "low", "notes": "Ecole de Paris, kubizm"},
    {"canonical_name": "Jozef Czapski", "birth_year": 1896, "death_year": 1993, "category": "painter",
     "fp_risk": "low", "notes": "Emigracja Paryz, tez pisarz"},
    {"canonical_name": "Feliks Topolski", "birth_year": 1907, "death_year": 1989, "category": "painter",
     "fp_risk": "low", "notes": "Emigracja Londyn"},
    {"canonical_name": "Konstanty Brandel", "birth_year": 1880, "death_year": 1970, "category": "painter",
     "fp_risk": "low", "notes": "Ecole de Paris"},
    {"canonical_name": "Waclaw Zawadowski", "birth_year": 1891, "death_year": 1982, "category": "painter",
     "fp_risk": "low", "notes": "Ecole de Paris"},
    {"canonical_name": "Jan Waclaw Zawadowski", "birth_year": 1891, "death_year": 1982, "category": "painter",
     "fp_risk": "low", "notes": "alias Zawadowski"},
    {"canonical_name": "Adam Marczyński", "birth_year": 1908, "death_year": 1985, "category": "painter", "fp_risk": "low"},

    # ====================================================================
    # MALARSTWO — KAPIZM / KOLORYZM POLSKI (1930-1960)
    # ====================================================================
    {"canonical_name": "Piotr Potworowski", "birth_year": 1898, "death_year": 1962, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Hanna Rudzka-Cybisowa", "birth_year": 1897, "death_year": 1988, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Czeslawa Ogrodzka-Wielowiejska", "birth_year": 1897, "death_year": 1963, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Jozef Jarema", "birth_year": 1900, "death_year": 1974, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Maria Jarema", "birth_year": 1908, "death_year": 1958, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Jonasz Stern", "birth_year": 1904, "death_year": 1988, "category": "painter",
     "fp_risk": "high", "context": ["pintura", "quadro", "arte", "painting", "polish", "polonesa"],
     "notes": "Nazwisko Stern bardzo popularne"},
    {"canonical_name": "Tadeusz Kantor", "birth_year": 1915, "death_year": 1990, "category": "painter",
     "fp_risk": "medium", "context": ["teatro", "theatre", "art", "arte", "pintura", "polish", "polonesa", "cricot"]},
    {"canonical_name": "Jerzy Nowosielski", "birth_year": 1923, "death_year": 2011, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Andrzej Wroblewski", "birth_year": 1927, "death_year": 1957, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Wojciech Fangor", "birth_year": 1922, "death_year": 2015, "category": "painter",
     "fp_risk": "low", "notes": "Op-art, emigracja USA"},
    {"canonical_name": "Stefan Gierowski", "birth_year": 1925, "death_year": 2022, "category": "painter", "fp_risk": "low"},

    # ====================================================================
    # MALARSTWO — NOWA FIGURACJA / POWOJENNE (1945-1990)
    # ====================================================================
    {"canonical_name": "Zdzislaw Beksinski", "birth_year": 1929, "death_year": 2005, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Nikifor Krynicki", "birth_year": 1895, "death_year": 1968, "category": "painter",
     "fp_risk": "medium", "context": ["pintura", "quadro", "naif", "naive", "primitivo", "krynica", "polish", "polonesa"]},
    {"canonical_name": "Wladyslaw Hasior", "birth_year": 1928, "death_year": 1999, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Roman Opalka", "birth_year": 1931, "death_year": 2011, "category": "painter",
     "fp_risk": "low", "notes": "Emigracja Francja, 1965/1-∞"},
    {"canonical_name": "Jerzy Stajuda", "birth_year": 1936, "death_year": 1992, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Jan Tarasin", "birth_year": 1926, "death_year": 2009, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Aleksander Kobzdej", "birth_year": 1920, "death_year": 1972, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Rajmund Ziemski", "birth_year": 1930, "death_year": 2005, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Jan Lebenstein", "birth_year": 1930, "death_year": 1999, "category": "painter",
     "fp_risk": "low", "notes": "Emigracja Paryz"},
    {"canonical_name": "Tadeusz Brzozowski", "birth_year": 1918, "death_year": 1987, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Alfred Lenica", "birth_year": 1899, "death_year": 1977, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Kazimierz Mikulski", "birth_year": 1918, "death_year": 1998, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Tadeusz Dominik", "birth_year": 1928, "death_year": 2014, "category": "painter",
     "fp_risk": "medium", "context": ["pintura", "quadro", "arte", "painting", "polish", "abstract"]},
    {"canonical_name": "Wieslaw Borowski", "birth_year": 1929, "death_year": 2009, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Edward Dwurnik", "birth_year": 1943, "death_year": 2018, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Jerzy Ryszard Zielinski", "birth_year": 1943, "death_year": 1980, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Wlodzimierz Borowski", "birth_year": 1930, "death_year": 2008, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Koji Kamoji", "birth_year": 1935, "death_year": None, "category": "painter",
     "fp_risk": "low", "notes": "Japonczyk ale calkowicie polski artysta, zwiazany z Polska od lat 60."},

    # ====================================================================
    # MALARSTWO — WSPOLCZESNE (1990+)
    # ====================================================================
    {"canonical_name": "Wilhelm Sasnal", "birth_year": 1972, "death_year": None, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Marcin Maciejowski", "birth_year": 1974, "death_year": None, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Rafal Bujnowski", "birth_year": 1974, "death_year": None, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Tomasz Kowalski", "birth_year": 1984, "death_year": None, "category": "painter",
     "fp_risk": "high", "context": ["pintura", "arte", "painting", "gallery", "galeria", "exhibition"]},
    {"canonical_name": "Jakub Julian Ziolkowski", "birth_year": 1980, "death_year": None, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Pawel Althamer", "birth_year": 1967, "death_year": None, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Leon Tarasewicz", "birth_year": 1957, "death_year": None, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Jaroslaw Modzelewski", "birth_year": 1955, "death_year": None, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Marek Sobczyk", "birth_year": 1955, "death_year": None, "category": "painter",
     "fp_risk": "medium", "context": ["pintura", "arte", "painting", "gallery"]},
    {"canonical_name": "Ryszard Grzyb", "birth_year": 1956, "death_year": None, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Wlodzimierz Pawlak", "birth_year": 1957, "death_year": None, "category": "painter",
     "fp_risk": "medium", "context": ["pintura", "arte", "painting", "abstract"]},
    {"canonical_name": "Marek Chlanda", "birth_year": 1954, "death_year": None, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Zbylut Grzywacz", "birth_year": 1939, "death_year": 2004, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Andrzej Szewczyk", "birth_year": 1950, "death_year": 2001, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Ryszard Winiarski", "birth_year": 1936, "death_year": 2006, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Teresa Pagowska", "birth_year": 1926, "death_year": 2007, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Jadwiga Maziarska", "birth_year": 1913, "death_year": 2003, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Jan Dobkowski", "birth_year": 1942, "death_year": None, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Jerzy Krawczyk", "birth_year": 1921, "death_year": 1969, "category": "painter",
     "fp_risk": "high", "context": ["pintura", "arte", "painting", "polish"]},
    {"canonical_name": "Erna Rosenstein", "birth_year": 1913, "death_year": 2004, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Sasza Blonder", "birth_year": 1909, "death_year": 1949, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Marek Wlodarski", "birth_year": 1903, "death_year": 1960, "category": "painter",
     "fp_risk": "low", "notes": "Henryk Streng"},
    {"canonical_name": "Jerzy Tchorzewski", "birth_year": 1928, "death_year": 1999, "category": "painter", "fp_risk": "low"},

    # ====================================================================
    # RZEZBA
    # ====================================================================
    {"canonical_name": "Magdalena Abakanowicz", "birth_year": 1930, "death_year": 2017, "category": "sculptor",
     "fp_risk": "low", "notes": "Emigracja/wystawy miedzynarodowe"},
    {"canonical_name": "Alina Szapocznikow", "birth_year": 1926, "death_year": 1973, "category": "sculptor",
     "fp_risk": "low", "notes": "Emigracja Paryz"},
    {"canonical_name": "Igor Mitoraj", "birth_year": 1944, "death_year": 2014, "category": "sculptor",
     "fp_risk": "low", "notes": "Emigracja Wlochy"},
    {"canonical_name": "Katarzyna Kobro", "birth_year": 1898, "death_year": 1951, "category": "sculptor", "fp_risk": "low"},
    {"canonical_name": "Xawery Dunikowski", "birth_year": 1875, "death_year": 1964, "category": "sculptor", "fp_risk": "low"},
    {"canonical_name": "Boleslaw Biegas", "birth_year": 1877, "death_year": 1954, "category": "sculptor",
     "fp_risk": "low", "notes": "Emigracja Paryz"},
    {"canonical_name": "Olga Niewska", "birth_year": 1898, "death_year": 1943, "category": "sculptor", "fp_risk": "low"},
    {"canonical_name": "August Zamoyski", "birth_year": 1893, "death_year": 1970, "category": "sculptor",
     "fp_risk": "low", "notes": "Emigracja Paryz/Brazylia"},
    {"canonical_name": "Henryk Kuna", "birth_year": 1879, "death_year": 1945, "category": "sculptor",
     "fp_risk": "medium", "context": ["escultura", "sculpture", "rzezba", "bronze", "bronzo"]},
    {"canonical_name": "Edward Wittig", "birth_year": 1879, "death_year": 1941, "category": "sculptor", "fp_risk": "low"},
    {"canonical_name": "Alfons Karny", "birth_year": 1901, "death_year": 1989, "category": "sculptor", "fp_risk": "low"},
    {"canonical_name": "Ludwika Nitschowa", "birth_year": 1889, "death_year": 1989, "category": "sculptor", "fp_risk": "low"},
    {"canonical_name": "Marian Konieczny", "birth_year": 1930, "death_year": 2017, "category": "sculptor",
     "fp_risk": "medium", "context": ["escultura", "sculpture", "bronze", "pomnik", "monument"]},
    {"canonical_name": "Jerzy Jarnuszkiewicz", "birth_year": 1919, "death_year": 2005, "category": "sculptor", "fp_risk": "low"},
    {"canonical_name": "Barbara Zbrożyna", "birth_year": 1923, "death_year": 2019, "category": "sculptor", "fp_risk": "low"},
    {"canonical_name": "Gustaw Zemla", "birth_year": 1931, "death_year": 2023, "category": "sculptor", "fp_risk": "low"},
    {"canonical_name": "Bronislaw Chromy", "birth_year": 1925, "death_year": 2017, "category": "sculptor", "fp_risk": "low"},
    {"canonical_name": "Adam Myjak", "birth_year": 1947, "death_year": None, "category": "sculptor", "fp_risk": "low"},
    {"canonical_name": "Krzysztof Bednarski", "birth_year": 1953, "death_year": None, "category": "sculptor", "fp_risk": "low"},
    {"canonical_name": "Miroslaw Balka", "birth_year": 1958, "death_year": None, "category": "sculptor",
     "fp_risk": "low", "notes": "Instalacje, miedzynarodowy"},
    {"canonical_name": "Monika Sosnowska", "birth_year": 1972, "death_year": None, "category": "sculptor",
     "fp_risk": "low", "notes": "Instalacje/rzezba"},

    # ====================================================================
    # GRAFIKA / PLAKAT — POLSKA SZKOLA PLAKATU
    # ====================================================================
    {"canonical_name": "Henryk Tomaszewski", "birth_year": 1914, "death_year": 2005, "category": "poster_artist",
     "fp_risk": "high", "context": ["cartaz", "poster", "plakat", "grafica", "graphic", "design"]},
    {"canonical_name": "Jan Lenica", "birth_year": 1928, "death_year": 2001, "category": "poster_artist",
     "fp_risk": "low", "notes": "Tez animacja"},
    {"canonical_name": "Roman Cieslewicz", "birth_year": 1930, "death_year": 1996, "category": "poster_artist",
     "fp_risk": "low", "notes": "Emigracja Paryz"},
    {"canonical_name": "Waldemar Swierzy", "birth_year": 1931, "death_year": 2013, "category": "poster_artist", "fp_risk": "low"},
    {"canonical_name": "Franciszek Starowieyski", "birth_year": 1930, "death_year": 2009, "category": "poster_artist", "fp_risk": "low"},
    {"canonical_name": "Wiktor Gorka", "birth_year": 1922, "death_year": 2004, "category": "poster_artist",
     "fp_risk": "medium", "context": ["cartaz", "poster", "plakat", "cinema", "film"]},
    {"canonical_name": "Jan Mlodozeniec", "birth_year": 1929, "death_year": 2000, "category": "poster_artist", "fp_risk": "low"},
    {"canonical_name": "Wojciech Zamecznik", "birth_year": 1923, "death_year": 1967, "category": "poster_artist", "fp_risk": "low"},
    {"canonical_name": "Tadeusz Trepkowski", "birth_year": 1914, "death_year": 1954, "category": "poster_artist", "fp_risk": "low"},
    {"canonical_name": "Jozef Mroszczak", "birth_year": 1910, "death_year": 1975, "category": "poster_artist", "fp_risk": "low"},
    {"canonical_name": "Mieczyslaw Wasilewski", "birth_year": 1942, "death_year": None, "category": "poster_artist", "fp_risk": "low"},
    {"canonical_name": "Wiktor Sadowski", "birth_year": 1956, "death_year": None, "category": "poster_artist",
     "fp_risk": "medium", "context": ["cartaz", "poster", "plakat", "design"]},
    {"canonical_name": "Stasys Eidrigevicius", "birth_year": 1949, "death_year": None, "category": "poster_artist",
     "fp_risk": "low", "notes": "Litewski ale aktywny w Polsce"},
    {"canonical_name": "Wieslaw Walkuski", "birth_year": 1956, "death_year": None, "category": "poster_artist", "fp_risk": "low"},
    {"canonical_name": "Andrzej Pagowski", "birth_year": 1953, "death_year": None, "category": "poster_artist", "fp_risk": "low"},
    {"canonical_name": "Rafal Olbinski", "birth_year": 1943, "death_year": None, "category": "poster_artist",
     "fp_risk": "low", "notes": "Emigracja USA, surrealizm"},
    {"canonical_name": "Leszek Zebrowski", "birth_year": 1950, "death_year": None, "category": "poster_artist", "fp_risk": "low"},

    # ====================================================================
    # GRAFIKA — DRZEWORYT / LINORYT / LITOGRAFIA
    # ====================================================================
    {"canonical_name": "Wladyslaw Skoczylas", "birth_year": 1883, "death_year": 1934, "category": "graphic_artist",
     "fp_risk": "low", "notes": "Ojciec polskiego drzeworytu"},
    {"canonical_name": "Stefan Mrozewski", "birth_year": 1894, "death_year": 1975, "category": "graphic_artist",
     "fp_risk": "low", "notes": "Emigracja USA"},
    {"canonical_name": "Tadeusz Kulisiewicz", "birth_year": 1899, "death_year": 1988, "category": "graphic_artist", "fp_risk": "low"},
    {"canonical_name": "Jozef Gielniak", "birth_year": 1932, "death_year": 1972, "category": "graphic_artist", "fp_risk": "low"},
    {"canonical_name": "Stanislaw Ostoja-Chrostowski", "birth_year": 1897, "death_year": 1947, "category": "graphic_artist", "fp_risk": "low"},
    {"canonical_name": "Stefan Suberlak", "birth_year": 1928, "death_year": 1994, "category": "graphic_artist", "fp_risk": "low"},
    {"canonical_name": "Halina Chlicka", "birth_year": 1925, "death_year": 2002, "category": "graphic_artist", "fp_risk": "low"},
    {"canonical_name": "Ludwik Tyrowicz", "birth_year": 1901, "death_year": 1958, "category": "graphic_artist", "fp_risk": "low"},
    {"canonical_name": "Maria Hiszpanska-Neumann", "birth_year": 1917, "death_year": 1980, "category": "graphic_artist", "fp_risk": "low"},
    {"canonical_name": "Mieczyslaw Wejman", "birth_year": 1912, "death_year": 1997, "category": "graphic_artist", "fp_risk": "low"},

    # ====================================================================
    # FOTOGRAFIA
    # ====================================================================
    {"canonical_name": "Zofia Rydet", "birth_year": 1911, "death_year": 1997, "category": "photographer", "fp_risk": "low"},
    {"canonical_name": "Natalia Lach-Lachowicz", "birth_year": 1937, "death_year": None, "category": "photographer",
     "fp_risk": "low", "notes": "NataLia LL, performance tez"},
    {"canonical_name": "Zbigniew Dlubak", "birth_year": 1921, "death_year": 2005, "category": "photographer", "fp_risk": "low"},
    {"canonical_name": "Jerzy Lewczynski", "birth_year": 1924, "death_year": 2014, "category": "photographer", "fp_risk": "low"},
    {"canonical_name": "Zdzislaw Bekinski", "birth_year": 1929, "death_year": 2005, "category": "photographer",
     "fp_risk": "low", "notes": "Tez fotografia, juz w painters"},
    {"canonical_name": "Edward Hartwig", "birth_year": 1909, "death_year": 2003, "category": "photographer",
     "fp_risk": "medium", "context": ["fotografia", "photography", "foto", "photograph"]},
    {"canonical_name": "Jan Bulhak", "birth_year": 1876, "death_year": 1950, "category": "photographer", "fp_risk": "low"},
    {"canonical_name": "Benedykt Jerzy Dorys", "birth_year": 1901, "death_year": 1990, "category": "photographer", "fp_risk": "low"},
    {"canonical_name": "Stefan Arczyński", "birth_year": 1916, "death_year": 2015, "category": "photographer", "fp_risk": "low"},

    # ====================================================================
    # SZTUKA KONCEPTUALNA / PERFORMANCE / INSTALACJA
    # ====================================================================
    {"canonical_name": "Krzysztof Wodiczko", "birth_year": 1943, "death_year": None, "category": "conceptual_artist",
     "fp_risk": "low", "notes": "Emigracja USA/Kanada, projekcje publiczne"},
    {"canonical_name": "Zbigniew Libera", "birth_year": 1959, "death_year": None, "category": "conceptual_artist", "fp_risk": "low"},
    {"canonical_name": "Katarzyna Kozyra", "birth_year": 1963, "death_year": None, "category": "conceptual_artist", "fp_risk": "low"},
    {"canonical_name": "Artur Zmijewski", "birth_year": 1966, "death_year": None, "category": "conceptual_artist", "fp_risk": "low"},
    {"canonical_name": "Joanna Rajkowska", "birth_year": 1968, "dead_year": None, "category": "conceptual_artist", "fp_risk": "low"},
    {"canonical_name": "Piotr Uklanski", "birth_year": 1968, "death_year": None, "category": "conceptual_artist",
     "fp_risk": "low", "notes": "Emigracja USA"},
    {"canonical_name": "Grzegorz Klaman", "birth_year": 1959, "death_year": None, "category": "conceptual_artist", "fp_risk": "low"},
    {"canonical_name": "Oskar Dawicki", "birth_year": 1971, "death_year": None, "category": "conceptual_artist", "fp_risk": "low"},
    {"canonical_name": "Agnieszka Polska", "birth_year": 1985, "death_year": None, "category": "conceptual_artist",
     "fp_risk": "high", "context": ["video", "arte", "art", "gallery", "galeria", "exhibition"],
     "notes": "Nazwisko = 'Polska' — mega false positive risk"},
    {"canonical_name": "Cezary Bodzianowski", "birth_year": 1968, "death_year": None, "category": "conceptual_artist", "fp_risk": "low"},
    {"canonical_name": "Jaroslaw Kozlowski", "birth_year": 1945, "death_year": None, "category": "conceptual_artist", "fp_risk": "low"},
    {"canonical_name": "Zofia Kulik", "birth_year": 1947, "death_year": None, "category": "conceptual_artist", "fp_risk": "low"},
    {"canonical_name": "Przemyslaw Kwiek", "birth_year": 1945, "death_year": None, "category": "conceptual_artist", "fp_risk": "low"},
    {"canonical_name": "Akademia Ruchu", "birth_year": None, "death_year": None, "category": "performance_group",
     "fp_risk": "high", "context": ["performance", "arte", "art", "teatro"],
     "notes": "Grupa artystyczna, nie osoba"},

    # ====================================================================
    # TEKSTYL / TKANINA ARTYSTYCZNA
    # ====================================================================
    {"canonical_name": "Jolanta Owidzka", "birth_year": 1927, "death_year": 2020, "category": "textile_artist", "fp_risk": "low"},
    {"canonical_name": "Wojciech Sadley", "birth_year": 1932, "death_year": 2018, "category": "textile_artist", "fp_risk": "low"},
    {"canonical_name": "Anna Sledziewska", "birth_year": 1928, "death_year": 2015, "category": "textile_artist", "fp_risk": "low"},
    {"canonical_name": "Urszula Plewka-Schmidt", "birth_year": 1939, "death_year": None, "category": "textile_artist", "fp_risk": "low"},

    # ====================================================================
    # CERAMIKA / SZKLO
    # ====================================================================
    {"canonical_name": "Lubomir Tomaszewski", "birth_year": 1923, "death_year": 2018, "category": "sculptor",
     "fp_risk": "low", "notes": "Emigracja USA, rzezba ze szkla"},

    # ====================================================================
    # MEBLE / DESIGN — POLSCY PROJEKTANCI W BRAZYLII
    # ====================================================================
    {"canonical_name": "Jorge Zalszupin", "birth_year": 1922, "death_year": 2020, "category": "furniture_designer",
     "fp_risk": "low", "notes": "Polak w Brazylii, L'Atelier Moveis"},

    # ====================================================================
    # DODATKOWI MALARZE — UZUPELNIENIE DO 250+
    # ====================================================================
    {"canonical_name": "Tadeusz Makowski", "birth_year": 1882, "death_year": 1932, "category": "painter",
     "fp_risk": "low", "notes": "Emigracja Paryz"},
    {"canonical_name": "Eugeniusz Eibisch", "birth_year": 1896, "death_year": 1987, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Ludwik de Laveaux", "birth_year": 1868, "death_year": 1894, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Wladyslaw Slewinski", "birth_year": 1856, "death_year": 1918, "category": "painter",
     "fp_risk": "low", "notes": "Pont-Aven, przyjaciel Gauguina"},
    {"canonical_name": "Jozef Czajkowski", "birth_year": 1872, "death_year": 1947, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Karol Tichy", "birth_year": 1871, "death_year": 1939, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Edward Okuń", "birth_year": 1872, "death_year": 1945, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Wojciech Weiss", "birth_year": 1875, "death_year": 1950, "category": "painter",
     "fp_risk": "high", "context": ["pintura", "quadro", "arte", "painting", "polish"],
     "notes": "Nazwisko Weiss popularne"},
    {"canonical_name": "Jozef Rapacki", "birth_year": 1871, "death_year": 1929, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Stanislaw Lentz", "birth_year": 1861, "death_year": 1920, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Waclaw Borowski", "birth_year": 1885, "death_year": 1954, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Felicjan Szczesny Kowarski", "birth_year": 1890, "death_year": 1948, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Tymon Niesiolowski", "birth_year": 1882, "death_year": 1965, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Eugeniusz Geppert", "birth_year": 1890, "death_year": 1979, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Waclaw Taranczewski", "birth_year": 1903, "death_year": 1987, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Adam Marczyński", "birth_year": 1908, "death_year": 1985, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Jerzy Fedkowicz", "birth_year": 1891, "death_year": 1959, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Jan Stanisławski", "birth_year": 1860, "death_year": 1907, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Konrad Srzednicki", "birth_year": 1894, "death_year": 1993, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Stanislaw Kamocki", "birth_year": 1875, "death_year": 1944, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Ludomir Slendzinski", "birth_year": 1889, "death_year": 1980, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Zygmunt Radnicki", "birth_year": 1894, "death_year": 1969, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Jacek Sienicki", "birth_year": 1928, "death_year": 2000, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Jerzy Panek", "birth_year": 1918, "death_year": 2001, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Benon Liberski", "birth_year": 1926, "death_year": 1983, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Andrzej Strumiłło", "birth_year": 1927, "death_year": 2020, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Stanislaw Fijałkowski", "birth_year": 1922, "death_year": 2020, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Jerzy Duda-Gracz", "birth_year": 1941, "death_year": 2004, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Franciszek Bunsch", "birth_year": 1952, "death_year": None, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Jaroslaw Modzelewski", "birth_year": 1955, "death_year": None, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Grupa Ładnie", "birth_year": None, "death_year": None, "category": "painter_group",
     "fp_risk": "high", "context": ["arte", "art", "painting", "gallery"],
     "notes": "Sasnal, Maciejowski, Bujnowski, Kowalski — juz dodani indywidualnie"},
    {"canonical_name": "Aleksandra Waliszewska", "birth_year": 1976, "death_year": None, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Anka Mierzejewska", "birth_year": 1973, "death_year": None, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Paulina Olowska", "birth_year": 1976, "death_year": None, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Agata Bogacka", "birth_year": 1976, "death_year": None, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Marta Deskur", "birth_year": 1962, "death_year": None, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Lech Majewski", "birth_year": 1953, "death_year": None, "category": "painter",
     "fp_risk": "high", "context": ["pintura", "arte", "painting", "film"],
     "notes": "Tez filmowiec — popularny wariant nazwiska"},
    {"canonical_name": "Tomasz Ciecierski", "birth_year": 1945, "death_year": None, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Koji Kamoji", "birth_year": 1935, "death_year": None, "category": "painter",
     "fp_risk": "low", "notes": "Japoncyzk ale calkowicie polski artysta"},
    {"canonical_name": "Krzysztof Bucka", "birth_year": 1958, "death_year": None, "category": "painter", "fp_risk": "low"},

    # ====================================================================
    # KOBIETY — DODATKOWE (zeby miec dobra reprezentacje)
    # ====================================================================
    {"canonical_name": "Katarzyna Grodecka", "birth_year": 1946, "death_year": None, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Alina Szapocznikow", "birth_year": 1926, "death_year": 1973, "category": "sculptor",
     "fp_risk": "low", "notes": "Juz dodana wyzej"},
    {"canonical_name": "Anna Bilinska-Bohdanowicz", "birth_year": 1857, "death_year": 1893, "category": "painter",
     "fp_risk": "low", "notes": "Jedna z pierwszych uznanych polskich malarek"},
    {"canonical_name": "Maria Pininska-Beres", "birth_year": 1931, "death_year": 1999, "category": "sculptor", "fp_risk": "low"},
    {"canonical_name": "Natalia Goncharova", "birth_year": 1881, "death_year": 1962, "category": "painter",
     "fp_risk": "low", "notes": "Rosyjsko-polska, awangarda"},
    {"canonical_name": "Wanda Czelkowska", "birth_year": 1930, "death_year": None, "category": "sculptor", "fp_risk": "low"},
    {"canonical_name": "Iwona Demko", "birth_year": 1974, "death_year": None, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Joanna Malinowska", "birth_year": 1972, "death_year": None, "category": "conceptual_artist",
     "fp_risk": "medium", "context": ["arte", "art", "video", "instalacao"]},
    {"canonical_name": "Anna Baumgart", "birth_year": 1966, "death_year": None, "category": "sculptor", "fp_risk": "low"},
    {"canonical_name": "Jadwiga Singer", "birth_year": 1879, "death_year": 1941, "category": "painter",
     "fp_risk": "high", "context": ["pintura", "arte", "painting", "polish"]},
    {"canonical_name": "Ewa Juszkiewicz", "birth_year": 1984, "death_year": None, "category": "painter",
     "fp_risk": "low", "notes": "Miedzynarodowa kariera, portrety"},
    {"canonical_name": "Maja Berezowska", "birth_year": 1893, "death_year": 1978, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Wanda Chelminská", "birth_year": 1891, "death_year": 1971, "category": "painter", "fp_risk": "low"},
    {"canonical_name": "Irena Lorentowicz", "birth_year": 1908, "death_year": 1985, "category": "sculptor",
     "fp_risk": "low", "notes": "Emigracja Brazylia — kluczowa dla leiloesbr!"},

    # ====================================================================
    # POLACY W BRAZYLII (szczegolnie istotni dla leiloesbr)
    # ====================================================================
    {"canonical_name": "Frans Krajcberg", "birth_year": 1921, "death_year": 2017, "category": "sculptor",
     "fp_risk": "low", "notes": "Polsko-brazylijski, ekologia, drewno"},
    {"canonical_name": "Pola Rezende", "birth_year": 1919, "death_year": 2010, "category": "painter",
     "fp_risk": "low", "notes": "Polka w Brazylii"},
    {"canonical_name": "Fayga Ostrower", "birth_year": 1920, "death_year": 2001, "category": "graphic_artist",
     "fp_risk": "low", "notes": "Urodzona w Lodzi, emigracja Brazylia, grafika"},
    {"canonical_name": "Irena Lorentowicz", "birth_year": 1908, "death_year": 1985, "category": "sculptor",
     "fp_risk": "low", "notes": "Emigracja Brazylia"},
    {"canonical_name": "Leopold Haar", "birth_year": 1910, "death_year": 1954, "category": "sculptor",
     "fp_risk": "medium", "context": ["escultura", "sculpture", "arte", "bronze"],
     "notes": "Emigracja Brazylia"},
    {"canonical_name": "August Zamoyski", "birth_year": 1893, "death_year": 1970, "category": "sculptor",
     "fp_risk": "low", "notes": "Emigracja Paryz/Brazylia — juz dodany wyzej"},
    {"canonical_name": "Tadeusz Lapinski", "birth_year": 1928, "death_year": 2016, "category": "painter",
     "fp_risk": "low", "notes": "Emigracja USA"},

    # ====================================================================
    # DODATKOWI RZEZBIARZ (z researchu)
    # ====================================================================
    {"canonical_name": "Konstanty Laszczka", "birth_year": 1865, "death_year": 1956, "category": "sculptor", "fp_risk": "low"},
    {"canonical_name": "Pius Welonski", "birth_year": 1849, "death_year": 1931, "category": "sculptor", "fp_risk": "low"},
    {"canonical_name": "Waclaw Szymanowski", "birth_year": 1859, "death_year": 1930, "category": "sculptor", "fp_risk": "low"},
    {"canonical_name": "Stanislaw Szukalski", "birth_year": 1893, "death_year": 1987, "category": "sculptor",
     "fp_risk": "low", "notes": "Emigracja USA, Szukalski movement"},
    {"canonical_name": "Jerzy Beres", "birth_year": 1930, "death_year": 2012, "category": "sculptor",
     "fp_risk": "low", "notes": "Performance i rzezba"},
    {"canonical_name": "Antoni Patek", "birth_year": 1851, "death_year": 1918, "category": "sculptor",
     "fp_risk": "high", "context": ["escultura", "sculpture", "rzezba", "arte", "polish"],
     "notes": "Patek to tez marka zegarkow — false positives"},
    {"canonical_name": "Tadeusz Breyer", "birth_year": 1874, "death_year": 1952, "category": "sculptor", "fp_risk": "low"},
    {"canonical_name": "Stanislaw Ostrowski", "birth_year": 1879, "death_year": 1947, "category": "sculptor",
     "fp_risk": "medium", "context": ["escultura", "sculpture", "bronze", "arte"]},
    {"canonical_name": "Alicja Bielawska", "birth_year": 1980, "death_year": None, "category": "sculptor", "fp_risk": "low"},

    # ====================================================================
    # DODATKOWI PLAKACISCI
    # ====================================================================
    {"canonical_name": "Hubert Hilscher", "birth_year": 1924, "death_year": 1999, "category": "poster_artist", "fp_risk": "low"},
    {"canonical_name": "Maciej Urbaniec", "birth_year": 1925, "death_year": 2004, "category": "poster_artist", "fp_risk": "low"},
    {"canonical_name": "Mieczyslaw Gorowski", "birth_year": 1941, "death_year": 2011, "category": "poster_artist", "fp_risk": "low"},
    {"canonical_name": "Wieslaw Rosocha", "birth_year": 1945, "death_year": None, "category": "poster_artist", "fp_risk": "low"},
    {"canonical_name": "Jerzy Czerniawski", "birth_year": 1947, "death_year": None, "category": "poster_artist", "fp_risk": "low"},
    {"canonical_name": "Eugeniusz Get-Stankiewicz", "birth_year": 1942, "death_year": 2011, "category": "poster_artist", "fp_risk": "low"},
    {"canonical_name": "Ryszard Kaja", "birth_year": 1962, "death_year": 2019, "category": "poster_artist", "fp_risk": "low"},
    {"canonical_name": "Sebastian Kubica", "birth_year": 1977, "death_year": None, "category": "poster_artist",
     "fp_risk": "high", "context": ["cartaz", "poster", "plakat", "design", "arte"],
     "notes": "Kubica to tez kierowca F1 — false positives"},
    {"canonical_name": "Jakub Zasada", "birth_year": 1981, "death_year": None, "category": "poster_artist", "fp_risk": "low"},
    {"canonical_name": "Eryk Lipinski", "birth_year": 1908, "death_year": 1991, "category": "poster_artist", "fp_risk": "low"},
    {"canonical_name": "Tadeusz Gronowski", "birth_year": 1894, "death_year": 1990, "category": "poster_artist",
     "fp_risk": "low", "notes": "Ojciec polskiego plakatu reklamowego"},
    {"canonical_name": "Roman Kalarus", "birth_year": 1951, "death_year": None, "category": "poster_artist", "fp_risk": "low"},
    {"canonical_name": "Jerzy Flisak", "birth_year": 1930, "death_year": 2008, "category": "poster_artist", "fp_risk": "low"},
    {"canonical_name": "Marian Stachurski", "birth_year": 1931, "death_year": 1980, "category": "poster_artist", "fp_risk": "low"},
    {"canonical_name": "Liliana Baczewska", "birth_year": 1930, "death_year": 2005, "category": "poster_artist", "fp_risk": "low"},
    {"canonical_name": "Tomasz Sarnecki", "birth_year": 1966, "death_year": None, "category": "poster_artist", "fp_risk": "low"},

    # ====================================================================
    # DODATKOWI GRAFICY
    # ====================================================================
    {"canonical_name": "Tadeusz Cieslewski", "birth_year": 1895, "death_year": 1944, "category": "graphic_artist",
     "fp_risk": "low", "notes": "Tadeusz Cieslewski syn, drzeworyt"},
    {"canonical_name": "Edmund Bartlomiejczyk", "birth_year": 1885, "death_year": 1950, "category": "graphic_artist", "fp_risk": "low"},
    {"canonical_name": "Halina Chrostowska", "birth_year": 1929, "death_year": 2015, "category": "graphic_artist", "fp_risk": "low"},
    {"canonical_name": "Jozef Szajna", "birth_year": 1922, "death_year": 2008, "category": "graphic_artist",
     "fp_risk": "low", "notes": "Tez scenograf i teatr"},
    {"canonical_name": "Ryszard Horowitz", "birth_year": 1939, "death_year": None, "category": "graphic_artist",
     "fp_risk": "medium", "context": ["fotografia", "photography", "arte", "design", "graphic"],
     "notes": "Emigracja USA, fotomontaz"},
    {"canonical_name": "Mieczyslaw Szczuka", "birth_year": 1898, "death_year": 1927, "category": "graphic_artist",
     "fp_risk": "low", "notes": "Konstruktywizm, grupa Blok"},
    {"canonical_name": "Teresa Zarnowerowna", "birth_year": 1897, "death_year": 1949, "category": "graphic_artist",
     "fp_risk": "low", "notes": "Konstruktywizm, grupa Blok"},
    {"canonical_name": "Karol Hiller", "birth_year": 1891, "death_year": 1939, "category": "graphic_artist",
     "fp_risk": "low", "notes": "Heliografia, awangarda"},
    {"canonical_name": "Marek Piasecki", "birth_year": 1935, "death_year": 2011, "category": "graphic_artist", "fp_risk": "low"},
    {"canonical_name": "Roslaw Szaybo", "birth_year": 1933, "death_year": 2019, "category": "graphic_artist",
     "fp_risk": "low", "notes": "Emigracja Londyn, okladki plyt"},
    {"canonical_name": "Wojciech Jastrzebowski", "birth_year": 1884, "death_year": 1963, "category": "graphic_artist",
     "fp_risk": "low", "notes": "Sztuka dekoracyjna / wzornictwo"},
    {"canonical_name": "Jan Bukowski", "birth_year": 1873, "death_year": 1938, "category": "graphic_artist",
     "fp_risk": "medium", "context": ["grafika", "graphic", "arte", "design", "drzeworyt"]},

    # ====================================================================
    # DODATKOWI FOTOGRAFOWIE
    # ====================================================================
    {"canonical_name": "Stefan Wojnecki", "birth_year": 1929, "death_year": 2017, "category": "photographer", "fp_risk": "low"},
    {"canonical_name": "Chris Niedenthal", "birth_year": 1950, "death_year": None, "category": "photographer",
     "fp_risk": "low", "notes": "Fotoreporter, Solidarnosc"},
    {"canonical_name": "Tomasz Gudzowaty", "birth_year": 1971, "death_year": None, "category": "photographer", "fp_risk": "low"},
    {"canonical_name": "Aneta Grzeszykowska", "birth_year": 1974, "death_year": None, "category": "photographer", "fp_risk": "low"},
    {"canonical_name": "Wojciech Prazmowski", "birth_year": 1949, "death_year": None, "category": "photographer", "fp_risk": "low"},

    # ====================================================================
    # DODATKOWI KONCEPTUALISCI / PERFORMANCE / INSTALACJA
    # ====================================================================
    {"canonical_name": "Zbigniew Warpechowski", "birth_year": 1938, "death_year": None, "category": "conceptual_artist",
     "fp_risk": "low", "notes": "Ojciec polskiego performance"},
    {"canonical_name": "Ewa Partum", "birth_year": 1945, "death_year": None, "category": "conceptual_artist",
     "fp_risk": "low", "notes": "Sztuka feministyczna, performance"},
    {"canonical_name": "Jan Swidzinski", "birth_year": 1923, "death_year": 2014, "category": "conceptual_artist",
     "fp_risk": "low", "notes": "Sztuka kontekstualna"},
    {"canonical_name": "Julita Wojcik", "birth_year": 1971, "death_year": None, "category": "conceptual_artist", "fp_risk": "low"},
    {"canonical_name": "Jadwiga Sawicka", "birth_year": 1959, "death_year": None, "category": "conceptual_artist", "fp_risk": "low"},
    {"canonical_name": "Goshka Macuga", "birth_year": 1967, "death_year": None, "category": "conceptual_artist",
     "fp_risk": "low", "notes": "Emigracja Londyn, instalacje"},
    {"canonical_name": "Robert Kusmirowski", "birth_year": 1973, "death_year": None, "category": "conceptual_artist", "fp_risk": "low"},
    {"canonical_name": "Konrad Smolenski", "birth_year": 1977, "death_year": None, "category": "conceptual_artist",
     "fp_risk": "low", "notes": "Instalacje dzwiekowe"},
    {"canonical_name": "Karol Kicinski", "birth_year": 1949, "death_year": None, "category": "graphic_artist", "fp_risk": "low"},

    # ====================================================================
    # WAZNE UZUPELNIENIA
    # ====================================================================
    {"canonical_name": "Ewa Kuryluk", "birth_year": 1946, "death_year": None, "category": "painter",
     "fp_risk": "low", "notes": "Malarstwo, tekstyl, instalacje, pisarka"},
    {"canonical_name": "Malgorzata Mirga-Tas", "birth_year": 1978, "death_year": None, "category": "painter",
     "fp_risk": "low", "notes": "Romska-polska artystka, Biennale Wenecja 2022"},
]
