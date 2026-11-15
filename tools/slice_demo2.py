import re

path = r'c:\Users\omarf\OneDrive\Desktop\modern-shikkha-portal-demo.html'
with open(path, encoding='utf-8') as f:
    text = f.read()

idx_paper = text.find('id="demo-paper"')
idx_classic = text.find('id="demo-classic"')
print("idx_paper:", idx_paper, "idx_classic:", idx_classic)

if idx_paper != -1 and idx_classic != -1:
    demo2_raw = text[idx_paper:idx_classic]
    with open('tools/demo2_raw.html', 'w', encoding='utf-8') as out:
        out.write(demo2_raw)
    print("Length of demo2:", len(demo2_raw))
    
    # Find all main components in demo 2
    tags = re.findall(r'<([a-zA-Z0-9]+)\s+[^>]*class="([^"]*)"', demo2_raw)
    unique_classes = set()
    for t, c in tags:
        for cls in c.split():
            if cls.startswith('n-') or cls.startswith('ht-') or cls.startswith('paper-'):
                unique_classes.add(cls)
    print("Unique classes in Demo 2:", sorted(list(unique_classes)))
