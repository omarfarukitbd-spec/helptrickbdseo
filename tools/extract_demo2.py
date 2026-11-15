import re

path = r'c:\Users\omarf\OneDrive\Desktop\modern-shikkha-portal-demo.html'
with open(path, encoding='utf-8') as f:
    text = f.read()

paper_match = re.search(r'<div[^>]*id="demo-paper"[^>]*>(.*?)</div>\s*<!--\s*==+\s*DEMO 3', text, re.DOTALL)
if paper_match:
    demo2_html = paper_match.group(1)
    print("Demo 2 HTML length:", len(demo2_html))
    
    # Save demo 2 html to a clean inspection file
    with open('tools/demo2_extracted.html', 'w', encoding='utf-8') as out:
        out.write(demo2_html)
    print("Saved to tools/demo2_extracted.html")

    # Find all section tags, classes, and sub-elements
    sections = re.findall(r'<section[^>]*>(.*?)</section>', demo2_html, re.DOTALL)
    print(f"Total sections in Demo 2: {len(sections)}")
    for i, s in enumerate(sections):
        cls_match = re.search(r'class="([^"]*)"', s)
        cls = cls_match.group(1) if cls_match else "none"
        h = re.search(r'<h[1-4][^>]*>(.*?)</h[1-4]>', s)
        h_text = re.sub('<[^>]+>', '', h.group(1)).strip() if h else "No heading"
        print(f"Section {i+1} [class: {cls}]: {h_text}")

# Also extract CSS rules for .n- (paper/demo2) classes
css_match = re.findall(r'(\.n-[^{]+\{[^}]+\})', text)
print(f"\nTotal .n- CSS rules found: {len(css_match)}")
with open('tools/demo2_css.css', 'w', encoding='utf-8') as out:
    for c in css_match:
        out.write(c + "\n")
print("Saved Demo 2 CSS to tools/demo2_css.css")
