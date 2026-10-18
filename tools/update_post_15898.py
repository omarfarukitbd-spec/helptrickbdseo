import os
import sys
import json
import requests

sys.stdout.reconfigure(encoding='utf-8')

POST_ID = 15898
HTML_PATH = 'output_posts/ntrca-school-level-assistant-teacher-syllabus-2026.html'
META_PATH = 'output_posts/ntrca-school-level-assistant-teacher-syllabus-2026_meta.json'
CONFIG_PATH = 'tools/wp_publisher/config.json'

with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
    cfg = json.load(f)

auth = (cfg['wp_user'], cfg['wp_app_password'])
base_url = cfg['wp_url'].rstrip('/')

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

with open(META_PATH, 'r', encoding='utf-8') as f:
    meta = json.load(f)

title = meta.get('title', '')
desc = meta.get('meta_description', '')
focus_kw = meta.get('focus_keyword', '')

payload = {
    'title': title,
    'content': content,
    'featured_media': 15895,
    'meta': {
        'rank_math_title': title,
        'rank_math_description': desc,
        'rank_math_focus_keyword': focus_kw,
        'rank_math_robots': 'index, follow, max-snippet:-1, max-video-preview:-1, max-image-preview:large'
    }
}

endpoint = f"{base_url}/wp-json/wp/v2/posts/{POST_ID}?context=edit"
print(f"[*] Updating Post {POST_ID} on {base_url}...")
res = requests.post(endpoint, json=payload, auth=auth)

if res.status_code == 200:
    data = res.json()
    print(f"[SUCCESS] Post {POST_ID} successfully updated!")
    print(f"[*] Title: {data.get('title', {}).get('raw')}")
    print(f"[*] Modified: {data.get('modified')}")
    print(f"[*] Content length: {len(data.get('content', {}).get('raw', ''))}")
    print(f"[*] Has rank-math/toc-block: {'rank-math/toc-block' in data.get('content', {}).get('raw', '')}")
    print(f"[*] Has id=\"rank-math-toc\": {'id=\"rank-math-toc\"' in data.get('content', {}).get('raw', '')}")
else:
    print(f"[ERROR] Failed to update post {POST_ID}: {res.status_code}")
    print(res.text)
    sys.exit(1)
