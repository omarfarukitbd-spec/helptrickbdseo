#!/usr/bin/env python3
"""
Generate 6 realistic high-resolution interface screenshots for the 2026 Certificate Correction Tutorial.
Uses pure relative CSS markup for 100% pixel-perfect click-target bounding boxes,
Google Fonts Hind Siliguri Bold badges, and pointing arrows.
"""

import os
import subprocess
import sys
import tempfile
from PIL import Image

try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "assets", "images", "tutorials")
os.makedirs(OUTPUT_DIR, exist_ok=True)

CHROME_CANDIDATES = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe"),
]

CHROME_PATH = None
for c in CHROME_CANDIDATES:
    if os.path.exists(c):
        CHROME_PATH = c
        break

if not CHROME_PATH:
    raise RuntimeError("Google Chrome executable not found.")


COMMON_CSS = """
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    width: 1200px;
    height: 675px;
    overflow: hidden;
    background: #f1f5f9;
    font-family: 'Hind Siliguri', 'Inter', sans-serif;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }

  /* Government Portal Top Header */
  .gov-header {
    background: #0f4c3a;
    color: #ffffff;
    padding: 10px 32px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 3.5px solid #d4af37;
  }
  .gov-brand {
    display: flex;
    align-items: center;
    gap: 14px;
  }
  .gov-logo {
    width: 44px;
    height: 44px;
    border-radius: 50%;
    background: #ffffff;
    color: #0f4c3a;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    font-size: 22px;
  }
  .gov-title h1 {
    font-size: 19px;
    font-weight: 700;
    line-height: 1.2;
  }
  .gov-title p {
    font-size: 13px;
    color: #cbd5e1;
  }
  .gov-nav {
    display: flex;
    gap: 20px;
    font-size: 14.5px;
    font-weight: 600;
  }
  .gov-nav span.active {
    color: #facc15;
    border-bottom: 2px solid #facc15;
    padding-bottom: 2px;
  }

  /* Main Canvas Area */
  .main-canvas {
    padding: 22px 36px;
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }

  /* Pixel-Perfect Click Target Container */
  .target-container {
    position: relative;
    display: inline-block;
  }
  .target-box {
    border: 3.5px solid #dc2626 !important;
    border-radius: 8px !important;
    box-shadow: 0 0 0 3px rgba(220, 38, 38, 0.35), 0 6px 18px rgba(220, 38, 38, 0.5) !important;
  }
  .target-badge-top {
    position: absolute;
    bottom: calc(100% + 12px);
    left: 8px;
    background: #dc2626;
    color: #ffffff;
    padding: 6px 18px;
    border-radius: 30px;
    border: 2px solid #ffffff;
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.35);
    font-size: 16px;
    font-weight: 700;
    white-space: nowrap;
    z-index: 200;
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .target-badge-top::after {
    content: '';
    position: absolute;
    top: 100%;
    left: 26px;
    width: 0;
    height: 0;
    border-left: 8px solid transparent;
    border-right: 8px solid transparent;
    border-top: 10px solid #dc2626;
  }

  .target-badge-bottom {
    position: absolute;
    top: calc(100% + 12px);
    left: 8px;
    background: #dc2626;
    color: #ffffff;
    padding: 6px 18px;
    border-radius: 30px;
    border: 2px solid #ffffff;
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.35);
    font-size: 16px;
    font-weight: 700;
    white-space: nowrap;
    z-index: 200;
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .target-badge-bottom::after {
    content: '';
    position: absolute;
    bottom: 100%;
    left: 26px;
    width: 0;
    height: 0;
    border-left: 8px solid transparent;
    border-right: 8px solid transparent;
    border-bottom: 10px solid #dc2626;
  }
"""


def render_html_page(html_body, output_filename):
    full_html = f"""<!DOCTYPE html>
<html lang="bn">
<head>
<meta charset="UTF-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Hind+Siliguri:wght@500;600;700&family=Inter:wght@500;600;700&display=swap" rel="stylesheet">
<style>
{COMMON_CSS}
</style>
</head>
<body>
{html_body}
</body>
</html>"""

    out_path = os.path.join(OUTPUT_DIR, output_filename)
    with tempfile.NamedTemporaryFile(suffix=".html", delete=False, mode="w", encoding="utf-8") as tf:
        tf.write(full_html)
        temp_html = tf.name

    try:
        cmd = [
            CHROME_PATH,
            "--headless=new",
            "--disable-gpu",
            "--hide-scrollbars",
            "--window-size=1200,675",
            f"--screenshot={out_path}",
            f"file:///{temp_html.replace(os.sep, '/')}",
        ]
        subprocess.run(cmd, check=True, capture_output=True)

        with Image.open(out_path) as im:
            im.save(out_path, optimize=True)

        print(f"✅ Generated: {output_filename}")
        return out_path
    finally:
        if os.path.exists(temp_html):
            os.remove(temp_html)


