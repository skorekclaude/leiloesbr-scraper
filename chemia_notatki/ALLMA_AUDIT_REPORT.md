# ALLMA -- Raport Audytu Kodu

**Data:** 2026-02-19
**Audytor:** Claude Opus 4.6
**Projekt:** ALLMA -- AI Psychology Coach
**Repo:** C:\Users\skore\allma (github.com/skore/allma)
**Stack:** Bun + TypeScript, Supabase, Anthropic Claude / Groq Llama, Telegram Bot, Web Chat (SSE)

---

## 1. Status Ogolny

### Architektura
- **16 plikow TypeScript** w `src/` (dobrze zorganizowane w core/, agents/, integrations/, tools/)
- **6 plikow frontendowych** w `web/` (index.html, chat.html, guide.html, privacy.html, terms.html, admin.html + assets)
- **8 promptow specjalistow** w `prompts/` (allma-coach.md, relations.md, career.md, body.md, mindfulness.md, habits.md, shadow.md, nutrition.md)
- **PWA Support:** manifest.json, service-worker.js, offline.html, ikony (72-512px + maskable)
- **Deploy:** Dockerfile dla Railway, PM2 lokalnie (`allma-coach`)

### Komponenty Dzialajace
- Web server (Bun.serve) na porcie 3456
- SSE streaming chat z Anthropic Claude / Groq fallback
- Telegram bot (long-polling) z transkrypcja glosowa (Groq Whisper)
- 8 agentow z keyword-based auto-routingiem
- System pamieci (Supabase: allma_users, allma_memory, allma_messages)
- Detekcja kryzysu (7 jezykow, high/medium severity)
- OTP email (Resend.com) -- gotowe, ale wylaczone (czeka na domena)
- Stripe webhooks (checkout, payment failed, subscription deleted)
- Admin dashboard (/admin?key=...)
- Self-learning pipeline (daily research + insight extraction)
- Session cleanup (co 15 min), rate limiting (15 msg/min), session limits (25 msg)
- i18n: 8 jezykow (EN, PL, PT, ES, DE, FR, IT, ZH)

---

## 2. KRYTYCZNE PROBLEMY BEZPIECZENSTWA

### 2.1 KLUCZE API W PLIKU .env COMMITOWANE DO MEMORY.md
**Plik:** `C:\Users\skore\.claude\projects\...\memory\MEMORY.md`
**Waga:** KRYTYCZNA

W kontekscie MEMORY.md (ktory trafia do AI) widoczny jest pelny klucz Anthropic API:
```
ANTHROPIC_API_KEY=sk-ant-api03-GOCqUkhDai9ckig5d_Q9oxWA...
```
Jesli MEMORY.md jest pushowany do repo lub dostepny publicznie, klucze sa skompromitowane.

**Rekomendacja:** Natychmiast zrotowac ANTHROPIC_API_KEY, GROQ_API_KEY, TELEGRAM_BOT_TOKEN, i wszystkie klucze Supabase. Usunac klucze z MEMORY.md.

### 2.2 Domyslny ADMIN_KEY
**Plik:** `src/integrations/webhook-server.ts:198`
```typescript
const ADMIN_KEY = process.env.ADMIN_KEY || "allma2026";
```
Domyslny klucz admin jest hardcodowany. Kazdy kto zna URL aplikacji moze wejsc na `/admin?key=allma2026` i zobaczyc:
- Email adresy uzytkownikow (czesciowo zamaskowane, ale wciaz identyfikowalne)
- Statystyki uzytkowania
- Bledy serwera
- Rozmiar sesji

**Rekomendacja:** Ustawic silny ADMIN_KEY w zmiennych srodowiskowych Railway. Dodac rate limiting na endpoint admin.

### 2.3 CORS: Access-Control-Allow-Origin: *
**Plik:** `src/integrations/webhook-server.ts:443-449`
```typescript
function corsHeaders(): Record<string, string> {
  return {
    "Access-Control-Allow-Origin": "*",
    ...
  };
}
```
Wildcard CORS pozwala dowolnej stronie na wykonywanie requestow do API. W polaczeniu z `Access-Control-Allow-Credentials: "true"` (linia 448), jest to niebezpieczne -- przegladarki powinny blokowac te kombinacje, ale lepiej ustawic konkretna domene.

**Rekomendacja:** Ustawic `Access-Control-Allow-Origin` na domena produkcyjna (np. `https://allma-production.up.railway.app`).

### 2.4 Brak walidacji emaila przy loginie
**Plik:** `src/integrations/webhook-server.ts:541-598`
Login wymaga jedynie emaila -- brak OTP, brak hasla, brak zadnej weryfikacji. Ktokolwiek znajacy email innego uzytkownika moze sie zalogowac na jego konto.

