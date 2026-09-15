import urllib.request
import json
import re
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

print("Fetching all live posts from HelpTrickBD feed to scan for container classes...")
# Blogger feed can return up to 150 posts
feed_url = "https://www.helptrickbd.com/feeds/posts/default?alt=json&max-results=150"
req = urllib.request.Request(feed_url, headers={'User-Agent': 'Mozilla/5.0'})

try:
    response = urllib.request.urlopen(req)
    data = json.loads(response.read().decode('utf-8'))
    entries = data.get('feed', {}).get('entry', [])
    print(f"Total live posts fetched: {len(entries)}\n")
    
    found_issues = []
    for i, entry in enumerate(entries):
        title = entry.get('title', {}).get('$t', 'Untitled')
        url = ""
        for link in entry.get('link', []):
            if link.get('rel') == 'alternate':
                url = link.get('href', '')
                break
                
        content = entry.get('content', {}).get('$t', '')
        
        # 1. Exact container class match
        exact_containers = re.findall(r'<[a-zA-Z0-9]+[^>]*class=[\'"][^\'"]*\bcontainer\b[^\'"]*[\'"][^>]*>', content, re.IGNORECASE)
        
        # 2. Style tags modifying container
        style_matches = []
        styles = re.findall(r'<style[^>]*>(.*?)</style>', content, re.DOTALL | re.IGNORECASE)
        for s in styles:
            if re.search(r'\bcontainer\b', s, re.IGNORECASE):
                style_matches.append(s.strip()[:100])
                
        # 3. Fixed width wrapper
        fixed_width_wrappers = re.findall(r'style=[\'"][^\'"]*width\s*:\s*(?:1[0-9]{3}|[2-9][0-9]{2})px[^\'"]*[\'"]', content, re.IGNORECASE)
        
        if exact_containers or style_matches or fixed_width_wrappers:
            print(f"🚨 FOUND ISSUE in Post #{i+1}: {title}")
            print(f"   URL: {url}")
            if exact_containers:
                print(f"   Exact container tags: {exact_containers}")
            if style_matches:
                print(f"   Style tag targeting container: {style_matches}")
            if fixed_width_wrappers:
                print(f"   Fixed px width: {fixed_width_wrappers}")
            print("-" * 60)
            found_issues.append((title, url, exact_containers, style_matches, fixed_width_wrappers))
            
    if not found_issues:
        print("✅ CLEAN! None of the live posts on HelpTrickBD contain class='container' or any <style> targeting .container!")
    else:
        print(f"\n⚠️ Total posts with container or fixed widths: {len(found_issues)}")

except Exception as e:
    print(f"Error fetching feed: {e}")
