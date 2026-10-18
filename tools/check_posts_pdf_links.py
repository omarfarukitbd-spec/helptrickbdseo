from bs4 import BeautifulSoup
import sys

sys.stdout.reconfigure(encoding='utf-8')

for post in ['primary-scholarship-exam-routine-2026', 'nu-degree-1st-year-rescheduled-routine-2026', 'ssc-2027-test-exam-form-fill-up-guide']:
    path = f'output_posts/{post}.html'
    soup = BeautifulSoup(open(path, encoding='utf-8'), 'html.parser')
    print(f"\n=== {post} ===")
    for ifr in soup.find_all('iframe'):
        print("Iframe src:", ifr.get('src'))
    for a in soup.find_all('a', href=True):
        if 'pdf' in a['href'].lower() or 'download' in a.get('class', []):
            print(f"Link: {a['href']} ({a.text.strip()[:40]})")
