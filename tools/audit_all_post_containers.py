import os
import glob
import re
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

revived_files = glob.glob('output_posts/**/*.html', recursive=True)
print(f"Checking {len(revived_files)} output HTML files...")

issues_found = 0
for f in revived_files:
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()
    
    # Check for container classes
    containers = re.findall(r'<[a-zA-Z0-9]+[^>]*class=[\'"][^\'"]*container[^\'"]*[\'"][^>]*>', content)
    for item in containers:
        if 'ht-toc-container' not in item and 'ht-reading-progress-container' not in item:
            print(f"[CONTAINER] {f}: {item}")
            issues_found += 1
            
    # Check for style tags that target container or set fixed width
    styles = re.findall(r'<style[^>]*>(.*?)</style>', content, re.DOTALL | re.IGNORECASE)
    for s in styles:
        if 'container' in s or 'width:' in s or 'max-width:' in s:
            print(f"[STYLE] {f}: {s.strip()[:120]}")
            issues_found += 1

    # Check for unclosed divs (open count vs close count)
    open_divs = len(re.findall(r'<div\b', content, re.IGNORECASE))
    close_divs = len(re.findall(r'</div\b', content, re.IGNORECASE))
    if open_divs != close_divs:
        print(f"[DIV MISMATCH] {f}: open={open_divs}, close={close_divs} (diff={open_divs-close_divs})")
        issues_found += 1

print(f"\nTotal potential issues flagged: {issues_found}")
