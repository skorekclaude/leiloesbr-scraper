const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  Header, Footer, AlignmentType, LevelFormat,
  FootnoteReferenceRun, HeadingLevel, BorderStyle, WidthType, ShadingType,
  PageNumber, PageBreak, TabStopType, TabStopPosition
} = require("docx");

// Helper: create a text run
const t = (text, opts = {}) => new TextRun({ text, ...opts });
const ti = (text, opts = {}) => new TextRun({ text, italics: true, ...opts });
const tb = (text, opts = {}) => new TextRun({ text, bold: true, ...opts });

// Helper: paragraph with default spacing
const p = (children, opts = {}) => new Paragraph({
  spacing: { after: 200, line: 360 }, // 1.5 line spacing (360 = 1.5 * 240)
  alignment: AlignmentType.JUSTIFIED,
  ...opts,
  children: Array.isArray(children) ? children : [children],
});

// Helper: footnote reference
const fn = (id) => new FootnoteReferenceRun(id);

// Table border style
const border = { style: BorderStyle.SINGLE, size: 1, color: "999999" };
const borders = { top: border, bottom: border, left: border, right: border };
const noBorderTop = { top: { style: BorderStyle.NONE }, bottom: border, left: border, right: border };

// Table cell helper
const cell = (text, opts = {}) => {
  const { width: w, ...rest } = opts;
  return new TableCell({
    borders,
    width: w ? { size: w, type: WidthType.DXA } : undefined,
    margins: { top: 40, bottom: 40, left: 80, right: 80 },
    children: [new Paragraph({
      spacing: { after: 0, line: 240 },
      children: Array.isArray(text) ? text : [t(text, { size: 20, font: "Times New Roman" })],
    })],
  });
};

const headerCell = (text, width) => new TableCell({
  borders,
  width: width ? { size: width, type: WidthType.DXA } : undefined,
  margins: { top: 40, bottom: 40, left: 80, right: 80 },
  shading: { fill: "F0F0F0", type: ShadingType.CLEAR },
  children: [new Paragraph({
    spacing: { after: 0, line: 240 },
    children: [tb(text, { size: 20, font: "Times New Roman" })],
  })],
});

// Build footnotes object
const footnotes = {
  1: { children: [new Paragraph({ spacing: { after: 60 }, children: [
    t("O rozproszeniu archiw\u00F3w emigracji polskiej zob. R. Habielski, ", { size: 18, font: "Times New Roman" }),
    ti("\u017Bycie spo\u0142eczne i kulturalne emigracji", { size: 18, font: "Times New Roman" }),
    t(", Warszawa 1999; M. Kry\u0144ska-\u0141owi\u0144ska, \u201EInstytut Pi\u0142sudskiego w Londynie: geneza i dzia\u0142alno\u015B\u0107,\u201D ", { size: 18, font: "Times New Roman" }),
    ti("Teki Archiwalne,", { size: 18, font: "Times New Roman" }),
    t(" seria nowa, t. 11, 2012. Instytut Pi\u0142sudskiego w Londynie przechowuje ponad 200 zespo\u0142\u00F3w; Instytut Sikorskiego \u2014 ponad 400.", { size: 18, font: "Times New Roman" }),
  ]})] },
  2: { children: [new Paragraph({ spacing: { after: 60 }, children: [
    t("Instytut J\u00F3zefa Pi\u0142sudskiego w Londynie, za\u0142. 15.III.1947, zarejestrowany w bazie SEZAM/IZA NDAP pod nr 709. G\u0142uchowski figuruje w\u015Br\u00F3d wsp\u00F3\u0142za\u0142o\u017Cycieli. Zesp\u00F3\u0142 70 wydzielony jako odr\u0119bna jednostka archiwalna.", { size: 18, font: "Times New Roman" }),
  ]})] },
  3: { children: [new Paragraph({ spacing: { after: 60 }, children: [
    t("ARG/II/1, Biogram WBH nr 76/45, 24.V.1937. Potwierdza: OB PPS od 1905 (w wieku 17 lat), ZWC w Li\u00E8ge (wsp\u00F3\u0142za\u0142o\u017Cyciel z T.\u00A0Piskorem, p\u00F3\u017Aniejszym gen. dyw. i szefem Sztabu G\u0142\u00F3wnego WP), Zwi\u0105zek Strzelecki. Dokument sporz\u0105dzony za \u017Cycia bohatera i zweryfikowany przez instytucj\u0119 wojskow\u0105.", { size: 18, font: "Times New Roman" }),
  ]})] },
  4: { children: [new Paragraph({ spacing: { after: 60 }, children: [
    t("Identyfikacja uczestnik\u00F3w patrolu na podstawie: IPN, baza biogramowa (ipn.gov.pl); jpilsudski.org (Instytut Pi\u0142sudskiego w Ameryce); fotokopia grupowa z podpisami ARG/II/2. Data patrolu: noc 2/3.VIII.1914. Zob. J.\u00A0Litewski, ", { size: 18, font: "Times New Roman" }),
    ti("Si\u00F3demka Beliny", { size: 18, font: "Times New Roman" }),
    t(", Krak\u00F3w 1999.", { size: 18, font: "Times New Roman" }),
  ]})] },
  5: { children: [new Paragraph({ spacing: { after: 60 }, children: [
    t("ARG/II/15: zaproszenie datowane IV.1923, ceremonia 3.V.1923, Plac Saski (dzi\u015B Plac Pi\u0142sudskiego), Warszawa. ARG/II/16: dyplom Ordinul Steaua Rom\u00E2niei w stopniu Comandor, podpisany przez kr\u00F3la Ferdynanda I i ministra I.G.\u00A0Duc\u0103, Sinaia, 1.VIII.1923. ARG/II/17: pismo MSWojsk L.75/25 G.M.I. z 29.XI.1925; w II RP oficerowie potrzebowali dekretu prezydenckiego z kontrasygnatur\u0105 ministerialn\u0105 do noszenia zagranicznych odznacze\u0144.", { size: 18, font: "Times New Roman" }),
  ]})] },
  6: { children: [new Paragraph({ spacing: { after: 60 }, children: [
    t("Encyklopedia PWN, has\u0142o \u201EG\u0142uchowski Janusz\u201D (encyklopedia.pwn.pl/haslo/3906169). IPN, biogram \u201EJanusz G\u0142uchowski\u201D (ipn.gov.pl/pl/100-bohaterow-na-100-le/104516). Cmentarz Brompton, Londyn, gr\u00F3b nr 576.", { size: 18, font: "Times New Roman" }),
  ]})] },
  7: { children: [new Paragraph({ spacing: { after: 60 }, children: [
    t("Opis Zespo\u0142u 70: Instytut Pi\u0142sudskiego w Londynie, pilsudski.org.uk/pl/archiwum-070.php (dost\u0119p: III.2026). Inwentarz ma charakter ramowy; pe\u0142ny opis na poziomie dokumentu dost\u0119pny w czytelni Instytutu.", { size: 18, font: "Times New Roman" }),
  ]})] },
  8: { children: [new Paragraph({ spacing: { after: 60 }, children: [
    t("Obecno\u015B\u0107 wierszy w Zespole 70 (jedn. 6, wsp\u00F3lnie z raportami i zapisami rozm\u00F3w, 1940\u20131945) jest zaskakuj\u0105ca i mo\u017Ce wskazywa\u0107 na aktywno\u015B\u0107 literack\u0105 genera\u0142a w okresie wojennym. Kalendarze i notatnik (jedn. 1) mog\u0105 pe\u0142ni\u0107 funkcj\u0119 dziennika \u2014 wymagaj\u0105 weryfikacji in situ.", { size: 18, font: "Times New Roman" }),
  ]})] },
  9: { children: [new Paragraph({ spacing: { after: 60 }, children: [
    t("Odsetek 60% ma charakter szacunkowy, oparty na por\u00F3wnaniu inwentarza ramowego Zesp. 70 z pe\u0142nym katalogiem ARG. Pe\u0142na taksonomia wymaga dost\u0119pu do orygina\u0142\u00F3w obu zbior\u00F3w i por\u00F3wnania na poziomie dokumentu jednostkowego. Szczeg\u00F3lne trudno\u015Bci sprawia jednostka 3 Zesp. 70 (\u201Ekorespondencja s\u0142u\u017Cbowa i prywatna, 1940\u20131961\u201D), kt\u00F3rej zakres mo\u017Ce cz\u0119\u015Bciowo pokrywa\u0107 si\u0119 z ARG/II/24\u201326.", { size: 18, font: "Times New Roman" }),
  ]})] },
  10: { children: [new Paragraph({ spacing: { after: 60 }, children: [
    t("ARG/II/27, list gen. broni Kazimierza Sosnkowskiego (1885\u20131969) do gen. dyw. Janusza G\u0142uchowskiego, dat. 28.V.1964, Arundel, P.\u00A0Qu\u00E9bec, Kanada. Inskrypcja: \u201EKochany Generale.\u201D Do listu do\u0142\u0105czono \u201EPro Memoria\u201D (ARG/II/28 \u2014 strona 1, ARG/II/29 \u2014 strona 2) z 24 pozycjami spraw. G\u0142uchowski zmar\u0142 14 dni p\u00F3\u017Aniej (11.VI.1964). Sosnkowski pisa\u0142 z farmy w Arundel, prowincja Quebec, dok\u0105d wyemigrowa\u0142 w XI.1944. Zmar\u0142 11.X.1969.", { size: 18, font: "Times New Roman" }),
  ]})] },
  11: { children: [new Paragraph({ spacing: { after: 60 }, children: [
    t("Zesp\u00F3\u0142 19 (Archiwum Sosnkowskiego), 33 jednostki. Jedn. 14: \u201EKorespondencja \u015Bci\u015Ble tajna z dow\u00F3dcami (1944, 1948\u201352)\u201D; jedn. 15: \u201EKopie list\u00F3w prywatnych (1939\u201344, 1970)\u201D; jedn. 18: \u201EKorespondencja wydawnicza, pisma wybrane Sosnkowskiego (1956, 1964\u201365).\u201D Rok 1964 w jedn. 17 i 18 pokrywa si\u0119 z dat\u0105 listu ARG/II/27. Opis zespo\u0142u: pilsudski.org.uk/pl/archiwum-019.php.", { size: 18, font: "Times New Roman" }),
  ]})] },
  12: { children: [new Paragraph({ spacing: { after: 60 }, children: [
    t("Zesp\u00F3\u0142 17 (Archiwum L.\u00A0Kmicic-Skrzy\u0144skiego). Nota biograficzna wg opisu zespo\u0142u (pilsudski.org.uk/pl/archiwum-017.php): ur. 1893 Odessa, studia chemii w Nancy, pluton Zwi\u0105zku Strzeleckiego, Legiony, kampania wrze\u015Bniowa, Oflag IID Gross-Born, 2 Korpus Polski, osiedlenie w Manchesterze. Zmar\u0142 14.II.1972. Jedn. 2: wspomnienia S.\u00A0Stablewskiego o A.\u00A0Jab\u0142o\u0144skim, referat o Bitwie Warszawskiej 1920 (1964\u201365). Jedn. 3: relacje o pu\u0142ku u\u0142an\u00F3w Legion\u00F3w, pami\u0119tnik Leona Kmicic-Skrzy\u0144skiego (1916\u20131918). Jedn. 7: wspomnienia nagrywane dla RWE (1964), wspomnienia z lat 1916\u20131918.", { size: 18, font: "Times New Roman" }),
  ]})] },
  13: { children: [new Paragraph({ spacing: { after: 60 }, children: [
    t("Instytut Pi\u0142sudskiego w Londynie, pe\u0142ny katalog zbior\u00F3w: pilsudski.org.uk/pl/katalog.php. Rejestracja NDAP pod nr 709: baza SEZAM (szukajwarchiwach.gov.pl). Stan na III.2026: ponad 200 zespo\u0142\u00F3w archiwalnych, w tym archiwa: J.\u00A0Pi\u0142sudskiego (zesp. 1), A.\u00A0Pi\u0142sudskiej (zesp. 2), K.\u00A0Sosnkowskiego (zesp. 19), S.\u00A0Mayera (zesp. 100), G.\u00A0Langera (zesp. 133, materia\u0142y kryptologiczne), W.\u00A0S\u0142awka (zesp. 92).", { size: 18, font: "Times New Roman" }),
  ]})] },
};

