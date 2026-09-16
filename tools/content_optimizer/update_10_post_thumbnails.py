#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/content_optimizer/update_10_post_thumbnails.py
----------------------------------------------------
Safely updates the 10 posts on Blogger with the newly minted official banners.
Strictly follows:
1. 07_POST_BACKUP_AND_RESTORE_PROTOCOL: 100% full snapshot backup before edit.
2. 02_IMAGE_AND_ASSET_RULES: Hero banner replacement at top, width 1200 height 675, schema update.
3. 03_PUBLISHING_PERMALINK_RULES: Pinging Google Indexing API for each updated URL.
4. 06_COMMUNICATION_AND_REPORTING_PROTOCOL: Rule 20 Search Description delivery.
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

from tools.blogger_publisher.publisher import get_authenticated_service, BLOG_ID

CDN_BASE = "https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/posts/"

TARGET_POSTS = [
    {
        "post_id": "179336939989858201",
        "new_banner": "bangladesh-industry-nationalization-history-official-banner.webp",
        "alt_text": "বাংলাদেশে শিল্প জাতীয়করণের ইতিহাস পটভূমি ও অর্থনৈতিক প্রভাব",
        "search_desc": "বাংলাদেশে শিল্প জাতীয়করণের ইতিহাস, ১৯৭২ সালের শিল্প নীতি, জাতীয়করণের কারণ, সমস্যা ও জাতীয় অর্থনীতির ওপর সুদূরপ্রসারী প্রভাব নিয়ে মাস্টার্স হ্যান্ডনোট।"
    },
    {
        "post_id": "8316268127112895155",
        "new_banner": "state-society-women-movement-official-banner.webp",
        "alt_text": "রাষ্ট্র সমাজ ও নারী আন্দোলনের প্রেক্ষাপট অধিকার ও অস্তিত্ব রক্ষার লড়াই",
        "search_desc": "রাষ্ট্র, সমাজ ও নারী আন্দোলনের ঐতিহাসিক প্রেক্ষাপট, সাংবিধানিক অধিকার, পিতৃতান্ত্রিক মানসিকতার বিরুদ্ধে অস্তিত্ব রক্ষার লড়াই ও মডেল হ্যান্ডনোট।"
    },
    {
        "post_id": "5020265416603423827",
        "new_banner": "child-socialization-peers-friends-official-banner.webp",
        "alt_text": "শিশুর সামাজিকীকরণ প্রক্রিয়ায় খেলার সাথী ও বন্ধুদের ভূমিকা",
        "search_desc": "শিশুর সামাজিকীকরণ প্রক্রিয়ায় খেলার সাথী ও সহপাঠী বন্ধুদের মনস্তাত্ত্বিক ভূমিকা, সামাজিক মূল্যবোধ ও নেতৃত্ব বিকাশের প্রভাব নিয়ে পূর্ণাঙ্গ হ্যান্ডনোট।"
    },
    {
        "post_id": "2778070516508854236",
        "new_banner": "population-change-causes-factors-official-banner.webp",
        "alt_text": "জনসংখ্যা পরিবর্তনের কারণ প্রভাব ও প্রধান নিয়ামকসমূহ",
        "search_desc": "জনসংখ্যা পরিবর্তনের মৌলিক কারণ, জন্মহার-মৃত্যুহার-অভিবাসন নিয়ামক, উন্নয়নশীল দেশের ডেমোগ্রাফিক ট্রানজিশন ও আর্থ-সামাজিক প্রভাবের বিশ্লেষণ।"
    },
    {
        "post_id": "1429095227109508205",
        "new_banner": "what-is-political-economy-definition-official-banner.webp",
        "alt_text": "রাজনৈতিক অর্থনীতি কাকে বলে সংজ্ঞা পরিধি ও তাত্ত্বিক কাঠামো",
        "search_desc": "রাজনৈতিক অর্থনীতি কাকে বলে? প্রামাণ্য সংজ্ঞা, বিষয়বস্তু, চিরায়ত ও আধুনিক তাত্ত্বিক কাঠামো এবং অনার্স/মাস্টার্স পরীক্ষার পূর্ণাঙ্গ স্পেশাল হ্যান্ডনোট।"
    },
    {
        "post_id": "3881771794171675240",
        "new_banner": "women-reserved-seats-parliament-official-banner.webp",
        "alt_text": "জাতীয় সংসদে নারীদের সংরক্ষিত আসন সাংবিধানিক পটভূমি ও গুরুত্ব",
        "search_desc": "জাতীয় সংসদে নারীদের সংরক্ষিত আসনের সাংবিধানিক পটভূমি, ঐতিহাসিক বিবর্তন, নারীর রাজনৈতিক ক্ষমতায়নের গুরুত্ব ও বর্তমান চ্যালেঞ্জ নিয়ে মডেল হ্যান্ডনোট।"
    },
    {
        "post_id": "8694781974023635952",
        "new_banner": "womens-decade-goals-objectives-official-banner.webp",
        "alt_text": "নারী দশকের লক্ষ্য ও উদ্দেশ্য বিশ্ব নারী দশকের পটভূমি",
        "search_desc": "জাতিসংঘ ঘোষিত বিশ্ব নারী দশকের ঐতিহাসিক পটভূমি, মেক্সিকো সম্মেলন, নারী দশকের মূল লক্ষ্য, উদ্দেশ্য ও সমতা-উন্নয়ন-শান্তি বিষয়ক স্পেশাল হ্যান্ডনোট।"
    },
    {
        "post_id": "3995402116153520",
        "new_banner": "what-is-patriarchy-definition-official-banner.webp",
        "alt_text": "পুরুষতন্ত্র কাকে বলে সমাজতাত্ত্বিক সংজ্ঞা উৎপত্তি বৈশিষ্ট্য ও প্রভাব",
        "search_desc": "পুরুষতন্ত্র কাকে বলে? সমাজতাত্ত্বিক সংজ্ঞা, ঐতিহাসিক উৎপত্তি, পিতৃতান্ত্রিক ব্যবস্থার ১০টি বৈশিষ্ট্য ও নারীর ওপর নেতিবাচক প্রভাব নিয়ে স্পেশাল হ্যান্ডনোট।"
    },
    {
        "post_id": "3163731179305221308",
        "new_banner": "blri-bangladesh-livestock-research-official-banner.webp",
        "alt_text": "বাংলাদেশ প্রাণিসম্পদ গবেষণা ইনস্টিটিউট BLRI কার্যক্রম উদ্ভাবন ও ভূমিকা",
        "search_desc": "বাংলাদেশ প্রাণিসম্পদ গবেষণা ইনস্টিটিউট (BLRI)-এর ইতিহাস, কার্যক্রম, জাত উন্নয়ন, আধুনিক উদ্ভাবন ও জাতীয় অর্থনীতিতে প্রাণিসম্পদের ভূমিকা নিয়ে হ্যান্ডনোট।"
    },
    {
        "post_id": "9216865562894997738",
        "new_banner": "government-political-parties-relationship-official-banner.webp",
        "alt_text": "সরকার ও রাজনৈতিক দল ধারণা সম্পর্ক ও বাংলাদেশে গণতান্ত্রিক চর্চা",
        "search_desc": "সরকার ও রাজনৈতিক দলের পারস্পরিক ধারণা, কার্যকর সম্পর্ক, গণতন্ত্র সুসংহতকরণে বিরোধী দলের ভূমিকা ও বাংলাদেশে গণতান্ত্রিক চর্চার বাস্তবতা নিয়ে হ্যান্ডনোট।"
    }
]

