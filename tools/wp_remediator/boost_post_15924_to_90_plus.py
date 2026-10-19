#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import json
import re
import requests

sys.stdout.reconfigure(encoding='utf-8')

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
CONFIG_PATH = os.path.join(PROJECT_ROOT, "tools", "wp_publisher", "config.json")

with open(CONFIG_PATH, "r", encoding="utf-8") as f:
    cfg = json.load(f)

auth = (cfg["wp_user"], cfg["wp_app_password"])
base_url = cfg["wp_url"].rstrip("/")

post_id = 15924

res = requests.get(f"{base_url}/wp-json/wp/v2/posts/{post_id}?context=edit", auth=auth)
if res.status_code != 200:
    print(f"[ERROR] Failed to fetch post {post_id}")
    sys.exit(1)

post = res.json()
content = post["content"]["raw"]
kw = "৮ম শ্রেণির জুনিয়র বৃত্তি পরীক্ষার রুটিন 2026"

replacements = [
    ("জুনিয়র বৃত্তি পরীক্ষায় ভালো ফলাফল করার পূর্বশর্ত হলো প্রশ্ন কাঠামোর ওপর শতভাগ দখল রাখা।",
     f"এই {kw}-এ ভালো ফলাফল করার পূর্বশর্ত হলো প্রশ্ন কাঠামোর ওপর শতভাগ দখল রাখা।"),

    ("বাংলায় ভালো নম্বর তুলতে হলে ১ম পত্রের গল্প-কবিতার মূলভাব ও শব্দার্থ এবং ২য় পত্রের ব্যাকরণ অংশে পূর্ণ প্রস্তুতি থাকা আবশ্যক।",
     f"{kw} অনুযায়ী বাংলায় ভালো নম্বর তুলতে হলে ১ম পত্রের গল্প-কবিতার মূলভাব ও শব্দার্থ এবং ২য় পত্রের ব্যাকরণ অংশে পূর্ণ প্রস্তুতি থাকা আবশ্যক।"),

    ("ইংরেজি বিষয়ে শিক্ষার্থীদের সবচেয়ে বেশি ভয় থাকে গ্রামার ও ফ্রি-হ্যান্ড রাইটিংয়ে।",
     f"{kw} অনুযায়ী ইংরেজি বিষয়ে শিক্ষার্থীদের সবচেয়ে বেশি ভয় থাকে গ্রামার ও ফ্রি-হ্যান্ড রাইটিংয়ে।"),

    ("বিজ্ঞানের কনসেপ্ট ক্লিয়ার থাকলে এই অংশে খুব কম সময়ে শতভাগ নম্বর অর্জন করা যায়।",
     f"{kw} নির্দেশিকায় বিজ্ঞানের কনসেপ্ট ক্লিয়ার থাকলে এই অংশে খুব কম সময়ে শতভাগ নম্বর অর্জন করা যায়।"),

    ("জুনিয়র বৃত্তি পরীক্ষায় দুই ধরনের বৃত্তি প্রদান করা হয়: মেধাবৃত্তি (Talentpool) এবং সাধারণ বৃত্তি।",
     f"{kw} অনুযায়ী দুই ধরনের বৃত্তি প্রদান করা হয়: মেধাবৃত্তি (Talentpool) এবং সাধারণ বৃত্তি।"),

    ("প্রশ্ন ১: ৮ম শ্রেণির সকল শিক্ষার্থী কি জুনিয়র বৃত্তি পরীক্ষা দিতে পারবে?",
     f"প্রশ্ন ১: এই {kw} অনুযায়ী সকল শিক্ষার্থী কি অংশ নিতে পারবে?"),

    ("প্রশ্ন ২: জুনিয়র বৃত্তি পরীক্ষায় কি কোনো নেগেটিভ মার্কিং আছে?",
     f"প্রশ্ন ২: {kw} অনুযায়ী পরীক্ষায় কি কোনো নেগেটিভ মার্কিং আছে?"),

    ("প্রশ্ন ৪: জুনিয়র বৃত্তি পরীক্ষার ফলাফল কখন প্রকাশিত হবে?",
     f"প্রশ্ন ৪: {kw} অনুযায়ী ফলাফল কখন প্রকাশিত হবে?")
]

applied_count = 0
for old, new in replacements:
    if old in content:
        content = content.replace(old, new)
        applied_count += 1
    else:
        print(f"[WARN] String not found: {old[:40]}...")

words = len(re.sub(r'<[^>]+>', ' ', content).split())
kw_count = content.count(kw)
density = (kw_count / words) * 100
print(f"Applied replacements: {applied_count}/{len(replacements)}")
print(f"Updated word count: {words}")
print(f"Updated keyword count: {kw_count}")
print(f"Updated keyword density: {density:.2f}% (Target: 0.8% - 1.2%)")

payload = {
    "content": content
}

update_res = requests.post(f"{base_url}/wp-json/wp/v2/posts/{post_id}", json=payload, auth=auth)
if update_res.status_code == 200:
    print(f"[SUCCESS] Post {post_id} updated with {kw_count} occurrences of Focus Keyword (Density: {density:.2f}%)!")
else:
    print(f"[ERROR] Failed to update post: {update_res.status_code}")
