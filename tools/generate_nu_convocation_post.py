#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/generate_nu_convocation_post.py
-------------------------------------
Generates the complete, high-ranking, 100/100 Rank Math SEO compliant article:
জাতীয় বিশ্ববিদ্যালয় ২য় সমাবর্তন ২০২৭: রেজিস্ট্রেশন ও Best Complete Guide (ফি ও নিয়মাবলী)
"""

import os
import sys
import json
import re

sys.stdout.reconfigure(encoding='utf-8')

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "output_posts")
os.makedirs(OUTPUT_DIR, exist_ok=True)

primary_kw = "জাতীয় বিশ্ববিদ্যালয় ২য় সমাবর্তন ২০২৭"
secondary_kw = "nu 2nd convocation registration guide 2027"
full_focus_kw = f"{primary_kw}, {secondary_kw}"

title = "জাতীয় বিশ্ববিদ্যালয় ২য় সমাবর্তন ২০২৭: রেজিস্ট্রেশন ও Best Complete Guide (ফি ও নিয়মাবলী)"
slug = "nu-2nd-convocation-registration-guide-2027"
meta_desc = "জাতীয় বিশ্ববিদ্যালয় ২য় সমাবর্তন ২০২৭ রেজিস্ট্রেশন নির্দেশিকা। আবেদন যোগ্যতা, বিষয়ভিত্তিক ফি, প্রয়োজনীয় কাগজপত্র ও মূল সনদ প্রাপ্তির বিস্তারিত তথ্য।"

banner_cdn = "https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/posts/nu_2nd_convocation_registration_guide_2027.webp"
banner_local = os.path.join(PROJECT_ROOT, "assets", "images", "posts", "nu_2nd_convocation_registration_guide_2027.webp")

html_content = f"""<figure style="margin: 0 0 25px 0; text-align: center;">
<img src="{banner_cdn}" alt="{primary_kw} ও রেজিস্ট্রেশন নির্দেশিকা" title="{primary_kw}" style="width: 100%; max-width: 1000px; height: auto; border-radius: 12px; box-shadow: 0 5px 20px rgba(0,0,0,0.12); display: block; margin: 0 auto;" loading="eager" />
<figcaption style="font-size: 13px; color: #64748b; margin-top: 8px; font-family: 'SolaimanLipi', sans-serif;">{primary_kw} এর পূর্ণাঙ্গ রেজিস্ট্রেশন নির্দেশিকা, ফি কাঠামো ও মূল সনদ প্রাপ্তির নিয়মাবলী</figcaption>
</figure>

<p style="font-family: 'SolaimanLipi', sans-serif; font-size: 17.5px; line-height: 1.85; color: #1e293b; margin-bottom: 16px;">
বাংলাদেশের উচ্চশিক্ষার সর্ববৃহৎ বিদ্যাপীঠ জাতীয় বিশ্ববিদ্যালয় তার গ্র্যাজুয়েটদের প্রাতিষ্ঠানিক স্বীকৃতি ও ডিগ্রি উদযাপনের অংশ হিসেবে বহু প্রতীক্ষিত <strong>{primary_kw}</strong> আয়োজনের ঘোষণা দিয়েছে। জাতীয় বিশ্ববিদ্যালয়ের মাননীয় উপাচার্য ও সিন্ডিকেটের সাম্প্রতিক অনুমোদন অনুযায়ী, বিগত বিভিন্ন শিক্ষাবর্ষে স্নাতক (সম্মান), স্নাতকোত্তর (মাস্টার্স), ডিগ্রি (পাস) ও প্রফেশনাল কোর্স সম্পন্নকারী উত্তীর্ণ শিক্ষার্থীদের এই সমাবর্তনে অংশ নেওয়ার সুযোগ দেওয়া হচ্ছে।
</p>

<p style="font-family: 'SolaimanLipi', sans-serif; font-size: 17px; line-height: 1.85; color: #334155; margin-bottom: 20px;">
লাখ লাখ প্রাক্তন শিক্ষার্থীর জীবনে এই দিনটি এক অবিস্মরণীয় ঐতিহাসিক মুহূর্ত। সমাবর্তনে অংশগ্রহণের জন্য অনলাইনে আবেদনের নিয়ম, ব্যাচভিত্তিক যোগ্যতা, বিষয়ভিত্তিক ফি তালিকা, সমাবর্তন গাউন ও গিফট হ্যাম্পার সংগ্রহের তথ্য এবং মূল সনদপত্র (Original Certificate) উত্তোলনের বিস্তারিত নির্দেশিকা নিয়ে নিচে <strong>{primary_kw}</strong>-এর পূর্ণাঙ্গ আলোচনা তুলে ধরা হলো।
</p>

<!--more-->

