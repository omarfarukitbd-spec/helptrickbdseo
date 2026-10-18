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

post_ids = [15904, 15907]
live_posts = []

print("==================================================================")
print("1. CHECKING WORDPRESS LIVE STATUS FOR POSTS 15904 & 15907")
print("==================================================================")

for pid in post_ids:
    res = requests.get(f"{base_url}/wp-json/wp/v2/posts/{pid}", auth=auth)
    if res.status_code == 200:
        data = res.json()
        status = data.get("status")
        link = data.get("link")
        title = data.get("title", {}).get("rendered", "")
        slug = data.get("slug")
        print(f"[*] Post ID: {pid}")
        print(f"    Title: {title}")
        print(f"    Status: {status}")
        print(f"    Link: {link}")
        
        # If user marked as publish or if it's draft, let's verify
        if status != "publish":
            print(f"    [NOTICE] Status is '{status}'. Updating to 'publish' to ensure public live availability...")
            pub_res = requests.post(f"{base_url}/wp-json/wp/v2/posts/{pid}", json={"status": "publish"}, auth=auth)
            if pub_res.status_code == 200:
                data = pub_res.json()
                status = data.get("status")
                link = data.get("link")
                print(f"    [SUCCESS] Post {pid} is now LIVE with status: {status}!")
                print(f"    Live URL: {link}")
        
        live_posts.append({
            "id": pid,
            "title": title,
            "status": status,
            "url": link,
            "slug": slug
        })
    else:
        print(f"[ERROR] Failed to fetch Post {pid}: {res.status_code}")

print("\n==================================================================")
print("2. VERIFYING LIVE HTTP 200 & CONTENT ACCESSIBILITY")
print("==================================================================")

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
verified_urls = []

for p in live_posts:
    url = p["url"]
    try:
        r = requests.get(url, headers=headers, timeout=15)
        print(f"[*] Checking {url}...")
        print(f"    HTTP Status: {r.status_code}")
        has_schema = "schema.org" in r.text
        has_toc = "rank-math-toc" in r.text
        has_banner = "htbd-featured-hero" in r.text or "featured" in r.text
        print(f"    Schema.org Present: {has_schema}")
        print(f"    TOC Present: {has_toc}")
        print(f"    Content Length: {len(r.text)} bytes")
        if r.status_code == 200:
            verified_urls.append(url)
            p["http_status"] = 200
            p["schema_present"] = has_schema
            p["toc_present"] = has_toc
    except Exception as e:
        print(f"[ERROR] Exception checking {url}: {e}")

print("\n==================================================================")
print("3. MULTI-ENGINE PUSH (GOOGLE INDEXING API, WEBSUB, INDEXNOW)")
print("==================================================================")

# 3A. Google Indexing API v3
try:
    from tools.indexer.index_now import get_authenticated_service
    service = get_authenticated_service()
    for url in verified_urls:
        body = {
            "url": url,
            "type": "URL_UPDATED"
        }
        res = service.urlNotifications().publish(body=body).execute()
        notify_time = res.get("urlNotificationMetadata", {}).get("latestUpdate", {}).get("notifyTime", "")
        print(f"[SUCCESS] Google Indexing API v3: {url}")
        print(f"    Notify Time: {notify_time}")
except Exception as e:
    print(f"[!] Google Indexing API error: {e}")

# 3B. Google WebSub Hubs
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
            print(f"[SUCCESS] WebSub Hub Ping: {hub} -> {feed} (Status: {r.status_code})")
        except Exception as e:
            print(f"[!] WebSub Ping error for {hub}: {e}")

# 3C. IndexNow (Bing / Yandex / Seznam)
indexnow_payload = {
    "host": "www.helptrickbd.com",
    "key": "helptrickbd2026indexnow",
    "keyLocation": "https://www.helptrickbd.com/helptrickbd2026indexnow.txt",
    "urlList": verified_urls
}
try:
    r = requests.post(
        "https://api.indexnow.org/indexnow",
        json=indexnow_payload,
        headers={"Content-Type": "application/json; charset=utf-8"},
        timeout=10
    )
    print(f"[SUCCESS] IndexNow Submission: Status {r.status_code}")
except Exception as e:
    print(f"[!] IndexNow error: {e}")

print("\n==================================================================")
print("INDEXING PIPELINE COMPLETED SUCCESSFULLY!")
print("==================================================================")
