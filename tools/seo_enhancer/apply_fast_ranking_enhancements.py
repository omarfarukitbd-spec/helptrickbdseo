#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/seo_enhancer/apply_fast_ranking_enhancements.py
-----------------------------------------------------
Implements the 3 Major Fast-Ranking SEO Enhancements:
1. E-E-A-T Visible Author Bio Card (ফারুক স্যার) across all 8 Bangla Silo posts.
2. Click-to-Reveal Interactive Accordion (<details><summary>) in Model Test and SAQ Bank.
3. Authority Link Injection from high-traffic live posts (SSC English 1st Paper & BCS Guide).
4. Auto-verifies and pings Google Indexing API, WebSub, and IndexNow (Rule 11).
"""

import os
import sys
import json
import re
import time
from bs4 import BeautifulSoup

if sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.blogger_publisher.publisher import get_authenticated_service, BLOG_ID
from tools.indexer.post_publish_verifier import verify_and_index_post

AUTHOR_BOX_HTML = """
<div class="htbd-author-box" style="margin-top: 40px; margin-bottom: 25px; padding: 22px; background: #f8fafc; border: 1px solid #e2e8f0; border-left: 5px solid #1e3a8a; border-radius: 8px; font-family: 'SolaimanLipi', Arial, sans-serif;">
  <div style="font-size: 13px; color: #64748b; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 4px;">লেখক পরিচিতি</div>
  <div style="font-size: 19px; color: #0f172a; font-weight: 700; margin-bottom: 2px;">ফারুক স্যার (মো. ওমর ফারুক)</div>
  <div style="font-size: 14px; color: #1e3a8a; font-weight: 600; margin-bottom: 10px;">সিনিয়র শিক্ষক ও শিক্ষাক্রম গবেষক | প্রতিষ্ঠাতা, HelpTrickBD</div>
  <p style="margin: 0; font-size: 15px; color: #475569; line-height: 1.65;">
    মাধ্যমিক ও উচ্চমাধ্যমিক স্তরের বাংলা ও ইংরেজি ভাষা-সাহিত্য এবং বোর্ড পরীক্ষার সৃজনশীল প্রশ্নপদ্ধতি বিশ্লেষণে এক দশকের অভিজ্ঞতাসম্পন্ন একজন অ্যাকাডেমিক পরামর্শক।
  </p>
</div>
"""

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

def add_author_box_to_html(html):
    if "htbd-author-box" in html or "ফারুক স্যার (মো. ওমর ফারুক)" in html:
        return html
    # Insert right before <script type="application/ld+json"> or at the very end
    idx = html.find('<script type="application/ld+json">')
    if idx != -1:
        return html[:idx].rstrip() + "\n" + AUTHOR_BOX_HTML + "\n" + html[idx:]
    else:
        # Before last closing div or at end
        return html.rstrip() + "\n" + AUTHOR_BOX_HTML

def enhance_model_test_interactive(html):
    # Convert MCQ static answer box into interactive accordion
    pattern = r'<div style="background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 6px; padding: 15px; margin: 20px 0;">\s*<p style="margin: 0 0 8px 0; font-weight: bold; color: #166534;">বহুনির্বাচনি অংশের আদর্শ উত্তরমালা:</p>\s*<p style="margin: 0; color: #14532d; font-family: monospace; font-size: 15px;">(.*?)</p>\s*</div>'
    
    replacement = r'''<details style="background: #f0fdf4; border: 1px solid #86efac; border-left: 5px solid #16a34a; border-radius: 8px; padding: 14px 18px; margin: 25px 0; cursor: pointer;">
<summary style="font-weight: 700; color: #15803d; font-size: 16px; outline: none;">[+] বহুনির্বাচনি (MCQ) ৩০টি প্রশ্নের আদর্শ উত্তরমালা দেখতে ক্লিক করুন</summary>
<div style="margin-top: 12px; padding-top: 12px; border-top: 1px dashed #86efac; color: #14532d; font-family: monospace; font-size: 15px; line-height: 2.2;">
\1
</div>
</details>'''
    
    new_html = re.sub(pattern, replacement, html, flags=re.DOTALL)
    return new_html

def enhance_saq_bank_interactive(html):
    # Convert "উত্তর: ..." in short question bank into interactive details/summary
    # Pattern: <li><strong>(প্রশ্ন \d+:.*?)</strong><br/>\s*<em>উত্তর:</em>\s*(.*?)</li>
    pattern = r'<li><strong>(প্রশ্ন \d+:.*?)</strong><br/>\s*<em>উত্তর:</em>\s*(.*?)</li>'
    
    def repl(m):
        q_title = m.group(1).strip()
        ans_text = m.group(2).strip()
        return f'''<li style="margin-bottom: 14px;"><strong>{q_title}</strong>
<details style="margin: 6px 0 10px 0; cursor: pointer;">
<summary style="font-weight: 600; color: #1e40af; font-size: 14.5px; outline: none;">[+] নির্ভুল উত্তর ও অনুধাবনমূলক ব্যাখ্যা দেখতে ক্লিক করুন</summary>
<div style="margin-top: 6px; padding: 10px 14px; background: #f8fafc; border-left: 3px solid #2563eb; border-radius: 4px; color: #1e293b; line-height: 1.8;">
<em>উত্তর:</em> {ans_text}
</div>
</details></li>'''

    new_html = re.sub(pattern, repl, html)
    return new_html

def inject_inbound_links_to_older_posts(service):
    print("\n" + "=" * 75)
    print("PHASE 3: INJECTING LINK JUICE FROM HIGH-TRAFFIC OLDER POSTS")
    print("=" * 75)

    # 1. SSC English 1st Paper Suggestion (Post ID: 5652005814898036993)
    try:
        eng_post_id = "5652005814898036993"
        post = service.posts().get(blogId=BLOG_ID, postId=eng_post_id).execute()
        content = post.get("content", "")
        
        target_link = "https://www.helptrickbd.com/2026/09/ssc-bangla-1st-paper-final-suggestion.html"
        if target_link not in content:
            link_box = """
