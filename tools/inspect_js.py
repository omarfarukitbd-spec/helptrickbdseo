import re

path = r'c:\Users\omarf\OneDrive\Desktop\modern-shikkha-portal-demo.html'
with open(path, encoding='utf-8') as f:
    text = f.read()

# Look for javascript functions populating demo 2
js_matches = re.findall(r'(function\s+renderPaper[a-zA-Z0-9_]*\s*\(.*?\)\s*\{.*?\}|function\s+initPaper[a-zA-Z0-9_]*\s*\(.*?\)\s*\{.*?\})', text, re.DOTALL)
print(f"Paper JS functions found: {len(js_matches)}")
for j in js_matches[:10]:
    name = re.match(r'function\s+([a-zA-Z0-9_]+)', j)
    print("-", name.group(1) if name else "")

# Search for n-grid, n-side, n-thumb-list rendering
scripts = re.findall(r'(\/\*.*?Paper.*?\*\/|const\s+paper[a-zA-Z0-9_]+|function\s+[a-zA-Z0-9_]*paper[a-zA-Z0-9_]*)', text, re.IGNORECASE)
print(f"Scripts references: {len(scripts)}")

# Let's search for "n-side" in text
for m in re.finditer(r'n-side', text):
    start = max(0, m.start() - 50)
    end = min(len(text), m.end() + 200)
    snippet = text[start:end]
    if 'innerHTML' in snippet or 'appendChild' in snippet or '<article' in snippet:
        print("\nSnippet near n-side:\n", snippet[:250])
