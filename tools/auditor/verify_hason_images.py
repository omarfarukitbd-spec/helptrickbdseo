import os, sys, io
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, PROJECT_ROOT)

from tools.blogger_publisher.update_post import get_authenticated_service, BLOG_ID
service = get_authenticated_service()
p = service.posts().get(blogId=BLOG_ID, postId='4269363058446270636').execute()
images = p.get('images', [])
print(f"Post Title: {p.get('title')}")
print(f"Images found by Blogger: {len(images)}")
for img in images:
    print(f"  • {img.get('url')}")
