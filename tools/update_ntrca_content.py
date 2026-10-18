import os
import sys
import re
import json
import requests

sys.stdout.reconfigure(encoding='utf-8')

HTML_PATH = 'output_posts/ntrca-school-level-assistant-teacher-syllabus-2026.html'
META_PATH = 'output_posts/ntrca-school-level-assistant-teacher-syllabus-2026_meta.json'
CONFIG_PATH = 'tools/wp_publisher/config.json'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Clean out any Gutenberg block comment for TOC to eliminate "Block contains unexpected or invalid content"
old_toc_pattern = r'<!-- wp:rank-math/toc-block.*?<!-- /wp:rank-math/toc-block -->'

new_toc = '''<!-- Table of Contents Box -->
<div class="htbd-toc-box wp-block-rank-math-toc-block" id="rank-math-toc" style="background: #f8fafc; border: 1.5px solid #0f766e; border-radius: 12px; padding: 22px 25px; margin: 30px 0; font-family: 'SolaimanLipi', sans-serif; box-shadow: 0 2px 10px rgba(0,0,0,0.04);">
  <div style="font-weight: 700; font-size: 19px; color: #0f766e; margin-bottom: 12px; display: flex; align-items: center; gap: 8px;">
    <span>সূচিপত্র (Table of Contents)</span>
  </div>
  <p style="margin: 0 0 12px 0; color: #475569; font-size: 15px;">
    নিচে সকল বিষয়ের লিখিত ও প্রিলিমিনারি সিলেবাস, মানবণ্টন ও PDF সহায়িকা বিস্তারিতভাবে সাজানো হলো:
  </p>
  <ol style="margin: 0; padding-left: 22px; color: #334155; line-height: 2; font-size: 15.5px;">
    <li><a href="#section-1" style="color: #0f766e; text-decoration: none; font-weight: 600;">NTRCA স্কুল পর্যায় সিলেবাস 2026 ও ব্লুমস ট্যাক্সোনমি মানবণ্টন</a></li>
    <li><a href="#section-2" style="color: #0f766e; text-decoration: none; font-weight: 600;">সহকারী শিক্ষক (বাংলা) লিখিত পরীক্ষার সিলেবাস</a></li>
    <li><a href="#section-3" style="color: #0f766e; text-decoration: none; font-weight: 600;">সহকারী শিক্ষক (বাধ্যতামূলক ইংরেজি) পূর্ণাঙ্গ সিলেবাস</a></li>
    <li><a href="#section-4" style="color: #0f766e; text-decoration: none; font-weight: 600;">সহকারী শিক্ষক (গণিত) লিখিত পরীক্ষার মানবণ্টন ও প্রশ্ন কাঠামো</a></li>
    <li><a href="#section-5" style="color: #0f766e; text-decoration: none; font-weight: 600;">সহকারী শিক্ষক (আইসিটি) লিখিত সিলেবাস ও টেকনিক্যাল টপিকস</a></li>
    <li><a href="#section-6" style="color: #0f766e; text-decoration: none; font-weight: 600;">ভৌতবিজ্ঞান, বাণিজ্য ও ধর্ম বিষয়ের সিলেবাস সারসংক্ষেপ</a></li>
    <li><a href="#section-7" style="color: #0f766e; text-decoration: none; font-weight: 600;">NTRCA স্কুল পর্যায় সিলেবাস 2026 অনুযায়ী প্রথমবারেই পাসের কার্যকরী কৌশল</a></li>
    <li><a href="#section-8" style="color: #0f766e; text-decoration: none; font-weight: 600;">প্রিলিমিনারি বনাম লিখিত সিলেবাস সমন্বিত প্রস্তুতি ম্যাপিং</a></li>
    <li><a href="#section-9" style="color: #0f766e; text-decoration: none; font-weight: 600;">ফারুক স্যারের ৭টি এক্সক্লুসিভ লিখিত পরীক্ষার খাতা উপস্থাপনা কৌশল</a></li>
    <li><a href="#section-10" style="color: #0f766e; text-decoration: none; font-weight: 600;">NTRCA স্কুল পর্যায় সিলেবাস 2026 অনুযায়ী বিষয়ভিত্তিক দৈনিক পড়ার কার্যকর রুটিন</a></li>
    <li><a href="#section-11" style="color: #0f766e; text-decoration: none; font-weight: 600;">বিগত বছরের প্রশ্নভিত্তিক অধ্যায়ভিত্তিক গুরুত্ব ও ট্রেন্ড বিশ্লেষণ</a></li>
    <li><a href="#section-12" style="color: #0f766e; text-decoration: none; font-weight: 600;">NTRCA স্কুল পর্যায় সিলেবাস 2026 অনুযায়ী নমুনা মডেল প্রশ্ন ও সমাধান</a></li>
    <li><a href="#section-13" style="color: #0f766e; text-decoration: none; font-weight: 600;">ভাইভা পরীক্ষা (Viva Voce) প্রস্তুতি ও সাধারণ প্রশ্নোত্তর গাইড</a></li>
    <li><a href="#section-14" style="color: #0f766e; text-decoration: none; font-weight: 600;">সেরা রেফারেন্স বই ও গাইডলাইন তালিকা</a></li>
    <li><a href="#section-15" style="color: #0f766e; text-decoration: none; font-weight: 600;">NTRCA স্কুল পর্যায় সিলেবাস 2026 সংক্রান্ত সাধারণ প্রশ্নোত্তর (FAQs)</a></li>
  </ol>
</div>'''

