#!/usr/bin/env python3
"""
tools/silo_architect/cluster_visualizer.py
Topical Authority & Silo Cluster Architect for Helptrickbd.
Analyzes category distributions, evaluates pillar-cluster silo completeness,
and maps the exact missing articles needed to achieve 100% Topical Authority for Google.
"""

import os
import sys
import json
import argparse
from datetime import datetime, timezone
from collections import defaultdict

try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
CATALOG_PATH = os.path.join(PROJECT_ROOT, "all_live_posts_catalog.json")
REPORT_PATH = os.path.join(PROJECT_ROOT, "silo_cluster_blueprint.md")

# Ideal Topical Authority Silo Benchmarks
REQUIRED_CLUSTER_DEPTH = 6  # Minimum 6 supporting articles per pillar


def categorize_post_into_silo(post: dict) -> str:
    """Classifies a post into a primary content silo based on categories, title, and slug."""
    title = post.get("title", "").lower()
    categories = [c.lower() for c in post.get("categories", [])]
    url = post.get("url", "").lower()
    combined = f"{title} {' '.join(categories)} {url}"

    if any(k in combined for k in ("পৌরনীতি", "রাষ্ট্রবিজ্ঞান", "সার্বভৌমত্ব", "যুক্তরাষ্ট্র", "সরকার", "রাজনৈতিক", "political", "patriarchy", "পিতৃতন্ত্র")):
        return "রাষ্ট্রবিজ্ঞান ও শাসনব্যবস্থা (Political Science)"
    elif any(k in combined for k in ("ইতিহাস", "মুক্তিযুদ্ধ", "১৯৫২", "১৯৭১", "bangladesh", "হৃদরোগ", "সমাজকর্ম", "বিদ্যাসাগর", "হৃদরোগ")):
        return "ইতিহাস, সমাজ ও স্বাস্থ্য (History & Society)"
    elif any(k in combined for k in ("সার্টিফিকেট", "এসএসসি", "এইচএসসি", "বোর্ড", "রুটিন", "ssc", "hsc", "নামতা", "হ্যান্ডনোট")):
        return "শিক্ষা ও বোর্ড শিক্ষার্থী সহায়িকা (Academic & Board Guides)"
    elif any(k in combined for k in ("কম্পিউটার", "computer", "প্রযুক্তি", "ict", "সফটওয়্যার", "মোবাইল")):
        return "আইসিটি ও কম্পিউটার শিক্ষা (ICT & Technology)"
    elif any(k in combined for k in ("আল্লাহ", "মিলাদ", "দরূদ", "ক্বাসিদা", "lyrics", "ইসলাম", "রাসূল")):
        return "ইসলামিক সাহিত্য ও নাশিদ (Islamic Literature)"
    elif any(k in combined for k in ("চাকরি", "বিসিএস", "job", "bcs", "প্রস্তুতি", "ব্যাংক", "নিয়োগ")):
        return "চাকরি ও ক্যারিয়ার প্রস্তুতি (Job & Career)"
    else:
        return "সাধারণ জ্ঞান ও অন্যান্য (General Studies)"


def build_silo_clusters(posts: list[dict]) -> dict:
    """Groups posts into silos and calculates health metrics."""
    silos = defaultdict(list)
    for p in posts:
        silo_name = categorize_post_into_silo(p)
        silos[silo_name].append(p)

    analysis = {}
    for name, cluster_posts in silos.items():
        count = len(cluster_posts)
        # Select Pillar Post: Longest title or primary foundational topic
        pillar = cluster_posts[0] if cluster_posts else {}
        for cp in cluster_posts:
            # Prefer comprehensive terms
            if any(term in cp.get("title", "").lower() for term in ("সংজ্ঞা", "ইতিহাস", "বৈশিষ্ট্য", "নিয়ম", "২০২৬")):
                pillar = cp
                break

        # Health score (0-100%)
        health = min(100, int((count / REQUIRED_CLUSTER_DEPTH) * 100))

        # Determine missing cluster topics needed
        missing = []
        if count < REQUIRED_CLUSTER_DEPTH:
            needed_count = REQUIRED_CLUSTER_DEPTH - count
            if "Political" in name:
                missing = [
                    "প্লেটোর আদর্শ রাষ্ট্র ও দার্শনিক রাজা তত্ত্ব (হ্যান্ডনোট)",
                    "অ্যারিস্টটলের নাগরিকত্ব ও বিপ্লব তত্ত্ব (মডেল প্রশ্ন)",
                    "গণতন্ত্র বনাম একনায়কতন্ত্র: তুলনামূলক সারণী ও বৈশিষ্ট্য"
                ][:needed_count]
            elif "ICT" in name:
                missing = [
                    "কম্পিউটার ভাইরাস ও সাইবার নিরাপত্তা থেকে বাঁচার সেরা উপায়",
                    "ক্লাউড কম্পিউটিং কি? প্রকারভেদ ও বাস্তব সুবিধা",
                    "ইন্টারনেট প্রটোকল (IP Address) ও ডোমেইন নেম সিস্টেম (DNS) ব্যাখ্যা"
                ][:needed_count]
            elif "Board" in name or "Academic" in name:
                missing = [
                    "বোর্ড পরীক্ষার খাতা মূল্যায়নের গোপন ট্রিকস ও নিয়ম",
                    "জেএসসি ও এসএসসি গ্রেডিং পয়েন্ট (GPA) হিসাব করার সঠিক পদ্ধতি",
                    "ইংরেজি ১ম ও ২য় পত্র দ্রুত রিভিশনের স্মার্ট হ্যান্ডনোট"
                ][:needed_count]
            elif "Job" in name:
                missing = [
                    "বিসিএস প্রিলিমিনারি ২০০ নম্বরের বিষয়ভিত্তিক মানবণ্টন ও বুক লিস্ট",
                    "সরকারি প্রাথমিক শিক্ষক নিয়োগ ভাইভায় সাধারণ ভুল ও প্রতিকার",
                    "ব্যাংক জব ও গণিত শর্টকাট টেকনিক (বাংলা ও ইংরেজি সমাধান)"
                ][:needed_count]
            else:
                missing = [f"{name} সম্পর্কিত অতিরিক্ত স্পেশাল মডেল গাইড ১", f"{name} সম্পর্কিত বিস্তারিত হ্যান্ডনোট ২"][:needed_count]

        analysis[name] = {
            "post_count": count,
            "pillar_post": pillar.get("title", "N/A"),
            "pillar_url": pillar.get("url", ""),
            "cluster_health": health,
            "missing_topics": missing,
            "posts": cluster_posts,
        }
    return analysis


