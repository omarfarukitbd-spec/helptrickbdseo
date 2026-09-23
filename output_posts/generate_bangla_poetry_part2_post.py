#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
output_posts/generate_bangla_poetry_part2_post.py
Generates the HTML article and metadata for:
SSC বাংলা ১ম পত্র কবিতাংশ পর্ব-২ সৃজনশীল প্রশ্ন ও উত্তর ২০২৬-২০২৭
Chapters: সেইদিন এই মাঠ, বৃষ্টি, আমি কোনো আগন্তুক নই, তোমাকে পাওয়ার জন্যে হে স্বাধীনতা, বোশেখ
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
HTML_OUTPUT_PATH = os.path.join(PROJECT_ROOT, "output_posts", "ssc-bangla-1st-paper-poetry-cq-part-2.html")
META_OUTPUT_PATH = os.path.join(PROJECT_ROOT, "output_posts", "ssc-bangla-1st-paper-poetry-cq-part-2_metadata.json")

HTML_CONTENT = """<figure style="margin: 0 0 25px 0; text-align: center;"><img alt="SSC 2027 Bangla 1st Paper Poetry Part 2 CQ Suggestion" class="responsive-img" loading="eager" src="https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/posts/ssc_bangla_1st_paper_poetry_part2_2027.webp" style="width: 100%; max-width: 100%; height: auto; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.08); display: block;" title="SSC বাংলা ১ম পত্র কবিতাংশ পর্ব-২ সৃজনশীল প্রশ্ন ও উত্তর ২০২৭"/><figcaption style="font-size: 13px; color: #64748b; margin-top: 8px; font-style: italic;">চিত্র: এসএসসি ও দাখিল ২০২৭ বাংলা ১ম পত্র কবিতাংশ পর্ব-২ (সেইদিন এই মাঠ, বৃষ্টি, আগন্তুক নই, স্বাধীনতা ও বোশেখ) চূড়ান্ত সৃজনশীল গাইডলাইন</figcaption></figure>

<div style="background: #f8fafc; border-left: 4px solid #0284c7; padding: 20px 24px; margin-bottom: 24px; border-radius: 0 10px 10px 0; font-family: 'SolaimanLipi', sans-serif;">
<p style="margin: 0; color: #1e293b; font-size: 17px; line-height: 1.85;"><strong>দ্রুত সারসংক্ষেপ (Overview):</strong> এসএসসি ও দাখিল পরীক্ষা ২০২৭ বাংলা ১ম পত্র (বিষয় কোড: ১৩৪) কবিতাংশ অংশের চূড়ান্ত প্রস্তুতিতে পর্ব-২ সর্বাধিক গুরুত্বপূর্ণ। এই পর্বে জীবনানন্দ দাশের অমর সৃষ্টি <em>সেইদিন এই মাঠ</em>, আহসান হাবীবের আত্মিক অনুভূতির কবিতা <em>আমি কোনো আগন্তুক নই</em>, শামসুর রাহমানের মুক্তিযুদ্ধের অমর দলিল <em>তোমাকে পাওয়ার জন্যে, হে স্বাধীনতা</em>, ফররুখ আহমদের <em>বৃষ্টি</em> এবং আল মাহমুদের <em>বোশেখ</em>-এর পূর্ণাঙ্গ সৃজনশীল প্রশ্ন (CQ), অনুধাবন প্রশ্নব্যাংক এবং বোর্ড পরীক্ষার আদর্শ উত্তর কাঠামো বিস্তারিতভাবে সন্নিবেশিত হয়েছে।</p>
</div>

<!--more-->

<div style="font-family: 'SolaimanLipi', Arial, sans-serif; color: #2d3748; line-height: 1.95; font-size: 17px;">

<h2 style="color: #0f172a; font-size: 24px; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px; margin-top: 35px;">কবিতাংশ পর্ব-২ এর গুরুত্ব ও বোর্ড পরীক্ষার প্রশ্ন কাঠামো</h2>

<p>জাতীয় শিক্ষাক্রম ও পাঠ্যপুস্তক বোর্ড (NCTB) এবং মাদ্রাসা শিক্ষা বোর্ডের ২০২৭ সালের মানবণ্টন অনুসারে বাংলা ১ম পত্র পরীক্ষায় কবিতাংশ থেকে ৪টি সৃজনশীল প্রশ্ন থাকবে, যার মধ্য থেকে শিক্ষার্থীদের ন্যূনতম ২টি প্রশ্নের উত্তর লিখতে হবে। পূর্ববর্তী পর্বে আমরা <a href="https://www.helptrickbd.com/2026/09/ssc-bangla-1st-paper-poetry-cq-part-1.html" style="color: #0284c7; text-decoration: underline;" title="বাংলা ১ম পত্র কবিতাংশ পর্ব-১">কবিতাংশ পর্ব-১ (কপোতাক্ষ নদ, উমর ফারুক, প্রাণ, জীবন বিনিময় ও বন্দনা)</a> বিস্তারিত আলোচনা করেছি। এই পর্বে বাকি গুরুত্বপূর্ণ কবিতাগুলোর বিশ্লেষণ তুলে ধরা হলো।</p>

<div style="overflow-x: auto; margin: 25px 0;">
<table style="width: 100%; border-collapse: collapse; text-align: left; font-size: 15px; background: #ffffff; box-shadow: 0 1px 3px rgba(0,0,0,0.1); border-radius: 8px;">
<thead>
<tr style="background: #0284c7; color: #ffffff;">
<th style="padding: 12px 16px; border: 1px solid #0284c7;">কবিতার নাম</th>
<th style="padding: 12px 16px; border: 1px solid #0284c7;">কবির নাম</th>
<th style="padding: 12px 16px; border: 1px solid #0284c7;">মূল ভাববস্তু ও তাৎপর্য</th>
<th style="padding: 12px 16px; border: 1px solid #0284c7;">গুরুত্ব স্তর</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom: 1px solid #e2e8f0;">
<td style="padding: 12px 16px; font-weight: bold;">সেইদিন এই মাঠ</td>
<td style="padding: 12px 16px;">জীবনানন্দ দাশ</td>
<td style="padding: 12px 16px;">প্রকৃতির শাশ্বত রূপ ও মানুষের মরণশীলতার চিরন্তন দ্বন্দ্ব</td>
<td style="padding: 12px 16px; color: #dc2626; font-weight: bold;">১০০% কমন (৩ স্টার)</td>
</tr>
<tr style="background: #f8fafc; border-bottom: 1px solid #e2e8f0;">
<td style="padding: 12px 16px; font-weight: bold;">আমি কোনো আগন্তুক নই</td>
<td style="padding: 12px 16px;">আহসান হাবীব</td>
<td style="padding: 12px 16px;">জন্মভূমির সাথে আত্মিক নাড়ির টান ও অবিচ্ছেদ্য অস্তিত্ববোধ</td>
<td style="padding: 12px 16px; color: #dc2626; font-weight: bold;">১০০% কমন (৩ স্টার)</td>
</tr>
<tr style="border-bottom: 1px solid #e2e8f0;">
<td style="padding: 12px 16px; font-weight: bold;">তোমাকে পাওয়ার জন্যে, হে স্বাধীনতা</td>
<td style="padding: 12px 16px;">শামসুর রাহমান</td>
<td style="padding: 12px 16px;">১৯৭১-এর মহান মুক্তিযুদ্ধ, আত্মত্যাগ ও স্বাধীনতার অনিবার্য আগমন</td>
<td style="padding: 12px 16px; color: #dc2626; font-weight: bold;">১০০% নিশ্চিত কমন</td>
</tr>
<tr style="background: #f8fafc; border-bottom: 1px solid #e2e8f0;">
<td style="padding: 12px 16px; font-weight: bold;">বৃষ্টি</td>
<td style="padding: 12px 16px;">ফররুখ আহমদ</td>
<td style="padding: 12px 16px;">খরতাপের অবসান, কৃষিজীবনে প্রাণের সঞ্চার ও প্রকৃতির পুনরুজ্জীবন</td>
<td style="padding: 12px 16px; color: #0284c7; font-weight: bold;">খুবই গুরুত্বপূর্ণ</td>
</tr>
<tr style="border-bottom: 1px solid #e2e8f0;">
<td style="padding: 12px 16px; font-weight: bold;">বোশেখ</td>
<td style="padding: 12px 16px;">আল মাহমুদ</td>
<td style="padding: 12px 16px;">কালবোশেখীর রুদ্র রূপ ও অন্যায়ের বিরুদ্ধে গণজাগরণের প্রতীক</td>
<td style="padding: 12px 16px; color: #16a34a; font-weight: bold;">স্পেশাল সিলেকশন</td>
</tr>
</tbody>
</table>
</div>

<h2 style="color: #0f172a; font-size: 24px; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px; margin-top: 35px;">কবিতা ০১: সেইদিন এই মাঠ — সৃজনশীল প্রশ্ন ও পূর্ণাঙ্গ মডেল উত্তর</h2>

<p>রূপসী বাংলার কবি জীবনানন্দ দাশের 'সেইদিন এই মাঠ' কবিতায় প্রকৃতির শাশ্বত সৌন্দর্য ও মানবজীবনের অনিত্যতার এক গভীর দার্শনিক উপলব্ধি প্রকাশ পেয়েছে। কবি জানেন, তিনি একদিন মারা যাবেন এবং এই নশ্বর ধরণী থেকে চিরতরে বিদায় নেবেন। কিন্তু তার মৃত্যুর পরও এই পৃথিবীর মাঠ-ঘাট, চালতাফুল, শিশিরবিন্দু এবং লক্ষ্মীপেঁচার গান চিরকাল অব্যাহত থাকবে। ব্যাবিলন ও এশিরীয় সাম্রাজ্যের মতো মহাশক্তিধর মানবসভ্যতা ধুলোয় মিশে গেছে, কিন্তু প্রকৃতির রূপমাধুরী কখনো ম্লান হয়নি।</p>

<div style="background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 8px; padding: 18px 20px; margin: 20px 0;">
<p style="margin: 0 0 10px 0; font-weight: bold; color: #1e40af;">মডেল উদ্দীপক:</p>
<p style="margin: 0; color: #1e3a8a; line-height: 1.8;">প্রবীণ চিত্রশিল্পী রফিক সাহেব সারাজীবন গ্রামবাংলার নদী, কাশবন ও পল্লীপ্রকৃতির অপরূপ ছবি এঁকেছেন। বার্ধক্যে শয্যাশায়ী হয়ে তিনি জানালা দিয়ে বাইরের শিউলি গাছের দিকে তাকিয়ে ভাবেন—"কয়েকদিন পর হয়তো আমি আর থাকব না, আমার তুলি চিরতরে থেমে যাবে। কিন্তু এই শিউলি গাছটিতে প্রতি শরতেই সাদা-হলুদ ফুল ফুটবে, দোয়েল পাখি এসে গান গাইবে এবং বাতাসে সুবাস ছড়াবে। প্রকৃতির এই রূপ অবিনশ্বর, কেবল মানুষের আয়ুই সীমিত।"</p>
</div>

<h3 style="color: #1e293b; font-size: 20px; margin-top: 25px;">সৃজনশীল প্রশ্নাবলি:</h3>
<ol style="margin-left: 20px; line-height: 2;">
<li><strong>(ক) জ্ঞানমূলক:</strong> 'সেইদিন এই মাঠ' কবিতায় কোন বিলুপ্ত সভ্যতার কথা উল্লেখ রয়েছে? (মান: ১)</li>
<li><strong>(খ) অনুধাবনমূলক:</strong> "সেইদিন এই মাঠ স্তব্ধ হবে নাকো জানি"—উক্তিটি দ্বারা কবি কী বুঝিয়েছেন? (মান: ২)</li>
<li><strong>(গ) প্রয়োগমূলক:</strong> উদ্দীপকের রফিক সাহেবের চিন্তায় 'সেইদিন এই মাঠ' কবিতার কোন দিকটি প্রতিভাত হয়েছে? ব্যাখ্যা করো। (মান: ৩)</li>
<li><strong>(ঘ) উচ্চতর দক্ষতামূলক:</strong> "প্রকৃতির শাশ্বত অস্তিত্বের বিপরীতে মানুষের নশ্বরতাই উভয় প্রসঙ্গের মূল সুর"—মন্তব্যটি বিশ্লেষণ করো। (মান: ৪)</li>
</ol>

<h4 style="color: #0369a1; font-size: 18px; margin-top: 20px;">উত্তর সংকেত ও সমাধান:</h4>
<p><strong>(ক) উত্তর:</strong> কবিতায় 'এশিরিয়া' ও 'ব্যাবিলন' নামক প্রাচীন সভ্যতার কথা উল্লেখ রয়েছে।</p>

<p><strong>(খ) উত্তর:</strong> উক্তিটির মাধ্যমে কবি বোঝাতে চেয়েছেন যে, কবির নিজের মৃত্যুর পরও এই পৃথিবীর প্রাকৃতিক রূপবৈচিত্র্য ও কর্মচাঞ্চল্য এতটুকুও ম্লান বা স্তব্ধ হবে না। মানুষ এককভাবে পৃথিবীতে ক্ষণস্থায়ী অতিথি, কিন্তু প্রকৃতি চিরকালীন। তাই কবির মৃত্যু হলেও শিশির ভেজা চালতাফুলের গন্ধ এবং ধরণীর প্রবাহমান জীবনধারা একই গতিতে অনন্তকাল ধরে বয়ে চলবে।</p>

<p><strong>(গ) উত্তর:</strong> উদ্দীপকের চিত্রশিল্পী রফিক সাহেবের উপলব্ধিতে 'সেইদিন এই মাঠ' কবিতার মূল দর্শন—মানবজীবনের ক্ষণস্থায়িত্ব বনাম প্রকৃতির চিরন্তন সৌন্দর্যের রূপটি ফুটে উঠেছে। রফিক সাহেব বুঝতে পেরেছেন তার মৃত্যুর মাধ্যমে তার নিজস্ব সৃষ্টি স্তব্ধ হলেও শরতের শিউলি ফুলের প্রস্ফুটন কিংবা দোয়েল পাখির গান কখনো থামবে না। কবি জীবনানন্দ দাশও ঠিক একইভাবে অনুভব করেছিলেন যে, তিনি না থাকলেও এই পৃথিবীর ঘাস, শিশির ও নক্ষত্রের আলো চিরকাল অম্লান থাকবে।</p>

<p><strong>(ঘ) উত্তর:</strong> উদ্দীপকের রফিক সাহেব এবং পাঠ্যবইয়ের কবি উভয়ের ভাবনার কেন্দ্রবিন্দু এক। মানুষ তার ব্যক্তিগত কর্মকাণ্ড ও আয়ুষ্কালের সমাপ্তির মধ্য দিয়ে অতীত হয়ে যায়, কিন্তু প্রাকৃতিক জগত তার আপন নিয়মে নব নব রূপে পুনরুজ্জীবিত হয়। ব্যাবিলন বা এশিরিয়ার মতো প্রতাপশালী জাতি যেমন ধ্বংসাবশেষে পরিণত হয়েছে অথচ প্রকৃতি টিকে রয়েছে, তেমনি ব্যক্তি মানুষের বিদায়ের পরও পৃথিবী থাকবে চিরযৌবনা। সুতরাং, প্রশ্নোক্ত মন্তব্যটি যথার্থ ও যুক্তিযুক্ত।</p>

<h2 style="color: #0f172a; font-size: 24px; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px; margin-top: 35px;">কবিতা ০২: আমি কোনো আগন্তুক নই — আত্মিক অস্তিত্বের প্রত্যয়</h2>

<p>আহসান হাবীবের 'আমি কোনো আগন্তুক নই' কবিতায় নিজ মাতৃভূমির সাথে মানুষের গভীর আত্মিক বন্ধন প্রকাশ পেয়েছে। কবি নিজেকে কোনো ভিনদেশি পথিক বা ক্ষণিকের অতিথি মানতে নারাজ। তিনি এই দেশের মাটির ঘ্রাণ চেনেন, কার্তিকের ধানের মঞ্জরিকে চেনেন এবং গ্রামের প্রতিটি দরিদ্র ও শ্রমজীবী মানুষের সুখে-দুঃখে তিনি অবিচ্ছেদ্য সঙ্গী।</p>

<div style="background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 8px; padding: 18px 20px; margin: 20px 0;">
<p style="margin: 0 0 10px 0; font-weight: bold; color: #166534;">শীর্ষ অনুধাবন (খ) প্রশ্নব্যাংক:</p>
<ul style="margin-left: 20px; line-height: 2;">
<li><strong>প্রশ্ন ০১:</strong> কবি নিজেকে কেন কোনো আগন্তুক নন বলে দাবি করেছেন?
<br/><span style="color: #475569;"><em>উত্তর সংকেত:</em> কবি এই দেশের মাটিতে জন্ম নিয়েছেন এবং বড় হয়েছেন। প্রকৃতি ও মানুষের সাথে তার সম্পর্ক জন্মজন্মান্তরের। তিনি কোনো অচেনা পথিক নন, বরং এই মৃত্তিকারই একান্ত আপন সন্তান।</span></li>
<li><strong>প্রশ্ন ০২:</strong> "কদম আলীর ক্লান্ত চোখের আঁধার আমি চিনি"—তাৎপর্য কী?
<br/><span style="color: #475569;"><em>উত্তর সংকেত:</em> গ্রামের খেটে খাওয়া সাধারণ মানুষ কদম আলীর জীবনসংগ্রাম, দারিদ্র্য ও বার্ধক্যের দুঃখ-বেদনাকে কবি খুব কাছ থেকে নিবিড়ভাবে প্রত্যক্ষ করেছেন। এই আত্মিক পরিচয়ের কারণেই কবি তার চোখের ক্লান্তি ও আঁধারকে চিনতে পারেন।</span></li>
<li><strong>প্রশ্ন ০৩:</strong> কবি প্রকৃতিকে কীভাবে নিজের সাক্ষী হিসেবে উপস্থাপন করেছেন?
<br/><span style="color: #475569;"><em>উত্তর সংকেত:</em> আসমানের তারা, চালের ওপরের খড়, জারুল-জামরুল গাছ এবং পুবের পুকুরকে কবি সাক্ষী মেনেছেন। কারণ এই প্রাকৃতিক উপাদানগুলোর সান্নিধ্যেই কবির জীবন ও অস্তিত্ব গড়ে উঠেছে।</span></li>
</ul>
</div>

<h2 style="color: #0f172a; font-size: 24px; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px; margin-top: 35px;">কবিতা ০৩: তোমাকে পাওয়ার জন্যে, হে স্বাধীনতা — পূর্ণাঙ্গ মডেল প্রশ্ন ও সমাধান</h2>

<p>শামসুর রাহমানের 'তোমাকে পাওয়ার জন্যে, হে স্বাধীনতা' বাংলাদেশের মুক্তিযুদ্ধের এক প্রামাণ্য কাব্যদলিল। স্বাধীনতা কোনো সহজলভ্য বস্তু নয়; এর জন্য বাঙালি জাতিকে অকাতরে বুকের রক্ত ঢালতে হয়েছে। পাকিস্তানি হানাদারদের নির্মম গণহত্যায় ধ্বংস হয়েছে একের পর এক গ্রাম, সাকিনা বিবির কপাল ভেঙেছে এবং সিঁথির সিঁদুর মুছে গেছে হরিদাসীর। তবু কবি দৃপ্ত কণ্ঠে ঘোষণা করেছেন—যে আত্মত্যাগ বাঙালি করেছে, তার বিনিময়ে এই বাংলায় স্বাধীনতা আসতেই হবে।</p>

<div style="background: #fff7ed; border: 1px solid #fed7aa; border-radius: 8px; padding: 18px 20px; margin: 20px 0;">
<p style="margin: 0 0 10px 0; font-weight: bold; color: #9a3412;">মডেল উদ্দীপক:</p>
<p style="margin: 0; color: #7c2d12; line-height: 1.8;">১৯৭১ সালের ২৫শে মার্চ কালরাতে হানাদার পাকিস্তানি বাহিনী নিরস্ত্র বাঙালিদের ওপর কাপুরুষোচিত হামলা চালায়। সেই রাতে তরুণ কৃষক মকবুল নিজের ঘরবাড়ি পুড়ে ছাই হতে দেখে। চোখের সামনে বৃদ্ধ মাতাপিতা ও ভাইকে হারিয়ে সে গভীর শোকে ভেঙে পড়েনি, বরং বুকভরা প্রতিশোধের আগুন নিয়ে যোগ দেয় মুক্তিবাহিনীর গেরিলা দলে। দীর্ঘ নয় মাস দুর্গম পাহাড়ে-জঙ্গলে যুদ্ধ করে সে নিজের একটি পা হারায়। কিন্তু বিজয়ের দিনে যখন স্বাধীন বাংলাদেশের লাল-সবুজ পতাকা উড়তে দেখে, তখন তার চোখ দিয়ে আনন্দের অশ্রু গড়িয়ে পড়ে। সে বুঝতে পারে, এই স্বাধীনতার মূল্য কোনো ব্যক্তিগত শোকের চেয়ে অনেক বেশি মহৎ।</p>
</div>

<h3 style="color: #1e293b; font-size: 20px; margin-top: 25px;">সৃজনশীল প্রশ্নাবলি:</h3>
<ol style="margin-left: 20px; line-height: 2;">
<li><strong>(ক) জ্ঞানমূলক:</strong> কার কপাল ভাঙল এবং কার সিঁথির সিঁদুর মুছে গেল? (মান: ১)</li>
<li><strong>(খ) অনুধাবনমূলক:</strong> "সিঁথির সিঁদুর মুছে গেল হরিদাসীর"—চরণটির মাধ্যমে কবি কী বুঝিয়েছেন? (মান: ২)</li>
<li><strong>(গ) প্রয়োগমূলক:</strong> উদ্দীপকের মকবুলের ত্যাগ ও সংগ্রামের সাথে 'তোমাকে পাওয়ার জন্যে, হে স্বাধীনতা' কবিতার কোন চরিত্রের সাদৃশ্য রয়েছে? ব্যাখ্যা করো। (মান: ৩)</li>
<li><strong>(ঘ) উচ্চতর দক্ষতামূলক:</strong> "মকবুলের মতো লাখো বীরের আত্মাহুতির মধ্য দিয়েই কবিতার শেষ চরণের স্বাধীনতার বার্তা সার্থক হয়েছে"—বিশ্লেষণ করো। (মান: ৪)</li>
</ol>

<h4 style="color: #c2410c; font-size: 18px; margin-top: 20px;">উত্তর সংকেত ও সমাধান নির্দেশিকা:</h4>
<p><strong>(ক) উত্তর:</strong> কবিতায় সাকিনা বিবির কপাল ভাঙল এবং হরিদাসীর সিঁথির সিঁদুর মুছে গেল।</p>

<p><strong>(খ) উত্তর:</strong> এই মর্মস্পর্শী চরণের মধ্য দিয়ে একাত্তরের মুক্তিযুদ্ধে হিন্দু নারী হরিদাসীর স্বামী হারানোর চরম ট্র্যাজেডি প্রকাশ পেয়েছে। সনাতন রীতি অনুযায়ী সিঁথির সিঁদুর হলো সধবা নারীর বিবাহিত জীবনের প্রতীক। পাকিস্তানি বাহিনীর নির্বিচার হত্যাকাণ্ডের শিকার হয়ে হরিদাসীর স্বামী প্রাণ হারায় এবং সে চিরতরে বিধবা হয়। বাঙালি মা-বোনদের এই অপূরণীয় ক্ষতি ও আত্মত্যাগের তীব্রতাই কবি চরণটিতে তুলে ধরেছেন।</p>

<p><strong>(গ) উত্তর:</strong> উদ্দীপকের মুক্তিযোদ্ধা মকবুলের আত্মত্যাগ ও অদম্য সাহসের সাথে 'তোমাকে পাওয়ার জন্যে, হে স্বাধীনতা' কবিতায় বর্ণিত সেই তেজস্বী তরুণ ও দুর্ধর্ষ মুক্তিপাগল যোদ্ধাদের সাদৃশ্য রয়েছে। কবিতায় কবি উল্লেখ করেছেন—যে তরুণের চোখে প্রতিশোধের আগুন, যে নতুন নিশান উড়িয়ে মৃত্যুর ভয় তুচ্ছ করে লড়াই করেছিল, মকবুল তারই বাস্তব প্রতিনিধি। ঘরবাড়ি পোড়া ছাইয়ের ওপর দাঁড়িয়েও মকবুল দেশের মুক্তির জন্য অস্ত্র তুলে নিয়েছিল।</p>

<p><strong>(ঘ) উত্তর:</strong> স্বাধীনতা কোনো আকাশকুসুম কল্পনা ছিল না; এর পেছনে ছিল লাখো সাধারণ মানুষের রক্ত ও নিঃস্বার্থ আত্মদান। কবি শামসুর রাহমান স্পষ্টভাবে তুলে ধরেছেন যে, সাকিনা বিবি, হরিদাসী, রুস্তম শেখ কিংবা দগ্ধ বাস্তুভিটায় দাঁড়িয়ে থাকা অবলা প্রাণীদের আর্তনাদ বৃথা যেতে পারে না। উদ্দীপকের মকবুল যেমন পঙ্গুত্ব বরণ করেও পতাকা দেখে বিজয়ের আনন্দ অনুভব করেছে, তেমনি বাঙালির প্রতিটি আত্মত্যাগই স্বাধীনতার ভিত্তিকে মজবুত করেছে। অতএব, উদ্দীপক ও কবিতার বক্তব্যের তাৎপর্য এক ও অভিন্ন।</p>

<h2 style="color: #0f172a; font-size: 24px; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px; margin-top: 35px;">কবিতা ০৪ ও ০৫: বৃষ্টি ও বোশেখ — প্রকৃতি, খরতাপ ও প্রতিবাদের রূপক</h2>

<p>ফররুখ আহমদের 'বৃষ্টি' কবিতায় গ্রীষ্মের প্রচণ্ড খরার পর বর্ষার আগমনে বাংলার প্রাণপ্রকৃতি ও কৃষকের ঘরে স্বস্তির বার্তা নেমে আসার চিত্র অত্যন্ত শৈল্পিকভাবে বর্ণিত হয়েছে। তৃষ্ণার্ত ধরণী যেমন বৃষ্টির এক একটি ফোঁটার স্পর্শে নতুন প্রাণের স্পন্দনে জেগে ওঠে, তেমনি কৃষকের বুকে সঞ্চারিত হয় নবান্নের নতুন স্বপ্ন।</p>

<p>অন্যদিকে আল মাহমুদের 'বোশেখ' কবিতায় বৈশাখী ঝড় কেবল একটি ঋতুভিত্তিক প্রাকৃতিক বিপর্যয় নয়, বরং তা সমাজের জমে থাকা অন্যায়, শোষণ, শোষণকারী অপশক্তি ও অনাচারের বিরুদ্ধে সাধারণ মানুষের প্রচণ্ড গণবিস্ফোরণের রূপক। কালবোশেখীর দমকা হাওয়া যেমন জীর্ণ-শীর্ণ ডালপালা ভেঙে নতুন কচি পাতার পথ সুগম করে, তেমনি গণসংগ্রামও সমাজ থেকে স্বৈরাচার ও অবিচারকে উপড়ে ফেলে মুক্তির পথ তৈরি করে।</p>


<h2 style="color: #0f172a; font-size: 24px; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px; margin-top: 35px;">শিক্ষার্থীদের জন্য প্রস্তুতি পরামর্শ ও অভ্যন্তরীণ লিংকসমূহ</h2>

<p>পরীক্ষায় পূর্ণ নম্বর পেতে সৃজনশীল প্রশ্নের (গ) ও (ঘ) অংশের উত্তরে কবিতার মূল চরণের প্রাসঙ্গিক উদ্ধৃতি ব্যবহার করুন। এতে উত্তর মানসম্মত হয় এবং পরীক্ষকের সন্তুষ্টি নিশ্চিত হয়। আমাদের অন্যান্য গুরুত্বপূর্ণ বিষয়ের চূড়ান্ত প্রস্তুতি গাইডলাইনগুলো দেখে নিন:</p>

<ul style="margin-left: 20px; line-height: 2.1;">
<li><a href="https://www.helptrickbd.com/2026/09/ssc-bangla-1st-paper-final-suggestion.html" style="color: #0284c7; text-decoration: underline;" title="এসএসসি বাংলা ১ম পত্র চূড়ান্ত মাস্টার সাজেশন ২০২৭">এসএসসি বাংলা ১ম পত্র চূড়ান্ত মাস্টার সাজেশন ২০২৬-২০২৭ (সকল অধ্যায় ও মানবণ্টন)</a></li>
<li><a href="https://www.helptrickbd.com/2026/09/ssc-bangla-1st-paper-prose-cq.html" style="color: #0284c7; text-decoration: underline;" title="বাংলা ১ম পত্র গদ্যাংশ পর্ব-১">বাংলা ১ম পত্র গদ্যাংশ পর্ব-১: প্রত্যুপকার, সুভা, বই পড়া ও নিরীহ বাঙালি CQ</a></li>
<li><a href="https://www.helptrickbd.com/2026/09/ssc-bangla-1st-paper-prose-cq-part-2.html" style="color: #0284c7; text-decoration: underline;" title="বাংলা ১ম পত্র গদ্যাংশ পর্ব-২">বাংলা ১ম পত্র গদ্যাংশ পর্ব-২: মানুষ মুহম্মদ (স.), নিমগাছ, উপেক্ষিত শক্তি ও শিক্ষা ও মনুষ্যত্ব</a></li>
<li><a href="https://www.helptrickbd.com/2026/09/ssc-bangla-1st-paper-prose-cq-part-3.html" style="color: #0284c7; text-decoration: underline;" title="বাংলা ১ম পত্র গদ্যাংশ পর্ব-৩">বাংলা ১ম পত্র গদ্যাংশ পর্ব-৩: প্রবাস বন্ধু, মমতাদি, একুশের গল্প ও নতুন গৌরবগাথা</a></li>
<li><a href="https://www.helptrickbd.com/2026/09/ssc-bangla-1st-paper-poetry-cq-part-1.html" style="color: #0284c7; text-decoration: underline;" title="বাংলা ১ম পত্র কবিতাংশ পর্ব-১">বাংলা ১ম পত্র কবিতাংশ পর্ব-১: কপোতাক্ষ নদ, উমর ফারুক, প্রাণ, জীবন বিনিময় ও বন্দনা</a></li>
<li><a href="https://www.helptrickbd.com/2026/09/ssc-english-1st-paper-suggestion-2027.html" style="color: #0284c7; text-decoration: underline;" title="SSC English 1st Paper Suggestion 2027">SSC English 1st Paper Final Suggestion 2027 (Passages, Dialogues & Writing)</a></li>
<li><a href="https://www.helptrickbd.com/2026/09/ssc-english-2nd-paper-suggestion-2027.html" style="color: #0284c7; text-decoration: underline;" title="SSC English 2nd Paper Suggestion 2027">SSC English 2nd Paper Final Suggestion 2027 (Top Grammar Rules & Models)</a></li>
<li><a href="https://www.helptrickbd.com/2025/04/important-instructions-for-ssc-candidates.html" style="color: #0284c7; text-decoration: underline;" title="এসএসসি পরীক্ষার্থীদের জন্য জরুরি নিয়মাবলী">এসএসসি পরীক্ষার্থীদের পরীক্ষার হলে করণীয় ও জরুরি নির্দেশিকা</a></li>
</ul>

</div>
"""

METADATA = {
    "title": "SSC বাংলা ১ম পত্র কবিতাংশ পর্ব-২ সৃজনশীল প্রশ্ন ও উত্তর ২০২৬-২০২৭ | সেইদিন এই মাঠ, বৃষ্টি, আগন্তুক নই, স্বাধীনতা ও বোশেখ",
    "slug": "ssc-bangla-1st-paper-poetry-cq-part-2",
    "labels": ["SSC Suggestion", "Bangla 1st Paper", "Education"],
    "search_description": "এসএসসি ২০২৭ বাংলা ১ম পত্র কবিতাংশ পর্ব-২ সেইদিন এই মাঠ, বৃষ্টি, আমি কোনো আগন্তুক নই, স্বাধীনতা ও বোশেখ সৃজনশীল প্রশ্ন ও উত্তর।",
    "featured_image": "https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/posts/ssc_bangla_1st_paper_poetry_part2_2027.webp"
}

def main():
    print("=" * 70)
    print("[*] GENERATING BANGLA 1ST POETRY PART 2 POST...")
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
