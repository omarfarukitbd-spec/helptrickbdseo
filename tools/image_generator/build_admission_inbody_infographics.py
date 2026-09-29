#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/image_generator/build_admission_inbody_infographics.py
------------------------------------------------------------
Generates 2 high-resolution, newspaper-grade in-body infographics for:
পাবলিক বিশ্ববিদ্যালয় ভর্তি তথ্য ২০২৬: যোগ্যতা, ইউনিট ও বিষয়ভিত্তিক পূর্ণাঙ্গ গাইড.
1. public_university_unit_matrix.webp
2. public_university_group_change_flow.webp
"""

import os
import sys
import subprocess
from PIL import Image

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.image_optimizer.webp_compressor import compress_to_target_webp

POSTS_DIR = os.path.join(PROJECT_ROOT, "assets", "images", "posts")
os.makedirs(POSTS_DIR, exist_ok=True)

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
if not os.path.exists(CHROME_PATH):
    CHROME_PATH = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"


def render_html_to_webp(html_content: str, output_path: str, width: int = 1200, height: int = 675):
    """Renders HTML layout with Chromium headless screenshot to produce perfect typography and compresses to WebP."""
    temp_html = os.path.join(PROJECT_ROOT, "scratch", "temp_infographic.html")
    temp_png = os.path.join(PROJECT_ROOT, "scratch", "temp_infographic.png")
    os.makedirs(os.path.dirname(temp_html), exist_ok=True)

    with open(temp_html, "w", encoding="utf-8") as f:
        f.write(html_content)

    cmd = [
        CHROME_PATH,
        "--headless",
        "--disable-gpu",
        "--hide-scrollbars",
        f"--window-size={width},{height}",
        f"--screenshot={temp_png}",
        f"file:///{temp_html.replace(os.sep, '/')}"
    ]

    subprocess.run(cmd, capture_output=True, check=True)

    if os.path.exists(temp_png):
        compress_to_target_webp(temp_png, output_path, target_min_kb=15, target_max_kb=35)
        try:
            os.remove(temp_html)
            os.remove(temp_png)
        except Exception:
            pass
        return True
    return False


def build_unit_matrix_card():
    """Generates the University Unit Matrix Infographic."""
    out_file = os.path.join(POSTS_DIR, "public_university_unit_matrix.webp")
    html = f"""<!DOCTYPE html>
