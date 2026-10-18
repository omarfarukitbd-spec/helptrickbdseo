import requests
import urllib3

urllib3.disable_warnings()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Referer': 'https://www.nu.ac.bd/examination-notice.php'
}

candidates = [
    'https://www.nu.ac.bd/uploads/notices/notice_6093_pub_date_15102026.PDF',
    'https://www.nu.ac.bd/uploads/notices/notice_6093_pub_date_15102026.pdf',
    'https://nu.ac.bd/uploads/notices/notice_6093_pub_date_15102026.PDF',
    'https://nu.ac.bd/uploads/notices/notice_6093_pub_date_15102026.pdf',
    'http://www.nubd.info/uploads/notices/notice_6093_pub_date_15102026.pdf'
]

for url in candidates:
    r = requests.get(url, headers=headers, verify=False, allow_redirects=True, timeout=10)
    print(f"URL: {url}")
    print(f"   Status: {r.status_code}, Content-Type: {r.headers.get('Content-Type')}, First 30 bytes: {r.content[:30]}")
