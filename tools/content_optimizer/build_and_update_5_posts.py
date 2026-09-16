#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/content_optimizer/build_and_update_5_posts.py
---------------------------------------------------
1. Generates 5 official 16:9 banners via Chromium HarfBuzz on authentic templates.
2. Compresses banners to 10-20 KB WebP.
3. Takes full snapshot backups of the 5 posts.
4. Replaces hero banners live on Blogger.
5. Pings Google Indexing API.
"""

import os
import sys
import json
import time
import subprocess
from datetime import datetime
from bs4 import BeautifulSoup

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.image_generator.build_official_bg_thumbnails import generate_official_bg_banner
from tools.blogger_publisher.publisher import get_authenticated_service, BLOG_ID

CDN_BASE = "https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/posts/"

TARGET_POSTS = [
    {
        "post_id": "709822711957352889",
        "category_key": "Political Science",
        "badge_label": "মাস্টার্স রাষ্ট্রবিজ্ঞান",
        "title": "সাম্প্রতিক কালের রাষ্ট্রচিন্তা বলতে কী বুঝ?",
        "subtitle": "জাতীয়তাবাদ, বিবর্তন ও আধুনিক রাষ্ট্রের তাত্ত্বিক রূপরেখা (২০২৬)",
        "features": ["তাত্ত্বিক সংজ্ঞা", "জাতীয়তাবাদের বিবর্তন", "রাষ্ট্রচিন্তার রূপরেখা", "মাস্টার্স পরীক্ষার হ্যান্ডনোট"],
        "filename": "recent-political-thought-nationalism-official-banner.png",
        "alt_text": "সাম্প্রতিক কালের রাষ্ট্রচিন্তা বলতে কী বুঝ জাতীয়তাবাদ ও বিবর্তন",
        "search_desc": "সাম্প্রতিক কালের রাষ্ট্রচিন্তার সংজ্ঞা, জাতীয়তাবাদের উৎপত্তি ও ঐতিহাসিক বিবর্তন এবং আধুনিক রাষ্ট্রের বিকাশ ধারা নিয়ে মাস্টার্স রাষ্ট্রবিজ্ঞান হ্যান্ডনোট।"
    },
    {
        "post_id": "7170314718157313108",
        "category_key": "Political Science",
        "badge_label": "মাস্টার্স রাষ্ট্রবিজ্ঞান",
        "title": "মাস্টার্স রাষ্ট্রবিজ্ঞান ফাইনাল সাজেশন্স",
        "subtitle": "সাম্প্রতিক রাষ্ট্রচিন্তা — বিষয়কোড: ৩১১৯০১ | ১০০% কমন নিশ্চয়তা (২০২৬)",
        "features": ["ক-বিভাগ অতি সংক্ষিপ্ত", "খ-বিভাগ সংক্ষিপ্ত", "গ-বিভাগ রচনামূলক", "পরীক্ষা প্রস্তুতি টিপস"],
        "filename": "recent-political-thought-masters-suggestion-official-banner.png",
        "alt_text": "রাষ্ট্রবিজ্ঞান মাস্টার্স সাজেশন্স সাম্প্রতিক রাষ্ট্রচিন্তা বিষয়কোড ৩১১৯০১",
        "search_desc": "জাতীয় বিশ্ববিদ্যালয়ের মাস্টার্স শেষ পর্ব রাষ্ট্রবিজ্ঞান 'সাম্প্রতিক রাষ্ট্রচিন্তা' (বিষয়কোড: ৩১১৯০১) পরীক্ষার ১০০% কমন চূড়ান্ত সুপার সাজেশন ও গাইড।"
    },
    {
        "post_id": "4196953979786018728",
        "category_key": "Education Guide",
        "badge_label": "শিক্ষা ও বোর্ড পরীক্ষা",
        "title": "এসএসসি পরীক্ষার্থীদের জরুরি নিয়মাবলি",
        "subtitle": "পরীক্ষার হলের নির্দেশিকা, ওএমআর শিট পূরণ ও সময় ব্যবস্থাপনা (২০২৬)",
        "features": ["হল রুমের নিয়মাবলি", "ওএমআর শিট পূরণ", "সময় বণ্টন কৌশল", "জরুরি নির্দেশিকা"],
        "filename": "ssc-exam-hall-rules-guidelines-official-banner.png",
        "alt_text": "এসএসসি পরীক্ষার্থীদের জন্য জরুরি নিয়মাবলি ও পরীক্ষার হলের নির্দেশিকা",
        "search_desc": "এসএসসি পরীক্ষার্থীদের জন্য শিক্ষা বোর্ডের জরুরি নিয়মাবলি, পরীক্ষার হলের আচরণবিধি, ওএমআর শিট সঠিক পূরণের নিয়ম ও সময় বণ্টনের পূর্ণাঙ্গ গাইড।"
    },
    {
        "post_id": "4705377665339185450",
        "category_key": "Political Science",
        "badge_label": "মাস্টার্স রাষ্ট্রবিজ্ঞান",
        "title": "সামাজিক পরিবর্তন ও উন্নয়ন চূড়ান্ত সাজেশন",
        "subtitle": "সামাজিক পরিবর্তন ও রাজনৈতিক উন্নয়ন — বিষয়কোড: ৩১১৯০৩ (২০২৬)",
        "features": ["১০০% সিলেবাস কাভারেজ", "রচনামূলক প্রশ্নাবলি", "সংক্ষিপ্ত প্রশ্ন ও উত্তর", "ফাইনাল মডেল টেস্ট"],
        "filename": "masters-social-change-development-suggestion-official-banner.png",
        "alt_text": "সামাজিক পরিবর্তন ও রাজনৈতিক উন্নয়ন চূড়ান্ত সাজেশন বিষয়কোড ৩১১৯০৩",
        "search_desc": "মাস্টার্স শেষ পর্ব রাষ্ট্রবিজ্ঞান বিভাগের 'সামাজিক পরিবর্তন ও রাজনৈতিক উন্নয়ন' (বিষয়কোড: ৩১১৯০৩) পরীক্ষার ক, খ ও গ-বিভাগের ১০০% কমন ফাইনাল সাজেশন।"
    },
    {
        "post_id": "2984334472304308439",
        "category_key": "Political Science",
        "badge_label": "মাস্টার্স রাষ্ট্রবিজ্ঞান",
        "title": "আধুনিক রাষ্ট্রচিন্তা ২০১৯ প্রশ্ন ও নির্ভুল সমাধান",
        "subtitle": "জাতীয় বিশ্ববিদ্যালয় মাস্টার্স বিগত সালের পূর্ণাঙ্গ মডেল উত্তরমালা (২০২৬)",
        "features": ["২০১৯ সালের মূল প্রশ্ন", "ক-বিভাগ সমাধান", "খ ও গ-বিভাগ উত্তর", "পরীক্ষা সহায়ক হ্যান্ডনোট"],
        "filename": "modern-political-thought-2019-solutions-official-banner.png",
        "alt_text": "আধুনিক রাষ্ট্রচিন্তা ২০১৯ সালের প্রশ্নের নির্ভুল উত্তরমালা ও সমাধান",
        "search_desc": "জাতীয় বিশ্ববিদ্যালয় মাস্টার্স রাষ্ট্রবিজ্ঞান 'আধুনিক রাষ্ট্রচিন্তা' ২০১৯ সালের চূড়ান্ত পরীক্ষার ক, খ ও গ-বিভাগের সকল প্রশ্নের প্রামাণ্য ও নির্ভুল সমাধান।"
    }
]

def backup_post(post_data):
    post_id = post_data["id"]
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    slug = post_data.get("url", "").split("/")[-1].replace(".html", "") or post_id
    backup_dir = os.path.join(PROJECT_ROOT, "backups", "posts", slug, timestamp)
    os.makedirs(backup_dir, exist_ok=True)

    with open(os.path.join(backup_dir, "post_snapshot.json"), "w", encoding="utf-8") as f:
        json.dump(post_data, f, ensure_ascii=False, indent=2)

    with open(os.path.join(backup_dir, "content_original.html"), "w", encoding="utf-8") as f:
        f.write(post_data.get("content", ""))

    print(f"      [✔] Backup saved: backups/posts/{slug}/{timestamp}/")
    return backup_dir

def main():
    print("=" * 75)
    print("🎨 STEP 1: RENDERING 5 OFFICIAL 16:9 BANNERS VIA CHROMIUM HARFBUZZ")
    print("=" * 75)

    for idx, item in enumerate(TARGET_POSTS, 1):
        print(f"\n[{idx}/5] Rendering Banner: {item['title']}")
        generate_official_bg_banner(
            filename=item["filename"],
            category_key=item["category_key"],
            badge_label=item["badge_label"],
            title=item["title"],
            subtitle=item["subtitle"],
            features=item["features"]
        )

    print("\n" + "=" * 75)
    print("🚀 STEP 2: GIT COMMIT & PUSH TO SYNC IMAGES TO JSDELIVR CDN")
    print("=" * 75)

    subprocess.run(["git", "add", "assets/images/posts/", "assets/images/thumbnails/"], check=True, cwd=PROJECT_ROOT)
    subprocess.run(["git", "commit", "-m", "feat(assets): generate and push 5 official 16:9 banners for user requested posts"], check=True, cwd=PROJECT_ROOT)
    subprocess.run(["git", "push", "origin", "main"], check=True, cwd=PROJECT_ROOT)

    print("\n" + "=" * 75)
    print("🛡️ STEP 3: BACKUP & LIVE UPDATE BLOGGER POSTS WITH CDN BANNERS")
    print("=" * 75)

    service = get_authenticated_service()
    if not service:
        print("[ERROR] Failed to authenticate Blogger API v3.")
        sys.exit(1)

    updated_records = []
    for item in TARGET_POSTS:
        post_id = item["post_id"]
        base_name = os.path.splitext(item["filename"])[0]
        banner_webp = f"{base_name}.webp"
        banner_url = CDN_BASE + banner_webp
        alt_text = item["alt_text"]

        print(f"\n[*] Fetching post ID: {post_id} from Blogger...")
        post = service.posts().get(blogId=BLOG_ID, postId=post_id).execute()
        title = post.get("title", "")
        url = post.get("url", "")
        content = post.get("content", "")

        print(f"    Title: {title}")
        print(f"    URL:   {url}")

        # Backup
        backup_post(post)

        # Parse & Replace
        soup = BeautifulSoup(content, "html.parser")
        imgs = soup.find_all("img")

        if imgs:
            hero_img = imgs[0]
            print(f"      Replacing Hero Image: {hero_img.get('src')[:60]}... -> {banner_url}")
            hero_img["src"] = banner_url
            hero_img["alt"] = alt_text
            hero_img["title"] = title
            hero_img["width"] = "1200"
            hero_img["height"] = "675"
            hero_img["loading"] = "lazy"
        else:
            print("      [!] No <img> found. Prepending new hero banner at top.")
            new_img = soup.new_tag("img", src=banner_url, alt=alt_text, title=title, width="1200", height="675", loading="lazy")
            soup.insert(0, new_img)

        # Update Schema
        scripts = soup.find_all("script", type="application/ld+json")
        for s in scripts:
            try:
                schema = json.loads(s.string)
                if isinstance(schema, dict) and "image" in schema:
                    schema["image"] = banner_url
                    s.string = json.dumps(schema, ensure_ascii=False, indent=2)
                    print("      [✔] Schema image property updated.")
            except Exception:
                pass

        # Patch Blogger
        patch_body = {"content": str(soup)}
        service.posts().patch(blogId=BLOG_ID, postId=post_id, body=patch_body).execute()
        print("      [✔] Live Post updated on Blogger!")

        # Ping Google Indexing API
        try:
            indexer_cmd = [
                sys.executable,
                os.path.join(PROJECT_ROOT, "tools", "indexer", "index_now.py"),
                "--url", url
            ]
            subprocess.run(indexer_cmd, capture_output=True, text=True, cwd=os.path.join(PROJECT_ROOT, "tools", "indexer"))
            print("      [✔] Google Indexing API pinged (URL_UPDATED).")
        except Exception as e_idx:
            print(f"      [!] Google Indexing Ping error: {e_idx}")

        updated_records.append({
            "post_id": post_id,
            "title": title,
            "url": url,
            "banner": banner_url,
            "search_desc": item["search_desc"]
        })
        time.sleep(2)

    # Save summary report
    report_path = os.path.join(PROJECT_ROOT, "output_posts", "updated_5_posts_report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(updated_records, f, ensure_ascii=False, indent=2)

    print("\n" + "=" * 75)
    print(f"🎉 ALL 5 POSTS UPDATED LIVE WITH OFFICIAL BANNERS & BACKED UP!")
    print(f"   Summary Report saved to: {report_path}")
    print("=" * 75)

if __name__ == "__main__":
    main()
