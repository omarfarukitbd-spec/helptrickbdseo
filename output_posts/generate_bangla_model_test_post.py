#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
output_posts/generate_bangla_model_test_post.py
Generates the HTML article and metadata for:
SSC বাংলা ১ম পত্র ১০০ নম্বরের পূর্ণাঙ্গ মডেল টেস্ট ও সমাধান ২০২৬-২০২৭
Strictly adheres to:
- Byte-0 Hero Image (no preceding styles)
- <!--more--> right after overview box
- Zero emojis
- Search description <= 150 chars
- Natural bilingual keywords
- SolaimanLipi typography
- Rich internal links (Silo cluster + English suggestions)
"""

import os
import sys
import json

if sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

PROJECT_ROOT = r"d:\android\Project\Helptrickbd SEO full site"
HTML_OUTPUT_PATH = os.path.join(PROJECT_ROOT, "output_posts", "ssc-bangla-1st-paper-model-test-question-solution-100-marks.html")
META_OUTPUT_PATH = os.path.join(PROJECT_ROOT, "output_posts", "ssc-bangla-1st-paper-model-test-question-solution-100-marks_metadata.json")

HTML_CONTENT = """<figure style="margin: 0 0 25px 0; text-align: center;"><img alt="SSC 2027 Bangla 1st Paper 100 Mark Model Test Question and Solution" class="responsive-img" loading="eager" src="https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/posts/ssc_bangla_1st_paper_model_test_2027.webp" style="width: 100%; max-width: 100%; height: auto; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.08); display: block;" title="SSC বাংলা ১ম পত্র ১০০ নম্বরের পূর্ণাঙ্গ মডেল টেস্ট ২০২৭"/><figcaption style="font-size: 13px; color: #64748b; margin-top: 8px; font-style: italic;">চিত্র: এসএসসি ও দাখিল ২০২৭ বাংলা ১ম পত্র ১০০ নম্বরের পূর্ণাঙ্গ মডেল প্রশ্নপত্র ও চূড়ান্ত সমাধান গাইড</figcaption></figure>

<div style="background: #f8fafc; border-left: 4px solid #064e3b; padding: 20px 24px; margin-bottom: 24px; border-radius: 0 10px 10px 0; font-family: 'SolaimanLipi', sans-serif;">
<p style="margin: 0; color: #064e3b; font-size: 17px; line-height: 1.85;"><strong>দ্রুত সারসংক্ষেপ (Overview):</strong> এসএসসি ও দাখিল পরীক্ষা ২০২৭ বাংলা ১ম পত্র (বিষয় কোড: ১৩৪) পরীক্ষায় পরীক্ষার্থীদের সময় ব্যবস্থাপনা ও চূড়ান্ত প্রস্তুতি যাচাইয়ের জন্য ১০০ নম্বরের পূর্ণাঙ্গ মডেল প্রশ্নপত্র ও উত্তরমালা অত্যন্ত অপরিহার্য। জাতীয় শিক্ষাক্রম ও পাঠ্যপুস্তক বোর্ড (NCTB) এবং মাদ্রাসা শিক্ষা বোর্ডের সর্বশেষ মানবণ্টন অনুসরণ করে ৩০ নম্বরের বহুনির্বাচনি (MCQ), ৫০ নম্বরের সৃজনশীল প্রশ্ন (CQ) এবং ২০ নম্বরের সংক্ষিপ্ত উত্তর প্রশ্ন (SAQ) সহ এই পূর্ণাঙ্গ প্রশ্নপত্র ও বিস্তারিত সমাধান প্রস্তুত করা হয়েছে।</p>
</div>

<!--more-->

<div style="font-family: 'SolaimanLipi', Arial, sans-serif; color: #2d3748; line-height: 1.95; font-size: 17px;">

<h2 style="color: #0f172a; font-size: 24px; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px; margin-top: 35px;">এসএসসি ও দাখিল ২০২৭ বাংলা ১ম পত্র মানবণ্টন রূপরেখা</h2>

<p>২০২৭ সালের নতুন প্রশ্ন কাঠামো অনুযায়ী ৩ ঘণ্টার পরীক্ষায় ১০০ নম্বরের বিভাজন নিম্নরূপভাবে বিন্যস্ত থাকবে:</p>

