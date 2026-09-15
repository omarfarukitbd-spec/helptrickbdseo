#!/usr/bin/env python3
"""
tools/content_optimizer/publish_thin_fixes.py
HelpTrickBD Batch Updater & Dwell Time Optimizer for Thin Posts.

Takes local rich revived posts, injects engagement boosters
(SolaimanLipi reading time badge, scroll progress bar, TOC, viral share),
and publishes updates directly to Blogger via Blogger API v3.
"""

import os
import sys
import json
import time

try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.blogger_publisher.update_post import get_authenticated_service, BLOG_ID
from tools.engagement_booster.dwell_optimizer import optimize_post_engagement

TARGET_FILES = [
    "ishwar-chandra-vidyasagar-social-reform-contribution.html",
    "government-political-parties-bangladesh-analysis.html",
    "computer-types-classification-part4.html",
    "recent-political-thought-suggestion-2024.html",
    "honours-political-science-book-list.html",
    "computer-generations-features-part3.html",
    "computer-history-inventions-part2.html",
    "what-is-statesmanship.html",
    "bangladeshe-shilpo-jatiyokoron-shomossha.html",
    "bangladesh-livestock-resources-research-institutes.html",
    "masters-social-change-and-political-development-suggestions.html",
    "role-of-ngos-in-womens-empowerment-benefits.html",
    "samajikikorone-khelar-sathir-bhumika.html",
    "simple-guide-to-job-and-bcs-preparation.html",
    "what-is-meant-by-recent-nationalism.html",
    "what-is-political-economy-definition-concept.html"
]


def update_all_thin_posts():
    service = get_authenticated_service()
    if not service:
        print("[!] Blogger API authentication failed.")
        sys.exit(1)

    print("\n=======================================================")
    print("  HelpTrickBD Batch Thin Post Reviver & Dwell Booster")
    print("=======================================================")

    success_count = 0
    updated_urls = []

    for filename in TARGET_FILES:
        html_path = os.path.join(PROJECT_ROOT, "output_posts", "revived_posts", filename)
        meta_path = html_path.replace(".html", "_metadata.json")

        if not os.path.exists(html_path) or not os.path.exists(meta_path):
            print(f"[!] Skipping {filename} (File or metadata missing)")
            continue

        with open(meta_path, "r", encoding="utf-8") as mf:
            meta = json.load(mf)

        post_id = meta.get("post_id")
        title = meta.get("title")
        labels = meta.get("labels", [])

        if not post_id:
            print(f"[!] No post_id in metadata for {filename}")
            continue

        print(f"\n[*] Processing: {title[:40]}... (ID: {post_id})")

        with open(html_path, "r", encoding="utf-8") as hf:
            raw_html = hf.read()

        # Step 1: Inject Dwell Time and Engagement boosters
        optimized_html, stats = optimize_post_engagement(raw_html)
        print(f"    - Injected Dwell Boosters: Read Time {stats['estimated_minutes']}m ({stats['word_count']} words), TOC: {stats['headings_count']} headings")

        # Step 2: Update live post on Blogger
        try:
            existing_post = service.posts().get(blogId=BLOG_ID, postId=post_id).execute()
            existing_post["content"] = optimized_html
            if title:
                existing_post["title"] = title
            if labels:
                # Merge existing and new labels cleanly
                current_labels = existing_post.get("labels", [])
                combined_labels = list(set(current_labels + labels))
                existing_post["labels"] = combined_labels

            updated_post = service.posts().update(
                blogId=BLOG_ID,
                postId=post_id,
                body=existing_post
            ).execute()

            live_url = updated_post.get("url")
            updated_urls.append(live_url)
            print(f"    [+] Updated successfully on Blogger! -> {live_url}")
            success_count += 1

            # Save the optimized HTML back to local file
            with open(html_path, "w", encoding="utf-8") as hf:
                hf.write(optimized_html)

            time.sleep(1.5)  # Respect API rate limits

        except Exception as e:
            print(f"    [!] Failed to update {post_id}: {e}")

    print("\n=======================================================")
    print(f"  [✓] Completed: {success_count}/{len(TARGET_FILES)} posts successfully updated on Blogger!")
    print("=======================================================\n")

    # Save list of updated URLs for Google Indexing
    urls_file = os.path.join(PROJECT_ROOT, "tools", "indexer", "updated_thin_fixed_urls.txt")
    with open(urls_file, "w", encoding="utf-8") as uf:
        for u in updated_urls:
            uf.write(u + "\n")
    print(f"[+] Saved {len(updated_urls)} live URLs to {urls_file}")


if __name__ == "__main__":
    update_all_thin_posts()