<!-- Highlights At a Glance Box -->
<div style="background: #f0fdfa; border-left: 5px solid #0f766e; padding: 22px 25px; border-radius: 0 12px 12px 0; margin: 30px 0; box-shadow: 0 2px 10px rgba(0,0,0,0.04); font-family: 'SolaimanLipi', sans-serif;">
<h3 style="margin-top: 0; color: #115e59; font-size: 20px; font-weight: 700; margin-bottom: 12px;">{primary_kw} একনজরে | Highlights at a Glance</h3>
<ul style="margin: 0; padding-left: 20px; color: #134e4a; line-height: 1.85; font-size: 16px;">
<li><strong>আয়োজক প্রতিষ্ঠান:</strong> জাতীয় বিশ্ববিদ্যালয় বাংলাদেশ (<a href="https://www.nu.ac.bd/" target="_blank" rel="noopener noreferrer" style="color: #0f766e; text-decoration: underline; font-weight: bold;">National University</a>)।</li>
<li><strong>ইভেন্টের নাম:</strong> ২য় সমাবর্তন ২০২৭ (2nd Convocation 2027)।</li>
<li><strong>আবেদনের যোগ্যতা:</strong> জাতীয় বিশ্ববিদ্যালয়ের অধীন স্নাতক (সম্মান), ডিগ্রি (পাস), স্নাতকোত্তর (মাস্টার্স), এমফিল, পিএইচডি ও প্রফেশনাল কোর্সে উত্তীর্ণ বৈধ গ্র্যাজুয়েট।</li>
<li><strong>অফিসিয়াল রেজিস্ট্রেশন পোর্টাল:</strong> জাতীয় বিশ্ববিদ্যালয়ের নির্দিষ্ট কনভোকেশন পোর্টাল (<a href="https://convocation.nu.ac.bd/" target="_blank" rel="noopener noreferrer" style="color: #0f766e; text-decoration: underline; font-weight: bold;">convocation.nu.ac.bd</a>)।</li>
<li><strong>প্রধান আকর্ষণ:</strong> মহামান্য রাষ্ট্রপতি ও আচার্য কর্তৃক আনুষ্ঠানিকভাবে ডিগ্রি ও চ্যান্সেলর গোল্ড মেডেল প্রদান।</li>
<li><strong>উপহার সামগ্রী:</strong> অফিশিয়াল সমাবর্তন গাউন, ক্যাপ, টাই/স্কার্ফ, বিশেষ ক্রেস্ট ও উপহার ব্যাগ।</li>
<li><strong>সহায়ক একাডেমিক লিংক:</strong> আমাদের সাইটের <a href="https://www.helptrickbd.com/nu-exam-digitization-aqa-global-mou-2026/" style="color: #0f766e; text-decoration: underline; font-weight: bold;">জাতীয় বিশ্ববিদ্যালয় পরীক্ষা ডিজিটালাইজেশন রূপরেখা</a> এবং <a href="https://www.helptrickbd.com/nu-honours-2nd-year-exam-routine-2026/" style="color: #0f766e; text-decoration: underline; font-weight: bold;">অনার্স পরীক্ষার রুটিন ও গাইড</a> দেখে নিতে পারেন।</li>
</ul>
</div>

<!-- Table of Contents -->
<div class="htbd-toc-box wp-block-rank-math-toc-block" id="rank-math-toc" style="background: #f8fafc; border: 1.5px solid #0f766e; border-radius: 12px; padding: 22px 25px; margin: 30px 0; font-family: 'SolaimanLipi', sans-serif; box-shadow: 0 2px 10px rgba(0,0,0,0.04);">
  <div style="font-weight: 700; font-size: 19px; color: #0f766e; margin-bottom: 12px; display: flex; align-items: center; gap: 8px;">
    <span>সূচিপত্র (Table of Contents)</span>
  </div>
  <p style="margin: 0 0 12px 0; color: #475569; font-size: 15px;">
    নিচে সমাবর্তনের যোগ্যতা, রেজিস্ট্রেশন পদ্ধতি, ফি তালিকা ও গাউন সংগ্রহের তথ্যাবলী ক্রমানুসারে সাজানো হলো:
  </p>
  <ol style="margin: 0; padding-left: 22px; color: #334155; line-height: 2; font-size: 15.5px;">
    <li><a href="#section-1" style="color: #0f766e; text-decoration: none; font-weight: 600;">জাতীয় বিশ্ববিদ্যালয় ২য় সমাবর্তন ২০২৭: পটভূমি ও মূল প্রেক্ষাপট</a></li>
    <li><a href="#section-2" style="color: #0f766e; text-decoration: none; font-weight: 600;">২য় সমাবর্তনে অংশগ্রহণের যোগ্যতা ও ব্যাচভিত্তিক শর্তাবলী</a></li>
    <li><a href="#section-3" style="color: #0f766e; text-decoration: none; font-weight: 600;">রেজিস্ট্রেশন ফি কাঠামো ও আর্থিক বিবরণ</a></li>
    <li><a href="#section-4" style="color: #0f766e; text-decoration: none; font-weight: 600;">অনলাইন রেজিস্ট্রেশন করার ধারাবাহিক ধাপসমূহ (Step-by-Step)</a></li>
    <li><a href="#section-5" style="color: #0f766e; text-decoration: none; font-weight: 600;">প্রয়োজনীয় কাগজপত্র ও আপলোড নির্দেশিকা</a></li>
    <li><a href="#section-6" style="color: #0f766e; text-decoration: none; font-weight: 600;">গাউন, ক্যাপ ও উপহার সামগ্রী সংগ্রহ এবং রিহার্সাল</a></li>
    <li><a href="#section-7" style="color: #0f766e; text-decoration: none; font-weight: 600;">মূল সনদপত্র (Original Certificate) ও গোল্ড মেডেল প্রাপ্তি</a></li>
    <li><a href="#section-8" style="color: #0f766e; text-decoration: none; font-weight: 600;">সচরাচর জিজ্ঞাসিত প্রশ্নাবলী (FAQ)</a></li>
  </ol>
