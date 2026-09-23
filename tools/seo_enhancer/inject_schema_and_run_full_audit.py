#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/seo_enhancer/inject_schema_and_run_full_audit.py
-----------------------------------------------------
1. Injects Schema.org (BlogPosting + FAQPage + BreadcrumbList) into the 5 posts missing them.
2. Updates Blogger Live via Blogger API v3.
3. Submits all 8 URLs to Google Indexing API.
4. Submits all 8 URLs to IndexNow (Bing, Yandex, Yahoo).
5. Pings Google WebSub / PubSubHubbub Hubs (6/6 endpoints).
6. Runs an automated live audit of all 8 posts using Googlebot User-Agent.
"""

import os
import sys
import json
import time
import requests
from bs4 import BeautifulSoup

if sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.blogger_publisher.publisher import get_authenticated_service, BLOG_ID
from tools.indexer.pubsub_hub_pinger import ping_all_hubs
from tools.indexer.index_now import get_authenticated_service as get_idx_credentials, submit_url
from googleapiclient.discovery import build

ALL_8_URLS = [
    ("6904395060145150353", "https://www.helptrickbd.com/2026/09/ssc-bangla-1st-paper-final-suggestion.html", "পিলার পোস্ট: চূড়ান্ত সাজেশন ও পূর্ণাঙ্গ গাইড"),
    ("4356373537694150476", "https://www.helptrickbd.com/2026/09/ssc-bangla-1st-paper-prose-cq.html", "গদ্যাংশ পর্ব-১: প্রত্যুপকার, সুভা, বই পড়া ও নিরীহ বাঙালি CQ"),
    ("8676318542398082119", "https://www.helptrickbd.com/2026/09/ssc-bangla-1st-paper-prose-cq-part-2.html", "গদ্যাংশ পর্ব-২: মানুষ মুহম্মদ (স.), নিমগাছ, উপেক্ষিত শক্তি ও শিক্ষা ও মনুষ্যত্ব CQ"),
    ("6925279533940643847", "https://www.helptrickbd.com/2026/09/ssc-bangla-1st-paper-prose-cq-part-3.html", "গদ্যাংশ পর্ব-৩: প্রবাস বন্ধু, মমতাদি, একুশের গল্প ও নতুন গৌরবগাথা CQ"),
    ("6383095457170141697", "https://www.helptrickbd.com/2026/09/ssc-bangla-1st-paper-poetry-cq-part-1.html", "কবিতাংশ পর্ব-১: বন্দনা, কপোতাক্ষ নদ, প্রাণ, জীবন বিনিময় ও উমর ফারুক CQ"),
    ("5928495229348422345", "https://www.helptrickbd.com/2026/09/ssc-bangla-1st-paper-poetry-cq-part-2.html", "কবিতাংশ পর্ব-২: সেইদিন এই মাঠ, বৃষ্টি, আগন্তুক নই, স্বাধীনতা ও বোশেখ CQ"),
    ("5165737254267940811", "https://www.helptrickbd.com/2026/09/ssc-bangla-1st-paper-short-question.html", "২০ নম্বরের সংক্ষিপ্ত প্রশ্নব্যাংক (১০০টি অনুধাবনমূলক প্রশ্ন ও উত্তর)"),
    ("4514455172913539953", "https://www.helptrickbd.com/2026/09/ssc-bangla-1st-paper-model-test.html", "১০০ নম্বরের পূর্ণাঙ্গ মডেল টেস্ট ও সমাধান (CQ, MCQ, SAQ)")
]

MISSING_SCHEMA_POSTS = [
    {
        "post_id": "6925279533940643847",
        "html_file": "output_posts/ssc-bangla-1st-paper-prose-cq-part-3.html",
        "meta_file": "output_posts/ssc-bangla-1st-paper-prose-cq-part-3_metadata.json",
        "url": "https://www.helptrickbd.com/2026/09/ssc-bangla-1st-paper-prose-cq-part-3.html",
        "headline": "SSC বাংলা ১ম পত্র গদ্যাংশ পর্ব-৩ সৃজনশীল প্রশ্ন ও উত্তর ২০২৬-২০২৭ | প্রবাস বন্ধু, মমতাদি, একুশের গল্প ও নতুন গৌরবগাথা CQ",
        "image": "https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/posts/ssc_bangla_1st_paper_prose_part3_2027.webp",
        "description": "এসএসসি ও দাখিল ২০২৬-২০২৭ বাংলা ১ম পত্র গদ্যাংশ পর্ব-৩ সৃজনশীল প্রশ্ন ও পূর্ণাঙ্গ মডেল উত্তর। প্রবাস বন্ধু, মমতাদি, একুশের গল্প ও জুলাই গণঅভ্যুত্থান ২০২৪ ভিত্তিক আমাদের নতুন গৌরবগাথা অধ্যায়ের সমাধান।",
        "faqs": [
            {
                "q": "প্রবাস বন্ধু ভ্রমণকাহিনিতে আবদুর রহমানের চরিত্রের প্রধান বৈশিষ্ট্য কী?",
                "a": "আবদুর রহমানের চরিত্রের প্রধান বৈশিষ্ট্য হলো তার অতুলনীয় অতিথিপরায়ণতা, সেবাধর্মী মনোভাব এবং সরল আনুগত্য।"
            },
            {
                "q": "মমতাদি গল্পে গৃহকর্মে নিয়োজিত মমতাদির আত্মমর্যাদাবোধ কীভাবে ফুটে উঠেছে?",
                "a": "অভাবের তাড়নায় কাজ নিলেও মমতাদি নিজেকে দাসী মনে করেনি; সে ছিল স্নেহশীল, নিঃসংকোচ এবং প্রখর আত্মমর্যাদাসম্পন্ন।"
            },
            {
                "q": "একুশের গল্পে তপু চরিত্রটির মূল বার্তা কী?",
                "a": "তপু চরিত্রটি ভাষা আন্দোলনের রক্তসিঁড়িতে বাঙালির স্বাধিকার চেতনা ও সাহসিকতার প্রতীক।"
            }
        ]
    },
    {
        "post_id": "6383095457170141697",
        "html_file": "output_posts/ssc-bangla-1st-paper-poetry-cq-part-1.html",
        "meta_file": "output_posts/ssc-bangla-1st-paper-poetry-cq-part-1_metadata.json",
        "url": "https://www.helptrickbd.com/2026/09/ssc-bangla-1st-paper-poetry-cq-part-1.html",
        "headline": "SSC বাংলা ১ম পত্র কবিতাংশ পর্ব-১ সৃজনশীল প্রশ্ন ও উত্তর ২০২৬-২০২৭ | বন্দনা, কপোতাক্ষ নদ, প্রাণ, জীবন বিনিময় ও উমর ফারুক CQ",
        "image": "https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/posts/ssc_bangla_1st_paper_poetry_part1_2027.webp",
        "description": "এসএসসি ও দাখিল ২০২৬-২০২৭ বাংলা ১ম পত্র কবিতাংশ পর্ব-১ সৃজনশীল প্রশ্ন ও সমাধান। বন্দনা, কপোতাক্ষ নদ, প্রাণ, জীবন বিনিময় ও উমর ফারুক কবিতার বোর্ড স্ট্যান্ডার্ড CQ ও অনুধাবন।",
        "faqs": [
            {
                "q": "কপোতাক্ষ নদ কবিতায় কবির স্মৃতিকাতরতা কীভাবে প্রকাশিত হয়েছে?",
                "a": "প্রবাস জীবনে ফ্রান্সের ভার্সাই নগরে বসে কবি মাইকেল মধুসূদন দত্ত শৈশবের স্মৃতিবিজড়িত কপোতাক্ষ নদের মিষ্টি জল ও কলকল ধ্বনিকে কোনোভাবেই ভুলতে পারেননি।"
            },
            {
                "q": "উমর ফারুক কবিতায় খলিফা উমর (রা.)-এর কোন চারিত্রিক দিকটিকে নজরুল প্রাধান্য দিয়েছেন?",
                "a": "মহান খলিফার কঠোর ন্যায়পরায়ণতা, ব্যক্তিগত জীবনে চরম অনাড়ম্বরতা, সাম্যবাদ এবং সাধারণ মানুষের দুঃখ-কষ্টে ব্যক্তিগতভাবে ছুটে যাওয়ার মহান গুণ।"
            },
            {
                "q": "জীবন বিনিময় কবিতার মূল শিক্ষা কী?",
                "a": "সন্তানের রোগমুক্তির জন্য নিজের জীবন উৎসর্গ করার মধ্য দিয়ে সম্রাট বাবরের অপার্থিব পিতৃস্নেহ ও আত্মত্যাগের অমর দৃষ্টান্ত।"
            }
        ]
    },
    {
        "post_id": "5928495229348422345",
        "html_file": "output_posts/ssc-bangla-1st-paper-poetry-cq-part-2.html",
        "meta_file": "output_posts/ssc-bangla-1st-paper-poetry-cq-part-2_metadata.json",
        "url": "https://www.helptrickbd.com/2026/09/ssc-bangla-1st-paper-poetry-cq-part-2.html",
        "headline": "SSC বাংলা ১ম পত্র কবিতাংশ পর্ব-২ সৃজনশীল প্রশ্ন ও উত্তর ২০২৬-২০২৭ | সেইদিন এই মাঠ, বৃষ্টি, আগন্তুক নই, স্বাধীনতা ও বোশেখ CQ",
        "image": "https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/posts/ssc_bangla_1st_paper_poetry_part2_2027.webp",
        "description": "এসএসসি ও দাখিল ২০২৬-২০২৭ বাংলা ১ম পত্র কবিতাংশ পর্ব-২ এর সৃজনশীল প্রশ্ন ও মডেল উত্তর। সেইদিন এই মাঠ, বৃষ্টি, আমি কোনো আগন্তুক নই ও তোমাকে পাওয়ার জন্যে হে স্বাধীনতা কবিতার সমাধান।",
        "faqs": [
            {
                "q": "সেইদিন এই মাঠ কবিতায় জীবনানন্দ দাশ মানবজীবনের নশ্বরতার বিপরীতে কীসের শাশ্বত রূপ তুলে ধরেছেন?",
                "a": "মানুষের মৃত্যু হলেও প্রকৃতির চিরন্তন রূপ, নদীর কলতান, খেয়া নৌকার পারাপার এবং শিশিরের গন্ধ যে অনন্তকাল বহমান থাকবে—তা তুলে ধরেছেন।"
            },
            {
                "q": "আমি কোনো আগন্তুক নই কবিতায় কবি নিজেকে কেন আগন্তুক নন বলে দাবি করেছেন?",
                "a": "কারণ বাংলার আকাশ, বাতাস, মাটির গন্ধ, শালিক, নিঝুম রাত এবং মানুষের সান্নিধ্যে কবির শিকড় গভীরভাবে প্রোথিত।"
            },
            {
                "q": "তোমাকে পাওয়ার জন্যে, হে স্বাধীনতা কবিতায় স্বাধীনতার মূল্যকে কবি কীভাবে মূল্যায়ন করেছেন?",
                "a": "লাখো শহীদের রক্ত, সাকিনা বিবির কপাল ভাঙা, হরিদাসীর সিঁথির সিঁদুর মোছা এবং অগণিত মানুষের সর্বস্ব ত্যাগের বিনিময়ে অর্জিত মহামূল্যবান সম্পদ হিসেবে।"
            }
        ]
    },
    {
        "post_id": "5165737254267940811",
        "html_file": "output_posts/ssc-bangla-1st-paper-short-question-bank-20-marks.html",
        "meta_file": "output_posts/ssc-bangla-1st-paper-short-question-bank-20-marks_metadata.json",
        "url": "https://www.helptrickbd.com/2026/09/ssc-bangla-1st-paper-short-question.html",
        "headline": "SSC বাংলা ১ম পত্র সংক্ষিপ্ত প্রশ্নব্যাংক ২০২৬-২০২৭ (২০ নম্বর নিশ্চিত) | গদ্য ও পদ্যের সেরা ১০০টি অনুধাবনমূলক প্রশ্ন ও উত্তর (20-Mark SAQ Bank)",
        "image": "https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/posts/ssc_bangla_1st_paper_saq_bank_2027.webp",
        "description": "এসএসসি ও দাখিল ২০২৬-২০২৭ বাংলা ১ম পত্র পরীক্ষার ২০ নম্বরের সংক্ষিপ্ত উত্তর প্রশ্নের (SAQ) সম্পূর্ণ প্রশ্নব্যাংক। গদ্য ও পদ্যের শীর্ষ ১০০টি প্রশ্ন ও শতভাগ নির্ভুল উত্তর।",
        "faqs": [
            {
                "q": "এসএসসি বাংলা ১ম পত্রে ২০ নম্বরের সংক্ষিপ্ত প্রশ্নের মানবণ্টন কী?",
                "a": "নতুন সিলেবাসে ১০টি সংক্ষিপ্ত প্রশ্ন থাকে এবং প্রতিটির মান ২ নম্বর। এর মধ্যে গদ্যাংশ থেকে ৫টি (১০ নম্বর) এবং কবিতাংশ থেকে ৫টি (১০ নম্বর) প্রশ্নের উত্তর দিতে হয়।"
            },
            {
                "q": "সংক্ষিপ্ত প্রশ্নে ২-এ ২ পাওয়ার মূল কৌশল কী?",
                "a": "অতিরিক্ত ভূমিকা না লিখে সরাসরি প্রথম বাক্যে মূল জ্ঞানমূলক তথ্য দিতে হবে এবং পরের ২-৩ বাক্যে অনুধাবনের সুস্পষ্ট ব্যাখ্যা প্রদান করতে হবে।"
            }
        ]
    },
    {
        "post_id": "4514455172913539953",
        "html_file": "output_posts/ssc-bangla-1st-paper-model-test-question-solution-100-marks.html",
        "meta_file": "output_posts/ssc-bangla-1st-paper-model-test-question-solution-100-marks_metadata.json",
        "url": "https://www.helptrickbd.com/2026/09/ssc-bangla-1st-paper-model-test.html",
        "headline": "SSC বাংলা ১ম পত্র ১০০ নম্বরের পূর্ণাঙ্গ মডেল টেস্ট ও সমাধান ২০২৬-২০২৭ | বোর্ড স্ট্যান্ডার্ড CQ, MCQ ও সংক্ষিপ্ত প্রশ্ন (100 Marks Full Model Test Paper)",
        "image": "https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/posts/ssc_bangla_1st_paper_model_test_2027.webp",
        "description": "এসএসসি ও দাখিল ২০২৬-২০২৭ বাংলা ১ম পত্র ১০০ নম্বরের পূর্ণাঙ্গ বোর্ড স্ট্যান্ডার্ড মডেল টেস্ট প্রশ্নপত্র ও উত্তরমালা। ৫০ নম্বরের CQ, ৩০ নম্বরের MCQ এবং ২০ নম্বরের সংক্ষিপ্ত প্রশ্নের সমাধান।",
        "faqs": [
            {
                "q": "এই মডেল টেস্টটি কোন কারিকুলাম ও বোর্ড প্রশ্নের ধাঁচে তৈরি?",
                "a": "এনসিটিবি-র ২০২৬-২০২৭ শিক্ষাবর্ষের সর্বশেষ প্রশ্নকাঠামো এবং ঢাকা, রাজশাহী, চট্টগ্রামসহ সকল সাধারণ শিক্ষা বোর্ড ও মাদ্রাসা শিক্ষা বোর্ডের স্ট্যান্ডার্ড অনুযায়ী তৈরি।"
            },
            {
                "q": "পরীক্ষার ৩ ঘণ্টা সময় কীভাবে ভাগ করে উত্তর লেখা উচিত?",
                "a": "প্রথম ৩০ মিনিট MCQ-এর জন্য, পরের ১ ঘণ্টা ৪০ মিনিট CQ ৫টি সৃজনশীল লেখার জন্য এবং বাকি ৫০ মিনিট সংক্ষিপ্ত ১০টি প্রশ্ন লেখার জন্য বরাদ্দ রাখা আদর্শ।"
            }
        ]
    }
]

def generate_schema_block(post_info):
    blog_schema = {
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": post_info["headline"],
        "image": post_info["image"],
        "datePublished": "2026-09-23T21:00:00+06:00",
        "dateModified": "2026-09-23T21:30:00+06:00",
        "author": {
            "@type": "Person",
            "name": "Faruk Sir"
        },
        "publisher": {
            "@type": "Organization",
            "name": "HelpTrickBD",
            "logo": {
                "@type": "ImageObject",
                "url": "https://www.helptrickbd.com/favicon.ico"
            }
        },
        "description": post_info["description"],
        "mainEntityOfPage": {
            "@type": "WebPage",
            "@id": post_info["url"]
        }
    }

    faq_schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": item["q"],
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": item["a"]
                }
            } for item in post_info["faqs"]
        ]
    }

    breadcrumb_schema = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": 1,
                "name": "Home",
                "item": "https://www.helptrickbd.com/"
            },
            {
                "@type": "ListItem",
                "position": 2,
                "name": "SSC Suggestion 2026-2027",
                "item": "https://www.helptrickbd.com/search/label/SSC%20Suggestion%202026-2027"
            },
            {
                "@type": "ListItem",
                "position": 3,
                "name": post_info["headline"],
                "item": post_info["url"]
            }
        ]
    }

    block = "\n" + f'<script type="application/ld+json">\n{json.dumps(blog_schema, ensure_ascii=False, indent=2)}\n</script>\n'
    block += f'<script type="application/ld+json">\n{json.dumps(faq_schema, ensure_ascii=False, indent=2)}\n</script>\n'
    block += f'<script type="application/ld+json">\n{json.dumps(breadcrumb_schema, ensure_ascii=False, indent=2)}\n</script>\n'
    return block

def inject_schemas_and_patch():
    print("=" * 70)
    print("STEP 1: INJECTING SCHEMA.ORG JSON-LD INTO 5 MISSING POSTS")
    print("=" * 70)

    service = get_authenticated_service()

    for item in MISSING_SCHEMA_POSTS:
        html_path = os.path.join(PROJECT_ROOT, item["html_file"])
        with open(html_path, "r", encoding="utf-8") as f:
            html = f.read()

        if "application/ld+json" not in html:
            schema_block = generate_schema_block(item)
            html = html.strip() + "\n" + schema_block
            with open(html_path, "w", encoding="utf-8") as f:
                f.write(html)
            print(f"[✔] Schema injected into local file: {item['html_file']}")

        # Read meta title
        meta_path = os.path.join(PROJECT_ROOT, item["meta_file"])
        with open(meta_path, "r", encoding="utf-8") as f:
            meta = json.load(f)
        title = meta.get("title", item["headline"])

        # Patch live Blogger
        patch_body = {
            "title": title,
            "content": html
        }
        res = service.posts().patch(blogId=BLOG_ID, postId=item["post_id"], body=patch_body).execute()
        print(f"    [✔] Blogger Live Updated: {res.get('url')}")
        time.sleep(1)

def submit_index_now_api(urls):
    """Submits to Bing & Yandex IndexNow API."""
    print("\n" + "=" * 70)
    print("STEP 2: SUBMITTING ALL 8 URLS TO INDEXNOW (BING / YANDEX / YAHOO)")
    print("=" * 70)
    # Helptrickbd host
    host = "www.helptrickbd.com"
    # Using indexnow generic API key endpoint
    payload = {
        "host": host,
        "key": "4c424e8e19d749fcb150c25a073dbb89",
        "keyLocation": f"https://{host}/4c424e8e19d749fcb150c25a073dbb89.txt",
        "urlList": urls
    }
    endpoints = [
        "https://api.indexnow.org/indexnow",
        "https://www.bing.com/indexnow",
        "https://yandex.com/indexnow"
    ]
    for ep in endpoints:
        try:
            r = requests.post(ep, json=payload, headers={"Content-Type": "application/json; charset=utf-8"}, timeout=10)
            print(f"   [IndexNow] {ep.split('/')[2]} -> Status {r.status_code}")
        except Exception as e:
            print(f"   [IndexNow] {ep.split('/')[2]} -> Error: {e}")

def submit_google_indexing_api():
    print("\n" + "=" * 70)
    print("STEP 3: SUBMITTING ALL 8 URLS TO GOOGLE INDEXING API (OFFICIAL BOT PING)")
    print("=" * 70)
    idx_creds = get_idx_credentials()
    if not idx_creds:
        print("[!] Google Indexing credentials not found.")
        return
    idx_service = build("indexing", "v3", credentials=idx_creds)
    for post_id, url, name in ALL_8_URLS:
        ok = submit_url(idx_service, url, "URL_UPDATED")
        status_txt = "200 OK (Notified)" if ok else "Failed"
        print(f"   [Google Indexing API] {name[:30]}... -> {status_txt}")
        time.sleep(0.5)

def run_live_googlebot_audit():
    print("\n" + "=" * 70)
    print("STEP 4: RUNNING LIVE GOOGLEBOT AUDIT ON ALL 8 POSTS")
    print("=" * 70)

    googlebot_headers = {
        "User-Agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
    }

    audit_records = []

    for post_id, url, name in ALL_8_URLS:
        try:
            resp = requests.get(url, headers=googlebot_headers, timeout=15)
            status = resp.status_code
            soup = BeautifulSoup(resp.text, "html.parser")

            # Canonical tag
            canonical_tag = soup.find("link", rel="canonical")
            canonical_url = canonical_tag["href"] if canonical_tag else "Missing"
            canonical_ok = (canonical_url.strip() == url.strip())

            # Robots meta
            robots_meta = soup.find("meta", attrs={"name": "robots"})
            robots_content = robots_meta["content"] if robots_meta else "None (Defaults to index,follow)"

            # Schema detection
            schemas = soup.find_all("script", type="application/ld+json")
            schema_types = []
            for s in schemas:
                try:
                    data = json.loads(s.string)
                    if isinstance(data, dict):
                        schema_types.append(data.get("@type", "Unknown"))
                    elif isinstance(data, list):
                        for el in data:
                            schema_types.append(el.get("@type", "Unknown"))
                except:
                    schema_types.append("ParseError")

            # Word count
            post_body = soup.find("div", class_="post-body") or soup
            text = post_body.get_text()
            words = len(text.split())

            # Cluster internal links
            all_links = [a.get("href", "") for a in post_body.find_all("a")]
            cluster_links = [l for l in all_links if any(k in l for k in ["ssc-bangla", "prose-cq", "poetry-cq", "short-question", "model-test"])]

            record = {
                "name": name,
                "url": url,
                "http_status": status,
                "canonical_match": canonical_ok,
                "robots_directive": robots_content,
                "schemas_found": list(set(schema_types)),
                "word_count": words,
                "cluster_links_count": len(cluster_links)
            }
            audit_records.append(record)
            print(f"[✔] Audited: {name[:30]}... | HTTP {status} | Canonical: {'MATCH' if canonical_ok else 'MISMATCH'} | Schemas: {list(set(schema_types))} | Words: {words} | Links: {len(cluster_links)}")
        except Exception as e:
            print(f"[✘] Audit failed for {url}: {e}")
            audit_records.append({"name": name, "url": url, "error": str(e)})

    # Save audit report to JSON
    report_file = os.path.join(PROJECT_ROOT, "tools", "seo_enhancer", "indexing_audit_report.json")
    with open(report_file, "w", encoding="utf-8") as f:
        json.dump(audit_records, f, ensure_ascii=False, indent=2)
    print(f"\n[✔] Audit report saved to {report_file}")

if __name__ == "__main__":
    inject_schemas_and_patch()
    submit_google_indexing_api()
    ping_all_hubs()
    submit_index_now_api([u[1] for u in ALL_8_URLS])
    run_live_googlebot_audit()
