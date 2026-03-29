# Instrukcja transkrypcji skanów — Kolekcja Głuchowskich

## Techniki enhancowania obrazu (Python/Pillow)

```python
from PIL import Image, ImageEnhance, ImageFilter, ImageOps

img = Image.open("skan.jpeg")

# 1. Upscale 3-4× (LANCZOS = najlepsza interpolacja)
img = img.resize((img.width * 3, img.height * 3), Image.LANCZOS)

# 2. Grayscale
img = img.convert('L')

# 3. Autocontrast (rozciąga histogram, cutoff=2 usuwa 2% outlierów)
img = ImageOps.autocontrast(img, cutoff=2)

# 4. Contrast boost (1.5-2.5 zależnie od skanu)
img = ImageEnhance.Contrast(img).enhance(2.0)

# 5. Sharpen (opcjonalnie, 1-2 razy)
img = img.filter(ImageFilter.SHARPEN)

# 6. Dla BARDZO trudnych: binaryzacja (czarno-białe)
img = img.point(lambda x: 0 if x < 140 else 255, '1')

# 7. Split na połówki dla dużych skanów
w, h = img.size
top = img.crop((0, 0, w, h//2))
bot = img.crop((0, h//2, w, h))
```

## Techniki odczytywania pisma odręcznego

### Ogólne zasady
1. **Czytaj KONTEKST przed literami** — jeśli list mówi o wojsku, słowo "kpt." ma sens, "kapt." nie
2. **Porównuj litery w obrębie dokumentu** — jak autor pisze "k"? "w"? "ł"? Znajdź wzorzec
3. **Imiona i nazwiska sprawdzaj w indeksie osób** — katalog ma indeks, użyj go
4. **Daty i miejsca weryfikuj z itinerarium** (ARG/V/203) — pełna trasa Krzysztofa
5. **Nieczytelne oznaczaj [?] lub [...]** — NIGDY nie zgaduj, lepiej luka niż błąd

### Specyfika pisma w kolekcji
- **Wanda Głuchowska**: pochyłe, atrament niebieski, zdrobnienia ("Krysieńku", "Mateńko")
- **Krzysztof**: drobne, gęste, młodzieńcze, często skreślenia
- **Kamiński**: czytelne, niebieski atrament na jasnoniebieskim papierze
- **Dębski ("Koniuś")**: kolokwialne, pełne żargonu, humor żołnierski
- **Krahelski ("Leszek")**: czytelne, wojskowe
- **Dokumenty urzędowe**: drukowane formularze z odręcznymi wpisami — puste pola = [puste], nie [...]

### Kontekst historyczny (kluczowe daty)
- IX-X.1944: Powstanie Warszawskie, kapitulacja, niewola
- X.1944-IV.1945: Stalag XI B Fallingbostel, przerzuty (Dorsten, Gladbach, Gerresheim)
- 25.IV.1945: wyzwolenie, Düsseldorf
- V-VII.1945: Reims → Paryż → Marsylia → Włochy (CMF)
- 1945-1946: Liceum 3 DSK (Gimnazjum), Włochy
- VII.1946: przeniesienie do Anglii, Bodney Airfield
- 1947: demobilizacja, PKPR, Coventry/High Wycombe/Sudbury
- 1949: emigracja do Brazylii

### Kluczowe skróty w dokumentach
- CMF = Central Mediterranean Forces (Włochy)
- 3 DSK = 3 Dywizja Strzelców Karpackich
- 7 P.Uł. = 7 Pułk Ułanów Lubelskich (kryptonim "Jeleń")
- PKPR = Polski Korpus Przysposobienia i Rozmieszczenia
- st.uł. = starszy ułan
- KH = Krzyż Harcerski
- AK = Armia Krajowa
- KWO AK = Komenda Warszawskiego Okręgu AK
- Pluton 1112 = jednostka Krzysztofa (kryptonim "Jeleń")

### Mapowanie plików
- `docs/MAPPING_JURAS_ARGV.txt` — juras_NNN → ARG/V/NNN
- `docs/gluchowski_img/originals_201_217/MAPPING.txt` — skany → sygnatury
- Enhancowane: `docs/gluchowski_img/juras_NNN_enhanced.jpg`
- Obrócone: `*_rot.jpg`

### Workflow
1. Otwórz skan: `Read docs/gluchowski_img/PLIK.jpeg`
2. Jeśli nieczytelny — enhancuj (kod wyżej), zapisz jako `_enhanced.jpg`
3. Czytaj linia po linii, od góry
4. Oznaczaj [?] i [...] uczciwie
5. Sprawdź kontekst: kto pisze? skąd? kiedy? do kogo?
6. Zapisz do `docs/research_gluchowski.md`
7. Commitnij

## Pliki do pracy
- Skany oryginalne: `docs/gluchowski_img/originals_201_217/`
- Skany z katalogu: `docs/gluchowski_img/Seria_29z_*.jpeg` i `Kolekcja_Gluchowski_*.jpeg`
- Transkrypcje: `transcriptions.py`
- Katalog: `katalog_gluchowski_v4.py`
- Notatki: `docs/research_gluchowski.md`
