#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/post_builders/pdf_download_component.py
------------------------------------------------
Official HelpTrickBD Pill Button Standards (v1.4.9):
1. Official PDF Download Pill Button (.pdf-download-btn) - Container-Free
2. Official Source Link / Navigation Pill Button (.source-link-btn)

Features:
- ZERO OUTER CONTAINER: No box, no borders around the section.
- Heading and paragraph sit naturally on the article canvas.
- Self-contained scoped CSS so it renders immediately and perfectly even before theme upload.
- 100% Dual-Mode (Light & Dark Mode) Compatible.
- Centered on page with responsive wrapping.
- Zero nested <div> tags inside <a> to prevent wpautop splitting.
- File size text removed from PDF button per editorial standard.
- Supports both 1-Click Direct Download and 30s Countdown Timer.
"""

import html

BUTTON_CSS_SCOPED = """<style>
.pdf-download-wrap { display: flex; justify-content: center; align-items: center; width: 100%; margin: 20px auto; }
.pdf-download-btn { display: flex; align-items: center; gap: 10px; width: 100%; max-width: 470px; min-height: 60px; padding: 7px 10px; box-sizing: border-box; background: #ffffff; border: 1px solid #e0e5ef; border-radius: 14px; box-shadow: 0 3px 8px rgba(30,50,90,0.14); text-decoration: none !important; transition: all .25s ease; cursor: pointer; }
.pdf-download-btn:hover { transform: translateY(-2px); box-shadow: 0 5px 12px rgba(30,50,90,0.20); background: #ffffff; text-decoration: none !important; }
.pdf-file-icon { width: 38px; height: 42px; flex-shrink: 0; display: block; }
.pdf-divider { width: 2px; height: 38px; background: #cbd3e2; flex-shrink: 0; }
.pdf-info { flex: 1; min-width: 0; text-align: left; }
.pdf-title { display: block; color: #17233d !important; font-size: 16px; font-weight: 700; line-height: 1.4; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; text-decoration: none !important; }
.pdf-download-action { display: flex; align-items: center; justify-content: center; gap: 7px; background: linear-gradient(135deg, #f02d35, #cf101c); color: #ffffff !important; padding: 10px 14px; border-radius: 8px; font-size: 13px; font-weight: 700; white-space: nowrap; box-shadow: 0 2px 4px rgba(210,20,30,0.20); flex-shrink: 0; text-decoration: none !important; }
.pdf-download-btn:hover .pdf-download-action { background: linear-gradient(135deg, #e01b23, #b80914); color: #ffffff !important; }
.pdf-download-action svg { width: 19px; height: 19px; flex-shrink: 0; }
.pdf-download-btn.is-counting .pdf-download-action { background: linear-gradient(135deg, #f59e0b, #d97706) !important; color: #ffffff !important; }
.pdf-download-btn.is-ready .pdf-download-action { background: linear-gradient(135deg, #10b981, #059669) !important; color: #ffffff !important; }
[data-theme="dark"] .pdf-download-btn, .dark .pdf-download-btn { background: #1e293b !important; border-color: #334155 !important; box-shadow: 0 4px 14px rgba(0,0,0,0.35) !important; }
[data-theme="dark"] .pdf-download-btn:hover, .dark .pdf-download-btn:hover { background: #243147 !important; border-color: #475569 !important; }
[data-theme="dark"] .pdf-divider, .dark .pdf-divider { background: #334155 !important; }
[data-theme="dark"] .pdf-title, .dark .pdf-title { color: #f8fafc !important; }
[data-theme="dark"] .pdf-download-action, .dark .pdf-download-action { background: linear-gradient(135deg, #ef4444, #dc2626) !important; color: #ffffff !important; }
@media (max-width: 480px) {
  .pdf-download-btn { gap: 7px; padding: 6px 7px; min-height: 52px; }
  .pdf-file-icon { width: 32px; height: 36px; }
  .pdf-divider { height: 32px; }
  .pdf-title { font-size: 14px; }
  .pdf-download-action { padding: 8px 10px; font-size: 12px; gap: 5px; }
  .pdf-download-action svg { width: 16px; height: 16px; }
}
</style>"""

TIMER_SCRIPT = """<script>
if (typeof triggerPdfTimer !== 'function') {
  function triggerPdfTimer(btn, targetUrl, duration) {
    if (btn.classList.contains('is-ready')) {
      window.open(targetUrl, '_blank');
      return;
    }
    if (btn.classList.contains('is-counting')) return;
    btn.classList.add('is-counting');
    var titleEl = btn.querySelector('.pdf-title');
    var actionEl = btn.querySelector('.pdf-download-action');
    var sec = duration || 30;
    if (titleEl) titleEl.textContent = 'লিংক প্রস্তুত হচ্ছে...';
    if (actionEl) actionEl.innerHTML = '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg> <span>' + sec + 's</span>';
    var iv = setInterval(function() {
      sec--;
      if (sec > 0) {
        var sp = actionEl ? actionEl.querySelector('span') : null;
        if (sp) sp.textContent = sec + 's';
      } else {
        clearInterval(iv);
        btn.classList.remove('is-counting');
        btn.classList.add('is-ready');
        if (titleEl) titleEl.textContent = 'ফাইল প্রস্তুত! এখনই নিন';
        if (actionEl) actionEl.innerHTML = '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><path d="m7 10 5 5 5-5"/><path d="M12 15V3"/></svg> <span>Download</span>';
        btn.onclick = function(e) { e.preventDefault(); window.open(targetUrl, '_blank'); };
      }
    }, 1000);
  }
}
</script>"""

def render_pdf_download_button(
    pdf_url: str,
    title: str = "Download PDF",
    mode: str = "timer",
    timer_seconds: int = 30,
    unique_id: str = "pdf"
) -> str:
    """
    Renders the official HelpTrickBD PDF Download Pill Button (.pdf-download-btn).
    """
    clean_url = pdf_url.strip()
    clean_title = html.escape(title) if "<" not in title else title
    mode = mode.lower().strip()

    if mode == "direct":
        return f"""<div class="pdf-download-wrap">
  <a class="pdf-download-btn" href="{clean_url}" target="_blank" rel="noopener noreferrer" download>
    <svg class="pdf-file-icon" viewBox="0 0 40 44" fill="none">
      <path d="M7 2H25L36 13V41H7V2Z" fill="#fff" stroke="#ef3038" stroke-width="2"/>
      <path d="M25 2V13H36" stroke="#ef3038" stroke-width="2"/>
      <rect x="2" y="20" width="35" height="16" rx="3" fill="#ef3038"/>
      <text x="19.5" y="32" text-anchor="middle" fill="white" font-size="11" font-weight="bold">PDF</text>
    </svg>
    <span class="pdf-divider"></span>
    <span class="pdf-info">
      <span class="pdf-title">{clean_title}</span>
    </span>
    <span class="pdf-download-action">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
        <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/>
        <path d="m7 10 5 5 5-5"/>
        <path d="M12 15V3"/>
      </svg>
      Download
    </span>
  </a>
</div>"""
    else:
        return f"""<div class="pdf-download-wrap">
  <a class="pdf-download-btn" href="{clean_url}" onclick="triggerPdfTimer(this, '{clean_url}', {timer_seconds}); return false;" target="_blank" rel="noopener noreferrer">
    <svg class="pdf-file-icon" viewBox="0 0 40 44" fill="none">
      <path d="M7 2H25L36 13V41H7V2Z" fill="#fff" stroke="#ef3038" stroke-width="2"/>
      <path d="M25 2V13H36" stroke="#ef3038" stroke-width="2"/>
      <rect x="2" y="20" width="35" height="16" rx="3" fill="#ef3038"/>
      <text x="19.5" y="32" text-anchor="middle" fill="white" font-size="11" font-weight="bold">PDF</text>
    </svg>
    <span class="pdf-divider"></span>
    <span class="pdf-info">
      <span class="pdf-title">{clean_title}</span>
    </span>
    <span class="pdf-download-action">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
        <circle cx="12" cy="12" r="10"/>
        <polyline points="12 6 12 12 16 14"/>
      </svg>
      Get Link ({timer_seconds}s)
    </span>
  </a>
</div>"""

def render_source_link_button(
    link_url: str,
    title: str = "Source Link",
    subtitle: str = "Visit the official source"
) -> str:
    """
    Renders the official HelpTrickBD Source Link / Navigation Pill Button (.source-link-btn).
    """
    clean_url = link_url.strip()
    clean_title = html.escape(title) if "<" not in title else title
    clean_sub = html.escape(subtitle) if "<" not in subtitle else subtitle

    return f"""<div class="source-link-wrap">
  <a class="source-link-btn" href="{clean_url}" target="_blank" rel="noopener noreferrer">
    <svg class="source-link-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round">
      <path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/>
      <path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/>
    </svg>
    <span class="source-link-divider"></span>
    <span class="source-link-content">
      <span class="source-link-title">{clean_title}</span>
      <span class="source-link-desc">{clean_sub}</span>
    </span>
    <span class="source-link-arrow">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
        <path d="M14 3h7v7"/>
        <path d="M10 14 21 3"/>
        <path d="M21 14v6a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1h6"/>
      </svg>
    </span>
  </a>
</div>"""

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
    Renders the clean, container-free PDF download section:
    - Pure H2 Heading (NO outer card or border)
    - Editorial explanatory paragraph
    - Centered official PDF pill button (.pdf-download-btn)
    - Embedded scoped CSS so it renders immediately and perfectly even before theme upload
    - Inline countdown timer script for 100% instant functionality
    """
    clean_heading = html.escape(heading_title) if "<" not in heading_title else heading_title

    if not description_text:
        description_text = (
            f"পরীক্ষার চূড়ান্ত প্রস্তুতি ও অফলাইন অনুশীলনের জন্য "
            f"<strong>{clean_heading}</strong>-এর প্রামাণ্য ই-বুকটি সংগ্রহ করতে নিচের বাটনটি ব্যবহার করুন:"
        )

    button_markup = render_pdf_download_button(
        pdf_url=pdf_url,
        title="Download PDF",
        mode=mode,
        timer_seconds=30,
        unique_id=unique_id
    )

    section_html = f"""{BUTTON_CSS_SCOPED}
{TIMER_SCRIPT}
<div style="margin: 40px 0 30px 0; padding-top: 10px;">
  <h2 id="pdf-download" style="color: #0f172a; font-size: 22px; font-weight: 700; margin: 0 0 12px 0; line-height: 1.4;">
    অফিসিয়াল PDF ডাউনলোড: {clean_heading}
  </h2>
  <p style="color: #475569; font-size: 15.5px; line-height: 1.8; margin: 0 0 16px 0;">
    {description_text}
  </p>

  {button_markup}

  <p style="text-align: center; font-size: 12.5px; color: #64748b; margin: 8px 0 0 0; opacity: 0.85;">
    নিরাপদ ক্লাউড সার্ভার • সম্পূর্ণ বিজ্ঞাপন-মুক্ত ডাউনলোড
  </p>
</div>"""

    return section_html
