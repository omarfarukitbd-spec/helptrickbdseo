import sys
try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass
import requests
from bs4 import BeautifulSoup

def main():
    r = requests.get('https://dhakaeducationboard.gov.bd/', verify=False)
    soup = BeautifulSoup(r.text, 'html.parser')
    print("=== DHAKA EDUCATION BOARD LINKS ===")
    for a in soup.find_all('a'):
        t = a.get_text(strip=True)
        h = a.get('href', '')
        if any(k in t for k in ['সংশোধন', 'সেবা', 'আবেদন', 'ফরম', 'Online', 'e-File', 'সনদ']):
            print(f"{t} -> {h}")

    print("\n=== EFILE DHAKA LINKS ===")
    r2 = requests.get('https://efile.dhakaeducationboard.gov.bd/', verify=False)
    soup2 = BeautifulSoup(r2.text, 'html.parser')
    for a in soup2.find_all('a'):
        t = a.get_text(strip=True)
        h = a.get('href', '')
        print(f"{t} -> {h}")
    for btn in soup2.find_all(['button', 'input']):
        print(f"BUTTON/INPUT: {btn}")

if __name__ == '__main__':
    main()