// ============= DOCUMENT CONTENT =============

const content = [];

// TITLE
content.push(new Paragraph({
  spacing: { after: 120 },
  alignment: AlignmentType.CENTER,
  children: [t("Teki Archiwalne \u00B7 Artyku\u0142 archiwoznawczy", { size: 18, font: "Times New Roman", color: "666666", allCaps: true, characterSpacing: 80 })],
}));

content.push(new Paragraph({
  spacing: { after: 200 },
  alignment: AlignmentType.CENTER,
  children: [tb("Od Si\u00F3demki Beliny do Instytutu Pi\u0142sudskiego: genera\u0142 Janusz G\u0142uchowski i dwa archiwa jednego \u017Cycia", { size: 32, font: "Times New Roman" })],
}));

content.push(new Paragraph({
  spacing: { after: 200 },
  alignment: AlignmentType.CENTER,
  children: [ti("Studium komplementarno\u015Bci kolekcji prywatnej ARG (217 jednostek) i Zespo\u0142u 70 Instytutu J\u00F3zefa Pi\u0142sudskiego w Londynie na tle pi\u0119ciu powi\u0105zanych zespo\u0142\u00F3w archiwalnych", { size: 24, font: "Times New Roman", color: "444444" })],
}));

content.push(new Paragraph({
  spacing: { after: 120 },
  alignment: AlignmentType.CENTER,
  children: [t("Opracowanie archiwalne, 2026", { size: 22, font: "Times New Roman", color: "666666" })],
}));

content.push(new Paragraph({
  spacing: { after: 400 },
  alignment: AlignmentType.CENTER,
  children: [t("Otrzymano: marzec 2026 \u00B7 \u0179r\u00F3d\u0142a: Kolekcja prywatna ARG (217 jedn.), Instytut Pi\u0142sudskiego w Londynie (Zesp. 17, 19, 22, 23, 70), WBH (biogram 76/45), AHM MPW (sygn. 1889)", { size: 18, font: "Times New Roman", color: "888888" })],
}));

// ---- ABSTRAKT PL ----
content.push(p([
  tb("Abstrakt: ", { size: 22, font: "Times New Roman" }),
  ti("Artyku\u0142 przedstawia por\u00F3wnawcz\u0105 analiz\u0119 zasob\u00F3w archiwalnych dokumentuj\u0105cych \u017Cycie genera\u0142a dywizji Janusza Juliana G\u0142uchowskiego (1888\u20131964). Przedmiotem analizy s\u0105 dwa zbiory: kolekcja prywatna ARG (217 jednostek w sze\u015Bciu seriach, skatalogowana w standardzie ISAD(G)) oraz Zesp\u00F3\u0142 70 Instytutu J\u00F3zefa Pi\u0142sudskiego w Londynie (9 jednostek, 1916\u20131964). Na podstawie por\u00F3wnania inwentarzy metod\u0105 pozycja-po-pozycji zidentyfikowano dokumenty kategorii A (duplikaty), B (uzupe\u0142nienia) i C (unikaty). Oko\u0142o 60% dokument\u00F3w serii ARG/II (33 jednostki dotycz\u0105ce genera\u0142a) stanowi materia\u0142 nieobecny w Zespole 70. W szerszym kontek\u015Bcie archiwalnym wykazano powi\u0105zania z pi\u0119cioma kolejnymi zespo\u0142ami Instytutu: Archiwum L.\u00A0Kmicic-Skrzy\u0144skiego (zesp. 17), Archiwum K.\u00A0Sosnkowskiego (zesp. 19), Legiony 1914\u20131918 (zesp. 22), Wojna polsko-bolszewicka (zesp. 23) oraz Zbi\u00F3r fotograficzny (zesp. 201). Artyku\u0142 dowodzi, \u017Ce dopiero po\u0142\u0105czenie obu zbior\u00F3w \u2014 instytucjonalnego i prywatnego \u2014 pozwala zrekonstruowa\u0107 pe\u0142n\u0105 biografi\u0119 archiwalnl\u0105 jednego z za\u0142o\u017Cycieli Si\u00F3demki Beliny, tw\u00F3rcy 7\u00A0Pu\u0142ku U\u0142an\u00F3w Lubelskich, I\u00A0Zast\u0119pcy Ministra Spraw Wojskowych i wsp\u00F3\u0142za\u0142o\u017Cyciela samego Instytutu.", { size: 22, font: "Times New Roman" }),
], { indent: { left: 400, right: 400 } }));

// ---- ABSTRACT EN ----
content.push(p([
  tb("Abstract: ", { size: 22, font: "Times New Roman", color: "666666" }),
  ti("This article presents a comparative analysis of archival resources documenting the life of Major General Janusz Julian G\u0142uchowski (1888\u20131964). Two collections are examined: the private ARG collection (217 items in six series, catalogued according to ISAD(G)) and Collection\u00A070 of the J\u00F3zef Pi\u0142sudski Institute in London (9 items, 1916\u20131964). Through item-by-item inventory comparison, documents were classified as Category\u00A0A (duplicates), B (supplements), or C (uniques). Approximately 60% of ARG Series\u00A0II documents (33 items relating to the General) constitute material absent from Collection\u00A070. The broader archival context reveals connections to five additional Institute collections: the L.\u00A0Kmicic-Skrzy\u0144ski Archive (coll.\u00A017), K.\u00A0Sosnkowski Archive (coll.\u00A019), Polish Legions 1914\u20131918 (coll.\u00A022), Polish-Soviet War (coll.\u00A023), and the Photographic Collection (coll.\u00A0201). The article demonstrates that only by combining both holdings \u2014 institutional and private \u2014 can the full archival biography of one of Belina\u2019s Seven, founder of the 7th\u00A0Uhlan Regiment, First Deputy Minister of Military Affairs, and co-founder of the Institute itself, be reconstructed.", { size: 22, font: "Times New Roman", color: "666666" }),
], { indent: { left: 400, right: 400 } }));

// ---- KEYWORDS ----
content.push(p([
  tb("S\u0142owa kluczowe / Keywords: ", { size: 20, font: "Times New Roman" }),
  t("archiwoznawstwo, komplementarno\u015B\u0107 archiwalna, kolekcja prywatna, Instytut Pi\u0142sudskiego w Londynie, Si\u00F3demka Beliny, gen. Janusz G\u0142uchowski, Polskie Si\u0142y Zbrojne, emigracja wojskowa, ISAD(G) \u00B7 archival science, archival complementarity, private collection, Pi\u0142sudski Institute London, Belina\u2019s Seven, Polish Armed Forces, military emigration", { size: 20, font: "Times New Roman" }),
], { spacing: { after: 400 } }));


// ============= SECTION 1 =============
content.push(new Paragraph({
  heading: HeadingLevel.HEADING_1,
  spacing: { before: 400, after: 200 },
  children: [tb("1. Wprowadzenie: problem rozproszenia \u017Ar\u00F3de\u0142", { size: 26, font: "Times New Roman" })],
}));

