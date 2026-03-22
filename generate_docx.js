const fs = require("fs");
const { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
        Header, Footer, AlignmentType, HeadingLevel, BorderStyle, WidthType,
        ShadingType, PageNumber, FootnoteReferenceRun, LevelFormat } = require("docx");

// ============================================================
// CONFIG
// ============================================================
const FONT = "Times New Roman";
const FONT_SIZE = 24; // 12pt
const LINE_SPACING = 360; // 1.5 line spacing (240 = single, 360 = 1.5)

const border = { style: BorderStyle.SINGLE, size: 1, color: "999999" };
const borders = { top: border, bottom: border, left: border, right: border };
const cellMargins = { top: 60, bottom: 60, left: 100, right: 100 };

// A4 page
const PAGE_W = 11906;
const PAGE_H = 16838;
const MARGIN = 1440; // 1 inch = 2.54cm
const CONTENT_W = PAGE_W - 2 * MARGIN; // ~9026

// ============================================================
// HELPERS
// ============================================================
function p(text, opts = {}) {
  const runs = [];
  // Parse text for **bold** markers
  const parts = text.split(/(\*\*.*?\*\*)/g);
  for (const part of parts) {
    if (part.startsWith("**") && part.endsWith("**")) {
      runs.push(new TextRun({ text: part.slice(2, -2), bold: true, font: FONT, size: FONT_SIZE, ...opts.runOpts }));
    } else if (part) {
      runs.push(new TextRun({ text: part, font: FONT, size: FONT_SIZE, ...opts.runOpts }));
    }
  }
  // Add footnote refs if specified
  if (opts.footnotes) {
    for (const fn of opts.footnotes) {
      runs.push(new FootnoteReferenceRun(fn));
    }
  }
  return new Paragraph({
    spacing: { line: opts.line || LINE_SPACING, after: opts.after || 120 },
    alignment: opts.align || AlignmentType.JUSTIFIED,
    indent: opts.indent ? { firstLine: 360 } : undefined,
    children: runs,
    ...(opts.heading ? { heading: opts.heading } : {}),
    ...(opts.pageBreakBefore ? { pageBreakBefore: true } : {}),
  });
}

function heading(level, text) {
  const hl = level === 1 ? HeadingLevel.HEADING_1 : level === 2 ? HeadingLevel.HEADING_2 : HeadingLevel.HEADING_3;
  return new Paragraph({
    heading: hl,
    spacing: { before: 360, after: 200, line: LINE_SPACING },
    children: [new TextRun({ text, font: FONT, size: level === 1 ? 28 : level === 2 ? 26 : FONT_SIZE, bold: true })],
  });
}

function cell(text, opts = {}) {
  const runs = [];
  const parts = text.split(/(\*\*.*?\*\*)/g);
  for (const part of parts) {
    if (part.startsWith("**") && part.endsWith("**")) {
      runs.push(new TextRun({ text: part.slice(2, -2), bold: true, font: FONT, size: 20 }));
    } else if (part) {
      runs.push(new TextRun({ text: part, font: FONT, size: 20, ...opts.runOpts }));
    }
  }
  return new TableCell({
    borders,
    margins: cellMargins,
    width: opts.width ? { size: opts.width, type: WidthType.DXA } : undefined,
    shading: opts.header ? { fill: "E8E8E8", type: ShadingType.CLEAR } : undefined,
    children: [new Paragraph({ spacing: { line: 240 }, children: runs })],
  });
}

function tableRow(cells, opts = {}) {
  return new TableRow({ children: cells.map((c, i) => {
    if (typeof c === "string") return cell(c, { width: opts.widths?.[i], header: opts.header });
    return c;
  })});
}

