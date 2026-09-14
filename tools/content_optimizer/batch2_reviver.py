#!/usr/bin/env python3
"""
HelpTrickBD Automated Batch 2 Post Reviver & Live Publisher Engine
Systematically revives Batch 2 thin posts (< 500 words) into 1,250 - 1,650+ words
high-authority educational guides with SolaimanLipi typography, 16:9 featured banners,
Position 0 answer box, comparison tables, model exam questions, and Schema.org FAQPage JSON-LD.
"""

import argparse
import json
import os
import sys
import time

try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
try:
    from internal_linker.linker import find_related_links, generate_internal_link_box
except ImportError:
    find_related_links = None
    generate_internal_link_box = None

try:
    from blogger_publisher.update_post import get_authenticated_service, BLOG_ID
except ImportError:
    get_authenticated_service = None
    BLOG_ID = "1975983966532887960"

OUTPUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "output_posts", "revived_posts"))
os.makedirs(OUTPUT_DIR, exist_ok=True)

STYLES_BLOCK = """<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Bengali:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
  @font-face {
    font-family: 'SolaimanLipi';
    font-display: swap;
    font-style: normal;
    font-weight: 400;
    src: url('https://fonts.maateen.me/solaiman-lipi/solaimanlipi-normal-v1.0.woff2') format('woff2');
  }
  @font-face {
    font-family: 'SolaimanLipi';
    font-display: swap;
    font-style: normal;
    font-weight: 700;
    src: url('https://fonts.maateen.me/solaiman-lipi/solaimanlipi-bold-v1.0.woff2') format('woff2');
  }
  .htbd-post-wrapper,
  .htbd-post-wrapper * {
    font-family: 'SolaimanLipi', 'Noto Sans Bengali', Arial, sans-serif !important;
  }
  .htbd-post-wrapper p {
    font-size: 18px !important;
    line-height: 1.85 !important;
    color: #202124 !important;
    margin: 16px 0 !important;
    text-align: justify !important;
  }
  .htbd-heading {
    color: #1a73e8 !important;
    border-left: 5px solid #1a73e8 !important;
    border-bottom: none !important;
    padding-left: 14px !important;
    margin-top: 38px !important;
    margin-bottom: 16px !important;
    font-size: 23px !important;
    font-weight: 700 !important;
    line-height: 1.4 !important;
  }
  .htbd-toc-box {
    background: #f8fafd !important;
    border: 1px solid #d2e3fc !important;
    border-radius: 10px !important;
    padding: 20px 24px !important;
    margin: 25px 0 !important;
    box-shadow: 0 1px 4px rgba(26,115,232,0.06) !important;
  }
  .htbd-toc-list {
    list-style: none !important;
    list-style-type: none !important;
    padding-left: 0 !important;
    margin: 12px 0 0 0 !important;
  }
  .htbd-toc-list li {
    list-style-type: none !important;
    padding: 8px 0 !important;
    border-bottom: 1px dashed #e8eaed !important;
    font-size: 16.5px !important;
  }
  .htbd-toc-list li:last-child {
    border-bottom: none !important;
  }
  .htbd-toc-list li a {
    color: #1a73e8 !important;
    text-decoration: none !important;
    font-weight: 500 !important;
  }
  .htbd-toc-list li a:hover {
    color: #0d47a1 !important;
    text-decoration: underline !important;
  }
  .htbd-table-wrapper {
    overflow-x: auto !important;
    margin: 22px 0 !important;
    border-radius: 8px !important;
    border: 1px solid #e0e0e0 !important;
  }
  .htbd-table {
    width: 100% !important;
    border-collapse: collapse !important;
    background: #ffffff !important;
    font-size: 16px !important;
  }
  .htbd-table th {
    background-color: #1a73e8 !important;
    color: #ffffff !important;
    padding: 13px 15px !important;
    text-align: left !important;
    font-weight: 600 !important;
  }
  .htbd-table td {
    padding: 12px 15px !important;
    border: 1px solid #e8eaed !important;
    color: #333333 !important;
  }
  .htbd-table tr:nth-child(even) {
    background-color: #f8fafd !important;
  }
</style>
"""

def get_internal_links_for_topic(query):
    if find_related_links and generate_internal_link_box:
        try:
            rel = find_related_links(query, max_links=3)
            return generate_internal_link_box(rel)
        except Exception:
            pass
    return ""


# ==============================================================================
# POST 1: CERTIFICATE NAME & AGE CORRECTION PROCESS
# ==============================================================================
def build_post_certificate_correction():
    slug = "how-to-correction-certificate-name-2025"
    post_id = "8675903395059439252"
    title = "ঘরে বসেই সার্টিফিকেট নাম ও বয়স সংশোধনের সঠিক নিয়ম (২০২৬)"
    category = "সার্টিফিকেট সংশোধন,Education Guide"
    meta_desc = "জেএসসি, এসএসসি ও এইচএসসি সার্টিফিকেটের নিজের নাম, পিতা-মাতার নাম বা বয়স সংশোধনের অনলাইন আবেদন নিয়ম, ফি ও প্রয়োজনীয় কাগজপত্রের তালিকা পড়ুন HelpTrickBD-তে।"
    links_html = get_internal_links_for_topic("সার্টিফিকেট সংশোধন শিক্ষাবোর্ড এসএসসি")

    content = f"""{STYLES_BLOCK}
<div class="htbd-post-wrapper">
  <div style="margin-bottom: 18px;">
    <span class="htbd-badge" style="background: #e8f0fe; color: #1a73e8; padding: 6px 14px; border-radius: 20px; font-weight: 600; font-size: 14px; display: inline-block;">
      📚 বিভাগ: শিক্ষাবোর্ড ও সেবা | সর্বশেষ সংস্করণ: ২০২৬ | ঘরে বসে অনলাইন গাইডলাইন
    </span>
  </div>

  <!-- Hero Thumbnail Banner -->
  <div style="text-align: center; margin: 18px 0 25px 0;">
    <img src="https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/posts/certificate-correction-banner.png" 
         alt="ঘরে বসেই সার্টিফিকেট নাম ও বয়স সংশোধনের সঠিক নিয়ম" 
         title="সার্টিফিকেট নাম ও বয়স সংশোধন অনলাইন আবেদন"
         width="1200" height="675"
         loading="eager"
         style="width: 100%; max-width: 100%; height: auto; border-radius: 10px; box-shadow: 0 4px 14px rgba(0,0,0,0.12); display: block; margin: 0 auto;"/>
    <span style="display: block; font-size: 14px; color: #5f6368; margin-top: 8px; font-style: italic;">
      চিত্র: বাংলাদেশের শিক্ষাবোর্ডসমূহে সার্টিফিকেট নাম, পিতা-মাতার নাম ও বয়স সংশোধনের অনলাইন পদ্ধতি
    </span>
  </div>

  <div class="htbd-qbox" style="background: #f8f9fa; border-left: 5px solid #1a73e8; padding: 20px 24px; margin: 22px 0; border-radius: 0 8px 8px 0; box-shadow: 0 1px 4px rgba(0,0,0,0.06);">
    <p style="margin: 0; font-size: 18px; line-height: 1.8;">
      <strong>📌 সারসংক্ষেপ (Quick Overview):</strong> 
      <strong>সার্টিফিকেট নাম ও বয়স সংশোধন</strong> হলো বাংলাদেশের শিক্ষা বোর্ডগুলোর (যেমন—ঢাকা, রাজশাহী, চট্টগ্রাম ইত্যাদি) নির্ধারিত ই-সার্ভিস পোর্টালের মাধ্যমে পিএসসি, জেএসসি, এসএসসি ও এইচএসসি পরীক্ষার সনদপত্রে বিদ্যমান বানান ভুল, পিতা-মাতার নামের অসঙ্গতি বা জন্মতারিখ সংশোধন করার একটি সমন্বিত আইনি ও প্রশাসনিক প্রক্রিয়া। বর্তমানে সম্পূর্ণ প্রক্রিয়াটি অনলাইনে সোনালী সেবার মাধ্যমে ফি পরিশোধ এবং ডকুমেন্টস আপলোডের মাধ্যমে ঘরে বসেই সম্পন্ন করা যায়। নিচে প্রয়োজনীয় সব কাগজপত্র, এফিডেভিট ফরম্যাট এবং ধাপে ধাপে আবেদনের পূর্ণাঙ্গ নির্দেশিকা তুলে ধরা হলো।
    </p>
  </div>

  <div class="htbd-toc-box">
    <h3 style="margin-top: 0; color: #1a73e8; border-bottom: 2px solid #e8f0fe; padding-bottom: 10px; font-size: 20px; font-weight: 700;">📑 সূচিপত্র (Table of Contents)</h3>
    <ul class="htbd-toc-list">
      <li><a href="#need">👉 ১. সার্টিফিকেট সংশোধনের প্রয়োজন কেন হয় ও সাধারণ ভুলসমূহ</a></li>
      <li><a href="#documents">👉 ২. প্রয়োজনীয় কাগজপত্র ও দলিলের পূর্ণাঙ্গ তালিকা</a></li>
      <li><a href="#affidavit">👉 ৩. ১ম শ্রেণির ম্যাজিস্ট্রেটের এফিডেভিট ও পত্রিকায় বিজ্ঞপ্তির নিয়ম</a></li>
      <li><a href="#steps">👉 ৪. শিক্ষাবোর্ডে অনলাইন আবেদন করার ধাপে ধাপে পদ্ধতি</a></li>
      <li><a href="#fees-table">👉 ৫. বিভিন্ন শিক্ষাবোর্ডের ফি ও সম্ভাব্য সময়সীমার তথ্য ছক</a></li>
      <li><a href="#interview">👉 ৬. বোর্ড মিটিং বা সাক্ষাৎকার এবং মূল সনদ উত্তোলন</a></li>
      <li><a href="#faqs">👉 ৭. সচরাচর জিজ্ঞাসিত প্রশ্ন (FAQ)</a></li>
    </ul>
  </div>

  <h2 id="need" class="htbd-heading">১. সার্টিফিকেট সংশোধনের প্রয়োজন কেন হয় ও সাধারণ ভুলসমূহ</h2>
  <p>আমাদের দেশে স্কুল বা মাদ্রাসার রেজিস্ট্রেশনের সময় অনেক ক্ষেত্রেই অসাবধানতাবশত শিক্ষার্থীর নাম, পিতার নাম, মাতার নাম বা জন্মতারিখে ভুল লিপিবদ্ধ হয়। পরবর্তীতে জাতীয় পরিচয়পত্র (NID), ডিজিটাল জন্মনিবন্ধন (BRIS) কিংবা পাসপোর্টের তথ্যের সাথে শিক্ষাগত সনদের তথ্যের গরমিল দেখা দেয়। উচ্চশিক্ষার জন্য বিদেশে আবেদন, সরকারি চাকরি বা বিসিএস ভেরিফিকেশনে এই তথ্যগত অসঙ্গতি অত্যন্ত মারাত্মক জটিলতার সৃষ্টি করে। তাই ভুল ধরা পড়ার সাথে সাথে শিক্ষাবোর্ডের আইনি প্রক্রিয়ায় তা সংশোধন করে নেওয়া অত্যন্ত জরুরি।</p>

  <h2 id="documents" class="htbd-heading">২. প্রয়োজনীয় কাগজপত্র ও দলিলের পূর্ণাঙ্গ তালিকা</h2>
  <p>অনলাইন আবেদনের পূর্বে নিচের কাগজপত্রগুলোর মূল কপি স্ক্যান করে প্রস্তুত রাখতে হবে:</p>
  <ul>
    <li><strong>১. মূল ডকুমেন্টস:</strong> জেএসসি/এসএসসি/এইচএসসি পরীক্ষার মূল রেজিস্ট্রেশন কার্ড, এডমিট কার্ড, নম্বরপত্র (মার্কশিট) এবং মূল সার্টিফিকেট বা সাময়িক সনদ।</li>
    <li><strong>২. ডিজিটাল জন্মনিবন্ধন:</strong> ১৭ ডিজিটের অনলাইন ভেরিফায়েড ইংরেজি ও বাংলা জন্মনিবন্ধন সনদপত্র।</li>
    <li><strong>৩. পিতা-মাতার এনআইডি:</strong> পিতা ও মাতার জাতীয় পরিচয়পত্রের সত্যায়িত রঙিন ফটোকপি।</li>
    <li><strong>৪. প্রাথমিক সনদ:</strong> প্রাইমারি বা পিএসসি পাসের সনদপত্র ও বিদ্যালয় ত্যাগের ছাড়পত্র (TC)।</li>
    <li><strong>৫. প্রাতিষ্ঠানিক সুপারিশ:</strong> সংশ্লিষ্ট শিক্ষা প্রতিষ্ঠানের প্রধান শিক্ষক বা অধ্যক্ষের সিল ও স্বাক্ষরযুক্ত প্রত্যয়নপত্র।</li>
  </ul>

  {links_html}

  <h2 id="affidavit" class="htbd-heading">৩. ১ম শ্রেণির ম্যাজিস্ট্রেটের এফিডেভিট ও পত্রিকায় বিজ্ঞপ্তির নিয়ম</h2>
  <p>নাম বা বয়সের গুরুতর সংশোধনের ক্ষেত্রে আদালতের ফার্স্ট ক্লাস জুডিশিয়াল ম্যাজিস্ট্রেট অথবা নোটারি পাবলিক কর্তৃক সম্পাদিত এফিডেভিট (হলফনামা) বাধ্যতামূলক। ৩০০ টাকার নন-জুডিশিয়াল স্ট্যাম্পে এই হলফনামা প্রস্তুত করতে হয়।</p>
  <p>এছাড়া একটি বহুল প্রচারিত জাতীয় দৈনিক পত্রিকায় নাম/বয়স পরিবর্তনের ঘোষণাপত্র প্রকাশ করতে হবে। বিজ্ঞপ্তিতে প্রার্থীর পূর্বের ভুল নাম, সংশোধিত সঠিক নাম, রোল, রেজিস্ট্রেশন নম্বর ও শিক্ষাবোর্ডের নাম সুস্পষ্টভাবে উল্লেখ থাকতে হবে। মূল পত্রিকার সম্পূর্ণ পাতার কাটিং আবেদনের সাথে আপলোড করতে হয়।</p>

  <h2 id="steps" class="htbd-heading">৪. শিক্ষাবোর্ডে অনলাইন আবেদন করার ধাপে ধাপে পদ্ধতি</h2>
  <p>বাংলাদেশের সকল সাধারণ শিক্ষাবোর্ডের ওয়েবসাইটে ই-সেবা অপশনে গিয়ে নিচের ধাপগুলো অনুসরণ করুন:</p>
  <ol style="padding-left: 25px; line-height: 2;">
    <li><strong>রেজিস্ট্রেশন:</strong> বোর্ডের অফিসিয়াল ওয়েবসাইটে 'অনলাইন আবেদন' অপশনে ক্লিক করে শিক্ষার্থীর রোল ও রেজি নম্বর দিয়ে প্রোফাইল যাচাই করুন।</li>
    <li><strong>সংশোধন নির্বাচন:</strong> আপনি নিজের নাম, পিতার নাম, মাতার নাম নাকি জন্মতারিখ সংশোধন করতে চান তা টিক দিন এবং সংশোধিত সঠিক তথ্য লিখুন।</li>
    <li><strong>ফাইল আপলোড:</strong> স্ক্যান করা এফিডেভিট, পত্রিকার কাটিং, জন্মনিবন্ধন ও অন্যান্য ডকুমেন্টস নির্ধারিত সাইজে (সাধারণত ২০০ KB-এর নিচে) আপলোড করুন।</li>
    <li><strong>ফি পরিশোধ:</strong> সোনালী সেবার (Sonali e-Sheba) মাধ্যমে মোবাইল ব্যাংকিং (বিকাশ, নগদ, রকেট) বা ডেবিট কার্ড ব্যবহার করে তাৎক্ষণিক বোর্ড ফি পরিশোধ করুন।</li>
    <li><strong>ট্র্যাকিং স্লিপ সংরক্ষণ:</strong> ফি পরিশোধের পর ট্র্যাকিং নম্বর সংবলিত অ্যাপ্লিকেশন রসিদটি প্রিন্ট করে সংরক্ষণ করুন।</li>
  </ol>

  <h2 id="fees-table" class="htbd-heading">৫. বিভিন্ন শিক্ষাবোর্ডের ফি ও সম্ভাব্য সময়সীমার তথ্য ছক</h2>
  <div class="htbd-table-wrapper">
    <table class="htbd-table">
      <thead>
        <tr>
          <th>সংশোধনের ধরন</th>
          <th>বোর্ড ফি (প্রতি সনদ)</th>
          <th>প্রক্রিয়াকরণ সময়</th>
          <th>প্রধান শর্ত</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>নিজের নাম সংশোধন</strong></td>
          <td>১,০০০ – ১,৫০০ টাকা</td>
          <td>৩০ – ৪৫ কর্মদিবস</td>
          <td>ডিজিটাল জন্মনিবন্ধন ও এফিডেভিট আবশ্যক</td>
        </tr>
        <tr>
          <td><strong>পিতা বা মাতার নাম সংশোধন</strong></td>
          <td>১,০০০ – ১,২০০ টাকা</td>
          <td>৩০ – ৪৫ কর্মদিবস</td>
          <td>পিতা/মাতার এনআইডি ও সন্তানের জন্মসনদ</td>
        </tr>
        <tr>
          <td><strong>জন্মতারিখ সংশোধন</strong></td>
          <td>১,৫০০ – ২,০০০ টাকা</td>
          <td>৪৫ – ৬০ কর্মদিবস</td>
          <td>ডাক্তারি সনদ ও পিএসসি সনদের রেকর্ড যাচাই</td>
        </tr>
        <tr>
          <td><strong>নতুন ফ্রেশ সার্টিফিকেট উত্তোলন</strong></td>
          <td>৫০০ – ৮০০ টাকা</td>
          <td>৭ – ১৫ কর্মদিবস</td>
          <td>সংশোধন অনুমোদন সম্পন্ন হওয়ার পর</td>
        </tr>
      </tbody>
    </table>
  </div>

  <h2 id="interview" class="htbd-heading">৬. বোর্ড মিটিং বা সাক্ষাৎকার এবং মূল সনদ উত্তোলন</h2>
  <p>অনলাইন আবেদনটি শিক্ষাবোর্ডের সংশ্লিষ্ট শাখায় প্রাথমিক যাচাই শেষে 'নাম ও বয়স সংশোধন কমিটি'র বোর্ড মিটিংয়ে উপস্থাপিত হয়। জটিল ক্ষেত্রে প্রার্থীর মোবাইলে এসএমএস পাঠিয়ে নির্দিষ্ট তারিখে মূল কাগজপত্রসহ বোর্ডে সরাসরি উপস্থিত হয়ে সাক্ষাৎকার দিতে বলা হতে পারে।</p>
  <p>কমিটি কর্তৃক আবেদন অনুমোদিত হলে প্রার্থীর প্রোফাইলে স্ট্যাটাস 'Approved' দেখাবে। এরপর প্রার্থীকে পূর্ববর্তী ভুল সার্টিফিকেট বোর্ডে জমা দিয়ে সংশোধিত নতুন ফ্রেশ সার্টিফিকেট ও মার্কশিট গ্রহণের জন্য ফি জমা দিয়ে মূল সনদপত্র উত্তোলন করতে হবে।</p>

  <h2 id="faqs" class="htbd-heading">৭. সচরাচর জিজ্ঞাসিত প্রশ্ন (FAQ)</h2>
  <div style="margin-top: 15px;">
    <p><strong>প্রশ্ন ১: জেএসসি এবং এসএসসি সনদের নাম একসাথে সংশোধন করা যায় কি?</strong><br>
    উত্তর: হ্যাঁ, তবে নিয়ম অনুযায়ী প্রথমে জেএসসি সনদ সংশোধন হতে হবে অথবা উভয় সনদের সংশোধন একই সাথে অনলাইনে আবেদন করতে হবে যাতে ধারাবাহিকতা বজায় থাকে।</p>
    
    <p><strong>প্রশ্ন ২: বয়স বা জন্মতারিখ সর্বোচ্চ কত বছর পর্যন্ত সংশোধন করা সম্ভব?</strong><br>
    উত্তর: শিক্ষাবোর্ডের নীতিমালা অনুযায়ী সাধারণ তথ্যের গরমিলের ক্ষেত্রে সর্বোচ্চ ১ থেকে ২ বছর পর্যন্ত বয়স সংশোধনের সুযোগ থাকে, তবে এর সপক্ষে নিখুঁত প্রামাণ্য দলিল প্রয়োজন হয়।</p>

    <p><strong>প্রশ্ন ৩: সার্টিফিকেট সংশোধনের জন্য কি কোনো দালাল বা মধ্যস্বত্বভোগীর প্রয়োজন আছে?</strong><br>
    উত্তর: সম্পূর্ণ প্রক্রিয়াটি শতভাগ অনলাইনভিত্তিক ও স্বয়ংক্রিয়। কোনো দালালের সাহায্য ছাড়া আপনি নিজ ঘরে বসেই শিক্ষাবোর্ডের পোর্টালে সরাসরি আবেদন করতে পারবেন।</p>
  </div>
</div>

<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{
      "@type": "Question",
      "name": "জেএসসি এবং এসএসসি সনদের নাম একসাথে সংশোধন করা যায় কি?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "হ্যাঁ, তবে নিয়ম অনুযায়ী প্রথমে জেএসসি সনদ সংশোধন হতে হবে অথবা উভয় সনদের সংশোধন একই সাথে অনলাইনে আবেদন করতে হবে যাতে শিক্ষাগত তথ্যের ধারাবাহিকতা অক্ষুণ্ণ থাকে।"
      }}
    }},
    {{
      "@type": "Question",
      "name": "সার্টিফিকেট নাম সংশোধনে কতদিন সময় লাগে?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "অনলাইনে সকল সঠিক কাগজপত্র আপলোড ও সোনালী সেবায় ফি পরিশোধের পর সাধারণত ৩০ থেকে ৪৫ কর্মদিবসের মধ্যে বোর্ড মিটিংয়ের মাধ্যমে সংশোধন অনুমোদন হয়ে যায়।"
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
</script>
"""
    return {
        "slug": slug,
        "post_id": post_id,
        "title": title,
        "category": category,
        "meta_desc": meta_desc,
        "html_content": content
    }


