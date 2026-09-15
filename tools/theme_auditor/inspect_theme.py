import re

def deep_theme_audit():
    with open('Helptrickbd theme code.xml', 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()

    print("==================================================")
    print("      FLEXSPOT THEME DEEP CODE & ARCHITECTURE     ")
    print("==================================================")

    # 1. Skin / Layout details
    body_bg = re.search(r'--body-color-main:\s*([^;]+);', text)
    link_color = re.search(r'--all-link-color:\s*([^;]+);', text)
    main_text = re.search(r'--main-text-color:\s*([^;]+);', text)
    outer_width = re.search(r'<Variable name="outerContainer.width"[^>]+value="([^"]+)"', text)
    sidebar_width = re.search(r'<Variable name="sidebar.width"[^>]+value="([^"]+)"', text)

    print(f"Theme Body Width: {outer_width.group(1) if outer_width else 'N/A'}")
    print(f"Sidebar Width: {sidebar_width.group(1) if sidebar_width else 'N/A'}")
    print(f"Body BG Token: {body_bg.group(1) if body_bg else 'N/A'}")
    print(f"Link Color Token: {link_color.group(1) if link_color else 'N/A'}")
    print(f"Main Text Token: {main_text.group(1) if main_text else 'N/A'}")

    # 2. Main DOM Hierarchy
    print("\n--- DOM LAYOUT CONTAINER HIERARCHY ---")
    containers = [
        "top-bar", "header-wrapper", "Super-MenuWorks", "ticker-wrapper",
        "main-wrapper", "content-wrapper", "main", "sidebar-wrapper", "sidebar",
        "post-body", "entry-content", "post-filter", "raw-box", "feed-view",
        "footer-wrapper", "footer-copyright"
    ]
    for c in containers:
        found_id = f'id="{c}"' in text or f"id='{c}'" in text
        found_class = f'class="{c}' in text or f"class='{c}" in text
        print(f"  Container '{c}': ID={found_id} | CLASS={found_class}")

    # 3. Post Body Specific Typography & Elements
    print("\n--- POST BODY ARCHITECTURE (.post-body) ---")
    pb_rules = re.findall(r'(\.post-body\s*[^{]*)\{([^}]+)\}', text)
    for sel, rules in pb_rules:
        sel_clean = sel.strip()
        rules_clean = " ".join(rules.strip().split())
        print(f"  {sel_clean}: {rules_clean[:100]}...")

    # 4. Heading styles (h1, h2, h3, h4)
    print("\n--- HEADING STYLES IN CONTENT ---")
    headings = re.findall(r'(\.post-body\s+h[1-6][^{]*)\{([^}]+)\}', text)
    for h_sel, h_rules in headings:
        print(f"  {h_sel.strip()} -> {' '.join(h_rules.strip().split())}")

    # 5. Media Queries & Responsive Breakpoints
    print("\n--- RESPONSIVE BREAKPOINTS ---")
    mq_blocks = re.findall(r'(@media[^{]+)\{((?:[^{}]*\{[^{}]*\})*[^{}]*)\}', text)
    for mq, block in mq_blocks:
        print(f"\nBreakpoint: {mq.strip()}")
        # find target classes in this breakpoint
        bp_classes = re.findall(r'([.#][a-zA-Z0-9_-]+)\s*\{', block)
        print(f"  Affects {len(set(bp_classes))} classes: {', '.join(sorted(list(set(bp_classes)))[:12])}...")

    # 6. Check Core Scripts & Functionality
    print("\n--- CORE SCRIPTS & FUNCTIONALITIES ---")
    features = {
        "Theia Sticky Sidebar": "theiaStickySidebar" in text,
        "Table of Contents (ndabas toc)": "Table of Contents jQuery Plugin" in text or "data-toc" in text,
        "Menuiki Mobile Navigation": "Menuiki" in text,
        "Lazy Ticker": "lazyticker" in text,
        "SolaimanLipi Custom Setup": "SolaimanLipi" in text,
        "Noto Sans Bengali": "Noto+Sans+Bengali" in text,
        "FontAwesome 6": "Font Awesome 6" in text or "fontawesome" in text.lower(),
        "Disqus Comments": "disqus" in text.lower(),
        "Blogger Native Comments": "comment-editor" in text,
        "Google AdSense": "adsbygoogle" in text,
        "Blogger Dynamic Views / v2 widgets": "b:defaultwidgetversion='2'" in text
    }
    for feat, present in features.items():
        print(f"  {feat}: {'YES' if present else 'NO'}")

    # 7. Audit & Recommendations Findings
    print("\n--- AUDIT FINDINGS FOR IMPROVEMENT ---")
    issues = []
    
    # Check 1: Google AdSense duplicate script loading
    ads_scripts = re.findall(r'<script[^>]*src=[\'"][^\'"]*adsbygoogle\.js[\'"][^>]*>', text)
    if len(ads_scripts) > 1:
        issues.append(f"Duplicate Google AdSense scripts loaded ({len(ads_scripts)} times). Should be loaded exactly ONCE asynchronously in the <head> to save mobile bandwidth.")
    elif len(ads_scripts) == 1:
        issues.append(f"Google AdSense script is present ({ads_scripts[0]}).")

    # Check 2: Outdated jQuery CDN
    if "jquery/3.5.1/jquery.min.js" in text:
        issues.append("jQuery version 3.5.1 from 2020 is used. Modern jQuery is 3.7.1+. Also jQuery is render-blocking if loaded without defer.")

    # Check 3: Mixed Fonts
    if "Raleway" in text and "SolaimanLipi" in text:
        issues.append("Font Conflict: Raleway @font-face rules take significant CSS weight while SolaimanLipi is declared with !important globally. Unused Raleway weights can be pruned.")

    # Check 4: Table responsiveness in .post-body
    if ".post-body table" in text:
        issues.append(".post-body table rules found. Needs overflow-x: auto wrapper for small mobile screens (<480px).")

    # Check 5: In-body images max-width
    if ".post-body img" in text:
        issues.append(".post-body img is styled. Verify width: 100% and height: auto to avoid layout shifts.")

    # Check 6: Dark Mode CSS
    if "body.dark" in text:
        issues.append("Native Dark Mode is supported via 'body.dark' class and CSS custom properties (variables).")

    for i, issue in enumerate(issues, 1):
        print(f"  {i}. {issue}")

if __name__ == '__main__':
    deep_theme_audit()
