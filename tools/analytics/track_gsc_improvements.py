#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/analytics/track_gsc_improvements.py
-----------------------------------------
Helptrickbd Google Search Console Improvement Tracker.
Tracks and compares daily/weekly progress against the baseline of 2026-09-17:
- Organic Clicks, Impressions, CTR, and Average Position
- Indexed vs. Not Indexed pages
- 404 Errors resolution (targeting 111 -> 0)
- Crawled - currently not indexed resolution (targeting 72 -> 0)
- Discovered - currently not indexed resolution (targeting 32 -> 0)
- Mobile Core Web Vitals Need Improvement resolution (targeting 33 -> 0)

Outputs formatted reports in standard Bengali, 100% zero-emoji compliant.
"""

import os
import sys
import json
import argparse
from datetime import datetime

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
BENCHMARKS_DIR = os.path.join(PROJECT_ROOT, "data", "gsc_benchmarks")
BASELINE_FILE = os.path.join(BENCHMARKS_DIR, "gsc_baseline_2026_09_17.json")
LATEST_FILE = os.path.join(BENCHMARKS_DIR, "gsc_latest.json")
HISTORY_FILE = os.path.join(BENCHMARKS_DIR, "gsc_history.json")
DOCS_TRACKER_FILE = os.path.join(PROJECT_ROOT, "docs", "GSC_IMPROVEMENT_TRACKER.md")

os.makedirs(BENCHMARKS_DIR, exist_ok=True)
os.makedirs(os.path.join(PROJECT_ROOT, "docs"), exist_ok=True)

def load_json(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

def save_json(filepath, data):
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def format_diff(curr, base, higher_is_better=True, unit="", is_float=False):
    diff = curr - base
    if is_float:
        diff_str = f"{diff:+.2f}{unit}"
    else:
        diff_str = f"{diff:+d}{unit}"

    if diff == 0:
        status = "অপরিবর্তিত"
    elif (diff > 0 and higher_is_better) or (diff < 0 and not higher_is_better):
        status = "উন্নতি হয়েছে"
    else:
        status = "অবনতি / লক্ষণীয়"
    return diff_str, status

def generate_comparison_report(latest, baseline):
    date_now = latest.get("date", datetime.now().strftime("%Y-%m-%d"))
    date_base = baseline.get("date", "2026-09-17")

    p_curr = latest.get("performance", {})
    p_base = baseline.get("performance", {})
    idx_curr = latest.get("indexing", {})
    idx_base = baseline.get("indexing", {})
    cwv_curr = latest.get("core_web_vitals", {}).get("mobile", {})
    cwv_base = baseline.get("core_web_vitals", {}).get("mobile", {})

    r_curr = idx_curr.get("reasons_not_indexed", {})
    r_base = idx_base.get("reasons_not_indexed", {})

    lines = []
    lines.append("=" * 80)
    lines.append("হেল্পট্রিকবিডি: গুগল সার্চ কনসোল দৈনিক উন্নতি ও অগ্রগতি ট্র্যাকার রিপোর্ট")
    lines.append(f"ভিত্তিপ্রস্তর তারিখ (Baseline): {date_base}  |  বর্তমান পর্যালোচনার তারিখ: {date_now}")
    lines.append("=" * 80)
    lines.append("")

    # 1. Performance Section
    lines.append("১. গুগল সার্চ পারফরম্যান্স মেট্রিক্স (Performance Metrics):")
    lines.append("-" * 80)
    lines.append(f"{'মেট্রিক':<28} | {'বেসলাইন (১৭ সেপ্টে)':<18} | {'বর্তমান মান':<16} | {'পরিবর্তন (Delta)':<14}")
    lines.append("-" * 80)

    # Clicks
    c_diff, c_stat = format_diff(p_curr.get("total_clicks", 0), p_base.get("total_clicks", 0), higher_is_better=True)
    lines.append(f"{'মোট ক্লিক (Total Clicks)':<28} | {p_base.get('total_clicks', 0):<18} | {p_curr.get('total_clicks', 0):<16} | {c_diff} ({c_stat})")

    # Impressions
    i_diff, i_stat = format_diff(p_curr.get("total_impressions", 0), p_base.get("total_impressions", 0), higher_is_better=True)
    lines.append(f"{'মোট ইমপ্রেশন (Impressions)':<28} | {p_base.get('total_impressions', 0):<18} | {p_curr.get('total_impressions', 0):<16} | {i_diff} ({i_stat})")

    # CTR
    ctr_diff, ctr_stat = format_diff(p_curr.get("average_ctr_percent", 0.0), p_base.get("average_ctr_percent", 0.0), higher_is_better=True, unit="%", is_float=True)
    lines.append(f"{'গড় CTR (Click-Through Rate)':<28} | {p_base.get('average_ctr_percent', 0.0):.1f}%{'':<14} | {p_curr.get('average_ctr_percent', 0.0):.1f}%{'':<12} | {ctr_diff} ({ctr_stat})")

    # Position (Lower is better!)
    pos_diff, pos_stat = format_diff(p_curr.get("average_position", 0.0), p_base.get("average_position", 0.0), higher_is_better=False, is_float=True)
    lines.append(f"{'গড় র‍্যাংকিং পজিশন (Position)':<28} | {p_base.get('average_position', 0.0):.1f}{'':<15} | {p_curr.get('average_position', 0.0):.1f}{'':<13} | {pos_diff} ({pos_stat})")
    lines.append("")

    # 2. Indexing Section
    lines.append("২. পেজ ইনডেক্সিং অগ্রগতি (Page Indexing Progress):")
    lines.append("-" * 80)
    lines.append(f"{'সূচক':<28} | {'বেসলাইন (১৭ সেপ্টে)':<18} | {'বর্তমান মান':<16} | {'পরিবর্তন (Delta)':<14}")
    lines.append("-" * 80)

    # Indexed Pages (Higher is better)
    idx_diff, idx_stat = format_diff(idx_curr.get("total_indexed", 0), idx_base.get("total_indexed", 0), higher_is_better=True)
    lines.append(f"{'ইনডেক্সড পেজ (Indexed)':<28} | {idx_base.get('total_indexed', 0):<18} | {idx_curr.get('total_indexed', 0):<16} | {idx_diff} ({idx_stat})")

    # Not Indexed Pages (Lower is better)
    nidx_diff, nidx_stat = format_diff(idx_curr.get("total_not_indexed", 0), idx_base.get("total_not_indexed", 0), higher_is_better=False)
    lines.append(f"{'অন-ইনডেক্সড পেজ (Not Indexed)':<28} | {idx_base.get('total_not_indexed', 0):<18} | {idx_curr.get('total_not_indexed', 0):<16} | {nidx_diff} ({nidx_stat})")
    lines.append("")

    # 3. Critical Fixes Breakdown
    lines.append("৩. প্রধান ফিক্স ও ত্রুটি নিরসন পর্যবেক্ষণ (Critical Error Resolution):")
    lines.append("-" * 80)
    lines.append(f"{'ত্রুটির ধরন (Target: 0)':<36} | {'বেসলাইন':<10} | {'বর্তমান':<10} | {'অবশিষ্ট / পরিবর্তন':<18}")
    lines.append("-" * 80)

    # 404
    err404_diff, err404_stat = format_diff(r_curr.get("not_found_404", 0), r_base.get("not_found_404", 0), higher_is_better=False)
    lines.append(f"{'Not found (404 এরর)':<36} | {r_base.get('not_found_404', 0):<10} | {r_curr.get('not_found_404', 0):<10} | {err404_diff} ({err404_stat})")

    # Crawled not indexed
    cni_diff, cni_stat = format_diff(r_curr.get("crawled_currently_not_indexed", 0), r_base.get("crawled_currently_not_indexed", 0), higher_is_better=False)
    lines.append(f"{'Crawled - currently not indexed':<36} | {r_base.get('crawled_currently_not_indexed', 0):<10} | {r_curr.get('crawled_currently_not_indexed', 0):<10} | {cni_diff} ({cni_stat})")

    # Discovered not indexed
    dni_diff, dni_stat = format_diff(r_curr.get("discovered_currently_not_indexed", 0), r_base.get("discovered_currently_not_indexed", 0), higher_is_better=False)
    lines.append(f"{'Discovered - currently not indexed':<36} | {r_base.get('discovered_currently_not_indexed', 0):<10} | {r_curr.get('discovered_currently_not_indexed', 0):<10} | {dni_diff} ({dni_stat})")

    # Core Web Vitals Need Improvement
    cwv_diff, cwv_stat = format_diff(cwv_curr.get("need_improvement_urls", 0), cwv_base.get("need_improvement_urls", 0), higher_is_better=False)
    lines.append(f"{'Mobile Core Web Vitals Need Imp.':<36} | {cwv_base.get('need_improvement_urls', 0):<10} | {cwv_curr.get('need_improvement_urls', 0):<10} | {cwv_diff} ({cwv_stat})")
    lines.append("=" * 80)

    return "\n".join(lines)

def update_docs_tracker(latest, baseline):
    report_text = generate_comparison_report(latest, baseline)
    md_content = f"""# হেল্পট্রিকবিডি: গুগল সার্চ কনসোল উন্নতি ও অগ্রগতি ট্র্যাকার

