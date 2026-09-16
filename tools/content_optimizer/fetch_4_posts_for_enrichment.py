#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import json
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.blogger_publisher.publisher import get_authenticated_service, BLOG_ID

try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

service = get_authenticated_service()
pids = [
    ("3708406842330148411", "bcs_post.html"),
    ("5695213693308965635", "cloud_post.html"),
    ("3998042912898607308", "virus_post.html"),
    ("4176960177069689710", "women_seats_post.html")
]

out_dir = os.path.join(os.path.dirname(__file__), "raw_thin_posts")
os.makedirs(out_dir, exist_ok=True)

for pid, filename in pids:
    p = service.posts().get(blogId=BLOG_ID, postId=pid).execute()
    filepath = os.path.join(out_dir, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(p.get("content", ""))
    print(f"[✔] Fetched: {p.get('title')} ({len(p.get('content', ''))} bytes) -> {filename}")
