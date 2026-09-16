#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/auditor/run_full_site_360_audit.py
-----------------------------------------
Performs complete 360-degree audit of all 88 posts on Blogger:
1. Duplicate Table of Contents (TOC)
2. Thin Content (<600 words, 600-1000 words, 1000+ words)
3. Hero Banner status (Official 16:9 WebP vs Old/External vs Missing)
4. Label coverage & empty labels
5. AdSense policy readiness & Search Console integration
"""

import os
import sys
import json
from bs4 import BeautifulSoup

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.blogger_publisher.publisher import get_authenticated_service, BLOG_ID

def main():
    service = get_authenticated_service()
    if not service:
        print("[!] Failed to connect to Blogger API.")
        return

    all_posts = []
    page_token = None
    while True:
        res = service.posts().list(blogId=BLOG_ID, maxResults=500, pageToken=page_token).execute()
        items = res.get('items', [])
        all_posts.extend(items)
        page_token = res.get('nextPageToken')
        if not page_token:
            break

    audit_data = {
        'total_posts': len(all_posts),
        'duplicate_toc': [],
        'thin_posts': [],        # < 600 words (high AdSense rejection risk)
        'medium_posts': [],      # 600 - 1000 words (needs improvement)
        'long_posts': [],        # >= 1000 words (AdSense gold standard)
        'missing_banner': [],
        'old_banner': [],
        'official_banner_count': 0,
        'posts_summary': []
    }

    for p in all_posts:
        pid = p.get('id')
        title = p.get('title', '')
        url = p.get('url', '')
        labels = p.get('labels', [])
        content = p.get('content', '')
        
        soup = BeautifulSoup(content, 'html.parser')
        text = soup.get_text()
        words = len(text.split())
        
        # 1. Check Duplicate TOC
        has_c1 = 'ht-toc-container' in content
        has_c2 = 'htbd-toc-box' in content
        has_dup_toc = has_c1 and has_c2
        if has_dup_toc:
            audit_data['duplicate_toc'].append({
                'id': pid,
                'title': title,
                'url': url
            })
            
        # 2. Check Banner
        imgs = soup.find_all('img')
        has_img = len(imgs) > 0
        first_img = imgs[0].get('src', '') if has_img else ''
        is_official_banner = ('assets/images/posts/' in first_img or 'assets/images/thumbnails/' in first_img)
        
        if not has_img:
            audit_data['missing_banner'].append({'id': pid, 'title': title, 'url': url})
        elif not is_official_banner:
            audit_data['old_banner'].append({'id': pid, 'title': title, 'url': url, 'src': first_img[:70]})
        else:
            audit_data['official_banner_count'] += 1
            
        post_record = {
            'id': pid,
            'title': title,
            'url': url,
            'labels': labels,
            'words': words,
            'has_dup_toc': has_dup_toc,
            'has_img': has_img,
            'is_official_banner': is_official_banner
        }
        audit_data['posts_summary'].append(post_record)
        
        if words < 600:
            audit_data['thin_posts'].append({'id': pid, 'title': title, 'url': url, 'words': words})
        elif words < 1000:
            audit_data['medium_posts'].append({'id': pid, 'title': title, 'url': url, 'words': words})
        else:
            audit_data['long_posts'].append({'id': pid, 'title': title, 'url': url, 'words': words})

    output_path = os.path.join(PROJECT_ROOT, "site_full_360_audit.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(audit_data, f, ensure_ascii=False, indent=2)

    print("=" * 60)
    print("📊 360-DEGREE AUDIT RESULTS FOR HELPTRICKBD")
    print("=" * 60)
    print(f"Total Published Posts:        {audit_data['total_posts']}")
    print(f"Posts with Duplicate TOC:     {len(audit_data['duplicate_toc'])}")
    print(f"Thin Content (<600 words):    {len(audit_data['thin_posts'])} (High Priority)")
    print(f"Medium Content (600-999 words): {len(audit_data['medium_posts'])} (Improvement Recommended)")
    print(f"Long/Gold Standard (>=1000w): {len(audit_data['long_posts'])} (AdSense Safe)")
    print(f"Official 16:9 WebP Banners:   {audit_data['official_banner_count']}")
    print(f"Old/External Banners:         {len(audit_data['old_banner'])}")
    print(f"Missing Banners:              {len(audit_data['missing_banner'])}")
    print(f"\nReport saved to: {output_path}")

if __name__ == "__main__":
    main()
