#!/usr/bin/env python3
"""
tools/serp_analyzer/content_gap_analyzer.py
Competitor SERP Content Gap Analyzer for Helptrickbd.
Analyzes top-ranking search results to extract heading hierarchies, word counts,
and topic coverage, revealing exactly what competitors missed to build the definitive 10x post.
"""

import os
import sys
import json
import argparse
import re
from urllib.parse import quote_plus
import requests
from bs4 import BeautifulSoup

try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}


def clean_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def analyze_webpage_content(url: str) -> dict:
    """Fetches and analyzes heading structure, word count, and data elements of a URL."""
    res = {
        "url": url,
        "title": "",
        "word_count": 0,
        "h2_headings": [],
        "h3_headings": [],
        "has_tables": False,
        "has_faq": False,
        "error": None,
    }

    try:
        resp = requests.get(url, headers=HEADERS, timeout=10)
        if resp.status_code != 200:
            res["error"] = f"Status {resp.status_code}"
            return res

        soup = BeautifulSoup(resp.text, "html.parser")
        # Remove scripts, styles, navigation, footer
        for tag in soup(["script", "style", "nav", "footer", "aside", "header"]):
            tag.decompose()

        title_tag = soup.find("title")
        if title_tag:
            res["title"] = clean_text(title_tag.get_text())

        # Extract Headings
        for h2 in soup.find_all("h2"):
            txt = clean_text(h2.get_text())
            if txt and len(txt) > 3:
                res["h2_headings"].append(txt)

        for h3 in soup.find_all("h3"):
            txt = clean_text(h3.get_text())
            if txt and len(txt) > 3:
                res["h3_headings"].append(txt)

        # Body Text & Word count
        body_text = clean_text(soup.get_text())
        words = body_text.split()
        res["word_count"] = len(words)

        res["has_tables"] = bool(soup.find("table"))
        res["has_faq"] = "faq" in resp.text.lower() or "প্রশ্ন" in resp.text
    except Exception as e:
        res["error"] = str(e)[:60]

    return res


def extract_top_serp_urls(keyword: str, max_results: int = 4) -> list[str]:
    """
    Extracts top organic search result URLs using multiple resilient sources:
    1. DuckDuckGo HTML / Lite
    2. Bing search
    3. Curated domain fallback
    """
    urls = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Accept-Language": "bn,en-US;q=0.9,en;q=0.8",
    }

    # Method 1: DuckDuckGo HTML
    try:
        search_url = f"https://html.duckduckgo.com/html/?q={quote_plus(keyword)}"
        resp = requests.post(search_url, data={"q": keyword}, headers=headers, timeout=8)
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text, "html.parser")
            for a in soup.find_all("a", class_="result__url"):
                href = a.get("href", "").strip()
                if href and not any(blocked in href for blocked in ("google.", "youtube.", "facebook.", "duckduckgo.", "bing.")):
                    if href.startswith("//"):
                        href = "https:" + href
                    elif not href.startswith("http"):
                        href = "https://" + href
                    if href not in urls:
                        urls.append(href)
                if len(urls) >= max_results:
                    return urls
    except Exception:
        pass

    # Method 2: DuckDuckGo Lite
    if len(urls) < 2:
        try:
            lite_url = f"https://lite.duckduckgo.com/lite/"
            resp = requests.post(lite_url, data={"q": keyword}, headers=headers, timeout=8)
            if resp.status_code == 200:
                soup = BeautifulSoup(resp.text, "html.parser")
                for a in soup.find_all("a", class_="result-link"):
                    href = a.get("href", "").strip()
                    if href and href.startswith("http") and not any(b in href for b in ("duckduckgo.", "google.")):
                        if href not in urls:
                            urls.append(href)
                    if len(urls) >= max_results:
                        return urls
        except Exception:
            pass

    # Method 3: Bing Search
    if len(urls) < 2:
        try:
            bing_url = f"https://www.bing.com/search?q={quote_plus(keyword)}"
            resp = requests.get(bing_url, headers=headers, timeout=8)
            if resp.status_code == 200:
                soup = BeautifulSoup(resp.text, "html.parser")
                for h2 in soup.find_all("h2"):
                    a = h2.find("a")
                    if a and a.get("href", "").startswith("http"):
                        href = a["href"]
                        if not any(b in href for b in ("bing.com", "microsoft.com", "msn.com")):
                            if href not in urls:
                                urls.append(href)
                    if len(urls) >= max_results:
                        return urls
        except Exception:
            pass

    return urls


def compare_with_local_post(our_post_path: str, competitor_data: list[dict], keyword: str) -> dict:
    """Compares Helptrickbd post with competitors to find gaps."""
    our_data = {
        "word_count": 0,
        "h2_headings": [],
        "h3_headings": [],
        "has_tables": False,
        "has_faq": False,
    }

    if our_post_path and os.path.exists(our_post_path):
        with open(our_post_path, "r", encoding="utf-8") as f:
            html = f.read()
        soup = BeautifulSoup(html, "html.parser")
        for h2 in soup.find_all("h2"):
            our_data["h2_headings"].append(clean_text(h2.get_text()))
        for h3 in soup.find_all("h3"):
            our_data["h3_headings"].append(clean_text(h3.get_text()))
        our_data["word_count"] = len(clean_text(soup.get_text()).split())
        our_data["has_tables"] = bool(soup.find("table"))
        our_data["has_faq"] = "faq" in html.lower() or "faqpage" in html.lower() or "প্রশ্ন" in html

    # Identify competitor subtopics
    comp_h2_set = set()
    total_comp_words = 0
    valid_comps = [c for c in competitor_data if not c.get("error") and c.get("word_count", 0) > 150]

    for c in valid_comps:
        total_comp_words += c["word_count"]
        for h in c["h2_headings"]:
            comp_h2_set.add(h)

    avg_comp_words = int(total_comp_words / max(1, len(valid_comps))) if valid_comps else 1000

    # Content gaps: topics competitors covered that we don't have
    missing_topics = []
    for h in comp_h2_set:
        # Check if any words match in our headings
        h_words = set(h.lower().split())
        covered = False
        for our_h in our_data["h2_headings"]:
            our_words = set(our_h.lower().split())
            if len(h_words.intersection(our_words)) >= 2 or our_h in h or h in our_h:
                covered = True
                break
        if not covered:
            missing_topics.append(h)

    return {
        "keyword": keyword,
        "our_data": our_data,
        "competitor_count": len(valid_comps),
        "avg_competitor_words": avg_comp_words,
        "missing_topics": missing_topics[:8],
        "competitors": valid_comps,
    }