# ==============================================================================
# 6 PIXEL-PERFECT STEP PAGES
# ==============================================================================

def step_1():
    """Step 1: Portal navigation."""
    body = """
    <div class="gov-header">
      <div class="gov-brand">
        <div class="gov-logo">🇧🇩</div>
        <div class="gov-title">
          <h1>মাধ্যমিক ও উচ্চমাধ্যমিক শিক্ষা বোর্ড, ঢাকা</h1>
          <p>বোর্ড অব ইন্টারমিডিয়েট অ্যান্ড সেকেন্ডারি এডুকেশন, ঢাকা | অফিশিয়াল পোর্টাল</p>
        </div>
      </div>
      <div class="gov-nav">
        <span>হোম</span>
        <span class="active">অনলাইন ই-সেবা (e-Services)</span>
        <span>সার্কুলার ও নোটিশ</span>
        <span>ফলাফল</span>
        <span>যোগাযোগ</span>
      </div>
    </div>
    <div class="main-canvas">
      <div>
        <div style="background: #ffffff; border-radius: 10px; padding: 16px 24px; border: 1px solid #e2e8f0; margin-bottom: 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.04);">
          <h2 style="font-size: 21px; color: #0f4c3a; font-weight: 700;">
            📋 শিক্ষাবোর্ড নাগরিক ই-সেবা ড্যাশবোর্ড (Online Citizen Services 2026)
          </h2>
          <p style="font-size: 14.5px; color: #64748b; margin-top: 4px;">অনলাইনে সনদপত্র ও তথ্যাদি সংশোধনের জন্য নিচের তালিকাভুক্ত নির্ধারিত সেবায় প্রবেশ করুন।</p>
        </div>

        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 18px;">
          <!-- Card 1: TARGET -->
          <div style="background: #eff6ff; border: 2px solid #3b82f6; border-radius: 12px; padding: 22px;">
            <span style="background: #2563eb; color: #ffffff; font-size: 12px; font-weight: 700; padding: 3px 10px; border-radius: 12px;">সর্বাধিক ব্যবহৃত</span>
            <h3 style="font-size: 18px; color: #1e3a8a; margin: 12px 0 8px 0; font-weight: 700;">নাম ও বয়স সংশোধন আবেদন</h3>
            <p style="font-size: 14px; color: #475569; line-height: 1.6; margin-bottom: 18px;">জেএসসি, এসএসসি ও এইচএসসি পরীক্ষার সনদপত্রের নাম, পিতার নাম, মাতার নাম ও জন্মতারিখ সংশোধন।</p>
            
            <div class="target-container" style="width: 100%;">
              <div class="target-badge-top">● ধাপ ১: 'নাম ও বয়স সংশোধন' অপশনে ক্লিক করুন</div>
              <div class="target-box" style="background: #2563eb; color: #ffffff; text-align: center; padding: 11px 16px; border-radius: 8px; font-size: 15.5px; font-weight: 700;">
                আবেদন করতে প্রবেশ করুন ➔
              </div>
            </div>
          </div>

          <!-- Card 2 -->
          <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 22px;">
            <span style="background: #64748b; color: #ffffff; font-size: 12px; font-weight: 700; padding: 3px 10px; border-radius: 12px;">সনদ সেবা</span>
            <h3 style="font-size: 18px; color: #334155; margin: 12px 0 8px 0; font-weight: 700;">হারানো বা ডুপ্লিকেট সনদ উত্তোলন</h3>
            <p style="font-size: 14px; color: #64748b; line-height: 1.6; margin-bottom: 18px;">মূল সনদ বা রেজিস্ট্রেশন কার্ড হারিয়ে গেলে ডুপ্লিকেট সনদের আবেদন করার সেবা।</p>
            <div style="background: #f1f5f9; color: #475569; text-align: center; padding: 11px 16px; border-radius: 8px; font-size: 15px; font-weight: 600;">
              বিস্তারিত দেখুন ➔
            </div>
          </div>

          <!-- Card 3 -->
          <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 22px;">
            <span style="background: #64748b; color: #ffffff; font-size: 12px; font-weight: 700; padding: 3px 10px; border-radius: 12px;">ভেরিফিকেশন</span>
            <h3 style="font-size: 18px; color: #334155; margin: 12px 0 8px 0; font-weight: 700;">অনলাইন সনদপত্র যাচাই (e-Verification)</h3>
            <p style="font-size: 14px; color: #64748b; line-height: 1.6; margin-bottom: 18px;">চাকরি ও বিদেশের জন্য শিক্ষা বোর্ডের মূল সনদপত্রের অনলাইন সত্যতা যাচাইকরণ সেবা।</p>
            <div style="background: #f1f5f9; color: #475569; text-align: center; padding: 11px 16px; border-radius: 8px; font-size: 15px; font-weight: 600;">
              যাচাই করুন ➔
            </div>
          </div>
        </div>
      </div>

      <div style="background: #f8fafc; border: 1px solid #e2e8f0; padding: 12px 20px; border-radius: 8px; font-size: 13.5px; color: #64748b; display: flex; justify-content: space-between;">
        <span>🌐 অফিশিয়াল ই-সেবা পোর্টাল লিংক: <strong>eservices.dhakaeducationboard.gov.bd</strong></span>
        <span>হেল্পলাইন: ১৬১২৩ | সাপোর্ট ইমেইল: support@dhakaeducationboard.gov.bd</span>
      </div>
    </div>
    """
    return render_html_page(body, "cert_step1_portal_access.png")