<html lang="bn">
<head>
<meta charset="UTF-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Hind+Siliguri:wght@500;600;700&display=swap');
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    width: 1200px;
    height: 675px;
    background: linear-gradient(135deg, #042f2e 0%, #0f172a 100%);
    font-family: 'Hind Siliguri', sans-serif;
    color: #ffffff;
    display: flex;
    flex-direction: column;
    padding: 35px 45px;
    justify-content: space-between;
  }}
  .header {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 2px solid rgba(45, 212, 191, 0.3);
    padding-bottom: 15px;
  }}
  .badge {{
    background: #0d9488;
    color: #ffffff;
    font-size: 15px;
    font-weight: 700;
    padding: 6px 16px;
    border-radius: 20px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }}
  .title {{
    font-size: 26px;
    font-weight: 700;
    color: #5eead4;
  }}
  .source {{
    font-size: 15px;
    color: #94a3b8;
  }}
  .grid {{
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 15px;
    margin: 20px 0;
  }}
  .card {{
    background: rgba(15, 23, 42, 0.75);
    border: 1px solid rgba(45, 212, 191, 0.25);
    border-radius: 12px;
    padding: 16px 14px;
    display: flex;
    flex-direction: column;
  }}
  .card-top {{
    font-size: 20px;
    font-weight: 700;
    color: #38bdf8;
    margin-bottom: 8px;
    border-bottom: 1px solid rgba(255,255,255,0.1);
    padding-bottom: 6px;
    text-align: center;
  }}
  .card-row {{
    font-size: 13.5px;
    margin-bottom: 6px;
    line-height: 1.35;
    color: #e2e8f0;
  }}
  .card-row strong {{
    color: #fde047;
  }}
  .footer {{
    background: rgba(0, 0, 0, 0.3);
    border-radius: 8px;
    padding: 10px 18px;
    display: flex;
    justify-content: space-between;
    font-size: 13px;
    color: #cbd5e1;
    border: 1px solid rgba(255,255,255,0.08);
  }}
  .highlight {{ color: #2dd4bf; font-weight: 700; }}
</style>
</head>
<body>
  <div class="header">
    <span class="badge">অ্যাডমিশন ডিরেক্টরি ২০২৬</span>
    <span class="title">শীর্ষ ৫ পাবলিক বিশ্ববিদ্যালয় ভর্তি যোগ্যতা ও মানবণ্টন ছক</span>
    <span class="source">helptrickbd.com</span>
  </div>

  <div class="grid">
    <div class="card">
      <div class="card-top">ঢাকা বিশ্ববিদ্যালয়</div>
      <div class="card-row"><strong>ইউনিট:</strong> ৪টি মূল + আইবিএ</div>
      <div class="card-row"><strong>ন্যূনতম জিপিএ:</strong> ৭.৫০ - ৮.০০</div>
      <div class="card-row"><strong>পরীক্ষা:</strong> ১০০ (৬০ MCQ + ৪০ লিখিত)</div>
      <div class="card-row"><strong>জিপিএ মার্ক:</strong> ২০ নম্বর</div>
      <div class="card-row"><strong>নেগেটিভ:</strong> ০.২৫</div>
      <div class="card-row"><strong>সেকেন্ড টাইম:</strong> সম্পূর্ণ নিষিদ্ধ</div>
    </div>

    <div class="card">
      <div class="card-top">চট্টগ্রাম বিশ্ববিদ্যালয়</div>
      <div class="card-row"><strong>ইউনিট:</strong> A, B, C, D (বি.প.)</div>
      <div class="card-row"><strong>ন্যূনতম জিপিএ:</strong> ৭.৫০ - ৮.২৫</div>
      <div class="card-row"><strong>পরীক্ষা:</strong> ১০০ MCQ (লিখিত নেই)</div>
      <div class="card-row"><strong>জিপিএ মার্ক:</strong> ২০ নম্বর</div>
      <div class="card-row"><strong>নেগেটিভ:</strong> ০.২৫</div>
      <div class="card-row"><strong>সেকেন্ড টাইম:</strong> আছে (৫ নম্বর কর্তন)</div>
    </div>

    <div class="card">
      <div class="card-top">রাজশাহী বিশ্ববিদ্যালয়</div>
      <div class="card-row"><strong>ইউনিট:</strong> A, B, C</div>
      <div class="card-row"><strong>ন্যূনতম জিপিএ:</strong> ৭.০০ - ৮.০০</div>
      <div class="card-row"><strong>পরীক্ষা:</strong> ৮০ MCQ = ১০০ নম্বর</div>
      <div class="card-row"><strong>জিপিএ মার্ক:</strong> নেই (০ নম্বর)</div>
      <div class="card-row"><strong>নেগেটিভ:</strong> ০.২৫ (৪ ভুলে ১)</div>
      <div class="card-row"><strong>সেকেন্ড টাইম:</strong> আছে (০ কর্তন)</div>
    </div>

    <div class="card">
      <div class="card-top">জাহাঙ্গীরনগর বিশ্ববিদ্যালয়</div>
      <div class="card-row"><strong>ইউনিট:</strong> A, B, C, D, E</div>
      <div class="card-row"><strong>ন্যূনতম জিপিএ:</strong> ৭.৫০ - ৯.০০</div>
      <div class="card-row"><strong>পরীক্ষা:</strong> ৮০ MCQ</div>
      <div class="card-row"><strong>জিপিএ মার্ক:</strong> ২০ নম্বর</div>
      <div class="card-row"><strong>নেগেটিভ:</strong> ০.২০</div>
      <div class="card-row"><strong>সেকেন্ড টাইম:</strong> আছে (শর্তসাপেক্ষ)</div>
    </div>

    <div class="card">
      <div class="card-top">গুচ্ছভুক্ত ২৪ ভার্সিটি</div>
      <div class="card-row"><strong>ইউনিট:</strong> A (বিজ্ঞান), B, C</div>
      <div class="card-row"><strong>ন্যূনতম জিপিএ:</strong> ৬.০০ - ৮.০০</div>
      <div class="card-row"><strong>পরীক্ষা:</strong> ১০০ MCQ</div>
      <div class="card-row"><strong>জিপিএ মার্ক:</strong> কোনো মার্ক নেই</div>
      <div class="card-row"><strong>নেগেটিভ:</strong> ০.২৫</div>
      <div class="card-row"><strong>সেকেন্ড টাইম:</strong> আছে (নম্বর কাটে না)</div>
    </div>
  </div>

  <div class="footer">
    <span>সতর্কতা: বিশ্ববিদ্যালয়গুলো প্রতি বছর সার্কুলারে জিপিএ শর্ত সামান্য হালনাগাদ করতে পারে।</span>
    <span class="highlight">HelpTrickBD • খাঁটি শিক্ষামূলক গাইডলাইন ২০২৬</span>
  </div>
</body>
</html>"""
    render_html_to_webp(html, out_file)
    print(f"[OK] Generated: {out_file}")


def build_group_change_card():
    """Generates the Group Change Flowchart Infographic."""
    out_file = os.path.join(POSTS_DIR, "public_university_group_change_flow.webp")
    html = f"""<!DOCTYPE html>
<html lang="bn">
<head>
<meta charset="UTF-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Hind+Siliguri:wght@500;600;700&display=swap');
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    width: 1200px;
    height: 675px;
    background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%);
    font-family: 'Hind Siliguri', sans-serif;
    color: #ffffff;
    display: flex;
    flex-direction: column;
    padding: 35px 45px;
    justify-content: space-between;
  }}
  .header {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 2px solid rgba(129, 140, 248, 0.3);
    padding-bottom: 15px;
  }}
  .badge {{
    background: #4f46e5;
    color: #ffffff;
    font-size: 15px;
    font-weight: 700;
    padding: 6px 16px;
    border-radius: 20px;
  }}
  .title {{
    font-size: 26px;
    font-weight: 700;
    color: #a5b4fc;
  }}
  .source {{
    font-size: 15px;
    color: #94a3b8;
  }}
  .flow-container {{
    display: flex;
    flex-direction: column;
    gap: 16px;
    margin: 15px 0;
  }}
  .flow-row {{
    background: rgba(30, 41, 59, 0.7);
    border: 1px solid rgba(129, 140, 248, 0.2);
    border-radius: 12px;
    padding: 14px 20px;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }}
  .flow-from {{
    width: 220px;
    font-size: 18px;
    font-weight: 700;
    color: #38bdf8;
    display: flex;
    flex-direction: column;
  }}
  .flow-from small {{
    font-size: 12.5px;
    color: #94a3b8;
    font-weight: 500;
  }}
  .arrow {{
    font-size: 24px;
    color: #818cf8;
    font-weight: 700;
    padding: 0 15px;
  }}
  .flow-to {{
    flex: 1;
    font-size: 14px;
    color: #e2e8f0;
    line-height: 1.45;
  }}
  .flow-to strong {{
    color: #fde047;
  }}
  .footer {{
    background: rgba(0, 0, 0, 0.3);
    border-radius: 8px;
    padding: 10px 18px;
    display: flex;
    justify-content: space-between;
    font-size: 13px;
    color: #cbd5e1;
    border: 1px solid rgba(255,255,255,0.08);
  }}
  .highlight {{ color: #a5b4fc; font-weight: 700; }}
</style>
</head>
<body>
  <div class="header">
    <span class="badge">বিভাগ পরিবর্তন ২০২৬</span>
    <span class="title">পাবলিক বিশ্ববিদ্যালয়ে বিভাগ পরিবর্তন ও বিষয় পাওয়ার রোডম্যাপ</span>
    <span class="source">helptrickbd.com</span>
  </div>

  <div class="flow-container">
    <div class="flow-row">
      <div class="flow-from">
        বিজ্ঞান বিভাগ
        <small>HSC Science Group</small>
      </div>
      <div class="arrow">---&gt;</div>
      <div class="flow-to">
        <strong>মানবিক ও বাণিজ্যে পরিবর্তন:</strong> আইন (Law), আন্তর্জাতিক সম্পর্ক (IR), অর্থনীতি, ইংরেজি, লোকপ্রশাসন, গণযোগাযোগ ও সাংবাদিকতা, ফিন্যান্স, মার্কেটিং এবং ম্যানেজমেন্টের প্রায় ৯০% উন্মুক্ত সিটে ভর্তি হতে পারে।
      </div>
    </div>

    <div class="flow-row">
      <div class="flow-from">
        ব্যবসায় শিক্ষা
        <small>HSC Commerce Group</small>
      </div>
      <div class="arrow">---&gt;</div>
      <div class="flow-to">
        <strong>মানবিকে পরিবর্তন:</strong> আইন, অর্থনীতি (শর্তসাপেক্ষ), আন্তর্জাতিক সম্পর্ক, লোকপ্রশাসন, সমাজবিজ্ঞান ও জনসংযোগের মতো সম্মানজনক বিষয়গুলোতে অনায়াসে ভর্তি পরীক্ষা দেওয়ার সুযোগ পায়।
      </div>
    </div>

    <div class="flow-row">
      <div class="flow-from">
        মানবিক বিভাগ
        <small>HSC Humanities Group</small>
      </div>
      <div class="arrow">---&gt;</div>
      <div class="flow-to">
        <strong>বাণিজ্যে পরিবর্তন:</strong> ব্যবসায় প্রশাসন অনুষদের (BBA) নির্ধারিত কোটা বা সমন্বিত 'D' ইউনিটের মাধ্যমে মার্কেটিং, ম্যানেজমেন্ট ও ট্যুরিজমের মতো বিষয়ে আবেদনের সুযোগ পায়।
      </div>
    </div>
  </div>

  <div class="footer">
    <span>বিশেষ দ্রষ্টব্য: মানবিক বা বাণিজ্য থেকে বিজ্ঞান অনুষদের পিওর সায়েন্স বা ইঞ্জিনিয়ারিংয়ে আবেদন করা যায় না।</span>
    <span class="highlight">HelpTrickBD • ক্যারিয়ার ও অ্যাডমিশন সেল</span>
  </div>
</body>
</html>"""
    render_html_to_webp(html, out_file)
    print(f"[OK] Generated: {out_file}")


def main():
    print("=" * 70)
    print("RENDERING IN-BODY ADMISSION INFOGRAPHICS...")
    print("=" * 70)
    build_unit_matrix_card()
    build_group_change_card()
    print("\n[✔] All in-body visual infographics generated successfully!")


if __name__ == "__main__":
    main()
