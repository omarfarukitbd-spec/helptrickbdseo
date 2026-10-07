import os
import sys
import io

if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, PROJECT_ROOT)

from tools.blogger_publisher.update_post import get_authenticated_service, BLOG_ID

service = get_authenticated_service()
posts_res = service.posts().list(blogId=BLOG_ID, maxResults=100, fetchBodies=False).execute()
for p in posts_res.get('items', []):
    if 'hason' in p['title'].lower() or 'hason' in p['url'].lower():
        print(f"FOUND: ID={p['id']} | Title={p['title']} | URL={p['url']}")