def step_2():
    """Step 2: Student search."""
    body = """
    <div class="gov-header">
      <div class="gov-brand">
        <div class="gov-logo">🇧🇩</div>
        <div class="gov-title">
          <h1>ঢাকা মাধ্যমিক ও উচ্চমাধ্যমিক শিক্ষা বোর্ড - ই-সেবা পোর্টাল</h1>
          <p>অনলাইন নাম ও বয়স সংশোধন শাখা (Name & Age Correction Wing)</p>
        </div>
      </div>
      <div class="gov-nav">
        <span>নির্দেশিকা</span>
        <span class="active">ফরম পূরণ</span>
        <span>আবেদন ট্র্যাকিং</span>
      </div>
    </div>
    <div class="main-canvas">
      <div style="background: #ffffff; border-radius: 12px; border: 1px solid #e2e8f0; padding: 24px 36px; box-shadow: 0 4px 14px rgba(0,0,0,0.05);">
        <div style="border-bottom: 2px solid #e2e8f0; padding-bottom: 14px; margin-bottom: 20px;">
          <span style="background: #dbeafe; color: #1e40af; font-size: 13px; font-weight: 700; padding: 4px 12px; border-radius: 12px;">ধাপ ০২: শিক্ষার্থী রেকর্ড অনুসন্ধান</span>
          <h2 style="font-size: 21px; color: #0f172a; margin-top: 6px; font-weight: 700;">পরীক্ষার তথ্য ও রোল-রেজিস্ট্রেশন দিয়ে ডাটাবেজ অনুসন্ধান</h2>
          <p style="font-size: 14px; color: #64748b;">বোর্ডের সেন্ট্রাল সার্ভার থেকে আপনার মূল সনদ রেকর্ডের ডাটা লোড করার জন্য সঠিক তথ্য প্রদান করুন।</p>
        </div>

        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 22px;">
          <div>
            <label style="font-size: 14.5px; font-weight: 700; color: #334155; display: block; margin-bottom: 6px;">পরীক্ষার নাম নির্বাচন করুন *</label>
            <div style="background: #f8fafc; border: 1.5px solid #94a3b8; border-radius: 8px; padding: 11px 16px; font-size: 15.5px; color: #0f172a; font-weight: 600;">
              SSC / সমমান পরীক্ষা (Secondary School Certificate)
            </div>
          </div>

          <div>
            <label style="font-size: 14.5px; font-weight: 700; color: #334155; display: block; margin-bottom: 6px;">পাসের সন (Passing Year) *</label>
            <div style="background: #f8fafc; border: 1.5px solid #94a3b8; border-radius: 8px; padding: 11px 16px; font-size: 15.5px; color: #0f172a; font-weight: 600;">
              2024
            </div>
          </div>

          <div>
            <label style="font-size: 14.5px; font-weight: 700; color: #334155; display: block; margin-bottom: 6px;">রোল নম্বর (Roll Number) *</label>
            <div style="background: #f8fafc; border: 1.5px solid #94a3b8; border-radius: 8px; padding: 11px 16px; font-size: 15.5px; color: #0f172a; font-weight: 600; font-family: monospace;">
              142857
            </div>
          </div>

          <div>
            <label style="font-size: 14.5px; font-weight: 700; color: #334155; display: block; margin-bottom: 6px;">রেজিস্ট্রেশন নম্বর (Registration Number) *</label>
            <div style="background: #f8fafc; border: 1.5px solid #94a3b8; border-radius: 8px; padding: 11px 16px; font-size: 15.5px; color: #0f172a; font-weight: 600; font-family: monospace;">
              1115283940
            </div>
          </div>
        </div>

        <!-- Target Button Area -->
        <div style="display: flex; gap: 16px; align-items: center; border-top: 1px dashed #e2e8f0; padding-top: 18px;">
          <div class="target-container">
            <div class="target-badge-top">● ধাপ ২: 'ডাটা খুঁজুন' বাটনে ক্লিক করুন</div>
            <div class="target-box" style="background: #2563eb; color: #ffffff; font-size: 16.5px; font-weight: 700; padding: 12px 30px; border-radius: 8px; text-align: center;">
              🔍 ডাটা খুঁজুন ও আবেদন ফরম খুলুন (Search Record)
            </div>
          </div>
          <div style="background: #ffffff; color: #64748b; border: 1.5px solid #cbd5e1; font-size: 15.5px; font-weight: 600; padding: 11px 22px; border-radius: 8px;">
            তথ্য রিসেট করুন
          </div>
          <span style="font-size: 13.5px; color: #059669; font-weight: 600; margin-left: auto;">✔ ঢাকা শিক্ষাবোর্ড ডাটাবেজ অনলাইন কানেক্টেড</span>
        </div>
      </div>

      <div style="background: #fef3c7; border: 1px solid #fde68a; border-radius: 8px; padding: 11px 20px; font-size: 13.5px; color: #92400e; display: flex; align-items: center; gap: 10px;">
        <span>💡</span> <strong>জরুরি নির্দেশ:</strong> জেএসসি ও এসএসসি সনদের তথ্যে মিল রাখার জন্য পূর্ববর্তী জেএসসি পাসের রোল ও রেজি নম্বর সাথে রাখুন।
      </div>
    </div>
    """
    return render_html_page(body, "cert_step2_student_search.png")


