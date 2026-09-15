#!/usr/bin/env python3
import urllib.request
import re

URLS = [
    "https://www.helptrickbd.com/2026/09/computer-virus-cyber-security-guide-2026.html",
    "https://www.helptrickbd.com/2026/09/cloud-computing-types-benefits-guide.html",
    "https://www.helptrickbd.com/2026/09/bcs-preliminary-marks-distribution_01436475916.html",
    "https://www.helptrickbd.com/2026/09/primary-teacher-job-viva-preparation.html"
]

print("Verifying Live Post Image Tags and HTTP status...")
for u in URLS:
    try:
        req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"})
        html = urllib.request.urlopen(req).read().decode("utf-8")
        matches = re.findall(r'src="(https://cdn\.jsdelivr\.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/posts/[^"]+)"', html)
        if matches:
            img_url = matches[0]
            # Check img_url status
            img_resp = urllib.request.urlopen(img_url)
            print(f"[OK] {u.split('/')[-1]}\n     -> Image URL: {img_url} (HTTP {img_resp.status}, {len(img_resp.read())} bytes)")
        else:
            print(f"[FAIL] No jsDelivr match found in {u}")
    except Exception as e:
        print(f"[ERROR] {u}: {e}")