content.push(p([
  t("Archiwa polskiej emigracji wojskowej po 1945 roku cechuje charakterystyczny podzia\u0142: cz\u0119\u015B\u0107 dokumentacji trafia\u0142a do instytucji powo\u0142anych dla ochrony pami\u0119ci \u2014 Instytutu Pi\u0142sudskiego, Instytutu Sikorskiego, Biblioteki Polskiej w Pary\u017Cu \u2014 podczas gdy dokumenty o charakterze prywatnym pozostawa\u0142y w r\u0119kach rodzin. Podzia\u0142 ten wynika\u0142 z praktyki archiwalnej: oficerowie przekazywali akta s\u0142u\u017Cby, rozkazy i korespondencj\u0119 urz\u0119dow\u0105, zatrzymuj\u0105c listy osobiste, fotografie i pami\u0105tki rodzinne.", { size: 22, font: "Times New Roman" }),
  fn(1),
]));

content.push(p([
  t("Genera\u0142 dywizji Janusz Julian G\u0142uchowski (1888\u20131964) stanowi modelowy przypadek takiego rozproszenia. Jego dokumentacja archiwalna istnieje w dw\u00F3ch odr\u0119bnych zbiorach: Zespole 70 Instytutu J\u00F3zefa Pi\u0142sudskiego w Londynie (9 jednostek archiwalnych, lata 1916\u20131964) oraz kolekcji prywatnej oznaczonej sygnatur\u0105 ARG (217 jednostek w sze\u015Bciu seriach, skatalogowanej w standardzie ISAD(G) w 2026 roku). Dodatkow\u0105 warto\u015B\u0107 analityczn\u0105 wnosi fakt, \u017Ce G\u0142uchowski by\u0142 wsp\u00F3\u0142za\u0142o\u017Cycielem instytucji, w kt\u00F3rej jego w\u0142asne akta s\u0105 dzi\u015B przechowywane.", { size: 22, font: "Times New Roman" }),
  fn(2),
]));

content.push(p([
  t("Celem niniejszego artyku\u0142u jest: (1) por\u00F3wnanie zawarto\u015Bci obu zbior\u00F3w metod\u0105 inwentarza r\u00F3wnoleg\u0142ego; (2) identyfikacja dokument\u00F3w komplementarnych, uzupe\u0142niaj\u0105cych i unikalnych; (3) umieszczenie obu zbior\u00F3w w szerszym kontek\u015Bcie archiwalnym Instytutu Pi\u0142sudskiego, z uwzgl\u0119dnieniem pi\u0119ciu powi\u0105zanych zespo\u0142\u00F3w (nr 17, 19, 22, 23, 201).", { size: 22, font: "Times New Roman" }),
]));


// ============= SECTION 2 =============
content.push(new Paragraph({
  heading: HeadingLevel.HEADING_1,
  spacing: { before: 400, after: 200 },
  children: [tb("2. Nota biograficzna: od bojowca PPS do wsp\u00F3\u0142za\u0142o\u017Cyciela Instytutu", { size: 26, font: "Times New Roman" })],
}));

content.push(p([
  t("Janusz Julian G\u0142uchowski urodzi\u0142 si\u0119 19 czerwca 1888 roku w Bukowej, powiat Piotrk\u00F3w Trybunalski. By\u0142 synem Mariana G\u0142uchowskiego, dzia\u0142acza Polskiej Organizacji Narodowej, kt\u00F3rego dokumenty zachowa\u0142y si\u0119 w serii ARG/I (6 jednostek, 1914). W 1905 roku, w wieku siedemnastu lat, wst\u0105pi\u0142 do Organizacji Bojowej PPS. Dzia\u0142a\u0142 w niej do 1908 roku, po czym wyjecha\u0142 na studia na Politechnik\u0119 w Li\u00E8ge, gdzie wsp\u00F3\u0142za\u0142o\u017Cy\u0142 z Tadeuszem Piskorem kom\u00F3rk\u0119 Zwi\u0105zku Walki Czynnej. Sekwencj\u0119 t\u0119 potwierdza biogram sporz\u0105dzony przez Wojskowe Biuro Historyczne (nr 76/45, 24.V.1937), zachowany jako ARG/II/1.", { size: 22, font: "Times New Roman" }),
  fn(3),
]));

content.push(p([
  t("W nocy z 2 na 3 sierpnia 1914 roku G\u0142uchowski, jako zast\u0119pca dow\u00F3dcy W\u0142adys\u0142awa Beliny-Pra\u017Cmowskiego, uczestniczy\u0142 w patrolu Si\u00F3demki Beliny \u2014 pierwszym regularnym oddziale polskim od Powstania Styczniowego. Sk\u0142ad patrolu, zweryfikowany na podstawie \u017Ar\u00F3de\u0142 IPN i fotokopii grupowej z podpisami (ARG/II/2), przedstawia tabela 1.", { size: 22, font: "Times New Roman" }),
  fn(4),
]));

// TABLE 1: Siódemka Beliny
content.push(p([ti("Tabela 1. Sk\u0142ad patrolu Si\u00F3demki Beliny (2/3.VIII.1914)", { size: 20, font: "Times New Roman" })], { spacing: { after: 60 } }));

const tw1 = 9360; // full width
const t1cols = [2400, 1400, 2400, 3160];
content.push(new Table({
  width: { size: tw1, type: WidthType.DXA },
  columnWidths: t1cols,
  rows: [
    new TableRow({ children: [
      headerCell("Uczestnik", t1cols[0]),
      headerCell("Lata \u017Cycia", t1cols[1]),
      headerCell("Rola / los", t1cols[2]),
      headerCell("\u0179r\u00F3d\u0142a archiwalne w Instytucie", t1cols[3]),
    ]}),
    new TableRow({ children: [
      cell("W\u0142adys\u0142aw Belina-Pra\u017Cmowski", { width: t1cols[0] }),
      cell("1888\u20131938", { width: t1cols[1] }),
      cell("dow\u00F3dca patrolu", { width: t1cols[2] }),
      cell("brak odr\u0119bnego zespo\u0142u", { width: t1cols[3] }),
    ]}),
    new TableRow({ children: [
      cell("Janusz G\u0142uchowski", { width: t1cols[0] }),
      cell("1888\u20131964", { width: t1cols[1] }),
      cell("zast\u0119pca dow\u00F3dcy", { width: t1cols[2] }),
      cell([tb("Zesp. 70", { size: 20, font: "Times New Roman" }), t(" + kolekcja ARG", { size: 20, font: "Times New Roman" })], { width: t1cols[3] }),
    ]}),
    new TableRow({ children: [
      cell("Stanis\u0142aw Grzmot-Skotnicki", { width: t1cols[0] }),
      cell("ok. 1890\u20131939", { width: t1cols[1] }),
      cell("poleg\u0142 IX.1939, Tu\u0142owice", { width: t1cols[2] }),
      cell("\u2014", { width: t1cols[3] }),
    ]}),
    new TableRow({ children: [
      cell("Ludwik Bo\u0144cza-Karwacki", { width: t1cols[0] }),
      cell("ok. 1889\u20131916", { width: t1cols[1] }),
      cell("poleg\u0142 pod Kostiuchn\u00F3wk\u0105", { width: t1cols[2] }),
      cell("Zesp. 22, jedn. 47 (wspomnienia)", { width: t1cols[3] }),
    ]}),
    new TableRow({ children: [
      cell("Zdzis\u0142aw Jab\u0142o\u0144ski ps. \u201EZdzis\u0142aw\u201D", { width: t1cols[0] }),
      cell("ok. 1896\u20131920", { width: t1cols[1] }),
      cell("poleg\u0142 w wojnie 1920", { width: t1cols[2] }),
      cell("Zesp. 17 (wspomn. S. Stablewskiego)", { width: t1cols[3] }),
    ]}),
    new TableRow({ children: [
      cell("Janusz Hanka-Kulesza", { width: t1cols[0] }),
      cell("1892\u20131964", { width: t1cols[1] }),
      cell("zmar\u0142 5.VI.1964, Londyn", { width: t1cols[2] }),
      cell("\u2014", { width: t1cols[3] }),
    ]}),
    new TableRow({ children: [
      cell("Ludwik Kmicic-Skrzy\u0144ski", { width: t1cols[0] }),
      cell("1893\u20131972", { width: t1cols[1] }),
      cell("ostatni \u017Cyj\u0105cy; Manchester", { width: t1cols[2] }),
      cell([tb("Zesp. 17", { size: 20, font: "Times New Roman" })], { width: t1cols[3] }),
    ]}),
  ],
}));

content.push(p([])); // spacer

content.push(p([
  t("Dalsze etapy kariery G\u0142uchowskiego dokumentowane s\u0105 przede wszystkim w serii ARG/II (33 jednostki). 5 listopada 1918 roku otrzyma\u0142 rozkaz Sztabu Generalnego w Lublinie organizacji nowego oddzia\u0142u jazdy (ARG/II/8) \u2014 przysz\u0142ego 7 Pu\u0142ku U\u0142an\u00F3w Lubelskich, kt\u00F3rym dowodzi\u0142 do lipca 1920 roku. W okresie mi\u0119dzywojennym by\u0142 dekorowany Legi\u0105 Honorow\u0105 przez marsza\u0142ka Focha (3.V.1923, ARG/II/15), Orderem Gwiazdy Rumunii w stopniu komandora (1.VIII.1923, ARG/II/16), a w 1925 roku otrzyma\u0142 dekret prezydencki zezwalaj\u0105cy na noszenie odznacze\u0144 zagranicznych (ARG/II/17).", { size: 22, font: "Times New Roman" }),
  fn(5),
]));