def step_3():
    """Step 3: Form filling."""
    body = """
    <div class="gov-header">
      <div class="gov-brand">
        <div class="gov-logo">🇧🇩</div>
        <div class="gov-title">
          <h1>ঢাকা মাধ্যমিক ও উচ্চমাধ্যমিক শিক্ষা বোর্ড - ই-সেবা পোর্টাল</h1>
          <p>অনলাইন নাম ও বয়স সংশোধন আবেদন ফরম (Online Correction Form 2026)</p>
        </div>
      </div>
      <div class="gov-nav">
        <span>রেকর্ড ভেরিফাইড ✔</span>
        <span class="active">সংশোধন এন্ট্রি</span>
        <span>ডকুমেন্ট আপলোড</span>
      </div>
    </div>
    <div class="main-canvas">
      <div style="background: #ffffff; border-radius: 12px; border: 1px solid #e2e8f0; padding: 22px 32px; box-shadow: 0 4px 14px rgba(0,0,0,0.05);">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px; border-bottom: 1.5px solid #e2e8f0; padding-bottom: 10px;">
          <div>
            <h2 style="font-size: 20px; color: #0f172a; font-weight: 700;">ধাপ ৩: বর্তমান তথ্য ও সংশোধিত সঠিক তথ্যের বিবরণ</h2>
            <p style="font-size: 13.5px; color: #64748b;">যে যে তথ্য সংশোধন করতে চান তার পাশে টিক দিন এবং অনলাইন জন্মনিবন্ধন অনুযায়ী প্রমিত বানান লিখুন।</p>
          </div>
          <span style="background: #dcfce7; color: #166534; font-size: 13px; font-weight: 700; padding: 4px 12px; border-radius: 20px;">শিক্ষার্থী: মোঃ রফিকুল ইসলাম | রোল: 142857</span>
        </div>

        <div style="border: 1px solid #e2e8f0; border-radius: 8px; overflow: hidden; margin-bottom: 18px;">
          <table style="width: 100%; border-collapse: collapse; font-size: 14.5px;">
            <thead>
              <tr style="background: #f8fafc; border-bottom: 1.5px solid #e2e8f0; color: #334155; text-align: left;">
                <th style="padding: 10px 14px;">বিবরণ</th>
                <th style="padding: 10px 14px;">বিদ্যমান ভুল রেকর্ড</th>
                <th style="padding: 10px 14px;">সংশোধন?</th>
                <th style="padding: 10px 14px;">সংশোধিত সঠিক নাম (বাংলা ও ইংরেজি)</th>
              </tr>
            </thead>
            <tbody>
              <!-- Row 1 -->
              <tr style="border-bottom: 1px solid #e2e8f0; background: #eff6ff;">
                <td style="padding: 10px 14px; font-weight: 700; color: #1e3a8a;">শিক্ষার্থীর নাম</td>
                <td style="padding: 10px 14px; color: #dc2626; font-weight: 600;">মোঃ রফিকুল ইসলম</td>
                <td style="padding: 10px 14px; text-align: center;"><input type="checkbox" checked style="width: 18px; height: 18px; accent-color: #2563eb;"></td>
                <td style="padding: 10px 14px;">
                  <div style="background: #ffffff; border: 1.5px solid #3b82f6; border-radius: 6px; padding: 6px 12px; font-weight: 700; color: #0f172a;">
                    মোঃ রফিকুল ইসলাম (MD. RAFIQUL ISLAM)
                  </div>
                </td>
              </tr>
              <!-- Row 2 -->
              <tr style="border-bottom: 1px solid #e2e8f0; background: #ffffff;">
                <td style="padding: 10px 14px; font-weight: 700; color: #1e3a8a;">পিতার নাম</td>
                <td style="padding: 10px 14px; color: #dc2626; font-weight: 600;">মোঃ আঃ রশিদ</td>
                <td style="padding: 10px 14px; text-align: center;"><input type="checkbox" checked style="width: 18px; height: 18px; accent-color: #2563eb;"></td>
                <td style="padding: 10px 14px;">
                  <div style="background: #f8fafc; border: 1.5px solid #94a3b8; border-radius: 6px; padding: 6px 12px; font-weight: 700; color: #0f172a;">
                    মোঃ আব্দুর রশিদ (MD. ABDUR RASHID)
                  </div>
                </td>
              </tr>
              <!-- Row 3 -->
              <tr style="background: #ffffff;">
                <td style="padding: 10px 14px; font-weight: 600; color: #475569;">মাতার নাম</td>
                <td style="padding: 10px 14px; color: #059669; font-weight: 600;">মোছাঃ রহিমা খাতুন</td>
                <td style="padding: 10px 14px; text-align: center;"><input type="checkbox" style="width: 18px; height: 18px;"></td>
                <td style="padding: 10px 14px; color: #94a3b8; font-style: italic;">অপরিবর্তিত থাকবে</td>
              </tr>
            </tbody>
          </table>
        </div>

        <div style="display: flex; justify-content: space-between; align-items: center; border-top: 1px solid #e2e8f0; padding-top: 14px;">
          <span style="font-size: 13.5px; color: #dc2626; font-weight: 600;">⚠️ সতর্কবাণী: NID ও জন্মনিবন্ধন অনুযায়ী ইংরেজি স্পেলিং ক্যাপিটাল লেটারে লিখুন।</span>
          
          <div class="target-container">
            <div class="target-badge-top">● ধাপ ৩: সঠিক বানান লিখে এখানে ক্লিক করুন</div>
            <div class="target-box" style="background: #2563eb; color: #ffffff; font-size: 16px; font-weight: 700; padding: 11px 28px; border-radius: 8px;">
              সংরক্ষণ করুন ও পরবর্তী ধাপে যান (Save & Next) ➔
            </div>
          </div>
        </div>
      </div>

      <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 10px 20px; font-size: 13.5px; color: #475569;">
        📌 <strong>নোট:</strong> একাধিক সংশোধন (যেমন: নিজের নাম + পিতার নাম) এক আবেদনেই একসাথে সিলেক্ট করা যায়।
      </div>
    </div>
    """
    return render_html_page(body, "cert_step3_correction_form.png")


