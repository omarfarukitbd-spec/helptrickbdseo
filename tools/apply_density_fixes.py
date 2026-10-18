import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

HTML_PATH = 'output_posts/ntrca-school-level-assistant-teacher-syllabus-2026.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    html = f.read()

kw = "NTRCA স্কুল পর্যায় সিলেবাস 2026"

replacements = [
    (
        "বাংলা বিষয়ের লিখিত পরীক্ষায় ভালো করার মূল চাবিকাঠি হলো সাহিত্য অংশে",
        f"{kw} এর অধীনে বাংলা বিষয়ের লিখিত পরীক্ষায় ভালো করার মূল চাবিকাঠি হলো সাহিত্য অংশে"
    ),
    (
        "ইংরেজি লিখিত পরীক্ষায় প্রার্থীরা সবচেয়ে বেশি দ্বিধায় ভোগেন।",
        f"{kw} এর ইংরেজি লিখিত পরীক্ষায় প্রার্থীরা সবচেয়ে বেশি দ্বিধায় ভোগেন।"
    ),
    (
        "গণিতে প্রতিটি প্রশ্নের ধাপভিত্তিক নম্বর (Step Marking) থাকে।",
        f"{kw} এর গণিত অংশে প্রতিটি প্রশ্নের ধাপভিত্তিক নম্বর (Step Marking) থাকে।"
    ),
    (
        "সহকারী শিক্ষক (আইসিটি) পদের প্রশ্ন কাঠামো অন্যান্য বিষয়ের চেয়ে কিছুটা ব্যতিক্রম।",
        f"{kw} এর সহকারী শিক্ষক (আইসিটি) পদের প্রশ্ন কাঠামো অন্যান্য বিষয়ের চেয়ে কিছুটা ব্যতিক্রম।"
    ),
    (
        "অনেক প্রার্থীর বড় ভুল হলো তারা প্রিলি ও লিখিত প্রস্তুতিকে আলাদা মনে করেন।",
        f"অনেক প্রার্থীর বড় ভুল হলো তারা {kw} এর প্রিলি ও লিখিত প্রস্তুতিকে আলাদা মনে করেন।"
    ),
    (
        "দিনভর টেবিলে বসে বই উল্টানোর চেয়ে পরিকল্পনা অনুযায়ী ৪ থেকে ৬ ঘণ্টা",
        f"দিনভর টেবিলে বসে বই উল্টানোর চেয়ে {kw} অনুযায়ী ৪ থেকে ৬ ঘণ্টা"
    ),
    (
        "গত ১০ম থেকে ১৮তম শিক্ষক নিবন্ধনের শত শত প্রশ্নপত্র ঘেঁটে দেখা যায় যে,",
        f"{kw} এর বিগত ১০ম থেকে ১৮তম শিক্ষক নিবন্ধনের শত শত প্রশ্নপত্র ঘেঁটে দেখা যায় যে,"
    )
]

applied = 0
for src, dst in replacements:
    if src in html:
        html = html.replace(src, dst, 1)
        applied += 1
        print(f"[+] Applied replacement: {src[:30]}...")
    else:
        print(f"[-] Could not find: {src[:30]}...")

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"[*] Total natural replacements applied: {applied}")

# Metrics
clean_text = re.sub(r'<[^>]+>', ' ', html)
words = clean_text.split()
total_words = len(words)
kw_count = clean_text.count(kw)
density = (kw_count / total_words) * 100
print(f"[*] Total Words: {total_words}")
print(f"[*] Total Visible Keyword Occurrences: {kw_count}")
print(f"[*] Final Keyword Density: {density:.2f}% (Ideal: 0.85% - 1.20%)")