content.push(p([
  t("5 pa\u017Adziernika 1935 roku zosta\u0142 mianowany I Zast\u0119pc\u0105 Ministra Spraw Wojskowych (ARG/II/19). Po kampanii wrze\u015Bniowej \u2014 internowanie w Rumunii, Palestyna (X.1940), Londyn (II.1941). Od wrze\u015Bnia 1943 dow\u00F3dca Polskich Jednostek Wojskowych w Wielkiej Brytanii. 1 czerwca 1945 \u2014 awans na genera\u0142a dywizji. We wrze\u015Bniu 1945 \u2014 Companion of the Order of the Bath (C.B.).", { size: 22, font: "Times New Roman" }),
]));

content.push(p([
  t("15 marca 1947 roku G\u0142uchowski wsp\u00F3\u0142za\u0142o\u017Cy\u0142 Instytut J\u00F3zefa Pi\u0142sudskiego w Londynie \u2014 instytucj\u0119, kt\u00F3rej przekaza\u0142 swoje akta urz\u0119dowe (obecny Zesp\u00F3\u0142 70). Zmar\u0142 11 czerwca 1964 roku w Londynie. Pochowany na cmentarzu Brompton (gr\u00F3b 576).", { size: 22, font: "Times New Roman" }),
  fn(6),
]));


// ============= SECTION 3 =============
content.push(new Paragraph({
  heading: HeadingLevel.HEADING_1,
  spacing: { before: 400, after: 200 },
  children: [tb("3. Zesp\u00F3\u0142 70: inwentarz i charakterystyka", { size: 26, font: "Times New Roman" })],
}));

content.push(p([
  t("Zesp\u00F3\u0142 70 Instytutu Pi\u0142sudskiego w Londynie nosi nazw\u0119 \u201EArchiwum Janusza G\u0142uchowskiego\u201D i obejmuje 9 jednostek archiwalnych z lat 1916\u20131964. Opis zespo\u0142u, dost\u0119pny na stronie Instytutu (pilsudski.org.uk/pl/archiwum-070.php), pozwala zrekonstruowa\u0107 nast\u0119puj\u0105c\u0105 struktur\u0119:", { size: 22, font: "Times New Roman" }),
  fn(7),
]));

// TABLE 2: Inwentarz Zespołu 70
content.push(p([ti("Tabela 2. Inwentarz Zespo\u0142u 70 \u2014 Archiwum Janusza G\u0142uchowskiego", { size: 20, font: "Times New Roman" })], { spacing: { after: 60 } }));

const t2cols = [600, 4760, 1200, 2800];
content.push(new Table({
  width: { size: tw1, type: WidthType.DXA },
  columnWidths: t2cols,
  rows: [
    new TableRow({ children: [
      headerCell("Nr", t2cols[0]),
      headerCell("Opis jednostki", t2cols[1]),
      headerCell("Daty", t2cols[2]),
      headerCell("Charakter", t2cols[3]),
    ]}),
    new TableRow({ children: [
      cell("1", { width: t2cols[0] }),
      cell("\u017Byciorys, rozkazy, nominacje, dokumenty osobiste (kalendarze, notatnik, listy), broszury, wycinki z gazet", { width: t2cols[1] }),
      cell("1916\u20131964", { width: t2cols[2] }),
      cell("osobisty / s\u0142u\u017Cbowy", { width: t2cols[3] }),
    ]}),
    new TableRow({ children: [
      cell("2", { width: t2cols[0] }),
      cell("Korespondencja z Ko\u0142em Genera\u0142\u00F3w, Pu\u0142kownik\u00F3w i by\u0142ych wy\u017Cszych dow\u00F3dc\u00F3w; wykaz adres\u00F3w", { width: t2cols[1] }),
      cell("1948\u20131963", { width: t2cols[2] }),
      cell("korporacyjny", { width: t2cols[3] }),
    ]}),
    new TableRow({ children: [
      cell("3", { width: t2cols[0] }),
      cell("Korespondencja s\u0142u\u017Cbowa i prywatna", { width: t2cols[1] }),
      cell("1940\u20131961", { width: t2cols[2] }),
      cell("mieszany", { width: t2cols[3] }),
    ]}),
    new TableRow({ children: [
      cell("4", { width: t2cols[0] }),
      cell("Wspomnienia, przem\u00F3wienia", { width: t2cols[1] }),
      cell("b.d.", { width: t2cols[2] }),
      cell("narracyjny", { width: t2cols[3] }),
    ]}),
    new TableRow({ children: [
      cell("5", { width: t2cols[0] }),
      cell("Korespondencja", { width: t2cols[1] }),
      cell("1943\u20131963", { width: t2cols[2] }),
      cell("mieszany", { width: t2cols[3] }),
    ]}),
    new TableRow({ children: [
      cell("6", { width: t2cols[0] }),
      cell("Raporty, sprawozdania ze Sztabu G\u0142\u00F3wnego, zapisy rozm\u00F3w, wiersze", { width: t2cols[1] }),
      cell("1940\u20131945", { width: t2cols[2] }),
      cell("s\u0142u\u017Cbowy / literacki", { width: t2cols[3] }),
    ]}),
    new TableRow({ children: [
      cell("7", { width: t2cols[0] }),
      cell("Korespondencja z pras\u0105, wycinki prasowe", { width: t2cols[1] }),
      cell("b.d.", { width: t2cols[2] }),
      cell("prasowy", { width: t2cols[3] }),
    ]}),
    new TableRow({ children: [
      cell("8", { width: t2cols[0] }),
      cell("Brudnopisy", { width: t2cols[1] }),
      cell("b.d.", { width: t2cols[2] }),
      cell("roboczy", { width: t2cols[3] }),
    ]}),
    new TableRow({ children: [
      cell("9", { width: t2cols[0] }),
      cell("Emigracja \u2014 druki ulotne, komunikaty, rozkazy, or\u0119dzia, odezwy", { width: t2cols[1] }),
      cell("1946\u20131961", { width: t2cols[2] }),
      cell("emigracyjny", { width: t2cols[3] }),
    ]}),
  ],
}));

content.push(p([])); // spacer

content.push(p([
  t("Analiza inwentarza ujawnia kilka cech istotnych dla dalszego por\u00F3wnania. Po pierwsze, Zesp\u00F3\u0142 70 ma charakter przede wszystkim ", { size: 22, font: "Times New Roman" }),
  tb("s\u0142u\u017Cbowy i korporacyjny", { size: 22, font: "Times New Roman" }),
  t(": dominuje korespondencja urz\u0119dowa (jedn. 2, 3, 5), raporty wojskowe (jedn. 6) i materia\u0142y emigracyjne (jedn. 9). Po drugie, zbi\u00F3r obejmuje wy\u0142\u0105cznie dokumenty samego genera\u0142a \u2014 brak jakiejkolwiek dokumentacji rodzinnej. Po trzecie, zas\u0142uguj\u0105 na uwag\u0119 dwa elementy niespodziewane: ", { size: 22, font: "Times New Roman" }),
  tb("wiersze", { size: 22, font: "Times New Roman" }),
  t(" (jedn. 6) oraz ", { size: 22, font: "Times New Roman" }),
  tb("kalendarze i notatnik", { size: 22, font: "Times New Roman" }),
  t(" (jedn. 1), kt\u00F3re mog\u0105 mie\u0107 walor \u017Ar\u00F3d\u0142a narracyjnego.", { size: 22, font: "Times New Roman" }),
  fn(8),
]));


// ============= SECTION 4 =============
content.push(new Paragraph({
  heading: HeadingLevel.HEADING_1,
  spacing: { before: 400, after: 200 },
  children: [tb("4. Kolekcja prywatna ARG: struktura i zakres", { size: 26, font: "Times New Roman" })],
}));

content.push(p([
  t("Kolekcja prywatna ARG (Archiwum Rodziny G\u0142uchowskich) zosta\u0142a skatalogowana w 2026 roku w standardzie ISAD(G). Obejmuje 217 jednostek w sze\u015Bciu seriach, z kt\u00F3rych ka\u017Cda odpowiada jednemu cz\u0142onkowi rodziny lub kategorii dokument\u00F3w:", { size: 22, font: "Times New Roman" }),
]));

// TABLE 3: Struktura kolekcji ARG
content.push(p([ti("Tabela 3. Struktura kolekcji ARG", { size: 20, font: "Times New Roman" })], { spacing: { after: 60 } }));

const t3cols = [1000, 2560, 700, 1400, 3700];
content.push(new Table({
  width: { size: tw1, type: WidthType.DXA },
  columnWidths: t3cols,
  rows: [
    new TableRow({ children: [
      headerCell("Seria", t3cols[0]),
      headerCell("Osoba", t3cols[1]),
      headerCell("Jedn.", t3cols[2]),
      headerCell("Daty skrajne", t3cols[3]),
      headerCell("Charakter", t3cols[4]),
    ]}),
    new TableRow({ children: [
      cell("ARG/I", { width: t3cols[0] }),
      cell("Marian G\u0142uchowski (ojciec)", { width: t3cols[1] }),
      cell("6", { width: t3cols[2] }),
      cell("1914", { width: t3cols[3] }),
      cell("PON, dzia\u0142alno\u015B\u0107 niepodleg\u0142o\u015Bciowa", { width: t3cols[4] }),
    ]}),
    new TableRow({ children: [
      cell("ARG/II", { width: t3cols[0] }),
      cell("Gen. dyw. Janusz G\u0142uchowski", { width: t3cols[1] }),
      cell("33", { width: t3cols[2] }),
      cell("1905\u20131964", { width: t3cols[3] }),
      cell("s\u0142u\u017Cba wojskowa, ordery, korespondencja prywatna, fotografie", { width: t3cols[4] }),
    ]}),
    new TableRow({ children: [
      cell("ARG/III", { width: t3cols[0] }),
      cell("Ppor. Stanis\u0142aw Stefan G\u0142uchowski (brat)", { width: t3cols[1] }),
      cell("38", { width: t3cols[2] }),
      cell("1944\u20131945", { width: t3cols[3] }),
      cell("AK, Powstanie Warszawskie, Stalag XI-B", { width: t3cols[4] }),
    ]}),
    new TableRow({ children: [
      cell("ARG/IV", { width: t3cols[0] }),
      cell("Lech G\u0142uchowski \u201EJe\u017Cycki\u201D (brat)", { width: t3cols[1] }),
      cell("wzm.", { width: t3cols[2] }),
      cell("1900\u20131944", { width: t3cols[3] }),
      cell("poleg\u0142 w Powstaniu 15.IX.1944", { width: t3cols[4] }),
    ]}),
    new TableRow({ children: [
      cell("ARG/V", { width: t3cols[0] }),
      cell("Krzysztof G\u0142uchowski \u201EJura\u015B\u201D (bratanek)", { width: t3cols[1] }),
      cell("150+", { width: t3cols[2] }),
      cell("1926\u20132020", { width: t3cols[3] }),
      cell("Powstanie, jeniec, emigracja, Brazylia", { width: t3cols[4] }),
    ]}),
    new TableRow({ children: [
      cell("ARG/VI", { width: t3cols[0] }),
      cell("Varia / Rodzina", { width: t3cols[1] }),
      cell("22", { width: t3cols[2] }),
      cell("r\u00F3\u017Cne", { width: t3cols[3] }),
      cell("dokumenty podr\u00F3\u017Cy, pami\u0105tki, korespondencja", { width: t3cols[4] }),
    ]}),
  ],
}));

