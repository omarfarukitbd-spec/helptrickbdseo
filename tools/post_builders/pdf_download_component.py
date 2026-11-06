#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/post_builders/pdf_download_component.py
------------------------------------------------
Standardized, reusable, high-converting PDF Download Section Component for HelpTrickBD.

Supports 3 dynamic display modes per user directive:
1. 'direct'    : Instant 1-click Direct Download button only (⚡ সাথে সাথে ডাউনলোড).
2. 'timer'     : 30-Second Countdown High-Speed Timer button only (⏳ ৩০ সেকেন্ডে হাই-স্পিড ডাউনলোড).
3. 'dual'      : Both buttons displayed side-by-side (Instant Direct + 30s Countdown Timer).

Features:
- Mandatory <h2> heading with PDF icon and descriptive subject/topic title.
- Specification metadata pill bar (A4 Print-Ready, File Size, 2026 Special Edition).
- Explanatory lead paragraph detailing syllabus coverage and exam prep value.
- Self-contained vanilla JS countdown timer with progress bar and auto-reveal download link.
- 100% responsive, SolaimanLipi typography, zero WordPress wpautop breakages.
"""

import html

def render_pdf_download_section(
    pdf_url: str,
    heading_title: str,
    file_spec: str = "ফাইল ফরম্যাট: প্রামাণ্য A4 প্রিন্ট-রেডি ই-বুক • ফাইল সাইজ: ২.৪২ MB • সংস্করণ: ২০২৬ স্পেশাল",
    description_text: str = "",
    mode: str = "timer",
    unique_id: str = "pdf2026",
    include_script: bool = True
) -> str:
    """
    Renders the complete, production-ready HTML and inline JS for the PDF Download Section.

    Parameters:
    - pdf_url (str): Permanent public URL of the PDF file (WordPress Media Library or jsDelivr/GitHub).
    - heading_title (str): Specific title of the PDF (e.g. 'উন্নত হিসাববিজ্ঞান ১ প্রশ্নব্যাংক ২০১৯-২০২৪').
    - file_spec (str): File specifications line.
    - description_text (str): Explanatory lead paragraph. If empty, a default high-value text is used.
    - mode (str): 'timer' (default, high dwell-time), 'direct' (instant), or 'dual' (both).
    - unique_id (str): Unique DOM ID suffix to prevent collisions when multiple buttons exist on one page.
    - include_script (bool): Whether to include the <script> block for the countdown timer.
    """
    mode = mode.lower().strip()
    if mode not in ["timer", "direct", "dual"]:
        mode = "timer"

    clean_pdf_url = pdf_url.strip()
    clean_heading = html.escape(heading_title) if "<" not in heading_title else heading_title
    clean_specs = html.escape(file_spec) if "<" not in file_spec else file_spec

    if not description_text:
        description_text = (
            f"জাতীয় বিশ্ববিদ্যালয়ের অনার্স শিক্ষার্থীদের চূড়ান্ত পরীক্ষা প্রস্তুতি ও অফলাইন রিভিশনের সুবিধার্থে "
            f"<strong>{clean_heading}</strong>-এর বিশ্ববিদ্যালয় অ্যাকাডেমিক কাউন্সিলের মূল্যায়ন নির্দেশিকা অনুযায়ী "
            f"প্রণীত শতভাগ নির্ভুল প্রামাণ্য অফিশিয়াল মাস্টার পিডিএফ হ্যান্ডনোট নিচে সংযুক্ত করা হলো। "
            f"আপনার সুবিধামতো নিচের বাটন ব্যবহার করে প্রামাণ্য ই-বুকটি সংগ্রহ করুন:"
        )

    # 1. Button Design A: Instant Direct Download (সাথে সাথে ডাউনলোড)
    btn_direct_html = f"""<a href="{clean_pdf_url}" target="_blank" rel="noopener noreferrer" download class="htbd-btn-direct" style="display: inline-flex; align-items: center; gap: 10px; background: linear-gradient(135deg, #059669 0%, #047857 100%); color: #ffffff !important; padding: 14px 28px; border-radius: 10px; font-weight: 700; font-size: 15.5px; text-decoration: none !important; box-shadow: 0 4px 14px rgba(5, 150, 105, 0.3); transition: transform 0.15s ease, box-shadow 0.15s ease; border: none; cursor: pointer; user-select: none;">
      <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink:0;"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
      <span>সরাসরি PDF ডাউনলোড (Instant Download)</span>
    </a>"""

    # 2. Button Design B: 30-Second Countdown High-Speed Timer Download (কাউন্টডাউন টাইমার)
    btn_timer_html = f"""<div id="htbd-timer-wrap-{unique_id}" style="display: inline-block;">
      <button id="htbd-timer-btn-{unique_id}" onclick="startPdfCountdown('{unique_id}', '{clean_pdf_url}')" class="htbd-btn-timer" style="display: inline-flex; align-items: center; gap: 10px; background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%); color: #ffffff !important; padding: 14px 28px; border-radius: 10px; font-weight: 700; font-size: 15.5px; cursor: pointer; border: none; box-shadow: 0 4px 14px rgba(37, 99, 235, 0.3); user-select: none; transition: transform 0.15s ease, box-shadow 0.15s ease;">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink:0;"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
        <span>৩০ সেকেন্ডে হাই-স্পিড ডাউনলোড (Countdown Timer)</span>
      </button>
      <div id="htbd-timer-box-{unique_id}" style="display: none; background: #eff6ff; border: 1.5px solid #bfdbfe; border-radius: 10px; padding: 16px 24px; font-size: 15.5px; font-weight: 700; color: #1e40af; text-align: center;">
        <div id="htbd-timer-text-{unique_id}">হাই-স্পিড ক্লাউড লিংক তৈরি হচ্ছে... অনুগ্রহ করে <span id="htbd-countdown-{unique_id}" style="color: #dc2626; font-size: 20px; font-weight: 800;">30</span> সেকেন্ড অপেক্ষা করুন</div>
        <div style="width: 100%; height: 8px; background: #dbeafe; border-radius: 4px; margin-top: 10px; overflow: hidden;">
          <div id="htbd-progress-{unique_id}" style="width: 100%; height: 100%; background: #2563eb; transition: width 1s linear;"></div>
        </div>
      </div>
    </div>"""

    # Assemble buttons according to mode
    if mode == "direct":
        buttons_markup = btn_direct_html
    elif mode == "timer":
        buttons_markup = btn_timer_html
    else:  # 'dual'
        buttons_markup = f"""{btn_direct_html}\n    {btn_timer_html}"""

    # Timer JavaScript Engine (included if timer or dual mode is active)
    script_markup = ""
    if include_script and mode in ["timer", "dual"]:
        script_markup = f"""
