import requests
from bs4 import BeautifulSoup
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

print("=== 1. CHECKING DHAKA BOARD ===")
try:
    r = requests.get('https://dhakaeducationboard.gov.bd/', timeout=10, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    for a in soup.find_all('a', href=True):
        href = a['href']
        text = a.get_text().strip()
        if '.pdf' in href.lower() or 'notice' in href.lower() or 'ssc' in href.lower():
            if any(k in text.lower() for k in ['এসএসসি', '২০২৭', 'ফরম', 'রুটিন', 'পরীক্ষা']):
                print(f"Dhaka Board: {text} -> {href}")
except Exception as e:
    print("Dhaka Board err:", e)

print("\n=== 2. CHECKING NATIONAL UNIVERSITY ===")
try:
    r = requests.get('http://www.nu.ac.bd/recent-notices.php', timeout=10, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    for a in soup.find_all('a', href=True):
        href = a['href']
        text = a.get_text().strip()
        if any(k in text.lower() for k in ['ডিগ্রি', 'degree', '১ম বর্ষ', 'স্থগিত', 'রুটিন']):
            print(f"NU: {text} -> {href}")
except Exception as e:
    print("NU err:", e)

print("\n=== 3. CHECKING DPE (DIRECTORATE OF PRIMARY EDUCATION) ===")
try:
    r = requests.get('http://www.dpe.gov.bd/site/view/notices', timeout=10, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    for a in soup.find_all('a', href=True):
        href = a['href']
        text = a.get_text().strip()
        if any(k in text.lower() for k in ['বৃত্তি', 'scholarship', 'প্রাথমিক', 'রুটিন']):
            print(f"DPE: {text} -> {href}")
except Exception as e:
    print("DPE err:", e)
