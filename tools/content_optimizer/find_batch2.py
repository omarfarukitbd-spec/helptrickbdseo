#!/usr/bin/env python3
import json
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from blogger_publisher.update_post import get_authenticated_service, BLOG_ID

batch2_slugs = [
    'certificate-name-correction-process',
    'ssc-exam-instructions-and-rules',
    'what-is-womens-decade',
    'hason-raja-er-jiboni-o-gan',
    'bangladesh-livestock-research-institute',
    'ishwar-chandra-vidyasagar-contribution-to-bengali-literature',
    'child-socialization-process',
    'causes-of-population-growth-in-bangladesh',
    'namta-1-to-20',
    'reserved-women-seats-in-national-parliament'
]

service = get_authenticated_service()
posts_res = service.posts().list(blogId=BLOG_ID, maxResults=150).execute()
all_posts = posts_res.get('items', [])
print(f"Total live posts fetched from Blogger API: {len(all_posts)}")

found = {}
for p in all_posts:
    url = p.get('url', '')
    for slug in batch2_slugs:
        if slug in url:
            found[slug] = {
                'id': p.get('id'),
                'title': p.get('title'),
                'url': url,
                'labels': p.get('labels', [])
            }

print(f"Found {len(found)}/{len(batch2_slugs)} posts:")
for slug, d in found.items():
    print(f"  {slug} -> ID: {d['id']} | Title: {d['title']}")

missing = set(batch2_slugs) - set(found.keys())
if missing:
    print(f"Missing from Blogger: {missing}")

with open('batch2_posts_meta.json', 'w', encoding='utf-8') as f:
    json.dump(found, f, ensure_ascii=False, indent=2)
print("Saved to batch2_posts_meta.json")
