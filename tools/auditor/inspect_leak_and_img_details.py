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
# Inspect Mahatma Gandhi post
post_mg = service.posts().get(blogId=BLOG_ID, postId="7152628717436788366").execute()
content_mg = post_mg.get('content', '')
leaks = re.findall(r'.{0,40}\[https?://[^\]]+\]\(https?://[^\)]+\).{0,40}', content_mg)
print(f"Mahatma Gandhi Post Bracket Leaks ({len(leaks)}):")
for l in leaks[:5]:
    print("  Leak snippet:", repr(l))

# Inspect post with multiple images
posts_res = service.posts().list(blogId=BLOG_ID, maxResults=15, fetchBodies=True).execute()
for p in posts_res.get('items', []):
    tags = re.findall(r'<img[^>]+>', p.get('content', ''))
    if len(tags) > 1:
        print(f"\nMulti-image Post: '{p['title'][:40]}' has {len(tags)} images:")
        for idx, t in enumerate(tags):
            print(f"  Img {idx+1}: {t[:160]}")
