const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  Header, Footer, AlignmentType, LevelFormat,
  FootnoteReferenceRun, HeadingLevel, BorderStyle, WidthType, ShadingType,
  PageNumber, PageBreak, TabStopType, TabStopPosition
} = require("docx");

// ============================================================
// HELPERS
// ============================================================
const FONT = "Times New Roman";
const SZ = 24;  // 12pt
const SZ_FN = 20; // 10pt for footnotes
const SZ_SMALL = 20; // 10pt
const SZ_H1 = 28; // 14pt
const SZ_H2 = 26; // 13pt
const LINE = 360; // 1.5 line spacing

const t = (text, opts = {}) => new TextRun({ text, font: FONT, size: SZ, ...opts });
const ti = (text, opts = {}) => new TextRun({ text, font: FONT, size: SZ, italics: true, ...opts });
const tb = (text, opts = {}) => new TextRun({ text, font: FONT, size: SZ, bold: true, ...opts });
const ts = (text, opts = {}) => new TextRun({ text, font: FONT, size: SZ_SMALL, ...opts });
const fn = (id) => new FootnoteReferenceRun(id);

const p = (children, opts = {}) => new Paragraph({
  spacing: { after: 200, line: LINE },
  alignment: AlignmentType.JUSTIFIED,
  indent: { firstLine: 720 }, // 0.5 inch indent
  ...opts,
  children: Array.isArray(children) ? children : [children],
});

const p0 = (children, opts = {}) => new Paragraph({
  spacing: { after: 200, line: LINE },
  alignment: AlignmentType.JUSTIFIED,
  ...opts,
  children: Array.isArray(children) ? children : [children],
});

const heading = (text, level = HeadingLevel.HEADING_1) => new Paragraph({
  heading: level,
  spacing: { before: 400, after: 200 },
  children: [new TextRun({ text, font: FONT, size: level === HeadingLevel.HEADING_1 ? SZ_H1 : SZ_H2, bold: true })],
});

// Table helpers
const border = { style: BorderStyle.SINGLE, size: 1, color: "999999" };
const borders = { top: border, bottom: border, left: border, right: border };
const hdrShading = { fill: "E8E8E8", type: ShadingType.CLEAR };

const cell = (content, w, opts = {}) => {
  const children = Array.isArray(content)
    ? [new Paragraph({ spacing: { after: 0, line: 240 }, children: content })]
    : [new Paragraph({ spacing: { after: 0, line: 240 }, children: [new TextRun({ text: content, font: FONT, size: SZ_SMALL })] })];
  return new TableCell({
    borders,
    width: { size: w, type: WidthType.DXA },
    margins: { top: 40, bottom: 40, left: 80, right: 80 },
    ...opts,
    children,
  });
};

const hdrCell = (text, w) => cell(
  [new TextRun({ text, font: FONT, size: SZ_SMALL, bold: true })],
  w,
  { shading: hdrShading }
);

// ============================================================
// FOOTNOTES
// ============================================================
const makeFn = (text) => ({ children: [new Paragraph({ spacing: { after: 60, line: 240 }, children: [new TextRun({ text, font: FONT, size: SZ_FN })] })] });

const footnotes = {
  1: makeFn("O rozproszeniu archiw\u00F3w emigracji polskiej zob. R. Habielski, \u017Bycie spo\u0142eczne i kulturalne emigracji, Warszawa 1999; M. Kry\u0144ska-\u0141owi\u0144ska, \u201EInstytut Pi\u0142sudskiego w Londynie: geneza i dzia\u0142alno\u015B\u0107\u201D, \u201ETeki Archiwalne\u201D, seria nowa, t. 11, 2012."),
  2: makeFn("Instytut J\u00F3zefa Pi\u0142sudskiego w Londynie, za\u0142. 15 III 1947 r., zarejestrowany w bazie SEZAM/IZA NDAP pod nr 709. G\u0142uchowski figuruje w\u015Br\u00F3d wsp\u00F3\u0142za\u0142o\u017Cycieli. Zesp\u00F3\u0142 70 wydzielony jako odr\u0119bna jednostka archiwalna."),
  3: makeFn("ARG/II/1, Biogram WBH nr 76/45, 24 V 1937 r. Potwierdza: OB PPS od 1905 (w wieku 17 lat), ZWC w Li\u00E8ge (wsp\u00F3\u0142za\u0142o\u017Cyciel z T. Piskorem), Zwi\u0105zek Strzelecki. Dokument sporz\u0105dzony za \u017Cycia bohatera i zweryfikowany przez instytucj\u0119 wojskow\u0105."),
  4: makeFn("Identyfikacja uczestnik\u00F3w patrolu na podstawie: IPN, baza biogramowa (ipn.gov.pl); jpilsudski.org; fotokopia grupowa z podpisami ARG/II/2. Zob. J. Litewski, Si\u00F3demka Beliny, Krak\u00F3w 1999."),
  5: makeFn("ARG/II/15: zaproszenie datowane IV 1923 r., ceremonia 3 V 1923 r., Plac Saski, Warszawa. ARG/II/16: dyplom Ordinul Steaua Rom\u00E2niei w stopniu Comandor, podpisany przez kr\u00F3la Ferdynanda I. ARG/II/17: pismo MSWojsk L.75/25 G.M.I. z 29 XI 1925 r."),
  6: makeFn("Encyklopedia PWN, has\u0142o \u201EG\u0142uchowski Janusz\u201D (encyklopedia.pwn.pl/haslo/3906169). IPN, biogram (ipn.gov.pl/pl/100-bohaterow-na-100-le/104516). Cmentarz Brompton, Londyn, gr\u00F3b nr 576."),
  7: makeFn("Opis Zespo\u0142u 70: Instytut Pi\u0142sudskiego w Londynie, pilsudski.org.uk/pl/archiwum-070.php (dost\u0119p: III 2026 r.). Inwentarz ma charakter ramowy; pe\u0142ny opis dost\u0119pny w czytelni Instytutu."),
  8: makeFn("Obecno\u015B\u0107 wierszy w Zespole 70 (jedn. 6) jest zaskakuj\u0105ca i mo\u017Ce wskazywa\u0107 na aktywno\u015B\u0107 literack\u0105 genera\u0142a w okresie wojennym. Kalendarze i notatnik (jedn. 1) mog\u0105 pe\u0142ni\u0107 funkcj\u0119 dziennika."),
  9: makeFn("Odsetek 60% ma charakter szacunkowy, oparty na por\u00F3wnaniu inwentarza ramowego Zesp. 70 z pe\u0142nym katalogiem ARG. Pe\u0142na taksonomia wymaga dost\u0119pu do orygina\u0142\u00F3w obu zbior\u00F3w."),
  10: makeFn("ARG/II/27, list gen. broni Kazimierza Sosnkowskiego do gen. dyw. Janusza G\u0142uchowskiego, dat. 28 V 1964 r., Arundel, P. Qu\u00E9bec, Kanada. Do listu do\u0142\u0105czono \u201EPro Memoria\u201D (ARG/II/28\u201329) z 24 pozycjami spraw."),
  11: makeFn("Zesp\u00F3\u0142 19 (Archiwum Sosnkowskiego), 33 jednostki. Jedn. 14: \u201EKorespondencja \u015Bci\u015Ble tajna z dow\u00F3dcami\u201D; jedn. 15: \u201EKopie list\u00F3w prywatnych\u201D; jedn. 18: \u201EKorespondencja wydawnicza\u201D. Rok 1964 pokrywa si\u0119 z dat\u0105 listu ARG/II/27."),
  12: makeFn("Zesp\u00F3\u0142 17 (Archiwum L. Kmicic-Skrzy\u0144skiego). Nota biograficzna wg opisu zespo\u0142u: pilsudski.org.uk/pl/archiwum-017.php."),
  13: makeFn("Instytut Pi\u0142sudskiego w Londynie, pe\u0142ny katalog zbior\u00F3w: pilsudski.org.uk/pl/katalog.php. Rejestracja NDAP pod nr 709: baza SEZAM (szukajwarchiwach.gov.pl)."),
  14: makeFn("Analiza fotograficzna przeprowadzona na podstawie czterech sesji skanowania kolekcji ARG w marcu 2026 r. Numery WSF (War Services Fund?) stanowi\u0105 systematyczn\u0105 numeracj\u0119 negatyw\u00F3w wojskowej pracowni fotograficznej PSZ w Szkocji."),
  15: makeFn("Zdj\u0119cie sup_p06_007: gen. W\u0142adys\u0142aw Sikorski, gen. Bronis\u0142aw Klimecki i gen. Janusz G\u0142uchowski. Klimecki zgin\u0105\u0142 razem z Sikorskim w katastrofie gibraltarskiej 4 VII 1943 r."),
  16: makeFn("8 zdj\u0119\u0107 WSF dokumentuj\u0105cych wyzwolenie obozu kobiet w Holandii (IV 1945 r.). Raport ppor. Milewskiej o warunkach w obozie \u2014 nieznana dotychczas relacja kobieca z wyzwolenia."),
};

