#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/wp_auditor/audit_rules.py
--------------------------------
Modular audit rules for WordPress posts, pages, images, and SEO metadata.
Zero-Emoji compliance (Rule 12).
"""

import re
from typing import Dict, Any, List

def audit_content_depth(post_data: Dict[str, Any], soup) -> Dict[str, Any]:
    """Audits word count and content substance (Rule 01: Zero Thin Content)."""
    # Remove script and style elements
    for el in soup(["script", "style"]):
        el.decompose()

    text = soup.get_text()
    words = [w for w in re.split(r'\s+', text) if w.strip()]
    count = len(words)

    result = {
        "check": "content_depth",
        "word_count": count,
        "status": "PASS",
        "messages": []
    }

    if count < 600:
        result["status"] = "CRITICAL"
        result["messages"].append(f"Critical thin content: only {count} words (AdSense Low Value Content risk). Target is 1,200+ words.")
    elif count < 1000:
        result["status"] = "WARNING"
        result["messages"].append(f"Content depth warning: {count} words is below the standard target of 1,200+ words.")
    else:
        result["messages"].append(f"Content depth passed: {count:,} words.")

    return result

def audit_image_seo(post_data: Dict[str, Any], soup) -> Dict[str, Any]:
    """Audits Featured Image assignment and in-body <img> alt tags and formats."""
    result = {
        "check": "image_seo",
        "status": "PASS",
        "messages": [],
        "total_images": 0,
        "missing_alt": 0
    }

    # 1. Featured Media check
    featured_media = post_data.get("featured_media", 0)
    if not featured_media:
        result["status"] = "WARNING"
        result["messages"].append("Missing Featured Image: No native featured_media attached to post.")

    # 2. In-content images
    imgs = soup.find_all("img")
    result["total_images"] = len(imgs)

    missing_alt_count = 0
    for idx, img in enumerate(imgs):
        alt = img.get("alt", "").strip()
        src = img.get("src", "").strip()

        if not alt or len(alt) < 4:
            missing_alt_count += 1

        # Check local leak
        src_lower = src.lower()
        if src_lower.startswith("file://") or src_lower.startswith("c:") or src_lower.startswith("d:"):
            result["status"] = "CRITICAL"
            result["messages"].append(f"Image #{idx+1} has local file path leak: {src}")

    result["missing_alt"] = missing_alt_count
    if missing_alt_count > 0:
        if result["status"] != "CRITICAL":
            result["status"] = "WARNING"
        result["messages"].append(f"{missing_alt_count} image(s) missing descriptive alt text.")
    else:
        result["messages"].append(f"All {len(imgs)} image(s) have descriptive alt tags.")

    return result

def audit_rank_math_seo(post_data: Dict[str, Any], soup) -> Dict[str, Any]:
    """Audits Rank Math SEO focus keyword, title length, and description length."""
    result = {
        "check": "rank_math_seo",
        "status": "PASS",
        "messages": []
    }

    meta = post_data.get("meta", {})
    title = meta.get("rank_math_title") or post_data.get("title", {}).get("rendered", "")
    desc = meta.get("rank_math_description", "")
    focus_kw = meta.get("rank_math_focus_keyword", "")

    # Title check
    title_len = len(title)
    if title_len < 30:
        result["status"] = "WARNING"
        result["messages"].append(f"SEO Title is too short ({title_len} chars). Optimal: 50-65 chars.")
    elif title_len > 75:
        result["status"] = "WARNING"
        result["messages"].append(f"SEO Title is long ({title_len} chars), might truncate in Google SERP.")

    # Description check
    if not desc:
        result["status"] = "WARNING"
        result["messages"].append("Missing Meta Description: rank_math_description is empty.")
    else:
        desc_len = len(desc)
        if desc_len < 100:
            result["status"] = "WARNING"
            result["messages"].append(f"Meta Description is short ({desc_len} chars). Optimal: 120-160 chars.")
        elif desc_len > 175:
            result["status"] = "WARNING"
            result["messages"].append(f"Meta Description is long ({desc_len} chars).")

    # Focus keyword check
    if not focus_kw:
        result["messages"].append("Notice: No explicit focus keyword defined in Rank Math postmeta.")
    else:
        # Check if keyword is in title
        if focus_kw.lower() not in title.lower():
            result["status"] = "WARNING"
            result["messages"].append(f"Focus keyword '{focus_kw}' not detected in post title.")

    return result

def audit_headings(post_data: Dict[str, Any], soup) -> Dict[str, Any]:
    """Audits H1, H2, and H3 structure."""
    result = {
        "check": "headings",
        "status": "PASS",
        "messages": []
    }

    h1_tags = soup.find_all("h1")
    if len(h1_tags) > 0:
        # In WordPress, the theme renders the post title as H1. Extra H1 in body is an SEO anti-pattern.
        result["status"] = "WARNING"
        result["messages"].append(f"Duplicate H1: Found {len(h1_tags)} <h1> tag(s) inside post body. Post title already provides primary H1.")

    h2_tags = soup.find_all("h2")
    if len(h2_tags) < 2:
        result["status"] = "WARNING"
        result["messages"].append(f"Weak heading hierarchy: Only {len(h2_tags)} <h2> tag(s) found. High-ranking posts need at least 2-4 structured H2 sections.")
    else:
        result["messages"].append(f"Structured heading hierarchy verified ({len(h2_tags)} H2 headings).")

    return result

def audit_links_and_legacy(post_data: Dict[str, Any], soup) -> Dict[str, Any]:
    """Audits for residual legacy Blogger .html links and broken structure."""
    result = {
        "check": "links_and_legacy",
        "status": "PASS",
        "messages": [],
        "legacy_html_links": []
    }

    anchors = soup.find_all("a", href=True)
    legacy_links = []

    for a in anchors:
        href = a["href"].strip()
        # Look for legacy blogger URL patterns pointing to helptrickbd
        if "helptrickbd.com" in href and (".html" in href or "/202" in href or "/p/" in href):
            legacy_links.append(href)

    if legacy_links:
        result["status"] = "WARNING"
        result["legacy_html_links"] = legacy_links
        result["messages"].append(f"Residual legacy links found: {len(legacy_links)} link(s) still point to old .html URLs.")
    else:
        result["messages"].append(f"Internal link check clean ({len(anchors)} links checked, zero legacy .html links).")

    return result

def audit_interactive_elements(post_data: Dict[str, Any], soup) -> Dict[str, Any]:
    """Audits presence of tables, callout boxes, or details accordions."""
    result = {
        "check": "interactive_elements",
        "status": "PASS",
        "messages": []
    }

    tables = len(soup.find_all("table"))
    accordions = len(soup.find_all("details"))
    callouts = len(soup.find_all(class_=re.compile(r'(box|callout|card|alert|overview)', re.I)))

    features = []
    if tables > 0:
        features.append(f"{tables} table(s)")
    if accordions > 0:
        features.append(f"{accordions} accordion(s)")
    if callouts > 0:
        features.append(f"{callouts} callout card(s)")

    if features:
        result["messages"].append(f"Rich interactive formatting verified: {', '.join(features)}.")
    else:
        result["status"] = "WARNING"
        result["messages"].append("Visual plainness: Post lacks comparison tables, callout boxes, or interactive accordions.")

    return result
