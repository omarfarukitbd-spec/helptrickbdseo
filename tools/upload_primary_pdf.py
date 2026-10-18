import os
import sys
import json
import requests

sys.stdout.reconfigure(encoding='utf-8')

with open('tools/wp_publisher/config.json', 'r', encoding='utf-8') as f:
    cfg = json.load(f)

auth = (cfg['wp_user'], cfg['wp_app_password'])
base_url = cfg['wp_url'].rstrip('/')

# Upload primary scholarship PDF
file_path = os.path.abspath('assets/pdf/primary/primary_scholarship_policy_routine_2026_clean.pdf')
filename = 'primary_scholarship_policy_routine_2026.pdf'

with open(file_path, 'rb') as f:
    data = f.read()

print(f"[*] Uploading {filename} ({len(data)} bytes) to WordPress...")
headers = {
    'Content-Type': 'application/pdf',
    'Content-Disposition': f'attachment; filename="{filename}"'
}

res = requests.post(f"{base_url}/wp-json/wp/v2/media", data=data, headers=headers, auth=auth, timeout=120)
if res.status_code == 201:
    media = res.json()
    mid = media['id']
    murl = media['source_url']
    print(f"[SUCCESS] Uploaded! Media ID: {mid}, URL: {murl}")
    
    meta_payload = {
        'title': 'প্রাথমিক বৃত্তি পরীক্ষা নীতিমালা ও নির্দেশিকা ২০২৬ - গণশিক্ষা মন্ত্রণালয়',
        'caption': 'গণপ্রজাতন্ত্রী বাংলাদেশ সরকার - প্রাথমিক ও গণশিক্ষা মন্ত্রণালয়'
    }
    requests.post(f"{base_url}/wp-json/wp/v2/media/{mid}", json=meta_payload, auth=auth)
else:
    print(f"[FAILED] Status: {res.status_code}, Body: {res.text[:300]}")
