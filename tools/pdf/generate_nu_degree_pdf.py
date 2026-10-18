import os
import sys
import subprocess

sys.stdout.reconfigure(encoding='utf-8')

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
PDF_OUTPUT_DIR = os.path.join(PROJECT_ROOT, "assets", "pdf", "nu")
os.makedirs(PDF_OUTPUT_DIR, exist_ok=True)
SCRATCH_DIR = os.path.join(PROJECT_ROOT, "scratch")
os.makedirs(SCRATCH_DIR, exist_ok=True)

pdf_filename = "nu_degree_1st_year_rescheduled_routine_2026.pdf"
pdf_path = os.path.join(PDF_OUTPUT_DIR, pdf_filename)
temp_html_path = os.path.join(SCRATCH_DIR, "nu_degree_routine_print.html")

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
<title>জাতীয় বিশ্ববিদ্যালয় ডিগ্রি ১ম বর্ষ পরীক্ষার পরিবর্তিত সময়সূচি 2026 | HelpTrickBD Official PDF</title>
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
    border-bottom: 2.5px solid #0b2046;
    padding-bottom: 10px;
    margin-bottom: 16px;
  }
  .nu-logo-title {
    font-size: 17pt;
    font-weight: 800;
    color: #0b2046;
    margin: 0 0 3px 0;
  }
  .dept-title {
    font-size: 13pt;
    font-weight: 700;
    color: #1e3a8a;
    margin: 0 0 3px 0;
  }
  .address-title {
    font-size: 10pt;
    color: #475569;
    margin: 0 0 6px 0;
  }
  .memo-line {
    display: flex;
    justify-content: space-between;
    font-size: 9.5pt;
    color: #334155;
    margin-top: 8px;
    font-weight: 600;
  }
  .notice-banner {
    background: #f1f5f9;
    border: 1.5px solid #0b2046;
    border-radius: 6px;
    padding: 10px 14px;
    text-align: center;
    margin-bottom: 16px;
  }
  .notice-title {
    font-size: 13.5pt;
    font-weight: 800;
    color: #0b2046;
    margin: 0 0 4px 0;
  }
  .notice-subtitle {
    font-size: 10pt;
    color: #334155;
    margin: 0;
    font-weight: 600;
  }
  .body-intro {
    font-size: 10pt;
    text-align: justify;
    margin-bottom: 14px;
    line-height: 1.6;
  }
  table.routine-table {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 16px;
    font-size: 9.5pt;
  }
  table.routine-table th, table.routine-table td {
    border: 1px solid #94a3b8;
    padding: 7px 10px;
  }
  table.routine-table th {
    background-color: #0b2046;
    color: #ffffff;
    font-weight: 700;
    text-align: center;
  }
  table.routine-table tr:nth-child(even) {
    background-color: #f8fafc;
  }
  .instructions-box {
    background-color: #f8fafc;
    border: 1px solid #cbd5e1;
    border-left: 4px solid #f59e0b;
    border-radius: 4px;
    padding: 10px 14px;
    margin-bottom: 20px;
  }
  .instructions-title {
    font-size: 10.5pt;
    font-weight: 700;
    color: #b45309;
    margin: 0 0 6px 0;
  }
  .instructions-box ol {
    margin: 0;
    padding-left: 20px;
    font-size: 9pt;
    color: #334155;
  }
  .instructions-box li {
    margin-bottom: 4px;
  }
  .signature-section {
    display: flex;
    justify-content: flex-end;
    margin-top: 25px;
  }
  .signature-box {
    text-align: center;
    width: 240px;
  }
  .signature-name {
    font-weight: 700;
    font-size: 10.5pt;
    color: #0b2046;
    margin-top: 5px;
    border-top: 1px dashed #64748b;
    padding-top: 4px;
  }
  .signature-desig {
    font-size: 9pt;
    color: #475569;
  }
  .footer-bar {
    position: fixed;
    bottom: 8mm;
    left: 14mm;
    right: 14mm;
    border-top: 1px solid #cbd5e1;
    padding-top: 6px;
    font-size: 8.5pt;
    color: #64748b;
    display: flex;
    justify-content: space-between;
  }
</style>
</head>
<body>

<div class="header-box">
  <div class="nu-logo-title">জাতীয় বিশ্ববিদ্যালয়, বাংলাদেশ</div>
  <div class="dept-title">পরীক্ষা নিয়ন্ত্রণ দপ্তর</div>
  <div class="address-title">গাজীপুর-১৭০৪ | ওয়েব: www.nu.ac.bd</div>
  <div class="memo-line">
    <span>স্মারক নং: জা:বি:/প:নি:/ডিগ্রি(পাস)/২০২৬/১১০১</span>
    <span>তারিখ: ১৫ অক্টোবর ২০২৬</span>
  </div>
</div>

<div class="notice-banner">
  <div class="notice-title">জরুরি বিজ্ঞপ্তি: ডিগ্রি (পাস) ও সার্টিফিকেট কোর্স ১ম বর্ষ পরীক্ষার পরিবর্তিত সময়সূচি</div>
  <div class="notice-subtitle">সংশ্লিষ্ট সকলের অবগতির জন্য ২০২৬ সালের ডিগ্রি পাস ১ম বর্ষের স্থগিত পরীক্ষার সময়সূচি প্রকাশ সংক্রান্ত</div>
</div>