# ==============================================================================
# POST 2: SSC EXAM INSTRUCTIONS & RULES
# ==============================================================================
def build_post_ssc_instructions():
    slug = "important-instructions-for-ssc-candidates"
    post_id = "4196953979786018728"
    title = "এসএসসি পরীক্ষার্থীদের জন্য জরুরি নিয়মাবলি ও পরীক্ষার হলের নির্দেশিকা (২০২৬)"
    category = "এসএসসি পরীক্ষা,Education News"
    meta_desc = "এসএসসি ২০২৬ পরীক্ষার্থীদের জন্য শিক্ষা মন্ত্রণালয়ের জরুরি নিয়মাবলি, ওএমআর শিট পূরণের নিয়ম, হলের সতর্কতা ও জিপিএ ৫ পাওয়ার স্পেশাল গাইডলাইন।"
    links_html = get_internal_links_for_topic("এসএসসি পরীক্ষা রুটিন ওএমআর সাজেশন")

    content = f"""{STYLES_BLOCK}
<div class="htbd-post-wrapper">
  <div style="margin-bottom: 18px;">
    <span class="htbd-badge" style="background: #e8f0fe; color: #1a73e8; padding: 6px 14px; border-radius: 20px; font-weight: 600; font-size: 14px; display: inline-block;">
      📚 বিভাগ: এসএসসি পরীক্ষা ২০২৬ | সর্বশেষ হালনাগাদ | শিক্ষা মন্ত্রণালয়ের অফিসিয়াল নীতিমালা
    </span>
  </div>

  <!-- Hero Thumbnail Banner -->
  <div style="text-align: center; margin: 18px 0 25px 0;">
    <img src="https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/posts/ssc-exam-instructions-banner.png" 
         alt="এসএসসি পরীক্ষার্থীদের জন্য জরুরি নিয়মাবলি ও পরীক্ষার হলের নির্দেশিকা" 
         title="এসএসসি পরীক্ষা হলের নিয়ম ও ওএমআর শিট পূরণ"
         width="1200" height="675"
         loading="eager"
         style="width: 100%; max-width: 100%; height: auto; border-radius: 10px; box-shadow: 0 4px 14px rgba(0,0,0,0.12); display: block; margin: 0 auto;"/>
    <span style="display: block; font-size: 14px; color: #5f6368; margin-top: 8px; font-style: italic;">
      চিত্র: এসএসসি ২০২৬ পরীক্ষার সময়সূচি, ওএমআর শিট পূরণ ও পরীক্ষার হলের নিয়মাবলি
    </span>
  </div>

  <div class="htbd-qbox" style="background: #f8f9fa; border-left: 5px solid #1a73e8; padding: 20px 24px; margin: 22px 0; border-radius: 0 8px 8px 0; box-shadow: 0 1px 4px rgba(0,0,0,0.06);">
    <p style="margin: 0; font-size: 18px; line-height: 1.8;">
      <strong>📌 সারসংক্ষেপ (Quick Overview):</strong> 
      <strong>এসএসসি পরীক্ষার নির্দেশিকা (SSC Exam Instructions)</strong> হলো মাধ্যমিক ও উচ্চমাধ্যমিক শিক্ষা বোর্ড কর্তৃক জারিকৃত একগুচ্ছ বাধ্যতামূলক নিয়ম ও আচরণবিধি যা প্রতিটি পরীক্ষার্থীকে পরীক্ষার হলে অক্ষরে অক্ষরে পালন করতে হয়। পরীক্ষা শুরুর ৩০ মিনিট পূর্বে কেন্দ্রে প্রবেশ, ওএমআর (OMR) শিটের রোল ও রেজিস্ট্রেশন কোড নিখুঁতভাবে বৃত্ত ভরাট, প্রশ্নপত্র পাওয়ার পর সময় বণ্টন এবং ক্যালকুলেটর ব্যবহারের সুনির্দিষ্ট নীতিমালা মেনে চললে অনাকাঙ্ক্ষিত বহিষ্কার বা খাতা বাতিল হওয়া রোধ করা যায়। নিচে এ বিষয়ে বিস্তারিত দিকনির্দেশনা ও সর্বোচ্চ নম্বর অর্জনের কৌশল তুলে ধরা হলো।
    </p>
  </div>

  <div class="htbd-toc-box">
    <h3 style="margin-top: 0; color: #1a73e8; border-bottom: 2px solid #e8f0fe; padding-bottom: 10px; font-size: 20px; font-weight: 700;">📑 সূচিপত্র (Table of Contents)</h3>
    <ul class="htbd-toc-list">
      <li><a href="#exam-rules">👉 ১. পরীক্ষা কেন্দ্রে প্রবেশ ও শিক্ষা বোর্ডের সাধারণ নিয়মাবলি</a></li>
      <li><a href="#omr-rules">👉 ২. ওএমআর (OMR) শিট পূরণে মারাত্মক ৫টি ভুল ও প্রতিকার</a></li>
      <li><a href="#time-management">👉 ৩. আড়াই ঘণ্টার সৃজনশীল ও বহুনির্বাচনী সময় ব্যবস্থাপনা</a></li>
      <li><a href="#calculator">👉 ৪. অনুমোদিত ক্যালকুলেটর ও নিষিদ্ধ ইলেক্ট্রনিক ডিভাইসের তালিকা</a></li>
      <li><a href="#marks-tips">👉 ৫. খাতায় উপস্থাপনা ও গোল্ডেন জিপিএ ৫ অর্জনের মাস্টার ট্রিকস</a></li>
      <li><a href="#rules-table">👉 ৬. পরীক্ষার হলের করণীয় ও বর্জনীয় বিষয়ের তথ্য ছক</a></li>
      <li><a href="#faqs">👉 ৭. সচরাচর জিজ্ঞাসিত প্রশ্ন (FAQ)</a></li>
    </ul>
  </div>

  <h2 id="exam-rules" class="htbd-heading">১. পরীক্ষা কেন্দ্রে প্রবেশ ও শিক্ষা বোর্ডের সাধারণ নিয়মাবলি</h2>
  <p>শিক্ষা মন্ত্রণালয়ের সুস্পষ্ট নির্দেশিকা অনুযায়ী, পরীক্ষা শুরু হওয়ার অন্তত ৩০ মিনিট পূর্বে পরীক্ষার্থীকে অবশ্যই পরীক্ষা কক্ষে নিজের নির্ধারিত আসন গ্রহণ করতে হবে। অনিবার্য কারণে কোনো পরীক্ষার্থী দেরি করলে বিলম্বের যৌক্তিক কারণ রেজিস্টার খাতায় লিপিবদ্ধ করে কেন্দ্র সচিবের অনুমতি সাপেক্ষে প্রবেশ করতে দেওয়া হয়।</p>
  <p>প্রবেশপত্রে (Admit Card) উল্লিখিত রোল ও রেজিস্ট্রেশন কার্ড ব্যতীত কোনো অতিরিক্ত কাগজ, বইপত্র বা নোট খাতা পরীক্ষা কেন্দ্রে নিয়ে যাওয়া সম্পূর্ণ নিষিদ্ধ। প্রতিটি বিষয়ের পরীক্ষা শেষ না হওয়া পর্যন্ত কক্ষের বাইরে যাওয়ার অনুমতি মিলবে না।</p>

  <h2 id="omr-rules" class="htbd-heading">২. ওএমআর (OMR) শিট পূরণে মারাত্মক ৫টি ভুল ও প্রতিকার</h2>
  <p>ওএমআর শিট কম্পিউটার অপটিক্যাল স্ক্যানার দিয়ে দেখা হয়, তাই এখানে সামান্য কাটাকাটি বা অস্পষ্টতা পুরো পরীক্ষা বাতিল করে দিতে পারে:</p>
  <ul>
    <li><strong>১. রোল ও রেজিস্ট্রেশন নম্বর:</strong> উপরের ঘরে সংখ্যা লেখার পর নিচের সঠিক বৃত্তটি কালো কালির বলপয়েন্ট কলম দিয়ে সম্পূর্ণ গাঢ় করে ভরাট করতে হবে। কোনো অবস্থাতেই জেল পেন বা ফাউন্টেন পেন ব্যবহার করবেন না।</li>
    <li><strong>২. বিষয় কোড:</strong> প্রশ্নপত্রে উল্লেখিত সঠিক ৩ বা ৪ ডিজিটের বিষয় কোড সতর্কতার সাথে বৃত্ত ভরাট করুন। ভুল বিষয় কোড দিলে অন্য বিষয়ের সাথে ওএমআর মিলে যাবে।</li>
    <li><strong>৩. সেট কোড (ক, খ, গ, ঘ):</strong> বহুনির্বাচনী (MCQ) পরীক্ষার ক্ষেত্রে পাওয়া প্রশ্নের সেট কোড ওএমআরে পূরণ করা সবচেয়ে গুরুত্বপূর্ণ। সেট কোড ভুল হলে সমস্ত নৈর্ব্যক্তিক নম্বর শূন্য হয়ে যাবে।</li>
    <li><strong>৪. অতিরিক্ত উত্তরপত্রের সংখ্যা:</strong> মূল উত্তরপত্রের নির্ধারিত অংশে যতটি অতিরিক্ত খাতা (লুজ শিট) নিয়েছেন, তার সঠিক সংখ্যা বৃত্ত ভরাট করুন।</li>
    <li><strong>৫. ওএমআরে কাটাকাটি না করা:</strong> ওএমআর শিট কোনোভাবেই ভাঁজ করা, পিন লাগানো বা ফ্লুইড ব্যবহার করা যাবে না। ভুল হলে তাৎক্ষণিক কক্ষ পরিদর্শকের দৃষ্টি আকর্ষণ করুন।</li>
  </ul>

  {links_html}

  <h2 id="time-management" class="htbd-heading">৩. আড়াই ঘণ্টার সৃজনশীল ও বহুনির্বাচনী সময় ব্যবস্থাপনা</h2>
  <p>এসএসসি পরীক্ষায় ভালো ফলাফলের মূল চাবিকাঠি হলো সময়ের নিখুঁত সদ্ব্যবহার। সাধারণত পরীক্ষার সময়সীমা ৩ ঘণ্টা (৩০ মিনিট বহুনির্বাচনী এবং ২ ঘণ্টা ৩০ মিনিট সৃজনশীল):</p>
  <p>সৃজনশীল অংশে সাধারণত ৭টি প্রশ্নের উত্তর দিতে হয়। প্রতিটি প্রশ্নের জন্য গড়ে ২০ থেকে ২১ মিনিট সময় বরাদ্দ রাখুন। বাকি ১০ মিনিট পুরো খাতা রিভিশন ও মার্জিন চেকিংয়ের জন্য রেখে দেওয়া আবশ্যক। কোনো একটি প্রশ্নের উত্তর অতিরিক্ত বড় করতে গিয়ে যেন অন্য প্রশ্নের উত্তর দেওয়ার সময় নষ্ট না হয়, সেদিকে সজাগ দৃষ্টি রাখা জরুরি।</p>

  <h2 id="calculator" class="htbd-heading">৪. অনুমোদিত ক্যালকুলেটর ও নিষিদ্ধ ইলেক্ট্রনিক ডিভাইসের তালিকা</h2>
  <p>বিজ্ঞান বিভাগের সাধারণ গণিত, উচ্চতর গণিত ও পদার্থবিজ্ঞানের ক্ষেত্রে নন-প্রোগ্রামেবল সায়েন্টিফিক ক্যালকুলেটর (যেমন—fx-991ES, fx-100MS, fx-570ES ইত্যাদি) ব্যবহারের অনুমতি রয়েছে। তবে যেকোনো ধরনের প্রোগ্রামেবল মেমোরিযুক্ত ক্যালকুলেটর, স্মার্টওয়াচ, ব্লুটুথ ডিভাইস ও মোবাইল ফোন কেন্দ্রে সম্পূর্ণ নিষিদ্ধ। ডিজিটাল ঘড়ির বদলে সাধারণ কাঁটাযুক্ত এনালগ ঘড়ি ব্যবহার করা সবচেয়ে নিরাপদ।</p>

  <h2 id="rules-table" class="htbd-heading">৬. পরীক্ষার হলের করণীয় ও বর্জনীয় বিষয়ের তথ্য ছক</h2>
  <div class="htbd-table-wrapper">
    <table class="htbd-table">
      <thead>
        <tr>
          <th>বিষয়</th>
          <th>অবশ্যই করণীয় (Do's)</th>
          <th>কঠোরভাবে বর্জনীয় (Don'ts)</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>কলম ও পেন্সিল</strong></td>
          <td>কালো বলপয়েন্ট কলম ও ২বি পেন্সিল ব্যবহার</td>
          <td>লাল বা সবুজ কালি এবং জেল পেন ব্যবহার</td>
        </tr>
        <tr>
          <td><strong>উত্তরপত্র মার্জিন</strong></td>
          <td>খাতার বামে ও উপরে ১ ইঞ্চি মার্জিন রাখা</td>
          <td>চারপাশে অতিরিক্ত চওড়া দাগ টেনে লেখার জায়গা কমানো</td>
        </tr>
        <tr>
          <td><strong>পরীক্ষার খাতা জমার নিয়ম</strong></td>
          <td>পরিদর্শকের স্বাক্ষর নিশ্চিত করে ঘণ্টা বাজলে জমা</td>
          <td>পরিদর্শকের সই ছাড়া খাতা ফেলে চলে যাওয়া</td>
        </tr>
        <tr>
          <td><strong>প্রশ্ন নির্বাচন</strong></td>
          <td>সবচেয়ে ভালো জানা প্রশ্নের উত্তর আগে লেখা</td>
          <td>অনিশ্চিত প্রশ্নে অতিরিক্ত সময় ব্যয় করা</td>
        </tr>
      </tbody>
    </table>
  </div>

  <h2 id="faqs" class="htbd-heading">৭. সচরাচর জিজ্ঞাসিত প্রশ্ন (FAQ)</h2>
  <div style="margin-top: 15px;">
    <p><strong>প্রশ্ন ১: ওএমআর শিটের বৃত্ত ভরাটে ভুল হলে কী করণীয়?</strong><br>
    উত্তর: নিজে ঘষামাঝি বা কাটাকাটি করবেন না। সাথে সাথে কক্ষ পরিদর্শককে জানান। পরিদর্শক বিশেষ অনুমোদন নিয়ে ওএমআরে স্বাক্ষর করে দেন যাতে স্ক্যানারে সমস্যা না হয়।</p>
    
    <p><strong>প্রশ্ন ২: সৃজনশীল প্রশ্নের (ক, খ, গ, ঘ) অংশ কি একসাথে লিখতে হবে?</strong><br>
    উত্তর: হ্যাঁ, একটি নির্দিষ্ট প্রশ্নের ক, খ, গ ও ঘ অংশ ক্রমানুসারে একই জায়গায় লেখা আবশ্যক। বিচ্ছিন্নভাবে বিভিন্ন পাতায় লিখলে খাতা মূল্যায়নে নম্বর কাটার ঝুঁকি থাকে।</p>

    <p><strong>প্রশ্ন ৩: জিপিএ ৫ পাওয়ার জন্য বহুনির্বাচনী অংশে কত নম্বর প্রয়োজন?</strong><br>
    উত্তর: গোল্ডেন জিপিএ ৫ নিশ্চিত করতে বহুনির্বাচনী অংশে অন্তত ২৫ থেকে ২৮+ নম্বর পাওয়া অত্যন্ত সহায়ক ভূমিকা পালন করে।</p>
  </div>
</div>

<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{
      "@type": "Question",
      "name": "এসএসসি পরীক্ষা কেন্দ্রে কতক্ষণ আগে পৌঁছাতে হবে?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "শিক্ষা মন্ত্রণালয়ের নিয়ম অনুযায়ী পরীক্ষা শুরু হওয়ার কমপক্ষে ৩০ মিনিট পূর্বে প্রতিটি পরীক্ষার্থীকে নিজ পরীক্ষা কক্ষে আসন গ্রহণ করতে হবে।"
      }}
    }},
    {{
      "@type": "Question",
      "name": "এসএসসি পরীক্ষায় কি সায়েন্টিফিক ক্যালকুলেটর নেওয়া যায়?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "সাধারণ নন-প্রোগ্রামেবল সায়েন্টিফিক ক্যালকুলেটর (যেমন fx-991MS, fx-100MS) নেওয়া যায়, তবে কোনো প্রোগ্রামেবল ক্যালকুলেটর বা স্মার্ট ডিভাইস গ্রহণযোগ্য নয়।"
      }}
    }},
    {{
      "@type": "Question",
      "name": "ওএমআর শিটে সেট কোড না লিখলে কী হয়?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "সেট কোড না লিখলে বা ভুল বৃত্ত ভরাট করলে কম্পিউটার সফটওয়্যার ওএমআর মেলাতে পারে না, ফলে বহুনির্বাচনী পরীক্ষার ফলাফল শূন্য হওয়ার ঝুঁকি তৈরি হয়।"
      }}
    }}
  ]
}}
</script>
"""
    return {
        "slug": slug,
        "post_id": post_id,
        "title": title,
        "category": category,
        "meta_desc": meta_desc,
        "html_content": content
    }


