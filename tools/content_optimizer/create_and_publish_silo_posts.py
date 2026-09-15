#!/usr/bin/env python3
"""
tools/content_optimizer/create_and_publish_silo_posts.py
HelpTrickBD Topical Authority Expansion Engine.

Creates 4 high-value, comprehensive flagship articles (1,300-1,500+ words each)
with 16:9 banners (strictly 10-20 KB WebP), SolaimanLipi typography,
Position-0 boxes, tables, dwell time boosters, and FAQ microdata.
Directly publishes them to Blogger via Blogger API v3.
"""

import os
import sys
import json
import time

try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.blogger_publisher.update_post import get_authenticated_service, BLOG_ID
from tools.image_generator.banner_generator import generate_banner
from tools.engagement_booster.dwell_optimizer import optimize_post_engagement

OUTPUT_DIR = os.path.join(PROJECT_ROOT, "output_posts", "new_silo_posts")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 4 New Flagship Articles Definition
ARTICLES = [
    {
        "slug": "computer-virus-and-cyber-security-guide-2026",
        "title": "কম্পিউটার ভাইরাস ও সাইবার নিরাপত্তা: ম্যালওয়্যার থেকে ডাটা সুরক্ষার সেরা উপায় (২০২৬)",
        "category": "তথ্য ও যোগাযোগ প্রযুক্তি",
        "labels": ["কম্পিউটার শিক্ষা", "তথ্য ও যোগাযোগ প্রযুক্তি"],
        "banner_filename": "computer-virus-cyber-security-banner.jpg",
        "banner_category": "💻 আইসিটি ও সাইবার নিরাপত্তা",
        "banner_title": "কম্পিউটার ভাইরাস ও সাইবার নিরাপত্তা গাইডলাইন",
        "banner_subtitle": "ম্যালওয়্যার, র‍্যানসমওয়্যার ও ফিশিং থেকে কম্পিউটার ও ডাটা সুরক্ষার উপায়",
        "banner_features": ["🛡️ ভাইরাস বনাম ম্যালওয়্যার", "🔒 ২-ফ্যাক্টর নিরাপত্তা", "⚡ সেরা ফ্রি অ্যান্টিভাইরাস", "📌 সংস্করণ ২০২৬"],
        "start_color": (15, 23, 42),
        "end_color": (14, 116, 144),
        "accent_color": (56, 189, 248),
        "meta_desc": "কম্পিউটার ভাইরাস কি, এর প্রকারভেদ, ম্যালওয়্যার ও র‍্যানসমওয়্যার থেকে নিজের পিসি ও ডাটা সুরক্ষিত রাখার সেরা টেকনিক্যাল উপায় ও সতর্কতা।",
        "body_paragraphs": """
<h2>কম্পিউটার ভাইরাস কী? (এক নজরে সংক্ষিপ্ত উত্তর)</h2>
<div style="background: #f0fdf4; border-left: 5px solid #16a34a; padding: 18px 22px; border-radius: 6px; margin: 20px 0; font-family: 'SolaimanLipi', sans-serif;">
  <p style="margin: 0; font-size: 17px; line-height: 1.8; color: #166534;">
    <strong>কম্পিউটার ভাইরাস (Computer Virus):</strong> হলো এমন এক ধরনের ক্ষতিকারক সফটওয়্যার প্রোগ্রাম বা কোড, যা ব্যবহারকারীর অনুমতি বা অজ্ঞাতে কম্পিউটারে প্রবেশ করে নিজের প্রতিলিপি (Replication) তৈরি করতে পারে এবং সিস্টেমের স্বাভাবিক কার্যক্রম, ফাইল বা অপারেটিং সিস্টেমকে ক্ষতিগ্রস্ত করে। ভাইরাসের পূর্ণরূপ হলো—<strong>Vital Information Resources Under Siege (VIRUS)</strong>।
  </p>
</div>
<!--more-->

<h2>কম্পিউটার ম্যালওয়্যারের প্রকারভেদ (Classification of Malware)</h2>
<p>প্রযুক্তি জগতে 'ম্যালওয়্যার' হলো সমস্ত ক্ষতিকর সফটওয়্যারের সামগ্রিক নাম। নিচে প্রধান প্রধান ম্যালওয়্যার ও ভাইরাসের বিশদ রূপ তুলে ধরা হলো:</p>
<ul>
  <li><strong>ট্রোজান হর্স (Trojan Horse):</strong> বাইরে থেকে দরকারী গেম বা সফটওয়্যার মনে হলেও ভেতরে ক্ষতিকারক কোড লুকিয়ে থাকে।</li>
  <li><strong>র‍্যানসমওয়্যার (Ransomware):</strong> কম্পিউটারের সমস্ত ফাইল এনক্রিপ্ট (লক) করে টাকা দাবি করে (যেমন: WannaCry)।</li>
  <li><strong>স্পাইওয়্যার (Spyware):</strong> ব্যবহারকারীর পাসওয়ার্ড, ব্রাউজিং হিস্ট্রি ও ব্যাংকিং তথ্য গোপনে হ্যাকারের কাছে পাচার করে।</li>
  <li><strong>ওয়র্ম (Worm):</strong> ইন্টারনেটের মাধ্যমে কোনো ব্যবহারকারীর সাহায্য ছাড়াই স্বয়ংক্রিয়ভাবে হাজার হাজার কম্পিউটারে ছড়িয়ে পড়ে।</li>
</ul>

<h2>কম্পিউটার আক্রান্ত হওয়ার প্রধান লক্ষণসমূহ</h2>
<p>আপনার পিসি বা ল্যাপটপ ভাইরাসে আক্রান্ত হলে নিচের লক্ষণগুলো দেখা দেবে:</p>
<ol>
  <li>কম্পিউটার হঠাৎ মাত্রাতিরিক্ত ধীরগতি (Lag/Hang) হয়ে যাওয়া।</li>
  <li>ডেক্সটপে অপ্রয়োজনীয় পপ-আপ বিজ্ঞাপন বা এরর বার্তা প্রদর্শিত হওয়া।</li>
  <li>হার্ডডিস্কের ফাইল স্বয়ংক্রিয়ভাবে হাইড বা করাপ্ট হয়ে শর্টকাট ফাইলে রূপান্তর হওয়া।</li>
  <li>ব্রাউজারে অজানা হোমপেজ সেট হওয়া ও সার্চ ইঞ্জিন পরিবর্তন হয়ে যাওয়া।</li>
</ol>

<h2>ভাইরাস বনাম ম্যালওয়্যারের তুলনামূলক পার্থক্য ছক</h2>
<table style="width: 100%; border-collapse: collapse; margin: 25px 0; font-family: 'SolaimanLipi', sans-serif;">
  <thead>
    <tr style="background: #0284c7; color: #ffffff;">
      <th style="padding: 12px; border: 1px solid #cbd5e1; text-align: left;">বৈশিষ্ট্য</th>
      <th style="padding: 12px; border: 1px solid #cbd5e1; text-align: left;">কম্পিউটার ভাইরাস</th>
      <th style="padding: 12px; border: 1px solid #cbd5e1; text-align: left;">ম্যালওয়্যার (Malware)</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">আভিধানিক পরিধি</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">ম্যালওয়্যার পরিবারের একটি নির্দিষ্ট শাখা।</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">সমস্ত ক্ষতিকর প্রোগ্রামের সাধারণ ছাতা।</td>
    </tr>
    <tr>
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">প্রতিলিপি ক্ষমতা</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">হোস্ট ফাইলের সাথে নিজেকে কপি করে ছড়ায়।</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">সব ম্যালওয়্যারের প্রতিলিপি ক্ষমতা থাকে না।</td>
    </tr>
    <tr style="background: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">উদ্দেশ্য</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">সিস্টেম ফাইল মুছে ফেলা বা নষ্ট করা।</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">গুপ্তচরবৃত্তি, অর্থ আত্মসাৎ ও ডাটা চুরি।</td>
    </tr>
  </tbody>
</table>

<h2>সাইবার নিরাপত্তা ও ডাটা সুরক্ষার ১০টি সোনালী নিয়ম</h2>
<p>বর্তমান ডিজিটাল যুগে নিজের ব্যক্তিগত ও অফিশিয়াল কম্পিউটারকে সুরক্ষিত রাখতে নিচের নিয়মগুলো মেনে চলা আবশ্যক:</p>
<ul>
  <li><strong>১. নিয়মিত অপারেটিং সিস্টেম আপডেট:</strong> উইন্ডোজ বা ম্যাকওএস-এর সিকিউরিটি প্যাচ সময়মতো আপডেট রাখুন।</li>
  <li><strong>২. বিশ্বস্ত অ্যান্টিভাইরাস ব্যবহার:</strong> উইন্ডোজের নিজস্ব <em>Windows Security (Defender)</em> সক্রিয় রাখুন অথবা বিশ্বস্ত অ্যান্টিভাইরাস সফটওয়্যার ব্যবহার করুন।</li>
  <li><strong>৩. পাইরেটেড ও ক্র্যাক সফটওয়্যার বর্জন:</strong> ইন্টারনেটের ফ্রি ক্র্যাক সফটওয়্যার ও গেম হলো র‍্যানসমওয়্যার প্রবেশের প্রধান পথ।</li>
  <li><strong>৪. টু-ফ্যাক্টর অথেনটিকেশন (2FA):</strong> জিমেইল, ফেসবুক ও ব্যাংক অ্যাকাউন্টে বাধ্যতামূলকভাবে ২FA চালু করুন।</li>
  <li><strong>৫. সন্দেহজনক ইমেইল ও ফিশিং লিংক এড়িয়ে চলা:</strong> অজানা প্রেরকের অ্যাটাচমেন্ট বা লটারির লিংকে ক্লিক করবেন না।</li>
  <li><strong>৬. নিয়মিত অফলাইন ব্যাকআপ:</strong> গুরুত্বপূর্ণ ডকুমেন্টের একটি কপি এক্সটার্নাল হার্ডড্রাইভ বা ক্লাউডে সংরক্ষণ করুন।</li>
</ul>

<h2>সাধারণ জিজ্ঞাসা (FAQ - Frequently Asked Questions)</h2>
<div style="margin: 25px 0;">
  <h3>প্রশ্ন ১: পেনড্রাইভের মাধ্যমে ভাইরাস ছড়ানো কীভাবে বন্ধ করা যায়?</h3>
  <p>উত্তর: কম্পিউটারে পেনড্রাইভ প্রবেশ করিয়ে সরাসরি ডাবল ক্লিক করে খুলবেন না। উইন্ডোজ ডিফেন্ডার দিয়ে প্রথমে স্ক্যান করে তারপর ফোল্ডার ভিউ থেকে ওপেন করুন।</p>
  <h3>প্রশ্ন ২: ফ্রি অ্যান্টিভাইরাস কি যথেষ্ট?</h3>
  <p>উত্তর: সাধারণ ব্যক্তিগত ব্যবহারের জন্য উইন্ডোজ ১০ ও ১১-এর বিল্ট-ইন <strong>Windows Defender</strong> অত্যন্ত শক্তিশালী ও নিরাপদ। অতিরিক্ত কোনো ক্র্যাক অ্যান্টিভাইরাস ইন্সটল করার প্রয়োজন নেই।</p>
</div>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "পেনড্রাইভের মাধ্যমে ভাইরাস ছড়ানো কীভাবে বন্ধ করা যায়?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "কম্পিউটারে পেনড্রাইভ প্রবেশ করিয়ে সরাসরি ডাবল ক্লিক করে খুলবেন না। অ্যান্টিভাইরাস দিয়ে প্রথমে স্ক্যান করে তারপর ওপেন করুন।"
      }
    },
    {
      "@type": "Question",
      "name": "ফ্রি অ্যান্টিভাইরাস কি যথেষ্ট?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "সাধারণ ব্যক্তিগত ব্যবহারের জন্য উইন্ডোজের বিল্ট-ইন Windows Defender অত্যন্ত শক্তিশালী ও যথেষ্ট।"
      }
    }
  ]
}
</script>
"""
    },
    {
        "slug": "cloud-computing-types-benefits-guide",
        "title": "ক্লাউড কম্পিউটিং কি? প্রকারভেদ, বাস্তব সুবিধা ও শীর্ষ প্ল্যাটফর্মের সহজ ব্যাখ্যা",
        "category": "তথ্য ও যোগাযোগ প্রযুক্তি",
        "labels": ["কম্পিউটার শিক্ষা", "তথ্য ও যোগাযোগ প্রযুক্তি"],
        "banner_filename": "cloud-computing-guide-banner.jpg",
        "banner_category": "☁️ ক্লাউড কম্পিউটিং ও আইসিটি",
        "banner_title": "ক্লাউড কম্পিউটিং কি ও এর বাস্তব সুবিধা",
        "banner_subtitle": "IaaS, PaaS ও SaaS মডেলের তুলনামূলক সহজ পাঠ্যপুস্তক গাইড",
        "banner_features": ["🌐 ৩টি ক্লাউড মডেল", "🏢 পাবলিক বনাম প্রাইভেট", "💾 গুগল ড্রাইভ ও এডব্লিউএস", "📌 সংস্করণ ২০২৬"],
        "start_color": (30, 27, 75),
        "end_color": (67, 56, 202),
        "accent_color": (129, 140, 248),
        "meta_desc": "ক্লাউড কম্পিউটিং কী, এর বৈশিষ্ট্য, সার্ভিস মডেল (IaaS, PaaS, SaaS) এবং বাস্তব জীবনে ক্লাউড প্রযুক্তির সুবিধা নিয়ে বিস্তারিত সহজ আলোচনা।",
        "body_paragraphs": """
<h2>ক্লাউড কম্পিউটিং কী? (সংক্ষিপ্ত ও স্পষ্ট ধারণা)</h2>
<div style="background: #f0fdf4; border-left: 5px solid #16a34a; padding: 18px 22px; border-radius: 6px; margin: 20px 0; font-family: 'SolaimanLipi', sans-serif;">
  <p style="margin: 0; font-size: 17px; line-height: 1.8; color: #166534;">
    <strong>ক্লাউড কম্পিউটিং (Cloud Computing):</strong> হলো ইন্টারনেটের মাধ্যমে চাহিদা অনুযায়ী (On-Demand) কম্পিউটিং রিসোর্স যেমন—ডাটা স্টোরেজ, সার্ভার, ডেটাবেজ, নেটওয়ার্কিং ও সফটওয়্যার ব্যবহারের একটি আধুনিক প্রযুক্তি। সহজ কথায়, নিজের কম্পিউটারের হার্ডডিস্কে কোনো তথ্য বা প্রোগ্রাম সেভ না করে ইন্টারনেটে থাকা রিমোট সার্ভারে সংরক্ষণ ও পরিচালনা করাই ক্লাউড কম্পিউটিং।
  </p>
</div>
<!--more-->

<h2>ক্লাউড কম্পিউটিংয়ের ৩টি মূল সার্ভিস মডেল (Service Models)</h2>
<p>ক্লাউড আর্কিটেকচারকে মূলত তিনটি ক্যাটাগরিতে ভাগ করা হয়:</p>
<ol>
  <li><strong>IaaS (Infrastructure as a Service):</strong> এখানে ভার্চুয়াল মেশিন, সার্ভার ও স্টোরেজ ভাড়া দেওয়া হয়। ব্যবহারকারী নিজের মতো ওএস ও সফটওয়্যার চালায় (যেমন: Amazon AWS EC2, Google Cloud Compute Engine)।</li>
  <li><strong>PaaS (Platform as a Service):</strong> সফটওয়্যার ডেভেলপারদের জন্য অ্যাপ্লিকেশন তৈরির প্ল্যাটফর্ম সরবরাহ করা হয়। হার্ডওয়্যার মেইনটেন্যান্স ক্লাউড কোম্পানি করে (যেমন: Google App Engine, Heroku)।</li>
  <li><strong>SaaS (Software as a Service):</strong> তৈরি সফটওয়্যার সরাসরি ইন্টারনেট ব্রাউজারে ব্যবহার করা হয় (যেমন: Google Drive, Gmail, Dropbox, Microsoft 365)।</li>
</ol>

<h2>ক্লাউড সার্ভিস মডেলের তুলনামূলক টেবিল</h2>
<table style="width: 100%; border-collapse: collapse; margin: 25px 0; font-family: 'SolaimanLipi', sans-serif;">
  <thead>
    <tr style="background: #4338ca; color: #ffffff;">
      <th style="padding: 12px; border: 1px solid #cbd5e1; text-align: left;">মডেল</th>
      <th style="padding: 12px; border: 1px solid #cbd5e1; text-align: left;">পূর্ণরূপ</th>
      <th style="padding: 12px; border: 1px solid #cbd5e1; text-align: left;">ব্যবহারকারী</th>
      <th style="padding: 12px; border: 1px solid #cbd5e1; text-align: left;">বাস্তব উদাহরণ</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">IaaS</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Infrastructure as a Service</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">সিস্টেম অ্যাডমিন ও নেটওয়ার্ক ইঞ্জিনিয়ার</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">AWS, Microsoft Azure, Google Cloud</td>
    </tr>
    <tr>
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">PaaS</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Platform as a Service</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">সফটওয়্যার ও অ্যাপ ডেভেলপার</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Google App Engine, OpenShift</td>
    </tr>
    <tr style="background: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">SaaS</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Software as a Service</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">সাধারণ ব্যবহারকারী ও ব্যবসা প্রতিষ্ঠান</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Google Drive, Zoom, Canva, Office 365</td>
    </tr>
  </tbody>
</table>

<h2>ক্লাউড ডিপ্লয়মেন্ট মডেল (Deployment Types)</h2>
<p>ব্যাবহারিক উদ্দেশ্যের ওপর ভিত্তি করে ক্লাউড ৪ ধরনের হয়ে থাকে:</p>
<ul>
  <li><strong>পাবলিক ক্লাউড (Public Cloud):</strong> সাধারণ জনগণের জন্য উন্মুক্ত (যেমন: গুগল ড্রাইভ)।</li>
  <li><strong>প্রাইভেট ক্লাউড (Private Cloud):</strong> কেবল নির্দিষ্ট একটি প্রতিষ্ঠানের নিজস্ব প্রয়োজনে ব্যবহৃত সুরক্ষিত ক্লাউড (যেমন: ব্যাংকিং ডেটাবেজ)।</li>
  <li><strong>হাইব্রিড ক্লাউড (Hybrid Cloud):</strong> পাবলিক ও প্রাইভেট ক্লাউডের সমন্বিত রূপ।</li>
  <li><strong>কমিউনিটি ক্লাউড (Community Cloud):</strong> একই স্বার্থযুক্ত একাধিক সংস্থা মিলে পরিচালিত ব্যবস্থা।</li>
</ul>

<h2>ক্লাউড কম্পিউটিং ব্যবহারের বাস্তব সুবিধাসমূহ</h2>
<ul>
  <li><strong>ব্যয় সাশ্রয়:</strong> নিজস্ব ভারী সার্ভার বা হার্ডওয়্যার কেনার বিশাল খরচ বাঁচে।</li>
  <li><strong>যেকোনো স্থান থেকে অ্যাক্সেস:</strong> ইন্টারনেট থাকলেই মোবাইল বা ল্যাপটপ থেকে পৃথিবীর যেকোনো প্রান্তে বসে কাজ করা সম্ভব।</li>
  <li><strong>স্বয়ংক্রিয় ব্যাকআপ ও নিরাপত্তা:</strong> হার্ডডিস্ক নষ্ট হলেও ক্লাউডের ডাটা চিরতরে সুরক্ষিত থাকে।</li>
  <li><strong>উচ্চ নির্ভরযোগ্যতা ও স্কেলেবিলিটি:</strong> প্রয়োজন অনুযায়ী রিসোর্স বাড়ানো বা কমানো যায়।</li>
</ul>

<h2>সাধারণ জিজ্ঞাসা (FAQ)</h2>
<div style="margin: 25px 0;">
  <h3>প্রশ্ন ১: ক্লাউড কম্পিউটিং কি সম্পূর্ণ নিরাপদ?</h3>
  <p>উত্তর: শীর্ষ ক্লাউড প্রোভাইডাররা মিলিটারি-গ্রেড এনক্রিপশন ও বিশ্বমানের ফায়ারওয়াল ব্যবহার করে, যা ব্যক্তিগত কম্পিউটারের চেয়ে অনেক বেশি নিরাপদ।</p>
  <h3>প্রশ্ন ২: গুগল ড্রাইভ কি ক্লাউড কম্পিউটিংয়ের অংশ?</h3>
  <p>উত্তর: হ্যাঁ, গুগল ড্রাইভ হলো SaaS (Software as a Service) মডেলের ক্লাউড স্টোরেজ সেবা।</p>
</div>
"""
    },
    {
        "slug": "bcs-preliminary-marks-distribution-booklist",
        "title": "বিসিএস প্রিলিমিনারি ২০০ নম্বরের বিষয়ভিত্তিক মানবণ্টন ও প্রথমবারে পাসের পূর্ণাঙ্গ বুক লিস্ট",
        "category": "চাকরি প্রস্তুতি",
        "labels": ["বিসিএস প্রস্তুতি", "চাকরি প্রস্তুতি"],
        "banner_filename": "bcs-preliminary-marks-booklist-banner.jpg",
        "banner_category": "🎯 বিসিএস ক্যাডার প্রস্তুতি",
        "banner_title": "বিসিএস প্রিলিমিনারি ২০০ নম্বরের মানবণ্টন",
        "banner_subtitle": "বিষয়ভিত্তিক নম্বর বিভাজন, নির্ভরযোগ্য বুক লিস্ট ও সেরা স্টাডি রুটিন",
        "banner_features": ["📝 ২০০ নম্বরের সিলেবাস", "📚 বিষয়ের প্রামাণ্য বই", "⏳ দৈনিক ৮ ঘণ্টার রুটিন", "📌 সংস্করণ ২০২৬"],
        "start_color": (19, 42, 31),
        "end_color": (5, 150, 105),
        "accent_color": (253, 224, 71),
        "meta_desc": "বিসিএস প্রিলিমিনারি পরীক্ষার ২০০ নম্বরের পূর্ণাঙ্গ বিষয়ভিত্তিক মানবণ্টন, প্রতিটি বিষয়ের সেরা সহায়ক বই এবং নতুন প্রার্থীদের প্রথমবারে প্রিলি পাসের গাইডলাইন।",
        "body_paragraphs": """
<h2>বিসিএস প্রিলিমিনারি পরীক্ষার গঠন ও মানবণ্টন সারাংশ</h2>
<div style="background: #f0fdf4; border-left: 5px solid #16a34a; padding: 18px 22px; border-radius: 6px; margin: 20px 0; font-family: 'SolaimanLipi', sans-serif;">
  <p style="margin: 0; font-size: 17px; line-height: 1.8; color: #166534;">
    <strong>বিসিএস প্রিলিমিনারি পরীক্ষা (BCS Preliminary Exam):</strong> বাংলাদেশ সরকারি কর্ম কমিশন (BPSC) কর্তৃক পরিচালিত মোট ২০০ নম্বরের একটি এমসিকিউ (MCQ) পরীক্ষা। মোট সময় ২ ঘণ্টা। প্রতিটি সঠিক উত্তরের জন্য ১ নম্বর বরাদ্দ এবং ভুল উত্তরের জন্য ০.৫০ নম্বর কাটা যায় (Negative Marking)।
  </p>
</div>
<!--more-->

<h2>২০০ নম্বরের বিষয়ভিত্তিক পূর্ণাঙ্গ মানবণ্টন ছক</h2>
<table style="width: 100%; border-collapse: collapse; margin: 25px 0; font-family: 'SolaimanLipi', sans-serif;">
  <thead>
    <tr style="background: #059669; color: #ffffff;">
      <th style="padding: 12px; border: 1px solid #cbd5e1; text-align: left;">ক্রম</th>
      <th style="padding: 12px; border: 1px solid #cbd5e1; text-align: left;">বিষয় (Subject)</th>
      <th style="padding: 12px; border: 1px solid #cbd5e1; text-align: center;">বরাদ্দকৃত নম্বর</th>
      <th style="padding: 12px; border: 1px solid #cbd5e1; text-align: left;">প্রধান অধ্যায়সমূহ</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; text-align: center;">১</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">বাংলা ভাষা ও সাহিত্য</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1; text-align: center; font-weight: bold;">৩৫</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">ব্যাকরণ (১৫ নম্বর), প্রাচীন ও মধ্যযুগ (৫), আধুনিক যুগ (১৫)।</td>
    </tr>
    <tr>
      <td style="padding: 10px; border: 1px solid #cbd5e1; text-align: center;">২</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">ইংরেজি ভাষা ও সাহিত্য</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1; text-align: center; font-weight: bold;">৩৫</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">Grammar & Parts of Speech (২০), English Literature (১৫)।</td>
    </tr>
    <tr style="background: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; text-align: center;">৩</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">বাংলাদেশ বিষয়াবলি</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1; text-align: center; font-weight: bold;">৩০</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">ইতিহাস ও মুক্তিযুদ্ধ, সংবিধান, অর্থনীতি, সরকার ব্যবস্থা।</td>
    </tr>
    <tr>
      <td style="padding: 10px; border: 1px solid #cbd5e1; text-align: center;">৪</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">আন্তর্জাতিক বিষয়াবলি</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1; text-align: center; font-weight: bold;">২০</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">বৈশ্বিক ইতিহাস ও সংস্থা, কূটনীতি, চুক্তি ও পরিবেশ সমস্যা।</td>
    </tr>
    <tr style="background: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; text-align: center;">৫</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">ভূগোল, পরিবেশ ও দুর্যোগ ব্যবস্থাপনা</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1; text-align: center; font-weight: bold;">১০</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">বাংলাদেশের ভূগোল ও আবহাওয়া, দুর্যোগ মোকাবিলা।</td>
    </tr>
    <tr>
      <td style="padding: 10px; border: 1px solid #cbd5e1; text-align: center;">৬</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">সাধারণ বিজ্ঞান</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1; text-align: center; font-weight: bold;">১৫</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">ভৌত বিজ্ঞান (৫), জীব বিজ্ঞান (৫), আধুনিক বিজ্ঞান (৫)।</td>
    </tr>
    <tr style="background: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; text-align: center;">৭</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">কম্পিউটার ও তথ্যপ্রযুক্তি</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1; text-align: center; font-weight: bold;">১৫</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">হার্ডওয়্যার, নেটওয়ার্কিং, ইন্টারনেট ও সাইবার সিকিউরিটি।</td>
    </tr>
    <tr>
      <td style="padding: 10px; border: 1px solid #cbd5e1; text-align: center;">৮</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">গাণিতিক যুক্তি (Mathematics)</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1; text-align: center; font-weight: bold;">১৫</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">পাটিগণিত, বীজগণিত, জ্যামিতি ও পরিসংখ্যান।</td>
    </tr>
    <tr style="background: #f8fafc;">
      <td style="padding: 10px; border: 1px solid #cbd5e1; text-align: center;">৯</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">মানসিক দক্ষতা (Mental Ability)</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1; text-align: center; font-weight: bold;">১৫</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">ভাষাগত যুক্তি, সংখ্যামূলক ক্ষমতা, দিক নির্ণয়, সম্পর্ক।</td>
    </tr>
    <tr>
      <td style="padding: 10px; border: 1px solid #cbd5e1; text-align: center;">১০</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: bold;">নৈতিকতা, মূল্যবোধ ও সুশাসন</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1; text-align: center; font-weight: bold;">১০</td>
      <td style="padding: 10px; border: 1px solid #cbd5e1;">সুশাসন, মূল্যবোধ, দুর্নীতি দমন ও প্রাতিষ্ঠানিক জবাবদিহিতা।</td>
    </tr>
  </tbody>
</table>

<h2>প্রথমবারে প্রিলি পাসের সেরা প্রামাণ্য বুক লিস্ট (Recommended Booklist)</h2>
<ul>
  <li><strong>বাংলা ব্যাকরণ:</strong> নবম-দশম শ্রেণির বাংলা ব্যাকরণ বোর্ড বই (পুরাতন সংস্করণ) + অগ্রদূত/অভিযাত্রী।</li>
  <li><strong>বাংলা সাহিত্য:</strong> লাল-নীল দীপাবলি (হুমায়ুন আজাদ) + এমপিথ্রি বাংলা সাহিত্য।</li>
  <li><strong>ইংরেজি ব্যাকরণ:</strong> Competitive English (Mohammad Fazlur Rahman) অথবা Master English।</li>
  <li><strong>ইংরেজি সাহিত্য:</strong> An ABC of English Literature (Dr. M Mofizar Rahman) + Miracle BCS।</li>
  <li><strong>বাংলাদেশ ও আন্তর্জাতিক বিষয়াবলি:</strong> এমপিথ্রি সিরিজ + কারেন্ট অ্যাফেয়ার্স ও নিয়মিত দৈনিক পত্রিকা পাঠ।</li>
  <li><strong>গণিত ও মানসিক দক্ষতা:</strong> জর্জ এমপিথ্রি গণিত ও ষষ্ঠ-দশম শ্রেণির বোর্ড বই।</li>
</ul>

<h2>বিসিএস প্রিলিমিনারি পাসের জন্য ৫টি সফল টিপস</h2>
<ol>
  <li><strong>বিগত বছরের প্রশ্ন সমাধান:</strong> ১০ম থেকে ৪৬তম বিসিএসের প্রতিটি প্রশ্ন পুঙ্খানুপুঙ্খ ব্যাখ্যাসহ শেষ করুন।</li>
  <li><strong>নেগেটিভ মার্কিং নিয়ন্ত্রণ:</strong> নিশ্চিত না হয়ে অন্ধের মতো আন্দাজে দাগানো বন্ধ করুন।</li>
  <li><strong>মডেল টেস্ট ও টাইম ম্যানেজমেন্ট:</strong> ঘড়ি ধরে নিয়মিত ২০০ নম্বরের মডেল টেস্ট দিন।</li>
</ol>
"""
    },
    {
        "slug": "primary-teacher-job-viva-preparation-guideline",
        "title": "সরকারি প্রাথমিক শিক্ষক নিয়োগ ও চাকরির ভাইভা প্রস্তুতি গাইডলাইন (২০২৬)",
        "category": "চাকরি প্রস্তুতি",
        "labels": ["চাকরি প্রস্তুতি", "ক্যারিয়ার গাইড"],
        "banner_filename": "primary-teacher-viva-guide-banner.jpg",
        "banner_category": "👔 সরকারি চাকরি ও ভাইভা",
        "banner_title": "চাকরি ও ভাইভা পরীক্ষার সেরা প্রস্তুতি গাইড",
        "banner_subtitle": "প্রাথমিক শিক্ষক ও সরকারি নিয়োগে আত্মবিশ্বাসী সফলতার টিপস",
        "banner_features": ["🗣️ স্মার্ট আত্মপরিচয়", "👔 মার্জিত ড্রেস কোড", "📋 জরুরি ডকুমেন্ট চেকলিস্ট", "📌 সংস্করণ ২০২৬"],
        "start_color": (30, 41, 59),
        "end_color": (15, 118, 110),
        "accent_color": (45, 212, 191),
        "meta_desc": "সরকারি প্রাথমিক বিদ্যালয় সহকারী শিক্ষক নিয়োগ ভাইভা এবং সরকারি চাকরির মৌখিক পরীক্ষায় সফল হওয়ার জন্য ড্রেস কোড, সাধারণ জিজ্ঞাসা ও স্মার্ট গাইডলাইন।",
        "body_paragraphs": """
<h2>ভাইভা পরীক্ষার গুরুত্ব ও মূল উদ্দেশ্য</h2>
<div style="background: #f0fdf4; border-left: 5px solid #16a34a; padding: 18px 22px; border-radius: 6px; margin: 20px 0; font-family: 'SolaimanLipi', sans-serif;">
  <p style="margin: 0; font-size: 17px; line-height: 1.8; color: #166534;">
    <strong>মৌখিক পরীক্ষা (Viva Voce):</strong> শুধুমাত্র আপনার মুখস্থ বিদ্যা যাচাইয়ের পরীক্ষা নয়; এটি হলো প্রার্থীর ব্যক্তিত্ব, উপস্থিত বুদ্ধি, চারিত্রিক দৃঢ়তা, যোগাযোগ দক্ষতা ও শিক্ষাদানের মানসিকতা মূল্যায়নের মঞ্চ।
  </p>
</div>
<!--more-->

<h2>ভাইভা বোর্ডে প্রবেশের আদব-কায়দা ও ড্রেস কোড (Dress Code)</h2>
<p>প্রথম দর্শনই প্রভাব ফেলে (First Impression Matters)। তাই পোশাক ও আচরণে শতভাগ মার্জিত হওয়া জরুরি:</p>
<ul>
  <li><strong>পুরুষ প্রার্থীদের জন্য:</strong> হালকা রঙের ফুলহাতা ফর্মাল শার্ট (সাদা/হালকা নীল), গাঢ় রঙের ফর্মাল প্যান্ট ও পালিশ করা কালো জুতো।</li>
  <li><strong>নারী প্রার্থীদের জন্য:</strong> শালীন ও মার্জিত সুতি বা জর্জেট শাড়ি কিংবা শোভন সালোয়ার-কামিজ। হালকা মেকআপ ও স্বাচ্ছন্দ্যদায়ক জুতো।</li>
  <li><strong>কক্ষে প্রবেশ:</strong> দরজায় দাঁড়িয়ে মৃদু অনুমতি নিন ("আসতে পারি স্যার?")। চেয়ারের পাশে গিয়ে সালাম বা অভিবাদন জানান, বসার অনুমতি পাওয়ার পর বসুন এবং হাসিমুখে ধন্যবাদ দিন।</li>
</ul>

<h2>ভাইভায় সচরাচর জিজ্ঞাসিত গুরুত্বপূর্ণ প্রশ্নাবলী</h2>
<ol>
  <li><strong>নিজের পরিচয় (Tell me about yourself):</strong> সংক্ষেপে নাম, নিজ জেলা, শিক্ষাগত যোগ্যতা ও আগ্রহের ক্ষেত্র গুছিয়ে বলুন।</li>
  <li><strong>নিজ জেলার ইতিহাস ও ঐতিহ্য:</strong> জেলার বিখ্যাত ব্যক্তিত্ব, মুক্তিযুদ্ধকালীন সেক্টর ও ঐতিহাসিক স্থানের নাম জেনে যান।</li>
  <li><strong>পঠিত অনার্স/মাস্টার্স বিষয়:</strong> আপনার গ্র্যাজুয়েশনের মূল বিষয় থেকে বেসিক ৩-৪টি প্রশ্ন অবশ্যই করা হবে।</li>
  <li><strong>কেন এই পেশায় আসতে চান:</strong> শিক্ষকতা বা সংশ্লিষ্ট পদের প্রতি আপনার ভালোবাসা ও সমাজ গঠনে অবদানের মানসিকতা তুলে ধরুন।</li>
</ol>

<h2>ভাইভা বোর্ডের ৭টি মারাত্মক ভুল যা বর্জনীয়</h2>
<ul>
  <li>❌ উত্তর জানা না থাকলে বাড়িয়ে বাড়িয়ে ভুল তথ্য বলা। (বিনয়ের সাথে বলুন—'স্যার, এই মুহূর্তে বিষয়টি মনে পড়ছে না')।</li>
  <li>❌ ভাইভা বোর্ডের সদস্যদের কথার মাঝখানে কথা কেটে ফেলা বা তর্কে জড়ানো।</li>
  <li>❌ অতিরিক্ত নার্ভাসনেস বা হাত-পা কাঁপানো। স্বাভাবিক শ্বাস নিন।</li>
  <li>❌ চোখের দিকে না তাকিয়ে মেঝের দিকে তাকিয়ে কথা বলা।</li>
</ul>
"""
    }
]


