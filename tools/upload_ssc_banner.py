import os
import sys
import json
import requests

sys.stdout.reconfigure(encoding='utf-8')

with open('tools/wp_publisher/config.json', 'r', encoding='utf-8') as f:
    cfg = json.load(f)

auth = (cfg['wp_user'], cfg['wp_app_password'])
base_url = cfg['wp_url'].rstrip('/')

file_path = os.path.abspath('assets/images/posts/ssc_2027_test_exam_form_fill_up_guide.webp')
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
        'title': 'এসএসসি ২০২৭ নির্বাচনী পরীক্ষা ও ফরম পূরণ নির্দেশিকা',
        'alt_text': 'এসএসসি ২০২৭ নির্বাচনী পরীক্ষা ও ফরম পূরণ নির্দেশিকা এবং বোর্ড ফি'
    }
    requests.post(f"{base_url}/wp-json/wp/v2/media/{mid}", json=meta_payload, auth=auth)
    
    with open('tools/ssc_media.json', 'w', encoding='utf-8') as f:
        json.dump({'media_id': mid, 'url': murl}, f, indent=2)
else:
    print('Failed upload:', res.status_code, res.text)
    sys.exit(1)