// ============================================================
// CONTENT SECTIONS
// ============================================================
const content = [];

// --- TITLE PAGE ---
content.push(new Paragraph({ spacing: { before: 2000, after: 200 }, alignment: AlignmentType.CENTER, children: [
  new TextRun({ text: "Od Si\u00F3demki Beliny do Instytutu Pi\u0142sudskiego", font: FONT, size: 36, bold: true }),
] }));
content.push(new Paragraph({ spacing: { after: 100 }, alignment: AlignmentType.CENTER, children: [
  new TextRun({ text: "Zesp\u00F3\u0142 nr 70 Archiwum Instytutu J\u00F3zefa Pi\u0142sudskiego w Londynie", font: FONT, size: 28, bold: true }),
] }));
content.push(new Paragraph({ spacing: { after: 100 }, alignment: AlignmentType.CENTER, children: [
  new TextRun({ text: "jako \u017Ar\u00F3d\u0142o do dziej\u00F3w kawalerii polskiej 1914\u20131947", font: FONT, size: 28, bold: true }),
] }));
content.push(new Paragraph({ spacing: { after: 100 }, alignment: AlignmentType.CENTER, children: [
  ti("Studium komplementarno\u015Bci kolekcji prywatnej ARG (311 jednostek) i Zespo\u0142u 70 Instytutu J\u00F3zefa Pi\u0142sudskiego w Londynie na tle pi\u0119ciu powi\u0105zanych zespo\u0142\u00F3w archiwalnych", { size: 22 }),
] }));
content.push(new Paragraph({ spacing: { before: 400, after: 100 }, alignment: AlignmentType.CENTER, children: [
  t("Marek Skonieczny", { bold: true }),
] }));
content.push(new Paragraph({ spacing: { after: 100 }, alignment: AlignmentType.CENTER, children: [
  ts("Badacz niezale\u017Cny"),
] }));
content.push(new Paragraph({ spacing: { after: 100 }, alignment: AlignmentType.CENTER, children: [
  ts("Warszawa \u2013 Rio de Janeiro"),
] }));
content.push(new Paragraph({ spacing: { after: 100 }, alignment: AlignmentType.CENTER, children: [
  ts("skorek2000@yahoo.com"),
] }));
content.push(new Paragraph({ spacing: { after: 400 }, alignment: AlignmentType.CENTER, children: [
  ts("Marzec 2026"),
] }));

// --- ABSTRAKT PL ---
content.push(new Paragraph({ spacing: { after: 40 }, children: [tb("Abstrakt", { size: SZ_SMALL })] }));
content.push(p0([
  ti("Artyku\u0142 przedstawia por\u00F3wnawcz\u0105 analiz\u0119 zasob\u00F3w archiwalnych dokumentuj\u0105cych \u017Cycie genera\u0142a dywizji Janusza Juliana G\u0142uchowskiego (1888\u20131964). Przedmiotem analizy s\u0105 dwa zbiory: kolekcja prywatna ARG (311 jednostek w sze\u015Bciu seriach, skatalogowana w standardzie ISAD(G)) oraz Zesp\u00F3\u0142 70 Instytutu J\u00F3zefa Pi\u0142sudskiego w Londynie (9 jednostek, 1916\u20131964). Na podstawie por\u00F3wnania inwentarzy metod\u0105 pozycja-po-pozycji zidentyfikowano dokumenty kategorii A (duplikaty), B (uzupe\u0142nienia) i C (unikaty). Oko\u0142o 60% dokument\u00F3w serii ARG/II stanowi materia\u0142 nieobecny w Zespole 70. W szerszym kontek\u015Bcie archiwalnym wykazano powi\u0105zania z pi\u0119cioma kolejnymi zespo\u0142ami Instytutu. Nowa sekcja artyku\u0142u prezentuje odkrycia z analizy 121 fotografii \u2014 w tym dokumentacj\u0119 wizyt najwy\u017Cszych w\u0142adz RP na uchod\u017Astwie, nieznanego fotografa wojskowego PSZ oraz moment wyzwolenia obozu kobiet w Holandii.", { size: SZ_SMALL }),
]));

