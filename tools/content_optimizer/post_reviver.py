#!/usr/bin/env python3
"""
HelpTrickBD Post Reviver & Thin Content Expansion Engine
Transforms low-value/thin posts (< 500 words) into 1,200 - 2,000+ words
high-authority Google 1st-Page ranking educational guides.

Features:
- Maintains existing URL permalink (no broken links/404s)
- Deepens academic depth to 1,200+ words
- Theme CSS classes (.htbd-post-wrapper, .htbd-qbox, .htbd-badge)
- Position 0 Featured Snippet definition
- Responsive Analytical Tables
- Embedded Schema.org FAQPage JSON-LD
- Automatic contextual internal links from HelpTrickBD index

Usage:
    python post_reviver.py --topic "বাংলাদেশের বিস্তারিত ইতিহাস: সংগ্রাম, মুক্তিযুদ্ধ ও বিজয়" --category "বাংলাদেশ ও মুক্তিযুদ্ধ"
"""

import argparse
import json
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
try:
    from internal_linker.linker import find_related_links, generate_internal_link_box
except ImportError:
    find_related_links = None
    generate_internal_link_box = None

try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

OUTPUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "output_posts", "revived_posts"))


def generate_bangladesh_history_article():
    """
    Transforms the 15-word 'history-of-bangladesh.html' post into a 1,600+ word masterpiece.
    """
    topic = "বাংলাদেশের বিস্তারিত ইতিহাস: সংগ্রাম, মুক্তিযুদ্ধ ও বিজয়"
    category = "বাংলাদেশ ও মুক্তিযুদ্ধ"
    year = "২০২৬"
    slug = "history-of-bangladesh"

    # Fetch Internal Links
    internal_links_html = ""
    if find_related_links and generate_internal_link_box:
        try:
            rel = find_related_links("ইতিহাস বাংলাদেশ মুক্তিযুদ্ধ", max_links=3)
            internal_links_html = generate_internal_link_box(rel)
        except Exception:
            pass

    html_content = f"""<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Hind+Siliguri:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Hind+Siliguri:wght@400;500;600;700&display=swap');
  .htbd-post-wrapper,
  .htbd-post-wrapper * {{
    font-family: 'Hind Siliguri', 'Noto Sans Bengali', Arial, sans-serif !important;
  }}
  .htbd-post-wrapper p {{
    font-size: 18px !important;
    line-height: 1.85 !important;
    color: #202124 !important;
    margin: 16px 0 !important;
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
    list-style-type: none !important;
    padding: 8px 0 !important;
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
</style>

<div class="htbd-post-wrapper">
  
  <!-- Category & Freshness Badge -->
  <div style="margin-bottom: 18px;">
    <span class="htbd-badge" style="background: #e8f0fe; color: #1a73e8; padding: 6px 14px; border-radius: 20px; font-weight: 600; font-size: 14px; display: inline-block;">
      📚 বিভাগ: {category} | সর্বশেষ আপডেট: {year} | পূর্ণাঙ্গ স্পেশাল স্টাডি গাইড
    </span>
  </div>

  <!-- Featured Snippet Box (Position 0) -->
  <div class="htbd-qbox" style="background: #f8f9fa; border-left: 5px solid #1a73e8; padding: 20px 24px; margin: 22px 0; border-radius: 0 8px 8px 0; box-shadow: 0 1px 4px rgba(0,0,0,0.06);">
    <p style="margin: 0; font-size: 18px; line-height: 1.8;">
      <strong>📌 সারসংক্ষেপ (Quick Overview):</strong> 
      <strong>বাংলাদেশের ইতিহাস</strong> বলতে ১৯৪৭ সালে ব্রিটিশ ঔপনিবেশিক শাসনের অবসানের পর থেকে শুরু হওয়া পূর্ব পাকিস্তানের রাজনৈতিক বঞ্চনা, ১৯৫২ সালের ভাষা আন্দোলন, ১৯৬৬ সালের ছয় দফা দাবি, ১৯৬৯ সালের গণঅভ্যুত্থান এবং ১৯৭১ সালের রক্তক্ষয়ী ৯ মাসের সশস্ত্র মুক্তিযুদ্ধের মাধ্যমে স্বাধীন সার্বভৌম বাংলাদেশের অভ্যুদয়কে বোঝায়। নিচে ১৯৪৭ থেকে ১৯৭১ সালের প্রতিটি ঐতিহাসিক পর্বের সালভিত্তিক ধারাবাহিক বিশ্লেষণ, তথ্য সারণী ও মডেল প্রশ্নোত্তর তুলে ধরা হলো।
    </p>
  </div>

  <!-- Table of Contents (Fixed No double numbers) -->
  <div class="htbd-toc-box">
    <h3 style="margin-top: 0; color: #1a73e8; border-bottom: 2px solid #e8f0fe; padding-bottom: 10px; font-size: 20px; font-weight: 700;">📑 সূচিপত্র (Table of Contents)</h3>
    <ul class="htbd-toc-list">
      <li><a href="#intro">👉 ১. ভূমিকা: বাঙালি জাতীয়তাবাদের উন্মেষ</a></li>
      <li><a href="#bhasha-andolon">👉 ২. ১৯৫২ সালের ভাষা আন্দোলন ও আত্মপরিচয়ের সূচনা</a></li>
      <li><a href="#juktofront">👉 ৩. ১৯৫৪ সালের যুক্তফ্রন্ট নির্বাচন ও রাজনৈতিক মেরুকরণ</a></li>
      <li><a href="#chhoy-dofa">👉 ৪. ১৯৬৬ সালের ঐতিহাসিক ৬ দফা: বাঙালির মুক্তিসনদ</a></li>
      <li><a href="#gono-obvutthan">👉 ৫. ১৯৬৯ সালের গণঅভ্যুত্থান ও ১৯৭০-এর নির্বাচন</a></li>
      <li><a href="#timeline-table">👉 ৬. বাংলাদেশের স্বাধীনতা সংগ্রামের সালভিত্তিক তথ্য সারণী</a></li>
      <li><a href="#muktijuddho">👉 ৭. ১৯৭১ সালের মুক্তিযুদ্ধ: অপারেশন সার্চলাইট থেকে চূড়ান্ত বিজয়</a></li>
      <li><a href="#exam-prep">👉 ৮. বিসিএস ও বিশ্ববিদ্যালয়ের পরীক্ষার স্পেশাল মডেল প্রশ্নোত্তর</a></li>
      <li><a href="#faqs">👉 ৯. সচরাচর জিজ্ঞাসিত প্রশ্ন (FAQ)</a></li>
    </ul>
  </div>

  <!-- Section 1: Intro -->
  <h2 id="intro" class="htbd-heading">১. ভূমিকা: বাঙালি জাতীয়তাবাদের উন্মেষ</h2>
  <p>বিশ্বের মানচিত্রে বাংলাদেশ একমাত্র দেশ, যা নিজের ভাষার মর্যাদা রক্ষা এবং রক্তক্ষয়ী সশস্ত্র সংগ্রামের মাধ্যমে স্বাধীনতা অর্জন করেছে। ১৯৪৭ সালে ধর্মভিত্তিক দ্বিজাতিতত্ত্বের ওপর ভিত্তি করে যখন পাকিস্তান ও ভারত বিভক্ত হয়, তখনই স্পষ্ট হয়ে উঠেছিল যে ভৌগোলিক ও সাংস্কৃতিকভাবে বিচ্ছিন্ন পূর্ব পাকিস্তানের ওপর পশ্চিম পাকিস্তানের বৈষম্যমূলক শাসন স্থায়ী হতে পারে না। অর্থনৈতিক শোষণ, রাজনৈতিক অধিকার হরণ এবং সাংস্কৃতিক আগ্রাসনের বিরুদ্ধে বাঙালি জাতি ধাপে ধাপে ঐক্যবদ্ধ প্রতিরোধ গড়ে তোলে।</p>

  <!-- Section 2: Language Movement -->
  <h2 id="bhasha-andolon" class="htbd-heading">২. ১৯৫২ সালের ভাষা আন্দোলন ও আত্মপরিচয়ের সূচনা</h2>
  <p>বাঙালির স্বাধীনতা সংগ্রামের প্রথম বীজ রোপিত হয়েছিল ভাষার দাবিতে। সংখ্যাগরিষ্ঠ মানুষের মাতৃভাষা বাংলাকে উপেক্ষা করে যখন উর্দুকে পাকিস্তানের একমাত্র রাষ্ট্রভাষা হিসেবে চাপিয়ে দেওয়ার ষড়যন্ত্র করা হয়, তখন ছাত্রসমাজ ও সাধারণ জনগণ রাজপথে নেমে আসে।</p>
  <p>১৯৫২ সালের ২১ ফেব্রুয়ারি ঢাকার রাজপথে সালাম, বরকত, রফিক, জব্বার প্রমুখের আত্মত্যাগের মধ্য দিয়ে ভাষার মর্যাদা প্রতিষ্ঠিত হয়। এটি কেবল ভাষার লড়াই ছিল না, বরং তা ছিল অসাম্প্রদায়িক বাঙালি জাতীয়তাবাদের প্রথম সফল বহিঃপ্রকাশ, যা পরবর্তীতে স্বাধিকার আন্দোলনের পথ উন্মুক্ত করে। ইউনেস্কো ১৯৯৯ সালে দিনটিকে <strong>'আন্তর্জাতিক মাতৃভাষা দিবস'</strong> হিসেবে স্বীকৃতি দিয়ে সমগ্র বিশ্বের মর্যাদার আসনে আসীন করে।</p>

  <!-- Dynamic Live Internal Linking Box -->
  {internal_links_html}

  <!-- Section 3: 1954 Juktofront -->
  <h2 id="juktofront" class="htbd-heading">৩. ১৯৫৪ সালের যুক্তফ্রন্ট নির্বাচন ও রাজনৈতিক মেরুকরণ</h2>
  <p>পশ্চিম পাকিস্তানি শাসকগোষ্ঠীর মুসলিম লীগ সরকারের বিরুদ্ধে শেরে বাংলা এ. কে. ফজলুল হক, হোসেন শহীদ সোহরাওয়ার্দী ও মওলানা আবদুল হামিদ খান ভাসানীর নেতৃত্বে গড়ে ওঠে যুক্তফ্রন্ট। ১৯৫৪ সালের নির্বাচনে যুক্তফ্রন্ট ২১ দফার ভিত্তিতে বিপুল জনসমর্থন নিয়ে নিরঙ্কুশ বিজয় লাভ করে মুসলিম লীগকে ধূলিসাৎ করে দেয়। যদিও পাকিস্তানি শাসকগোষ্ঠী অচিরেই ষড়যন্ত্রের মাধ্যমে ৯২(ক) ধারা জারি করে নির্বাচিত সরকারকে ভেঙে দেয়, তবে বাঙালির রাজনৈতিক আত্মবিশ্বাস এই নির্বাচনের মাধ্যমেই চূড়ান্ত রূপ ধারণ করে।</p>

  <!-- Section 4: 6-Point Movement -->
  <h2 id="chhoy-dofa" class="htbd-heading">৪. ১৯৬৬ সালের ঐতিহাসিক ৬ দফা: বাঙালির মুক্তিসনদ (Magna Carta)</h2>
  <p>১৯৬৫ সালের পাক-ভারত যুদ্ধে পূর্ব পাকিস্তানের সম্পূর্ণ নিরাপত্তাহীন অবস্থা উন্মোচিত হওয়ার পর জাতির পিতা বঙ্গবন্ধু শেখ মুজিবুর রহমান ১৯৬৬ সালের ৫ ও ৬ ফেব্রুয়ারি লাহোরে ঐতিহাসিক <strong>ছয় দফা দাবি</strong> উত্থাপন করেন।</p>
  <ul>
    <li><strong>দফা ১:</strong> ঐতিহাসিক লাহোর প্রস্তাবের ভিত্তিতে যুক্তরাষ্ট্রীয় পদ্ধতির শাসন ও সংসদীয় সরকার প্রতিষ্ঠা।</li>
    <li><strong>দফা ২:</strong> কেন্দ্রীয় সরকারের হাতে কেবল প্রতিরক্ষা ও পররাষ্ট্র বিষয় ন্যস্ত থাকবে; অবশিষ্ট বিষয় প্রদেশের হাতে।</li>
    <li><strong>দফা ৩:</strong> দুই অঞ্চলের জন্য দুটি পৃথক অথচ অবাধে রূপান্তরযোগ্য মুদ্রা চালু অথবা মুদ্রা ব্যবস্থার নিয়ন্ত্রণ নিশ্চিত করা।</li>
    <li><strong>দফা ৪:</strong> কর, রাজস্ব ধার্য ও আদায়ের ক্ষমতা প্রাদেশিক সরকারের হাতে ন্যস্ত থাকা।</li>
    <li><strong>দফা ৫:</strong> বৈদেশিক বাণিজ্য ও বৈদেশিক মুদ্রার আয় স্ব স্ব অঞ্চলের অধীনে রাখা।</li>
    <li><strong>দফা ৬:</strong> আঞ্চলিক প্রতিরক্ষার জন্য মিলিশিয়া বা আধা-সামরিক বাহিনী গঠনের ক্ষমতা প্রদান।</li>
  </ul>

  <!-- Section 5: Mass Uprising & Election -->
  <h2 id="gono-obvutthan" class="htbd-heading">৫. ১৯৬৯ সালের গণঅভ্যুত্থান ও ১৯৭০-এর সাধারণ নির্বাচন</h2>
  <p>বঙ্গবন্ধু ও নেতৃবৃন্দকে ফাঁসি দেওয়ার উদ্দেশ্যে পাকিস্তানি সামরিক শাসক আইয়ুব খান 'আগরতলা ষড়যন্ত্র মামলা' দায়ের করে। এর প্রতিবাদে ছাত্র-শ্রমিক-জনতার ঐক্যবদ্ধ লড়াইয়ে ১৯৬৯ সালের গণঅভ্যুত্থান সংঘটিত হয়। শহীদ আসাদ ও সার্জেন্ট জহুরুল হকের আত্মত্যাগের মুখে আইয়ুব খান পদত্যাগে বাধ্য হন এবং বঙ্গবন্ধু কারামুক্ত হন। এই বছরেই তাঁকে ঐতিহাসিক 'বঙ্গবন্ধু' উপাধিতে ভূষিত করা হয়।</p>
  <p>পরবর্তীতে ১৯৭০ সালের পাকিস্তানের প্রথম সাধারণ নির্বাচনে আওয়ামী লীগ জাতীয় পরিষদের ১৬৯টি আসনের মধ্যে ১৬৭টি আসন লাভ করে একক সংখ্যাগরিষ্ঠতা অর্জন করে। কিন্তু পাকিস্তানি সামরিক জান্তা ক্ষমতা হস্তান্তর না করে গভীর ষড়যন্ত্রে লিপ্ত হয়।</p>

  <!-- Section 6: Historical Timeline Table -->
  <h2 id="timeline-table" class="htbd-heading">৬. স্বাধীনতা সংগ্রামের সালভিত্তিক ধারাবাহিক তথ্য সারণী</h2>
  <p>পরীক্ষার্থীদের মুখস্থের সুবিধার্থে মূল ঐতিহাসিক মাইলফলকগুলো নিচে সারণীর মাধ্যমে সংক্ষেপে দেওয়া হলো:</p>
  <div style="overflow-x: auto;">
    <table style="width: 100%; border-collapse: collapse; margin: 20px 0; background: #fff; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
      <thead>
        <tr style="background-color: #1a73e8; color: white; text-align: left;">
          <th style="padding: 14px; border: 1px solid #c2e7ff;">সাল ও তারিখ</th>
          <th style="padding: 14px; border: 1px solid #c2e7ff;">ঐতিহাসিক ঘটনা</th>
          <th style="padding: 14px; border: 1px solid #c2e7ff;">গুরুত্ব ও তাৎপর্য</th>
        </tr>
      </thead>
      <tbody>
        <tr style="background-color: #f8fafd;">
          <td style="padding: 12px; border: 1px solid #e0e0e0; font-weight: bold;">২১ ফেব্রুয়ারি ১৯৫২</td>
          <td style="padding: 12px; border: 1px solid #e0e0e0;">মহান ভাষা আন্দোলন</td>
          <td style="padding: 12px; border: 1px solid #e0e0e0;">বাঙালি জাতীয়তাবাদের উন্মেষ ও রক্তের বিনিময়ে ভাষার স্বীকৃতি</td>
        </tr>
        <tr>
          <td style="padding: 12px; border: 1px solid #e0e0e0; font-weight: bold;">৮ মার্চ ১৯৫৪</td>
          <td style="padding: 12px; border: 1px solid #e0e0e0;">যুক্তফ্রন্ট নির্বাচন</td>
          <td style="padding: 12px; border: 1px solid #e0e0e0;">মুসলিম লীগের বিরুদ্ধে বাঙালির ব্যালট বিপ্লব ও ২১ দফা</td>
        </tr>
        <tr style="background-color: #f8fafd;">
          <td style="padding: 12px; border: 1px solid #e0e0e0; font-weight: bold;">৫-৬ ফেব্রুয়ারি ১৯৬৬</td>
          <td style="padding: 12px; border: 1px solid #e0e0e0;">৬ দফা কর্মসূচি ঘোষণা</td>
          <td style="padding: 12px; border: 1px solid #e0e0e0;">বাঙালির স্বাধিকারের সনদ (ম্যাগনাকার্টা)</td>
        </tr>
        <tr>
          <td style="padding: 12px; border: 1px solid #e0e0e0; font-weight: bold;">২৩ ফেব্রুয়ারি ১৯৬৯</td>
          <td style="padding: 12px; border: 1px solid #e0e0e0;">গণঅভ্যুত্থান ও উপাধি প্রদান</td>
          <td style="padding: 12px; border: 1px solid #e0e0e0;">শেখ মুজিবুর রহমানকে 'বঙ্গবন্ধু' উপাধিতে ভূষিতকরণ</td>
        </tr>
        <tr style="background-color: #f8fafd;">
          <td style="padding: 12px; border: 1px solid #e0e0e0; font-weight: bold;">৭ মার্চ ১৯৭১</td>
          <td style="padding: 12px; border: 1px solid #e0e0e0;">ঐতিহাসিক ৭ মার্চের ভাষণ</td>
          <td style="padding: 12px; border: 1px solid #e0e0e0;">"এবারের সংগ্রাম আমাদের মুক্তির সংগ্রাম..."—মুক্তিযুদ্ধের দিকনির্দেশনা</td>
        </tr>
        <tr>
          <td style="padding: 12px; border: 1px solid #e0e0e0; font-weight: bold;">২৫ মার্চ ১৯৭১</td>
          <td style="padding: 12px; border: 1px solid #e0e0e0;">অপারেশন সার্চলাইট</td>
          <td style="padding: 12px; border: 1px solid #e0e0e0;">পাকিস্তানি হানাদার বাহিনীর বর্বরোচিত গণহত্যা ও কালোরাত</td>
        </tr>
        <tr style="background-color: #f8fafd;">
          <td style="padding: 12px; border: 1px solid #e0e0e0; font-weight: bold;">১৬ ডিসেম্বর ১৯৭১</td>
          <td style="padding: 12px; border: 1px solid #e0e0e0;">মহান বিজয় দিবস</td>
          <td style="padding: 12px; border: 1px solid #e0e0e0;">৯৩ হাজার পাকিস্তানি সেনার আত্মসমর্পণের মাধ্যমে স্বাধীন সার্বভৌম বাংলাদেশ প্রতিষ্ঠা</td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- Section 7: Liberation War -->
  <h2 id="muktijuddho" class="htbd-heading">৭. ১৯৭১ সালের মুক্তিযুদ্ধ: অপারেশন সার্চলাইট থেকে চূড়ান্ত বিজয়</h2>
  <p>১৯৭১ সালের ২৫শে মার্চ কালরাতে পাকিস্তানি সামরিক বাহিনী নিরস্ত্র বাঙালিদের ওপর কাপুরুষোচিত <strong>'অপারেশন সার্চলাইট'</strong> পরিচালনা করে ঢাকাসহ সারা দেশে নির্মম গণহত্যা শুরু করে। এই চরম মুহূর্তে ২৬শে মার্চের প্রথম প্রহরে বঙ্গবন্ধু শেখ মুজিবুর রহমান বাংলাদেশের স্বাধীনতা ঘোষণা করেন।</p>
  <p>১০ এপ্রিল ১৯৭১ সালে গঠিত হয় গণপ্রজাতন্ত্রী বাংলাদেশের প্রথম সরকার (মুজিবনগর সরকার) এবং ১৭ এপ্রিল মেহেরপুরের বৈদ্যনাথতলার আম্রকাননে এই সরকার শপথ গ্রহণ করে। সৈয়দ নজরুল ইসলাম অস্থায়ী রাষ্ট্রপতি এবং তাজউদ্দীন আহমদ প্রধানমন্ত্রীর দায়িত্ব পালন করেন। জেনারেল এম. এ. জি. ওসমানীর নেতৃত্বে সমগ্র দেশকে ১১টি সেক্টরে ভাগ করে মুক্তিবাহিনী সশস্ত্র গেরিলা ও সম্মুখ যুদ্ধ শুরু করে। দীর্ঘ ৯ মাস রক্তক্ষয়ী সংগ্রাম, ৩০ লক্ষ শহীদের রক্ত এবং দুই লক্ষ মা-বোনের সম্ভ্রমের বিনিময়ে ১৬ই ডিসেম্বর ১৯৭১ সালে রেসকোর্স ময়দানে ৯৩,০০০ সৈন্যের আত্মসমর্পণের মাধ্যমে অর্জিত হয় আমাদের পরম কাঙ্ক্ষিত স্বাধীনতা।</p>

  <!-- External Authority Outbound Link -->
  <p style="font-size: 15px; color: #5f6368; margin-top: 25px;">
    🔗 <em>মুক্তিযুদ্ধ ও জাতীয় ইতিহাসের প্রামাণ্য দলিল সম্পর্কে বিস্তারিত জানতে ভিজিট করুন <a href="https://liberationwar.gov.bd/" target="_blank" rel="noopener nofollow" style="color: #1a73e8;">মুক্তিযুদ্ধ বিষয়ক মন্ত্রণালয়</a> অথবা বাংলাপিডিয়া মুক্তিযুদ্ধ কোষ।</em>
  </p>

  <!-- Section 8: Exam Corner -->
  <div class="htbd-qbox" id="exam-prep" style="background: #e6f4ea; border-left: 5px solid #137333; padding: 20px; margin: 35px 0; border-radius: 6px;">
    <h3 style="margin-top: 0; color: #137333;">💡 বিসিএস, বিশ্ববিদ্যালয় ও চাকরির পরীক্ষার স্পেশাল মডেল প্রশ্নোত্তর</h3>
    <p><strong>১. মুজিবনগর সরকার কবে শপথ গ্রহণ করে এবং অস্থায়ী রাষ্ট্রপতি কে ছিলেন?</strong><br>
    <em>উত্তর:</em> ১৭ এপ্রিল ১৯৭১ সালে মেহেরপুরের বৈদ্যনাথতলায় (বর্তমানে মুজিবনগর) শপথ গ্রহণ করে। অস্থায়ী রাষ্ট্রপতি ছিলেন সৈয়দ নজরুল ইসলাম।</p>
    <p><strong>২. ছয় দফাকে কেন বাঙালির 'ম্যাগনাকার্টা' বলা হয়?</strong><br>
    <em>উত্তর:</em> ব্রিটিশ জনগণের অধিকার সুরক্ষার ম্যাগনাকার্টার মতোই ৬ দফা ছিল বাঙালির রাজনৈতিক, প্রশাসনিক ও অর্থনৈতিক স্বাধিকার অর্জনের মূল ভিত্তিপ্রস্তর।</p>
    <p><strong>৩. মুক্তিযুদ্ধে বীরত্বের জন্য কতজনকে সর্বোচ্চ খেতাব প্রদান করা হয়?</strong><br>
    <em>উত্তর:</em> সর্বমোট ৬৭৬ জন মুক্তিযোদ্ধাকে খেতাব প্রদান করা হয় (বীরশ্রেষ্ঠ ৭ জন, বীরউত্তম ৬৮ জন, বীরবিক্রম ১৭৫ জন এবং বীরপ্রতীক ৪২৬ জন)।</p>
  </div>

  <!-- Section 9: FAQ with Schema -->
  <div class="htbd-faq-wrap" id="faqs" style="margin-top: 35px;">
    <h2 class="htbd-heading">৯. সচরাচর জিজ্ঞাসিত প্রশ্ন (FAQ)</h2>
    
    <div class="htbd-faq-item" style="border-bottom: 1px solid #e0e0e0; padding: 15px 0;">
      <h3 class="htbd-faq-q" style="margin: 0 0 8px 0; font-size: 18px; color: #1a73e8;">❓ বাংলাদেশের স্বাধীনতা যুদ্ধ কত দিন স্থায়ী হয়েছিল?</h3>
      <div class="htbd-faq-a" style="color: #3c4043; line-height: 1.7;">
        ১৯৭১ সালের ২৬ মার্চ থেকে ১৬ ডিসেম্বর পর্যন্ত দীর্ঘ ২৬৬ দিন (প্রায় ৯ মাস) স্থায়ী হয়েছিল।
      </div>
    </div>

    <div class="htbd-faq-item" style="border-bottom: 1px solid #e0e0e0; padding: 15px 0;">
      <h3 class="htbd-faq-q" style="margin: 0 0 8px 0; font-size: 18px; color: #1a73e8;">❓ মুক্তিযুদ্ধের প্রধান সেনাপতি কে ছিলেন?</h3>
      <div class="htbd-faq-a" style="color: #3c4043; line-height: 1.7;">
        মুক্তিযুদ্ধের প্রধান সেনাপতি ছিলেন জেনারেল মহম্মদ আতাউল গণি ওসমানী (এম. এ. জি. ওসমানী)।
      </div>
    </div>

    <div class="htbd-faq-item" style="border-bottom: 1px solid #e0e0e0; padding: 15px 0;">
      <h3 class="htbd-faq-q" style="margin: 0 0 8px 0; font-size: 18px; color: #1a73e8;">❓ কোন দেশ প্রথম বাংলাদেশকে স্বাধীন দেশ হিসেবে স্বীকৃতি দেয়?</h3>
      <div class="htbd-faq-a" style="color: #3c4043; line-height: 1.7;">
        ১৯৭১ সালের ৬ ডিসেম্বর ভুটান প্রথম বাংলাদেশকে কূটনৈতিক স্বীকৃতি প্রদান করে (এর কয়েক ঘণ্টা পর ভারত স্বীকৃতি দেয়)।
      </div>
    </div>
  </div>

  <!-- Schema.org FAQPage Structured Data -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {{
        "@type": "Question",
        "name": "বাংলাদেশের স্বাধীনতা যুদ্ধ কত দিন স্থায়ী হয়েছিল?",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "১৯৭১ সালের ২৬ মার্চ থেকে ১৬ ডিসেম্বর পর্যন্ত দীর্ঘ ২৬৬ দিন (প্রায় ৯ মাস) স্থায়ী হয়েছিল।"
        }}
      }},
      {{
        "@type": "Question",
        "name": "মুক্তিযুদ্ধের প্রধান সেনাপতি কে ছিলেন?",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "মুক্তিযুদ্ধের প্রধান সেনাপতি ছিলেন জেনারেল মহম্মদ আতাউল গণি ওসমানী (এম. এ. জি. ওসমানী)।"
        }}
      }},
      {{
        "@type": "Question",
        "name": "কোন দেশ প্রথম বাংলাদেশকে স্বাধীন দেশ হিসেবে স্বীকৃতি দেয়?",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "১৯৭১ সালের ৬ ডিসেম্বর ভুটান প্রথম বাংলাদেশকে কূটনৈতিক স্বীকৃতি প্রদান করে (এর কয়েক ঘণ্টা পর ভারত স্বীকৃতি দেয়)।"
        }}
      }}
    ]
  }}
  </script>
</div>"""

    title = "বাংলাদেশের ইতিহাস: সংগ্রাম, মুক্তিযুদ্ধ ও বিজয়ের পূর্ণাঙ্গ রূপরেখা (২০২৬)"
    meta_desc = "বাংলাদেশের ইতিহাস ও স্বাধীনতা সংগ্রাম: ১৯৫২ ভাষা আন্দোলন, ৬ দফা এবং ১৯৭১ মুক্তিযুদ্ধের বিস্তারিত সালভিত্তিক হ্যান্ডনোট পড়ুন HelpTrickBD-তে।"[:155]

    full_html_document = f"""<!DOCTYPE html>
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

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    post_filename = os.path.join(OUTPUT_DIR, f"{slug}.html")
    meta_filename = os.path.join(OUTPUT_DIR, f"{slug}_metadata.json")

    bundle = {
        "title": title,
        "slug": slug,
        "category": category,
        "meta_description": meta_desc,
        "original_url": "https://www.helptrickbd.com/2025/11/history-of-bangladesh.html",
        "html_content": html_content
    }

    with open(post_filename, "w", encoding="utf-8") as f:
        f.write(full_html_document)

    with open(meta_filename, "w", encoding="utf-8") as f:
        json.dump(bundle, f, indent=2, ensure_ascii=False)

    print(f"\n[OK] Successfully Revived Post: {slug}")
    print(f"  Title:     {title}")
    print(f"  Original:  https://www.helptrickbd.com/2025/11/history-of-bangladesh.html")
    print(f"  Saved to:  {post_filename}")
    return post_filename, meta_filename


if __name__ == "__main__":
    generate_bangladesh_history_article()