content.push(p([])); // spacer

content.push(p([
  t("Kluczowa r\u00F3\u017Cnica mi\u0119dzy oboma zbiorami le\u017Cy w ", { size: 22, font: "Times New Roman" }),
  tb("zakresie podmiotowym", { size: 22, font: "Times New Roman" }),
  t(". Zesp\u00F3\u0142 70 dokumentuje wy\u0142\u0105cznie genera\u0142a. Kolekcja ARG dokumentuje ca\u0142\u0105 rodzin\u0119 \u2014 pi\u0119\u0107 os\u00F3b w trzech pokoleniach, z kt\u00F3rych ka\u017Cde walczy\u0142o o niepodleg\u0142o\u015B\u0107 innymi \u015Brodkami: ojciec w PON (1914), genera\u0142 w Legionach i II RP, bracia w AK i Powstaniu Warszawskim, bratanek jako m\u0142odociany powsta\u0144iec, a nast\u0119pnie emigrant w Brazylii. Ten wielopokoleniowy kontekst jest niedost\u0119pny z poziomu Zespo\u0142u 70.", { size: 22, font: "Times New Roman" }),
]));


// ============= SECTION 5 =============
content.push(new Paragraph({
  heading: HeadingLevel.HEADING_1,
  spacing: { before: 400, after: 200 },
  children: [tb("5. Metodologia por\u00F3wnania inwentarzy", { size: 26, font: "Times New Roman" })],
}));

content.push(p([
  t("Analiz\u0119 komplementarno\u015Bci przeprowadzono metod\u0105 ", { size: 22, font: "Times New Roman" }),
  tb("inwentarza r\u00F3wnoleg\u0142ego", { size: 22, font: "Times New Roman" }),
  t(": dla ka\u017Cdego dokumentu serii ARG/II (33 jednostki) weryfikowano, czy odpowiadaj\u0105cy mu dokument istnieje w Zespole 70, i odwrotnie. Zastosowano trzy kategorie klasyfikacyjne:", { size: 22, font: "Times New Roman" }),
]));

content.push(p([
  tb("Kategoria A \u2014 duplikaty. ", { size: 22, font: "Times New Roman" }),
  t("Dokumenty obecne w obu zbiorach (np. odpisy mianowa\u0144, kopie rozkaz\u00F3w). Warto\u015B\u0107 archiwalna: potwierdzaj\u0105ca, uwierzytelniaj\u0105ca. Umo\u017Cliwiaj\u0105 weryfikacj\u0119 autentyczno\u015Bci poszczeg\u00F3lnych egzemplarzy.", { size: 22, font: "Times New Roman" }),
]));

content.push(p([
  tb("Kategoria B \u2014 uzupe\u0142nienia. ", { size: 22, font: "Times New Roman" }),
  t("Dokumenty obecne tylko w jednym zbiorze, dotycz\u0105ce okres\u00F3w lub wydarze\u0144 udokumentowanych w drugim. Warto\u015B\u0107: kontekstualizuj\u0105ca. Przyk\u0142ad: zaproszenie na dekoracj\u0119 przez marsz. Focha (ARG/II/15) uzupe\u0142nia dokumentacj\u0119 orderow\u0105 obecn\u0105 w Zespole 70 (jedn. 1).", { size: 22, font: "Times New Roman" }),
]));

content.push(p([
  tb("Kategoria C \u2014 unikaty. ", { size: 22, font: "Times New Roman" }),
  t("Dokumenty bez odpowiednika w drugim zbiorze, dokumentuj\u0105ce aspekty \u017Cycia nieobj\u0119te archiwum alternatywnym. Warto\u015B\u0107: najwy\u017Csza, \u017Ar\u00F3d\u0142owa. Przyk\u0142ad: korespondencja prywatna gen. Sosnkowskiego (ARG/II/27\u201329).", { size: 22, font: "Times New Roman" }),
]));

// TABLE 4: Wybór dokumentów kategorii B i C
content.push(p([ti("Tabela 4. Wyb\u00F3r dokument\u00F3w kategorii B i C z serii ARG/II", { size: 20, font: "Times New Roman" })], { spacing: { after: 60 } }));

const t4cols = [1200, 3060, 500, 4600];
content.push(new Table({
  width: { size: tw1, type: WidthType.DXA },
  columnWidths: t4cols,
  rows: [
    new TableRow({ children: [
      headerCell("Sygn.", t4cols[0]),
      headerCell("Dokument", t4cols[1]),
      headerCell("Kat.", t4cols[2]),
      headerCell("Relacja do Zesp. 70", t4cols[3]),
    ]}),
    new TableRow({ children: [
      cell("ARG/II/2", { width: t4cols[0] }),
      cell("Fotokopia grupowa Si\u00F3demki Beliny z podpisami uczestnik\u00F3w", { width: t4cols[1] }),
      cell("C", { width: t4cols[2] }),
      cell("Brak ikonografii za\u0142o\u017Cycielskiej w Zesp. 70; jedyny znany egzemplarz z podpisami", { width: t4cols[3] }),
    ]}),
    new TableRow({ children: [
      cell("ARG/II/8", { width: t4cols[0] }),
      cell("Rozkaz Sztabu Generalnego, Lublin, 5.XI.1918 \u2014 za\u0142o\u017Cenie oddzia\u0142u jazdy", { width: t4cols[1] }),
      cell("B", { width: t4cols[2] }),
      cell("Akt za\u0142o\u017Cycielski 7 P.U\u0142.; w Zesp. 70 prawdopodobnie odpisy w jedn. 1", { width: t4cols[3] }),
    ]}),
    new TableRow({ children: [
      cell("ARG/II/14", { width: t4cols[0] }),
      cell("List marsza\u0142ka \u015Amig\u0142ego-Rydza (r\u0119kopis, ~1935\u20131939)", { width: t4cols[1] }),
      cell("C", { width: t4cols[2] }),
      cell("Korespondencja prywatna z Naczelnym Wodzem; brak odpowiednika", { width: t4cols[3] }),
    ]}),
    new TableRow({ children: [
      cell("ARG/II/15", { width: t4cols[0] }),
      cell("Zaproszenie na dekoracj\u0119 Legi\u0105 Honorow\u0105 przez marsz. Focha (IV.1923)", { width: t4cols[1] }),
      cell("B", { width: t4cols[2] }),
      cell("Dokumentuje ceremoni\u0119 nieobj\u0119t\u0105 aktami urz\u0119dowymi", { width: t4cols[3] }),
    ]}),
    new TableRow({ children: [
      cell("ARG/II/16", { width: t4cols[0] }),
      cell("Dyplom Orderu Gwiazdy Rumunii, st. komandora (1.VIII.1923)", { width: t4cols[1] }),
      cell("C", { width: t4cols[2] }),
      cell("Orygina\u0142 dyplomu orderowego; w Zesp. 70 najwy\u017Cej wzmianka", { width: t4cols[3] }),
    ]}),
    new TableRow({ children: [
      cell("ARG/II/17", { width: t4cols[0] }),
      cell("Dekret prezydencki \u2014 zgoda na noszenie order\u00F3w zagranicznych (29.XI.1925)", { width: t4cols[1] }),
      cell("B", { width: t4cols[2] }),
      cell("Uzupe\u0142nia dokumentacj\u0119 orderow\u0105 jedn. 1", { width: t4cols[3] }),
    ]}),
    new TableRow({ children: [
      cell("ARG/II/23", { width: t4cols[0] }),
      cell("Portret oficjalny w mundurze ga\u0142owym z odznaczeniami (lata 30.)", { width: t4cols[1] }),
      cell("C", { width: t4cols[2] }),
      cell("Jedyny znany pe\u0142ny portret formalny; identyfikacja odznacze\u0144", { width: t4cols[3] }),
    ]}),
    new TableRow({ children: [
      cell("ARG/II/27", { width: t4cols[0] }),
      cell("List gen. Sosnkowskiego, Arundel, Kanada (28.V.1964)", { width: t4cols[1] }),
      cell("C", { width: t4cols[2] }),
      cell("Korespondencja prywatna; 14 dni przed \u015Bmierci\u0105 G\u0142uchowskiego", { width: t4cols[3] }),
    ]}),
    new TableRow({ children: [
      cell("ARG/II/28\u201329", { width: t4cols[0] }),
      cell("\u201EPro Memoria\u201D Sosnkowskiego \u2014 24 sprawy (28.V.1964)", { width: t4cols[1] }),
      cell("C", { width: t4cols[2] }),
      cell("Mapa siatki emigracyjnej; Giedroyc, Nowak-Jeziora\u0144ski, Belina", { width: t4cols[3] }),
    ]}),
  ],
}));