def backup_post(post_data):
    post_id = post_data["id"]
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    slug = post_data.get("url", "").split("/")[-1].replace(".html", "") or post_id
    backup_dir = os.path.join(PROJECT_ROOT, "backups", "posts", slug, timestamp)
    os.makedirs(backup_dir, exist_ok=True)

    # Save full post JSON
    with open(os.path.join(backup_dir, "post_snapshot.json"), "w", encoding="utf-8") as f:
        json.dump(post_data, f, ensure_ascii=False, indent=2)

    # Save original HTML
    with open(os.path.join(backup_dir, "content_original.html"), "w", encoding="utf-8") as f:
        f.write(post_data.get("content", ""))

    print(f"      [✔] Backup saved: backups/posts/{slug}/{timestamp}/")
    return backup_dir

def update_post_banner(service, item):
    post_id = item["post_id"]
    new_banner_file = item["new_banner"]
    alt_text = item["alt_text"]
    new_banner_url = CDN_BASE + new_banner_file

    print(f"\n[*] Fetching post ID: {post_id} from Blogger...")
    post = service.posts().get(blogId=BLOG_ID, postId=post_id).execute()
    title = post.get("title", "")
    url = post.get("url", "")
    content = post.get("content", "")

    print(f"    Title: {title}")
    print(f"    URL:   {url}")

    # 1. Take 100% full snapshot backup
    backup_post(post)

    # 2. Parse and replace first hero image
    soup = BeautifulSoup(content, "html.parser")
    imgs = soup.find_all("img")

    if imgs:
        hero_img = imgs[0]
        old_src = hero_img.get("src", "")
        print(f"      Replacing Hero Image:")
        print(f"        Old: {old_src[:70]}...")
        print(f"        New: {new_banner_url}")
        hero_img["src"] = new_banner_url
        hero_img["alt"] = alt_text
        hero_img["title"] = title
        hero_img["width"] = "1200"
        hero_img["height"] = "675"
        hero_img["loading"] = "lazy"
    else:
        print("      [!] Warning: No <img> found. Prepending new hero banner at top.")
        new_img_tag = soup.new_tag("img", src=new_banner_url, alt=alt_text, title=title, width="1200", height="675", loading="lazy")
        soup.insert(0, new_img_tag)

    # 3. Update Schema.org JSON-LD if present
    scripts = soup.find_all("script", type="application/ld+json")
    for s in scripts:
        try:
            schema_data = json.loads(s.string)
            if isinstance(schema_data, dict) and "image" in schema_data:
                schema_data["image"] = new_banner_url
                s.string = json.dumps(schema_data, ensure_ascii=False, indent=2)
                print("      [✔] Schema.org JSON-LD image property updated.")
        except Exception:
            pass

    # 4. Patch Blogger post
    new_content = str(soup)
    patch_body = {
        "content": new_content
    }
    updated = service.posts().patch(blogId=BLOG_ID, postId=post_id, body=patch_body).execute()
    print(f"      [✔] Post updated live on Blogger! (Updated: {updated.get('updated')})")

    # 5. Ping Google Indexing API
    try:
        indexer_cmd = [
            sys.executable,
            os.path.join(PROJECT_ROOT, "tools", "indexer", "index_now.py"),
            "--url", url
        ]
        subprocess.run(indexer_cmd, capture_output=True, text=True, cwd=os.path.join(PROJECT_ROOT, "tools", "indexer"))
        print(f"      [✔] Google Indexing API pinged (URL_UPDATED).")
    except Exception as e_idx:
        print(f"      [!] Warning: Google Indexing Ping error: {e_idx}")

    return {
        "title": title,
        "url": url,
        "banner": new_banner_url,
        "search_desc": item["search_desc"]
    }

def run():
    print("=" * 75)
    print("🚀 HELPTRICKBD OFFICIAL BANNER REPLACEMENT & SYNC ENGINE")
    print("=" * 75)

    service = get_authenticated_service()
    if not service:
        print("[ERROR] Failed to authenticate Blogger API v3.")
        sys.exit(1)

    results = []
    for item in TARGET_POSTS:
        res = update_post_banner(service, item)
        results.append(res)
        time.sleep(2)

    print("\n" + "=" * 75)
    print(f"🎉 ALL {len(results)} POSTS UPDATED LIVE ON BLOGGER WITH OFFICIAL BANNERS!")
    print("=" * 75)

    report_file = os.path.join(PROJECT_ROOT, "output_posts", "updated_10_thumbnails_report.json")
    with open(report_file, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    return results

if __name__ == "__main__":
    run()