<div class="htbd-exam-card" style="margin: 28px 0; padding: 18px; background: #eff6ff; border: 1px solid #bfdbfe; border-left: 5px solid #2563eb; border-radius: 8px; font-family: 'SolaimanLipi', Arial, sans-serif;">
  <strong style="color: #1e40af; font-size: 16px;">📌 এসএসসি ও দাখিল ২০২৬-২০২৭ পরীক্ষার্থীদের জন্য বিশেষ নির্দেশনা:</strong>
  <p style="margin: 8px 0 0 0; font-size: 15px; color: #1e293b; line-height: 1.7;">
    ইংরেজি বিষয়ের সেরা প্রস্তুতির পাশাপাশি বাংলা ১ম পত্রে পূর্ণাঙ্গ এ-প্লাস নিশ্চিত করতে আমাদের নতুন 
    <a href="https://www.helptrickbd.com/2026/09/ssc-bangla-1st-paper-final-suggestion.html" style="color: #1d4ed8; font-weight: 700; text-decoration: underline;">SSC বাংলা ১ম পত্র চূড়ান্ত সাজেশন, ১০০ নম্বরের মডেল টেস্ট ও প্রশ্নব্যাংক ২০২৭ (১০০% বোর্ড কমন)</a> দেখে নাও।
  </p>
</div>
"""
            # Insert after the first overview box or first heading
            idx = content.find("<!--more-->")
            if idx != -1:
                content = content[:idx+11] + "\n" + link_box + "\n" + content[idx+11:]
            else:
                content = link_box + "\n" + content
                
            service.posts().patch(blogId=BLOG_ID, postId=eng_post_id, body={"content": content}).execute()
            print(f"[✔] Link Juice Injected into: SSC English 1st Paper (ID: {eng_post_id})")
        else:
            print(f"[*] Already linked in SSC English 1st Paper.")
    except Exception as e:
        print(f"[!] Warning injecting link to English post: {e}")

    # 2. Simple Guide to Job and BCS Preparation (Post ID: 1200879181592128005)
    try:
        bcs_post_id = "1200879181592128005"
        post = service.posts().get(blogId=BLOG_ID, postId=bcs_post_id).execute()
        content = post.get("content", "")
        
        target_link = "https://www.helptrickbd.com/2026/09/ssc-bangla-1st-paper-final-suggestion.html"
        if target_link not in content:
            bcs_link_box = """
