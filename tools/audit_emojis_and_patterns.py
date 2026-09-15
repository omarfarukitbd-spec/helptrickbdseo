import urllib.request
import json
import re
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

feed_url = 'https://www.helptrickbd.com/feeds/posts/default?alt=json&max-results=150'
req = urllib.request.Request(feed_url, headers={'User-Agent': 'Mozilla/5.0'})
feed = json.loads(urllib.request.urlopen(req).read().decode('utf-8'))
entries = feed['feed']['entry']

emoji_pattern = re.compile(r'[\U00010000-\U0010FFFF\uD800-\uDBFF\uDC00-\uDFFF\u2600-\u26FF\u2700-\u27BF\uFE00-\uFE0F📌📊📝⚡⭐🛡️🔒🌐🏢💾💻☁️✨👉📘📢⏱️✅🎓💬💡⚠️]')

emoji_posts = []
pattern_posts = []

for entry in entries:
    title = entry['title']['$t']
    url = ''
    for l in entry['link']:
        if l['rel'] == 'alternate':
            url = l['href']
            break
    content = entry.get('content', {}).get('$t', '')
    
    # Check emojis
    emojis = emoji_pattern.findall(content)
    if emojis:
        emoji_posts.append({
            'title': title,
            'url': url,
            'count': len(emojis),
            'unique': list(set(emojis))
        })
        
    # Check robotic repetitive patterns
    patterns_found = []
    if 'সারসংক্ষেপ (Quick Overview)' in content or 'ht-quick-answer' in content:
        patterns_found.append('Cookie-Cutter Quick Overview Box')
    if 'ht-social-share-box' in content or 'আপনার সহপাঠী ও বন্ধুদের সাথে শেয়ার করুন' in content:
        patterns_found.append('Redundant Share Box')
    if 'border-left: 4px solid #1a73e8' in content or 'border-left: 4px solid #2563eb' in content:
        patterns_found.append('Repetitive Blue Left-Border Callouts')
        
    if patterns_found:
        pattern_posts.append({
            'title': title,
            'url': url,
            'patterns': patterns_found
        })

print(f"Total live posts analyzed: {len(entries)}")
print(f"Posts still containing emojis: {len(emoji_posts)}")
print(f"Posts with repetitive AI cookie-cutter patterns: {len(pattern_posts)}\n")

print("=" * 70)
print("TOP POSTS WITH EMOJIS:")
print("=" * 70)
for p in sorted(emoji_posts, key=lambda x: x['count'], reverse=True)[:15]:
    print(f"• {p['title']} ({p['count']} emojis)")
    print(f"  URL: {p['url']}")
    print(f"  Emojis: {' '.join(p['unique'][:8])}")
    print()

print("=" * 70)
print("POSTS WITH COOKIE-CUTTER REPETITIVE PATTERNS:")
print("=" * 70)
for p in pattern_posts[:15]:
    print(f"• {p['title']}")
    print(f"  URL: {p['url']}")
    print(f"  Patterns: {', '.join(p['patterns'])}")
    print()
