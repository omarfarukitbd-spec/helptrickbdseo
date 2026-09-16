import re

def find_block():
    with open('Helptrickbd theme code.xml', 'r', encoding='utf-8') as f:
        text = f.read()

    # Search for block-section, raw-main-wrapper, or t-hero-flow
    idx = text.find('case"block1":')
    if idx != -1:
        print("=== case block1 ===")
        print(text[idx:idx+600])

    idx2 = text.find('case"block2":')
    if idx2 != -1:
        print("\n=== case block2 ===")
        print(text[idx2:idx2+600])

    # Search for CSS styling of entry-title in these overlay boxes
    print("\n=== CSS for entery-category-fly / overlay titles ===")
    matches = re.findall(r'(\.entery-category-fly[^{]*)\{([^}]+)\}', text)
    for sel, rule in matches:
        print(f"  {sel.strip()} -> {rule.strip()[:80]}")

if __name__ == '__main__':
    find_block()
