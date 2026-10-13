#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/pdf/generate_ntrca_pdf.py
--------------------------------
Generates official, textbook-grade HelpTrickBD branded PDFs for NTRCA syllabus
using Chromium Headless with 100% perfect SolaimanLipi / Noto Sans Bengali typography.
"""

import os
import sys
import subprocess
import json

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
PDF_OUTPUT_DIR = os.path.join(PROJECT_ROOT, "assets", "pdf", "ntrca")
os.makedirs(PDF_OUTPUT_DIR, exist_ok=True)

def get_chromium_executable():
    chrome_candidates = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"
    ]
    for c in chrome_candidates:
        if os.path.exists(c):
            return c
    raise FileNotFoundError("Chromium / Chrome / Edge executable not found.")

def build_school_syllabus_pdf():
    pdf_filename = "ntrca_school_level_assistant_teacher_syllabus_2026.pdf"
    pdf_path = os.path.join(PDF_OUTPUT_DIR, pdf_filename)
    temp_html_path = os.path.join(PROJECT_ROOT, "scratch", "ntrca_school_syllabus_print.html")

    html_content = """<!DOCTYPE html>
<html lang="bn">
<head>
<meta charset="UTF-8">
<title>NTRCA সহকারী শিক্ষক পূর্ণাঙ্গ সিলেবাস ২০২৬ | HelpTrickBD Official PDF</title>
<style>
  @import url('https://fonts.maateen.me/solaiman-lipi/font.css');
  @page {
    size: A4;
    margin: 18mm 14mm 18mm 14mm;
    @top-center {
      content: "HelpTrickBD.com • শিক্ষক নিবন্ধন (NTRCA) স্কুল পর্যায় পূর্ণাঙ্গ সিলেবাস ও মানবণ্টন";
      font-family: 'SolaimanLipi', sans-serif;
      font-size: 9.5pt;
      color: #0f766e;
    }
    @bottom-center {
      content: "Downloaded from www.helptrickbd.com | সর্বস্বত্ব সংরক্ষিত ২০২৬ HelpTrickBD";
      font-family: 'SolaimanLipi', sans-serif;
      font-size: 8.5pt;
      color: #64748b;
    }
  }
  body {
    font-family: 'SolaimanLipi', 'Noto Sans Bengali', sans-serif;
    color: #1e293b;
    margin: 0;
    padding: 0;
    line-height: 1.6;
    font-size: 13pt;
  }
  .header-card {
    background: linear-gradient(135deg, #0f766e 0%, #115e59 100%);
    color: #ffffff;
    padding: 22px 24px;
    border-radius: 8px;
    margin-bottom: 22px;
  }
  .header-card h1 {
    font-size: 21pt;
    margin: 0 0 6px 0;
    font-weight: 700;
  }
  .header-card .badge {
    display: inline-block;
    background: #f59e0b;
    color: #000000;
    font-size: 9.5pt;
    font-weight: 700;
    padding: 3px 10px;
    border-radius: 12px;
    margin-bottom: 8px;
    text-transform: uppercase;
  }
  .header-card .meta {
    font-size: 11pt;
    color: #ccfbf1;
    margin-top: 4px;
  }
  .notice-box {
    background: #f0fdfa;
    border-left: 4px solid #0f766e;
    padding: 12px 16px;
    border-radius: 0 6px 6px 0;
    margin-bottom: 18px;
    font-size: 11.5pt;
    color: #134e4a;
  }
  h2.section-title {
    font-size: 15pt;
    font-weight: 700;
    color: #0f766e;
    margin: 22px 0 10px 0;
    border-bottom: 2px solid #e2e8f0;
    padding-bottom: 5px;
    page-break-after: avoid;
  }
  h3.sub-title {
    font-size: 13pt;
    font-weight: 700;
    color: #1e293b;
    margin: 14px 0 6px 0;
    page-break-after: avoid;
  }
  table {
    width: 100%;
    border-collapse: collapse;
    margin: 14px 0;
    font-size: 11pt;
    page-break-inside: avoid;
  }
  th {
    background: #0f766e;
    color: #ffffff;
    padding: 8px 10px;
    text-align: left;
    border: 1px solid #0d9488;
  }
  td {
    padding: 8px 10px;
    border: 1px solid #cbd5e1;
  }
  tr:nth-child(even) {
    background: #f8fafc;
  }
  ul {
    margin: 6px 0 14px 20px;
    padding: 0;
  }
  li {
    margin-bottom: 5px;
  }
  .page-break {
    page-break-before: always;
  }
</style>
</head>
<body>

<!-- Header Banner -->
<div class="header-card">
  <span class="badge">অফিসিয়াল সিলেবাস ২০২৬</span>
  <h1>NTRCA স্কুল পর্যায় সহকারী শিক্ষক পূর্ণাঙ্গ সিলেবাস ও মানবণ্টন ২০২৬</h1>
  <div class="meta">বেসরকারি শিক্ষক নিবন্ধন ও প্রত্যয়ন কর্তৃপক্ষ (NTRCA) • স্কুল ও মাদ্রাসা পর্যায়</div>
  <div class="meta">প্রস্তুতকারক: ফারুক স্যার (মো. ওমর ফারুক), শিক্ষাবিদ ও অ্যাকাডেমিক গবেষক | প্রতিষ্ঠাতা, HelpTrickBD</div>
</div>

<div class="notice-box">
  <strong>সংক্ষিপ্ত রূপরেখা:</strong> এনটিআরসিএ কর্তৃক অনুমোদিত সর্বশেষ রূপরেখা অনুযায়ী স্কুল পর্যায়ের সহকারী শিক্ষক পদে প্রিলিমিনারি ১০০ নম্বরের এমসিকিউ এবং বিষয়ভিত্তিক ১০০ নম্বরের লিখিত পরীক্ষা অনুষ্ঠিত হয়। লিখিত পরীক্ষার প্রতিটি পদের বিষয়ভিত্তিক বিস্তারিত সিলেবাস ও মানবণ্টন নিচে সংকলিত হলো।
</div>

<h2 class="section-title">১. প্রশ্নের ব্লুমস ট্যাক্সোনমি (Bloom's Taxonomy) মানবণ্টন কাঠামো</h2>
<p>এনটিআরসিএ-এর লিখিত পরীক্ষায় প্রশ্নের মেধা যাচাইয়ের জন্য নিচের আন্তর্জাতিক ব্লুমস ট্যাক্সোনমি কাঠামো কঠোরভাবে অনুসরণ করা হয়:</p>
<table>
  <thead>
    <tr>
      <th style="width: 25%;">দক্ষতার ক্ষেত্র</th>
      <th style="width: 45%;">প্রশ্নের প্রকৃতি ও বিশ্লেষণ</th>
      <th style="width: 15%;">শতকরা হার</th>
      <th style="width: 15%;">মূল্যায়ন পর্যায়</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>জ্ঞান (Knowledge)</strong></td>
      <td>মৌলিক তথ্য, সংজ্ঞা, সূত্র ও পারিভাষিক অর্থ</td>
      <td>৪০%</td>
      <td>প্রিলি / লিখিত</td>
    </tr>
    <tr>
      <td><strong>অনুধাবন (Understanding)</strong></td>
      <td>মূলভাব ব্যাখ্যা, তুলনামূলক পার্থক্য ও সারসংক্ষেপ</td>
      <td>৩০%</td>
      <td>লিখিত পরীক্ষা</td>
    </tr>
    <tr>
      <td><strong>প্রয়োগ (Application)</strong></td>
      <td>বাস্তব সমস্যা সমাধান, ব্যাকরণ ও গাণিতিক প্রয়োগ</td>
      <td>২০%</td>
      <td>লিখিত পরীক্ষা</td>
    </tr>
    <tr>
      <td><strong>উচ্চতর দক্ষতা (Higher Order)</strong></td>
      <td>সৃজনশীল বিশ্লেষণ, মূল্যায়ন ও যৌক্তিক সিদ্ধান্ত গ্রহণ</td>
      <td>১০%</td>
      <td>লিখিত ও ভাইভা</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">২. সহকারী শিক্ষক (বাংলা) লিখিত সিলেবাস</h2>
<ul>
  <li><strong>ক. বাংলা সাহিত্যের ইতিহাস:</strong> প্রাচীন যুগ (চর্যাপদ ও আদি নিদর্শন), মধ্যযুগ (শ্রীকৃষ্ণকীর্তন, মঙ্গলকাব্য, বৈষ্ণব পদাবলী, অনুবাদ সাহিত্য, আরাকান রাজসভা) এবং আধুনিক যুগ (ফোর্ট উইলিয়াম কলেজ, মাইকেল মধুসূদন দত্ত, বঙ্কিমচন্দ্র, রবীন্দ্রনাথ ঠাকুর, কাজী নজরুল ইসলাম, জসীমউদ্দীন ও জীবনানন্দ দাশ)।</li>
  <li><strong>খ. বাংলা ব্যাকরণ:</strong> ধ্বনি ও বর্ণ প্রকরণ, সন্ধি, ণ-ত্ব ও ষ-ত্ব বিধান, সমাস, প্রত্যয়, উপসর্গ, অনুসর্গ, পদ প্রকরণ ও রূপান্তর, বাচ্য ও বাক্য পরিবর্তন।</li>
  <li><strong>গ. প্রায়োগিক বাংলা:</strong> বাগধারা, প্রবাদ-প্রবচন, সমার্থক ও বিপরীতার্থক শব্দ, বিরাম চিহ্নের সঠিক ব্যবহার এবং অশুদ্ধি সংশোধন।</li>
  <li><strong>ঘ. সাহিত্যিক বিশ্লেষণ:</strong> নির্বাচিত কবিতা, গল্প ও উপন্যাসের মূলভাব অনুধাবন এবং চরিত্র মূল্যায়ন।</li>
</ul>

<h2 class="section-title">৩. সহকারী শিক্ষক (বাধ্যতামূলক ইংরেজি) সিলেবাস</h2>
<ul>
  <li><strong>Grammar & Usage:</strong> Parts of Speech identification & usage, Tense, Subject-Verb Agreement, Right form of Verbs, Voice Change, Narration (Direct & Indirect), Conditionals, Tag Questions, Modifiers.</li>
  <li><strong>Prepositions & Vocabulary:</strong> Appropriate Prepositions, Idioms & Phrases, Synonyms, Antonyms, One-word substitution, Spelling accuracy.</li>
  <li><strong>Transformation of Sentences:</strong> Simple, Complex & Compound transformations, Affirmative-Negative, Assertive-Interrogative-Exclamatory, Degree changes.</li>
  <li><strong>Reading & Writing Skills:</strong> Comprehension Passage analysis, Theme writing, Letter/Application writing principles, Report writing basics.</li>
</ul>

<div class="page-break"></div>

<h2 class="section-title">৪. সহকারী শিক্ষক (গণিত) লিখিত সিলেবাস</h2>
<table>
  <thead>
    <tr>
      <th style="width: 25%;">শাখা</th>
      <th style="width: 75%;">অন্তর্ভুক্ত বিষয়বস্তু ও অধ্যায়সমূহ</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>পাটিগণিত</strong></td>
      <td>বাস্তব সংখ্যা, ল.সা.গু ও গ.সা.গু, শতকরা, লাভ-ক্ষতি, সরল ও চক্রবৃদ্ধি সুদ, অনুপাত-সমানুপাত, ঐকিক নিয়ম এবং দূরত্ব-সময় ও গতির হিসাব।</td>
    </tr>
    <tr>
      <td><strong>বীজগণিত</strong></td>
      <td>বীজগাণিতিক সূত্রাবলি ও উৎপাদক, সূচক ও লগারিদম, সরল ও দ্বিঘাত সমীকরণ, অসমতা, সমান্তর ও গুণোত্তর ধারা, সেট ও ফাংশন।</td>
    </tr>
    <tr>
      <td><strong>জ্যামিতি</strong></td>
      <td>রেখা, কোণ, ত্রিভুজ ও চতুর্ভুজের উপপাদ্য, পিথাগোরাসের উপপাদ্য, বৃত্ত সংক্রান্ত উপপাদ্য এবং স্পর্শক।</td>
    </tr>
    <tr>
      <td><strong>পরিমিতি ও ত্রিকোণমিতি</strong></td>
      <td>ত্রিভুজ, চতুর্ভুজ ও বৃত্তক্ষেত্রের ক্ষেত্রফল নির্ণয়; ত্রিকোণমিতিক অনুপাত, কোণ ও উচ্চতা এবং দূরত্বের ব্যবহারিক সমস্যা।</td>
    </tr>
  </tbody>
</table>

<h2 class="section-title">৫. সহকারী শিক্ষক (তথ্য ও যোগাযোগ প্রযুক্তি - আইসিটি) লিখিত সিলেবাস (১৪০ নম্বর কাঠামো)</h2>
<p>আইসিটি বিষয়ের লিখিত পরীক্ষায় মোট ১৪০ নম্বরের প্রশ্ন থাকবে। নিম্নের প্রতিটি ইউনিট থেকে ন্যূনতম ৮টি করে প্রশ্ন প্রণয়ন করা হবে:</p>
<table>
  <thead>
    <tr>
      <th style="width: 30%;">ইউনিট নম্বর ও শিরোনাম</th>
      <th style="width: 70%;">প্রধান বিষয়বস্তু</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Unit 1: Fundamentals of Computer</strong></td>
      <td>Computer Architecture, CPU, Memory Hierarchy (RAM, ROM, Cache), Input/Output devices.</td>
    </tr>
    <tr>
      <td><strong>Unit 2: Logic Design & Number System</strong></td>
      <td>Binary, Octal, Hexadecimal conversions, Boolean Algebra, Logic Gates (AND, OR, NOT, NAND, NOR, XOR, XNOR).</td>
    </tr>
    <tr>
      <td><strong>Unit 3: Electrical Circuits</strong></td>
      <td>Ohm's Law, Kirchhoff's Laws, Semiconductor basics, Diodes & Transistors.</td>
    </tr>
    <tr>
      <td><strong>Unit 4: Data Structure & Algorithms</strong></td>
      <td>Array, Linked List, Stack, Queue, Tree, Binary Search, Bubble/Quick Sort, Time Complexity.</td>
    </tr>
    <tr>
      <td><strong>Unit 5: Computer Programming</strong></td>
      <td>C Programming syntax, Variables, Data Types, Control Structures, Functions, Pointers.</td>
    </tr>
    <tr>
      <td><strong>Unit 6: Database Management (DBMS)</strong></td>
      <td>RDBMS concepts, Primary/Foreign Key, Normalization (1NF, 2NF, 3NF), SQL Queries (SELECT, INSERT, UPDATE, JOIN).</td>
    </tr>
    <tr>
      <td><strong>Unit 7: Computer Networks</strong></td>
      <td>OSI 7 Layers, TCP/IP, Topologies (Star, Mesh, Bus), IP Addressing, Subnetting, Routing basics.</td>
    </tr>
    <tr>
      <td><strong>Unit 8: Security & Ethical Issues</strong></td>
      <td>Malware, Firewalls, Encryption basics, Cyber Law, Intellectual Property, Ethics in IT.</td>
    </tr>
    <tr>
      <td><strong>Unit 9: Software Engineering</strong></td>
      <td>SDLC models (Waterfall, Agile), Testing, Maintenance, UML Diagrams.</td>
    </tr>
    <tr>
      <td><strong>Unit 10: Artificial Intelligence</strong></td>
      <td>AI overview, Machine Learning basics, Neural Networks concept, Natural Language Processing.</td>
    </tr>
    <tr>
      <td><strong>Unit 11: Emerging Technology</strong></td>
      <td>Cloud Computing (SaaS, PaaS, IaaS), IoT (Internet of Things), Big Data, Blockchain.</td>
    </tr>
    <tr>
      <td><strong>Unit 12: Real-world Applications</strong></td>
      <td>E-Commerce, Smart Education, Digital Governance, Automation in daily life.</td>
    </tr>
  </tbody>
</table>

<div class="page-break"></div>

<h2 class="section-title">৬. সহকারী শিক্ষক (ভৌতবিজ্ঞান - পদার্থ ও রসায়ন)</h2>
<ul>
  <li><strong>পদার্থবিজ্ঞান অংশ:</strong> বল ও গতি (নিউটনের গতিসূত্র, ভরবেগ), কাজ, ক্ষমতা ও শক্তি, মহাকর্ষ ও অভিকর্ষ, পদার্থের অবস্থা ও চাপ, শব্দ তরঙ্গ ও প্রতিধ্বনি, আলো (প্রতিফলন, প্রতিসরণ, লেন্স), চলবিদ্যুৎ ও স্থির তড়িৎ (ওহমের সূত্র, রোধের বর্তনী) এবং আধুনিক পদার্থবিজ্ঞানের সূচনা।</li>
  <li><strong>রসায়ন অংশ:</strong> পদার্থের গঠন, পরমাণুর মডেল ও কোয়ান্টাম ধারণা, পর্যায় সারণি ও মৌলের পর্যায়বৃত্ত ধর্ম, রাসায়নিক বন্ধন (আয়নিক, সমযোজী), রাসায়নিক গণনা ও মোল ধারণা, এসিড-ক্ষারক সমতা ও pH মান, জারণ-বিজারণ বিক্রিয়া এবং হাইড্রোকার্বন ও জৈব রসায়নের পরিচিতি।</li>
</ul>

<h2 class="section-title">৭. সহকারী শিক্ষক (সামাজিক বিজ্ঞান)</h2>
<ul>
  <li><strong>বাংলাদেশের ইতিহাস ও মুক্তিযুদ্ধ:</strong> প্রাচীন বাংলা, সুলতানি ও মুঘল আমল, ব্রিটিশ বিরোধী আন্দোলন, ১৯৫২-এর ভাষা আন্দোলন, ১৯৬৬-এর ৬ দফা, ১৯৬৯-এর গণঅভ্যুত্থান এবং ১৯৭১ সালের মহান মুক্তিযুদ্ধ।</li>
  <li><strong>পৌরনীতি ও সুশাসন:</strong> নাগরিক অধিকার ও কর্তব্য, সংবিধানের মৌলিক বৈশিষ্ট্য, সরকারের অঙ্গসমূহ (আইন, শাসন ও বিচার বিভাগ), স্থানীয় সরকার ও গণতন্ত্র।</li>
  <li><strong>অর্থনীতি ও ভূগোল:</strong> বাংলাদেশের প্রাকৃতিক ভূগোল, নদী ব্যবস্থা, জনসংখ্যা ও মানবসম্পদ উন্নয়ন, দারিদ্র্য বিমোচন ও টেকসই উন্নয়ন লক্ষ্যমাত্রা (SDG)।</li>
</ul>

<h2 class="section-title">৮. সহকারী শিক্ষক (ব্যবসায় শিক্ষা)</h2>
<ul>
  <li><strong>হিসাববিজ্ঞান:</strong> দু'তরফা দাখিলা পদ্ধতি, জাবেদা, খতিয়ান, রেওয়ামিল, কার্যপত্র, চূড়ান্ত হিসাব ও আর্থিক বিবরণী বিশ্লেষণ, ব্যাংক সমন্বয় বিবরণী এবং অবচয় হিসাব।</li>
  <li><strong>ব্যবসায় সংগঠন ও ব্যবস্থাপনা:</strong> একমালিকানা, অংশীদারি ও যৌথ মূলধনী ব্যবসায়, ব্যবস্থাপনার নীতি ও কার্যাবলি, প্রেষণা ও নেতৃত্ব।</li>
  <li><strong>ফিন্যান্স ও ব্যাংকিং:</strong> অর্থের সময়মূল্য, মূলধন বাজেটিং, ব্যাংকিং ব্যবস্থার প্রকারভেদ ও বাণিজ্যিক ব্যাংকের কার্যাবলি।</li>
</ul>

<h2 class="section-title">৯. সহকারী শিক্ষক (কৃষি শিক্ষা ও লাইব্রেরি সায়েন্স)</h2>
<ul>
  <li><strong>কৃষি শিক্ষা:</strong> বাংলাদেশের কৃষি অঞ্চল ও মাটির উর্বরতা, বীজ সংরক্ষণ প্রযুক্তি, মাঠ ফসল ও উদ্যান ফসল চাষ, মাছ চাষ ও আধুনিক পোল্ট্রি খামার ব্যবস্থাপনা।</li>
  <li><strong>গ্রন্থাগার ও তথ্য বিজ্ঞান:</strong> লাইব্রেরি ম্যানেজমেন্ট সিস্টেম, ডিউই ডেসিমাল ক্লাসিফিকেশন (DDC), ক্যাটালগিং কোড (AACR-2) এবং ডিজিটাল লাইব্রেরি সফটওয়্যার (Koha, DSpace)।</li>
</ul>

<h2 class="section-title">১০. সহকারী শিক্ষক (ইসলাম, হিন্দু ও বৌদ্ধ ধর্ম শিক্ষা)</h2>
<ul>
  <li><strong>ইসলাম শিক্ষা:</strong> আকাইদ (তাওহীদ, রিসালাত, আখিরাত), পবিত্র কুরআন তিলাওয়াত ও নির্দিষ্ট সূরার তাফসির, হাদিস পরিচিতি ও ফিকহ শাস্ত্রের মৌলিক বিধান।</li>
  <li><strong>হিন্দু ধর্ম শিক্ষা:</strong> বৈদিক সাহিত্য, উপনিষদ, শ্রীমদ্ভগবদ্গীতা, ধর্মাচরণ, নীতিশাস্ত্র এবং দেবদেবী পূজা বিধি।</li>
  <li><strong>বৌদ্ধ ধর্ম শিক্ষা:</strong> চতুরার্য সত্য, অষ্টাঙ্গিক মার্গ, ত্রিপিটক (সূত্র, বিনয় ও অভিধর্ম পিটক) ও বৌদ্ধ দর্শন।</li>
</ul>

<div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 6px; padding: 14px 18px; margin-top: 25px; font-size: 11pt;">
  <strong style="color: #0f766e;">💡 পরীক্ষার সেরা প্রস্তুতির বিশেষ টিপস:</strong>
  <p style="margin: 5px 0 0 0; color: #475569;">
    লিখিত পরীক্ষায় প্রতিটি উত্তরের শুরুতে একটি পরিষ্কার সংজ্ঞা ও শেষে বুলেট পয়েন্টে বাস্তব উদাহরণ দিলে পরীক্ষক সর্বোচ্চ নম্বর প্রদান করেন। গণিত ও বিজ্ঞানে রাফ খসড়া স্পষ্ট রাখবেন এবং আইসিটি অংশে প্রয়োজনীয় ব্লক ডায়াগ্রাম বা ফ্লোচার্ট ব্যবহার করবেন।
  </p>
</div>

</body>
</html>
"""

    with open(temp_html_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    chrome = get_chromium_executable()
    cmd = [
        chrome,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--run-all-compositor-stages-before-draw",
        f"--print-to-pdf={pdf_path}",
        "--print-to-pdf-no-header",
        temp_html_path
    ]

    print(f"[*] Compiling School Syllabus PDF using Chromium: {pdf_path} ...")
    subprocess.run(cmd, check=True)
    file_size_kb = os.path.getsize(pdf_path) / 1024
    print(f"[SUCCESS] PDF generated: {pdf_path} ({file_size_kb:.1f} KB)")
    return pdf_path

if __name__ == "__main__":
    build_school_syllabus_pdf()
