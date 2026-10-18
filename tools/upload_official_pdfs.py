import os
import sys
import json
import requests

sys.stdout.reconfigure(encoding='utf-8')

with open('tools/wp_publisher/config.json', 'r', encoding='utf-8') as f:
    cfg = json.load(f)

auth = (cfg['wp_user'], cfg['wp_app_password'])
base_url = cfg['wp_url'].rstrip('/')

pdfs_to_upload = [
    {
        'key': 'ssc_2027',
        'path': 'assets/pdf/ssc/ssc_2027_form_fill_up_notice_dhaka_board.pdf',
        'title': '২০২৭ সালের এসএসসি পরীক্ষার ফরমপূরণের অফিশিয়াল বিজ্ঞপ্তি - ঢাকা শিক্ষা বোর্ড',
        'caption': 'মাধ্যমিক ও উচ্চমাধ্যমিক শিক্ষা বোর্ড, ঢাকা - স্মারক নং ঢাবো/পনি/৮৬০'
    },
    {
        'key': 'nu_degree',
        'path': 'assets/pdf/nu/nu_degree_1st_year_rescheduled_routine_notice.pdf',
        'title': '২০২৫ সালের ডিগ্রি ১ম বর্ষের পরিবর্তিত সময়সূচির অফিশিয়াল বিজ্ঞপ্তি - জাতীয় বিশ্ববিদ্যালয়',
        'caption': 'জাতীয় বিশ্ববিদ্যালয় পরীক্ষা নিয়ন্ত্রণ দপ্তর - স্মারক নং ০৫(৫৩৩) জাতীঃ বিঃ/পরীঃ/ডিগ্রী (পাস)/২০২২/৬০৯৩'
    },
    {
        'key': 'primary_scholarship',
        'path': 'assets/pdf/primary/primary_scholarship_policy_routine_2026.pdf',
        'title': 'প্রাথমিক বৃত্তি পরীক্ষা নীতিমালা ও নির্দেশিকা ২০২৬ - গণশিক্ষা মন্ত্রণালয়',
        'caption': 'গণপ্রজাতন্ত্রী বাংলাদেশ সরকার - প্রাথমিক ও গণশিক্ষা মন্ত্রণালয়'
    }
]

uploaded_pdfs = {}

for item in pdfs_to_upload:
    file_path = os.path.abspath(item['path'])
    filename = os.path.basename(file_path)
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        continue
    
    with open(file_path, 'rb') as f:
        data = f.read()
        
    print(f"\n[*] Uploading {filename} ({len(data)} bytes) to WordPress...")
    headers = {
        'Content-Type': 'application/pdf',
        'Content-Disposition': f'attachment; filename="{filename}"'
    }
    
    res = requests.post(f"{base_url}/wp-json/wp/v2/media", data=data, headers=headers, auth=auth, timeout=60)
    if res.status_code == 201:
        media = res.json()
        mid = media['id']
        murl = media['source_url']
        print(f"[SUCCESS] Uploaded! Media ID: {mid}, URL: {murl}")
        
        # Update title & caption
        meta_payload = {
            'title': item['title'],
            'caption': item['caption']
        }
        requests.post(f"{base_url}/wp-json/wp/v2/media/{mid}", json=meta_payload, auth=auth)
        uploaded_pdfs[item['key']] = {
            'id': mid,
            'url': murl,
            'title': item['title']
        }
    else:
        print(f"[FAILED] Status: {res.status_code}, Body: {res.text[:300]}")

with open('assets/pdf/uploaded_manifest.json', 'w', encoding='utf-8') as f:
    json.dump(uploaded_pdfs, f, indent=2, ensure_ascii=False)

print("\nAll done! Manifest saved to assets/pdf/uploaded_manifest.json")
