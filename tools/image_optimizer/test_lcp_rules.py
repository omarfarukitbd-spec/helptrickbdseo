import os
import sys
import io
import re

if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, PROJECT_ROOT)

from tools.blogger_publisher.update_post import get_authenticated_service, BLOG_ID

def optimize_img_tag(tag: str, is_first: bool) -> str:
    # Clean existing loading, fetchpriority, decoding
    clean_tag = re.sub(r'\s*loading=["\'][^"\']*["\']', '', tag, flags=re.IGNORECASE)
    clean_tag = re.sub(r'\s*fetchpriority=["\'][^"\']*["\']', '', clean_tag, flags=re.IGNORECASE)
    clean_tag = re.sub(r'\s*decoding=["\'][^"\']*["\']', '', clean_tag, flags=re.IGNORECASE)
    
    # Remove trailing slash or angle bracket
    end_match = re.search(r'(\s*/?>)$', clean_tag)
    end_str = end_match.group(1) if end_match else '>'
    clean_tag = clean_tag[:end_match.start()] if end_match else clean_tag.rstrip('>')

    if is_first:
        # Hero Image: EAGER + HIGH PRIORITY + ASYNC DECODING (Fixes Mobile LCP!)
        new_tag = f'{clean_tag} loading="eager" fetchpriority="high" decoding="async"{end_str}'
    else:
        # Below fold: LAZY + ASYNC DECODING (Saves Mobile Bandwidth!)
        new_tag = f'{clean_tag} loading="lazy" decoding="async"{end_str}'

    return new_tag

def dry_run():
    service = get_authenticated_service()
    all_posts = []
    page_token = None
    while True:
        res = service.posts().list(blogId=BLOG_ID, maxResults=50, pageToken=page_token, fetchBodies=True).execute()
        all_posts.extend(res.get('items', []))
        page_token = res.get('nextPageToken')
        if not page_token:
            break

    posts_to_update = 0
    hero_with_lazy_found = 0
    below_fold_missing_lazy_found = 0

    for p in all_posts:
        content = p.get('content', '')
        img_tags = re.findall(r'<img[^>]+>', content, re.IGNORECASE)
        if not img_tags:
            continue

        needs_update = False
        # Check first image
        if 'loading="lazy"' in img_tags[0].lower() or 'fetchpriority="high"' not in img_tags[0].lower():
            hero_with_lazy_found += 1
            needs_update = True

        # Check subsequent images
        for tag in img_tags[1:]:
            if 'loading="lazy"' not in tag.lower():
                below_fold_missing_lazy_found += 1
                needs_update = True

        if needs_update:
            posts_to_update += 1

    print(f"Total live posts: {len(all_posts)}")
    print(f"Posts requiring Mobile LCP / Lazy-load optimization: {posts_to_update}")
    print(f"  - Hero images currently penalized with loading='lazy' (or missing fetchpriority='high'): {hero_with_lazy_found}")
    print(f"  - Below-the-fold images missing loading='lazy': {below_fold_missing_lazy_found}")

if __name__ == '__main__':
    dry_run()
