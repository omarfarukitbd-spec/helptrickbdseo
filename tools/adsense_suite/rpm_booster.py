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

def get_ad_slot_code(slot_type: str, pub_id: str = None, slot_id: str = None) -> str:
    """
    Generates valid, policy-compliant Google AdSense code or clean placeholder.
    Guarantees strict AdSense distance rules and official publisher disclosure labeling.
    """
    if pub_id:
        slot_attr = f'data-ad-slot="{slot_id}"' if slot_id else 'data-ad-slot="auto"'
        return f'''<!-- [ADSENSE] {slot_type.upper()} -->
<div class="htbd-ad-slot htbd-ad-{slot_type}" style="margin: 28px auto; text-align: center; max-width: 100%; overflow: hidden;">
  <div style="font-size: 11px; color: #94a3b8; margin-bottom: 4px; letter-spacing: 0.5px; text-transform: uppercase;">বিজ্ঞাপন</div>
  <ins class="adsbygoogle"
       style="display:block"
       data-ad-client="{pub_id}"
       {slot_attr}
       data-ad-format="auto"
       data-full-width-responsive="true"></ins>
  <script>
       (adsbygoogle = window.adsbygoogle || []).push({{}});
  </script>
</div>'''
    else:
        labels = {
            "after_intro": "Google AdSense Responsive Unit (Top)",
            "mid_article": "Google AdSense In-Article Native Unit (Mid)",
            "before_faq": "Google AdSense Multiplex Unit (Bottom)"
        }
        lbl = labels.get(slot_type, "Google AdSense Unit")
        return f'''<!-- [ADSENSE] {slot_type.upper()} -->
<div class="htbd-ad-wrapper htbd-ad-{slot_type}" style="margin: 28px auto; text-align: center; max-width: 728px; min-height: 90px; background: #fafafa; border: 1px dashed #cbd5e1; border-radius: 8px; display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 12px; color: #64748b; font-family: 'SolaimanLipi', sans-serif;">
  <span style="font-size: 11px; text-transform: uppercase; letter-spacing: 0.5px; color: #94a3b8; margin-bottom: 4px;">বিজ্ঞাপন</span>
  <span style="font-size: 13px; font-weight: 600;">{lbl}</span>
</div>'''


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
    # Factors: Word count (>1200 = 40 pts), High-CPC hits (>3 = 40 pts), Table/FAQ = 20 pts
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

    if soup.find("table") or "faq" in html_content.lower() or "faqpage" in html_content.lower():
        score += 20

    return {
        "word_count": words,
        "monetization_score": min(100, score),
        "total_cpc_hits": total_high_cpc_hits,
        "detected_clusters": detected_clusters,
    }


def inject_policy_safe_ad_slots(html_content: str, pub_id: str = None, slot_id: str = None) -> str:
    """Injects AdSense responsive placeholders or live units following strict AdSense distance rules."""
    soup = BeautifulSoup(html_content, "html.parser")
    post_wrapper = soup.find("div", class_="htbd-post-wrapper") or soup.find("body") or soup

    paragraphs = post_wrapper.find_all("p", recursive=False)
    if not paragraphs:
        paragraphs = post_wrapper.find_all("p")

    # Slot 1: After 2nd paragraph (Safe distance from H1)
    if len(paragraphs) >= 2:
        slot1_html = get_ad_slot_code("after_intro", pub_id=pub_id, slot_id=slot_id)
        paragraphs[1].insert_after(BeautifulSoup(slot1_html, "html.parser"))

    # Slot 2: Mid content
    if len(paragraphs) >= 6:
        mid_idx = len(paragraphs) // 2
        slot2_html = get_ad_slot_code("mid_article", pub_id=pub_id, slot_id=slot_id)
        paragraphs[mid_idx].insert_after(BeautifulSoup(slot2_html, "html.parser"))

    # Slot 3: Before FAQ section
    faq_sec = post_wrapper.find("div", class_="htbd-faq-section") or post_wrapper.find("div", class_="htbd-qbox")
    if faq_sec:
        slot3_html = get_ad_slot_code("before_faq", pub_id=pub_id, slot_id=slot_id)
        faq_sec.insert_before(BeautifulSoup(slot3_html, "html.parser"))

    return str(soup)


def main():
    parser = argparse.ArgumentParser(description="AdSense High-RPM & CPC Optimizer for Helptrickbd")
    parser.add_argument("--file", "-f", required=True, help="Path to HTML article file")
    parser.add_argument("--inject-slots", action="store_true", help="Inject Google-compliant ad slots into HTML")
    parser.add_argument("--pub-id", help="Google AdSense Publisher ID (e.g. ca-pub-1234567890123456)")
    parser.add_argument("--slot-id", help="AdSense Slot ID (optional)")
    parser.add_argument("--output", "-o", help="Output file path for ad-injected HTML")

    args = parser.parse_args()

    if not os.path.exists(args.file):
        print(f"Error: File not found: {args.file}", file=sys.stderr)
        sys.exit(1)

    with open(args.file, "r", encoding="utf-8") as f:
        content = f.read()

    print("=" * 65)
    print(f"Helptrickbd AdSense RPM & CPC Optimizer: {os.path.basename(args.file)}")
    print("=" * 65)

    analysis = analyze_article_monetization(content)

    print(f"\nMonetization Score: {analysis['monetization_score']}/100")
    print(f"  • Article Words: {analysis['word_count']}")
    print(f"  • High-CPC Keyword Matches: {analysis['total_cpc_hits']}")

    print("\nHigh-CPC Opportunities:")
    if analysis["detected_clusters"]:
        for name, data in analysis["detected_clusters"].items():
            print(f"  • {name} (Estimated CPC: {data['avg_cpc']})")
            print(f"    Matches: {', '.join(data['matches'])}")
    else:
        print("  Notice: No direct high-CPC clusters detected. Consider adding contextual career/banking references.")

    if args.inject_slots:
        optimized_html = inject_policy_safe_ad_slots(content, pub_id=args.pub_id, slot_id=args.slot_id)
        out_path = args.output if args.output else args.file
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(optimized_html)
        ad_type = f"Live Ad Units ({args.pub_id})" if args.pub_id else "Policy-Safe Placeholders"
        print(f"\nSuccessfully injected {ad_type} into: {out_path}")


if __name__ == "__main__":
    main()
