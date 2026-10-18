import requests
from bs4 import BeautifulSoup
import urllib3
import sys

sys.stdout.reconfigure(encoding='utf-8')
urllib3.disable_warnings()

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

url = 'https://nu.ac.bd/examination-notice.php'
r = requests.get(url, headers=headers, verify=False, timeout=15)
soup = BeautifulSoup(r.text, 'html.parser')
for tr in soup.find_all('tr'):
    if '১৮/১০/২০২৬' in tr.text or 'ডিগ্রি (পাস)' in tr.text:
        print(tr.prettify())
        print("---")
