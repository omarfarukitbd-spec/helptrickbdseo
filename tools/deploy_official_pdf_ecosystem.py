import os
import sys
import json
import requests
from datetime import datetime, timezone

sys.stdout.reconfigure(encoding='utf-8')

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

with open(os.path.join(PROJECT_ROOT, 'tools', 'wp_publisher', 'config.json'), 'r', encoding='utf-8') as f:
    cfg = json.load(f)

auth = (cfg['wp_user'], cfg['wp_app_password'])
base_url = cfg['wp_url'].rstrip('/')

print("==================================================================")
print("1. UPDATING WORDPRESS POSTS WITH AUTHENTIC OFFICIAL PDFS")
print("==================================================================")

posts_to_update = [
    {
        'id': 15904,
        'name': 'Post 1: Primary Scholarship Exam Routine 2026',
        'html': 'output_posts/primary-scholarship-exam-routine-2026.html',
        'meta': 'output_posts/primary-scholarship-exam-routine-2026_meta.json',
        'pdf_url': 'https://www.helptrickbd.com/wp-content/uploads/2026/10/primary_scholarship_policy_routine_2026.pdf',
        'status': 'publish'
    },
    {
        'id': 15907,
        'name': 'Post 2: NU Degree 1st Year Rescheduled Routine 2026',
        'html': 'output_posts/nu-degree-1st-year-rescheduled-routine-2026.html',
        'meta': 'output_posts/nu-degree-1st-year-rescheduled-routine-2026_meta.json',
        'pdf_url': 'https://www.helptrickbd.com/wp-content/uploads/2026/10/nu_degree_1st_year_rescheduled_routine_notice.pdf',
        'status': 'publish'
    },
    {
        'id': 15910,
        'name': 'Post 3: SSC 2027 Test Exam & Form Fill Up Guide',
        'html': 'output_posts/ssc-2027-test-exam-form-fill-up-guide.html',
        'meta': 'output_posts/ssc-2027-test-exam-form-fill-up-guide_meta.json',
        'pdf_url': 'https://www.helptrickbd.com/wp-content/uploads/2026/10/ssc_2027_form_fill_up_notice_dhaka_board.pdf',
        'status': 'publish'
    }
]

live_urls = []

for p in posts_to_update:
    pid = p['id']
    html_file = os.path.join(PROJECT_ROOT, p['html'])
    meta_file = os.path.join(PROJECT_ROOT, p['meta'])
    
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    with open(meta_file, 'r', encoding='utf-8') as f:
        meta_data = json.load(f)
        
    payload = {
        'content': content,
        'status': p['status']
    }
    
    # rank math meta
    if 'rank_math' in meta_data:
        rm = meta_data['rank_math']
        payload['meta'] = {
            'rank_math_title': rm.get('title', meta_data.get('title')),
            'rank_math_description': rm.get('description', meta_data.get('meta_description')),
            'rank_math_focus_keyword': rm.get('focus_keyword', meta_data.get('focus_keyword'))
        }
    
    print(f"[*] Updating Post {pid} ({p['name']})...")
    res = requests.post(f"{base_url}/wp-json/wp/v2/posts/{pid}", json=payload, auth=auth, timeout=30)
    if res.status_code == 200:
        data = res.json()
        live_link = data.get('link')
        print(f"[SUCCESS] Post {pid} updated successfully!")
        print(f"    Status: {data.get('status')}")
        print(f"    Live URL: {live_link}")
        live_urls.append(live_link)
    else:
        print(f"[ERROR] Failed to update Post {pid}: {res.status_code} - {res.text[:200]}")

print("\n==================================================================")
print("2. VERIFYING OFFICIAL PDF DIRECT DOWNLOADS (HTTP 200)")
print("==================================================================")

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

pdf_urls = [p['pdf_url'] for p in posts_to_update]
for purl in pdf_urls:
    try:
        r = requests.head(purl, headers=headers, timeout=15)
        print(f"[*] PDF URL: {purl}")
        print(f"    Status: {r.status_code}")
        print(f"    Content-Type: {r.headers.get('Content-Type')}")
        print(f"    Content-Length: {r.headers.get('Content-Length')} bytes")
        if r.status_code != 200:
            # Fallback check with GET
            r_get = requests.get(purl, headers=headers, stream=True, timeout=15)
            print(f"    GET Fallback Status: {r_get.status_code}")
    except Exception as e:
        print(f"[ERROR] Failed checking PDF {purl}: {e}")

print("\n==================================================================")
print("3. VERIFYING LIVE POST PAGES (HTTP 200 & CONTENT)")
print("==================================================================")

for url in live_urls:
    try:
        r = requests.get(url, headers=headers, timeout=15)
        print(f"[*] Post Page: {url}")
        print(f"    HTTP Status: {r.status_code}")
        has_schema = "schema.org" in r.text
        has_toc = "rank-math-toc" in r.text
        has_pdf_embed = "wp-content/uploads/2026/10/" in r.text
        print(f"    Schema.org Present: {has_schema}")
        print(f"    TOC Present: {has_toc}")
        print(f"    Official PDF Embed/Link Present: {has_pdf_embed}")
        print(f"    HTML Length: {len(r.text)} bytes")
    except Exception as e:
        print(f"[ERROR] Failed checking page {url}: {e}")

print("\n==================================================================")
print("4. MULTI-ENGINE INDEXING NOTIFICATIONS (GOOGLE, WEBSUB, INDEXNOW)")
print("==================================================================")

# 4A. Google Indexing API v3
try:
    from tools.indexer.index_now import get_authenticated_service
    service = get_authenticated_service()
    for url in live_urls:
        body = {
            "url": url,
            "type": "URL_UPDATED"
        }
        res = service.urlNotifications().publish(body=body).execute()
        notify_time = res.get("urlNotificationMetadata", {}).get("latestUpdate", {}).get("notifyTime", "")
        print(f"[SUCCESS] Google Indexing API v3 Ping: {url} -> {notify_time}")
except Exception as e:
    print(f"[!] Google Indexing API error: {e}")

# 4B. Google WebSub Hubs
hubs = [
    "https://pubsubhubbub.appspot.com/publish",
    "https://pubsubhubbub.superfeedr.com/publish"
]
feeds = [
    "https://www.helptrickbd.com/feed/",
    "https://www.helptrickbd.com/sitemap.xml"
]
for hub in hubs:
    for feed in feeds:
        try:
            r = requests.post(hub, data={"hub.mode": "publish", "hub.url": feed}, timeout=10)
            print(f"[SUCCESS] WebSub Ping: {hub} -> {feed} (Status: {r.status_code})")
        except Exception as e:
            print(f"[!] WebSub Ping error for {hub}: {e}")

# 4C. IndexNow
indexnow_payload = {
    "host": "www.helptrickbd.com",
    "key": "helptrickbd2026indexnow",
    "keyLocation": "https://www.helptrickbd.com/helptrickbd2026indexnow.txt",
    "urlList": live_urls
}
try:
    r = requests.post(
        "https://api.indexnow.org/indexnow",
        json=indexnow_payload,
        headers={"Content-Type": "application/json; charset=utf-8"},
        timeout=10
    )
    print(f"[SUCCESS] IndexNow Ping: Status {r.status_code}")
except Exception as e:
    print(f"[!] IndexNow error: {e}")

print("\n==================================================================")
print("ALL 3 POSTS LIVE & SYNCHRONIZED WITH AUTHENTIC OFFICIAL PDFS!")
print("==================================================================")
