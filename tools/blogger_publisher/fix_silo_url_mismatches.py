#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/blogger_publisher/fix_silo_url_mismatches.py
---------------------------------------------------
Fixes URL mismatches in:
1. The Pillar Post (silo series links)
2. All 5 Silo Posts (series nav links to each other)

Blogger truncated long slugs. Correct URL mapping:
  -summary-writing.html       → -summary.html
  -rules-solution.html        → -rearrange.html
  -question-answer-guide.html → -question.html
  -dialogue-suggestion.html   → -completing-story.html
"""

import os, sys, json, time

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

RAW_POSTS_DIR = os.path.join(PROJECT_ROOT, "scratch", "raw_posts")

from tools.blogger_publisher.publisher import get_authenticated_service, BLOG_ID

BLOG_BASE = "https://www.helptrickbd.com/2026/09"

# ─── URL corrections (old → new) ────────────────────────────────────────────
URL_FIXES = {
    f"{BLOG_BASE}/ssc-2027-english-unseen-passage-summary-writing.html":
        f"{BLOG_BASE}/ssc-2027-english-unseen-passage-summary.html",
    f"{BLOG_BASE}/ssc-2027-english-matching-rearrange-rules-solution.html":
        f"{BLOG_BASE}/ssc-2027-english-matching-rearrange.html",
    f"{BLOG_BASE}/ssc-2027-english-poems-stories-question-answer-guide.html":
        f"{BLOG_BASE}/ssc-2027-english-poems-stories-question.html",
    f"{BLOG_BASE}/ssc-2027-english-completing-story-dialogue-suggestion.html":
        f"{BLOG_BASE}/ssc-2027-english-completing-story.html",
}

# ─── Post IDs ────────────────────────────────────────────────────────────────
PILLAR_POST_ID    = "5652005814898036993"
SILO_POST_IDS = {
    "ssc_2027_silo_01_seen_passage":      ("6338741433469034454", "ssc-2027-english-seen-passage-suggestion"),
    "ssc_2027_silo_02_unseen_summary":    ("7053633278573752071", "ssc-2027-english-unseen-passage-summary-writing"),
    "ssc_2027_silo_03_matching_rearrange":("7415763963240393114", "ssc-2027-english-matching-rearrange-rules-solution"),
    "ssc_2027_silo_04_poems_stories":     ("1093847854655422506", "ssc-2027-english-poems-stories-question-answer-guide"),
    "ssc_2027_silo_05_story_dialogue":    ("4013582929893307058", "ssc-2027-english-completing-story-dialogue-suggestion"),
}

# ─── Pillar post HTML path ────────────────────────────────────────────────────
PILLAR_HTML = os.path.join(PROJECT_ROOT, "scratch", "raw_posts", "ssc_2027_english_1st_paper_pillar.html")


def apply_url_fixes(content):
    """Replace all wrong URLs with correct ones."""
    fixed = content
    count = 0
    for wrong, correct in URL_FIXES.items():
        if wrong in fixed:
            fixed = fixed.replace(wrong, correct)
            count += 1
    return fixed, count


def fix_pillar_post(service):
    """Fix silo links in the live Pillar Post."""
    print("\n[*] Fixing Pillar Post silo links...")

    # Fetch live pillar content
    live = service.posts().get(blogId=BLOG_ID, postId=PILLAR_POST_ID,
                                fields="content,title,labels").execute()
    original_content = live.get("content", "")
    fixed_content, num_fixes = apply_url_fixes(original_content)

    if num_fixes == 0:
        print("  [OK] Pillar Post: No URL fixes needed (already correct).")
        return True

    print(f"  [*] Applied {num_fixes} URL fixes to Pillar Post.")
    patch = {"content": fixed_content}
    service.posts().patch(blogId=BLOG_ID, postId=PILLAR_POST_ID, body=patch).execute()
    print("  [OK] Pillar Post updated successfully!")

    # Also fix local HTML file if it exists
    if os.path.exists(PILLAR_HTML):
        with open(PILLAR_HTML, 'r', encoding='utf-8') as f:
            local_content = f.read()
        fixed_local, _ = apply_url_fixes(local_content)
        with open(PILLAR_HTML, 'w', encoding='utf-8') as f:
            f.write(fixed_local)
        print(f"  [OK] Local pillar HTML also updated.")

    time.sleep(2)
    return True


def fix_silo_posts(service):
    """Fix series nav links in all 5 silo posts."""
    print("\n[*] Fixing series nav links in silo posts...")

    for file_prefix, (post_id, slug) in SILO_POST_IDS.items():
        print(f"\n  [*] {slug}")

        # Fix local HTML file
        html_path = os.path.join(RAW_POSTS_DIR, f"{file_prefix}.html")
        if os.path.exists(html_path):
            with open(html_path, 'r', encoding='utf-8') as f:
                local_html = f.read()
            fixed_html, count = apply_url_fixes(local_html)
            if count > 0:
                with open(html_path, 'w', encoding='utf-8') as f:
                    f.write(fixed_html)
                print(f"  [OK] Local HTML: {count} URLs fixed.")
            else:
                print(f"  [OK] Local HTML: No fixes needed.")
        else:
            fixed_html = None
            print(f"  [!] Local HTML not found: {html_path}")

        # Fix live post via API
        try:
            live = service.posts().get(blogId=BLOG_ID, postId=post_id,
                                        fields="content,title,labels").execute()
            live_content = live.get("content", "")
            fixed_live, count = apply_url_fixes(live_content)

            if count > 0:
                service.posts().patch(blogId=BLOG_ID, postId=post_id,
                                       body={"content": fixed_live}).execute()
                print(f"  [OK] Live post updated: {count} URLs fixed.")
            else:
                print(f"  [OK] Live post: No fixes needed.")

        except Exception as e:
            print(f"  [!] API error for {slug}: {e}")

        time.sleep(2)

    return True


def main():
    print("=" * 65)
    print("SSC 2027 SILO SERIES — URL MISMATCH FIXER")
    print("=" * 65)
    print("\nURL Fixes to apply:")
    for wrong, correct in URL_FIXES.items():
        wrong_slug = wrong.split("/")[-1]
        correct_slug = correct.split("/")[-1]
        print(f"  {wrong_slug}")
        print(f"  → {correct_slug}")

    service = get_authenticated_service()
    if not service:
        print("[ERROR] Auth failed!")
        sys.exit(1)
    print("\n[OK] Authenticated.")

    fix_pillar_post(service)
    fix_silo_posts(service)

    print("\n" + "=" * 65)
    print("URL fix complete! All silo links now point to correct URLs.")
    print("=" * 65)


if __name__ == "__main__":
    main()
