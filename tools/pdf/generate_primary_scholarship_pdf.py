import os
import sys
import subprocess

sys.stdout.reconfigure(encoding='utf-8')

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
PDF_OUTPUT_DIR = os.path.join(PROJECT_ROOT, "assets", "pdf", "primary")
os.makedirs(PDF_OUTPUT_DIR, exist_ok=True)
SCRATCH_DIR = os.path.join(PROJECT_ROOT, "scratch")
os.makedirs(SCRATCH_DIR, exist_ok=True)

pdf_filename = "primary_scholarship_exam_routine_2026.pdf"
pdf_path = os.path.join(PDF_OUTPUT_DIR, pdf_filename)
temp_html_path = os.path.join(SCRATCH_DIR, "primary_scholarship_routine_print.html")

chrome_candidates = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"
]
chrome_bin = None
for c in chrome_candidates:
    if os.path.exists(c):
        chrome_bin = c
        break

if not chrome_bin:
    raise FileNotFoundError("Browser binary not found for PDF rendering.")

html_content = """<!DOCTYPE html>
<html lang="bn">
<head>
<meta charset="UTF-8">
<title>প্রাথমিক বৃত্তি পরীক্ষার রুটিন 2026 | HelpTrickBD Official PDF</title>
<style>
  @page {
    size: A4 portrait;
    margin: 15mm 14mm 15mm 14mm;
  }
  body {
    font-family: 'SolaimanLipi', 'Hind Siliguri', Arial, sans-serif;
    color: #1e293b;
    line-height: 1.6;
    margin: 0;
    padding: 0;
    background: #ffffff;
  }
  .header-box {
    text-align: center;
    border-bottom: 2.5px solid #0f766e;
    padding-bottom: 12px;
    margin-bottom: 20px;
  }
  .govt-title {
    font-size: 16pt;
    font-weight: bold;
    color: #0f766e;
    margin: 0 0 4px 0;
  }
  .sub-title {
    font-size: 11pt;
    color: #334155;
    margin: 0 0 2px 0;
  }
  .doc-title {
    font-size: 14pt;
    font-weight: bold;
    color: #115e59;
    margin-top: 10px;
    background: #f0fdfa;
    display: inline-block;
    padding: 6px 20px;
    border-radius: 6px;
    border: 1px solid #99f6e4;
  }
  .info-bar {
    display: flex;
    justify-content: space-between;
    font-size: 10pt;
    color: #475569;
    margin-bottom: 15px;
    border-bottom: 1px dashed #cbd5e1;
    padding-bottom: 6px;
  }
  table {
    width: 100%;
    border-collapse: collapse;
    margin: 16px 0;
    font-size: 10.5pt;
  }
  th, td {
    border: 1px solid #cbd5e1;
    padding: 9px 12px;
    text-align: left;
  }
  th {
    background: #0f766e;
    color: #ffffff;
    font-weight: bold;
    text-align: center;
  }
  tr:nth-child(even) {
    background: #f8fafc;
  }
  .center {
    text-align: center;
  }
  .bold {
    font-weight: bold;
  }
  .badge {
    background: #ccfbf1;
    color: #0f766e;
    padding: 3px 8px;
    border-radius: 4px;
    font-weight: bold;
    font-size: 9pt;
  }
  .section-heading {
    font-size: 12pt;
    font-weight: bold;
    color: #0f766e;
    margin: 18px 0 8px 0;
    border-left: 4px solid #0f766e;
    padding-left: 8px;
  }
  ul, ol {
    margin: 6px 0 14px 20px;
    padding: 0;
    font-size: 10pt;
    color: #334155;
  }
  li {
    margin-bottom: 5px;
  }
  .callout-box {
    background: #f0fdfa;
    border: 1px solid #99f6e4;
    border-radius: 6px;
    padding: 12px 16px;
    margin: 16px 0;
    font-size: 10pt;
  }
  .footer-box {
    margin-top: 25px;
    border-top: 1px solid #e2e8f0;
    padding-top: 10px;
    display: flex;
    justify-content: space-between;
    font-size: 8.5pt;
    color: #64748b;
  }
</style>
</head>
<body>

<div class="header-box">
  <div class="govt-title">গণপ্রজাতন্ত্রী বাংলাদেশ সরকার</div>
  <div class="sub-title">প্রাথমিক শিক্ষা অধিদপ্তর, সেকশন-২, মিরপুর, ঢাকা-১২১৬</div>
  <div class="sub-title">www.dpe.gov.bd • প্রকাশকাল: ১৭ অক্টোবর ২০২৬</div>
  <div class="doc-title">প্রাথমিক বৃত্তি পরীক্ষা ২০২৬-এর অফিশিয়াল সময়সূচি ও নির্দেশিকা</div>
</div>

<div class="info-bar">
  <span><strong>পরীক্ষার স্তর:</strong> প্রাথমিক স্তর (৫ম শ্রেণি)</span>
  <span><strong>মোট নম্বর:</strong> ১০০ নম্বর (৪ বিষয়)</span>
  <span><strong>পরীক্ষার সময়:</strong> প্রতিদিন সকাল ১০:০০ টা – দুপুর ১২:৩০ টা</span>
</div>

<div class="section-heading">১. প্রাথমিক বৃত্তি পরীক্ষা ২০২৬-এর চূড়ান্ত সময়সূচি (Exam Routine)</div>
<table>
  <thead>
    <tr>
      <th style="width: 18%;">তারিখ ও বার</th>
      <th style="width: 25%;">পরীক্ষার সময়</th>
      <th style="width: 32%;">বিষয়</th>
      <th style="width: 15%;">পূর্ণমান</th>
      <th style="width: 10%;">স্ট্যাটাস</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="bold center">২০ ডিসেম্বর ২০২৬<br>(রবিবার)</td>
      <td class="center">সকাল ১০:০০ টা হতে দুপুর ১২:৩০ টা</td>
      <td class="bold">বাংলা</td>
      <td class="center bold">২৫ নম্বর</td>
      <td class="center"><span class="badge">আবশ্যিক</span></td>
    </tr>
    <tr>
      <td class="bold center">২১ ডিসেম্বর ২০২৬<br>(সোমবার)</td>
      <td class="center">সকাল ১০:০০ টা হতে দুপুর ১২:৩০ টা</td>
      <td class="bold">ইংরেজি</td>
      <td class="center bold">২৫ নম্বর</td>
      <td class="center"><span class="badge">আবশ্যিক</span></td>
    </tr>
    <tr>
      <td class="bold center">২২ ডিসেম্বর ২০২৬<br>(মঙ্গলবার)</td>
      <td class="center">সকাল ১০:০০ টা হতে দুপুর ১২:৩০ টা</td>
      <td class="bold">প্রাথমিক গণিত</td>
      <td class="center bold">২৫ নম্বর</td>
      <td class="center"><span class="badge">আবশ্যিক</span></td>
    </tr>
    <tr>
      <td class="bold center">২৩ ডিসেম্বর ২০২৬<br>(বুধবার)</td>
      <td class="center">সকাল ১০:০০ টা হতে দুপুর ১২:৩০ টা</td>
      <td class="bold">বাংলাদেশ ও বিশ্বপরিচয় এবং প্রাথমিক বিজ্ঞান</td>
      <td class="center bold">২৫ নম্বর<br><small>(১২.৫ + ১২.৫)</small></td>
      <td class="center"><span class="badge">আবশ্যিক</span></td>
    </tr>
  </tbody>
</table>

<div class="callout-box">
  <strong>বিশেষ নির্দেশনা (সময় ও ফি):</strong><br>
  ১. প্রতিদিনের পরীক্ষার সময়কাল ২ ঘণ্টা ৩০ মিনিট। তবে বিশেষ চাহিদাসম্পন্ন (প্রতিবন্ধী) শিক্ষার্থীদের জন্য অতিরিক্ত ৩০ মিনিট সময় দেওয়া হবে।<br>
  ২. প্রাথমিক শিক্ষা অধিদপ্তরের স্পষ্ট আদেশ অনুযায়ী—<strong>শিক্ষার্থীদের কাছ থেকে পরীক্ষার জন্য কোনো প্রকার ফি গ্রহণ করা সম্পূর্ণ নিষিদ্ধ।</strong>
</div>

<div class="section-heading">২. বিষয়ভিত্তিক প্রশ্ন কাঠামো ও মানবণ্টন (Marks Distribution)</div>
<ul>
  <li><strong>বাংলা (২৫ নম্বর):</strong> গদ্যাংশ ও পদ্যাংশ থেকে অনুধাবনমূলক প্রশ্ন, যুক্তবর্ণ বিভাজন ও বাক্য তৈরি, শব্দার্থ, বাক্য সংকোচন এবং সংক্ষিপ্ত অনুচ্ছেদ লিখন।</li>
  <li><strong>ইংরেজি (২৫ নম্বর):</strong> Seen & Unseen Passage Comprehension, Wh-questions, Fill in the blanks with correct forms, এবং একটি 5-sentence Short Composition.</li>
  <li><strong>প্রাথমিক গণিত (২৫ নম্বর):</strong> যোগ্যতাভিত্তিক ৪ প্রক্রিয়া সম্পর্কিত সমস্যা সমাধান, ভগ্নাংশ ও দশমিক, গড় ও শতকরা, জ্যামিতিক চিত্র ও পরিমাপ সংক্রান্ত প্রায়োগিক সমস্যা।</li>
  <li><strong>বিজ্ঞান ও বিশ্বপরিচয় (২৫ নম্বর):</strong> পরিবেশ দূষণ, সুস্থ জীবনযাপন, জনসংখ্যা ও প্রাকৃতিক সম্পদ, মুক্তিযুদ্ধ ও বাংলাদেশের ঐতিহ্য সম্পর্কিত সংক্ষিপ্ত ও বর্ণনামূলক প্রশ্ন।</li>
</ul>

<div class="section-heading">৩. কোটা ও অংশগ্রহণের যোগ্যতা</div>
<ul>
  <li>প্রতিটি প্রাথমিক বিদ্যালয়ের ৫ম শ্রেণির বার্ষিক পরীক্ষায় অংশগ্রহণকারী সর্বোচ্চ ২০% মেধাবী শিক্ষার্থী এই বৃত্তি পরীক্ষায় অংশগ্রহণের যোগ্য বলে বিবেচিত হবে।</li>
  <li>ট্যালেন্টপুল ও সাধারণ—উভয় ক্যাটাগরিতে উপজেলা ও থানাভিত্তিক কোটা অনুযায়ী মেধা তালিকা প্রণয়ন করা হবে।</li>
</ul>

<div class="footer-box">
  <span>অফিসিয়াল ডকুমেন্ট সংকলন: HelpTrickBD স্মার্ট এডুকেশন প্ল্যাটফর্ম</span>
  <span>www.helptrickbd.com • সর্বস্বত্ব সংরক্ষিত ২০২৬</span>
</div>

</body>
</html>
"""

with open(temp_html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"[*] Rendering PDF via Chromium: {pdf_path}...")
cmd = [
    chrome_bin,
    "--headless=new",
    "--disable-gpu",
    "--no-pdf-header-footer",
    f"--print-to-pdf={pdf_path}",
    temp_html_path
]
subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

if os.path.exists(pdf_path):
    print(f"[SUCCESS] PDF Generated: {pdf_path} ({os.path.getsize(pdf_path)} bytes)")
else:
    print("[ERROR] PDF generation failed!")
    sys.exit(1)

if os.path.exists(temp_html_path):
    os.remove(temp_html_path)
