#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/build_5_audit_posts.py
-----------------------------------
End-to-end master orchestrator:
1. Generates 5 16:9 10-20 KB WebP thumbnails
2. Generates 5 comprehensive academic posts from 'Publication Books' data
3. Validates each with PreFlightChecker
4. Posts each to WordPress REST API as DRAFT (idempotent create or update)
"""

import os
import sys
import json
import io
import re
from bs4 import BeautifulSoup

try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.image_generator.thumbnail_generator import generate_thumbnail
from tools.wp_publisher.publisher import WordPressPublisher
from tools.governance.pre_flight_checker import PreFlightChecker

from tools.post_builders.post_01_builder import get_post_data as get_p1
from tools.post_builders.post_02_builder import get_post_data as get_p2
from tools.post_builders.post_03_builder import get_post_data as get_p3
from tools.post_builders.post_04_builder import get_post_data as get_p4
from tools.post_builders.post_05_builder import get_post_data as get_p5

OUTPUT_DIR = os.path.join(PROJECT_ROOT, "output_posts")
os.makedirs(OUTPUT_DIR, exist_ok=True)

THUMBNAIL_DIR = os.path.join(PROJECT_ROOT, "assets", "images", "thumbnails")
os.makedirs(THUMBNAIL_DIR, exist_ok=True)

POSTS_CONFIG = [
    {
        "id": 1,
        "title": "অনার্স ৩য় বর্ষ নিরীক্ষা ও নিশ্চয়তা সাজেশন 2026: Best Complete Exam Guide",
        "subtitle": "National University BBA 3rd Year Audit & Assurance Final Suggestion 2026",
        "thumb_name": "audit_post_1_banner.png",
        "builder": get_p1,
    },
    {
        "id": 2,
        "title": "নিরীক্ষা প্রতিবেদনের প্রকারভেদ: Best Complete Guide 2026 (ISA 700 ও 705 নমুনা ছক)",
        "subtitle": "Audit Report Types, Components & Specimen under ISA 700 & 705",
        "thumb_name": "audit_post_2_banner.png",
        "builder": get_p2,
    },
    {
        "id": 3,
        "title": "নিরীক্ষকের আইনগত দায়: Best Complete Legal Analysis 2026 (দেওয়ানি ও ফৌজদারি দায়)",
        "subtitle": "Auditor Legal Liability under Companies Act 1994 & Landmark Cases",
        "thumb_name": "audit_post_3_banner.png",
        "builder": get_p3,
    },
    {
        "id": 4,
        "title": "কোম্পানি নিরীক্ষকের অধিকার ও কর্তব্য: Best Complete Guide 2026 (ধারা ২১৩ ও অপসারণ)",
        "subtitle": "Rights, Duties & Removal of Company Auditor under Section 213",
        "thumb_name": "audit_post_4_banner.png",
        "builder": get_p4,
    },
    {
        "id": 5,
        "title": "নিরীক্ষা ও অনুসন্ধানের মধ্যে পার্থক্য: Best Complete Comparison 2026 (উদ্দেশ্য ও ছক)",
        "subtitle": "Difference between Auditing & Investigation with Objectives 2026",
        "thumb_name": "audit_post_5_banner.png",
        "builder": get_p5,
    }
]

def main():
    print("==================================================================")
    print(" HELPTRICKBD: 5-POST GENERATION & DRAFT CREATION PIPELINE ")
    print("==================================================================")

    publisher = WordPressPublisher()
    manifest = []

    for cfg in POSTS_CONFIG:
        p_id = cfg["id"]
        print(f"\n------------------------------------------------------------------")
        print(f"[*] Processing Post {p_id}: {cfg['title']}")
        print(f"------------------------------------------------------------------")

        # 1. Generate Thumbnail
        thumb_out = cfg["thumb_name"]
        print(f"[*] Generating Thumbnail: {thumb_out}...")
        webp_path = generate_thumbnail(
            title=cfg["title"],
            category="Education Guide",
            subtitle=cfg["subtitle"],
            output_filename=thumb_out
        )
        print(f"[+] Thumbnail ready at: {webp_path}")

        # 2. Build HTML and Metadata
        html_content, meta_data = cfg["builder"](webp_path)
        slug = meta_data["slug"]

        html_file = os.path.join(OUTPUT_DIR, f"{slug}.html")
        meta_file = os.path.join(OUTPUT_DIR, f"{slug}_meta.json")

        with open(html_file, "w", encoding="utf-8") as f:
            f.write(html_content)

        with open(meta_file, "w", encoding="utf-8") as f:
            json.dump(meta_data, f, ensure_ascii=False, indent=2)

        print(f"[+] Saved HTML: {html_file}")
        print(f"[+] Saved Meta: {meta_file}")

        # 3. Pre-Flight Quality Check
        print(f"[*] Running Pre-Flight Quality Checker...")
        checker = PreFlightChecker(html_file, meta_file)
        is_clean = checker.run_all()
        checker.print_report()

        if not is_clean:
            print(f"[CRITICAL] Pre-flight failed for Post {p_id} with {len(checker.errors)} errors! Aborting.")
            sys.exit(1)

        # 4. Upload Featured Image to WordPress Media Library
        print(f"[*] Uploading Featured Image to WordPress Media Library...")
        featured_media_id = publisher.upload_featured_image(
            file_path=webp_path,
            alt_text=meta_data["focus_keyword"],
            title=meta_data["title"]
        )
        print(f"[+] Featured Media ID: {featured_media_id}")

        # 5. Map Categories and Tags
        cat_ids = []
        for cname in meta_data.get("categories", []):
            cid = publisher.get_or_create_category(cname)
            if cid:
                cat_ids.append(cid)

        tag_ids = []
        for tname in meta_data.get("tags", []):
            tid = publisher.get_or_create_tag(tname)
            if tid:
                tag_ids.append(tid)

        # 6. Publish or Update in WordPress as DRAFT
        print(f"[*] Checking if post with slug '{slug}' already exists in WordPress...")
        existing_res = publisher.client.get("posts", params={"slug": slug, "status": "any"})
        existing_posts = existing_res.json() if existing_res.status_code == 200 else []

        focus_kw = meta_data.get("rank_math_focus_keyword") or meta_data["focus_keyword"]
        meta_dict = {
            "rank_math_title": meta_data["title"],
            "rank_math_description": meta_data["meta_description"],
            "rank_math_focus_keyword": focus_kw,
            "rank_math_robots": "index, follow, max-snippet:-1, max-video-preview:-1, max-image-preview:large",
            "rank_math_canonical_url": ""
        }

        if existing_posts and len(existing_posts) > 0:
            wp_id = existing_posts[0]["id"]
            print(f"[*] Found existing post ID: {wp_id}. Updating content & metadata...")
            update_payload = {
                "title": meta_data["title"],
                "content": html_content,
                "status": "draft",
                "categories": cat_ids,
                "tags": tag_ids,
                "meta": meta_dict
            }
            if featured_media_id:
                update_payload["featured_media"] = featured_media_id
            
            pub_res = publisher.update_post(wp_id, **update_payload)
            wp_link = existing_posts[0].get("link", f"https://www.helptrickbd.com/?p={wp_id}")
            wp_edit_link = f"{publisher.client.base_url}/wp-admin/post.php?post={wp_id}&action=edit"
        else:
            print(f"[*] Creating Post in WordPress (Status: DRAFT)...")
            seo_meta = {
                "title": meta_data["title"],
                "seo_title": meta_data["title"],
                "seo_description": meta_data["meta_description"],
                "focus_keyword": focus_kw,
                "canonical_url": f"https://www.helptrickbd.com/{slug}/",
                "robots": ["index", "follow"]
            }
            result = publisher.create_post(
                title=meta_data["title"],
                content=html_content,
                slug=slug,
                status="draft",
                featured_media_id=featured_media_id,
                categories=cat_ids,
                tags=tag_ids,
                seo_meta=seo_meta
            )
            wp_id = result.get("id")
            wp_link = result.get("url") or f"https://www.helptrickbd.com/?p={wp_id}"
            wp_edit_link = result.get("edit_url") or f"{publisher.client.base_url}/wp-admin/post.php?post={wp_id}&action=edit"

        print(f"[SUCCESS] Post {p_id} successfully saved as DRAFT in WordPress!")
        print(f"  -> WordPress Post ID: {wp_id}")
        print(f"  -> Draft Preview URL: {wp_link}")
        print(f"  -> WP Admin Edit URL: {wp_edit_link}")

        soup = BeautifulSoup(html_content, 'html.parser')
        word_count = len(re.findall(r'\S+', soup.get_text()))

        manifest.append({
            "id": p_id,
            "wp_id": wp_id,
            "title": meta_data["title"],
            "slug": slug,
            "focus_keyword": meta_data["focus_keyword"],
            "draft_preview_url": wp_link,
            "wp_admin_edit_url": wp_edit_link,
            "featured_media_id": featured_media_id,
            "categories": meta_data["categories"],
            "word_count": word_count
        })

    manifest_file = os.path.join(OUTPUT_DIR, "5_audit_posts_draft_manifest.json")
    with open(manifest_file, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    print("\n==================================================================")
    print(" ALL 5 AUDIT & ASSURANCE POSTS CREATED AS DRAFT SUCCESSFULLY! ")
    print(f" Manifest saved: {manifest_file}")
    print("==================================================================")

if __name__ == "__main__":
    main()
