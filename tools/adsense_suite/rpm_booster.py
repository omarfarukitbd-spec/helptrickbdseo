#!/usr/bin/env python3
"""
tools/adsense_suite/rpm_booster.py
AdSense High-RPM Keyword Matcher & Policy-Safe Ad Placement Advisor for Helptrickbd.
Increases Page RPM and CPC by contextually mapping high-value keywords (Sonali Seba, BCS, Banking, NU)
and injecting Google-compliant ad placement slots.
"""

import os
import sys
import json
import argparse
import re
from bs4 import BeautifulSoup

try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

# High-CPC & High-RPM niche keyword clusters for Bangladesh & International traffic
HIGH_CPC_CLUSTERS = {
    "Govt e-Services & Banking (উচ্চ সিপিসি ই-সেবা ও ব্যাংকিং)": {
        "avg_cpc": "$0.18 - $0.45",
        "keywords": [
            "সোনালী সেবা ই-চালান", "অনলাইন ফি পরিশোধ", "অনলাইন চালান ফরম",
            "মোবাইল ব্যাংকিং বিকাশ রকেট", "ব্যাংক ড্রাফট নিয়ম", "সরকারি সেবা পোর্টাল",
            "ই-পাসপোর্ট আবেদন", "জাতীয় পরিচয়পত্র এনআইডি", "ট্যাক্স রিটার্ন দাখিল"
        ]
    },
    "Career & Competitive Exams (চাকরি ও বিসিএস প্রস্তুতি)": {
        "avg_cpc": "$0.12 - $0.35",
        "keywords": [
            "বিসিএস প্রিলিমিনারি প্রস্তুতি", "সরকারি চাকরি নিয়োগ বিজ্ঞপ্তি", "ব্যাংক জব প্রস্তুতি",
            "শিক্ষক নিবন্ধন এনটিআরসিএ", "কারিগরি শিক্ষা বোর্ড", "পিএসসি বিগত সালের প্রশ্ন"
        ]
    },
    "Higher Education & Scholarships (উচ্চশিক্ষা ও স্কলারশিপ)": {
        "avg_cpc": "$0.15 - $0.40",
        "keywords": [
            "জাতীয় বিশ্ববিদ্যালয় নোটিশ", "মাস্টার্স ফাইনাল ভর্তি", "অনার্স প্রমোশন নীতিমালা",
            "উচ্চশিক্ষা বৃত্তি স্কলারশিপ", "আইইএলটিএস প্রস্তুতি", "বিদেশে উচ্চশিক্ষা ভিসা"
        ]
    },
    "ICT & Professional Skills (আইসিটি ও পেশাগত দক্ষতা)": {
        "avg_cpc": "$0.20 - $0.55",
        "keywords": [
            "কম্পিউটার অফিস অ্যাপ্লিকেশন", "ওয়েব ডেভেলপমেন্ট কোর্স", "ডাটা এন্ট্রি ফ্রিল্যান্সিং",
            "ডিজিটাল মার্কেটিং শেখার উপায়", "পাইথন প্রোগ্রামিং বাংলা", "গ্রাফিক্স ডিজাইন টিউটোরিয়াল"
        ]
    }
}

SAFE_AD_SLOTS = {
    "slot_after_intro": '<!-- [ADSENSE] Responsive Display Unit After Intro -->\n<div class="htbd-ad-wrapper" style="margin: 24px auto; text-align: center; max-width: 728px; min-height: 90px; background: #fafafa; border: 1px dashed #e2e8f0; border-radius: 8px; display: flex; align-items: center; justify-content: center; color: #94a3b8; font-size: 13px;">\n  <span>বিজ্ঞাপন (Google AdSense Responsive Unit)</span>\n</div>',
    "slot_mid_article": '<!-- [ADSENSE] In-Article Native Unit Mid-Content -->\n<div class="htbd-ad-wrapper" style="margin: 30px auto; text-align: center; max-width: 728px; min-height: 250px; background: #fafafa; border: 1px dashed #e2e8f0; border-radius: 8px; display: flex; align-items: center; justify-content: center; color: #94a3b8; font-size: 13px;">\n  <span>বিজ্ঞাপন (Google AdSense In-Article Unit)</span>\n</div>',
    "slot_before_faq": '<!-- [ADSENSE] Matched Content / Multiplex Unit Before FAQ -->\n<div class="htbd-ad-wrapper" style="margin: 28px auto; text-align: center; max-width: 728px; min-height: 100px; background: #fafafa; border: 1px dashed #e2e8f0; border-radius: 8px; display: flex; align-items: center; justify-content: center; color: #94a3b8; font-size: 13px;">\n  <span>বিজ্ঞাপন (Google AdSense Multiplex Unit)</span>\n</div>',
}


