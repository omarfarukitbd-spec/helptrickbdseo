#!/usr/bin/env python3
"""
tools/cannibalization_detector/cannibalization_finder.py
Keyword Cannibalization Detective for Helptrickbd.
Identifies internal self-competing posts that divide Google ranking authority
and provides clear remediation (Canonicalize, 301 Redirect/Merge, or H2 Retargeting).
"""

import os
import sys
import json
import argparse
import re
from itertools import combinations
from datetime import datetime, timezone

try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
CATALOG_PATH = os.path.join(PROJECT_ROOT, "all_live_posts_catalog.json")
REPORT_PATH = os.path.join(PROJECT_ROOT, "cannibalization_audit_report.md")

# Stopwords to exclude from similarity calculation (Bengali & English)
STOPWORDS = {
    "ও", "এবং", "বা", "কি", "কী", "কাকে", "বলে", "এর", "তে", "এ", "থেকে", "দিয়ে",
    "জন্য", "নিয়ে", "সম্পর্কে", "বিস্তারিত", "নিয়ম", "পদ্ধতি", "সহজ", "২০২৪", "২০২৫", "২০২৬",
    "the", "a", "an", "and", "or", "in", "on", "at", "to", "for", "of", "with", "is", "what", "how"
}


def clean_and_tokenize(text: str) -> set[str]:
    """Cleans punctuation and returns set of meaningful keyword tokens."""
    tokens = re.findall(r"[\w]+", text.lower())
    return {t for t in tokens if t not in STOPWORDS and len(t) > 1}


def jaccard_similarity(set1: set, set2: set) -> float:
    """Calculates Jaccard overlap between two token sets."""
    if not set1 or not set2:
        return 0.0
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    return intersection / union if union > 0 else 0.0


def extract_slug_from_url(url: str) -> str:
    parts = url.strip().rstrip("/").split("/")
    return parts[-1].replace(".html", "") if parts else url


def find_cannibalization(catalog_posts: list[dict], threshold: float = 0.35) -> list[dict]:
    """Compares all post pairs and flags significant keyword overlap."""
    processed = []
    for p in catalog_posts:
        title = p.get("title", "")
        url = p.get("url", "")
        slug = extract_slug_from_url(url)
        slug_clean = slug.replace("-", " ")
        combined_text = f"{title} {slug_clean}"
        tokens = clean_and_tokenize(combined_text)

        processed.append({
            "title": title,
            "url": url,
            "slug": slug,
            "tokens": tokens,
            "categories": p.get("categories", []),
        })

    conflicts = []
    for p1, p2 in combinations(processed, 2):
        score = jaccard_similarity(p1["tokens"], p2["tokens"])
        overlap_tokens = p1["tokens"].intersection(p2["tokens"])

        if score >= threshold and len(overlap_tokens) >= 2:
            severity = "High" if score >= 0.55 else "Medium"
            conflicts.append({
                "post1": p1,
                "post2": p2,
                "similarity": round(score * 100, 1),
                "severity": severity,
                "shared_keywords": sorted(list(overlap_tokens)),
            })

    conflicts.sort(key=lambda x: x["similarity"], reverse=True)
    return conflicts


def generate_cannibalization_report(conflicts: list[dict], total_posts: int, output_file: str):
    """Writes actionable markdown audit report."""
    md = []
    md.append("# 🕵️ Helptrickbd Keyword Cannibalization Audit Report")
    md.append(f"**Generated Date:** {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}")
    md.append(f"**Total Posts Audited:** {total_posts} | **Competing Pairs Identified:** {len(conflicts)}\n")

    if not conflicts:
        md.append("### ✅ No Critical Keyword Cannibalization Detected!")
        md.append("সাইটের প্রতিটি পোস্ট স্বতন্ত্র ও নিজস্ব কি-ওয়ার্ডে ফোকাস করা রয়েছে। গুগল সহজেই প্রত্যেকটি পেজকে আলাদাভাবে মূল্যায়ন করতে পারছে।\n")
    else:
        md.append("### 🚨 অ্যাকশন প্রয়োজন: পরস্পর প্রতিযোগী পোস্টের তালিকা\n")
        md.append("> নিচের পোস্টগুলো গুগলে একই কি-ওয়ার্ডে একে অপরের সাথে প্রতিযোগিতা করছে। এর ফলে কোনোটিই গুগলের শীর্ষ ৩-এ উঠতে পারছে না।\n")
        md.append("| ক্রম | তীব্রতা | মিলের হার | সাধারণ কি-ওয়ার্ড | পোস্ট ১ ও পোস্ট ২ | প্রস্তাবিত সমাধান |")
        md.append("| :---: | :---: | :---: | :--- | :--- | :--- |")

        for idx, c in enumerate(conflicts, start=1):
            p1_slug = c["post1"]["slug"]
            p2_slug = c["post2"]["slug"]
            kw_str = ", ".join(c["shared_keywords"][:4])
            badge = "🔴 High" if c["severity"] == "High" else "🟡 Medium"

            if c["severity"] == "High":
                action = "একটি প্রধান আর্টিকেলে মার্জ করে অন্যটিকে 301 Redirect দিন অথবা Rel=Canonical সেট করুন"
            else:
                action = "পোস্ট ২-এর H2 সাব-হেডিং পরিবর্তন করে সেকেন্ডারি বিষয়ে রি-টার্গেট করুন"

            links = f"1. [`{p1_slug[:30]}...`]({c['post1']['url']})<br>2. [`{p2_slug[:30]}...`]({c['post2']['url']})"
            md.append(f"| {idx} | {badge} | **{c['similarity']}%** | `{kw_str}` | {links} | {action} |")

    report_content = "\n".join(md)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(report_content)
    return report_content


def main():
    parser = argparse.ArgumentParser(description="Keyword Cannibalization Detective for Helptrickbd")
    parser.add_argument("--threshold", type=float, default=0.35, help="Similarity threshold (default: 0.35)")
    parser.add_argument("--output", "-o", default=REPORT_PATH, help="Path to save audit report")

    args = parser.parse_args()

    print("=" * 65)
    print("🕵️ Helptrickbd Keyword Cannibalization Detective")
    print("=" * 65)

    if not os.path.exists(CATALOG_PATH):
        print(f"❌ Error: Catalog file not found at {CATALOG_PATH}", file=sys.stderr)
        sys.exit(1)

    with open(CATALOG_PATH, "r", encoding="utf-8") as f:
        catalog = json.load(f)

    posts = catalog if isinstance(catalog, list) else catalog.get("posts", [])
    print(f"📡 Loaded {len(posts)} published posts from catalog...")

    conflicts = find_cannibalization(posts, threshold=args.threshold)

    high_count = sum(1 for c in conflicts if c["severity"] == "High")
    med_count = sum(1 for c in conflicts if c["severity"] == "Medium")

    print(f"\n📊 Cannibalization Analysis:")
    print(f"  • Total Conflicts Found: {len(conflicts)}")
    print(f"  • 🔴 High Risk Pairs: {high_count}")
    print(f"  • 🟡 Medium Risk Pairs: {med_count}")

    generate_cannibalization_report(conflicts, len(posts), args.output)
    print(f"\n💾 Actionable Report saved to: {args.output}")


if __name__ == "__main__":
    main()
