#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/trend_forecaster/bd_exam_early_radar.py
---------------------------------------------
Helptrickbd Bangladesh Exam Early-Warning & SEO Opportunity Radar Engine.

Solves the core problem:
Publishing exam content 2-3 days before the exam results in poor Google ranking
because Google SEO indexing, crawling, and click-through authority require 21 to 45 days.
This engine predicts upcoming examinations in Bangladesh 30-60 days ahead,
fetches live educational board notices, identifies content gaps in Helptrickbd,
and generates an actionable early-publishing blueprint.

Zero-emoji compliance (Rule 12).
"""

import os
import sys
import json
import argparse
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone

try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUTPUT_REPORT = os.path.join(PROJECT_ROOT, "bd_exam_seo_radar_report.md")
LIVE_POSTS_PATH = os.path.join(PROJECT_ROOT, "scratch", "all_112_live_posts.json")

# Master Bangladesh Academic & Competitive Exam Seasonality Database
BD_EXAM_CALENDAR = [
    {
        "exam_name": "জাতীয় বিশ্ববিদ্যালয় অনার্স ২য় বর্ষ ফাইনাল পরীক্ষা",
        "category": "Political Science / Honours",
        "exam_window": "নভেম্বর - ডিসেম্বর",
        "target_month": 11,
        "lead_time_days": 40,
        "search_volume": "অত্যধিক উচ্চ (12x)",
        "target_keywords": [
            "অনার্স ২য় বর্ষ রুটিন ২০২৬",
            "অনার্স ২য় বর্ষ সাজেশন",
            "honours 2nd year exam routine",
            "অনার্স ২য় বর্ষ রাষ্ট্রবিজ্ঞান হ্যান্ডনোট",
            "ইংরেজি আবশ্যিক অনার্স ২য় বর্ষ শর্টকাট"
        ],
        "content_blueprint": "জাতীয় বিশ্ববিদ্যালয়ের অনার্স ২য় বর্ষের রুটিন, ফরম পূরণ গাইড, রাষ্ট্রবিজ্ঞান ও সমাজবিজ্ঞান সাজেশন এবং বাধ্যতামূলক ইংরেজি বিষয়ের স্পেশাল পাস মার্কস ট্রিকস।"
    },
    {
        "exam_name": "জাতীয় বিশ্ববিদ্যালয় মাস্টার্স শেষ পর্ব পরীক্ষা (৩১১৯১৩ ও ৩১১৯০১)",
        "category": "Political Science / Masters",
        "exam_window": "অক্টোবর - নভেম্বর",
        "target_month": 11,
        "lead_time_days": 35,
        "search_volume": "উচ্চ (9x)",
        "target_keywords": [
            "মাস্টার্স ফাইনাল ভূরাজনীতি ও বাংলাদেশ হ্যান্ডনোট",
            "মাস্টার্স রাষ্ট্রবিজ্ঞান সাজেশন বিষয়কোড ৩১১৯১৩",
            "সাম্প্রতিক রাষ্ট্রচিন্তা ৩১১৯০১ সাজেশন",
            "মাস্টার্স শেষ পর্ব পরীক্ষার রুটিন ২০২৬"
        ],
        "content_blueprint": "মাস্টার্স ফাইনাল ভূ-রাজনীতি ও বাংলাদেশ (৩১১৯১৩) এবং সাম্প্রতিক রাষ্ট্রচিন্তা (৩১১৯০১) কোর্সের ক, খ ও গ বিভাগের পূর্ণাঙ্গ সমাধান।"
    },
    {
        "exam_name": "এসএসসি ও দাখিল নির্বাচনী (টেস্ট) পরীক্ষা",
        "category": "School / SSC",
        "exam_window": "অক্টোবর - নভেম্বর",
        "target_month": 11,
        "lead_time_days": 30,
        "search_volume": "বিশাল (15x)",
        "target_keywords": [
            "এসএসসি টেস্ট পরীক্ষার প্রশ্ন ২০২৬",
            "এসএসসি বাংলা ১ম পত্র টেস্ট সাজেশন",
            "ssc english 2nd paper model test",
            "দাখিল নির্বাচনী পরীক্ষার প্রশ্ন ব্যাংক"
        ],
        "content_blueprint": "এসএসসি ও দাখিল পরীক্ষার্থীদের নির্বাচনী পরীক্ষার জন্য বাংলা ১ম, ইংরেজি ২য় পত্র এবং গণিতের ১০০% কমন টেস্ট সাজেশন ও মডেল টেস্ট।"
    },
    {
        "exam_name": "পাবলিক বিশ্ববিদ্যালয় ভর্তি পরীক্ষা সার্কুলার ও প্রস্তুতি (ঢাবি, রাবি, গুচ্ছ)",
        "category": "University Admission",
        "exam_window": "ডিসেম্বর - ফেব্রুয়ারি",
        "target_month": 12,
        "lead_time_days": 60,
        "search_volume": "অত্যধিক উচ্চ (14x)",
        "target_keywords": [
            "বিশ্ববিদ্যালয় ভর্তি আবেদন ২০২৬",
            "ঢাবি খ ইউনিট ভর্তি প্রস্তুতি ও মানবণ্টন",
            "গুচ্ছ ভর্তি সার্কুলার ও কাটমার্কস",
            "মেডিকেল ভর্তি পরীক্ষা আবেদন ও সিলেবাস"
        ],
        "content_blueprint": "সকল পাবলিক বিশ্ববিদ্যালয়ের ভর্তি পরীক্ষার যোগ্যতা, জিপিএ রিকোয়ারমেন্টস, আসন সংখ্যা, আবেদন ফি এবং বিগত বছরের কাটমার্কস অ্যানালাইসিস।"
    },
    {
        "exam_name": "৪৭তম বিসিএস প্রিলিমিনারি সার্কুলার ও প্রস্তুতি বুক লিস্ট",
        "category": "Job Study / BCS",
        "exam_window": "নভেম্বর - জানুয়ারি",
        "target_month": 12,
        "lead_time_days": 45,
        "search_volume": "দীর্ঘস্থায়ী উচ্চ (10x)",
        "target_keywords": [
            "৪৭তম বিসিএস সার্কুলার ২০২৬",
            "বিসিএস প্রিলিমিনারি ২০০ নম্বরের মানবণ্টন",
            "বিসিএস প্রস্তুতি বুক লিস্ট",
            "বিসিএস সাধারণ জ্ঞান বাংলাদেশ ও আন্তর্জাতিক বিষয়াবলী"
        ],
        "content_blueprint": "বিসিএস প্রিলিমিনারির ১০টি বিষয়ের নম্বর বণ্টন, ক্যাডার চয়েস নির্দেশিকা এবং প্রথমবারে প্রিলি পাসের সুনির্দিষ্ট বুক লিস্ট ও পড়ার রুটিন।"
    },
    {
        "exam_name": "এসএসসি ও দাখিল বোর্ড পরীক্ষা ২০২৭/২০২৬ চূড়ান্ত প্রস্তুতি",
        "category": "School / SSC",
        "exam_window": "ফেব্রুয়ারি - মার্চ",
        "target_month": 2,
        "lead_time_days": 90,
        "search_volume": "সর্বোচ্চ (20x)",
        "target_keywords": [
            "ssc routine 2027",
            "এসএসসি বাংলা সাজেশন",
            "ssc english 1st paper suggestion 2027",
            "এসএসসি গণিত সৃজনশীল ১০০% কমন"
        ],
        "content_blueprint": "এসএসসি ও দাখিল বোর্ড পরীক্ষার চূড়ান্ত এ প্লাস গাইডলাইন, বোর্ড প্রশ্ন সমাধান ও রিভিশন ট্রিকস।"
    },
    {
        "exam_name": "প্রাথমিক সহকারী শিক্ষক নিয়োগ পরীক্ষা (প্রাইমারি শিক্ষক)",
        "category": "Job Study / Primary",
        "exam_window": "নভেম্বর - জানুয়ারি",
        "target_month": 12,
        "lead_time_days": 45,
        "search_volume": "বিশাল (12x)",
        "target_keywords": [
            "প্রাথমিক শিক্ষক নিয়োগ পরীক্ষা তারিখ",
            "প্রাইমারি শিক্ষক নিয়োগ সাজেশন",
            "প্রাইমারি প্রশ্ন ব্যাংক সমাধান",
            "প্রাথমিক শিক্ষক ভাইভা প্রস্তুতি"
        ],
        "content_blueprint": "প্রাইমারি শিক্ষক নিয়োগের ৮০ নম্বরের মানবণ্টন, বিগত ১০ বছরের প্রশ্ন সমাধান ও শর্টকাট টেকনিক।"
    },
    {
        "exam_name": "এইচএসসি ও আলিম পরীক্ষা ২০২৬/২০২৭ প্রস্তুতি",
        "category": "College / HSC",
        "exam_window": "এপ্রিল - জুন",
        "target_month": 4,
        "lead_time_days": 90,
        "search_volume": "সর্বোচ্চ (18x)",
        "target_keywords": [
            "এইচএসসি পরীক্ষার রুটিন ২০২৬",
            "এইচএসসি বাংলা ১ম পত্র সাজেশন",
            "এইচএসসি আইসিটি হ্যান্ডনোট",
            "এইচএসসি পৌরনীতি ও সুশাসন"
        ],
        "content_blueprint": "এইচএসসি পরীক্ষার্থীদের জন্য আইসিটি ও বাংলা প্রথম পত্রের সুপার শর্ট হ্যান্ডনোট।"
    }
]

LIVE_NEWS_QUERIES = [
    "পরীক্ষা routine",
    "জাতীয় বিশ্ববিদ্যালয় নোটিশ",
    "এসএসসি পরীক্ষা",
    "এইচএসসি পরীক্ষা",
    "বিশ্ববিদ্যালয় ভর্তি পরীক্ষা",
    "বিসিএস সার্কুলার"
]


def fetch_live_education_notices() -> list[dict]:
    """Fetches real-time educational notices and news from Google News Bangladesh RSS."""
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    live_notices = []
    seen_titles = set()

    for q in LIVE_NEWS_QUERIES:
        url = f"https://news.google.com/rss/search?q={urllib.parse.quote(q)}&hl=bn&gl=BD&ceid=BD:bn"
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=7) as resp:
                root = ET.fromstring(resp.read())
                items = root.findall("./channel/item")
                for item in items[:4]:
                    title_elem = item.find("title")
                    pub_elem = item.find("pubDate")
                    link_elem = item.find("link")
                    if title_elem is not None and title_elem.text:
                        title = title_elem.text.strip()
                        if title not in seen_titles:
                            seen_titles.add(title)
                            live_notices.append({
                                "title": title,
                                "pub_date": pub_elem.text.strip() if pub_elem is not None else "",
                                "link": link_elem.text.strip() if link_elem is not None else "",
                                "source_query": q
                            })
        except Exception:
            pass

    return live_notices[:10]


def load_helptrickbd_live_titles() -> list[str]:
    """Loads existing live post titles from scratch/all_112_live_posts.json."""
    if not os.path.exists(LIVE_POSTS_PATH):
        return []
    try:
        with open(LIVE_POSTS_PATH, "r", encoding="utf-8") as f:
            posts = json.load(f)
            return [p.get("title", "") for p in posts]
    except Exception:
        return []


def evaluate_seo_golden_window(current_month: int) -> list[dict]:
    """
    Evaluates which exams are in the 30-45 day SEO Golden Window for publishing today.
    Formula: If current month matches target_month or target_month - 1, it's URGENT/GOLDEN.
    """
    radar_results = []
    live_titles = load_helptrickbd_live_titles()

    for exam in BD_EXAM_CALENDAR:
        target_m = exam["target_month"]
        # Calculate month difference
        diff_months = (target_m - current_month) % 12

        if diff_months == 0:
            status = "URGENT ACTION (গোল্ডেন উইন্ডো — আজই পোস্ট লিখতে হবে)"
            urgency_score = 1
            reason = "পরীক্ষা ১ মাসের মধ্যে অনুষ্ঠিত হবে। গুগল ইন্ডেক্সিং ও র‍্যাংকিং পাওয়ার জন্য এখনই পোস্ট করার শেষ সুযোগ।"
        elif diff_months == 1:
            status = "IDEAL TIMING (আদর্শ গোল্ডেন উইন্ডো — পরবর্তী ৩০ দিনের টার্গেট)"
            urgency_score = 2
            reason = "পরীক্ষার ৩০-৬০ দিন পূর্বে পোস্ট করলে পরীক্ষার দিন সার্চ ভলিউম বাড়ামাত্র গুগল ১ নম্বর পজিশন নিশ্চিত করে।"
        elif diff_months == 2:
            status = "EARLY PREPARATION (আগাম প্রস্তুতি — ড্রাফট ও রিসার্চ শুরু করুন)"
            urgency_score = 3
            reason = "৬০-৯০ দিন পূর্বে ব্যাকলিংক ও কনটেন্ট পিলারের আর্কিটেকচার তৈরি করার উপযুক্ত সময়।"
        else:
            status = "OFF-SEASON (এখন পোস্ট না করলেও চলবে)"
            urgency_score = 4
            reason = "পরীক্ষা অনুষ্ঠিত হতে বেশ দেরি আছে।"

        # Check coverage on Helptrickbd
        has_coverage = False
        matching_titles = []
        for kw in exam["target_keywords"]:
            for t in live_titles:
                if any(k.lower() in t.lower() for k in [kw.split()[0], kw.split()[-1]]):
                    has_coverage = True
                    matching_titles.append(t)
                    break
            if has_coverage:
                break

        radar_results.append({
            "exam_name": exam["exam_name"],
            "category": exam["category"],
            "exam_window": exam["exam_window"],
            "status": status,
            "urgency_score": urgency_score,
            "reason": reason,
            "search_volume": exam["search_volume"],
            "target_keywords": exam["target_keywords"],
            "content_blueprint": exam["content_blueprint"],
            "has_coverage": has_coverage,
            "matching_titles": matching_titles[:2]
        })

    # Sort by urgency score
    radar_results.sort(key=lambda x: x["urgency_score"])
    return radar_results


def generate_radar_report(radar_results: list[dict], live_notices: list[dict], current_date: datetime) -> str:
    """Generates the master markdown report for the user."""
    lines = []
    lines.append("# বাংলাদেশ এক্সাম আর্লি-ওয়ার্নিং ও এসইও র‍্যাংকিং রাডার রিপোর্ট")
    lines.append(f"**তারিখ:** {current_date.strftime('%Y-%m-%d')} | **চলতি মাস:** {current_date.strftime('%B %Y')}")
    lines.append("**উদ্দেশ্য:** পরীক্ষার ৩০ থেকে ৪৫ দিন পূর্বে আগাম কন্টেন্ট তৈরি করে গুগলের ১ নম্বর পজিশন দখল করা।\n")

    lines.append("## ১. মূল এসইও গোল্ডেন রুল (কেন পরীক্ষার ৩০-৪৫ দিন আগেই পোস্ট করতে হবে)")
    lines.append("- **গুগল ট্রাস্ট ও ক্রলিং টাইম:** গুগলে একটি নতুন পোস্ট ইনডেক্স হয়ে ক্লিক ও ইম্প্রেশনের মাধ্যমে অথরিটি তৈরি করতে ন্যূনতম ২১ থেকে ৩০ দিন সময় লাগে।")
    lines.append("- **দেরিতে পোস্ট করার ক্ষতি:** পরীক্ষার ২-৩ দিন আগে পোস্ট করলে সেই পোস্ট কখনো ১ নম্বরে আসতে পারে না; কারণ পুরনো সাইটগুলো আগেই অবস্থান দখল করে নেয়।")
    lines.append("- **গোল্ডেন উইন্ডো নীতি:** যখন পরীক্ষার ১-২ মাস বাকি থাকে, তখনই ১,৫০০+ শব্দের পূর্ণাঙ্গ গাইডলাইন পোস্ট করে গুগলকে জানাতে হবে। ফলে পরীক্ষার রুটিন ও প্রশ্ন খোঁজার পিক টাইমে আপনার পোস্ট শীর্ষে থাকবে।\n")

    lines.append("## ২. আজই পোস্ট করার সর্বোচ্চ অগ্রাধিকার তালিকা (Urgent & Golden Window)")
    lines.append("| অগ্রাধিকার | পরীক্ষার নাম | পরীক্ষার সময়কাল | সার্চ ভলিউম | আমাদের সাইটে কভার আছে কি? | অ্যাকশন প্ল্যান |")
    lines.append("| :--- | :--- | :--- | :--- | :--- | :--- |")

    for r in radar_results:
        if r["urgency_score"] <= 2:
            cov_status = "হ্যাঁ (আপডেট করুন)" if r["has_coverage"] else "না (জরুরি নতুন পোস্ট)"
            lines.append(f"| **{r['status'].split('(')[0].strip()}** | **{r['exam_name']}** | {r['exam_window']} | {r['search_volume']} | `{cov_status}` | {r['content_blueprint'][:60]}... |")

    lines.append("\n## ৩. পরীক্ষার বিস্তারিত অ্যাকশন ব্লুপ্রিন্ট ও টার্গেট কি-ওয়ার্ডস\n")
    for idx, r in enumerate(radar_results, 1):
        if r["urgency_score"] <= 2:
            lines.append(f"### ৩.{idx}. {r['exam_name']} ({r['category']})")
            lines.append(f"- **স্ট্যাটাস:** {r['status']}")
            lines.append(f"- **পরীক্ষার সম্ভাব্য সময়কাল:** {r['exam_window']}")
            lines.append(f"- **কেন এখনই লিখতে হবে:** {r['reason']}")
            lines.append(f"- **টার্গেট কি-ওয়ার্ডস:** `{', '.join(r['target_keywords'])}`")
            lines.append(f"- **কনটেন্ট ব্লুপ্রিন্ট:** {r['content_blueprint']}")
            if r["has_coverage"]:
                lines.append(f"- **সাইটে বিদ্যমান রিলেটেড পোস্ট:** {r['matching_titles']}")
            else:
                lines.append("- **কনটেন্ট গ্যাপ:** সাইটে এই বিষয়ে এখনও পূর্ণাঙ্গ পিলার পোস্ট নেই। দ্রুত পোস্ট তৈরি করা প্রয়োজন।")
            lines.append("")

    if live_notices:
        lines.append("## ৪. লাইভ এডুকেশন বোর্ড ও এক্সাম নোটিশ ট্র্যাকার (আজকের সর্বশেষ সংবাদ)")
        lines.append("গুগল নিউজ ও শিক্ষা বোর্ড সোর্স থেকে সরাসরি সংগৃহীত রিয়েল-টাইম তথ্য:")
        for idx, n in enumerate(live_notices, 1):
            lines.append(f"{idx}. **{n['title']}** (প্রকাশকাল: {n['pub_date'][:16]})")
        lines.append("")

    lines.append("## ৫. হেল্পট্রিকবিডির জন্য পরবর্তী ৭ দিনের সুনির্দিষ্ট কন্টেন্ট ক্যালেন্ডার")
    lines.append("1. **দিন ০১-০২:** জাতীয় বিশ্ববিদ্যালয় অনার্স ২য় বর্ষ পরীক্ষার রুটিন ও রাষ্ট্রবিজ্ঞান স্পেশাল সাজেশন।")
    lines.append("2. **দিন ০৩-০৪:** এসএসসি ২০২৬/২০২৭ নির্বাচনী (টেস্ট) পরীক্ষার বাংলা ১ম পত্র ও ইংরেজি ২য় পত্র মডেল টেস্ট।")
    lines.append("3. **দিন ০৫-০৬:** পাবলিক বিশ্ববিদ্যালয় ভর্তি পরীক্ষা ২০২৬ সার্কুলার, ইউনিটভিত্তিক যোগ্যতা ও মানবণ্টন।")
    lines.append("4. **দিন ০৭:** ৪৭তম বিসিএস প্রিলিমিনারি বুক লিস্ট ও ২০০ নম্বরের বিষয়ভিত্তিক পূর্ণাঙ্গ রুটিন।")

    report_text = "\n".join(lines)
    with open(OUTPUT_REPORT, "w", encoding="utf-8") as f:
        f.write(report_text)
    return report_text


def main():
    parser = argparse.ArgumentParser(description="Bangladesh Exam Early-Warning & SEO Radar Engine for Helptrickbd")
    parser.add_argument("--month", type=int, help="Target month (1-12, default: current month)")
    args = parser.parse_args()

    now = datetime.now()
    cur_month = args.month if args.month else now.month

    print("=" * 70)
    print("  HELPTRICKBD BANGLADESH EXAM EARLY-WARNING & SEO RADAR ENGINE")
    print("=" * 70)
    print(f"[*] চলতি তারিখ: {now.strftime('%Y-%m-%d')} (মাস: {cur_month})")

    print("[*] রিয়েল-টাইম শিক্ষা বোর্ড ও এক্সাম নোটিশ ট্র্যাক করা হচ্ছে...")
    live_notices = fetch_live_education_notices()
    print(f"[OK] {len(live_notices)}টি লাইভ নোটিশ সফলভাবে সংগ্রহ করা হয়েছে।")

    print("[*] এসইও ৩০-৪৫ দিন গোল্ডেন উইন্ডো ক্যালকুলেশন সম্পন্ন হচ্ছে...")
    radar_results = evaluate_seo_golden_window(cur_month)

    urgent_count = sum(1 for r in radar_results if r["urgency_score"] <= 2)
    print(f"[OK] মোট {urgent_count}টি পরীক্ষা বর্তমানে ৩০-৪৫ দিনের এসইও গোল্ডেন উইন্ডোতে রয়েছে।")

    print(f"[*] রিপোর্ট তৈরি ও সেভ করা হচ্ছে: {OUTPUT_REPORT}")
    generate_radar_report(radar_results, live_notices, now)
    print("[SUCCESS] এক্সাম রাডার রিপোর্ট সফলভাবে জেনারেট হয়েছে!")
    print("=" * 70)


if __name__ == "__main__":
    main()
