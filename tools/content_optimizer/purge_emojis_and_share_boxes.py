#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/content_optimizer/purge_emojis_and_share_boxes.py
--------------------------------------------------------
Surgically cleans all post HTML files:
1. Removes redundant custom social share boxes (<div class="ht-social-share-box">)
   because Blogger theme natively displays built-in share buttons.
2. Removes all decorative emojis (📌, 👉, 📢, ⏱️, ✅, 🎓, 📘, 💬, 💡, ⚠️, etc.)
   from TOC, headings, badges, callouts, and body text.
3. Standardizes Table of Contents (TOC) with clean, professional typographic styling.
4. Cleans meta reading badges to be elegant and emoji-free.
"""

import os
import sys
import re
from bs4 import BeautifulSoup

if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

EMOJI_REGEX = re.compile(
    r"[\U00010000-\U0010FFFF\uD800-\uDBFF\uDC00-\uDFFF\u2600-\u26FF\u2700-\u27BF\uFE00-\uFE0F]"
    r"|[📌📊📝⚡⭐🛡️🔒🌐🏢💾💻☁️✨👉📘📢⏱️✅🎓💬💡⚠️❶❷❸❹❺❻❼❽❾❿]"
)

def clean_text_of_emojis(text: str) -> str:
    """Removes emojis and collapses unnecessary spaces."""
    cleaned = EMOJI_REGEX.sub("", text)
    # Fix common artifacts
    cleaned = re.sub(r"\s+", " ", cleaned)
    cleaned = cleaned.replace(" :", ":").replace(" | |", " |")
    return cleaned.strip()

def sanitize_html_file(file_path: str) -> dict:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    soup = BeautifulSoup(content, "html.parser")
    stats = {
        "share_boxes_removed": 0,
        "emojis_purged": 0,
        "toc_cleaned": False,
        "badges_cleaned": False
    }

    # 1. Remove redundant social share box
    share_boxes = soup.find_all("div", class_=lambda c: c and "ht-social-share-box" in c)
    for box in share_boxes:
        box.decompose()
        stats["share_boxes_removed"] += 1

    # Also search for manual share box paragraphs
    for p in soup.find_all("p"):
        if "আপনার সহপাঠী ও বন্ধুদের সাথে শেয়ার করুন" in p.get_text() or "Share this helpful guide" in p.get_text():
            parent = p.find_parent("div")
            if parent and ("whatsapp.com" in parent.decode() or "facebook.com" in parent.decode()):
                parent.decompose()
                stats["share_boxes_removed"] += 1
            else:
                p.decompose()
                stats["share_boxes_removed"] += 1

    # 2. Clean TOC
    toc_containers = soup.find_all("div", class_=lambda c: c and "ht-toc-container" in c)
    for toc in toc_containers:
        stats["toc_cleaned"] = True
        # Clean title
        title_div = toc.find("div")
        if title_div:
            title_span = title_div.find("span")
            if title_span:
                txt = title_span.get_text()
                if bool(re.search(r'[\u0980-\u09FF]', txt)):
                    title_span.string = "সূচিপত্র (গুরুত্বপূর্ণ বিষয়বস্তু)"
                else:
                    title_span.string = "Table of Contents"

        # Clean list items
        for li in toc.find_all("li"):
            a = li.find("a")
            if a:
                link_text = a.get_text()
                is_h3 = "margin-left" in li.get("style", "") or "↳" in link_text
                clean_link = EMOJI_REGEX.sub("", link_text).replace("👉", "").replace("↳", "").strip()
                prefix = "— " if is_h3 else "• "
                a.string = f"{prefix}{clean_link}"
                # Ensure clean styling
                if is_h3:
                    a["style"] = "color: #475569; text-decoration: none; font-size: 15px; transition: color 0.2s;"
                else:
                    a["style"] = "color: #1d4ed8; text-decoration: none; font-size: 15px; transition: color 0.2s;"

    # 3. Clean meta engagement badges
    badges = soup.find_all("div", class_=lambda c: c and "ht-meta-engagement-badge" in c)
    for badge in badges:
        stats["badges_cleaned"] = True
        for span in badge.find_all("span"):
            span_text = span.get_text()
            if "⏱️" in span_text or "পড়ার আনুমানিক সময়" in span_text or "Estimated Reading Time" in span_text:
                span.string = EMOJI_REGEX.sub("", span_text).replace("পড়ার আনুমানিক সময়", "পড়ার সময়").strip()
            elif "✅" in span_text or "সর্বশেষ হালনাগাদ" in span_text:
                span.string = EMOJI_REGEX.sub("", span_text).replace("সর্বশেষ হালনাগাদ", "সর্বশেষ সংস্করণ:").strip()
            elif "🎓" in span_text:
                span.string = EMOJI_REGEX.sub("", span_text).strip()

    # 4. Global Emoji Purge across all text nodes (headings, callouts, paragraphs)
    # We do not touch <script> or <style> tags
    for tag in soup.find_all(True):
        if tag.name in ["script", "style"]:
            continue
        # Check direct text children
        for child in list(tag.children):
            if child.name is None: # NavigableString
                original_str = str(child)
                if EMOJI_REGEX.search(original_str):
                    stats["emojis_purged"] += len(EMOJI_REGEX.findall(original_str))
                    new_str = clean_text_of_emojis(original_str)
                    child.replace_with(new_str)

    # Convert soup back to string and perform regex polish
    cleaned_html = str(soup)
    # Final pass on any residual raw emoji characters
    final_html = EMOJI_REGEX.sub("", cleaned_html)

    # Save cleaned file
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(final_html)

    return stats

def main():
    target_dirs = [
        os.path.join(PROJECT_ROOT, "output_posts", "new_silo_posts"),
        os.path.join(PROJECT_ROOT, "output_posts", "revived_posts"),
    ]

    total_files = 0
    total_shares = 0
    total_emojis = 0

    print("=" * 75)
    print("🧹 PURGING EMOJIS & REDUNDANT SHARE BOXES ACROSS ALL POSTS")
    print("=" * 75)

    for d in target_dirs:
        if not os.path.exists(d):
            continue
        for f in sorted(os.listdir(d)):
            if f.endswith(".html"):
                path = os.path.join(d, f)
                stats = sanitize_html_file(path)
                total_files += 1
                total_shares += stats["share_boxes_removed"]
                total_emojis += stats["emojis_purged"]
                if stats["share_boxes_removed"] > 0 or stats["emojis_purged"] > 0:
                    print(f"  [Cleaned] {f} -> {stats['share_boxes_removed']} share box(es) removed, {stats['emojis_purged']} emoji(s) purged")

    print("\n" + "=" * 75)
    print(f"🎉 SANITIZATION COMPLETE:")
    print(f"   - Total files processed: {total_files}")
    print(f"   - Redundant share boxes eliminated: {total_shares}")
    print(f"   - Total emojis purged: {total_emojis}")
    print("=" * 75)

if __name__ == "__main__":
    main()
