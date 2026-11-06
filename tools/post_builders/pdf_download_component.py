#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/post_builders/pdf_download_component.py
------------------------------------------------
Authoritative, production-grade PDF Download Section Component for HelpTrickBD.
Implements UI/UX Pattern 01: Interactive 3-State Live Countdown Button.

Features:
- State 1 (Idle): Royal Blue (#2563eb / --ht-primary) 2-line action button with clock icon.
- State 2 (Counting): Smooth animated progress fill layer (0% -> 100%) with live second countdown.
- State 3 (Ready): Instant morph to Emerald Green (#059669 / --ht-accent) with checkmark icon and active download link.
- Instant Download variant (mode='direct') with matching 2-line layout and download arrow icon.
- Dual Mode (mode='dual') with both Instant and Countdown options cleanly stacked.
- 100% Mobile Responsive (320px - 1200px), zero awkward line-wrapping, zero emojis (pre-flight compliant).
- SolaimanLipi typography, safe vanilla JavaScript without external dependencies.
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
    - pdf_url (str): Permanent public URL of the PDF file (e.g. Google Drive or WordPress Media Library).
    - heading_title (str): Specific title of the PDF (e.g. 'উন্নত হিসাববিজ্ঞান ১ প্রশ্নব্যাংক ২০১৯-২০২৪').
    - file_spec (str): File specifications line.
    - description_text (str): Explanatory lead paragraph.
    - mode (str): 'timer' (default 30s countdown), 'direct' (instant 1-click), or 'dual' (both).
    - unique_id (str): Unique DOM ID suffix to prevent collisions.
    - include_script (bool): Whether to include the vanilla JS engine.
    """
    mode = mode.lower().strip()
    if mode not in ["timer", "direct", "dual"]:
        mode = "timer"

    clean_pdf_url = pdf_url.strip()
    clean_heading = html.escape(heading_title) if "<" not in heading_title else heading_title
    clean_specs = html.escape(file_spec) if "<" not in file_spec else file_spec

    if not description_text:
        description_text = (
            f"জাতীয় বিশ্ববিদ্যালয়ের অনার্স ৩য় বর্ষের শিক্ষার্থীদের চূড়ান্ত পরীক্ষা প্রস্তুতি ও অফলাইন অনুশীলনের সুবিধার্থে "
            f"<strong>{clean_heading}</strong>-এর অ্যাকাডেমিক মানদণ্ড অনুযায়ী প্রণীত সম্পূর্ণ নির্ভুল সমাধান হ্যান্ডনোট "
            f"নিচে পিডিএফ আকারে যুক্ত করা হলো। আপনার সুবিধাজনক অপশন ব্যবহার করে প্রামাণ্য হ্যান্ডনোটটি এখনই সংগ্রহ করুন:"
        )

    # -------------------------------------------------------------
    # 1. Instant Direct Download Button (Mode: 'direct')
    # -------------------------------------------------------------
    btn_direct_html = f"""<a href="{clean_pdf_url}" target="_blank" rel="noopener noreferrer" download class="htbd-btn-direct" style="display: inline-flex; align-items: center; justify-content: space-between; gap: 12px; background: linear-gradient(135deg, #059669 0%, #047857 100%); color: #ffffff !important; padding: 12px 18px; border-radius: 12px; text-decoration: none !important; box-shadow: 0 4px 14px rgba(5, 150, 105, 0.28); transition: transform 0.15s ease, box-shadow 0.15s ease; border: 1px solid rgba(255, 255, 255, 0.2); width: 100%; max-width: 420px; box-sizing: border-box;">
      <div style="display: flex; align-items: center; gap: 12px;">
        <div style="width: 42px; height: 42px; border-radius: 10px; background: rgba(255, 255, 255, 0.2); backdrop-filter: blur(4px); display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round">
            <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/>
            <polyline points="7 10 12 15 17 10"/>
            <line x1="12" y1="15" x2="12" y2="3"/>
          </svg>
        </div>
        <div style="text-align: left;">
          <div style="font-size: 15.5px; font-weight: 700; color: #ffffff; line-height: 1.25;">সরাসরি PDF ডাউনলোড</div>
          <div style="font-size: 11px; color: #d1fae5; line-height: 1.2; margin-top: 2px;">তাত্ক্ষণিক গুগল ড্রাইভ লিংক • সম্পূর্ণ সমাধান</div>
        </div>
      </div>
      <div style="width: 28px; height: 28px; border-radius: 50%; background: rgba(255, 255, 255, 0.2); display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18l6-6-6-6"/></svg>
      </div>
    </a>"""

    # -------------------------------------------------------------
    # 2. Interactive 3-State Countdown Timer Button (Mode: 'timer')
    # -------------------------------------------------------------
    btn_timer_html = f"""<div id="htbd-timer-wrap-{unique_id}" style="width: 100%; max-width: 420px; box-sizing: border-box;">
      <button id="htbd-timer-btn-{unique_id}" onclick="startInteractiveCountdown('{unique_id}', '{clean_pdf_url}')" class="htbd-btn-timer-morph" style="position: relative; overflow: hidden; width: 100%; display: flex; align-items: center; justify-content: space-between; gap: 12px; background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%); color: #ffffff !important; padding: 12px 18px; border-radius: 12px; border: 1px solid rgba(255, 255, 255, 0.25); box-shadow: 0 4px 15px rgba(37, 99, 235, 0.3); cursor: pointer; user-select: none; transition: background 0.3s ease, box-shadow 0.3s ease; box-sizing: border-box;">
        
        <!-- Animated Progress Fill Layer -->
        <div id="htbd-progress-fill-{unique_id}" style="position: absolute; top: 0; left: 0; bottom: 0; width: 0%; background: rgba(30, 58, 138, 0.85); transition: width 0.1s linear; pointer-events: none; z-index: 1;"></div>
        
        <!-- Foreground Content Layer -->
        <div style="position: relative; z-index: 2; display: flex; align-items: center; gap: 12px;">
          <!-- Icon Box -->
          <div id="htbd-icon-box-{unique_id}" style="width: 42px; height: 42px; border-radius: 10px; background: rgba(255, 255, 255, 0.2); backdrop-filter: blur(4px); display: flex; align-items: center; justify-content: center; flex-shrink: 0; transition: transform 0.2s ease;">
            <!-- State 1 & 2 Clock Icon -->
            <svg id="htbd-icon-clock-{unique_id}" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round">
              <circle cx="12" cy="12" r="10"/>
              <polyline points="12 6 12 12 16 14"/>
            </svg>
            <!-- State 3 Check Icon (hidden initially) -->
            <svg id="htbd-icon-check-{unique_id}" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round" style="display: none;">
              <polyline points="20 6 9 17 4 12"/>
            </svg>
          </div>
          <!-- Text Hierarchy -->
          <div style="text-align: left;">
            <div id="htbd-btn-title-{unique_id}" style="font-size: 15.5px; font-weight: 700; color: #ffffff; line-height: 1.25;">কাউন্টডাউন শুরু করুন</div>
            <div id="htbd-btn-sub-{unique_id}" style="font-size: 11px; color: #dbeafe; line-height: 1.2; margin-top: 2px;">ক্লিক করলে ৩০ সেকেন্ডে লিংক তৈরি হবে</div>
          </div>
        </div>

        <!-- Right Badge Pill -->
        <div id="htbd-btn-badge-{unique_id}" style="position: relative; z-index: 2; padding: 4px 10px; border-radius: 6px; background: rgba(255, 255, 255, 0.22); font-size: 11.5px; font-weight: 700; color: #ffffff; flex-shrink: 0; white-space: nowrap;">
          ৩০ সে.
        </div>
      </button>

      <!-- Live Micro Status Notice -->
      <div id="htbd-status-notice-{unique_id}" style="font-size: 11.5px; color: #64748b; font-weight: 600; text-align: center; margin-top: 7px;">
        নিরাপদ ক্লাউড সার্ভার • সম্পূর্ণ বিজ্ঞাপন-মুক্ত ডাউনলোড
      </div>
    </div>"""

    # Assemble buttons according to mode
    if mode == "direct":
        buttons_markup = btn_direct_html
    elif mode == "timer":
        buttons_markup = btn_timer_html
    else:  # 'dual'
        buttons_markup = f"""<div style="display: flex; flex-direction: column; gap: 14px; width: 100%;">
      {btn_direct_html}
      {btn_timer_html}
    </div>"""

    # -------------------------------------------------------------
    # 3. Vanilla JavaScript 3-State Morphing Engine
    # -------------------------------------------------------------
    script_markup = ""
    if include_script and mode in ["timer", "dual"]:
        script_markup = f"""
<script>
if (typeof startInteractiveCountdown !== 'function') {{
  function startInteractiveCountdown(uniqueId, downloadUrl) {{
    var btn = document.getElementById('htbd-timer-btn-' + uniqueId);
    var progressFill = document.getElementById('htbd-progress-fill-' + uniqueId);
    var iconBox = document.getElementById('htbd-icon-box-' + uniqueId);
    var iconClock = document.getElementById('htbd-icon-clock-' + uniqueId);
    var iconCheck = document.getElementById('htbd-icon-check-' + uniqueId);
    var title = document.getElementById('htbd-btn-title-' + uniqueId);
    var subtitle = document.getElementById('htbd-btn-sub-' + uniqueId);
    var badge = document.getElementById('htbd-btn-badge-' + uniqueId);
    var notice = document.getElementById('htbd-status-notice-' + uniqueId);

    if (!btn || btn.getAttribute('data-running') === 'true') {{
      if (btn && btn.getAttribute('data-completed') === 'true') {{
        window.open(downloadUrl, '_blank');
      }}
      return;
    }}

    btn.setAttribute('data-running', 'true');
    btn.style.cursor = 'wait';

    // State 2: Counting in progress
    title.innerText = 'লিংক তৈরি হচ্ছে...';
    subtitle.innerText = 'অনুগ্রহ করে অপেক্ষা করুন';
    if (notice) notice.innerHTML = '<span style="color: #2563eb; font-weight: 700;">[প্রস্তুতি চলছে] হাই-স্পিড সার্ভার ফাইল প্রস্তুত করছে...</span>';

    var totalDuration = 30; // 30 seconds
    var remaining = totalDuration;
    var stepMs = 100;
    var totalSteps = (totalDuration * 1000) / stepMs;
    var currentStep = 0;

    var countdownInterval = setInterval(function() {{
      currentStep++;
      var percent = (currentStep / totalSteps) * 100;
      if (progressFill) progressFill.style.width = percent + '%';

      var secondsLeft = Math.ceil(totalDuration - (currentStep * stepMs / 1000));
      if (badge && secondsLeft >= 0) {{
        badge.innerText = secondsLeft + ' সে.';
      }}

      if (currentStep >= totalSteps) {{
        clearInterval(countdownInterval);

        // State 3: Ready / Success Morph
        btn.setAttribute('data-running', 'false');
        btn.setAttribute('data-completed', 'true');
        btn.style.cursor = 'pointer';
        btn.style.background = 'linear-gradient(135deg, #059669 0%, #047857 100%)';
        btn.style.boxShadow = '0 4px 18px rgba(5, 150, 105, 0.35)';

        if (progressFill) progressFill.style.width = '0%';
        if (iconClock) iconClock.style.display = 'none';
        if (iconCheck) iconCheck.style.display = 'block';

        title.innerText = 'ডাউনলোড লিংক প্রস্তুত!';
        subtitle.innerText = 'ক্লিক করলেই PDF ফাইল ওপেন হবে';

        if (badge) {{
          badge.innerText = 'ডাউনলোড';
          badge.style.background = '#ffffff';
          badge.style.color = '#047857';
          badge.style.boxShadow = '0 2px 6px rgba(0,0,0,0.15)';
        }}

        if (notice) {{
          notice.innerHTML = '<span style="color: #059669; font-weight: 700;">[সম্পন্ন] ডাউনলোড লিংক সক্রিয় হয়েছে! ক্লিকেই ফাইলটি সেভ হবে।</span>';
        }}

        // Direct click trigger
        btn.onclick = function() {{
          window.open(downloadUrl, '_blank');
        }};

        // Auto-open in new tab
        window.open(downloadUrl, '_blank');
      }}
    }}, stepMs);
  }}
}}
</script>"""

    # -------------------------------------------------------------
    # 4. Master Section HTML Container
    # -------------------------------------------------------------
    section_html = f"""<div class="htbd-pdf-section" style="margin: 40px 0 35px 0; background: #ffffff; border: 1.5px solid #e2e8f0; border-top: 5px solid #dc2626; border-radius: 14px; padding: 26px 28px; box-shadow: 0 4px 20px rgba(0,0,0,0.05); font-family: 'SolaimanLipi', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; box-sizing: border-box;">
  <div style="display: flex; align-items: center; gap: 14px; margin-bottom: 14px;">
    <span style="display: inline-flex; align-items: center; justify-content: center; width: 44px; height: 44px; background: #fee2e2; border-radius: 10px; color: #dc2626; flex-shrink: 0;">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#dc2626" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
        <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
        <polyline points="14 2 14 8 20 8"/>
        <line x1="16" y1="13" x2="8" y2="13"/>
        <line x1="16" y1="17" x2="8" y2="17"/>
        <polyline points="10 9 9 9 8 9"/>
      </svg>
    </span>
    <div>
      <h2 id="pdf-download" style="color: #0b2046; font-size: 21px; font-weight: 700; margin: 0; line-height: 1.35; border: none; padding: 0;">
        অফিসিয়াল PDF ডাউনলোড: {clean_heading}
      </h2>
      <div style="color: #64748b; font-size: 13px; font-weight: 600; margin-top: 3px;">
        {clean_specs}
      </div>
    </div>
  </div>

  <p style="color: #475569; font-size: 15.5px; line-height: 1.85; margin: 0 0 20px 0;">
    {description_text}
  </p>

  <div class="htbd-download-buttons-grid" style="display: flex; flex-wrap: wrap; gap: 14px; align-items: center;">
    {buttons_markup}
  </div>
</div>{script_markup}"""

    return section_html


if __name__ == "__main__":
    test_url = "https://www.helptrickbd.com/sample.pdf"
    test_title = "উন্নত হিসাববিজ্ঞান ১ প্রশ্নব্যাংক ২০১৯-২০২৪ (মাস্টার সল্যুশন)"
    
    print("=== Testing Pattern 01: Direct Mode ===")
    res_direct = render_pdf_download_section(test_url, test_title, mode="direct", unique_id="t_dir")
    assert "htbd-btn-direct" in res_direct
    assert "startInteractiveCountdown" not in res_direct

    print("=== Testing Pattern 01: Timer Mode (Default) ===")
    res_timer = render_pdf_download_section(test_url, test_title, mode="timer", unique_id="t_tmr")
    assert "htbd-btn-timer-morph" in res_timer
    assert "startInteractiveCountdown" in res_timer
    assert "htbd-progress-fill-t_tmr" in res_timer

    print("=== Testing Pattern 01: Dual Mode ===")
    res_dual = render_pdf_download_section(test_url, test_title, mode="dual", unique_id="t_dual")
    assert "htbd-btn-direct" in res_dual
    assert "htbd-btn-timer-morph" in res_dual

    print("\n✅ All Pattern 01 modes rendered and verified successfully!")
