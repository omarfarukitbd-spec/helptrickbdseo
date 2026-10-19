#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import json
import re
import requests
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

with open('tools/wp_publisher/config.json', 'r', encoding='utf-8') as f:
    cfg = json.load(f)
auth = (cfg['wp_user'], cfg['wp_app_password'])
base_url = cfg['wp_url'].rstrip('/')

post = requests.get(f'{base_url}/wp-json/wp/v2/posts/15924?context=edit', auth=auth).json()
title = post['title']['raw']
slug = post['slug']
meta = post['meta']
content = post['content']['raw']
focus_kw = meta.get('rank_math_focus_keyword', '').split(',')[0].strip()
secondary_kw = meta.get('rank_math_focus_keyword', '').split(',')[1].strip() if ',' in meta.get('rank_math_focus_keyword', '') else ''
desc = meta.get('rank_math_description', '')

soup = BeautifulSoup(content, 'html.parser')

print('=== Rank Math Tests Diagnosis for Post 15924 ===')
print('Title:', title)
print('Focus KW:', focus_kw)
print('Secondary KW:', secondary_kw)
print('Slug:', slug)

# Basic SEO
print('\n[Basic SEO]')
print('1. Keyword in Title:', focus_kw.lower() in title.lower())
print('2. Keyword in Meta Description:', focus_kw.lower() in desc.lower())
print('3. Keyword in URL (primary or secondary):', any(w in slug for w in secondary_kw.split()[:4]))
words = len(re.sub(r'<[^>]+>', ' ', content).split())
first_10 = ' '.join(content.split()[:max(1, len(content.split())//10)])
print('4. Keyword in first 10%:', focus_kw.lower() in first_10.lower())
kw_count = content.count(focus_kw)
print(f'5. Keyword in content count: {kw_count}')
print(f'6. Content word count: {words} (Note: >=2500 words is needed for 100% full length score)')

# Additional SEO
print('\n[Additional SEO]')
h2s = [h.get_text() for h in soup.find_all(['h2', 'h3'])]
has_h2 = any(focus_kw.lower() in h.lower() for h in h2s)
print('7. Keyword in Subheadings:', has_h2)
alts = [img.get('alt', '') for img in soup.find_all('img')]
has_alt = any(focus_kw.lower() in a.lower() for a in alts)
print('8. Keyword in Image Alt:', has_alt)
density = (kw_count / words) * 100 if words else 0
print(f'9. Keyword Density: {density:.2f}% (Target: 0.8% - 1.5%)')
url_len = len(f'https://www.helptrickbd.com/{slug}/')
print(f'10. URL length: {url_len} chars (<=75 chars is ideal)')
ext_links = [a.get('href') for a in soup.find_all('a') if a.get('href') and 'helptrickbd.com' not in a.get('href')]
print(f'11. Has External Links: {len(ext_links)}')
int_links = [a.get('href') for a in soup.find_all('a') if a.get('href') and 'helptrickbd.com' in a.get('href')]
print(f'12. Has Internal Links: {len(int_links)}')

# Title Readability
print('\n[Title Readability]')
print('13. Keyword near beginning:', title.lower().startswith(focus_kw.lower()))
print('14. Title Sentiment:', any(w in title.lower() for w in ['best', 'top', 'great', 'perfect']))
print('15. Title Power Word:', any(w in title.lower() for w in ['complete guide', 'guide', 'official', 'secret']))
print('16. Title has number:', bool(re.search(r'\d+', title)))

# Content Readability
print('\n[Content Readability]')
has_toc = 'id="rank-math-toc"' in content or 'rank-math/toc-block' in content
print('17. Has Table of Contents:', has_toc)