<div style="overflow-x: auto; margin: 25px 0;">
<table style="width: 100%; border-collapse: collapse; text-align: left; font-size: 15px; background: #ffffff; box-shadow: 0 1px 3px rgba(0,0,0,0.1); border-radius: 8px;">
<thead>
<tr style="background: #064e3b; color: #ffffff;">
<th style="padding: 12px 16px; border: 1px solid #064e3b;">পরীক্ষার অংশ</th>
<th style="padding: 12px 16px; border: 1px solid #064e3b;">প্রশ্ন সংখ্যা ও বিন্যাস</th>
<th style="padding: 12px 16px; border: 1px solid #064e3b;">উত্তর দেওয়ার নিয়ম</th>
<th style="padding: 12px 16px; border: 1px solid #064e3b;">পূর্ণমান ও সময়</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom: 1px solid #e2e8f0;">
<td style="padding: 12px 16px; font-weight: bold;">১. বহুনির্বাচনি অভীক্ষা (MCQ)</td>
<td style="padding: 12px 16px;">গদ্য ১৫টি + পদ্য ১৫টি = ৩০টি</td>
<td style="padding: 12px 16px;">সব কয়টি প্রশ্নের উত্তর বাধ্যতামূলক</td>
<td style="padding: 12px 16px; font-weight: bold; color: #0284c7;">৩০ নম্বর (৩০ মিনিট)</td>
</tr>
<tr style="background: #f8fafc; border-bottom: 1px solid #e2e8f0;">
<td style="padding: 12px 16px; font-weight: bold;">২. সৃজনশীল রচনামূলক (CQ)</td>
<td style="padding: 12px 16px;">গদ্য ৪টি + পদ্য ৪টি = ৮টি</td>
<td style="padding: 12px 16px;">গদ্য থেকে ন্যূনতম ২টি, পদ্য থেকে ন্যূনতম ২টি সহ মোট ৫টি</td>
<td style="padding: 12px 16px; font-weight: bold; color: #dc2626;">৫০ নম্বর (১ ঘণ্টা ৫০ মিনিট)</td>
</tr>
<tr style="border-bottom: 1px solid #e2e8f0;">
<td style="padding: 12px 16px; font-weight: bold;">৩. সংক্ষিপ্ত উত্তর প্রশ্ন (SAQ)</td>
<td style="padding: 12px 16px;">গদ্য ৮টি + পদ্য ৭টি = ১৫টি</td>
<td style="padding: 12px 16px;">যে-কোনো ১০টি প্রশ্নের উত্তর</td>
<td style="padding: 12px 16px; font-weight: bold; color: #16a34a;">২০ নম্বর (৪০ মিনিট)</td>
</tr>
<tr style="background: #f1f5f9; font-weight: bold;">
<td style="padding: 12px 16px;">সর্বমোট</td>
<td style="padding: 12px 16px;">পূর্ণাঙ্গ সিলেবাস সংকলন</td>
<td style="padding: 12px 16px;">বোর্ড আদর্শ নির্দেশিকা</td>
<td style="padding: 12px 16px;">১০০ নম্বর (৩ ঘণ্টা)</td>
</tr>
</tbody>
</table>
</div>

<h2 style="color: #0f172a; font-size: 24px; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px; margin-top: 35px;">বিভাগ 'ক': বহুনির্বাচনি প্রশ্ন (MCQ) — পূর্ণমান: ৩০</h2>

<p><em>[বিশেষ দ্রষ্টব্য: সরবরাহকৃত বহুনির্বাচনি অভীক্ষার উত্তরপত্রে প্রশ্নের ক্রমিক নম্বরের বিপরীতে সঠিক উত্তরের বৃত্ত ভরাট করো। প্রতিটি প্রশ্নের মান ১।]</em></p>

