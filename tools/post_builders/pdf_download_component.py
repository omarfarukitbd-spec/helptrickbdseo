#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/post_builders/pdf_download_component.py
------------------------------------------------
Ultra-Compact, Bulletproof PDF Download Component for HelpTrickBD.

Fixes & Enhancements:
1. Text Minimized: Ultra-concise single-line button text ("Download PDF (৩০s টাইমার)").
2. Zero wpautop Breakage: Built with <button type="button"> containing only <span> and <svg> (no block <div>).
3. 100% Dual-Mode (Light & Dark Mode) Compatible via CSS variables and [data-theme="dark"].
4. Pre-Flight Clean: 0 emojis (no unicode checkmarks), no dead javascript:void links.
"""

import html

def render_pdf_download_section(
    pdf_url: str,
    heading_title: str,
    file_spec: str = "A4 প্রিন্ট কপি • ২.৪২ MB • সম্পূর্ণ সমাধান",
    description_text: str = "",
    mode: str = "timer",
    unique_id: str = "pdf2026",
    include_script: bool = True
) -> str:
    """
    Renders the compact, dual-mode compatible PDF Download Section.
    """
    mode = mode.lower().strip()
    if mode not in ["timer", "direct", "dual"]:
        mode = "timer"

    clean_pdf_url = pdf_url.strip()
    clean_heading = html.escape(heading_title) if "<" not in heading_title else heading_title
    clean_specs = html.escape(file_spec) if "<" not in file_spec else file_spec

    if not description_text:
        description_text = (
            f"পরীক্ষার চূড়ান্ত প্রস্তুতি ও অফলাইন অনুশীলনের জন্য "
            f"<strong>{clean_heading}</strong>-এর নির্ভুল সমাধান সমৃদ্ধ ই-বুকটি নিচে দেওয়া বাটন ব্যবহার করে সংগ্রহ করুন:"
        )

    # -------------------------------------------------------------
    # 1. Instant Direct Download Button (Mode: 'direct')
    # -------------------------------------------------------------
    btn_direct_html = f"""<a href="{clean_pdf_url}" target="_blank" rel="noopener noreferrer" download class="htbd-pdf-btn htbd-pdf-btn-direct" style="display: inline-flex; align-items: center; justify-content: center; gap: 8px; background: #059669; color: #ffffff !important; font-size: 15px; font-weight: 700; padding: 10px 22px; border-radius: 9px; text-decoration: none !important; border: none; cursor: pointer; box-shadow: 0 3px 10px rgba(5, 150, 105, 0.28); transition: all 0.2s ease;"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink:0;"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg><span>Download PDF (২.৪২ MB)</span></a>"""

    # -------------------------------------------------------------
    # 2. Compact Countdown Timer Button (Mode: 'timer')
    # -------------------------------------------------------------
    btn_timer_html = f"""<button type="button" id="htbd-timer-btn-{unique_id}" onclick="startCompactCountdown('{unique_id}', '{clean_pdf_url}')" class="htbd-pdf-btn htbd-pdf-btn-timer" style="display: inline-flex; align-items: center; justify-content: center; gap: 8px; background: #2563eb; color: #ffffff !important; font-size: 15px; font-weight: 700; padding: 10px 22px; border-radius: 9px; border: none; cursor: pointer; box-shadow: 0 3px 12px rgba(37, 99, 235, 0.28); transition: all 0.2s ease; outline: none;"><svg id="htbd-icon-clock-{unique_id}" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink:0;"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg><svg id="htbd-icon-check-{unique_id}" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" style="display: none; flex-shrink:0;"><polyline points="20 6 9 17 4 12"/></svg><span id="htbd-btn-text-{unique_id}">Download PDF (৩০s টাইমার)</span></button>"""

    if mode == "direct":
        buttons_markup = btn_direct_html
    elif mode == "timer":
        buttons_markup = btn_timer_html
    else:  # 'dual'
        buttons_markup = f"""<div style="display: flex; flex-wrap: wrap; gap: 12px; align-items: center;">{btn_direct_html} {btn_timer_html}</div>"""

    # -------------------------------------------------------------
    # 3. Compact Vanilla JavaScript Timer Engine
    # -------------------------------------------------------------
    script_markup = ""
    if include_script and mode in ["timer", "dual"]:
        script_markup = f"""
<script>
if (typeof startCompactCountdown !== 'function') {{
  function startCompactCountdown(uniqueId, downloadUrl) {{
    var btn = document.getElementById('htbd-timer-btn-' + uniqueId);
    var text = document.getElementById('htbd-btn-text-' + uniqueId);
    var iconClock = document.getElementById('htbd-icon-clock-' + uniqueId);
    var iconCheck = document.getElementById('htbd-icon-check-' + uniqueId);

    if (!btn || btn.getAttribute('data-running') === 'true') {{
      if (btn && btn.getAttribute('data-completed') === 'true') {{
        window.open(downloadUrl, '_blank');
      }}
      return;
    }}

    btn.setAttribute('data-running', 'true');
    btn.style.background = '#1e3a8a';
    btn.style.cursor = 'wait';

    var totalDuration = 30;
    var remaining = totalDuration;
    text.innerText = 'অপেক্ষা করুন (' + remaining + 's)...';

    var interval = setInterval(function() {{
      remaining--;
      if (remaining > 0) {{
        text.innerText = 'অপেক্ষা করুন (' + remaining + 's)...';
      }} else {{
        clearInterval(interval);
        btn.setAttribute('data-running', 'false');
        btn.setAttribute('data-completed', 'true');
        btn.style.background = '#059669';
        btn.style.cursor = 'pointer';
        btn.style.boxShadow = '0 4px 14px rgba(5, 150, 105, 0.35)';

        if (iconClock) iconClock.style.display = 'none';
        if (iconCheck) iconCheck.style.display = 'inline-block';
        text.innerText = 'Download PDF Now (ক্লিক করুন)';

        btn.onclick = function() {{
          window.open(downloadUrl, '_blank');
        }};

        window.open(downloadUrl, '_blank');
      }}
    }}, 1000);
  }}
}}
</script>"""

    # -------------------------------------------------------------
    # 4. Scoped Styles for Light & Dark Mode
    # -------------------------------------------------------------
    style_markup = """<style>
.htbd-pdf-section { background: #ffffff; border: 1.5px solid #e2e8f0; border-top: 4px solid #dc2626; border-radius: 12px; padding: 20px 24px; margin: 30px 0 25px 0; box-shadow: 0 4px 15px rgba(0,0,0,0.04); color: #334155; box-sizing: border-box; }
.htbd-pdf-title { color: #0f172a; font-size: 19px; font-weight: 700; margin: 0; line-height: 1.35; border: none; padding: 0; }
.htbd-pdf-desc { color: #475569; font-size: 14.5px; line-height: 1.75; margin: 10px 0 16px 0; }
.htbd-pdf-btn:hover, .htbd-pdf-btn:focus { color: #ffffff !important; text-decoration: none !important; transform: translateY(-1px); filter: brightness(1.08); }
.htbd-year-link-btn { display: inline-flex !important; align-items: center !important; gap: 8px !important; background: #0284c7 !important; color: #ffffff !important; font-size: 14px !important; font-weight: 700 !important; padding: 8px 18px !important; border-radius: 8px !important; text-decoration: none !important; box-shadow: 0 2px 8px rgba(2, 132, 199, 0.22) !important; transition: all 0.2s ease !important; margin-top: 10px !important; }
.htbd-year-link-btn:hover, .htbd-year-link-btn:focus { background: #0369a1 !important; color: #ffffff !important; text-decoration: none !important; transform: translateY(-1px) !important; box-shadow: 0 4px 12px rgba(2, 132, 199, 0.35) !important; }
[data-theme="dark"] .htbd-pdf-section { background: #1e293b !important; border-color: #334155 !important; border-top-color: #ef4444 !important; color: #cbd5e1 !important; box-shadow: 0 4px 20px rgba(0,0,0,0.3) !important; }
[data-theme="dark"] .htbd-pdf-title { color: #f8fafc !important; }
[data-theme="dark"] .htbd-pdf-desc { color: #94a3b8 !important; }
[data-theme="dark"] .htbd-year-link-btn { background: #0284c7 !important; color: #ffffff !important; }
[data-theme="dark"] .htbd-year-link-btn:hover { background: #0369a1 !important; color: #ffffff !important; }
</style>"""

    section_html = f"""{style_markup}
<div class="htbd-pdf-section" style="box-sizing: border-box; font-family: 'SolaimanLipi', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
  <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 8px;">
    <span style="display: inline-flex; align-items: center; justify-content: center; width: 38px; height: 38px; background: rgba(220, 38, 38, 0.12); border-radius: 8px; color: #dc2626; flex-shrink: 0;">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#dc2626" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
        <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
        <polyline points="14 2 14 8 20 8"/>
        <line x1="16" y1="13" x2="8" y2="13"/>
        <line x1="16" y1="17" x2="8" y2="17"/>
      </svg>
    </span>
    <div>
      <h2 id="pdf-download" class="htbd-pdf-title">
        অফিসিয়াল PDF ডাউনলোড: {clean_heading}
      </h2>
      <div style="font-size: 12px; opacity: 0.8; margin-top: 2px;">
        {clean_specs}
      </div>
    </div>
  </div>

  <p class="htbd-pdf-desc">
    {description_text}
  </p>

  <div style="display: flex; flex-wrap: wrap; gap: 12px; align-items: center;">
    {buttons_markup}
  </div>

  <div style="font-size: 11.5px; opacity: 0.75; margin-top: 10px;">
    [নিরাপদ ক্লাউড লিংক] সম্পূর্ণ বিজ্ঞাপন-মুক্ত ডাউনলোড সুবিধা
  </div>
</div>{script_markup}"""

    return section_html


if __name__ == "__main__":
    test_url = "https://www.helptrickbd.com/sample.pdf"
    test_title = "উন্নত হিসাববিজ্ঞান ১ প্রশ্নব্যাংক ২০১৯-২০২৪"
    
    res = render_pdf_download_section(test_url, test_title, mode="timer", unique_id="t_test")
    assert "Download PDF (৩০s টাইমার)" in res
    assert "startCompactCountdown" in res
    assert "[data-theme=\"dark\"]" in res
    assert "javascript:void" not in res
    assert "✓" not in res
    print("✅ Pre-flight compliant Compact PDF Component verified successfully!")
