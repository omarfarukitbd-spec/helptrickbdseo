import os
import sys
import json
import requests

sys.stdout.reconfigure(encoding='utf-8')

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.wp_publisher.publisher import WordPressPublisher

publisher = WordPressPublisher()
auth = publisher.client.auth if hasattr(publisher.client, 'auth') else (publisher.config['wp_user'], publisher.config['wp_app_password'])
base_url = publisher.client.base_url

HTML_PATH = os.path.join(PROJECT_ROOT, "output_posts", "ssc-2027-test-exam-form-fill-up-guide.html")
META_PATH = os.path.join(PROJECT_ROOT, "output_posts", "ssc-2027-test-exam-form-fill-up-guide_meta.json")

with open(HTML_PATH, "r", encoding="utf-8") as f:
    content = f.read()

with open(META_PATH, "r", encoding="utf-8") as f:
    meta = json.load(f)

title = meta.get("title", "")
slug = meta.get("slug", "")
focus_kw = meta.get("focus_keyword", "")
desc = meta.get("meta_description", "")
featured_media_id = meta.get("featured_media_id", 15909)

# Check if slug already exists to prevent duplicate
print(f"[*] Checking if slug '{slug}' already exists on WordPress...")
check_res = requests.get(f"{base_url}/wp-json/wp/v2/posts?slug={slug}&status=any", auth=auth)
if check_res.status_code == 200 and len(check_res.json()) > 0:
    existing_id = check_res.json()[0]["id"]
    print(f"[*] Found existing post with ID {existing_id}. Deleting to ensure clean deployment...")
    del_res = requests.delete(f"{base_url}/wp-json/wp/v2/posts/{existing_id}?force=true", auth=auth)
    if del_res.status_code in [200, 404]:
        print(f"[SUCCESS] Old post {existing_id} permanently deleted.")

# 1. Resolve categories
cat_ids = []
for cname in meta.get("categories", []):
    cid = publisher.get_or_create_category(cname)
    if cid:
        cat_ids.append(cid)

# 2. Resolve tags
tag_ids = []
for tname in meta.get("tags", []):
    tid = publisher.get_or_create_tag(tname)
    if tid:
        tag_ids.append(tid)

# 3. Mint brand new clean draft post
print("[*] Minting brand new clean draft post...")
seo_meta = {
    "title": title,
    "seo_title": title,
    "focus_keyword": focus_kw,
    "seo_description": desc,
    "search_desc": desc
}

new_post = publisher.create_post(
    title=title,
    content=content,
    slug=slug,
    categories=cat_ids,
    tags=tag_ids,
    status="draft",
    featured_media_id=featured_media_id,
    seo_meta=seo_meta
)

if not new_post or not new_post.get("id"):
    print("[ERROR] Failed to create new clean post!")
    sys.exit(1)

new_id = new_post["id"]
print("=================================================================")
print(f"[SUCCESS] CLEAN DRAFT POST MINTED! ID: {new_id}")
print(f"Edit URL: {base_url}/wp-admin/post.php?post={new_id}&action=edit")
print(f"Preview URL: {base_url}/?p={new_id}&preview=true")
print("=================================================================")

# 4. Verify live state
verify_res = requests.get(f"{base_url}/wp-json/wp/v2/posts/{new_id}?context=edit", auth=auth)
if verify_res.status_code == 200:
    p = verify_res.json()
    raw_content = p.get("content", {}).get("raw", "")
    print(f"[*] Verified Post ID: {p.get('id')}")
    print(f"[*] Status: {p.get('status')}")
    print(f"[*] Featured Media ID: {p.get('featured_media')}")
    print(f"[*] Content Length: {len(raw_content)}")
    print(f"[*] Clean TOC ID Present: {'id=\"rank-math-toc\"' in raw_content}")
    print(f"[*] Meta Rank Math Title: {p.get('meta', {}).get('rank_math_title')}")
    print(f"[*] Meta Focus KW: {p.get('meta', {}).get('rank_math_focus_keyword')}")
    print(f"[*] Meta Description: {p.get('meta', {}).get('rank_math_description')}")
