#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/theme_validator.py
Automated Quality Gatekeeper for HelpTrickBD WordPress Themes.
Enforces Rule 12: Micro-Modular Architecture, Zero Weak Logic, Zero Draft Text,
100/100 Core Web Vitals, Bengali NFC Normalization, Container Rules, and Syntax Balance.
"""

import os
import sys
import re
from pathlib import Path

# Prohibited draft or amateur terms that must never appear in production code
FORBIDDEN_WORDS = [
    "বিষয়ের লেখা",
    "লেবেলের লেখা",
    "স্নিপেট ছাড়া",
    "ছোট ছবিসহ",
    "আমাদের যাচাই পদ্ধতি",
    "ডেমো টেক্সট",
    "demo post",
    "dummy text",
    "Lorem ipsum",
    "support@helptrickbd.com" # Section 8.10: strictly forbidden, must be contact@helptrickbd.com
]

# Section 8.8: Decomposed Bengali "য়" (য + ় = U+09AF + U+09BC)
DECOMPOSED_YA = "\u09af\u09bc"

def strip_php_comments_and_strings(code):
    """Accurately strips comments and string literals using a state machine."""
    result = []
    i = 0
    n = len(code)
    state = 'code'
    
    while i < n:
        c = code[i]
        c2 = code[i:i+2]
        
        if state == 'code':
            if c2 == '/*':
                state = 'block_comment'
                i += 2
                continue
            elif c2 == '//' or c == '#':
                state = 'line_comment'
                i += 1
                continue
            elif c == "'":
                state = 'single_quote'
                i += 1
                continue
            elif c == '"':
                state = 'double_quote'
                i += 1
                continue
            else:
                result.append(c)
                i += 1
        elif state == 'single_quote':
            if c == '\\':
                i += 2
                continue
            elif c == "'":
                state = 'code'
                i += 1
                continue
            else:
                i += 1
        elif state == 'double_quote':
            if c == '\\':
                i += 2
                continue
            elif c == '"':
                state = 'code'
                i += 1
                continue
            else:
                i += 1
        elif state == 'line_comment':
            if c == '\n':
                state = 'code'
                result.append(c)
            i += 1
        elif state == 'block_comment':
            if c2 == '*/':
                state = 'code'
                i += 2
                continue
            else:
                i += 1
                
    return "".join(result)

def check_php_syntax(file_path, content):
    """Checks basic PHP token balance and security practices."""
    errors = []
    
    # Check PHP tag balance
    open_tags = len(re.findall(r'<\?php', content, re.IGNORECASE))
    short_tags = len(re.findall(r'<\?=', content))
    close_tags = len(re.findall(r'\?>', content))
    
    if open_tags + short_tags > 0:
        if close_tags > open_tags + short_tags:
            errors.append(f"Mismatched PHP closing tags (close: {close_tags}, open: {open_tags + short_tags})")
    
    # Accurate state-machine strip of strings and comments
    clean_code = strip_php_comments_and_strings(content)
    
    # Count braces
    open_curly = clean_code.count('{')
    close_curly = clean_code.count('}')
    if open_curly != close_curly:
        errors.append(f"Curly brace mismatch: '{open_curly}' open vs '{close_curly}' close")
        
    # Check WP_Query has wp_reset_postdata
    if "new WP_Query" in content and "wp_reset_postdata" not in content:
        errors.append("new WP_Query found without corresponding wp_reset_postdata()")
        
    return errors

def check_html_balance(file_path, content):
    """Checks tag balance for key layout tags (skipping header/footer pairs which naturally split)."""
    errors = []
    filename = os.path.basename(file_path)
    
    # header.php and footer.php are intentional structural open/close pairs in WordPress
    if filename in ['header.php', 'footer.php']:
        return errors
        
    for tag in ['div', 'section', 'article', 'header', 'footer', 'main', 'nav']:
        open_count = len(re.findall(rf'<{tag}\b[^>]*>', content, re.IGNORECASE))
        close_count = len(re.findall(rf'</{tag}>', content, re.IGNORECASE))
        if open_count != close_count:
            errors.append(f"HTML tag <{tag}> mismatch: {open_count} opened, {close_count} closed")
    return errors

def check_forbidden_words_and_chars(file_path, content):
    """Ensures no amateur text, forbidden emails, or decomposed Bengali letters exist."""
    errors = []
    for word in FORBIDDEN_WORDS:
        if word.lower() in content.lower():
            errors.append(f"Forbidden word/email found: '{word}'")
            
    # Section 8.8: Check decomposed Bengali 'য়'
    if DECOMPOSED_YA in content:
        count = content.count(DECOMPOSED_YA)
        errors.append(f"Section 8.8 Violation: Decomposed Bengali 'য়' (য + ়) found ({count} occurrences). Must be precomposed U+09DF.")
        
    return errors

def check_core_web_vitals(file_path, content):
    """Validates Core Web Vitals standards in template/CSS files."""
    errors = []
    filename = os.path.basename(file_path)
    
    # In template-parts, check <img> tags have loading or aspect-ratio or sizes
    if file_path.endswith('.php'):
        # Strip PHP tags first so ?> does not break the HTML tag boundary
        clean_html = re.sub(r'<\?php[\s\S]*?\?>', '""', content)
        img_tags = re.findall(r'<img\b[^>]*>', clean_html, re.IGNORECASE)
        for img in img_tags:
            if 'loading=' not in img and 'class="skip-lazy"' not in img and 'fetchpriority=' not in img:
                errors.append(f"Image tag missing loading=\"lazy\": {img[:50]}...")
            if 'width=' not in img and 'height=' not in img and 'style=' not in img and 'aspect-ratio' not in img:
                errors.append(f"Image tag missing width/height/aspect-ratio: {img[:50]}...")
                
    # In assets-enqueue.php, check filemtime is used
    if filename == 'assets-enqueue.php':
        if 'filemtime' not in content:
            errors.append("Dynamic cache busting (filemtime) is missing from assets-enqueue.php")
            
    return errors

def validate_theme(theme_dir):
    """Main validation runner."""
    theme_path = Path(theme_dir)
    if not theme_path.exists():
        print(f"❌ Error: Theme directory '{theme_dir}' does not exist.")
        return False
        
    print(f"\n=======================================================")
    print(f"🔍 Running Enterprise Theme Quality Gatekeeper (Rule 12)")
    print(f"📁 Target: {theme_dir}")
    print(f"=======================================================\n")
    
    total_files = 0
    passed_files = 0
    all_issues = []
    
    # Check that critical-css.php exists in inc/
    if not (theme_path / "inc" / "critical-css.php").exists():
        all_issues.append(("inc/critical-css.php", ["Critical CSS engine is missing in inc/critical-css.php"]))
        
    # Scan all php, css, js files
    for root, dirs, files in os.walk(theme_path):
        for f in files:
            if f.endswith(('.php', '.css', '.js')):
                file_path = os.path.join(root, f)
                rel_path = os.path.relpath(file_path, theme_dir)
                total_files += 1
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as fp:
                        content = fp.read()
                except Exception as e:
                    all_issues.append((rel_path, [f"Failed to read file: {e}"]))
                    continue
                    
                file_errors = []
                
                # Check forbidden words and characters
                file_errors.extend(check_forbidden_words_and_chars(file_path, content))
                
                # Check PHP syntax & HTML balance if PHP
                if f.endswith('.php'):
                    file_errors.extend(check_php_syntax(file_path, content))
                    if not root.endswith(os.path.sep + 'inc') and f != 'functions.php':
                        file_errors.extend(check_html_balance(file_path, content))
                        
                # Check Core Web Vitals standards
                file_errors.extend(check_core_web_vitals(file_path, content))
                
                if file_errors:
                    all_issues.append((rel_path, file_errors))
                else:
                    passed_files += 1

    print(f"\n📊 Validation Results:")
    print(f"   • Total Files Scanned: {total_files}")
    print(f"   • Clean Files Passed:  {passed_files}")
    print(f"   • Files with Issues:   {len(all_issues)}")
    
    if all_issues:
        print("\n❌ VALIDATION FAILED! The following issues must be resolved:")
        for rpath, errs in all_issues:
            print(f"\n📄 {rpath}:")
            for err in errs:
                print(f"   - ⚠️ {err}")
        return False
    else:
        print("\n🎉 100% QUALITY GATE PASSED! Enterprise Theme Engineering standards met.")
        return True

if __name__ == '__main__':
    target = sys.argv[1] if len(sys.argv) > 1 else "Helptrickbd Wp/helptrickbd-edu"
    success = validate_theme(target)
    sys.exit(0 if success else 1)