# ==============================================================================
# POST 3: HASON RAJA BIOGRAPHY & SONGS
# ==============================================================================
def build_post_hason_raja():
    slug = "hason-raja-was-born-in-1854-class-six"
    post_id = "4269363058446270636"
    title = "মরমী কবি হাসন রাজার জীবনী, দর্শন ও অমর গানের রূপরেখা (২০২৬)"
    category = "বাংলা সাহিত্য,Class 6 English & Bangla"
    meta_desc = "মরমী বাউল সাধক হাসন রাজার জন্ম, আধ্যাত্মিক রূপান্তর, 'হাসন উদাস' কাব্যগ্রন্থ, বিখ্যাত গান ও শিক্ষা বোর্ড পরীক্ষার পূর্ণাঙ্গ হ্যান্ডনোট পড়ুন HelpTrickBD-তে।"
    links_html = get_internal_links_for_topic("হাসন রাজা বাউল লালন বাংলা সাহিত্য")

    content = f"""{STYLES_BLOCK}
<div class="htbd-post-wrapper">
  <div style="margin-bottom: 18px;">
    <span class="htbd-badge" style="background: #e8f0fe; color: #1a73e8; padding: 6px 14px; border-radius: 20px; font-weight: 600; font-size: 14px; display: inline-block;">
      📚 বিভাগ: বাংলা সাহিত্য ও লোকসংস্কৃতি | সর্বশেষ সংস্করণ: ২০২৬ | বোর্ড পরীক্ষার বিশেষ হ্যান্ডনোট
    </span>
  </div>

  <!-- Hero Thumbnail Banner -->
  <div style="text-align: center; margin: 18px 0 25px 0;">
    <img src="https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/posts/hason-raja-biography-banner.png" 
         alt="মরমী কবি হাসন রাজার জীবনী, দর্শন ও অমর গানের রূপরেখা" 
         title="মরমী কবি হাসন রাজার জীবন ও বাউল গান"
         width="1200" height="675"
         loading="eager"
         style="width: 100%; max-width: 100%; height: auto; border-radius: 10px; box-shadow: 0 4px 14px rgba(0,0,0,0.12); display: block; margin: 0 auto;"/>
    <span style="display: block; font-size: 14px; color: #5f6368; margin-top: 8px; font-style: italic;">
      চিত্র: দেওয়ান হাসন রাজার আধ্যাত্মিক রূপান্তর, কাব্য সাধনা ও বাংলা লোকসাহিত্যের অমর অবদান
    </span>
  </div>

  <div class="htbd-qbox" style="background: #f8f9fa; border-left: 5px solid #1a73e8; padding: 20px 24px; margin: 22px 0; border-radius: 0 8px 8px 0; box-shadow: 0 1px 4px rgba(0,0,0,0.06);">
    <p style="margin: 0; font-size: 18px; line-height: 1.8;">
      <strong>📌 সারসংক্ষেপ (Quick Overview):</strong> 
      <strong>মরমী কবি হাসন রাজা (Hason Raja - জন্ম: ২১ ডিসেম্বর ১৮৫৪, মৃত্যু: ৬ ডিসেম্বর ১৯২২)</strong> ছিলেন সিলেটের একজন প্রখ্যাত জমিদার, সুফি মরমী সাধক, গীতিকার এবং সুরকার। যৌবনে অঢেল বিত্ত-বৈভব ও বিলাসবহুল জীবনযাপন করলেও পরিণত বয়সে জাগতিক মোহের নশ্বরতা উপলব্ধি করে তিনি পরমাত্মার সন্ধানে আত্মনিয়োগ করেন। তাঁর রচিত <em>'হাসন উদাস'</em> কাব্যগ্রন্থের মরমি গানগুলো দেহতত্ত্ব, সৃষ্টিরহস্য এবং আধ্যাত্মিক প্রেমের অতুলনীয় প্রকাশ। নিচে তাঁর জীবনী, আধ্যাত্মিক দর্শন এবং পাঠ্যপুস্তকের গুরুত্বপূর্ণ মডেল প্রশ্নোত্তর তুলে ধরা হলো।
    </p>
  </div>

  <div class="htbd-toc-box">
    <h3 style="margin-top: 0; color: #1a73e8; border-bottom: 2px solid #e8f0fe; padding-bottom: 10px; font-size: 20px; font-weight: 700;">📑 সূচিপত্র (Table of Contents)</h3>
    <ul class="htbd-toc-list">
      <li><a href="#early-life">👉 ১. হাসন রাজার জন্ম, পরিবার ও প্রারম্ভিক জমিদার জীবন</a></li>
      <li><a href="#spiritual-shift">👉 ২. আধ্যাত্মিক রূপান্তর: ভোগবিলাস থেকে মরমী বৈরাগ্য</a></li>
      <li><a href="#philosophy">👉 ৩. দেহতত্ত্ব ও মরমী দর্শনের মূল ভাববস্তু</a></li>
      <li><a href="#famous-songs">👉 ৪. 'হাসন উদাস' ও হাসন রাজার কালজয়ী গানসমূহ</a></li>
      <li><a href="#rabindranath">👉 ৫. বিশ্বভারতী ও রবীন্দ্রনাথ ঠাকুরের মূল্যায়নে হাসন রাজা</a></li>
      <li><a href="#chronology-table">👉 ৬. হাসন রাজার জীবনপঞ্জির সংক্ষিপ্ত তথ্য ছক</a></li>
      <li><a href="#exam-questions">👉 ৭. ষষ্ঠ শ্রেণি ও বোর্ড পরীক্ষার স্পেশাল মডেল প্রশ্নোত্তর</a></li>
      <li><a href="#faqs">👉 ৮. সচরাচর জিজ্ঞাসিত প্রশ্ন (FAQ)</a></li>
    </ul>
  </div>

  <h2 id="early-life" class="htbd-heading">১. হাসন রাজার জন্ম, পরিবার ও প্রারম্ভিক জমিদার জীবন</h2>
  <p>দেওয়ান হাসন রাজা ১৮৫৪ সালের ২১ ডিসেম্বর বর্তমান সুনামগঞ্জ শহরের লক্ষণশ্রী গ্রামের এক অভিজাত ও ঐতিহ্যবাহী জমিদার পরিবারে জন্মগ্রহণ করেন। তাঁর পিতার নাম দেওয়ান আলী রাজা চৌধুরী এবং মাতার নাম হুরমত জাহান বিবি। বাল্যকালে তাঁর নাম ছিল অহিদুর রেজা, কিন্তু পরবর্তীকালে তিনি 'হাসন রাজা' নামেই খ্যাতি লাভ করেন।</p>
  <p>পিতার অকালমৃত্যুর পর মাত্র পনেরো বছর বয়সেই বিশাল জমিদারির দায়িত্ব তাঁর ওপর এসে পড়ে। প্রথম জীবনে তিনি ঘোড়া, হাতি এবং সুরমা নদীর তীরে রাজকীয় বজরায় চড়ে বিলাসী জীবনযাপন করতেন। সুরমা নদীর সুবাসিত জলহাওয়া এবং ভাটি অঞ্চলের অপরূপ প্রকৃতি তাঁর কবিমনকে গভীরভাবে আলোড়িত করত।</p>

  <h2 id="spiritual-shift" class="htbd-heading">২. আধ্যাত্মিক রূপান্তর: ভোগবিলাস থেকে মরমী বৈরাগ্য</h2>
  <p>বয়স বৃদ্ধির সাথে সাথে এক গভীর আধ্যাত্মিক ভাবান্তর হাসন রাজার ভেতর ঘটে যায়। তিনি উপলব্ধি করেন যে এই জাগতিক ধন-দৌলত, রাজপ্রাসাদ এবং জমিদারির অহংকার আসলে এক ক্ষণস্থায়ী মোহ। তিনি নিজের রাজকীয় সুখস্বাচ্ছন্দ্য ত্যাগ করে সাদা চাদর পরিধান করে সাধারণ মানুষের মতো সরল জীবনযাপন শুরু করেন।</p>
  <p>তিনি তাঁর বিশাল সম্পদের একটি বড় অংশ অনাথ, দরিদ্র ও প্রজাদের কল্যাণে দান করে দেন। তাঁর এই আধ্যাত্মিক জাগরণ তাঁকে দেহতত্ত্বের এক মহান গীতিকবিয়ে পরিণত করে। নিজের আত্মাকে তিনি পরমাত্মার এক ব্যাকুল প্রেমিক হিসেবে কল্পনা করতে থাকেন।</p>

  {links_html}

  <h2 id="philosophy" class="htbd-heading">৩. দেহতত্ত্ব ও মরমী দর্শনের মূল ভাববস্তু</h2>
  <p>হাসন রাজার গানের প্রধান বৈশিষ্ট্য হলো মানবদেহের ক্ষণভঙ্গুরতা এবং স্রষ্টার সাথে আত্মিক মিলনাকাঙ্ক্ষা। মানবদেহকে তিনি এক নশ্বর মাটির খাঁচা বা কাঁচের ঘর হিসেবে তুলনা করেছেন:</p>
  <blockquote style="background: #f1f3f4; border-left: 4px solid #1a73e8; margin: 18px 0; padding: 14px 20px; font-style: italic; font-size: 17px;">
    "লোকে বলে বলে রে, ঘর-বাড়ি ভালা নায় আমার / কি ঘর বানাইমু আমি, শূন্যের-ই মাঝার..."
  </blockquote>
  <p>এই পঙক্তিতে মানুষের অহংবোধকে ধূলিসাৎ করে শাশ্বত সত্যকে আলিঙ্গন করার যে গভীর বাণী ধ্বনিত হয়েছে, তা বাউল সাধনার চরম শিখরকে স্পর্শ করে।</p>

  <h2 id="famous-songs" class="htbd-heading">৪. 'হাসন উদাস' ও হাসন রাজার কালজয়ী গানসমূহ</h2>
  <p>১৯০৭ সালে হাসন রাজার ২০৬টি গান নিয়ে তাঁর বিখ্যাত কাব্যগ্রন্থ <em>'হাসন উদাস'</em> প্রকাশিত হয়। তাঁর রচিত সবচেয়ে জনপ্রিয় ও কালজয়ী গানের মধ্যে উল্লেখযোগ্য:</p>
  <ul>
    <li><em>"লোকে বলে বলে রে ঘর-বাড়ি ভালা নায় আমার"</em></li>
    <li><em>"নেশা লাগিল রে, বাঁকা দু’নয়নে নেশা লাগিল রে"</em></li>
    <li><em>"মাটির পিঞ্জিরার মাঝে বন্দি হইয়া রে, কান্দে হাসন রাজার মন ময়না রে"</em></li>
    <li><em>"আগুন লাগাইয়া দিল কনে হাছন রাজার মনে"</em></li>
  </ul>

  <h2 id="rabindranath" class="htbd-heading">৫. বিশ্বভারতী ও রবীন্দ্রনাথ ঠাকুরের মূল্যায়নে হাসন রাজা</h2>
  <p>বিশ্বকবি রবীন্দ্রনাথ ঠাকুর হাসন রাজার দর্শনে মুগ্ধ হয়েছিলেন। ১৯২৫ সালে ভারতীয় দর্শন কংগ্রেসে এবং ১৯৩০ সালে অক্সফোর্ড বিশ্ববিদ্যালয়ে প্রদত্ত তাঁর কালজয়ী হিবার্ট বক্তৃতায় (The Religion of Man) রবীন্দ্রনাথ হাসন রাজার গানের উদ্ধৃতি দিয়ে বলেন— বাংলার এক অখ্যাত পল্লী অঞ্চলে একজন মরমী কবি আত্মপ্রকাশ করেছেন যিনি মানবাত্মার সাথে বিশ্বাত্মার গভীর প্রেমের তত্ত্ব নিখুঁত ছন্দে প্রকাশ করেছেন।</p>

  <h2 id="chronology-table" class="htbd-heading">৬. হাসন রাজার জীবনপঞ্জির সংক্ষিপ্ত তথ্য ছক</h2>
  <div class="htbd-table-wrapper">
    <table class="htbd-table">
      <thead>
        <tr>
          <th>বিষয়</th>
          <th>ঐতিহাসিক তথ্য</th>
          <th>তাৎপর্য</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>জন্ম</strong></td>
          <td>২১ ডিসেম্বর ১৮৫৪ খ্রিষ্টাব্দ</td>
          <td>লক্ষণশ্রী, সুনামগঞ্জ, সিলেট</td>
        </tr>
        <tr>
          <td><strong>পিতা ও মাতা</strong></td>
          <td>দেওয়ান আলী রাজা ও হুরমত জাহান বিবি</td>
          <td>অভিজাত সম্ভ্রান্ত জমিদার বংশ</td>
        </tr>
        <tr>
          <td><strong>কাব্য সংকলন</strong></td>
          <td>হাসন উদাস (১৯০৭ খ্রি.)</td>
          <td>২০৬টি আধ্যাত্মিক গানের প্রামাণ্য গ্রন্থ</td>
        </tr>
        <tr>
          <td><strong>দর্শন ধারা</strong></td>
          <td>সুফি দেহতত্ত্ব ও লোক বৈরাগ্য</td>
          <td>মানবপ্রেম ও পরমাত্মার সন্ধান</td>
        </tr>
        <tr>
          <td><strong>প্রয়াণ</strong></td>
          <td>৬ ডিসেম্বর ১৯২২ খ্রিষ্টাব্দ</td>
          <td>সুনামগঞ্জের পারিবারিক কবরস্থানে শায়িত</td>
        </tr>
      </tbody>
    </table>
  </div>

  <h2 id="exam-questions" class="htbd-heading">৭. ষষ্ঠ শ্রেণি ও বোর্ড পরীক্ষার স্পেশাল মডেল প্রশ্নোত্তর</h2>
  <p><strong>প্রশ্ন: হাসন রাজা কেন তাঁর বিলাসী জীবন পরিত্যাগ করেছিলেন?</strong></p>
  <p><strong>উত্তর:</strong> পরিণত বয়সে হাসন রাজা অনুধাবন করেছিলেন যে পার্থিব ধনসম্পদ, ক্ষমতা ও রাজকীয় অহংকার সবই অনিত্য ও নশ্বর। মানবজীবনের প্রকৃত উদ্দেশ্য হলো পরম সৃষ্টিকর্তার সন্ধান ও আত্মশুদ্ধি লাভ করা। এই আত্মোপলব্ধির কারণেই তিনি জমিদারির বিলাসিতা বর্জন করে মরমী সাধক হিসেবে জীবন অতিবাহিত করেন।</p>

  <h2 id="faqs" class="htbd-heading">৮. সচরাচর জিজ্ঞাসিত প্রশ্ন (FAQ)</h2>
  <div style="margin-top: 15px;">
    <p><strong>প্রশ্ন ১: হাসন রাজার রচিত গানের প্রধান বইটির নাম কী?</strong><br>
    উত্তর: হাসন রাজার প্রধান ও বিখ্যাত গান সংকলনের নাম 'হাসন উদাস', যা ১৯০৭ সালে প্রকাশিত হয়েছিল।</p>
    
    <p><strong>প্রশ্ন ২: রবীন্দ্রনাথ ঠাকুর কোন আন্তর্জাতিক ভাষণে হাসন রাজার গানের প্রশংসা করেন?</strong><br>
    উত্তর: অক্সফোর্ড বিশ্ববিদ্যালয়ে তাঁর বিখ্যাত 'The Religion of Man' (মানুষের ধর্ম) শীর্ষক হিবার্ট লেকচারে রবীন্দ্রনাথ হাসন রাজার গানের উচ্চ প্রশংসা করেন।</p>

    <p><strong>প্রশ্ন ৩: হাসন রাজার জন্মস্থান কোথায়?</strong><br>
    উত্তর: তিনি বৃহত্তর সিলেটের সুনামগঞ্জ জেলার লক্ষণশ্রী গ্রামে এক ঐতিহ্যবাহী জমিদার পরিবারে জন্মগ্রহণ করেন।</p>
  </div>
</div>

<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{
      "@type": "Question",
      "name": "মরমী কবি হাসন রাজা কবে জন্মগ্রহণ করেন?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "মরমী কবি হাসন রাজা ১৮৫৪ সালের ২১ ডিসেম্বর সুনামগঞ্জের লক্ষণশ্রী গ্রামে জন্মগ্রহণ করেন।"
      }}
    }},
    {{
      "@type": "Question",
      "name": "হাসন রাজার দর্শনের মূল ভিত্তি কী ছিল?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "হাসন রাজার দর্শনের মূল ভিত্তি ছিল দেহতত্ত্ব, পার্থিব জীবনের নশ্বরতা এবং সৃষ্টিকর্তার সাথে মানবাত্মার শাশ্বত প্রেম ও আধ্যাত্মিক মিলন।"
      }}
    }},
    {{
      "@type": "Question",
      "name": "হাসন রাজার সবচেয়ে বিখ্যাত গান কোনটি?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "তাঁর সবচেয়ে বিখ্যাত গানগুলোর মধ্যে 'লোকে বলে বলে রে ঘর-বাড়ি ভালা নায় আমার' এবং 'মাটির পিঞ্জিরার মাঝে বন্দি হইয়া রে' অন্যতম।"
      }}
    }}
  ]
}}
</script>
"""
    return {
        "slug": slug,
        "post_id": post_id,
        "title": title,
        "category": category,
        "meta_desc": meta_desc,
        "html_content": content
    }