এই নথিতে ১৭ সেপ্টেম্বর ২০২৬ তারিখের প্রাথমিক বেঞ্চমার্ক ডাটার সাথে প্রতিদিনের অর্জিত অগ্রগতি এবং পরিবর্তনের ইতিহাস ট্র্যাক করা হয়।

## ১. সর্বশেষ ট্র্যাকিং সারাংশ (Latest Tracking Summary)

```text
{report_text}
```

## ২. লক্ষ্যমাত্রা ও টার্গেট মানদণ্ড (Target Objectives)
1. **Not found (404) এরর:** ১১১ থেকে শূন্যে (০) নামিয়ে আনা।
2. **ইনডেক্সড পেজ সংখ্যা:** ৬১ থেকে ১০০+ পেজে উন্নীত করা।
3. **Crawled - currently not indexed:** ৭২ থেকে শূন্যে নামিয়ে আনা (কনটেন্ট ১,২০০+ শব্দে সমৃদ্ধ করে)।
4. **Discovered - currently not indexed:** ৩২ থেকে শূন্যে নামিয়ে আনা (ইনডেক্সিং এপিআই দিয়ে দ্রুত ক্রলিং সম্পন্ন করা)।
5. **Core Web Vitals Need Improvement:** ৩৩ থেকে শূন্যে নামিয়ে আনা (সব ইউআরএল Good স্টেটে রূপান্তর)।
6. **গড় সার্চ পজিশন:** ৬.১ থেকে টপ ৩-এ নিয়ে আসা এবং CTR ৩.০% থেকে ৫%–৮%-এ বৃদ্ধি করা।

