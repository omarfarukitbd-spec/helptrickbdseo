#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/post_builders/pdf_download_component.py
------------------------------------------------
Official HelpTrickBD Pill Button Standards (v1.4.9):
1. Official PDF Download Pill Button (.pdf-download-btn)
2. Official Source Link / Navigation Pill Button (.source-link-btn)

Features:
- 100% Dual-Mode (Light & Dark Mode) Compatible.
- Centered on page with responsive wrapping.
- Zero nested <div> tags inside <a> to prevent wpautop splitting.
- File size text removed from PDF button per editorial standard.
- Supports both 1-Click Direct Download and 30s Countdown Timer.
"""

import html

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
        # 1-Click Instant Download
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
        # 30-Second Countdown Timer Mode
        return f"""<div class="pdf-download-wrap">
  <a class="pdf-download-btn" href="{clean_url}" data-timer="{timer_seconds}" data-url="{clean_url}" target="_blank" rel="noopener noreferrer">
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
    include_script: bool = False
) -> str:
    """
    Renders the complete editorial PDF download section including introductory card
    and the centered official PDF pill button.
    """
    clean_heading = html.escape(heading_title) if "<" not in heading_title else heading_title
    clean_specs = html.escape(file_spec) if "<" not in file_spec else file_spec

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

    section_html = f"""<div class="htbd-pdf-section" style="box-sizing: border-box; font-family: 'SolaimanLipi', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #ffffff; border: 1.5px solid #e2e8f0; border-top: 4px solid #dc2626; border-radius: 14px; padding: 22px 20px; margin: 30px 0 25px 0; box-shadow: 0 4px 15px rgba(0,0,0,0.04); color: #334155;">
  <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 10px;">
    <span style="display: inline-flex; align-items: center; justify-content: center; width: 38px; height: 38px; background: rgba(220, 38, 38, 0.1); border-radius: 9px; color: #dc2626; flex-shrink: 0;">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#dc2626" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
        <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
        <polyline points="14 2 14 8 20 8"/>
        <line x1="16" y1="13" x2="8" y2="13"/>
        <line x1="16" y1="17" x2="8" y2="17"/>
      </svg>
    </span>
    <div>
      <h2 id="pdf-download" style="color: #0f172a; font-size: 19px; font-weight: 700; margin: 0; line-height: 1.35; border: none; padding: 0;">
        অফিসিয়াল PDF ডাউনলোড: {clean_heading}
      </h2>
      <div style="font-size: 12px; opacity: 0.8; margin-top: 3px;">
        {clean_specs}
      </div>
    </div>
  </div>

  <p style="color: #475569; font-size: 15px; line-height: 1.75; margin: 12px 0 16px 0;">
    {description_text}
  </p>

  {button_markup}

  <div style="margin-top: 14px; font-size: 12px; opacity: 0.75; text-align: center;">
    নিরাপদ ক্লাউড সার্ভার • সম্পূর্ণ বিজ্ঞাপন-মুক্ত ডাউনলোড
  </div>
</div>"""

    return section_html