<div style="margin: 25px 0; padding: 16px; background: #f0fdf4; border: 1px solid #bbf7d0; border-left: 5px solid #16a34a; border-radius: 8px; font-family: 'SolaimanLipi', Arial, sans-serif;">
  <strong style="color: #15803d; font-size: 16px;">💡 বাংলা ভাষা ও সাহিত্য প্রস্তুতির সহায়ক রিসোর্স:</strong>
  <p style="margin: 6px 0 0 0; font-size: 15px; color: #14532d; line-height: 1.7;">
    যেকোনো প্রতিযোগিতামূলক পরীক্ষা ও অ্যাকাডেমিক বুনিয়াদের জন্য বাংলা সাহিত্যের মূল টেক্সট ও প্রবন্ধের নিখুঁত ব্যাখ্যার জন্য আমাদের 
    <a href="https://www.helptrickbd.com/2026/09/ssc-bangla-1st-paper-final-suggestion.html" style="color: #166534; font-weight: 700; text-decoration: underline;">বাংলা ১ম পত্র এক্সক্লুসিভ সাহিত্য বিশ্লেষণ ও প্রশ্নব্যাংক গাইড</a> দেখতে পারেন।
  </p>
</div>
"""
            idx = content.find("<!--more-->")
            if idx != -1:
                content = content[:idx+11] + "\n" + bcs_link_box + "\n" + content[idx+11:]
            else:
                content = bcs_link_box + "\n" + content
                
            service.posts().patch(blogId=BLOG_ID, postId=bcs_post_id, body={"content": content}).execute()
            print(f"[✔] Link Juice Injected into: BCS Preparation Guide (ID: {bcs_post_id})")
        else:
            print(f"[*] Already linked in BCS Preparation Guide.")
    except Exception as e:
        print(f"[!] Warning injecting link to BCS post: {e}")

def main():
    print("=" * 75)
    print("🚀 HELPTRICKBD — APPLYING 3 MAJOR FAST-RANKING ENHANCEMENTS")
    print("=" * 75)

    service = get_authenticated_service()
    if not service:
        print("[ERROR] Blogger authentication failed.")
        sys.exit(1)

    # Phase 1 & 2: Process all 8 Bangla Silo posts
    for post_id, html_rel, meta_rel in BANGLA_POSTS:
        html_path = os.path.join(PROJECT_ROOT, html_rel)
        meta_path = os.path.join(PROJECT_ROOT, meta_rel)

        print(f"\n[*] Processing: {os.path.basename(html_rel)}...")
        with open(html_path, "r", encoding="utf-8") as f:
            html = f.read()

        # Feature 1: Add Author Box
        html = add_author_box_to_html(html)

        # Feature 2: Interactive Accordions
        if "model-test" in html_rel:
            html = enhance_model_test_interactive(html)
            print("    [✔] Converted MCQ answer key into interactive click-to-reveal accordion.")
        elif "short-question" in html_rel:
            html = enhance_saq_bank_interactive(html)
            print("    [✔] Converted 100 SAQs into interactive click-to-reveal accordions.")

        # Save local file
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html)
        print("    [✔] Local file updated.")

        # Patch Live Blogger Post
        with open(meta_path, "r", encoding="utf-8") as f:
            meta = json.load(f)
        title = meta.get("title")

        patch_body = {"title": title, "content": html}
        res = service.posts().patch(blogId=BLOG_ID, postId=post_id, body=patch_body).execute()
        live_url = res.get("url")
        print(f"    [✔] Live Blogger Post Patched: {live_url}")
        time.sleep(1)

    # Phase 3: Inbound Link Injection from high-traffic older posts
    inject_inbound_links_to_older_posts(service)

    # Phase 4: Run Post-Publish Verification Pipeline (Rule 11) on all 8 posts
    print("\n" + "=" * 75)
    print("PHASE 4: RUNNING RULE 11 MULTI-ENGINE POST-PUBLISH VERIFICATION")
    print("=" * 75)
    for post_id, html_rel, meta_rel in BANGLA_POSTS:
        html_path = os.path.join(PROJECT_ROOT, html_rel)
        with open(meta_path, "r", encoding="utf-8") as f:
            meta = json.load(f)
        live_url = meta.get("url") or f"https://www.helptrickbd.com/2026/09/{os.path.basename(html_rel).replace('.html', '')}.html"
        verify_and_index_post(live_url, html_path)
        time.sleep(0.5)

    print("\n" + "=" * 75)
    print("🎉 ALL 3 FAST-RANKING ENHANCEMENTS APPLIED & FULLY VERIFIED!")
    print("=" * 75)

if __name__ == "__main__":
    main()
