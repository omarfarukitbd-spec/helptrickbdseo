import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('all_live_posts_catalog.json', 'r', encoding='utf-8') as f:
    catalog = json.load(f)

keywords = ['বৃত্তি', 'ডিগ্রি', 'degree', 'scholarship', 'প্রাথমিক', 'primary', 'অনার্স ৩য়', 'honours 3rd', 'জিপিএ']
found = 0
for p in catalog:
    title = p.get('title', '')
    slug = p.get('slug', '')
    for kw in keywords:
        if kw in title.lower() or kw in slug.lower():
            print(f"[{kw}] {title} -> slug: {slug}")
            found += 1
            break

if found == 0:
    print("NO existing posts found in catalog for these keywords! Complete content gap!")