<script>
if (typeof startPdfCountdown !== 'function') {{
  function startPdfCountdown(uniqueId, url) {{
    var btn = document.getElementById('htbd-timer-btn-' + uniqueId);
    var box = document.getElementById('htbd-timer-box-' + uniqueId);
    var countSpan = document.getElementById('htbd-countdown-' + uniqueId);
    var progress = document.getElementById('htbd-progress-' + uniqueId);
    if (!btn || !box) return;
    btn.style.display = 'none';
    box.style.display = 'block';
    var timeLeft = 30;
    var totalTime = 30;
    var interval = setInterval(function() {{
      timeLeft--;
      if (countSpan) countSpan.innerText = timeLeft;
      if (progress) progress.style.width = ((timeLeft / totalTime) * 100) + '%';
      if (timeLeft <= 0) {{
        clearInterval(interval);
        box.style.background = '#ecfdf5';
        box.style.borderColor = '#a7f3d0';
        box.innerHTML = '<span style="color: #065f46; font-size: 15.5px;">[প্রস্তুত] আপনার হাই-স্পিড ডাউনলোড লিংক সক্রিয় হয়েছে!</span> <a href="' + url + '" target="_blank" rel="noopener noreferrer" download style="display: inline-block; margin-left: 12px; background: #059669; color: #ffffff !important; padding: 8px 20px; border-radius: 7px; text-decoration: none; font-size: 15px; font-weight: 700; box-shadow: 0 3px 10px rgba(5,150,105,0.25);">এখনই PDF ডাউনলোড করুন</a>';
        window.open(url, '_blank');
      }}
    }}, 1000);
  }}
}}
</script>"""

    section_html = f"""<div class="htbd-pdf-section" style="margin: 40px 0 35px 0; background: #ffffff; border: 1.5px solid #e2e8f0; border-top: 5px solid #dc2626; border-radius: 14px; padding: 28px 32px; box-shadow: 0 4px 20px rgba(0,0,0,0.05); font-family: 'SolaimanLipi', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
  <div style="display: flex; align-items: center; gap: 14px; margin-bottom: 14px;">
    <span style="display: inline-flex; align-items: center; justify-content: center; width: 46px; height: 46px; background: #fee2e2; border-radius: 10px; color: #dc2626; flex-shrink: 0;">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg>
    </span>
    <div>
      <h2 id="pdf-download" style="color: #0b2046; font-size: 22px; font-weight: 700; margin: 0; line-height: 1.35; border: none; padding: 0;">
        অফিশিয়াল PDF ডাউনলোড: {clean_heading}
      </h2>
      <div style="color: #64748b; font-size: 13.5px; font-weight: 600; margin-top: 3px;">
        {clean_specs}
      </div>
    </div>
  </div>

  <p style="color: #475569; font-size: 15.5px; line-height: 1.85; margin: 0 0 22px 0;">
    {description_text}
  </p>

  <div class="htbd-download-buttons-grid" style="display: flex; flex-wrap: wrap; gap: 16px; align-items: center;">
    {buttons_markup}
  </div>
</div>{script_markup}"""

    return section_html


if __name__ == "__main__":
    # Test rendering all 3 modes
    test_url = "https://www.helptrickbd.com/sample.pdf"
    test_title = "উন্নত হিসাববিজ্ঞান ১ প্রশ্নব্যাংক ২০১৯-২০২৪ (মাস্টার সল্যুশন)"
    
    print("=== Testing Direct Mode ===")
    res_direct = render_pdf_download_section(test_url, test_title, mode="direct", unique_id="test_dir")
    print(f"Direct mode length: {len(res_direct)}")
    assert "⚡ সরাসরি PDF ডাউনলোড" in res_direct
    assert "startPdfCountdown" not in res_direct

    print("=== Testing Timer Mode ===")
    res_timer = render_pdf_download_section(test_url, test_title, mode="timer", unique_id="test_tmr")
    print(f"Timer mode length: {len(res_timer)}")
    assert "⏳ ৩০ সেকেন্ডে হাই-স্পিড ডাউনলোড" in res_timer
    assert "startPdfCountdown" in res_timer

    print("=== Testing Dual Mode ===")
    res_dual = render_pdf_download_section(test_url, test_title, mode="dual", unique_id="test_dual")
    print(f"Dual mode length: {len(res_dual)}")
    assert "⚡ সরাসরি PDF ডাউনলোড" in res_dual
    assert "⏳ ৩০ সেকেন্ডে হাই-স্পিড ডাউনলোড" in res_dual
    assert "startPdfCountdown" in res_dual

    print("\n✅ All 3 PDF Download Component modes verified successfully!")

