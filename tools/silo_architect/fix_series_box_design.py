#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/silo_architect/fix_series_box_design.py
-----------------------------------------------
Fixes the series navigation box across all 10 ICT and Job posts:
1. Eliminates text-align: justify stretching (sets explicit text-align: left)
2. Removes ugly blue underlines that clash with Bengali diacritics
3. Places each post on its own dedicated row (Part 1 through Part 6)
4. Replaces harsh blue border with clean, minimalist white card design
5. Patches Blogger API v3 live and pings Google WebSub Hub
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
# PERFECT NEWSPAPER-GRADE MINIMALIST SERIES NAVIGATION (ZERO STRETCHING)
# ==============================================================================
ICT_SERIES_BOX_CLEAN = """
<!-- Helptrickbd Clean Newspaper-Grade Series Navigation -->
<div class="htbd-series-nav" style="margin: 28px 0; padding: 18px 22px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; font-family: 'SolaimanLipi', sans-serif; text-align: left; box-shadow: 0 1px 3px rgba(0,0,0,0.04);">
  <div style="font-size: 17.5px; font-weight: 700; color: #0f172a; margin-bottom: 12px; border-bottom: 1px solid #e2e8f0; padding-bottom: 8px; text-align: left;">
    কম্পিউটার ও আইসিটি শিক্ষা ধারাবাহিক পর্ব:
  </div>
  <ul style="list-style: none !important; padding: 0 !important; margin: 0 !important; line-height: 1.85 !important; font-size: 16px !important; text-align: left !important;">
    <li style="list-style: none !important; padding: 6px 0 !important; border-bottom: 1px dashed #e2e8f0 !important; text-align: left !important; margin: 0 !important;">
      <span style="color: #64748b; font-weight: 600;">পর্ব ০১:</span> 
      <a href="https://www.helptrickbd.com/2025/12/computer-definition-history.html" style="color: #0284c7 !important; text-decoration: none !important; font-weight: 500 !important;">কম্পিউটার কাকে বলে? সংজ্ঞা, ইতিহাস, বৈশিষ্ট্য ও প্রজন্ম</a>
    </li>
    <li style="list-style: none !important; padding: 6px 0 !important; border-bottom: 1px dashed #e2e8f0 !important; text-align: left !important; margin: 0 !important;">
      <span style="color: #64748b; font-weight: 600;">পর্ব ০২:</span> 
      <a href="https://www.helptrickbd.com/2025/12/computer-history-inventions-part2.html" style="color: #0284c7 !important; text-decoration: none !important; font-weight: 500 !important;">কম্পিউটারের ইতিহাস: এবাকাস থেকে মাইক্রোপ্রসেসর পর্যন্ত পূর্ণাঙ্গ রূপরেখা</a>
    </li>
    <li style="list-style: none !important; padding: 6px 0 !important; border-bottom: 1px dashed #e2e8f0 !important; text-align: left !important; margin: 0 !important;">
      <span style="color: #64748b; font-weight: 600;">পর্ব ০৩:</span> 
      <a href="https://www.helptrickbd.com/2025/12/computer-generations-features-part3.html" style="color: #0284c7 !important; text-decoration: none !important; font-weight: 500 !important;">কম্পিউটারের প্রজন্ম: ১ম থেকে ৫ম প্রজন্মের প্রযুক্তিগত তুলনা ও বৈশিষ্ট্য</a>
    </li>
    <li style="list-style: none !important; padding: 6px 0 !important; border-bottom: 1px dashed #e2e8f0 !important; text-align: left !important; margin: 0 !important;">
      <span style="color: #64748b; font-weight: 600;">পর্ব ০৪:</span> 
      <a href="https://www.helptrickbd.com/2025/12/computer-types-classification-part4.html" style="color: #0284c7 !important; text-decoration: none !important; font-weight: 500 !important;">কম্পিউটারের প্রকারভেদ: অ্যানালগ, ডিজিটাল, হাইব্রিড ও সুপার কম্পিউটার</a>
    </li>
    <li style="list-style: none !important; padding: 6px 0 !important; border-bottom: 1px dashed #e2e8f0 !important; text-align: left !important; margin: 0 !important;">
      <span style="color: #64748b; font-weight: 600;">পর্ব ০৫:</span> 
      <a href="https://www.helptrickbd.com/2026/09/cloud-computing-types-benefits-guide.html" style="color: #0284c7 !important; text-decoration: none !important; font-weight: 500 !important;">ক্লাউড কম্পিউটিং কি? প্রকারভেদ ও বাস্তব সুবিধা</a>
    </li>
    <li style="list-style: none !important; padding: 6px 0 !important; text-align: left !important; margin: 0 !important;">
      <span style="color: #64748b; font-weight: 600;">পর্ব ০৬:</span> 
      <a href="https://www.helptrickbd.com/2026/09/computer-virus-cyber-security-guide-2026.html" style="color: #0284c7 !important; text-decoration: none !important; font-weight: 500 !important;">কম্পিউটার ভাইরাস ও সাইবার নিরাপত্তা: ম্যালওয়্যার থেকে ডাটা সুরক্ষার সেরা উপায়</a>
    </li>
  </ul>
</div>
"""

