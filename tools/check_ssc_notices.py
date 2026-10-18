import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('tools/trend_forecaster/seen_radar_notices.json', 'r', encoding='utf-8') as f:
    notices = json.load(f)

print(f"Total notices in DB: {len(notices)}")

matches = []
for nid, data in notices.items():
    if not isinstance(data, dict):
        continue
    title = data.get('title', '')
    if any(k in title.lower() for k in ['ssc', 'এসএসসি', 'নির্বাচনী', 'ফরম পূরণ', 'ঢাকা বোর্ড', 'test']):
        matches.append((nid, data))

print(f"Matches found: {len(matches)}\n")
for nid, d in matches:
    print(f"ID: {nid}")
    print(f"Title: {d.get('title')}")
    print(f"Date: {d.get('pub_date')}, First seen: {d.get('first_seen')}")
    print(f"Link: {d.get('link')}")
    print("-" * 60)