// ============================================================
// FOOTNOTES
// ============================================================
const footnotes = {};
const fnTexts = [
  "O rozproszeniu archiwów emigracji polskiej zob. R. Habielski, Życie społeczne i kulturalne emigracji, Warszawa 1999; M. Kryńska-Łowińska, Instytut Piłsudskiego w Londynie: geneza i działalność, \u201eTeki Archiwalne,\u201d seria nowa, t. 11, 2012. Instytut Piłsudskiego w Londynie przechowuje ponad 200 zespołów; Instytut Sikorskiego \u2014 ponad 400.",
  "Instytut Józefa Piłsudskiego w Londynie, zał. 15.III.1947, zarejestrowany w bazie SEZAM/IZA NDAP pod nr 709. Głuchowski figuruje wśród współzałożycieli. Zespół 70 wydzielony jako odrębna jednostka archiwalna.",
  "ARG/II/1, Biogram WBH nr 76/45, 24.V.1937. Potwierdza: OB PPS od 1905 (w wieku 17 lat), ZWC w Li\u00e8ge (współzałożyciel z T. Piskorem, późniejszym gen. dyw. i szefem Sztabu Głównego WP), Związek Strzelecki.",
  "Identyfikacja uczestników patrolu na podstawie: IPN, baza biogramowa (ipn.gov.pl); jpilsudski.org; fotokopia grupowa z podpisami ARG/II/2. Data patrolu: noc 2/3.VIII.1914. Zob. J. Litewski, Siódemka Beliny, Kraków 1999.",
  "ARG/II/15: zaproszenie dat. IV.1923, ceremonia 3.V.1923, Plac Saski, Warszawa. ARG/II/16: dyplom Ordinul Steaua Rom\u00e2niei, Comandor, podp. króla Ferdynanda I, Sinaia, 1.VIII.1923. ARG/II/17: pismo MSWojsk L.75/25 G.M.I. z 29.XI.1925.",
  "Encyklopedia PWN, hasło \u201eGłuchowski Janusz\u201d; IPN, biogram \u201eJanusz Głuchowski\u201d (ipn.gov.pl/pl/100-bohaterow-na-100-le/104516). Cmentarz Brompton, Londyn, grób nr 576.",
  "Opis Zespołu 70: Instytut Piłsudskiego w Londynie, pilsudski.org.uk/pl/archiwum-070.php (dostęp: III.2026). Inwentarz ma charakter ramowy; pełny opis na poziomie dokumentu dostępny w czytelni Instytutu.",
  "Obecność wierszy w Zespole 70 (jedn. 6, 1940\u20131945) jest zaskakująca i może wskazywać na aktywność literacką generała w okresie wojennym. Kalendarze i notatnik (jedn. 1) mogą pełnić funkcję dziennika.",
  "Odsetek 60% ma charakter szacunkowy, oparty na porównaniu inwentarza ramowego Zesp. 70 z pełnym katalogiem ARG. Pełna taksonomia wymaga dostępu do oryginałów obu zbiorów.",
  "ARG/II/27, list gen. broni Kazimierza Sosnkowskiego (1885\u20131969) do gen. dyw. Janusza Głuchowskiego, dat. 28.V.1964, Arundel, P. Qu\u00e9bec, Kanada. Inskrypcja: \u201eKochany Generale.\u201d Załącznik \u201ePro Memoria\u201d (ARG/II/28\u201329) z 24 pozycjami spraw. Głuchowski zmarł 14 dni później.",
  "Zespół 19 (Archiwum Sosnkowskiego), 33 jednostki. Jedn. 14: korespondencja ściśle tajna z dowódcami (1944, 1948\u201352); jedn. 15: kopie listów prywatnych (1939\u201344, 1970); jedn. 18: korespondencja wydawnicza (1964\u201365). Opis: pilsudski.org.uk/pl/archiwum-019.php.",
  "Zespół 17 (Archiwum L. Kmicic-Skrzyńskiego). Nota biograficzna wg opisu zespołu (pilsudski.org.uk/pl/archiwum-017.php): ur. 1893 Odessa, studia chemii w Nancy, Legiony, Oflag IID Gross-Born, 2 Korpus Polski, Manchester. Zmarł 14.II.1972.",
  "Instytut Piłsudskiego w Londynie, pełny katalog zbiorów: pilsudski.org.uk/pl/katalog.php. Rejestracja NDAP pod nr 709. Stan na III.2026: ponad 200 zespołów archiwalnych.",
];
for (let i = 0; i < fnTexts.length; i++) {
  footnotes[i + 1] = { children: [new Paragraph({ spacing: { line: 240 }, children: [new TextRun({ text: fnTexts[i], font: FONT, size: 18 })] })] };
}

// ============================================================
// DOCUMENT
// ============================================================