**Status:** OTP jest gotowe w `src/integrations/email.ts`, ale wylaczone (linie 602-607: "OTP will be enabled after domain setup").

**Rekomendacja:** Wlaczyc OTP lub przynajmniej dodac rate limiting na endpoint /api/auth/login. Obecnie brak jakiejkolwiek ochrony.

### 2.5 Logowanie OTP kodow w konsoli
**Plik:** `src/integrations/email.ts:86`
```typescript
console.log(`[OTP] Code for ${normalizedEmail}: ${code}`);
```
Nawet po wlaczeniu OTP, kod jest logowany w plain text. W produkcji logi moga byc widoczne w Railway dashboard.

**Rekomendacja:** Usunac logowanie OTP kodow lub ograniczyc do trybu dev.

### 2.6 Stripe Webhook Secret pusty
**Plik:** `.env:27`
```
STRIPE_WEBHOOK_SECRET=
```
Bez webhook secret, weryfikacja podpisu Stripe jest pomijana (`webhook-server.ts:260-262`):
```typescript
if (!STRIPE_WEBHOOK_SECRET) {
    console.warn("[Webhook] No webhook secret configured — skipping verification");
    return true; // <-- AKCEPTUJE WSZYSTKO
}
```
Ktokolwiek moze sfalszyc eventy Stripe.

**Rekomendacja:** Skonfigurowac STRIPE_WEBHOOK_SECRET w Railway.

### 2.7 Path traversal -- niewystarczajaca ochrona
**Plik:** `src/integrations/webhook-server.ts:1088-1089`
```typescript
const safePath = url.pathname.replace(/\.\./g, "");
```
Replace `..` jest niewystarczajace. Atakujacy moze uzyc `%2e%2e` (URL encoding), `..%252f` (double encoding), lub `....//` (po usunieciu `..` zostaje `../`).

**Rekomendacja:** Uzyc `path.resolve()` + sprawdzic czy wynikowa sciezka zaczyna sie od WEB_DIR.

---

## 3. BUGI I PROBLEMY

### 3.1 Tools uzywaja hardcoded "default" userId
**Plik:** `src/tools/index.ts:98, 118, 130`
```typescript
const userId = "default"; // TODO: pass from context
```
Trzy toole (search_memory, add_fact, memory_read) operuja na uzytkownika "default" zamiast na aktualnego uzytkownika. Oznacza to ze agent loop nie moze poprawnie odczytywac/zapisywac pamieci per-user.

**Rekomendacja:** Przekazywac userId przez ToolContext.

### 3.2 web_search tool niezaimplementowany
**Plik:** `src/tools/index.ts:150`
```typescript
// TODO: Implement with DuckDuckGo or Perplexity Sonar
```
Tool zarejestrowany ale zwraca blad. Agent loop moze probowac go uzyc i dostac niepotrzebne errory.

### 3.3 Telegram /lang wspiera tylko 3 jezyki
**Plik:** `src/integrations/telegram.ts:170`
```typescript
if (newLang === "pt" || newLang === "pl" || newLang === "en") {
```
Frontend i system i18n wspieraja 8 jezykow, ale komenda /lang w Telegramie akceptuje tylko pt, pl, en. Brakuje es, de, fr, it, zh.

### 3.4 Telegram error messages -- brak jezykow
**Plik:** `src/integrations/telegram.ts:446-451`
```typescript
const errorMsgs: Record<Language, string> = {
    pt: "...", pl: "...", en: "...",
};
```
Tylko 3 jezyki w komunikatach bledu (i kilku innych miejscach). Brak es, de, fr, it, zh -- powoduje TypeScript error lub fallback na `undefined`.

### 3.5 Onboarding modal -- brak i18n w HTML
**Plik:** `web/chat.html:183-206`
Onboarding modal ma hardcoded angielski tekst w HTML:
```html
<h2>Welcome to ALLMA</h2>
<label>1. What brings you here today?</label>
```
JavaScript (`chat.js:1166-1189`) tlumaczy to dynamicznie, ale jest chwilowy flash angielskiego tekstu zanim JS zalaczy sie na DOM.

### 3.6 Calorie bar nie otrzymuje danych z backendu
**Plik:** `web/assets/chat.js:797-810`
Funkcja `updateCalorieBar(data)` istnieje w frontendzie, ale **nigdzie w backendzie** nie jest wywoywana ani dane kaloryczne nie sa wysylane do frontendu. Calorie bar zawsze pokazuje "0 kcal | P: 0g | C: 0g | F: 0g".

**Rekomendacja:** Backend (webhook-server.ts) powinien parsowac odpowiedzi nutrition agenta i wysylac dane kaloryczne w SSE stream, albo calorie bar powinien byc ukryty dopoki dane nie sa dostepne.