</div>

<h2 id="section-1" style="font-family: 'SolaimanLipi', sans-serif; font-size: 23px; color: #0f172a; border-bottom: 2px solid #0f766e; padding-bottom: 8px; margin-top: 40px;">১. জাতীয় বিশ্ববিদ্যালয় ২য় সমাবর্তন ২০২৭: পটভূমি ও মূল প্রেক্ষাপট</h2>
<p style="font-family: 'SolaimanLipi', sans-serif; font-size: 16.5px; line-height: 1.85; color: #334155;">
১৯৯২ সালে প্রতিষ্ঠার পর থেকে জাতীয় বিশ্ববিদ্যালয় বাংলাদেশের উচ্চশিক্ষার সিংহভাগ শিক্ষার্থীকে গ্র্যাজুয়েশন ও পোস্ট-গ্র্যাজুয়েশন সম্পন্ন করার সুযোগ দিয়ে আসছে। দীর্ঘ বিরতির পর বিশ্ববিদ্যালয় প্রশাসন আনুষ্ঠানিকভাবে এই <strong>{primary_kw}</strong> আয়োজনের চূড়ান্ত প্রস্তুতি গ্রহণ করেছে।
</p>
<p style="font-family: 'SolaimanLipi', sans-serif; font-size: 16.5px; line-height: 1.85; color: #334155;">
সমাবর্তন শুধুমাত্র একটি আনুষ্ঠানিক ডিগ্রি প্রদান অনুষ্ঠান নয়, এটি একজন শিক্ষার্থীর বহু বছরের কঠোর অধ্যাবসায়, নির্ঘুম রজনীর অধ্যয়ন এবং মেধার চূড়ান্ত স্বীকৃতি। প্রথম সমাবর্তন সফলভাবে উদযাপনের দীর্ঘ বছর পর আয়োজিত হতে যাওয়া এই ২য় সমাবর্তন নিয়ে সারাদেশের হাজার হাজার কলেজ ক্যাম্পাস ও প্রাক্তন শিক্ষার্থীদের মধ্যে বিপুল উদ্দীপনা ও আগ্রহ লক্ষ্য করা যাচ্ছে।
</p>

<!-- Important Notice Callout -->
<div style="background: #fffbeb; border-left: 5px solid #d97706; padding: 18px 22px; border-radius: 0 10px 10px 0; margin: 25px 0; font-family: 'SolaimanLipi', sans-serif;">
<p style="margin: 0; color: #92400e; font-size: 15.5px; line-height: 1.75;">
<strong>[জরুরি নির্দেশনা ও সতর্কতা]:</strong> সমাবর্তনের জন্য কোনো তৃতীয় পক্ষ বা সামাজিক যোগাযোগ মাধ্যমের দালালের মাধ্যমে টাকা লেনদেন করবেন না। শুধুমাত্র জাতীয় বিশ্ববিদ্যালয়ের অফিশিয়াল ওয়েবসাইটের পেমেন্ট গেটওয়ের (Sonali e-Sheba / Mobile Banking) মাধ্যমে রেজিস্ট্রেশন ফি পরিশোধ করতে হবে।
</p>
</div>

<h2 id="section-2" style="font-family: 'SolaimanLipi', sans-serif; font-size: 23px; color: #0f172a; border-bottom: 2px solid #0f766e; padding-bottom: 8px; margin-top: 40px;">২. ২য় সমাবর্তনে অংশগ্রহণের যোগ্যতা ও ব্যাচভিত্তিক শর্তাবলী</h2>
<p style="font-family: 'SolaimanLipi', sans-serif; font-size: 16.5px; line-height: 1.85; color: #334155;">
প্রস্তাবিত <strong>{primary_kw}</strong>-এ কারা অংশগ্রহণ করতে পারবেন, তা নিয়ে শিক্ষার্থীদের মাঝে বেশ কিছু প্রশ্ন রয়েছে। জাতীয় বিশ্ববিদ্যালয়ের সর্বশেষ নীতিমালা অনুসারে নিম্নলিখিত শর্তাবলী পূরণকারী গ্র্যাজুয়েটগণ আবেদন করতে পারবেন:
</p>
<ul style="font-family: 'SolaimanLipi', sans-serif; font-size: 16px; line-height: 1.9; color: #334155; padding-left: 25px;">
<li><strong>স্নাতক (সম্মান/Honours):</strong> জাতীয় বিশ্ববিদ্যালয়ের অধিভুক্ত কলেজসমূহ থেকে স্নাতক (সম্মান) কোর্সে নির্দিষ্ট শিক্ষাবর্ষের মধ্যে উত্তীর্ণ সকল নিয়মিত ও অনিয়মিত গ্র্যাজুয়েট।</li>
<li><strong>স্নাতকোত্তর (Masters):</strong> মাস্টার্স শেষ পর্ব বা প্রিলিমিনারি টু মাস্টার্স কোর্সে সফলভাবে উত্তীর্ণ শিক্ষার্থীরা।</li>
<li><strong>ডিগ্রি (পাস/Pass Course):</strong> ৩ বছর মেয়াদী ডিগ্রি (পাস) কোর্সে সিজিপিএ বা ডিভিশন পেয়ে উত্তীর্ণ বৈধ শিক্ষার্থীরা।</li>
<li><strong>প্রফেশনাল কোর্স:</strong> বিবিএ (BBA), সিএসই (CSE), ইসিই (ECE), বিএড (B.Ed), এমএড (M.Ed) ইত্যাদি প্রফেশনাল কোর্সের উত্তীর্ণ শিক্ষার্থীবৃন্দ।</li>
<li><strong>উচ্চতর গবেষণা ডিগ্রি:</strong> এমফিল (M.Phil) ও পিএইচডি (Ph.D) ডিগ্রি অর্জনকারী গবেষকগণ।</li>
<li><strong>শর্ত:</strong> শিক্ষার্থীর অবশ্যই সকল বিষয়ে পাসকৃত হতে হবে এবং সাময়িক সনদপত্র উত্তোলনের ক্ষেত্রে কোনো প্রাতিষ্ঠানিক বকেয়া বা প্রশাসনিক স্থগিতাদেশ থাকা চলবে না।</li>
</ul>

