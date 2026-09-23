#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import re
import json

if sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.blogger_publisher.publisher import get_authenticated_service, BLOG_ID
from tools.indexer.post_publish_verifier import verify_and_index_post

# 1. Update metadata json with exact live URLs
with open("output_posts/ssc-bangla-1st-paper-short-question-bank-20-marks_metadata.json", "r", encoding="utf-8") as f:
    d_short = json.load(f)
d_short["url"] = "https://www.helptrickbd.com/2026/09/ssc-bangla-1st-paper-short-question.html"
d_short["post_id"] = "5165737254267940811"
with open("output_posts/ssc-bangla-1st-paper-short-question-bank-20-marks_metadata.json", "w", encoding="utf-8") as f:
    json.dump(d_short, f, ensure_ascii=False, indent=2)

with open("output_posts/ssc-bangla-1st-paper-model-test-question-solution-100-marks_metadata.json", "r", encoding="utf-8") as f:
    d_model = json.load(f)
d_model["url"] = "https://www.helptrickbd.com/2026/09/ssc-bangla-1st-paper-model-test.html"
d_model["post_id"] = "4514455172913539953"
with open("output_posts/ssc-bangla-1st-paper-model-test-question-solution-100-marks_metadata.json", "w", encoding="utf-8") as f:
    json.dump(d_model, f, ensure_ascii=False, indent=2)

# 2. Convert model test MCQ answer box to details/summary
model_html_path = "output_posts/ssc-bangla-1st-paper-model-test-question-solution-100-marks.html"
with open(model_html_path, "r", encoding="utf-8") as f:
    html = f.read()

pattern = r'<div style="[^"]*border:\s*1px solid #bbf7d0;[^"]*">\s*<p[^>]*>বহুনির্বাচনি অংশের আদর্শ উত্তরমালা:</p>\s*<p[^>]*>(.*?)</p>\s*</div>'
replacement = r'''<details style="background: #f0fdf4; border: 1px solid #86efac; border-left: 5px solid #16a34a; border-radius: 8px; padding: 14px 18px; margin: 25px 0; cursor: pointer;">
<summary style="font-weight: 700; color: #15803d; font-size: 16px; outline: none;">[+] বহুনির্বাচনি (MCQ) ৩০টি প্রশ্নের আদর্শ উত্তরমালা দেখতে ক্লিক করুন</summary>
<div style="margin-top: 12px; padding-top: 12px; border-top: 1px dashed #86efac; color: #14532d; font-family: monospace; font-size: 15px; line-height: 2.2;">
\1
</div>
</details>'''

new_html, count = re.subn(pattern, replacement, html, flags=re.DOTALL)
print(f"Model test MCQ replaced: {count} occurrence(s)")

with open(model_html_path, "w", encoding="utf-8") as f:
    f.write(new_html)

# 3. Patch model test to Blogger Live
service = get_authenticated_service()
service.posts().patch(blogId=BLOG_ID, postId="4514455172913539953", body={"content": new_html}).execute()
print("Patched Model Test live on Blogger!")

# 4. Run verify_and_index_post on both URLs
print("\n--- Verifying Short Question Bank ---")
verify_and_index_post("https://www.helptrickbd.com/2026/09/ssc-bangla-1st-paper-short-question.html", "output_posts/ssc-bangla-1st-paper-short-question-bank-20-marks.html")

print("\n--- Verifying Model Test ---")
verify_and_index_post("https://www.helptrickbd.com/2026/09/ssc-bangla-1st-paper-model-test.html", model_html_path)
