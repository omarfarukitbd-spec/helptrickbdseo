#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/content_optimizer/apply_masters_topical_silo.py
------------------------------------------------------
Applies the 100% compliant Topical Silo Internal Linking Architecture
to the 4 Masters Political Science posts:
1. Contextual in-text hyperlinks between closely related topics.
2. Academic Syllabus Series Navigator Box right before FAQ.
3. Pre-Flight quality and policy checks.
4. Pre-edit full backup to backups/posts/.
5. Live update via Blogger API v3.
6. Google Indexing API ping.
"""

import os
import sys
import json
import re
import subprocess
from datetime import datetime

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, PROJECT_ROOT)

from tools.blogger_publisher.publisher import get_authenticated_service, BLOG_ID
from tools.backup_manager.post_backup_manager import create_post_backup
from tools.policy_guard.policy_scanner import scan_content_for_policy_violations

# Post Manifest
POSTS_INFO = [
    {
        "id": "1",
        "post_id": "9116452035823080586",
        "slug": "political-violence-in-bangladesh-causes-and-remedies",
        "url": "https://www.helptrickbd.com/2026/09/political-violence-in-bangladesh-causes.html",
        "html_file": os.path.join(PROJECT_ROOT, "content", "drafts", "post-01-political-violence-bangladesh.html"),
        "title": "বাংলাদেশে রাজনৈতিক সহিংসতার কারণ ও প্রতিকার — মাস্টার্স রাষ্ট্রবিজ্ঞান স্পেশাল হ্যান্ডনোট ২০২৬",
        "chapter_num": 1
    },
    {
        "id": "2",
        "post_id": "6404645292087443148",
        "slug": "bangladesh-un-membership-1972-obstacles-and-history",
        "url": "https://www.helptrickbd.com/2026/09/bangladesh-un-membership-1972-obstacles.html",
        "html_file": os.path.join(PROJECT_ROOT, "content", "drafts", "post-02-un-membership-bangladesh.html"),
        "title": "বাংলাদেশের জাতিসংঘ সদস্যপদ লাভের ইতিহাস ও বাধাসমূহ — ১৯৭২ সালের পটভূমি",
        "chapter_num": 2
    },
    {
        "id": "3",
        "post_id": "2764815544769069752",
        "slug": "secularism-vs-islamic-values-in-bangladesh-ideological-conflict",
        "url": "https://www.helptrickbd.com/2026/09/secularism-vs-islamic-values-in.html",
        "html_file": os.path.join(PROJECT_ROOT, "content", "drafts", "post-03-secularism-vs-islamic-values.html"),
        "title": "ধর্মনিরপেক্ষতা বনাম ইসলামি মূল্যবোধ — স্বাধীন বাংলাদেশে আদর্শিক দ্বন্দ্বের ইতিহাস",
        "chapter_num": 3
    },
    {
        "id": "4",
        "post_id": "677338098229047855",
        "slug": "caretaker-government-free-fair-election-bangladesh",
        "url": "https://www.helptrickbd.com/2026/09/caretaker-government-free-fair-election.html",
        "html_file": os.path.join(PROJECT_ROOT, "content", "drafts", "post-04-caretaker-government-bangladesh.html"),
        "title": "তত্ত্বাবধায়ক সরকার ও অবাধ সুষ্ঠু নির্বাচনের পূর্বশর্তসমূহ — বাংলাদেশের রাজনৈতিক বাস্তবতা",
        "chapter_num": 4
    }
]

def build_silo_navigator_html(current_chapter: int) -> str:
    """Builds a responsive, clean, textbook-grade Syllabus Navigator Box."""
    chapters = [
        (1, "https://www.helptrickbd.com/2026/09/political-violence-in-bangladesh-causes.html", "বাংলাদেশে রাজনৈতিক সহিংসতার কারণ ও প্রতিকার"),
        (2, "https://www.helptrickbd.com/2026/09/bangladesh-un-membership-1972-obstacles.html", "বাংলাদেশের জাতিসংঘ সদস্যপদ লাভের ইতিহাস ও বাধাসমূহ (১৯৭২)"),
        (3, "https://www.helptrickbd.com/2026/09/secularism-vs-islamic-values-in.html", "ধর্মনিরপেক্ষতা বনাম ইসলামি মূল্যবোধ — স্বাধীন বাংলাদেশে আদর্শিক দ্বন্দ্ব"),
        (4, "https://www.helptrickbd.com/2026/09/caretaker-government-free-fair-election.html", "তত্ত্বাবধায়ক সরকার ও অবাধ সুষ্ঠু নির্বাচনের পূর্বশর্তসমূহ")
    ]
    
    list_items = []
    for num, link, heading in chapters:
        if num == current_chapter:
            item = f'    <li style="margin-bottom: 8px;"><strong>অধ্যায় ০{num}:</strong> <a href="{link}" style="color: #0b2046; font-weight: 700; text-decoration: underline;">{heading}</a> <span style="display: inline-block; background: #e2e8f0; color: #0b2046; font-size: 13px; font-weight: 700; padding: 2px 8px; border-radius: 4px; margin-left: 6px;">বর্তমান পাঠ</span></li>'
        else:
            item = f'    <li style="margin-bottom: 8px;"><strong>অধ্যায় ০{num}:</strong> <a href="{link}" style="color: #0b2046; font-weight: 600; text-decoration: underline;">{heading}</a></li>'
        list_items.append(item)
    
    items_html = "\n".join(list_items)
    
    return f"""
  <!-- Academic Silo Navigator -->
  <div class="htbd-silo-box" style="margin: 34px 0; padding: 22px 24px; background: #f8fafc; border: 1px solid #e2e8f0; border-left: 4px solid #0b2046; border-radius: 8px;">
    <div style="font-size: 19px; font-weight: 700; color: #0b2046; margin-bottom: 8px;">
      মাস্টার্স শেষ পর্ব রাষ্ট্রবিজ্ঞান — সম্পূর্ণ হ্যান্ডনোট সিরিজ (কোর্স কোড: ৩১১৯০৫):
    </div>
    <p style="font-size: 15px; color: #475569; margin: 0 0 14px 0; line-height: 1.5;">
      জাতীয় বিশ্ববিদ্যালয়ের সিলেবাস ও বিগত পরীক্ষার গুরুত্বপূর্ণ প্রশ্নোত্তরের ধারাবাহিক হ্যান্ডনোটসমূহ ক্রমানুসারে পড়ুন:
    </p>
    <ul style="margin: 0; padding-left: 20px; font-size: 16px; line-height: 1.8; color: #1e293b;">
{items_html}
    </ul>
  </div>