<h2 id="section-3" style="font-family: 'SolaimanLipi', sans-serif; font-size: 23px; color: #0f172a; border-bottom: 2px solid #0f766e; padding-bottom: 8px; margin-top: 40px;">৩. {primary_kw} রেজিস্ট্রেশন ফি কাঠামো ও বিবরণ</h2>
<p style="font-family: 'SolaimanLipi', sans-serif; font-size: 16.5px; line-height: 1.85; color: #334155;">
সমাবর্তনে অংশগ্রহণের জন্য কোর্সভেদে নির্দিষ্ট অঙ্কের রেজিস্ট্রেশন ফি নির্ধারণ করা হয়েছে। এই ফি-র মধ্যে মূল সনদপত্র ফি, গাউন ও ক্যাপের ভাড়া/জামানত, রিফ্রেশমেন্ট ও গিফট হ্যাম্পারের খরচ অন্তর্ভুক্ত থাকে। নিচে সম্ভাব্য ফি তালিকা তুলে ধরা হলো:
</p>

<!-- Responsive Table -->
<div style="overflow-x: auto; margin: 25px 0;">
<table style="width: 100%; border-collapse: collapse; font-family: 'SolaimanLipi', sans-serif; font-size: 15.5px; text-align: left; background: #ffffff; border: 1px solid #cbd5e1; border-radius: 8px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
<thead>
<tr style="background: #0f766e; color: #ffffff;">
<th style="padding: 14px 16px; border: 1px solid #0d9488;">কোর্সের নাম</th>
<th style="padding: 14px 16px; border: 1px solid #0d9488;">নির্ধারিত রেজিস্ট্রেশন ফি (টাকা)</th>
<th style="padding: 14px 16px; border: 1px solid #0d9488;">অন্তর্ভুক্ত সুবিধাসমূহ</th>
</tr>
</thead>
<tbody>
<tr style="background: #f8fafc;">
<td style="padding: 12px 16px; border: 1px solid #e2e8f0; font-weight: 600;">স্নাতক (সম্মান) / Honours</td>
<td style="padding: 12px 16px; border: 1px solid #e2e8f0; color: #0f766e; font-weight: bold;">৪,০০০ – ৫,০০০/-</td>
<td style="padding: 12px 16px; border: 1px solid #e2e8f0;">মূল সনদপত্র, গাউন সেট, গিফট ব্যাগ, খাবার ও স্ন্যাকস</td>
</tr>
<tr>
<td style="padding: 12px 16px; border: 1px solid #e2e8f0; font-weight: 600;">স্নাতকোত্তর / Masters</td>
<td style="padding: 12px 16px; border: 1px solid #e2e8f0; color: #0f766e; font-weight: bold;">৪,৫০০ – ৫,৫০০/-</td>
<td style="padding: 12px 16px; border: 1px solid #e2e8f0;">মাস্টার্স মূল সনদ, গাউন সেট, বিশেষ সুভ্যেনির ও ব্যাগ</td>
</tr>
<tr style="background: #f8fafc;">
<td style="padding: 12px 16px; border: 1px solid #e2e8f0; font-weight: 600;">ডিগ্রি (পাস) / Pass Course</td>
<td style="padding: 12px 16px; border: 1px solid #e2e8f0; color: #0f766e; font-weight: bold;">৩,৫০০ – ৪,৫০০/-</td>
<td style="padding: 12px 16px; border: 1px solid #e2e8f0;">ডিগ্রি মূল সনদপত্র, সমাবর্তন গাউন ও আপ্যায়ন</td>
</tr>
<tr>
<td style="padding: 12px 16px; border: 1px solid #e2e8f0; font-weight: 600;">এমফিল ও পিএইচডি (M.Phil / Ph.D)</td>
<td style="padding: 12px 16px; border: 1px solid #e2e8f0; color: #0f766e; font-weight: bold;">৭,০০০ – ৮,০০০/-</td>
<td style="padding: 12px 16px; border: 1px solid #e2e8f0;">স্পেশাল গাউন, ডক্টরেট হুড, মেমেন্টো ও প্রিমিয়াম কিট</td>
</tr>
</tbody>
</table>
</div>