content.push(p([])); // spacer

content.push(p([
  t("Wst\u0119pne wyniki wskazuj\u0105, \u017Ce oko\u0142o 60% dokument\u00F3w serii ARG/II nale\u017Cy do kategorii B lub C \u2014 stanowi zatem materia\u0142 nieobecny lub niedostatecznie udokumentowany w Zespole 70. Wynik ten potwierdza tez\u0119 o wysokiej komplementarno\u015Bci obu zbior\u00F3w. Pe\u0142na taksonomia wymaga jednak dost\u0119pu do orygina\u0142\u00F3w obu zasob\u00F3w i por\u00F3wnania na poziomie dokumentu jednostkowego.", { size: 22, font: "Times New Roman" }),
  fn(9),
]));


// ============= SECTION 6 =============
content.push(new Paragraph({
  heading: HeadingLevel.HEADING_1,
  spacing: { before: 400, after: 200 },
  children: [tb("6. List Sosnkowskiego jako studium przypadku \u017Ar\u00F3d\u0142a unikalnego", { size: 26, font: "Times New Roman" })],
}));

content.push(p([
  t("Spo\u015Br\u00F3d dokument\u00F3w kategorii C, szczeg\u00F3lnej analizy wymaga zesp\u00F3\u0142 trzech dokument\u00F3w: list gen. broni Kazimierza Sosnkowskiego do gen. G\u0142uchowskiego (ARG/II/27) wraz z dwustronicowym za\u0142\u0105cznikiem \u201EPro Memoria\u201D (ARG/II/28\u201329), datowany 28 maja 1964 roku, Arundel, prowincja Quebec, Kanada.", { size: 22, font: "Times New Roman" }),
  fn(10),
]));

content.push(p([
  t("Sosnkowski \u2014 by\u0142y Naczelny W\u00F3dz PSZ (1943\u20131944), za\u0142o\u017Cyciel ZWC, najbli\u017Cszy wsp\u00F3\u0142pracownik Pi\u0142sudskiego \u2014 u\u017Cy\u0142 formu\u0142y \u201EKochany Generale.\u201D W tre\u015Bci przeprasza\u0142 za nieporozumienie dotycz\u0105ce Instytutu Pi\u0142sudskiego i sprawy Larousse\u2019a. Obiecywa\u0142 przy\u015Bpieszy\u0107 prac\u0119 nad tekstem o patrolu Beliny. G\u0142uchowski zmar\u0142 czterna\u015Bcie dni p\u00F3\u017Aniej.", { size: 22, font: "Times New Roman" }),
]));

content.push(p([
  t("Za\u0142\u0105cznik \u201EPro Memoria\u201D stanowi list\u0119 24 spraw prowadzonych jednocze\u015Bnie przez Sosnkowskiego. Pozycja 5: pro\u015Bba G\u0142uchowskiego o tekst o pocz\u0105tkach kawalerii. Pozycja 7: pro\u015Bba p\u0142k. Smole\u0144skiego o wspomnienia z patrolu Beliny. W dalszych pozycjach pojawiaj\u0105 si\u0119: Jerzy Giedroyc (paryska \u201EKultura,\u201D dwa artyku\u0142y), Jan Nowak-Jeziora\u0144ski (Radio Wolna Europa), 21. rocznica \u015Bmierci gen. Sikorskiego (Chicago). Dokument stanowi map\u0119 siatki polskiego \u017Cycia intelektualnego na uchod\u017Astwie \u2014 od Buenos Aires po Toronto \u2014 i jako taki ma warto\u015B\u0107 wykraczaj\u0105c\u0105 poza biografi\u0119 adresata.", { size: 22, font: "Times New Roman" }),
]));

content.push(p([
  t("Warto\u015B\u0107 archiwalna tego zespo\u0142u dokument\u00F3w jest potr\u00F3jna: (1) stanowi jedno z ostatnich \u015Bwiadectw relacji Sosnkowski\u2013G\u0142uchowski, trwaj\u0105cej od 1913 roku; (2) jako \u201EPro Memoria\u201D dokumentuje metod\u0119 pracy i siatk\u0119 kontakt\u00F3w by\u0142ego Naczelnego Wodza; (3) koresponduje bezpo\u015Brednio z Zespo\u0142em 19 Instytutu (Archiwum Sosnkowskiego, 33 jednostki), gdzie mog\u0105 znajdowa\u0107 si\u0119 listy G\u0142uchowskiego do Sosnkowskiego \u2014 zamykaj\u0105c potencjalnie \u0142uk korespondencji.", { size: 22, font: "Times New Roman" }),
  fn(11),
]));


// ============= SECTION 7 =============
content.push(new Paragraph({
  heading: HeadingLevel.HEADING_1,
  spacing: { before: 400, after: 200 },
  children: [tb("7. Szerszy kontekst archiwalny: zespo\u0142y powi\u0105zane", { size: 26, font: "Times New Roman" })],
}));

content.push(p([
  t("Obydwa zbiory \u2014 Zesp\u00F3\u0142 70 i kolekcja ARG \u2014 nie istniej\u0105 w izolacji archiwalnej. W zasobach Instytutu Pi\u0142sudskiego w Londynie (ponad 200 zespo\u0142\u00F3w) zidentyfikowano pi\u0119\u0107 dalszych zasob\u00F3w bezpo\u015Brednio powi\u0105zanych z biografi\u0105 genera\u0142a G\u0142uchowskiego i histori\u0105 kolekcji ARG.", { size: 22, font: "Times New Roman" }),
]));

// TABLE 5: Zespoły powiązane
content.push(p([ti("Tabela 5. Zespo\u0142y Instytutu Pi\u0142sudskiego powi\u0105zane z kolekcj\u0105 ARG", { size: 20, font: "Times New Roman" })], { spacing: { after: 60 } }));

const t5cols = [700, 1800, 3460, 3400];
content.push(new Table({
  width: { size: tw1, type: WidthType.DXA },
  columnWidths: t5cols,
  rows: [
    new TableRow({ children: [
      headerCell("Zesp.", t5cols[0]),
      headerCell("Nazwa", t5cols[1]),
      headerCell("Zawarto\u015B\u0107 istotna", t5cols[2]),
      headerCell("Powi\u0105zanie z ARG", t5cols[3]),
    ]}),
    new TableRow({ children: [
      cell("17", { width: t5cols[0] }),
      cell("Archiwum Ludwika Kmicic-Skrzy\u0144skiego", { width: t5cols[1] }),
      cell("Dokumenty dot. 1 P.U\u0142. Legion\u00F3w (Beliniak\u00F3w) i 7 P.U\u0142. Lubelskich. Pami\u0119tnik 1916\u20131918. Wspomnienia nagrywane dla RWE (1964). Wspomnienia S.\u00A0Stablewskiego o A.\u00A0Jab\u0142o\u0144skim \u2014 cz\u0142onku Si\u00F3demki.", { width: t5cols[2] }),
      cell("Lustrzane odbicie serii ARG/II. Dw\u00F3ch z Si\u00F3demki z\u0142o\u017Cy\u0142o archiwa w tym samym Instytucie.", { width: t5cols[3] }),
    ]}),
    new TableRow({ children: [
      cell("19", { width: t5cols[0] }),
      cell("Archiwum Kazimierza Sosnkowskiego (33 jedn.)", { width: t5cols[1] }),
      cell("Korespondencja s\u0142u\u017Cbowa i prywatna 1939\u20131970. Jedn. 14: korespondencja \u015Bci\u015Ble tajna z dow\u00F3dcami (1944, 1948\u201352). Jedn. 15: kopie list\u00F3w prywatnych. Jedn. 18: korespondencja wydawnicza (1964\u201365).", { width: t5cols[2] }),
      cell("Potencjalna \u201Edruga strona\u201D korespondencji ARG/II/27\u201329. Zamyka \u0142uk 51 lat relacji.", { width: t5cols[3] }),
    ]}),
    new TableRow({ children: [
      cell("22", { width: t5cols[0] }),
      cell("Legiony 1914\u20131918 (120 jedn.)", { width: t5cols[1] }),
      cell("Jedn. 37: Kronika 1 P.U\u0142. z listami oficer\u00F3w i strat. Jedn. 47: wspomnienia o Kostiuchn\u00F3wce. Jedn. 90: lista starszeNstwa oficer\u00F3w (1917).", { width: t5cols[2] }),
      cell("Dokumentuje okres Si\u00F3demki i kampanii legionowej; G\u0142uchowski powinien figurowa\u0107 w wykazach.", { width: t5cols[3] }),
    ]}),
    new TableRow({ children: [
      cell("23", { width: t5cols[0] }),
      cell("Wojna polsko-bolszewicka 1919\u20131920", { width: t5cols[1] }),
      cell("Telegramy frontowe VIII.1920. Historia 1 Dywizji Jazdy p\u0142k. R\u00F6mmla. Korespondencja od oficera \u0142\u0105cznikowego przy sztabie marsz. Focha.", { width: t5cols[2] }),
      cell("G\u0142uchowski dowodzi\u0142 7 P.U\u0142. w tej wojnie; Foch dekorowa\u0142 go w 1923.", { width: t5cols[3] }),
    ]}),
    new TableRow({ children: [
      cell("201", { width: t5cols[0] }),
      cell("Zbi\u00F3r fotograficzny", { width: t5cols[1] }),
      cell("Albumy i zdj\u0119cia lu\u017Ane z I wojny, mi\u0119dzywojnia, emigracji.", { width: t5cols[2] }),
      cell("Mog\u0105 zawiera\u0107 zdj\u0119cia G\u0142uchowskiego, Si\u00F3demki, 7 P.U\u0142., uroczysto\u015Bci emigracyjnych.", { width: t5cols[3] }),
    ]}),
  ],
}));

