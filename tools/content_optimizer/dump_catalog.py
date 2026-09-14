#!/usr/bin/env python3
import json
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from blogger_publisher.update_post import get_authenticated_service, BLOG_ID

service = get_authenticated_service()
posts_res = service.posts().list(blogId=BLOG_ID, maxResults=150).execute()
items = posts_res.get('items', [])

catalog = []
for p in items:
    plain_content = " ".join(p.get("content", "").split())
    words = len(plain_content.split())
    catalog.append({
        "id": p.get("id"),
        "title": p.get("title"),
        "url": p.get("url"),
        "words": words,
        "labels": p.get("labels", [])
    })

catalog.sort(key=lambda x: x["words"])

with open("all_live_posts_catalog.json", "w", encoding="utf-8") as f:
    json.dump(catalog, f, ensure_ascii=False, indent=2)

print(f"Dumped {len(catalog)} live posts to all_live_posts_catalog.json")
print("Top 25 lowest word-count posts right now:")
for p in catalog[:25]:
    slug = p["url"].split("/")[-1].replace(".html", "")
    print(f"  [{p['words']} words] {slug} -> ID: {p['id']} | Title: {p['title'][:40]}")