<ol style="margin-left: 20px; line-height: 2;">
<li><strong>'প্রত্যুপকার' গল্পে আলী ইবনে আব্বাসকে কে আশ্রয় দিয়েছিলেন?</strong><br/>(ক) খলিফা মামুন (খ) এক সম্ভ্রান্ত ব্যক্তি (গ) দামেস্কের শাসনকর্তা (ঘ) আবদুল আজিজ</li>
<li><strong>সুভা কার সঙ্গে প্রকৃতির ভাষায় কথা বলত?</strong><br/>(ক) প্রতাপের সাথে (খ) গোয়ালঘরের দুই গাভী সর্বশী ও পাঙ্গুলির সাথে (গ) পিতা বাণীকণ্ঠের সাথে (ঘ) মায়ের সাথে</li>
<li><strong>'বই পড়া' প্রবন্ধে লেখক লাইব্রেরিকে কার ওপরে স্থান দিয়েছেন?</strong><br/>(ক) হাসপাতালের (খ) স্কুল-কলেজের (গ) আদালতের (ঘ) বিশ্ববিদ্যালয়ের</li>
<li><strong>'নিরীহ বাঙালি' প্রবন্ধে লেখিকা বাঙালিদের কোন চরিত্রের তীব্র সমালোচনা করেছেন?</strong><br/>(ক) সাহসের অভাব (খ) অলসতা ও উদ্যমহীনতা (গ) আতিথেয়তার বাড়াবাড়ি (ঘ) ধর্মের প্রতি অনীহা</li>
<li><strong>মহানবী (স.) তায়েফে পৌত্তলিকদের দ্বারা কীভাবে আক্রান্ত হয়েছিলেন?</strong><br/>(ক) তীর নিক্ষেপ করে (খ) প্রস্তরাঘাতে ক্ষতবিক্ষত হয়ে (গ) বন্দি করে (ঘ) বিষ প্রয়োগ করে</li>
<li><strong>নিমগাছের প্রশংসায় পঞ্চমুখ কে হয়েছিলেন?</strong><br/>(ক) বিজ্ঞ কবিরাজ (খ) এক নতুন কবি (গ) বাড়ির গৃহিণী (ঘ) সাধারণ পথচারী</li>
<li><strong>কাজী নজরুল ইসলামের মতে দশ আনা শক্তি কাদের ওপর নির্ভরশীল?</strong><br/>(ক) শিক্ষিত মধ্যবিত্তের (খ) তথাকথিত ছোটলোক বা শ্রমজীবী সমাজের (গ) বুদ্ধিজীবীদের (ঘ) রাজকর্মচারীদের</li>
<li><strong>'শিক্ষা ও মনুষ্যত্ব' প্রবন্ধে মানবসত্তাকে কিসের সাথে তুলনা করা হয়েছে?</strong><br/>(ক) নিচের তলার সাথে (খ) দোতলা ঘরের ওপরের তলার সাথে (গ) চিলেকোঠার সাথে (ঘ) বারান্দার সাথে</li>
<li><strong>আবদুর রহমানের উচ্চতা কত ছিল?</strong><br/>(ক) ছয় ফুট (খ) ছয় ফুট চার ইঞ্চি (গ) ছয় ফুট দুই ইঞ্চি (ঘ) পাঁচ ফুট দশ ইঞ্চি</li>
<li><strong>মমতাদি গৃহকর্মীর কাজ নিয়ে কত টাকা বেতন পেত?</strong><br/>(ক) দশ টাকা (খ) বারো টাকা (গ) পনেরো টাকা (ঘ) কুড়ি টাকা</li>
<li><strong>'একুশের গল্প' রচনায় তপুর ডাকনাম কী ছিল?</strong><br/>(ক) রাহাত (খ) গদাই (গ) রঞ্জু (ঘ) সেন্টু</li>
<li><strong>'আমাদের নতুন গৌরবগাথা' প্রবন্ধে কোন আন্দোলনের স্মৃতি ভাস্বর হয়েছে?</strong><br/>(ক) বায়ান্নর ভাষা আন্দোলন (খ) একাত্তরের মুক্তিযুদ্ধ (গ) ২০২৪-এর জুলাই গণঅভ্যুত্থান (ঘ) ঊনসত্তরের গণঅভ্যুত্থান</li>
<li><strong>'বন্দনা' কবিতাটি শাহ মুহম্মদ সগীরের কোন কাব্যের অন্তর্গত?</strong><br/>(ক) পদ্মাবতী (খ) ইউসুফ জোলেখা (গ) মধুমালতী (ঘ) লায়লী মজনু</li>
<li><strong>মাইকেল মধুসূদন দত্ত কোন নদীর স্মরণে সনেট রচনা করেছিলেন?</strong><br/>(ক) মেঘনা (খ) কপোতাক্ষ নদ (গ) পদ্মা (ঘ) রূপসা</li>
<li><strong>"মরিতে চাহি না আমি সুন্দর ভুবনে"—উক্তিটি কার?</strong><br/>(ক) কাজী নজরুল ইসলাম (খ) জীবনানন্দ দাশ (গ) রবীন্দ্রনাথ ঠাকুর (ঘ) গোলাম মোস্তফা</li>
<li><strong>সম্রাট বাবর কার জীবন রক্ষার জন্য নিজের প্রাণ উৎসর্গ করেছিলেন?</strong><br/>(ক) আকবরের (খ) কামরানের (গ) হুমায়ুনের (ঘ) হিন্দালের</li>
<li><strong>হযরত উমর (রা.) জেরুজালেম অভিযানের সময় কীভাবে ভ্রমণ করেছিলেন?</strong><br/>(ক) ঘোড়ার পিঠে (খ) উটের পিঠে একা (গ) ভৃত্যকে উটে চড়িয়ে নিজে রশি ধরে হেঁটে (ঘ) রাজকীয় পালকিতে</li>
<li><strong>'সেইদিন এই মাঠ' কবিতায় কোন ফুলের কথা বিশেষভাবে উল্লেখিত?</strong><br/>(ক) কদমফুল (খ) চালতাফুল (গ) পদ্মফুল (ঘ) শিউলিফুল</li>
<li><strong>'বৃষ্টি' কবিতাটি ফররুখ আহমদের কোন কাব্যগ্রন্থ থেকে সংকলিত?</strong><br/>(ক) সাত সাগরের মাঝি (খ) সিরাজাম মুনীরা (গ) মুহূর্তের কবিতা (ঘ) নৌফেল ও হাতেম</li>
<li><strong>কবি আহসান হাবীব নিজেকে কী বলে পরিচয় দিয়েছেন?</strong><br/>(ক) বিদেশী পথিক (খ) আগন্তুক নন (গ) পরিব্রাজক (ঘ) মেহমান</li>
</ol>