### 3.7 Duplikacja prompta jezykowego
**Pliki:** `src/integrations/webhook-server.ts:795-804` i `src/core/conversation.ts:271-279`
Identyczny `languageInstruction` Record jest zduplikowany w dwoch plikach. Zmiana w jednym nie aktualizuje drugiego.

**Rekomendacja:** Wyekstrahowac do wspolnego modulu (np. i18n.ts).

### 3.8 Chat session nie ma timestamp -- czyszczenie na slepo
**Plik:** `src/integrations/webhook-server.ts:151-158`
```typescript
// Chat sessions don't have timestamps — purge if map grows too large
if (chatSessions.size > 200) {
    const entries = [...chatSessions.entries()];
    chatSessions.clear();
    entries.slice(-100).forEach(([k, v]) => chatSessions.set(k, v));
```
Komentarz sam mowi ze sesje czatu nie maja timestampow. Czyszczenie opiera sie na pozycji w Map (ktora w JS jest Insert order), wiec "ostatnie 100" to te dodane najpozniej, niekoniecznie najaktywniejsze.

**Rekomendacja:** Dodac `lastActivity: number` do UserSession i sortowac po nim.

### 3.9 Index.ts sprawdza tylko GROQ_API_KEY
**Plik:** `src/index.ts:38`
```typescript
const required = ["GROQ_API_KEY"];
```
Jesli backend to "anthropic", GROQ_API_KEY jest technicznie niepotrzebny. Ale ANTHROPIC_API_KEY nie jest sprawdzany na starcie. Bot wystartuje bez bledu nawet z pustym kluczem Anthropic, a bledy pojawia sie dopiero przy pierwszym requeście.

### 3.10 Brak prompta data/knowledge.md w Dockerfile
**Plik:** Dockerfile
```
COPY data/ data/
```
Katalog `data/` zawiera `knowledge.md` (self-learning knowledge base). Jest kopiowany, ale jesli plik nie istnieje (clean build), `self-learning.ts` moze rzucic blad. Na szczescie kod prawdopodobnie obsluguje brakujacy plik gracefully -- do weryfikacji w `src/core/self-learning.ts`.

---

## 4. BRAKUJACE FUNKCJONALNOSCI / NIEKOMPLETNE IMPLEMENTACJE

### 4.1 OTP Auth -- wymagana domena
Endpoint `/api/auth/send-otp` i `/api/auth/verify-otp` zwracaja 410 Gone. OTP czeka na konfiguracje domeny z Resend.com. Bez OTP, logowanie jest otwarte.

### 4.2 Calorie bar data pipeline
Frontend ma `updateCalorieBar()` ale backend nie parsuje danych z nutrition agenta. Caly calorie bar jest dekoracyjny.

### 4.3 Telegram-Web Linking
Brak mechanizmu laczenia konta Telegram z kontem Web (ten sam uzytkownik, rozne platfromy). Web uzywa emaila, Telegram uzywa telegram_id. Negative sentinel telegram_id dla web users to workaround, nie rozwiazanie.

### 4.4 /delete_my_data -- niekompletne
**Plik:** `src/integrations/telegram.ts:161-164`
```typescript
if (cmd === "delete_my_data") {
    await sendMessage(chatId, "Data deletion requested. Use /start to begin fresh.");
    sessions.delete(sessionKey);
    return;
}
```
Komenda nie kasuje danych z Supabase (allma_memory, allma_messages, allma_users). Usuwa tylko sesje in-memory. Uzytkownik moze myslic ze jego dane zostaly skasowane, gdy w rzeczywistosci sa nadal w bazie.

**Waga:** SREDNIA-WYSOKA (naruszenie obietnic RODO/GDPR skladanych na landing page)

### 4.5 Session limit warning -- brak i18n
**Plik:** `src/core/safety.ts:158-166`
Wiadomosci o limicie sesji sa tylko po angielsku:
```typescript
warning: "Session limit reached. Take a break and reflect."
```

### 4.6 Privacy.html i Terms.html -- nieznana zawartosc
Pliki istnieja ale nie zostaly w pelni sprawdzone pod katem zgodnosci RODO/LGPD. Landing page obiecuje:
- "AES-256 encrypted" -- czy to prawda? Supabase uzywa TLS, ale dane at-rest?
- "Never used to train AI" -- dane ida do Anthropic/Groq API, ich polityka moze byc inna
- "GDPR-compliant" -- /delete_my_data nie kasuje danych z bazy

### 4.7 Brak testow
`package.json` ma `"test": "bun test"`, ale brak jakichkolwiek plikow testowych w projekcie. Zero testow jednostkowych, integracyjnych, E2E.

