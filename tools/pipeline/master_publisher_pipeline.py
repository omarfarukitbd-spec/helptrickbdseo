#!/usr/bin/env python3
"""
tools/pipeline/master_publisher_pipeline.py
HelpTrickBD - Master Unified Publishing & SEO Automation Pipeline.

Orchestrates the entire publishing workflow in a single command:
1. Content Quality & Policy Audit (Word count, Zero-emoji check, SolaimanLipi, <!--more--> tag, Schema.org)
2. Inbound & Outbound Link Health Verification (Zero 404/broken links)
3. 10–20 KB Ultra-WebP Image Optimization & Compression (Core Web Vitals LCP < 1.0s)
4. AdSense RPM & High-CPC Monetization Injection
5. Direct Blogger API v3 Live Publishing
6. Google Indexing API Instant Crawl Submission
"""

import os
import sys
import re
import json
import argparse
from bs4 import BeautifulSoup

try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.image_optimizer.webp_compressor import compress_to_target_webp
from tools.link_guardian.link_checker import check_single_url
from tools.adsense_suite.rpm_booster import analyze_article_monetization, inject_policy_safe_ad_slots


def audit_content_quality(html_content: str) -> dict:
    """Performs rigorous quality audit based on HelpTrickBD editorial and SEO standards."""
    soup = BeautifulSoup(html_content, "html.parser")
    text = soup.get_text()
    words = len(text.split())

    # 1. Emoji Detection (Zero-Emoji Policy)
    emoji_pattern = re.compile(
        r"[\U0001F300-\U0001F9FF\U0001FA00-\U0001FAFF\u2600-\u26FF\u2700-\u27BF]"
    )
    detected_emojis = emoji_pattern.findall(html_content)

    # 2. Font & Typography
    has_solaiman = "solaimanlipi" in html_content.lower()

    # 3. Jump Break <!--more-->
    has_jump_break = "<!--more-->" in html_content

    # 4. Schema.org Microdata
    has_faq_schema = "faqpage" in html_content.lower()
    has_howto_schema = "howto" in html_content.lower()
    has_article_schema = "blogposting" in html_content.lower() or "article" in html_content.lower()

    # 5. Tables & Callouts
    has_table = bool(soup.find("table"))
    has_callout = bool(soup.find(class_=re.compile(r"callout|box|qbox|card", re.I)))

    # 6. Images
    images = soup.find_all("img")
    missing_alts = [img.get("src", "") for img in images if not img.get("alt")]

    return {
        "word_count": words,
        "is_thin": words < 1150,
        "emojis": detected_emojis,
        "emoji_free": len(detected_emojis) == 0,
        "has_solaiman_font": has_solaiman,
        "has_jump_break": has_jump_break,
        "has_schema": has_faq_schema or has_howto_schema or has_article_schema,
        "schema_types": [s for s, cond in [("FAQPage", has_faq_schema), ("HowTo", has_howto_schema), ("Article", has_article_schema)] if cond],
        "has_table": has_table,
        "has_callout": has_callout,
        "image_count": len(images),
        "missing_alts": missing_alts,
    }


def strip_all_emojis(html_content: str) -> str:
    """Strips all emoji characters to enforce the strict zero-emoji policy."""
    emoji_pattern = re.compile(
        r"[\U0001F300-\U0001F9FF\U0001FA00-\U0001FAFF\u2600-\u26FF\u2700-\u27BF]"
    )
    return emoji_pattern.sub("", html_content)


def audit_article_links(html_content: str) -> list[dict]:
    """Validates all outbound and internal links."""
    soup = BeautifulSoup(html_content, "html.parser")
    links = []
    for a in soup.find_all("a", href=True):
        href = a["href"].strip()
        if href.startswith(("http://", "https://")):
            links.append(href)

    unique_links = list(set(links))
    results = []
    for u in unique_links:
        res = check_single_url(u)
        results.append(res)
    return results