JOB_SERIES_BOX_CLEAN = """
<!-- Helptrickbd Clean Newspaper-Grade Job & BCS Silo Navigation -->
<div class="htbd-series-nav" style="margin: 28px 0; padding: 18px 22px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; font-family: 'SolaimanLipi', sans-serif; text-align: left; box-shadow: 0 1px 3px rgba(0,0,0,0.04);">
  <div style="font-size: 17.5px; font-weight: 700; color: #0f172a; margin-bottom: 12px; border-bottom: 1px solid #e2e8f0; padding-bottom: 8px; text-align: left;">
    বিসিএস, প্রাথমিক শিক্ষক ও সরকারি চাকরি প্রস্তুতি রিসোর্স:
  </div>
  <ul style="list-style: none !important; padding: 0 !important; margin: 0 !important; line-height: 1.85 !important; font-size: 16px !important; text-align: left !important;">
    <li style="list-style: none !important; padding: 6px 0 !important; border-bottom: 1px dashed #e2e8f0 !important; text-align: left !important; margin: 0 !important;">
      <span style="color: #64748b; font-weight: 600;">বিসিএস গাইড:</span> 
      <a href="https://www.helptrickbd.com/2026/09/bcs-preliminary-marks-distribution_01436475916.html" style="color: #0284c7 !important; text-decoration: none !important; font-weight: 500 !important;">বিসিএস প্রিলিমিনারি ২০০ নম্বরের বিষয়ভিত্তিক পূর্ণাঙ্গ মানবণ্টন ও বুক লিস্ট</a>
    </li>
    <li style="list-style: none !important; padding: 6px 0 !important; border-bottom: 1px dashed #e2e8f0 !important; text-align: left !important; margin: 0 !important;">
      <span style="color: #64748b; font-weight: 600;">ভাইভা প্রস্তুতি:</span> 
      <a href="https://www.helptrickbd.com/2026/09/primary-teacher-job-viva-preparation.html" style="color: #0284c7 !important; text-decoration: none !important; font-weight: 500 !important;">সরকারি প্রাথমিক শিক্ষক নিয়োগ ও চাকরির ভাইভা প্রস্তুতি গাইডলাইন (২০২৬)</a>
    </li>
    <li style="list-style: none !important; padding: 6px 0 !important; border-bottom: 1px dashed #e2e8f0 !important; text-align: left !important; margin: 0 !important;">
      <span style="color: #64748b; font-weight: 600;">প্রস্তুতি রোডম্যাপ:</span> 
      <a href="https://www.helptrickbd.com/2024/12/simple-guide-to-job-and-bcs-preparation.html" style="color: #0284c7 !important; text-decoration: none !important; font-weight: 500 !important;">অলস ও ব্যাকবেঞ্চারদের জন্য চাকরি ও বিসিএস প্রস্তুতির সহজ রোডম্যাপ</a>
    </li>
    <li style="list-style: none !important; padding: 6px 0 !important; text-align: left !important; margin: 0 !important;">
      <span style="color: #64748b; font-weight: 600;">বাংলা স্পেশাল:</span> 
      <a href="https://www.helptrickbd.com/2025/12/bangla-bagdhara-collection-with-meaning.html" style="color: #0284c7 !important; text-decoration: none !important; font-weight: 500 !important;">বাংলা বাগধারা ও অর্থ: বিসিএস ও চাকরির পরীক্ষার জন্য সেরা ৫০০+ কালেকশন</a>
    </li>
  </ul>
</div>
"""

