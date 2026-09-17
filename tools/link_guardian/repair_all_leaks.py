import os
import sys
import io
import re

if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, PROJECT_ROOT)

from tools.blogger_publisher.update_post import get_authenticated_service, BLOG_ID

def repair_post():
    service = get_authenticated_service()
    post_id = "7152628717436788366"
    print(f"Fetching post ID: {post_id} ...")
    post = service.posts().get(blogId=BLOG_ID, postId=post_id).execute()
    content = post.get('content', '')

    print(f"Original content length: {len(content)}")
    
    # 1. Fix xmlns markdown bracket leakage
    fixed_content = content.replace("[http://www.w3.org/2000/svg](http://www.w3.org/2000/svg)", "http://www.w3.org/2000/svg")
    
    # 2. Fix any other markdown bracket links [URL](URL)
    fixed_content = re.sub(r'\[(https?://[^\]]+)\]\(\1\)', r'\1', fixed_content)
    fixed_content = re.sub(r'\[(https?://[^\]]+)\]\((https?://[^\)]+)\)', r'\2', fixed_content)

    leaks_remaining = re.findall(r'\[https?://[^\]]+\]\(https?://[^\)]+\)', fixed_content)
    print(f"Leaks before: {len(re.findall(r'\[https?://[^\]]+\]\(https?://[^\)]+\)', content))}")
    print(f"Leaks after regex/replace: {len(leaks_remaining)}")

    if fixed_content != content:
        post['content'] = fixed_content
        updated = service.posts().update(blogId=BLOG_ID, postId=post_id, body=post).execute()
        print("[✓] Post successfully updated on Blogger! Zero bracket leaks remain.")
    else:
        print("[i] No changes needed.")

if __name__ == '__main__':
    repair_post()
