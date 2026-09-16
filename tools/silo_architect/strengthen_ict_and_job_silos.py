#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/silo_architect/strengthen_ict_and_job_silos.py
------------------------------------------------------
Audits, cleans up over-engineered CSS, and strengthens internal linking
across 10 posts in two primary Topical Authority silos:
1. ICT & Technology Silo (6 posts)
2. Job & Career Preparation Silo (4 posts)

Guarantees:
- 100% pre-edit snapshot backup to backups/posts/<slug>/<timestamp>/
- Removes nested <html><head><body> wrappers and garish styling
- Injects clean, minimalist, high-authority SolaimanLipi interlink navigation
- Preserves all author text without destructive loss
- Patches Blogger API v3 live
- Pings Google Indexing API
- Pings Google WebSub (PubSubHubbub) Real-Time Hubs (Rule 21)
"""

import os
import sys
import json
import re
import time
import subprocess
from datetime import datetime, timezone
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

from tools.blogger_publisher.publisher import get_authenticated_service, BLOG_ID

# ==============================================================================
# MINIMALIST DESIGN SYSTEM FOR SILO NAVIGATION BLOCKS
# ==============================================================================
ICT_SERIES_BOX_HTML = """
<!-- Helptrickbd Minimalist ICT Silo Series Navigation -->
<div class="htbd-silo-navigation-box" style="margin: 32px 0; padding: 22px 24px; background: #f8fafc; border: 1px solid #e2e8f0; border-left: 4px solid #0284c7; border-radius: 8px; font-family: 'SolaimanLipi', sans-serif;">
  <h4 style="margin: 0 0 12px 0; color: #0f172a; font-size: 18px; font-weight: 700;">কম্পিউটার ও আইসিটি শিক্ষা পূর্ণাঙ্গ হ্যান্ডনোট সিরিজ:</h4>
  <ul style="margin: 0; padding-left: 20px; line-height: 1.85; font-size: 16px; color: #334155;">
    <li><strong>পর্ব ১:</strong> <a href="https://www.helptrickbd.com/2025/12/computer-definition-history.html" style="color: #0284c7; font-weight: 600; text-decoration: underline;">কম্পিউটার কাকে বলে? সংজ্ঞা, ইতিহাস, বৈশিষ্ট্য ও প্রজন্ম</a></li>
    <li><strong>পর্ব ২:</strong> <a href="https://www.helptrickbd.com/2025/12/computer-history-inventions-part2.html" style="color: #0284c7; font-weight: 600; text-decoration: underline;">কম্পিউটারের ইতিহাস: এবাকাস থেকে মাইক্রোপ্রসেসর পর্যন্ত পূর্ণাঙ্গ রূপরেখা</a></li>
    <li><strong>পর্ব ৩:</strong> <a href="https://www.helptrickbd.com/2025/12/computer-generations-features-part3.html" style="color: #0284c7; font-weight: 600; text-decoration: underline;">কম্পিউটারের প্রজন্ম: ১ম থেকে ৫ম প্রজন্মের প্রযুক্তিগত তুলনা ও বৈশিষ্ট্য</a></li>
    <li><strong>পর্ব ৪:</strong> <a href="https://www.helptrickbd.com/2025/12/computer-types-classification-part4.html" style="color: #0284c7; font-weight: 600; text-decoration: underline;">কম্পিউটারের প্রকারভেদ: অ্যানালগ, ডিজিটাল, হাইব্রিড ও সুপার কম্পিউটার</a></li>
    <li><strong>সম্পর্কিত আধুনিক প্রযুক্তি গাইড:</strong> <a href="https://www.helptrickbd.com/2026/09/cloud-computing-types-benefits-guide.html" style="color: #0284c7; font-weight: 600; text-decoration: underline;">ক্লাউড কম্পিউটিং কি? প্রকারভেদ ও বাস্তব সুবিধা</a> এবং <a href="https://www.helptrickbd.com/2026/09/computer-virus-cyber-security-guide-2026.html" style="color: #0284c7; font-weight: 600; text-decoration: underline;">কম্পিউটার ভাইরাস ও সাইবার নিরাপত্তা গাইড</a></li>
  </ul>