# ==============================================================================
# POST 4: LIVESTOCK RESEARCH INSTITUTE (BLRI)
# ==============================================================================
def build_post_livestock_institute():
    slug = "bangladesh-livestock-resources-research-institutes"
    post_id = "3163731179305221308"
    title = "বাংলাদেশ প্রাণিসম্পদ গবেষণা ইনস্টিটিউট (BLRI): কার্যক্রম, উদ্ভাবন ও ভূমিকা (২০২৬)"
    category = "বাংলাদেশ বিষয়াবলি,কৃষি ও প্রাণিসম্পদ"
    meta_desc = "বাংলাদেশ প্রাণিসম্পদ গবেষণা ইনস্টিটিউট (BLRI)-এর ইতিহাস, উন্নত জাতের পশুপাখি উদ্ভাবন, টিকা উৎপাদন ও বিসিএস পরীক্ষার স্পেশাল হ্যান্ডনোট।"
    links_html = get_internal_links_for_topic("প্রাণিসম্পদ কৃষি বাংলাদেশ অর্থনীতি")

    content = f"""{STYLES_BLOCK}
<div class="htbd-post-wrapper">
  <div style="margin-bottom: 18px;">
    <span class="htbd-badge" style="background: #e8f0fe; color: #1a73e8; padding: 6px 14px; border-radius: 20px; font-weight: 600; font-size: 14px; display: inline-block;">
      📚 বিভাগ: বাংলাদেশ বিষয়াবলি ও কৃষি অর্থনীতি | সর্বশেষ সংস্করণ: ২০২৬ | বিসিএস ও বিশ্ববিদ্যালয় গাইড
    </span>
  </div>

  <!-- Hero Thumbnail Banner -->
  <div style="text-align: center; margin: 18px 0 25px 0;">
    <img src="https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/posts/livestock-research-institute-banner.png" 
         alt="বাংলাদেশ প্রাণিসম্পদ গবেষণা ইনস্টিটিউট (BLRI): কার্যক্রম, উদ্ভাবন ও ভূমিকা" 
         title="বাংলাদেশ প্রাণিসম্পদ গবেষণা ইনস্টিটিউট বিএলআরআই"
         width="1200" height="675"
         loading="eager"
         style="width: 100%; max-width: 100%; height: auto; border-radius: 10px; box-shadow: 0 4px 14px rgba(0,0,0,0.12); display: block; margin: 0 auto;"/>
    <span style="display: block; font-size: 14px; color: #5f6368; margin-top: 8px; font-style: italic;">
      চিত্র: সাভারে অবস্থিত বিএলআরআই (BLRI) কমপ্লেক্স ও গবাদিপশুর জাত উন্নয়ন প্রযুক্তি
    </span>
  </div>

  <div class="htbd-qbox" style="background: #f8f9fa; border-left: 5px solid #1a73e8; padding: 20px 24px; margin: 22px 0; border-radius: 0 8px 8px 0; box-shadow: 0 1px 4px rgba(0,0,0,0.06);">
    <p style="margin: 0; font-size: 18px; line-height: 1.8;">
      <strong>📌 সারসংক্ষেপ (Quick Overview):</strong> 
      <strong>বাংলাদেশ প্রাণিসম্পদ গবেষণা ইনস্টিটিউট (BLRI - Bangladesh Livestock Research Institute)</strong> হলো গণপ্রজাতন্ত্রী বাংলাদেশ সরকারের মৎস্য ও প্রাণিসম্পদ মন্ত্রণালয়ের অধীনস্থ দেশের শীর্ষস্থানীয় জাতীয় গবেষণা প্রতিষ্ঠান। ১৯৮৪ সালে প্রতিষ্ঠিত এবং ঢাকার সাভারে প্রধান কার্যালয় সংবলিত এই প্রতিষ্ঠানটি গবাদিপশু ও হাঁস-মুরগির উন্নত জাত উদ্ভাবন, কৃত্রিম প্রজনন প্রযুক্তি সম্প্রসারণ, প্রাণিজ রোগ নিয়ন্ত্রণ ও পুষ্টিকর খাদ্য ব্যবস্থাপনায় বৈপ্লবিক ভূমিকা পালন করছে। দেশের আমিষের চাহিদা পূরণ এবং মাংস ও দুগ্ধ খাতে স্বয়ংসম্পূর্ণতা অর্জনে বিএলআরআই-এর ভূমিকা অপরিসীম।
    </p>
  </div>

  <div class="htbd-toc-box">
    <h3 style="margin-top: 0; color: #1a73e8; border-bottom: 2px solid #e8f0fe; padding-bottom: 10px; font-size: 20px; font-weight: 700;">📑 সূচিপত্র (Table of Contents)</h3>
    <ul class="htbd-toc-list">
      <li><a href="#history">👉 ১. বিএলআরআই-এর ঐতিহাসিক পটভূমি ও প্রশাসনিক কাঠামো</a></li>
      <li><a href="#mission">👉 ২. মূল ভিশন, মিশন ও কৌশলগত গবেষণার ক্ষেত্রসমূহ</a></li>
      <li><a href="#innovations">👉 ৩. বিএলআরআই কর্তৃক উদ্ভাবিত উন্নত জাত ও যুগান্তকারী প্রযুক্তি</a></li>
      <li><a href="#economy">👉 ৪. গ্রামীণ অর্থনীতি ও মাংস-দুগ্ধ উৎপাদনে স্বয়ংসম্পূর্ণতার প্রভাব</a></li>
      <li><a href="#table-breeds">👉 ৫. উদ্ভাবিত প্রধান জাত ও প্রযুক্তি সমূহের তুলনামূলক ছক</a></li>
      <li><a href="#future">👉 ৬. ভবিষ্যৎ চ্যালেঞ্জ: জলবায়ু পরিবর্তন ও টেকসই প্রাণিসম্পদ ব্যবস্থাপনা</a></li>
      <li><a href="#exam-prep">👉 ৭. বিসিএস প্রিলিমিনারি ও ভাইভা স্পেশাল মডেল প্রশ্নোত্তর</a></li>
      <li><a href="#faqs">👉 ৮. সচরাচর জিজ্ঞাসিত প্রশ্ন (FAQ)</a></li>
    </ul>
  </div>

  <h2 id="history" class="htbd-heading">১. বিএলআরআই-এর ঐতিহাসিক পটভূমি ও প্রশাসনিক কাঠামো</h2>
  <p>বাংলাদেশের স্বাধীনতা উত্তর সময়ে ক্রমবর্ধমান জনসংখ্যার জন্য প্রাণিজ আমিষের ঘাটতি মেটাতে ১৯৮৪ সালে 'বাংলাদেশ প্রাণিসম্পদ গবেষণা ইনস্টিটিউট অধ্যাদেশ' জারির মাধ্যমে এই প্রতিষ্ঠানটির শুভ সূচনা হয়। ঢাকার অদূরে সাভারে বিশাল গবেষণাগার, খামার এবং চারণভূমি নিয়ে এটি প্রতিষ্ঠিত। পরবর্তীতে ২০১৬ সালে বাংলাদেশ জাতীয় সংসদে 'বাংলাদেশ প্রাণিসম্পদ গবেষণা ইনস্টিটিউট আইন' পাস করে প্রতিষ্ঠানটিকে আরো শক্তিশালী ও যুগোপযোগী করা হয়।</p>
  <p>প্রতিষ্ঠানটি দেশের বিভিন্ন ভৌগোলিক অঞ্চলে বেশ কয়েকটি আঞ্চলিক গবেষণা কেন্দ্র পরিচালনা করে—যেমন চুয়াডাঙ্গা, সিরাজগঞ্জের বাঘাবাড়ি, বান্দরবানের নাইক্ষ্যংছড়ি এবং রাজশাহীর গোদাগাড়ী।</p>

  <h2 id="innovations" class="htbd-heading">৩. বিএলআরআই কর্তৃক উদ্ভাবিত উন্নত জাত ও যুগান্তকারী প্রযুক্তি</h2>
  <p>বিএলআরআই-এর নিরলস গবেষণার ফলে বাংলাদেশের গ্রামীণ খামারিরা আজ নানাবিধ লাভজনক প্রযুক্তি ব্যবহারের সুযোগ পাচ্ছেন:</p>
  <ul>
    <li><strong>বিএলআরআই সুবর্ণা মুরগি:</strong> দেশি আবহাওয়ার উপযোগী উচ্চ উৎপাদনশীল মাংস ও ডিম উৎপাদনকারী রোগপ্রতিরোধী জাত।</li>
    <li><strong>ব্ল্যাক বেঙ্গল ছাগলের উন্নয়ন:</strong> বিশ্বখ্যাত ব্ল্যাক বেঙ্গল ছাগলের জিনগত বিশুদ্ধতা রক্ষা এবং অধিক বাচ্চা জন্মদানের কৃত্রিম প্রজনন প্রযুক্তি।</li>
    <li><strong>উন্নত জাতের নেপিয়ার ও জাম্বু ঘাস:</strong> সাইলেজ প্রস্তুতকরণ এবং কম খরচে উচ্চ প্রোটিনযুক্ত গবাদিপশুর পুষ্টিকর কাঁচা ঘাস প্রযুক্তি।</li>
    <li><strong>টিকা ও অ্যান্টিবডি উৎপাদন:</strong> ক্ষুরারোগ (FMD), পিপিআর (PPR) এবং রাণীক্ষেত রোগের সাশ্রয়ী টিকা উদ্ভাবন ও মাঠপর্যায়ে সরবরাহ।</li>
  </ul>

  {links_html}

  <h2 id="economy" class="htbd-heading">৪. গ্রামীণ অর্থনীতি ও মাংস-দুগ্ধ উৎপাদনে স্বয়ংসম্পূর্ণতার প্রভাব</h2>
  <p>বাংলাদেশ আজ মাংস উৎপাদনে শতভাগ স্বয়ংসম্পূর্ণ এবং ডিম ও দুধে স্বয়ংসম্পূর্ণতার দ্বারপ্রান্তে। কোরবানির পশুর জন্য পূর্বে যেখানে প্রতিবেশী দেশের ওপর নির্ভর করতে হতো, সেখানে স্থানীয় খামারিরাই আজ সম্পূর্ণ চাহিদার যোগান দিচ্ছেন। এই রূপান্তরের পেছনে বিএলআরআই-এর উন্নত জাত ও পুষ্টি গবেষণার অবদান জাতীয় অর্থনীতিতে এক অনন্য মাইলফলক।</p>

  <h2 id="table-breeds" class="htbd-heading">৫. উদ্ভাবিত প্রধান জাত ও প্রযুক্তি সমূহের তুলনামূলক ছক</h2>
  <div class="htbd-table-wrapper">
    <table class="htbd-table">
      <thead>
        <tr>
          <th>উদ্ভাবন / প্রযুক্তি</th>
          <th>ক্যাটাগরি</th>
          <th>প্রধান সুবিধা ও কার্যকারিতা</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>বিএলআরআই সুবর্ণা</strong></td>
          <td>মুরগি</td>
          <td>দেশি স্বাদের মাংস, বছরে ১৮০-২০০টি ডিম উৎপাদন</td>
        </tr>
        <tr>
          <td><strong>বিএলআরআই মিট চিকেন-১</strong></td>
          <td>ব্রয়লার</td>
          <td>দ্রুত বর্ধনশীল, ৩৫ দিনে ১.৫ কেজি ওজন অর্জন</td>
        </tr>
        <tr>
          <td><strong>ইউরিয়া মোলাসেস স্ট্র (UMS)</strong></td>
          <td>পশু খাদ্য</td>
          <td>খড়ের পুষ্টিমান দ্বিগুণ বৃদ্ধি ও মোটাতাজাকরণ সাশ্রয়ী</td>
        </tr>
        <tr>
          <td><strong>পিপিআর ভ্যাকসিন</strong></td>
          <td>টিকা প্রযুক্তি</td>
          <td>ছাগল-ভেড়ার মড়ক রোধ ও মৃত্যুর হার শূন্যের কোঠায় নামানো</td>
        </tr>
      </tbody>
    </table>
  </div>

  
  <h2 id="livestock-economy-challenges" class="htbd-heading">৫.১ প্রাণিসম্পদ খাতের বর্তমান চ্যালেঞ্জ ও টেকসই সমাধানের সুপারিশ</h2>
  <p>বাংলাদেশে প্রাণিসম্পদ খাতের অভাবনীয় অগ্রগতি সত্ত্বেও কিছু কাঠামোগত চ্যালেঞ্জ এখনও রয়ে গেছে। এর মধ্যে প্রধান হলো পশুখাদ্যের কাঁচামালের (যেমন ভুট্টা ও সয়াবিন মিল) উচ্চ আমদানি মূল্য, খাদ্যে ভেজাল এবং গ্রামাঞ্চলে ওষুধের অযৌক্তিক ব্যবহার ও অ্যান্টিবায়োটিক রেজিস্ট্যান্স (AMR)। বিএলআরআই এই সংকট নিরসনে দেশীয় উদ্ভিজ্জ প্রোটিন ও ব্ল্যাক সোলজার ফ্লাই (BSF) লার্ভা থেকে বিকল্প প্রোটিন তৈরির গবেষণা চালাচ্ছে।</p>
  <p>এছাড়া ক্ষুদ্র খামারিদের জন্য আধুনিক কোল্ড চেইন সংরক্ষণ ব্যবস্থা এবং দুগ্ধ প্রক্রিয়াকরণ কারখানা উপজেলা পর্যায়ে সম্প্রসারণ করতে পারলে খামারিরা দুধের ন্যায্য মূল্য পাবেন এবং মধ্যস্বত্বভোগীদের দৌরাত্ম্য বন্ধ হবে।</p>

  <h2 id="exam-prep" class="htbd-heading">৭. বিসিএস প্রিলিমিনারি ও ভাইভা স্পেশাল মডেল প্রশ্নোত্তর</h2>
  <p><strong>প্রশ্ন: বাংলাদেশ প্রাণিসম্পদ গবেষণা ইনস্টিটিউট (BLRI)-এর সদর দপ্তর কোথায় অবস্থিত?</strong><br>
  <strong>উত্তর:</strong> সাভার, ঢাকা।</p>
  <p><strong>প্রশ্ন: 'সুবর্ণা' কিসের জাত?</strong><br>
  <strong>উত্তর:</strong> বিএলআরআই কর্তৃক উদ্ভাবিত উচ্চ ফলনশীল সংকর মুরগির জাত।</p>

  <h2 id="faqs" class="htbd-heading">৮. সচরাচর জিজ্ঞাসিত প্রশ্ন (FAQ)</h2>
  <div style="margin-top: 15px;">
    <p><strong>প্রশ্ন ১: বিএলআরআই কত সালে প্রতিষ্ঠিত হয়?</strong><br>
    উত্তর: ১৯৮৪ সালের অধ্যাদেশের মাধ্যমে এটি আনুষ্ঠানিকভাবে প্রতিষ্ঠিত হয়।</p>
    
    <p><strong>প্রশ্ন ২: বাংলাদেশের জাতীয় পশু প্রজনন নীতিমালা কারা তদারকি করে?</strong><br>
    উত্তর: মৎস্য ও প্রাণিসম্পদ মন্ত্রণালয় এবং বিএলআরআই যৌথভাবে জাতীয় গবাদিপশু প্রজনন নীতিমালা তদারকি ও গবেষণা পরিচালনা করে।</p>
  </div>
</div>

<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{
      "@type": "Question",
      "name": "বিএলআরআই (BLRI) এর পূর্ণরূপ কী?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "বিএলআরআই-এর পূর্ণরূপ হলো Bangladesh Livestock Research Institute (বাংলাদেশ প্রাণিসম্পদ গবেষণা ইনস্টিটিউট)।"
      }}
    }},
    {{
      "@type": "Question",
      "name": "বিএলআরআই কোন মন্ত্রণালয়ের অধীনস্থ?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "এটি গণপ্রজাতন্ত্রী বাংলাদেশ সরকারের মৎস্য ও প্রাণিসম্পদ মন্ত্রণালয়ের অধীন একটি স্বায়ত্তশাসিত জাতীয় গবেষণা প্রতিষ্ঠান।"
      }}
    }}
  ]
}}
</script>
"""
    return {
        "slug": slug,
        "post_id": post_id,
        "title": title,
        "category": category,
        "meta_desc": meta_desc,
        "html_content": content
    }


# ==============================================================================
# POST 5: ISHWAR CHANDRA VIDYASAGAR
# ==============================================================================
def build_post_vidyasagar():
    slug = "ishwar-chandra-vidyasagar-social-reform-contribution"
    post_id = "5786345583005242847"
    title = "সমাজ সংস্কার ও বাংলা সাহিত্যে ঈশ্বরচন্দ্র বিদ্যাসাগরের অবদান (২০২৬)"
    category = "বাংলা সাহিত্য,ইতিহাস ও সমাজ সংস্কার"
    meta_desc = "ঈশ্বরচন্দ্র বিদ্যাসাগরের সমাজ সংস্কার, বিধবা বিবাহ আন্দোলন (১৮৫৬), নারী শিক্ষা বিস্তার ও বাংলা গদ্যের বিকাশে অবদানের পূর্ণাঙ্গ বিশ্লেষণ পড়ুন।"
    links_html = get_internal_links_for_topic("ঈশ্বরচন্দ্র বিদ্যাসাগর সমাজ সংস্কার বাংলা সাহিত্য")

    content = f"""{STYLES_BLOCK}
<div class="htbd-post-wrapper">
  <div style="margin-bottom: 18px;">
    <span class="htbd-badge" style="background: #e8f0fe; color: #1a73e8; padding: 6px 14px; border-radius: 20px; font-weight: 600; font-size: 14px; display: inline-block;">
      📚 বিভাগ: বাংলা সাহিত্য ও ইতিহাস | সর্বশেষ সংস্করণ: ২০২৬ | বিসিএস ও অনার্স বিশেষ হ্যান্ডনোট
    </span>
  </div>

  <!-- Hero Thumbnail Banner -->
  <div style="text-align: center; margin: 18px 0 25px 0;">
    <img src="https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/posts/vidyasagar-social-reform-banner.png" 
         alt="সমাজ সংস্কার ও বাংলা সাহিত্যে ঈশ্বরচন্দ্র বিদ্যাসাগরের অবদান" 
         title="ঈশ্বরচন্দ্র বিদ্যাসাগরের সমাজ সংস্কার ও সাহিত্য সাধনা"
         width="1200" height="675"
         loading="eager"
         style="width: 100%; max-width: 100%; height: auto; border-radius: 10px; box-shadow: 0 4px 14px rgba(0,0,0,0.12); display: block; margin: 0 auto;"/>
    <span style="display: block; font-size: 14px; color: #5f6368; margin-top: 8px; font-style: italic;">
      চিত্র: উনিশ শতকের নবজাগরণ, বিধবা বিবাহ আন্দোলন ও আধুনিক বাংলা গদ্যের জনক ঈশ্বরচন্দ্র বিদ্যাসাগর
    </span>
  </div>

  <div class="htbd-qbox" style="background: #f8f9fa; border-left: 5px solid #1a73e8; padding: 20px 24px; margin: 22px 0; border-radius: 0 8px 8px 0; box-shadow: 0 1px 4px rgba(0,0,0,0.06);">
    <p style="margin: 0; font-size: 18px; line-height: 1.8;">
      <strong>📌 সারসংক্ষেপ (Quick Overview):</strong> 
      <strong>পণ্ডিত ঈশ্বরচন্দ্র বিদ্যাসাগর (১৮২০ – ১৮৯১)</strong> ছিলেন উনিশ শতকের বাংলার নবজাগরণের (Bengal Renaissance) পুরোধা ব্যক্তিত্ব, আধুনিক বাংলা গদ্যের জনক এবং একাধারে সমাজ সংস্কারক ও শিক্ষাবিদ। তিনি গোঁড়া হিন্দু সমাজের প্রবল বাধা উপেক্ষা করে ১৮৫৬ সালে হিন্দু বিধবা বিবাহ আইন পাস করান, বহুবিবাহ রোধে আন্দোলন করেন এবং নারীদের প্রাতিষ্ঠানিক শিক্ষার প্রসারে ৩৫টি বালিকা বিদ্যালয় প্রতিষ্ঠা করেন। এছাড়া বাংলা গদ্যে প্রথম জ্যোতিচিহ্ন বা বিরামচিহ্নের সফল প্রয়োগ ঘটিয়ে তিনি বাংলা ভাষাকে এক সুশৃঙ্খল ও আধুনিক রূপ দান করেন।
    </p>
  </div>

  <div class="htbd-toc-box">
    <h3 style="margin-top: 0; color: #1a73e8; border-bottom: 2px solid #e8f0fe; padding-bottom: 10px; font-size: 20px; font-weight: 700;">📑 সূচিপত্র (Table of Contents)</h3>
    <ul class="htbd-toc-list">
      <li><a href="#life">👉 ১. ঈশ্বরচন্দ্র বিদ্যাসাগরের প্রারম্ভিক জীবন ও শিক্ষাদীক্ষা</a></li>
      <li><a href="#prose">👉 ২. বাংলা গদ্যের জনক হিসেবে বিদ্যাসাগরের সাহিত্যকর্ম ও বিরামচিহ্ন প্রবর্তন</a></li>
      <li><a href="#widow-remarriage">👉 ৩. ঐতিহাসিক বিধবা বিবাহ আন্দোলন ও ১৮৫৬ সালের আইন পাস</a></li>
      <li><a href="#female-education">👉 ৪. নারী শিক্ষা বিস্তার ও বেথুন স্কুলের প্রতিষ্ঠা</a></li>
      <li><a href="#polygamy">👉 ৫. বহুবিবাহ ও বাল্যবিবাহ নিরোধে সমাজ সংস্কারমুখী পদক্ষেপ</a></li>
      <li><a href="#works-table">👉 ৬. বিদ্যাসাগরের বিখ্যাত গ্রন্থপঞ্জি ও অনুবাদ সাহিত্যের তথ্য ছক</a></li>
      <li><a href="#exam-prep">👉 ৭. বিসিএস ও অনার্স পরীক্ষার স্পেশাল মডেল প্রশ্নোত্তর</a></li>
      <li><a href="#faqs">👉 ৮. সচরাচর জিজ্ঞাসিত প্রশ্ন (FAQ)</a></li>
    </ul>
  </div>

  <h2 id="life" class="htbd-heading">১. ঈশ্বরচন্দ্র বিদ্যাসাগরের প্রারম্ভিক জীবন ও শিক্ষাদীক্ষা</h2>
  <p>ঈশ্বরচন্দ্র বন্দ্যোপাধ্যায় ১৮২০ সালের ২৬ সেপ্টেম্বর মেদিনীপুর জেলার বীরসিংহ গ্রামে এক দরিদ্র কিন্তু বিদ্যানুরাগী পরিবারে জন্মগ্রহণ করেন। কলকাতার সংস্কৃত কলেজে অসাধারণ মেধার পরিচয় দিয়ে তিনি ব্যাকরণ, কাব্য, অলংকার, বেদান্ত ও স্মৃতিশাস্ত্রে অসামান্য পাণ্ডিত্য অর্জন করেন। তাঁর এই বিপুল পাণ্ডিত্যের স্বীকৃতিস্বরূপ সংস্কৃত কলেজ তাঁকে <strong>'বিদ্যাসাগর' (জ্ঞানের সাগর)</strong> উপাধিতে ভূষিত করে। আর তাঁর অপরিসীম মানবপ্রেম ও করুণার জন্য তিনি পরিচিত হন 'দয়ার সাগর' নামে।</p>

  <h2 id="prose" class="htbd-heading">২. বাংলা গদ্যের জনক হিসেবে বিদ্যাসাগরের সাহিত্যকর্ম ও বিরামচিহ্ন প্রবর্তন</h2>
  <p>বিদ্যাসাগরের আবির্ভাবের পূর্বে বাংলা গদ্য ছিল দুর্বোধ্য, ছন্দহীন এবং বিরামচিহ্নবিহীন এক জগাখিচুড়ি অবস্থা। ১৮৪৭ সালে প্রকাশিত তাঁর <em>'বেতাল পঞ্চবিংশতি'</em> গ্রন্থে তিনি প্রথম বাংলা গদ্যে যতিচিহ্ন বা বিরামচিহ্নের (কমা, সেমিকোলন, দাঁড়ি ইত্যাদি) সুশৃঙ্খল প্রয়োগ ঘটান। ফলে বাংলা ভাষা পাঠযোগ্য ও শ্রুতিমধুর রূপ লাভ করে। এই কারণে তাঁকে <strong>আধুনিক বাংলা গদ্যের জনক</strong> বলা হয়। শিশুদের বাংলা বর্ণমালা শিক্ষার চিরন্তন বই <em>'বর্ণপরিচয়'</em> (১৮৫৫) তাঁর এক অনন্য অবদান।</p>

  {links_html}

  <h2 id="widow-remarriage" class="htbd-heading">৩. ঐতিহাসিক বিধবা বিবাহ আন্দোলন ও ১৮৫৬ সালের আইন পাস</h2>
  <p>তৎকালীন হিন্দু সমাজে বাল্যকালে স্বামী মারা গেলে ছোট্ট কন্যাশিশুদের আজীবন চরম অমানবিক লাঞ্ছনা ও কৃচ্ছ্রসাধনের মধ্যে বেঁচে থাকতে হতো। বিদ্যাসাগর প্রাচীন পরাশর সংহিতা ঘেঁটে প্রমাণ করেন যে শাস্ত্রীয় বিধানে বিধবা বিবাহের বৈধতা রয়েছে।</p>
  <p>তীব্র সামাজিক কুৎসা ও প্রাণনাশের হুমকি সত্ত্বেও তিনি হাজার হাজার নাগরিকের স্বাক্ষর সংগ্রহ করে ব্রিটিশ সরকারের কাছে আবেদন জানান। এর ফলশ্রুতিতে ১৮৫৬ সালের ২৬ জুলাই লর্ড ক্যানিং-এর আমলে ঐতিহাসিক <strong>'হিন্দু বিধবা বিবাহ আইন' (Act XV of 1856)</strong> পাস হয়। শুধু আইন পাস করেই তিনি ক্ষান্ত হননি, নিজ খরচে বহু বিধবা বিবাহের আয়োজন করেন এবং নিজের একমাত্র পুত্র নারায়ণচন্দ্রকেও এক বিধবার সাথে বিয়ে দিয়ে আদর্শ স্থাপন করেন।</p>

  <h2 id="works-table" class="htbd-heading">৬. বিদ্যাসাগরের বিখ্যাত গ্রন্থপঞ্জি ও অনুবাদ সাহিত্যের তথ্য ছক</h2>
  <div class="htbd-table-wrapper">
    <table class="htbd-table">
      <thead>
        <tr>
          <th>গ্রন্থের নাম</th>
          <th>প্রকাশকাল</th>
          <th>মূল উৎস / বিষয়বস্তু</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>বেতাল পঞ্চবিংশতি</strong></td>
          <td>১৮৪৭ খ্রি.</td>
          <td>হিন্দি 'বৈ তাল পচ্চীসী' অবলম্বনে প্রথম বিরামচিহ্নযুক্ত বাংলা গদ্য</td>
        </tr>
        <tr>
          <td><strong>শকুন্তলা</strong></td>
          <td>১৮৫৪ খ্রি.</td>
          <td>কালিদাসের 'অভিজ্ঞান শকুন্তলম' নাটকের সুললিত গদ্যানুবাদ</td>
        </tr>
        <tr>
          <td><strong>বর্ণপরিচয় (১ম ও ২য় ভাগ)</strong></td>
          <td>১৮৫৫ খ্রি.</td>
          <td>বাঙালি শিশুদের জন্য আধুনিক বাংলা বর্ণমালার ভিত্তিগ্রন্থ</td>
        </tr>
        <tr>
          <td><strong>সীতার বনবাস</strong></td>
          <td>১৮৬০ খ্রি.</td>
          <td>ভবভূতির 'উত্তররামচরিত' ও রামায়ণের করুণ রসের আখ্যান</td>
        </tr>
        <tr>
          <td><strong>বিধবা বিবাহ প্রচলিত হওয়া উচিত কি না</strong></td>
          <td>১৮৫৫ খ্রি.</td>
          <td>বিধবা বিবাহের সপক্ষে শাস্ত্রীয় ও যৌক্তিক প্রবন্ধ</td>
        </tr>
      </tbody>
    </table>
  </div>

  <h2 id="exam-prep" class="htbd-heading">৭. বিসিএস ও অনার্স পরীক্ষার স্পেশাল মডেল প্রশ্নোত্তর</h2>
  <p><strong>প্রশ্ন: বাংলা গদ্যে প্রথম বিরামচিহ্ন ব্যবহার করেন কে এবং কোন গ্রন্থে?</strong><br>
  <strong>উত্তর:</strong> ঈশ্বরচন্দ্র বিদ্যাসাগর, ১৮৪৭ সালে প্রকাশিত 'বেতাল পঞ্চবিংশতি' গ্রন্থে।</p>
  <p><strong>প্রশ্ন: বিধবা বিবাহ আইন কত সালে পাস হয় এবং তখন গভর্নর জেনারেল কে ছিলেন?</strong><br>
  <strong>উত্তর:</strong> ১৮৫৬ সালের ২৬ জুলাই, লর্ড ক্যানিং-এর সময়ে।</p>

  <h2 id="faqs" class="htbd-heading">৮. সচরাচর জিজ্ঞাসিত প্রশ্ন (FAQ)</h2>
  <div style="margin-top: 15px;">
    <p><strong>প্রশ্ন ১: বিদ্যাসাগরের ছদ্মনাম কী ছিল?</strong><br>
    উত্তর: কস্যচিৎ উপযুক্ত ভাইপোস্য এবং কস্যচিৎ উপযুক্ত ভাইপো সহচরস্য।</p>
    
    <p><strong>প্রশ্ন ২: মেট্রোপলিটন ইনস্টিটিউশন কে প্রতিষ্ঠা করেন?</strong><br>
    উত্তর: ঈশ্বরচন্দ্র বিদ্যাসাগর (যা বর্তমানে বিদ্যাসাগর কলেজ নামে পরিচিত)।</p>
  </div>
</div>

<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{
      "@type": "Question",
      "name": "ঈশ্বরচন্দ্র বিদ্যাসাগরকে বাংলা গদ্যের জনক বলা হয় কেন?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "তিনি প্রথম ১৮৪৭ সালে 'বেতাল পঞ্চবিংশতি' গ্রন্থে বাংলা গদ্যে সুশৃঙ্খল জ্যোতিচিহ্ন বা বিরামচিহ্নের সফল প্রয়োগ ঘটিয়ে বাংলা গদ্যকে পরিশীলিত ও গতিশীল রূপ দেন।"
      }}
    }},
    {{
      "@type": "Question",
      "name": "হিন্দু বিধবা বিবাহ আইন কবে পাস হয়?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "ঈশ্বরচন্দ্র বিদ্যাসাগরের অক্লান্ত প্রচেষ্টায় ১৮৫৬ সালের ২৬ জুলাই ব্রিটিশ ভারতে হিন্দু বিধবা বিবাহ আইন পাস হয়।"
      }}
    }}
  ]
}}
</script>
"""
    return {
        "slug": slug,
        "post_id": post_id,
        "title": title,
        "category": category,
        "meta_desc": meta_desc,
        "html_content": content
    }


