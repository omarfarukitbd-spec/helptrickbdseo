import requests
from bs4 import BeautifulSoup
import urllib3
import sys

sys.stdout.reconfigure(encoding='utf-8')
urllib3.disable_warnings()

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

url = 'https://dhakaeducationboard.gov.bd/index.php/site/product/ssccorner'
try:
    r = requests.get(url, headers=headers, verify=False, timeout=15)
    soup = BeautifulSoup(r.text, 'html.parser')
    rows = soup.find_all('tr')
    print(f"Total rows: {len(rows)}")
    for tr in rows[:35]: # First 35 rows
        text = tr.get_text(" ", strip=True)
        links = [a['href'] for a in tr.find_all('a', href=True)]
        if links:
            print(f"{text} -> {links}")
except Exception as e:
    print("Error:", e)
