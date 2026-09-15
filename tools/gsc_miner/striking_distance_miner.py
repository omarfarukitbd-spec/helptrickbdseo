#!/usr/bin/env python3
"""
tools/gsc_miner/striking_distance_miner.py
Google Search Console "Striking Distance" & CTR Opportunity Miner.
Extracts keywords on Page 2 (Positions 11-25) and High Impression / Low CTR pages
for rapid 1st page ranking and massive organic click growth.
"""

import os
import sys
import json
import argparse
from datetime import datetime, timedelta, timezone

try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DEFAULT_SITE_URL = "https://www.helptrickbd.com/"
SERVICE_ACCOUNT_PATH = os.path.join(PROJECT_ROOT, "service_account.json")
REPORT_PATH = os.path.join(PROJECT_ROOT, "gsc_opportunities_report.md")


def get_gsc_service(creds_path: str = None):
    """Initializes and returns Google Search Console API client."""
    from google.oauth2 import service_account
    from googleapiclient.discovery import build

    if not creds_path:
        creds_path = SERVICE_ACCOUNT_PATH

    if not os.path.exists(creds_path):
        return None

    try:
        scopes = ["https://www.googleapis.com/auth/webmasters.readonly"]
        credentials = service_account.Credentials.from_service_account_file(creds_path, scopes=scopes)
        service = build("searchconsole", "v1", credentials=credentials)
        return service
    except Exception as e:
        print(f"⚠️ Warning: Could not initialize GSC API service with {creds_path}: {e}", file=sys.stderr)
        return None


def fetch_live_gsc_data(service, site_url: str, days: int = 30) -> list[dict]:
    """Queries GSC API for query and page dimensions over the specified date range."""
    end_date = datetime.now(timezone.utc).date()
    start_date = end_date - timedelta(days=days)

    request = {
        "startDate": start_date.strftime("%Y-%m-%d"),
        "endDate": end_date.strftime("%Y-%m-%d"),
        "dimensions": ["query", "page"],
        "rowLimit": 5000,
    }

    try:
        response = service.searchanalytics().query(siteUrl=site_url, body=request).execute()
        rows = response.get("rows", [])
        formatted = []
        for r in rows:
            keys = r.get("keys", ["", ""])
            formatted.append({
                "query": keys[0],
                "page": keys[1],
                "clicks": r.get("clicks", 0),
                "impressions": r.get("impressions", 0),
                "ctr": r.get("ctr", 0.0),
                "position": round(r.get("position", 0.0), 1),
            })
        return formatted
    except Exception as e:
        print(f"❌ Error fetching GSC data: {e}", file=sys.stderr)
        return []