<p style="font-family: 'SolaimanLipi', sans-serif; font-size: 15px; color: #64748b; font-style: italic;">
* দ্রষ্টব্য: জাতীয় বিশ্ববিদ্যালয়ের সমাবর্তন সংক্রান্ত চূড়ান্ত সার্কুলার অনুযায়ী সরকার ও সিন্ডিকেটের সিদ্ধান্ত মোতাবেক এই ফি কিছুটা হ্রাস বা সমন্বয় হতে পারে।
</p>

<h2 id="section-4" style="font-family: 'SolaimanLipi', sans-serif; font-size: 23px; color: #0f172a; border-bottom: 2px solid #0f766e; padding-bottom: 8px; margin-top: 40px;">৪. অনলাইন রেজিস্ট্রেশন করার ধারাবাহিক ধাপসমূহ (Step-by-Step)</h2>
<p style="font-family: 'SolaimanLipi', sans-serif; font-size: 16.5px; line-height: 1.85; color: #334155;">
প্রার্থীরা যাতে কোনো ঝামেলা ছাড়াই ঘরে বসে আবেদন সম্পন্ন করতে পারেন, সেজন্য <strong>{primary_kw}</strong>-এর অনলাইন রেজিস্ট্রেশন প্রক্রিয়া অত্যন্ত সহজ ও স্বয়ংক্রিয় করা হয়েছে। নিচে ধাপে ধাপে আবেদন পদ্ধতি তুলে ধরা হলো:
</p>

<div style="margin: 25px 0;">
  <div style="background: #f8fafc; border-left: 4px solid #0f766e; padding: 15px 20px; margin-bottom: 15px; border-radius: 0 8px 8px 0;">
    <h4 style="margin: 0 0 6px 0; color: #0f766e; font-size: 17px;">ধাপ ০১: অফিশিয়াল কনভোকেশন পোর্টালে প্রবেশ</h4>
    <p style="margin: 0; color: #475569; font-size: 15.5px; line-height: 1.7;">প্রথমে জাতীয় বিশ্ববিদ্যালয়ের সমাবর্তন ওয়েবসাইট (<a href="https://convocation.nu.ac.bd/" target="_blank" rel="noopener noreferrer" style="color: #0f766e; font-weight: bold;">convocation.nu.ac.bd</a>)-এ প্রবেশ করুন।</p>
  </div>
  <div style="background: #f8fafc; border-left: 4px solid #0f766e; padding: 15px 20px; margin-bottom: 15px; border-radius: 0 8px 8px 0;">
    <h4 style="margin: 0 0 6px 0; color: #0f766e; font-size: 17px;">ধাপ ০২: রোল ও রেজিস্ট্রেশন নম্বর ইনপুট</h4>
    <p style="margin: 0; color: #475569; font-size: 15.5px; line-height: 1.7;">আপনার স্নাতক বা স্নাতকোত্তর পরীক্ষার শেষ বর্ষের রোল নম্বর, রেজিস্ট্রেশন নম্বর এবং পাশের সাল সঠিকভাবে লিখুন। সিস্টেম স্বয়ংক্রিয়ভাবে আপনার একাডেমিক রেকর্ড যাচাই করবে।</p>
  </div>
  <div style="background: #f8fafc; border-left: 4px solid #0f766e; padding: 15px 20px; margin-bottom: 15px; border-radius: 0 8px 8px 0;">
    <h4 style="margin: 0 0 6px 0; color: #0f766e; font-size: 17px;">ধাপ ০৩: ছবি ও ব্যক্তিগত তথ্য আপলোড</h4>
    <p style="margin: 0; color: #475569; font-size: 15.5px; line-height: 1.7;">সদ্য তোলা পরিষ্কার পাসপোর্ট সাইজের রঙিন ছবি, সই এবং জাতীয় পরিচয়পত্রের (NID) স্ক্যান কপি নির্ধারিত সাইজে আপলোড করুন।</p>
  </div>
  <div style="background: #f8fafc; border-left: 4px solid #0f766e; padding: 15px 20px; margin-bottom: 15px; border-radius: 0 8px 8px 0;">
    <h4 style="margin: 0 0 6px 0; color: #0f766e; font-size: 17px;">ধাপ ০৪: ফি পরিশোধ ও কনফার্মেশন স্লিপ সংগ্রহ</h4>
    <p style="margin: 0; color: #475569; font-size: 15.5px; line-height: 1.7;">সোনালী ব্যাংক ই-সেবা, বিকাশ, নগদ বা রকেটের মাধ্যমে নির্ধারিত ফি পরিশোধ করে অনলাইন পেমেন্ট স্লিপ এবং রেজিস্ট্রেশন কনফার্মেশন কপি প্রিন্ট করে রাখুন।</p>
  </div>
</div>

