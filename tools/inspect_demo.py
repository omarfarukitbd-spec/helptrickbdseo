import re

path = r'c:\Users\omarf\OneDrive\Desktop\modern-shikkha-portal-demo.html'
with open(path, encoding='utf-8') as f:
    text = f.read()

# Find details about the 3 tabs
buttons = re.findall(r'<button class="switch-btn"[^>]*>(.*?)</button>', text, re.DOTALL)
for i, b in enumerate(buttons):
    title = re.search(r'<b>(.*?)</b>', b)
    sub = re.search(r'<span>(.*?)</span>', b)
    print(f"Tab {i+1}: {title.group(1) if title else ''} - {sub.group(1) if sub else ''}")

# Extract sections for demo-modern
modern_match = re.search(r'<div[^>]*id="demo-modern"[^>]*>(.*?)</div>\s*<!--\s*==+\s*DEMO 2', text, re.DOTALL)
if modern_match:
    m_text = modern_match.group(1)
    print("\n=== DEMO 1 (MODERN) SECTIONS ===")
    m_secs = re.findall(r'<section[^>]*class="([^"]*)"[^>]*>.*?<h[1-4][^>]*>(.*?)</h[1-4]>', m_text, re.DOTALL)
    for cls, h in m_secs:
        print(f"Section [{cls}]: {re.sub('<[^>]+>', '', h).strip()}")

# Extract sections for demo-paper
paper_match = re.search(r'<div[^>]*id="demo-paper"[^>]*>(.*?)</div>\s*<!--\s*==+\s*DEMO 3', text, re.DOTALL)
if paper_match:
    p_text = paper_match.group(1)
    print("\n=== DEMO 2 (PAPER / SERIF) SECTIONS ===")
    p_secs = re.findall(r'<section[^>]*class="([^"]*)"[^>]*>.*?<h[1-4][^>]*>(.*?)</h[1-4]>', p_text, re.DOTALL)
    for cls, h in p_secs:
        print(f"Section [{cls}]: {re.sub('<[^>]+>', '', h).strip()}")

# Extract sections for demo-classic
classic_match = re.search(r'<div[^>]*id="demo-classic"[^>]*>(.*?)</div>\s*<!--\s*==+\s*WordPress', text, re.DOTALL)
if classic_match:
    c_text = classic_match.group(1)
    print("\n=== DEMO 3 (CLASSIC) SECTIONS ===")
    c_secs = re.findall(r'<section[^>]*class="([^"]*)"[^>]*>.*?<h[1-4][^>]*>(.*?)</h[1-4]>', c_text, re.DOTALL)
    for cls, h in c_secs:
        print(f"Section [{cls}]: {re.sub('<[^>]+>', '', h).strip()}")
