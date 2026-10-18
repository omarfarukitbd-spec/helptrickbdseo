import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

HTML_PATH = 'output_posts/ntrca-school-level-assistant-teacher-syllabus-2026.html'

with open(HTML_PATH, 'r', encoding='utf-8') as f:
    html = f.read()

kw = "NTRCA স্কুল পর্যায় সিলেবাস 2026"

# Check where sections are
sections = [
    ('id="section-2"', 'বাংলা'),
    ('id="section-3"', 'ইংরেজি'),
    ('id="section-4"', 'গণিত'),
    ('id="section-5"', 'আইসিটি'),
    ('id="section-8"', 'ম্যাপিং'),
    ('id="section-10"', 'রুটিন'),
    ('id="section-11"', 'ট্রেন্ড'),
    ('id="section-13"', 'ভাইভা')
]

for sid, label in sections:
    pos = html.find(sid)
    if pos != -1:
        p_match = re.search(r'<p[^>]*>(.*?)</p>', html[pos:pos+1500], re.DOTALL)
        if p_match:
            clean = re.sub(r'<[^>]+>', '', p_match.group(1)).strip()
            print(f"[{label}] {clean[:120]}...")
