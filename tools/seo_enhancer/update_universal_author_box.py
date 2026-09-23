#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/seo_enhancer/update_universal_author_box.py
-------------------------------------------------
Updates all 8 post author boxes with Option 02 (Universal Academic E-E-A-T):
- Covers School/College to Honours/Masters Political Science & Literature.
- Patches Blogger live and verifies.
"""

import os
import sys
import re
import json
import time

if sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.blogger_publisher.publisher import get_authenticated_service, BLOG_ID

NEW_AUTHOR_BOX_HTML = """<div class="htbd-author-box" style="margin-top: 40px; margin-bottom: 25px; padding: 22px; background: #f8fafc; border: 1px solid #e2e8f0; border-left: 5px solid #1e3a8a; border-radius: 8px; font-family: 'SolaimanLipi', Arial, sans-serif;">
  <div style="font-size: 13px; color: #64748b; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 4px;">লেখক পরিচিতি</div>
  <div style="font-size: 19px; color: #0f172a; font-weight: 700; margin-bottom: 2px;">ফারুক স্যার (মো. ওমর ফারুক)</div>
  <div style="font-size: 14px; color: #1e3a8a; font-weight: 600; margin-bottom: 10px;">শিক্ষাবিদ ও অ্যাকাডেমিক গবেষক | প্রতিষ্ঠাতা, HelpTrickBD</div>
  <p style="margin: 0; font-size: 15px; color: #475569; line-height: 1.65;">
    অ্যাকাডেমিক পাঠ্যক্রম এবং স্নাতক ও স্নাতকোত্তর পর্যায়ের রাষ্ট্রবিজ্ঞান, আধুনিক রাষ্ট্রচিন্তা ও সাহিত্য বিশ্লেষণে এক দশকের বাস্তব শিক্ষকতার অভিজ্ঞতাসম্পন্ন একজন অ্যাকাডেমিক মেন্টর।
  </p>
</div>"""

BANGLA_POSTS = [
    ("6904395060145150353", "output_posts/ssc-bangla-1st-paper-final-suggestion-2027.html", "output_posts/ssc-bangla-1st-paper-final-suggestion-2027_metadata.json"),
    ("4356373537694150476", "output_posts/ssc-bangla-1st-paper-prose-cq-suggestions-2027.html", "output_posts/ssc-bangla-1st-paper-prose-cq-suggestions-2027_metadata.json"),
    ("8676318542398082119", "output_posts/ssc-bangla-1st-paper-prose-cq-part-2.html", "output_posts/ssc-bangla-1st-paper-prose-cq-part-2_metadata.json"),
    ("6925279533940643847", "output_posts/ssc-bangla-1st-paper-prose-cq-part-3.html", "output_posts/ssc-bangla-1st-paper-prose-cq-part-3_metadata.json"),
    ("6383095457170141697", "output_posts/ssc-bangla-1st-paper-poetry-cq-part-1.html", "output_posts/ssc-bangla-1st-paper-poetry-cq-part-1_metadata.json"),
    ("5928495229348422345", "output_posts/ssc-bangla-1st-paper-poetry-cq-part-2.html", "output_posts/ssc-bangla-1st-paper-poetry-cq-part-2_metadata.json"),
    ("5165737254267940811", "output_posts/ssc-bangla-1st-paper-short-question-bank-20-marks.html", "output_posts/ssc-bangla-1st-paper-short-question-bank-20-marks_metadata.json"),
    ("4514455172913539953", "output_posts/ssc-bangla-1st-paper-model-test-question-solution-100-marks.html", "output_posts/ssc-bangla-1st-paper-model-test-question-solution-100-marks_metadata.json"),
]

def main():
    print("=" * 75)
    print("UPDATING UNIVERSAL E-E-A-T AUTHOR BOX (OPTION 02) ACROSS ALL 8 POSTS")
    print("=" * 75)

    service = get_authenticated_service()
    if not service:
        print("[ERROR] Blogger authentication failed.")
        sys.exit(1)

    author_pattern = r'<div class="htbd-author-box"[^>]*>.*?</div>\s*</div>'

    for post_id, html_rel, meta_rel in BANGLA_POSTS:
        html_path = os.path.join(PROJECT_ROOT, html_rel)
        meta_path = os.path.join(PROJECT_ROOT, meta_rel)

        print(f"\n[*] Updating: {os.path.basename(html_rel)} (ID: {post_id})...")
        with open(html_path, "r", encoding="utf-8") as f:
            html = f.read()

        # Regex to match existing author box
        # Matches <div class="htbd-author-box" ... </div>
        # Note: the inner text has no closing </div> except the outer container
        # Let's match from <div class="htbd-author-box" to </p>\s*</div>
        sub_pattern = r'<div class="htbd-author-box".*?</p>\s*</div>'
        if re.search(sub_pattern, html, flags=re.DOTALL):
            new_html = re.sub(sub_pattern, NEW_AUTHOR_BOX_HTML, html, flags=re.DOTALL)
            print("    [✔] Matched and replaced with Option 02 Author Box.")
        else:
            # Fallback: if not matched by regex, insert right before script or at end
            idx = html.find('<script type="application/ld+json">')
            if idx != -1:
                new_html = html[:idx].rstrip() + "\n" + NEW_AUTHOR_BOX_HTML + "\n" + html[idx:]
            else:
                new_html = html.rstrip() + "\n" + NEW_AUTHOR_BOX_HTML
            print("    [!] Injected as new block.")

        with open(html_path, "w", encoding="utf-8") as f:
            f.write(new_html)

        # Patch live Blogger post
        with open(meta_path, "r", encoding="utf-8") as f:
            meta = json.load(f)
        title = meta.get("title")

        res = service.posts().patch(blogId=BLOG_ID, postId=post_id, body={"content": new_html}).execute()
        print(f"    [✔] Live Blogger Post Patched: {res.get('url')}")
        time.sleep(1)

    print("\n" + "=" * 75)
    print("ALL 8 POSTS UPDATED WITH UNIVERSAL OPTION 02 AUTHOR BOX!")
    print("=" * 75)

if __name__ == "__main__":
    main()