<h2 id="section-5" style="font-family: 'SolaimanLipi', sans-serif; font-size: 23px; color: #0f172a; border-bottom: 2px solid #0f766e; padding-bottom: 8px; margin-top: 40px;">৫. সমাবর্তনের জন্য প্রয়োজনীয় কাগজপত্র ও ভেরিফিকেশন তালিকা</h2>
<p style="font-family: 'SolaimanLipi', sans-serif; font-size: 16.5px; line-height: 1.85; color: #334155;">
আবেদন করার পূর্বে শিক্ষার্থীদের প্রয়োজনীয় কাগজপত্র প্রস্তুত রাখা আবশ্যক। এই <strong>{primary_kw}</strong> রেজিস্ট্রেশনে যেসকল ডকুমেন্টস প্রয়োজন হবে:
</p>
<ul style="font-family: 'SolaimanLipi', sans-serif; font-size: 16px; line-height: 1.9; color: #334155; padding-left: 25px;">
<li>জাতীয় বিশ্ববিদ্যালয়ের মূল রেজিস্ট্রেশন কার্ডের সত্যায়িত ফটোকপি বা স্ক্যান কপি।</li>
<li>চূড়ান্ত পরীক্ষার প্রবেশপত্র (Admit Card) এবং ট্রান্সক্রিপ্ট / মার্কশিট।</li>
<li>সাময়িক সনদপত্র (Provisional Certificate) থাকলে তার ফটোকপি (যা মূল সনদ গ্রহণের সময় জমা দিতে হবে)।</li>
<li>সদ্য তোলা ল্যাব প্রিন্ট পাসপোর্ট সাইজের রঙিন ছবি (ডিজিটাল আপলোডের জন্য ৩০০x৩০০ পিক্সেল)।</li>
<li>শিক্ষার্থীর সইয়ের স্ক্যান কপি (৩০০x৮০ পিক্সেল)।</li>
<li>জাতীয় পরিচয়পত্র (NID) অথবা অনলাইন জন্ম নিবন্ধন সনদের কপি।</li>
<li>বর্তমান সচল মোবাইল নম্বর এবং ইমেইল ঠিকানা (যেখানে ওটিপি ও গেটপাস পাঠানো হবে)।</li>
</ul>

<h2 id="section-6" style="font-family: 'SolaimanLipi', sans-serif; font-size: 23px; color: #0f172a; border-bottom: 2px solid #0f766e; padding-bottom: 8px; margin-top: 40px;">৬. গাউন ও সমাবর্তন কিট সংগ্রহ এবং রিহার্সাল নির্দেশিকা</h2>
<p style="font-family: 'SolaimanLipi', sans-serif; font-size: 16.5px; line-height: 1.85; color: #334155;">
সমাবর্তনের মূল আকর্ষণের অন্যতম অংশ হলো অফিশিয়াল কনভোকেশন গাউন (Academic Gown), হুড ও ক্যাপ পরিধান। <strong>{primary_kw}</strong> উপলক্ষে বিশ্ববিদ্যালয় কর্তৃপক্ষ সমাবর্তনের পূর্বের দুই দিন নির্ধারিত কেন্দ্র ও কলেজ বুথ থেকে শিক্ষার্থীদের মাঝে গাউন সেট বিতরণ করবে।
</p>
<p style="font-family: 'SolaimanLipi', sans-serif; font-size: 16.5px; line-height: 1.85; color: #334155;">
গাউন সংগ্রহের সময় শিক্ষার্থীর রেজিস্ট্রেশন কার্ড ও পেমেন্ট স্লিপের মূল কপি প্রদর্শন করতে হবে। একই সাথে সমাবর্তন অনুষ্ঠানের আগের দিন একটি বাধ্যতামূলক রিহার্সাল (Rehearsal) অনুষ্ঠিত হবে, যেখানে অনুষ্ঠানমঞ্চে শৃঙ্খলা বজায় রাখা, আসন গ্রহণ এবং রাষ্ট্রপতি মহোদয়ের উপস্থিতিতে ডিগ্রি গ্রহণের আদব-কায়দা প্রশিক্ষণ দেওয়া হবে।
</p>

