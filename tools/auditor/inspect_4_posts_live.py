#!/usr/bin/env python3
import re
import sys
import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, PROJECT_ROOT)

from tools.blogger_publisher.update_post import get_authenticated_service, BLOG_ID

service = get_authenticated_service()
posts = service.posts().list(blogId=BLOG_ID, maxResults=8).execute().get('items', [])
print("=" * 60)
print("Live Blogger Posts - First Image Tag Inspection:")
print("=" * 60)
for p in posts:
    content = p.get('content', '')
    imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', content)
    print(f"Title: {p['title']}")
    print(f"  ID:  {p['id']}")
    print(f"  URL: {p.get('url')}")
    print(f"  Img: {imgs[0] if imgs else 'NO IMAGE'}")
    print("-" * 60)
