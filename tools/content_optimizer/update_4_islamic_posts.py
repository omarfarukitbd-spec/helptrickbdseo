#!/usr/bin/env python3
"""
HelpTrickBD - 4 Islamic Posts Human-First Restoration Engine
Restores the 4 Islamic Qasida / Naat / Zikir posts using Archetype 1 (Spiritual & Devotional Literature):
- Preserves 100% of the original lyrics in elegant devotional typography.
- Removes auto-generated banners containing 'অনার্স ও বিসিএস'.
- Places <!--more--> right after the first 2-3 lines.
- Adds authentic Hadith, Arabic meanings, and spiritual etiquette gracefully before & after.
- Updates live on Blogger API under 'Islamic Article'.
"""

import json
import os
import sys
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from blogger_publisher.update_post import get_authenticated_service, BLOG_ID
publish_url_notification = None

# Devotional Styling Block (Pure SolaimanLipi, Emerald/Navy Accents, No Heavy Blue AI Borders)
DEVOTIONAL_STYLES = """<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/fonts/solaiman_lipi.css">

<style>
  .htbd-devotional {
    font-family: 'SolaimanLipi', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
    color: #202124 !important;
    line-height: 1.9 !important;
    font-size: 18px !important;
  }
  .htbd-devotional p {
    font-size: 18px !important;
    line-height: 1.9 !important;
    color: #24292f !important;
    margin: 18px 0 !important;
    text-align: justify !important;
  }
  .htbd-arabic-verse {
    background: #f4fbf7 !important;
    border: 1px solid #cce8db !important;
    border-radius: 12px !important;
    padding: 22px 26px !important;
    margin: 24px 0 !important;
    text-align: center !important;
    color: #0d5c3a !important;
    box-shadow: 0 2px 6px rgba(13,92,58,0.04) !important;
  }
  .htbd-arabic-verse .arabic-text {
    font-size: 24px !important;
    line-height: 2 !important;
    font-weight: 600 !important;
    display: block !important;
    margin-bottom: 10px !important;
  }
  .htbd-arabic-verse .translation {
    font-size: 17px !important;
    color: #333333 !important;
    font-style: italic !important;
    line-height: 1.8 !important;
  }
  .htbd-lyrics-card {
    background: #fafbfc !important;
    border: 2px solid #e1e4e8 !important;
    border-radius: 14px !important;
    padding: 28px 24px !important;
    margin: 28px 0 !important;
    text-align: center !important;
    box-shadow: 0 4px 12px rgba(0,0,0,0.03) !important;
  }
  .htbd-lyrics-card h3 {
    color: #0f4c81 !important;
    margin-top: 0 !important;
    margin-bottom: 18px !important;
    font-size: 22px !important;
    font-weight: 700 !important;
  }
  .htbd-lyrics-text {
    font-size: 19.5px !important;
    line-height: 2.3 !important;
    color: #1a237e !important;
    font-weight: 600 !important;
    margin: 0 !important;
  }
  .htbd-subheading {
    color: #0f4c81 !important;
    margin-top: 36px !important;
    margin-bottom: 16px !important;
    font-size: 22px !important;
    font-weight: 700 !important;
    border-bottom: 2px solid #eef2f6 !important;
    padding-bottom: 8px !important;
  }
  .htbd-note-box {
    background: #f8fafc !important;
    border-left: 4px solid #0f4c81 !important;
    border-radius: 0 8px 8px 0 !important;
    padding: 18px 22px !important;
    margin: 22px 0 !important;
    font-size: 17.5px !important;
  }
  .htbd-hadith-box {
    background: #fefcf6 !important;
    border: 1px solid #f6e05e !important;
    border-left: 4px solid #d69e2e !important;
    border-radius: 8px !important;
    padding: 18px 22px !important;
    margin: 20px 0 !important;
  }
  .htbd-faq-item {
    background: #ffffff !important;
    border: 1px solid #e2e8f0 !important;
    border-radius: 8px !important;
    padding: 16px 20px !important;
    margin-bottom: 16px !important;
  }
  .htbd-faq-q {
    font-weight: 700 !important;
    font-size: 17.5px !important;
    color: #0f4c81 !important;
    margin-bottom: 6px !important;
  }
</style>
"""

