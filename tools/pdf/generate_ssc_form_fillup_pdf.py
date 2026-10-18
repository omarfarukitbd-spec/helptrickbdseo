import os
import sys
import subprocess

sys.stdout.reconfigure(encoding='utf-8')

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
PDF_OUTPUT_DIR = os.path.join(PROJECT_ROOT, "assets", "pdf", "ssc")
os.makedirs(PDF_OUTPUT_DIR, exist_ok=True)
SCRATCH_DIR = os.path.join(PROJECT_ROOT, "scratch")
os.makedirs(SCRATCH_DIR, exist_ok=True)

pdf_filename = "ssc_2027_test_exam_form_fill_up_notice.pdf"
pdf_path = os.path.join(PDF_OUTPUT_DIR, pdf_filename)
temp_html_path = os.path.join(SCRATCH_DIR, "ssc_form_fillup_notice_print.html")

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
<title>২০২৭ সালের এসএসসি পরীক্ষার ফরম পূরণ ও ফি নির্দেশিকা | HelpTrickBD Official PDF</title>
<style>
  @page {
    size: A4 portrait;
    margin: 14mm 14mm 14mm 14mm;
  }
  body {
    font-family: 'SolaimanLipi', 'Hind Siliguri', Arial, sans-serif;
    color: #1e293b;
    line-height: 1.55;
    margin: 0;
    padding: 0;
    background: #ffffff;
  }
  .header-box {
    text-align: center;
    border-bottom: 2.5px solid #0f766e;
    padding-bottom: 10px;
    margin-bottom: 14px;
  }
  .board-title {
    font-size: 16pt;
    font-weight: 800;
    color: #0f766e;
    margin: 0 0 2px 0;
  }
  .address-title {
    font-size: 9.5pt;
    color: #475569;
    margin: 0 0 4px 0;
  }
  .memo-line {
    display: flex;
    justify-content: space-between;
    font-size: 9.5pt;
    color: #334155;
    margin-top: 6px;
    font-weight: 600;
  }
  .notice-banner {
    background: #f0fdfa;
    border: 1.5px solid #0f766e;
    border-radius: 6px;
    padding: 8px 12px;
    text-align: center;
    margin-bottom: 14px;
  }
  .notice-title {
    font-size: 13pt;
    font-weight: 800;
    color: #115e59;
    margin: 0 0 3px 0;
  }
  .notice-subtitle {
    font-size: 9.5pt;
    color: #334155;
    margin: 0;
    font-weight: 600;
  }
  .body-intro {
    font-size: 9.5pt;
    text-align: justify;
    margin-bottom: 12px;
    line-height: 1.6;
  }
  table.data-table {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 14px;
    font-size: 9pt;
  }
  table.data-table th, table.data-table td {
    border: 1px solid #94a3b8;
    padding: 6px 8px;
  }
  table.data-table th {
    background-color: #0f766e;
    color: #ffffff;
    font-weight: 700;
    text-align: center;
  }
  table.data-table tr:nth-child(even) {
    background-color: #f8fafc;
  }
  .instructions-box {
    background-color: #f8fafc;
    border: 1px solid #cbd5e1;
    border-left: 4px solid #f59e0b;
    border-radius: 4px;
    padding: 10px 14px;
    margin-bottom: 16px;
  }
  .instructions-title {
    font-size: 10pt;
    font-weight: 700;
    color: #b45309;
    margin: 0 0 6px 0;
  }
  .instructions-box ol {
    margin: 0;
    padding-left: 18px;
    font-size: 9pt;
    color: #334155;
  }
  .instructions-box li {
    margin-bottom: 4px;
  }
  .signature-section {
    display: flex;
    justify-content: flex-end;
    margin-top: 20px;
  }
  .signature-box {
    text-align: center;
    width: 240px;
  }
  .signature-name {
    font-weight: 700;
    font-size: 10pt;
    color: #0f766e;
    margin-top: 4px;
    border-top: 1px dashed #64748b;
    padding-top: 3px;
  }
  .signature-desig {
    font-size: 8.5pt;
    color: #475569;
  }
  .footer-bar {
    position: fixed;
    bottom: 8mm;
    left: 14mm;
    right: 14mm;
    border-top: 1px solid #cbd5e1;
    padding-top: 5px;
    font-size: 8pt;
    color: #64748b;
    display: flex;
    justify-content: space-between;
  }
</style>
</head>
<body>

<div class="header-box">
  <div class="board-title">মাধ্যমিক ও উচ্চমাধ্যমিক শিক্ষা বোর্ড, ঢাকা</div>
  <div class="address-title">৪৩/২, জয়কালী মন্দির রোড, ঢাকা-১২০৩ | ওয়েবসাইট: www.dhakaeducationboard.gov.bd</div>
  <div class="memo-line">
    <span>স্মারক নং: মাউশিবো/পনি/মাধ্য/২০২৭/৮৫২</span>
    <span>তারিখ: ১৫ অক্টোবর ২০২৬</span>
  </div>