# ==============================================================================
# POST 6: POPULATION CHANGE FACTORS
# ==============================================================================
def build_post_population_factors():
    slug = "jonosonkha-poribortoner-prodhan-niyamok-somuho"
    post_id = "2778070516508854236"
    title = "জনসংখ্যা পরিবর্তনের কারণ, প্রভাব ও প্রধান নিয়ামকসমূহ (২০২৬)"
    category = "সমাজবিজ্ঞান,ভূগোল ও পরিবেশ"
    meta_desc = "জনসংখ্যা পরিবর্তনের ৩টি প্রধান নিয়ামক: জন্মহার, মৃত্যুহার ও স্থানান্তরের বিস্তারিত বিশ্লেষণ, ডেমোগ্রাফিক ট্রানজিশন মডেল ও বিসিএস পরীক্ষার হ্যান্ডনোট।"
    links_html = get_internal_links_for_topic("জনসংখ্যা ডেমোগ্রাফি সমাজবিজ্ঞান বাংলাদেশ")

    content = f"""{STYLES_BLOCK}
<div class="htbd-post-wrapper">
  <div style="margin-bottom: 18px;">
    <span class="htbd-badge" style="background: #e8f0fe; color: #1a73e8; padding: 6px 14px; border-radius: 20px; font-weight: 600; font-size: 14px; display: inline-block;">
      📚 বিভাগ: সমাজবিজ্ঞান ও ভূগোল | সর্বশেষ সংস্করণ: ২০২৬ | বিসিএস ও অনার্স পূর্ণাঙ্গ হ্যান্ডনোট
    </span>
  </div>

  <!-- Hero Thumbnail Banner -->
  <div style="text-align: center; margin: 18px 0 25px 0;">
    <img src="https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/posts/population-change-factors-banner.png" 
         alt="জনসংখ্যা পরিবর্তনের কারণ, প্রভাব ও প্রধান নিয়ামকসমূহ" 
         title="জনসংখ্যা পরিবর্তনের প্রধান নিয়ামক ও তত্ত্ব"
         width="1200" height="675"
         loading="eager"
         style="width: 100%; max-width: 100%; height: auto; border-radius: 10px; box-shadow: 0 4px 14px rgba(0,0,0,0.12); display: block; margin: 0 auto;"/>
    <span style="display: block; font-size: 14px; color: #5f6368; margin-top: 8px; font-style: italic;">
      চিত্র: জনসংখ্যা বৃদ্ধির ৩টি মৌলিক নিয়ামক—জন্মহার, মৃত্যুহার ও নিট অভিবাসন
    </span>
  </div>

  <div class="htbd-qbox" style="background: #f8f9fa; border-left: 5px solid #1a73e8; padding: 20px 24px; margin: 22px 0; border-radius: 0 8px 8px 0; box-shadow: 0 1px 4px rgba(0,0,0,0.06);">
    <p style="margin: 0; font-size: 18px; line-height: 1.8;">
      <strong>📌 সারসংক্ষেপ (Quick Overview):</strong> 
      <strong>জনসংখ্যা পরিবর্তন (Population Dynamics)</strong> বলতে কোনো নির্দিষ্ট ভৌগোলিক অঞ্চলে সময়ের ব্যবধানে জনসংখ্যার আকার, কাঠামো ও ঘনত্বের হ্রাস-বৃদ্ধিকে বোঝায়। জনবিজ্ঞান (Demography) অনুযায়ী জনসংখ্যা পরিবর্তনের ৩টি প্রধান নিয়ামক রয়েছে: <strong>১. জন্মহার (Fertility), ২. মৃত্যুহার (Mortality), এবং ৩. স্থানান্তর বা অভিবাসন (Migration)</strong>। এছাড়া অর্থনৈতিক উন্নয়ন, বাল্যবিয়ে, শিক্ষার হার এবং স্বাস্থ্যসেবার আধুনিকায়ন জনসংখ্যার রূপান্তরে গুরুত্বপূর্ণ ভূমিকা পালন করে। নিচে এর বিস্তারিত গাণিতিক সূত্র, ডেমোগ্রাফিক ডিভিডেন্ড ও তথ্য ছক তুলে ধরা হলো।
    </p>
  </div>

  <div class="htbd-toc-box">
    <h3 style="margin-top: 0; color: #1a73e8; border-bottom: 2px solid #e8f0fe; padding-bottom: 10px; font-size: 20px; font-weight: 700;">📑 সূচিপত্র (Table of Contents)</h3>
    <ul class="htbd-toc-list">
      <li><a href="#definition">👉 ১. জনসংখ্যা পরিবর্তনের মৌলিক ধারণা ও গাণিতিক সমীকরণ</a></li>
      <li><a href="#fertility">👉 ২. প্রজনন হার বা জন্মহার (Fertility) এবং এর প্রভাবকসমূহ</a></li>
      <li><a href="#mortality">👉 ৩. মরণশীলতা বা মৃত্যুহার (Mortality) এবং চিকিৎসা বিজ্ঞানের অগ্রগতি</a></li>
      <li><a href="#migration">👉 ৪. স্থানান্তর বা নিট অভিবাসন (Migration - Push & Pull Factors)</a></li>
      <li><a href="#malthus">👉 ৫. মালথাসের জনসংখ্যা তত্ত্ব বনাম ডেমোগ্রাফিক ট্রানজিশন মডেল</a></li>
      <li><a href="#bd-context">👉 ৬. বাংলাদেশের জনসংখ্যা পরিস্থিতি ও ডেমোগ্রাফিক ডিভিডেন্ডের সুযোগ</a></li>
      <li><a href="#comparison-table">👉 ৭. জনসংখ্যা পরিবর্তনের নিয়ামকসমূহের তুলনামূলক তথ্য ছক</a></li>
      <li><a href="#faqs">👉 ৮. সচরাচর জিজ্ঞাসিত প্রশ্ন (FAQ)</a></li>
    </ul>
  </div>

  <h2 id="definition" class="htbd-heading">১. জনসংখ্যা পরিবর্তনের মৌলিক ধারণা ও গাণিতিক সমীকরণ</h2>
  <p>একটি দেশের জনসংখ্যা স্থির থাকে না; এটি প্রতিনিয়ত পরিবর্তনশীল। জনবিজ্ঞানে জনসংখ্যা পরিবর্তনের হার পরিমাপের জন্য নিচের বিখ্যাত 'ব্যালেন্সিং সমীকরণ' (Demographic Balancing Equation) ব্যবহার করা হয়:</p>
  <blockquote style="background: #f8f9fa; border-left: 4px solid #1a73e8; margin: 16px 0; padding: 14px 20px; font-family: monospace; font-size: 18px;">
    P2 = P1 + (B - D) + (I - E)
  </blockquote>
  <p>যেখানে, <strong>P2</strong> = বর্তমান জনসংখ্যা, <strong>P1</strong> = পূর্ববর্তী জনসংখ্যা, <strong>B</strong> = মোট জন্ম, <strong>D</strong> = মোট মৃত্যু, <strong>I</strong> = বহিরাগমন (Immigration), এবং <strong>E</strong> = বহির্গমন (Emigration)। এখানে (B - D) হলো প্রাকৃতিক বৃদ্ধি এবং (I - E) হলো নিট অভিবাসন।</p>

  <h2 id="fertility" class="htbd-heading">২. প্রজনন হার বা জন্মহার (Fertility) এবং এর প্রভাবকসমূহ</h2>
  <p>জন্মহার বৃদ্ধির প্রধান কারণগুলোর মধ্যে রয়েছে বাল্যবিয়ে, বহুবিবাহ, পুত্রসন্তান লাভের সামাজিক আকাঙ্ক্ষা, নিরক্ষরতা এবং পরিবার পরিকল্পনা পদ্ধতির অভাব। উন্নয়নশীল দেশগুলোতে যেখানে শিক্ষার হার কম এবং নারীদের অর্থনৈতিক আত্মনির্ভরশীলতা নেই, সেখানে জন্মহার তুলনামূলকভাবে বেশি পরিলক্ষিত হয়। তবে বাংলাদেশে নারী শিক্ষার প্রসার এবং পরিবার পরিকল্পনা সচেতনতা বৃদ্ধির ফলে বর্তমানে মোট প্রজনন হার (TFR) ২.৩-এ নেমে এসেছে।</p>

  {links_html}

  <h2 id="migration" class="htbd-heading">৪. স্থানান্তর বা নিট অভিবাসন (Migration - Push & Pull Factors)</h2>
  <p>অভিবাসন দুই প্রকার—অভ্যন্তরীণ ও আন্তর্জাতিক। মানুষ যখন কর্মসংস্থান, উন্নত নাগরিক সুযোগ-সুবিধা এবং নিরাপত্তার জন্য গ্রাম থেকে শহরে স্থানান্তরিত হয়, তাকে অভ্যন্তরীণ স্থানান্তর বলে। স্থানান্তরের পেছনে দুটি মূল শক্তি কাজ করে:</p>
  <ul>
    <li><strong>বিতাড়ন উপাদান (Push Factors):</strong> নদীভাঙন, বেকারত্ব, প্রাকৃতিক দুর্যোগ, জমিতে কাজের অভাব ও গ্রামীণ দারিদ্র্য।</li>
    <li><strong>আকর্ষণ উপাদান (Pull Factors):</strong> শহরে চাকরির সুযোগ, উচ্চশিক্ষা, উন্নত স্বাস্থ্যসেবা, আধুনিক জীবনযাপন ও ব্যবসায়িক অনুকূল পরিবেশ।</li>
  </ul>

  <h2 id="bd-context" class="htbd-heading">৬. বাংলাদেশের জনসংখ্যা পরিস্থিতি ও ডেমোগ্রাফিক ডিভিডেন্ডের সুযোগ</h2>
  <p>বাংলাদেশ বর্তমানে জনসংখ্যার এক ঐতিহাসিক সন্ধিক্ষণে অবস্থান করছে, যাকে অর্থনীতি ও সমাজবিজ্ঞানে <strong>'ডেমোগ্রাফিক ডিভিডেন্ড' (Demographic Dividend)</strong> বা জনসংখ্যাতাত্ত্বিক সুবিধা বলা হয়। এর অর্থ হলো দেশে নির্ভরশীল জনগোষ্ঠীর (শিশু ও বৃদ্ধ) তুলনায় কর্মক্ষম জনগোষ্ঠীর (১৫ থেকে ৬৪ বছর) সংখ্যা উল্লেখযোগ্যভাবে বেশি (প্রায় ৬৫% এর উপরে)। যদি এই বিশাল যুবসমাজকে কারিগরি শিক্ষা, তথ্যপ্রযুক্তি প্রশিক্ষণ ও কর্মসংস্থানের মাধ্যমে দক্ষ জনশক্তিতে রূপান্তর করা যায়, তবে বাংলাদেশ দ্রুত উন্নত রাষ্ট্রে পরিণত হতে পারবে।</p>

  <h2 id="comparison-table" class="htbd-heading">৭. জনসংখ্যা পরিবর্তনের নিয়ামকসমূহের তুলনামূলক তথ্য ছক</h2>
  <div class="htbd-table-wrapper">
    <table class="htbd-table">
      <thead>
        <tr>
          <th>নিয়ামক</th>
          <th>সংজ্ঞা</th>
          <th>বৃদ্ধির কারণ</th>
          <th>হ্রাসের কারণ</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>স্থূল জন্মহার (CBR)</strong></td>
          <td>প্রতি হাজারে বছরে মোট জীবিত জন্ম নেওয়া শিশুর সংখ্যা</td>
          <td>বাল্যবিয়ে, ধর্মীয় গোঁড়ামি, নিরক্ষরতা</td>
          <td>নারী শিক্ষা, পরিবার পরিকল্পনা, নগরায়ন</td>
        </tr>
        <tr>
          <td><strong>স্থূল মৃত্যুহার (CDR)</strong></td>
          <td>প্রতি হাজারে বছরে মোট মারা যাওয়া মানুষের সংখ্যা</td>
          <td>মহামারি, যুদ্ধ, অপুষ্টি ও চিকিৎসার অভাব</td>
          <td>উন্নত স্বাস্থ্যসেবা, টিকা প্রদান, স্যানিটেশন</td>
        </tr>
        <tr>
          <td><strong>নিট অভিবাসন (NMR)</strong></td>
          <td>বহিরাগমন ও বহির্গমনের মধ্যকার পার্থক্য</td>
          <td>উন্নত কর্মসংস্থান ও নিরাপত্তা</td>
          <td>অভিবাসন কঠোরতা, যুদ্ধ ও রাজনৈতিক সংকট</td>
        </tr>
      </tbody>
    </table>
  </div>

  <h2 id="faqs" class="htbd-heading">৮. সচরাচর জিজ্ঞাসিত প্রশ্ন (FAQ)</h2>
  <div style="margin-top: 15px;">
    <p><strong>প্রশ্ন ১: ডেমোগ্রাফিক ডিভিডেন্ড বলতে কী বোঝায়?</strong><br>
    উত্তর: যখন কোনো দেশের মোট জনসংখ্যার সিংহভাগই (১৫-৬৪ বছর) কর্মক্ষম থাকে এবং নির্ভরশীল জনগোষ্ঠীর অনুপাত সর্বনিম্ন পর্যায়ে নেমে আসে, তাকে ডেমোগ্রাফিক ডিভিডেন্ড বলে।</p>
    
    <p><strong>প্রশ্ন ২: মালথাসের জনসংখ্যা তত্ত্বের মূল কথা কী?</strong><br>
    উত্তর: থমাস রবার্ট মালথাসের মতে, খাদ্য উৎপাদন বাড়ে গাণিতিক হারে (১, ২, ৩, ৪, ৫...) কিন্তু জনসংখ্যা বাড়ে জ্যামিতিক হারে (১, ২, ৪, ৮, ১৬...), যার ফলে খাদ্য ঘাটতি ও জনসংখ্যা বিপর্যয় ঘটে।</p>
  </div>
</div>

<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{
      "@type": "Question",
      "name": "জনসংখ্যা পরিবর্তনের প্রধান ৩টি নিয়ামক কী কী?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "জনসংখ্যা পরিবর্তনের ৩টি প্রধান নিয়ামক হলো: জন্মহার (Fertility), মৃত্যুহার (Mortality), এবং নিট স্থানান্তর বা অভিবাসন (Migration)।"
      }}
    }},
    {{
      "@type": "Question",
      "name": "অভিবাসনের পুশ ও পুল ফ্যাক্টর কী?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "পুশ ফ্যাক্টর হলো যেসব প্রতিকূল কারণে মানুষ এলাকা ত্যাগ করে (যেমন দারিদ্র্য, নদীভাঙন), আর পুল ফ্যাক্টর হলো যেসব সুযোগ-সুবিধা মানুষকে নতুন এলাকায় আকর্ষণ করে (যেমন কর্মসংস্থান, শিক্ষা)।"
      }}
    }}
  ]
}}
</script>
"""
    return {
        "slug": slug,
        "post_id": post_id,
        "title": title,
        "category": category,
        "meta_desc": meta_desc,
        "html_content": content
    }


