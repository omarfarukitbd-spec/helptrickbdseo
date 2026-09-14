#!/usr/bin/env python3
"""
HelpTrickBD Google SERP Snippet Preview & CTR Optimizer
Simulates how your articles look on Google Search (Desktop & Mobile)
to avoid snippet truncation and maximize organic click-through rate (CTR).

Usage:
    python serp_preview.py --url https://www.helptrickbd.com/2026/01/sarbobhoumotto-ki-songga-boishisto-o-prokarved.html
    python serp_preview.py --title "Custom Title" --desc "Custom Description" --url "https://..."
"""

import argparse
import os
import sys

try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("[!] Missing requests/bs4. Run: pip install requests beautifulsoup4")
    sys.exit(1)

OUTPUT_HTML = "serp_preview.html"


def generate_html_preview(title, desc, url):
    desktop_title = title if len(title) <= 60 else title[:57] + "..."
    desktop_desc = desc if len(desc) <= 160 else desc[:157] + "..."
    mobile_title = title if len(title) <= 55 else title[:52] + "..."
    mobile_desc = desc if len(desc) <= 130 else desc[:127] + "..."

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>HelpTrickBD - Google SERP Snippet Preview</title>
  <style>
    body {{
      font-family: Arial, sans-serif;
      background-color: #f8f9fa;
      padding: 30px;
      color: #202124;
    }}
    .container {{
      max-width: 800px;
      margin: 0 auto;
      background: #fff;
      padding: 30px;
      border-radius: 10px;
      box-shadow: 0 4px 12px rgba(0,0,0,0.06);
    }}
    h1 {{ font-size: 24px; color: #1a0dab; margin-bottom: 20px; }}
    .snippet-box {{
      border: 1px solid #dfe1e5;
      padding: 20px;
      border-radius: 8px;
      margin-bottom: 30px;
      background: #fff;
    }}
    .badge {{
      display: inline-block;
      padding: 4px 10px;
      border-radius: 4px;
      font-size: 12px;
      font-weight: bold;
      margin-bottom: 12px;
      background: #e8f0fe;
      color: #1967d2;
    }}
    .google-url {{
      font-size: 14px;
      color: #202124;
      line-height: 1.3;
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .google-title {{
      font-size: 20px;
      color: #1a0dab;
      text-decoration: none;
      margin: 6px 0 4px 0;
      display: block;
      font-weight: 400;
      line-height: 1.3;
    }}
    .google-title:hover {{ text-decoration: underline; }}
    .google-desc {{
      font-size: 14px;
      color: #4d5156;
      line-height: 1.58;
    }}
    .metrics {{
      margin-top: 15px;
      font-size: 13px;
      color: #5f6368;
      border-top: 1px dashed #eee;
      padding-top: 10px;
    }}
  </style>
</head>
<body>
  <div class="container">
    <h1>Google Search Snippet Preview</h1>
    <p>Target URL: <a href="{url}" target="_blank">{url}</a></p>

    <!-- Desktop Preview -->
    <div class="snippet-box">
      <span class="badge">🖥️ Desktop Search Preview</span>
      <div class="google-url">
        <img src="https://www.google.com/s2/favicons?domain=helptrickbd.com" width="16" height="16" alt="favicon">
        <span>https://www.helptrickbd.com &rsaquo; {url.split('/')[-1]}</span>
      </div>
      <a class="google-title" href="{url}">{desktop_title}</a>
      <div class="google-desc">{desktop_desc}</div>
      <div class="metrics">
        Title length: <strong>{len(title)} chars</strong> ({'✅ Optimal (under 60)' if len(title) <= 60 else '⚠️ Warning: May truncate in desktop'}) |
        Description length: <strong>{len(desc)} chars</strong> ({'✅ Optimal (under 160)' if len(desc) <= 160 else '⚠️ Warning: May truncate in desktop'})
      </div>
    </div>

    <!-- Mobile Preview -->
    <div class="snippet-box">
      <span class="badge">📱 Mobile Search Preview</span>
      <div class="google-url">
        <img src="https://www.google.com/s2/favicons?domain=helptrickbd.com" width="16" height="16" alt="favicon">
        <span>HelpTrickBD</span>
      </div>
      <a class="google-title" style="font-size: 18px;" href="{url}">{mobile_title}</a>
      <div class="google-desc" style="font-size: 13px;">{mobile_desc}</div>
      <div class="metrics">
        Title limit: <strong>55 chars</strong> | Description limit: <strong>130 chars</strong>
      </div>
    </div>
  </div>
</body>
</html>"""

    with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"\n[OK] SERP Preview generated successfully!")
    print(f"     View report at: {os.path.abspath(OUTPUT_HTML)}\n")


def main():
    parser = argparse.ArgumentParser(description="Google SERP Snippet Preview Tool for HelpTrickBD")
    parser.add_argument("--url", default="https://www.helptrickbd.com/2026/01/sarbobhoumotto-ki-songga-boishisto-o-prokarved.html", help="Post URL")
    parser.add_argument("--title", help="Custom Title override")
    parser.add_argument("--desc", help="Custom Meta Description override")

    args = parser.parse_args()

    title = args.title or ""
    desc = args.desc or ""

    if not title or not desc:
        try:
            res = requests.get(args.url, timeout=10)
            soup = BeautifulSoup(res.text, "html.parser")
            if not title and soup.find("title"):
                title = soup.find("title").get_text().strip()
            if not desc:
                meta_tag = soup.find("meta", attrs={"name": "description"})
                desc = meta_tag.get("content", "").strip() if meta_tag else ""
        except Exception as e:
            print(f"[!] Error fetching post data: {e}")

    generate_html_preview(title, desc, args.url)


if __name__ == "__main__":
    main()