// --- ABSTRAKT EN ---
content.push(new Paragraph({ spacing: { before: 200, after: 40 }, children: [tb("Abstract", { size: SZ_SMALL })] }));
content.push(p0([
  ti("This article presents a comparative analysis of archival resources documenting the life of Major General Janusz Julian G\u0142uchowski (1888\u20131964). Two collections are examined: the private ARG collection (311 items in six series, catalogued according to ISAD(G)) and Collection 70 of the J\u00F3zef Pi\u0142sudski Institute in London (9 items, 1916\u20131964). Through item-by-item inventory comparison, documents were classified as Category A (duplicates), B (supplements), or C (uniques). Approximately 60% of ARG Series II documents constitute material absent from Collection 70. A new section presents discoveries from the analysis of 121 photographs, including documentation of visits by the highest Polish authorities in exile, an unknown military photographer of the Polish Armed Forces, and the moment of liberation of a women\u2019s camp in Holland.", { size: SZ_SMALL }),
]));

// --- S\u0141OWA KLUCZOWE ---
content.push(new Paragraph({ spacing: { before: 200, after: 200 }, children: [
  tb("S\u0142owa kluczowe: ", { size: SZ_SMALL }),
  ts("archiwoznawstwo, komplementarno\u015B\u0107 archiwalna, kolekcja prywatna, Instytut Pi\u0142sudskiego w Londynie, Si\u00F3demka Beliny, gen. Janusz G\u0142uchowski, Polskie Si\u0142y Zbrojne, emigracja wojskowa, ISAD(G), fotografia wojskowa"),
] }));
content.push(new Paragraph({ spacing: { after: 200 }, children: [
  tb("Keywords: ", { size: SZ_SMALL }),
  ts("archival science, archival complementarity, private collection, Pi\u0142sudski Institute London, Belina\u2019s Seven, Polish Armed Forces, military emigration, ISAD(G), military photography"),
] }));

content.push(new Paragraph({ children: [new PageBreak()] }));

// ============================================================
// 1. WPROWADZENIE
// ============================================================
content.push(heading("1. Wprowadzenie: problem rozproszenia \u017Ar\u00F3de\u0142"));

content.push(p([
  t("Archiwa polskiej emigracji wojskowej po 1945 roku cechuje charakterystyczny podzia\u0142: cz\u0119\u015B\u0107 dokumentacji trafia\u0142a do instytucji powo\u0142anych dla ochrony pami\u0119ci \u2014 Instytutu Pi\u0142sudskiego, Instytutu Sikorskiego, Biblioteki Polskiej w Pary\u017Cu \u2014 podczas gdy dokumenty o charakterze prywatnym pozostawa\u0142y w r\u0119kach rodzin. Podzia\u0142 ten wynika\u0142 z praktyki archiwalnej: oficerowie przekazywali akta s\u0142u\u017Cby, rozkazy i korespondencj\u0119 urz\u0119dow\u0105, zatrzymuj\u0105c listy osobiste, fotografie i pami\u0105tki rodzinne."),
  fn(1),
]));

content.push(p([
  t("Genera\u0142 dywizji Janusz Julian G\u0142uchowski (1888\u20131964) stanowi modelowy przypadek takiego rozproszenia. Jego dokumentacja archiwalna istnieje w dw\u00F3ch odr\u0119bnych zbiorach: Zespole 70 Instytutu J\u00F3zefa Pi\u0142sudskiego w Londynie (9 jednostek archiwalnych, lata 1916\u20131964) oraz kolekcji prywatnej oznaczonej sygnatur\u0105 ARG (311 jednostek w sze\u015Bciu seriach, skatalogowanej w standardzie ISAD(G) w 2026 roku). Dodatkow\u0105 warto\u015B\u0107 analityczn\u0105 wnosi fakt, \u017Ce G\u0142uchowski by\u0142 wsp\u00F3\u0142za\u0142o\u017Cycielem instytucji, w kt\u00F3rej jego w\u0142asne akta s\u0105 dzi\u015B przechowywane."),
  fn(2),
]));

content.push(p([
  t("Celem niniejszego artyku\u0142u jest: (1) por\u00F3wnanie zawarto\u015Bci obu zbior\u00F3w metod\u0105 inwentarza r\u00F3wnoleg\u0142ego; (2) identyfikacja dokument\u00F3w komplementarnych, uzupe\u0142niaj\u0105cych i unikalnych; (3) umieszczenie obu zbior\u00F3w w szerszym kontek\u015Bcie archiwalnym Instytutu Pi\u0142sudskiego; (4) prezentacja nowych odkry\u0107 wynikaj\u0105cych z analizy 121 fotografii ze zbioru ARG."),
]));

// ============================================================
// 2. NOTA BIOGRAFICZNA
// ============================================================
content.push(heading("2. Nota biograficzna: od bojowca PPS do wsp\u00F3\u0142za\u0142o\u017Cyciela Instytutu"));

content.push(p([
  t("Janusz Julian G\u0142uchowski urodzi\u0142 si\u0119 19 czerwca 1888 roku w Bukowej, powiat Piotrk\u00F3w Trybunalski. By\u0142 synem Mariana G\u0142uchowskiego, dzia\u0142acza Polskiej Organizacji Narodowej, kt\u00F3rego dokumenty zachowa\u0142y si\u0119 w serii ARG/I (6 jednostek, 1914). W 1905 roku, w wieku siedemnastu lat, wst\u0105pi\u0142 do Organizacji Bojowej PPS. Dzia\u0142a\u0142 w niej do 1908 roku, po czym wyjecha\u0142 na studia na Politechnik\u0119 w Li\u00E8ge, gdzie wsp\u00F3\u0142za\u0142o\u017Cy\u0142 z Tadeuszem Piskorem kom\u00F3rk\u0119 Zwi\u0105zku Walki Czynnej."),
  fn(3),
]));

