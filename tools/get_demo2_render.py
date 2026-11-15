import re

path = r'c:\Users\omarf\OneDrive\Desktop\modern-shikkha-portal-demo.html'
with open(path, encoding='utf-8') as f:
    text = f.read()

# Search for the script that sets up demo-paper
idx = text.find("document.getElementById('n-side')")
if idx != -1:
    print(text[idx-200:idx+1500])
