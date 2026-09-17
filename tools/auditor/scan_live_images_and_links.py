import os
import sys
import io
import re

if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, PROJECT_ROOT)

from tools.blogger_publisher.update_post import get_authenticated_service, BLOG_ID

def analyze_site():
    service = get_authenticated_service()
    if not service:
        print("[!] Blogger API authentication failed.")
        return

    print("Fetching all live posts from Blogger...")
    all_posts = []
    page_token = None
    while True:
        res = service.posts().list(blogId=BLOG_ID, maxResults=50, pageToken=page_token, fetchBodies=True).execute()
        items = res.get('items', [])
        all_posts.extend(items)
        page_token = res.get('nextPageToken')
        if not page_token:
            break

    print(f"Total live posts fetched: {len(all_posts)}\n")

    # 1. Check for the 5 known broken links
    print("="*60)
    print(" 1. AUDITING 5 SPECIFIC BROKEN LINKS IN POSTS")
    print("="*60)
    broken_targets = {
        "Mahatma Gandhi": "reasons-mahatma-gandhi-popularity-political-ideals",
        "Population Growth": "jonosonkha-briddhi-poribesh-probhav",
        "Women Reserved Seats": "jatiyo-songsode-narider-songrokhito-asoner-guruttox"
    }

    found_broken = 0
    for p in all_posts:
        url = p.get('url', '')
        content = p.get('content', '')
        title = p.get('title', '')
        
        # Check bracket leakage
        bracket_leaks = re.findall(r'href="\[https?://[^\]]+\]\([^\)]+\)"', content) or re.findall(r'\[https?://[^\]]+\]\(https?://[^\)]+\)', content)
        if bracket_leaks:
            print(f"[!] Bracket leakage found in '{title}' ({url}): {len(bracket_leaks)} occurrences")
            found_broken += len(bracket_leaks)

        # Check 404 Wikipedia link
        if "বনভূমি_উজাড়" in content or "বনভূমি%20উজাড়" in content:
            print(f"[!] 404 Wikipedia URL found in '{title}' ({url})")
            found_broken += 1

        # Check 404 IPU link
        if "ipu.org/women-in-politics-2023" in content and "publications/infographics" not in content:
            print(f"[!] 404 IPU URL found in '{title}' ({url})")
            found_broken += 1

    if found_broken == 0:
        print(" [✓] Great news: The 5 specific broken links are ALREADY fixed in live Blogger posts!")
    else:
        print(f" [!] Total broken links remaining: {found_broken}")

    # 2. Audit images across all posts
    print("\n" + "="*60)
    print(" 2. AUDITING IMAGES, LOADING='LAZY', WEBP, AND LCP ATTRIBUTES")
    print("="*60)

    total_images = 0
    lazy_images = 0
    eager_or_no_lazy = 0
    webp_images = 0
    missing_alt = 0
    posts_with_images = 0
    posts_without_images = 0

    posts_img_stats = []

    for p in all_posts:
        content = p.get('content', '')
        img_tags = re.findall(r'<img[^>]+>', content, re.IGNORECASE)
        if not img_tags:
            posts_without_images += 1
            continue

        posts_with_images += 1
        p_img_count = len(img_tags)
        total_images += p_img_count

        for idx, tag in enumerate(img_tags):
            is_lazy = 'loading="lazy"' in tag.lower() or "loading='lazy'" in tag.lower()
            is_webp = '.webp' in tag.lower()
            has_alt = 'alt=' in tag.lower() and not re.search(r'alt=["\']\s*["\']', tag, re.IGNORECASE)

            if is_lazy:
                lazy_images += 1
            else:
                eager_or_no_lazy += 1

            if is_webp:
                webp_images += 1
            if not has_alt:
                missing_alt += 1

        posts_img_stats.append({
            'title': p['title'],
            'url': p['url'],
            'id': p['id'],
            'img_count': p_img_count,
            'has_lazy_all': all('loading="lazy"' in t.lower() for t in img_tags),
            'first_img_tag': img_tags[0]
        })

    print(f"Posts with images: {posts_with_images} / {len(all_posts)}")
    print(f"Posts without images: {posts_without_images}")
    print(f"Total images found: {total_images}")
    print(f"  - WebP images: {webp_images} ({webp_images/max(1, total_images)*100:.1f}%)")
    print(f"  - Images with loading='lazy': {lazy_images}")
    print(f"  - Images WITHOUT loading='lazy': {eager_or_no_lazy}")
    print(f"  - Images missing descriptive ALT text: {missing_alt}")

    # Inspect the first 5 posts' image tags
    print("\n--- Sample Image Tags from First 5 Posts ---")
    for s in posts_img_stats[:5]:
        print(f"Post: {s['title'][:40]} (Images: {s['img_count']})")
        print(f"  First Tag: {s['first_img_tag'][:150]}")

if __name__ == '__main__':
    analyze_site()