content.push(p([])); // spacer

content.push(p([
  t("Szczeg\u00F3lnie istotny jest Zesp\u00F3\u0142 17. Genera\u0142 Ludwik Kmicic-Skrzy\u0144ski (1893\u20131972), urodzony w Odessie, studiowa\u0142 chemi\u0119 w Nancy, organizowa\u0142 pluton Zwi\u0105zku Strzeleckiego, walczy\u0142 w Legionach, przeszed\u0142 przez Oflag IID Gross-Born, s\u0142u\u017Cy\u0142 w 2 Korpusie Polskim, a po wojnie osiad\u0142 w Manchesterze.", { size: 22, font: "Times New Roman" }),
  fn(12),
  t(" Jego archiwum zawiera: pami\u0119tnik z lat 1916\u20131918 (jedn. 3), wspomnienia nagrywane dla Radia Wolna Europa w 1964 roku (jedn. 7) oraz materia\u0142y dotycz\u0105ce zar\u00F3wno 1 Pu\u0142ku U\u0142an\u00F3w Legion\u00F3w (Beliniak\u00F3w), jak i 7 Pu\u0142ku U\u0142an\u00F3w Lubelskich \u2014 pu\u0142ku za\u0142o\u017Conego przez G\u0142uchowskiego. W jednostce 2 znajduj\u0105 si\u0119 wspomnienia Stefana Stablewskiego o Antonim Jab\u0142o\u0144skim \u2014 uczestniku Si\u00F3demki Beliny, kt\u00F3ry poleg\u0142 w wojnie 1920 roku.", { size: 22, font: "Times New Roman" }),
]));

content.push(p([
  t("Fakt, \u017Ce dw\u00F3ch z siedmiu kawalerzyst\u00F3w patrolu za\u0142o\u017Cycielskiego z\u0142o\u017Cy\u0142o swoje archiwa w tym samym Instytucie \u2014 kt\u00F3ry jeden z nich wsp\u00F3\u0142za\u0142o\u017Cy\u0142 \u2014 pozwala na unikalne zestawienie: rekonstrukcj\u0119 historii Si\u00F3demki z dw\u00F3ch perspektyw osobistych, uzupe\u0142nionych o relacje z kolekcji ARG i materia\u0142y z Zespo\u0142u 22 (Legiony). Belina-Pra\u017Cmowski, dow\u00F3dca patrolu, nie pozostawi\u0142 odr\u0119bnego archiwum (zmar\u0142 w 1938), co dodatkowo podnosi warto\u015B\u0107 \u017Ar\u00F3de\u0142 zachowanych przez jego zast\u0119pc\u0119 i ostatniego \u017Cyj\u0105cego cz\u0142onka patrolu.", { size: 22, font: "Times New Roman" }),
]));


// ============= SECTION 8 =============
content.push(new Paragraph({
  heading: HeadingLevel.HEADING_1,
  spacing: { before: 400, after: 200 },
  children: [tb("8. Instytut jako archiwum i pami\u0119\u0107: rola G\u0142uchowskiego-za\u0142o\u017Cyciela", { size: 26, font: "Times New Roman" })],
}));

content.push(p([
  t("Instytut J\u00F3zefa Pi\u0142sudskiego w Londynie, za\u0142o\u017Cony 15 marca 1947 roku, gromadzi ponad 200 zespo\u0142\u00F3w archiwalnych dokumentuj\u0105cych histori\u0119 polskiej emigracji wojskowej i politycznej. W\u015Br\u00F3d zdigitalizowanych kolekcji znajduj\u0105 si\u0119 archiwa najwy\u017Cszych dow\u00F3dc\u00F3w (Pi\u0142sudski \u2014 zesp. 1, Sosnkowski \u2014 zesp. 19, D\u0105b-Biernacki \u2014 zesp. 47), dokumentacja instytucji (Legiony \u2014 zesp. 22, PSZ w ZSRR \u2014 zesp. 21, Traktat Ryski \u2014 zesp. 106), a tak\u017Ce zbiory specjalne (mapy \u2014 zesp. 200, fotografie \u2014 zesp. 201). Zasoby Instytutu s\u0105 zarejestrowane w bazie SEZAM i IZA Naczelnej Dyrekcji Archiw\u00F3w Pa\u0144stwowych pod numerem 709.", { size: 22, font: "Times New Roman" }),
  fn(13),
]));

content.push(p([
  t("Przypadek G\u0142uchowskiego jest archiwoznawczo wyj\u0105tkowy: tw\u00F3rca zespo\u0142u (Zesp. 70) by\u0142 jednocze\u015Bnie wsp\u00F3\u0142tw\u00F3rc\u0105 instytucji przechowuj\u0105cej ten zesp\u00F3\u0142. Ta podw\u00F3jna rola \u2014 depozytariusza i za\u0142o\u017Cyciela \u2014 rodzi pytanie o \u015Bwiadomo\u015B\u0107 archiwistyczn\u0105: czy genera\u0142 dokonuj\u0105c selekcji dokument\u00F3w do przekazania, mia\u0142 \u015Bwiadomo\u015B\u0107 tego, kt\u00F3re akta nale\u017C\u0105 do sfery publicznej, a kt\u00F3re do prywatnej? Zestawienie inwentarzy sugeruje, \u017Ce tak: Zesp\u00F3\u0142 70 ma charakter wyra\u017Anie urz\u0119dowy (raporty, rozkazy, korespondencja s\u0142u\u017Cbowa), podczas gdy w rodzinie pozosta\u0142y dokumenty o charakterze osobistym (listy prywatne, fotografie, ordery w orygina\u0142ach, pami\u0105tki). Ten \u015Bwiadomy podzia\u0142 jest sam w sobie \u017Ar\u00F3d\u0142em informacji o mentalno\u015Bci archiwalnej tw\u00F3rcy zespo\u0142u.", { size: 22, font: "Times New Roman" }),
]));


// ============= SECTION 9: WNIOSKI =============
content.push(new Paragraph({
  heading: HeadingLevel.HEADING_1,
  spacing: { before: 400, after: 200 },
  children: [tb("9. Wnioski", { size: 26, font: "Times New Roman" })],
}));

content.push(p([
  t("Analiza por\u00F3wnawcza kolekcji prywatnej ARG i Zespo\u0142u 70 Instytutu Pi\u0142sudskiego prowadzi do nast\u0119puj\u0105cych wniosk\u00F3w:", { size: 22, font: "Times New Roman" }),
]));

content.push(p([
  tb("1. ", { size: 22, font: "Times New Roman" }),
  t("Oba zbiory s\u0105 ", { size: 22, font: "Times New Roman" }),
  tb("komplementarne, nie konkurencyjne", { size: 22, font: "Times New Roman" }),
  t(". Zesp\u00F3\u0142 70 (9 jednostek) dokumentuje karier\u0119 oficjaln\u0105 \u2014 s\u0142u\u017Cb\u0119, korespondencj\u0119 korporacyjn\u0105, raporty. Kolekcja ARG/II (33 jednostki) dokumentuje \u017Cycie prywatne, relacje osobiste i kontekst rodzinny. Dopiero po\u0142\u0105czenie obu pozwala zrekonstruowa\u0107 pe\u0142n\u0105 biografi\u0119 archiwalnl\u0105.", { size: 22, font: "Times New Roman" }),
]));

content.push(p([
  tb("2. ", { size: 22, font: "Times New Roman" }),
  t("Kolekcja ARG zawiera ", { size: 22, font: "Times New Roman" }),
  tb("dokumenty o najwy\u017Cszej warto\u015Bci \u017Ar\u00F3d\u0142owej", { size: 22, font: "Times New Roman" }),
  t(", nieobecne w zbiorach instytucjonalnych. W szczeg\u00F3lno\u015Bci: korespondencja Sosnkowskiego z \u201EPro Memoria\u201D (ARG/II/27\u201329), list marsza\u0142ka \u015Amig\u0142ego-Rydza (ARG/II/14), oryginalny dyplom Orderu Gwiazdy Rumunii (ARG/II/16), fotokopia Si\u00F3demki Beliny z podpisami (ARG/II/2). Ka\u017Cdy z tych dokument\u00F3w stanowi unikat.", { size: 22, font: "Times New Roman" }),
]));

content.push(p([
  tb("3. ", { size: 22, font: "Times New Roman" }),
  tb("Wielopokoleniowy charakter kolekcji ARG", { size: 22, font: "Times New Roman" }),
  t(" (5 os\u00F3b w 6 seriach) daje jej warto\u015B\u0107 niedost\u0119pn\u0105 z poziomu Zespo\u0142u 70. Rodzina G\u0142uchowskich \u2014 od ojca w PON, przez genera\u0142a w Legionach i II RP, braci w AK i Powstaniu, po bratanka-emigranta w Brazylii \u2014 stanowi mikrohistori\u0119 polskiego XX wieku.", { size: 22, font: "Times New Roman" }),
]));

content.push(p([
  tb("4. ", { size: 22, font: "Times New Roman" }),
  tb("Powi\u0105zania z pi\u0119cioma kolejnymi zespo\u0142ami", { size: 22, font: "Times New Roman" }),
  t(" Instytutu (17, 19, 22, 23, 201) tworz\u0105 szeroki kontekst archiwalny, w kt\u00F3rym kolekcja ARG pe\u0142ni rol\u0119 w\u0119z\u0142a \u0142\u0105cz\u0105cego \u017Ar\u00F3d\u0142a rozproszone mi\u0119dzy wieloma zasobami. Zesp\u00F3\u0142 17 (Kmicic-Skrzy\u0144ski) jest tu szczeg\u00F3lnie istotny: dw\u00F3ch z Si\u00F3demki Beliny z\u0142o\u017Cy\u0142o swoje archiwa w tej samej instytucji.", { size: 22, font: "Times New Roman" }),
]));