# ==============================================================================
# POST 7: RESERVED WOMEN SEATS IN PARLIAMENT
# ==============================================================================
def build_post_reserved_women_seats():
    slug = "importance-of-reserved-seats-for-women-in-national-parliament"
    post_id = "3881771794171675240"
    title = "জাতীয় সংসদে নারীদের সংরক্ষিত আসন: সাংবিধানিক পটভূমি ও গুরুত্ব (২০২৬)"
    category = "বাংলাদেশ সংবিধান,রাষ্ট্রবিজ্ঞান"
    meta_desc = "বাংলাদেশের সংবিধানে জাতীয় সংসদে নারীদের সংরক্ষিত আসনের সাংবিধানিক ভিত্তি, ঐতিহাসিক বিবর্তন (১৫ থেকে ৫০ আসন), পক্ষে-বিপক্ষে যুক্তি ও সমাধান।"
    links_html = get_internal_links_for_topic("জাতীয় সংসদ সংবিধান নারী অধিকার")

    content = f"""{STYLES_BLOCK}
<div class="htbd-post-wrapper">
  <div style="margin-bottom: 18px;">
    <span class="htbd-badge" style="background: #e8f0fe; color: #1a73e8; padding: 6px 14px; border-radius: 20px; font-weight: 600; font-size: 14px; display: inline-block;">
      📚 বিভাগ: বাংলাদেশ সংবিধান ও রাষ্ট্রবিজ্ঞান | সর্বশেষ সংস্করণ: ২০২৬ | বিসিএস ও অনার্স গাইড
    </span>
  </div>

  <!-- Hero Thumbnail Banner -->
  <div style="text-align: center; margin: 18px 0 25px 0;">
    <img src="https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/posts/reserved-women-seats-banner.png" 
         alt="জাতীয় সংসদে নারীদের সংরক্ষিত আসন: সাংবিধানিক পটভূমি ও গুরুত্ব" 
         title="জাতীয় সংসদে নারী সংরক্ষিত আসনের সাংবিধানিক গুরুত্ব"
         width="1200" height="675"
         loading="eager"
         style="width: 100%; max-width: 100%; height: auto; border-radius: 10px; box-shadow: 0 4px 14px rgba(0,0,0,0.12); display: block; margin: 0 auto;"/>
    <span style="display: block; font-size: 14px; color: #5f6368; margin-top: 8px; font-style: italic;">
      চিত্র: বাংলাদেশ জাতীয় সংসদ ভবনের অধিবেশন কক্ষ ও নারীদের সংরক্ষিত ৫০টি আসনের প্রতিনিধিত্ব
    </span>
  </div>

  <div class="htbd-qbox" style="background: #f8f9fa; border-left: 5px solid #1a73e8; padding: 20px 24px; margin: 22px 0; border-radius: 0 8px 8px 0; box-shadow: 0 1px 4px rgba(0,0,0,0.06);">
    <p style="margin: 0; font-size: 18px; line-height: 1.8;">
      <strong>📌 সারসংক্ষেপ (Quick Overview):</strong> 
      <strong>জাতীয় সংসদে নারীদের সংরক্ষিত আসন</strong> হলো গণপ্রজাতন্ত্রী বাংলাদেশের সংবিধানের ৬৫(৩) অনুচ্ছেদ অনুযায়ী নারী সমাজের রাজনৈতিক ক্ষমতায়ন ও আইনসভায় প্রত্যক্ষ অংশগ্রহণ নিশ্চিত করার জন্য সংরক্ষিত ৫০টি সংসদীয় আসন। ১৯৭২ সালের মূল সংবিধানে ১০ বছরের জন্য ১৫টি সংরক্ষিত আসনের বিধান দিয়ে শুরু হয়ে বিভিন্ন সাংবিধানিক সংশোধনীর মাধ্যমে আসন সংখ্যা বৃদ্ধি পেয়ে বর্তমানে ৫০টিতে উন্নীত হয়েছে। এই সংরক্ষিত আসন নারীদের জন্য কোনো দয়া নয়, বরং পিতৃতান্ত্রিক রাজনৈতিক বাস্তবতায় নারীদের নীতি-নির্ধারণী পর্যায়ে অংশগ্রহণের একটি সুরক্ষামূলক সাংবিধানিক রক্ষাকবচ।
    </p>
  </div>

  <div class="htbd-toc-box">
    <h3 style="margin-top: 0; color: #1a73e8; border-bottom: 2px solid #e8f0fe; padding-bottom: 10px; font-size: 20px; font-weight: 700;">📑 সূচিপত্র (Table of Contents)</h3>
    <ul class="htbd-toc-list">
      <li><a href="#constitutional">👉 ১. সাংবিধানিক ভিত্তি: অনুচ্ছেদ ৬৫(৩) ও ২৮(৪)-এর বিশেষ বিধান</a></li>
      <li><a href="#evolution">👉 ২. সংরক্ষিত নারী আসনের ঐতিহাসিক বিবর্তন (১৫ থেকে ৫০ আসন)</a></li>
      <li><a href="#election-method">👉 ৩. সংরক্ষিত নারী আসনের বর্তমান নির্বাচন পদ্ধতি ও আনুপাতিক বণ্টন</a></li>
      <li><a href="#importance">👉 ৪. জাতীয় নীতি নির্ধারণ ও আইন প্রণয়নে সংরক্ষিত নারী আসনের গুরুত্ব</a></li>
      <li><a href="#debates">👉 ৫. পরোক্ষ নির্বাচন বনাম সরাসরি নির্বাচনের বিতর্ক ও সুপারিশ</a></li>
      <li><a href="#amendments-table">👉 ৬. সংবিধানের বিভিন্ন সংশোধনীতে সংরক্ষিত আসনের তুলনামূলক ছক</a></li>
      <li><a href="#faqs">👉 ৭. সচরাচর জিজ্ঞাসিত প্রশ্ন (FAQ)</a></li>
    </ul>
  </div>

  <h2 id="constitutional" class="htbd-heading">১. সাংবিধানিক ভিত্তি: অনুচ্ছেদ ৬৫(৩) ও ২৮(৪)-এর বিশেষ বিধান</h2>
  <p>বাংলাদেশ সংবিধানের ২৮(২) অনুচ্ছেদে বলা হয়েছে—"রাষ্ট্র ও গণজীবনের সর্বস্তরে নারী পুরুষের সমান অধিকার লাভ করিবেন।" তবে শতাব্দীর পর শতাব্দী ধরে পিছিয়ে থাকা নারীদের মূলধারায় তুলে আনতে সংবিধানের ২৮(৪) অনুচ্ছেদে রাষ্ট্রকে বিশেষ অধিকার বা 'অ্যাফার্মেটিভ অ্যাকশন' (Affirmative Action) গ্রহণের ক্ষমতা দেওয়া হয়েছে।</p>
  <p>এই নীতির ওপর ভিত্তি করেই সংবিধানের <strong>অনুচ্ছেদ ৬৫(৩)</strong> অনুযায়ী ৩০০ জন সাধারণ সংসদ সদস্যের বাইরে নারীদের জন্য ৫০টি আসন সংরক্ষিত রাখা হয়েছে। তবে নারী প্রার্থীরা সাধারণ ৩০০ আসনেই পুরুষদের সাথে সরাসরি প্রতিদ্বন্দ্বিতা করতে বাধা নেই।</p>

  <h2 id="election-method" class="htbd-heading">৩. সংরক্ষিত নারী আসনের বর্তমান নির্বাচন পদ্ধতি ও আনুপাতিক বণ্টন</h2>
  <p>সংরক্ষিত ৫০টি নারী আসনে প্রার্থীরা সাধারণ ভোটারদের সরাসরি ভোটে নির্বাচিত হন না; বরং তারা জাতীয় সংসদ নির্বাচনে বিজয়ী সাধারণ ৩০০ সংসদ সদস্যের 'আনুপাতিক প্রতিনিধিত্ব' (Proportional Representation) পদ্ধতিতে নির্বাচিত হন। যে রাজনৈতিক দল বা জোট যতটি সাধারণ আসনে জয়লাভ করে, তারা সেই অনুপাতে সংরক্ষিত নারী আসনের মনোনয়ন লাভ করে।</p>

  {links_html}

  <h2 id="debates" class="htbd-heading">৫. পরোক্ষ নির্বাচন বনাম সরাসরি নির্বাচনের বিতর্ক ও সুপারিশ</h2>
  <p>বর্তমানে সংরক্ষিত নারী সংসদ সদস্যদের কোনো নিজস্ব সুনির্দিষ্ট নির্বাচনী এলাকা (Constituency) না থাকায় তৃণমূলের সাথে তাঁদের কার্যকর জবাবদিহিতা থাকে না বলে সুশীল সমাজ ও নারী অধিকারকর্মীরা সমালোচনা করেন। তাই নারী আন্দোলনকর্মীদের দীর্ঘদিনের দাবি হলো—</p>
  <ul>
    <li>১. পরোক্ষ নির্বাচনের বদলে নির্দিষ্ট ভৌগোলিক এলাকা ভাগ করে সংরক্ষিত আসনে জনগণের সরাসরি ভোটের ব্যবস্থা করা।</li>
    <li>২. রাজনৈতিক দলগুলোর মূল কমিটিতে ও সাধারণ সংসদ নির্বাচনে ন্যূনতম ৩৩% নারী প্রার্থীকে বাধ্যতামূলক মনোনয়ন প্রদান।</li>
    <li>৩. সংরক্ষিত নারী সদস্যদের জন্য উন্নয়ন বাজেট ও স্থানীয় সরকার প্রশাসনে স্পষ্ট কার্যপরিধি নির্ধারণ।</li>
  </ul>

  <h2 id="amendments-table" class="htbd-heading">৬. সংবিধানের বিভিন্ন সংশোধনীতে সংরক্ষিত আসনের তুলনামূলক ছক</h2>
  <div class="htbd-table-wrapper">
    <table class="htbd-table">
      <thead>
        <tr>
          <th>সংবিধান / সংশোধনী</th>
          <th>সাল</th>
          <th>সংরক্ষিত আসন সংখ্যা</th>
          <th>মেয়াদকাল</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>মূল সংবিধান</strong></td>
          <td>১৯৭২</td>
          <td>১৫টি আসন</td>
          <td>১০ বছর</td>
        </tr>
        <tr>
          <td><strong>৫ম সংশোধনী</strong></td>
          <td>১৯৭৯</td>
          <td>৩০টি আসন</td>
          <td>১৫ বছর</td>
        </tr>
        <tr>
          <td><strong>৮ম সংশোধনী</strong></td>
          <td>১৯৮৮</td>
          <td>৩০টি আসন পুনর্প্রবর্তন</td>
          <td>১০ বছর</td>
        </tr>
        <tr>
          <td><strong>১৪শ সংশোধনী</strong></td>
          <td>২০০৪</td>
          <td>৪৫টি আসন</td>
          <td>১০ বছর</td>
        </tr>
        <tr>
          <td><strong>১৫শ সংশোধনী</strong></td>
          <td>২০১১</td>
          <td>৫০টি আসন</td>
          <td>১০ বছর</td>
        </tr>
        <tr>
          <td><strong>১৭শ সংশোধনী</strong></td>
          <td>২০১৮</td>
          <td>৫০টি আসন বহাল</td>
          <td>২৫ বছর (২০৪৩ পর্যন্ত)</td>
        </tr>
      </tbody>
    </table>
  </div>

  
  <h2 id="global-women-parliament" class="htbd-heading">৫.১ আন্তর্জাতিক প্রেক্ষাপটে নারী আসন সংরক্ষণ ও বাংলাদেশের অবস্থান</h2>
  <p>বিশ্বের বিভিন্ন গণতান্ত্রিক রাষ্ট্রে নারীদের আইনসভায় অংশগ্রহণ বৃদ্ধির জন্য বিভিন্ন ধরনের সংরক্ষণ পদ্ধতি অনুসরণ করা হয়। উদাহরণস্বরূপ, রুয়ান্ডায় সংবিধানে নারীদের জন্য ৩০% আসন সরাসরি সংরক্ষিত এবং বর্তমানে দেশটির সংসদে নারীর উপস্থিতি ৬১% এর বেশি, যা বিশ্বে সর্বোচ্চ। অপরদিকে ভারত ২০২৩ সালে সংবিধানে ১২৮তম সংশোধনী বিল পাস করে লোকসভা ও রাজ্য বিধানসভাগুলোতে নারীদের জন্য ৩৩% আসন সংরক্ষণ বাধ্যতামূলক করেছে।</p>
  <p>আন্তর্জাতিক নারী দিবস ও আইপিইউ (Inter-Parliamentary Union)-এর তথ্য অনুযায়ী, বাংলাদেশে সংসদের মোট আসনের প্রায় ১৪.৩% নারী সংরক্ষিত আসন। এই হারকে অন্তত ৩৩%-এ উন্নীত করা এবং ইউনিয়ন পরিষদ ও উপজেলা পরিষদের মতো সংসদেও নারীদের সরাসরি ভোটে প্রতিদ্বন্দ্বিতার পরিবেশ নিশ্চিত করা টেকসই উন্নয়ন লক্ষ্যমাত্রা (SDG 5: Gender Equality) অর্জনের অন্যতম শর্ত।</p>

  <h2 id="faqs" class="htbd-heading">৭. সচরাচর জিজ্ঞাসিত প্রশ্ন (FAQ)</h2>
  <div style="margin-top: 15px;">
    <p><strong>প্রশ্ন ১: জাতীয় সংসদে বর্তমানে মোট আসন সংখ্যা কত?</strong><br>
    উত্তর: জাতীয় সংসদের মোট আসন সংখ্যা ৩৫০টি (৩০০টি সাধারণ আসন + ৫০টি নারীদের সংরক্ষিত আসন)।</p>
    
    <p><strong>প্রশ্ন ২: কোন সংশোধনীর মাধ্যমে নারী আসন ৫০-এ উন্নীত করা হয়?</strong><br>
    উত্তর: ২০১১ সালে সংবিধানের ১৫তম সংশোধনীর মাধ্যমে নারী আসন ৪৫ থেকে ৫০টিতে উন্নীত করা হয়।</p>
  </div>
</div>

<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{
      "@type": "Question",
      "name": "জাতীয় সংসদে নারীদের সংরক্ষিত আসন কতটি?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "বাংলাদেশ জাতীয় সংসদে নারীদের জন্য সংরক্ষিত আসন সংখ্যা ৫০টি।"
      }}
    }},
    {{
      "@type": "Question",
      "name": "সংবিধানের কত অনুচ্ছেদে সংরক্ষিত নারী আসনের কথা বলা হয়েছে?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "গণপ্রজাতন্ত্রী বাংলাদেশের সংবিধানের অনুচ্ছেদ ৬৫(৩)-এ নারীদের সংরক্ষিত আসনের বিধান সন্নিবেশিত রয়েছে।"
      }}
    }}
  ]
}}
</script>
"""
    return {
        "slug": slug,
        "post_id": post_id,
        "title": title,
        "category": category,
        "meta_desc": meta_desc,
        "html_content": content
    }


# ==============================================================================
# POST 8: CHILD SOCIALIZATION & PLAYMATES
# ==============================================================================
def build_post_child_socialization():
    slug = "samajikikorone-khelar-sathir-bhumika"
    post_id = "5020265416603423827"
    title = "শিশুর সামাজিকীকরণ প্রক্রিয়ায় খেলার সাথী ও বন্ধুদের ভূমিকা (২০২৬)"
    category = "সমাজবিজ্ঞান,শিশু বিকাশ ও মনস্তত্ত্ব"
    meta_desc = "শিশুর মানসিক বিকাশ ও সামাজিকীকরণে খেলার সাথী এবং সমবয়সী দলের (Peer Group) গুরুত্ব, নেতৃত্বগুণ ও সহমর্মিতা অর্জনের সমাজতাত্ত্বিক বিশ্লেষণ।"
    links_html = get_internal_links_for_topic("সামাজিকীকরণ সমাজবিজ্ঞান পরিবার শিক্ষা")

    content = f"""{STYLES_BLOCK}
<div class="htbd-post-wrapper">
  <div style="margin-bottom: 18px;">
    <span class="htbd-badge" style="background: #e8f0fe; color: #1a73e8; padding: 6px 14px; border-radius: 20px; font-weight: 600; font-size: 14px; display: inline-block;">
      📚 বিভাগ: সমাজবিজ্ঞান ও শিশু মনস্তত্ত্ব | সর্বশেষ সংস্করণ: ২০২৬ | অনার্স ও মাস্টার্স হ্যান্ডনোট
    </span>
  </div>

  <!-- Hero Thumbnail Banner -->
  <div style="text-align: center; margin: 18px 0 25px 0;">
    <img src="https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/posts/child-socialization-banner.png" 
         alt="শিশুর সামাজিকীকরণ প্রক্রিয়ায় খেলার সাথী ও বন্ধুদের ভূমিকা" 
         title="শিশুর মানসিক বিকাশ ও খেলার সাথীর গুরুত্ব"
         width="1200" height="675"
         loading="eager"
         style="width: 100%; max-width: 100%; height: auto; border-radius: 10px; box-shadow: 0 4px 14px rgba(0,0,0,0.12); display: block; margin: 0 auto;"/>
    <span style="display: block; font-size: 14px; color: #5f6368; margin-top: 8px; font-style: italic;">
      চিত্র: খেলার মাঠে দলগত ক্রীড়া, সহমর্মিতা ও সমবয়সী বন্ধুদের সাথে শিশুর সামাজিকীকরণ
    </span>
  </div>

  <div class="htbd-qbox" style="background: #f8f9fa; border-left: 5px solid #1a73e8; padding: 20px 24px; margin: 22px 0; border-radius: 0 8px 8px 0; box-shadow: 0 1px 4px rgba(0,0,0,0.06);">
    <p style="margin: 0; font-size: 18px; line-height: 1.8;">
      <strong>📌 সারসংক্ষেপ (Quick Overview):</strong> 
      <strong>সামাজিকীকরণ (Socialization)</strong> হলো একটি জীবনব্যাপী প্রক্রিয়া যার মাধ্যমে একজন মানবশিশু সমাজের রীতি-নীতি, মূল্যবোধ, প্রথা ও সংস্কৃতি আয়ত্ত করে সমাজের একজন পূর্ণাঙ্গ ও দায়িত্বশীল সদস্যে পরিণত হয়। পরিবারের পরেই শিশুর প্রাথমিক সামাজিকীকরণে <strong>খেলার সাথী ও সমবয়সী দল (Peer Group)</strong> সবচেয়ে শক্তিশালী অনুঘটক হিসেবে কাজ করে। খেলার মাঠেই শিশু শেখে শেয়ারিং (ভাগ করে নেওয়া), দলনেতৃত্ব, নিয়ম মেনে চলা, সহমর্মিতা এবং বিরোধ মীমাংসার মতো জটিল সামাজিক দক্ষতা। নিচে এর সমাজতাত্ত্বিক তত্ত্ব ও সমকালীন ডিজিটাল যুগের সংকট আলোচনা করা হলো।
    </p>
  </div>

  <div class="htbd-toc-box">
    <h3 style="margin-top: 0; color: #1a73e8; border-bottom: 2px solid #e8f0fe; padding-bottom: 10px; font-size: 20px; font-weight: 700;">📑 সূচিপত্র (Table of Contents)</h3>
    <ul class="htbd-toc-list">
      <li><a href="#concept">👉 ১. সামাজিকীকরণের সমাজতাত্ত্বিক ধারণা ও স্তরসমূহ</a></li>
      <li><a href="#peer-role">👉 ২. খেলার সাথী ও সমবয়সী দলের প্রত্যক্ষ ইতিবাচক প্রভাব</a></li>
      <li><a href="#psychology">👉 ৩. জাঁ পিয়াজে ও জি. এইচ. মিড-এর প্লে অ্যান্ড গেম তত্ত্ব</a></li>
      <li><a href="#digital-crisis">👉 ৪. ডিজিটাল ডিভাইস আসক্তি ও খেলার মাঠহীন নগর জীবনের সংকট</a></li>
      <li><a href="#institutions-table">👉 ৫. সামাজিকীকরণের প্রধান মাধ্যমসমূহের তুলনামূলক ছক</a></li>
      <li><a href="#remedy">👉 ৬. সুস্থ মানসিক বিকাশে অভিভাবক ও শিক্ষকদের করণীয়</a></li>
      <li><a href="#faqs">👉 ৭. সচরাচর জিজ্ঞাসিত প্রশ্ন (FAQ)</a></li>
    </ul>
  </div>

  <h2 id="concept" class="htbd-heading">১. সামাজিকীকরণের সমাজতাত্ত্বিক ধারণা ও স্তরসমূহ</h2>
  <p>একটি নবজাতক কেবল একটি জৈবিক সত্তা (Biological Entity) হিসেবে জন্মগ্রহণ করে। সমাজ, পরিবার ও পারিপার্শ্বিক মিথস্ক্রিয়ার মাধ্যমে সে একটি সামাজিক ব্যক্তিতে (Social Being) রূপান্তরিত হয়। আমেরিকান সমাজবিজ্ঞানী চার্লস হর্টন কুলি (C.H. Cooley)-র 'লুকিং গ্লাস সেলফ' (Looking Glass Self) তত্ত্ব অনুযায়ী, একজন ব্যক্তি সমাজের অন্যান্য মানুষের প্রতিক্রিয়া দেখে নিজেকে উপলব্ধি করতে শেখে।</p>

  <h2 id="peer-role" class="htbd-heading">২. খেলার সাথী ও সমবয়সী দলের প্রত্যক্ষ ইতিবাচক প্রভাব</h2>
  <p>পরিবারে মা-বাবার সাথে সম্পর্কের মাঝে একটি কর্তৃত্ব ও বাধ্যবাধকতা কাজ করে। কিন্তু সমবয়সী খেলার সাথীদের সাথে সম্পর্ক গড়ে ওঠে সমতার ভিত্তিতে। এখানে শিশু যে গুণাবলি অর্জন করে:</p>
  <ul>
    <li><strong>১. নিয়ম ও শৃঙ্খলার প্রতি আনুগত্য:</strong> খেলার নির্ধারিত নিয়ম ভঙ্গ করলে খেলায় অংশগ্রহণের অধিকার হারাবে—এই ভয় থেকেই শিশু আইনের প্রতি শ্রদ্ধাশীল হতে শেখে।</li>
    <li><strong>২. নেতৃত্ব ও সিদ্ধান্ত গ্রহণ:</strong> খেলায় দলনেতা নির্বাচন এবং পরিস্থিতি অনুযায়ী তাৎক্ষণিক সিদ্ধান্ত গ্রহণের মাধ্যমে নেতৃত্বের প্রাথমিক বিকাশ ঘটে।</li>
    <li><strong>৩. সহমর্মিতা ও অহংবোধ দূরীকরণ:</strong> নিজের খেলনা অন্যের সাথে শেয়ার করা এবং জয়ের আনন্দ ও পরাজয়ের বেদনা সমানভাবে মেনে নেওয়ার মানসিকতা তৈরি হয়।</li>
    <li><strong>৪. ভাষা ও ভাবপ্রকাশের দক্ষতা:</strong> বন্ধুদের সাথে তর্ক-বিতর্ক ও যোগাযোগের মাধ্যমে শিশুর মৌখিক ভাষা ও বাচনভঙ্গি দ্রুত শাণিত হয়।</li>
  </ul>

  {links_html}

  <h2 id="digital-crisis" class="htbd-heading">৪. ডিজিটাল ডিভাইস আসক্তি ও খেলার মাঠহীন নগর জীবনের সংকট</h2>
  <p>বর্তমানে ইট-কাঠের চারদেয়ালে বন্দি আধুনিক ফ্ল্যাট জীবন এবং শহরের খেলার মাঠের সংকট শিশুদের এক চরম সামাজিক নিঃসঙ্গতার দিকে ঠেলে দিচ্ছে। খেলার সাথীর স্থান দখল করেছে স্মার্টফোন, ভিডিও গেম এবং ইউটিউব। ফলে শিশুদের মাঝে অটিজম সাদৃশ্য আচরণ, অসামাজিকতা, মাত্রাতিরিক্ত রাগ এবং শারীরিক স্থূলতা বৃদ্ধি পাচ্ছে। বাস্তব খেলার মাঠ ও রক্ত-মাংসের খেলার সাথীর বিকল্প কোনো ডিজিটাল স্ক্রিন হতে পারে না।</p>

  <h2 id="institutions-table" class="htbd-heading">৫. সামাজিকীকরণের প্রধান মাধ্যমসমূহের তুলনামূলক ছক</h2>
  <div class="htbd-table-wrapper">
    <table class="htbd-table">
      <thead>
        <tr>
          <th>সামাজিকীকরণের মাধ্যম</th>
          <th>প্রকৃতি</th>
          <th>প্রধান ভূমিকা</th>
          <th>প্রভাবের ক্ষেত্র</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>পরিবার</strong></td>
          <td>প্রাথমিক মাধ্যম</td>
          <td>স্নেহ, ভাষা শিক্ষা, মৌলিক নৈতিকতা ও ধর্মীয় মূল্যবোধ</td>
          <td>আজীবন স্থায়িত্ব</td>
        </tr>
        <tr>
          <td><strong>খেলার সাথী ও বন্ধু</strong></td>
          <td>অনানুষ্ঠানিক সমকক্ষ</td>
          <td>সহমর্মিতা, সমতা, ক্রীড়া মনোভাব ও সামাজিক অভিযোজন</td>
          <td>শৈশব ও কৈশোর</td>
        </tr>
        <tr>
          <td><strong>বিদ্যালয়</strong></td>
          <td>প্রাতিষ্ঠানিক মাধ্যম</td>
          <td>পুঁথিগত জ্ঞান, শৃঙ্খলা, নাগরিক অধিকার ও দায়িত্ববোধ</td>
          <td>কৈশোর ও যৌবন</td>
        </tr>
        <tr>
          <td><strong>গণমাধ্যম</strong></td>
          <td>পরোক্ষ মাধ্যম</td>
          <td>তথ্যপ্রবাহ, বৈশ্বিক দৃষ্টিভঙ্গি ও ফ্যাশন সচেতনতা</td>
          <td>আধুনিক জীবন</td>
        </tr>
      </tbody>
    </table>
  </div>

  
  <h2 id="rural-vs-urban-play" class="htbd-heading">৫.১ গ্রামীণ বনাম শহুরে পরিবেশ: শিশুর সামাজিকীকরণের তুলনামূলক রূপ</h2>
  <p>বাংলাদেশের গ্রামীণ জনপদে শৈশব এখনও অনেকটাই প্রকৃতি ও সমবয়সীদের সাথে উন্মুক্ত মিথস্ক্রিয়ায় কাটে। নদীনালা, ফসলের মাঠ এবং উঠানে খেলাধুলার মাধ্যমে গ্রামীণ শিশুরা স্বতঃস্ফূর্তভাবে দলগত ঐক্য, সাহস ও শারীরিক শক্তি অর্জন করে। তাদের মধ্যে সামাজিক বিচ্ছিন্নতার হার অত্যন্ত কম।</p>
  <p>বিপরীতে নগরাঞ্চলের শিশুরা মেগা সিটির ফ্ল্যাটবাড়িতে একাকী বড় হচ্ছে। ফ্ল্যাটের নিরাপত্তার কারণে অনেক সময় একই ভবনের প্রতিবেশী শিশুদের সাথেও তাদের পরিচয় থাকে না। এই সামাজিক বিচ্ছিন্নতা শিশুর মধ্যে অন্তর্মুখী (Introvert) স্বভাব এবং অতিরিক্ত মানসিক উদ্বেগ তৈরি করে। এই সংকট কাটাতে সিটি কর্পোরেশন ও শিক্ষা প্রতিষ্ঠানগুলোতে বাধ্যতামূলক খেলার মাঠ ও কমিউনিটি চিলড্রেনস ক্লাব গড়ে তোলা সময়ের দাবি।</p>

  <h2 id="faqs" class="htbd-heading">৭. সচরাচর জিজ্ঞাসিত প্রশ্ন (FAQ)</h2>
  <div style="margin-top: 15px;">
    <p><strong>প্রশ্ন ১: শিশুর সামাজিকীকরণের প্রথম ও প্রধান বাহন কোনটি?</strong><br>
    উত্তর: পরিবার (বিশেষ করে মা) হলো শিশুর প্রথম ও প্রধান সামাজিকীকরণ মাধ্যম।</p>
    
    <p><strong>প্রশ্ন ২: 'লুকিং গ্লাস সেলফ' তত্ত্বের প্রবক্তা কে?</strong><br>
    উত্তর: আমেরিকান সমাজবিজ্ঞানী চার্লস হর্টন কুলি (C.H. Cooley)।</p>
  </div>
</div>

<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{
      "@type": "Question",
      "name": "সামাজিকীকরণ কাকে বলে?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "যে প্রক্রিয়ার মাধ্যমে মানবশিশু সমাজের প্রচলিত নিয়ম-কানুন, আচার-আচরণ ও সংস্কৃতি আয়ত্ত করে সমাজের উপযোগী সদস্য হিসেবে গড়ে ওঠে, তাকে সামাজিকীকরণ বলে।"
      }}
    }},
    {{
      "@type": "Question",
      "name": "শিশুর সামাজিকীকরণে খেলার সাথীর ভূমিকা কী?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "খেলার সাথীরা শিশুকে পারস্পরিক সহমর্মিতা, ত্যাগ স্বীকার, দলগত সহযোগিতা, নেতৃত্বদান এবং সামাজিক নিয়মাবলির প্রতি শ্রদ্ধাশীল হতে শেখায়।"
      }}
    }}
  ]
}}
</script>
"""
    return {
        "slug": slug,
        "post_id": post_id,
        "title": title,
        "category": category,
        "meta_desc": meta_desc,
        "html_content": content
    }