---
*সর্বশেষ আপডেট: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}*
"""
    with open(DOCS_TRACKER_FILE, "w", encoding="utf-8") as f:
        f.write(md_content)

def main():
    parser = argparse.ArgumentParser(description="Helptrickbd GSC Daily Improvement Tracker")
    parser.add_argument("--clicks", type=int, help="Update current total clicks")
    parser.add_argument("--impressions", type=int, help="Update current total impressions")
    parser.add_argument("--ctr", type=float, help="Update current average CTR percentage")
    parser.add_argument("--position", type=float, help="Update current average position")
    parser.add_argument("--indexed", type=int, help="Update current total indexed pages")
    parser.add_argument("--not-indexed", type=int, help="Update current total not indexed pages")
    parser.add_argument("--errors-404", type=int, help="Update current 404 count")
    parser.add_argument("--crawled-not-indexed", type=int, help="Update current crawled-not-indexed count")
    parser.add_argument("--discovered-not-indexed", type=int, help="Update current discovered-not-indexed count")
    parser.add_argument("--cwv-need-improvement", type=int, help="Update Mobile Core Web Vitals Need Improvement count")
    parser.add_argument("--date", type=str, default=datetime.now().strftime("%Y-%m-%d"), help="Snapshot date (YYYY-MM-DD)")
    args = parser.parse_args()

    baseline = load_json(BASELINE_FILE)
    if not baseline:
        print(f"[ত্রুটি] বেসলাইন ফাইল পাওয়া যায়নি: {BASELINE_FILE}")
        sys.exit(1)

    latest = load_json(LATEST_FILE) or json.loads(json.dumps(baseline))

    updated_any = False
    if args.clicks is not None:
        latest["performance"]["total_clicks"] = args.clicks
        updated_any = True
    if args.impressions is not None:
        latest["performance"]["total_impressions"] = args.impressions
        updated_any = True
    if args.ctr is not None:
        latest["performance"]["average_ctr_percent"] = args.ctr
        updated_any = True
    if args.position is not None:
        latest["performance"]["average_position"] = args.position
        updated_any = True
    if args.indexed is not None:
        latest["indexing"]["total_indexed"] = args.indexed
        updated_any = True
    if args.not_indexed is not None:
        latest["indexing"]["total_not_indexed"] = args.not_indexed
        updated_any = True
    if args.errors_404 is not None:
        latest["indexing"]["reasons_not_indexed"]["not_found_404"] = args.errors_404
        updated_any = True
    if args.crawled_not_indexed is not None:
        latest["indexing"]["reasons_not_indexed"]["crawled_currently_not_indexed"] = args.crawled_not_indexed
        updated_any = True
    if args.discovered_not_indexed is not None:
        latest["indexing"]["reasons_not_indexed"]["discovered_currently_not_indexed"] = args.discovered_not_indexed
        updated_any = True
    if args.cwv_need_improvement is not None:
        latest["core_web_vitals"]["mobile"]["need_improvement_urls"] = args.cwv_need_improvement
        updated_any = True

    if updated_any:
        latest["date"] = args.date
        save_json(LATEST_FILE, latest)
        print(f"[সফল] নতুন স্ন্যাপশট সংরক্ষণ করা হয়েছে: {LATEST_FILE}")

        # Append to history log
        history = load_json(HISTORY_FILE) or []
        history.append({
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "snapshot": latest
        })
        save_json(HISTORY_FILE, history)

    # Generate and print the report
    report = generate_comparison_report(latest, baseline)
    print(report)

    # Update docs tracker
    update_docs_tracker(latest, baseline)
    print(f"\n[নথি সংরক্ষণ] বিস্তারিত ট্র্যাকিং রিপোর্ট সংরক্ষিত হয়েছে: {DOCS_TRACKER_FILE}")

if __name__ == "__main__":
    main()