---

## 5. POTENCJALNE PROBLEMY WYDAJNOSCIOWE

### 5.1 Ogromna lista keywordow nutrition
**Plik:** `src/agents/registry.ts:267-377`
Agent nutrition ma ponad 400 keywordow (wlaczajac nazwy polskich dan, skladnikow, napojow). Kazda wiadomosc jest porownywana z kazdy keywordem za pomoca `string.includes()`. Dla dlugich wiadomosci to setki operacji.

**Rekomendacja:** Rozwazyc uzycie Set lub trie data structure dla szybszego dopasowania. Albo przynajmniej wczesne wyjscie jesli juz znaleziono wysoki wynik.

### 5.2 Brak limitowania kontekstu LLM w streaming
**Plik:** `src/integrations/webhook-server.ts:760-814`
W endpoincie `/api/chat/stream`, historia sesji jest wlaczana bezposrednio do wiadomosci LLM bez limitowania rozmiaru. Jesli uzytkownik ma dluga sesje, prompt moze przekroczyc limity tokenow.

Conversation.ts (handleConversation) ma to obslugzone (trimowanie do 20 wiadomosci), ale streaming endpoint robi to niezaleznie i mniej agresywnie.

### 5.3 Memory leaks -- in-memory stores
Trzy mapy w pamięci bez hard limit:
- `webSessions` (webhook-server.ts) -- czyszczone co 15 min, max 7 dni
- `rateLimits` (webhook-server.ts) -- czyszczone co 5 min
- `otpStore` (email.ts) -- czyszczone co 5 min

Plus w telegram.ts:
- `sessions` -- nigdy nie czyszczone (uzytkownik moze sie nie odezwac wiecej)
- `userChatIds` -- nigdy nie czyszczone

**Rekomendacja:** Dodac czyszczenie dla sesji Telegram (np. po 24h braku aktywnosci).

---

## 6. SUGESTIE DOTYCZACE JAKOSCI KODU

### 6.1 Duplikacja kodu
- `languageInstruction` -- zduplikowany w webhook-server.ts i conversation.ts
- `teamContext` -- zduplikowany w webhook-server.ts i conversation.ts
- Format emocji (`detectEmotion`) -- tylko w webhook-server.ts, nie uzyty w Telegram
- Specialist routing logic -- prawie identyczna w webhook-server.ts i conversation.ts

**Rekomendacja:** Wyekstrahowac wspollny modul `src/core/prompt-builder.ts`.

### 6.2 Brak typow TypeScript w kilku miejscach
- `(await res.json()) as Record<string, any>` -- czeste w Stripe, Telegram
- `any` casts w webhook handlerach

### 6.3 Logowanie endpointu admin z kluczem
**Plik:** `src/integrations/webhook-server.ts:1160`
```typescript
console.log(`[Web] Admin:   http://localhost:${server.port}/admin?key=${ADMIN_KEY}`);
```
Klucz admin jest logowany do stdout przy starcie serwera.

---

## 7. OCENA OGOLNA

| Aspekt | Ocena | Komentarz |
|--------|-------|-----------|
| Architektura | 8/10 | Czysta separacja concerns, dobry podzia plikow |
| Bezpieczenstwo | 4/10 | Otwarte logowanie, domyslne klucze, brak OTP |
| Frontend | 7/10 | Ladny UI, PWA support, i18n 8 jezykow |
| Backend | 7/10 | Solidny streaming, dual LLM backend, safety system |
| Testy | 0/10 | Brak testow |
| Dokumentacja | 6/10 | Komentarze w kodzie dobre, brak README |
| Deploy | 7/10 | Dockerfile OK, healthcheck, Railway ready |
| i18n | 8/10 | 8 jezykow, ale Telegram obsluguje tylko 3 |

### Priorytety Naprawy
1. **NATYCHMIAST:** Zrotowac wszystkie klucze API (wyciekly do MEMORY.md)
2. **NATYCHMIAST:** Ustawic silny ADMIN_KEY w Railway
3. **WYSOKI:** Wlaczyc OTP lub dodac rate limiting na login
4. **WYSOKI:** Naprawic CORS (zamienic * na domene produkcyjna)
5. **WYSOKI:** Implementowac prawdziwe usuwanie danych w /delete_my_data
6. **SREDNI:** Naprawic tools userId "default"
7. **SREDNI:** Dodac brakujace jezyki do Telegram /lang
8. **NISKI:** Refaktoryzacja duplikacji kodu
9. **NISKI:** Dodac calorie bar data pipeline

---

*Raport wygenerowany automatycznie przez Claude Opus 4.6 na podstawie analizy 16 plikow TypeScript, 6 plikow frontendowych, Dockerfile, .env i package.json.*