content.push(p([
  t("W nocy z 2 na 3 sierpnia 1914 roku G\u0142uchowski, jako zast\u0119pca dow\u00F3dcy W\u0142adys\u0142awa Beliny-Pra\u017Cmowskiego, uczestniczy\u0142 w patrolu Si\u00F3demki Beliny \u2014 pierwszym regularnym oddziale polskim od Powstania Styczniowego."),
  fn(4),
  t(" Dalsze etapy kariery: 5 listopada 1918 roku otrzyma\u0142 rozkaz organizacji nowego oddzia\u0142u jazdy (ARG/II/8) \u2014 przysz\u0142ego 7 Pu\u0142ku U\u0142an\u00F3w Lubelskich. W okresie mi\u0119dzywojennym dekorowany Legi\u0105 Honorow\u0105 przez marsza\u0142ka Focha (3 V 1923 r., ARG/II/15), Orderem Gwiazdy Rumunii w stopniu komandora (1 VIII 1923 r., ARG/II/16)."),
  fn(5),
]));

content.push(p([
  t("5 pa\u017Adziernika 1935 roku zosta\u0142 mianowany I Zast\u0119pc\u0105 Ministra Spraw Wojskowych (ARG/II/19). Po kampanii wrze\u015Bniowej \u2014 internowanie w Rumunii, Palestyna (X 1940 r.), Londyn (II 1941 r.). Od wrze\u015Bnia 1943 r. dow\u00F3dca Polskich Jednostek Wojskowych w Wielkiej Brytanii. 1 czerwca 1945 r. \u2014 awans na genera\u0142a dywizji. 15 marca 1947 roku wsp\u00F3\u0142za\u0142o\u017Cy\u0142 Instytut J\u00F3zefa Pi\u0142sudskiego w Londynie. Zmar\u0142 11 czerwca 1964 roku. Pochowany na cmentarzu Brompton (gr\u00F3b 576)."),
  fn(6),
]));

// ============================================================
// 3. ZESP\u00D3\u0141 70
// ============================================================
content.push(heading("3. Zesp\u00F3\u0142 70: inwentarz i charakterystyka"));

content.push(p([
  t("Zesp\u00F3\u0142 70 Instytutu Pi\u0142sudskiego w Londynie nosi nazw\u0119 \u201EArchiwum Janusza G\u0142uchowskiego\u201D i obejmuje 9 jednostek archiwalnych z lat 1916\u20131964."),
  fn(7),
]));

// Table 2 - Inwentarz Zespo\u0142u 70
const TW = 9026; // A4 content width
const t2cols = [600, 5426, 1200, 1800];
content.push(p0([ts("Tabela 1. Inwentarz Zespo\u0142u 70 \u2014 Archiwum Janusza G\u0142uchowskiego", { italics: true })]));
content.push(new Table({
  width: { size: TW, type: WidthType.DXA },
  columnWidths: t2cols,
  rows: [
    new TableRow({ children: [hdrCell("Nr", t2cols[0]), hdrCell("Opis jednostki", t2cols[1]), hdrCell("Daty", t2cols[2]), hdrCell("Charakter", t2cols[3])] }),
    new TableRow({ children: [cell("1", t2cols[0]), cell("\u017Byciorys, rozkazy, nominacje, dokumenty osobiste, broszury, wycinki", t2cols[1]), cell("1916\u20131964", t2cols[2]), cell("osobisty/s\u0142u\u017Cbowy", t2cols[3])] }),
    new TableRow({ children: [cell("2", t2cols[0]), cell("Korespondencja z Ko\u0142em Genera\u0142\u00F3w i Pu\u0142kownik\u00F3w; wykaz adres\u00F3w", t2cols[1]), cell("1948\u20131963", t2cols[2]), cell("korporacyjny", t2cols[3])] }),
    new TableRow({ children: [cell("3", t2cols[0]), cell("Korespondencja s\u0142u\u017Cbowa i prywatna", t2cols[1]), cell("1940\u20131961", t2cols[2]), cell("mieszany", t2cols[3])] }),
    new TableRow({ children: [cell("4", t2cols[0]), cell("Wspomnienia, przem\u00F3wienia", t2cols[1]), cell("b.d.", t2cols[2]), cell("narracyjny", t2cols[3])] }),
    new TableRow({ children: [cell("5", t2cols[0]), cell("Korespondencja", t2cols[1]), cell("1943\u20131963", t2cols[2]), cell("mieszany", t2cols[3])] }),
    new TableRow({ children: [cell("6", t2cols[0]), cell("Raporty, sprawozdania ze Sztabu G\u0142\u00F3wnego, zapisy rozm\u00F3w, wiersze", t2cols[1]), cell("1940\u20131945", t2cols[2]), cell("s\u0142u\u017Cbowy/lit.", t2cols[3])] }),
    new TableRow({ children: [cell("7", t2cols[0]), cell("Korespondencja z pras\u0105, wycinki prasowe", t2cols[1]), cell("b.d.", t2cols[2]), cell("prasowy", t2cols[3])] }),
    new TableRow({ children: [cell("8", t2cols[0]), cell("Brudnopisy", t2cols[1]), cell("b.d.", t2cols[2]), cell("roboczy", t2cols[3])] }),
    new TableRow({ children: [cell("9", t2cols[0]), cell("Emigracja \u2014 druki ulotne, komunikaty, rozkazy, or\u0119dzia", t2cols[1]), cell("1946\u20131961", t2cols[2]), cell("emigracyjny", t2cols[3])] }),
  ],
}));

content.push(p([
  t("Analiza inwentarza ujawnia kilka cech istotnych. Po pierwsze, Zesp\u00F3\u0142 70 ma charakter przede wszystkim "),
  tb("s\u0142u\u017Cbowy i korporacyjny"),
  t(". Po drugie, zbi\u00F3r obejmuje wy\u0142\u0105cznie dokumenty samego genera\u0142a \u2014 brak jakiejkolwiek dokumentacji rodzinnej. Po trzecie, zas\u0142uguj\u0105 na uwag\u0119 dwa elementy niespodziewane: "),
  tb("wiersze"),
  t(" (jedn. 6) oraz "),
  tb("kalendarze i notatnik"),
  t(" (jedn. 1)."),
  fn(8),
]));

