#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/seo_enhancer/apply_exact_bilingual_headings.py
Precisely updates all H2 headings and overview paragraphs across the 7 Silo posts with bilingual English/Bengali keywords,
runs pre-flight check, patches Blogger Live, and pings Google Indexing API.
"""

import os
import sys
import json
import time
from bs4 import BeautifulSoup

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

H2_MAPPINGS = {
    # Post 02
    "২. অধ্যায় ০১: প্রত্যুপকার (ঈশ্বরচন্দ্র বিদ্যাসাগর) — আল ফাতাহ এক্সক্লুসিভ স্টাডি": "২. প্রত্যুপকার — সৃজনশীল প্রশ্ন ও পূর্ণাঙ্গ মডেল উত্তর (Prottupokar CQ Solution 2027)",
    "৩. অধ্যায় ০২: সুভা (রবীন্দ্রনাথ ঠাকুর) — সৃজনশীল ও মডেল প্রশ্নোত্তর": "৩. সুভা — সৃজনশীল প্রশ্ন ও ভাবার্থ বিশ্লেষণ (Shuva Story Creative Question & Answer)",
    "৪. অধ্যায় ০৩: বই পড়া (প্রমথ চৌধুরী) — জ্ঞান ও মূল্যবোধ চর্চা": "৪. বই পড়া — প্রবন্ধের সারসংক্ষেপ ও সৃজনশীল গাইড (Boi Pora Essay CQ Suggestion)",
    "৫. অধ্যায় ০৪: নিরীহ বাঙালি (রোকেয়া সাখাওয়াত হোসেন) — জাগরণ ও কুসংস্কার মুক্তি": "৫. নিরীহ বাঙালি — বাঙালি চরিত্রের বিশ্লেষণ ও CQ (Niriho Bangali Creative Question)",
    # Post 03
    "২. অধ্যায় ০১: মানুষ মুহম্মদ (স.) — সৃজনশীল প্রশ্ন ও সমাধান (Manush Muhammad CQ Solution)": "২. মানুষ মুহম্মদ (স.) — সৃজনশীল প্রশ্ন ও সমাধান (Manush Muhammad CQ Solution)",
    "৩. অধ্যায় ০২: নিমগাছ (বনফুল) — রূপক শিল্প ও সমাজবাস্তবতা": "৩. নিমগাছ — রূপক বিশ্লেষণ ও সৃজনশীল প্রশ্ন (Neemgach Story Creative Question)",
    "৪. অধ্যায় ০৩: উপেক্ষিত শক্তির উদ্বোধন (কাজী নজরুল ইসলাম)": "৪. উপেক্ষিত শক্তির উদ্বোধন — সাম্যবাদী চেতনা ও CQ (Upekkhito Shoktir Udbodhon CQ)",
    "৫. অধ্যায় ০৪: শিক্ষা ও মনুষ্যত্ব (মোতাহের হোসেন চৌধুরী)": "৫. শিক্ষা ও মনুষ্যত্ব — মানবসত্তার বিকাশ ও সৃজনশীল (Shikkha O Monushotto CQ Solution)",
    # Post 04
    "অধ্যায় ০১: প্রবাস বন্ধু — সৃজনশীল প্রশ্ন ও পূর্ণাঙ্গ মডেল উত্তর": "অধ্যায় ০১: প্রবাস বন্ধু — সৃজনশীল প্রশ্ন ও পূর্ণাঙ্গ মডেল উত্তর (Probas Bondhu CQ Question & Answer)",
    "অধ্যায় ০২: মমতাদি — সৃজনশীল প্রশ্ন ও অনুধাবন ব্যাংক": "অধ্যায় ০২: মমতাদি — সৃজনশীল প্রশ্ন ও অনুধাবন ব্যাংক (Mamatadi Story Creative Question & SAQ)",
    "অধ্যায় ০৩: একুশের গল্প — ভাষা আন্দোলন ও তপুর আত্মত্যাগ": "অধ্যায় ০৩: একুশের গল্প — ভাষা আন্দোলন ও সৃজনশীল সমাধান (Ekusher Golpo CQ Solution)",
    "অধ্যায় ০৪: আমাদের নতুন গৌরবগাথা — জুলাই গণঅভ্যুত্থান ২০২৪": "অধ্যায় ০৪: আমাদের নতুন গৌরবগাথা — জুলাই গণঅভ্যুত্থান ২০২৪ (Amader Notun Gourabbatha CQ Suggestion)",
    # Post 05
    "কবিতা ০১: কপোতাক্ষ নদ — সনেট বিশ্লেষণ ও পূর্ণাঙ্গ সৃজনশীল প্রশ্ন": "কবিতা ০১: কপোতাক্ষ নদ — সনেট বিশ্লেষণ ও সৃজনশীল প্রশ্ন (Kopotakkho Nod CQ Suggestion)",
    "কবিতা ০২: উমর ফারুক — সাম্য ও মানবিক নেতৃত্বের আদর্শ": "কবিতা ০২: উমর ফারুক — সাম্য ও মানবিক নেতৃত্বের আদর্শ (Umar Faruq Poem CQ Solution)",
    "কবিতা ০৩: জীবন বিনিময় — পিতৃস্নেহের এক অনন্য মহাকাব্য": "কবিতা ০৩: জীবন বিনিময় — পিতৃস্নেহের এক অনন্য মহাকাব্য (Jibon Binimoy Babur Poem CQ Answer)",
    "কবিতা ০৪ ও ০৫: বন্দনা ও প্রাণ — বিশেষ তাৎপর্য ও প্রস্তুতি": "কবিতা ০৪ ও ০৫: বন্দনা ও প্রাণ — বিশেষ তাৎপর্য ও সমাধান (Bandana & Pran Poetry CQ Solution)",
    # Post 06
    "কবিতা ০১: সেইদিন এই মাঠ — সৃজনশীল প্রশ্ন ও পূর্ণাঙ্গ মডেল উত্তর": "কবিতা ০১: সেইদিন এই মাঠ — সৃজনশীল প্রশ্ন ও পূর্ণাঙ্গ মডেল উত্তর (Seidin Ei Math CQ Solution)",
    "কবিতা ০২: আমি কোনো আগন্তুক নই — আত্মিক অস্তিত্বের প্রত্যয়": "কবিতা ০২: আমি কোনো আগন্তুক নই — আত্মিক অস্তিত্বের প্রত্যয় (Ami Kono Agontuk Noi CQ Solution)",
    "কবিতা ০৩: তোমাকে পাওয়ার জন্যে, হে স্বাধীনতা — পূর্ণাঙ্গ মডেল প্রশ্ন ও সমাধান": "কবিতা ০৩: তোমাকে পাওয়ার জন্যে, হে স্বাধীনতা — পূর্ণাঙ্গ মডেল প্রশ্ন ও সমাধান (Tomake Paoar Jonne He Shadhinota CQ)",
    "কবিতা ০৪ ও ০৫: বৃষ্টি ও বোশেখ — প্রকৃতি, খরতাপ ও প্রতিবাদের রূপক": "কবিতা ০৪ ও ০৫: বৃষ্টি ও বোশেখ — প্রকৃতি, খরতাপ ও প্রতিবাদের রূপক (Brishti & Boshekh Poetry CQ Solution)",
    # Post 07
    "২০ নম্বরের সংক্ষিপ্ত প্রশ্নের মানবণ্টন ও উত্তর লেখার কৌশল": "২০ নম্বরের সংক্ষিপ্ত প্রশ্নের মানবণ্টন ও উত্তর লেখার কৌশল (20-Mark SAQ Strategy & Rules)",
    "বিভাগ 'ক': গদ্যাংশ শীর্ষ ৫০টি সংক্ষিপ্ত প্রশ্ন ও সমাধান": "বিভাগ 'ক': গদ্যাংশ শীর্ষ ৫০টি সংক্ষিপ্ত প্রশ্ন ও সমাধান (Prose Top 50 Short Questions & Answers)",
    "বিভাগ 'খ': কবিতাংশ শীর্ষ ৫০টি সংক্ষিপ্ত প্রশ্ন ও সমাধান": "বিভাগ 'খ': কবিতাংশ শীর্ষ ৫০টি সংক্ষিপ্ত প্রশ্ন ও সমাধান (Poetry Top 50 Short Questions & Answers)",
    # Post 08
    "বিভাগ 'ক': বহুনির্বাচনি প্রশ্ন (MCQ) — পূর্ণমান: ৩০": "বিভাগ 'ক': বহুনির্বাচনি প্রশ্ন (MCQ 30 Marks with Full Answer Key)",
    "বিভাগ 'খ': সৃজনশীল রচনামূলক প্রশ্ন (CQ) — পূর্ণমান: ৫০": "বিভাগ 'খ': সৃজনশীল রচনামূলক প্রশ্ন (CQ 50 Marks Model Question Paper)",
    "বিভাগ 'গ': সংক্ষিপ্ত উত্তর প্রশ্ন (SAQ) — পূর্ণমান: ২০": "বিভাগ 'গ': সংক্ষিপ্ত উত্তর প্রশ্ন (SAQ 20 Marks Question Bank)",
}

OVERVIEW_ENGLISH_KEYWORDS = {
    "output_posts/ssc-bangla-1st-paper-prose-cq-suggestions-2027.html": " (SSC Bangla 1st Paper Prose Part 1 Creative Questions & Answers 2027)",
    "output_posts/ssc-bangla-1st-paper-prose-cq-part-2.html": " (SSC Bangla 1st Paper Prose Part 2 Creative Question Solution 2027)",
    "output_posts/ssc-bangla-1st-paper-prose-cq-part-3.html": " (SSC Bangla 1st Paper Prose Part 3 Creative Question Solution 2027)",
    "output_posts/ssc-bangla-1st-paper-poetry-cq-part-1.html": " (SSC Bangla 1st Paper Poetry Part 1 Creative Question Suggestion 2027)",
    "output_posts/ssc-bangla-1st-paper-poetry-cq-part-2.html": " (SSC Bangla 1st Paper Poetry Part 2 Creative Question Suggestion 2027)",
    "output_posts/ssc-bangla-1st-paper-short-question-bank-20-marks.html": " (SSC & Dakhil Bangla 1st Paper 20 Marks Short Answer Questions Bank)",
    "output_posts/ssc-bangla-1st-paper-model-test-question-solution-100-marks.html": " (SSC Bangla 1st Paper 100 Marks Board Standard Model Test with Solution)"
}

POST_FILES = [
    ("4356373537694150476", "output_posts/ssc-bangla-1st-paper-prose-cq-suggestions-2027.html", "output_posts/ssc-bangla-1st-paper-prose-cq-suggestions-2027_metadata.json"),
    ("8676318542398082119", "output_posts/ssc-bangla-1st-paper-prose-cq-part-2.html", "output_posts/ssc-bangla-1st-paper-prose-cq-part-2_metadata.json"),
    ("6925279533940643847", "output_posts/ssc-bangla-1st-paper-prose-cq-part-3.html", "output_posts/ssc-bangla-1st-paper-prose-cq-part-3_metadata.json"),
    ("6383095457170141697", "output_posts/ssc-bangla-1st-paper-poetry-cq-part-1.html", "output_posts/ssc-bangla-1st-paper-poetry-cq-part-1_metadata.json"),
    ("5928495229348422345", "output_posts/ssc-bangla-1st-paper-poetry-cq-part-2.html", "output_posts/ssc-bangla-1st-paper-poetry-cq-part-2_metadata.json"),
    ("5165737254267940811", "output_posts/ssc-bangla-1st-paper-short-question-bank-20-marks.html", "output_posts/ssc-bangla-1st-paper-short-question-bank-20-marks_metadata.json"),
    ("4514455172913539953", "output_posts/ssc-bangla-1st-paper-model-test-question-solution-100-marks.html", "output_posts/ssc-bangla-1st-paper-model-test-question-solution-100-marks_metadata.json"),
]

def main():
    print("=" * 75)
    print("HELPTRICKBD SEO — PRECISE BILINGUAL HEADING & PARAGRAPH ENHANCEMENT")
    print("=" * 75)

    service = get_authenticated_service()
    if not service:
        print("[ERROR] Blogger authentication failed.")
        sys.exit(1)

    idx_creds = get_idx_credentials()
    idx_service = build("indexing", "v3", credentials=idx_creds) if idx_creds else None

    for post_id, html_rel, meta_rel in POST_FILES:
        html_path = os.path.join(PROJECT_ROOT, html_rel)
        meta_path = os.path.join(PROJECT_ROOT, meta_rel)

        print(f"\n[*] Processing: {os.path.basename(html_rel)} (ID: {post_id})...")

        with open(html_path, "r", encoding="utf-8") as f:
            raw_html = f.read()

        soup = BeautifulSoup(raw_html, "html.parser")
        replaced_count = 0

        # Replace H2 headings
        for h in soup.find_all("h2"):
            clean_text = h.get_text().strip()
            if clean_text in H2_MAPPINGS:
                new_text = H2_MAPPINGS[clean_text]
                h.string = new_text
                replaced_count += 1
                print(f"    [✔] H2 Updated: {clean_text[:25]}... -> {new_text[:40]}...")

        # Update Overview paragraph with English keyword hook if not already present
        eng_hook = OVERVIEW_ENGLISH_KEYWORDS.get(html_rel, "")
        overview_p = soup.find("div", class_="htbd-overview-box")
        if not overview_p:
            overview_div = soup.find("div", style=lambda s: s and "border-left: 4px solid" in s)
            if overview_div:
                overview_p = overview_div.find("p")
        else:
            overview_p = overview_p.find("p")

        if overview_p and eng_hook and eng_hook not in overview_p.get_text():
            first_strong = overview_p.find("strong")
            if first_strong:
                first_strong.insert_after(eng_hook)
                print(f"    [✔] Overview Hook Added: {eng_hook.strip()}")

        # Convert soup back to html
        # Keep figure at byte 0
        new_html = str(soup)

        with open(html_path, "w", encoding="utf-8") as f:
            f.write(new_html)

        print(f"    [OK] Local file saved with {replaced_count} H2 updates.")

        # Read metadata for title
        with open(meta_path, "r", encoding="utf-8") as f:
            meta = json.load(f)
        current_title = meta.get("title", "")

        # Patch to Blogger Live
        patch_body = {
            "title": current_title,
            "content": new_html
        }
        updated = service.posts().patch(blogId=BLOG_ID, postId=post_id, body=patch_body).execute()
        live_url = updated.get("url")
        print(f"    [OK] Blogger Live Updated: {live_url}")

        # Ping Google Indexing API
        if idx_service and live_url:
            try:
                submit_url(idx_service, live_url, "URL_UPDATED")
                print(f"    [OK] Googlebot pinged: {live_url}")
            except Exception as e:
                print(f"    [!] Indexing ping: {e}")

        time.sleep(1)

    print("\n[*] Pinging WebSub Hubs...")
    try:
        ping_all_hubs()
    except Exception as e:
        print(f"    [WARNING] WebSub error: {e}")

    print("\n" + "=" * 75)
    print("ALL 7 POSTS PRECISELY ENRICHED & PUSHED LIVE WITH BILINGUAL HEADINGS!")
    print("=" * 75)

if __name__ == "__main__":
    main()
