import requests
from bs4 import BeautifulSoup
import urllib3
import sys

sys.stdout.reconfigure(encoding='utf-8')
urllib3.disable_warnings()

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

for path in ['notice-news-press-release.php', 'examination-notice.php', 'notice.php']:
    url = f'https://nu.ac.bd/{path}'
    try:
        r = requests.get(url, headers=headers, verify=False, timeout=10)
        print(f"Path: {path} -> Status: {r.status_code}")
        if r.status_code == 200:
            soup = BeautifulSoup(r.text, 'html.parser')
            for a in soup.find_all('a', href=True):
                txt = a.get_text(" ", strip=True)
                href = a['href']
                if any(w in txt for w in ['ডিগ্রি', 'degree', '১ম বর্ষ', 'সময়সূচি', 'রুটিন']) or any(w in href for w in ['degree', 'routine']):
                    print(f"   {txt[:60]} -> {href}")
    except Exception as e:
        print(f"Path {path} err:", e)