def step_4():
    """Step 4: Uploading documents."""
    body = """
    <div class="gov-header">
      <div class="gov-brand">
        <div class="gov-logo">🇧🇩</div>
        <div class="gov-title">
          <h1>ঢাকা মাধ্যমিক ও উচ্চমাধ্যমিক শিক্ষা বোর্ড - ই-সেবা পোর্টাল</h1>
          <p>কাগজপত্র ও ডকুমেন্টস আপলোড সেকশন (Document Attachment Portal)</p>
        </div>
      </div>
      <div class="gov-nav">
        <span>ফরম সম্পন্ন ✔</span>
        <span class="active">ডকুমেন্টস আপলোড</span>
        <span>পেমেন্ট</span>
      </div>
    </div>
    <div class="main-canvas">
      <div style="background: #ffffff; border-radius: 12px; border: 1px solid #e2e8f0; padding: 22px 34px; box-shadow: 0 4px 14px rgba(0,0,0,0.05);">
        <div style="border-bottom: 2px solid #e2e8f0; padding-bottom: 12px; margin-bottom: 16px;">
          <h2 style="font-size: 21px; color: #0f172a; font-weight: 700;">ধাপ ৪: প্রয়োজনীয় এফিডেভিট, জন্মসনদ ও পেপার কাটিং আপলোড</h2>
          <p style="font-size: 14px; color: #64748b;">সকল ফাইলের স্পষ্ট স্ক্যান কপি সংযুক্ত করুন (ফরম্যাট: PDF / JPG, প্রতি ফাইলের সর্বোচ্চ সাইজ: 2 MB)।</p>
        </div>

        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 18px;">
          <!-- Doc 1 -->
          <div style="border: 1.5px dashed #94a3b8; background: #f8fafc; border-radius: 8px; padding: 12px 16px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
              <span style="font-weight: 700; font-size: 14.5px; color: #1e3a8a;">১. ১ম শ্রেণির ম্যাজিস্ট্রেট এফিডেভিট / নোটারি</span>
              <span style="color: #059669; font-weight: 700; font-size: 13px;">✔ আপলোড সম্পন্ন</span>
            </div>
            <div style="font-size: 13px; color: #64748b; font-family: monospace;">affidavit_first_class_magistrate.pdf (420 KB)</div>
          </div>

          <!-- Doc 2 -->
          <div style="border: 1.5px dashed #94a3b8; background: #f8fafc; border-radius: 8px; padding: 12px 16px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
              <span style="font-weight: 700; font-size: 14.5px; color: #1e3a8a;">২. জাতীয় দৈনিক পত্রিকায় বিজ্ঞপ্তির মূল কাটিং</span>
              <span style="color: #059669; font-weight: 700; font-size: 13px;">✔ আপলোড সম্পন্ন</span>
            </div>
            <div style="font-size: 13px; color: #64748b; font-family: monospace;">daily_ittefaq_notice_cutting.jpg (850 KB)</div>
          </div>

          <!-- Doc 3 -->
          <div style="border: 1.5px dashed #94a3b8; background: #f8fafc; border-radius: 8px; padding: 12px 16px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
              <span style="font-weight: 700; font-size: 14.5px; color: #1e3a8a;">৩. ১৭ ডিজিটের ডিজিটাল জন্মনিবন্ধন সনদ (BRIS)</span>
              <span style="color: #059669; font-weight: 700; font-size: 13px;">✔ আপলোড সম্পন্ন</span>
            </div>
            <div style="font-size: 13px; color: #64748b; font-family: monospace;">online_birth_certificate_17digit.pdf (310 KB)</div>
          </div>

          <!-- Doc 4 -->
          <div style="border: 1.5px dashed #94a3b8; background: #f8fafc; border-radius: 8px; padding: 12px 16px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">
              <span style="font-weight: 700; font-size: 14.5px; color: #1e3a8a;">৪. পিতা ও মাতার জাতীয় পরিচয়পত্র (NID)</span>
              <span style="color: #059669; font-weight: 700; font-size: 13px;">✔ আপলোড সম্পন্ন</span>
            </div>
            <div style="font-size: 13px; color: #64748b; font-family: monospace;">father_mother_nid_scanned.pdf (620 KB)</div>
          </div>
        </div>

        <!-- Target Button -->
        <div style="display: flex; justify-content: space-between; align-items: center; border-top: 1px solid #e2e8f0; padding-top: 16px;">
          <span style="font-size: 14px; color: #059669; font-weight: 600;">✔ ৪টি বাধ্যতামূলক ডকুমেন্টস সফলভাবে সংযুক্ত হয়েছে</span>
          
          <div class="target-container">
            <div class="target-badge-top">● ধাপ ৪: ফাইল জমা দিয়ে পেমেন্টে এগিয়ে যান</div>
            <div class="target-box" style="background: #2563eb; color: #ffffff; font-size: 16px; font-weight: 700; padding: 12px 30px; border-radius: 8px;">
              ডকুমেন্টস জমা দিয়ে ফি প্রদানের জন্য এগিয়ে যান ➔
            </div>
          </div>
        </div>
      </div>

      <div style="background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 8px; padding: 11px 20px; font-size: 13.5px; color: #1e40af;">
        📄 <strong>গুরুত্বপূর্ণ:</strong> এফিডেভিটের ক্ষেত্রে ৩০০ টাকার নন-জুডিশিয়াল স্ট্যাম্প ও আদালতের স্বাক্ষর স্পষ্ট দেখা যেতে হবে।
      </div>
    </div>
    """
    return render_html_page(body, "cert_step4_document_upload.png")


