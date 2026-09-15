import requests
from bs4 import BeautifulSoup
import subprocess
import os

def main():
    r = requests.get('https://dhakaeducationboard.gov.bd/', verify=False)
    html = r.text

    # Make asset URLs absolute
    soup = BeautifulSoup(html, 'html.parser')
    for tag in soup.find_all(['link', 'script', 'img']):
        if tag.name == 'link' and tag.get('href'):
            if tag['href'].startswith('/'):
                tag['href'] = 'https://dhakaeducationboard.gov.bd' + tag['href']
        elif tag.name == 'script' and tag.get('src'):
            if tag['src'].startswith('/'):
                tag['src'] = 'https://dhakaeducationboard.gov.bd' + tag['src']
        elif tag.name == 'img' and tag.get('src'):
            if tag['src'].startswith('/'):
                tag['src'] = 'https://dhakaeducationboard.gov.bd' + tag['src']

    # Remove modal popup
    for m in soup.find_all(class_=lambda c: c and ('modal' in c or 'popup' in c)):
        m.decompose()
    for b in soup.find_all(class_=lambda c: c and 'backdrop' in c):
        b.decompose()

    clean_file = os.path.abspath('dhaka_board_clean.html')
    with open(clean_file, 'w', encoding='utf-8') as f:
        f.write(str(soup))

    chrome = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    abs_out = os.path.abspath('dhaka_board_no_modal.png')
    cmd = [
        chrome,
        '--headless=new',
        '--disable-gpu',
        '--virtual-time-budget=5000',
        '--window-size=1280,900',
        f'--screenshot={abs_out}',
        f'file:///{clean_file.replace(os.sep, "/")}'
    ]
    subprocess.run(cmd)
    print('Dhaka board screenshot saved:', os.path.exists(abs_out))

if __name__ == '__main__':
    main()