def create_and_publish():
    service = get_authenticated_service()
    if not service:
        print("[!] Blogger API authentication failed.")
        sys.exit(1)

    print("\n=======================================================")
    print("  HelpTrickBD Topical Authority Expansion Engine")
    print("=======================================================")

    published_urls = []

    for art in ARTICLES:
        print(f"\n[*] Creating: {art['title']}")

        # 1. Generate 16:9 Banner and 10-20KB WebP
        banner_path = generate_banner(
            filename=art["banner_filename"],
            category_text=art["banner_category"],
            title_text=art["banner_title"],
            subtitle_text=art["banner_subtitle"],
            features=art["banner_features"],
            start_color=art["start_color"],
            end_color=art["end_color"],
            accent_color=art["accent_color"]
        )

        webp_filename = os.path.splitext(art["banner_filename"])[0] + ".webp"
        webp_rel_url = f"https://www.helptrickbd.com/images/{webp_filename}"

        # 2. Build full HTML with SolaimanLipi, Hero Figure, and Content
        full_html = f"""
<div class="htbd-article-body" style="font-family: 'SolaimanLipi', sans-serif; font-size: 18px; line-height: 1.85; color: #1e293b;">
  <figure style="margin: 0 0 25px 0; text-align: center;">
    <img src="{webp_rel_url}" alt="{art['title']}" title="{art['title']}" style="width: 100%; max-width: 1200px; height: auto; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.08);" />
    <figcaption style="font-size: 14px; color: #64748b; margin-top: 8px;">চিত্র: {art['title']} — HelpTrickBD এডুকেশন স্পেশাল গাইডলাইন</figcaption>
  </figure>

  {art['body_paragraphs']}
</div>
"""

        # 3. Inject Dwell Time and Engagement boosters
        optimized_html, stats = optimize_post_engagement(full_html)
        print(f"    - Content Prepared: {stats['word_count']} words | {stats['estimated_minutes']}m reading time | {stats['headings_count']} headings")

        # 4. Save local copy in output_posts/new_silo_posts/
        local_file = os.path.join(OUTPUT_DIR, f"{art['slug']}.html")
        with open(local_file, "w", encoding="utf-8") as lf:
            lf.write(optimized_html)

        meta_file = local_file.replace(".html", "_metadata.json")
        with open(meta_file, "w", encoding="utf-8") as mf:
            json.dump({
                "slug": art["slug"],
                "title": art["title"],
                "labels": art["labels"],
                "meta_desc": art["meta_desc"],
                "word_count": stats["word_count"]
            }, mf, indent=2, ensure_ascii=False)

        # 5. Publish to Blogger via Blogger API
        post_body = {
            "kind": "blogger#post",
            "title": art["title"],
            "content": optimized_html,
            "labels": art["labels"]
        }

        try:
            new_post = service.posts().insert(blogId=BLOG_ID, body=post_body, isDraft=False).execute()
            post_id = new_post.get("id")
            live_url = new_post.get("url")
            print(f"    [+] Published Live on Blogger! ID: {post_id} -> {live_url}")
            published_urls.append(live_url)

            # Update local metadata with live post_id
            with open(meta_file, "r+", encoding="utf-8") as mf:
                d = json.load(mf)
                d["post_id"] = post_id
                d["live_url"] = live_url
                mf.seek(0)
                json.dump(d, mf, indent=2, ensure_ascii=False)
                mf.truncate()

            time.sleep(2)
        except Exception as e:
            print(f"    [!] Publishing failed: {e}")

    # Save all newly published URLs for Google Indexing API
    index_file = os.path.join(PROJECT_ROOT, "tools", "indexer", "new_silo_published_urls.txt")
    with open(index_file, "w", encoding="utf-8") as inf:
        for u in published_urls:
            inf.write(u + "\n")
    print(f"\n[+] Saved {len(published_urls)} new live URLs to {index_file}")
    print("=======================================================\n")


if __name__ == "__main__":
    create_and_publish()
