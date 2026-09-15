import sys
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')
import urllib.request
import re

url = "https://www.helptrickbd.com/"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
html = urllib.request.urlopen(req).read().decode("utf-8")

for slug in ['primary-teacher-job-viva-preparation', 'bcs-preliminary-marks-distribution', 'cloud-computing-types-benefits-guide', 'computer-virus-cyber-security-guide-2026']:
    pos = html.find(slug)
    if pos != -1:
        snippet = html[pos-800:pos+800]
        proxy = re.findall(r'https://lh3\.googleusercontent\.com/blogger_img_proxy/[^\s\'\"]+', snippet)
        img_src = re.findall(r'src=["\']([^"\']+)["\']', snippet)
        print(f"Slug: {slug}")
        print(f"  Proxy: {proxy[0] if proxy else 'None'}")
        print(f"  Imgs: {img_src}")
        print("-" * 50)