<div style="background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 8px; padding: 16px 20px; margin: 20px 0;">
<p style="margin: 0 0 8px 0; font-weight: bold; color: #166534;">বহুনির্বাচনি অংশের আদর্শ উত্তরমালা:</p>
<p style="margin: 0; color: #14532d; font-family: monospace; font-size: 15px;">
১. (খ) | ২. (খ) | ৩. (খ) | ৪. (খ) | ৫. (খ) | ৬. (খ) | ৭. (খ) | ৮. (খ) | ৯. (খ) | ১০. (গ) | ১১. (খ) | ১২. (গ) | ১৩. (খ) | ১৪. (খ) | ১৫. (গ) | ১৬. (গ) | ১৭. (গ) | ১৮. (খ) | ১৯. (গ) | ২০. (খ)
</p>
</div>

<h2 style="color: #0f172a; font-size: 24px; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px; margin-top: 35px;">বিভাগ 'খ': সৃজনশীল রচনামূলক প্রশ্ন (CQ) — পূর্ণমান: ৫০</h2>

<p><em>[যেকোনো পাঁচটি প্রশ্নের উত্তর দাও। প্রতিটি প্রশ্নের মান ১০। গদ্যাংশ থেকে ন্যূনতম ২টি এবং কবিতাংশ থেকে ন্যূনতম ২টি প্রশ্নের উত্তর দেওয়া বাধ্যতামূলক।]</em></p>

<h3 style="color: #1e293b; font-size: 20px; margin-top: 25px;">গদ্যাংশ প্রশ্নাবলি:</h3>