// ============================================================
// 4. KOLEKCJA ARG
// ============================================================
content.push(heading("4. Kolekcja prywatna ARG: struktura i zakres"));

content.push(p([
  t("Kolekcja prywatna ARG (Archiwum Rodziny G\u0142uchowskich) zosta\u0142a skatalogowana w 2026 roku w standardzie ISAD(G). Obejmuje 311 jednostek w sze\u015Bciu seriach:"),
]));

// Table 3
const t3cols = [900, 3126, 700, 1300, 3000];
content.push(p0([ts("Tabela 2. Struktura kolekcji ARG", { italics: true })]));
content.push(new Table({
  width: { size: TW, type: WidthType.DXA },
  columnWidths: t3cols,
  rows: [
    new TableRow({ children: [hdrCell("Seria", t3cols[0]), hdrCell("Osoba", t3cols[1]), hdrCell("Jedn.", t3cols[2]), hdrCell("Daty", t3cols[3]), hdrCell("Charakter", t3cols[4])] }),
    new TableRow({ children: [cell("ARG/I", t3cols[0]), cell("Marian G\u0142uchowski (ojciec)", t3cols[1]), cell("6", t3cols[2]), cell("1914", t3cols[3]), cell("PON, dzia\u0142alno\u015B\u0107 niepodleg\u0142o\u015Bciowa", t3cols[4])] }),
    new TableRow({ children: [cell("ARG/II", t3cols[0]), cell("Gen. dyw. Janusz G\u0142uchowski", t3cols[1]), cell("66", t3cols[2]), cell("1905\u20131964", t3cols[3]), cell("s\u0142u\u017Cba, ordery, fotografie", t3cols[4])] }),
    new TableRow({ children: [cell("ARG/III", t3cols[0]), cell("Ppor. Stanis\u0142aw Stefan G\u0142uchowski", t3cols[1]), cell("38", t3cols[2]), cell("1944\u20131945", t3cols[3]), cell("AK, Powstanie, Stalag XI-B", t3cols[4])] }),
    new TableRow({ children: [cell("ARG/IV", t3cols[0]), cell("Lech G\u0142uchowski \u201EJe\u017Cycki\u201D", t3cols[1]), cell("wzm.", t3cols[2]), cell("1900\u20131944", t3cols[3]), cell("poleg\u0142 w Powstaniu 15 IX 1944 r.", t3cols[4])] }),
    new TableRow({ children: [cell("ARG/V", t3cols[0]), cell("Krzysztof G\u0142uchowski \u201EJura\u015B\u201D", t3cols[1]), cell("173", t3cols[2]), cell("1926\u20132020", t3cols[3]), cell("Powstanie, jeniec, emigracja", t3cols[4])] }),
    new TableRow({ children: [cell("ARG/VI", t3cols[0]), cell("Varia / Rodzina", t3cols[1]), cell("28", t3cols[2]), cell("r\u00F3\u017Cne", t3cols[3]), cell("dokumenty podr\u00F3\u017Cy, pami\u0105tki", t3cols[4])] }),
  ],
}));

content.push(p([
  t("Kluczowa r\u00F3\u017Cnica mi\u0119dzy oboma zbiorami le\u017Cy w "),
  tb("zakresie podmiotowym"),
  t(". Zesp\u00F3\u0142 70 dokumentuje wy\u0142\u0105cznie genera\u0142a. Kolekcja ARG dokumentuje ca\u0142\u0105 rodzin\u0119 \u2014 pi\u0119\u0107 os\u00F3b w trzech pokoleniach, z kt\u00F3rych ka\u017Cde walczy\u0142o o niepodleg\u0142o\u015B\u0107."),
]));

// ============================================================
// 5. METODOLOGIA
// ============================================================
content.push(heading("5. Metodologia por\u00F3wnania inwentarzy"));

content.push(p([
  t("Analiz\u0119 komplementarno\u015Bci przeprowadzono metod\u0105 "),
  tb("inwentarza r\u00F3wnoleg\u0142ego"),
  t(": dla ka\u017Cdego dokumentu serii ARG/II weryfikowano, czy odpowiadaj\u0105cy mu dokument istnieje w Zespole 70. Zastosowano trzy kategorie: "),
  tb("A"),
  t(" \u2014 duplikaty; "),
  tb("B"),
  t(" \u2014 uzupe\u0142nienia; "),
  tb("C"),
  t(" \u2014 unikaty."),
]));

content.push(p([
  t("Wst\u0119pne wyniki wskazuj\u0105, \u017Ce oko\u0142o 60% dokument\u00F3w serii ARG/II nale\u017Cy do kategorii B lub C \u2014 stanowi zatem materia\u0142 nieobecny lub niedostatecznie udokumentowany w Zespole 70."),
  fn(9),
]));

// ============================================================
// 6. LIST SOSNKOWSKIEGO
// ============================================================
content.push(heading("6. List Sosnkowskiego jako studium przypadku \u017Ar\u00F3d\u0142a unikalnego"));

content.push(p([
  t("Spo\u015Br\u00F3d dokument\u00F3w kategorii C, szczeg\u00F3lnej analizy wymaga zesp\u00F3\u0142 trzech dokument\u00F3w: list gen. broni Kazimierza Sosnkowskiego do gen. G\u0142uchowskiego (ARG/II/27) wraz z dwustronicowym za\u0142\u0105cznikiem \u201EPro Memoria\u201D (ARG/II/28\u201329), datowany 28 maja 1964 roku, Arundel, prowincja Quebec, Kanada."),
  fn(10),
  t(" Sosnkowski u\u017Cy\u0142 formu\u0142y \u201EKochany Generale.\u201D Za\u0142\u0105cznik stanowi list\u0119 24 spraw prowadzonych jednocze\u015Bnie: Jerzy Giedroyc (paryska \u201EKultura\u201D), Jan Nowak-Jeziora\u0144ski (Radio Wolna Europa), 21. rocznica \u015Bmierci gen. Sikorskiego. G\u0142uchowski zmar\u0142 czterna\u015Bcie dni p\u00F3\u017Aniej."),
]));

