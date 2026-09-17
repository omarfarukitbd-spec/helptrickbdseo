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

no_lazy_tags = []
for p in all_posts:
    content = p.get('content', '')
    img_tags = re.findall(r'<img[^>]+>', content, re.IGNORECASE)
    for idx, t in enumerate(img_tags):
        if 'loading="lazy"' not in t.lower() and "loading='lazy'" not in t.lower():
            no_lazy_tags.append((p['title'], idx, t))

print(f"Total img tags without loading='lazy': {len(no_lazy_tags)}")
print("\nFirst 10 tags without loading='lazy':")
for title, idx, tag in no_lazy_tags[:10]:
    print(f"- Post: {title[:35]} (Image #{idx+1})")
    print(f"  Tag: {tag[:140]}")