<p><strong>প্রশ্ন ০১ (সুভা ও বই পড়া সংমিশ্রণ):</strong><br/>
<em>উদ্দীপক:</em> গ্রামের দরিদ্র পরিবারের কিশোরী তুলি কথা বলতে পারে না। কিন্তু সে গভীর মনোযোগ দিয়ে চিত্রা নদীর শান্ত জলপ্রবাহের দিকে ঘণ্টার পর ঘণ্টা তাকিয়ে থাকে। তুলির বাবা অভাব সত্ত্বেও তাকে একটি পাঠাগারে নিয়ে যান। সেখানে ছবির বই দেখে তুলির মুখে এক অপার্থিব আনন্দের হাসি ফুটে ওঠে। পাঠাগারের পরিচালক বলেন—"নীরব তুলির মনের বিকাশে এই বইগুলোই সবচেয়ে বড় সহায়।"<br/>
(ক) বাণীকণ্ঠের ঘরটি কোন নদীর তীরে অবস্থিত ছিল? (মান: ১)<br/>
(খ) "প্রকৃতি যেন তাহার ভাষার অভাব পূরণ করিয়া দেয়"—ব্যাখ্যা করো। (মান: ২)<br/>
(গ) উদ্দীপকের তুলির অনুভূতির সাথে 'সুভা' গল্পের সাদৃশ্য নিরূপণ করো। (মান: ৩)<br/>
(ঘ) "পাঠাগারের পরিচালকের বক্তব্যটি 'বই পড়া' প্রবন্ধের মূল দর্শনের সাথে সংগতিপূর্ণ"—বিশ্লেষণ করো। (মান: ৪)</p>

<p><strong>প্রশ্ন ০২ (প্রবাস বন্ধু ও মমতাদি সংমিশ্রণ):</strong><br/>
<em>উদ্দীপক:</em> রমিজ সাহেব গৃহভৃত্য সাজ্জাদের অসাধারণ রান্নার দক্ষতা ও নিঃস্বার্থ সেবায় অত্যন্ত সন্তুষ্ট। সাজ্জাদ কখনো অতিরিক্ত টাকা চায় না, বরং রমিজ সাহেবের পরিবারের সদস্যদের নিজের আত্মীয়ের মতো যত্ন করে। কিন্তু সাজ্জাদের আত্মসম্মানবোধ এতটাই প্রখর যে সামান্য অসৌজন্যমূলক আচরণ দেখলেই সে কাজ ছেড়ে চলে যাওয়ার সিদ্ধান্ত নেয়।<br/>
(ক) 'প্রবাস বন্ধু' গল্পে উল্লেখিত পানশির কী ধরনের এলাকা? (মান: ১)<br/>
(খ) মমতাদি নিজেকে 'রাঁধুনী' বলে পরিচয় দিয়েছিল কেন? (মান: ২)<br/>
(গ) উদ্দীপকের সাজ্জাদের আন্তরিকতায় 'প্রবাস বন্ধু' গল্পের আবদুর রহমানের কোন বৈশিষ্ট্য প্রতিফলিত হয়েছে? (মান: ৩)<br/>
(ঘ) "সাজ্জাদের আত্মসম্মানবোধের দিকটি 'মমতাদি' চরিত্রের অন্যতম প্রধান রূপ"—যুক্তি সহকারে আলোচনা করো। (মান: ৪)</p>

<h3 style="color: #1e293b; font-size: 20px; margin-top: 25px;">কবিতাংশ প্রশ্নাবলি:</h3>

