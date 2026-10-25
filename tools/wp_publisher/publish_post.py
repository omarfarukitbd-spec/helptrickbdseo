#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/wp_publisher/publish_post.py
----------------------------------
CLI script to publish or draft a post to WordPress 6.7+ via the REST API,
including Featured Image upload, category/tag mapping, and Rank Math SEO metadata.

Usage:
  python tools/wp_publisher/publish_post.py <HTML_FILE> --meta <META_JSON> [--status draft|publish]
"""

import os
import sys
import json
import argparse

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.wp_publisher.publisher import WordPressPublisher

sys.stdout.reconfigure(encoding='utf-8')

def publish_from_files(html_path: str, meta_path: str, status: str = "draft"):
    if not os.path.exists(html_path):
        print(f"[ERROR] HTML file not found: {html_path}")
        sys.exit(1)

    with open(html_path, "r", encoding="utf-8") as f:
        content = f.read()

    meta = {}
    if os.path.exists(meta_path):
        with open(meta_path, "r", encoding="utf-8") as f:
            meta = json.load(f)

    title = meta.get("title", "Untitled Post")
    slug = meta.get("slug", "")
    focus_kw = meta.get("focus_keyword", "")
    meta_desc = meta.get("meta_description", "")

    publisher = WordPressPublisher()

    print("=================================================================")
    print(f"[*] HELPTRICKBD POST PUBLISHING INITIATED (Status: {status.upper()})")
    print("=================================================================")
    print(f"Title     : {title}")
    print(f"Slug      : {slug}")
    print(f"Focus KW  : {focus_kw}")
    print(f"Target WP : {publisher.client.base_url}")
    print("-----------------------------------------------------------------")

    # 1. Upload or reuse Featured Image
    featured_media_id = meta.get("featured_media_id")
    if featured_media_id:
        print(f"[+] Reusing existing Featured Media ID from metadata: {featured_media_id}")
    else:
        banner_path = meta.get("banner_path")
        if banner_path and os.path.exists(banner_path):
            print(f"[*] Uploading Featured Image: {banner_path}...")
            featured_media_id = publisher.upload_featured_image(
                file_path=banner_path,
                alt_text=focus_kw,
                title=title
            )
            if featured_media_id:
                print(f"[SUCCESS] Featured Image uploaded to Media Library! ID: {featured_media_id}")
            else:
                print("[WARN] Featured image upload failed. Continuing without attachment.")
        elif banner_path:
            print(f"[WARN] Banner file does not exist locally: {banner_path}")

    # 2. Resolve Categories
    cat_ids = []
    category_names = meta.get("categories", [])
    for cname in category_names:
        cid = publisher.get_or_create_category(cname)
        if cid:
            cat_ids.append(cid)
            print(f"[+] Category mapped: '{cname}' -> ID {cid}")
        else:
            print(f"[-] Category resolution failed for: '{cname}'")

    # 3. Resolve Tags
    tag_ids = []
    tag_names = meta.get("tags", [])
    for tname in tag_names:
        tid = publisher.get_or_create_tag(tname)
        if tid:
            tag_ids.append(tid)
            print(f"[+] Tag mapped: '{tname}' -> ID {tid}")
        else:
            print(f"[-] Tag resolution failed for: '{tname}'")

    # 4. Prepare Rank Math SEO Metadata
    seo_meta = {
        "title": title,
        "seo_title": title,
        "focus_keyword": focus_kw,
        "seo_description": meta_desc,
        "search_desc": meta_desc
    }

    # 5. Create / Draft Post
    print(f"[*] Creating post as '{status}' on WordPress...")
    res = publisher.create_post(
        title=title,
        content=content,
        slug=slug,
        categories=cat_ids,
        tags=tag_ids,
        status=status,
        featured_media_id=featured_media_id,
        seo_meta=seo_meta
    )

    if res.get("success"):
        post_id = res.get("id")
        preview_url = f"{publisher.client.base_url}/?p={post_id}&preview=true"
        edit_url = res.get("edit_url")
        public_url = res.get("url")

        print("=================================================================")
        print(f"[SUCCESS] POST CREATED SUCCESSFULLY (Status: {status.upper()})")
        print("=================================================================")
        print(f"Post ID     : {post_id}")
        print(f"Preview URL : {preview_url}")
        print(f"Edit URL    : {edit_url}")
        print(f"Live URL    : {public_url}")
        print("=================================================================")
        return res
    else:
        print("=================================================================")
        print(f"[ERROR] Failed to create post: {res.get('error')}")
        print("=================================================================")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Publish or draft a post to WordPress 6.7+")
    parser.add_argument("html_file", help="Path to post HTML file")
    parser.add_argument("--meta", required=True, help="Path to post metadata JSON file")
    parser.add_argument("--status", choices=["draft", "publish", "pending"], default="draft", help="Post status (default: draft)")

    args = parser.parse_args()
    publish_from_files(args.html_file, args.meta, status=args.status)

if __name__ == "__main__":
    main()
