#!/usr/bin/env python3
import os
import sys
import re

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, PROJECT_ROOT)

from tools.blogger_publisher.update_post import get_authenticated_service, BLOG_ID

service = get_authenticated_service()
pid = '5898560761534163519'
post = service.posts().get(blogId=BLOG_ID, postId=pid).execute()
content = post.get('content', '')

new_url = 'https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/posts/primary-teacher-viva-preparation-guide-banner.webp'

# Replace any primary teacher image src with new_url
new_content = re.sub(r'https://cdn\.jsdelivr\.net/[^"\'>]+primary-teacher[^"\'>]+\.webp', new_url, content)

if new_content != content:
    post['content'] = new_content
    updated = service.posts().update(blogId=BLOG_ID, postId=pid, body=post).execute()
    print("SUCCESS: Post updated with brand new cache-busted banner URL!")
    print(f"Post Title: {updated.get('title')}")
    print(f"Live URL:   {updated.get('url')}")
else:
    print("Pattern match failed, force-replacing in img tag:")
    new_content = re.sub(r'(<img[^>]+src=")[^"]+(")', r'\g<1>' + new_url + r'\g<2>', content, count=1)
    post['content'] = new_content
    updated = service.posts().update(blogId=BLOG_ID, postId=pid, body=post).execute()
    print("SUCCESS (force): First img src replaced!")