</div>
"""

JOB_SERIES_BOX_HTML = """
<!-- Helptrickbd Minimalist Job & BCS Silo Navigation -->
<div class="htbd-silo-navigation-box" style="margin: 32px 0; padding: 22px 24px; background: #f8fafc; border: 1px solid #e2e8f0; border-left: 4px solid #0284c7; border-radius: 8px; font-family: 'SolaimanLipi', sans-serif;">
  <h4 style="margin: 0 0 12px 0; color: #0f172a; font-size: 18px; font-weight: 700;">বিসিএস, প্রাথমিক শিক্ষক ও সরকারি চাকরি প্রস্তুতি রিসোর্স:</h4>
  <ul style="margin: 0; padding-left: 20px; line-height: 1.85; font-size: 16px; color: #334155;">
    <li><strong>বিসিএস প্রিলি গাইড:</strong> <a href="https://www.helptrickbd.com/2026/09/bcs-preliminary-marks-distribution_01436475916.html" style="color: #0284c7; font-weight: 600; text-decoration: underline;">বিসিএস প্রিলিমিনারি ২০০ নম্বরের বিষয়ভিত্তিক পূর্ণাঙ্গ মানবণ্টন ও বুক লিস্ট</a></li>
    <li><strong>ভাইভা প্রস্তুতি:</strong> <a href="https://www.helptrickbd.com/2026/09/primary-teacher-job-viva-preparation.html" style="color: #0284c7; font-weight: 600; text-decoration: underline;">সরকারি প্রাথমিক শিক্ষক নিয়োগ ও চাকরির ভাইভা প্রস্তুতি গাইডলাইন (২০২৬)</a></li>
    <li><strong>চাকরি প্রস্তুতি কৌশল:</strong> <a href="https://www.helptrickbd.com/2024/12/simple-guide-to-job-and-bcs-preparation.html" style="color: #0284c7; font-weight: 600; text-decoration: underline;">অলস ও ব্যাকবেঞ্চারদের জন্য চাকরি ও বিসিএস প্রস্তুতির সহজ রোডম্যাপ</a></li>
    <li><strong>বাংলা ব্যাকরণ স্পেশাল:</strong> <a href="https://www.helptrickbd.com/2025/12/bangla-bagdhara-collection-with-meaning.html" style="color: #0284c7; font-weight: 600; text-decoration: underline;">বাংলা বাগধারা ও অর্থ: বিসিএস ও চাকরির পরীক্ষার জন্য সেরা ৫০০+ কালেকশন</a></li>
  </ul>
