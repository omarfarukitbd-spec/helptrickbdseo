import os, sys, io, re
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, PROJECT_ROOT)

from tools.blogger_publisher.update_post import get_authenticated_service, BLOG_ID
service = get_authenticated_service()
posts_res = service.posts().list(blogId=BLOG_ID, maxResults=10, fetchBodies=True).execute()
for p in posts_res.get('items', []):
    imgs = p.get('images', [])
    print(f"Post: {p['title'][:40]} | Images: {len(imgs)}")
    if imgs:
        print(f"  Blogger Image URL: {imgs[0].get('url')}")
        m = re.search(r'<img[^>]+>', p.get('content', ''))
        if m:
            print(f"  First img tag in HTML: {m.group(0)[:150]}")
