import json
import sys
from datetime import datetime

sys.stdout.reconfigure(encoding='utf-8')

with open('tools/trend_forecaster/seen_radar_notices.json', 'r', encoding='utf-8') as f:
    notices = json.load(f)

recent = []
# Match dates: 14, 15, 16, 17, 18 Oct 2026
target_dates = ['2026-10-14', '2026-10-15', '2026-10-16', '2026-10-17', '2026-10-18', '14-oct-2026', '15-oct-2026', '16-oct-2026', '17-oct-2026', '18-oct-2026', '14 oct 2026', '15 oct 2026', '16 oct 2026', '17 oct 2026', '18 oct 2026']

for k, v in notices.items():
    if not isinstance(v, dict):
        continue
    fs = v.get('first_seen', '')
    pd = v.get('pub_date', '')
    title = v.get('title', '')

    matched = False
    for td in target_dates:
        if td in fs.lower() or td in pd.lower() or td in title.lower():
            matched = True
            break

    if matched:
        recent.append({'id': k, 'first_seen': fs, 'pub_date': pd, 'title': title})

print(f"Total matching notices found: {len(recent)}\n")
for i, r in enumerate(recent, 1):
    print(f"{i:2d}. [{r['first_seen']}] | Pub: {r['pub_date']} | Title: {r['title']}")