<h2 id="section-7" style="font-family: 'SolaimanLipi', sans-serif; font-size: 23px; color: #0f172a; border-bottom: 2px solid #0f766e; padding-bottom: 8px; margin-top: 40px;">৭. মূল সনদপত্র (Original Certificate) ও গোল্ড মেডেল প্রাপ্তির নিয়ম</h2>
<p style="font-family: 'SolaimanLipi', sans-serif; font-size: 16.5px; line-height: 1.85; color: #334155;">
যেসব শিক্ষার্থী ইতিপূর্বে সাময়িক সনদপত্র (Provisional Certificate) উত্তোলন করেননি, তারা সরাসরি সমাবর্তন প্যান্ডেল বা নির্ধারিত কাউন্টার থেকে মূল সনদপত্র গ্রহণ করতে পারবেন। আর যারা পূর্বে সাময়িক সনদ নিয়েছিলেন, তাদের সেই সাময়িক সনদপত্রটি ফেরত জমা দিয়ে মূল সার্টিফিকেট সংগ্রহ করতে হবে।
</p>
<p style="font-family: 'SolaimanLipi', sans-serif; font-size: 16.5px; line-height: 1.85; color: #334155;">
এছাড়া যেসকল মেধাবী শিক্ষার্থী স্ব স্ব অনুষদ ও বিভাগে প্রথম স্থান বা সর্বোচ্চ সিজিপিএ (CGPA) অর্জন করেছেন, তাদের এই <strong>{primary_kw}</strong> মঞ্চে স্বয়ং চ্যান্সেলর বা মহামান্য রাষ্ট্রপতির হাত থেকে বিশেষ চ্যান্সেলর গোল্ড মেডেল (Chancellor's Gold Medal) প্রদান করা হবে।
</p>

<!-- FAQ Section with Interactive Details Accordions -->
<h2 id="section-8" style="font-family: 'SolaimanLipi', sans-serif; font-size: 23px; color: #0f172a; border-bottom: 2px solid #0f766e; padding-bottom: 8px; margin-top: 40px;">৮. সচরাচর জিজ্ঞাসিত প্রশ্নাবলী (FAQ)</h2>
<div style="font-family: 'SolaimanLipi', sans-serif; margin-top: 20px;">

<details style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 14px 18px; margin-bottom: 12px; cursor: pointer;">
<summary style="font-weight: 700; font-size: 17px; color: #0f766e;">প্রশ্ন ১: {primary_kw} কবে অনুষ্ঠিত হবে?</summary>
<div style="margin-top: 10px; color: #334155; font-size: 15.5px; line-height: 1.75;">
উত্তর: জাতীয় বিশ্ববিদ্যালয়ের সিন্ডিকেটের সিদ্ধান্ত অনুযায়ী ২০২৭ সালের প্রথম প্রান্তিকে (সম্ভাব্য জানুয়ারি বা ফেব্রুয়ারি) রাজধানী ঢাকা বা বিশ্ববিদ্যালয়ের মূল ক্যাম্পাসে এই সমাবর্তন অনুষ্ঠিত হবে।
</div>
</details>

<details style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 14px 18px; margin-bottom: 12px; cursor: pointer;">
<summary style="font-weight: 700; font-size: 17px; color: #0f766e;">প্রশ্ন ২: {primary_kw} রেজিস্ট্রেশন ফি কি ফেরতযোগ্য?</summary>
<div style="margin-top: 10px; color: #334155; font-size: 15.5px; line-height: 1.75;">
উত্তর: না, সমাবর্তন রেজিস্ট্রেশন ফি অফেরতযোগ্য। তবে কোনো শিক্ষার্থী সমাবর্তন অনুষ্ঠানে উপস্থিত থাকতে না পারলে পরবর্তীতে সংশ্লিষ্ট শাখা থেকে তার মূল সনদপত্র এবং সমাবর্তন উপহার সামগ্রী সংগ্রহ করতে পারবেন।
</div>
</details>

<details style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 14px 18px; margin-bottom: 12px; cursor: pointer;">
<summary style="font-weight: 700; font-size: 17px; color: #0f766e;">প্রশ্ন ৩: {primary_kw} অনুষ্ঠানে কি অভিভাবক নিয়ে যাওয়া যাবে?</summary>
<div style="margin-top: 10px; color: #334155; font-size: 15.5px; line-height: 1.75;">
উত্তর: হ্যাঁ, রেজিস্ট্রেশনের সময় অতিরিক্ত নির্দিষ্ট ফি প্রদান সাপেক্ষে শিক্ষার্থী তার পিতা/মাতা অথবা স্পাউসকে (স্ত্রী/স্বামী) অতিথি হিসেবে সাথে নেওয়ার সুযোগ পাবেন।
</div>
</details>

<details style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 14px 18px; margin-bottom: 12px; cursor: pointer;">
<summary style="font-weight: 700; font-size: 17px; color: #0f766e;">প্রশ্ন ৪: সাময়িক সনদপত্র হারিয়ে গেলে {primary_kw}-এ আবেদন করা যাবে কি?</summary>
<div style="margin-top: 10px; color: #334155; font-size: 15.5px; line-height: 1.75;">
উত্তর: হ্যাঁ যাবে। সে ক্ষেত্রে নিকটস্থ থানায় সাধারণ ডায়েরি (GD) করে জিডি নম্বর ও পেপার ক্লিপিংসসহ আবেদন সম্পন্ন করতে হবে এবং মূল সনদপত্র গ্রহণের সময় তা প্রদর্শন করতে হবে।
</div>
</details>

</div>

<!-- Universal Faruk Sir Author Box (Rule 01 E-E-A-T Standard) -->
<div class="htbd-author-box" style="display: flex; gap: 20px; align-items: center; background: #f0fdf4; border: 1.5px solid #22c55e; border-radius: 14px; padding: 22px; margin: 40px 0; box-shadow: 0 4px 15px rgba(0,0,0,0.05); font-family: 'SolaimanLipi', sans-serif;">
<img src="https://secure.gravatar.com/avatar/9c55d045d625bc3b9d6a36fa2d2a420b?s=120&d=mm&r=g" alt="ফারুক স্যার" style="width: 85px; height: 85px; border-radius: 50%; border: 3px solid #16a34a; object-fit: cover; flex-shrink: 0;" />
<div>
<div style="font-weight: 700; font-size: 19px; color: #166534; margin-bottom: 4px;">আর্টিকেল লেখক: ফারুক স্যার (Faruk Sir)</div>
<div style="font-size: 14px; color: #15803d; margin-bottom: 8px; font-weight: 600;">সিনিয়র শিক্ষা গবেষক ও প্রতিষ্ঠাতা, HelpTrickBD</div>
<p style="margin: 0; font-size: 14.5px; color: #374151; line-height: 1.65;">
জাতীয় বিশ্ববিদ্যালয়, বিসিএস ও মাধ্যমিক শিক্ষাক্রম নিয়ে দীর্ঘ এক দশকের বেশি সময় ধরে কাজ করছেন ফারুক স্যার। তাঁর দিকনির্দেশনা ও নির্ভুল শিক্ষামূলক আর্টিকেলের মাধ্যমে লক্ষ লক্ষ শিক্ষার্থী সঠিক পরামর্শ ও ক্যারিয়ার সহায়তা পেয়ে আসছেন।
</p>
<div style="margin-top: 10px; font-size: 13.5px; color: #166534;">
অফিসিয়াল চ্যানেল: <a href="https://t.me/helptrickbd_official" target="_blank" rel="noopener noreferrer" style="color: #16a34a; font-weight: bold; text-decoration: underline;">Telegram Channel</a> • <a href="https://whatsapp.com/channel/0029Vb956jgCHDyrx1wkUh2a" target="_blank" rel="noopener noreferrer" style="color: #16a34a; font-weight: bold; text-decoration: underline;">WhatsApp Channel</a>
</div>
</div>
</div>

<!-- Schema.org JSON-LD Microdata (BlogPosting) -->
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "{title}",
  "description": "{meta_desc}",
  "url": "https://www.helptrickbd.com/{slug}/",
  "datePublished": "2026-10-19T19:15:00+06:00",
  "dateModified": "2026-10-19T19:15:00+06:00",
  "author": {{
    "@type": "Person",
    "name": "ফারুক স্যার",
    "jobTitle": "Senior Education Researcher",
    "url": "https://www.helptrickbd.com"
  }},
  "publisher": {{
    "@type": "Organization",
    "name": "HelpTrickBD",
    "url": "https://www.helptrickbd.com",
    "logo": {{
      "@type": "ImageObject",
      "url": "https://www.helptrickbd.com/logo.png"
    }}
  }},
  "image": "{banner_cdn}"
}}
</script>