const doc = new Document({
  styles: {
    default: { document: { run: { font: FONT, size: FONT_SIZE } } },
    paragraphStyles: [
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 28, bold: true, font: FONT },
        paragraph: { spacing: { before: 360, after: 200 }, outlineLevel: 0 } },
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 26, bold: true, font: FONT },
        paragraph: { spacing: { before: 300, after: 180 }, outlineLevel: 1 } },
    ]
  },
  footnotes,
  sections: [{
    properties: {
      page: {
        size: { width: PAGE_W, height: PAGE_H },
        margin: { top: MARGIN, right: MARGIN, bottom: MARGIN, left: MARGIN }
      }
    },
    headers: {
      default: new Header({ children: [new Paragraph({
        alignment: AlignmentType.RIGHT,
        children: [new TextRun({ text: "Teki Archiwalne \u00b7 Artykuł archiwoznawczy", font: FONT, size: 16, italics: true, color: "888888" })]
      })] })
    },
    footers: {
      default: new Footer({ children: [new Paragraph({
        alignment: AlignmentType.CENTER,
        children: [new TextRun({ children: [PageNumber.CURRENT], font: FONT, size: 18 })]
      })] })
    },
    children: [
      // ============ TITLE PAGE ============
      new Paragraph({ spacing: { before: 2000, after: 100 }, children: [] }),

      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { after: 200 },
        children: [new TextRun({ text: "Od Siódemki Beliny do Instytutu Piłsudskiego:", font: FONT, size: 36, bold: true })]
      }),
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { after: 300 },
        children: [new TextRun({ text: "generał Janusz Głuchowski i dwa archiwa jednego życia", font: FONT, size: 36, bold: true })]
      }),
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { after: 400 },
        children: [new TextRun({ text: "Studium komplementarności kolekcji prywatnej ARG (217 jednostek) i Zespołu 70 Instytutu Józefa Piłsudskiego w Londynie na tle pięciu powiązanych zespołów archiwalnych", font: FONT, size: 22, italics: true, color: "555555" })]
      }),

      new Paragraph({ spacing: { before: 600, after: 80 }, alignment: AlignmentType.CENTER,
        children: [new TextRun({ text: "Marek Skonieczny", font: FONT, size: 26, bold: true })]
      }),
      new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 80 },
        children: [new TextRun({ text: "Badacz niezależny, Warszawa \u2013 Rio de Janeiro", font: FONT, size: 22, italics: true })]
      }),
      new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 200 },
        children: [new TextRun({ text: "skorek2000@yahoo.com", font: FONT, size: 22 })]
      }),

      new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 400, after: 100 },
        children: [new TextRun({ text: "Otrzymano: marzec 2026", font: FONT, size: 20, color: "888888" })]
      }),
      new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 100 },
        children: [new TextRun({ text: "Źródła: Kolekcja prywatna ARG (217 jedn.), Instytut Piłsudskiego w Londynie (Zesp. 17, 19, 22, 23, 70), WBH (biogram 76/45), AHM MPW (sygn. 1889)", font: FONT, size: 20, color: "888888" })]
      }),

      // ============ ABSTRAKT PL ============
      heading(1, "Abstrakt"),
      p("Artykuł przedstawia porównawczą analizę zasobów archiwalnych dokumentujących życie generała dywizji Janusza Juliana Głuchowskiego (1888\u20131964). Przedmiotem analizy są dwa zbiory: kolekcja prywatna ARG (217 jednostek w sześciu seriach, skatalogowana w standardzie ISAD(G)) oraz Zespół 70 Instytutu Józefa Piłsudskiego w Londynie (9 jednostek, 1916\u20131964). Na podstawie porównania inwentarzy metodą pozycja-po-pozycji zidentyfikowano dokumenty kategorii A (duplikaty), B (uzupełnienia) i C (unikaty). Około 60% dokumentów serii ARG/II (33 jednostki dotyczące generała) stanowi materiał nieobecny w Zespole 70. W szerszym kontekście archiwalnym wykazano powiązania z pięcioma kolejnymi zespołami Instytutu: Archiwum L. Kmicic-Skrzyńskiego (zesp. 17), Archiwum K. Sosnkowskiego (zesp. 19), Legiony 1914\u20131918 (zesp. 22), Wojna polsko-bolszewicka (zesp. 23) oraz Zbiór fotograficzny (zesp. 201). Artykuł dowodzi, że dopiero połączenie obu zbiorów \u2014 instytucjonalnego i prywatnego \u2014 pozwala zrekonstruować pełną biografię archiwalną jednego z założycieli Siódemki Beliny, twórcy 7 Pułku Ułanów Lubelskich, I Zastępcy Ministra Spraw Wojskowych i współzałożyciela samego Instytutu.", { runOpts: { italics: true } }),

      // ============ ABSTRACT EN ============
      heading(1, "Abstract"),
      p("This article presents a comparative analysis of archival resources documenting the life of Major General Janusz Julian Głuchowski (1888\u20131964). Two collections are examined: the private ARG collection (217 items in six series, catalogued according to ISAD(G)) and Collection 70 of the Józef Piłsudski Institute in London (9 items, 1916\u20131964). Through item-by-item inventory comparison, documents were classified as Category A (duplicates), B (supplements), or C (uniques). Approximately 60% of ARG Series II documents (33 items relating to the General) constitute material absent from Collection 70. The broader archival context reveals connections to five additional Institute collections. The article demonstrates that only by combining both holdings can the full archival biography of one of Belina\u2019s Seven, founder of the 7th Uhlan Regiment, First Deputy Minister of Military Affairs, and co-founder of the Institute itself, be reconstructed.", { runOpts: { italics: true } }),

      // ============ KEYWORDS ============
      p("**Słowa kluczowe:** archiwoznawstwo, komplementarność archiwalna, kolekcja prywatna, Instytut Piłsudskiego w Londynie, Siódemka Beliny, gen. Janusz Głuchowski, Polskie Siły Zbrojne, emigracja wojskowa, ISAD(G)"),
      p("**Keywords:** archival science, archival complementarity, private collection, Piłsudski Institute London, Belina\u2019s Seven, Polish Armed Forces, military emigration"),

      // ============ 1. WPROWADZENIE ============
      heading(1, "1. Wprowadzenie: problem rozproszenia źródeł"),

      p("Archiwa polskiej emigracji wojskowej po 1945 roku cechuje charakterystyczny podział: część dokumentacji trafiała do instytucji powołanych dla ochrony pamięci \u2014 Instytutu Piłsudskiego, Instytutu Sikorskiego, Biblioteki Polskiej w Paryżu \u2014 podczas gdy dokumenty o charakterze prywatnym pozostawały w rękach rodzin. Podział ten wynikał z praktyki archiwalnej: oficerowie przekazywali akta służby, rozkazy i korespondencję urzędową, zatrzymując listy osobiste, fotografie i pamiątki rodzinne.", { footnotes: [1], indent: true }),

      p("Generał dywizji Janusz Julian Głuchowski (1888\u20131964) stanowi modelowy przypadek takiego rozproszenia. Jego dokumentacja archiwalna istnieje w dwóch odrębnych zbiorach: Zespole 70 Instytutu Józefa Piłsudskiego w Londynie (9 jednostek archiwalnych, lata 1916\u20131964) oraz kolekcji prywatnej oznaczonej sygnaturą ARG (217 jednostek w sześciu seriach, skatalogowanej w standardzie ISAD(G) w 2026 roku). Dodatkową wartość analityczną wnosi fakt, że Głuchowski był współzałożycielem instytucji, w której jego własne akta są dziś przechowywane.", { footnotes: [2], indent: true }),

      p("Celem niniejszego artykułu jest: (1) porównanie zawartości obu zbiorów metodą inwentarza równoległego; (2) identyfikacja dokumentów komplementarnych, uzupełniających i unikalnych; (3) umieszczenie obu zbiorów w szerszym kontekście archiwalnym Instytutu Piłsudskiego, z uwzględnieniem pięciu powiązanych zespołów (nr 17, 19, 22, 23, 201).", { indent: true }),

      // ============ 2. NOTA BIOGRAFICZNA ============
      heading(1, "2. Nota biograficzna: od bojowca PPS do współzałożyciela Instytutu"),

      p("Janusz Julian Głuchowski urodził się 19 czerwca 1888 roku w Bukowej, powiat Piotrków Trybunalski. Był synem Mariana Głuchowskiego, działacza Polskiej Organizacji Narodowej, którego dokumenty zachowały się w serii ARG/I (6 jednostek, 1914). W 1905 roku, w wieku siedemnastu lat, wstąpił do Organizacji Bojowej PPS. Działał w niej do 1908 roku, po czym wyjechał na studia na Politechnikę w Li\u00e8ge, gdzie współzałożył z Tadeuszem Piskorem komórkę Związku Walki Czynnej. Sekwencję tę potwierdza biogram sporządzony przez Wojskowe Biuro Historyczne (nr 76/45, 24.V.1937), zachowany jako ARG/II/1.", { footnotes: [3], indent: true }),

      p("W nocy z 2 na 3 sierpnia 1914 roku Głuchowski, jako zastępca dowódcy Władysława Beliny-Prażmowskiego, uczestniczył w patrolu Siódemki Beliny \u2014 pierwszym regularnym oddziale polskim od Powstania Styczniowego. Skład patrolu, zweryfikowany na podstawie źródeł IPN i fotokopii grupowej z podpisami (ARG/II/2), przedstawia tabela 1.", { footnotes: [4], indent: true }),

      // Tabela 1: Siódemka Beliny
      p("**Tabela 1.** Skład patrolu Siódemki Beliny (2/3.VIII.1914)", { runOpts: { size: 20 }, after: 60 }),
      new Table({
        width: { size: CONTENT_W, type: WidthType.DXA },
        columnWidths: [2400, 1200, 2800, 2626],
        rows: [
          tableRow(["Uczestnik", "Lata życia", "Rola / los", "Źródła archiwalne"], { header: true, widths: [2400, 1200, 2800, 2626] }),
          tableRow(["W. Belina-Prażmowski", "1888\u20131938", "dowódca patrolu", "brak odr. zespołu"], { widths: [2400, 1200, 2800, 2626] }),
          tableRow(["Janusz Głuchowski", "1888\u20131964", "zastępca dowódcy", "**Zesp. 70** + kolekcja ARG"], { widths: [2400, 1200, 2800, 2626] }),
          tableRow(["S. Grzmot-Skotnicki", "ok. 1890\u20131939", "poległ IX.1939, Tułowice", "\u2014"], { widths: [2400, 1200, 2800, 2626] }),
          tableRow(["L. Bończa-Karwacki", "ok. 1889\u20131916", "poległ, Kostiuchnówka", "Zesp. 22, jedn. 47"], { widths: [2400, 1200, 2800, 2626] }),
          tableRow(["Z. Jabłoński \u201eZdzisław\u201d", "ok. 1896\u20131920", "poległ w wojnie 1920", "Zesp. 17 (wspomnienia)"], { widths: [2400, 1200, 2800, 2626] }),
          tableRow(["J. Hanka-Kulesza", "1892\u20131964", "zmarł 5.VI.1964, Londyn", "\u2014"], { widths: [2400, 1200, 2800, 2626] }),
          tableRow(["L. Kmicic-Skrzyński", "1893\u20131972", "ostatni żyjący; Manchester", "**Zesp. 17**"], { widths: [2400, 1200, 2800, 2626] }),
        ]
      }),
      new Paragraph({ spacing: { after: 200 }, children: [] }),

      p("Dalsze etapy kariery Głuchowskiego dokumentowane są przede wszystkim w serii ARG/II (33 jednostki). 5 listopada 1918 roku otrzymał rozkaz Sztabu Generalnego w Lublinie organizacji nowego oddziału jazdy (ARG/II/8) \u2014 przyszłego 7 Pułku Ułanów Lubelskich, którym dowodził do lipca 1920 roku. W okresie międzywojennym był dekorowany Legią Honorową przez marszałka Focha (3.V.1923, ARG/II/15), Orderem Gwiazdy Rumunii w stopniu komandora (1.VIII.1923, ARG/II/16), a w 1925 roku otrzymał dekret prezydencki zezwalający na noszenie odznaczeń zagranicznych (ARG/II/17).", { footnotes: [5], indent: true }),

      p("5 października 1935 roku został mianowany I Zastępcą Ministra Spraw Wojskowych (ARG/II/19). Po kampanii wrześniowej \u2014 internowanie w Rumunii, Palestyna (X.1940), Londyn (II.1941). Od września 1943 dowódca Polskich Jednostek Wojskowych w Wielkiej Brytanii. 1 czerwca 1945 \u2014 awans na generała dywizji. We wrześniu 1945 \u2014 Companion of the Order of the Bath (C.B.).", { indent: true }),

      p("15 marca 1947 roku Głuchowski współzałożył Instytut Józefa Piłsudskiego w Londynie \u2014 instytucję, której przekazał swoje akta urzędowe (obecny Zespół 70). Zmarł 11 czerwca 1964 roku w Londynie. Pochowany na cmentarzu Brompton (grób 576).", { footnotes: [6], indent: true }),

      // ============ 3. ZESPÓŁ 70 ============
      heading(1, "3. Zespół 70: inwentarz i charakterystyka"),

      p("Zespół 70 Instytutu Piłsudskiego w Londynie nosi nazwę \u201eArchiwum Janusza Głuchowskiego\u201d i obejmuje 9 jednostek archiwalnych z lat 1916\u20131964. Opis zespołu, dostępny na stronie Instytutu (pilsudski.org.uk/pl/archiwum-070.php), pozwala zrekonstruować następującą strukturę:", { footnotes: [7], indent: true }),

      p("**Tabela 2.** Inwentarz Zespołu 70 \u2014 Archiwum Janusza Głuchowskiego", { runOpts: { size: 20 }, after: 60 }),
      new Table({
        width: { size: CONTENT_W, type: WidthType.DXA },
        columnWidths: [500, 4526, 1500, 2500],
        rows: [
          tableRow(["Nr", "Opis jednostki", "Daty", "Charakter"], { header: true, widths: [500, 4526, 1500, 2500] }),
          tableRow(["1", "Życiorys, rozkazy, nominacje, dokumenty osobiste (kalendarze, notatnik, listy), broszury, wycinki z gazet", "1916\u20131964", "osobisty / służbowy"], { widths: [500, 4526, 1500, 2500] }),
          tableRow(["2", "Korespondencja z Kołem Generałów, Pułkowników i byłych wyższych dowódców; wykaz adresów", "1948\u20131963", "korporacyjny"], { widths: [500, 4526, 1500, 2500] }),
          tableRow(["3", "Korespondencja służbowa i prywatna", "1940\u20131961", "mieszany"], { widths: [500, 4526, 1500, 2500] }),
          tableRow(["4", "Wspomnienia, przemówienia", "b.d.", "narracyjny"], { widths: [500, 4526, 1500, 2500] }),
          tableRow(["5", "Korespondencja", "1943\u20131963", "mieszany"], { widths: [500, 4526, 1500, 2500] }),
          tableRow(["6", "Raporty, sprawozdania ze Sztabu Głównego, zapisy rozmów, wiersze", "1940\u20131945", "służbowy / literacki"], { widths: [500, 4526, 1500, 2500] }),
          tableRow(["7", "Korespondencja z prasą, wycinki prasowe", "b.d.", "prasowy"], { widths: [500, 4526, 1500, 2500] }),
          tableRow(["8", "Brudnopisy", "b.d.", "roboczy"], { widths: [500, 4526, 1500, 2500] }),
          tableRow(["9", "Emigracja \u2014 druki ulotne, komunikaty, rozkazy, orędzia, odezwy", "1946\u20131961", "emigracyjny"], { widths: [500, 4526, 1500, 2500] }),
        ]
      }),
      new Paragraph({ spacing: { after: 200 }, children: [] }),

      p("Analiza inwentarza ujawnia kilka cech istotnych dla dalszego porównania. Po pierwsze, Zespół 70 ma charakter przede wszystkim **służbowy i korporacyjny**: dominuje korespondencja urzędowa (jedn. 2, 3, 5), raporty wojskowe (jedn. 6) i materiały emigracyjne (jedn. 9). Po drugie, zbiór obejmuje wyłącznie dokumenty samego generała \u2014 brak jakiejkolwiek dokumentacji rodzinnej. Po trzecie, zasługują na uwagę dwa elementy niespodziewane: **wiersze** (jedn. 6) oraz **kalendarze i notatnik** (jedn. 1), które mogą mieć walor źródła narracyjnego.", { footnotes: [8], indent: true }),

      // ============ 4. KOLEKCJA ARG ============
      heading(1, "4. Kolekcja prywatna ARG: struktura i zakres"),

      p("Kolekcja prywatna ARG (Archiwum Rodziny Głuchowskich) została skatalogowana w 2026 roku w standardzie ISAD(G). Obejmuje 217 jednostek w sześciu seriach, z których każda odpowiada jednemu członkowi rodziny lub kategorii dokumentów:", { indent: true }),

      p("**Tabela 3.** Struktura kolekcji ARG", { runOpts: { size: 20 }, after: 60 }),
      new Table({
        width: { size: CONTENT_W, type: WidthType.DXA },
        columnWidths: [1000, 2526, 600, 1200, 3700],
        rows: [
          tableRow(["Seria", "Osoba", "Jedn.", "Daty", "Charakter"], { header: true, widths: [1000, 2526, 600, 1200, 3700] }),
          tableRow(["ARG/I", "Marian Głuchowski (ojciec)", "6", "1914", "PON, działalność niepodległościowa"], { widths: [1000, 2526, 600, 1200, 3700] }),
          tableRow(["ARG/II", "Gen. dyw. Janusz Głuchowski", "33", "1905\u20131964", "służba wojskowa, ordery, korespondencja, fotografie"], { widths: [1000, 2526, 600, 1200, 3700] }),
          tableRow(["ARG/III", "Ppor. Stanisław Stefan Głuchowski", "38", "1944\u20131945", "AK, Powstanie Warszawskie, Stalag XI-B"], { widths: [1000, 2526, 600, 1200, 3700] }),
          tableRow(["ARG/IV", "Lech Głuchowski \u201eJeżycki\u201d", "wzm.", "1900\u20131944", "poległ w Powstaniu 15.IX.1944"], { widths: [1000, 2526, 600, 1200, 3700] }),
          tableRow(["ARG/V", "Krzysztof Głuchowski \u201eJuraś\u201d", "150+", "1926\u20132020", "Powstanie, jeniec, emigracja, Brazylia"], { widths: [1000, 2526, 600, 1200, 3700] }),
          tableRow(["ARG/VI", "Varia / Rodzina", "22", "różne", "dokumenty podróży, pamiątki, korespondencja"], { widths: [1000, 2526, 600, 1200, 3700] }),
        ]
      }),
      new Paragraph({ spacing: { after: 200 }, children: [] }),

      p("Kluczowa różnica między oboma zbiorami leży w **zakresie podmiotowym**. Zespół 70 dokumentuje wyłącznie generała. Kolekcja ARG dokumentuje całą rodzinę \u2014 pięć osób w trzech pokoleniach, z których każde walczyło o niepodległość innymi środkami: ojciec w PON (1914), generał w Legionach i II RP, bracia w AK i Powstaniu Warszawskim, bratanek jako młodociany powstaniec, a następnie emigrant w Brazylii. Ten wielopokoleniowy kontekst jest niedostępny z poziomu Zespołu 70.", { indent: true }),

      // ============ 5. METODOLOGIA ============
      heading(1, "5. Metodologia porównania inwentarzy"),

      p("Analizę komplementarności przeprowadzono metodą **inwentarza równoległego**: dla każdego dokumentu serii ARG/II (33 jednostki) weryfikowano, czy odpowiadający mu dokument istnieje w Zespole 70, i odwrotnie. Zastosowano trzy kategorie klasyfikacyjne:", { indent: true }),

      p("**Kategoria A \u2014 duplikaty.** Dokumenty obecne w obu zbiorach (np. odpisy mianowań, kopie rozkazów). Wartość archiwalna: potwierdzająca, uwierzytelniająca.", { indent: true }),
      p("**Kategoria B \u2014 uzupełnienia.** Dokumenty obecne tylko w jednym zbiorze, dotyczące okresów lub wydarzeń udokumentowanych w drugim. Wartość: kontekstualizująca.", { indent: true }),
      p("**Kategoria C \u2014 unikaty.** Dokumenty bez odpowiednika w drugim zbiorze. Wartość: najwyższa, źródłowa.", { indent: true }),

      p("**Tabela 4.** Wybór dokumentów kategorii B i C z serii ARG/II", { runOpts: { size: 20 }, after: 60 }),
      new Table({
        width: { size: CONTENT_W, type: WidthType.DXA },
        columnWidths: [1200, 3126, 500, 4200],
        rows: [
          tableRow(["Sygn.", "Dokument", "Kat.", "Relacja do Zesp. 70"], { header: true, widths: [1200, 3126, 500, 4200] }),
          tableRow(["ARG/II/2", "Fotokopia Siódemki Beliny z podpisami", "C", "Brak ikonografii założycielskiej w Zesp. 70"], { widths: [1200, 3126, 500, 4200] }),
          tableRow(["ARG/II/8", "Rozkaz Szt. Gen., Lublin, 5.XI.1918", "B", "Akt założycielski 7 P.Uł.; prawdopodobnie odpisy w jedn. 1"], { widths: [1200, 3126, 500, 4200] }),
          tableRow(["ARG/II/14", "List marsz. Śmigłego-Rydza (~1935\u20131939)", "C", "Koresp. prywatna z Naczelnym Wodzem; brak odpowiednika"], { widths: [1200, 3126, 500, 4200] }),
          tableRow(["ARG/II/15", "Zaproszenie na dekorację przez marsz. Focha (1923)", "B", "Dokumentuje ceremonię nieobjętą aktami urzędowymi"], { widths: [1200, 3126, 500, 4200] }),
          tableRow(["ARG/II/16", "Dyplom Orderu Gwiazdy Rumunii, komandor (1923)", "C", "Oryginał dyplomu; w Zesp. 70 najwyżej wzmianka"], { widths: [1200, 3126, 500, 4200] }),
          tableRow(["ARG/II/17", "Dekret prezydencki \u2014 ordery zagraniczne (1925)", "B", "Uzupełnia dokumentację orderową jedn. 1"], { widths: [1200, 3126, 500, 4200] }),
          tableRow(["ARG/II/23", "Portret oficjalny w mundurze galowym (lata 30.)", "C", "Jedyny znany pełny portret formalny"], { widths: [1200, 3126, 500, 4200] }),
          tableRow(["ARG/II/27", "List gen. Sosnkowskiego, Kanada (28.V.1964)", "C", "Koresp. prywatna; 14 dni przed śmiercią"], { widths: [1200, 3126, 500, 4200] }),
          tableRow(["ARG/II/28\u201329", "\u201ePro Memoria\u201d Sosnkowskiego \u2014 24 sprawy", "C", "Mapa siatki emigracyjnej; Giedroyc, Nowak-Jeziorański"], { widths: [1200, 3126, 500, 4200] }),
        ]
      }),
      new Paragraph({ spacing: { after: 200 }, children: [] }),

      p("Wstępne wyniki wskazują, że około 60% dokumentów serii ARG/II należy do kategorii B lub C \u2014 stanowi zatem materiał nieobecny lub niedostatecznie udokumentowany w Zespole 70. Pełna taksonomia wymaga jednak dostępu do oryginałów obu zasobów i porównania na poziomie dokumentu jednostkowego.", { footnotes: [9], indent: true }),

      // ============ 6. LIST SOSNKOWSKIEGO ============
      heading(1, "6. List Sosnkowskiego jako studium przypadku źródła unikalnego"),

      p("Spośród dokumentów kategorii C, szczególnej analizy wymaga zespół trzech dokumentów: list gen. broni Kazimierza Sosnkowskiego do gen. Głuchowskiego (ARG/II/27) wraz z dwustronicowym załącznikiem \u201ePro Memoria\u201d (ARG/II/28\u201329), datowany 28 maja 1964 roku, Arundel, prowincja Quebec, Kanada.", { footnotes: [10], indent: true }),

      p("Sosnkowski \u2014 były Naczelny Wódz PSZ (1943\u20131944), założyciel ZWC, najbliższy współpracownik Piłsudskiego \u2014 użył formuły \u201eKochany Generale.\u201d W treści przepraszał za nieporozumienie dotyczące Instytutu Piłsudskiego i sprawy Larousse\u2019a. Obiecywał przyśpieszyć pracę nad tekstem o patrolu Beliny. Głuchowski zmarł czternaście dni później.", { indent: true }),

      p("Załącznik \u201ePro Memoria\u201d stanowi listę 24 spraw prowadzonych jednocześnie przez Sosnkowskiego. Pozycja 5: prośba Głuchowskiego o tekst o początkach kawalerii. Pozycja 7: prośba płk. Smoleńskiego o wspomnienia z patrolu Beliny. W dalszych pozycjach pojawiają się: Jerzy Giedroyc (paryska \u201eKultura,\u201d dwa artykuły), Jan Nowak-Jeziorański (Radio Wolna Europa), 21. rocznica śmierci gen. Sikorskiego (Chicago). Dokument stanowi mapę siatki polskiego życia intelektualnego na uchodźstwie \u2014 od Buenos Aires po Toronto \u2014 i jako taki ma wartość wykraczającą poza biografię adresata.", { indent: true }),

      p("Wartość archiwalna tego zespołu dokumentów jest potrójna: (1) stanowi jedno z ostatnich świadectw relacji Sosnkowski\u2013Głuchowski, trwającej od 1913 roku; (2) jako \u201ePro Memoria\u201d dokumentuje metodę pracy i siatkę kontaktów byłego Naczelnego Wodza; (3) koresponduje bezpośrednio z Zespołem 19 Instytutu (Archiwum Sosnkowskiego, 33 jednostki), gdzie mogą znajdować się listy Głuchowskiego do Sosnkowskiego \u2014 zamykając potencjalnie łuk korespondencji.", { footnotes: [11], indent: true }),

      // ============ 7. SZERSZY KONTEKST ============
      heading(1, "7. Szerszy kontekst archiwalny: zespoły powiązane"),

      p("Obydwa zbiory \u2014 Zespół 70 i kolekcja ARG \u2014 nie istnieją w izolacji archiwalnej. W zasobach Instytutu Piłsudskiego w Londynie (ponad 200 zespołów) zidentyfikowano pięć dalszych zasobów bezpośrednio powiązanych z biografią generała Głuchowskiego i historią kolekcji ARG.", { indent: true }),

      p("**Tabela 5.** Zespoły Instytutu Piłsudskiego powiązane z kolekcją ARG", { runOpts: { size: 20 }, after: 60 }),
      new Table({
        width: { size: CONTENT_W, type: WidthType.DXA },
        columnWidths: [600, 2126, 3600, 2700],
        rows: [
          tableRow(["Zesp.", "Nazwa", "Zawartość istotna", "Powiązanie z ARG"], { header: true, widths: [600, 2126, 3600, 2700] }),
          tableRow(["17", "Archiwum L. Kmicic-Skrzyńskiego", "Dok. 1 P.Uł. Legionów i 7 P.Uł. Lubelskich. Pamiętnik 1916\u201318. Nagrania RWE (1964). Wspomnienia o A. Jabłońskim.", "Lustrzane odbicie ARG/II. Dwóch z Siódemki w jednym Instytucie."], { widths: [600, 2126, 3600, 2700] }),
          tableRow(["19", "Archiwum K. Sosnkowskiego (33 jedn.)", "Koresp. ściśle tajna z dowódcami. Kopie listów prywatnych. Koresp. wydawnicza 1964\u201365.", "Potencjalna \u201edruga strona\u201d korespondencji ARG/II/27\u201329."], { widths: [600, 2126, 3600, 2700] }),
          tableRow(["22", "Legiony 1914\u20131918 (120 jedn.)", "Kronika 1 P.Uł. z listami oficerów. Wspomnienia o Kostiuchnówce. Lista starszeństwa oficerów.", "Dokumentuje okres Siódemki; Głuchowski w wykazach."], { widths: [600, 2126, 3600, 2700] }),
          tableRow(["23", "Wojna 1919\u20131920", "Telegramy frontowe VIII.1920. Historia 1 Dyw. Jazdy. Koresp. oficera łącznikowego przy marsz. Fochu.", "Głuchowski dowodził 7 P.Uł.; Foch dekorował go w 1923."], { widths: [600, 2126, 3600, 2700] }),
          tableRow(["201", "Zbiór fotograficzny", "Albumy z I wojny, międzywojnia, emigracji.", "Potencjalne zdjęcia Głuchowskiego i Siódemki."], { widths: [600, 2126, 3600, 2700] }),
        ]
      }),
      new Paragraph({ spacing: { after: 200 }, children: [] }),

      p("Szczególnie istotny jest Zespół 17. Generał Ludwik Kmicic-Skrzyński (1893\u20131972), urodzony w Odessie, studiował chemię w Nancy, organizował pluton Związku Strzeleckiego, walczył w Legionach, przeszedł przez Oflag IID Gross-Born, służył w 2 Korpusie Polskim, a po wojnie osiadł w Manchesterze. Jego archiwum zawiera: pamiętnik z lat 1916\u20131918 (jedn. 3), wspomnienia nagrywane dla Radia Wolna Europa w 1964 roku (jedn. 7) oraz materiały dotyczące zarówno 1 Pułku Ułanów Legionów (Beliniaków), jak i 7 Pułku Ułanów Lubelskich \u2014 pułku założonego przez Głuchowskiego. W jednostce 2 znajdują się wspomnienia Stefana Stablewskiego o Antonim Jabłońskim \u2014 uczestniku Siódemki Beliny, który poległ w wojnie 1920 roku.", { footnotes: [12], indent: true }),

      p("Fakt, że dwóch z siedmiu kawalerzystów patrolu założycielskiego złożyło swoje archiwa w tym samym Instytucie \u2014 który jeden z nich współzałożył \u2014 pozwala na unikalne zestawienie: rekonstrukcję historii Siódemki z dwóch perspektyw osobistych, uzupełnionych o relacje z kolekcji ARG i materiały z Zespołu 22 (Legiony). Belina-Prażmowski, dowódca patrolu, nie pozostawił odrębnego archiwum (zmarł w 1938), co dodatkowo podnosi wartość źródeł zachowanych przez jego zastępcę i ostatniego żyjącego członka patrolu.", { indent: true }),

      // ============ 8. INSTYTUT ============
      heading(1, "8. Instytut jako archiwum i pamięć: rola Głuchowskiego-założyciela"),

      p("Instytut Józefa Piłsudskiego w Londynie, założony 15 marca 1947 roku, gromadzi ponad 200 zespołów archiwalnych dokumentujących historię polskiej emigracji wojskowej i politycznej. Wśród zdigitalizowanych kolekcji znajdują się archiwa najwyższych dowódców (Piłsudski \u2014 zesp. 1, Sosnkowski \u2014 zesp. 19, Dąb-Biernacki \u2014 zesp. 47), dokumentacja instytucji (Legiony \u2014 zesp. 22, PSZ w ZSRR \u2014 zesp. 21, Traktat Ryski \u2014 zesp. 106), a także zbiory specjalne (mapy \u2014 zesp. 200, fotografie \u2014 zesp. 201). Zasoby Instytutu są zarejestrowane w bazie SEZAM i IZA Naczelnej Dyrekcji Archiwów Państwowych pod numerem 709.", { footnotes: [13], indent: true }),

      p("Przypadek Głuchowskiego jest archiwoznawczo wyjątkowy: twórca zespołu (Zesp. 70) był jednocześnie współtwórcą instytucji przechowującej ten zespół. Ta podwójna rola \u2014 depozytariusza i założyciela \u2014 rodzi pytanie o świadomość archiwistyczną: czy generał dokonując selekcji dokumentów do przekazania, miał świadomość tego, które akta należą do sfery publicznej, a które do prywatnej? Zestawienie inwentarzy sugeruje, że tak: Zespół 70 ma charakter wyraźnie urzędowy (raporty, rozkazy, korespondencja służbowa), podczas gdy w rodzinie pozostały dokumenty o charakterze osobistym (listy prywatne, fotografie, ordery w oryginałach, pamiątki). Ten świadomy podział jest sam w sobie źródłem informacji o mentalności archiwalnej twórcy zespołu.", { indent: true }),

      // ============ 9. WNIOSKI ============
      heading(1, "9. Wnioski"),

      p("Analiza porównawcza kolekcji prywatnej ARG i Zespołu 70 Instytutu Piłsudskiego prowadzi do następujących wniosków:", { indent: true }),

      p("**1.** Oba zbiory są **komplementarne, nie konkurencyjne**. Zespół 70 (9 jednostek) dokumentuje karierę oficjalną. Kolekcja ARG/II (33 jednostki) dokumentuje życie prywatne, relacje osobiste i kontekst rodzinny. Dopiero połączenie obu pozwala zrekonstruować pełną biografię archiwalną.", { indent: true }),

      p("**2.** Kolekcja ARG zawiera **dokumenty o najwyższej wartości źródłowej**, nieobecne w zbiorach instytucjonalnych: korespondencja Sosnkowskiego z \u201ePro Memoria\u201d (ARG/II/27\u201329), list marszałka Śmigłego-Rydza (ARG/II/14), oryginalny dyplom Orderu Gwiazdy Rumunii (ARG/II/16), fotokopia Siódemki Beliny z podpisami (ARG/II/2). Każdy z tych dokumentów stanowi unikat.", { indent: true }),

      p("**3.** **Wielopokoleniowy charakter kolekcji ARG** (5 osób w 6 seriach) daje jej wartość niedostępną z poziomu Zespołu 70. Rodzina Głuchowskich stanowi mikrohistorię polskiego XX wieku.", { indent: true }),

      p("**4.** **Powiązania z pięcioma kolejnymi zespołami** Instytutu (17, 19, 22, 23, 201) tworzą szeroki kontekst archiwalny. Zespół 17 (Kmicic-Skrzyński) jest tu szczególnie istotny: dwóch z Siódemki Beliny złożyło swoje archiwa w tej samej instytucji.", { indent: true }),

      p("**5.** Podział dokumentów między zbiór instytucjonalny i prywatny odzwierciedla **świadomy wybór archiwalny twórcy zespołu**, który był jednocześnie współzałożycielem instytucji przechowującej jego akta.", { indent: true }),

      p("**Postulat badawczy:** Wskazane jest przeprowadzenie pełnej analizy porównawczej na poziomie dokumentu jednostkowego, obejmującej dostęp do oryginałów Zespołu 70 w czytelni Instytutu Piłsudskiego w Londynie, a także kwerendę w Zespołach 17 i 19 pod kątem korespondencji wzajemnej.", { indent: true }),

      // ============ BIBLIOGRAFIA ============
      heading(1, "Bibliografia"),

      heading(2, "Źródła archiwalne"),
      p("Kolekcja prywatna ARG \u2014 Archiwum Rodziny Głuchowskich. 217 jednostek w 6 seriach (ARG/I\u2013VI). Skatalogowane w standardzie ISAD(G), 2026."),
      p("Instytut Józefa Piłsudskiego w Londynie, Zespół 17 \u2014 Archiwum Ludwika Kmicic-Skrzyńskiego. 8 jednostek."),
      p("Instytut Józefa Piłsudskiego w Londynie, Zespół 19 \u2014 Archiwum Kazimierza Sosnkowskiego. 33 jednostki."),
      p("Instytut Józefa Piłsudskiego w Londynie, Zespół 22 \u2014 Legiony 1914\u20131918. 120 jednostek."),
      p("Instytut Józefa Piłsudskiego w Londynie, Zespół 23 \u2014 Wojna polsko-bolszewicka 1919\u20131920."),
      p("Instytut Józefa Piłsudskiego w Londynie, Zespół 70 \u2014 Archiwum Janusza Głuchowskiego. 9 jednostek, 1916\u20131964."),
      p("Instytut Józefa Piłsudskiego w Londynie, Zespół 201 \u2014 Zbiór fotograficzny."),
      p("Wojskowe Biuro Historyczne, Biogram nr 76/45 (24.V.1937) \u2014 gen. Janusz Głuchowski."),
      p("Archiwum Historii Mówionej Muzeum Powstania Warszawskiego, sygn. 1889."),

      heading(2, "Opracowania"),
      p("Chmielarz A., Kedyw Okręgu Warszawa Armii Krajowej. Dokumenty \u2014 rok 1944, Warszawa 2014."),
      p("Habielski R., Życie społeczne i kulturalne emigracji, Warszawa 1999."),
      p("Kryńska-Łowińska M., \u201eInstytut Piłsudskiego w Londynie: geneza i działalność,\u201d Teki Archiwalne, seria nowa, t. 11, 2012."),
      p("Litewski J., Siódemka Beliny, Kraków 1999."),
      p("Stachiewicz P., Parasol. Dzieje oddziału do zadań specjalnych Kedywu Komendy Głównej AK, Warszawa 1984."),
      p("Wroński T., Kronika Powstania Warszawskiego, Warszawa 2004."),

      heading(2, "Portale i bazy danych"),
      p("Instytut Józefa Piłsudskiego w Londynie \u2014 katalog zbiorów: pilsudski.org.uk/pl/katalog.php"),
      p("Instytut Piłsudskiego w Ameryce \u2014 baza archiwalna: pilsudski.org"),
      p("Instytut Pamięci Narodowej \u2014 baza biogramowa: ipn.gov.pl"),
      p("Encyklopedia PWN: encyklopedia.pwn.pl/haslo/Gluchowski-Janusz;3906169.html"),
      p("Muzeum Powstania Warszawskiego \u2014 biogramy: 1944.pl"),
      p("Naczelna Dyrekcja Archiwów Państwowych: szukajwarchiwach.gov.pl (baza SEZAM/IZA, nr 709)"),
    ]
  }]
});

// ============================================================
// GENERATE
// ============================================================
Packer.toBuffer(doc).then(buffer => {
  fs.writeFileSync("C:/Users/skore/leiloesbr-scraper/docs/artykul_belina_instytut.docx", buffer);
  console.log("OK: artykul_belina_instytut.docx created");
});