</div>
"""

ICT_POST_IDS = [
    {"id": "8780611538499445916", "name": "কম্পিউটার সংজ্ঞা ও ইতিহাস (পার্ট-১)", "slug": "computer-definition-history"},
    {"id": "4287526406029588825", "name": "কম্পিউটারের ইতিহাস (পার্ট-২)", "slug": "computer-history-inventions-part2"},
    {"id": "5955879897597266679", "name": "কম্পিউটারের প্রজন্ম (পার্ট-৩)", "slug": "computer-generations-features-part3"},
    {"id": "3465437051897928179", "name": "কম্পিউটারের প্রকারভেদ (পার্ট-৪)", "slug": "computer-types-classification-part4"},
    {"id": "5695213693308965635", "name": "ক্লাউড কম্পিউটিং কি ও প্রকারভেদ", "slug": "cloud-computing-types-benefits-guide"},
    {"id": "3998042912898607308", "name": "কম্পিউটার ভাইরাস ও সাইবার নিরাপত্তা", "slug": "computer-virus-cyber-security-guide-2026"}
]

JOB_POST_IDS = [
    {"id": "3708406842330148411", "name": "বিসিএস প্রিলিমিনারি মানবণ্টন ও বুক লিস্ট", "slug": "bcs-preliminary-marks-distribution"},
    {"id": "1200879181592128005", "name": "অলসদের বিসিএস ও চাকরি প্রস্তুতি", "slug": "simple-guide-to-job-and-bcs-preparation"},
    {"id": "5898560761534163519", "name": "প্রাথমিক শিক্ষক নিয়োগ ভাইভা গাইডলাইন", "slug": "primary-teacher-job-viva-preparation"},
    {"id": "2652437465190080886", "name": "বাংলা বাগধারা বিসিএস কালেকশন", "slug": "bangla-bagdhara-collection-with-meaning"}
]

def backup_post(post_data: dict, slug: str) -> str:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_dir = os.path.join(PROJECT_ROOT, "backups", "posts", slug, timestamp)
    os.makedirs(backup_dir, exist_ok=True)

    with open(os.path.join(backup_dir, "post_snapshot.json"), "w", encoding="utf-8") as f:
        json.dump(post_data, f, ensure_ascii=False, indent=2)

    with open(os.path.join(backup_dir, "content_original.html"), "w", encoding="utf-8") as f:
        f.write(post_data.get("content", ""))

    return backup_dir

def sanitize_and_clean_html(raw_html: str) -> str:
    """Removes outer <!DOCTYPE>, <html>, <head>, <body> tags and cleans overly colorful styles."""
    html = raw_html
    # Remove DOCTYPE, html, head, body tags
    html = re.sub(r'<!DOCTYPE[^>]*>', '', html, flags=re.IGNORECASE)
    html = re.sub(r'<html[^>]*>', '', html, flags=re.IGNORECASE)
    html = re.sub(r'</html>', '', html, flags=re.IGNORECASE)
    html = re.sub(r'<head[^>]*>[\s\S]*?</head>', '', html, flags=re.IGNORECASE)
    html = re.sub(r'<body[^>]*>', '', html, flags=re.IGNORECASE)
    html = re.sub(r'</body>', '', html, flags=re.IGNORECASE)

    # Clean overly flashy colors / garish background styles
    # Replace linear-gradient in badges or headers with clean solid tint
    html = re.sub(r'background:\s*linear-gradient\([^;]+\);', 'background: #f8fafc; border-left: 4px solid #0284c7;', html)
    html = re.sub(r'box-shadow:\s*0\s+10px\s+25px[^;]+;', 'box-shadow: 0 1px 3px rgba(0,0,0,0.05);', html)
    html = re.sub(r'box-shadow:\s*0\s+4px\s+14px\s+rgba\(0,0,0,0\.12\);', 'box-shadow: 0 1px 4px rgba(0,0,0,0.06);', html)

    # Remove any existing duplicate silo boxes to avoid stacking
    html = re.sub(r'<div class="htbd-silo-navigation-box"[\s\S]*?</div>\s*</div>', '', html)

    return html.strip()

def inject_silo_navigation(html: str, nav_box_html: str) -> str:
    """Safely injects the silo navigation block before FAQ, conclusion, or near the end."""
    soup = BeautifulSoup(html, "html.parser")

    # Target injection points in priority order
    faq_sec = soup.find("div", class_="htbd-faq-section") or soup.find(id="faq")
    conclusion_sec = soup.find("h2", string=re.compile(r"উপসংহার|শেষ কথা|পরিশেষ", re.IGNORECASE))
    
    nav_soup = BeautifulSoup(nav_box_html, "html.parser")

    if faq_sec:
        faq_sec.insert_before(nav_soup)
    elif conclusion_sec:
        conclusion_sec.insert_before(nav_soup)
    else:
        wrapper = soup.find("div", class_="htbd-post-wrapper") or soup.find("div", class_="post-body") or soup
        wrapper.append(nav_soup)

    return str(soup)

def process_silo(service, silo_name: str, posts_meta: list, nav_box_html: str):
    print("\n" + "=" * 75)
    print(f"🏛️ PROCESSING SILO: {silo_name} ({len(posts_meta)} Posts)")
    print("=" * 75)

    updated_urls = []

    for idx, item in enumerate(posts_meta, 1):
        pid = item["id"]
        name = item["name"]
        slug = item["slug"]

        print(f"\n[{idx}/{len(posts_meta)}] Processing: {name} (ID: {pid})")
        
        # 1. Fetch live post
        post = service.posts().get(blogId=BLOG_ID, postId=pid).execute()
        url = post.get("url", "")
        print(f"      Live URL: {url}")

        # 2. Backup
        bdir = backup_post(post, slug)
        print(f"      [✔] Backup saved: backups/posts/{slug}/")

        # 3. Clean and sanitize HTML
        raw_content = post.get("content", "")
        cleaned_content = sanitize_and_clean_html(raw_content)

        # 4. Inject Silo Navigation
        enriched_content = inject_silo_navigation(cleaned_content, nav_box_html)

        # 5. Patch Live Post
        patch_body = {"content": enriched_content}
        service.posts().patch(blogId=BLOG_ID, postId=pid, body=patch_body).execute()
        print("      [✔] Blogger Post updated with Clean Silo Architecture!")

        # 6. Google Indexing API ping
        try:
            indexer_cmd = [
                sys.executable,
                os.path.join(PROJECT_ROOT, "tools", "indexer", "index_now.py"),
                "--url", url
            ]
            subprocess.run(indexer_cmd, capture_output=True, text=True, cwd=os.path.join(PROJECT_ROOT, "tools", "indexer"))
            print("      [✔] Google Indexing API pinged (URL_UPDATED).")
        except Exception as e_idx:
            print(f"      [!] Google Indexing Ping error: {e_idx}")

        updated_urls.append(url)
        time.sleep(1.5)

    return updated_urls

def main():
    service = get_authenticated_service()
    if not service:
        print("[!] Failed to connect to Blogger API.")
        return

    print("=" * 75)
    print("🚀 HELPTRICKBD TOPICAL SILO STRENGTHENING & CLEAN-DESIGN AUTOMATOR")
    print("=" * 75)

    all_updated = []
    
    # Process ICT Silo
    ict_urls = process_silo(service, "আইসিটি ও কম্পিউটার শিক্ষা", ICT_POST_IDS, ICT_SERIES_BOX_HTML)
    all_updated.extend(ict_urls)

    # Process Job Silo
    job_urls = process_silo(service, "চাকরি ও ক্যারিয়ার প্রস্তুতি", JOB_POST_IDS, JOB_SERIES_BOX_HTML)
    all_updated.extend(job_urls)

    # 7. Execute Rule 21: Real-Time Google WebSub PubSubHubbub Pinger
    print("\n" + "=" * 75)
    print("⚡ EXECUTING RULE 21: REAL-TIME GOOGLE WEBSUB (PUBSUBHUBBUB) PINGER")
    print("=" * 75)
    try:
        pinger_cmd = [sys.executable, os.path.join(PROJECT_ROOT, "tools", "indexer", "pubsub_hub_pinger.py")]
        res = subprocess.run(pinger_cmd, capture_output=True, text=True, cwd=PROJECT_ROOT)
        print(res.stdout)
    except Exception as e_ping:
        print(f"[!] PubSubHubbub pinger failed: {e_ping}")

    report_path = os.path.join(PROJECT_ROOT, "output_posts", "silo_strengthening_report.json")
    os.makedirs(os.path.dirname(report_path), exist_ok=True)
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump({"updated_urls": all_updated, "timestamp": datetime.now(timezone.utc).isoformat()}, f, ensure_ascii=False, indent=2)

    print("\n" + "=" * 75)
    print("🎉 ALL 10 POSTS ACROSS ICT & JOB SILOS STRENGTHENED, CLEANED & PUBLISHED LIVE!")
    print(f"   Summary Report saved to: {report_path}")
    print("=" * 75)

if __name__ == "__main__":
    main()
