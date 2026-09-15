#!/usr/bin/env python3
"""
tools/trend_forecaster/trend_predictor.py
Google Trends & Seasonal Traffic Forecaster for Helptrickbd.
Combines real-time Google Trends Bangladesh data with an academic/exam seasonality calendar
to forecast search spikes 15-30 days before competitors.
"""

import os
import sys
import json
import argparse
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
import requests

try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
REPORT_PATH = os.path.join(PROJECT_ROOT, "seasonal_traffic_forecast.md")
TRENDS_RSS_URL = "https://trends.google.com/trending/rss?geo=BD"

# Bangladesh Educational, Career, and Seasonal Search Surge Calendar (Months 1 to 12)
BANGLADESH_SEASONAL_CALENDAR = {
    1: [
        {"topic": "এসএসসি পরীক্ষার চূড়ান্ত প্রস্তুতি ও রুটিন", "category": "শিক্ষা", "surge_factor": "8x", "target_keywords": ["ssc routine 2026", "এসএসসি সাজেশন", "এসএসসি প্রবেশপত্র"]},
        {"topic": "বিশ্ববিদ্যালয় ভর্তি পরীক্ষা ও সিট প্ল্যান", "category": "উচ্চশিক্ষা", "surge_factor": "6x", "target_keywords": ["ঢাবি ভর্তি প্রস্তুতি", "মেডিকেল ভর্তি পরীক্ষা", "বুয়েট আবেদন"]},
        {"topic": "বিসিএস প্রিলিমিনারি মডেল টেস্ট ও শর্ট সাজেশন", "category": "চাকরি", "surge_factor": "5x", "target_keywords": ["bcs preliminary preparation", "বিসিএস সাধারণ জ্ঞান", "বিসিএস বাংলা"]},
    ],
    2: [
        {"topic": "২১শে ফেব্রুয়ারি ও আন্তর্জাতিক মাতৃভাষা দিবস ইতিহাস", "category": "ইতিহাস", "surge_factor": "10x", "target_keywords": ["ভাষা আন্দোলন ইতিহাস", "২১শে ফেব্রুয়ারি বক্তব্য", "শহীদ দিবস প্রবন্ধ"]},
        {"topic": "এসএসসি পরীক্ষা চলমান ও প্রশ্ন সমাধান বিশ্লেষণ", "category": "শিক্ষা", "surge_factor": "12x", "target_keywords": ["এসএসসি প্রশ্ন সমাধান", "এসএসসি বাংলা ১ম পত্র", "এসএসসি গণিত"]},
        {"topic": "একুশে বইমেলা ও বাংলা সাহিত্যের বিশিষ্ট কবি-লেখক", "category": "সাহিত্য", "surge_factor": "4x", "target_keywords": ["বইমেলা ইতিহাস", "রবীন্দ্রনাথ ও নজরুল জীবন", "বাংলা ব্যাকরণ"]},
    ],
    3: [
        {"topic": "২৬শে মার্চ স্বাধীনতা দিবস ও মুক্তিযুদ্ধ পূর্ণাঙ্গ হ্যান্ডনোট", "category": "ইতিহাস", "surge_factor": "10x", "target_keywords": ["স্বাধীনতা দিবস প্রবন্ধ", "১৯৭১ মুক্তিযুদ্ধ হ্যান্ডনোট", "৭ই মার্চের ভাষণ বিশ্লেষণ"]},
        {"topic": "পবিত্র রমজান ও সাহরি-ইফতারের সময়সূচি", "category": "ইসলামিক", "surge_factor": "15x", "target_keywords": ["রমজানের সময়সূচি", "রোজা রাখার নিয়ত", "ইফতারের দোয়া", "তারাবীহ নামাজ"]},
        {"topic": "এইচএসসি পরীক্ষার ফরম পূরণ ও বোর্ড রুটিন", "category": "শিক্ষা", "surge_factor": "5x", "target_keywords": ["hsc exam routine", "এইচএসসি পরীক্ষার সময়সূচি", "এইচএসসি ফরম পূরণ"]},
    ],
    4: [
        {"topic": "পহেলা বৈশাখ ও বাংলা নববর্ষের ঐতিহ্য", "category": "সংস্কৃতি", "surge_factor": "8x", "target_keywords": ["পহেলা বৈশাখ ইতিহাস", "মঙ্গল শোভাযাত্রা তাৎপর্য", "নববর্ষ প্রবন্ধ"]},
        {"topic": "ঈদুল ফিতর ও ফিতরার হিসাব-নিয়ম", "category": "ইসলামিক", "surge_factor": "12x", "target_keywords": ["ঈদুল ফিতর নামাজ নিয়ম", "ফিতরা কত টাকা", "ঈদের শুভেচ্ছা মেসেজ"]},
        {"topic": "জাতীয় বিশ্ববিদ্যালয় ডিগ্রি ও অনার্স পরীক্ষার ফলাফল", "category": "উচ্চশিক্ষা", "surge_factor": "9x", "target_keywords": ["nu result check", "অনার্স ১ম বর্ষ ফলাফল", "ডিগ্রি পাস মার্কস"]},
    ],
    5: [
        {"topic": "এসএসসি পরীক্ষার ফলাফল ও পুনঃনিরীক্ষণ আবেদন নিয়ম", "category": "শিক্ষা", "surge_factor": "14x", "target_keywords": ["ssc result mark sheet", "বোর্ড চ্যালেঞ্জ আবেদন নিয়ম", "কলেজ ভর্তি আবেদন"]},
        {"topic": "একাদশ শ্রেণিতে অনলাইন ভর্তি ও কলেজ চয়েস নিয়ম", "category": "শিক্ষা", "surge_factor": "10x", "target_keywords": ["xi class admission", "কলেজ ভর্তির নিশ্চায়ন", "সেরা সরকারি কলেজ তালিকা"]},
        {"topic": "জাতীয় বিশ্ববিদ্যালয় মাস্টার্স শেষ বর্ষ সাজেশন", "category": "উচ্চশিক্ষা", "surge_factor": "6x", "target_keywords": ["masters political science suggestion", "মাস্টার্স পরীক্ষা রুটিন", "মাস্টার্স রেজাল্ট"]},
    ],
    6: [
        {"topic": "পবিত্র ঈদুল আজহা ও কোরবানির সঠিক নিয়ম-মাসায়েল", "category": "ইসলামিক", "surge_factor": "12x", "target_keywords": ["কোরবানির পশু জবাই নিয়ম", "কোরবানির মাসায়েল", "ঈদুল আজহা নামাজ"]},
        {"topic": "এইচএসসি পরীক্ষার চূড়ান্ত রিভিশন ও মডেল টেস্ট", "category": "শিক্ষা", "surge_factor": "8x", "target_keywords": ["hsc exam final revision", "এইচএসসি বাংলা সাজেশন", "এইচএসসি আইসিটি হ্যান্ডনোট"]},
        {"topic": "বাজেট বিশ্লেষণ ও বাংলাদেশের অর্থনৈতিক সমীক্ষা", "category": "অর্থনীতি", "surge_factor": "5x", "target_keywords": ["বাংলাদেশ জাতীয় বাজেট", "মূল্যস্ফীতি ও রাজস্ব নীতি", "এডিপি বরাদ্দ"]},
    ],
    7: [
        {"topic": "এইচএসসি পরীক্ষা পর্যবেক্ষণ ও বোর্ড প্রশ্ন অ্যানালাইসিস", "category": "শিক্ষা", "surge_factor": "10x", "target_keywords": ["hsc question analysis", "এইচএসসি রসায়ন ও পদার্থ", "এইচএসসি পৌরনীতি"]},
        {"topic": "প্রাথমিক সহকারী শিক্ষক নিয়োগ প্রস্তুতি ও ভাইভা", "category": "চাকরি", "surge_factor": "7x", "target_keywords": ["primary teacher exam", "প্রাইমারি ভাইভা প্রস্তুতি", "প্রাইমারি প্রশ্ন ব্যাংক"]},
        {"topic": "ডিগ্রি ও অনার্স ইনকোর্স ও ব্যবহারিক পরীক্ষার নিয়ম", "category": "উচ্চশিক্ষা", "surge_factor": "5x", "target_keywords": ["জাতীয় বিশ্ববিদ্যালয় নোটিশ", "অনার্স ব্যবহারিক পরীক্ষা", "ইনকোর্স নম্বর"]},
    ],
    8: [
        {"topic": "সার্টিফিকেট নাম, পিতা-মাতা ও বয়স সংশোধন অনলাইন আবেদন", "category": "শিক্ষা সেবা", "surge_factor": "7x", "target_keywords": ["certificate correction online", "বোর্ড সার্টিফিকেট নাম সংশোধন", "সোনালী সেবা ফি"]},
        {"topic": "জাতীয় বিশ্ববিদ্যালয় অনার্স ভর্তি আবেদন ও মেধা তালিকা", "category": "উচ্চশিক্ষা", "surge_factor": "9x", "target_keywords": ["honours admission nu", "রিলিজ স্লিপ আবেদন", "অনার্স সাবজেক্ট চয়েস"]},
        {"topic": "পবিত্র আশুরা ও কারবালার ঐতিহাসিক প্রেক্ষাপট", "category": "ইতিহাস", "surge_factor": "6x", "target_keywords": ["আশুরা তাৎপর্য", "কারবালার যুদ্ধ ইতিহাস", "মহররম মাসের ফজিলত"]},
    ],
    9: [
        {"topic": "জাতীয় বিশ্ববিদ্যালয় অনার্স ১ম/২য়/৩য় বর্ষ ফাইনাল রুটিন", "category": "উচ্চশিক্ষা", "surge_factor": "11x", "target_keywords": ["nu exam routine", "রাষ্ট্রবিজ্ঞান বিভাগ সাজেশন", "সমাজবিজ্ঞান হ্যান্ডনোট"]},
        {"topic": "পবিত্র ঈদে মিলাদুন্নবী (সা.) ও সিরাতুন্নবী আলোচনা", "category": "ইসলামিক", "surge_factor": "8x", "target_keywords": ["ঈদে মিলাদুন্নবী ইতিহাস", "রাসূল (সা.) এর জীবনী", "মিলাদ ও কিয়াম"]},
        {"topic": "ভোকেশনাল ও কারিগরি শিক্ষা বোর্ড ডিপ্লোমা রুটিন", "category": "কারিগরি", "surge_factor": "5x", "target_keywords": ["কারিগরি শিক্ষা বোর্ড নোটিশ", "পলিটেকনিক সেমিস্টার পরীক্ষা", "ডিপ্লোমা সাজেশন"]},
    ],
    10: [
        {"topic": "এইচএসসি পরীক্ষার ফলাফল ও মার্কশিট ডাউনলোড নিয়ম", "category": "শিক্ষা", "surge_factor": "15x", "target_keywords": ["hsc result with marksheet", "এইচএসসি বোর্ড চ্যালেঞ্জ ফি", "বিশ্ববিদ্যালয় ভর্তি আবেদন"]},
        {"topic": "সরকারি চাকরি ও ব্যাংক অফিসার নিয়োগ সার্কুলার", "category": "চাকরি", "surge_factor": "6x", "target_keywords": ["govt job circular", "কম্বাইন্ড ব্যাংক অফিসার প্রস্তুতি", "এনটিআরসিএ শিক্ষক নিবন্ধন"]},
        {"topic": "বিশ্ববিদ্যালয় গুচ্ছ (GST) ভর্তি পরীক্ষার আবেদন", "category": "উচ্চশিক্ষা", "surge_factor": "8x", "target_keywords": ["গুচ্ছ ভর্তি সার্কুলার", "জিএসটি সিট প্ল্যান", "বিশ্ববিদ্যালয় কাটমার্কস"]},
    ],
    11: [
        {"topic": "আয়কর রিটার্ন দাখিল ও ই-ট্যাক্স অনলাইন নিয়ম", "category": "সরকারি সেবা", "surge_factor": "12x", "target_keywords": ["tax return online submission", "জিরো রিটার্ন দাখিল নিয়ম", "টিন সার্টিফিকেট"]},
        {"topic": "জাতীয় বিশ্ববিদ্যালয় মাস্টার্স প্রিলিমিনারি ও ফাইনাল পরীক্ষা", "category": "উচ্চশিক্ষা", "surge_factor": "9x", "target_keywords": ["masters exam center list", "মাস্টার্স সাজেশন রাষ্ট্রবিজ্ঞান", "আন্তর্জাতিক সম্পর্ক হ্যান্ডনোট"]},
        {"topic": "জেএসসি ও পিইসি সনদপত্র ও বৃত্তি পরীক্ষার ফলাফল", "category": "শিক্ষা", "surge_factor": "5x", "target_keywords": ["ট্যালেন্টপুল বৃত্তি ফলাফল", "বৃত্তি পরীক্ষার রেজাল্ট", "বৃত্তি সনদপত্র"]},
    ],
    12: [
        {"topic": "১৬ই ডিসেম্বর মহান বিজয় দিবস ও ঐতিহাসিক ঘটনাপ্রবাহ", "category": "ইতিহাস", "surge_factor": "10x", "target_keywords": ["বিজয় দিবস প্রবন্ধ", "১৯৭১ পাকিস্তানি বাহিনীর আত্মসমর্পণ", "বীরশ্রেষ্ঠদের জীবনী"]},
        {"topic": "নতুন শিক্ষাবর্ষের বই উৎসব ও নতুন ক্লাসে ভর্তি নিয়ম", "category": "শিক্ষা", "surge_factor": "7x", "target_keywords": ["বই উৎসব ২০২৬", "লটারি ভর্তি ফলাফল", "সরকারি স্কুল ভর্তি"]},
        {"topic": "নতুন বিসিএস সার্কুলার প্রকাশ ও আবেদন ফরম পূরণ", "category": "চাকরি", "surge_factor": "14x", "target_keywords": ["new bcs circular", "বিসিএস ক্যাডার চয়েস লিস্ট", "বিসিএস আবেদন পদ্ধতি"]},
    ]
}


