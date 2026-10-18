import requests
from bs4 import BeautifulSoup
import urllib3
import sys

sys.stdout.reconfigure(encoding='utf-8')
urllib3.disable_warnings()

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

for page in ['recent-news-notice.php', 'examination-notice.php']:
    url = f'https://nu.ac.bd/{page}'
    print(f"\n=== FETCHING: {url} ===")
    try:
        r = requests.get(url, headers=headers, verify=False, timeout=15)
        soup = BeautifulSoup(r.text, 'html.parser')
        rows = soup.find_all('tr')
        print(f"Total rows found: {len(rows)}")
        for tr in rows[:40]: # First 40 rows
            txt = tr.get_text(" ", strip=True)
            links = [a['href'] for a in tr.find_all('a', href=True)]
            if links:
                print(f"{txt} -> {links}")
    except Exception as e:
        print(f"Error on {page}:", e)