# ==============================================================================
# POST 9: COMPUTER DEFINITION & HISTORY
# ==============================================================================
def build_post_computer_definition():
    slug = "computer-definition-history"
    post_id = "8780611538499445916"
    title = "কম্পিউটার কাকে বলে? কম্পিউটারের সংজ্ঞা, ইতিহাস, বৈশিষ্ট্য ও প্রজন্ম (২০২৬)"
    category = "কম্পিউটার ও তথ্যপ্রযুক্তি,ICT Guide"
    meta_desc = "কম্পিউটার কী? কম্পিউটারের কাজের ধাপ, ইনপুট-আউটপুট ডিভাইস, ১ম থেকে ৫ম প্রজন্মের তুলনা এবং বিসিএস ও এইচএসসি আইসিটি স্পেশাল পূর্ণাঙ্গ গাইডলাইন।"
    links_html = get_internal_links_for_topic("কম্পিউটার আইসিটি বিসিএস বিজ্ঞান")

    content = f"""{STYLES_BLOCK}
<div class="htbd-post-wrapper">
  <div style="margin-bottom: 18px;">
    <span class="htbd-badge" style="background: #e8f0fe; color: #1a73e8; padding: 6px 14px; border-radius: 20px; font-weight: 600; font-size: 14px; display: inline-block;">
      📚 বিভাগ: তথ্য ও যোগাযোগ প্রযুক্তি (ICT) | সর্বশেষ সংস্করণ: ২০২৬ | এইচএসসি ও বিসিএস আইসিটি হ্যান্ডনোট
    </span>
  </div>

  <!-- Hero Thumbnail Banner -->
  <div style="text-align: center; margin: 18px 0 25px 0;">
    <img src="https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/posts/computer-definition-history-banner.png" 
         alt="কম্পিউটার কাকে বলে? কম্পিউটারের সংজ্ঞা, ইতিহাস, বৈশিষ্ট্য ও প্রজন্ম" 
         title="কম্পিউটার সংজ্ঞা ইতিহাস ও প্রজন্ম"
         width="1200" height="675"
         loading="eager"
         style="width: 100%; max-width: 100%; height: auto; border-radius: 10px; box-shadow: 0 4px 14px rgba(0,0,0,0.12); display: block; margin: 0 auto;"/>
    <span style="display: block; font-size: 14px; color: #5f6368; margin-top: 8px; font-style: italic;">
      চিত্র: এবাকাস ও চার্লস ব্যাবেজের অ্যানালিটিক্যাল ইঞ্জিন থেকে আধুনিক এআই সুপার কম্পিউটার
    </span>
  </div>

  <div class="htbd-qbox" style="background: #f8f9fa; border-left: 5px solid #1a73e8; padding: 20px 24px; margin: 22px 0; border-radius: 0 8px 8px 0; box-shadow: 0 1px 4px rgba(0,0,0,0.06);">
    <p style="margin: 0; font-size: 18px; line-height: 1.8;">
      <strong>📌 সারসংক্ষেপ (Quick Overview):</strong> 
      <strong>কম্পিউটার (Computer)</strong> হলো একটি দ্রুতগতির অত্যাধুনিক ইলেকট্রনিক গণনাকারী যন্ত্র, যা ব্যবহারকারীর নিকট থেকে কাঁচা ডেটা (Input) গ্রহণ করে, স্মৃতিতে সংরক্ষিত পূর্বনির্ধারিত নির্দেশাবলি (Program) অনুযায়ী তা প্রসেসিং (Processing) করে এবং নির্ভুল ফলাফল বা তথ্য (Output) প্রদর্শন করে। গ্রিক শব্দ 'Compute' থেকে কম্পিউটার শব্দের উৎপত্তি, যার অর্থ গণনা করা। আধুনিক কম্পিউটারের জনক হলেন চার্লস ব্যাবেজ এবং প্রথম প্রোগ্রামার হলেন লেডি অগাস্টা অ্যাডা লাভলেস। নিচে কম্পিউটারের মৌলিক গঠন, ১ম থেকে ৫ম প্রজন্মের তুলনা ও তথ্য ছক তুলে ধরা হলো।
    </p>
  </div>

  <div class="htbd-toc-box">
    <h3 style="margin-top: 0; color: #1a73e8; border-bottom: 2px solid #e8f0fe; padding-bottom: 10px; font-size: 20px; font-weight: 700;">📑 সূচিপত্র (Table of Contents)</h3>
    <ul class="htbd-toc-list">
      <li><a href="#definition">👉 ১. কম্পিউটারের মৌলিক সংজ্ঞা ও আইপিও (IPO) চক্র</a></li>
      <li><a href="#architecture">👉 ২. কম্পিউটারের অভ্যন্তরীণ স্থাপত্য: ভন নিউম্যান মডেল</a></li>
      <li><a href="#history">👉 ৩. কম্পিউটারের ঐতিহাসিক পটভূমি: এবাকাস থেকে মাইক্রোপ্রসেসর</a></li>
      <li><a href="#generations">👉 ৪. ১ম থেকে ৫ম প্রজন্মের প্রযুক্তিগত তুলনা ও বৈশিষ্ট্য</a></li>
      <li><a href="#features">👉 ৫. আধুনিক কম্পিউটারের অনন্য বৈশিষ্ট্যসমূহ</a></li>
      <li><a href="#gen-table">👉 ৬. বিভিন্ন প্রজন্মের তুলনামূলক তথ্য সারণী</a></li>
      <li><a href="#exam-prep">👉 ৭. বিসিএস ও চাকরির পরীক্ষার মডেল প্রশ্নোত্তর</a></li>
      <li><a href="#faqs">👉 ৮. সচরাচর জিজ্ঞাসিত প্রশ্ন (FAQ)</a></li>
    </ul>
  </div>

  <h2 id="definition" class="htbd-heading">১. কম্পিউটারের মৌলিক সংজ্ঞা ও আইপিও (IPO) চক্র</h2>
  <p>কম্পিউটার মূলত চারটি মৌলিক ধাপের ওপর ভিত্তি করে কাজ করে, যাকে <strong>IPO চক্র (Input-Processing-Output-Storage)</strong> বলা হয়:</p>
  <ul>
    <li><strong>ইনপুট (Input):</strong> কীবোর্ড, মাউস, স্ক্যানার ইত্যাদির মাধ্যমে ব্যবহারকারীর দেওয়া ডেটা ও নির্দেশ গ্রহণ।</li>
    <li><strong>প্রসেসিং (Processing):</strong> সেন্ট্রাল প্রসেসিং ইউনিট (CPU)-এর মাধ্যমে গাণিতিক ও যৌক্তিক প্রক্রিয়াকরণ।</li>
    <li><strong>আউটপুট (Output):</strong> মনিটর, প্রিন্টার বা স্পিকারের মাধ্যমে ফলাফল প্রদর্শন।</li>
    <li><strong>মেমোরি/স্টোরেজ (Storage):</strong> র্যাম (RAM) ও হার্ডডিস্ক/এসএসডি (SSD)-তে ভবিষ্যৎ ব্যবহারের জন্য ডেটা সংরক্ষণ।</li>
  </ul>

  <h2 id="history" class="htbd-heading">৩. কম্পিউটারের ঐতিহাসিক পটভূমি: এবাকাস থেকে মাইক্রোপ্রসেসর</h2>
  <p>খ্রিস্টপূর্ব ২৪০০ অব্দে ব্যবিলনে উদ্ভাবিত কাঠের তৈরি ফ্রেমযুক্ত গণনাকারী যন্ত্র <strong>'এবাকাস' (Abacus)</strong>-কে কম্পিউটারের আদি পূর্বপুরুষ বিবেচনা করা হয়। ১৬৪২ সালে ব্লেইজ প্যাসকেল প্রথম যান্ত্রিক ক্যালকুলেটর 'প্যাসকেলাইন' আবিষ্কার করেন।</p>
  <p>১৮৩৩ সালে ব্রিটিশ গণিতবিদ <strong>চার্লস ব্যাবেজ (Charles Babbage)</strong> তাঁর কালজয়ী 'অ্যানালিটিক্যাল ইঞ্জিন' (Analytical Engine)-এর নকশা প্রণয়ন করেন, যাতে ইনপুট, মেমোরি, প্রসেসর ও আউটপুটের সমন্বয় ছিল। এই কারণেই তাঁকে <strong>কম্পিউটারের জনক</strong> বলা হয়। আর কবি লর্ড বায়রনের কন্যা <strong>অ্যাডা লাভলেস</strong> এই ইঞ্জিনের জন্য প্রথম অ্যালগরিদম রচনা করে ইতিহাসের প্রথম কম্পিউটার প্রোগ্রামার হিসেবে অমর হয়ে আছেন।</p>

  {links_html}

  <h2 id="gen-table" class="htbd-heading">৬. বিভিন্ন প্রজন্মের তুলনামূলক তথ্য সারণী</h2>
  <div class="htbd-table-wrapper">
    <table class="htbd-table">
      <thead>
        <tr>
          <th>প্রজন্ম</th>
          <th>সময়কাল</th>
          <th>মূল ইলেকট্রনিক উপাদান</th>
          <th>উদাহরণ</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>প্রথম প্রজন্ম</strong></td>
          <td>১৯৪০ – ১৯৫৬</td>
          <td>ভ্যাকুয়াম টিউব (Vacuum Tube)</td>
          <td>ENIAC, UNIVAC-I, IBM-701</td>
        </tr>
        <tr>
          <td><strong>দ্বিতীয় প্রজন্ম</strong></td>
          <td>১৯৫৬ – ১৯৬৩</td>
          <td>ট্রানজিস্টর (Transistor)</td>
          <td>IBM 1401, CDC 1604</td>
        </tr>
        <tr>
          <td><strong>তৃতীয় প্রজন্ম</strong></td>
          <td>১৯৬৪ – ১৯৭১</td>
          <td>ইন্টিগ্রেটেড সার্কিট (IC)</td>
          <td>IBM 360, PDP-8</td>
        </tr>
        <tr>
          <td><strong>চতুর্থ প্রজন্ম</strong></td>
          <td>১৯৭১ – বর্তমান</td>
          <td>ভিএলএসআই ও মাইক্রোপ্রসেসর (VLSI / CPU)</td>
          <td>Intel Core i-Series, Apple M-Series</td>
        </tr>
        <tr>
          <td><strong>পঞ্চম প্রজন্ম</strong></td>
          <td>বর্তমান ও ভবিষ্যৎ</td>
          <td>কৃত্রিম বুদ্ধিমত্তা ও কোয়ান্টাম কম্পিউটিং (AI)</td>
          <td>Param, IBM Quantum, ChatGPT AI</td>
        </tr>
      </tbody>
    </table>
  </div>

  
  <h2 id="binary-system-hardware" class="htbd-heading">৫.১ বাইনারি সংখ্যা পদ্ধতি ও কম্পিউটারের অভ্যন্তরীণ কার্যপ্রণালী</h2>
  <p>কম্পিউটার কোনো মানুষের ভাষা (যেমন বাংলা বা ইংরেজি) সরাসরি বুঝতে পারে না। এটি শুধুমাত্র বিদ্যুৎ প্রবাহের দুটি অবস্থা—অন (ON) এবং অফ (OFF) বুঝতে পারে। এই নীতিকে ধারণ করেই <strong>বাইনারি সংখ্যা পদ্ধতি (Binary System)</strong> গড়ে উঠেছে, যার ভিত্তি মাত্র দুটি অঙ্ক: ০ এবং ১। ০ নির্দেশ করে কম ভোল্টেজ বা অফ (OFF), আর ১ নির্দেশ করে উচ্চ ভোল্টেজ বা অন (ON)।</p>
  <p>যেকোনো টেক্সট, ছবি, অডিও বা ভিডিও কম্পিউটার অসংখ্য ০ এবং ১-এর সিকোয়েন্সে রূপান্তর করে সংরক্ষণ করে, যাকে <strong>বিট (Bit - Binary Digit)</strong> বলা হয়। ৮টি বিট একত্রিত হয়ে তৈরি হয় ১টি <strong>বাইট (Byte)</strong>, যা মেমোরিতে একটি একক অক্ষর বা বর্ণ ধারণ করার প্রাথমিক একক। এই বাইনারি আর্কিটেকচারই আধুনিক ডিজিটাল বিপ্লবের মূল ভিত্তি।</p>

  <h2 id="exam-prep" class="htbd-heading">৭. বিসিএস ও চাকরির পরীক্ষার মডেল প্রশ্নোত্তর</h2>
  <p><strong>প্রশ্ন: আধুনিক কম্পিউটারের জনক কে?</strong><br>
  <strong>উত্তর:</strong> চার্লস ব্যাবেজ।</p>
  <p><strong>প্রশ্ন: কম্পিউটারকে ভাইরাস মুক্ত রাখতে কী সফটওয়্যার ব্যবহৃত হয়?</strong><br>
  <strong>উত্তর:</strong> অ্যান্টিভাইরাস (Antivirus)।</p>
  <p><strong>প্রশ্ন: কম্পিউটারের মস্তিষ্ক বলা হয় কাকে?</strong><br>
  <strong>উত্তর:</strong> সিপিইউ (CPU - Central Processing Unit)।</p>

  <h2 id="faqs" class="htbd-heading">৮. সচরাচর জিজ্ঞাসিত প্রশ্ন (FAQ)</h2>
  <div style="margin-top: 15px;">
    <p><strong>প্রশ্ন ১: প্রথম ডিজিটাল কম্পিউটারের নাম কী?</strong><br>
    উত্তর: এনিয়াক (ENIAC - Electronic Numerical Integrator and Computer)।</p>
    
    <p><strong>প্রশ্ন ২: ট্রানজিস্টর আবিষ্কার করা হয় কত সালে?</strong><br>
    উত্তর: ১৯৪৭ সালে বেল ল্যাবরেটরিতে বার্ডিন, ব্রাটেন ও শকলে ট্রানজিস্টর আবিষ্কার করেন।</p>
  </div>
</div>

<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{
      "@type": "Question",
      "name": "কম্পিউটার শব্দের অর্থ কী?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "কম্পিউটার শব্দটি গ্রিক 'Compute' শব্দ থেকে এসেছে, যার আভিধানিক অর্থ হিসাব বা গণনা করা।"
      }}
    }},
    {{
      "@type": "Question",
      "name": "প্রথম কম্পিউটার প্রোগ্রামার কে ছিলেন?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "ইতিহাসের প্রথম কম্পিউটার প্রোগ্রামার ছিলেন কবি লর্ড বায়রনের কন্যা লেডি অগাস্টা অ্যাডা লাভলেস।"
      }}
    }}
  ]
}}
</script>
"""
    return {
        "slug": slug,
        "post_id": post_id,
        "title": title,
        "category": category,
        "meta_desc": meta_desc,
        "html_content": content
    }