if re.search(old_toc_pattern, html, flags=re.DOTALL):
    html = re.sub(old_toc_pattern, new_toc, html, flags=re.DOTALL)
    print("[+] Replaced broken Gutenberg TOC block comment with clean HTML TOC.")
elif 'id="rank-math-toc"' not in html:
    # insert before interactive pdf study hub
    idx = html.find('<!-- ========================================== -->')
    if idx != -1:
        html = html[:idx] + new_toc + '\n\n' + html[idx:]
        print("[+] Inserted clean HTML TOC before PDF hub.")

# 2. Heading 1 starts cleanly with Focus Keyword for 100% Rank Math regex match
old_h1 = r'<h2 style="[^"]*">\s*১\.\s*NTRCA স্কুল পর্যায় সিলেবাস 2026 ও ব্লুমস ট্যাক্সোনমি মানবণ্টন\s*</h2>'
new_h1 = '''<h2 id="section-1" style="font-family: 'SolaimanLipi', sans-serif; color: #0f172a; font-size: 24px; font-weight: 700; margin: 40px 0 20px 0; border-bottom: 2px solid #e2e8f0; padding-bottom: 10px;">
NTRCA স্কুল পর্যায় সিলেবাস 2026: ব্লুমস ট্যাক্সোনমি ও বিষয়ভিত্তিক পূর্ণাঙ্গ মানবণ্টন
</h2>'''
html, count_h1 = re.subn(old_h1, new_h1, html)
print(f"[+] Heading 1 updated with ID: {count_h1}")