</div>

<div class="notice-banner">
  <div class="notice-title">জরুরি বিজ্ঞপ্তি: ২০২৭ সালের এসএসসি পরীক্ষার ফরম পূরণ ও ফি জমার সময়সূচি</div>
  <div class="notice-subtitle">সংশ্লিষ্ট সকল শিক্ষাপ্রতিষ্ঠান প্রধান, শিক্ষার্থী ও অভিভাবকদের অবগতির জন্য নির্দেশিকা</div>
</div>

<div class="body-intro">
  এতদ্বারা মাধ্যমিক ও উচ্চমাধ্যমিক শিক্ষা বোর্ড, ঢাকা-এর আওতাধীন সকল মাধ্যমিক পর্যায়ের শিক্ষাপ্রতিষ্ঠান প্রধান, শিক্ষক, শিক্ষার্থী এবং অভিভাবকদের জানানো যাচ্ছে যে, ২০২৭ সালের মাধ্যমিক স্কুল সার্টিফিকেট (এসএসসি) পরীক্ষার অনলাইনে ফরম পূরণ ও প্রয়োজনীয় ফি জমাদানের কার্যক্রম নিম্নবর্ণিত সময়সূচি ও নির্দেশিকা অনুযায়ী পরিচালিত হবে:
</div>

<table class="data-table">
  <thead>
    <tr>
      <th style="width: 50%;">কার্যক্রমের বিবরণ</th>
      <th style="width: 50%;">নির্ধারিত সময়সীমা / শেষ তারিখ</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>১. শিক্ষাপ্রতিষ্ঠানে নির্বাচনী (টেস্ট) পরীক্ষা সমাপ্তি ও ফল প্রকাশ</strong></td>
      <td style="text-align: center; font-weight: 600; color: #047857;">১৫ নভেম্বর ২০২৬ তারিখের মধ্যে</td>
    </tr>
    <tr>
      <td><strong>২. শিক্ষার্থীদের তথ্যসংবলিত সম্ভাব্য তালিকা (Probable List) প্রকাশ</strong></td>
      <td style="text-align: center; font-weight: 600;">১৫ নভেম্বর ২০২৬</td>
    </tr>
    <tr>
      <td><strong>৩. বিলম্ব ফি ছাড়া অনলাইনে ফরম পূরণ (e-Form Fill-up)</strong></td>
      <td style="text-align: center; font-weight: 700; color: #047857; background: #ecfdf5;">১৬ নভেম্বর থেকে ২৩ নভেম্বর ২০২৬</td>
    </tr>
    <tr>
      <td><strong>৪. বিলম্ব ফি ছাড়া সোনালী সেবার মাধ্যমে ফি জমার শেষ তারিখ</strong></td>
      <td style="text-align: center; font-weight: 600;">২৪ নভেম্বর ২০২৬</td>
    </tr>
    <tr>
      <td><strong>৫. বিলম্ব ফিসহ (পরীক্ষার্থীপ্রতি ১০০/- হারে) ফরম পূরণ</strong></td>
      <td style="text-align: center; font-weight: 700; color: #b45309; background: #fffbeb;">২৪ নভেম্বর থেকে ২৯ নভেম্বর ২০২৬</td>
    </tr>
    <tr>
      <td><strong>৬. বিলম্ব ফিসহ ফি জমাদানের সর্বশেষ তারিখ</strong></td>
      <td style="text-align: center; font-weight: 600;">৩০ নভেম্বর ২০২৬</td>
    </tr>
  </tbody>
</table>

<table class="data-table">
  <thead>
    <tr>
      <th>বিভাগ (Group)</th>
      <th>বোর্ড ফি</th>
      <th>কেন্দ্র ও ব্যবহারিক ফি</th>
      <th>সর্বমোট নির্ধারিত ফি</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>বিজ্ঞান বিভাগ (Science)</strong></td>
      <td style="text-align: center;">১,৯২০/- টাকা</td>
      <td style="text-align: center;">৫১৫/- টাকা</td>
      <td style="text-align: center; font-weight: 700; color: #047857;">২,৪৩৫/- টাকা</td>
    </tr>
    <tr>
      <td><strong>ব্যবসায় শিক্ষা বিভাগ (Business Studies)</strong></td>
      <td style="text-align: center;">১,৮৩০/- টাকা</td>
      <td style="text-align: center;">৪৮৫/- টাকা</td>
      <td style="text-align: center; font-weight: 700; color: #047857;">২,৩১৫/- টাকা</td>
    </tr>
    <tr>
      <td><strong>মানবিক বিভাগ (Humanities)</strong></td>
      <td style="text-align: center;">১,৮৩০/- টাকা</td>
      <td style="text-align: center;">৪৮৫/- টাকা</td>
      <td style="text-align: center; font-weight: 700; color: #047857;">২,৩১৫/- টাকা</td>
    </tr>
  </tbody>