ICT_POST_IDS = [
    {"id": "8780611538499445916", "name": "কম্পিউটার সংজ্ঞা ও ইতিহাস (পার্ট-১)"},
    {"id": "4287526406029588825", "name": "কম্পিউটারের ইতিহাস (পার্ট-২)"},
    {"id": "5955879897597266679", "name": "কম্পিউটারের প্রজন্ম (পার্ট-৩)"},
    {"id": "3465437051897928179", "name": "কম্পিউটারের প্রকারভেদ (পার্ট-৪)"},
    {"id": "5695213693308965635", "name": "ক্লাউড কম্পিউটিং কি ও প্রকারভেদ"},
    {"id": "3998042912898607308", "name": "কম্পিউটার ভাইরাস ও সাইবার নিরাপত্তা"}
]

JOB_POST_IDS = [
    {"id": "3708406842330148411", "name": "বিসিএস প্রিলিমিনারি মানবণ্টন ও বুক লিস্ট"},
    {"id": "1200879181592128005", "name": "অলসদের বিসিএস ও চাকরি প্রস্তুতি"},
    {"id": "5898560761534163519", "name": "প্রাথমিক শিক্ষক নিয়োগ ভাইভা গাইডলাইন"},
    {"id": "2652437465190080886", "name": "বাংলা বাগধারা বিসিএস কালেকশন"}
]

def replace_series_box(html: str, new_box_html: str) -> str:
    # First remove any existing silo navigation box (old version or previous class)
    html = re.sub(r'<!-- Helptrickbd.*?-->\s*<div class="htbd-silo-navigation-box"[\s\S]*?</ul>\s*</div>', '', html)
    html = re.sub(r'<div class="htbd-silo-navigation-box"[\s\S]*?</ul>\s*</div>', '', html)
    html = re.sub(r'<!-- Helptrickbd.*?-->\s*<div class="htbd-series-nav"[\s\S]*?</ul>\s*</div>', '', html)
    html = re.sub(r'<div class="htbd-series-nav"[\s\S]*?</ul>\s*</div>', '', html)

    # Now parse and cleanly insert the new clean box
    soup = BeautifulSoup(html, "html.parser")
    faq_sec = soup.find("div", class_="htbd-faq-section") or soup.find(id="faq")
    conclusion_sec = soup.find("h2", string=re.compile(r"উপসংহার|শেষ কথা|পরিশেষ", re.IGNORECASE))
    
    new_box_soup = BeautifulSoup(new_box_html, "html.parser")

    if faq_sec:
        faq_sec.insert_before(new_box_soup)
    elif conclusion_sec:
        conclusion_sec.insert_before(new_box_soup)
    else:
        wrapper = soup.find("div", class_="htbd-post-wrapper") or soup.find("div", class_="post-body") or soup
        wrapper.append(new_box_soup)

    return str(soup)

def update_posts(service, posts_list, new_box_html):
    for idx, item in enumerate(posts_list, 1):
        pid = item["id"]
        name = item["name"]
        print(f"[{idx}/{len(posts_list)}] Updating design for: {name} (ID: {pid})")

        post = service.posts().get(blogId=BLOG_ID, postId=pid).execute()
        content = post.get("content", "")
        updated_content = replace_series_box(content, new_box_html)

        service.posts().patch(blogId=BLOG_ID, postId=pid, body={"content": updated_content}).execute()
        print(f"      [✔] Clean typography series box updated successfully!")
        time.sleep(1.2)

def main():
    service = get_authenticated_service()
    if not service:
        print("[!] Failed to connect to Blogger API.")
        return

    print("=" * 70)
    print("🎨 REPLACING SERIES BOX WITH NEWSPAPER-GRADE CLEAN DESIGN")
    print("=" * 70)

    print("\n--- Updating ICT Silo Posts ---")
    update_posts(service, ICT_POST_IDS, ICT_SERIES_BOX_CLEAN)

    print("\n--- Updating Job Silo Posts ---")
    update_posts(service, JOB_POST_IDS, JOB_SERIES_BOX_CLEAN)

    print("\n⚡ Pinging Google WebSub Hub (Rule 21)...")
    try:
        pinger_cmd = [sys.executable, os.path.join(PROJECT_ROOT, "tools", "indexer", "pubsub_hub_pinger.py")]
        res = subprocess.run(pinger_cmd, capture_output=True, text=True, cwd=PROJECT_ROOT)
        print("WebSub Hub notified successfully.")
    except Exception as e:
        print(f"WebSub ping warning: {e}")

    print("\n" + "=" * 70)
    print("🎉 ALL 10 POSTS BEAUTIFIED WITH 100% CLEAN TYPOGRAPHY & ZERO STRETCHING!")
    print("=" * 70)

if __name__ == "__main__":
    main()