# 3. Add IDs to other headings
heading_map = [
    (r'<h2 style="([^"]*)">\s*২\.\s*সহকারী শিক্ষক \(বাংলা\)', r'<h2 id="section-2" style="\1">২. সহকারী শিক্ষক (বাংলা)'),
    (r'<h2 style="([^"]*)">\s*৩\.\s*সহকারী শিক্ষক \(বাধ্যতামূলক ইংরেজি\)', r'<h2 id="section-3" style="\1">৩. সহকারী শিক্ষক (বাধ্যতামূলক ইংরেজি)'),
    (r'<h2 style="([^"]*)">\s*৪\.\s*সহকারী শিক্ষক \(গণিত\)', r'<h2 id="section-4" style="\1">৪. সহকারী শিক্ষক (গণিত)'),
    (r'<h2 style="([^"]*)">\s*৫\.\s*সহকারী শিক্ষক \(আইসিটি\)', r'<h2 id="section-5" style="\1">৫. সহকারী শিক্ষক (আইসিটি)'),
    (r'<h2 style="([^"]*)">\s*৬\.\s*ভৌতবিজ্ঞান', r'<h2 id="section-6" style="\1">৬. ভৌতবিজ্ঞান'),
    (r'<h2 style="([^"]*)">\s*৭\.\s*NTRCA', r'<h2 id="section-7" style="\1">৭. NTRCA'),
    (r'<h2 style="([^"]*)">\s*৮\.\s*প্রিলিমিনারি', r'<h2 id="section-8" style="\1">৮. প্রিলিমিনারি'),
    (r'<h2 style="([^"]*)">\s*৯\.\s*ফারুক স্যারের', r'<h2 id="section-9" style="\1">৯. ফারুক স্যারের'),
    (r'<h2 style="([^"]*)">\s*১০\.\s*NTRCA', r'<h2 id="section-10" style="\1">১০. NTRCA'),
    (r'<h2 style="([^"]*)">\s*১১\.\s*বিগত বছরের', r'<h2 id="section-11" style="\1">১১. বিগত বছরের'),
    (r'<h2 style="([^"]*)">\s*১২\.\s*NTRCA', r'<h2 id="section-12" style="\1">১২. NTRCA'),
    (r'<h2 style="([^"]*)">\s*১৩\.\s*ভাইভা পরীক্ষা', r'<h2 id="section-13" style="\1">১৩. ভাইভা পরীক্ষা'),
    (r'<h2 style="([^"]*)">\s*১৪\.\s*NTRCA', r'<h2 id="section-14" style="\1">১৪. NTRCA'),
    (r'<h2 style="([^"]*)">\s*১৫\.\s*NTRCA', r'<h2 id="section-15" style="\1">১৫. NTRCA')
]

for pat, repl in heading_map:
    html, n = re.subn(pat, repl, html)
    if n > 0:
        print(f"[+] Heading mapped: {pat[:25]}... (count: {n})")

# 4. Natural keyword density augmentation across sections (7 natural additions)
kw = "NTRCA স্কুল পর্যায় সিলেবাস 2026"

# In Section 1
p1_target = 'আন্তর্জাতিক ব্লুমস ট্যাক্সোনমি (Bloom\'s Taxonomy) নীতি মেনে লিখিত প্রশ্নপত্র প্রণয়ন করছেন।'
p1_repl = f'আন্তর্জাতিক ব্লুমস ট্যাক্সোনমি (Bloom\'s Taxonomy) নীতি মেনে {kw} এর আওতায় লিখিত প্রশ্নপত্র প্রণয়ন করছেন।'
if p1_target in html:
    html = html.replace(p1_target, p1_repl, 1)
    print("[+] Added kw in Section 1")

# In Section 2
p2_target = 'সহকারী শিক্ষক (বাংলা) পদের জন্য ব্যাকরণ ও সাহিত্যের যুগ বিভাগ গভীরভাবে পড়া জরুরি।'
p2_repl = f'সহকারী শিক্ষক (বাংলা) পদের জন্য {kw} এর নির্ধারিত ব্যাকরণ ও সাহিত্যের যুগ বিভাগ গভীরভাবে পড়া জরুরি।'
if p2_target in html:
    html = html.replace(p2_target, p2_repl, 1)
    print("[+] Added kw in Section 2")

# In Section 3
p3_target = 'ইংরেজিতে মুখস্থ উত্তরের চেয়ে ব্যাকরণগত নির্ভুলতা ও ফ্রি-হ্যান্ড লেখার দক্ষতাকে বেশি প্রাধান্য দেওয়া হয়।'
p3_repl = f'ইংরেজিতে মুখস্থ উত্তরের চেয়ে {kw} অনুযায়ী ব্যাকরণগত নির্ভুলতা ও ফ্রি-হ্যান্ড লেখার দক্ষতাকে বেশি প্রাধান্য দেওয়া হয়।'
if p3_target in html:
    html = html.replace(p3_target, p3_repl, 1)
    print("[+] Added kw in Section 3")