</table>

<div class="instructions-box">
  <div class="instructions-title">বোর্ড নির্দেশিত ৬টি অত্যাবশ্যক নীতিমালা ও সতর্কতা:</div>
  <ol>
    <li><strong>বেতন ও সেশনচার্জ সীমা:</strong> পরীক্ষার্থীদের নবম ও দশম শ্রেণির সর্বমোট ২৪ মাসের বেশি বেতন ও সেশনচার্জ আদায় করা সম্পূর্ণ নিষিদ্ধ। সকল বকেয়া ৩১ ডিসেম্বর ২০২৬-এর মধ্যে পরিশোধ করতে হবে।</li>
    <li><strong>অতিরিক্ত ফি নিষেধাজ্ঞা:</strong> বোর্ড নির্ধারিত ফির বাইরে কোচিং ফি বা অন্য কোনো নামে অতিরিক্ত অর্থ আদায় করলে সংশ্লিষ্ট প্রতিষ্ঠানের বিরুদ্ধে শাস্তিমূলক ব্যবস্থা গ্রহণ করা হবে।</li>
    <li><strong>সিলেবাস মানদণ্ড:</strong> নিয়মিত পরীক্ষার্থীরা ২০২৭ সালের পূর্ণাঙ্গ সিলেবাসে এবং অনিয়মিত/মানোন্নয়ন পরীক্ষার্থীরা পূর্ববর্তী শিক্ষাবর্ষের (২০২৫ ও ২০২৬) সিলেবাসে পরীক্ষায় অংশ নেবে।</li>
    <li><strong>জিপিএ উন্নয়ন (GPA Improvement):</strong> রেজিস্ট্রেশনের মেয়াদ থাকা সাপেক্ষে ২০২৬ সালে উত্তীর্ণ কিন্তু জিপিএ-৫ না পাওয়া শিক্ষার্থীরা সব বিষয়ে অংশ নিয়ে ফল উন্নয়ন করতে পারবে (নতুন ফল উন্নত না হলে পূর্বের ফলই বহাল থাকবে)।</li>
    <li><strong>বহিষ্কৃত পরীক্ষার্থী:</strong> শাস্তির মেয়াদ শেষ হওয়া এবং রেজিস্ট্রেশনের মেয়াদ সাপেক্ষে অনিয়মিত হিসেবে অংশগ্রহণের সুযোগ পাবে।</li>
    <li><strong>ডাটা যাচাই:</strong> সম্ভাব্য তালিকা থেকে পরীক্ষার্থীর নাম, পিতা-মাতার নাম ও বিষয় কোড অত্যন্ত সতর্কতার সাথে মিলিয়ে ফরম পূরণ নিশ্চিত করতে হবে।</li>
  </ol>
</div>

<div class="signature-section">
  <div class="signature-box">
    <div style="height: 30px; color: #0f766e; font-style: italic; font-weight: bold; font-size: 10.5pt;">স্বাক্ষরিত/-</div>
    <div class="signature-name">প্রফেসর মো. আবুল বাশার</div>
    <div class="signature-desig">পরীক্ষা নিয়ন্ত্রক</div>
    <div class="signature-desig">মাধ্যমিক ও উচ্চমাধ্যমিক শিক্ষা বোর্ড, ঢাকা</div>
  </div>
</div>

<div class="footer-bar">
  <span>অফিসিয়াল তথ্যসূত্র: ঢাকা শিক্ষা বোর্ড (www.dhakaeducationboard.gov.bd)</span>
  <span>ডিজিটাল প্রকাশনা ও সংরক্ষণ: HelpTrickBD.com • সর্বস্বত্ব সংরক্ষিত</span>
</div>

</body>
</html>
"""

with open(temp_html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"[*] Temporary HTML written to {temp_html_path}")
print(f"[*] Rendering PDF via Chromium: {chrome_bin}...")

cmd = [
    chrome_bin,
    "--headless=new",
    "--disable-gpu",
    "--no-pdf-header-footer",
    f"--print-to-pdf={pdf_path}",
    temp_html_path
]

res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
if res.returncode == 0 and os.path.exists(pdf_path):
    size_kb = os.path.getsize(pdf_path) / 1024
    print("=================================================================")
    print(f"[SUCCESS] Official SSC Notice PDF generated: {pdf_path}")
    print(f"[SUCCESS] File Size: {size_kb:.2f} KB")
    print("=================================================================")
else:
    print(f"[ERROR] Failed to generate PDF! Return code: {res.returncode}")
    print(res.stderr.decode('utf-8', errors='ignore'))
    sys.exit(1)