content.push(p([
  tb("5. ", { size: 22, font: "Times New Roman" }),
  t("Podzia\u0142 dokument\u00F3w mi\u0119dzy zbi\u00F3r instytucjonalny i prywatny odzwierciedla ", { size: 22, font: "Times New Roman" }),
  tb("\u015Bwiadomy wyb\u00F3r archiwalny tw\u00F3rcy zespo\u0142u", { size: 22, font: "Times New Roman" }),
  t(", kt\u00F3ry by\u0142 jednocze\u015Bnie wsp\u00F3\u0142za\u0142o\u017Cycielem instytucji przechowuj\u0105cej jego akta. Ta podw\u00F3jna rola \u2014 depozytariusza i za\u0142o\u017Cyciela \u2014 czyni przypadek G\u0142uchowskiego wyj\u0105tkowym w archiwoznawstwie emigracji polskiej.", { size: 22, font: "Times New Roman" }),
]));

content.push(p([
  tb("Postulat badawczy: ", { size: 22, font: "Times New Roman" }),
  t("Wskazane jest przeprowadzenie pe\u0142nej analizy por\u00F3wnawczej na poziomie dokumentu jednostkowego, obejmuj\u0105cej dost\u0119p do orygina\u0142\u00F3w Zespo\u0142u 70 w czytelni Instytutu Pi\u0142sudskiego w Londynie, a tak\u017Ce kwerend\u0119 w Zespo\u0142ach 17 i 19 pod k\u0105tem korespondencji wzajemnej. Przydatna by\u0142aby r\u00F3wnie\u017C kwerenda w Zespole 22 (listy oficer\u00F3w Legion\u00F3w, jedn. 37 i 90) w celu potwierdzenia obecno\u015Bci G\u0142uchowskiego w wykazach personalnych.", { size: 22, font: "Times New Roman" }),
]));


// ============= BIBLIOGRAPHY =============
content.push(new Paragraph({ children: [new PageBreak()] }));

content.push(new Paragraph({
  heading: HeadingLevel.HEADING_1,
  spacing: { before: 200, after: 300 },
  children: [tb("Bibliografia", { size: 26, font: "Times New Roman" })],
}));

// Sources archiwalne
content.push(new Paragraph({
  spacing: { before: 200, after: 120 },
  children: [tb("\u0179r\u00F3d\u0142a archiwalne", { size: 22, font: "Times New Roman" })],
}));

const bibArchive = [
  "Kolekcja prywatna ARG \u2014 Archiwum Rodziny G\u0142uchowskich. 217 jednostek w 6 seriach (ARG/I\u2013VI). Skatalogowane w standardzie ISAD(G), 2026.",
  "Instytut J\u00F3zefa Pi\u0142sudskiego w Londynie, Zesp\u00F3\u0142 17 \u2014 Archiwum Ludwika Kmicic-Skrzy\u0144skiego. 8 jednostek.",
  "Instytut J\u00F3zefa Pi\u0142sudskiego w Londynie, Zesp\u00F3\u0142 19 \u2014 Archiwum Kazimierza Sosnkowskiego. 33 jednostki.",
  "Instytut J\u00F3zefa Pi\u0142sudskiego w Londynie, Zesp\u00F3\u0142 22 \u2014 Legiony 1914\u20131918. 120 jednostek, 1912\u20131988.",
  "Instytut J\u00F3zefa Pi\u0142sudskiego w Londynie, Zesp\u00F3\u0142 23 \u2014 Wojna polsko-bolszewicka 1919\u20131920.",
  "Instytut J\u00F3zefa Pi\u0142sudskiego w Londynie, Zesp\u00F3\u0142 70 \u2014 Archiwum Janusza G\u0142uchowskiego. 9 jednostek, 1916\u20131964.",
  "Instytut J\u00F3zefa Pi\u0142sudskiego w Londynie, Zesp\u00F3\u0142 201 \u2014 Zbi\u00F3r fotograficzny.",
  "Wojskowe Biuro Historyczne, Biogram nr 76/45 (24.V.1937) \u2014 gen. Janusz G\u0142uchowski.",
  "Archiwum Historii M\u00F3wionej Muzeum Powstania Warszawskiego, sygn. 1889.",
];
for (const entry of bibArchive) {
  content.push(p([t(entry, { size: 22, font: "Times New Roman" })], { indent: { left: 480, hanging: 480 }, spacing: { after: 80, line: 360 } }));
}

// Opracowania
content.push(new Paragraph({
  spacing: { before: 200, after: 120 },
  children: [tb("Opracowania", { size: 22, font: "Times New Roman" })],
}));

const bibStudies = [
  [t("Chmielarz A., ", { size: 22, font: "Times New Roman" }), ti("Kedyw Okr\u0119gu Warszawa Armii Krajowej. Dokumenty \u2014 rok 1944", { size: 22, font: "Times New Roman" }), t(", Warszawa 2014.", { size: 22, font: "Times New Roman" })],
  [t("Habielski R., ", { size: 22, font: "Times New Roman" }), ti("\u017Bycie spo\u0142eczne i kulturalne emigracji", { size: 22, font: "Times New Roman" }), t(", Warszawa 1999.", { size: 22, font: "Times New Roman" })],
  [t("Kry\u0144ska-\u0141owi\u0144ska M., \u201EInstytut Pi\u0142sudskiego w Londynie: geneza i dzia\u0142alno\u015B\u0107,\u201D ", { size: 22, font: "Times New Roman" }), ti("Teki Archiwalne", { size: 22, font: "Times New Roman" }), t(", seria nowa, t. 11, 2012.", { size: 22, font: "Times New Roman" })],
  [t("Litewski J., ", { size: 22, font: "Times New Roman" }), ti("Si\u00F3demka Beliny", { size: 22, font: "Times New Roman" }), t(", Krak\u00F3w 1999.", { size: 22, font: "Times New Roman" })],
  [t("Stachiewicz P., ", { size: 22, font: "Times New Roman" }), ti("Parasol. Dzieje oddzia\u0142u do zada\u0144 specjalnych Kedywu Komendy G\u0142\u00F3wnej AK", { size: 22, font: "Times New Roman" }), t(", Warszawa 1984.", { size: 22, font: "Times New Roman" })],
  [t("Wro\u0144ski T., ", { size: 22, font: "Times New Roman" }), ti("Kronika Powstania Warszawskiego", { size: 22, font: "Times New Roman" }), t(", Warszawa 2004.", { size: 22, font: "Times New Roman" })],
];
for (const runs of bibStudies) {
  content.push(p(runs, { indent: { left: 480, hanging: 480 }, spacing: { after: 80, line: 360 } }));
}

// Portale
content.push(new Paragraph({
  spacing: { before: 200, after: 120 },
  children: [tb("Portale i bazy danych", { size: 22, font: "Times New Roman" })],
}));

const bibPortals = [
  "Instytut J\u00F3zefa Pi\u0142sudskiego w Londynie \u2014 katalog zbior\u00F3w: pilsudski.org.uk/pl/katalog.php",
  "Instytut Pi\u0142sudskiego w Ameryce \u2014 baza archiwalna: pilsudski.org",
  "Instytut Pami\u0119ci Narodowej \u2014 baza biogramowa: ipn.gov.pl",
  "Encyklopedia PWN: encyklopedia.pwn.pl/haslo/Gluchowski-Janusz;3906169.html",
  "Muzeum Powstania Warszawskiego \u2014 biogramy: 1944.pl",
  "Naczelna Dyrekcja Archiw\u00F3w Pa\u0144stwowych: szukajwarchiwach.gov.pl (baza SEZAM/IZA, Instytut Pi\u0142sudskiego Londyn \u2014 nr 709)",
];
for (const entry of bibPortals) {
  content.push(p([t(entry, { size: 22, font: "Times New Roman" })], { indent: { left: 480, hanging: 480 }, spacing: { after: 80, line: 360 } }));
}


// ============= BUILD DOCUMENT =============

const doc = new Document({
  styles: {
    default: {
      document: {
        run: { font: "Times New Roman", size: 24 }, // 12pt default
      },
    },
    paragraphStyles: [
      {
        id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 26, bold: true, font: "Times New Roman" },
        paragraph: { spacing: { before: 400, after: 200 }, outlineLevel: 0 },
      },
    ],
  },
  footnotes,
  sections: [{
    properties: {
      page: {
        size: {
          width: 11906, // A4
          height: 16838,
        },
        margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 },
      },
    },
    headers: {
      default: new Header({
        children: [new Paragraph({
          alignment: AlignmentType.CENTER,
          children: [t("Teki Archiwalne \u00B7 2026", { size: 18, font: "Times New Roman", color: "999999", italics: true })],
        })],
      }),
    },
    footers: {
      default: new Footer({
        children: [new Paragraph({
          alignment: AlignmentType.CENTER,
          children: [new TextRun({ children: [PageNumber.CURRENT], size: 18, font: "Times New Roman", color: "999999" })],
        })],
      }),
    },
    children: content,
  }],
});

// Generate and save
const outPath = "C:\\Users\\skore\\leiloesbr-scraper\\docs\\artykul_belina_instytut.docx";
Packer.toBuffer(doc).then(buffer => {
  fs.writeFileSync(outPath, buffer);
  console.log(`DOCX saved: ${outPath} (${(buffer.length / 1024).toFixed(0)} KB)`);
}).catch(err => {
  console.error("Error:", err.message);
  process.exit(1);
});