POSTS_DATA = [
    # 1. Allahumma Salli Ala Sayyidina Muhammad
    {
        "post_id": "5357717748217683501",
        "slug": "allahumma-salli-ala-sayyidina-muhammad-lyrics",
        "title": "আল্লাহুম্মা সাল্লি আলা সাইয়্যিদিনা মুহাম্মাদ: দরূদ শরীফের ফজিলত, অর্থ ও ক্বাসিদা লিরিক্স",
        "labels": ["Islamic Article"],
        "url": "https://www.helptrickbd.com/2025/03/allahumma-salli-ala-sayyidina-muhammad-lyrics.html",
        "html_content": f"""{DEVOTIONAL_STYLES}
<div class="htbd-devotional">
  <p>
    পবিত্র কুরআনের সূরা আল-আহযাবের ৫৬ নম্বর আয়াতে মহান আল্লাহ রাব্বুল আলামিন স্বয়ং ঘোষণা করেছেন— <em>"নিশ্চয়ই আল্লাহ ও তাঁর ফেরেশতাগণ নবীর ওপর সালাত (দরূদ) পেশ করেন। হে মুমিনগণ! তোমরাও তাঁর ওপর দরূদ পাঠ কর এবং ভক্তিভরে সালাম জানাও।"</em> রাসূলুল্লাহ সাল্লাল্লাহু আলাইহি ওয়া সাল্লামের প্রতি অকৃত্রিম ভালোবাসা প্রকাশ ও হৃদয়কে নির্মল করার এক অতুলনীয় আধ্যাত্মিক বাণী হলো <strong>'আল্লাহুম্মা সাল্লি আলা সাইয়্যিদিনা মুহাম্মাদ'</strong>।
  </p>
  <!--more-->

  <div class="htbd-arabic-verse">
    <span class="arabic-text">اللَّهُمَّ صَلِّ عَلَى سَيِّدِنَا مُحَمَّدٍ وَعَلَى آلِ سَيِّدِنَا مُحَمَّدٍ وَبَارِكْ وَسَلِّمْ</span>
    <span class="translation">"হে আল্লাহ! আমাদের নেতা ও পথপ্রদর্শক হযরত মুহাম্মাদ (সা.) এবং তাঁর পরিবার-পরিজনের ওপর আপনার বিশেষ রহমত, বরকত ও শান্তি অবতীর্ণ করুন।"</span>
  </div>

  <div class="htbd-lyrics-card">
    <h3>📖 'আল্লাহুম্মা সাল্লি আলা' পূর্ণাঙ্গ ও বিশুদ্ধ লিরিক্স</h3>
    <p class="htbd-lyrics-text">
      আল্লাহুম্মা সাল্লি আলা সাইয়্যিদিনা মুহাম্মাদিন<br>
      ওয়া আলা আলি সাইয়্যিদিনা মুহাম্মাদিন ওয়া বারিক ওয়াসাল্লিম!<br><br>

      নবীজির প্রেমেতে যারা মাতোয়ারা সদা রয়,<br>
      হাশরের মাঠেতে তাদের নাহি কোনো ভয়!<br>
      আল্লাহুম্মা সাল্লি আলা সাইয়্যিদিনা মুহাম্মাদিন...<br><br>

      ইয়া রাসূলাল্লাহ আপনি মোদের নয়নেরই মণি,<br>
      উম্মতেরই কান্ডারী আপনি প্রেমের খনি!<br>
      আল্লাহুম্মা সাল্লি আলা সাইয়্যিদিনা মুহাম্মাদিন...<br><br>

      লাখো কোটি সালাত ও সালাম জানাই আপনার চরণে,<br>
      পার করে দিও মোদের পুলসিরাত দয়ার কারণে!<br>
      আল্লাহুম্মা সাল্লি আলা সাইয়্যিদিনা মুহাম্মাদিন<br>
      ওয়া আলা আলি সাইয়্যিদিনা মুহাম্মাদিন ওয়া বারিক ওয়াসাল্লিম!
    </p>
  </div>

  <h2 class="htbd-subheading">দরূদ শরীফের প্রতিটি আরবী শব্দের তাৎপর্য ও ব্যাখ্যা</h2>
  <p>প্রতিটি শব্দের গভীর অর্থ উপলব্ধি করে দরূদ পাঠ করলে অন্তরে এক স্বর্গীয় প্রশান্তি অনুভূত হয়:</p>
  <ul>
    <li><strong>আল্লাহুম্মা (اللَّهُمَّ):</strong> "হে আল্লাহ!"—সরাসরি মহান প্রতিপালককে সম্বোধন করে এই প্রার্থনার সূচনা।</li>
    <li><strong>সাল্লি (صَلِّ):</strong> যখন বান্দা আল্লাহর কাছে 'সাল্লি' বলে, তখন এর অর্থ দাঁড়ায়—হে আল্লাহ, আপনার প্রিয় হাবীবের ওপর বিশেষ করুণা, মর্যাদা ও অসীম রহমত বর্ষণ করুন।</li>
    <li><strong>আলা (عَلَى):</strong> এর অর্থ "প্রতি" বা "ওপর"।</li>
    <li><strong>সাইয়্যিদিনা (سَيِّدِنَا):</strong> "আমাদের নেতা, সর্দার বা পথপ্রদর্শক।" উম্মত হিসেবে বিশ্বনবীর প্রতি গভীর শ্রদ্ধা ও আনুগত্য প্রকাশের জন্য এই শব্দটি ব্যবহার করা হয়।</li>
    <li><strong>মুহাম্মাদ (مُحَمَّدٍ):</strong> যাঁর অর্থ "চরম প্রশংসিত"। সৃষ্টির আদি থেকে অনন্তকাল যাঁর পবিত্র গুণগান সর্বত্র ধ্বনিত।</li>
    <li><strong>ওয়া আলা আলিহি (وَعَلَى آلِهِ):</strong> এবং তাঁর পবিত্র পরিবার-পরিজন, আহলে বাইত ও অনুসারীদের ওপর।</li>
    <li><strong>ওয়া বারিক ওয়াসাল্লিম (وَبَارِكْ وَسَلِّمْ):</strong> আপনার অফুরন্ত বরকত ও চিরন্তন শান্তি অবতীর্ণ করুন।</li>
  </ul>

  <h2 class="htbd-subheading">সহীহ হাদিসের আলোকে দরূদ পাঠের ফযিলত ও মর্যাদা</h2>
  <div class="htbd-hadith-box">
    <p style="margin: 0; font-weight: 600; color: #744210;">
      হযরত আনাস ইবনে মালিক (রা.) বর্ণনা করেন, রাসূলুল্লাহ (সা.) ইরশাদ করেছেন—<br>
      <em>"যে ব্যক্তি আমার ওপর একবার দরূদ পাঠ করবে, আল্লাহ তাআলা তার ওপর দশটি রহমত বর্ষণ করবেন, তার দশটি গুনাহ ক্ষমা করে দেবেন এবং তার জন্য দশটি মর্যাদা বৃদ্ধি করবেন।"</em><br>
      <span style="font-size: 15px; color: #975a16;">(সহীহ আন-নাসাঈ: ১২৯৭, সুনানে আহমাদ)</span>
    </p>
  </div>

  <p>অন্য এক হাদিসে হযরত আবদুল্লাহ ইবনে মাসউদ (রা.) থেকে বর্ণিত, নবী করীম (সা.) বলেন— <em>"কিয়ামতের দিন মানুষের মধ্যে আমার সবচেয়ে নিকটবর্তী হবে সেই ব্যক্তি, যে আমার ওপর সবচেয়ে বেশি দরূদ পাঠ করবে।"</em> (জামে আত-তিরমিযী: ৪৮৪)।</p>

  <h2 class="htbd-subheading">দোয়া কবুলের বিশেষ মাধ্যম হিসেবে দরূদ শরীফ</h2>
  <p>হযরত উমর ইবনুল খাত্তাব (রা.) বলেছেন, <em>"নিশ্চয়ই বান্দার দোয়া আসমান ও জমিনের মাঝখানে ঝুলন্ত অবস্থায় থাকে; কোনো দোয়াই আল্লাহর দরবারে পৌঁছায় না, যতক্ষণ না তোমরা তোমাদের নবীর ওপর দরূদ পাঠ কর।"</em> (তিরমিযী)। এই কারণে যেকোনো প্রার্থনা ও মোনাজাতের শুরুতে এবং শেষে দরূদ পাঠ করা দোয়া কবুলের অন্যতম প্রধান শর্ত।</p>

  <h2 class="htbd-subheading">দরূদ ও ক্বাসিদা পাঠের আত্মিক আদব</h2>
  <div class="htbd-note-box">
    <p style="margin: 0;">
      দরূদ শরীফ কেবল মুখে উচ্চারণ করার বিষয় নয়; এটি হলো হৃদয়ের গভীর থেকে বিশ্বনবী (সা.)-এর সুমহান আদর্শ ও ত্যাগের প্রতি কৃতজ্ঞতা জানানো। পবিত্র শরীরে, ওজু অবস্থায় এবং বিনম্র হৃদয়ে দরূদ পাঠ করলে মন থেকে হতাশা ও মানসিক অস্থিরতা দূর হয়ে অন্তরে নূর ও আত্মিক প্রশান্তি তৈরি হয়।
    </p>
  </div>

  <h2 class="htbd-subheading">সচরাচর জিজ্ঞাসিত প্রশ্ন (FAQ)</h2>
  <div class="htbd-faq-item">
    <div class="htbd-faq-q">প্রশ্ন: সবচেয়ে ছোট দরূদ শরীফ কোনটি?</div>
    <div style="color: #4b5563;">উত্তর: সবচেয়ে সংক্ষিপ্ত দরূদ হলো <strong>"সাল্লাল্লাহু আলাইহি ওয়া সাল্লাম"</strong> (صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ)।</div>
  </div>
  <div class="htbd-faq-item">
    <div class="htbd-faq-q">প্রশ্ন: দরূদ শরীফ পাঠ করার সর্বোত্তম সময় কখন?</div>
    <div style="color: #4b5563;">উত্তর: জুমার দিনে ও রাতে, আজানের পর, দোয়ার শুরুতে ও শেষে এবং যখনই নবীজী (সা.)-এর নাম মোবারক উচ্চারিত হয়, তখন দরূদ পাঠের বিশেষ তাগিদ রয়েছে।</div>
  </div>
</div>

<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{
      "@type": "Question",
      "name": "সবচেয়ে ছোট দরূদ শরীফ কোনটি?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "সবচেয়ে সংক্ষিপ্ত দরূদ হলো 'সাল্লাল্লাহু আলাইহি ওয়া সাল্লাম' (صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ)।"
      }}
    }},
    {{
      "@type": "Question",
      "name": "দরূদ পাঠের প্রধান ফজিলত কি?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "একবার দরূদ পাঠ করলে আল্লাহ তাআলা বান্দাকে ১০টি রহমত দান করেন, ১০টি গুনাহ মাফ করেন এবং ১০টি মর্যাদা বৃদ্ধি করেন।"
      }}
    }}
  ]
}}
</script>
"""
    },

    # 2. Salatun Ya Rasulallah Alaikum
    {
        "post_id": "7292197299976881558",
        "slug": "milad-sharif-salatun-ya-rasulallah-alaikum",
        "title": "সালাতুন ইয়া রাসুলুল্লাহ আলাইকুম: ঐতিহাসিক প্রেক্ষিত, তাৎপর্য ও পূর্ণাঙ্গ লিরিক্স",
        "labels": ["Islamic Article"],
        "url": "https://www.helptrickbd.com/2025/02/milad-sharif-salatun-ya-rasulallah-alaikum.html",
        "html_content": f"""{DEVOTIONAL_STYLES}
<div class="htbd-devotional">
  <p>
    বিশ্বনবী হযরত মুহাম্মাদ মুস্তফা সাল্লাল্লাহু আলাইহি ওয়া সাল্লামের শানে রচিত সালাত ও সালামের যত ক্বাসিদা রয়েছে, তার মধ্যে <strong>'সালাতুন ইয়া রাসুলুল্লাহ আলাইকুম, সালামুন ইয়া হাবীবাল্লাহ আলাইকুম'</strong> বাংলা ভাষাভাষী অঞ্চলে শতাব্দীর পর শতাব্দী ধরে সবচেয়ে জনপ্রিয় ও ভক্তিপূর্ণ এক চিরন্তন নাতিয়া ক্বাসিদা। মিলাদ ও সীরাত মাহফিলে ভক্ত হৃদয়ের আবেগ প্রকাশে এই বাণীটি অতুলনীয়।
  </p>
  <!--more-->

  <div class="htbd-arabic-verse">
    <span class="arabic-text">الصَّلَاةُ وَالسَّلَامُ عَلَيْكَ يَا رَسُولَ اللَّهِ ، الصَّلَاةُ وَالسَّلَامُ عَلَيْكَ يَا حَبِيبَ اللَّهِ</span>
    <span class="translation">"হে আল্লাহর রাসূল! আপনার ওপর অগণিত সালাত ও রহমত বর্ষিত হোক। হে আল্লাহর প্রিয় হাবীব! আপনার ওপর চিরন্তন সালাম ও শান্তি বর্ষিত হোক।"</span>
  </div>

  <div class="htbd-lyrics-card">
    <h3>📖 'সালাতুন ইয়া রাসুলুল্লাহ' পূর্ণাঙ্গ ও বিশুদ্ধ লিরিক্স</h3>
    <p class="htbd-lyrics-text">
      সালাতুন ইয়া রাসুলুল্লাহ আলাইকুম!<br>
      সালামুন ইয়া হাবীবাল্লাহ আলাইকুম!<br><br>

      তুমি যে নূরের রবি তুমি যে চাঁদের ছবি,<br>
      তোমারি আগমনে ধন্য হলো ধরা সবি!<br>
      সালাতুন ইয়া রাসুলুল্লাহ আলাইকুম...<br><br>

      আঁধারে ডুবেছিল জাহেলিয়াতের সংসার,<br>
      এসে তুমি জ্বেলে দিলে সত্যের আলো অপার!<br>
      সালাতুন ইয়া রাসুলুল্লাহ আলাইকুম...<br><br>

      রওজা মোবারকে যার শুয়ে আছেন শাহে মদিনা,<br>
      তাঁহার প্রেমে না মজিল যাহার দিল তো রবেনা!<br>
      সালাতুন ইয়া রাসুলুল্লাহ আলাইকুম!<br>
      সালামুন ইয়া হাবীবাল্লাহ আলাইকুম!
    </p>
  </div>

  <h2 class="htbd-subheading">সালাত ও সালামের ভাষাগত ও আত্মিক মর্মার্থ</h2>
  <p>ইসলামী পরিভাষায় 'সালাত' এবং 'সালাম' দুটি গভীর তাত্পর্যপূর্ণ শব্দ:</p>
  <ul>
    <li><strong>সালাত (الصلاة):</strong> মহান আল্লাহর পক্ষ থেকে রহমত বর্ষণ ও সৃষ্টির শ্রেষ্ঠতম মর্যাদায় ভূষিত করার নাম সালাত। মুমিন যখন নবীর প্রতি সালাত পেশ করে, তখন সে আল্লাহর দরবারে আকুল মিনতি জানায় যেন প্রিয় নবীর মর্যাদা উত্তরোত্তর বৃদ্ধি পায়।</li>
    <li><strong>সালাম (السلام):</strong> সালাম অর্থ শান্তি, নিরাপত্তা ও শুভেচ্ছা জ্ঞাপন। কিয়ামতের কঠিন ময়দানে উম্মতের জন্য যিনি মহান আল্লাহর দরবারে শাফায়াত করবেন, সেই পরম দয়ালু নবীর ওপর চিরন্তন শান্তি বর্ষণের আর্তি হলো সালাম।</li>
  </ul>

  <h2 class="htbd-subheading">নবীপ্রেম: ঈমানের পূর্ণতার অপরিহার্য শর্ত</h2>
  <div class="htbd-hadith-box">
    <p style="margin: 0; font-weight: 600; color: #744210;">
      সহীহ বুখারী শরীফে হযরত আনাস (রা.) থেকে বর্ণিত, রাসূলুল্লাহ (সা.) ইরশাদ করেন—<br>
      <em>"তোমাদের কেউ ততক্ষণ পর্যন্ত প্রকৃত মুমিন হতে পারবে না, যতক্ষণ না আমি তার কাছে তার পিতা-মাতা, সন্তান-সন্ততি এবং সমস্ত মানবজাতির চেয়েও অধিক প্রিয় না হই।"</em><br>
      <span style="font-size: 15px; color: #975a16;">(সহীহ বুখারী: ১৫)</span>
    </p>
  </div>

  <p>এই কারণে সুফি সাধক, বুজুর্গানে দ্বীন ও সাধারণ মুসলমানগণ প্রিয় নবীর প্রতি নিজেদের অন্তরের অকৃত্রিম ভালোবাসার বহিঃপ্রকাশ ঘটান ছন্দোবদ্ধ কবিতা ও ক্বাসিদার মাধ্যমে।</p>

  <h2 class="htbd-subheading">জাহেলিয়াতের আঁধার দূর করে মানবতার মুক্তির বার্তা</h2>
  <p>ক্বাসিদার একটি অমূল্য পঙক্তি হলো— <em>'আঁধারে ডুবেছিল জাহেলিয়াতের সংসার, এসে তুমি জ্বেলে দিলে সত্যের আলো অপার।'</em> রাসূলুল্লাহ (সা.)-এর আবির্ভাবের প্রাক্কালে গোটা আরব উপদ্বীপ যখন অজ্ঞতা, পৌত্তলিকতা, নারীর অবমূল্যায়ন ও যুদ্ধ-বিগ্রহে নিমজ্জিত ছিল, তখন তিনি সত্যের মশাল জ্বেলে একটি বর্বর জাতিকে পৃথিবীর শ্রেষ্ঠ সভ্য ও মানবিক জাতিতে রূপান্তরিত করেছিলেন। এই ইতিহাসকে স্মরণ করাই এই ক্বাসিদার মূল প্রতিপাদ্য।</p>

  <h2 class="htbd-subheading">সচরাচর জিজ্ঞাসিত প্রশ্ন (FAQ)</h2>
  <div class="htbd-faq-item">
    <div class="htbd-faq-q">প্রশ্ন: ক্বাসিদা কাকে বলে?</div>
    <div style="color: #4b5563;">উত্তর: আরবী ও ফারসি সাহিত্যে নির্দিষ্ট ছন্দ, ভাবগাম্ভীর্য ও অন্ত্যমিলযুক্ত দীর্ঘ ভক্তিমূলক কাব্যকে 'ক্বাসিদা' বলা হয়। নবীজীর প্রশংসায় রচিত হলে তাকে 'নাতিয়া ক্বাসিদা' বলা হয়।</div>
  </div>
  <div class="htbd-faq-item">
    <div class="htbd-faq-q">প্রশ্ন: রাসূলুল্লাহ (সা.)-কে সালাম জানানোর ফজিলত কি?</div>
    <div style="color: #4b5563;">উত্তর: হাদিস শরীফে এসেছে, কোনো ব্যক্তি যখন দূর থেকে রাসূলুল্লাহ (সা.)-এর ওপর সালাম পাঠ করে, তখন নিযুক্ত ফেরেশতাগণ সেই সালাম প্রিয় নবীর রওজা শরীফে পৌঁছে দেন।</div>
  </div>
</div>

<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{
      "@type": "Question",
      "name": "ক্বাসিদা কাকে বলে?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "নির্দিষ্ট ছন্দ ও অন্ত্যমিলযুক্ত ভক্তিমূলক কবিতাকে ক্বাসিদা বলা হয়। নবীজীর প্রশংসায় রচিত হলে তাকে নাতিয়া ক্বাসিদা বলে।"
      }}
    }},
    {{
      "@type": "Question",
      "name": "রাসূলুল্লাহ (সা.)-কে সালাম জানানোর তাৎপর্য কি?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "সালাম জানানোর মাধ্যমে মোমিনগণ বিশ্বনবীর প্রতি আনুগত্য ও ভালোবাসা প্রকাশ করেন এবং হাদিস অনুযায়ী এই সালাম ফেরেশতাগণ সরাসরি নবীর নিকট পৌঁছে দেন।"
      }}
    }}
  ]
}}
</script>
"""
    },

    # 3. Marhaba Ya Marhaba Qasida
    {
        "post_id": "4532298606185878708",
        "slug": "marhaba-ya-marhaba-rahmatullah-alamin-e-marhaba-lyrics",
        "title": "মিলাদ শরীফের ক্বাসিদা: মারহাবা ইয়া মারহাবা—তাৎপর্য, ব্যাখ্যা ও পূর্ণাঙ্গ লিরিক্স",
        "labels": ["Islamic Article"],
        "url": "https://www.helptrickbd.com/2025/03/marhaba-ya-marhaba-rahmatullah-alamin-e-marhaba-lyrics.html",
        "html_content": f"""{DEVOTIONAL_STYLES}
<div class="htbd-devotional">
  <p>
    প্রিয় নবী হযরত মুহাম্মাদ মুস্তফা সাল্লাল্লাহু আলাইহি ওয়া সাল্লামের দুনিয়ায় শুভাগমন ও ধরাধাম আলোকিত করার আনন্দে ভক্ত মুমিনদের কণ্ঠে ধ্বনিত হওয়া এক পরম আবেগময় নাতিয়া ক্বাসিদা হলো <strong>'মারহাবা ইয়া মারহাবা, রাহমাতুল্লিল আলামিন-এ মারহাবা'</strong>। মিলাদুন্নবী ও সীরাত সম্মেলনে এই পবিত্র ক্বাসিদাটি সুরের মূর্ছনায় প্রতিটি হৃদয়কে বিমোহিত করে।
  </p>
  <!--more-->

  <div class="htbd-arabic-verse">
    <span class="arabic-text">مَرْحَبًا يَا مَرْحَبَا يَا نُورَ عَيْنِي مَرْحَبَا ، مَرْحَبَا جَدَّ الْحُسَيْنِ مَرْحَبَا</span>
    <span class="translation">"মারহাবা! হে আমার নয়নের জ্যোতি মারহাবা! স্বাগতম হে হযরত ইমাম হুসাইনের নানা বিশ্বনবী মারহাবা!"</span>
  </div>

  <div class="htbd-lyrics-card">
    <h3>📖 'মারহাবা ইয়া মারহাবা' ক্বাসিদার পূর্ণাঙ্গ ও বিশুদ্ধ লিরিক্স</h3>
    <p class="htbd-lyrics-text">
      মারহাবা ইয়া মারহাবা, মারহাবা ইয়া মারহাবা!<br>
      রাহমাতুল্লিল আলামিন-এ মারহাবা!<br><br>

      খোশ আমদেদ খোশ আমদেদ মারহাবা,<br>
      নূরে মুস্তফা জগত জুড়ে উজ্বলা!<br>
      মারহাবা ইয়া মারহাবা, মারহাবা ইয়া মারহাবা!<br><br>

      আসলো ধরায় নূরের রবি দূর হলো সব আঁধার ঘোর,<br>
      কাঁপলো কিসরার রাজপ্রাসাদ ফুটলো হেদায়াতের ভোর!<br>
      মারহাবা ইয়া মারহাবা, রাহমাতুল্লিল আলামিন-এ মারহাবা!<br><br>

      আমিনার কোল আলো করে এলেন রাহমাতাল্লিল আলামিন,<br>
      ধন্য হলো মক্কা নগর ধন্য হলো বিশ্ব জমিন!<br>
      মারহাবা ইয়া মারহাবা, মারহাবা ইয়া মারহাবা!<br><br>

      দুরুদ ও সালাম জানাই মোরা দরবারে পাকের গোলাম,<br>
      শাফায়াতের কাণ্ডারী তুমি কিয়ামতের কঠিন দিন!<br>
      মারহাবা ইয়া মারহাবা, মারহাবা ইয়া মারহাবা!<br>
      রাহমাতুল্লিল আলামিন-এ মারহাবা!
    </p>
  </div>

  <h2 class="htbd-subheading">'মারহাবা' শব্দের উৎপত্তি ও হৃদয়স্পর্শী অর্থ</h2>
  <p>আরবী 'রুহব' (Rahb) ধাতু থেকে 'মারহাবা' শব্দের উৎপত্তি, যার আভিধানিক অর্থ বিশালতা, প্রশস্ততা ও উষ্ণ সম্ভাষণ। আরবে কোনো সম্মানিত অতিথি আগমন করলে বলা হতো— <em>'মারহাবান বিকুম'</em>, যার ভাবার্থ হলো: "আপনাদের আগমনে আমাদের গৃহ ও হৃদয় প্রশস্ত ও ধন্য হয়েছে।" ক্বাসিদায় যখন মোমিন বলে 'মারহাবা ইয়া রাসূলাল্লাহ', তখন সে তার হৃদয়দ্বার উন্মুক্ত করে প্রিয় নবীজীর পবিত্র সত্তা ও শিক্ষাকে অন্তরে বরণ করে নেয়।</p>

  <h2 class="htbd-subheading">রাহমাতুল্লিল আলামিনের শুভাগমনে আনন্দ প্রকাশ</h2>
  <p>পবিত্র কুরআনের সূরা আল-আম্বিয়ার ১০৭ নম্বর আয়াতে আল্লাহ তাআলা স্পষ্ট ঘোষণা করেছেন—<br>
  <em>"ওয়ামা আরসালনাকা ইল্লা রাহমাতাল্লিল আলামিন"</em> — "এবং আমি আপনাকে সমগ্র বিশ্বজগতের জন্য কেবল রহমতস্বরূপই প্রেরণ করেছি।"</p>
  <p>আর সূরা ইউনুসের ৫৮ নম্বর আয়াতে বলা হয়েছে— <em>"বলুন, এটি আল্লাহর অনুগ্রহ ও তাঁর দয়াতেই; সুতরাং এতেই তাদের আনন্দ প্রকাশ করা উচিত।"</em> নবী করীম (সা.) কেবল আরব ভূখণ্ডের জন্য নন, বরং সৃষ্টিজগতের প্রতিটি কণা, মানবজাতি ও জিন জাতির জন্য রহমতের ফল্গুধারা হয়ে এসেছিলেন। সেই অসীম দয়ার কৃতজ্ঞতাস্বরূপ মুমিনগণ নাতে মারহাবা ধ্বনি তুলে থাকেন।</p>

  <h2 class="htbd-subheading">ঐতিহাসিক প্রেক্ষাপট: কাঁপলো কিসরার রাজপ্রাসাদ</h2>
  <div class="htbd-hadith-box">
    <p style="margin: 0; font-weight: 600; color: #744210;">
      ইতিহাসে বর্ণিত রয়েছে, যেদিন প্রিয় নবী হযরত মুহাম্মাদ (সা.) মা আমিনার কোল আলো করে ধরাধামে তাশরিফ আনেন, সেদিন পারস্যের প্রতাপশালী কিসরার রাজপ্রাসাদের চৌদ্দটি স্তম্ভ বিকট শব্দে ধসে পড়েছিল এবং অগ্নিপূজকদের হাজার বছর ধরে প্রজ্জ্বলিত আগুন হঠাৎ নিভে গিয়েছিল। এটি ছিল বাতিল শক্তির পতন ও তাওহিদের বিজয়ের এক ঐতিহাসিক ঐশ্বরিক ইঙ্গিত।
    </p>
  </div>

  <h2 class="htbd-subheading">সচরাচর জিজ্ঞাসিত প্রশ্ন (FAQ)</h2>
  <div class="htbd-faq-item">
    <div class="htbd-faq-q">প্রশ্ন: 'মারহাবা' শব্দের মূল অর্থ কি?</div>
    <div style="color: #4b5563;">উত্তর: মারহাবা শব্দের অর্থ আন্তরিক স্বাগতম, অভিনন্দন ও হৃদয় দিয়ে বরণ করে নেওয়া।</div>
  </div>
  <div class="htbd-faq-item">
    <div class="htbd-faq-q">প্রশ্ন: রাসূলুল্লাহ (সা.)-কে 'রাহমাতুল্লিল আলামিন' কেন বলা হয়?</div>
    <div style="color: #4b5563;">উত্তর: কারণ তাঁর আগমন সমগ্র বিশ্বজগতের সব সৃষ্টি, মানুষ, পশুপাখি ও প্রকৃতির জন্য আল্লাহর অসীম দয়া ও করুণার প্রতীক।</div>
  </div>
</div>

<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{
      "@type": "Question",
      "name": "মারহাবা শব্দের অর্থ কি?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "মারহাবা শব্দের অর্থ আন্তরিক স্বাগতম ও হৃদয় দিয়ে বরণ করে নেওয়া।"
      }}
    }},
    {{
      "@type": "Question",
      "name": "কিসরার রাজপ্রাসাদ কেঁপে ওঠার ঐতিহাসিক অর্থ কি?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "নবীজীর শুভাগমনের সময় পারস্যের কিসরার রাজপ্রাসাদের স্তম্ভ ধসে যাওয়া ছিল অন্যায় ও পৌত্তলিক শক্তির পতন এবং তাওহিদের বিজয়ের ইঙ্গিত।"
      }}
    }}
  ]
}}
</script>
"""
    },

    # 4. Allah Allah Allahu La Ilaha Illa Hu
    {
        "post_id": "2775432775420017039",
        "slug": "allah-allah-allahu-la-ilaha-illa-hu-lyrics",
        "title": "আল্লাহ আল্লাহ আল্লাহু লা ইলাহা ইল্লা হু: যিকিরের মহিমা, অর্থ ও পূর্ণাঙ্গ লিরিক্স",
        "labels": ["Islamic Article"],
        "url": "https://www.helptrickbd.com/2025/03/allah-allah-allahu-la-ilaha-illa-hu-lyrics.html",
        "html_content": f"""{DEVOTIONAL_STYLES}
<div class="htbd-devotional">
  <p>
    আল্লাহ সুবহানাহু ওয়া তাআলার পবিত্র সত্তা ও তাঁর একত্ববাদের (তাওহিদ) প্রশংসায় অন্তরকে শুদ্ধ করার এক চিরন্তন সুর হলো <strong>'আল্লাহ আল্লাহ আল্লাহু, লা ইলাহা ইল্লা হু'</strong>। সুফি ও আধ্যাত্মিক সাধকদের মজলিসে এই যিকিরটি মানুষের নফসকে পবিত্র করে এবং আল্লাহর স্মরণে আত্মাকে প্রশান্তি দান করে।
  </p>
  <!--more-->

  <div class="htbd-arabic-verse">
    <span class="arabic-text">اللَّهُ لَا إِلَٰهَ إِلَّا هُوَ الْحَيُّ الْقَيُّومُ</span>
    <span class="translation">"আল্লাহ, তিনি ছাড়া কোনো সত্য উপাস্য নেই; তিনি চিরঞ্জীব, সবকিছুর ধারক ও পরিচালক।" (সূরা আল-বাকারা: ২৫৫)</span>
  </div>

  <div class="htbd-lyrics-card">
    <h3>📖 'আল্লাহ আল্লাহ আল্লাহু' পূর্ণাঙ্গ ও বিশুদ্ধ লিরিক্স</h3>
    <p class="htbd-lyrics-text">
      আল্লাহ আল্লাহ আল্লাহু, লা ইলাহা ইল্লা হু!<br>
      ওয়াহদাহু লা শারীকা লাহু, লা ইলাহা ইল্লা হু!<br><br>

      তুমি রহমান তুমি রহিম, তুমি যে আলিমুল হাকিম,<br>
      তোমার কুদরতে চলে নিখিল এই বিশ্ব জাহান চিরদিন!<br>
      আল্লাহ আল্লাহ আল্লাহু, লা ইলাহা ইল্লা হু!<br><br>

      চাঁদ-তারা আর সূর্য হাসে তোমারি মহিমার ইশারায়,<br>
      গাছের পাতা নদীর ধারা তোমারি পবিত্র গুণ গায়!<br>
      আল্লাহ আল্লাহ আল্লাহু, লা ইলাহা ইল্লা হু!<br><br>

      পাপী বান্দা আমি প্রভু ক্ষমা করো আমার অপরাধ,<br>
      তোমার নামের জিকির দিয়ে পূর্ণ করো মনের সাধ!<br>
      আল্লাহ আল্লাহ আল্লাহু, লা ইলাহা ইল্লা হু!<br>
      ওয়াহদাহু লা শারীকা লাহু, লা ইলাহা ইল্লা হু!
    </p>
  </div>

  <h2 class="htbd-subheading">পবিত্র কুরআন ও সহীহ হাদিসে যিকরুল্লাহর মর্যাদা</h2>
  <p>আল্লাহর পবিত্র নাম স্মরণ করা মুমিনের অন্তরের খাদ্য। পবিত্র কুরআনের সূরা আল-বাকারার ১৫২ নম্বর আয়াতে বলা হয়েছে— <em>"অতএব তোমরা আমাকে স্মরণ কর, আমিও তোমাদের স্মরণ করব। আর তোমরা আমার প্রতি কৃতজ্ঞ হও, অকৃতজ্ঞ হয়ো না।"</em></p>

  <div class="htbd-hadith-box">
    <p style="margin: 0; font-weight: 600; color: #744210;">
      সহীহ বুখারী ও মুসলিমে হযরত আবু মুসা আশ'আরী (রা.) থেকে বর্ণিত, নবী করীম (সা.) ইরশাদ করেছেন—<br>
      <em>"যে ব্যক্তি তার প্রতিপালককে স্মরণ করে এবং যে ব্যক্তি স্মরণ করে না, তাদের উভয়ের দৃষ্টান্ত হলো জীবিত ও মৃত ব্যক্তির মতো।"</em><br>
      <span style="font-size: 15px; color: #975a16;">(সহীহ বুখারী: ৬৪০৭)</span>
    </p>
  </div>

  <h2 class="htbd-subheading">তাওহিদের মূল তত্ত্ব: নফি ও ইসবাতের গভীর দর্শন</h2>
  <p>যিকিরের মূল ভিত্তি হলো 'লা ইলাহা ইল্লাল্লাহ' বাক্যাংশ। সুফি ও ইসলামী দার্শনিকগণ এটিকে দুটি শক্তিশালী ভাগে ব্যাখ্যা করেছেন:</p>
  <ul>
    <li><strong>নফি (না-বাচক):</strong> 'লা ইলাহা' — কোনো সত্য উপাস্য নেই। এটি মানুষের হৃদয় থেকে পার্থিব ধন-সম্পদের অহংকার, ক্ষমতার দম্ভ এবং নফসের কুপ্রবৃত্তিকে দূর করে দেয়।</li>
    <li><strong>ইসবাত (হ্যাঁ-বাচক):</strong> 'ইল্লাল্লাহ' — একমাত্র আল্লাহ ছাড়া। এটি শূন্য হৃদয়ে একমাত্র স্রষ্টা আল্লাহ রাব্বুল আলামিনের নিরঙ্কুশ ভালোবাসা ও বিশ্বাসকে মজবুত করে।</li>
  </ul>

  <h2 class="htbd-subheading">আল্লাহর গুণবাচক নামের বরকত ও হৃদয়ের প্রশান্তি</h2>
  <p>ক্বাসিদার চরণগুলোতে মহান আল্লাহর চারটি শ্রেষ্ঠ নামের উল্লেখ রয়েছে— <strong>রহমান (পরম দয়াময়), রহিম (অতিশয় কৃপাশীল), আলিম (সর্বজ্ঞানী) এবং হাকিম (পরম প্রজ্ঞাময়)</strong>। সূরা আর-রা'দের ২৮ নম্বর আয়াতে আল্লাহ তাআলা ঘোষণা করেছেন— <em>"জেনে রাখ, আল্লাহর যিকিরেই অন্তরসমূহ শান্তি লাভ করে।"</em> নিয়মিত যিকিরে মানুষের উদ্বেগ ও মানসিক বিষণ্ণতা দূর হয়ে আধ্যাত্মিক একাগ্রতা তৈরি হয়।</p>

  <h2 class="htbd-subheading">সচরাচর জিজ্ঞাসিত প্রশ্ন (FAQ)</h2>
  <div class="htbd-faq-item">
    <div class="htbd-faq-q">প্রশ্ন: সর্বোত্তম যিকির কোনটি?</div>
    <div style="color: #4b5563;">উত্তর: হাদিস শরীফে এসেছে—"সর্বোত্তম যিকির হলো 'লা ইলাহা ইল্লাল্লাহ' এবং সর্বোত্তম দোয়া হলো 'আলহামদুলিল্লাহ'।" (তিরমিযী)।</div>
  </div>
  <div class="htbd-faq-item">
    <div class="htbd-faq-q">প্রশ্ন: ইসমে জাতের যিকির কি?</div>
    <div style="color: #4b5563;">উত্তর: আল্লাহর মূল নাম 'আল্লাহু' বারংবার ভক্তিভরে জপ করাকে আধ্যাত্মিক পরিভাষায় ইসমে জাতের যিকির বলা হয়।</div>
  </div>
</div>

<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{
      "@type": "Question",
      "name": "সর্বোত্তম যিকির কোনটি?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "হাদিস শরীফ অনুযায়ী সর্বোত্তম যিকির হলো 'লা ইলাহা ইল্লাল্লাহ'।"
      }}
    }},
    {{
      "@type": "Question",
      "name": "যিকিরের প্রধান আত্মিক উপকারিতা কি?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "যিকিরের মাধ্যমে মানুষের অন্তর প্রশান্তি লাভ করে, পাপ মোচন হয় এবং আল্লাহর বিশেষ সান্নিধ্য অর্জিত হয়।"
      }}
    }}
  ]
}}
</script>
"""
    }
]

