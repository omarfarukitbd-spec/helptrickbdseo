import os
import sys
import re

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

sys.path.append(os.path.join(os.path.dirname(__file__), 'blogger_publisher'))
from update_post import get_authenticated_service, BLOG_ID

POST_ID = "2652437465190080886"

service = get_authenticated_service()
if not service:
    print("Failed to authenticate Blogger API service.")
    sys.exit(1)

post = service.posts().get(blogId=BLOG_ID, postId=POST_ID).execute()
title = post.get('title')
content = post.get('content')
print(f"Fetched post: {title}")

# Check if <div class="container"> exists
if '<div class="container">' in content or "<div class='container'>" in content:
    print("Found <div class=\"container\"> in post content! Replacing with <div class=\"ht-bagdhara-wrapper\">...")
    new_content = content.replace('<div class="container">', '<div class="ht-bagdhara-wrapper">')
    new_content = new_content.replace("<div class='container'>", "<div class='ht-bagdhara-wrapper'>")
    
    # Save a backup locally
    os.makedirs('backup_posts', exist_ok=True)
    with open('backup_posts/bagdhara_before_fix.html', 'w', encoding='utf-8') as f:
        f.write(content)
        
    patch_body = {
        'content': new_content
    }
    updated = service.posts().patch(blogId=BLOG_ID, postId=POST_ID, body=patch_body).execute()
    print(f"SUCCESS! Post updated live on Blogger. URL: {updated.get('url')}")
else:
    print("No <div class=\"container\"> found in this post.")
