import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from datetime import datetime
import time

ARTISTS = [
    "Wyspianski", "Malczewski", "Matejko", "Beksinski", "Witkacy",
    "Lempicka", "Abakanowicz", "Szapocznikow", "Kantor", "Mitoraj",
    "Chelmonski", "Gierymski", "Mehoffer", "Kossak", "Brandt",
    "Siemiradzki", "Sienkiewicz", "Conrad", "Milosz", "Szymborska",
    "Nowosielski", "Strzemiński", "Kobro", "Stryjenska", "Nikifor"
]

print("=" * 70)
print("LEILOESBR POLISH ARTISTS SCRAPER - PEŁNA WERSJA")
print("=" * 70)
print(f"Cel: 871 stron (~109,701 lotów)")
print(f"Szukam: {len(ARTISTS)} polskich artystów")
print(f"Start: {datetime.now().strftime('%H:%M:%S')}")
print("=" * 70)
print()

session = requests.Session()
session.headers.update({'User-Agent': 'Mozilla/5.0'})
all_matches = []
total_lots = 0
start_time = time.time()

for page in range(1, 872):  # WSZYSTKIE 871 STRON
    url = f"https://www.leiloesbr.com.br/busca_andamento.asp?pesquisa=&op=1&v=126&tp=|&b=0&pag={page}"
    
    try:
        response = session.get(url, timeout=15)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a', href=re.compile(r'abre_catalogo'))
        total_lots += len(links)
        
        for link in links:
            title = link.get_text(strip=True)
            for artist in ARTISTS:
                if artist.lower() in title.lower():
                    print(f"\n🎯 MATCH! Strona {page}: {artist}")
                    print(f"   '{title[:65]}...'")
                    all_matches.append({
                        'artist': artist,
                        'title': title,
                        'url': link.get('href', ''),
                        'page': page
                    })
                    break
        
        # Postęp co 50 stron
        if page % 50 == 0:
            elapsed = (time.time() - start_time) / 60
            rate = page / elapsed if elapsed > 0 else 0
            remaining = (871 - page) / rate if rate > 0 else 0
            print(f"\n📊 Postęp: {page}/871 ({page/871*100:.1f}%)")
            print(f"   Loty: {total_lots:,} | Znaleziono: {len(all_matches)}")
            print(f"   Czas: {elapsed:.1f}min | Pozostało: ~{remaining:.0f}min")
        
        time.sleep(0.5)  # Bezpieczna przerwa
        
    except Exception as e:
        print(f"\n⚠️ Błąd strona {page}: {e}")
        time.sleep(2)

# PODSUMOWANIE
print("\n" + "=" * 70)
print("ZAKOŃCZONO!")
print("=" * 70)
print(f"Przeskanowano: {871} stron")
print(f"Sprawdzono: {total_lots:,} lotów")
print(f"Znaleziono: {len(all_matches)} polskich dzieł")
print(f"Czas: {(time.time()-start_time)/60:.1f} minut")
print("=" * 70)

if all_matches:
    df = pd.DataFrame(all_matches)
    filename = f'polskie_dziela_leiloesbr_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'
    df.to_csv(filename, index=False, encoding='utf-8-sig')
    print(f"\n✅ Zapisano do: {filename}")
    print("\nZnalezione dzieła:")
    for i, match in enumerate(all_matches, 1):
        print(f"{i}. {match['artist']}: {match['title'][:60]}...")
else:
    print("\n⚠️ Nie znaleziono polskich artystów")

print("\n" + "=" * 70)
input("Enter aby zakończyć...")