content.push(p([
  t("Warto\u015B\u0107 archiwalna tego zespo\u0142u dokument\u00F3w jest potr\u00F3jna: (1) stanowi jedno z ostatnich \u015Bwiadectw relacji Sosnkowski\u2013G\u0142uchowski; (2) dokumentuje siatk\u0119 kontakt\u00F3w by\u0142ego Naczelnego Wodza; (3) koresponduje z Zespo\u0142em 19 Instytutu."),
  fn(11),
]));

// ============================================================
// 7. KONTEKST ARCHIWALNY
// ============================================================
content.push(heading("7. Szerszy kontekst archiwalny: zespo\u0142y powi\u0105zane"));

content.push(p([
  t("W zasobach Instytutu Pi\u0142sudskiego zidentyfikowano pi\u0119\u0107 dalszych zasob\u00F3w bezpo\u015Brednio powi\u0105zanych z biografi\u0105 genera\u0142a: Zesp\u00F3\u0142 17 (Kmicic-Skrzy\u0144ski \u2014 drugi kawalerzysta Si\u00F3demki), Zesp\u00F3\u0142 19 (Sosnkowski \u2014 \u201Edruga strona\u201D korespondencji), Zesp\u00F3\u0142 22 (Legiony 1914\u20131918), Zesp\u00F3\u0142 23 (Wojna polsko-bolszewicka), Zesp\u00F3\u0142 201 (Zbi\u00F3r fotograficzny)."),
  fn(12),
]));

content.push(p([
  t("Fakt, \u017Ce dw\u00F3ch z siedmiu kawalerzy\u015Bt\u00F3w patrolu za\u0142o\u017Cycielskiego z\u0142o\u017Cy\u0142o swoje archiwa w tej samej instytucji \u2014 kt\u00F3r\u0105 jeden z nich wsp\u00F3\u0142za\u0142o\u017Cy\u0142 \u2014 pozwala na unikalne zestawienie: rekonstrukcj\u0119 historii Si\u00F3demki z dw\u00F3ch perspektyw osobistych."),
  fn(13),
]));

// ============================================================
// 8. NOWA SEKCJA: ODKRYCIA FOTOGRAFICZNE
// ============================================================
content.push(new Paragraph({ children: [new PageBreak()] }));
content.push(heading("8. Odkrycia z analizy fotograficznej"));

content.push(p([
  t("W marcu 2026 roku przeprowadzono szczeg\u00F3\u0142ow\u0105 analiz\u0119 121 fotografii ze zbioru ARG, pochodz\u0105cych z czterech sesji skanowania. Zdj\u0119cia zosta\u0142y uporz\u0105dkowane w dziesi\u0119\u0107 rozdzia\u0142\u00F3w biograficznych \u2014 od Legion\u00F3w (1914) po \u017Cycie powojenne w Londynie. Analiza ujawni\u0142a kilka odkry\u0107 o potencjalnym znaczeniu \u017Ar\u00F3d\u0142owym."),
  fn(14),
]));

content.push(heading("8.1. Gibraltar: Sikorski, Klimecki i G\u0142uchowski na jednym zdj\u0119ciu", HeadingLevel.HEADING_2));

content.push(p([
  t("Fotografia sup_p06_007 przedstawia trzech genera\u0142\u00F3w: W\u0142adys\u0142awa Sikorskiego (Naczelny W\u00F3dz i Premier), Bronis\u0142awa Klimeckiego (szef Sztabu Naczelnego Wodza) oraz Janusza G\u0142uchowskiego, uj\u0119tych podczas inspekcji jednostek polskich w Szkocji, prawdopodobnie na prze\u0142omie 1942/1943 roku. Sikorski i Klimecki zgin\u0119li w katastrofie gibraltarskiej 4 lipca 1943 roku."),
  fn(15),
  t(" Zdj\u0119cie dokumentuje bezpo\u015Bredni kontakt G\u0142uchowskiego z obiema ofiarami na kilka miesi\u0119cy przed katastref\u0105 i rodzi pytanie o zakres jego wiedzy o okoliczno\u015Bciach lotu."),
]));

content.push(heading("8.2. Fotograf \u201EPrytys\u201D: nieznane archiwum wizualne PSZ", HeadingLevel.HEADING_2));

content.push(p([
  t("Na rewersach wielu zdj\u0119\u0107 widniej\u0105 numery serii WSF (War Services Fund?), si\u0119gaj\u0105ce od N\u00B0888 do N\u00B09840+. Systematyczna numeracja wskazuje na istnienie "),
  tb("tysi\u0119cy"),
  t(" negatyw\u00F3w. Na jednym ze zdj\u0119\u0107 widoczny jest oficer z aparatem fotograficznym na szyi \u2014 prawdopodobnie sam Prytys. Je\u015Bli archiwum to zachowa\u0142o si\u0119, mo\u017Ce stanowi\u0107 "),
  tb("najwi\u0119kszy nieznany zbi\u00F3r dokumentacji wizualnej PSZ na Zachodzie"),
  t("."),
]));

content.push(heading("8.3. Wyzwolenie obozu kobiet w Holandii", HeadingLevel.HEADING_2));

content.push(p([
  t("Osiem zdj\u0119\u0107 serii WSF dokumentuje moment wyzwolenia obozu kobiet w Holandii (kwiecie\u0144 1945 r.). Fotografie pokazuj\u0105 chaos momentu zero: otwart\u0105 bram\u0119, kobiety w ruchu, mieszank\u0119 mundur\u00F3w i cywilnych ubra\u0144, niemowl\u0119 w ramionach matki. Na jednym ze zdj\u0119\u0107 widoczny jest raport ppor. Milewskiej o warunkach w obozie \u2014 je\u015Bli jest to jedyna kobieta-oficer raportuj\u0105ca z wyzwolenia, stanowi posta\u0107 nieznan\u0105 historiografii."),
  fn(16),
]));

content.push(heading("8.4. Czeski genera\u0142 Janou\u0161ek w\u015Br\u00F3d Polak\u00F3w", HeadingLevel.HEADING_2));

content.push(p([
  t("Zdj\u0119cie v2_p12_033 przedstawia genera\u0142a Karela Janou\u0161ka, dow\u00F3dc\u0119 czeskiego lotnictwa w RAF, w\u015Br\u00F3d polskich oficer\u00F3w w Szkocji. Wsp\u00F3\u0142praca czesko-polska na szczeblu dowodzenia w Szkocji jest s\u0142abo udokumentowana. Zdj\u0119cie jest dowodem bezpo\u015Bredniego kontaktu mi\u0119dzysojuszniczego."),
]));

