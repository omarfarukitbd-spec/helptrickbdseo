import json
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('tools/trend_forecaster/seen_radar_notices.json', 'r', encoding='utf-8') as f:
    notices = json.load(f)

# Filter notices between Oct 14 and Oct 18, 2026
target_notices = []
seen_titles = set()

junk_keywords = [
    'পরিদর্শন ছক', 'বাস্তবায়নাধীন উন্নয়ন', 'অগ্রিম বর্ধিতবেতনের', 'সৌর বিদ্যুৎ',
    'মেডিকেল এডুকেশন বুলেটিন', 'নার্সিং এবং মিডওয়াইফারি', 'মাদকের কুফল'
]

for nid, data in notices.items():
    if not isinstance(data, dict):
        continue
    fs = data.get('first_seen', '')
    title = data.get('title', '').strip()
    pd = data.get('pub_date', '')
    link = data.get('link', '')

    # Check date
    if not any(fs.startswith(f"2026-10-{d}") for d in ['14', '15', '16', '17', '18']):
        continue

    # Filter junk
    if any(jk in title for jk in junk_keywords) or len(title) < 15:
        continue

    # Clean title
    clean_title = re.sub(r'\s+', ' ', title)
    if clean_title in seen_titles:
        continue
    seen_titles.add(clean_title)

    target_notices.append({
        'title': clean_title,
        'first_seen': fs,
        'pub_date': pd,
        'link': link
    })

print(f"Total Unique Actionable Exam/Education Notices: {len(target_notices)}\n")
for i, item in enumerate(target_notices, 1):
    print(f"[{i:02d}] Date: {item['first_seen'][:10]} | {item['title']}")
