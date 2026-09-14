#!/usr/bin/env python3
"""
HelpTrickBD Intelligent Dynamic Internal Linker
Crawls HelpTrickBD's live sitemap, caches posts with semantic keywords,
and automatically recommends/injects 2-3 highly relevant internal links
into new articles to maximize topical authority and PageRank flow.

Usage:
    python linker.py --update-cache
    python linker.py --find "যুক্তরাষ্ট্রীয় সরকার"
"""

import argparse
import json
import os
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET

try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

SITEMAP_URL = "https://www.helptrickbd.com/sitemap.xml"
CACHE_FILE = os.path.join(os.path.dirname(__file__), "site_articles_index.json")


def fetch_site_urls(sitemap_url=SITEMAP_URL):
    """Fetches all article URLs from the live Blogger sitemap."""
    print(f"[*] Fetching sitemap from: {sitemap_url} ...")
    req = urllib.request.Request(sitemap_url, headers={"User-Agent": "Mozilla/5.0 (HelpTrickBD InternalLinker/2.0)"})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            xml_data = resp.read()
        root = ET.fromstring(xml_data)
        namespaces = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
        
        urls = []
        for loc in root.findall('.//ns:loc', namespaces):
            u = loc.text.strip()
            # Exclude legal/static pages
            if "/p/" not in u and "helptrickbd.com/20" in u:
                urls.append(u)
        
        print(f"[OK] Found {len(urls)} published blog articles.")
        return urls
    except Exception as e:
        print(f"[!] Failed to fetch live sitemap: {e}")
        return []


def build_keyword_index(urls):
    """Builds a searchable keyword index from article URL slugs."""
    indexed_posts = []
    
    # Common stop words in slugs
    stopwords = {"post", "html", "the", "a", "an", "and", "or", "in", "on", "of", "to", "for", "with"}
    
    for u in urls:
        slug = u.split("/")[-1].replace(".html", "")
        # Remove date prefixes if any
        parts = re.split(r"[-_]", slug)
        words = [p.lower() for p in parts if p.lower() not in stopwords and not p.isdigit()]
        
        title_readable = " ".join(words).title()
        indexed_posts.append({
            "url": u,
            "slug": slug,
            "title": title_readable,
            "keywords": words
        })
    
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(indexed_posts, f, indent=2, ensure_ascii=False)
    
    print(f"[OK] Cached {len(indexed_posts)} posts in {CACHE_FILE}")
    return indexed_posts


def load_cached_index():
    if os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    urls = fetch_site_urls()
    return build_keyword_index(urls)


# Academic Bengali-English Semantic Concept Map
BENGALI_CONCEPT_MAP = {
    "রাষ্ট্রবিজ্ঞান": ["political", "science", "government", "state", "constitution", "suggestion"],
    "যুক্তরাষ্ট্রীয়": ["political", "government", "constitution"],
    "যুক্তরাষ্ট্রীয়": ["political", "government", "constitution"],
    "সরকার": ["government", "political", "state"],
    "সার্বভৌমত্ব": ["sarbobhoumotto", "sovereignty", "political"],
    "সংবিধান": ["constitution", "law"],
    "ইতিহাস": ["history", "itihas"],
    "সমাজবিজ্ঞান": ["sociology", "social"],
    "অর্থনীতি": ["economics"],
    "ইসলামের ইতিহাস": ["islamic", "history"],
    "ভূগোল": ["geography"],
    "বাংলা": ["bangla", "bengali"],
    "ইংরেজি": ["english"],
    "অনার্স": ["honours", "exam", "suggestion"],
    "মাস্টার্স": ["masters"],
    "ডিগ্রি": ["degree"],
    "সাজেশন": ["suggestion", "exam"]
}


def find_related_links(query_text, max_links=3):
    """
    Finds top matching posts from HelpTrickBD for a given query or article text.
    """
    posts = load_cached_index()
    if not posts:
        return []
    
    query_words = set(re.findall(r"\w+", query_text.lower()))
    # Expand query words using BENGALI_CONCEPT_MAP
    expanded_words = set(query_words)
    for bn_key, en_terms in BENGALI_CONCEPT_MAP.items():
        if bn_key in query_text.lower():
            expanded_words.update(en_terms)
        for qw in query_words:
            if qw in bn_key or bn_key in qw:
                expanded_words.update(en_terms)

    scored_posts = []
    
    for p in posts:
        kw_set = set(p["keywords"])
        match_count = len(expanded_words.intersection(kw_set))
        
        # Substring / partial match boost
        for qw in expanded_words:
            if len(qw) > 3:
                for kw in p["keywords"]:
                    if qw in kw or kw in qw:
                        match_count += 0.5
        
        if match_count > 0:
            scored_posts.append((match_count, p))
            
    scored_posts.sort(key=lambda x: x[0], reverse=True)
    
    # If still no direct match, return recent high-value educational posts
    if not scored_posts and posts:
        return posts[:max_links]

    results = [item[1] for item in scored_posts[:max_links]]
    return results


def generate_internal_link_box(related_posts):
    """
    Generates a beautifully styled theme-native callout box for related posts.
    """
    if not related_posts:
        return ""
    
    links_html = []
    for p in related_posts:
        title = p["title"]
        url = p["url"]
        links_html.append(f'<li><a href="{url}" target="_blank" rel="noopener">📌 {title}</a></li>')
    
    html = f"""<div class="htbd-link-box" style="margin: 25px 0; padding: 15px 20px; background: #f0f7ff; border-left: 5px solid #1a73e8; border-radius: 6px;">
  <strong style="color: #1a73e8; font-size: 17px; display: block; margin-bottom: 8px;">📖 সম্পর্কিত আরো গুরুত্বপূর্ণ আর্টিকেল পড়ুন:</strong>
  <ul style="margin: 0; padding-left: 20px; line-height: 1.8;">
    {"".join(links_html)}
  </ul>
</div>"""
    return html


def main():
    parser = argparse.ArgumentParser(description="HelpTrickBD Dynamic Internal Linker")
    parser.add_argument("--update-cache", action="store_true", help="Refresh sitemap cache")
    parser.add_argument("--find", help="Find related posts for a topic or text")
    parser.add_argument("--count", type=int, default=3, help="Max links to return")
    
    args = parser.parse_args()
    
    if args.update_cache:
        urls = fetch_site_urls()
        build_keyword_index(urls)
    elif args.find:
        results = find_related_links(args.find, args.count)
        print(f"\n[+] Top {len(results)} Related Posts for '{args.find}':")
        for i, r in enumerate(results, 1):
            print(f"  {i}. {r['title']}")
            print(f"     URL: {r['url']}")
        print("\n[+] Generated Theme HTML Box:")
        print(generate_internal_link_box(results))
    else:
        urls = fetch_site_urls()
        build_keyword_index(urls)


if __name__ == "__main__":
    main()