content.push(heading("8.5. Polskie poci\u0105gi pancerne na brytyjskich torach", HeadingLevel.HEADING_2));

content.push(p([
  t("Fotografie sup_p23_034 i sup_p24_037 dokumentuj\u0105 polskie poci\u0105gi pancerne stacjonuj\u0105ce w Szkocji \u2014 fakt ma\u0142o znany w standardowych opracowaniach. Zdj\u0119cia pokazuj\u0105 lokomotyw\u0119 z polskimi \u017Co\u0142nierzami i stanowi\u0105 dow\u00F3d na operacyjn\u0105 zdolno\u015B\u0107 pancern\u0105 PSZ na terenie Wielkiej Brytanii."),
]));

content.push(heading("8.6. Skala polskiej obecno\u015Bci wojskowej w Szkocji", HeadingLevel.HEADING_2));

content.push(p([
  t("Suma 121 fotografii dokumentuje infrastruktur\u0119 wojskow\u0105 znacznie przekraczaj\u0105c\u0105 obraz znany z podr\u0119cznik\u00F3w: Szko\u0142a Podchor\u0105\u017Cych, 10. Brygada Kawalerii, poci\u0105gi pancerne, Zjazdy Kawaleryjskie z setkami oficer\u00F3w, pe\u0142na infrastruktura z kasynem, \u0142azaretem, kaplic\u0105. Wizyty najwy\u017Cszych w\u0142adz RP (Sikorski, Raczkiewicz, Anders, B\u00F3r-Komorowski, Arciszewski, Kopa\u0144ski) \u015Bwiadcz\u0105 o strategicznym znaczeniu tych jednostek."),
]));

// ============================================================
// 9. INSTYTUT JAKO ARCHIWUM
// ============================================================
content.push(heading("9. Instytut jako archiwum i pami\u0119\u0107: rola G\u0142uchowskiego-za\u0142o\u017Cyciela"));

content.push(p([
  t("Przypadek G\u0142uchowskiego jest archiwoznawczo wyj\u0105tkowy: tw\u00F3rca zespo\u0142u (Zesp. 70) by\u0142 jednocze\u015Bnie wsp\u00F3\u0142tw\u00F3rc\u0105 instytucji przechowuj\u0105cej ten zesp\u00F3\u0142. Ta podw\u00F3jna rola \u2014 depozytariusza i za\u0142o\u017Cyciela \u2014 rodzi pytanie o \u015Bwiadomo\u015B\u0107 archiwistyczn\u0105: Zesp\u00F3\u0142 70 ma charakter wyra\u017Anie urz\u0119dowy, podczas gdy w rodzinie pozosta\u0142y dokumenty osobiste. Ten \u015Bwiadomy podzia\u0142 jest sam w sobie \u017Ar\u00F3d\u0142em informacji o mentalno\u015Bci archiwalnej tw\u00F3rcy zespo\u0142u."),
]));

// ============================================================
// 10. WNIOSKI
// ============================================================
content.push(heading("10. Wnioski"));

content.push(p([
  tb("1. "),
  t("Oba zbiory s\u0105 "),
  tb("komplementarne, nie konkurencyjne"),
  t(". Zesp\u00F3\u0142 70 (9 jednostek) dokumentuje karier\u0119 oficjaln\u0105. Kolekcja ARG (311 jednostek) dokumentuje \u017Cycie prywatne, relacje osobiste i kontekst rodzinny. Dopiero po\u0142\u0105czenie obu pozwala zrekonstruowa\u0107 pe\u0142n\u0105 biografi\u0119 archiwalnl\u0105."),
]));

content.push(p([
  tb("2. "),
  t("Kolekcja ARG zawiera "),
  tb("dokumenty o najwy\u017Cszej warto\u015Bci \u017Ar\u00F3d\u0142owej"),
  t(": korespondencja Sosnkowskiego z \u201EPro Memoria\u201D (ARG/II/27\u201329), list marsza\u0142ka \u015Amig\u0142ego-Rydza (ARG/II/14), oryginalny dyplom Orderu Gwiazdy Rumunii (ARG/II/16), fotokopia Si\u00F3demki Beliny z podpisami (ARG/II/2)."),
]));

content.push(p([
  tb("3. "),
  tb("Wielopokoleniowy charakter kolekcji ARG"),
  t(" (5 os\u00F3b w 6 seriach) daje jej warto\u015B\u0107 niedost\u0119pn\u0105 z poziomu Zespo\u0142u 70. Rodzina G\u0142uchowskich stanowi mikrohistori\u0119 polskiego XX wieku."),
]));

content.push(p([
  tb("4. "),
  t("Analiza 121 fotografii ujawni\u0142a "),
  tb("nowe \u017Ar\u00F3d\u0142a"),
  t(": zdj\u0119cie Sikorski\u2013Klimecki\u2013G\u0142uchowski z kontekstem gibraltarskim, archiwum fotografa Prytys, dokumentacj\u0119 wyzwolenia obozu kobiet w Holandii, polskie poci\u0105gi pancerne w Szkocji oraz wsp\u00F3\u0142prac\u0119 czesko-polsk\u0105 na szczeblu dowodzenia."),
]));

content.push(p([
  tb("5. "),
  tb("Postulat badawczy: "),
  t("Wskazane jest przeprowadzenie pe\u0142nej kwerendy w Zespo\u0142ach 17 i 19 Instytutu Pi\u0142sudskiego, identyfikacja fotografa Prytys i lokalizacja reszty archiwum WSF, a tak\u017Ce ustalenie to\u017Csamo\u015Bci ppor. Milewskiej \u2014 potencjalnie nieznanej postaci z wyzwolenia oboz\u00F3w."),
]));

// ============================================================
// BIBLIOGRAFIA
// ============================================================
content.push(new Paragraph({ children: [new PageBreak()] }));
content.push(heading("Bibliografia"));