def generate_manifesto_markdown(analysis: dict, output_file: str):
    """Generates the Content Gap Manifesto markdown without any emojis."""
    md = []
    md.append(f"# Content Gap Manifesto: '{analysis['keyword']}'")
    md.append(f"> গুগল সার্চ রেজাল্টে ১ নম্বরে র‍্যাংক করার জন্য প্রতিযোগীদের চেয়ে তথ্যবহুল ও প্রামাণ্য কন্টেন্ট বিশ্লেষণ।\n")

    md.append("## ১. তুলনামূলক পরিসংখ্যান (HelpTrickBD vs Competitors)")
    md.append("| সূচক | HelpTrickBD পোস্ট | প্রতিযোগী গড় | প্রস্তাবিত মানদণ্ড |")
    md.append("| :--- | :---: | :---: | :---: |")

    our_words = analysis["our_data"]["word_count"]
    comp_words = analysis["avg_competitor_words"]
    rec_words = max(1350, int(comp_words * 1.25))

    has_table_str = "[উপস্থিত]" if analysis['our_data']['has_tables'] else "[অনুপস্থিত]"
    has_faq_str = "[উপস্থিত]" if analysis['our_data']['has_faq'] else "[অনুপস্থিত]"

    md.append(f"| মোট শব্দ সংখ্যা | **{our_words:,} শব্দ** | {comp_words:,} শব্দ | **{rec_words:,}+ শব্দ** |")
    md.append(f"| তথ্য সারণী (Comparison Table) | {has_table_str} | বিভিন্ন | **বাধ্যতামূলক তুলনামূলক সারণী** |")
    md.append(f"| FAQ সেকশন ও Microdata | {has_faq_str} | সাধারণ প্রশ্নোত্তর | **Schema.org FAQPage** |")

    md.append("\n## ২. প্রস্তাবিত সাব-টপিক ও কন্টেন্ট গ্যাপসমূহ:")
    if analysis["missing_topics"]:
        for idx, topic in enumerate(analysis["missing_topics"], 1):
            md.append(f"{idx}. **{topic}** (এই বিষয়টি আপনার আর্টিকেলে একটি নতুন H2 সেকশন বা হাইলাইট বক্সে অন্তর্ভুক্ত করুন)")
    else:
        md.append("HelpTrickBD-এর এই পোস্টটিতে ইতিমধ্যেই শীর্ষ প্রতিযোগীদের তুলনায় পূর্ণাঙ্গ ও সমৃদ্ধ সাব-হেডিংস রয়েছে।")

    md.append("\n## ৩. প্রতিযোগী সাইটসমূহের বিস্তারিত কন্টেন্ট বিশ্লেষণ:")
    if analysis["competitors"]:
        for c in analysis["competitors"]:
            md.append(f"- **{c['title']}** ({c['word_count']} শব্দ)")
            md.append(f"  URL: {c['url']}")
            if c['h2_headings']:
                md.append(f"  *হেডিংস:* {', '.join(c['h2_headings'][:4])}")
    else:
        md.append("সরাসরি প্রতিযোগী পৃষ্ঠা লোড করা সম্ভব হয়নি; বেঞ্চমার্ক মানদণ্ড অনুযায়ী কন্টেন্ট প্রস্তুত করা হয়েছে।")

    report = "\n".join(md)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(report)
    return report


def main():
    parser = argparse.ArgumentParser(description="Competitor SERP Content Gap Analyzer for Helptrickbd")
    parser.add_argument("--keyword", "-k", required=True, help="Target search keyword")
    parser.add_argument("--post", "-p", help="Path to our local HTML post to compare against")
    parser.add_argument("--urls", "-u", nargs="*", help="Direct competitor URLs to analyze (optional)")
    parser.add_argument("--output", "-o", default="content_gap_manifesto.md", help="Output report path")

    args = parser.parse_args()

    print("=" * 65)
    print(f"🎯 Helptrickbd SERP Content Gap Analyzer: '{args.keyword}'")
    print("=" * 65)

    comp_urls = args.urls if args.urls else extract_top_serp_urls(args.keyword)
    if not comp_urls:
        print("ℹ️ Auto-discovering simulated search targets...")
        comp_urls = [
            "https://bn.wikipedia.org/wiki/" + quote_plus(args.keyword),
        ]

    print(f"📡 Analyzing {len(comp_urls)} competitor pages...")
    competitor_data = []
    for u in comp_urls:
        print(f"  Fetching: {u[:60]} ...")
        competitor_data.append(analyze_webpage_content(u))

    analysis = compare_with_local_post(args.post, competitor_data, args.keyword)
    generate_manifesto_markdown(analysis, args.output)

    print(f"\n✅ Content Gap Manifesto generated successfully!")
    print(f"💾 Report saved to: {args.output}")


if __name__ == "__main__":
    main()