def optimize_article_images(html_content: str, auto_compress: bool = True) -> tuple[str, list[dict]]:
    """
    Finds referenced local images and ensures 10–20 KB WebP versions exist.
    Updates HTML img src if WebP versions are available.
    """
    soup = BeautifulSoup(html_content, "html.parser")
    images = soup.find_all("img")
    stats = []

    for img in images:
        src = img.get("src", "")
        # Check if local image path
        local_candidate = None
        if src.startswith("file:///"):
            local_candidate = src.replace("file:///", "").replace("/", os.sep)
        elif os.path.exists(src):
            local_candidate = src
        elif os.path.exists(os.path.join(PROJECT_ROOT, src.lstrip("/"))):
            local_candidate = os.path.join(PROJECT_ROOT, src.lstrip("/"))

        if local_candidate and os.path.exists(local_candidate):
            orig_sz = os.path.getsize(local_candidate) / 1024.0
            if auto_compress and not local_candidate.lower().endswith(".webp"):
                webp_candidate = os.path.splitext(local_candidate)[0] + ".webp"
                try:
                    compress_to_target_webp(local_candidate, webp_candidate, target_min_kb=10.0, target_max_kb=20.0)
                    final_sz = os.path.getsize(webp_candidate) / 1024.0
                    stats.append({"file": os.path.basename(local_candidate), "orig_kb": orig_sz, "final_kb": final_sz, "optimized": True})
                except Exception as e:
                    stats.append({"file": os.path.basename(local_candidate), "error": str(e), "optimized": False})
            else:
                stats.append({"file": os.path.basename(local_candidate), "orig_kb": orig_sz, "final_kb": orig_sz, "optimized": False})

    return str(soup), stats


def publish_to_blogger(post_id: str, html_content: str, title: str = None, labels: list[str] = None) -> bool:
    """Publishes updated content directly to Blogger via Blogger API v3."""
    try:
        from tools.blogger_publisher.update_post import get_authenticated_service, BLOG_ID
        service = get_authenticated_service()
        if not service:
            print("Error: Could not authenticate with Blogger API v3.", file=sys.stderr)
            return False

        post_body = {"content": html_content}
        if title:
            post_body["title"] = title
        if labels:
            post_body["labels"] = labels

        result = service.posts().patch(
            blogId=BLOG_ID,
            postId=post_id,
            body=post_body
        ).execute()

        print(f"Blogger Post Updated Successfully! URL: {result.get('url')}")
        return True
    except Exception as e:
        print(f"Error publishing to Blogger: {e}", file=sys.stderr)
        return False


def submit_to_google_indexing(url: str) -> bool:
    """Submits URL to Google Indexing API."""
    try:
        import httplib2
        from googleapiclient.discovery import build
        from oauth2client.service_account import ServiceAccountCredentials

        sa_path = os.path.join(PROJECT_ROOT, "service_account.json")
        if not os.path.exists(sa_path):
            sa_path = os.path.join(PROJECT_ROOT, "tools", "indexer", "service_account.json")

        if not os.path.exists(sa_path):
            print(f"Warning: service_account.json not found. Indexing skipped.", file=sys.stderr)
            return False

        scopes = ["https://www.googleapis.com/auth/indexing"]
        credentials = ServiceAccountCredentials.from_json_keyfile_name(sa_path, scopes=scopes)
        http = credentials.authorize(httplib2.Http())
        service = build("indexing", "v3", http=http)

        body = {"url": url, "type": "URL_UPDATED"}
        service.urlNotifications().publish(body=body).execute()
        print(f"Google Indexing API: URL submitted successfully (URL_UPDATED).")
        return True
    except Exception as e:
        print(f"Warning: Indexing submission failed: {e}", file=sys.stderr)
        return False


