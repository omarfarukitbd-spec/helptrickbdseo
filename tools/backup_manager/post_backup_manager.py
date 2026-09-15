#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/backup_manager/post_backup_manager.py
-------------------------------------------
Automated Post Backup & Rollback Guardian for HelpTrickBD.
Strictly captures and preserves 100% of the original post state
(HTML code, image links, labels, title, and metadata) BEFORE
any edit is executed on live Blogger.
"""

import os
import sys
import json
import re
from datetime import datetime
from bs4 import BeautifulSoup

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
BACKUP_ROOT = os.path.join(PROJECT_ROOT, "backups", "posts")


def extract_images_from_html(html_content):
    """Extract all image tags, their URLs, alt text, and titles from HTML."""
    if not html_content:
        return []
    soup = BeautifulSoup(html_content, "html.parser")
    images = []
    for idx, img in enumerate(soup.find_all("img")):
        src = img.get("src", "")
        alt = img.get("alt", "")
        title = img.get("title", "")
        width = img.get("width", "")
        height = img.get("height", "")
        images.append({
            "index": idx + 1,
            "src": src,
            "alt": alt,
            "title": title,
            "width": width,
            "height": height
        })
    return images


def get_slug_from_url(url):
    """Extract URL slug from a full Blogger post URL."""
    if not url:
        return "unknown_post"
    # Example: https://www.helptrickbd.com/2025/01/honours-political-science-book-list.html
    m = re.search(r"/([^/]+)\.html$", url)
    if m:
        return m.group(1)
    return "post_" + re.sub(r"[^a-zA-Z0-9_-]", "_", url.split("/")[-1])


def create_post_backup(post_data, reason="pre_edit_backup"):
    """
    Creates an immutable, timestamped backup of a live Blogger post before editing.
    Stores:
      1. original_content.html (Exact original post HTML)
      2. metadata.json (Post ID, Title, URL, Labels, Published, Updated, Backup Time, Reason)
      3. images.json (Every image URL, alt, and title)
      4. README.md (Human-readable summary of the post state)
    """
    if not post_data:
        print("[!] Backup Error: No post data provided.")
        return None

    post_id = str(post_data.get("id", "unknown_id"))
    title = post_data.get("title", "Untitled Post")
    url = post_data.get("url", "")
    content = post_data.get("content", "")
    labels = post_data.get("labels", [])
    published = post_data.get("published", "")
    updated = post_data.get("updated", "")

    slug = get_slug_from_url(url)
    timestamp_str = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Folder: backups/posts/<slug>/<timestamp>
    post_backup_dir = os.path.join(BACKUP_ROOT, slug, timestamp_str)
    os.makedirs(post_backup_dir, exist_ok=True)

    # 1. Save original HTML content
    html_path = os.path.join(post_backup_dir, "original_content.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(content)

    # 2. Extract and save image data
    images = extract_images_from_html(content)
    images_path = os.path.join(post_backup_dir, "images.json")
    with open(images_path, "w", encoding="utf-8") as f:
        json.dump(images, f, ensure_ascii=False, indent=2)

    # 3. Save comprehensive metadata
    metadata = {
        "post_id": post_id,
        "title": title,
        "url": url,
        "slug": slug,
        "labels": labels,
        "published": published,
        "updated": updated,
        "backup_timestamp": datetime.now().isoformat(),
        "backup_reason": reason,
        "total_images": len(images),
        "content_length_chars": len(content)
    }
    meta_path = os.path.join(post_backup_dir, "metadata.json")
    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump(metadata, f, ensure_ascii=False, indent=2)

    # 4. Save human-readable README.md
    readme_path = os.path.join(post_backup_dir, "README.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(f"# Post Backup: {title}\n\n")
        f.write(f"- **Post ID:** `{post_id}`\n")
        f.write(f"- **URL:** [{url}]({url})\n")
        f.write(f"- **Original Labels:** {', '.join(labels) if labels else 'None'}\n")
        f.write(f"- **Published Date:** {published}\n")
        f.write(f"- **Last Updated (at backup):** {updated}\n")
        f.write(f"- **Backup Timestamp:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"- **Reason:** {reason}\n")
        f.write(f"- **Images Detected:** {len(images)}\n\n")
        f.write("### Images in Post:\n")
        for img in images:
            f.write(f"- [{img['alt'] or 'No Alt'}]({img['src']})\n")

    # 5. Also update the 'latest' folder for this slug
    latest_dir = os.path.join(BACKUP_ROOT, slug, "latest")
    os.makedirs(latest_dir, exist_ok=True)
    with open(os.path.join(latest_dir, "original_content.html"), "w", encoding="utf-8") as f:
        f.write(content)
    with open(os.path.join(latest_dir, "metadata.json"), "w", encoding="utf-8") as f:
        json.dump(metadata, f, ensure_ascii=False, indent=2)
    with open(os.path.join(latest_dir, "images.json"), "w", encoding="utf-8") as f:
        json.dump(images, f, ensure_ascii=False, indent=2)

    print("\n" + "=" * 70)
    print("🛡️  [BACKUP GUARDIAN] পূর্ববর্তী পোস্টের সম্পূর্ণ ব্যাকআপ সম্পন্ন হয়েছে!")
    print(f"  • Post ID:      {post_id}")
    print(f"  • Title:        {title}")
    print(f"  • Labels:       {labels}")
    print(f"  • Images Saved: {len(images)} টি ইমেজ লিঙ্ক সংরক্ষিত")
    print(f"  • Backup Dir:   {post_backup_dir}")
    print("=" * 70 + "\n")

    return post_backup_dir


def list_all_backups(slug=None):
    """List all available post backups."""
    if not os.path.exists(BACKUP_ROOT):
        print("[!] No backups directory found.")
        return []

    backups = []
    slugs = [slug] if slug else os.listdir(BACKUP_ROOT)

    for s in slugs:
        sdir = os.path.join(BACKUP_ROOT, s)
        if not os.path.isdir(sdir):
            continue
        for ts in os.listdir(sdir):
            if ts == "latest":
                continue
            bdir = os.path.join(sdir, ts)
            meta_file = os.path.join(bdir, "metadata.json")
            if os.path.exists(meta_file):
                with open(meta_file, "r", encoding="utf-8") as f:
                    try:
                        m = json.load(f)
                        m["dir_path"] = bdir
                        backups.append(m)
                    except Exception:
                        pass
    return backups


if __name__ == "__main__":
    print(f"Backup Root Directory: {BACKUP_ROOT}")
    backups = list_all_backups()
    print(f"Total backups found: {len(backups)}")
    for b in backups:
        print(f" - {b.get('slug')} | {b.get('title')} | {b.get('backup_timestamp')}")