def step_5():
    """Step 5: Sonali e-Sheba payment."""
    body = """
    <div class="gov-header" style="background: #025955;">
      <div class="gov-brand">
        <div class="gov-logo" style="color: #025955;">🏦</div>
        <div class="gov-title">
          <h1>সোনালী ব্যাংক লিমিটেড - সোনালী পেমেন্ট গেটওয়ে (Sonali e-Sheba)</h1>
          <p>বাংলাদেশ শিক্ষাবোর্ড সরকারি ফি কালেকশন পোর্টাল | সিকিউর পেমেন্ট গেটওয়ে</p>
        </div>
      </div>
      <div class="gov-nav">
        <span>SSL Secured 🔒</span>
      </div>
    </div>
    <div class="main-canvas">
      <div style="background: #ffffff; border-radius: 12px; border: 1px solid #e2e8f0; padding: 22px 36px; box-shadow: 0 4px 14px rgba(0,0,0,0.05);">
        <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #e2e8f0; padding-bottom: 14px; margin-bottom: 20px;">
          <div>
            <h2 style="font-size: 21px; color: #025955; font-weight: 700;">ধাপ ৫: সোনালী সেবায় অনলাইন বোর্ড ফি পরিশোধ</h2>
            <p style="font-size: 14px; color: #64748b;">বিকাশ, নগদ, রকেট অথবা সোনালী ব্যাংক অ্যাকাউন্টের মাধ্যমে তাৎক্ষণিক ফি পরিশোধ করুন।</p>
          </div>
          <div style="background: #f0fdf4; border: 1.5px solid #86efac; border-radius: 10px; padding: 8px 18px; text-align: right;">
            <span style="font-size: 12px; color: #166534; font-weight: 700;">মোট প্রদেয় ফি (Total Payable)</span>
            <div style="font-size: 22px; font-weight: 700; color: #15803d;">৳ ১,৫০০.০০</div>
          </div>
        </div>

        <!-- Payment Methods Grid -->
        <div style="margin-bottom: 22px;">
          <label style="font-size: 15px; font-weight: 700; color: #334155; display: block; margin-bottom: 12px;">পেমেন্ট মেথড নির্বাচন করুন *</label>
          <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px;">
            <!-- Bkash: Active Target -->
            <div style="background: #fdf2f8; border: 2.5px solid #db2777; border-radius: 10px; padding: 14px; text-align: center;">
              <div style="font-size: 22px;">📱</div>
              <div style="font-size: 16px; font-weight: 700; color: #db2777; margin-top: 4px;">বিকাশ (bKash)</div>
              <div style="font-size: 12px; color: #059669; font-weight: 600;">✔ নির্বাচিত</div>
            </div>

            <!-- Nagad -->
            <div style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 10px; padding: 14px; text-align: center;">
              <div style="font-size: 22px;">📲</div>
              <div style="font-size: 16px; font-weight: 700; color: #ea580c; margin-top: 4px;">নগদ (Nagad)</div>
              <div style="font-size: 12px; color: #64748b;">ইনস্ট্যান্ট ফি</div>
            </div>

            <!-- Rocket -->
            <div style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 10px; padding: 14px; text-align: center;">
              <div style="font-size: 22px;">💳</div>
              <div style="font-size: 16px; font-weight: 700; color: #7c3aed; margin-top: 4px;">রকেট (Rocket)</div>
              <div style="font-size: 12px; color: #64748b;">DBBL ওয়ালেট</div>
            </div>

            <!-- Sonali Bank -->
            <div style="background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 10px; padding: 14px; text-align: center;">
              <div style="font-size: 22px;">🏛️</div>
              <div style="font-size: 16px; font-weight: 700; color: #0f4c3a; margin-top: 4px;">সোনালী ব্যাংক</div>
              <div style="font-size: 12px; color: #64748b;">অ্যাকাউন্ট / কার্ড</div>
            </div>
          </div>
        </div>

        <!-- Target Pay Button -->
        <div style="display: flex; justify-content: space-between; align-items: center; border-top: 1px solid #e2e8f0; padding-top: 16px;">
          <span style="font-size: 13.5px; color: #64748b;">আবেদন ট্র্যাকিং রেফারেন্স: <strong>DEB-2026-78491</strong></span>
          
          <div class="target-container">
            <div class="target-badge-top">● ধাপ ৫: ফি পরিশোধ করতে এখানে ক্লিক করুন</div>
            <div class="target-box" style="background: #025955; color: #ffffff; font-size: 17px; font-weight: 700; padding: 13px 36px; border-radius: 8px;">
              বিকাশ দিয়ে ফি পরিশোধ করুন (Pay ৳ 1,500 via bKash) ➔
            </div>
          </div>
        </div>
      </div>

      <div style="background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 8px; padding: 11px 20px; font-size: 13.5px; color: #166534;">
        🔒 <strong>নিরাপদ লেনদেন:</strong> সোনালী ই-সেবার মাধ্যমে টাকা পরিশোধের সাথে সাথে মোবাইল নম্বরে এসএমএস কনফার্মেশন পাঠানো হয়।
      </div>
    </div>
    """
    return render_html_page(body, "cert_step5_sonali_payment.png")


