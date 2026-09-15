#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/content_optimizer/live_purge_all_emojis.py
-------------------------------------------------
Comprehensive, 100% Live Emoji & Robotic Artifact Purger for Blogger.
1. Connects directly to Google Blogger API v3.
2. Scans all live posts on HelpTrickBD.
3. Completely purges every single decorative emoji from post titles and body content:
   (📌, 👉, 📢, ⏱️, ✅, 🎓, 📘, 💬, 💡, ⚠️, ❓, 🔗, 📚, 📑, ✨, ⭐, ⚡, 💻, 💾, 🏢, 🌐, 🔒, 🛡️, 📝, 📊, etc.)
4. Removes redundant custom social share boxes (<div class="ht-social-share-box"> and "আপনার সহপাঠী ও বন্ধুদের সাথে শেয়ার করুন").
5. Patches each modified post live on Blogger.
6. Submits all updated URLs to Google Indexing API.
"""

import os
import sys
import re
import json
import subprocess
from bs4 import BeautifulSoup, NavigableString

if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, PROJECT_ROOT)

from tools.blogger_publisher.update_post import get_authenticated_service, BLOG_ID

# Comprehensive Regex covering all unicode emojis, surrogate pairs, and decorative symbols
EMOJI_REGEX = re.compile(
    r"[\U00010000-\U0010FFFF\uD800-\uDBFF\uDC00-\uDFFF\u2600-\u26FF\u2700-\u27BF\uFE00-\uFE0F]"
    r"|[📌📊📝⚡⭐🛡️🔒🌐🏢💾💻☁️✨👉📘📢⏱️✅🎓💬💡⚠️❓🔗📚📑❶❷❸❹❺❻❼❽❾❿▶️◀️⏩⏪🔹🔸▪️▫️]"
)

def clean_string_of_emojis(text: str) -> str:
    if not text:
        return ""
    cleaned = EMOJI_REGEX.sub("", text)
    cleaned = re.sub(r"\s+", " ", cleaned)
    cleaned = cleaned.replace(" :", ":").replace(" | |", " |")
    return cleaned.strip()

def clean_post_soup(soup: BeautifulSoup) -> int:
    """Recursively purges emojis and removes redundant share boxes from BeautifulSoup tree."""
    emojis_removed = 0
    
    # 1. Remove redundant social share boxes
    share_boxes = soup.find_all("div", class_=lambda c: c and "ht-social-share-box" in c)
    for box in share_boxes:
        box.decompose()
        
    for p in soup.find_all("p"):
        txt = p.get_text()
        if "আপনার সহপাঠী ও বন্ধুদের সাথে শেয়ার করুন" in txt or "Share this helpful guide" in txt:
            parent = p.find_parent("div")
            if parent and ("whatsapp.com" in parent.decode() or "facebook.com" in parent.decode()):
                parent.decompose()
            else:
                p.decompose()

    # 2. Clean text in all navigable strings
    for element in soup.find_all(text=True):
        if isinstance(element, NavigableString) and not element.parent.name in ['script', 'style']:
            original = str(element)
            matches = EMOJI_REGEX.findall(original)
            if matches:
                emojis_removed += len(matches)
                cleaned = EMOJI_REGEX.sub("", original)
                # Replace double spaces
                cleaned = re.sub(r"[ \t]+", " ", cleaned)
                element.replace_with(cleaned)
                
    # 3. Clean TOC title and styling
    for toc in soup.find_all("div", class_=lambda c: c and "ht-toc-container" in c):
        title_span = toc.find("span")
        if title_span:
            txt = title_span.get_text()
            if bool(re.search(r'[\u0980-\u09FF]', txt)):
                title_span.string = "সূচিপত্র (গুরুত্বপূর্ণ বিষয়বস্তু)"
            else:
                title_span.string = "Table of Contents"

    return emojis_removed

def main():
    print("=" * 70)
    print("🧹 HelpTrickBD — Universal Live Emoji & Pattern Purge Engine")
    print("=" * 70)

    service = get_authenticated_service()
    if not service:
        print("[!] Error: Could not authenticate Blogger API.")
        return

    # Fetch all live posts
    print("[*] Retrieving all live posts from Blogger API...")
    posts_res = service.posts().list(blogId=BLOG_ID, maxResults=150, fetchBodies=True).execute()
    items = posts_res.get('items', [])
    print(f"[*] Retrieved {len(items)} posts from live blog.\n")

    updated_posts = []

    for idx, item in enumerate(items):
        post_id = item["id"]
        post_title = item.get("title", "")
        post_url = item.get("url", "")
        content = item.get("content", "")

        # Clean title
        title_emojis = len(EMOJI_REGEX.findall(post_title))
        clean_title = clean_string_of_emojis(post_title)

        # Clean content
        soup = BeautifulSoup(content, 'html.parser')
        content_emojis = clean_post_soup(soup)

        total_emojis = title_emojis + content_emojis
        has_share_box = ("ht-social-share-box" in content) or ("আপনার সহপাঠী ও বন্ধুদের সাথে শেয়ার করুন" in content)

        if total_emojis > 0 or has_share_box or (clean_title != post_title):
            print(f"[{idx+1}/{len(items)}] 🧹 Purging: {post_title}")
            print(f"    • Emojis removed: {total_emojis} (Title: {title_emojis}, Content: {content_emojis})")
            if has_share_box:
                print("    • Redundant share box purged.")

            new_content = str(soup)
            patch_body = {
                "title": clean_title,
                "content": new_content
            }
            
            try:
                updated = service.posts().patch(blogId=BLOG_ID, postId=post_id, body=patch_body).execute()
                print(f"    [✔] Successfully updated live on Blogger! URL: {post_url}\n")
                updated_posts.append({
                    "id": post_id,
                    "title": clean_title,
                    "url": post_url,
                    "emojis": total_emojis
                })
            except Exception as e:
                print(f"    [!] Error updating post {post_id}: {e}\n")

    print("=" * 70)
    print(f"🎉 Purge Completed! Total posts cleaned live: {len(updated_posts)}")
    print(f"   Total emojis eliminated: {sum(p['emojis'] for p in updated_posts)}")
    print("=" * 70)

    if updated_posts:
        # Submit to Google Indexing API
        index_file = os.path.join(PROJECT_ROOT, "tools", "indexer", "emojis_purged_urls.txt")
        with open(index_file, "w", encoding="utf-8") as f:
            for p in updated_posts:
                f.write(p["url"] + "\n")

        print(f"\n📡 Submitting {len(updated_posts)} Cleaned URLs to Google Indexing API...")
        res = subprocess.run(["python", os.path.join(PROJECT_ROOT, "tools", "indexer", "index_now.py"), "--file", index_file], capture_output=True, text=True)
        print(res.stdout)
        if res.stderr:
            print("[!] Indexing API Stderr:", res.stderr)

    # Also clean local revived files to keep git repo 100% in sync
    print("\n[*] Synchronizing local output_posts/ files...")
    revived_dir = os.path.join(PROJECT_ROOT, "output_posts", "revived_posts")
    if os.path.exists(revived_dir):
        for fname in os.listdir(revived_dir):
            if fname.endswith(".html"):
                fpath = os.path.join(revived_dir, fname)
                with open(fpath, "r", encoding="utf-8") as f:
                    c = f.read()
                soup_local = BeautifulSoup(c, "html.parser")
                clean_post_soup(soup_local)
                with open(fpath, "w", encoding="utf-8") as f:
                    f.write(str(soup_local))
    print("[✔] Local HTML files synchronized.")

if __name__ == "__main__":
    main()
