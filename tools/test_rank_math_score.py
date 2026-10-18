import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

html_file = sys.argv[1] if len(sys.argv) > 1 else 'output_posts/ntrca-school-level-assistant-teacher-syllabus-2026.html'
meta_file = sys.argv[2] if len(sys.argv) > 2 else html_file.replace('.html', '_meta.json')

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

with open(meta_file, 'r', encoding='utf-8') as f:
    meta = json.load(f)

title = meta.get('title', '')
desc = meta.get('meta_description', '')
slug = meta.get('slug', '')
focus_kw = meta.get('focus_keyword', '').split(',')[0].strip()

print(f"Focus keyword: {focus_kw}")
print(f"Title: {title}")
print(f"Slug: {slug}")

# 1. keywordInTitle
print(f"1. keywordInTitle: {focus_kw.lower() in title.lower()}")

# 2. keywordInMetaDescription
print(f"2. keywordInMetaDescription: {focus_kw.lower() in desc.lower()}")

# 3. keywordInPermalink
print(f"3. keywordInPermalink: {focus_kw.lower() in slug.lower()}")

# 4. keywordIn10Percent
words = content.split()
first_10 = ' '.join(words[:max(1, len(words)//10)])
print(f"4. keywordIn10Percent: {focus_kw.lower() in first_10.lower()}")

# 5. keywordInContent count
count = content.lower().count(focus_kw.lower())
print(f"5. keywordInContent count: {count}")

# 6. contentWordCount
clean_text = re.sub(r'<[^>]+>', ' ', content)
text_words = clean_text.split()
word_count = len(text_words)
print(f"6. contentWordCount: {word_count}")

# 7. keywordInSubheadings
headings = re.findall(r'<h[23][^>]*>(.*?)</h[23]>', content, re.IGNORECASE | re.DOTALL)
kw_in_heading = any(focus_kw.lower() in h.lower() for h in headings)
print(f"7. keywordInSubheadings: {kw_in_heading}")
for h in headings:
    if focus_kw.lower() in h.lower():
        print(f"   Matched heading: {h.strip()}")

# 8. keywordInImageAlt
alts = re.findall(r'alt=[\"\'](.*?)[\"\']', content, re.IGNORECASE)
print(f"8. keywordInImageAlt: {any(focus_kw.lower() in a.lower() for a in alts)}")
for a in alts:
    if focus_kw.lower() in a.lower():
        print(f"   Matched alt: {a}")

# 9. keywordDensity
density = (count / word_count) * 100 if word_count else 0
print(f"9. keywordDensity: {density:.2f}% (count={count}, words={word_count})")

# 10. lengthOfURL
full_url = f"https://www.helptrickbd.com/{slug}/"
print(f"10. lengthOfURL: {len(full_url)} (good <= 75)")

# 11. Links
out_links = re.findall(r'href=[\"\'](https?://[^\s\"\']+)[\"\']', content, re.IGNORECASE)
ext_links = [l for l in out_links if 'helptrickbd.com' not in l]
int_links = [l for l in out_links if 'helptrickbd.com' in l]
print(f"11. extLinks: {len(ext_links)}, intLinks: {len(int_links)}")

# 12. titleSentiment
print(f"12. titleSentiment: {'best' in title.lower() or 'top' in title.lower()}")

# 13. titleHasPowerWords
print(f"13. titleHasPowerWords: {'guide' in title.lower() or 'complete' in title.lower()}")

# 14. titleHasNumber
print(f"14. titleHasNumber: {bool(re.search(r'\d+', title))}")

# 15. contentHasTOC
print(f"15. contentHasTOC: {'id=\"rank-math-toc\"' in content or 'rank-math/toc-block' in content}")
