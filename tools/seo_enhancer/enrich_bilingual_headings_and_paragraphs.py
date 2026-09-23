#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/seo_enhancer/enrich_bilingual_headings_and_paragraphs.py
Enriches Headings (H2, H3), Titles, and Overview Paragraphs across all Bangla 1st Paper Silo Posts
with high-ranking bilingual English/Bengali keywords for maximum Google ranking dominance.
"""

import os
import sys
import json
import time

if sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.blogger_publisher.publisher import get_authenticated_service, BLOG_ID
from tools.governance.pre_flight_checker import PreFlightChecker
from tools.indexer.pubsub_hub_pinger import ping_all_hubs
from tools.indexer.index_now import get_authenticated_service as get_idx_credentials, submit_url
from googleapiclient.discovery import build

POST_ENHANCEMENT_CONFIGS = [
    # Post 02: Prose Part 1
    {
        "post_id": "4356373537694150476",
        "html_file": "output_posts/ssc-bangla-1st-paper-prose-cq-suggestions-2027.html",
        "meta_file": "output_posts/ssc-bangla-1st-paper-prose-cq-suggestions-2027_metadata.json",
        "new_title": "SSC বাংলা ১ম পত্র গদ্যাংশ পর্ব-১ সৃজনশীল প্রশ্ন ও উত্তর ২০২৬-২০২৭ | প্রত্যুপকার, সুভা, বই পড়া ও নিরীহ বাঙালি CQ Solution",
        "replacements": [
            ("<h2>২. প্রত্যুপকার — ঈশ্বরচন্দ্র বিদ্যাসাগর (সৃজনশীল প্রশ্ন ও উত্তর)</h2>",
             "<h2>২. প্রত্যুপকার — সৃজনশীল প্রশ্ন ও পূর্ণাঙ্গ মডেল উত্তর (Prottupokar CQ Solution 2027)</h2>"),
            ("<h2>৩. সুভা — রবীন্দ্রনাথ ঠাকুর (সৃজনশীল প্রশ্ন ও উত্তর)</h2>",
             "<h2>৩. সুভা — সৃজনশীল প্রশ্ন ও ভাবার্থ বিশ্লেষণ (Shuva Story Creative Question & Answer)</h2>"),
            ("<h2>৪. বই পড়া — প্রমথ চৌধুরী (সৃজনশীল প্রশ্ন ও উত্তর)</h2>",
             "<h2>৪. বই পড়া — প্রবন্ধের সারসংক্ষেপ ও সৃজনশীল গাইড (Boi Pora Essay CQ Suggestion)</h2>"),
            ("<h2>৫. নিরীহ বাঙালি — রোকেয়া সাখাওয়াত হোসেন (সৃজনশীল প্রশ্ন ও উত্তর)</h2>",
             "<h2>৫. নিরীহ বাঙালি — বাঙালি চরিত্রের বিশ্লেষণ ও CQ (Niriho Bangali Creative Question)</h2>"),
        ]
    },
    # Post 03: Prose Part 2
    {
        "post_id": "8676318542398082119",
        "html_file": "output_posts/ssc-bangla-1st-paper-prose-cq-part-2.html",
        "meta_file": "output_posts/ssc-bangla-1st-paper-prose-cq-part-2_metadata.json",
        "new_title": "SSC বাংলা ১ম পত্র গদ্যাংশ পর্ব-২ সৃজনশীল প্রশ্ন ও উত্তর ২০২৬-২০২৭ | মানুষ মুহম্মদ (স.), নিমগাছ, উপেক্ষিত শক্তি ও শিক্ষা ও মনুষ্যত্ব CQ",
        "replacements": [
            ("<h2>২. অধ্যায় ০১: মানুষ মুহম্মদ (স.) — সৃজনশীল ও মানবিক মাহাত্ম্য</h2>",
             "<h2>২. অধ্যায় ০১: মানুষ মুহম্মদ (স.) — সৃজনশীল প্রশ্ন ও সমাধান (Manush Muhammad CQ Solution)</h2>"),
            ("<h2>৩. অধ্যায় ০২: নিমগাছ — রূপক ও নিঃস্বার্থ আত্মত্যাগ</h2>",
             "<h2>৩. অধ্যায় ০২: নিমগাছ — রূপক বিশ্লেষণ ও সৃজনশীল প্রশ্ন (Neemgach Story Creative Question)</h2>"),
            ("<h2>৪. অধ্যায় ০৩: উপেক্ষিত শক্তির উদ্বোধন — সাম্যবাদী চেতনা</h2>",
             "<h2>৪. অধ্যায় ০৩: উপেক্ষিত শক্তির উদ্বোধন — সাম্যবাদী চেতনা ও CQ (Upekkhito Shoktir Udbodhon CQ)</h2>"),
            ("<h2>৫. অধ্যায় ০৪: শিক্ষা ও মনুষ্যত্ব — আত্মিক মুক্তি ও মনুষ্যত্ববোধ</h2>",
             "<h2>৫. অধ্যায় ০৪: শিক্ষা ও মনুষ্যত্ব — মানবসত্তার বিকাশ ও সৃজনশীল (Shikkha O Monushotto CQ Solution)</h2>"),
        ]
    },
    # Post 04: Prose Part 3
    {
        "post_id": "6925279533940643847",
        "html_file": "output_posts/ssc-bangla-1st-paper-prose-cq-part-3.html",
        "meta_file": "output_posts/ssc-bangla-1st-paper-prose-cq-part-3_metadata.json",
        "new_title": "SSC বাংলা ১ম পত্র গদ্যাংশ পর্ব-৩ সৃজনশীল প্রশ্ন ও উত্তর ২০২৬-২০২৭ | প্রবাস বন্ধু, মমতাদি, একুশের গল্প ও নতুন গৌরবগাথা CQ",
        "replacements": [
            ("<h2>অধ্যায় ০১: প্রবাস বন্ধু — সৃজনশীল প্রশ্ন ও পূর্ণাঙ্গ মডেল উত্তর</h2>",
             "<h2>অধ্যায় ০১: প্রবাস বন্ধু — সৃজনশীল প্রশ্ন ও পূর্ণাঙ্গ মডেল উত্তর (Probas Bondhu CQ Question & Answer)</h2>"),
            ("<h2>অধ্যায় ০২: মমতাদি — সৃজনশীল প্রশ্ন ও অনুধাবন ব্যাংক</h2>",
             "<h2>অধ্যায় ০২: মমতাদি — সৃজনশীল প্রশ্ন ও অনুধাবন ব্যাংক (Mamatadi Story Creative Question & SAQ)</h2>"),
            ("<h2>অধ্যায় ০৩: একুশের গল্প — ভাষা আন্দোলন ও তপুর আত্মত্যাগ</h2>",
             "<h2>অধ্যায় ০৩: একুশের গল্প — ভাষা আন্দোলন ও সৃজনশীল সমাধান (Ekusher Golpo CQ Solution)</h2>"),
            ("<h2>অধ্যায় ০৪: আমাদের নতুন গৌরবগাথা — জুলাই গণঅভ্যুত্থান ২০২৪</h2>",
             "<h2>অধ্যায় ০৪: আমাদের নতুন গৌরবগাথা — জুলাই গণঅভ্যুত্থান ২০২৪ (Amader Notun Gourabbatha CQ Suggestion)</h2>"),
        ]
    },
    # Post 05: Poetry Part 1
    {
        "post_id": "6383095457170141697",
        "html_file": "output_posts/ssc-bangla-1st-paper-poetry-cq-part-1.html",
        "meta_file": "output_posts/ssc-bangla-1st-paper-poetry-cq-part-1_metadata.json",
        "new_title": "SSC বাংলা ১ম পত্র কবিতাংশ পর্ব-১ সৃজনশীল প্রশ্ন ও উত্তর ২০২৬-২০২৭ | বন্দনা, কপোতাক্ষ নদ, প্রাণ, জীবন বিনিময় ও উমর ফারুক CQ",
        "replacements": [
            ("<h2>কবিতা ০১: কপোতাক্ষ নদ — সনেট বিশ্লেষণ ও পূর্ণাঙ্গ সৃজনশীল প্রশ্ন</h2>",
             "<h2>কবিতা ০১: কপোতাক্ষ নদ — সনেট বিশ্লেষণ ও সৃজনশীল প্রশ্ন (Kopotakkho Nod CQ Suggestion)</h2>"),
            ("<h2>কবিতা ০২: উমর ফারুক — সাম্য ও মানবিক নেতৃত্বের আদর্শ</h2>",
             "<h2>কবিতা ০২: উমর ফারুক — সাম্য ও মানবিক নেতৃত্বের আদর্শ (Umar Faruq Poem CQ Solution)</h2>"),
            ("<h2>কবিতা ০৩: জীবন বিনিময় — পিতৃস্নেহের এক অনন্য মহাকাব্য</h2>",
             "<h2>কবিতা ০৩: জীবন বিনিময় — পিতৃস্নেহের এক অনন্য মহাকাব্য (Jibon Binimoy Babur Poem CQ Answer)</h2>"),
            ("<h2>কবিতা ০৪ ও ০৫: বন্দনা ও প্রাণ — বিশেষ তাৎপর্য ও প্রস্তুতি</h2>",
             "<h2>কবিতা ০৪ ও ০৫: বন্দনা ও প্রাণ — বিশেষ তাৎপর্য ও সমাধান (Bandana & Pran Poetry CQ Solution)</h2>"),
        ]
    },
    # Post 06: Poetry Part 2
    {
        "post_id": "5928495229348422345",
        "html_file": "output_posts/ssc-bangla-1st-paper-poetry-cq-part-2.html",
        "meta_file": "output_posts/ssc-bangla-1st-paper-poetry-cq-part-2_metadata.json",
        "new_title": "SSC বাংলা ১ম পত্র কবিতাংশ পর্ব-২ সৃজনশীল প্রশ্ন ও উত্তর ২০২৬-২০২৭ | সেইদিন এই মাঠ, বৃষ্টি, আগন্তুক নই, স্বাধীনতা ও বোশেখ CQ",
        "replacements": [
            ("<h2>কবিতা ০১: সেইদিন এই মাঠ — সৃজনশীল প্রশ্ন ও পূর্ণাঙ্গ মডেল উত্তর</h2>",
             "<h2>কবিতা ০১: সেইদিন এই মাঠ — সৃজনশীল প্রশ্ন ও পূর্ণাঙ্গ মডেল উত্তর (Seidin Ei Math CQ Solution)</h2>"),
            ("<h2>কবিতা ০২: আমি কোনো আগন্তুক নই — আত্মিক অস্তিত্বের প্রত্যয়</h2>",
             "<h2>কবিতা ০২: আমি কোনো আগন্তুক নই — আত্মিক অস্তিত্বের প্রত্যয় (Ami Kono Agontuk Noi CQ Solution)</h2>"),
            ("<h2>কবিতা ০৩: তোমাকে পাওয়ার জন্যে, হে স্বাধীনতা — পূর্ণাঙ্গ মডেল প্রশ্ন ও সমাধান</h2>",
             "<h2>কবিতা ০৩: তোমাকে পাওয়ার জন্যে, হে স্বাধীনতা — পূর্ণাঙ্গ মডেল প্রশ্ন ও সমাধান (Tomake Paoar Jonne He Shadhinota CQ)</h2>"),
            ("<h2>কবিতা ০৪ ও ০৫: বৃষ্টি ও বোশেখ — প্রকৃতি, খরতাপ ও প্রতিবাদের রূপক</h2>",
             "<h2>কবিতা ০৪ ও ০৫: বৃষ্টি ও বোশেখ — প্রকৃতি, খরতাপ ও প্রতিবাদের রূপক (Brishti & Boshekh Poetry CQ Solution)</h2>"),
        ]
    },
    # Post 07: SAQ Bank
    {
        "post_id": "5165737254267940811",
        "html_file": "output_posts/ssc-bangla-1st-paper-short-question-bank-20-marks.html",
        "meta_file": "output_posts/ssc-bangla-1st-paper-short-question-bank-20-marks_metadata.json",
        "new_title": "SSC বাংলা ১ম পত্র সংক্ষিপ্ত প্রশ্নব্যাংক ২০২৬-২০২৭ (২০ নম্বর নিশ্চিত) | গদ্য ও পদ্যের সেরা ১০০টি অনুধাবনমূলক প্রশ্ন ও উত্তর (20-Mark SAQ Bank)",
        "replacements": [
            ("<h2>২০ নম্বরের সংক্ষিপ্ত প্রশ্নের মানবণ্টন ও উত্তর লেখার কৌশল</h2>",
             "<h2>২০ নম্বরের সংক্ষিপ্ত প্রশ্নের মানবণ্টন ও উত্তর লেখার কৌশল (20-Mark SAQ Strategy & Rules)</h2>"),
            ("<h2>বিভাগ 'ক': গদ্যাংশ শীর্ষ ৫০টি সংক্ষিপ্ত প্রশ্ন ও সমাধান</h2>",
             "<h2>বিভাগ 'ক': গদ্যাংশ শীর্ষ ৫০টি সংক্ষিপ্ত প্রশ্ন ও সমাধান (Prose Top 50 Short Questions & Answers)</h2>"),
            ("<h2>বিভাগ 'খ': কবিতাংশ শীর্ষ ৫০টি সংক্ষিপ্ত প্রশ্ন ও সমাধান</h2>",
             "<h2>বিভাগ 'খ': কবিতাংশ শীর্ষ ৫০টি সংক্ষিপ্ত প্রশ্ন ও সমাধান (Poetry Top 50 Short Questions & Answers)</h2>"),
        ]
    },
    # Post 08: Model Test
    {
        "post_id": "4514455172913539953",
        "html_file": "output_posts/ssc-bangla-1st-paper-model-test-question-solution-100-marks.html",
        "meta_file": "output_posts/ssc-bangla-1st-paper-model-test-question-solution-100-marks_metadata.json",
        "new_title": "SSC বাংলা ১ম পত্র ১০০ নম্বরের পূর্ণাঙ্গ মডেল টেস্ট ও সমাধান ২০২৬-২০২৭ | বোর্ড স্ট্যান্ডার্ড CQ, MCQ ও সংক্ষিপ্ত প্রশ্ন (100 Marks Full Model Test Paper)",
        "replacements": [
            ("<h2>বিভাগ 'ক': বহুনির্বাচনি প্রশ্ন (MCQ) — পূর্ণমান: ৩০</h2>",
             "<h2>বিভাগ 'ক': বহুনির্বাচনি প্রশ্ন (MCQ 30 Marks with Full Answer Key)</h2>"),
            ("<h2>বিভাগ 'খ': সৃজনশীল রচনামূলক প্রশ্ন (CQ) — পূর্ণমান: ৫০</h2>",
             "<h2>বিভাগ 'খ': সৃজনশীল রচনামূলক প্রশ্ন (CQ 50 Marks Model Question Paper)</h2>"),
            ("<h2>বিভাগ 'গ': সংক্ষিপ্ত উত্তর প্রশ্ন (SAQ) — পূর্ণমান: ২০</h2>",
             "<h2>বিভাগ 'গ': সংক্ষিপ্ত উত্তর প্রশ্ন (SAQ 20 Marks Question Bank)</h2>"),
        ]
    }
]

def main():
    print("=" * 75)
    print("HELPTRICKBD SEO — BILINGUAL KEYWORD ENHANCEMENT ENGINE")
    print("=" * 75)

    service = get_authenticated_service()
    if not service:
        print("[ERROR] Blogger authentication failed.")
        sys.exit(1)

    idx_creds = get_idx_credentials()
    idx_service = build("indexing", "v3", credentials=idx_creds) if idx_creds else None

    for cfg in POST_ENHANCEMENT_CONFIGS:
        html_path = os.path.join(PROJECT_ROOT, cfg["html_file"])
        meta_path = os.path.join(PROJECT_ROOT, cfg["meta_file"])
        post_id = cfg["post_id"]
        new_title = cfg["new_title"]

        print(f"\n[*] Processing Post ID: {post_id} ({cfg['html_file']})...")

        with open(html_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Apply replacements
        for target, repl in cfg["replacements"]:
            if target in content:
                content = content.replace(target, repl)
                print(f"    [✔] Replaced: {target[:30]}... -> {repl[:40]}...")
            else:
                print(f"    [!] Not found: {target[:40]}")

        # Save updated HTML
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(content)

        # Update metadata title
        if os.path.exists(meta_path):
            with open(meta_path, "r", encoding="utf-8") as f:
                meta = json.load(f)
            meta["title"] = new_title
            with open(meta_path, "w", encoding="utf-8") as f:
                json.dump(meta, f, ensure_ascii=False, indent=2)

        # Pre-Flight Checker
        checker = PreFlightChecker(html_path, metadata_path=meta_path)
        if not checker.run_all():
            print(f"    [WARNING] Pre-flight warning/failure for {html_path}")

        # Patch to Blogger Live
        patch_body = {
            "title": new_title,
            "content": content
        }
        updated = service.posts().patch(blogId=BLOG_ID, postId=post_id, body=patch_body).execute()
        live_url = updated.get("url")
        print(f"    [OK] Blogger Updated: {live_url}")
        print(f"    [OK] Live Title: {updated.get('title')}")

        # Ping Indexing API
        if idx_service and live_url:
            try:
                submit_url(idx_service, live_url, "URL_UPDATED")
                print(f"    [OK] Googlebot pinged: {live_url}")
            except Exception as e:
                print(f"    [!] Indexing ping notice: {e}")

        time.sleep(1)

    print("\n[*] Pinging WebSub Hubs...")
    try:
        ping_all_hubs()
    except Exception as e:
        print(f"    [WARNING] WebSub error: {e}")

    print("\n" + "=" * 75)
    print("ALL 7 POSTS ENRICHED WITH BILINGUAL KEYWORDS & PUSHED LIVE!")
    print("=" * 75)

if __name__ == "__main__":
    main()
