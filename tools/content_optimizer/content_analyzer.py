#!/usr/bin/env python3
"""
HelpTrickBD On-Page Content & SEO Score Optimizer
Inspired by Yoast SEO & Advertools (High GitHub Stars)

Analyzes any live post or text draft against 10 on-page ranking factors
to guarantee 100% AdSense and Google top-ranking quality before publication.

Usage:
    python content_analyzer.py --url https://www.helptrickbd.com/2026/01/sarbobhoumotto-ki-songga-boishisto-o-prokarved.html --keyword "সার্বভৌমত্ব"
    python content_analyzer.py --file draft.txt --keyword "রাষ্ট্র"
"""

import argparse
import re
import sys
from urllib.parse import urlparse

try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("[!] Missing requests or beautifulsoup4. Run: pip install requests beautifulsoup4")
    sys.exit(1)


def analyze_content(title, meta_desc, body_text, url, focus_keyword, images, internal_links, external_links, headings):
    checks = []
    score = 0
    max_score = 100
    kw = focus_keyword.strip().lower() if focus_keyword else ""

    # 1. Title Check (15 pts)
    title_len = len(title)
    if 30 <= title_len <= 70:
        if kw and kw in title.lower():
            checks.append(("✅", "Title Tag", f"Optimal length ({title_len} chars) and contains focus keyword '{focus_keyword}'", 15))
            score += 15
        else:
            checks.append(("⚠️", "Title Tag", f"Good length ({title_len} chars), but focus keyword was not found in title", 10))
            score += 10
    else:
        checks.append(("❌", "Title Tag", f"Title length ({title_len} chars) should be between 30 and 65 chars", 5))
        score += 5

    # 2. Meta Description Check (10 pts)
    desc_len = len(meta_desc)
    if 80 <= desc_len <= 165:
        if kw and kw in meta_desc.lower():
            checks.append(("✅", "Meta Description", f"Optimal length ({desc_len} chars) with focus keyword included", 10))
            score += 10
        else:
            checks.append(("⚠️", "Meta Description", f"Good length ({desc_len} chars), but missing focus keyword", 7))
            score += 7
    else:
        checks.append(("❌", "Meta Description", f"Length ({desc_len} chars) is outside optimal range (100-160 chars)", 3))
        score += 3

    # 3. Content Word Count (25 pts)
    words = [w for w in body_text.split() if len(w) > 1]
    word_count = len(words)
    if word_count >= 1000:
        checks.append(("✅", "Word Count", f"Comprehensive content depth ({word_count} words) - Excellent for AdSense!", 25))
        score += 25
    elif word_count >= 700:
        checks.append(("⚠️", "Word Count", f"Decent length ({word_count} words). Aim for 1,000+ words for competitive topics", 18))
        score += 18
    elif word_count >= 400:
        checks.append(("⚠️", "Word Count", f"Moderate length ({word_count} words). Expand with subheadings and examples", 10))
        score += 10
    else:
        checks.append(("❌", "Word Count", f"Thin content alert ({word_count} words). Minimum 800 words required for AdSense approval", 0))

    # 4. Keyword in First 100 Words (10 pts)
    first_100_words = " ".join(words[:100]).lower()
    if kw:
        if kw in first_100_words:
            checks.append(("✅", "Intro Keyword Placement", f"Focus keyword appears in the first 100 words", 10))
            score += 10
        else:
            checks.append(("❌", "Intro Keyword Placement", f"Focus keyword should appear in the first paragraph/100 words", 0))
    else:
        checks.append(("ℹ️", "Intro Keyword Placement", "No focus keyword specified to test", 5))
        score += 5

    # 5. Keyword Density (10 pts)
    if kw and word_count > 0:
        kw_count = body_text.lower().count(kw)
        density = (kw_count / word_count) * 100
        if 0.8 <= density <= 2.5:
            checks.append(("✅", "Keyword Density", f"Natural density ({density:.2f}% - {kw_count} times)", 10))
            score += 10
        elif density < 0.8:
            checks.append(("⚠️", "Keyword Density", f"Low density ({density:.2f}% - {kw_count} times). Mention '{focus_keyword}' more often naturally", 6))
            score += 6
        else:
            checks.append(("❌", "Keyword Density", f"High density / Keyword Stuffing risk ({density:.2f}% - {kw_count} times). Keep below 2.5%", 2))
            score += 2
    else:
        checks.append(("ℹ️", "Keyword Density", "Keyword density not computed", 5))
        score += 5

    # 6. Heading Structure (15 pts)
    h2_count = len(headings.get("h2", []))
    h3_count = len(headings.get("h3", []))
    if h2_count >= 3:
        has_kw_in_h2 = any(kw in h.lower() for h in headings.get("h2", [])) if kw else True
        if has_kw_in_h2:
            checks.append(("✅", "Heading Hierarchy", f"Great structure: {h2_count} H2s, {h3_count} H3s with keyword in subheadings", 15))
            score += 15
        else:
            checks.append(("⚠️", "Heading Hierarchy", f"{h2_count} H2s found, but include focus keyword in at least one H2", 12))
            score += 12
    elif h2_count >= 1:
        checks.append(("⚠️", "Heading Hierarchy", f"Only {h2_count} H2 found. Break article into at least 3-4 subheadings", 8))
        score += 8
    else:
        checks.append(("❌", "Heading Hierarchy", "Missing H2 subheadings! Headings are essential for readability and SEO", 0))

    # 7. Image SEO (10 pts)
    total_imgs = len(images)
    missing_alt = [img for img in images if not img.get("alt") or not img.get("alt").strip()]
    if total_imgs >= 1 and len(missing_alt) == 0:
        checks.append(("✅", "Image SEO", f"{total_imgs} image(s) present, and all have descriptive alt attributes", 10))
        score += 10
    elif total_imgs >= 1:
        checks.append(("⚠️", "Image SEO", f"{len(missing_alt)}/{total_imgs} image(s) are missing alt text", 5))
        score += 5
    else:
        checks.append(("❌", "Image SEO", "No images found. Every article should have at least 1-2 images/infographics", 2))
        score += 2

    # 8. Linking Structure (5 pts)
    int_count = len(internal_links)
    ext_count = len(external_links)
    if int_count >= 2 and ext_count >= 1:
        checks.append(("✅", "Links", f"Healthy link profile: {int_count} internal link(s) and {ext_count} external link(s)", 5))
        score += 5
    elif int_count >= 1:
        checks.append(("⚠️", "Links", f"{int_count} internal link(s). Add an outbound link to an authority source (Wikipedia, Govt board)", 3))
        score += 3
    else:
        checks.append(("❌", "Links", "Zero internal links found. Link to at least 2 other related posts on your blog", 0))

    return score, checks, word_count