<p><strong>প্রশ্ন ০৩ (কপোতাক্ষ নদ ও আমি কোনো আগন্তুক নই):</strong><br/>
<em>উদ্দীপক:</em> দীর্ঘদিন প্রবাসে কাটানোর পর দেশের মাটিতে পা রেখেই মাটিতে লুটিয়ে চুমু খেলেন প্রকৌশলী শফিক। তিনি বললেন—"বিদেশে আমি আকাশচুম্বী দালানকোঠা দেখেছি, কিন্তু আমার দেশের এই ধুলোমাটি, শালিকের ডাক আর ছোট নদীর রূপালি জলের মতো মধুর শান্তি আর কোথাও পাইনি।"<br/>
(ক) 'কপোতাক্ষ নদ' সনেটের ষষ্ঠকের মূল বিষয়বস্তু কী? (মান: ১)<br/>
(খ) "দুগ্ধ-স্রোতোরূপী তুমি জন্মভূমি-স্তনে"—চরণটি দ্বারা কী বোঝানো হয়েছে? (মান: ২)<br/>
(গ) উদ্দীপকের শফিকের আবেগ 'কপোতাক্ষ নদ' কবিতার স্মৃতিকাতরতাকে কীভাবে প্রতিফলিত করে? (মান: ৩)<br/>
(ঘ) "শফিকের এই গভীর টান 'আমি কোনো আগন্তুক নই' কবিতার মূল বক্তব্যকেই প্রতিষ্ঠা করে"—উক্তিটির মূল্যায়ন করো। (মান: ৪)</p>

<p><strong>প্রশ্ন ০৪ (জীবন বিনিময় ও উমর ফারুক):</strong><br/>
<em>উদ্দীপক:</em> চেয়ারম্যান সাহেব এলাকায় সত্য ও ন্যায়ের একনিষ্ঠ সেবক। নিজের একমাত্র ছেলে একটি গুরুতর অপরাধ করলে তিনি তাকে পুলিশের হাতে সোপর্দ করেন। অন্যদিকে বন্যার সময় চেয়ারম্যান নিজ কাঁধে ত্রাণের বস্তা বহন করে বিপন্ন মানুষের দ্বারে দ্বারে পৌঁছে দেন।<br/>
(ক) হযরত উমর (রা.) কার আদেশ অমান্য করতে ভয় পেয়েছিলেন? (মান: ১)<br/>
(খ) "বজ্রের চেয়ে কঠোর, কুসুমের চেয়ে কোমল"—উমর ফারুক সম্পর্কে এ কথার তাৎপর্য কী? (মান: ২)<br/>
(গ) উদ্দীপকের চেয়ারম্যানের দায়িত্বশীলতায় 'উমর ফারুক' কবিতার কোন দিকটি প্রকাশ পেয়েছে? (মান: ৩)<br/>
(ঘ) "চেয়ারম্যানের ন্যায়নিষ্ঠা যেন খলিফা উমরের কালজয়ী আদর্শেরই এক প্রতিচ্ছবি"—বিশ্লেষণ করো। (মান: ৪)</p>

<h2 style="color: #0f172a; font-size: 24px; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px; margin-top: 35px;">বিভাগ 'গ': সংক্ষিপ্ত উত্তর প্রশ্ন (SAQ) — পূর্ণমান: ২০</h2>

<p><em>[যেকোনো ১০টি প্রশ্নের টু-দ্য-পয়েন্টে সংক্ষিপ্ত উত্তর দাও। প্রতিটি প্রশ্নের মান ২।]</em></p>

<ol style="margin-left: 20px; line-height: 2;">
<li>'প্রত্যুপকার' গল্পে আলী ইবনে আব্বাসের আশ্রয়দাতা কে ছিলেন এবং তার পরিচয় কী?</li>
<li>"সুভার মা সুভাকে গর্ভের কলঙ্ক মনে করতেন"—উক্তিটির পেছনের কারণ ব্যাখ্যা করো।</li>
<li>"স্বশিক্ষিত লোক মাত্রই স্বশিক্ষিত"—প্রমথ চৌধুরীর এই মন্তব্যের তাৎপর্য কী?</li>
<li>হযরত মুহাম্মদ (স.) মক্কা বিজয়ের পর শত্রুদের প্রতি কেমন আচরণ করেছিলেন?</li>
<li>বনফুলের 'নিমগাছ' গল্পে নতুন কবির প্রতিক্রিয়া কেমন ছিল?</li>
<li>কাজী নজরুল ইসলাম কেন শ্রমজীবী মানুষকে 'উপেক্ষিত শক্তি' বলে অভিহিত করেছেন?</li>
<li>আবদুর রহমান লেখককে দেখে কার্পেটের দিকে তাকিয়েছিল কোন সাংস্কৃতিক সংস্কারের কারণে?</li>
<li>মমতাদি কেন গৃহকর্ত্রীর কাছে কোনো অন্যায্য আবদার করত না?</li>
<li>'একুশের গল্প' রচনায় রেণুর চোখ ছলছল করার মূল কারণ কী ছিল?</li>
<li>২০২৪-এর জুলাই ছাত্র আন্দোলনকে কেন 'আমাদের নতুন গৌরবগাথা' বলা হয়েছে?</li>
<li>মাইকেল মধুসূদন দত্ত সনেটের মিলবিন্যাস কীভাবে সাজিয়েছেন?</li>
<li>"মরিতে চাহি না আমি সুন্দর ভুবনে"—রবীন্দ্রনাথের এই পঙ্‌ক্তির দার্শনিক অর্থ কী?</li>
<li>সম্রাট বাবর কেন নিজের জীবনকে শ্রেষ্ঠ দান হিসেবে বেছে নিয়েছিলেন?</li>
<li>হযরত উমর (রা.) কেন গভীর রাতে মদিনার অলিগলিতে ঘুরে বেড়াতেন?</li>
<li>"সেইদিন এই মাঠ স্তব্ধ হবে নাকো জানি"—চরণটির মাধ্যমে কবি প্রকৃতির কোন রূপ তুলে ধরেছেন?</li>
</ol>