def run_pipeline(args):
    print("=" * 70)
    print("HELPTRICKBD MASTER PUBLISHING & SEO PIPELINE")
    print("=" * 70)

    if not os.path.exists(args.html):
        print(f"Error: HTML file not found: {args.html}", file=sys.stderr)
        sys.exit(1)

    with open(args.html, "r", encoding="utf-8") as f:
        html_content = f.read()

    # Step 1: Content Quality & Policy Audit
    print("\n[Step 1/6] Running Quality & Policy Pre-flight Audit...")
    quality = audit_content_quality(html_content)
    print(f"  • Words Count: {quality['word_count']} words {'(PASS)' if not quality['is_thin'] else '(WARNING: Thin content < 1150 words)'}")
    print(f"  • SolaimanLipi Font: {'PASS' if quality['has_solaiman_font'] else 'WARNING: SolaimanLipi not detected'}")
    print(f"  • Jump Break (<!--more-->): {'PASS' if quality['has_jump_break'] else 'WARNING: Missing <!--more-->'}")
    print(f"  • Schema.org Microdata: {', '.join(quality['schema_types']) if quality['has_schema'] else 'NONE'}")
    emoji_cnt = len(quality['emojis'])
    emoji_status = "PASS (100% Emoji-Free)" if quality['emoji_free'] else f"FAILED ({emoji_cnt} emojis detected)"
    print(f"  • Zero-Emoji Status: {emoji_status}")

    if not quality['emoji_free']:
        if args.strip_emojis:
            print(f"  Action: Auto-stripping {len(quality['emojis'])} detected emojis...")
            html_content = strip_all_emojis(html_content)
            with open(args.html, "w", encoding="utf-8") as f:
                f.write(html_content)
            print("  Notice: All emojis successfully stripped from HTML file.")
        else:
            print("  Notice: Use --strip-emojis to automatically remove emojis to meet policy.")

    # Step 2: Link Validation
    if args.check_links:
        print("\n[Step 2/6] Validating Inbound & Outbound Links...")
        links_res = audit_article_links(html_content)
        broken = [l for l in links_res if l["is_broken"]]
        print(f"  • Checked {len(links_res)} links: {len(links_res) - len(broken)} Valid, {len(broken)} Broken")
        for b in broken:
            print(f"    [BROKEN] {b['url']} -> {b['error_msg']}")
    else:
        print("\n[Step 2/6] Link check skipped (use --check-links to run).")

    # Step 3: WebP Compression & Image Optimization
    print("\n[Step 3/6] Image Optimization (10–20 KB WebP Target)...")
    html_content, img_stats = optimize_article_images(html_content, auto_compress=args.auto_compress)
    if img_stats:
        for s in img_stats:
            if s.get("optimized"):
                print(f"  • {s['file']}: {s['orig_kb']:.1f} KB -> {s['final_kb']:.1f} KB (Optimized WebP)")
            elif "error" in s:
                print(f"  • {s['file']}: Error ({s['error']})")
            else:
                print(f"  • {s['file']}: Current size {s.get('orig_kb', 0):.1f} KB")
    else:
        print("  • No local images required processing.")

    # Step 4: AdSense Monetization & Slots
    print("\n[Step 4/6] AdSense Monetization Scoring...")
    monetization = analyze_article_monetization(html_content)
    print(f"  • Score: {monetization['monetization_score']}/100")
    print(f"  • High-CPC Matches: {monetization['total_cpc_hits']}")
    if args.inject_ads:
        print(f"  • Injecting policy-safe AdSense slots...")
        html_content = inject_policy_safe_ad_slots(html_content, pub_id=args.pub_id, slot_id=args.slot_id)
        with open(args.html, "w", encoding="utf-8") as f:
            f.write(html_content)
        print("  • Ad units successfully embedded.")

    # Step 5: Blogger API v3 Live Publishing
    if args.publish:
        if not args.post_id:
            print("\n[Step 5/6] Error: --post-id required to publish to Blogger.", file=sys.stderr)
        else:
            print(f"\n[Step 5/6] Publishing directly to Blogger (Post ID: {args.post_id})...")
            labels = [l.strip() for l in args.labels.split(",")] if args.labels else None
            success = publish_to_blogger(args.post_id, html_content, title=args.title, labels=labels)
            if success and args.index and args.url:
                print("\n[Step 6/6] Pinging Google Indexing API...")
                submit_to_google_indexing(args.url)
            elif args.index and not args.url:
                print("\n[Step 6/6] Notice: --url is required to ping Google Indexing API.")
            else:
                print("\n[Step 6/6] Google Indexing ping skipped (use --index and --url).")
    else:
        print("\n[Step 5/6] Blogger publishing skipped (use --publish --post-id <ID>).")
        print("[Step 6/6] Google Indexing skipped.")

    print("\n" + "=" * 70)
    print("PIPELINE EXECUTION COMPLETED")
    print("=" * 70)


def main():
    parser = argparse.ArgumentParser(description="HelpTrickBD Master Publishing & SEO Automation Pipeline")
    parser.add_argument("--html", required=True, help="Path to article HTML file")
    parser.add_argument("--post-id", help="Blogger Post ID (for publishing)")
    parser.add_argument("--url", help="Live article URL (for Google Indexing API)")
    parser.add_argument("--title", help="Post Title override (optional)")
    parser.add_argument("--labels", help="Comma-separated labels (optional)")
    parser.add_argument("--auto-compress", action="store_true", default=True, help="Auto-compress linked images to 10-20 KB WebP")
    parser.add_argument("--strip-emojis", action="store_true", help="Automatically strip all emojis to ensure zero-emoji compliance")
    parser.add_argument("--check-links", action="store_true", help="Validate all internal and external links")
    parser.add_argument("--inject-ads", action="store_true", help="Inject policy-compliant AdSense slots")
    parser.add_argument("--pub-id", help="AdSense Publisher ID")
    parser.add_argument("--slot-id", help="AdSense Slot ID")
    parser.add_argument("--publish", action="store_true", help="Publish directly to Blogger via Blogger API v3")
    parser.add_argument("--index", action="store_true", help="Submit to Google Indexing API after publishing")

    args = parser.parse_args()
    run_pipeline(args)


if __name__ == "__main__":
    main()