def generate_silo_blueprint_markdown(analysis: dict, total_posts: int, output_file: str):
    """Generates the Silo Cluster Blueprint markdown document."""
    md = []
    md.append("# 🏛️ Helptrickbd Topical Authority & Silo Cluster Blueprint")
    md.append(f"**Generated Date:** {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}")
    md.append(f"**Total Live Articles Analyzed:** {total_posts} | **Total Silo Clusters:** {len(analysis)}\n")

    md.append("> গুগলের Helpful Content System ও Topical Authority অ্যালগরিদমে শীর্ষ র‍্যাংক পাওয়ার জন্য নিচে প্রতিটি কন্টেন্ট সাইলোর আর্কিটেকচার তুলে ধরা হলো।\n")

    md.append("## 📊 ১. সাইলো ক্লাস্টার সামারি ও হেলথ স্কোর")
    md.append("| ক্রম | কনটেন্ট সাইলো (Topic Silo) | বর্তমান পোস্ট | পিলারের স্থিতি | সাইলো হেলথ | স্ট্যাটাস |")
    md.append("| :---: | :--- | :---: | :--- | :---: | :---: |")

    for idx, (name, d) in enumerate(analysis.items(), start=1):
        score = d["cluster_health"]
        badge = "🟢 Strong" if score >= 100 else ("🟡 Good" if score >= 60 else "🔴 Needs Posts")
        pillar_display = f"[`{d['pillar_post'][:25]}...`]({d['pillar_url']})" if d['pillar_url'] else d['pillar_post']
        md.append(f"| {idx} | **{name}** | **{d['post_count']} টি** | {pillar_display} | `{score}%` | {badge} |")

    md.append("\n## 🗺️ ২. টপিকাল অথরিটি সম্পন্ন করার জন্য প্রয়োজনীয় নতুন পোস্টসমূহ (Action Blueprint):")
    for name, d in analysis.items():
        if d["missing_topics"]:
            md.append(f"\n### 📌 {name}")
            md.append(f"- **বর্তমান স্বাস্থ্য:** `{d['cluster_health']}%` ({d['post_count']}/{REQUIRED_CLUSTER_DEPTH} পোস্ট)")
            md.append("- **এই ক্লাস্টারকে গুগলে ১০০% ডমিনেট করতে যেসব নতুন পোস্ট প্রয়োজন:**")
            for t in d["missing_topics"]:
                md.append(f"  * ✍️ **{t}**")

    # Mermaid Visual Architecture Diagram
    md.append("\n## 📐 ৩. সাইলো ক্লাস্টার ভিজ্যুয়াল আর্কিটেকচার ডায়াগ্রাম:")
    md.append("```mermaid")
    md.append("graph TD")
    md.append("    Home[Helptrickbd.com Hub] --> Silo1[রাষ্ট্রবিজ্ঞান ও শাসনব্যবস্থা]")
    md.append("    Home --> Silo2[ইতিহাস, সমাজ ও স্বাস্থ্য]")
    md.append("    Home --> Silo3[শিক্ষা ও বোর্ড সহায়িকা]")
    md.append("    Home --> Silo4[আইসিটি ও প্রযুক্তি]")
    md.append("    Home --> Silo5[ইসলামিক সাহিত্য]")
    md.append("    Home --> Silo6[চাকরি ও ক্যারিয়ার]")
    md.append("```")

    report_content = "\n".join(md)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(report_content)
    return report_content


def main():
    parser = argparse.ArgumentParser(description="Topical Authority & Silo Cluster Architect for Helptrickbd")
    parser.add_argument("--output", "-o", default=REPORT_PATH, help="Path to save blueprint report")

    args = parser.parse_args()

    print("=" * 65)
    print("🏛️ Helptrickbd Topical Authority & Silo Cluster Architect")
    print("=" * 65)

    if not os.path.exists(CATALOG_PATH):
        print(f"❌ Error: Catalog file not found at {CATALOG_PATH}", file=sys.stderr)
        sys.exit(1)

    with open(CATALOG_PATH, "r", encoding="utf-8") as f:
        catalog = json.load(f)

    posts = catalog if isinstance(catalog, list) else catalog.get("posts", [])
    print(f"📡 Loaded {len(posts)} published posts from catalog...")

    analysis = build_silo_clusters(posts)

    print("\n📊 Silo Cluster Analysis:")
    for name, d in analysis.items():
        print(f"  • {name:40} : {d['post_count']:2d} posts | Health: {d['cluster_health']:3d}%")

    generate_silo_blueprint_markdown(analysis, len(posts), args.output)
    print(f"\n💾 Silo Cluster Blueprint saved to: {args.output}")


if __name__ == "__main__":
    main()