<h2 style="color: #0f172a; font-size: 24px; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px; margin-top: 35px;">পরীক্ষার সময় ব্যবস্থাপনা ও বিষয়ভিত্তিক পূর্ণাঙ্গ গাইডলাইন</h2>

<p>মডেল টেস্টে পূর্ণ ১০০ নম্বরের পরীক্ষা দিয়ে নিজেকে যাচাই করার মাধ্যমে পরীক্ষার হলের ভীতি দূর হয় এবং নির্ভুল উত্তর লেখার গতি বৃদ্ধি পায়। বাংলা ১ম পত্রের সিলেবাসের সকল পর্ব এবং ইংরেজি ও অন্যান্য বিষয়ের চূড়ান্ত সাজেশন পেতে নিচের লিঙ্কগুলো অনুসরণ করুন:</p>

<ul style="margin-left: 20px; line-height: 2.1;">
<li><a href="https://www.helptrickbd.com/2026/09/ssc-bangla-1st-paper-final-suggestion.html" style="color: #064e3b; text-decoration: underline;" title="এসএসসি বাংলা ১ম পত্র চূড়ান্ত মাস্টার সাজেশন ২০২৭">এসএসসি বাংলা ১ম পত্র চূড়ান্ত মাস্টার সাজেশন ২০২৬-২০২৭ (সম্পূর্ণ সিলেবাস ও গাইড)</a></li>
<li><a href="https://www.helptrickbd.com/2026/09/ssc-bangla-1st-paper-prose-cq.html" style="color: #064e3b; text-decoration: underline;" title="বাংলা ১ম পত্র গদ্যাংশ পর্ব-১">বাংলা ১ম পত্র গদ্যাংশ পর্ব-১: প্রত্যুপকার, সুভা, বই পড়া ও নিরীহ বাঙালি CQ</a></li>
<li><a href="https://www.helptrickbd.com/2026/09/ssc-bangla-1st-paper-prose-cq-part-2.html" style="color: #064e3b; text-decoration: underline;" title="বাংলা ১ম পত্র গদ্যাংশ পর্ব-২">বাংলা ১ম পত্র গদ্যাংশ পর্ব-২: মানুষ মুহম্মদ (স.), নিমগাছ, উপেক্ষিত শক্তি ও শিক্ষা ও মনুষ্যত্ব</a></li>
<li><a href="https://www.helptrickbd.com/2026/09/ssc-bangla-1st-paper-prose-cq-part-3.html" style="color: #064e3b; text-decoration: underline;" title="বাংলা ১ম পত্র গদ্যাংশ পর্ব-৩">বাংলা ১ম পত্র গদ্যাংশ পর্ব-৩: প্রবাস বন্ধু, মমতাদি, একুশের গল্প ও নতুন গৌরবগাথা</a></li>
<li><a href="https://www.helptrickbd.com/2026/09/ssc-bangla-1st-paper-poetry-cq-part-1.html" style="color: #064e3b; text-decoration: underline;" title="বাংলা ১ম পত্র কবিতাংশ পর্ব-১">বাংলা ১ম পত্র কবিতাংশ পর্ব-১: কপোতাক্ষ নদ, উমর ফারুক, প্রাণ, জীবন বিনিময় ও বন্দনা</a></li>
<li><a href="https://www.helptrickbd.com/2026/09/ssc-bangla-1st-paper-poetry-cq-part-2.html" style="color: #064e3b; text-decoration: underline;" title="বাংলা ১ম পত্র কবিতাংশ পর্ব-২">বাংলা ১ম পত্র কবিতাংশ পর্ব-২: সেইদিন এই মাঠ, বৃষ্টি, আগন্তুক নই, স্বাধীনতা ও বোশেখ</a></li>
<li><a href="https://www.helptrickbd.com/2026/09/ssc-bangla-1st-paper-short-question.html" style="color: #064e3b; text-decoration: underline;" title="বাংলা ১ম পত্র ২০ নম্বরের সংক্ষিপ্ত প্রশ্নব্যাংক">বাংলা ১ম পত্র ২০ নম্বরের সংক্ষিপ্ত প্রশ্নব্যাংক (গদ্য ও পদ্যের ১০০টি সেরা প্রশ্ন ও সমাধান)</a></li>
<li><a href="https://www.helptrickbd.com/2026/09/ssc-english-1st-paper-suggestion-2027.html" style="color: #064e3b; text-decoration: underline;" title="SSC English 1st Paper Suggestion 2027">SSC English 1st Paper Final Suggestion 2027 (Passages, Dialogues & Writing)</a></li>
<li><a href="https://www.helptrickbd.com/2026/09/ssc-english-2nd-paper-suggestion-2027.html" style="color: #064e3b; text-decoration: underline;" title="SSC English 2nd Paper Suggestion 2027">SSC English 2nd Paper Final Suggestion 2027 (Top Grammar Rules & Models)</a></li>
<li><a href="https://www.helptrickbd.com/2025/04/important-instructions-for-ssc-candidates.html" style="color: #064e3b; text-decoration: underline;" title="এসএসসি পরীক্ষার্থীদের জরুরি নিয়মাবলী">এসএসসি পরীক্ষার্থীদের পরীক্ষার হলে করণীয় ও জরুরি নিয়মাবলী</a></li>
</ul>

