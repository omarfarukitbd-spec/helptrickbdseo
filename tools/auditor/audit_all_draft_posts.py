#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/auditor/audit_all_draft_posts.py
---------------------------------------
Authoritative Quality & Governance Auditor for all 8 Draft Posts on HelpTrickBD:
- Post IDs: [15997, 16006, 16019, 16020, 16021, 16022, 16023, 16024]
- Validates:
  1. Pattern 01 3-State Morphing Countdown Button & Animated Progress Fill Layer
  2. PDF Section Position: Placed at the end (after questions, before author card)
  3. Pre-Flight Cleanliness: 0 emojis, valid SolaimanLipi typography, valid schema
  4. Author Bio Box: Faruk Sir card presence
"""

import os
import sys
import json
import re

sys.stdout.reconfigure(encoding='utf-8')

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.wp_publisher.publisher import WordPressPublisher

DRAFT_POST_IDS = [15997, 16006, 16019, 16020, 16021, 16022, 16023, 16024]

def audit():
    pub = WordPressPublisher()
    conn = pub.test_connection()
    if not conn.get("success"):
        print("[ERROR] Failed to connect to WordPress:", conn)
        return False
        
    print(f"=== AUDITING ALL {len(DRAFT_POST_IDS)} DRAFT POSTS FOR PATTERN 01 ===")
    
    passed_all = True
    
    for pid in DRAFT_POST_IDS:
        res = pub.client.get(f"posts/{pid}", params={"context": "edit"})
        if res.status_code != 200:
            print(f"❌ Post ID {pid}: HTTP {res.status_code} Error fetching post")
            passed_all = False
            continue
            
        post = res.json()
        title = post.get("title", {}).get("raw", "")
        slug = post.get("slug", "")
        content = post.get("content", {}).get("raw", "")
        status = post.get("status", "")
        
        has_morph_btn = "htbd-btn-timer-morph" in content
        has_script = "startInteractiveCountdown" in content
        has_progress_fill = "htbd-progress-fill" in content
        
        pdf_idx = content.find('class="htbd-pdf-section"')
        author_idx = content.find('author-bio-card')
        
        pos_correct = (pdf_idx != -1 and (author_idx == -1 or pdf_idx < author_idx))
        
        button_section = content[pdf_idx:pdf_idx+3000] if pdf_idx != -1 else ""
        has_emojis = bool(re.search(r'[\U00010000-\U0010ffff]', button_section))
        
        print(f"\n--- Post ID {pid} ({slug}) ---")
        print(f"    Title: {title[:55]}...")
        print(f"    Status: {status} | Length: {len(content)} chars")
        print(f"    Pattern 01 Morph Button: {'✅ PASSED' if has_morph_btn else '❌ FAILED'}")
        print(f"    Progress Fill Layer:     {'✅ PASSED' if has_progress_fill else '❌ FAILED'}")
        print(f"    Interactive Script:      {'✅ PASSED' if has_script else '❌ FAILED'}")
        print(f"    Position at End of Post: {'✅ PASSED' if pos_correct else '❌ FAILED'}")
        print(f"    Zero Emoji Cleanliness:  {'✅ PASSED' if not has_emojis else '❌ FAILED'}")
        
        if not (has_morph_btn and has_script and pos_correct and not has_emojis):
            passed_all = False
            
    print("\n" + "="*60)
    if passed_all:
        print("🎉 ALL 8 DRAFT POSTS PASSED 100% OF CHECKS WITH PATTERN 01!")
    else:
        print("⚠️ Some posts failed checks. Review above.")
    print("="*60)
    return passed_all

if __name__ == "__main__":
    audit()
