#!/usr/bin/env python3
"""
Builds the complete 2026 flagship tutorial post for:
"ঘরে বসেই সার্টিফিকেট নাম ও বয়স সংশোধনের সঠিক নিয়ম (২০২৬)"
Includes all 6 annotated interface step cards, legal drafting templates,
fee schedule, troubleshooting guide, FAQs, and valid HowTo + FAQPage Schema.
"""

import json
import os
import sys

try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUTPUT_FILE = os.path.join(PROJECT_ROOT, "output_posts", "revived_posts", "how-to-correction-certificate-name-2025.html")
METADATA_FILE = os.path.join(PROJECT_ROOT, "output_posts", "revived_posts", "how-to-correction-certificate-name-2025_metadata.json")

CDN_PREFIX = "https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images"

HTML_CONTENT = f"""<!DOCTYPE html>
<html lang="bn">
<head>
  <meta charset="UTF-8">
  <title>ঘরে বসেই সার্টিফিকেট নাম ও বয়স সংশোধনের সঠিক নিয়ম (২০২৬)</title>
  <meta name="description" content="জেএসসি, এসএসসি ও এইচএসসি সার্টিফিকেটের নিজের নাম, পিতা-মাতার নাম বা বয়স সংশোধনের অনলাইন আবেদন নিয়ম, ফি ও প্রয়োজনীয় কাগজপত্রের তালিকা পড়ুন HelpTrickBD-তে।">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/fonts/solaiman_lipi.css">

<style>
  .htbd-post-wrapper,
  .htbd-post-wrapper * {{
    font-family: 'SolaimanLipi', Arial, sans-serif !important;
  }}
  .htbd-post-wrapper {{
    color: #202124 !important;
    line-height: 1.85 !important;
  }}
  .htbd-post-wrapper p {{
    font-size: 18px !important;
    line-height: 1.85 !important;
    color: #202124 !important;
    margin: 16px 0 !important;
    text-align: justify !important;
  }}
  .htbd-heading {{
    color: #1a73e8 !important;
    border-left: 5px solid #1a73e8 !important;
    border-bottom: none !important;
    padding-left: 14px !important;
    margin-top: 38px !important;
    margin-bottom: 16px !important;
    font-size: 23px !important;
    font-weight: 700 !important;
    line-height: 1.4 !important;
  }}
  .htbd-toc-box {{
    background: #f8fafd !important;
    border: 1px solid #d2e3fc !important;
    border-radius: 10px !important;
    padding: 20px 24px !important;
    margin: 25px 0 !important;
    box-shadow: 0 1px 4px rgba(26,115,232,0.06) !important;
  }}
  .htbd-toc-list {{
    list-style: none !important;
    list-style-type: none !important;
    padding-left: 0 !important;
    margin: 12px 0 0 0 !important;
  }}
  .htbd-toc-list li {{
    padding: 7px 0 !important;
    border-bottom: 1px dashed #e8eaed !important;
    font-size: 16.5px !important;
  }}
  .htbd-toc-list li:last-child {{
    border-bottom: none !important;
  }}
  .htbd-toc-list li a {{
    color: #1a73e8 !important;
    text-decoration: none !important;
    font-weight: 500 !important;
  }}
  .htbd-toc-list li a:hover {{
    color: #0d47a1 !important;
    text-decoration: underline !important;
  }}
  .htbd-qbox {{
    background: #f8f9fa !important;
    border-left: 5px solid #1a73e8 !important;
    padding: 20px 24px !important;
    margin: 22px 0 !important;
    border-radius: 0 8px 8px 0 !important;
    box-shadow: 0 1px 4px rgba(0,0,0,0.06) !important;
  }}
  .htbd-table-wrapper {{
    overflow-x: auto !important;
    margin: 25px 0 !important;
    border-radius: 8px !important;
    border: 1px solid #e0e0e0 !important;
  }}
  .htbd-table {{
    width: 100% !important;
    border-collapse: collapse !important;
    background: #ffffff !important;
  }}
  .htbd-table th {{
    background-color: #1a73e8 !important;
    color: #ffffff !important;
    font-weight: 700 !important;
    padding: 14px 18px !important;
    text-align: left !important;
    font-size: 16px !important;
  }}
  .htbd-table td {{
    padding: 13px 18px !important;
    border-bottom: 1px solid #eeeeee !important;
    font-size: 15.5px !important;
    color: #333333 !important;
  }}
  .htbd-table tr:nth-child(even) {{
    background-color: #f8f9fa !important;
  }}

  /* Step Cards */
  .htbd-tutorial-step-card {{
    background: #ffffff !important;
    border: 1.5px solid #e2e8f0 !important;
    border-radius: 12px !important;
    padding: 24px 28px !important;
    margin: 32px 0 !important;
    box-shadow: 0 4px 16px rgba(0,0,0,0.05) !important;
  }}
  .htbd-step-header {{
    display: flex !important;
    align-items: center !important;
    gap: 14px !important;
    margin-bottom: 16px !important;
  }}
  .htbd-step-num {{
    background: #2563eb !important;
    color: #ffffff !important;
    padding: 6px 16px !important;
    border-radius: 24px !important;
    font-weight: 700 !important;
    font-size: 15px !important;
    letter-spacing: 0.3px !important;
  }}
  .htbd-step-title {{
    margin: 0 !important;
    font-size: 20px !important;
    color: #0f172a !important;
    font-weight: 700 !important;
  }}
  .htbd-step-img {{
    width: 100% !important;
    max-width: 100% !important;
    height: auto !important;
    border-radius: 10px !important;
    border: 1.5px solid #cbd5e1 !important;
    box-shadow: 0 6px 18px rgba(0,0,0,0.08) !important;
    display: block !important;
    margin: 16px auto !important;
  }}
  .htbd-step-caption {{
    font-size: 14px !important;
    color: #64748b !important;
    margin-top: 8px !important;
    font-style: italic !important;
    text-align: center !important;
  }}
  .htbd-tip-box {{
    background: #eff6ff !important;
    border-left: 4px solid #2563eb !important;
    padding: 12px 18px !important;
    border-radius: 0 8px 8px 0 !important;
    font-size: 15.5px !important;
    color: #1e40af !important;
    margin-top: 18px !important;
  }}

  /* Document Draft Box */
  .htbd-draft-box {{
    background: #fdfbf7 !important;
    border: 1.5px solid #e7d8c5 !important;
    border-radius: 8px !important;
    padding: 18px 22px !important;
    margin: 20px 0 !important;
    font-size: 16px !important;
    line-height: 1.9 !important;
    color: #3b2a1a !important;
  }}
</style>

<div class="htbd-post-wrapper">
  <div style="margin-bottom: 18px;">
    <span class="htbd-badge" style="background: #e8f0fe; color: #1a73e8; padding: 6px 14px; border-radius: 20px; font-weight: 600; font-size: 14px; display: inline-block;">
      📚 বিভাগ: শিক্ষা সহায়িকা ও নাগরিক ই-সেবা | সংস্করণ: ২০২৬ | ঘরে বসে অনলাইন গাইডলাইন
    </span>
  </div>

  <!-- Hero Thumbnail Banner -->
  <div style="text-align: center; margin: 18px 0 25px 0;">
    <img src="{CDN_PREFIX}/thumbnails/thumb_certificate_correction_2026.png" 
         alt="ঘরে বসেই সার্টিফিকেট নাম ও বয়স সংশোধনের সঠিক নিয়ম ২০২৬" 
         title="সার্টিফিকেট নাম ও বয়স সংশোধন অনলাইন আবেদন"
         width="1200" height="675"
         loading="eager"
         style="width: 100%; max-width: 100%; height: auto; border-radius: 10px; box-shadow: 0 4px 14px rgba(0,0,0,0.12); display: block; margin: 0 auto;"/>
    <span style="display: block; font-size: 14px; color: #5f6368; margin-top: 8px; font-style: italic;">
      চিত্র: বাংলাদেশের শিক্ষাবোর্ডসমূহে সার্টিফিকেট নাম, পিতা-মাতার নাম ও বয়স সংশোধনের অনলাইন পদ্ধতি (২০২৬)
    </span>
  </div>

  <div class="htbd-qbox">
    <p style="margin: 0; font-size: 18px; line-height: 1.8;">
      <strong>📌 সারসংক্ষেপ (Quick Overview):</strong> 
      <strong>সার্টিফিকেট নাম ও বয়স সংশোধন</strong> হলো বাংলাদেশের শিক্ষা বোর্ডগুলোর (যেমন—ঢাকা, রাজশাহী, চট্টগ্রাম, কুমিল্লা ইত্যাদি) নির্ধারিত অফিসিয়াল ই-সার্ভিস পোর্টালের মাধ্যমে পিএসসি, জেএসসি, এসএসসি ও এইচএসসি পরীক্ষার সনদপত্রে বিদ্যমান নামের বানান ভুল, পিতা-মাতার নামের অসঙ্গতি কিংবা জন্মতারিখ সংশোধন করার একটি সমন্বিত আইনি ও প্রশাসনিক প্রক্রিয়া। ২০২৬ সালের হালনাগাদ নিয়মে সম্পূর্ণ প্রক্রিয়াটি ঘরে বসেই অনলাইনে সোনালী সেবার মাধ্যমে ফি পরিশোধ, ডিজিটাল জন্মসনদ ভেরিফিকেশন ও এফিডেভিট আপলোড করে সম্পন্ন করা যায়। নিচে প্রামাণ্য নথিপত্র, এফিডেভিটের খসড়া বয়ান এবং <strong>প্রতিটি ধাপের অরিজিনাল ইন্টারফেস স্ক্রিনশট ও লাল ক্লিক মার্কারসহ</strong> পূর্ণাঙ্গ নির্দেশিকা তুলে ধরা হলো।
    </p>
  </div>

  <!--more-->

  <div class="htbd-toc-box">
    <h3 style="margin-top: 0; color: #1a73e8; border-bottom: 2px solid #e8f0fe; padding-bottom: 10px; font-size: 20px; font-weight: 700;">📑 সূচিপত্র (Table of Contents)</h3>
    <ul class="htbd-toc-list">
      <li><a href="#need">👉 ১. সার্টিফিকেট সংশোধনের প্রয়োজনীয়তা ও সাধারণ জটিলতাসমূহ</a></li>
      <li><a href="#documents">👉 ২. প্রয়োজনীয় কাগজপত্র ও দলিলের পূর্ণাঙ্গ চেকলিস্ট</a></li>
      <li><a href="#affidavit-sample">👉 ৩. ১ম শ্রেণির ম্যাজিস্ট্রেট এফিডেভিট ও পত্রিকায় বিজ্ঞপ্তির আইনি নমুনা বয়ান</a></li>
      <li><a href="#step-by-step">👉 ৪. ধাপে ধাপে অনলাইন আবেদন নির্দেশিকা (৬টি ইন্টারফেস স্ক্রিনশটসহ)</a></li>
      <li><a href="#fees-table">👉 ৫. বিভিন্ন শিক্ষাবোর্ডের ফি ও সম্ভাব্য সময়সীমার তথ্য ছক</a></li>
      <li><a href="#board-hearing">👉 ৬. বোর্ড মিটিংয়ের শুনানি, সাক্ষাৎকার ও নতুন মূল সনদ উত্তোলন</a></li>
      <li><a href="#troubleshooting">👉 ৭. সাধারণ ভুল ও টেকনিক্যাল ট্রাবলশুটিং গাইড</a></li>
      <li><a href="#faqs">👉 ৮. সচরাচর জিজ্ঞাসিত প্রশ্ন (FAQ)</a></li>
    </ul>
  </div>

  <h2 id="need" class="htbd-heading">১. সার্টিফিকেট সংশোধনের প্রয়োজনীয়তা ও সাধারণ জটিলতাসমূহ</h2>
  <p>আমাদের দেশের স্কুল বা মাদ্রাসার প্রাথমিক রেজিস্ট্রেশনের সময় অনেক ক্ষেত্রেই অসাবধানতাবশত শিক্ষার্থীর নাম, পিতার নাম, মাতার নাম কিংবা জন্মতারিখে টাইপিং ভুল হয়ে থাকে। পরবর্তীতে যখন শিক্ষার্থী জাতীয় পরিচয়পত্র (NID), পাসপোর্ট তৈরি কিংবা ডিজিটাল জন্মনিবন্ধন (BRIS) গ্রহণ করতে যায়, তখন শিক্ষাগত সনদের তথ্যের সাথে সরকারি ডেটাবেজের বড় ধরনের অমিল ধরা পড়ে।</p>
  <p>বিশেষ করে বিসিএস বা অন্যান্য সরকারি চাকরির পুলিশ ভেরিফিকেশন, ব্যাংক ড্রাফট উত্তোলন, কিংবা বিদেশে উচ্চশিক্ষার ভিসা প্রসেসিংয়ের ক্ষেত্রে নামের বানানে মাত্র একটি অক্ষরের ভুল থাকলেও পুরো আবেদন বাতিল হয়ে যেতে পারে। তাই ভুল চিহ্নিত হওয়ার সাথে সাথেই শিক্ষাবোর্ডের নির্ধারিত আইনসম্মত পদ্ধতিতে সংশোধন করিয়ে নেওয়া প্রতিটি শিক্ষার্থীর জন্য অত্যন্ত জরুরি।</p>

  <h2 id="documents" class="htbd-heading">২. প্রয়োজনীয় কাগজপত্র ও দলিলের পূর্ণাঙ্গ চেকলিস্ট</h2>
  <p>অনলাইনে আবেদন শুরু করার পূর্বে নিচের নথিপত্রগুলোর মূল কপি স্ক্যান করে নির্দিষ্ট ফোল্ডারে প্রস্তুত রাখুন:</p>
  <ul>
    <li><strong>১. মূল শিক্ষাগত সনদসমূহ:</strong> জেএসসি/এসএসসি/এইচএসসি পরীক্ষার মূল রেজিস্ট্রেশন কার্ড, এডমিট কার্ড, নম্বরপত্র (মার্কশিট) এবং মূল সার্টিফিকেট বা সাময়িক সনদ।</li>
    <li><strong>২. ১৭ ডিজিটের ডিজিটাল জন্মনিবন্ধন:</strong> স্থানীয় সরকার বিভাগের BRIS অনলাইন ডেটাবেজে নিবন্ধিত বাংলা ও ইংরেজি উভয় ভাষার অনলাইন ভেরিফায়েড জন্মসনদ।</li>
    <li><strong>৩. পিতা ও মাতার জাতীয় পরিচয়পত্র:</strong> পিতা ও মাতার স্মার্ট এনআইডি কার্ডের রঙিন ও স্পষ্ট স্ক্যান কপি।</li>
    <li><strong>৪. ১ম শ্রেণির জুডিশিয়াল ম্যাজিস্ট্রেট এফিডেভিট:</strong> আদালতের ফার্স্ট ক্লাস ম্যাজিস্ট্রেট বা নোটারি পাবলিক কর্তৃক সম্পাদিত ৩০০ টাকার নন-জুডিশিয়াল স্ট্যাম্পের মূল হলফনামা।</li>
    <li><strong>৫. জাতীয় দৈনিক পত্রিকার মূল বিজ্ঞপ্তি:</strong> একটি বহুল প্রচারিত জাতীয় বাংলা দৈনিক পত্রিকায় প্রকাশিত নাম/বয়স সংশোধন সংক্রান্ত মূল বিজ্ঞপ্তির সম্পূর্ণ পাতার পেপার কাটিং।</li>
    <li><strong>৬. শিক্ষাপ্রতিষ্ঠানের প্রধানের প্রত্যয়নপত্র:</strong> যে প্রতিষ্ঠান থেকে পরীক্ষা উত্তীর্ণ হয়েছেন, সেই প্রতিষ্ঠানের প্রধান শিক্ষক বা অধ্যক্ষ কর্তৃক স্বাক্ষরিত প্রাতিষ্ঠানিক সুপারিশপত্র।</li>
  </ul>

  <div class="htbd-link-box" style="margin: 25px 0; padding: 15px 20px; background: #f0f7ff; border-left: 5px solid #1a73e8; border-radius: 6px;">
    <strong style="color: #1a73e8; font-size: 17px; display: block; margin-bottom: 8px;">📖 সম্পর্কিত আরো গুরুত্বপূর্ণ আর্টিকেল পড়ুন:</strong>
    <ul style="margin: 0; padding-left: 20px; line-height: 1.8;">
      <li><a href="https://www.helptrickbd.com/2026/01/what-is-patriarchy-definition-characteristics-impact.html" target="_blank" rel="noopener">📌 পিতৃতন্ত্র কাকে বলে? সমাজতাত্ত্বিক সংজ্ঞা, উৎপত্তি ও বৈশিষ্ট্য</a></li>
      <li><a href="https://www.helptrickbd.com/2025/01/namta-1-to-20.html" target="_blank" rel="noopener">📌 নামতা ১ থেকে ২০ পর্যন্ত সহজে মুখস্থ করার চার্ট ও টেকনিক</a></li>
      <li><a href="https://www.helptrickbd.com/2025/12/sher-e-bangla-fazlul-haque-social-welfare.html" target="_blank" rel="noopener">📌 শেরে বাংলা এ কে ফজলুল হকের সমাজকল্যাণমূলক অবদান</a></li>
    </ul>
  </div>

  <h2 id="affidavit-sample" class="htbd-heading">৩. ১ম শ্রেণির ম্যাজিস্ট্রেট এফিডেভিট ও পত্রিকায় বিজ্ঞপ্তির আইনি নমুনা বয়ান</h2>
  <p>সার্টিফিকেট সংশোধনের আইনি ভিত্তি তৈরি হয় আদালতের এফিডেভিট এবং সংবাদপত্রের উন্মুক্ত বিজ্ঞপ্তির মাধ্যমে। নিচে উভয় নথির জন্য নির্ভুল খসড়া বয়ান প্রদান করা হলো:</p>

  <h3 style="font-size: 19px; color: #1e3a8a; margin-top: 22px;">ক) ১ম শ্রেণির ম্যাজিস্ট্রেট এফিডেভিট (হলফনামার নমুনা)</h3>
  <div class="htbd-draft-box">
    <strong>হলফনামার মূল বয়ান (৩০০ টাকার স্ট্যাম্পে মুদ্রণযোগ্য):</strong><br>
    "আমি নিম্নস্বাক্ষরকারী [আপনার নাম], পিতা: [পিতার নাম], মাতা: [মাতার নাম], সাং: [গ্রাম/মহল্লা], ডাকঘর: [ডাকঘর], উপজেলা: [উপজেলা], জেলা: [জেলা]—এই মর্মে শপথপূর্বক ঘোষণা করিতেছি যে, আমার এসএসসি পরীক্ষা পাসের মূল সনদ ও রেজিস্ট্রেশন কার্ডে অসাবধানতাবশত আমার নামের বানান ভুলক্রমে <em>'মোঃ রফিকুল ইসলম'</em> লিপিবদ্ধ হইয়াছে। অথচ আমার ডিজিটাল জন্মনিবন্ধন সনদ ও পারিবারিক রেকর্ড অনুযায়ী আমার প্রকৃত ও শুদ্ধ নাম <strong>'মোঃ রফিকুল ইসলাম' (ইংরেজিতে: MD. RAFIQUL ISLAM)</strong>। অতএব আমি অত্র হলফনামার মাধ্যমে ঘোষণা করিতেছি যে, এখন হইতে আমার সকল শিক্ষাগত সনদ ও দাপ্তরিক নথিতে সংশোধিত শুদ্ধ নাম কার্যকর হইবে।"
  </div>

  <h3 style="font-size: 19px; color: #1e3a8a; margin-top: 22px;">খ) জাতীয় পত্রিকায় বিজ্ঞপ্তির সঠিক নমুনা বয়ান</h3>
  <div class="htbd-draft-box">
    <strong>বিজ্ঞপ্তির বয়ান (যেকোনো জাতীয় দৈনিকের জন্য):</strong><br>
    "এতদ্বারা সর্বসাধারণের অবগতির জন্য জানানো যাইতেছে যে, আমি [আপনার বর্তমান নাম], পিতা: [পিতার নাম], মাতা: [মাতার নাম], ঢাকা শিক্ষাবোর্ডের অধীনে ২০২৪ সনের এসএসসি পরীক্ষায় [বিদ্যালয়ের নাম] হইতে অংশগ্রহণ করিয়া উত্তীর্ণ হই (রোল নং: ১৪২৮৫৭, রেজি নং: ১১১৫২৮৩৯৪০)। আমার সনদে নামের বানান ভুলবশত <em>'মোঃ রফিকুল ইসলম'</em> লিপিবদ্ধ হইয়াছে। বিজ্ঞ ১ম শ্রেণির জুডিশিয়াল ম্যাজিস্ট্রেট আদালত, ঢাকার এফিডেভিট নং [নম্বর/তারিখ] মূলে আমার নাম সংশোধনপূর্বক <strong>'মোঃ রফিকুল ইসলাম' (MD. RAFIQUL ISLAM)</strong> করা হইল। ভবিষ্যতে সর্বক্ষেত্রে ইহা ব্যবহৃত হইবে।"
  </div>

  <h2 id="step-by-step" class="htbd-heading">৪. ধাপে ধাপে অনলাইন আবেদন নির্দেশিকা (৬টি ইন্টারফেস স্ক্রিনশটসহ)</h2>
  <p>বাংলাদেশ শিক্ষাবোর্ডের অনলাইন পোর্টালে ঘরে বসেই কীভাবে আবেদন করবেন, তা নিচের ৬টি কার্ডে বিস্তারিত দেখানো হলো। প্রতিটি স্ক্রিনশটের <strong>লাল চিহ্নিত বর্ডার ও নির্দেশক তীর</strong> খেয়াল করুন:</p>

  <!-- STEP 1 -->
  <div class="htbd-tutorial-step-card">
    <div class="htbd-step-header">
      <span class="htbd-step-num">ধাপ ০১</span>
      <h3 class="htbd-step-title">শিক্ষা বোর্ডের অফিসিয়াল ই-সেবা পোর্টালে প্রবেশ ও মেনু নির্বাচন</h3>
    </div>
    <p>প্রথমে আপনার কম্পিউটার বা মোবাইলের ব্রাউজার থেকে ঢাকা শিক্ষা বোর্ডের অফিসিয়াল ই-সেবা পোর্টাল (<strong>eservices.dhakaeducationboard.gov.bd</strong>)-এ প্রবেশ করুন। হোমপেজের নাগরিক সেবা গ্রিড থেকে 'নাম ও বয়স সংশোধন আবেদন' কার্ডে থাকা নীল বাটনে ক্লিক করুন।</p>
    
    <figure style="margin: 20px 0; text-align: center;">
      <img src="{CDN_PREFIX}/tutorials/cert_step1_portal_access.png" 
           alt="ঢাকা শিক্ষা বোর্ড ই-সেবা পোর্টালে নাম ও বয়স সংশোধন মেনু নির্বাচন ধাপ ১" 
           title="ই-সেবা ড্যাশবোর্ডে আবেদন বাটনে ক্লিক করুন" 
           loading="lazy" 
           width="1200" height="675"
           class="htbd-step-img">
      <figcaption class="htbd-step-caption">
        📷 চিত্র ১: লাল বক্স চিহ্নিত 'আবেদন করতে প্রবেশ করুন' বাটনে ক্লিক করে পরবর্তী ধাপে প্রবেশ করুন।
      </figcaption>
    </figure>

    <div class="htbd-tip-box">
      💡 <strong>জরুরি টিপস:</strong> অন্যান্য সাধারণ শিক্ষাবোর্ড (যেমন: রাজশাহী, কুমিল্লা, চট্টগ্রাম, যশোর, দিনাজপুর, বরিশাল, সিলেট, ময়মনসিংহ) এবং মাদ্রাসা বোর্ডের নিজস্ব পোর্টালেও একইভাবে 'অনলাইন নাম সংশোধন' মেনু পাওয়া যায়।
    </div>
  </div>

  <!-- STEP 2 -->
  <div class="htbd-tutorial-step-card">
    <div class="htbd-step-header">
      <span class="htbd-step-num">ধাপ ০২</span>
      <h3 class="htbd-step-title">পরীক্ষার সন, রোল ও রেজিস্ট্রেশন নম্বর দিয়ে ডাটাবেজ অনুসন্ধান</h3>
    </div>
    <p>এই ধাপে একটি সার্চ ফরম প্রদর্শিত হবে। ড্রপডাউন মেনু থেকে আপনার পরীক্ষার নাম (জেএসসি/এসএসসি/এইচএসসি), পাসের সন (যেমন: ২০২৪) নির্বাচন করুন এবং এডমিট কার্ড দেখে রোল ও রেজিস্ট্রেশন নম্বর নির্ভুলভাবে টাইপ করুন। এরপর নীল রঙের 'ডাটা খুঁজুন' বাটনে ক্লিক করুন।</p>
    
    <figure style="margin: 20px 0; text-align: center;">
      <img src="{CDN_PREFIX}/tutorials/cert_step2_student_search.png" 
           alt="শিক্ষার্থীর রোল ও রেজিস্ট্রেশন দিয়ে ডাটাবেজ অনুসন্ধান ধাপ ২" 
           title="ডাটা খুঁজুন ও আবেদন ফরম খুলুন বাটনে ক্লিক করুন" 
           loading="lazy" 
           width="1200" height="675"
           class="htbd-step-img">
      <figcaption class="htbd-step-caption">
        📷 চিত্র ২: লাল বক্স চিহ্নিত 'ডাটা খুঁজুন ও আবেদন ফরম খুলুন' বাটনে ক্লিক করে সেন্ট্রাল সার্ভার থেকে ডাটা লোড করুন।
      </figcaption>
    </figure>

    <div class="htbd-tip-box">
      💡 <strong>জরুরি টিপস:</strong> তথ্য দেওয়ার পর যদি "Record Not Found" দেখায়, তবে আপনার পাসের সাল বা বোর্ডের নাম পুনরায় মিলিয়ে দেখুন। পুরাতন সনদের ক্ষেত্রে রোল-রেজির আগে অতিরিক্ত কোনো শূন্য আছে কি না নিশ্চিত হোন।
    </div>
  </div>

  <!-- STEP 3 -->
  <div class="htbd-tutorial-step-card">
    <div class="htbd-step-header">
      <span class="htbd-step-num">ধাপ ০৩</span>
      <h3 class="htbd-step-title">আবেদন ফরম পূরণ ও সংশোধিত তথ্যের সঠিক বানান এন্ট্রি</h3>
    </div>
    <p>ডাটা লোড হলে স্ক্রিনে শিক্ষার্থীর বর্তমান সংরক্ষিত তথ্য দেখতে পাবেন। আপনি যে তথ্যটি সংশোধন করতে চান (নিজের নাম, পিতার নাম, বা মাতার নাম) তার পাশের চেকক্সে টিক দিন। এরপর ডানপাশের বক্সে ডিজিটাল জন্মনিবন্ধন বা এনআইডি কার্ড অনুযায়ী সংশোধিত বাংলা ও ইংরেজি সঠিক বানান টাইপ করুন। ইংরেজি নামের প্রতিটি অক্ষর ক্যাপিটাল লেটারে লিখবেন। এরপর 'সংরক্ষণ করুন ও পরবর্তী ধাপে যান' বাটনে ক্লিক করুন।</p>
    
    <figure style="margin: 20px 0; text-align: center;">
      <img src="{CDN_PREFIX}/tutorials/cert_step3_correction_form.png" 
           alt="সার্টিফিকেট নাম সংশোধন ফরম পূরণ ও সঠিক নাম এন্ট্রি ধাপ ৩" 
           title="সঠিক বানান লিখে সংরক্ষণ করুন ও পরবর্তী ধাপে যান" 
           loading="lazy" 
           width="1200" height="675"
           class="htbd-step-img">
      <figcaption class="htbd-step-caption">
        📷 চিত্র ৩: লাল বক্স চিহ্নিত 'সংরক্ষণ করুন ও পরবর্তী ধাপে যান' বাটনে ক্লিক করে তথ্য নিশ্চিত করুন।
      </figcaption>
    </figure>

    <div class="htbd-tip-box">
      💡 <strong>জরুরি টিপস:</strong> একই আবেদনে একসাথে একাধিক বিষয় (যেমন: নিজের নাম + পিতার নাম) সংশোধন করা সম্ভব। তবে প্রতিটি সংশোধনের জন্য নির্ধারিত সরকারি বোর্ড ফি প্রযোজ্য হবে।
    </div>
  </div>

  <!-- STEP 4 -->
  <div class="htbd-tutorial-step-card">
    <div class="htbd-step-header">
      <span class="htbd-step-num">ধাপ ০৪</span>
      <h3 class="htbd-step-title">এফিডেভিট, জন্মসনদ, এনআইডি ও পেপার কাটিং আপলোড</h3>
    </div>
    <p>এই ধাপে প্রয়োজনীয় প্রামাণ্য নথিসমূহ সংযুক্ত করতে হবে। ১ম শ্রেণির ম্যাজিস্ট্রেটের এফিডেভিট, জাতীয় দৈনিক পত্রিকার মূল কাটিং, ১৭ ডিজিটের অনলাইন জন্মসনদ এবং পিতা-মাতার এনআইডি কার্ডের স্ক্যান কপি নির্ধারিত আপলোড বক্সে আপলোড করুন। ফাইল ফরম্যাট হতে হবে PDF বা JPG এবং প্রতি ফাইলের সাইজ ২ মেগাবাইটের মধ্যে হতে হবে। সব ফাইল আপলোড শেষ হলে 'ডকুমেন্টস জমা দিয়ে ফি প্রদানের জন্য এগিয়ে যান' বাটনে ক্লিক করুন।</p>
    
    <figure style="margin: 20px 0; text-align: center;">
      <img src="{CDN_PREFIX}/tutorials/cert_step4_document_upload.png" 
           alt="প্রয়োজনীয় কাগজপত্র এফিডেভিট ও পেপার কাটিং আপলোড ধাপ ৪" 
           title="ডকুমেন্টস জমা দিয়ে ফি প্রদানের জন্য এগিয়ে যান বাটনে ক্লিক করুন" 
           loading="lazy" 
           width="1200" height="675"
           class="htbd-step-img">
      <figcaption class="htbd-step-caption">
        📷 চিত্র ৪: লাল চিহ্নিত 'ডকুমেন্টস জমা দিয়ে ফি প্রদানের জন্য এগিয়ে যান' বাটনে ক্লিক করুন।
      </figcaption>
    </figure>

    <div class="htbd-tip-box">
      ⚠️ <strong>সতর্কতা:</strong> ঝাপসা বা মোবাইল দিয়ে সাধারণ ছবি তুলে আপলোড করবেন না। স্পষ্ট ফ্ল্যাটবেড স্ক্যানার দিয়ে ৩০০ ডিপিআই (300 DPI)-তে স্ক্যান করে ফাইল আপলোড করুন, অন্যথায় যাচাই কমিটি ফাইল রিজেক্ট করতে পারে।
    </div>
  </div>

  <!-- STEP 5 -->
  <div class="htbd-tutorial-step-card">
    <div class="htbd-step-header">
      <span class="htbd-step-num">ধাপ ০৫</span>
      <h3 class="htbd-step-title">সোনালী সেবায় অনলাইন ফি পরিশোধ (Sonali e-Sheba / bKash / Nagad)</h3>
    </div>
    <p>ডকুমেন্টস আপলোড শেষ হলে সিস্টেম আপনাকে সোনালী ব্যাংকের সরকারি পেমেন্ট গেটওয়েতে (Sonali e-Sheba) নিয়ে যাবে। স্ক্রিনে আপনার আবেদন ফি (যেমন: ১,৫০০ টাকা) প্রদর্শিত হবে। পেমেন্ট অপশন থেকে বিকাশ (bKash), নগদ (Nagad), রকেট বা সোনালী ব্যাংক একাউন্ট সিলেক্ট করুন। এরপর নিচের লাল চিহ্নিত 'বিকাশ দিয়ে ফি পরিশোধ করুন' বাটনে ক্লিক করে মোবাইল পিন ও ওটিপি (OTP) দিয়ে ফি জমা সম্পন্ন করুন।</p>
    
    <figure style="margin: 20px 0; text-align: center;">
      <img src="{CDN_PREFIX}/tutorials/cert_step5_sonali_payment.png" 
           alt="সোনালী সেবায় বিকাশ ও নগদ দিয়ে বোর্ড ফি পরিশোধ ধাপ ৫" 
           title="বিকাশ দিয়ে ফি পরিশোধ করুন বাটনে ক্লিক করুন" 
           loading="lazy" 
           width="1200" height="675"
           class="htbd-step-img">
      <figcaption class="htbd-step-caption">
        📷 চিত্র ৫: লাল চিহ্নিত 'বিকাশ দিয়ে ফি পরিশোধ করুন' বাটনে ক্লিক করে সরকারি ফি পরিশোধ সম্পন্ন করুন।
      </figcaption>
    </figure>

    <div class="htbd-tip-box">
      💡 <strong>জরুরি টিপস:</strong> সোনালী সেবায় ট্রানজেকশন সফল হলে স্ক্রিন রিফ্রেশ করবেন না। ৫–১০ সেকেন্ড অপেক্ষা করলে স্বয়ংক্রিয়ভাবে পোর্টালে ফিরে আসবে এবং পেমেন্ট রসিদ জেনারেট হবে।
    </div>
  </div>

  <!-- STEP 6 -->
  <div class="htbd-tutorial-step-card">
    <div class="htbd-step-header">
      <span class="htbd-step-num">ধাপ ০৬</span>
      <h3 class="htbd-step-title">অফিসিয়াল আবেদন রসিদ ও ট্র্যাকিং স্লিপ ডাউনলোড ও সংরক্ষণ</h3>
    </div>
    <p>পেমেন্ট সফল হওয়ার সাথে সাথে অভিনন্দন বার্তা এবং একটি ইউনিক <strong>Application ID (যেমন: DEB-2026-78491)</strong> ও সিকিউরিটি পিন নম্বর প্রদান করা হবে। সবুজ রঙের 'অফিসিয়াল আবেদন রসিদ ও ট্র্যাকিং স্লিপ ডাউনলোড করুন' বাটনে ক্লিক করে মূল আবেদন কপিটি PDF ফরম্যাটে ডাউনলোড করে ২ কপি রঙিন প্রিন্ট নিয়ে নিজের কাছে সংরক্ষণ করুন।</p>
    
    <figure style="margin: 20px 0; text-align: center;">
      <img src="{CDN_PREFIX}/tutorials/cert_step6_tracking_receipt.png" 
           alt="আবেদন সফল ও অফিসিয়াল ট্র্যাকিং স্লিপ ডাউনলোড ধাপ ৬" 
           title="অফিসিয়াল আবেদন রসিদ ও ট্র্যাকিং স্লিপ ডাউনলোড করুন" 
           loading="lazy" 
           width="1200" height="675"
           class="htbd-step-img">
      <figcaption class="htbd-step-caption">
        📷 চিত্র ৬: লাল চিহ্নিত 'অফিসিয়াল আবেদন রসিদ ও ট্র্যাকিং স্লিপ ডাউনলোড করুন' বাটনে ক্লিক করে রসিদ সংরক্ষণ করুন।
      </figcaption>
    </figure>

    <div class="htbd-tip-box">
      ⚠️ <strong>সতর্কতা:</strong> এই ট্র্যাকিং স্লিপেই আপনার সিকিউরিটি পাসকোড সংরক্ষিত থাকে। পরবর্তীতে আবেদন কোন পর্যায়ে আছে তা ট্র্যাক করতে এবং বোর্ড মিটিংয়ে মূল সনদ উত্তোলনের সময় এই ট্র্যাকিং স্লিপ প্রদর্শন বাধ্যতামূলক।
    </div>
  </div>

  <h2 id="fees-table" class="htbd-heading">৫. বিভিন্ন শিক্ষাবোর্ডের ফি ও সম্ভাব্য সময়সীমার তথ্য ছক (২০২৬)</h2>
  <p>শিক্ষা বোর্ড অনুযায়ী ফি-এর পরিমাণে সামান্য তারতম্য হতে পারে। সাধারণ শিক্ষাবোর্ডসমূহের স্ট্যান্ডার্ড ফি তালিকা নিচে তুলে ধরা হলো:</p>

  <div class="htbd-table-wrapper">
    <table class="htbd-table">
      <thead>
        <tr>
          <th>সংশোধনের ধরন</th>
          <th>সরকারি বোর্ড ফি (প্রতি স্তর)</th>
          <th>প্রক্রিয়াকরণ সময়সীমা</th>
          <th>বাধ্যতামূলক শর্তসমূহ</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>শিক্ষার্থীর নিজের নাম সংশোধন</strong></td>
          <td>১,০০০ – ১,৫০০ টাকা</td>
          <td>৩০ – ৪৫ কর্মদিবস</td>
          <td>১৭ ডিজিটের ডিজিটাল জন্মসনদ ও ম্যাজিস্ট্রেটের এফিডেভিট</td>
        </tr>
        <tr>
          <td><strong>পিতা বা মাতার নাম সংশোধন</strong></td>
          <td>১,০০০ – ১,২০০ টাকা</td>
          <td>৩০ – ৪৫ কর্মদিবস</td>
          <td>পিতা/মাতার স্মার্ট এনআইডি কার্ড ও সন্তানের জন্মসনদ</td>
        </tr>
        <tr>
          <td><strong>জন্মতারিখ বা বয়স সংশোধন</strong></td>
          <td>১,৫০০ – ২,০০০ টাকা</td>
          <td>৪৫ – ৬০ কর্মদিবস</td>
          <td>পিএসসি সনদের রেকর্ড, ক্লিনিক্যাল সার্টিফিকেট ও সিভিল সার্জন মতামত</td>
        </tr>
        <tr>
          <td><strong>সংশোধিত নতুন ফ্রেশ সনদপত্র উত্তোলন</strong></td>
          <td>৬০০ – ৮০০ টাকা</td>
          <td>৭ – ১৫ কর্মদিবস</td>
          <td>বোর্ড মিটিংয়ে সংশোধন অনুমোদনের পর পূর্বের ভুল সনদ জমা দিতে হবে</td>
        </tr>
        <tr>
          <td><strong>নতুন ফ্রেশ নম্বরপত্র (মার্কশিট) উত্তোলন</strong></td>
          <td>৪০০ – ৬০০ টাকা</td>
          <td>৫ – ৭ কর্মদিবস</td>
          <td>অনুমোদন পত্রের কপি ও মূল নম্বরপত্র জমা প্রদান সাপেক্ষে</td>
        </tr>
      </tbody>
    </table>
  </div>

  <h2 id="board-hearing" class="htbd-heading">৬. বোর্ড মিটিংয়ের শুনানি, সাক্ষাৎকার ও নতুন মূল সনদ উত্তোলন</h2>
  <p>অনলাইনে সফল আবেদনের পর বোর্ডের সংশ্লিষ্ট শাখা আপনার দাখিলকৃত ডকুমেন্টস প্রাথমিক স্ক্রিনিং করে। এরপর শিক্ষাবোর্ডের উচ্চপর্যায়ের <strong>'নাম ও বয়স সংশোধন কমিটি'র (Name & Age Correction Committee)</strong> নিয়মিত সভায় নথিটি পেশ করা হয়।</p>
  <p>যদি তথ্যে কোনো অস্পষ্টতা বা জটিলতা থাকে, তবে প্রার্থীর আবেদনে উল্লেখিত মোবাইল নম্বরে এসএমএস পাঠিয়ে নির্দিষ্ট দিনে বোর্ড ভবনে উপস্থিত হয়ে মূল কাগজপত্রসহ সাক্ষাৎকারের জন্য ডাকা হতে পারে। শুনানি সম্পন্ন হলে বা সাধারণ ক্ষেত্রে সরাসরি আবেদন Approved হিসেবে ওয়েবসাইটে স্ট্যাটাস পরিবর্তন হয়।</p>
  <p>অনুমোদন পাওয়ার পর প্রার্থীকে নির্ধারিত সাময়িক সনদ/মূল সনদ উত্তোলন ফি সোনালী সেবায় জমা দিয়ে পূর্বের মূল ভুল সার্টিফিকেটটি বোর্ডের কাউন্টারে জমা দিয়ে সংশোধিত নতুন ফ্রেশ সনদপত্র গ্রহণ করতে হয়।</p>

  <h2 id="troubleshooting" class="htbd-heading">৭. সাধারণ ভুল ও টেকনিক্যাল ট্রাবলশুটিং গাইড</h2>
  <div style="margin: 20px 0;">
    <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 16px 20px; margin-bottom: 14px;">
      <h4 style="margin: 0 0 6px 0; color: #dc2626; font-size: 17px; font-weight: 700;">❓ সমস্যা ১: বিকাশ থেকে ফি কেটে নিয়েছে কিন্তু ওয়েবসাইটে ট্র্যাকিং স্লিপ আসেনি—কী করবেন?</h4>
      <p style="margin: 0; font-size: 15.5px; color: #475569;">
        ঘাবড়াবেন না। পেমেন্ট গেটওয়েতে নেটওয়ার্ক সমস্যার কারণে এমন হতে পারে। বিকাশ ট্রানজেকশন আইডি (TrxID) সংরক্ষণ করুন। ১-২ ঘণ্টা পর শিক্ষা বোর্ডের পোর্টালে গিয়ে 'আবেদন ট্র্যাকিং' মেনুতে রোল-রেজি দিয়ে সার্চ করলে স্বয়ংক্রিয়ভাবে পেমেন্ট ভেরিফায়েড দেখাবে। তখনও সমস্যা থাকলে বোর্ডের হেল্পলাইন ১৬১২৩ নম্বরে TrxID জানিয়ে রসিদ ভ্যালিড করে নেওয়া যায়।
      </p>
    </div>

    <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 16px 20px; margin-bottom: 14px;">
      <h4 style="margin: 0 0 6px 0; color: #dc2626; font-size: 17px; font-weight: 700;">❓ সমস্যা ২: জেএসসি ও এসএসসি সনদে একই সাথে ভুল থাকলে কোনটা আগে আবেদন করবেন?</h4>
      <p style="margin: 0; font-size: 15.5px; color: #475569;">
        নিয়ম অনুযায়ী নিচের ক্লাসের তথ্য আগে সংশোধিত হতে হয়। তবে শিক্ষা বোর্ডের অনলাইন পোর্টালে একই সাথে জেএসসি ও এসএসসি উভয় সনদের জন্য ধারাবাহিক আবেদন দাখিল করা যায়। এতে উভয় সনদ একই বোর্ড মিটিংয়ে একসাথে অনুমোদিত হয়ে যায় এবং সময় বাঁচে।
      </p>
    </div>

    <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 16px 20px;">
      <h4 style="margin: 0 0 6px 0; color: #dc2626; font-size: 17px; font-weight: 700;">❓ সমস্যা ৩: দালাল বা তৃতীয় পক্ষের মাধ্যমে আবেদন করা কি নিরাপদ?</h4>
      <p style="margin: 0; font-size: 15.5px; color: #475569;">
        সম্পূর্ণ অপ্রয়োজনীয় ও ঝুঁকিপূর্ণ। শিক্ষাবোর্ডের সকল সেবা বর্তমানে শতভাগ ডিজিটাল ও স্বচ্ছ। দালালরা সাধারণ শিক্ষার্থীদের বিভ্রান্ত করে অতিরিক্ত অর্থ হাতিয়ে নেয়। আপনি নিজেই মোবাইল বা কম্পিউটারে বসে আমাদের এই গাইডের ৬টি ধাপ অনুসরণ করে মাত্র ২০ মিনিটে আবেদন শেষ করতে পারবেন।
      </p>
    </div>
  </div>

  <h2 id="faqs" class="htbd-heading">৮. সচরাচর জিজ্ঞাসিত প্রশ্ন (FAQ)</h2>
  <div style="margin-top: 15px;">
    <p><strong>প্রশ্ন ১: সার্টিফিকেট নাম সংশোধনে সর্বোচ্চ কতদিন সময় লাগে?</strong><br>
    উত্তর: অনলাইনে সকল সঠিক কাগজপত্র আপলোড ও সোনালী সেবায় ফি পরিশোধের পর সাধারণত ৩০ থেকে ৪৫ কর্মদিবসের মধ্যে বোর্ড সভার মাধ্যমে চূড়ান্ত অনুমোদন সম্পন্ন হয়।</p>
    
    <p><strong>প্রশ্ন ২: বয়স বা জন্মতারিখ কত বছর পর্যন্ত সংশোধন করা সম্ভব?</strong><br>
    উত্তর: শিক্ষা বোর্ডের প্রচলিত নীতিমালা অনুযায়ী টাইপিং বা অসাবধানতাবশত গরমিলের ক্ষেত্রে সর্বোচ্চ ১ থেকে ২ বছর পর্যন্ত বয়স সংশোধনের সুযোগ থাকে, যার জন্য পিএসসি সনদ বা ডাক্তারের মেডিকেল বয়স প্রাক্কলন সনদ প্রয়োজন হয়।</p>

    <p><strong>প্রশ্ন ৩: পত্রিকায় বিজ্ঞাপন দেওয়ার পর কতদিন পর অনলাইনে আবেদন করা যায়?</strong><br>
    উত্তর: জাতীয় দৈনিকে বিজ্ঞাপন প্রকাশের দিনই পত্রিকার মূল পেপার কাটিং স্ক্যান করে সাথে সাথে অনলাইন আবেদন ফরমের সাথে আপলোড করা যায়। কোনো নির্দিষ্ট বিলম্বের প্রয়োজন নেই।</p>

    <p><strong>প্রশ্ন ৪: মাদ্রাসা শিক্ষা বোর্ডের (দাখিল/আলিম) সনদের নিয়ম কি একই?</strong><br>
    উত্তর: হ্যাঁ, বাংলাদেশ মাদ্রাসা শিক্ষা বোর্ডের ওয়েবসাইট (bmeb.gov.bd)-এর ই-সেবা অপশনে গিয়ে দাখিল ও আলিম সনদের জন্যও হুবহু একই নিয়মে অনলাইনে আবেদন ও সোনালী সেবায় ফি দিতে হয়।</p>

    <p><strong>প্রশ্ন ৫: আবেদন কোন পর্যায়ে আছে তা ঘরে বসে কীভাবে জানব?</strong><br>
    উত্তর: বোর্ডের ওয়েবসাইটে 'আবেদন স্ট্যাটাস ট্র্যাকিং' অপশনে গিয়ে আপনার Application ID এবং পাসকোড দিলেই আবেদনটি ব্রাঞ্চ স্ক্রিনিং, কমিটি রিভিউ নাকি অনুমোদিত হয়েছে তা লাইভ দেখা যায়। এছাড়া প্রতিটি বড় আপডেটে মোবাইলে ফ্রি এসএমএস পাঠানো হয়।</p>
  </div>
</div>

<!-- Structured Schema Microdata: FAQPage & HowTo -->
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@graph": [
    {{
      "@type": "HowTo",
      "name": "ঘরে বসেই সার্টিফিকেট নাম ও বয়স সংশোধনের সঠিক নিয়ম (২০২৬)",
      "description": "জেএসসি, এসএসসি ও এইচএসসি সার্টিফিকেটের নাম, পিতা-মাতার নাম ও বয়স সংশোধনের সম্পূর্ণ অনলাইন আবেদন গাইডলাইন।",
      "image": "{CDN_PREFIX}/thumbnails/thumb_certificate_correction_2026.png",
      "totalTime": "P30D",
      "step": [
        {{
          "@type": "HowToStep",
          "name": "ই-সেবা পোর্টালে প্রবেশ",
          "text": "ঢাকা শিক্ষাবোর্ডের অফিশিয়াল ওয়েবসাইটে গিয়ে 'নাম ও বয়স সংশোধন অনলাইন আবেদন' লিংকে ক্লিক করুন।",
          "image": "{CDN_PREFIX}/tutorials/cert_step1_portal_access.png",
          "url": "https://www.helptrickbd.com/2025/03/how-to-correction-certificate-name-2025.html#step-by-step"
        }},
        {{
          "@type": "HowToStep",
          "name": "রোল-রেজিস্ট্রেশন দিয়ে ডাটাবেজ অনুসন্ধান",
          "text": "পরীক্ষার নাম, পাসের সন, রোল এবং রেজি নম্বর প্রদান করে 'ডাটা খুঁজুন' বাটনে ক্লিক করে রেকর্ড লোড করুন।",
          "image": "{CDN_PREFIX}/tutorials/cert_step2_student_search.png",
          "url": "https://www.helptrickbd.com/2025/03/how-to-correction-certificate-name-2025.html#step-by-step"
        }},
        {{
          "@type": "HowToStep",
          "name": "সংশোধিত তথ্যের সঠিক বানান এন্ট্রি",
          "text": "যে যে তথ্য পরিবর্তন করতে চান তার টিক দিন এবং ডিজিটাল জন্মসনদ অনুযায়ী সঠিক বানান লিখুন।",
          "image": "{CDN_PREFIX}/tutorials/cert_step3_correction_form.png",
          "url": "https://www.helptrickbd.com/2025/03/how-to-correction-certificate-name-2025.html#step-by-step"
        }},
        {{
          "@type": "HowToStep",
          "name": "এফিডেভিট ও প্রামাণ্য দলিল আপলোড",
          "text": "১ম শ্রেণির ম্যাজিস্ট্রেট এফিডেভিট, পেপার কাটিং ও জন্মসনদের স্পষ্ট স্ক্যান কপি সংযুক্ত করুন।",
          "image": "{CDN_PREFIX}/tutorials/cert_step4_document_upload.png",
          "url": "https://www.helptrickbd.com/2025/03/how-to-correction-certificate-name-2025.html#step-by-step"
        }},
        {{
          "@type": "HowToStep",
          "name": "সোনালী সেবায় ফি পরিশোধ",
          "text": "সোনালী পেমেন্ট গেটওয়েতে বিকাশ, নগদ বা রকেটের মাধ্যমে বোর্ড ফি পরিশোধ সম্পন্ন করুন।",
          "image": "{CDN_PREFIX}/tutorials/cert_step5_sonali_payment.png",
          "url": "https://www.helptrickbd.com/2025/03/how-to-correction-certificate-name-2025.html#step-by-step"
        }},
        {{
          "@type": "HowToStep",
          "name": "ট্র্যাকিং স্লিপ ডাউনলোড",
          "text": "আবেদন সফল হওয়ার পর ইউনিক Application ID সম্বলিত ট্র্যাকিং স্লিপটি প্রিন্ট করে নিজের কাছে রাখুন।",
          "image": "{CDN_PREFIX}/tutorials/cert_step6_tracking_receipt.png",
          "url": "https://www.helptrickbd.com/2025/03/how-to-correction-certificate-name-2025.html#step-by-step"
        }}
      ]
    }},
    {{
      "@type": "FAQPage",
      "mainEntity": [
        {{
          "@type": "Question",
          "name": "সার্টিফিকেট নাম সংশোধনে সর্বোচ্চ কতদিন সময় লাগে?",
          "acceptedAnswer": {{
            "@type": "Answer",
            "text": "অনলাইনে সকল সঠিক কাগজপত্র আপলোড ও সোনালী সেবায় ফি পরিশোধের পর সাধারণত ৩০ থেকে ৪৫ কর্মদিবসের মধ্যে বোর্ড সভার মাধ্যমে চূড়ান্ত অনুমোদন সম্পন্ন হয়।"
          }}
        }},
        {{
          "@type": "Question",
          "name": "বয়স বা জন্মতারিখ কত বছর পর্যন্ত সংশোধন করা সম্ভব?",
          "acceptedAnswer": {{
            "@type": "Answer",
            "text": "শিক্ষা বোর্ডের প্রচলিত নীতিমালা অনুযায়ী টাইপিং বা অসাবধানতাবশত গরমিলের ক্ষেত্রে সর্বোচ্চ ১ থেকে ২ বছর পর্যন্ত বয়স সংশোধনের সুযোগ থাকে, যার জন্য পিএসসি সনদ বা ডাক্তারের মেডিকেল বয়স প্রাক্কলন সনদ প্রয়োজন হয়।"
          }}
        }},
        {{
          "@type": "Question",
          "name": "জেএসসি এবং এসএসসি সনদের নাম একসাথে সংশোধন করা যায় কি?",
          "acceptedAnswer": {{
            "@type": "Answer",
            "text": "হ্যাঁ, শিক্ষা বোর্ডের অনলাইন পোর্টালে একই সাথে জেএসসি ও এসএসসি উভয় সনদের জন্য ধারাবাহিক আবেদন দাখিল করা যায়, যাতে উভয় সনদ একই বোর্ড মিটিংয়ে একসাথে অনুমোদিত হতে পারে।"
          }}
        }},
        {{
          "@type": "Question",
          "name": "সার্টিফিকেট সংশোধনে পত্রিকার বিজ্ঞাপনের গুরুত্ব কী?",
          "acceptedAnswer": {{
            "@type": "Answer",
            "text": "আইনি স্বচ্ছতা নিশ্চিত করতে এবং কোনো প্রতারণামূলক পরিচয় পরিবর্তন রোধ করতে শিক্ষাবোর্ড জাতীয় দৈনিকে নাম পরিবর্তনের উন্মুক্ত বিজ্ঞপ্তি বাধ্যতামূলক করে থাকে।"
          }}
        }}
      ]
    }}
  ]
}}
</script>

</body>
</html>
"""

def main():
    print("Building full tutorial article...")
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(HTML_CONTENT)

    word_count = len(HTML_CONTENT.split())
    meta = {
        "slug": "how-to-correction-certificate-name-2025",
        "post_id": "8675903395059439252",
        "title": "ঘরে বসেই সার্টিফিকেট নাম ও বয়স সংশোধনের সঠিক নিয়ম (২০২৬)",
        "category": "Education Guide,সার্টিফিকেট সংশোধন",
        "labels": ["Education Guide", "সার্টিফিকেট সংশোধন"],
        "meta_description": "জেএসসি, এসএসসি ও এইচএসসি সার্টিফিকেটের নিজের নাম, পিতা-মাতার নাম বা বয়স সংশোধনের অনলাইন আবেদন নিয়ম, ফি ও প্রয়োজনীয় কাগজপত্রের তালিকা পড়ুন HelpTrickBD-তে।",
        "word_count": word_count,
        "updated_at": "2026-09-15T12:45:00+06:00"
    }

    with open(METADATA_FILE, "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)

    print(f"✅ Generated article saved to: {OUTPUT_FILE}")
    print(f"📊 Total word count: {word_count}")


if __name__ == "__main__":
    main()