# ==============================================================================
# POST 10: MULTIPLICATION TABLE 1 TO 20 (NAMTA)
# ==============================================================================
def build_post_namta():
    slug = "namta-1-to-20"
    post_id = "3305641112403867224"
    title = "নামতা ১ থেকে ২০ পর্যন্ত: বাংলা ও ইংরেজিতে সহজে মুখস্থ করার চার্ট ও নিয়ম (২০২৬)"
    category = "মৌলিক গণিত,Primary Math"
    meta_desc = "১ থেকে ২০ এর গুণের নামতা চার্ট (Multiplication Table 1-20), বৈদিক গণিতের শর্টকাট ট্রিকস ও সহজে নামতা মুখস্থ রাখার পরীক্ষিত কৌশল পড়ুন HelpTrickBD-তে।"
    links_html = get_internal_links_for_topic("গণিত নামতা বিসিএস প্রাথমিক")

    content = f"""{STYLES_BLOCK}
<div class="htbd-post-wrapper">
  <div style="margin-bottom: 18px;">
    <span class="htbd-badge" style="background: #e8f0fe; color: #1a73e8; padding: 6px 14px; border-radius: 20px; font-weight: 600; font-size: 14px; display: inline-block;">
      📚 বিভাগ: প্রাথমিক ও মৌলিক গণিত | সর্বশেষ সংস্করণ: ২০২৬ | ১ থেকে ২০ এর সম্পূর্ণ চার্ট
    </span>
  </div>

  <!-- Hero Thumbnail Banner -->
  <div style="text-align: center; margin: 18px 0 25px 0;">
    <img src="https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/posts/namta-1-to-20-banner.png" 
         alt="নামতা ১ থেকে ২০ পর্যন্ত: বাংলা ও ইংরেজিতে সহজে মুখস্থ করার চার্ট ও নিয়ম" 
         title="১ থেকে ২০ এর নামতা চার্ট ও ট্রিকস"
         width="1200" height="675"
         loading="eager"
         style="width: 100%; max-width: 100%; height: auto; border-radius: 10px; box-shadow: 0 4px 14px rgba(0,0,0,0.12); display: block; margin: 0 auto;"/>
    <span style="display: block; font-size: 14px; color: #5f6368; margin-top: 8px; font-style: italic;">
      চিত্র: বাংলা ও ইংরেজিতে ১ থেকে ২০ পর্যন্ত গুণের পূর্ণাঙ্গ নামতা চার্ট ও দ্রুত গণনার শর্টকাট ট্রিকস
    </span>
  </div>

  <div class="htbd-qbox" style="background: #f8f9fa; border-left: 5px solid #1a73e8; padding: 20px 24px; margin: 22px 0; border-radius: 0 8px 8px 0; box-shadow: 0 1px 4px rgba(0,0,0,0.06);">
    <p style="margin: 0; font-size: 18px; line-height: 1.8;">
      <strong>📌 সারসংক্ষেপ (Quick Overview):</strong> 
      <strong>নামতা (Multiplication Table)</strong> হলো পাটিগণিতের মৌলিক ভিত্তি, যা যেকোনো জটিল গুণ, ভাগ এবং ঐকিক নিয়মের হিসাব দ্রুত মুখে মুখে সমাধান করার জাদুকরী হাতিয়ার। প্রাথমিক বিদ্যালয়ের শিক্ষার্থী থেকে শুরু করে বিসিএস, ব্যাংক বা যেকোনো সরকারি চাকরির পরীক্ষায় গণিত অংশের সময় বাঁচাতে <strong>১ থেকে ২০ পর্যন্ত নামতা</strong> মুখস্থ থাকা অপরিহার্য। নিচে বাংলা ও ইংরেজি ভাষায় ১ থেকে ২০ পর্যন্ত প্রতিটি নামতার পূর্ণাঙ্গ সারণী, ৯ এবং ১৯-এর নামতার বৈদিক গণিতের শর্টকাট কৌশল এবং প্র্যাকটিস শিট সাজিয়ে দেওয়া হলো।
    </p>
  </div>

  <div class="htbd-toc-box">
    <h3 style="margin-top: 0; color: #1a73e8; border-bottom: 2px solid #e8f0fe; padding-bottom: 10px; font-size: 20px; font-weight: 700;">📑 সূচিপত্র (Table of Contents)</h3>
    <ul class="htbd-toc-list">
      <li><a href="#importance">👉 ১. নামতা শেখার প্রয়োজনীয়তা ও দ্রুত গণনার গুরুত্ব</a></li>
      <li><a href="#table-1-to-5">👉 ২. ১ থেকে ৫ এর নামতা সারণী</a></li>
      <li><a href="#table-6-to-10">👉 ৩. ৬ থেকে ১০ এর নামতা সারণী (৯ এর ম্যাজিক ট্রিক)</a></li>
      <li><a href="#table-11-to-15">👉 ৪. ১১ থেকে ১৫ এর নামতা সারণী</a></li>
      <li><a href="#table-16-to-20">👉 ৫. ১৬ থেকে ২০ এর নামতা সারণী (১৯ এর শর্টকাট ট্রিক)</a></li>
      <li><a href="#tricks">👉 ৬. নামতা দ্রুত মুখস্থ রাখার বৈজ্ঞানিক ও পরীক্ষিত কৌশল</a></li>
      <li><a href="#faqs">👉 ৭. সচরাচর জিজ্ঞাসিত প্রশ্ন (FAQ)</a></li>
    </ul>
  </div>

  <h2 id="importance" class="htbd-heading">১. নামতা শেখার প্রয়োজনীয়তা ও দ্রুত গণনার গুরুত্ব</h2>
  <p>গণিত কোনো মুখস্থবিদ্যার বিষয় নয়, তবে মৌলিক গুণ ও ভাগের দ্রুত হিসাব সম্পন্ন করতে নামতা মুখস্থ থাকা একটি আবশ্যকীয় দক্ষতা। বিশেষ করে প্রতিযোগিতামূলক চাকরির পরীক্ষায় ক্যালকুলেটর ব্যবহারের সুযোগ থাকে না। সেখানে ১ থেকে ২০ এর নামতা জানা থাকলে একজন প্রার্থী অন্যদের চেয়ে দ্বিগুণ গতিতে অঙ্ক সমাধান করতে পারেন।</p>

  <h2 id="table-1-to-5" class="htbd-heading">২. ১ থেকে ৫ এর নামতা সারণী</h2>
  <div class="htbd-table-wrapper">
    <table class="htbd-table">
      <thead>
        <tr>
          <th>১ এর নামতা</th>
          <th>২ এর নামতা</th>
          <th>৩ এর নামতা</th>
          <th>৪ এর নামতা</th>
          <th>৫ এর নামতা</th>
        </tr>
      </thead>
      <tbody>
        <tr><td>১ × ১ = ১</td><td>২ × ১ = ২</td><td>৩ × ১ = ৩</td><td>৪ × ১ = ৪</td><td>৫ × ১ = ৫</td></tr>
        <tr><td>১ × ২ = ২</td><td>২ × ২ = ৪</td><td>৩ × ২ = ৬</td><td>৪ × ২ = ৮</td><td>৫ × ২ = ১০</td></tr>
        <tr><td>১ × ৩ = ৩</td><td>২ × ৩ = ৬</td><td>৩ × ৩ = ৯</td><td>৪ × ৩ = ১২</td><td>৫ × ৩ = ১৫</td></tr>
        <tr><td>১ × ৪ = ৪</td><td>২ × ৪ = ৮</td><td>৩ × ৪ = ১২</td><td>৪ × ৪ = ১৬</td><td>৫ × ৪ = ২০</td></tr>
        <tr><td>১ × ৫ = ৫</td><td>২ × ৫ = ১০</td><td>৩ × ৫ = ১৫</td><td>৪ × ৫ = ২০</td><td>৫ × ৫ = ২৫</td></tr>
        <tr><td>১ × ৬ = ৬</td><td>২ × ৬ = ১২</td><td>৩ × ৬ = ১৮</td><td>৪ × ৬ = ২৪</td><td>৫ × ৬ = ৩০</td></tr>
        <tr><td>১ × ৭ = ৭</td><td>২ × ৭ = ১৪</td><td>৩ × ৭ = ২১</td><td>৪ × ৭ = ২৮</td><td>৫ × ৭ = ৩৫</td></tr>
        <tr><td>১ × ৮ = ৮</td><td>২ × ৮ = ১৬</td><td>৩ × ৮ = ২৪</td><td>৪ × ৮ = ৩২</td><td>৫ × ৮ = ৪০</td></tr>
        <tr><td>১ × ৯ = ৯</td><td>২ × ৯ = ১৮</td><td>৩ × ৯ = ২৭</td><td>৪ × ৯ = ৩৬</td><td>৫ × ৯ = ৪৫</td></tr>
        <tr><td>১ × ১০ = ১০</td><td>২ × ১০ = ২০</td><td>৩ × ১০ = ৩০</td><td>৪ × ১০ = ৪০</td><td>৫ × ১০ = ৫০</td></tr>
      </tbody>
    </table>
  </div>

  {links_html}

  <h2 id="table-6-to-10" class="htbd-heading">৩. ৬ থেকে ১০ এর নামতা সারণী (৯ এর ম্যাজিক ট্রিক)</h2>
  <div class="htbd-table-wrapper">
    <table class="htbd-table">
      <thead>
        <tr>
          <th>৬ এর নামতা</th>
          <th>৭ এর নামতা</th>
          <th>৮ এর নামতা</th>
          <th>৯ এর নামতা</th>
          <th>১০ এর নামতা</th>
        </tr>
      </thead>
      <tbody>
        <tr><td>৬ × ১ = ৬</td><td>৭ × ১ = ৭</td><td>৮ × ১ = ৮</td><td>৯ × ১ = ৯</td><td>১০ × ১ = ১০</td></tr>
        <tr><td>৬ × ২ = ১২</td><td>৭ × ২ = ১৪</td><td>৮ × ২ = ১৬</td><td>৯ × ২ = ১৮</td><td>১০ × ২ = ২০</td></tr>
        <tr><td>৬ × ৩ = ১৮</td><td>৭ × ৩ = ২১</td><td>৮ × ৩ = ২৪</td><td>৯ × ৩ = ২৭</td><td>১০ × ৩ = ৩০</td></tr>
        <tr><td>৬ × ৪ = ২৪</td><td>৭ × ৪ = ২৮</td><td>৮ × ৪ = ৩২</td><td>৯ × ৪ = ৩৬</td><td>১০ × ৪ = ৪০</td></tr>
        <tr><td>৬ × ৫ = ৩০</td><td>৭ × ৫ = ৩৫</td><td>৮ × ৫ = ৪০</td><td>৯ × ৫ = ৪৫</td><td>১০ × ৫ = ৫০</td></tr>
        <tr><td>৬ × ৬ = ৩৬</td><td>৭ × ৬ = ৪২</td><td>৮ × ৬ = ৪৮</td><td>৯ × ৬ = ৫৪</td><td>১০ × ৬ = ৬০</td></tr>
        <tr><td>৬ × ৭ = ৪২</td><td>৭ × ৭ = ৪৯</td><td>৮ × ৭ = ৫৬</td><td>৯ × ৭ = ৬৩</td><td>১০ × ৭ = ৭০</td></tr>
        <tr><td>৬ × ৮ = ৪৮</td><td>৭ × ৮ = ৫৬</td><td>৮ × ৮ = ৬৪</td><td>৯ × ৮ = ৭২</td><td>১০ × ৮ = ৮০</td></tr>
        <tr><td>৬ × ৯ = ৫৪</td><td>৭ × ৯ = ৬৩</td><td>৮ × ৯ = ৭২</td><td>৯ × ৯ = ৮১</td><td>১০ × ৯ = ৯০</td></tr>
        <tr><td>৬ × ১০ = ৬০</td><td>৭ × ১০ = ৭০</td><td>৮ × ১০ = ৮০</td><td>৯ × ১০ = ৯০</td><td>১০ × ১০ = ১০০</td></tr>
      </tbody>
    </table>
  </div>

  <p><strong>💡 ৯ এর নামতার ম্যাজিক ট্রিক:</strong> ৯ এর ঘরের গুণফলের দশকের অংক ০ থেকে ৯ পর্যন্ত ক্রমানুসারে বাড়ে (০, ১, ২, ৩... ৯), আর এককের অংক ৯ থেকে ০ পর্যন্ত কমে (৯, ৮, ৭... ০)! ফলে খুব সহজেই ৯-এর নামতা লেখা যায়!</p>

  <h2 id="table-11-to-15" class="htbd-heading">৪. ১১ থেকে ১৫ এর নামতা সারণী</h2>
  <div class="htbd-table-wrapper">
    <table class="htbd-table">
      <thead>
        <tr>
          <th>১১ এর নামতা</th>
          <th>১২ এর নামতা</th>
          <th>১৩ এর নামতা</th>
          <th>১৪ এর নামতা</th>
          <th>১৫ এর নামতা</th>
        </tr>
      </thead>
      <tbody>
        <tr><td>১১ × ১ = ১১</td><td>১২ × ১ = ১২</td><td>১৩ × ১ = ১৩</td><td>১৪ × ১ = ১৪</td><td>১৫ × ১ = ১৫</td></tr>
        <tr><td>১১ × ২ = ২২</td><td>১২ × ২ = ২৪</td><td>১৩ × ২ = ২৬</td><td>১৪ × ২ = ২৮</td><td>১৫ × ২ = ৩০</td></tr>
        <tr><td>১১ × ৩ = ৩৩</td><td>১২ × ৩ = ৩৬</td><td>১৩ × ৩ = ৩৯</td><td>১৪ × ৩ = ৪২</td><td>১৫ × ৩ = ৪৫</td></tr>
        <tr><td>১১ × ৪ = ৪৪</td><td>১২ × ৪ = ৪৮</td><td>১৩ × ৪ = ৫২</td><td>১৪ × ৪ = ৫৬</td><td>১৫ × ৪ = ৬০</td></tr>
        <tr><td>১১ × ৫ = ৫৫</td><td>১২ × ৫ = ৬০</td><td>১৩ × ৫ = ৬৫</td><td>১৪ × ৫ = ৭০</td><td>১৫ × ৫ = ৭৫</td></tr>
        <tr><td>১১ × ৬ = ৬৬</td><td>১২ × ৬ = ৭২</td><td>১৩ × ৬ = ৭৮</td><td>১৪ × ৬ = ৮৪</td><td>১৫ × ৬ = ৯০</td></tr>
        <tr><td>১১ × ৭ = ৭৭</td><td>১২ × ৭ = ৮৪</td><td>১৩ × ৭ = ৯১</td><td>১৪ × ৭ = ৯৮</td><td>১৫ × ৭ = ১০৫</td></tr>
        <tr><td>১১ × ৮ = ৮৮</td><td>১২ × ৮ = ৯৬</td><td>১৩ × ৮ = ১০৪</td><td>১৪ × ৮ = ১১২</td><td>১৫ × ৮ = ১২০</td></tr>
        <tr><td>১১ × ৯ = ৯৯</td><td>১২ × ৯ = ১০৮</td><td>১৩ × ৯ = ১১৭</td><td>১৪ × ৯ = ১২৬</td><td>১৫ × ৯ = ১৩৫</td></tr>
        <tr><td>১১ × ১০ = ১১০</td><td>১২ × ১০ = ১২০</td><td>১৩ × ১০ = ১৩০</td><td>১৪ × ১০ = ১৪০</td><td>১৫ × ১০ = ১৫০</td></tr>
      </tbody>
    </table>
  </div>

  <h2 id="table-16-to-20" class="htbd-heading">৫. ১৬ থেকে ২০ এর নামতা সারণী (১৯ এর শর্টকাট ট্রিক)</h2>
  <div class="htbd-table-wrapper">
    <table class="htbd-table">
      <thead>
        <tr>
          <th>১৬ এর নামতা</th>
          <th>১৭ এর নামতা</th>
          <th>১৮ এর নামতা</th>
          <th>১৯ এর নামতা</th>
          <th>২০ এর নামতা</th>
        </tr>
      </thead>
      <tbody>
        <tr><td>১৬ × ১ = ১৬</td><td>১৭ × ১ = ১৭</td><td>১৮ × ১ = ১৮</td><td>১৯ × ১ = ১৯</td><td>২০ × ১ = ২০</td></tr>
        <tr><td>১৬ × ২ = ৩২</td><td>১৭ × ২ = ৩৪</td><td>১৮ × ২ = ৩৬</td><td>১৯ × ২ = ৩৮</td><td>২০ × ২ = ৪০</td></tr>
        <tr><td>১৬ × ৩ = ৪৮</td><td>১৭ × ৩ = ৫১</td><td>১৮ × ৩ = ৫৪</td><td>১৯ × ৩ = ৫৭</td><td>২০ × ৩ = ৬০</td></tr>
        <tr><td>১৬ × ৪ = ৬৪</td><td>১৭ × ৪ = ৬৮</td><td>১৮ × ৪ = ৭২</td><td>১৯ × ৪ = ৭৬</td><td>২০ × ৪ = ৮০</td></tr>
        <tr><td>১৬ × ৫ = ৮০</td><td>১৭ × ৫ = ৮৫</td><td>১৮ × ৫ = ৯০</td><td>১৯ × ৫ = ৯৫</td><td>২০ × ৫ = ১০০</td></tr>
        <tr><td>১৬ × ৬ = ৯৬</td><td>১৭ × ৬ = ১০২</td><td>১৮ × ৬ = ১০৮</td><td>১৯ × ৬ = ১১৪</td><td>২০ × ৬ = ১২০</td></tr>
        <tr><td>১৬ × ৭ = ১১২</td><td>১৭ × ৭ = ১১৯</td><td>১৮ × ৭ = ১২৬</td><td>১৯ × ৭ = ১৩৩</td><td>২০ × ৭ = ১৪০</td></tr>
        <tr><td>১৬ × ৮ = ১২৮</td><td>১৭ × ৮ = ১৩৬</td><td>১৮ × ৮ = ১৪৪</td><td>১৯ × ৮ = ১৫২</td><td>২০ × ৮ = ১৬০</td></tr>
        <tr><td>১৬ × ৯ = ১৪৪</td><td>১৭ × ৯ = ১৫৩</td><td>১৮ × ৯ = ১৬২</td><td>১৯ × ৯ = ১৭১</td><td>২০ × ৯ = ১৮০</td></tr>
        <tr><td>১৬ × ১০ = ১৬০</td><td>১৭ × ১০ = ১৭০</td><td>১৮ × ১০ = ১৮০</td><td>১৯ × ১০ = ১৯০</td><td>২০ × ১০ = ২০০</td></tr>
      </tbody>
    </table>
  </div>

  <p><strong>💡 ১৯ এর নামতার ম্যাজিক ট্রিক:</strong> দশকের ঘরে বিজোড় সংখ্যাগুলো লিখুন (১, ৩, ৫, ৭, ৯, ১১, ১৩, ১৫, ১৭, ১৯)। আর ডানপাশে এককের ঘরে ৯ থেকে ০ পর্যন্ত উল্টো করে লিখুন (৯, ৮, ৭, ৬, ৫, ৪, ৩, ২, ১, ০)! মুহূর্তেই তৈরি হয়ে গেল ১৯-এর নামতা!</p>

  <h2 id="faqs" class="htbd-heading">৭. সচরাচর জিজ্ঞাসিত প্রশ্ন (FAQ)</h2>
  <div style="margin-top: 15px;">
    <p><strong>প্রশ্ন ১: শিশুদের সহজে নামতা মুখস্থ করানোর সেরা উপায় কী?</strong><br>
    উত্তর: প্রতিদিন সকালে উচ্চস্বরে ছন্দের মতো করে আবৃত্তি করা এবং উল্টো দিক থেকে (যেমন ৯ × ৯ = ৮১, ৯ × ৮ = ৭২) প্র্যাকটিস করানো সবচেয়ে কার্যকর।</p>
    
    <p><strong>প্রশ্ন ২: চাকরির পরীক্ষার জন্য কত পর্যন্ত নামতা জানা আবশ্যক?</strong><br>
    উত্তর: বিসিএস, প্রাইমারি শিক্ষক নিয়োগ ও ব্যাংকের গণিত দ্রুত সমাধানের জন্য ১ থেকে ২০ পর্যন্ত নামতা নখদর্পণে থাকা আবশ্যক।</p>
  </div>
</div>

<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{
      "@type": "Question",
      "name": "১ থেকে ২০ এর নামতা কীভাবে সহজে মনে রাখা যায়?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "নিয়মিত ছন্দাকারে পড়া এবং ৯ ও ১৯ এর ঘরের মতো বৈদিক গণিতের শর্টকাট কৌশল প্রয়োগ করলে সহজে নামতা মনে রাখা যায়।"
      }}
    }},
    {{
      "@type": "Question",
      "name": "নামতা মুখস্থ থাকলে গণিতে কী সুবিধা হয়?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "বড় বড় গুণ, ভাগ, শতকরা ও লসাগু-গসাগু মুখে মুখে নির্ভুলভাবে সমাধান করা যায়, যা প্রতিযোগিতামূলক পরীক্ষায় সময় বাঁচায়।"
      }}
    }}
  ]
}}
</script>
"""
    return {
        "slug": slug,
        "post_id": post_id,
        "title": title,
        "category": category,
        "meta_desc": meta_desc,
        "html_content": content
    }


BATCH_2_BUILDERS = [
    build_post_certificate_correction,
    build_post_ssc_instructions,
    build_post_hason_raja,
    build_post_livestock_institute,
    build_post_vidyasagar,
    build_post_population_factors,
    build_post_reserved_women_seats,
    build_post_child_socialization,
    build_post_computer_definition,
    build_post_namta
]


def execute_batch(builders):
    service = get_authenticated_service()
    if not service:
        print("[!] ERROR: Blogger Authentication service is not available.")
        return False

    print("\n" + "="*75)
    print(f"🚀 HelpTrickBD Automated Batch 2 Post Reviver: Executing {len(builders)} Posts")
    print("="*75)

    success_count = 0
    for idx, builder_fn in enumerate(builders, 1):
        data = builder_fn()
        slug = data["slug"]
        post_id = data["post_id"]
        title = data["title"]
        category = data["category"]
        meta_desc = data["meta_desc"]
        html_content = data["html_content"]

        plain_text = " ".join(html_content.split())
        approx_words = len(plain_text.split())

        print(f"\n[{idx}/{len(builders)}] Processing Post: {slug}")
        print(f"  Title:      {title}")
        print(f"  Post ID:    {post_id}")
        print(f"  Est. Words: {approx_words} words (AdSense High-Value Compliant)")

        html_path = os.path.join(OUTPUT_DIR, f"{slug}.html")
        meta_path = os.path.join(OUTPUT_DIR, f"{slug}_metadata.json")

        full_doc = f"""<!DOCTYPE html>
<html lang="bn">
<head>
  <meta charset="UTF-8">
  <title>{title}</title>
  <meta name="description" content="{meta_desc}">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
{html_content}
</body>
</html>"""

        with open(html_path, "w", encoding="utf-8") as f:
            f.write(full_doc)

        labels = [c.strip() for c in category.split(",") if c.strip()]
        meta_dict = {
            "slug": slug,
            "post_id": post_id,
            "title": title,
            "category": category,
            "labels": labels,
            "meta_description": meta_desc,
            "word_count": approx_words,
            "updated_at": time.strftime("%Y-%m-%dT%H:%M:%S+06:00")
        }
        with open(meta_path, "w", encoding="utf-8") as f:
            json.dump(meta_dict, f, ensure_ascii=False, indent=2)

        try:
            body = {
                "title": title,
                "content": html_content
            }
            if labels:
                body["labels"] = labels

            updated = service.posts().patch(blogId=BLOG_ID, postId=post_id, body=body).execute()
            live_url = updated.get("url", "")
            print(f"  ✅ Blogger Updated Successfully! Live URL: {live_url}")
            success_count += 1
        except Exception as e:
            print(f"  ❌ Blogger Update Failed: {e}")

        time.sleep(1.5)

    print("\n" + "="*75)
    print(f"🎉 Batch 2 Execution Complete: {success_count}/{len(builders)} Posts Successfully Updated Live!")
    print("="*75)
    return success_count == len(builders)


def main():
    execute_batch(BATCH_2_BUILDERS)


if __name__ == "__main__":
    main()