def step_6():
    """Step 6: Tracking slip download."""
    body = """
    <div class="gov-header">
      <div class="gov-brand">
        <div class="gov-logo">🇧🇩</div>
        <div class="gov-title">
          <h1>ঢাকা মাধ্যমিক ও উচ্চমাধ্যমিক শিক্ষা বোর্ড - ই-সেবা পোর্টাল</h1>
          <p>অনলাইন আবেদন সফল ও ট্র্যাকিং ড্যাশবোর্ড (Application Tracking Status 2026)</p>
        </div>
      </div>
      <div class="gov-nav">
        <span class="active">আবেদন স্ট্যাটাস</span>
        <span>লগআউট</span>
      </div>
    </div>
    <div class="main-canvas">
      <div style="background: #ffffff; border-radius: 12px; border: 1px solid #e2e8f0; padding: 24px 36px; box-shadow: 0 4px 14px rgba(0,0,0,0.05);">
        <div style="display: flex; align-items: center; gap: 14px; background: #f0fdf4; border: 1.5px solid #86efac; border-radius: 10px; padding: 14px 20px; margin-bottom: 20px;">
          <div style="font-size: 32px;">🎉</div>
          <div>
            <h2 style="font-size: 20px; color: #15803d; font-weight: 700;">অভিনন্দন! আপনার আবেদনটি সফলভাবে গৃহীত ও ফি পরিশোধিত হয়েছে</h2>
            <p style="font-size: 14px; color: #166534;">আপনার আবেদনটি শিক্ষাবোর্ডের 'নাম ও বয়স সংশোধন কমিটি'র পর্যালোচনার জন্য জমা হয়েছে।</p>
          </div>
        </div>

        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 18px; margin-bottom: 22px;">
          <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 14px 18px;">
            <span style="font-size: 13px; color: #64748b; font-weight: 600;">আবেদন আইডি (Application ID)</span>
            <div style="font-size: 19px; font-weight: 700; color: #1e3a8a; font-family: monospace; margin-top: 4px;">DEB-2026-78491</div>
          </div>

          <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 14px 18px;">
            <span style="font-size: 13px; color: #64748b; font-weight: 600;">সিকিউরিটি পাসকোড (Security PIN)</span>
            <div style="font-size: 19px; font-weight: 700; color: #0f172a; font-family: monospace; margin-top: 4px;">9842</div>
          </div>

          <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 14px 18px;">
            <span style="font-size: 13px; color: #64748b; font-weight: 600;">বর্তমান স্ট্যাটাস (Current Status)</span>
            <div style="font-size: 16px; font-weight: 700; color: #b45309; margin-top: 4px;">⏳ কমিটি সভার জন্য অপেক্ষমাণ</div>
          </div>
        </div>

        <!-- Target Button: Download Tracking Slip -->
        <div style="display: flex; gap: 16px; align-items: center; border-top: 1px dashed #e2e8f0; padding-top: 20px;">
          <div class="target-container">
            <div class="target-badge-top">● ধাপ ৬: ট্র্যাকিং স্লিপ ডাউনলোড করতে এখানে ক্লিক করুন</div>
            <div class="target-box" style="background: #059669; color: #ffffff; font-size: 17px; font-weight: 700; padding: 13px 34px; border-radius: 8px; text-align: center;">
              📄 অফিসিয়াল আবেদন রসিদ ও ট্র্যাকিং স্লিপ ডাউনলোড করুন (Download Slip)
            </div>
          </div>
          <div style="background: #ffffff; color: #1e40af; border: 1.5px solid #bfdbfe; font-size: 16px; font-weight: 600; padding: 12px 24px; border-radius: 8px;">
            🔍 অনলাইনে স্ট্যাটাস ট্র্যাক করুন
          </div>
        </div>
      </div>

      <div style="background: #fef2f2; border: 1px solid #fecaca; border-radius: 8px; padding: 12px 20px; font-size: 13.5px; color: #991b1b; display: flex; align-items: center; gap: 10px;">
        <span>⚠️</span> <strong>জরুরি সতর্কবার্তা:</strong> ট্র্যাকিং স্লিপটি প্রিন্ট করে সংরক্ষণ করুন। পরবর্তীতে বোর্ড মিটিংয়ে উপস্থিতির সময় এই স্লিপ প্রদর্শন বাধ্যতামূলক।
      </div>
    </div>
    """
    return render_html_page(body, "cert_step6_tracking_receipt.png")


def main():
    print("=" * 70)
    print("🚀 Rendering 6 Pixel-Perfect Tutorial Step Screenshots...")
    print("=" * 70)

    p1 = step_1()
    p2 = step_2()
    p3 = step_3()
    p4 = step_4()
    p5 = step_5()
    p6 = step_6()

    print("=" * 70)
    print("🎉 All 6 Screenshots Successfully Generated!")
    print("=" * 70)


if __name__ == "__main__":
    main()
