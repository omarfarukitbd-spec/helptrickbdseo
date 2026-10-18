import requests
from bs4 import BeautifulSoup
import urllib3
import sys

sys.stdout.reconfigure(encoding='utf-8')
urllib3.disable_warnings()

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

url = 'https://nu.ac.bd'
try:
    r = requests.get(url, headers=headers, verify=False, timeout=15)
    soup = BeautifulSoup(r.text, 'html.parser')
    for a in soup.find_all('a', href=True):
        href = a['href']
        txt = a.get_text(" ", strip=True)
        if any(w in txt for w in ['ডিগ্রি', 'degree', 'নোটিশ', 'Notice', 'পরীক্ষা', 'রুটিন']) or any(w in href.lower() for w in ['notice', 'degree', 'routine', '.pdf']):
            print(f"TXT: {txt[:50]} | HREF: {href}")
except Exception as e:
    print("Error:", e)
