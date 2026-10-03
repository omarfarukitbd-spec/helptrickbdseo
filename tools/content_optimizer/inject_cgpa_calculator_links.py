#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/content_optimizer/inject_cgpa_calculator_links.py
-------------------------------------------------------
Contextually links the NU CGPA Calculator into high-priority National University
and academic posts via Blogger API v3, with full pre-edit backup (Rule 07).
"""

import os
import sys
import json
import re
from datetime import datetime

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.blogger_publisher.publisher import get_authenticated_service, BLOG_ID

# Target Posts for Internal Linking
TARGET_POSTS = [
    {
        "id": "7901118775212196810",
        "slug": "nu-honours-2nd-year-exam-guide-and",
        "name": "অনার্স ২য় বর্ষ পরীক্ষার গাইড ও প্রমোশনের নিয়মাবলী ২০২৬",
        "hook_text": "জাতীয় বিশ্ববিদ্যালয়ের অনার্স ২য় বর্ষ থেকে ৩য় বর্ষে প্রমোশনের জন্য ন্যূনতম জিপিএ ও ক্রেডিট অর্জনের শর্তাবলী যাচাইয়ের পাশাপাশি"
    },
    {
        "id": "1085826635177863206",
        "slug": "nu-honours-2nd-year-exam-routine-2026",
        "name": "অনার্স ২য় বর্ষ পরীক্ষার রুটিন ২০২৬",
        "hook_text": "পরীক্ষার চূড়ান্ত প্রস্তুতির পাশাপাশি আপনার কাঙ্ক্ষিত জিপিএ ও ৪ বছরের সামগ্রিক সিজিপিএ পরিকল্পনা করতে"
    },
    {
        "id": "3467234920665395308",
        "slug": "nu-degree-2nd-year-in-course-and-exam",
        "name": "ডিগ্রি ২য় বর্ষ ইনকোর্স ও পরীক্ষার গাইড ২০২৬",
        "hook_text": "ডিগ্রি (পাস) কোর্সের ইনকোর্স ও তত্ত্বীয় পরীক্ষার সম্মিলিত ফলাফল এবং ৩ বছরের সিজিপিএ নির্ভুলভাবে হিসাব করতে"
    },
    {
        "id": "4710432391315087780",
        "slug": "honours-political-science-book-list",
        "name": "রাষ্ট্রবিজ্ঞান অনার্স পাঠ্য বইয়ের তালিকা ও বিষয় কোড",
        "hook_text": "রাষ্ট্রবিজ্ঞান বিভাগের সকল বর্ষের কোর্স কোড অনুযায়ী সরাসরি বিষয়ভিত্তিক সিলেবাস লোড ও গ্রেড পয়েন্ট হিসাব করতে"
    },
    {
        "id": "7338193345529576604",
        "slug": "nu-exam-digitization-aqa-global-mou-2026",
        "name": "জাতীয় বিশ্ববিদ্যালয়ের পরীক্ষা ডিজিটালাইজেশন ও মূল্যায়ন সংস্কার",
        "hook_text": "জাতীয় বিশ্ববিদ্যালয়ের নতুন ডিজিটালাইজড ৪.০০ ক্রেডিট-ওয়েটেড গ্রেডিং সিস্টেম অনুযায়ী নিজের ফলাফল মূল্যায়ন করতে"
    },
    {
        "id": "7170314718157313108",
        "slug": "recent-political-thought-suggestion-2024",
        "name": "রাষ্ট্রবিজ্ঞান মাস্টার্স সাজেশন্স: সাম্প্রতিক রাষ্ট্রচিন্তা",
        "hook_text": "মাস্টার্স পরীক্ষার কাঙ্ক্ষিত সিজিপিএ (ফার্স্ট ক্লাস ৩.০০) অর্জন নিশ্চিত করতে এবং আপনার বর্তমান ফলাফল পর্যালোচনা করতে"
    },
    {
        "id": "96563581694548240",
        "slug": "political-science-masters-exam-2022-all-short-questions-and-answers",
        "name": "রাষ্ট্রবিজ্ঞান মাস্টার্স পরীক্ষা ক বিভাগের প্রশ্নোত্তর",
        "hook_text": "মাস্টার্স ফাইনাল পরীক্ষার গ্রেড পয়েন্ট ও সামগ্রিক ফলাফল মূল্যায়নের জন্য"
    },
    {
        "id": "8675903395059439252",
        "slug": "how-to-correction-certificate-name-2025",
        "name": "ঢাকা শিক্ষাবোর্ডে সার্টিফিকেট নাম ও বয়স সংশোধন গাইড",
        "hook_text": "সনদ বা সার্টিফিকেটের গ্রেড ও জিপিএ মূল্যায়নের সুবিধার্থে"
    }
]

def make_callout_box(hook_text):
    return f"""