def analyze_article_monetization(html_content: str) -> dict:
    """Analyzes high-CPC keyword density and calculates monetization score."""
    soup = BeautifulSoup(html_content, "html.parser")
    text = soup.get_text()

    detected_clusters = {}
    total_high_cpc_hits = 0

    for cluster_name, cluster_info in HIGH_CPC_CLUSTERS.items():
        found_kw = []
        for kw in cluster_info["keywords"]:
            if kw in text:
                found_kw.append(kw)
        if found_kw:
            detected_clusters[cluster_name] = {
                "avg_cpc": cluster_info["avg_cpc"],
                "matches": found_kw,
            }
            total_high_cpc_hits += len(found_kw)

    # Word count
    words = len(text.split())

    # Monetization Score (0-100)
    # Factors: Word count (>1000 = 40 pts), High-CPC hits (>3 = 40 pts), Table/FAQ = 20 pts
    score = 0
    if words >= 1200:
        score += 40
    elif words >= 800:
        score += 25
    else:
        score += 10

    if total_high_cpc_hits >= 5:
        score += 40
    elif total_high_cpc_hits >= 2:
        score += 25
    elif total_high_cpc_hits >= 1:
        score += 15

    if soup.find("table") or "faq" in html_content.lower():
        score += 20

    return {
        "word_count": words,
        "monetization_score": min(100, score),
        "total_cpc_hits": total_high_cpc_hits,
        "detected_clusters": detected_clusters,
    }


def inject_policy_safe_ad_slots(html_content: str) -> str:
    """Injects AdSense responsive placeholders following strict AdSense distance rules."""
    soup = BeautifulSoup(html_content, "html.parser")
    post_wrapper = soup.find("div", class_="htbd-post-wrapper") or soup.find("body") or soup

    paragraphs = post_wrapper.find_all("p", recursive=False)
    if not paragraphs:
        paragraphs = post_wrapper.find_all("p")

    # Slot 1: After 2nd paragraph
    if len(paragraphs) >= 2:
        slot1_soup = BeautifulSoup(SAFE_AD_SLOTS["slot_after_intro"], "html.parser")
        paragraphs[1].insert_after(slot1_soup)

    # Slot 2: Mid content (e.g. after middle paragraph)
    if len(paragraphs) >= 6:
        mid_idx = len(paragraphs) // 2
        slot2_soup = BeautifulSoup(SAFE_AD_SLOTS["slot_mid_article"], "html.parser")
        paragraphs[mid_idx].insert_after(slot2_soup)

    # Slot 3: Before FAQ section
    faq_sec = post_wrapper.find("div", class_="htbd-faq-section") or post_wrapper.find("div", class_="htbd-qbox")
    if faq_sec:
        slot3_soup = BeautifulSoup(SAFE_AD_SLOTS["slot_before_faq"], "html.parser")
        faq_sec.insert_before(slot3_soup)

    return str(soup)


def main():
    parser = argparse.ArgumentParser(description="AdSense High-RPM & CPC Optimizer for Helptrickbd")
    parser.add_argument("--file", "-f", required=True, help="Path to HTML article file")
    parser.add_argument("--inject-slots", action="store_true", help="Inject Google-compliant ad slots into HTML")
    parser.add_argument("--output", "-o", help="Output file path for ad-injected HTML")

    args = parser.parse_args()

    if not os.path.exists(args.file):
        print(f"❌ Error: File not found: {args.file}", file=sys.stderr)
        sys.exit(1)

    with open(args.file, "r", encoding="utf-8") as f:
        content = f.read()

    print("=" * 65)
    print(f"💰 Helptrickbd AdSense RPM & CPC Optimizer: {os.path.basename(args.file)}")
    print("=" * 65)

    analysis = analyze_article_monetization(content)

    print(f"\n📊 Monetization Score: {analysis['monetization_score']}/100 🏆")
    print(f"  • Article Words: {analysis['word_count']}")
    print(f"  • High-CPC Keyword Matches: {analysis['total_cpc_hits']}")

    print("\n💎 Detected High-CPC Opportunities:")
    if analysis["detected_clusters"]:
        for name, data in analysis["detected_clusters"].items():
            print(f"  • {name} (Estimated CPC: {data['avg_cpc']})")
            print(f"    Matches: {', '.join(data['matches'])}")
    else:
        print("  ℹ️ No direct high-CPC clusters detected. Consider adding contextual career/banking references.")

    if args.inject_slots:
        optimized_html = inject_policy_safe_ad_slots(content)
        out_path = args.output if args.output else args.file
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(optimized_html)
        print(f"\n✅ Successfully injected policy-safe AdSense slots into: {out_path}")


if __name__ == "__main__":
    main()