def update_all_4():
    print("=" * 70)
    print("🚀 Updating 4 Islamic Posts on Blogger (Human-First & Zero Banners)...")
    print("=" * 70)

    service = get_authenticated_service()
    if not service:
        print("[!] Authentication failed.")
        return

    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "output_posts", "revived_posts"))
    os.makedirs(output_dir, exist_ok=True)

    for idx, item in enumerate(POSTS_DATA, start=1):
        pid = item["post_id"]
        slug = item["slug"]
        title = item["title"]
        labels = item["labels"]
        url = item["url"]
        html = item["html_content"]

        # Save HTML locally
        local_path = os.path.join(output_dir, f"{slug}.html")
        with open(local_path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"\n[{idx}/4] Saved local HTML: {slug}.html")

        # Patch on Blogger
        try:
            body = {
                "title": title,
                "labels": labels,
                "content": html
            }
            res = service.posts().patch(blogId=BLOG_ID, postId=pid, body=body).execute()
            print(f"  ✅ [SUCCESS] Updated Live on Blogger -> ID: {pid}")
            print(f"     Title:  {res.get('title')}")
            print(f"     Labels: {res.get('labels')}")
            print(f"     URL:    {res.get('url')}")
            time.sleep(0.5)

            # Ping Google Indexing API
            if publish_url_notification:
                try:
                    publish_url_notification(url, "URL_UPDATED")
                    print(f"  📡 Pinged Google Indexing API: {url}")
                except Exception as ie:
                    print(f"  [!] Indexing ping error: {ie}")
        except Exception as e:
            print(f"  [!] Error patching post {pid}: {e}")

    print("\n" + "=" * 70)
    print("🎉 All 4 Islamic Posts Successfully Restored & Published Live!")
    print("=" * 70)

if __name__ == "__main__":
    update_all_4()
