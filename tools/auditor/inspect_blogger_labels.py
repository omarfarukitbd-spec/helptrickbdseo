#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/auditor/inspect_blogger_labels.py
Lists all live posts and their labels from Blogger API.
"""

import os
import sys
import io

if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, PROJECT_ROOT)

from tools.blogger_publisher.update_post import get_authenticated_service, BLOG_ID

service = get_authenticated_service()
if not service:
    print("Could not authenticate to Blogger API.")
    sys.exit(1)

posts_res = service.posts().list(blogId=BLOG_ID, maxResults=100, fetchBodies=False).execute()
posts = posts_res.get('items', [])

label_map = {}
post_labels = []

for p in posts:
    labels = p.get('labels', ['[NO LABEL]'])
    post_labels.append({
        'id': p['id'],
        'title': p['title'],
        'url': p['url'],
        'labels': labels
    })
    for l in labels:
        label_map[l] = label_map.get(l, 0) + 1

print(f"Total Published Posts: {len(posts)}")
print(f"Total Unique Labels  : {len(label_map)}")
print("-" * 60)
print("LABEL DISTRIBUTION:")
for l, c in sorted(label_map.items(), key=lambda x: -x[1]):
    print(f"  [{c:2d} posts] {l}")
