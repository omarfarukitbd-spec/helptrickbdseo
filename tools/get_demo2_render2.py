import re

path = r'c:\Users\omarf\OneDrive\Desktop\modern-shikkha-portal-demo.html'
with open(path, encoding='utf-8') as f:
    text = f.read()

idx = text.find("/* newspaper category list + sort */")
if idx != -1:
    print(text[idx:idx+2500])