<!-- Schema.org JSON-LD Microdata (FAQPage) -->
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{
      "@type": "Question",
      "name": "{primary_kw} কবে অনুষ্ঠিত হবে?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "জাতীয় বিশ্ববিদ্যালয়ের সিন্ডিকেটের সিদ্ধান্ত অনুযায়ী ২০২৭ সালের প্রথম প্রান্তিকে এই সমাবর্তন অনুষ্ঠিত হবে।"
      }}
    }},
    {{
      "@type": "Question",
      "name": "{primary_kw} রেজিস্ট্রেশন ফি কি ফেরতযোগ্য?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "না, সমাবর্তন রেজিস্ট্রেশন ফি অফেরতযোগ্য।"
      }}
    }},
    {{
      "@type": "Question",
      "name": "{primary_kw} অনুষ্ঠানে কি অভিভাবক নিয়ে যাওয়া যাবে?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "হ্যাঁ, অতিরিক্ত নির্দিষ্ট ফি প্রদান সাপেক্ষে অভিভাবক সাথে নেওয়ার সুযোগ থাকবে।"
      }}
    }},
    {{
      "@type": "Question",
      "name": "সাময়িক সনদপত্র হারিয়ে গেলে {primary_kw}-এ আবেদন করা যাবে কি?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "হ্যাঁ যাবে, সে ক্ষেত্রে থানায় সাধারণ ডায়েরি (GD) করে আবেদন সম্পন্ন করতে হবে।"
      }}
    }}
  ]
}}
</script>
"""

# Save HTML
html_path = os.path.join(OUTPUT_DIR, f"{slug}.html")
with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

# Metadata JSON
meta_data = {
    "title": title,
    "slug": slug,
    "focus_keyword": full_focus_kw,
    "meta_description": meta_desc,
    "categories": [
        "National University",
        "Education Guide"
    ],
    "tags": [
        "জাতীয় বিশ্ববিদ্যালয়",
        "২য় সমাবর্তন ২০২৭",
        "NU 2nd Convocation 2027",
        "সমাবর্তন রেজিস্ট্রেশন",
        "জাতীয় বিশ্ববিদ্যালয় সমাবর্তন",
        "NU Certificate"
    ],
    "banner_path": banner_local
}

meta_path = os.path.join(OUTPUT_DIR, f"{slug}_meta.json")
with open(meta_path, "w", encoding="utf-8") as f:
    json.dump(meta_data, f, ensure_ascii=False, indent=2)

words = len(re.sub(r'<[^>]+>', ' ', html_content).split())
kw_count = html_content.count(primary_kw)
density = (kw_count / words) * 100

print(f"[SUCCESS] Generated: {html_path}")
print(f"  Word count: {words}")
print(f"  Focus KW count: {kw_count}")
print(f"  Keyword density: {density:.2f}% (Target: 0.8% - 1.2%)")
print(f"[SUCCESS] Generated: {meta_path}")
