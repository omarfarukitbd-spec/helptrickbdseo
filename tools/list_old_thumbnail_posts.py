import urllib.request
import json
import re
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

feed_url = 'https://www.helptrickbd.com/feeds/posts/default?alt=json&max-results=150'
req = urllib.request.Request(feed_url, headers={'User-Agent': 'Mozilla/5.0'})
feed = json.loads(urllib.request.urlopen(req).read().decode('utf-8'))
entries = feed['feed']['entry']

print(f"Total posts fetched: {len(entries)}")

old_pill_posts = []
clean_bg_posts = []

for i, entry in enumerate(entries):
    title = entry.get('title', {}).get('$t', '')
    url = ''
    for l in entry.get('link', []):
        if l.get('rel') == 'alternate':
            url = l.get('href', '')
            break
            
    content = entry.get('content', {}).get('$t', '')
    imgs = re.findall(r'<img[^>]+src=[\'"]([^\'"]+)[\'"]', content)
    first_img = imgs[0] if imgs else entry.get('media$thumbnail', {}).get('url', '')
    
    # Check if image name has 'official_bg' or comes from user's BG template
    if 'official_bg' in first_img or 'official-bg' in first_img or 'bcs-preli-hero' in first_img or 'primary-viva' in first_img or 'cloud-computing' in first_img or 'cyber-security' in first_img or 'dhaka_board' in first_img:
        clean_bg_posts.append((title, url, first_img))
    else:
        old_pill_posts.append((title, url, first_img))

print(f"Posts with clean official Thumbnail BG: {len(clean_bg_posts)}")
print(f"Posts that still have old/dark pill/unformatted thumbnails: {len(old_pill_posts)}\n")

print("="*70)
print("LIST OF POSTS NEEDING OFFICIAL THUMBNAIL BG REPLACEMENT:")
print("="*70)
for idx, (title, url, img) in enumerate(old_pill_posts):
    print(f"#{idx+1}: {title}")
    print(f"   URL: {url}")
    print(f"   Current Image: {img}")
    print("-" * 70)
