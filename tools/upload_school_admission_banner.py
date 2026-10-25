import os
import sys
import json
import requests

sys.stdout.reconfigure(encoding='utf-8')

with open('tools/wp_publisher/config.json', 'r', encoding='utf-8') as f:
    cfg = json.load(f)

auth = (cfg['wp_user'], cfg['wp_app_password'])
base_url = cfg['wp_url'].rstrip('/')

file_path = os.path.abspath('assets/images/posts/school_admission_lottery_exam_guide_2027.webp')
filename = os.path.basename(file_path)

with open(file_path, 'rb') as f:
    img_data = f.read()

headers = {
    'Content-Type': 'image/webp',
    'Content-Disposition': f'attachment; filename="{filename}"'
}

print(f"[*] Uploading {filename} ({len(img_data)} bytes) to WordPress Media Library...")
res = requests.post(f"{base_url}/wp-json/wp/v2/media", data=img_data, headers=headers, auth=auth)

if res.status_code == 201:
    media = res.json()
    mid = media['id']
    murl = media['source_url']
    print(f"[SUCCESS] Uploaded! Media ID: {mid}, URL: {murl}")
    
    # Update alt text and title
    meta_payload = {
        'title': 'স্কুল ভর্তি লটারি ও লিখিত পরীক্ষা ২০২৭ নির্দেশিকা',
        'alt_text': 'স্কুল ভর্তি লটারি ২০২৭ ১ম শ্রেণি লটারি ও ২য়-৯ম শ্রেণি লিখিত পরীক্ষার মানবণ্টন'
    }
    requests.post(f"{base_url}/wp-json/wp/v2/media/{mid}", json=meta_payload, auth=auth)
    
    with open('tools/school_admission_media.json', 'w', encoding='utf-8') as f:
        json.dump({'media_id': mid, 'url': murl}, f, indent=2)
    print(f"[SUCCESS] Saved media metadata to tools/school_admission_media.json")
else:
    print('Failed upload:', res.status_code, res.text)
    sys.exit(1)
