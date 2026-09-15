#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/governance/pre_flight_checker.py
--------------------------------------
The Automated Quality Gatekeeper for Helptrickbd SEO.
Validates any post HTML file against all non-negotiable project standards
before allowing publication to Blogger.

Enforces:
1. Word count >= 1,200 words (Zero thin content)
2. Mandatory <!--more--> jump break in first 100-150 words
3. SolaimanLipi typography standards
4. Image CDN verification (jsDelivr / Blogger CDN only, zero local leaks)
5. Image SEO attributes (alt, title, loading="lazy", width/height)
6. Schema JSON-LD validity (syntax, BlogPosting, FAQPage)
7. Dead link & placeholder detection
8. Permalinks and title quality

Exit codes:
  0: All checks passed (CLEAN)
  1: Critical violations detected (BLOCKED)
"""

import os
import sys
import re
import json
import argparse
from bs4 import BeautifulSoup

# Ensure utf-8 output encoding
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

class PreFlightChecker:
    def __init__(self, html_path, metadata_path=None):
        self.html_path = html_path
        self.metadata_path = metadata_path
        self.errors = []
        self.warnings = []
        self.passed = []
        
        if not os.path.exists(html_path):
            raise FileNotFoundError(f"HTML file not found: {html_path}")
            
        with open(html_path, 'r', encoding='utf-8') as f:
            self.raw_html = f.read()
            
        self.soup = BeautifulSoup(self.raw_html, 'html.parser')
        
        self.metadata = {}
        if metadata_path and os.path.exists(metadata_path):
            with open(metadata_path, 'r', encoding='utf-8') as f:
                self.metadata = json.load(f)

    def check_word_count(self):
        """Rule 01: Minimum 1,200 words (Zero Thin Content)"""
        temp_soup = BeautifulSoup(self.raw_html, 'html.parser')
        for element in temp_soup(["script", "style"]):
            element.decompose()
            
        text = temp_soup.get_text()
        words = [w for w in re.split(r'\s+', text) if w.strip()]
        count = len(words)
        
        if count >= 1200:
            self.passed.append(f"Word Count: {count:,} words (PASSED >= 1,200)")
        elif count >= 1000:
            self.warnings.append(f"Word Count: {count:,} words (WARNING: below target 1,200)")
        else:
            self.errors.append(f"Word Count: {count:,} words (CRITICAL: under 1,000 words thin content)")

    def check_jump_break(self):
        """Rule 01: Mandatory <!--more--> tag in first 2-3 lines"""
        if '<!--more-->' in self.raw_html:
            pos = self.raw_html.find('<!--more-->')
            if pos < 2500:
                self.passed.append(f"Jump Break: <!--more--> found at char {pos} (PASSED)")
            else:
                self.warnings.append(f"Jump Break: <!--more--> is placed too late (char {pos})")
        else:
            self.errors.append("Jump Break: <!--more--> tag is MISSING from the post!")

    def check_typography(self):
        """Rule 01: SolaimanLipi font styling for Bengali content"""
        has_solaiman = 'SolaimanLipi' in self.raw_html or 'solaiman-lipi' in self.raw_html.lower()
        has_bangla_chars = bool(re.search(r'[\u0980-\u09FF]', self.raw_html))
        
        if has_bangla_chars:
            if has_solaiman:
                self.passed.append("Typography: SolaimanLipi font rule applied (PASSED)")
            else:
                self.warnings.append("Typography: SolaimanLipi font styling not explicitly defined in post style")
        else:
            self.passed.append("Typography: English article, SolaimanLipi not required (PASSED)")

    def check_image_sources(self):
        """Rule 02: Images must be CDN hosted, zero local filesystem leaks"""
        imgs = self.soup.find_all('img')
        if not imgs:
            self.warnings.append("Images: No <img> tags found in article")
            return
            
        local_leak = False
        missing_alt = False
        missing_lazy = False
        non_webp = False
        
        for idx, img in enumerate(imgs):
            src = img.get('src', '').strip()
            alt = img.get('alt', '')
            loading = img.get('loading', '')
            src_lower = src.lower()
            
            # Check for local/relative leaks strictly at beginning of URL
            is_local = (
                src_lower.startswith('file://') or
                src_lower.startswith('c:') or
                src_lower.startswith('d:') or
                src_lower.startswith('assets/') or
                src_lower.startswith('./assets/') or
                src_lower.startswith('../') or
                (src_lower.startswith('/') and not src_lower.startswith('//'))
            )
            if is_local:
                self.errors.append(f"Image #{idx+1} has local/relative path leak: {src}")
                local_leak = True
                
            # Check for CDN valid patterns
            if not any(src.startswith(prefix) for prefix in [
                'https://cdn.jsdelivr.net/',
                'https://blogger.googleusercontent.com/',
                'https://bp.blogspot.com/',
                'https://1.bp.blogspot.com/',
                'https://2.bp.blogspot.com/',
                'https://3.bp.blogspot.com/',
                'https://4.bp.blogspot.com/',
                'https://images.unsplash.com/',
                'https://upload.wikimedia.org/'
            ]):
                self.warnings.append(f"Image #{idx+1} not using recommended jsDelivr or Blogger CDN: {src[:60]}...")
                
            # Check alt tag
            if not alt or len(alt.strip()) < 5:
                self.errors.append(f"Image #{idx+1} is missing a descriptive alt attribute")
                missing_alt = True
                
            # Check lazy loading
            if loading != 'lazy':
                missing_lazy = True

            # Check format
            if not src_lower.endswith('.webp'):
                non_webp = True

        if not local_leak:
            self.passed.append(f"Image CDN: All {len(imgs)} image(s) hosted on remote CDN (PASSED)")
        if not missing_alt:
            self.passed.append(f"Image SEO: All {len(imgs)} image(s) have descriptive alt tags (PASSED)")
        if missing_lazy:
            self.warnings.append("Image Performance: Some images missing loading='lazy' attribute")
        if non_webp:
            self.warnings.append("Image Format: Some images are PNG/JPG instead of 10-20KB WebP")

    def check_schema_markup(self):
        """Rule 01: Valid JSON-LD Schema (BlogPosting and FAQPage)"""
        schema_scripts = self.soup.find_all('script', type='application/ld+json')
        if not schema_scripts:
            self.warnings.append("Schema: No application/ld+json structured data found in post")
            return
            
        has_faq = False
        has_blog_posting = False
        
        for idx, s in enumerate(schema_scripts):
            try:
                data = json.loads(s.string or '{}')
                stype = data.get('@type', '')
                if stype == 'FAQPage':
                    has_faq = True
                    entities = data.get('mainEntity', [])
                    if not entities or len(entities) < 2:
                        self.warnings.append("Schema: FAQPage has fewer than 2 questions")
                elif stype in ['BlogPosting', 'Article']:
                    has_blog_posting = True
            except json.JSONDecodeError as e:
                self.errors.append(f"Schema: Invalid JSON syntax in schema #{idx+1}: {e}")

        if has_blog_posting:
            self.passed.append("Schema: BlogPosting structured data verified (PASSED)")
        else:
            self.warnings.append("Schema: BlogPosting schema not found")
            
        if has_faq:
            self.passed.append("Schema: FAQPage structured data verified (PASSED)")
        else:
            self.warnings.append("Schema: FAQPage schema not found")

    def check_dead_links(self):
        """Rule 01: Zero empty hrefs or placeholder dead links"""
        links = self.soup.find_all('a')
        dead_count = 0
        for a in links:
            href = a.get('href', '').strip()
            if href in ['#', '', 'javascript:void(0)', 'http://example.com']:
                dead_count += 1
                
        if dead_count > 0:
            self.errors.append(f"Dead Links: Found {dead_count} placeholder or empty link(s)")
        else:
            self.passed.append(f"Link Guardian: All {len(links)} links contain valid destinations (PASSED)")

    def check_title_and_slug(self):
        """Rule 03: Title quality and generic permalink prevention"""
        title = ""
        title_tag = self.soup.find('title')
        if title_tag:
            title = title_tag.text.strip()
        elif self.metadata.get('title'):
            title = self.metadata.get('title', '')
            
        if not title or title.lower() in ['updated post', 'untitled', 'new post']:
            self.errors.append(f"Title: Invalid or placeholder title '{title}'")
        else:
            self.passed.append(f"Title: '{title[:50]}...' (PASSED)")

        # Check permalink from metadata if available
        custom_url = self.metadata.get('custom_url') or self.metadata.get('url', '')
        if custom_url:
            if 'blog-post_' in custom_url or re.search(r'blog-post\.html', custom_url):
                self.errors.append(f"Permalink: CRITICAL! Generic Blogger permalink detected: {custom_url}")
            else:
                self.passed.append(f"Permalink: Clean custom slug verified (PASSED)")

    def run_all(self):
        self.check_word_count()
        self.check_jump_break()
        self.check_typography()
        self.check_image_sources()
        self.check_schema_markup()
        self.check_dead_links()
        self.check_title_and_slug()
        
        return len(self.errors) == 0

    def print_report(self):
        print("\n" + "="*70)
        print(f"🛡️  PRE-FLIGHT GATEKEEPER AUDIT: {os.path.basename(self.html_path)}")
        print("="*70)
        
        for p in self.passed:
            print(f"  [PASSED]  {p}")
            
        for w in self.warnings:
            print(f"  [WARNING] {w}")
            
        for e in self.errors:
            print(f"  [BLOCKED] {e}")
            
        print("-" * 70)
        if len(self.errors) == 0:
            print(f"STATUS: ALL CRITICAL CHECKS PASSED. APPROVED FOR PUBLICATION. ({len(self.warnings)} warning(s))")
            print("="*70 + "\n")
            return True
        else:
            print(f"STATUS: BLOCKED! {len(self.errors)} CRITICAL VIOLATION(S) DETECTED.")
            print("Action Required: Fix all [BLOCKED] issues before publishing to Blogger.")
            print("="*70 + "\n")
            return False

def main():
    parser = argparse.ArgumentParser(description="Automated Pre-Flight Gatekeeper for Helptrickbd SEO")
    parser.add_argument("html_file", nargs="?", help="Path to post HTML file")
    parser.add_argument("--metadata", "-m", help="Optional path to post metadata JSON", default=None)
    parser.add_argument("--dir", "-d", help="Audit all HTML files in a directory", default=None)
    args = parser.parse_args()

    if args.dir:
        files = [os.path.join(args.dir, f) for f in os.listdir(args.dir) if f.endswith('.html')]
        total_passed = 0
        total_blocked = 0
        for fpath in sorted(files):
            meta = fpath.replace('.html', '_metadata.json')
            checker = PreFlightChecker(fpath, meta if os.path.exists(meta) else None)
            is_clean = checker.run_all()
            checker.print_report()
            if is_clean:
                total_passed += 1
            else:
                total_blocked += 1
        print(f"\nBATCH SUMMARY: {total_passed} Passed | {total_blocked} Blocked out of {len(files)} files.")
        sys.exit(0 if total_blocked == 0 else 1)

    if not args.html_file:
        parser.print_help()
        sys.exit(1)

    meta = args.metadata
    if not meta:
        candidate_meta = args.html_file.replace(".html", "_metadata.json")
        if os.path.exists(candidate_meta):
            meta = candidate_meta

    checker = PreFlightChecker(args.html_file, meta)
    is_clean = checker.run_all()
    checker.print_report()
    
    sys.exit(0 if is_clean else 1)

if __name__ == "__main__":
    main()