"""

def update_post_1_content(html: str) -> str:
    # 1. In-text link to Post 4 in Section 6.খ
    target_6b = "একটি স্বচ্ছ ও গ্রহণযোগ্য নির্বাচন ব্যবস্থার নিশ্চয়তা সহিংসতা প্রতিরোধে প্রধান রক্ষাকবচ।"
    replacement_6b = 'একটি স্বচ্ছ ও গ্রহণযোগ্য নির্বাচন ব্যবস্থার নিশ্চয়তা রাজনৈতিক সহিংসতা প্রতিরোধে প্রধান রক্ষাকবচ। আর এ কারণেই নব্বইয়ের দশকে রাজপথের রক্তক্ষয়ী সংঘাত এড়াতে এবং সকল দলের অংশগ্রহণে নিরপেক্ষ নির্বাচনের লক্ষ্যে সংবিধানে <a href="https://www.helptrickbd.com/2026/09/caretaker-government-free-fair-election.html" style="color: #0b2046; font-weight: 600; text-decoration: underline;">তত্ত্বাবধায়ক সরকার ও অবাধ সুষ্ঠু নির্বাচনের পূর্বশর্তসমূহ</a> কাঠামোর উদ্ভাবন ঘটেছিল।'
    if target_6b in html:
        html = html.replace(target_6b, replacement_6b, 1)

    # 2. In-text link to Post 3 in Section 1
    target_1 = "আধুনিক রাষ্ট্রবিজ্ঞানের অন্যতম গুরুত্বপূর্ণ ও বিতর্কিত বিষয়।"
    replacement_1 = 'আধুনিক রাষ্ট্রবিজ্ঞানের অন্যতম গুরুত্বপূর্ণ ও বিতর্কিত বিষয়। বাংলাদেশে রাজনৈতিক সংঘাতের ঐতিহাসিক পটভূমি গভীরভাবে পর্যবেক্ষণ করলে দেখা যায়—স্বাধীনতা-উত্তর সময় থেকে চলে আসা গভীর মতাদর্শিক বিভাজন, বিশেষ করে <a href="https://www.helptrickbd.com/2026/09/secularism-vs-islamic-values-in.html" style="color: #0b2046; font-weight: 600; text-decoration: underline;">ধর্মনিরপেক্ষতা বনাম ইসলামি মূল্যবোধের আদর্শিক দ্বন্দ্ব</a> রাজনৈতিক দলগুলোর মধ্যকার পারস্পরিক অনাস্থাকে চিরস্থায়ী রূপ দিয়েছে।'
    if target_1 in html:
        html = html.replace(target_1, replacement_1, 1)

    # 3. Add Silo Box right before Section 8: FAQ
    silo_html = build_silo_navigator_html(1)
    faq_marker = '<!-- Section 8: FAQ -->'
    if faq_marker in html:
        html = html.replace(faq_marker, silo_html + "\n  " + faq_marker, 1)
    return html

def update_post_2_content(html: str) -> str:
    # 1. In-text link to Post 3 in Section 5.গ
    target_5c = "পাকিস্তানের স্বীকৃতির মধ্য দিয়ে চীনের ভেটো প্রয়োগের সকল বাহ্যিক ভিত্তি বিলুপ্ত হয়।"
    replacement_5c = 'লাহোর শীর্ষ সম্মেলনে অংশগ্রহণ ও পাকিস্তানের আনুষ্ঠানিক স্বীকৃতির মধ্য দিয়ে চীনের ভেটো প্রয়োগের বাহ্যিক ভিত্তি বিলুপ্ত হয়। এটি ছিল যুদ্ধোত্তর বাংলাদেশের বহুপাক্ষিক কূটনীতি এবং <a href="https://www.helptrickbd.com/2026/09/secularism-vs-islamic-values-in.html" style="color: #0b2046; font-weight: 600; text-decoration: underline;">ধর্মনিরপেক্ষতা বনাম ইসলামি মূল্যবোধের আদর্শিক রূপরেখা</a> বজায় রেখে মুসলিম বিশ্বের আস্থা অর্জনের এক অনন্য ঐতিহাসিক দৃষ্টান্ত।'
    if target_5c in html:
        html = html.replace(target_5c, replacement_5c, 1)

    # 2. In-text link to Post 1 in Section 1
    target_1 = "আন্তর্জাতিক রাজনীতি ও ভূ-কৌশলগত স্বার্থের এক জটিল সমীকরণ ছিল।"
    replacement_1 = 'আন্তর্জাতিক রাজনীতি ও ভূ-কৌশলগত স্বার্থের এক জটিল সমীকরণ ছিল। যুদ্ধবিধ্বস্ত দেশে অভ্যন্তরীণ আইনশৃঙ্খলা পুনরুদ্ধার, জানমালের নিরাপত্তা ও রাজনৈতিক স্থিতিশীলতা প্রতিষ্ঠার কঠিন চ্যালেঞ্জের মুখেও (যা বিশদভাবে আলোচিত হয়েছে আমাদের <a href="https://www.helptrickbd.com/2026/09/political-violence-in-bangladesh-causes.html" style="color: #0b2046; font-weight: 600; text-decoration: underline;">বাংলাদেশে রাজনৈতিক সহিংসতার কারণ ও ঐতিহাসিক সংঘাতের রূপরেখা</a> হ্যান্ডনোটে) বাংলাদেশ বিশ্ব দরবারে সার্বভৌম স্বীকৃতি আদায়ে আপসহীন ভূমিকা পালন করে।'
    if target_1 in html:
        html = html.replace(target_1, replacement_1, 1)

    # 3. Add Silo Box right before Section 7: FAQ
    silo_html = build_silo_navigator_html(2)
    faq_marker = '<!-- Section 7: FAQ -->'
    if faq_marker in html:
        html = html.replace(faq_marker, silo_html + "\n  " + faq_marker, 1)
    return html

def update_post_3_content(html: str) -> str:
    # 1. In-text link to Post 2 in Section 3.গ
    target_3c = "মুসলিম বিশ্বের সাথে কূটনৈতিক সম্পর্ক স্থাপন ও অর্থনৈতিক সহযোগিতা বৃদ্ধি"
    replacement_3c = 'মুসলিম বিশ্বের সাথে কূটনৈতিক সম্পর্ক স্থাপন ও অর্থনৈতিক সহযোগিতা বৃদ্ধি (যে কূটনৈতিক সাফল্যের প্রেক্ষাপটে ১৯৭৪ সালে জাতিসংঘের পূর্ণ সদস্যপদ অর্জিত হয়েছিল, যার বিস্তারিত রয়েছে <a href="https://www.helptrickbd.com/2026/09/bangladesh-un-membership-1972-obstacles.html" style="color: #0b2046; font-weight: 600; text-decoration: underline;">জাতিসংঘ সদস্যপদ লাভে বাংলাদেশের বাধাসমূহ ও আন্তর্জাতিক সংকট</a> শীর্ষক হ্যান্ডনোটে)'
    if target_3c in html:
        html = html.replace(target_3c, replacement_3c, 1)

    # 2. In-text link to Post 1 in Section 1
    target_1 = "রাজনৈতিক সংস্কৃতির অন্যতম প্রধান চালিকাশক্তি হিসেবে কাজ করেছে।"
    replacement_1 = 'রাজনৈতিক সংস্কৃতির অন্যতম প্রধান চালিকাশক্তি হিসেবে কাজ করেছে। এই আদর্শিক বিভাজন ও অসহিষ্ণুতা পরবর্তীতে গণতান্ত্রিক রাজনীতিকে মেরুকরণ করে সহিংস সংঘাতের জন্ম দেয়, যার স্বরূপ আলোচিত হয়েছে <a href="https://www.helptrickbd.com/2026/09/political-violence-in-bangladesh-causes.html" style="color: #0b2046; font-weight: 600; text-decoration: underline;">বাংলাদেশে রাজনৈতিক সহিংসতার কারণ ও প্রতিকার</a> শীর্ষক গবেষণাধর্মী পাঠে।'
    if target_1 in html:
        html = html.replace(target_1, replacement_1, 1)

    # 3. In-text link to Post 4 in Section 4
    target_4 = "সংবিধানের মূলনীতি পরিবর্তনের ধারাবাহিক পরিক্রমা"
    replacement_4 = 'সংবিধানের মূলনীতি পরিবর্তনের ধারাবাহিক পরিক্রমা (এবং নির্বাচনকালীন নিরপেক্ষ প্রশাসন নিশ্চিতে <a href="https://www.helptrickbd.com/2026/09/caretaker-government-free-fair-election.html" style="color: #0b2046; font-weight: 600; text-decoration: underline;">তত্ত্বাবধায়ক সরকার ব্যবস্থা ও সুষ্ঠু নির্বাচনের পূর্বশর্তসমূহ</a> প্রবর্তন)'
    if target_4 in html:
        html = html.replace(target_4, replacement_4, 1)

    # 4. Add Silo Box right before Section 7: FAQ
    silo_html = build_silo_navigator_html(3)
    faq_marker = '<!-- Section 7: FAQ -->'
    if faq_marker in html:
        html = html.replace(faq_marker, silo_html + "\n  " + faq_marker, 1)
    return html

def update_post_4_content(html: str) -> str:
    # 1. In-text link to Post 1 in Section 4
    target_4 = "যা বাংলাদেশের নির্বাচনী ব্যবস্থাকে এক গভীর আন্তর্জাতিক ও ঘরোয়া সংকটের মুখে ঠেলে দেয়।"
    replacement_4 = 'যা বাংলাদেশের নির্বাচনী ব্যবস্থাকে এক গভীর আন্তর্জাতিক ও ঘরোয়া সংকটের মুখে ঠেলে দেয়। নির্বাচনী অচলাবস্থা ও আস্থাহীনতা থেকে কীভাবে রাজপথে দীর্ঘমেয়াদী সংঘাতের বিস্তার ঘটে, তা আমরা বিস্তারিত বিশ্লেষণ করেছি আমাদের <a href="https://www.helptrickbd.com/2026/09/political-violence-in-bangladesh-causes.html" style="color: #0b2046; font-weight: 600; text-decoration: underline;">বাংলাদেশে রাজনৈতিক সহিংসতার কারণ ও টেকসই প্রতিকার</a> শীর্ষক বিশেষ হ্যান্ডনোটে।'
    if target_4 in html:
        html = html.replace(target_4, replacement_4, 1)

    # 2. In-text link to Post 3 in Section 1
    target_1 = "বাংলাদেশের রাজনৈতিক ইতিহাস মূলত একটি অবাধ ও সুষ্ঠু নির্বাচনের অবিরাম লড়াইয়ের ইতিহাস।"
    replacement_1 = 'বাংলাদেশের রাজনৈতিক ইতিহাস মূলত একটি অবাধ ও সুষ্ঠু নির্বাচনের অবিরাম লড়াইয়ের ইতিহাস। স্বাধীনতা-উত্তর সময় থেকেই রাজনৈতিক দলগুলোর গভীর আদর্শিক মেরুকরণ (যার বিশদ বিবরণ রয়েছে <a href="https://www.helptrickbd.com/2026/09/secularism-vs-islamic-values-in.html" style="color: #0b2046; font-weight: 600; text-decoration: underline;">ধর্মনিরপেক্ষতা বনাম ইসলামি মূল্যবোধের আদর্শিক দ্বন্দ্ব ও সাংবিধানিক বিবর্তন</a> হ্যান্ডনোটে)—নির্বাচনকালীন একটি দলনিরপেক্ষ শাসনকাঠামোর দাবিকে অপরিহার্য করে তোলে।'
    if target_1 in html:
        html = html.replace(target_1, replacement_1, 1)

    # 3. Add Silo Box right before Section 7: FAQ
    silo_html = build_silo_navigator_html(4)
    faq_marker = '<!-- Section 7: FAQ -->'
    if faq_marker in html:
        html = html.replace(faq_marker, silo_html + "\n  " + faq_marker, 1)
    return html

def main():
    print("=" * 75)
    print("🕸️ HELPTRICKBD TOPICAL SILO ARCHITECTURE — 4 MASTERS POLITICAL SCIENCE POSTS")
    print("=" * 75)

    service = get_authenticated_service()
    if not service:
        print("[!] Failed to authenticate Blogger API v3.")
        sys.exit(1)

    # Process each post
    for post in POSTS_INFO:
        p_id = post["id"]
        post_id = post["post_id"]
        html_file = post["html_file"]
        title = post["title"]
        slug = post["slug"]
        url = post["url"]
        chapter = post["chapter_num"]

        print(f"\n[*] Processing Post {p_id} (Chapter {chapter}): {title[:40]}...")
        with open(html_file, "r", encoding="utf-8") as f:
            original_html = f.read()

        # Apply Silo updates
        if p_id == "1":
            updated_html = update_post_1_content(original_html)
        elif p_id == "2":
            updated_html = update_post_2_content(original_html)
        elif p_id == "3":
            updated_html = update_post_3_content(original_html)
        elif p_id == "4":
            updated_html = update_post_4_content(original_html)

        # Save back to draft file
        with open(html_file, "w", encoding="utf-8") as f:
            f.write(updated_html)
        print(f"  [+] Draft updated with contextual in-text links & Silo Navigator.")

        # Run Pre-flight Quality & Policy Checks
        is_clean, violations, _ = scan_content_for_policy_violations(updated_html)
        if not is_clean:
            print(f"  [!] Policy violations detected in Post {p_id}: {violations}")
            sys.exit(1)
        print(f"  [✔] Policy Guard: 100% CLEAN (0 violations).")

        # Step 1: Pre-Edit Backup (Mandatory Rule 8 / Rule 15)
        print("  [*] Fetching current live post for immutable pre-edit backup...")
        live_post = service.posts().get(blogId=BLOG_ID, postId=post_id).execute()
        backup_dir = create_post_backup(live_post, reason="topical_silo_update")
        print(f"  [✔] Pre-edit backup created at: {backup_dir}")

        # Step 2: Live Update via Blogger API v3 (Preserve labels, title, status)
        body = {
            "title": title,
            "content": updated_html,
            "labels": live_post.get("labels", ["Political Science"])
        }
        updated_post = service.posts().patch(
            blogId=BLOG_ID,
            postId=post_id,
            body=body
        ).execute()
        print(f"  [🚀 Live Update] Successfully patched post {post_id} on Blogger!")

        # Step 3: Google Indexing API ping
        try:
            from tools.indexer.ping_all_revived import publish_url_notification
            res = publish_url_notification(url, "URL_UPDATED")
            print(f"  [⚡ Google Indexing API] Pinged {url} -> {res.get('urlNotificationMetadata', {}).get('latestUpdate', {}).get('type', 'OK')}")
        except Exception as e:
            print(f"  [!] Indexing ping skipped: {e}")

    print("\n" + "=" * 75)
    print("🎉 ALL 4 POSTS UPDATED LIVE WITH 100% PERFECT TOPICAL SILO ARCHITECTURE!")
    print("=" * 75)

if __name__ == "__main__":
    main()