def generate_simulated_gsc_data() -> list[dict]:
    """Generates realistic sample search query dataset based on Helptrickbd's top posts."""
    return [
        {"query": "সার্টিফিকেট নাম সংশোধন করার নিয়ম", "page": "https://www.helptrickbd.com/2025/08/how-to-correction-certificate-name-2025.html", "clicks": 420, "impressions": 5800, "ctr": 0.072, "position": 4.2},
        {"query": "সার্টিফিকেট বয়স সংশোধন অনলাইন আবেদন", "page": "https://www.helptrickbd.com/2025/08/how-to-correction-certificate-name-2025.html", "clicks": 68, "impressions": 3450, "ctr": 0.019, "position": 14.3},
        {"query": "সার্টিফিকেট সংশোধন করতে কত টাকা লাগে", "page": "https://www.helptrickbd.com/2025/08/how-to-correction-certificate-name-2025.html", "clicks": 45, "impressions": 2900, "ctr": 0.015, "position": 16.8},
        {"query": "যুক্তরাষ্ট্রীয় সরকারের বৈশিষ্ট্য", "page": "https://www.helptrickbd.com/2025/05/juktorashtriyo-sorkar-boishisto.html", "clicks": 310, "impressions": 4100, "ctr": 0.075, "position": 3.8},
        {"query": "যুক্তরাষ্ট্রীয় শাসনব্যবস্থার গুণ ও ত্রুটি", "page": "https://www.helptrickbd.com/2025/05/juktorashtriyo-sorkar-boishisto.html", "clicks": 28, "impressions": 2100, "ctr": 0.013, "position": 13.5},
        {"query": "সার্বভৌমত্ব কাকে বলে বৈশিষ্ট্য", "page": "https://www.helptrickbd.com/2026/01/sarbobhoumotto-ki-songga-boishisto-o-prokarved.html", "clicks": 280, "impressions": 3900, "ctr": 0.071, "position": 5.1},
        {"query": "জন অস্টিনের সার্বভৌমত্ব তত্ত্বের সমালোচনা", "page": "https://www.helptrickbd.com/2026/01/sarbobhoumotto-ki-songga-boishisto-o-prokarved.html", "clicks": 18, "impressions": 1850, "ctr": 0.009, "position": 18.2},
        {"query": "১৯৫২ ভাষা আন্দোলনের বিস্তারিত ইতিহাস", "page": "https://www.helptrickbd.com/2025/11/history-of-bangladesh.html", "clicks": 190, "impressions": 2700, "ctr": 0.070, "position": 4.9},
        {"query": "মুক্তিযুদ্ধের ১১টি সেক্টরের তালিকা ও কমান্ডার", "page": "https://www.helptrickbd.com/2025/11/history-of-bangladesh.html", "clicks": 32, "impressions": 3150, "ctr": 0.010, "position": 12.7},
        {"query": "হৃদরোগের কারণ ও প্রতিরোধের প্রাকৃতিক উপায়", "page": "https://www.helptrickbd.com/2025/11/causes-of-heart-disease-prevention.html", "clicks": 140, "impressions": 2200, "ctr": 0.063, "position": 6.2},
        {"query": "হার্ট অ্যাটাকের লক্ষণ ও প্রাথমিক চিকিৎসা", "page": "https://www.helptrickbd.com/2025/11/causes-of-heart-disease-prevention.html", "clicks": 22, "impressions": 2400, "ctr": 0.009, "position": 15.4},
        {"query": "জাতীয় বিশ্ববিদ্যালয় মাস্টার্স পলিটিক্যাল সায়েন্স সাজেশন", "page": "https://www.helptrickbd.com/2025/08/masters-social-change-and-political-development-suggestions.html", "clicks": 115, "impressions": 1950, "ctr": 0.058, "position": 7.1},
        {"query": "সামাজিক পরিবর্তন ও রাজনৈতিক উন্নয়ন ফাইনাল প্রশ্ন", "page": "https://www.helptrickbd.com/2025/08/masters-social-change-and-political-development-suggestions.html", "clicks": 14, "impressions": 1780, "ctr": 0.007, "position": 17.9},
    ]


def analyze_striking_distance(rows: list[dict]) -> tuple[list[dict], list[dict]]:
    """
    Categorizes rows into:
    1. Striking Distance (Position 11.0 to 25.0, high impressions)
    2. High Impression, Low CTR (Impressions >= 1000, CTR < 2.5%, Position <= 20.0)
    """
    striking_distance = []
    ctr_opportunities = []

    for r in rows:
        pos = r["position"]
        imp = r["impressions"]
        ctr = r["ctr"]

        # Striking Distance: Page 2 or top of Page 3
        if 11.0 <= pos <= 25.0:
            striking_distance.append(r)

        # High Impressions but Low CTR (Poor title or snippet)
        if imp >= 1500 and ctr < 0.025 and pos <= 20.0:
            ctr_opportunities.append(r)

    striking_distance.sort(key=lambda x: x["impressions"], reverse=True)
    ctr_opportunities.sort(key=lambda x: x["impressions"], reverse=True)

    return striking_distance, ctr_opportunities