# In Section 4
p4_target = 'গণিতে পূর্ণ নম্বর পেতে হলে প্রতিটি ধাপ স্পষ্ট ও নির্ভুলভাবে উপস্থাপন করতে হবে।'
p4_repl = f'{kw} এর গণিত অংশে পূর্ণ নম্বর পেতে হলে প্রতিটি ধাপ স্পষ্ট ও নির্ভুলভাবে উপস্থাপন করতে হবে।'
if p4_target in html:
    html = html.replace(p4_target, p4_repl, 1)
    print("[+] Added kw in Section 4")

# In Section 5
p5_target = 'আইসিটি বিষয়ের প্রার্থীরা প্রায়ই প্রোগ্রামিং লজিক ও ডেটাবেস কোয়েরির মতো প্রায়োগিক প্রশ্নে ভুল করেন।'
p5_repl = f'{kw} অনুযায়ী সহকারী শিক্ষক (আইসিটি) বিষয়ের প্রার্থীরা প্রায়ই প্রোগ্রামিং লজিক ও ডেটাবেস কোয়েরির মতো প্রায়োগিক প্রশ্নে ভুল করেন।'
if p5_target in html:
    html = html.replace(p5_target, p5_repl, 1)
    print("[+] Added kw in Section 5")

# In Section 8
p8_target = 'প্রিলিমিনারি ও লিখিত উভয় পরীক্ষার মধ্যে অনেক বিষয়ের সরাসরি মিল রয়েছে।'
p8_repl = f'{kw} বিশ্লেষণ করলে দেখা যায়, প্রিলিমিনারি ও লিখিত উভয় পরীক্ষার মধ্যে অনেক বিষয়ের সরাসরি মিল রয়েছে।'
if p8_target in html:
    html = html.replace(p8_target, p8_repl, 1)
    print("[+] Added kw in Section 8")

# In Section 11
p11_target = 'বিগত বছরের প্রশ্ন পর্যালোচনা করলে দেখা যায় যে, নির্দিষ্ট কিছু অধ্যায় থেকে প্রতি বছর নিশ্চিত প্রশ্ন থাকে।'
p11_repl = f'{kw} এর বিগত বছরের প্রশ্ন পর্যালোচনা করলে দেখা যায় যে, নির্দিষ্ট কিছু অধ্যায় থেকে প্রতি বছর নিশ্চিত প্রশ্ন থাকে।'
if p11_target in html:
    html = html.replace(p11_target, p11_repl, 1)
    print("[+] Added kw in Section 11")

# In Section 13
p13_target = 'ভাইভা বোর্ডে প্রার্থীর জড়তাহীন বাচনভঙ্গি ও বিষয়ের গভীরতা যাচাই করা হয়।'
p13_repl = f'ভাইভা বোর্ডে প্রার্থীর জড়তাহীন বাচনভঙ্গি ও {kw} এর বিষয়ের গভীরতা যাচাই করা হয়।'
if p13_target in html:
    html = html.replace(p13_target, p13_repl, 1)
    print("[+] Added kw in Section 13")

# Save updated HTML
with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(html)
print("[+] Successfully wrote updated HTML to disk.")

# Check final metrics
clean_text = re.sub(r'<[^>]+>', ' ', html)
words = clean_text.split()
total_words = len(words)
kw_count = clean_text.count(kw)
density = (kw_count / total_words) * 100
print(f"[*] Final Word Count: {total_words}")
print(f"[*] Final Visible Keyword Count: {kw_count}")
print(f"[*] Final Keyword Density: {density:.2f}% (Target: 0.80% - 1.20%)")