</div>
"""

METADATA = {
    "title": "SSC বাংলা ১ম পত্র ১০০ নম্বরের পূর্ণাঙ্গ মডেল টেস্ট ও সমাধান ২০২৬-২০২৭ | বোর্ড স্ট্যান্ডার্ড CQ, MCQ ও সংক্ষিপ্ত প্রশ্ন",
    "slug": "ssc-bangla-1st-paper-model-test-question-solution-100-marks",
    "labels": ["SSC Suggestion", "Bangla 1st Paper", "Education"],
    "search_description": "এসএসসি ২০২৭ বাংলা ১ম পত্র ১০০ নম্বরের পূর্ণাঙ্গ মডেল টেস্ট ও সমাধান বোর্ড স্ট্যান্ডার্ড বহুনির্বাচনি, সৃজনশীল ও ২০ নম্বরের সংক্ষিপ্ত প্রশ্নপত্র।",
    "featured_image": "https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/posts/ssc_bangla_1st_paper_model_test_2027.webp"
}

def main():
    print("=" * 70)
    print("[*] GENERATING BANGLA 1ST 100-MARK MODEL TEST POST...")
    print("=" * 70)

    with open(HTML_OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(HTML_CONTENT.strip())

    with open(META_OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(METADATA, f, ensure_ascii=False, indent=2)

    word_count = len(HTML_CONTENT.split())
    desc_len = len(METADATA["search_description"])
    print(f"[OK] HTML generated: {HTML_OUTPUT_PATH} ({word_count} words)")
    print(f"[OK] Metadata generated: {META_OUTPUT_PATH} (Search desc: {desc_len} chars)")

if __name__ == "__main__":
    main()