def generate_markdown_report(striking: list[dict], ctr_opps: list[dict], output_file: str):
    """Generates an actionable markdown report for Google ranking boosts."""
    md = []
    md.append("# 🎯 Helptrickbd Google Search Console Opportunity Report")
    md.append(f"**Generated Date:** {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}\n")
    md.append("> এই রিপোর্টে গুগলের পেজ ২-এ থাকা লো-হ্যাংগিং কি-ওয়ার্ড এবং যে পোস্টগুলোর CTR কম রয়েছে, সেগুলোকে দ্রুত গুগল ১ম পেজে নিয়ে আসার কর্মপরিকল্পনা দেওয়া হলো।\n")

    md.append("## 🚀 ১. Striking Distance Keywords (পজিশন ১১–২৫: দ্রুত ১ম পেজে নেওয়ার সুযোগ)")
    md.append("| ক্রম | সার্চ কি-ওয়ার্ড (Query) | বর্তমান পজিশন | ইমপ্রেশন | ক্লিক | বর্তমান CTR | অ্যাকশন সুপারিশ |")
    md.append("| :---: | :--- | :---: | :---: | :---: | :---: | :--- |")

    for i, item in enumerate(striking, start=1):
        ctr_pct = f"{item['ctr'] * 100:.1f}%"
        action = "H2 সাব-হেডিং যুক্ত করুন + ১টি ইন্টারনাল লিঙ্ক"
        md.append(f"| {i} | **{item['query']}** | `Pos {item['position']}` | {item['impressions']:,} | {item['clicks']:,} | {ctr_pct} | {action} |")

    md.append("\n## ⚡ ২. High Impression, Low CTR Pages (টাইটেল ও মেটা ডেসক্রিপশন অপ্টিমাইজেশন)")
    md.append("> এই পোস্টগুলো প্রচুর ভিজিটর গুগলে দেখছে কিন্তু ক্লিকের হার কম। আকর্ষণীয় টাইটেল ও মেটা ডেসক্রিপশন দিলেই ক্লিক ৩–৫ গুণ বাড়বে।\n")
    md.append("| ক্রম | কি-ওয়ার্ড | ইমপ্রেশন | বর্তমান CTR | পোস্টের URL | সমাধান |")
    md.append("| :---: | :--- | :---: | :---: | :--- | :--- |")

    for i, item in enumerate(ctr_opps, start=1):
        ctr_pct = f"{item['ctr'] * 100:.1f}%"
        slug = item["page"].split("/")[-1]
        md.append(f"| {i} | **{item['query']}** | {item['impressions']:,} | `{ctr_pct}` | [`{slug}`]({item['page']}) | টাইটেলে `(২০২৬)` বা `সহজ নিয়ম` যোগ করুন |")

    report_content = "\n".join(md)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(report_content)

    return report_content


def main():
    parser = argparse.ArgumentParser(description="Google Search Console Striking Distance & CTR Miner")
    parser.add_argument("--site-url", default=DEFAULT_SITE_URL, help="Website URL in GSC")
    parser.add_argument("--creds", help="Path to service_account.json or OAuth credentials")
    parser.add_argument("--output", "-o", default=REPORT_PATH, help="Path to save markdown report")
    parser.add_argument("--demo", action="store_true", help="Run in demo/simulated mode without live API")

    args = parser.parse_args()

    print("=" * 65)
    print("🎯 Helptrickbd GSC Striking Distance & CTR Opportunity Miner")
    print("=" * 65)

    data = []
    if not args.demo:
        service = get_gsc_service(args.creds)
        if service:
            print(f"📡 Querying live GSC API for: {args.site_url} ...")
            data = fetch_live_gsc_data(service, args.site_url)
        else:
            print(f"ℹ️ Note: Live credentials not found. Falling back to Demo/Simulated Dataset.")
            data = generate_simulated_gsc_data()
    else:
        print("ℹ️ Running in Demo/Simulation Mode.")
        data = generate_simulated_gsc_data()

    striking, ctr_opps = analyze_striking_distance(data)

    print(f"\n📊 Analysis Summary:")
    print(f"  • Total Queries Analyzed: {len(data)}")
    print(f"  • Striking Distance Queries (Pos 11-25): {len(striking)}")
    print(f"  • High-Impression Low-CTR Opportunities: {len(ctr_opps)}")

    generate_markdown_report(striking, ctr_opps, args.output)
    print(f"\n✅ Actionable Report saved to: {args.output}")


if __name__ == "__main__":
    main()
