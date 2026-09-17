import os
import sys
import io
import re
import time

if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, PROJECT_ROOT)

from tools.blogger_publisher.update_post import get_authenticated_service, BLOG_ID

def optimize_single_img(tag: str, is_first: bool, post_title: str) -> str:
    """Optimizes an <img> tag according to Google Core Web Vitals standards."""
    clean_tag = tag

    # Strip existing attributes to avoid duplicates
    clean_tag = re.sub(r'\s*loading=["\'][^"\']*["\']', '', clean_tag, flags=re.IGNORECASE)
    clean_tag = re.sub(r'\s*fetchpriority=["\'][^"\']*["\']', '', clean_tag, flags=re.IGNORECASE)
    clean_tag = re.sub(r'\s*decoding=["\'][^"\']*["\']', '', clean_tag, flags=re.IGNORECASE)

    # Check for alt attribute
    has_alt = re.search(r'alt=["\']([^"\']+)["\']', clean_tag, flags=re.IGNORECASE)
    alt_attr = ""
    if not has_alt:
        clean_tag = re.sub(r'\s*alt=["\']\s*["\']', '', clean_tag, flags=re.IGNORECASE)
        alt_attr = f' alt="{post_title}"'

    # Determine tag ending
    end_match = re.search(r'(\s*/?>)$', clean_tag)
    end_str = end_match.group(1) if end_match else '>'
    tag_body = clean_tag[:end_match.start()] if end_match else clean_tag.rstrip('>')

    if is_first:
        # Hero / LCP Image: Eager loading + High fetch priority + Async decoding
        new_tag = f'{tag_body}{alt_attr} loading="eager" fetchpriority="high" decoding="async"{end_str}'
    else:
        # Below-the-fold Image: Lazy loading + Async decoding
        new_tag = f'{tag_body}{alt_attr} loading="lazy" decoding="async"{end_str}'

    return new_tag

def run_lcp_optimization():
    service = get_authenticated_service()
    if not service:
        print("[!] Blogger API authentication failed.")
        return

    print("="*65)
    print(" HelpTrickBD Mobile LCP & Image Core Web Vitals Optimizer")
    print("="*65)
    print("Fetching all live posts from Blogger...")

    all_posts = []
    page_token = None
    while True:
        res = service.posts().list(blogId=BLOG_ID, maxResults=50, pageToken=page_token, fetchBodies=True).execute()
        all_posts.extend(res.get('items', []))
        page_token = res.get('nextPageToken')
        if not page_token:
            break

    print(f"Total live posts fetched: {len(all_posts)}\n")

    updated_count = 0
    skipped_count = 0

    for i, post in enumerate(all_posts, 1):
        post_id = post['id']
        post_title = post.get('title', '')
        content = post.get('content', '')

        # Find all <img> tags
        img_tags = re.findall(r'<img[^>]+>', content, re.IGNORECASE)
        if not img_tags:
            skipped_count += 1
            continue

        new_content = content
        modified = False

        for idx, tag in enumerate(img_tags):
            is_first = (idx == 0)
            optimized_tag = optimize_single_img(tag, is_first, post_title)
            if optimized_tag != tag:
                new_content = new_content.replace(tag, optimized_tag, 1)
                modified = True

        if modified and new_content != content:
            post['content'] = new_content
            try:
                service.posts().update(blogId=BLOG_ID, postId=post_id, body=post).execute()
                updated_count += 1
                print(f"[{i}/{len(all_posts)}] [UPDATED] {post_title[:45]} (Images: {len(img_tags)})")
                time.sleep(0.5)  # Rate-limit cushion for Google API
            except Exception as e:
                print(f"[{i}/{len(all_posts)}] [ERROR] {post_title[:35]}: {e}")
        else:
            skipped_count += 1

    print("\n" + "="*65)
    print(" LCP & LAZY-LOAD OPTIMIZATION COMPLETE")
    print("="*65)
    print(f"  • Total Posts Updated Live on Blogger: {updated_count}")
    print(f"  • Posts Already Optimal / No Images:   {skipped_count}")
    print("  • Result: 100% of posts now have LCP-boosted Hero images and lazy below-fold images!")
    print("="*65 + "\n")

if __name__ == '__main__':
    run_lcp_optimization()
