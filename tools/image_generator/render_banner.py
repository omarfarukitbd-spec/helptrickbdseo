#!/usr/bin/env python3
"""
HelpTrickBD Chrome-Headless High Resolution 16:9 Banner Generator
Renders beautiful HTML5 + CSS cards with SolaimanLipi, gradients, badges,
and captures exact 1200x675 PNG/JPG thumbnails.
"""

import os
import subprocess
import time

CHROME_PATH = "C:/Program Files/Google/Chrome/Application/chrome.exe"
if not os.path.exists(CHROME_PATH):
    CHROME_PATH = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"

OUTPUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "assets", "images", "posts"))
os.makedirs(OUTPUT_DIR, exist_ok=True)
TEMP_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "temp_banners"))
os.makedirs(TEMP_DIR, exist_ok=True)


def generate_html_card(
    category_badge,
    title,
    subtitle,
    features,
    gradient_colors=("linear-gradient(135deg, #0d47a1 0%, #1565c0 50%, #00838f 100%)"),
    accent_color="#ffc107"
):
    feat_pills_html = "".join([f'<div class="feat-pill">{f}</div>' for f in features])
    
    return f"""<!DOCTYPE html>
<html lang="bn">
<head>
<meta charset="utf-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Bengali:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
  @font-face {{
    font-family: 'SolaimanLipi';
    font-display: swap;
    font-style: normal;
    font-weight: 400;
    src: url('https://fonts.maateen.me/solaiman-lipi/solaimanlipi-normal-v1.0.woff2') format('woff2');
  }}
  @font-face {{
    font-family: 'SolaimanLipi';
    font-display: swap;
    font-style: normal;
    font-weight: 700;
    src: url('https://fonts.maateen.me/solaiman-lipi/solaimanlipi-bold-v1.0.woff2') format('woff2');
  }}
  * {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    font-family: 'SolaimanLipi', 'Noto Sans Bengali', Arial, sans-serif !important;
  }}
  body {{
    width: 1200px;
    height: 675px;
    background: {gradient_colors};
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    position: relative;
  }}
  /* Subtle Background Accent Rings */
  .bg-circle-1 {{
    position: absolute;
    width: 600px;
    height: 600px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(255,255,255,0.08) 0%, rgba(255,255,255,0) 70%);
    top: -150px;
    right: -100px;
    pointer-events: none;
  }}
  .bg-circle-2 {{
    position: absolute;
    width: 500px;
    height: 500px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(255,193,7,0.08) 0%, rgba(255,193,7,0) 70%);
    bottom: -150px;
    left: -100px;
    pointer-events: none;
  }}
  .card {{
    width: 1080px;
    height: 545px;
    background: rgba(13, 27, 62, 0.45);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 2px solid rgba(255, 255, 255, 0.22);
    border-radius: 22px;
    padding: 48px 56px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    box-shadow: 0 25px 50px rgba(0, 0, 0, 0.35);
    z-index: 2;
  }}
  .top-bar {{
    display: flex;
    justify-content: space-between;
    align-items: center;
  }}
  .brand {{
    background: rgba(255, 255, 255, 0.14);
    border: 1px solid rgba(255, 255, 255, 0.25);
    padding: 8px 24px;
    border-radius: 30px;
    color: #ffffff;
    font-size: 20px;
    font-weight: 700;
    letter-spacing: 0.5px;
    display: flex;
    align-items: center;
    gap: 8px;
  }}
  .badge {{
    background: {accent_color};
    color: #0d1b3e;
    padding: 8px 26px;
    border-radius: 30px;
    font-size: 20px;
    font-weight: 700;
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
  }}
  .content-box {{
    margin: 10px 0;
  }}
  .title {{
    color: #ffffff;
    font-size: 48px;
    font-weight: 700;
    line-height: 1.35;
    text-shadow: 0 3px 12px rgba(0, 0, 0, 0.4);
  }}
  .subtitle {{
    color: #e0e7ff;
    font-size: 23px;
    margin-top: 14px;
    line-height: 1.5;
    text-shadow: 0 2px 6px rgba(0, 0, 0, 0.3);
  }}
  .features {{
    display: flex;
    gap: 16px;
    flex-wrap: wrap;
  }}
  .feat-pill {{
    background: rgba(255, 255, 255, 0.12);
    border: 1px solid rgba(255, 255, 255, 0.25);
    color: #ffffff;
    padding: 9px 20px;
    border-radius: 12px;
    font-size: 19px;
    font-weight: 500;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  }}
  .footer {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    color: rgba(255, 255, 255, 0.75);
    font-size: 17px;
    border-top: 1px solid rgba(255, 255, 255, 0.15);
    padding-top: 16px;
  }}
</style>
</head>
<body>
  <div class="bg-circle-1"></div>
  <div class="bg-circle-2"></div>
  <div class="card">
    <div class="top-bar">
      <div class="brand">🚀 HelpTrickBD • www.helptrickbd.com</div>
      <div class="badge">{category_badge}</div>
    </div>
    <div class="content-box">
      <h1 class="title">{title}</h1>
      <p class="subtitle">{subtitle}</p>
    </div>
    <div class="features">
      {feat_pills_html}
    </div>
    <div class="footer">
      <span>© HelpTrickBD Smart Education Platform</span>
      <span style="color: {accent_color}; font-weight: bold;">⭐ অনার্স ও বিসিএস পরীক্ষার পূর্ণাঙ্গ সহায়িকা</span>
    </div>
  </div>
</body>
</html>"""


def render_banner(
    filename,
    category_badge,
    title,
    subtitle,
    features,
    gradient_colors="linear-gradient(135deg, #0d47a1 0%, #1565c0 50%, #00838f 100%)",
    accent_color="#ffc107"
):
    html_code = generate_html_card(category_badge, title, subtitle, features, gradient_colors, accent_color)
    temp_html_path = os.path.join(TEMP_DIR, f"{filename}.html")
    with open(temp_html_path, "w", encoding="utf-8") as f:
        f.write(html_code)

    output_path = os.path.join(OUTPUT_DIR, filename)

    chrome_cmd = [
        CHROME_PATH,
        "--headless",
        "--disable-gpu",
        "--hide-scrollbars",
        "--window-size=1200,675",
        f"--screenshot={output_path}",
        temp_html_path
    ]

    subprocess.run(chrome_cmd, check=True)
    if os.path.exists(output_path):
        print(f"  [+] Banner successfully generated: {filename} ({os.path.getsize(output_path)} bytes)")
        return output_path
    else:
        raise RuntimeError(f"Failed to generate {filename}")


if __name__ == "__main__":
    out = render_banner(
        "test-chrome-banner.png",
        "🎓 রাষ্ট্রবিজ্ঞান স্পেশাল",
        "পিতৃতন্ত্র কাকে বলে? সংজ্ঞা, বৈশিষ্ট্য, প্রভাব ও নারীবাদী তত্ত্ব",
        "অনার্স ও মাস্টার্স সমাজবিজ্ঞান এবং রাষ্ট্রবিজ্ঞান বিষয়ের পূর্ণাঙ্গ স্পেশাল হ্যান্ডনোট",
        ["📌 ১. প্রামাণ্য সংজ্ঞা ও বৈশিষ্ট্য", "📊 তাত্ত্বিক কাঠামো ও প্রভাব", "📝 বিসিএস মডেল টেস্ট", "⚡ সংস্করণ ২০২৬"],
        gradient_colors="linear-gradient(135deg, #28103c 0%, #581c87 50%, #7e22ce 100%)",
        accent_color="#fbbf24"
    )
    print("Generated:", out)