<div class="htbd-link-box" style="margin: 26px 0; padding: 18px 22px; background: #f0fdf4; border-left: 5px solid #16a34a; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.04);">
  <strong style="color: #15803d; font-size: 16px; display: block; margin-bottom: 6px;">[শিক্ষার্থীদের জন্য বিশেষ অ্যাকাডেমিক টুল]:</strong>
  <p style="margin: 0; font-size: 15.5px; color: #1e293b; line-height: 1.65;">
    {hook_text} ব্যবহার করুন আমাদের স্বয়ংক্রিয় 
    <a href="https://www.helptrickbd.com/p/nu-cgpa-calculator.html" style="color: #1e40af; font-weight: 700; text-decoration: underline;" title="জাতীয় বিশ্ববিদ্যালয় সিজিপিএ ক্যালকুলেটর ও গ্রেডিং গাইড ২০২৬">জাতীয় বিশ্ববিদ্যালয় সিজিপিএ ক্যালকুলেটর ও গ্রেডিং গাইড ২০২৬</a>। এতে রয়েছে সরাসরি সিলেবাস অটো-লোড, রেজাল্ট পেস্ট পার্সার, টার্গেট ফার্স্ট ক্লাস প্ল্যানার ও ১-পাতা প্রাতিষ্ঠানিক গ্রেড রিপোর্ট প্রিন্ট সুবিধা।
  </p>
</div>
"""

def backup_post(slug, post_obj):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_dir = os.path.join(PROJECT_ROOT, "backups", "posts", slug, timestamp)
    os.makedirs(backup_dir, exist_ok=True)

    with open(os.path.join(backup_dir, "post_snapshot.json"), "w", encoding="utf-8") as f:
        json.dump(post_obj, f, ensure_ascii=False, indent=2)

    with open(os.path.join(backup_dir, "content_original.html"), "w", encoding="utf-8") as f:
        f.write(post_obj.get("content", ""))

    print(f"    [BACKUP CREATED] -> backups/posts/{slug}/{timestamp}/")
    return backup_dir

def inject_callout_into_html(html, callout_box):
    # If already linked, skip
    if "nu-cgpa-calculator.html" in html:
        return None, "Already linked"

    # Best insertion point: Right after the first <h2> section or before the first table/H2
    # Or right after the Quick Overview box (htbd-qbox)
    qbox_match = re.search(r'(</div>\s*<!--\s*TOC|</div>\s*<div class="htbd-toc-box")', html, re.IGNORECASE)
    if qbox_match:
        idx = qbox_match.start()
        new_html = html[:idx] + callout_box + "\n" + html[idx:]
        return new_html, "Inserted before TOC"

    # Alternative: Before the first <h2> tag
    h2_match = re.search(r'(<h2\b)', html, re.IGNORECASE)
    if h2_match:
        idx = h2_match.start()
        new_html = html[:idx] + callout_box + "\n" + html[idx:]
        return new_html, "Inserted before first H2"

    # Fallback: Before conclusion or related links box
    footer_match = re.search(r'(<div class="htbd-link-box"|<div class="htbd-author-card"|<!--\s*Author)', html, re.IGNORECASE)
    if footer_match:
        idx = footer_match.start()
        new_html = html[:idx] + callout_box + "\n" + html[idx:]
        return new_html, "Inserted before footer cards"

    # Absolute fallback: append to end
    return html + "\n" + callout_box, "Appended to end"

def main():
    service = get_authenticated_service()
    if not service:
        print("[ERROR] Blogger API Authentication Failed.")
        return False

    print("=" * 70)
    print("🚀 INJECTING NU CGPA CALCULATOR INTERNAL LINKS VIA BLOGGER API V3")
    print("=" * 70)

    updated_count = 0
    skipped_count = 0

    for item in TARGET_POSTS:
        post_id = item["id"]
        slug = item["slug"]
        name = item["name"]
        hook = item["hook_text"]

        print(f"\n[*] Processing: {name} (ID: {post_id})")

        try:
            post = service.posts().get(blogId=BLOG_ID, postId=post_id).execute()
        except Exception as e:
            print(f"    [ERROR] Failed to fetch post {post_id}: {e}")
            continue

        orig_content = post.get("content", "")
        if "nu-cgpa-calculator.html" in orig_content:
            print(f"    [SKIP] Already contains link to nu-cgpa-calculator.html")
            skipped_count += 1
            continue

        # 1. Mandatory Pre-Edit Backup (Rule 07)
        backup_post(slug, post)

        # 2. Inject Callout Box
        callout_html = make_callout_box(hook)
        updated_content, strategy = inject_callout_into_html(orig_content, callout_html)

        if not updated_content or updated_content == orig_content:
            print(f"    [SKIP] Could not inject: {strategy}")
            skipped_count += 1
            continue

        # 3. Patch Post via Blogger API v3
        print(f"    [PATCHING] Strategy: {strategy} (Length: {len(orig_content)} -> {len(updated_content)})")
        patch_body = {
            "content": updated_content
        }

        try:
            res = service.posts().patch(blogId=BLOG_ID, postId=post_id, body=patch_body).execute()
            print(f"    [SUCCESS] Post updated live! URL: {res.get('url')}")
            updated_count += 1
        except Exception as e:
            print(f"    [ERROR] Failed to patch post {post_id}: {e}")

    print("\n" + "=" * 70)
    print(f"SUMMARY: Successfully Updated: {updated_count} | Skipped: {skipped_count} | Total: {len(TARGET_POSTS)}")
    print("=" * 70)
    return True

if __name__ == "__main__":
    main()
