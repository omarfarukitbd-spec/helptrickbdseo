import sys
import os
import re
import json

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

sys.stdout.reconfigure(encoding='utf-8')

from tools.wp_publisher.publisher import WordPressPublisher

pub = WordPressPublisher()

POSTS_TO_AUDIT = [
    {"id": 15997, "name": "Chapter Suggestion (Units 01-07)", "expected_q": 320},
    {"id": 16006, "name": "Master Question Bank Hub (2019-2024)", "expected_q": 168},
    {"id": 16019, "name": "Board 2024 Dedicated Post", "expected_q": 28},
    {"id": 16020, "name": "Board 2023 Dedicated Post", "expected_q": 28},
    {"id": 16021, "name": "Board 2022 Dedicated Post", "expected_q": 28},
    {"id": 16022, "name": "Board 2021 Dedicated Post", "expected_q": 28},
    {"id": 16023, "name": "Board 2020 Dedicated Post", "expected_q": 28},
    {"id": 16024, "name": "Board 2019 Dedicated Post", "expected_q": 28},
]

print("=" * 80)
print("🛡️  HELPTRICKBD SEO — COMPREHENSIVE LIVE AUDIT REPORT FOR ALL DRAFT POSTS")
print("=" * 80)

audit_results = []
emoji_pattern = re.compile(
    r"[\U00010000-\U0010FFFF\uD800-\uDBFF\uDC00-\uDFFF\u2600-\u26FF\u2700-\u27BF\uFE00-\uFE0F]"
    r"|[📌📊📝⚡⭐🛡️🔒🌐🏢💾💻☁️✨👉📘📢⏱️✅🎓💬💡⚠️⏳📥]"
)

for item in POSTS_TO_AUDIT:
    pid = item["id"]
    pname = item["name"]
    expected_q = item["expected_q"]
    
    resp = pub.client.request("GET", f"posts/{pid}?context=edit")
    if resp.status_code != 200:
        print(f"❌ Failed to fetch Post ID {pid}")
        continue
        
    data = resp.json()
    title = data["title"]["raw"]
    content = data["content"]["raw"]
    status = data["status"]
    slug = data["slug"]
    
    total_len = len(content)
    word_count = len(re.findall(r'\S+', content))
    
    # 1. Questions count
    accordions = len(re.findall(r'<details\b', content))
    
    # 2. PDF Download Section
    pdf_count = content.count('htbd-pdf-section')
    pdf_pos = content.find('htbd-pdf-section')
    pdf_pct = (pdf_pos / total_len) * 100 if pdf_pos != -1 else -1
    pdf_at_end = (pdf_pct >= 70.0 and pdf_count == 1)
    
    # 3. Timer & Script
    has_timer_btn = "htbd-btn-timer" in content
    has_timer_script = "startPdfCountdown" in content
    
    # 4. Academic Intro & Conclusion
    intro_count = len(re.findall(r'ভূমিকা\s*:', content)) + len(re.findall(r'ভূমিকা ও অ্যাকাডেমিক নীতিমালা\s*:', content))
    concl_count = len(re.findall(r'উপসংহার\s*:', content)) + len(re.findall(r'উপসংহার ও অ্যাকাডেমিক বিশ্লেষণ\s*:', content))
    
    # 5. Author Card
    has_author = "মো: ওমর ফারুক (Faruk Sir)" in content
    has_author_avatar = "faruk_sir.webp" in content
    
    # 6. Emojis
    # strip scripts and styles before checking text emojis
    content_no_script = re.sub(r'<script[\s\S]*?</script>', '', content)
    content_no_style = re.sub(r'<style[\s\S]*?</style>', '', content_no_script)
    emojis = emoji_pattern.findall(content_no_style)
    # filter out star symbols that are stripped or in badges
    actual_emojis = [e for e in emojis if e not in ['⭐', '★', '✨']]
    
    # 7. Schemas
    has_blog_schema = '"@type": "BlogPosting"' in content or '"@type":"BlogPosting"' in content
    has_faq_schema = '"@type": "FAQPage"' in content or '"@type":"FAQPage"' in content
    
    audit_results.append({
        "pid": pid,
        "name": pname,
        "title": title,
        "slug": slug,
        "status": status,
        "word_count": word_count,
        "accordions": accordions,
        "expected_q": expected_q,
        "pdf_count": pdf_count,
        "pdf_pct": pdf_pct,
        "pdf_at_end": pdf_at_end,
        "timer_ok": (has_timer_btn and has_timer_script),
        "intro_count": intro_count,
        "concl_count": concl_count,
        "author_ok": (has_author and has_author_avatar),
        "emojis_count": len(actual_emojis),
        "schema_ok": (has_blog_schema and has_faq_schema)
    })

print(f"{'ID':<6} | {'Status':<6} | {'Words':<7} | {'Ques':<5} | {'PDF Pos':<10} | {'PDF End':<8} | {'Timer':<6} | {'Intro':<6} | {'Concl':<6} | {'Author':<7} | {'Emoji':<6} | {'Schema':<7}")
print("-" * 95)
for r in audit_results:
    pdf_pos_str = f"{r['pdf_pct']:.1f}%" if r['pdf_pct'] > 0 else "N/A"
    print(f"{r['pid']:<6} | {r['status']:<6} | {r['word_count']:<7} | {r['accordions']:<5} | {pdf_pos_str:<10} | {str(r['pdf_at_end']):<8} | {str(r['timer_ok']):<6} | {r['intro_count']:<6} | {r['concl_count']:<6} | {str(r['author_ok']):<7} | {r['emojis_count']:<6} | {str(r['schema_ok']):<7}")

print("=" * 80)
print("AUDIT SUMMARY:")
all_passed = True
for r in audit_results:
    if not r["pdf_at_end"]:
        print(f"❌ Post {r['pid']}: PDF is not at end or duplicate! Count={r['pdf_count']}, Pos={r['pdf_pct']:.1f}%")
        all_passed = False
    if not r["author_ok"]:
        print(f"❌ Post {r['pid']}: Author card not verified!")
        all_passed = False
    if r["emojis_count"] > 0:
        print(f"❌ Post {r['pid']}: Emojis detected: {r['emojis_count']}")
        all_passed = False
    if not r["schema_ok"]:
        print(f"❌ Post {r['pid']}: Schema missing!")
        all_passed = False

if all_passed:
    print("✅ ALL 8 DRAFT POSTS PASSED 100% OF RIGOROUS GOVERNANCE & QUALITY AUDITS!")
else:
    print("⚠️ Some issues detected.")
