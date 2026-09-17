import os
import sys
import io
import re

if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, PROJECT_ROOT)

from tools.blogger_publisher.update_post import get_authenticated_service, BLOG_ID

service = get_authenticated_service()
all_posts = []
page_token = None
while True:
    res = service.posts().list(blogId=BLOG_ID, maxResults=50, pageToken=page_token, fetchBodies=True).execute()
    all_posts.extend(res.get('items', []))
    page_token = res.get('nextPageToken')
    if not page_token:
        break

lazy_hero_posts = []
for p in all_posts:
    content = p.get('content', '')
    img_tags = re.findall(r'<img[^>]+>', content, re.IGNORECASE)
    if img_tags:
        first_img = img_tags[0]
        if 'loading="lazy"' in first_img.lower() or "loading='lazy'" in first_img.lower():
            lazy_hero_posts.append((p['id'], p['title'], p['url'], first_img))

print(f"Posts where the FIRST image has loading='lazy': {len(lazy_hero_posts)}")
print("\nSample posts:")
for pid, title, url, tag in lazy_hero_posts[:10]:
    print(f"- {title[:40]} | URL: {url}")
    print(f"  Tag: {tag[:130]}")