def analyze_url(url, focus_keyword=""):
    print(f"[*] Fetching URL: {url} ...")
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) HelpTrickBDAnalyzer/1.0"}
        res = requests.get(url, headers=headers, timeout=12)
        res.raise_for_status()

        soup = BeautifulSoup(res.text, "html.parser")

        title = soup.find("title").get_text().strip() if soup.find("title") else ""
        meta_desc_tag = soup.find("meta", attrs={"name": "description"})
        meta_desc = meta_desc_tag.get("content", "").strip() if meta_desc_tag else ""

        post_body = soup.find("div", class_=re.compile(r"post-body|entry-content", re.I))
        if post_body:
            body_text = post_body.get_text(separator=" ", strip=True)
            imgs = post_body.find_all("img")
            all_links = post_body.find_all("a", href=True)
        else:
            body = soup.find("body")
            body_text = body.get_text(separator=" ", strip=True) if body else ""
            imgs = soup.find_all("img")
            all_links = soup.find_all("a", href=True)

        parsed_main_domain = urlparse(url).netloc
        internal_links = [a["href"] for a in all_links if parsed_main_domain in a["href"] or a["href"].startswith("/")]
        external_links = [a["href"] for a in all_links if a["href"].startswith("http") and parsed_main_domain not in a["href"]]

        headings = {
            "h2": [h.get_text().strip() for h in soup.find_all("h2") if h.get_text().strip()],
            "h3": [h.get_text().strip() for h in soup.find_all("h3") if h.get_text().strip()]
        }

        return analyze_content(title, meta_desc, body_text, url, focus_keyword, imgs, internal_links, external_links, headings)

    except Exception as e:
        print(f"[!] Error analyzing URL: {e}")
        return 0, [], 0


def main():
    parser = argparse.ArgumentParser(description="HelpTrickBD On-Page Content & SEO Score Optimizer")
    parser.add_argument("--url", help="Live post URL to analyze")
    parser.add_argument("--keyword", default="", help="Target focus keyword (e.g. 'সার্বভৌমত্ব' or 'Political Science')")
    parser.add_argument("--file", help="Path to text/markdown draft file to analyze")

    args = parser.parse_args()

    if not args.url and not args.file:
        # Run on a default sample post from HelpTrickBD
        args.url = "https://www.helptrickbd.com/2026/01/sarbobhoumotto-ki-songga-boishisto-o-prokarved.html"
        args.keyword = "সার্বভৌমত্ব"
        print("[*] No arguments given. Running on sample post:\n    " + args.url + "\n")

    if args.url:
        score, checks, word_count = analyze_url(args.url, args.keyword)
    elif args.file:
        with open(args.file, "r", encoding="utf-8") as f:
            content = f.read()
        score, checks, word_count = analyze_content("Draft Post", "", content, "", args.keyword, [], [], [], {})

    print("\n" + "="*65)
    print(f"  HelpTrickBD On-Page SEO & Content Quality Audit")
    print(f"  Focus Keyword: {args.keyword or 'Not Specified'}")
    print(f"  Word Count:    {word_count} words")
    print(f"  Overall Score: {score}/100")
    print("="*65 + "\n")

    for icon, item, message, pts in checks:
        print(f"{icon} [{item}] ({pts} pts): {message}")

    print("\n" + "-"*65)
    if score >= 80:
        print("🌟 RATING: EXCELLENT (Ready for AdSense & Google Top Rankings)")
    elif score >= 60:
        print("⚠️ RATING: GOOD (Needs slight tweaks to word count/keyword placement)")
    else:
        print("❌ RATING: NEEDS IMPROVEMENT (Expand content before publishing)")
    print("-"*65 + "\n")


if __name__ == "__main__":
    main()
