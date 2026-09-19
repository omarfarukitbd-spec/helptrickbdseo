import os
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, PROJECT_ROOT)

from tools.blogger_publisher.publisher import get_authenticated_service, BLOG_ID

service = get_authenticated_service()
pid = "4710432391315087780"

post = service.posts().get(blogId=BLOG_ID, postId=pid, view="ADMIN").execute()
print(f"Current labels: {post.get('labels')}")

updated = service.posts().patch(
    blogId=BLOG_ID,
    postId=pid,
    body={
        "labels": ["Political Science"],
        "published": post.get("published")
    }
).execute()

print(f"[OK] New labels: {updated.get('labels')}")