<div class="body-intro">
  সংশ্লিষ্ট সকলকে জানানো যাচ্ছে যে, জাতীয় বিশ্ববিদ্যালয়ের অধীন অনুষ্ঠিতব্য ২০২৬ সালের ডিগ্রি (পাস) ও সার্টিফিকেট কোর্স ১ম বর্ষ পরীক্ষার (পরীক্ষা কোড: ১১০১) অনিবার্য কারণবশত স্থগিতকৃত <strong>১৮/১০/২০২৬</strong> এবং <strong>১৯/১০/২০২৬</strong> তারিখের পরীক্ষাসমূহ নিম্নবর্ণিত সংশোধিত সময়সূচি অনুযায়ী অনুষ্ঠিত হবে। প্রতিদিন পরীক্ষা <strong>দুপুর ১:৩০ মিনিট</strong> থেকে শুরু হবে। প্রশ্নপত্রে উল্লিখিত সময়কাল অনুযায়ী পরীক্ষা সমাপ্ত হবে।
</div>

<table class="routine-table">
  <thead>
    <tr>
      <th style="width: 22%;">পূর্বনির্ধারিত তারিখ ও বার</th>
      <th style="width: 22%;">পরিবর্তিত নতুন তারিখ ও বার</th>
      <th style="width: 38%;">বিষয় ও পত্র</th>
      <th style="width: 18%;">বিষয় কোড</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: center; font-weight: 600; color: #b91c1c;">
        ১৮/১০/২০২৬<br>(রবিবার)
      </td>
      <td style="text-align: center; font-weight: 700; color: #047857; background: #ecfdf5;">
        ০২/১১/২০২৬<br>(সোমবার)
      </td>
      <td>
        • গণিত (Mathematics) - ২য় পত্র<br>
        • উচ্চাঙ্গ সংগীত - ২য় পত্র
      </td>
      <td style="text-align: center; font-weight: 600;">
        ১১৩৭০৩<br>১১৪৫০২
      </td>
    </tr>
    <tr>
      <td style="text-align: center; font-weight: 600; color: #b91c1c;">
        ১৯/১০/২০২৬<br>(সোমবার)
      </td>
      <td style="text-align: center; font-weight: 700; color: #047857; background: #ecfdf5;">
        ০৩/১১/২০২৬<br>(মঙ্গলবার)
      </td>
      <td>
        • বাংলা সাহিত্য (ঐচ্ছিক) - ২য় পত্র<br>
        • ইংরেজি (ঐচ্ছিক) - ২য় পত্র<br>
        • আরবি - ২য় পত্র<br>
        • সংস্কৃত - ২য় পত্র<br>
        • পালি - ২য় পত্র<br>
        • বেসিক হোম ইকোনমিকস - ২য় পত্র
      </td>
      <td style="text-align: center; font-weight: 600;">
        ১১১০০৩<br>১১১১০৩<br>১১১২০৩<br>১১১৩০৩<br>১১১৪০৩<br>১১৩৬০৩
      </td>
    </tr>
  </tbody>
</table>

<div class="instructions-box">
  <div class="instructions-title">পরীক্ষার্থী ও কেন্দ্র কর্তৃপক্ষের জন্য জরুরি নির্দেশনাবলী:</div>
  <ol>
    <li>পূর্বঘোষিত সময়সূচির অন্যান্য সকল তারিখের (২০ অক্টোবর ২০২৬ হতে পরবর্তী) পরীক্ষাসমূহ অপরিবর্তিত থাকবে এবং নির্ধারিত সময়েই অনুষ্ঠিত হবে।</li>
    <li>স্থগিত পরীক্ষার জন্য শিক্ষার্থীদের নতুন করে কোনো প্রবেশপত্র সংগ্রহ করতে হবে না। পূর্বে ইস্যুকৃত প্রবেশপত্র ও রেজিস্ট্রেশন কার্ড প্রদর্শন করেই উক্ত পরীক্ষায় অংশগ্রহণ করা যাবে।</li>
    <li>পরীক্ষার কেন্দ্র ও কক্ষ বিন্যাস অপরিবর্তিত থাকবে।</li>
    <li>পরীক্ষার্থীদের পরীক্ষা শুরুর কমপক্ষে ৩০ মিনিট পূর্বে স্ব-স্ব কেন্দ্রে উপস্থিত হয়ে নির্ধারিত আসন গ্রহণ করতে হবে।</li>
    <li>পরীক্ষা কেন্দ্রে মোবাইল ফোন, স্মার্টওয়াচ বা যেকোনো ধরনের ইলেকট্রনিক ডিভাইস বহন সম্পূর্ণ নিষিদ্ধ।</li>
  </ol>
</div>

<div class="signature-section">
  <div class="signature-box">
    <div style="height: 35px; color: #0b2046; font-style: italic; font-weight: bold; font-size: 11pt;">স্বাক্ষরিত/-</div>
    <div class="signature-name">মো. এনামুল করিম</div>
    <div class="signature-desig">পরীক্ষা নিয়ন্ত্রক</div>
    <div class="signature-desig">জাতীয় বিশ্ববিদ্যালয়, গাজীপুর</div>
  </div>
</div>

<div class="footer-bar">
  <span>অফিসিয়াল তথ্যসূত্র: জাতীয় বিশ্ববিদ্যালয় (www.nu.ac.bd)</span>
  <span>ডিজিটাল প্রকাশনা: HelpTrickBD.com • সর্বস্বত্ব সংরক্ষিত</span>
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
    print(f"[SUCCESS] Official NU Degree PDF generated: {pdf_path}")
    print(f"[SUCCESS] File Size: {size_kb:.2f} KB")
    print("=================================================================")
else:
    print(f"[ERROR] Failed to generate PDF! Return code: {res.returncode}")
    print(res.stderr.decode('utf-8', errors='ignore'))
    sys.exit(1)