def fetch_live_google_trends_bd() -> list[str]:
    """Fetches real-time search trends from Google Trends RSS feed for Bangladesh."""
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    trending_topics = []
    try:
        resp = requests.get(TRENDS_RSS_URL, headers=headers, timeout=8)
        if resp.status_code == 200:
            root = ET.fromstring(resp.content)
            for item in root.findall("./channel/item"):
                title = item.find("title")
                if title is not None and title.text:
                    trending_topics.append(title.text.strip())
    except Exception as e:
        print(f"⚠️ Google Trends RSS notice: {e}", file=sys.stderr)
    return trending_topics[:8]


def generate_forward_forecast(current_month: int = None) -> tuple[list[dict], list[dict]]:
    """Generates 30-day and 60-day ahead topic forecast for Helptrickbd."""
    if not current_month:
        current_month = datetime.now().month

    next_month = current_month + 1 if current_month < 12 else 1
    following_month = next_month + 1 if next_month < 12 else 1

    next_month_trends = BANGLADESH_SEASONAL_CALENDAR.get(next_month, [])
    following_month_trends = BANGLADESH_SEASONAL_CALENDAR.get(following_month, [])

    return next_month_trends, following_month_trends


def generate_forecast_report(next_month_trends: list[dict], following_trends: list[dict], live_trends: list[str], output_file: str):
    """Generates an actionable 30-day forecast report for content publishing."""
    now = datetime.now(timezone.utc)
    current_month_name = now.strftime("%B %Y")
    next_month_name = (now + timedelta(days=30)).strftime("%B %Y")

    md = []
    md.append("# 📈 Helptrickbd Google Trends & Seasonal Traffic Forecast")
    md.append(f"**Generated Date:** {now.strftime('%Y-%m-%d %H:%M UTC')}")
    md.append(f"**Target Optimization Window:** {next_month_name} (পরবর্তী ৩০-৬০ দিনের আগাম প্রস্তুতি)\n")

    md.append("## 🚀 ১. আগামী ৩০ দিনে সর্বাধিক ট্রাফিক আসার শীর্ষ ৩টি টপিক (Must-Publish):")
    md.append("| ক্রম | টপিক ও বিষয়বস্তু | ক্যাটাগরি | প্রত্যাশিত ট্রাফিক সার্জ | টার্গেট ফোকাস কি-ওয়ার্ডস | অ্যাকশন প্ল্যান |")
    md.append("| :---: | :--- | :---: | :---: | :--- | :--- |")

    for idx, item in enumerate(next_month_trends, 1):
        kw_str = ", ".join(item["target_keywords"])
        md.append(f"| {idx} | **{item['topic']}** | `{item['category']}` | ⚡ **{item['surge_factor']}** | `{kw_str}` | এখনই ১,৫০০ শব্দের গাইড তৈরি করে শিডিউল করুন |")

    md.append("\n## 🔮 ২. পরবর্তী ৬০ দিনের লং-টার্ম ট্রাফিক সুযোগ (Following Month):")
    for idx, item in enumerate(following_trends, 1):
        kw_str = ", ".join(item["target_keywords"])
        md.append(f"- **{item['topic']}** (`{item['category']}`) — ট্রাফিক সার্জ: `{item['surge_factor']}` | কি-ওয়ার্ড: `{kw_str}`")

    if live_trends:
        md.append("\n## 📡 ৩. আজ গুগলে বাংলাদেশের রিয়েল-টাইম ট্রেন্ডিং সার্চেস (Live Trends):")
        for idx, t in enumerate(live_trends, 1):
            md.append(f"{idx}. 🔍 {t}")

    report_content = "\n".join(md)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(report_content)
    return report_content


def main():
    parser = argparse.ArgumentParser(description="Google Trends & Seasonal Traffic Forecaster for Helptrickbd")
    parser.add_argument("--month", type=int, help="Target current month (1-12, default: current month)")
    parser.add_argument("--output", "-o", default=REPORT_PATH, help="Path to save forecast report")

    args = parser.parse_args()

    print("=" * 65)
    print("📈 Helptrickbd Google Trends & Seasonal Traffic Forecaster")
    print("=" * 65)

    live_trends = fetch_live_google_trends_bd()
    print(f"📡 Fetched {len(live_trends)} live trending search queries from Google Trends BD...")

    cur_m = args.month if args.month else datetime.now().month
    next_m_trends, foll_m_trends = generate_forward_forecast(current_month=cur_m)

    print(f"\n🔮 Forecasting Next 30–60 Days Traffic Surge for Helptrickbd...")
    for item in next_m_trends:
        print(f"  ⚡ [{item['surge_factor']}] {item['topic']} ({item['category']})")

    generate_forecast_report(next_m_trends, foll_m_trends, live_trends, args.output)
    print(f"\n💾 Forecast Report saved to: {args.output}")


if __name__ == "__main__":
    main()