content.push(heading("I. \u0179r\u00F3d\u0142a archiwalne", HeadingLevel.HEADING_2));
const bibSrc = [
  "Kolekcja prywatna ARG \u2014 Archiwum Rodziny G\u0142uchowskich. 311 jednostek w 6 seriach (ARG/I\u2013VI). Skatalogowane w standardzie ISAD(G), 2026.",
  "Instytut J\u00F3zefa Pi\u0142sudskiego w Londynie, Zesp\u00F3\u0142 17 \u2014 Archiwum Ludwika Kmicic-Skrzy\u0144skiego. 8 jednostek.",
  "Instytut J\u00F3zefa Pi\u0142sudskiego w Londynie, Zesp\u00F3\u0142 19 \u2014 Archiwum Kazimierza Sosnkowskiego. 33 jednostki.",
  "Instytut J\u00F3zefa Pi\u0142sudskiego w Londynie, Zesp\u00F3\u0142 22 \u2014 Legiony 1914\u20131918. 120 jednostek.",
  "Instytut J\u00F3zefa Pi\u0142sudskiego w Londynie, Zesp\u00F3\u0142 23 \u2014 Wojna polsko-bolszewicka 1919\u20131920.",
  "Instytut J\u00F3zefa Pi\u0142sudskiego w Londynie, Zesp\u00F3\u0142 70 \u2014 Archiwum Janusza G\u0142uchowskiego. 9 jednostek, 1916\u20131964.",
  "Instytut J\u00F3zefa Pi\u0142sudskiego w Londynie, Zesp\u00F3\u0142 201 \u2014 Zbi\u00F3r fotograficzny.",
  "Wojskowe Biuro Historyczne, Biogram nr 76/45 (24 V 1937 r.) \u2014 gen. Janusz G\u0142uchowski.",
  "Archiwum Historii M\u00F3wionej Muzeum Powstania Warszawskiego, sygn. 1889.",
];
for (const b of bibSrc) {
  content.push(p0([t(b)], { spacing: { after: 80, line: 280 } }));
}

content.push(heading("II. Opracowania", HeadingLevel.HEADING_2));
const bibOpr = [
  ["Habielski R., ", "\u017Bycie spo\u0142eczne i kulturalne emigracji", ", Warszawa 1999."],
  ["Kry\u0144ska-\u0141owi\u0144ska M., \u201EInstytut Pi\u0142sudskiego w Londynie: geneza i dzia\u0142alno\u015B\u0107\u201D, ", "Teki Archiwalne", ", seria nowa, t. 11, 2012."],
  ["Litewski J., ", "Si\u00F3demka Beliny", ", Krak\u00F3w 1999."],
  ["Stachiewicz P., ", "Parasol. Dzieje oddzia\u0142u do zada\u0144 specjalnych Kedywu KG AK", ", Warszawa 1984."],
  ["Wro\u0144ski T., ", "Kronika Powstania Warszawskiego", ", Warszawa 2004."],
];
for (const [pre, title, post] of bibOpr) {
  content.push(p0([t(pre), ti(title), t(post)], { spacing: { after: 80, line: 280 } }));
}

content.push(heading("III. Portale i bazy danych", HeadingLevel.HEADING_2));
const bibWeb = [
  "Instytut J\u00F3zefa Pi\u0142sudskiego w Londynie \u2014 katalog zbior\u00F3w: pilsudski.org.uk/pl/katalog.php",
  "Instytut Pami\u0119ci Narodowej \u2014 baza biogramowa: ipn.gov.pl",
  "Encyklopedia PWN: encyklopedia.pwn.pl/haslo/Gluchowski-Janusz;3906169.html",
  "Muzeum Powstania Warszawskiego \u2014 biogramy: 1944.pl",
  "Naczelna Dyrekcja Archiw\u00F3w Pa\u0144stwowych: szukajwarchiwach.gov.pl (SEZAM/IZA, nr 709)",
];
for (const b of bibWeb) {
  content.push(p0([t(b)], { spacing: { after: 80, line: 280 } }));
}

// ============================================================
// NOTA BIOGRAFICZNA AUTORA
// ============================================================
content.push(new Paragraph({ spacing: { before: 600 }, border: { top: { style: BorderStyle.SINGLE, size: 6, color: "999999", space: 8 } }, children: [] }));
content.push(p0([
  tb("Nota o autorze: ", { size: SZ_SMALL }),
  ts("Marek Skonieczny \u2014 badacz niezale\u017Cny, specjalizacja: archiwistyka polskiej emigracji wojskowej i kawaleria polska XX wieku. Autor katalogu kolekcji ARG (311 jednostek, standard ISAD(G)). Adres korespondencyjny: Warszawa \u2013 Rio de Janeiro. E-mail: skorek2000@yahoo.com."),
]));

// ============================================================
// BUILD DOCUMENT
// ============================================================
const doc = new Document({
  styles: {
    default: {
      document: {
        run: { font: FONT, size: SZ },
      },
    },
    paragraphStyles: [
      {
        id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: SZ_H1, bold: true, font: FONT },
        paragraph: { spacing: { before: 400, after: 200 }, outlineLevel: 0 },
      },
      {
        id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: SZ_H2, bold: true, font: FONT },
        paragraph: { spacing: { before: 300, after: 160 }, outlineLevel: 1 },
      },
    ],
  },
  footnotes,
  sections: [{
    properties: {
      page: {
        size: { width: 11906, height: 16838 }, // A4
        margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 }, // 2.54 cm
      },
    },
    headers: {
      default: new Header({
        children: [new Paragraph({
          alignment: AlignmentType.RIGHT,
          children: [new TextRun({ text: "M. Skonieczny \u2014 Od Si\u00F3demki Beliny do Instytutu Pi\u0142sudskiego", font: FONT, size: 16, color: "999999", italics: true })],
        })],
      }),
    },
    footers: {
      default: new Footer({
        children: [new Paragraph({
          alignment: AlignmentType.CENTER,
          children: [new TextRun({ children: [PageNumber.CURRENT], font: FONT, size: 18 })],
        })],
      }),
    },
    children: content,
  }],
});

Packer.toBuffer(doc).then(buffer => {
  const outPath = "C:\\Users\\skore\\Downloads\\artykul_zespol_70_v2.docx";
  fs.writeFileSync(outPath, buffer);
  console.log(`OK: ${outPath} (${(buffer.length / 1024).toFixed(0)} KB)`);
}).catch(err => {
  console.error("ERROR:", err.message);
  process.exit(1);
});
