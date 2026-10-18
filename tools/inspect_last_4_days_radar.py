import json
import sys
from datetime import datetime

sys.stdout.reconfigure(encoding='utf-8')

with open('tools/trend_forecaster/seen_radar_notices.json', 'r', encoding='utf-8') as f:
    notices = json.load(f)

print(f"Total notices in radar database: {len(notices)}")

# Parse first_seen
recent_items = []
for nid, data in notices.items():
    if not isinstance(data, dict):
        continue
    fs = data.get('first_seen', '')
    title = data.get('title', '')
    pub_date = data.get('pub_date', '')
    link = data.get('link', '')
    
    # Check if first_seen is from Oct 14 to Oct 18, 2026
    # formats: '2026-10-14 ...'
    if fs.startswith('2026-10-14') or fs.startswith('2026-10-15') or fs.startswith('2026-10-16') or fs.startswith('2026-10-17') or fs.startswith('2026-10-18'):
        recent_items.append({
            'id': nid,
            'first_seen': fs,
            'pub_date': pub_date,
            'title': title,
            'link': link
        })

print(f"Notices first seen in last 4 days (2026-10-14 to 2026-10-18): {len(recent_items)}")

# Sort by first_seen descending
recent_items.sort(key=lambda x: x['first_seen'], reverse=True)

for i, it in enumerate(recent_items, 1):
    print(f"{i:2d}. [{it['first_seen']}] {it['title']} (Pub: {it['pub_date']})")
