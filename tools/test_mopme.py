import requests
from bs4 import BeautifulSoup
import urllib3
import sys

sys.stdout.reconfigure(encoding='utf-8')
urllib3.disable_warnings()

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
url = 'https://mopme.gov.bd/pages/policies/%E0%A6%AA%E0%A7%8D%E0%A6%B0%E0%A6%BE%E0%A6%A5%E0%A6%AE%E0%A6%BF%E0%A6%95-%E0%A6%AC%E0%A7%83%E0%A6%A4%E0%A7%8D%E0%A6%A4%E0%A6%BF-%E0%A6%AA%E0%A6%B0%E0%A7%80%E0%A6%95%E0%A7%8D%E0%A6%B7%E0%A6%BE-%E0%A6%A8%E0%A7%80%E0%A6%A4%E0%A6%BF%E0%A6%AE%E0%A6%BE%E0%A6%B2%E0%A6%BE-%E0%A7%A8%E0%A7%A6%E0%A7%A8%E0%A7%AC-63kvuk-69ae8a047706b1acf8d9e615'

try:
    r = requests.get(url, headers=headers, verify=False, timeout=15)
    print("Status:", r.status_code)
    soup = BeautifulSoup(r.text, 'html.parser')
    for a in soup.find_all('a', href=True):
        if '.pdf' in a['href'].lower() or 'download' in a['href'].lower() or 'file' in a['href'].lower():
            print(f"{a.get_text(strip=True)} -> {a['href']}")
    # print iframes
    for ifr in soup.find_all('iframe', src=True):
        print("Iframe:", ifr['src'])
except Exception as e:
    print("Error:", e)
