#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/page_builder/build_nu_cgpa_calculator_page.py
----------------------------------------------------
Compiles the master HTML and metadata for the National University (NU) CGPA Calculator Page.
Includes:
- Full responsive canvas and modern card transformation for mobile viewports (<= 640px)
- Ultra-polished, 100% color-matched bi-modal dark mode support (Blogger .dark & body.dark)
- Two-way exact point (GP) and letter grade synchronization
- Full academic syllabus auto-loader, smart paste parser, target planner & improvement simulator
- High-definition official National University Academic Transcript & Grade Report PDF/Print Engine
- Isolated iframe print architecture (STRICTLY 1-page A4 PDF output, zero blank trailing pages, zero blog clutter)
- Verified against pre_flight_checker.py
"""

import os
import sys
import json

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

OUTPUT_DIR = os.path.join(PROJECT_ROOT, "output_pages")
os.makedirs(OUTPUT_DIR, exist_ok=True)

HTML_PATH = os.path.join(OUTPUT_DIR, "nu-cgpa-calculator.html")
META_PATH = os.path.join(OUTPUT_DIR, "nu-cgpa-calculator_meta.json")

def generate_page():
    # 1. Read syllabus DB from python dict
    from tools.page_builder.test_syllabus import SYLLABUS_DB
    syllabus_json_str = json.dumps(SYLLABUS_DB, ensure_ascii=False)

    html_content = f'''<figure style="margin: 0 0 25px 0; text-align: center;">
<img src="https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/posts/nu_cgpa_calculator_honours_degree_masters_2026.webp" alt="জাতীয় বিশ্ববিদ্যালয় সিজিপিএ ক্যালকুলেটর ২০২৬" title="National University CGPA Calculator and Honours Grading Guide 2026" width="1200" height="675" style="max-width: 100%; height: auto; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.08); display: block; margin: 0 auto;" loading="eager" />
<figcaption style="font-family: 'SolaimanLipi', Arial, sans-serif; font-size: 14px; color: #64748b; margin-top: 10px; font-weight: 500;">
ছবি: জাতীয় বিশ্ববিদ্যালয় সিজিপিএ ক্যালকুলেটর, গ্রেডিং স্কেল ও একাডেমিক রেজাল্ট রূপরেখা
</figcaption>
</figure>

<p style="font-family: 'SolaimanLipi', sans-serif; font-size: 17px; line-height: 1.85; color: #1e293b; margin-bottom: 20px;">
জাতীয় বিশ্ববিদ্যালয় (National University, Bangladesh)-এর অধীনে স্নাতক (সম্মান), ডিগ্রি (পাস) এবং মাস্টার্স কোর্সের শিক্ষার্থীদের ফলাফল প্রকাশের পর সবচেয়ে গুরুত্বপূর্ণ বিষয় হলো সঠিক পদ্ধতিতে জিপিএ (GPA) ও সম্মিলিত সিজিপিএ (CGPA) গণনা করা। ক্রেডিট পদ্ধতির জটিল নিয়ম, নন-ক্রেডিট আবশ্যিক ইংরেজি বিষয় এবং ইনকোর্স ও ব্যবহারিক নম্বরের প্রভাবে ম্যানুয়ালি রেজাল্ট হিসাব করতে গিয়ে অধিকাংশ শিক্ষার্থীই বিভ্রান্ত হন। শিক্ষার্থীদের এই ভোগান্তি দূর করতে হেল্পট্রিকবিডি নিয়ে এলো দেশের প্রথম <strong>সম্পূর্ণ ইন্টারেক্টিভ ও স্বয়ংক্রিয় জাতীয় বিশ্ববিদ্যালয় সিজিপিএ ক্যালকুলেটর ২০২৬</strong>। এই টুলের মাধ্যমে শিক্ষার্থী কেবল তাদের প্রাপ্ত লেটার গ্রেড বা নম্বর ইনপুট দিয়েই নয়, বরং ডিপার্টমেন্টভিত্তিক অফিসিয়াল সিলেবাস অটো-লোড এবং রেজাল্ট টেক্সট কপি-পেস্ট করে মুহূর্তে নির্ভুল সিজিপিএ ও ক্লাস (First Class / Second Class) যাচাই করতে পারবেন।
</p>

<!-- Quick Overview Callout Box -->
<div class="htbd-overview-box" style="background: #eff6ff; border-left: 5px solid #2563eb; border-radius: 8px; padding: 20px 24px; margin: 25px 0; font-family: 'SolaimanLipi', sans-serif;">
<h3 class="htbd-overview-title" style="margin: 0 0 10px 0; color: #1e3a8a; font-size: 19px; font-weight: 700;">এনইউ সিজিপিএ ক্যালকুলেটরের মূল বৈশিষ্ঠ্য একনজরে | Tool Overview</h3>
<p class="htbd-overview-text" style="margin: 0; color: #1e293b; font-size: 16px; line-height: 1.85;">
জাতীয় বিশ্ববিদ্যালয়ের ৪.০০ স্কেল ভিত্তিক এই ক্যালকুলেটরে রয়েছে: <strong>১. ইয়ার-ওয়াইজ লাইভ স্লাইডার সিজিপিএ ক্যালকুলেটর</strong>, <strong>২. ডিপার্টমেন্ট ও সিলেবাস অটো-লোড সুবিধা সহ বিষয়ভিত্তিক জিপিএ গণনা</strong>, <strong>৩. টার্গেট ফার্স্ট ক্লাস (৩.০০) প্ল্যানার</strong> এবং <strong>৪. মানোন্নয়ন (Improvement) পরীক্ষার প্রভাব সিমুলেটর</strong>। এছাড়া ফলাফল সরাসরি অফিসিয়াল প্রাতিষ্ঠানিক একাডেমিক ট্রান্সক্রিপ্ট ও গ্রেড শিট আকারে <strong>শতভাগ প্রফেশনাল ১-পাতা A4 PDF</strong> হিসেবে প্রিন্ট বা সংরক্ষণের সুবিধা যুক্ত রয়েছে।
</p>
<div class="htbd-overview-source" style="margin-top: 12px; font-size: 14.5px; color: #1d4ed8; font-weight: 600;">
তথ্যসূত্র: জাতীয় বিশ্ববিদ্যালয় পরীক্ষা নিয়ন্ত্রণ দপ্তর ও স্নাতক (সম্মান) অর্ডিন্যান্স অনুযায়ী শতভাগ পরীক্ষিত
</div>
</div>

<!--more-->

<style>
/* ========================================================================== */
/* 0. SOLAIMANLIPI & BENGALI HIGH-PRECISION WEB TYPOGRAPHY                    */
/* ========================================================================== */
@import url('https://fonts.maateen.me/solaiman-lipi/font.css');
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Bengali:wght@400;500;600;700&display=swap');

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

/* ========================================================================== */
/* 1. FULL-WIDTH RESPONSIVE CANVAS FOR BLOGGER                                */
/* ========================================================================== */
.static_page #feed-view, .item-view #feed-view, #feed-view,
.static_page .main-wrapper, .item-view .main-wrapper,
.static_page .content-wrapper, .item-view .content-wrapper,
.static_page #main, .item-view #main,
.static_page .blog-post, .item-view .blog-post,
.static_page .post-body, .item-view .post-body,
.static_page .post-outer-container, .item-view .post-outer-container {{
  width: 100% !important;
  max-width: 100% !important;
  float: none !important;
  box-sizing: border-box !important;
}}
.static_page #sidebar-container, .item-view #sidebar-container, #sidebar-container {{
  display: none !important;
}}

/* ========================================================================== */
/* 2. BASE APP ARCHITECTURE & GRID                                            */
/* ========================================================================== */
#htbd-nu-cgpa-app {{
  width: 100% !important;
  max-width: 100% !important;
  box-sizing: border-box !important;
  font-family: 'SolaimanLipi', 'Noto Sans Bengali', Arial, sans-serif !important;
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 16px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.06);
  padding: 24px;
  margin: 35px 0;
  color: #0f172a;
  transition: background 0.3s ease, border-color 0.3s ease, color 0.3s ease;
}}

.htbd-calc-grid {{
  display: grid;
  grid-template-columns: 1.15fr 0.85fr;
  gap: 24px;
  width: 100%;
  box-sizing: border-box;
}}

.htbd-left-panel {{
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 12px;
  padding: 20px;
  transition: all 0.3s ease;
}}

.htbd-right-panel {{
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 12px;
  padding: 22px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  box-shadow: 0 4px 15px rgba(0,0,0,0.03);
  transition: all 0.3s ease;
}}

/* Program Selector Buttons */
.htbd-prog-btn {{
  background: #f1f5f9;
  color: #475569;
  border: 1px solid #cbd5e1;
  padding: 8px 18px;
  border-radius: 30px;
  font-size: 15px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
  font-family: inherit;
}}
.htbd-prog-btn:hover {{
  background: #e2e8f0;
  color: #1e293b;
}}
.htbd-prog-btn.active {{
  background: #1e3a8a !important;
  color: #ffffff !important;
  border-color: #1e3a8a !important;
  box-shadow: 0 2px 8px rgba(30,58,138,0.25);
}}

/* Master Mode Switcher Tab Buttons */
.htbd-tab-btn {{
  flex: 1;
  min-width: 140px;
  padding: 10px 14px;
  background: #f8fafc;
  color: #334155;
  border: 1px solid #cbd5e1;
  border-radius: 8px;
  font-size: 15px;
  font-weight: 600;
  cursor: pointer;
  text-align: center;
  transition: all 0.2s ease;
  font-family: inherit;
}}
.htbd-tab-btn:hover {{
  background: #f1f5f9;
  color: #0f172a;
}}
.htbd-tab-btn.active {{
  background: #2563eb !important;
  color: #ffffff !important;
  border-color: #2563eb !important;
  box-shadow: 0 2px 8px rgba(37,99,235,0.25);
}}

/* Secondary Action Buttons */
.htbd-btn-secondary {{
  background: #f1f5f9;
  color: #475569;
  border: 1px solid #cbd5e1;
  padding: 8px 12px;
  border-radius: 6px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
  font-family: inherit;
}}
.htbd-btn-secondary:hover {{
  background: #e2e8f0;
  color: #1e293b;
}}

/* Cards & Metric Containers */
.htbd-year-card {{
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 10px;
  padding: 14px;
  transition: all 0.2s ease;
}}
.htbd-syllabus-box {{
  background: #e0f2fe;
  border: 1px solid #bae6fd;
  border-radius: 8px;
  padding: 12px;
  margin-bottom: 16px;
  transition: all 0.2s ease;
}}
.htbd-smart-paste-box {{
  background: #f1f5f9;
  border: 2px dashed #94a3b8;
  border-radius: 8px;
  padding: 14px;
  margin-bottom: 16px;
  transition: all 0.2s ease;
}}
.htbd-target-card {{
  background: #ffffff;
  border: 1px solid #cbd5e1;
  border-radius: 8px;
  padding: 16px;
  margin-top: 5px;
  transition: all 0.2s ease;
}}
.htbd-imp-box {{
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  padding: 14px;
  transition: all 0.2s ease;
}}
.htbd-imp-result-box {{
  background: #ecfdf5;
  border: 1px solid #a7f3d0;
  border-radius: 8px;
  padding: 14px;
  transition: all 0.2s ease;
}}
.htbd-metric-pill {{
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  padding: 10px;
  text-align: center;
  transition: all 0.2s ease;
}}
.htbd-trend-card {{
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  padding: 12px;
  margin-bottom: 20px;
  transition: all 0.2s ease;
}}

/* ========================================================================== */
/* 3. DESKTOP TABLE HEADERS & ROWS                                            */
/* ========================================================================== */
.htbd-course-header {{
  display: grid;
  grid-template-columns: 2.2fr 1fr 1.25fr 1fr 38px;
  gap: 8px;
  padding: 8px 12px;
  background: #e2e8f0;
  border-radius: 6px;
  font-size: 13px;
  font-weight: 700;
  color: #334155;
  margin-bottom: 8px;
  align-items: center;
}}

.htbd-course-row {{
  display: grid;
  grid-template-columns: 2.2fr 1fr 1.25fr 1fr 38px;
  gap: 8px;
  padding: 8px 10px;
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  align-items: center;
  box-shadow: 0 1px 3px rgba(0,0,0,0.02);
  transition: all 0.2s ease;
  box-sizing: border-box;
  width: 100%;
}}
.htbd-course-row:hover {{
  border-color: #93c5fd;
  box-shadow: 0 2px 6px rgba(37,99,235,0.08);
}}
.cr-top {{
  display: contents;
}}
.cr-controls {{
  display: contents;
}}
.cr-name {{
  grid-column: 1;
}}
.cr-col-credit {{
  grid-column: 2;
}}
.cr-col-grade {{
  grid-column: 3;
}}
.cr-col-point {{
  grid-column: 4;
}}
.cr-del-wrap {{
  grid-column: 5;
  text-align: center;
}}
.cr-label {{
  display: none;
}}
.c-name, .c-credit, .c-grade, .c-point {{
  box-sizing: border-box !important;
  transition: border-color 0.2s, box-shadow 0.2s;
  font-family: inherit;
}}
.c-name:focus, .c-credit:focus, .c-grade:focus, .c-point:focus {{
  outline: none !important;
  border-color: #2563eb !important;
  box-shadow: 0 0 0 3px rgba(37,99,235,0.15) !important;
}}
.btn-del-course {{
  background: #fee2e2;
  color: #ef4444;
  border: none;
  width: 34px;
  height: 34px;
  border-radius: 6px;
  cursor: pointer;
  font-size: 18px;
  font-weight: bold;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s;
}}
.btn-del-course:hover {{
  background: #fecaca;
  color: #dc2626;
  transform: scale(1.05);
}}

/* Improvement Simulator Row (Desktop) */
.htbd-imp-header {{
  display: grid;
  grid-template-columns: 1.8fr 1.1fr 1.1fr 34px;
  gap: 6px;
  padding: 6px 10px;
  background: #f1f5f9;
  border-radius: 4px;
  font-size: 12px;
  font-weight: 700;
  color: #475569;
  margin-bottom: 6px;
  align-items: center;
}}
.imp-course-row {{
  display: grid;
  grid-template-columns: 1.8fr 1.1fr 1.1fr 34px;
  gap: 6px;
  align-items: center;
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 6px;
  padding: 6px 8px;
  box-sizing: border-box;
}}
.imp-top {{
  display: contents;
}}
.imp-bottom {{
  display: contents;
}}
.imp-name-wrap {{
  grid-column: 1;
}}
.imp-col-old {{
  grid-column: 2;
}}
.imp-col-new {{
  grid-column: 3;
}}
.imp-del-wrap {{
  grid-column: 4;
  text-align: center;
}}
.imp-label {{
  display: none;
}}
.btn-del-imp {{
  background: #fee2e2;
  color: #ef4444;
  border: none;
  width: 30px;
  height: 30px;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
  font-weight: bold;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s;
}}
.btn-del-imp:hover {{
  background: #fecaca;
  color: #dc2626;
}}

/* ========================================================================== */
/* 4. DYNAMIC BADGE STYLING (LIGHT & DARK BI-MODAL)                          */
/* ========================================================================== */
.htbd-badge {{
  display: inline-block;
  padding: 6px 16px;
  border-radius: 20px;
  font-size: 14.5px;
  font-weight: 700;
  transition: all 0.3s ease;
}}
.htbd-badge-empty {{
  background: #f1f5f9;
  color: #475569;
  border: 1px solid #cbd5e1;
}}
.htbd-badge-first {{
  background: #dcfce7;
  color: #15803d;
  border: 1px solid #86efac;
}}
.htbd-badge-second {{
  background: #dbeafe;
  color: #1e40af;
  border: 1px solid #93c5fd;
}}
.htbd-badge-third {{
  background: #fef3c7;
  color: #b45309;
  border: 1px solid #fde68a;
}}
.htbd-badge-fail {{
  background: #fee2e2;
  color: #b91c1c;
  border: 1px solid #fca5a5;
}}

/* Target Planner Badges */
.htbd-target-easy {{
  background: #dcfce7;
  color: #15803d;
  border: 1px solid #86efac;
}}
.htbd-target-medium {{
  background: #dbeafe;
  color: #1e40af;
  border: 1px solid #93c5fd;
}}
.htbd-target-hard {{
  background: #fef3c7;
  color: #b45309;
  border: 1px solid #fde68a;
}}
.htbd-target-impossible {{
  background: #fee2e2;
  color: #b91c1c;
  border: 1px solid #fca5a5;
}}

/* ========================================================================== */
/* 5. LIVE TRANSCRIPT PREVIEW MODAL STYLING                                  */
/* ========================================================================== */
#htbd-transcript-modal {{
  display: none;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(15, 23, 42, 0.85);
  backdrop-filter: blur(8px);
  z-index: 999999;
  overflow-y: auto;
  padding: 20px 10px;
  box-sizing: border-box;
}}
.htbd-modal-wrapper {{
  max-width: 880px;
  margin: 15px auto 40px auto;
  background: #ffffff;
  border-radius: 14px;
  box-shadow: 0 20px 50px rgba(0,0,0,0.35);
  overflow: hidden;
  border: 1px solid #cbd5e1;
}}
.htbd-modal-header {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 16px 22px;
  background: #1e3a8a;
  color: #ffffff;
}}
.htbd-modal-toolbar {{
  background: #f8fafc;
  border-bottom: 1px solid #e2e8f0;
  padding: 16px 20px;
  display: grid;
  grid-template-columns: 1fr 1fr 1fr auto;
  gap: 12px;
  align-items: flex-end;
}}
.htbd-modal-input-group {{
  display: flex;
  flex-direction: column;
  gap: 4px;
}}
.htbd-modal-label {{
  font-size: 12.5px;
  font-weight: 700;
  color: #334155;
}}
.htbd-modal-input {{
  padding: 8px 10px;
  border: 1.5px solid #cbd5e1;
  border-radius: 6px;
  font-size: 13.5px;
  box-sizing: border-box;
  width: 100%;
  font-family: inherit;
}}
.btn-trigger-print {{
  background: #15803d;
  color: #ffffff;
  border: none;
  padding: 9px 18px;
  border-radius: 6px;
  font-size: 14px;
  font-weight: 700;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  transition: all 0.2s ease;
  white-space: nowrap;
}}
.btn-trigger-print:hover {{
  background: #166534;
  transform: translateY(-1px);
}}
.btn-modal-close {{
  background: rgba(255,255,255,0.15);
  color: #ffffff;
  border: none;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  cursor: pointer;
  font-size: 18px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: 0.2s;
}}
.btn-modal-close:hover {{
  background: rgba(255,255,255,0.3);
}}
.htbd-preview-scroll {{
  padding: 24px;
  background: #e2e8f0;
  overflow-x: auto;
  display: flex;
  justify-content: center;
}}

/* The Pure A4 Transcript Sheet */
#htbd-certificate-paper, #htbd-certificate-paper * {{
  font-family: 'SolaimanLipi', 'Noto Sans Bengali', Arial, sans-serif !important;
}}
#htbd-certificate-paper {{
  width: 100%;
  max-width: 790px;
  background: #ffffff !important;
  color: #0c2340 !important;
  padding: 24px;
  box-shadow: 0 4px 20px rgba(0,0,0,0.1);
  box-sizing: border-box;
  position: relative;
  border: 3px solid #1e3a8a;
  border-radius: 8px;
}}
.htbd-cert-inner-frame {{
  border: 1.5px solid #b45309;
  padding: 16px 18px;
  border-radius: 4px;
  position: relative;
  background: #ffffff;
}}

/* ========================================================================== */
/* 6. MOBILE & TABLET RESPONSIVE RULES (< 880px and < 640px)                  */
/* ========================================================================== */
@media (max-width: 880px) {{
  .htbd-calc-grid {{
    grid-template-columns: 1fr;
    gap: 20px;
  }}
  .htbd-modal-toolbar {{
    grid-template-columns: 1fr 1fr;
  }}
}}

@media (max-width: 640px) {{
  #htbd-nu-cgpa-app {{
    padding: 14px 10px !important;
    border-radius: 12px !important;
    margin: 15px 0 !important;
  }}
  .htbd-left-panel, .htbd-right-panel {{
    padding: 14px 10px !important;
  }}
  .htbd-prog-btn {{
    font-size: 13px !important;
    padding: 6px 14px !important;
  }}
  .htbd-tab-btn {{
    font-size: 13.5px !important;
    padding: 8px 10px !important;
    min-width: 130px !important;
  }}
  .htbd-modal-toolbar {{
    grid-template-columns: 1fr;
  }}
  .htbd-preview-scroll {{
    padding: 10px 4px;
  }}
  #htbd-certificate-paper {{
    padding: 12px 8px;
  }}
  .htbd-cert-inner-frame {{
    padding: 10px 8px;
  }}

  /* Hide raw table header on mobile */
  .htbd-course-header {{
    display: none !important;
  }}

  /* Transform Subject Row into an Ultra-Modern Card */
  .htbd-course-row {{
    display: flex !important;
    flex-direction: column !important;
    gap: 8px !important;
    padding: 12px 10px !important;
    border-radius: 10px !important;
    border: 1px solid #cbd5e1 !important;
    box-shadow: 0 2px 5px rgba(0,0,0,0.03) !important;
  }}
  .cr-top {{
    display: flex !important;
    align-items: center !important;
    gap: 8px !important;
    width: 100% !important;
  }}
  .cr-name {{
    flex: 1 1 auto !important;
    min-width: 0 !important;
    grid-column: auto !important;
  }}
  .cr-name input {{
    font-size: 14px !important;
    font-weight: 600 !important;
    padding: 8px 10px !important;
    height: 38px !important;
    border: 1px solid #94a3b8 !important;
    border-radius: 6px !important;
  }}
  .cr-del-wrap {{
    grid-column: auto !important;
    flex-shrink: 0 !important;
  }}
  .btn-del-course {{
    width: 36px !important;
    height: 36px !important;
  }}
  .cr-controls {{
    display: grid !important;
    grid-template-columns: 1fr 1.15fr 1fr !important;
    gap: 6px !important;
    width: 100% !important;
  }}
  .cr-col-credit, .cr-col-grade, .cr-col-point {{
    display: flex !important;
    flex-direction: column !important;
    gap: 3px !important;
    min-width: 0 !important;
    grid-column: auto !important;
  }}
  .cr-label {{
    display: block !important;
    font-size: 11.5px !important;
    font-weight: 700 !important;
    color: #475569 !important;
    white-space: nowrap !important;
  }}
  .c-credit, .c-grade, .c-point {{
    width: 100% !important;
    height: 38px !important;
    padding: 5px 4px !important;
    font-size: 13px !important;
    border-radius: 6px !important;
  }}

  /* Improvement Simulator Mobile Card */
  .htbd-imp-header {{
    display: none !important;
  }}
  .imp-course-row {{
    display: flex !important;
    flex-direction: column !important;
    gap: 8px !important;
    padding: 10px !important;
  }}
  .imp-top {{
    display: flex !important;
    align-items: center !important;
    gap: 8px !important;
    width: 100% !important;
  }}
  .imp-name-wrap {{
    flex: 1 1 auto !important;
    min-width: 0 !important;
    grid-column: auto !important;
  }}
  .imp-del-wrap {{
    grid-column: auto !important;
    flex-shrink: 0 !important;
  }}
  .imp-bottom {{
    display: grid !important;
    grid-template-columns: 1fr 1fr !important;
    gap: 8px !important;
    width: 100% !important;
  }}
  .imp-col-old, .imp-col-new {{
    display: flex !important;
    flex-direction: column !important;
    gap: 3px !important;
    grid-column: auto !important;
  }}
  .imp-label {{
    display: block !important;
    font-size: 11.5px !important;
    font-weight: 700 !important;
    color: #475569 !important;
    white-space: nowrap !important;
  }}
  .imp-old-gp, .imp-new-gp {{
    height: 36px !important;
  }}
}}

/* ========================================================================== */
/* 7. FLAWLESS BI-MODAL DARK MODE ENGINE (100% COLOR HARMONY)                */
/* ========================================================================== */
.dark, body.dark, html.dark {{
  color-scheme: dark;
}}

/* Outer App Container */
.dark #htbd-nu-cgpa-app, body.dark #htbd-nu-cgpa-app {{
  background: #1e293b !important;
  border-color: #334155 !important;
  color: #f1f5f9 !important;
  box-shadow: 0 10px 30px rgba(0,0,0,0.3) !important;
}}

/* Header Elements */
.dark .htbd-app-badge, body.dark .htbd-app-badge {{
  background: #312e81 !important;
  color: #c7d2fe !important;
}}
.dark .htbd-app-title, body.dark .htbd-app-title {{
  color: #f8fafc !important;
}}
.dark .htbd-app-subtitle, body.dark .htbd-app-subtitle {{
  color: #94a3b8 !important;
}}
.dark .htbd-app-divider, body.dark .htbd-app-divider {{
  border-bottom-color: #334155 !important;
}}

/* Panels */
.dark .htbd-left-panel, body.dark .htbd-left-panel {{
  background: #0f172a !important;
  border-color: #334155 !important;
}}
.dark .htbd-right-panel, body.dark .htbd-right-panel {{
  background: #0f172a !important;
  border-color: #334155 !important;
  box-shadow: 0 4px 20px rgba(0,0,0,0.25) !important;
}}

/* Headings inside App */
.dark #htbd-nu-cgpa-app h2, body.dark #htbd-nu-cgpa-app h2,
.dark #htbd-nu-cgpa-app h3, body.dark #htbd-nu-cgpa-app h3,
.dark #htbd-nu-cgpa-app h4, body.dark #htbd-nu-cgpa-app h4 {{
  color: #f8fafc !important;
}}

/* Program Selector Buttons */
.dark .htbd-prog-btn, body.dark .htbd-prog-btn {{
  background: #1e293b !important;
  color: #94a3b8 !important;
  border-color: #334155 !important;
}}
.dark .htbd-prog-btn:hover, body.dark .htbd-prog-btn:hover {{
  background: #334155 !important;
  color: #f8fafc !important;
}}
.dark .htbd-prog-btn.active, body.dark .htbd-prog-btn.active {{
  background: #3b82f6 !important;
  color: #ffffff !important;
  border-color: #3b82f6 !important;
  box-shadow: 0 2px 10px rgba(59,130,246,0.3) !important;
}}

/* Mode Tab Buttons */
.dark .htbd-tab-btn, body.dark .htbd-tab-btn {{
  background: #1e293b !important;
  color: #94a3b8 !important;
  border-color: #334155 !important;
}}
.dark .htbd-tab-btn:hover, body.dark .htbd-tab-btn:hover {{
  background: #334155 !important;
  color: #f8fafc !important;
}}
.dark .htbd-tab-btn.active, body.dark .htbd-tab-btn.active {{
  background: #2563eb !important;
  color: #ffffff !important;
  border-color: #2563eb !important;
  box-shadow: 0 2px 10px rgba(37,99,235,0.3) !important;
}}

/* Form Inputs, Selects & Textarea */
.dark input, body.dark input,
.dark select, body.dark select,
.dark textarea, body.dark textarea {{
  color-scheme: dark !important;
  background: #0f172a !important;
  color: #f8fafc !important;
  border-color: #475569 !important;
}}
.dark input:focus, body.dark input:focus,
.dark select:focus, body.dark select:focus,
.dark textarea:focus, body.dark textarea:focus {{
  border-color: #3b82f6 !important;
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.25) !important;
}}

/* Secondary Action Buttons */
.dark .htbd-btn-secondary, body.dark .htbd-btn-secondary {{
  background: #334155 !important;
  color: #e2e8f0 !important;
  border-color: #475569 !important;
}}
.dark .htbd-btn-secondary:hover, body.dark .htbd-btn-secondary:hover {{
  background: #475569 !important;
  color: #ffffff !important;
}}

/* Year Cards */
.dark .htbd-year-card, body.dark .htbd-year-card {{
  background: #1e293b !important;
  border-color: #334155 !important;
}}
.dark .htbd-year-title, body.dark .htbd-year-title {{
  color: #93c5fd !important;
}}
.dark .htbd-year-credit-lbl, body.dark .htbd-year-credit-lbl {{
  color: #94a3b8 !important;
}}

/* Table Headers & Course Rows */
.dark .htbd-course-header, body.dark .htbd-course-header {{
  background: #334155 !important;
  color: #cbd5e1 !important;
}}
.dark .htbd-course-row, body.dark .htbd-course-row {{
  background: #1e293b !important;
  border-color: #334155 !important;
}}
.dark .c-point, body.dark .c-point {{
  background: #0f172a !important;
  color: #f8fafc !important;
  border-color: #475569 !important;
}}
.dark .c-grade, body.dark .c-grade {{
  color: #93c5fd !important;
}}
.dark .cr-label, body.dark .cr-label,
.dark .imp-label, body.dark .imp-label {{
  color: #94a3b8 !important;
}}
.dark .btn-del-course, body.dark .btn-del-course,
.dark .btn-del-imp, body.dark .btn-del-imp {{
  background: #450a0a !important;
  color: #f87171 !important;
}}
.dark .btn-del-course:hover, body.dark .btn-del-course:hover,
.dark .btn-del-imp:hover, body.dark .btn-del-imp:hover {{
  background: #7f1d1d !important;
  color: #fca5a5 !important;
}}

/* Syllabus Box */
.dark .htbd-syllabus-box, body.dark .htbd-syllabus-box {{
  background: #082f49 !important;
  border-color: #0284c7 !important;
}}
.dark .htbd-syllabus-label, body.dark .htbd-syllabus-label {{
  color: #7dd3fc !important;
}}

/* Smart Paste Box */
.dark .htbd-smart-paste-box, body.dark .htbd-smart-paste-box {{
  background: #1e293b !important;
  border-color: #475569 !important;
}}
.dark .htbd-smart-paste-title, body.dark .htbd-smart-paste-title {{
  color: #f8fafc !important;
}}
.dark .htbd-smart-paste-desc, body.dark .htbd-smart-paste-desc {{
  color: #94a3b8 !important;
}}

/* Target First Class Planner */
.dark .htbd-target-card, body.dark .htbd-target-card {{
  background: #1e293b !important;
  border-color: #334155 !important;
}}
.dark .htbd-target-label, body.dark .htbd-target-label {{
  color: #cbd5e1 !important;
}}
.dark #target-req-gpa, body.dark #target-req-gpa {{
  color: #60a5fa !important;
}}
.dark #target-advice, body.dark #target-advice {{
  color: #cbd5e1 !important;
}}

/* Improvement Simulator */
.dark .htbd-imp-box, body.dark .htbd-imp-box {{
  background: #1e293b !important;
  border-color: #334155 !important;
}}
.dark .htbd-imp-header, body.dark .htbd-imp-header {{
  background: #334155 !important;
  color: #cbd5e1 !important;
}}
.dark .imp-course-row, body.dark .imp-course-row {{
  background: #0f172a !important;
  border-color: #334155 !important;
}}
.dark .imp-new-gp, body.dark .imp-new-gp {{
  border-color: #059669 !important;
  background: #064e3b !important;
  color: #6ee7b7 !important;
}}
.dark #btn-add-imp-course, body.dark #btn-add-imp-course {{
  background: #1e293b !important;
  color: #93c5fd !important;
  border-color: #3b82f6 !important;
}}
.dark .htbd-imp-result-box, body.dark .htbd-imp-result-box {{
  background: #064e3b !important;
  border-color: #047857 !important;
}}
.dark .htbd-imp-res-label, body.dark .htbd-imp-res-label {{
  color: #a7f3d0 !important;
}}
.dark #imp-new-gpa, body.dark #imp-new-gpa {{
  color: #34d399 !important;
}}
.dark #imp-delta-gpa, body.dark #imp-delta-gpa {{
  color: #6ee7b7 !important;
}}

/* Dashboard Badges in Dark Mode */
.dark .htbd-badge-empty, body.dark .htbd-badge-empty {{
  background: #334155 !important;
  color: #cbd5e1 !important;
  border-color: #475569 !important;
}}
.dark .htbd-badge-first, body.dark .htbd-badge-first,
.dark .htbd-target-easy, body.dark .htbd-target-easy {{
  background: rgba(34, 197, 94, 0.18) !important;
  color: #4ade80 !important;
  border: 1px solid rgba(34, 197, 94, 0.4) !important;
}}
.dark .htbd-badge-second, body.dark .htbd-badge-second,
.dark .htbd-target-medium, body.dark .htbd-target-medium {{
  background: rgba(59, 130, 246, 0.18) !important;
  color: #60a5fa !important;
  border: 1px solid rgba(59, 130, 246, 0.4) !important;
}}
.dark .htbd-badge-third, body.dark .htbd-badge-third,
.dark .htbd-target-hard, body.dark .htbd-target-hard {{
  background: rgba(245, 158, 11, 0.18) !important;
  color: #fbbf24 !important;
  border: 1px solid rgba(245, 158, 11, 0.4) !important;
}}
.dark .htbd-badge-fail, body.dark .htbd-badge-fail,
.dark .htbd-target-impossible, body.dark .htbd-target-impossible {{
  background: rgba(239, 68, 68, 0.18) !important;
  color: #f87171 !important;
  border: 1px solid rgba(239, 68, 68, 0.4) !important;
}}

/* Circular Gauge & Analytics Dashboard */
.dark #dash-program-badge, body.dark #dash-program-badge {{
  background: #1e3a8a !important;
  color: #93c5fd !important;
}}
.dark .dash-gauge-track, body.dark .dash-gauge-track {{
  stroke: #334155 !important;
}}
.dark #dash-cgpa-val, body.dark #dash-cgpa-val {{
  color: #f8fafc !important;
}}
.dark .dash-gauge-subtext, body.dark .dash-gauge-subtext {{
  color: #94a3b8 !important;
}}
.dark .htbd-metric-pill, body.dark .htbd-metric-pill {{
  background: #1e293b !important;
  border-color: #334155 !important;
}}
.dark .htbd-metric-val, body.dark .htbd-metric-val {{
  color: #f8fafc !important;
}}
.dark .htbd-metric-lbl, body.dark .htbd-metric-lbl {{
  color: #94a3b8 !important;
}}

/* Trend Graph */
.dark .htbd-trend-card, body.dark .htbd-trend-card {{
  background: #1e293b !important;
  border-color: #334155 !important;
}}
.dark .htbd-trend-title, body.dark .htbd-trend-title {{
  color: #cbd5e1 !important;
}}
.dark .dash-trend-axis, body.dark .dash-trend-axis {{
  stroke: #334155 !important;
}}
.dark #dash-trend-line, body.dark #dash-trend-line {{
  stroke: #38bdf8 !important;
}}
.dark #dash-trend-svg circle, body.dark #dash-trend-svg circle {{
  fill: #60a5fa !important;
}}

/* Transcript Modal in Dark Mode */
.dark .htbd-modal-wrapper, body.dark .htbd-modal-wrapper {{
  background: #1e293b !important;
  border-color: #334155 !important;
}}
.dark .htbd-modal-toolbar, body.dark .htbd-modal-toolbar {{
  background: #0f172a !important;
  border-bottom-color: #334155 !important;
}}
.dark .htbd-modal-label, body.dark .htbd-modal-label {{
  color: #cbd5e1 !important;
}}
.dark .htbd-modal-input, body.dark .htbd-modal-input {{
  background: #1e293b !important;
  border-color: #475569 !important;
  color: #f8fafc !important;
}}
.dark .htbd-preview-scroll, body.dark .htbd-preview-scroll {{
  background: #0f172a !important;
}}

/* Quick Overview Box Dark Mode */
.dark .htbd-overview-box, body.dark .htbd-overview-box {{
  background: #1e293b !important;
  border-left-color: #3b82f6 !important;
}}
.dark .htbd-overview-title, body.dark .htbd-overview-title {{
  color: #93c5fd !important;
}}
.dark .htbd-overview-text, body.dark .htbd-overview-text {{
  color: #cbd5e1 !important;
}}
.dark .htbd-overview-source, body.dark .htbd-overview-source {{
  color: #60a5fa !important;
}}

/* Academic Content Headings & Text */
.dark .htbd-content-h2, body.dark .htbd-content-h2 {{
  color: #93c5fd !important;
  border-left-color: #3b82f6 !important;
}}
.dark .post-body p, body.dark .post-body p,
.dark .post-body li, body.dark .post-body li {{
  color: #cbd5e1 !important;
}}
.dark .post-body strong, body.dark .post-body strong {{
  color: #f8fafc !important;
}}

/* Grading Table Dark Mode */
.dark .htbd-grade-table, body.dark .htbd-grade-table {{
  border-color: #334155 !important;
}}
.dark .htbd-grade-table th, body.dark .htbd-grade-table th {{
  background: #1e3a8a !important;
  color: #ffffff !important;
  border-color: #334155 !important;
}}
.dark .htbd-grade-table td, body.dark .htbd-grade-table td {{
  border-color: #334155 !important;
  color: #e2e8f0 !important;
}}
.dark .htbd-grade-table tr.row-even, body.dark .htbd-grade-table tr.row-even {{
  background: #1e293b !important;
}}
.dark .htbd-grade-table tr.row-odd, body.dark .htbd-grade-table tr.row-odd {{
  background: #0f172a !important;
}}
.dark .htbd-grade-table tr.row-fail, body.dark .htbd-grade-table tr.row-fail {{
  background: rgba(220, 38, 38, 0.18) !important;
}}
.dark .htbd-grade-table tr.row-fail td, body.dark .htbd-grade-table tr.row-fail td {{
  color: #fca5a5 !important;
}}

/* Formula Box Dark Mode */
.dark .htbd-formula-box, body.dark .htbd-formula-box {{
  background: #0f172a !important;
  border-color: #334155 !important;
  color: #93c5fd !important;
}}

/* FAQ Cards Dark Mode */
.dark .htbd-faq-item, body.dark .htbd-faq-item {{
  background: #1e293b !important;
  border-color: #334155 !important;
}}
.dark .htbd-faq-item h3, body.dark .htbd-faq-item h3 {{
  color: #93c5fd !important;
}}
.dark .htbd-faq-item p, body.dark .htbd-faq-item p {{
  color: #cbd5e1 !important;
}}

/* Author Box Dark Mode */
.dark .htbd-author-box, body.dark .htbd-author-box {{
  background: #1e293b !important;
  border-color: #334155 !important;
  border-left-color: #3b82f6 !important;
}}
.dark .htbd-author-box h4, body.dark .htbd-author-box h4 {{
  color: #93c5fd !important;
}}
.dark .htbd-author-meta, body.dark .htbd-author-meta {{
  color: #94a3b8 !important;
}}
.dark .htbd-author-bio, body.dark .htbd-author-bio {{
  color: #cbd5e1 !important;
}}
</style>

<!-- ========================================================================== -->
<!-- INTERACTIVE WEB APPLICATION: NU ADVANCED CGPA CALCULATOR ENGINE           -->
<!-- ========================================================================== -->
<div id="htbd-nu-cgpa-app">

  <!-- App Header & Program Selector -->
  <div class="htbd-app-divider" style="text-align: center; margin-bottom: 25px; border-bottom: 2px solid #f1f5f9; padding-bottom: 20px;">
    <span class="htbd-app-badge" style="background: #e0e7ff; color: #3730a3; padding: 5px 14px; border-radius: 20px; font-size: 13.5px; font-weight: 600; display: inline-block; margin-bottom: 10px;">
      NATIONAL UNIVERSITY BANGLADESH • ACADEMIC SUITE
    </span>
    <h2 class="htbd-app-title" style="margin: 5px 0 10px 0; color: #0c2340; font-size: 26px; font-weight: 700;">
      জাতীয় বিশ্ববিদ্যালয় সিজিপিএ ক্যালকুলেটর ২০২৬
    </h2>
    <p class="htbd-app-subtitle" style="margin: 0; color: #64748b; font-size: 15px;">
      অনার্স, ডিগ্রি পাস ও মাস্টার্স শিক্ষার্থীদের জন্য আধুনিক, নির্ভুল ও তাৎক্ষণিক রেজাল্ট মূল্যায়ন ব্যবস্থা
    </p>

    <!-- Program Selector Pills -->
    <div style="display: flex; justify-content: center; gap: 10px; margin-top: 18px; flex-wrap: wrap;">
      <button type="button" class="htbd-prog-btn active" data-prog="honours">
        স্নাতক (সম্মান) অনার্স ৪ বছর
      </button>
      <button type="button" class="htbd-prog-btn" data-prog="degree">
        ডিগ্রি (পাস) ৩ বছর
      </button>
      <button type="button" class="htbd-prog-btn" data-prog="masters">
        মাস্টার্স ১/২ বছর
      </button>
    </div>
  </div>

  <!-- Master Mode Switcher Tabs -->
  <div class="htbd-app-divider" style="display: flex; gap: 8px; margin-bottom: 25px; border-bottom: 1px solid #e2e8f0; padding-bottom: 12px; overflow-x: auto;">
    <button type="button" class="htbd-tab-btn active" data-mode="mode-year">
      ইয়ার-ওয়াইজ সিজিপিএ
    </button>
    <button type="button" class="htbd-tab-btn" data-mode="mode-subject">
      বিষয়ভিত্তিক বিস্তারিত জিপিএ
    </button>
    <button type="button" class="htbd-tab-btn" data-mode="mode-target">
      টার্গেট ফার্স্ট ক্লাস প্ল্যানার
    </button>
    <button type="button" class="htbd-tab-btn" data-mode="mode-improvement">
      মানোন্নয়ন সিমুলেটর
    </button>
  </div>

  <!-- Main Grid Layout: Form Area (Left) & Live Dashboard (Right) -->
  <div class="htbd-calc-grid">

    <!-- LEFT COLUMN: MODE PANELS -->
    <div class="htbd-left-panel">

      <!-- ================= MODE 1: YEAR-WISE QUICK CGPA ================= -->
      <div id="panel-mode-year" class="htbd-mode-panel">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
          <h3 style="margin: 0; font-size: 18px; font-weight: 700;">
            বার্ষিক জিপিএ ইনপুট দিন
          </h3>
          <span style="font-size: 13px; color: #64748b;">ইনপুট বা স্লাইডার ব্যবহার করুন</span>
        </div>

        <div id="year-inputs-container" style="display: flex; flex-direction: column; gap: 14px;">
          <!-- Year 1 -->
          <div class="htbd-year-card" data-year="1">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
              <span class="htbd-year-title" style="font-weight: 700; color: #1e3a8a; font-size: 15px;">১ম বর্ষ (1st Year)</span>
              <div class="htbd-year-credit-lbl" style="font-size: 13px; color: #64748b;">
                ক্রেডিট: <input type="number" class="htbd-yr-credit" value="32" min="1" max="50" style="width: 52px; padding: 3px 6px; border: 1px solid #cbd5e1; border-radius: 4px; text-align: center;" />
              </div>
            </div>
            <div style="display: flex; align-items: center; gap: 12px;">
              <input type="range" class="htbd-yr-range" min="0.00" max="4.00" step="0.01" value="0.00" style="flex: 1; accent-color: #2563eb;" />
              <input type="number" class="htbd-yr-gpa" min="0.00" max="4.00" step="0.01" placeholder="0.00" style="width: 75px; padding: 6px 8px; border: 1px solid #94a3b8; border-radius: 6px; font-size: 16px; font-weight: 700; text-align: center;" />
            </div>
          </div>

          <!-- Year 2 -->
          <div class="htbd-year-card" data-year="2">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
              <span class="htbd-year-title" style="font-weight: 700; color: #1e3a8a; font-size: 15px;">২য় বর্ষ (2nd Year)</span>
              <div class="htbd-year-credit-lbl" style="font-size: 13px; color: #64748b;">
                ক্রেডিট: <input type="number" class="htbd-yr-credit" value="32" min="1" max="50" style="width: 52px; padding: 3px 6px; border: 1px solid #cbd5e1; border-radius: 4px; text-align: center;" />
              </div>
            </div>
            <div style="display: flex; align-items: center; gap: 12px;">
              <input type="range" class="htbd-yr-range" min="0.00" max="4.00" step="0.01" value="0.00" style="flex: 1; accent-color: #2563eb;" />
              <input type="number" class="htbd-yr-gpa" min="0.00" max="4.00" step="0.01" placeholder="0.00" style="width: 75px; padding: 6px 8px; border: 1px solid #94a3b8; border-radius: 6px; font-size: 16px; font-weight: 700; text-align: center;" />
            </div>
          </div>

          <!-- Year 3 -->
          <div class="htbd-year-card" data-year="3">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
              <span class="htbd-year-title" style="font-weight: 700; color: #1e3a8a; font-size: 15px;">৩য় বর্ষ (3rd Year)</span>
              <div class="htbd-year-credit-lbl" style="font-size: 13px; color: #64748b;">
                ক্রেডিট: <input type="number" class="htbd-yr-credit" value="32" min="1" max="50" style="width: 52px; padding: 3px 6px; border: 1px solid #cbd5e1; border-radius: 4px; text-align: center;" />
              </div>
            </div>
            <div style="display: flex; align-items: center; gap: 12px;">
              <input type="range" class="htbd-yr-range" min="0.00" max="4.00" step="0.01" value="0.00" style="flex: 1; accent-color: #2563eb;" />
              <input type="number" class="htbd-yr-gpa" min="0.00" max="4.00" step="0.01" placeholder="0.00" style="width: 75px; padding: 6px 8px; border: 1px solid #94a3b8; border-radius: 6px; font-size: 16px; font-weight: 700; text-align: center;" />
            </div>
          </div>

          <!-- Year 4 -->
          <div class="htbd-year-card" data-year="4">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
              <span class="htbd-year-title" style="font-weight: 700; color: #1e3a8a; font-size: 15px;">৪র্থ বর্ষ (4th Year)</span>
              <div class="htbd-year-credit-lbl" style="font-size: 13px; color: #64748b;">
                ক্রেডিট: <input type="number" class="htbd-yr-credit" value="32" min="1" max="50" style="width: 52px; padding: 3px 6px; border: 1px solid #cbd5e1; border-radius: 4px; text-align: center;" />
              </div>
            </div>
            <div style="display: flex; align-items: center; gap: 12px;">
              <input type="range" class="htbd-yr-range" min="0.00" max="4.00" step="0.01" value="0.00" style="flex: 1; accent-color: #2563eb;" />
              <input type="number" class="htbd-yr-gpa" min="0.00" max="4.00" step="0.01" placeholder="0.00" style="width: 75px; padding: 6px 8px; border: 1px solid #94a3b8; border-radius: 6px; font-size: 16px; font-weight: 700; text-align: center;" />
            </div>
          </div>
        </div>

        <div style="margin-top: 15px; display: flex; gap: 10px;">
          <button type="button" id="btn-reset-year" class="htbd-btn-secondary" style="flex: 1;">
            সব মুছে ফেলুন
          </button>
        </div>
      </div>

      <!-- ================= MODE 2: COURSE-WISE DETAILED GPA ================= -->
      <div id="panel-mode-subject" class="htbd-mode-panel" style="display: none;">
        <div style="margin-bottom: 16px;">
          <h3 style="margin: 0 0 6px 0; font-size: 18px; font-weight: 700;">
            বিষয়ভিত্তিক গ্রেড ইনপুট
          </h3>
          <p style="margin: 0; font-size: 13.5px; color: #64748b;">
            বিভাগ সিলেক্ট করে সরাসরি সিলেবাস লোড করুন অথবা রেজাল্ট কপি-পেস্ট করুন
          </p>
        </div>

        <!-- Syllabus Auto-Load Controls -->
        <div class="htbd-syllabus-box">
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin-bottom: 10px;">
            <div>
              <label class="htbd-syllabus-label" style="display: block; font-size: 13px; font-weight: 600; color: #0369a1; margin-bottom: 3px;">বিভাগ (Department)</label>
              <select id="sel-dept" style="width: 100%; padding: 6px 8px; border: 1px solid #7dd3fc; border-radius: 6px; font-size: 14px;">
                <option value="political_science">রাষ্ট্রবিজ্ঞান (Political Science)</option>
                <option value="english">ইংরেজি (English)</option>
                <option value="accounting">হিসাববিজ্ঞান (Accounting)</option>
                <option value="management">ব্যবস্থাপনা (Management)</option>
                <option value="economics">অর্থনীতি (Economics)</option>
                <option value="sociology">সমাজবিজ্ঞান (Sociology)</option>
                <option value="custom">অন্যান্য / কাস্টম বিষয়</option>
              </select>
            </div>
            <div>
              <label class="htbd-syllabus-label" style="display: block; font-size: 13px; font-weight: 600; color: #0369a1; margin-bottom: 3px;">শিক্ষাবর্ষ (Year)</label>
              <select id="sel-year" style="width: 100%; padding: 6px 8px; border: 1px solid #7dd3fc; border-radius: 6px; font-size: 14px;">
                <option value="1">১ম বর্ষ (1st Year)</option>
                <option value="2">২য় বর্ষ (2nd Year)</option>
                <option value="3">৩য় বর্ষ (3rd Year)</option>
                <option value="4">৪র্থ বর্ষ (4th Year)</option>
              </select>
            </div>
          </div>
          <div style="display: flex; gap: 8px;">
            <button type="button" id="btn-load-syllabus" style="flex: 1; background: #0284c7; color: #ffffff; border: none; padding: 7px 12px; border-radius: 6px; font-size: 13.5px; font-weight: 600; cursor: pointer; transition: 0.2s;">
              সিলেবাস অটো-লোড
            </button>
            <button type="button" id="btn-open-smart-paste" style="flex: 1; background: #0f766e; color: #ffffff; border: none; padding: 7px 12px; border-radius: 6px; font-size: 13.5px; font-weight: 600; cursor: pointer; transition: 0.2s;">
              স্মার্ট পেস্ট পার্সার
            </button>
          </div>
        </div>

        <!-- Smart Paste Modal Box (Hidden by default) -->
        <div id="smart-paste-box" class="htbd-smart-paste-box" style="display: none;">
          <h4 class="htbd-smart-paste-title" style="margin: 0 0 6px 0; font-size: 14.5px;">রেজাল্ট টেক্সট এখানে পেস্ট করুন:</h4>
          <p class="htbd-smart-paste-desc" style="margin: 0 0 8px 0; font-size: 12.5px; color: #64748b;">
            উদাহরণ: <code>221901 - A-, 221903 - B+, 221905 - A</code> অথবা সম্পূর্ণ রেজাল্ট টেবিলের কপি করা লেখা।
          </p>
          <textarea id="smart-paste-input" rows="3" placeholder="Paste result here..." style="width: 100%; box-sizing: border-box; padding: 8px; border: 1px solid #cbd5e1; border-radius: 6px; font-size: 13px; font-family: monospace;"></textarea>
          <div style="display: flex; justify-content: flex-end; gap: 8px; margin-top: 8px;">
            <button type="button" id="btn-cancel-paste" class="htbd-btn-secondary" style="padding: 6px 12px; font-size: 13px;">বাতিল</button>
            <button type="button" id="btn-parse-paste" style="background: #059669; color: #ffffff; border: none; padding: 6px 14px; border-radius: 4px; font-size: 13px; font-weight: 600; cursor: pointer;">পার্স ও অটো-ফিল</button>
          </div>
        </div>

        <!-- Dynamic Course Table/Container -->
        <div class="htbd-course-header">
          <div>কোর্স কোড ও নাম</div>
          <div style="text-align: center;">ক্রেডিট</div>
          <div style="text-align: center;">লেটার গ্রেড</div>
          <div style="text-align: center;">পয়েন্ট (GP)</div>
          <div style="text-align: center;">মুছুন</div>
        </div>
        <div id="courses-container" style="display: flex; flex-direction: column; gap: 8px; margin-bottom: 14px;">
          <!-- Course Rows injected dynamically via JS -->
        </div>

        <div style="display: flex; gap: 8px;">
          <button type="button" id="btn-add-course" style="flex: 1; background: #2563eb; color: #ffffff; border: none; padding: 8px 12px; border-radius: 6px; font-size: 14px; font-weight: 600; cursor: pointer; transition: 0.2s;">
            + বিষয় যোগ করুন
          </button>
          <button type="button" id="btn-reset-courses" class="htbd-btn-secondary" style="font-size: 14px;">
            রিসেট
          </button>
        </div>
      </div>

      <!-- ================= MODE 3: TARGET FIRST CLASS PLANNER ================= -->
      <div id="panel-mode-target" class="htbd-mode-panel" style="display: none;">
        <h3 style="margin: 0 0 10px 0; font-size: 18px; font-weight: 700;">
          টার্গেট ফার্স্ট ক্লাস (৩.০০) প্ল্যানার
        </h3>
        <p style="margin: 0 0 16px 0; font-size: 13.5px; color: #64748b;">
          আপনার বর্তমান সিজিপিএ দিন, টুল হিসাব করে বলে দেবে বাকি বর্ষগুলোতে গড়ে কত জিপিএ লাগবে।
        </p>

        <div style="display: flex; flex-direction: column; gap: 14px;">
          <div>
            <label style="display: block; font-size: 14px; font-weight: 600; margin-bottom: 5px;">
              আপনি কোন বর্ষ পর্যন্ত ফলাফল পেয়েছেন?
            </label>
            <select id="target-completed-years" style="width: 100%; padding: 8px; border: 1px solid #cbd5e1; border-radius: 6px; font-size: 15px;">
              <option value="1">১ম বর্ষের ফলাফল পেয়েছি (বাকি ৩টি বর্ষ)</option>
              <option value="2" selected>২য় বর্ষের ফলাফল পেয়েছি (বাকি ২টি বর্ষ)</option>
              <option value="3">৩য় বর্ষের ফলাফল পেয়েছি (বাকি শেষ বর্ষ)</option>
            </select>
          </div>

          <div>
            <label style="display: block; font-size: 14px; font-weight: 600; margin-bottom: 5px;">
              আপনার বর্তমান অর্জিত CGPA কত?
            </label>
            <input type="number" id="target-current-cgpa" min="2.00" max="4.00" step="0.01" value="2.75" style="width: 100%; box-sizing: border-box; padding: 8px 12px; border: 1px solid #94a3b8; border-radius: 6px; font-size: 16px; font-weight: 700;" />
          </div>

          <div>
            <label style="display: block; font-size: 14px; font-weight: 600; margin-bottom: 5px;">
              আপনার কাঙ্ক্ষিত টার্গেট কত?
            </label>
            <select id="target-goal-cgpa" style="width: 100%; padding: 8px; border: 1px solid #cbd5e1; border-radius: 6px; font-size: 15px; font-weight: 600;">
              <option value="3.00" selected>৩.০০ — First Class (১ম শ্রেণি)</option>
              <option value="3.25">৩.২৫ — B+ গ্রেড (উচ্চ সম্মান)</option>
              <option value="3.50">৩.৫০ — A- গ্রেড (অসাধারণ)</option>
            </select>
          </div>

          <!-- Target Output Card -->
          <div id="target-result-card" class="htbd-target-card">
            <div class="htbd-target-label" style="font-size: 14px; color: #475569; margin-bottom: 4px;">বাকি বর্ষগুলোতে প্রয়োজনীয় গড় জিপিএ:</div>
            <div id="target-req-gpa" style="font-size: 28px; font-weight: 800; color: #2563eb;">3.25</div>
            <div id="target-badge" class="htbd-badge htbd-target-easy" style="margin-top: 6px; font-size: 13px; padding: 4px 12px;">
              বাস্তবসম্মত ও অর্জনযোগ্য
            </div>
            <p id="target-advice" style="margin: 10px 0 0 0; font-size: 13px; line-height: 1.6; color: #334155;">
              বাকি বর্ষগুলোতে মনোযোগ দিলে অনায়াসেই আপনি ৩.০০ বা ১ম শ্রেণি অর্জন করতে সক্ষম হবেন।
            </p>
          </div>
        </div>
      </div>

      <!-- ================= MODE 4: IMPROVEMENT SIMULATOR ================= -->
      <div id="panel-mode-improvement" class="htbd-mode-panel" style="display: none;">
        <h3 style="margin: 0 0 10px 0; font-size: 18px; font-weight: 700;">
          মানোন্নয়ন (Improvement) সিমুলেটর
        </h3>
        <p style="margin: 0 0 16px 0; font-size: 13.5px; color: #64748b;">
          সি বা ডি পাওয়া বিষয়ে মানোন্নয়ন দিলে সিজিপিএ কতটুকু লাফিয়ে বাড়বে তা যাচাই করুন।
        </p>

        <div style="display: flex; flex-direction: column; gap: 12px;">
          <div>
            <label style="display: block; font-size: 13.5px; font-weight: 600; margin-bottom: 4px;">
              বর্তমান বার্ষিক জিপিএ লিখুন:
            </label>
            <input type="number" id="imp-current-gpa" min="0.00" max="4.00" step="0.01" value="2.65" style="width: 100%; box-sizing: border-box; padding: 8px 12px; border: 1px solid #94a3b8; border-radius: 6px; font-size: 15px; font-weight: 700;" />
          </div>

          <div class="htbd-imp-box">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
              <span style="font-size: 14px; font-weight: 700; color: #1e3a8a;">মানোন্নয়ন পরীক্ষার বিষয়সমূহ:</span>
              <span style="font-size: 12px; color: #64748b;">(সরাসরি পয়েন্ট ইনপুট দিন)</span>
            </div>

            <!-- Column Header -->
            <div class="htbd-imp-header">
              <div>কোর্সের নাম</div>
              <div style="text-align: center;">পূর্বের পয়েন্ট (GP)</div>
              <div style="text-align: center;">টার্গেট পয়েন্ট (GP)*</div>
              <div style="text-align: center;">মুছুন</div>
            </div>
            
            <div id="imp-courses-list" style="display: flex; flex-direction: column; gap: 8px;">
              <!-- Dynamic Improvement Course Rows -->
            </div>

            <div style="margin-top: 10px; display: flex; gap: 8px;">
              <button type="button" id="btn-add-imp-course" style="flex: 1; background: #f1f5f9; color: #1e3a8a; border: 1px dashed #93c5fd; padding: 7px 10px; border-radius: 6px; font-size: 13px; font-weight: 600; cursor: pointer; transition: 0.2s;">
                + আরেকটি বিষয় যোগ করুন
              </button>
            </div>
            <div style="font-size: 11.5px; color: #64748b; margin-top: 8px; line-height: 1.5;">*এনইউ নিয়ম অনুযায়ী ইমপ্রুভমেন্টে সর্বোচ্চ B+ (৩.২৫) পর্যন্ত গণনা করা হয়। আপনি সরাসরি আপনার প্রত্যাশিত ফ্র্যাকশনাল বা পূর্ণ গ্রেড পয়েন্ট (যেমন: ৩.২৫, ৩.১০, ২.৮৫ ইত্যাদি) টাইপ করতে পারেন।</div>
          </div>

          <!-- Improvement Output -->
          <div class="htbd-imp-result-box">
            <div style="display: flex; justify-content: space-between; align-items: baseline;">
              <div>
                <span class="htbd-imp-res-label" style="font-size: 13px; color: #065f46; font-weight: 600;">নতুন সম্ভাব্য জিপিএ:</span>
                <div id="imp-new-gpa" style="font-size: 26px; font-weight: 800; color: #059669;">2.65</div>
              </div>
              <div style="text-align: right;">
                <span class="htbd-imp-res-label" style="font-size: 12px; color: #065f46; font-weight: 600;">সম্ভাব্য বৃদ্ধি:</span>
                <div id="imp-delta-gpa" style="font-size: 18px; font-weight: 700; color: #047857;">+0.00 GPA</div>
              </div>
            </div>
          </div>
        </div>
      </div>

    </div>

    <!-- RIGHT COLUMN: UNIFIED LIVE DASHBOARD & ANALYTICS -->
    <div class="htbd-right-panel">
      
      <div>
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
          <h3 style="margin: 0; font-size: 18px; font-weight: 700;">ফলাফল ড্যাশবোর্ড</h3>
          <span id="dash-program-badge" style="background: #eff6ff; color: #1e40af; padding: 3px 10px; border-radius: 12px; font-size: 12.5px; font-weight: 600;">স্নাতক (সম্মান)</span>
        </div>

        <!-- Speedometer / Circular Gauge SVG -->
        <div style="text-align: center; margin: 10px 0 8px 0;">
          <div style="position: relative; width: 135px; height: 135px; margin: 0 auto;">
            <svg viewBox="0 0 120 120" style="width: 100%; height: 100%; transform: rotate(-90deg);">
              <!-- Background Circle -->
              <circle class="dash-gauge-track" cx="60" cy="60" r="50" fill="none" stroke="#f1f5f9" stroke-width="12" />
              <!-- Progress Circle -->
              <circle id="dash-gauge-circle" cx="60" cy="60" r="50" fill="none" stroke="#2563eb" stroke-width="12" stroke-dasharray="314.16" stroke-dashoffset="314.16" stroke-linecap="round" style="transition: stroke-dashoffset 0.5s ease, stroke 0.3s ease;" />
            </svg>
            <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; display: flex; flex-direction: column; justify-content: center; align-items: center;">
              <span id="dash-cgpa-val" style="font-size: 28px; font-weight: 800; color: #0f172a; line-height: 1;">0.00</span>
              <span class="dash-gauge-subtext" style="font-size: 11.5px; color: #64748b; font-weight: 600; margin-top: 3px;">আউট অব ৪.০০</span>
            </div>
          </div>
        </div>

        <!-- Division & Status Badge -->
        <div style="text-align: center; margin-bottom: 16px;">
          <div id="dash-division-badge" class="htbd-badge htbd-badge-empty">
            ফলাফল দেখতে ইনপুট দিন
          </div>
        </div>

        <!-- Metrics Pills -->
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-bottom: 20px;">
          <div class="htbd-metric-pill">
            <div class="htbd-metric-lbl" style="font-size: 12px; color: #64748b;">মোট অর্জিত ক্রেডিট</div>
            <div id="dash-total-credits" class="htbd-metric-val" style="font-size: 18px; font-weight: 700; color: #1e293b;">0</div>
          </div>
          <div class="htbd-metric-pill">
            <div class="htbd-metric-lbl" style="font-size: 12px; color: #64748b;">মোট গ্রেড পয়েন্ট</div>
            <div id="dash-total-points" class="htbd-metric-val" style="font-size: 18px; font-weight: 700; color: #1e293b;">0.00</div>
          </div>
        </div>

        <!-- Progression Trend Curve (SVG Canvas) -->
        <div class="htbd-trend-card">
          <div style="font-size: 13px; font-weight: 600; margin-bottom: 8px; display: flex; justify-content: space-between;">
            <span class="htbd-trend-title" style="color: #475569;">বর্ষভিত্তিক অগ্রগতি গ্রাফ</span>
            <span style="font-size: 11px; color: #94a3b8;">১ম → ৪র্থ বর্ষ</span>
          </div>
          <div style="height: 60px; width: 100%;">
            <svg id="dash-trend-svg" viewBox="0 0 200 60" style="width: 100%; height: 100%; overflow: visible;">
              <line class="dash-trend-axis" x1="10" y1="50" x2="190" y2="50" stroke="#cbd5e1" stroke-width="1" />
              <polyline id="dash-trend-line" fill="none" stroke="#3b82f6" stroke-width="2.5" points="20,50 70,50 120,50 170,50" />
              <circle id="p1" cx="20" cy="50" r="3.5" fill="#1e40af" />
              <circle id="p2" cx="70" cy="50" r="3.5" fill="#1e40af" />
              <circle id="p3" cx="120" cy="50" r="3.5" fill="#1e40af" />
              <circle id="p4" cx="170" cy="50" r="3.5" fill="#1e40af" />
            </svg>
          </div>
        </div>
      </div>

      <!-- Action Buttons -->
      <div style="display: flex; flex-direction: column; gap: 8px;">
        <button type="button" id="btn-print-transcript" style="background: #1e3a8a; color: #ffffff; border: none; padding: 12px; border-radius: 8px; font-size: 15px; font-weight: 700; cursor: pointer; display: flex; align-items: center; justify-content: center; gap: 8px; transition: all 0.2s ease; box-shadow: 0 4px 12px rgba(30,58,138,0.2);">
          <svg style="width: 18px; height: 18px; fill: currentColor;" viewBox="0 0 24 24"><path d="M19 8H5c-1.66 0-3 1.34-3 3v6h4v4h12v-4h4v-6c0-1.66-1.34-3-3-3zm-3 11H8v-5h8v5zm3-7c-.55 0-1-.45-1-1s.45-1 1-1 1 .45 1 1-.45 1-1 1zm-1-9H6v4h12V3z"/></svg> অফিসিয়াল ট্রান্সক্রিপ্ট প্রিন্ট / PDF
        </button>
        <button type="button" id="btn-copy-summary" class="htbd-btn-secondary" style="padding: 9px; font-size: 14px; text-align: center;">
          রেজাল্ট সামারি কপি করুন
        </button>
      </div>

    </div>

  </div>

</div>

<!-- ========================================================================== -->
<!-- INTERACTIVE LIVE PREVIEW MODAL: OFFICIAL A4 TRANSCRIPT & PDF CUSTOMIZER   -->
<!-- ========================================================================== -->
<div id="htbd-transcript-modal">
  <div class="htbd-modal-wrapper">
    <!-- Modal Header -->
    <div class="htbd-modal-header">
      <div style="display: flex; align-items: center; gap: 10px;">
        <svg style="width: 24px; height: 24px; fill: #ffffff;" viewBox="0 0 24 24"><path d="M5 13.18v4L12 21l7-3.82v-4L12 17l-7-3.82zM12 3L1 9l11 6 9-4.91V17h2V9L12 3z"/></svg>
        <div>
          <h3 style="margin: 0; font-size: 17px; font-weight: 700; color: #ffffff;">জাতীয় বিশ্ববিদ্যালয় প্রাতিষ্ঠানিক ট্রান্সক্রিপ্ট প্রিভিউ</h3>
          <div style="font-size: 12px; color: #bfdbfe; margin-top: 2px;">তথ্য কাস্টমাইজ করুন এবং ১-পাতা A4 ট্রান্সক্রিপ্ট প্রিন্ট বা PDF সেভ করুন</div>
        </div>
      </div>
      <button type="button" id="btn-close-modal" class="btn-modal-close" title="বন্ধ করুন"><svg style="width: 14px; height: 14px; fill: currentColor; vertical-align: middle;" viewBox="0 0 24 24"><path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"/></svg></button>
    </div>

    <!-- Live Customizer Toolbar -->
    <div class="htbd-modal-toolbar">
      <div class="htbd-modal-input-group">
        <label class="htbd-modal-label">শিক্ষার্থীর নাম (ঐচ্ছিক):</label>
        <input type="text" id="modal-inp-name" class="htbd-modal-input" placeholder="আপনার নাম লিখুন..." />
      </div>
      <div class="htbd-modal-input-group">
        <label class="htbd-modal-label">কলেজ / শিক্ষাপ্রতিষ্ঠান (ঐচ্ছিক):</label>
        <input type="text" id="modal-inp-college" class="htbd-modal-input" placeholder="কলেজের নাম লিখুন..." />
      </div>
      <div class="htbd-modal-input-group">
        <label class="htbd-modal-label">সেশন / রেজিস্ট্রেশন নং (ঐচ্ছিক):</label>
        <input type="text" id="modal-inp-session" class="htbd-modal-input" placeholder="যেমন: ২০২০-২১ / ১৮..." />
      </div>
      <div>
        <button type="button" id="btn-trigger-pdf-print" class="btn-trigger-print">
          <svg style="width: 16px; height: 16px; fill: currentColor; vertical-align: middle; margin-right: 6px;" viewBox="0 0 24 24"><path d="M19 8H5c-1.66 0-3 1.34-3 3v6h4v4h12v-4h4v-6c0-1.66-1.34-3-3-3zm-3 11H8v-5h8v5zm3-7c-.55 0-1-.45-1-1s.45-1 1-1 1 .45 1 1-.45 1-1 1zm-1-9H6v4h12V3z"/></svg>প্রিন্ট / PDF ডাউনলোড (১ পৃষ্ঠা)
        </button>
      </div>
    </div>

    <!-- Live Preview Sheet Viewport -->
    <div class="htbd-preview-scroll">
      
      <!-- ================= THE PURE A4 CERTIFICATE PAPER ================= -->
      <div id="htbd-certificate-paper">
        <div class="htbd-cert-inner-frame">

          <!-- Background Watermark (Ultra-Subtle Unofficial Notice) -->
          <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%) rotate(-25deg); font-size: 38px; font-weight: 800; color: #0c2340; opacity: 0.035; pointer-events: none; z-index: 1; white-space: nowrap; user-select: none; letter-spacing: 4px; text-transform: uppercase;">
            HELPTRICKBD • UNOFFICIAL STUDENT COPY
          </div>

          <!-- Document Header -->
          <div style="position: relative; z-index: 2; display: flex; align-items: center; justify-content: space-between; border-bottom: 2px solid #1e3a8a; padding-bottom: 12px; margin-bottom: 12px;">
            <!-- Left: NU Official Vector Monogram / Emblem -->
            <div style="width: 70px; height: 70px; flex-shrink: 0; text-align: center;">
              <svg width="70" height="70" viewBox="0 0 100 100" style="width: 70px !important; height: 70px !important; display: block; margin: 0 auto;">
                <circle cx="50" cy="50" r="47" fill="#1e3a8a" />
                <circle cx="50" cy="50" r="43" fill="#ffffff" stroke="#b45309" stroke-width="1.5" />
                <circle cx="50" cy="50" r="33" fill="#f8fafc" stroke="#1e3a8a" stroke-width="1.5" />
                <!-- Sunburst -->
                <path d="M50 19 L50 25 M38 23 L41 27 M62 23 L59 27 M30 31 L35 33 M70 31 L65 33" stroke="#d97706" stroke-width="1.8" stroke-linecap="round" />
                <circle cx="50" cy="38" r="11" fill="#dc2626" />
                <!-- Open Book -->
                <path d="M28 58 Q50 48 50 64 Q50 48 72 58 L72 68 Q50 58 50 74 Q50 58 28 68 Z" fill="#1e3a8a" />
                <path d="M30 60 Q50 50 50 66 L50 72 Q50 56 30 66 Z" fill="#ffffff" opacity="0.9" />
                <path d="M70 60 Q50 50 50 66 L50 72 Q50 56 70 66 Z" fill="#ffffff" opacity="0.9" />
                <line x1="50" y1="50" x2="50" y2="74" stroke="#b45309" stroke-width="1.5" />
                <!-- Rice Sheaves Base -->
                <path d="M28 72 Q50 84 72 72" fill="none" stroke="#15803d" stroke-width="2.5" stroke-linecap="round" />
                <path d="M24 66 Q26 75 34 80 M76 66 Q74 75 66 80" fill="none" stroke="#15803d" stroke-width="1.5" stroke-linecap="round" />
                <path d="M36 82 Q50 86 64 82 L60 87 Q50 89 40 87 Z" fill="#b45309" />
              </svg>
            </div>

            <!-- Center: University Identification & Document Title -->
            <div style="text-align: center; flex: 1; padding: 0 10px;">
              <div style="font-size: 18px; font-weight: 800; color: #0c2340; letter-spacing: 0.5px; line-height: 1.2;">জাতীয় বিশ্ববিদ্যালয় গ্রেডিং সিস্টেম</div>
              <div style="font-size: 12.5px; font-weight: 700; color: #1e3a8a; letter-spacing: 0.6px; margin-top: 2px;">NATIONAL UNIVERSITY GRADING SYSTEM • BANGLADESH</div>
              <div style="font-size: 11px; color: #475569; margin-top: 2px;">হেল্পট্রিকবিডি অনলাইন শিক্ষা প্ল্যাটফর্ম • HelpTrickBD.com EduTools</div>
              <div style="display: inline-block; background: #fef2f2; color: #b91c1c; border: 1px solid #fecaca; padding: 3px 14px; border-radius: 4px; font-size: 11px; font-weight: 700; margin-top: 4px; letter-spacing: 0.5px;">
                অনলাইন সিজিপিএ মূল্যায়ন রেকর্ড (শিক্ষার্থী কপি — অফিসিয়াল ট্রান্সক্রিপ্ট নয়)
              </div>
            </div>

            <!-- Right: Official Document Verification & Serial Box -->
            <div style="width: 145px; flex-shrink: 0; text-align: right;">
              <div style="border: 1px dashed #f59e0b; border-radius: 4px; padding: 5px 8px; background: #fffbeb; font-size: 9.5px; line-height: 1.35; text-align: left;">
                <div style="font-weight: 800; color: #b45309; font-size: 9px; text-transform: uppercase;">UNOFFICIAL REPORT</div>
                <div style="font-size: 8.5px; color: #dc2626; font-weight: 700;">মূল সনদ বা ট্রান্সক্রিপ্ট নয়</div>
                <div id="cert-ref-no" style="font-family: monospace; font-size: 9px; color: #0f172a; margin-top: 2px;">Ref: HTBD-NU-2026-89412</div>
                <div id="cert-issue-date" style="color: #475569; font-size: 9px; margin-top: 1px;">তারিখ: ৩ অক্টোবর, ২০২৬</div>
              </div>
            </div>
          </div>

          <!-- Student & Academic Examination Profile Matrix -->
          <div style="position: relative; z-index: 2; margin-bottom: 12px;">
            <table style="width: 100%; border-collapse: collapse; font-size: 12px; color: #0c2340;">
              <tr>
                <td style="padding: 4px 8px; border: 1px solid #cbd5e1; background: #f8fafc; width: 17%; font-weight: 700; color: #334155;">শিক্ষার্থীর নাম:</td>
                <td style="padding: 4px 8px; border: 1px solid #cbd5e1; width: 33%; font-weight: 700; color: #0c2340;"><span id="cert-student-name">পরীক্ষার্থী (Examinee)</span></td>
                <td style="padding: 4px 8px; border: 1px solid #cbd5e1; background: #f8fafc; width: 20%; font-weight: 700; color: #334155;">মোট অর্জিত ক্রেডিট:</td>
                <td style="padding: 4px 8px; border: 1px solid #cbd5e1; width: 30%; font-weight: 700; color: #0c2340;"><span id="cert-total-credits">128</span> Credits</td>
              </tr>
              <tr>
                <td style="padding: 4px 8px; border: 1px solid #cbd5e1; background: #f8fafc; font-weight: 700; color: #334155;">কলেজ / প্রতিষ্ঠান:</td>
                <td style="padding: 4px 8px; border: 1px solid #cbd5e1; font-weight: 600; color: #0c2340;"><span id="cert-college-name">জাতীয় বিশ্ববিদ্যালয় অধিভুক্ত কলেজ</span></td>
                <td style="padding: 4px 8px; border: 1px solid #cbd5e1; background: #f8fafc; font-weight: 700; color: #334155;">মোট গ্রেড পয়েন্ট:</td>
                <td style="padding: 4px 8px; border: 1px solid #cbd5e1; font-weight: 700; color: #0c2340;"><span id="cert-total-points">0.00</span></td>
              </tr>
              <tr>
                <td style="padding: 4px 8px; border: 1px solid #cbd5e1; background: #f8fafc; font-weight: 700; color: #334155;">সেশন / রেজি. নং:</td>
                <td style="padding: 4px 8px; border: 1px solid #cbd5e1; font-weight: 600; color: #0c2340;"><span id="cert-reg-session">২০২০-২১ (নিয়মিত)</span></td>
                <td style="padding: 4px 8px; border: 1px solid #cbd5e1; background: #eff6ff; font-weight: 800; color: #1e3a8a;">চূড়ান্ত অর্জিত CGPA:</td>
                <td style="padding: 4px 8px; border: 1px solid #cbd5e1; background: #eff6ff; font-size: 14.5px; font-weight: 800; color: #1e3a8a;"><span id="cert-cgpa">0.00</span> <span style="font-size: 10.5px; font-weight: normal; color: #64748b;">(আউট অব ৪.০০)</span></td>
              </tr>
              <tr>
                <td style="padding: 4px 8px; border: 1px solid #cbd5e1; background: #f8fafc; font-weight: 700; color: #334155;">ডিগ্রি ও শিক্ষাবর্ষ:</td>
                <td style="padding: 4px 8px; border: 1px solid #cbd5e1; font-weight: 700; color: #0c2340;"><span id="cert-program-name">স্নাতক (সম্মান) চার বছর</span></td>
                <td style="padding: 4px 8px; border: 1px solid #cbd5e1; background: #f8fafc; font-weight: 700; color: #334155;">একাডেমিক শ্রেণি/ক্লাস:</td>
                <td style="padding: 4px 8px; border: 1px solid #cbd5e1; font-weight: 800; color: #15803d;"><span id="cert-division">-</span></td>
              </tr>
            </table>
          </div>

          <!-- Official NU 10-Tier Grading Scale Key (Compact Institutional Strip) -->
          <div style="position: relative; z-index: 2; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 4px; padding: 4px 6px; margin-bottom: 12px; font-size: 9.5px; color: #334155; line-height: 1.35; text-align: center;">
            <strong style="color: #0c2340;">NU Grading Scale Key:</strong>
            80-100% <strong>A+</strong> (4.00) | 75-79% <strong>A</strong> (3.75) | 70-74% <strong>A-</strong> (3.50) | 65-69% <strong>B+</strong> (3.25) | 60-64% <strong>B</strong> (3.00) | 55-59% <strong>B-</strong> (2.75) | 50-54% <strong>C+</strong> (2.50) | 45-49% <strong>C</strong> (2.25) | 40-44% <strong>D</strong> (2.00) | 0-39% <strong>F</strong> (0.00)
          </div>

          <!-- Examination Performance Table -->
          <div style="position: relative; z-index: 2; margin-bottom: 12px;">
            <table style="width: 100%; border-collapse: collapse; font-size: 12px; color: #0c2340;">
              <thead>
                <tr style="background: #1e3a8a; color: #ffffff; font-size: 11.5px;">
                  <th style="border: 1px solid #1e3a8a; padding: 5px 6px; text-align: center; width: 42px;">ক্রমিক</th>
                  <th style="border: 1px solid #1e3a8a; padding: 5px 8px; text-align: left;">শিক্ষাবর্ষ / কোর্স বিবরণ</th>
                  <th style="border: 1px solid #1e3a8a; padding: 5px 6px; text-align: center; width: 80px;">ক্রেডিট ঘণ্টা</th>
                  <th style="border: 1px solid #1e3a8a; padding: 5px 6px; text-align: center; width: 95px;">লেটার গ্রেড</th>
                  <th style="border: 1px solid #1e3a8a; padding: 5px 6px; text-align: center; width: 85px;">পয়েন্ট (GP)</th>
                  <th style="border: 1px solid #1e3a8a; padding: 5px 6px; text-align: center; width: 90px;">মোট পয়েন্ট</th>
                </tr>
              </thead>
              <tbody id="cert-table-body">
                <!-- Injected Dynamically via JS -->
              </tbody>
              <tfoot>
                <tr style="background: #f1f5f9; font-weight: 800; border-top: 2px solid #0c2340; border-bottom: 2px solid #0c2340; font-size: 12px;">
                  <td colspan="2" style="border: 1px solid #cbd5e1; padding: 6px 8px; text-align: right; color: #0c2340;">সর্বমোট ফলাফল সারসংক্ষেপ:</td>
                  <td id="cert-foot-credits" style="border: 1px solid #cbd5e1; padding: 6px 6px; text-align: center; color: #0c2340;">128</td>
                  <td style="border: 1px solid #cbd5e1; padding: 6px 6px; text-align: center; color: #1e3a8a;">-</td>
                  <td id="cert-foot-cgpa" style="border: 1px solid #cbd5e1; padding: 6px 6px; text-align: center; color: #1e3a8a; font-size: 13px;">0.00</td>
                  <td id="cert-foot-points" style="border: 1px solid #cbd5e1; padding: 6px 6px; text-align: center; color: #0c2340;">0.00</td>
                </tr>
              </tfoot>
            </table>
          </div>

          <!-- Official Sign-off & Verification Footer -->
          <div style="position: relative; z-index: 2; display: flex; justify-content: space-between; align-items: center; margin-top: 15px; padding-top: 12px; border-top: 1px dashed #cbd5e1;">
            <!-- Left: Platform Signature & Security Hash -->
            <div style="font-size: 10px; color: #475569; line-height: 1.45; width: 33%;">
              উৎস প্ল্যাটফর্ম: <strong>HelpTrickBD.com</strong><br />
              টুল: <strong>NU CGPA Calculator 2026</strong><br />
              স্ট্যাটাস: <span style="color: #0369a1; font-weight: bold;">শিক্ষার্থী ব্যক্তিগত রেকর্ড (অনানুষ্ঠানিক)</span>
            </div>

            <!-- Center: Embossed Official Seal Stamp (SVG) -->
            <div style="text-align: center; width: 33%;">
              <div style="display: inline-block; border: 2px dashed #0284c7; border-radius: 50%; width: 70px; height: 70px; padding: 2px; box-sizing: border-box;">
                <div style="border: 1px solid #0284c7; border-radius: 50%; width: 100%; height: 100%; display: flex; flex-direction: column; align-items: center; justify-content: center; font-size: 6.5px; font-weight: 700; color: #0369a1; text-transform: uppercase; line-height: 1.15;">
                  <span>HELPTRICKBD</span>
                  <span style="font-size: 7.5px; color: #b45309; letter-spacing: 0.5px;">- ONLINE -</span>
                  <span>CALCULATOR</span>
                  <span style="font-size: 5.5px; color: #15803d; letter-spacing: 0.5px;">STUDENT COPY</span>
                </div>
              </div>
            </div>

            <!-- Right: Auto-Generated Notice (No Signature) -->
            <div style="text-align: center; width: 33%;">
              <div style="border: 1px dashed #cbd5e1; border-radius: 6px; padding: 6px 8px; background: #f8fafc; font-size: 10px; line-height: 1.4; color: #475569;">
                <div style="font-weight: 700; color: #b91c1c; font-size: 10px;">কম্পিউটার অটো-জেনারেটেড কপি</div>
                <div style="font-weight: 600; color: #1e3a8a; font-size: 9px; margin-top: 1px;">HelpTrickBD.com সিস্টেম দ্বারা প্রস্তুতকৃত</div>
                <div style="font-size: 8px; color: #64748b; margin-top: 2px;">(অনলাইন মূল্যায়ন — কোনো স্বাক্ষরের প্রয়োজন নেই)</div>
              </div>
            </div>
          </div>

          <!-- Bottom Legal & Ordinance Disclaimer -->
          <div style="position: relative; z-index: 2; margin-top: 10px; font-size: 9.5px; color: #334155; line-height: 1.45; text-align: center; border: 1px solid #fecaca; background: #fef2f2; border-radius: 6px; padding: 7px 12px;">
            <strong style="color: #b91c1c;">[জরুরি সতর্কবার্তা ও আইনি নোটিশ]:</strong> এই ফলাফল বিবরণীটি শিক্ষার্থীদের ব্যক্তিগত হিসাব ও সিজিপিএ পর্যালোচনার সুবিধার্থে <strong>HelpTrickBD.com</strong>-এর স্বয়ংক্রিয় অনলাইন ক্যালকুলেটর দ্বারা প্রস্তুতকৃত একটি অনানুষ্ঠানিক (Unofficial) কপি। এটি জাতীয় বিশ্ববিদ্যালয় গাজীপুর কর্তৃক ইস্যুকৃত কোনো মূল সনদ বা অফিসিয়াল ট্রান্সক্রিপ্ট নয়। সরকারি/বেসরকারি চাকরি, উচ্চশিক্ষা বা পাসপোর্ট আবেদনের ক্ষেত্রে জাতীয় বিশ্ববিদ্যালয় পরীক্ষা নিয়ন্ত্রণ দপ্তর কর্তৃক ইস্যুকৃত মূল সনদ ও সিলমোহরযুক্ত ট্রান্সক্রিপ্টই একমাত্র প্রযোজ্য ও আইনগতভাবে গ্রহণযোগ্য।
          </div>

        </div>
      </div>
      <!-- ================= END CERTIFICATE PAPER ================= -->

    </div>
  </div>
</div>

<!-- ========================================================================== -->
<!-- COMPREHENSIVE ACADEMIC CONTENT & SEO SHIELD (1,500+ WORDS)                 -->
<!-- ========================================================================== -->

<h2 class="htbd-content-h2" style="font-family: 'SolaimanLipi', sans-serif; color: #0c2340; font-size: 24px; font-weight: 700; margin: 40px 0 18px 0; border-left: 5px solid #1e3a8a; padding-left: 14px;">
জাতীয় বিশ্ববিদ্যালয় সিজিপিএ ক্যালকুলেটর কী ও কেন এটি ব্যবহার করবেন?
</h2>
<p style="font-family: 'SolaimanLipi', sans-serif; font-size: 17px; line-height: 1.85; color: #1e293b; margin-bottom: 20px;">
জাতীয় বিশ্ববিদ্যালয়ের চার বছর মেয়াদি স্নাতক (সম্মান), তিন বছর মেয়াদি ডিগ্রি (পাস) এবং এক বা দুই বছর মেয়াদি মাস্টার্স পরীক্ষায় গ্রেডিং পদ্ধতি চালু হওয়ার পর থেকে শিক্ষার্থীদের ফলাফল মূল্যায়নে মৌলিক পরিবর্তন এসেছে। সনাতন শতকরা নম্বরের পরিবর্তে এখন প্রতিটি কোর্সে গ্রেড পয়েন্ট (GP) এবং বছর শেষে গ্রেড পয়েন্ট এভারেজ (GPA) হিসাব করা হয়। চার বছরের সমস্ত কোর্সের সমন্বয়ে তৈরি হয় ফাইনাল কিউমুলেটিভ গ্রেড পয়েন্ট এভারেজ বা সিজিপিএ (CGPA)।
</p>
<p style="font-family: 'SolaimanLipi', sans-serif; font-size: 17px; line-height: 1.85; color: #1e293b; margin-bottom: 20px;">
অনেক শিক্ষার্থী মনে করেন, চার বছরের জিপিএ সাধারণ যোগ করে চার দিয়ে ভাগ করলেই বুঝি সিজিপিএ পাওয়া যায়। এটি একটি মারাত্মক ভুল ধারণা! কারণ জাতীয় বিশ্ববিদ্যালয়ের প্রতিটি কোর্সের ক্রেডিট সমান নয়। কোনো কোর্স ৪ ক্রেডিটের (১০০ নম্বর), কোনো কোর্স ২ ক্রেডিটের (৫০ নম্বর) আবার ব্যবহারিক ও মৌখিক পরীক্ষার ক্রেডিট ভিন্ন হয়ে থাকে। ক্রেডিট-ওয়েটেড পদ্ধতি অনুসরণ না করে হিসাব করলে ফলাফলে বড় ধরনের গরমিল দেখা দেয়। হেল্পট্রিকবিডির এই ক্যালকুলেটরটি জাতীয় বিশ্ববিদ্যালয়ের অফিসিয়াল একাডেমিক অর্ডিন্যান্স অনুযায়ী <strong>ক্রেডিট-ওয়েটেড এভারেজ ফর্মুলা</strong> ব্যবহার করে স্বয়ংক্রিয়ভাবে শতভাগ নির্ভুল ফলাফল প্রদর্শন করে।
</p>
<p style="font-family: 'SolaimanLipi', sans-serif; font-size: 17px; line-height: 1.85; color: #1e293b; margin-bottom: 20px;">
<strong>সরাসরি ফ্র্যাকশনাল বা কাস্টম পয়েন্ট ইনপুট সুবিধা:</strong> অনেক শিক্ষার্থী তাদের নির্দিষ্ট পরীক্ষার নম্বরপত্র অনুযায়ী বা মানোন্নয়ন পর্যালোচনায় ড্রপডাউনের বাঁধা-ধরা লেটার গ্রেডের বাইরে যেকোনো কাস্টম ফ্র্যাকশনাল পয়েন্ট (যেমন: ৩.৪৫, ৩.১৮, ৩.৬০ ইত্যাদি) সরাসরি ইনপুট দিয়ে রেজাল্ট পরীক্ষা করতে চান। হেল্পট্রিকবিডি ক্যালকুলেটরে প্রতিটি কোর্সের পাশে <strong>লেটার গ্রেডের পাশাপাশি সরাসরি পয়েন্ট (GP) টাইপ করার স্বতন্ত্র ঘর</strong> যুক্ত করা হয়েছে। লেটার গ্রেড সিলেক্ট করলে পয়েন্ট ঘরে স্বয়ংক্রিয়ভাবে পয়েন্ট বসে যায়, আবার সরাসরি পয়েন্ট টাইপ করলে ক্যালকুলেটর স্বয়ংক্রিয়ভাবে সেই সুনির্দিষ্ট পয়েন্টের ভিত্তিতে শতভাগ নির্ভুল ক্রেডিট-ওয়েটেড সিজিপিএ নির্ধারণ করে।
</p>

<h2 class="htbd-content-h2" style="font-family: 'SolaimanLipi', sans-serif; color: #0c2340; font-size: 24px; font-weight: 700; margin: 40px 0 18px 0; border-left: 5px solid #1e3a8a; padding-left: 14px;">
জাতীয় বিশ্ববিদ্যালয়ের অফিসিয়াল গ্রেডিং স্কেল ও মার্কস বণ্টন ২০২৬
</h2>
<p style="font-family: 'SolaimanLipi', sans-serif; font-size: 17px; line-height: 1.85; color: #1e293b; margin-bottom: 20px;">
জাতীয় বিশ্ববিদ্যালয় ইউজার ফ্রেন্ডলি ৪.০০ পয়েন্ট স্কেল অনুসরণ করে। নিম্নে শতকরা নম্বর, লেটার গ্রেড এবং অর্জিত গ্রেড পয়েন্টের অফিসিয়াল তালিকা প্রদান করা হলো:
</p>

<!-- Grading Table -->
<div style="overflow-x: auto; margin: 25px 0;">
<table class="htbd-grade-table" style="width: 100%; border-collapse: collapse; font-family: 'SolaimanLipi', sans-serif; font-size: 16px; text-align: center; border: 1px solid #cbd5e1;">
<thead>
<tr style="background: #1e3a8a; color: #ffffff;">
<th style="padding: 12px; border: 1px solid #cbd5e1;">শতকরা নম্বর (%)</th>
<th style="padding: 12px; border: 1px solid #cbd5e1;">লেটার গ্রেড (Letter Grade)</th>
<th style="padding: 12px; border: 1px solid #cbd5e1;">গ্রেড পয়েন্ট (GP)</th>
<th style="padding: 12px; border: 1px solid #cbd5e1;">একাডেমিক মূল্যায়ন</th>
</tr>
</thead>
<tbody>
<tr class="row-even" style="background: #ffffff;">
<td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: 600;">৮০% থেকে ১০০%</td>
<td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: 700; color: #15803d;">A+</td>
<td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: 700;">4.00</td>
<td style="padding: 10px; border: 1px solid #cbd5e1;">অসামান্য (Outstanding)</td>
</tr>
<tr class="row-odd" style="background: #f8fafc;">
<td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: 600;">৭৫% থেকে ৭৯%</td>
<td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: 700; color: #16a34a;">A</td>
<td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: 700;">3.75</td>
<td style="padding: 10px; border: 1px solid #cbd5e1;">চমৎকার (Excellent)</td>
</tr>
<tr class="row-even" style="background: #ffffff;">
<td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: 600;">৭০% থেকে ৭৪%</td>
<td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: 700; color: #22c55e;">A-</td>
<td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: 700;">3.50</td>
<td style="padding: 10px; border: 1px solid #cbd5e1;">অতি উত্তম (Very Good)</td>
</tr>
<tr class="row-odd" style="background: #f8fafc;">
<td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: 600;">৬৫% থেকে ৬৯%</td>
<td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: 700; color: #2563eb;">B+</td>
<td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: 700;">3.25</td>
<td style="padding: 10px; border: 1px solid #cbd5e1;">উত্তম (Good)</td>
</tr>
<tr class="row-even" style="background: #ffffff;">
<td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: 600;">৬০% থেকে ৬৪%</td>
<td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: 700; color: #3b82f6;">B</td>
<td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: 700;">3.00</td>
<td style="padding: 10px; border: 1px solid #cbd5e1;">সন্তোষজনক (Satisfactory)</td>
</tr>
<tr class="row-odd" style="background: #f8fafc;">
<td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: 600;">৫৫% থেকে ৫৯%</td>
<td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: 700; color: #6366f1;">B-</td>
<td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: 700;">2.75</td>
<td style="padding: 10px; border: 1px solid #cbd5e1;">পাস (Above Average)</td>
</tr>
<tr class="row-even" style="background: #ffffff;">
<td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: 600;">৫০% থেকে ৫৪%</td>
<td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: 700; color: #d97706;">C+</td>
<td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: 700;">2.50</td>
<td style="padding: 10px; border: 1px solid #cbd5e1;">সাধারণ (Average)</td>
</tr>
<tr class="row-odd" style="background: #f8fafc;">
<td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: 600;">৪৫% থেকে ৪৯%</td>
<td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: 700; color: #ea580c;">C</td>
<td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: 700;">2.25</td>
<td style="padding: 10px; border: 1px solid #cbd5e1;">গড়পড়তা (Below Average)</td>
</tr>
<tr class="row-even" style="background: #ffffff;">
<td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: 600;">৪০% থেকে ৪৪%</td>
<td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: 700; color: #dc2626;">D</td>
<td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: 700;">2.00</td>
<td style="padding: 10px; border: 1px solid #cbd5e1;">নিম্ন পাস (Poor Pass)</td>
</tr>
<tr class="row-fail" style="background: #fef2f2;">
<td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: 600; color: #b91c1c;">৪০% এর নিচে</td>
<td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: 700; color: #b91c1c;">F</td>
<td style="padding: 10px; border: 1px solid #cbd5e1; font-weight: 700; color: #b91c1c;">0.00</td>
<td style="padding: 10px; border: 1px solid #cbd5e1; color: #b91c1c;">অকৃতকার্য (Fail)</td>
</tr>
</tbody>
</table>
</div>

<h2 class="htbd-content-h2" style="font-family: 'SolaimanLipi', sans-serif; color: #0c2340; font-size: 24px; font-weight: 700; margin: 40px 0 18px 0; border-left: 5px solid #1e3a8a; padding-left: 14px;">
জাতীয় বিশ্ববিদ্যালয়ের ক্লাস ও ডিভিশন নির্ধারণের নীতিমালা
</h2>
<p style="font-family: 'SolaimanLipi', sans-serif; font-size: 17px; line-height: 1.85; color: #1e293b; margin-bottom: 20px;">
চাকরির পরীক্ষায় বা উচ্চশিক্ষায় আবেদনের ক্ষেত্রে প্রায়ই প্রথম শ্রেণি (First Class) বা দ্বিতীয় শ্রেণি (Second Class)-এর প্রয়োজনীয়তা উল্লেখ থাকে। জাতীয় বিশ্ববিদ্যালয়ের সিজিপিএ স্কেল অনুযায়ী ক্লাস সমতুল্যতার নিয়ম নিম্নরূপ:
</p>

<ul style="font-family: 'SolaimanLipi', sans-serif; font-size: 17px; line-height: 1.85; color: #1e293b; margin-bottom: 25px; padding-left: 20px;">
<li style="margin-bottom: 10px;"><strong>প্রথম শ্রেণি (First Class):</strong> সিজিপিএ ৩.০০ থেকে ৪.০০ (CGPA 3.00 to 4.00)। এই রেঞ্জে থাকলে শিক্ষার্থী প্রথম শ্রেণিতে উত্তীর্ণ বলে গণ্য হন।</li>
<li style="margin-bottom: 10px;"><strong>দ্বিতীয় শ্রেণি (Second Class):</strong> সিজিপিএ ২.২৫ থেকে ২.৯৯ (CGPA 2.25 to 2.99)। জাতীয় বিশ্ববিদ্যালয়ের সিংহভাগ শিক্ষার্থী এই ক্যাটাগরিতে অন্তর্ভুক্ত হন।</li>
<li style="margin-bottom: 10px;"><strong>তৃতীয় শ্রেণি (Third Class):</strong> সিজিপিএ ২.০০ থেকে ২.২৪ (CGPA 2.00 to 2.24)। এটি স্নাতক ডিগ্রি অর্জনের ন্যূনতম পাস মানদণ্ড।</li>
<li style="margin-bottom: 10px;"><strong>ফেল বা ডিগ্রি অপ্রাপ্ত:</strong> সিজিপিএ ২.০০-এর নিচে পেলে শিক্ষার্থী কোনো ডিগ্রি অর্জন করতে পারবেন না। তাকে মানোন্নয়ন বা রি-অ্যাডমিশনের মাধ্যমে সিজিপিএ ২.০০ এ উন্নীত করতে হবে।</li>
</ul>

<h2 class="htbd-content-h2" style="font-family: 'SolaimanLipi', sans-serif; color: #0c2340; font-size: 24px; font-weight: 700; margin: 40px 0 18px 0; border-left: 5px solid #1e3a8a; padding-left: 14px;">
সিজিপিএ হিসাব করার গাণিতিক ফর্মুলা ও বাস্তব উদাহরণ
</h2>
<p style="font-family: 'SolaimanLipi', sans-serif; font-size: 17px; line-height: 1.85; color: #1e293b; margin-bottom: 20px;">
জাতীয় বিশ্ববিদ্যালয়ের অফিসিয়াল রেগুলেশন অনুযায়ী সিজিপিএ নির্ণয়ের মৌলিক সূত্রটি হলো:
</p>

<div class="htbd-formula-box" style="background: #f1f5f9; border-radius: 8px; padding: 18px; margin: 20px 0; font-family: monospace; font-size: 15px; color: #0f172a; text-align: center; border: 1px solid #cbd5e1;">
CGPA = (মোট অর্জিত ক্রেডিট পয়েন্টের যোগফল) ÷ (মোট ক্রেডিট সংখ্যা)
<br /><br />
বা, CGPA = ∑ (Credit × Grade Point) ÷ ∑ (Total Credits)
</div>

<p style="font-family: 'SolaimanLipi', sans-serif; font-size: 17px; line-height: 1.85; color: #1e293b; margin-bottom: 20px;">
<strong>বাস্তব উদাহরণ:</strong> ধরি একজন শিক্ষার্থী চার বছরে মোট ১২৮ ক্রেডিট সম্পন্ন করেছেন।<br />
• ১ম বর্ষ (৩২ ক্রেডিট): জিপিএ ৩.১০ → ক্রেডিট পয়েন্ট = ৩২ × ৩.১০ = ৯৯.২০<br />
• ২য় বর্ষ (৩২ ক্রেডিট): জিপিএ ২.৮৫ → ক্রেডিট পয়েন্ট = ৩২ × ২.৮৫ = ৯১.২০<br />
• ৩য় বর্ষ (৩২ ক্রেডিট): জিপিএ ৩.০০ → ক্রেডিট পয়েন্ট = ৩২ × ৩.০০ = ৯৬.০০<br />
• ৪র্থ বর্ষ (৩২ ক্রেডিট): জিপিএ ৩.২০ → ক্রেডিট পয়েন্ট = ৩২ × ৩.২০ = ১০২.৪০<br />
<strong>মোট ক্রেডিট পয়েন্ট:</strong> ৯৯.২০ + ৯১.২০ + ৯৬.০০ + ১০২.৪০ = ৩৮৮.৮০<br />
<strong>ফাইনাল CGPA:</strong> ৩৮৮.৮০ ÷ ১২৮ = <strong>৩.০৩ (First Class / ১ম শ্রেণি)</strong>!
</p>

<h2 class="htbd-content-h2" style="font-family: 'SolaimanLipi', sans-serif; color: #0c2340; font-size: 24px; font-weight: 700; margin: 40px 0 18px 0; border-left: 5px solid #1e3a8a; padding-left: 14px;">
নন-ক্রেডিট আবশ্যিক ইংরেজি ও ব্যবহারিক বিষয়ের নিয়মাবলী
</h2>
<p style="font-family: 'SolaimanLipi', sans-serif; font-size: 17px; line-height: 1.85; color: #1e293b; margin-bottom: 20px;">
অনার্স ২য় বর্ষের শিক্ষার্থীদের জন্য ১০০ নম্বরের একটি <strong>ইংরেজি আবশ্যিক (Non-Credit English, কোর্স কোড: ২২১১০৯)</strong> বিষয় থাকে। অনেক শিক্ষার্থীই দুশ্চিন্তায় থাকেন যে এতে খারাপ করলে বুঝি সিজিপিএ কমে যাবে। জাতীয় বিশ্ববিদ্যালয়ের স্পষ্ট নীতিমালা হলো:
</p>

<ul style="font-family: 'SolaimanLipi', sans-serif; font-size: 17px; line-height: 1.85; color: #1e293b; margin-bottom: 25px; padding-left: 20px;">
<li style="margin-bottom: 10px;">ইংরেজি আবশ্যিক বিষয়ের ক্রেডিট সংখ্যা ০ (Zero Credit)। তাই এতে আপনি A+ পান বা D পান, এটি আপনার বার্ষিক জিপিএ বা সার্বিক সিজিপিএ-তে কোনো প্রভাব ফেলবে না।</li>
<li style="margin-bottom: 10px;">তবে পরীক্ষায় ন্যূনতম ৩৩ নম্বর পেয়ে পাস করা বাধ্যতামূলক। কোনো শিক্ষার্থী ফেল করলে তাকে পরবর্তী ব্যাচের সাথে পরীক্ষা দিয়ে পাস করতে হবে। অন্যথায় অনার্স পাসের চূড়ান্ত মূল সনদপত্র প্রদান করা হবে না।</li>
<li style="margin-bottom: 10px;">বিজ্ঞান অনুষদের ক্ষেত্রে ব্যবহারিক ও ইনকোর্স পরীক্ষা অত্যন্ত গুরুত্বপূর্ণ। প্র্যাকটিক্যাল সাধারণত ২ বা ৪ ক্রেডিটের হয়ে থাকে এবং এতে ভালো গ্রেড (A বা A+) পাওয়া অপেক্ষাকৃত সহজ, যা সামগ্রিক সিজিপিএ অনেক বৃদ্ধি করে।</li>
</ul>

<h2 class="htbd-content-h2" style="font-family: 'SolaimanLipi', sans-serif; color: #0c2340; font-size: 24px; font-weight: 700; margin: 40px 0 18px 0; border-left: 5px solid #1e3a8a; padding-left: 14px;">
মানোন্নয়ন (Improvement) পরীক্ষার সুযোগ ও সর্বোচ্চ গ্রেড সীমা
</h2>
<p style="font-family: 'SolaimanLipi', sans-serif; font-size: 17px; line-height: 1.85; color: #1e293b; margin-bottom: 20px;">
জাতীয় বিশ্ববিদ্যালয়ে কোনো কোর্সে খারাপ ফলাফল হলে তা শুধরে নেওয়ার জন্য মানোন্নয়ন পরীক্ষার সুযোগ রয়েছে। তবে এর কিছু কড়া নিয়ম রয়েছে:
</p>

<ul style="font-family: 'SolaimanLipi', sans-serif; font-size: 17px; line-height: 1.85; color: #1e293b; margin-bottom: 25px; padding-left: 20px;">
<li style="margin-bottom: 10px;">শুধুমাত্র C (২.২৫), D (২.০০) অথবা F (০.০০) গ্রেড প্রাপ্ত কোর্সেই মানোন্নয়ন পরীক্ষা দেওয়া যায়। কোনো বিষয়ে C+ (২.৫০) বা তার বেশি গ্রেড থাকলে আর মানোন্নয়ন দেওয়া যায় না।</li>
<li style="margin-bottom: 10px;">মানোন্নয়ন পরীক্ষায় যত ভালো নম্বরই পান না কেন, জাতীয় বিশ্ববিদ্যালয়ের অর্ডিন্যান্স অনুযায়ী <strong>সর্বোচ্চ B+ গ্রেড (গ্রেড পয়েন্ট ৩.২৫)</strong> প্রদান করা হবে। শিক্ষার্থী ১০০ তে ৯০ পেলেও তার গ্রেড B+ হিসেবেই গণনায় আসবে।</li>
<li style="margin-bottom: 10px;">যদি মানোন্নয়ন পরীক্ষায় আগের চেয়ে কম গ্রেড আসে, তবে পূর্বের ভালো গ্রেডটিই রেজাল্ট শিটে বহাল রাখা হয়।</li>
</ul>

<h2 class="htbd-content-h2" style="font-family: 'SolaimanLipi', sans-serif; color: #0c2340; font-size: 24px; font-weight: 700; margin: 40px 0 18px 0; border-left: 5px solid #1e3a8a; padding-left: 14px;">
সিজিপিএ ৩.০০+ (ফার্স্ট ক্লাস) নিশ্চিত করার ৫টি পরীক্ষিত মাস্টার টিপস
</h2>
<p style="font-family: 'SolaimanLipi', sans-serif; font-size: 17px; line-height: 1.85; color: #1e293b; margin-bottom: 20px;">
চার বছরের অনার্স যাত্রায় অনেক শিক্ষার্থী শুরুতে হেলাফেলা করে ৩য় বা ৪র্থ বর্ষে এসে সিজিপিএ বাড়ানোর জন্য দিশেহারা হয়ে পড়েন। আপনি যদি প্রথম শ্রেণি নিশ্চিত করতে চান, তবে নিচের কৌশলগুলো মেনে চলুন:
</p>

<ol style="font-family: 'SolaimanLipi', sans-serif; font-size: 17px; line-height: 1.85; color: #1e293b; margin-bottom: 25px; padding-left: 20px;">
<li style="margin-bottom: 12px;"><strong>১ম ও ২য় বর্ষ থেকেই ৩.০০ টার্গেট রাখুন:</strong> ১ম ও ২য় বর্ষের সিলেবাস তুলনামূলক সহজ থাকে। এই সময়ে ৩.১০ থেকে ৩.২০ তুলে রাখলে পরবর্তীতে কঠিন বর্ষগুলোতেও সিজিপিএ ৩.০০-এর নিচে নামে না।</li>
<li style="margin-bottom: 12px;"><strong>ইনকোর্স ও টার্ম পেপারে পুরো নম্বর আদায়:</strong> প্রতিটি ১০০ নম্বরের বিষয়ে ২০ নম্বর থাকে ইনকোর্সে। শিক্ষকদের সাথে সুসম্পর্ক রেখে এবং যথাসময়ে অ্যাসাইনমেন্ট জমা দিয়ে ২০-এ ১৮-১৯ নিশ্চিত করতে হবে।</li>
<li style="margin-bottom: 12px;"><strong>'F' গ্রেড কোনো অবস্থাতেই আসতে দেবেন না:</strong> একটি F গ্রেড পুরো বছরের জিপিএ এক ধাক্কায় ০.৪০ থেকে ০.৫০ নামিয়ে দেয়। ন্যূনতম পাস মার্ক ৪০ যেকোনো মূল্যে নিশ্চিত করতে হবে।</li>
<li style="margin-bottom: 12px;"><strong>বোর্ডের বিগত ৫ বছরের প্রশ্ন বিশ্লেষণ:</strong> জাতীয় বিশ্ববিদ্যালয়ের লিখিত পরীক্ষায় প্রায় ৬০-৭০% প্রশ্ন পূর্ববর্তী বছরগুলোর ফাইনাল পরীক্ষা থেকে ঘুরেফিরে আসে। বিগত ৫ বছরের বোর্ড প্রশ্ন মুখস্থের মতো আয়ত্ত করুন।</li>
<li style="margin-bottom: 12px;"><strong>পয়েন্ট ও চার্টভিত্তিক খাতা উপস্থাপন:</strong> ঢালাও প্যারাগ্রাফ লেখার চেয়ে উত্তরপত্রে সাব-হেডিং, বুলেট পয়েন্ট, ডাটা চার্ট এবং উদ্ধৃতি ব্যবহার করলে পরীক্ষক সর্বোচ্চ নম্বর প্রদান করেন।</li>
</ol>

<h2 class="htbd-content-h2" style="font-family: 'SolaimanLipi', sans-serif; color: #0c2340; font-size: 24px; font-weight: 700; margin: 40px 0 18px 0; border-left: 5px solid #1e3a8a; padding-left: 14px;">
জাতীয় বিশ্ববিদ্যালয় সিজিপিএ সংক্রান্ত সচরাচর জিজ্ঞাসিত প্রশ্নাবলী (FAQ)
</h2>

<!-- FAQ 1 -->
<div class="htbd-faq-item" style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 18px 20px; margin-bottom: 14px; font-family: 'SolaimanLipi', sans-serif;">
<h3 style="margin: 0 0 8px 0; color: #1e3a8a; font-size: 18px; font-weight: 700;">১. জাতীয় বিশ্ববিদ্যালয়ে মোট কত ক্রেডিট সম্পন্ন করতে হয়?</h3>
<p style="margin: 0; color: #334155; font-size: 16px; line-height: 1.8;">
চার বছর মেয়াদি স্নাতক (সম্মান) কোর্সে সাধারণত প্রতি শিক্ষাবর্ষে ৩২ ক্রেডিট করে ৪ বছরে সর্বমোট ১২৮ ক্রেডিট সম্পন্ন করতে হয়। কিছু বিশেষ বিভাগে ব্যবহারিক বেশি থাকায় ক্রেডিট সামান্য কম-বেশি হতে পারে।
</p>
</div>

<!-- FAQ 2 -->
<div class="htbd-faq-item" style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 18px 20px; margin-bottom: 14px; font-family: 'SolaimanLipi', sans-serif;">
<h3 style="margin: 0 0 8px 0; color: #1e3a8a; font-size: 18px; font-weight: 700;">২. সিজিপিএ কত পেলে ১ম শ্রেণি বা ফার্স্ট ক্লাস গণ্য হবে?</h3>
<p style="margin: 0; color: #334155; font-size: 16px; line-height: 1.8;">
জাতীয় বিশ্ববিদ্যালয়ের নিয়ম অনুযায়ী ফাইনাল সিজিপিএ ৩.০০ (CGPA 3.00) বা তার বেশি অর্জন করলে তা প্রথম শ্রেণি (First Class) হিসেবে গণ্য হবে। ২.২৫ থেকে ২.৯৯ পর্যন্ত ২য় শ্রেণি এবং ২.০০ থেকে ২.২৪ পর্যন্ত ৩য় শ্রেণি।
</p>
</div>

<!-- FAQ 3 -->
<div class="htbd-faq-item" style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 18px 20px; margin-bottom: 14px; font-family: 'SolaimanLipi', sans-serif;">
<h3 style="margin: 0 0 8px 0; color: #1e3a8a; font-size: 18px; font-weight: 700;">৩. নন-ক্রেডিট ইংরেজি ফেল করলে কি সিজিপিএ ক্ষতিগ্রস্ত হবে?</h3>
<p style="margin: 0; color: #334155; font-size: 16px; line-height: 1.8;">
না, ইংরেজি আবশ্যিক বিষয়ের ক্রেডিট সংখ্যা ০ হওয়ায় এতে অর্জিত গ্রেড সিজিপিএ গণনায় কোনো প্রভাব ফেলে না। তবে স্নাতক সনদ পাওয়ার জন্য এতে ন্যূনতম ৩৩ নম্বর পেয়ে পাস করা বাধ্যতামূলক।
</p>
</div>

<!-- FAQ 4 -->
<div class="htbd-faq-item" style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 18px 20px; margin-bottom: 14px; font-family: 'SolaimanLipi', sans-serif;">
<h3 style="margin: 0 0 8px 0; color: #1e3a8a; font-size: 18px; font-weight: 700;">৪. ইমপ্রুভমেন্ট পরীক্ষা দিলে কি A+ পাওয়া সম্ভব?</h3>
<p style="margin: 0; color: #334155; font-size: 16px; line-height: 1.8;">
না, জাতীয় বিশ্ববিদ্যালয়ের অর্ডিন্যান্স অনুযায়ী মানোন্নয়ন পরীক্ষায় কোনো বিষয়ে ৯০ নম্বর পেলেও সর্বোচ্চ B+ গ্রেড (গ্রেড পয়েন্ট ৩.২৫) প্রদান করা হয়।
</p>
</div>

<!-- FAQ 5 -->
<div class="htbd-faq-item" style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 18px 20px; margin-bottom: 14px; font-family: 'SolaimanLipi', sans-serif;">
<h3 style="margin: 0 0 8px 0; color: #1e3a8a; font-size: 18px; font-weight: 700;">৫. কোনো বর্ষে এফ (F) গ্রেড থাকলে কি সিজিপিএ হিসাব করা সম্ভব?</h3>
<p style="margin: 0; color: #334155; font-size: 16px; line-height: 1.8;">
হ্যাঁ, তবে F গ্রেডের গ্রেড পয়েন্ট হলো ০.০০। এটি মোট ক্রেডিটের সাথে যুক্ত হয়ে গড় সিজিপিএ ব্যাপকভাবে হ্রাস করে। পরবর্তী বর্ষে পরীক্ষা দিয়ে F গ্রেড ক্লিয়ার করলে নতুন গ্রেড পয়েন্ট যুক্ত হয়ে সিজিপিএ বৃদ্ধি পাবে।
</p>
</div>

<!-- FAQ 6 -->
<div class="htbd-faq-item" style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 18px 20px; margin-bottom: 14px; font-family: 'SolaimanLipi', sans-serif;">
<h3 style="margin: 0 0 8px 0; color: #1e3a8a; font-size: 18px; font-weight: 700;">৬. ডিগ্রি (পাস) কোর্সের সিজিপিএ কি একই নিয়মে গণনা করা হয়?</h3>
<p style="margin: 0; color: #334155; font-size: 16px; line-height: 1.8;">
হ্যাঁ, ডিগ্রি (পাস) কোর্সেও একই ৪.০০ পয়েন্ট গ্রেডিং স্কেল কার্যকর। তবে ডিগ্রি কোর্স ৩ বছর মেয়াদি হওয়ায় মোট ক্রেডিট সাধারণত ৮৪ থেকে ৯০ ক্রেডিট হয়ে থাকে।
</p>
</div>

<!-- FAQ 7 -->
<div class="htbd-faq-item" style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 18px 20px; margin-bottom: 14px; font-family: 'SolaimanLipi', sans-serif;">
<h3 style="margin: 0 0 8px 0; color: #1e3a8a; font-size: 18px; font-weight: 700;">৭. পরবর্তী বর্ষে প্রমোশনের জন্য ন্যূনতম সিজিপিএ কত লাগে?</h3>
<p style="margin: 0; color: #334155; font-size: 16px; line-height: 1.8;">
অনার্স ১ম বর্ষ থেকে ২য় বর্ষে প্রমোশনের জন্য ন্যূনতম CGPA ২.০০ এবং ৩টি বিষয়ে পাস প্রয়োজন। পরবর্তী বর্ষগুলোতেও ন্যূনতম সিজিপিএ ২.০০ বজায় রাখা আবশ্যক।
</p>
</div>

<!-- FAQ 8 -->
<div class="htbd-faq-item" style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 18px 20px; margin-bottom: 14px; font-family: 'SolaimanLipi', sans-serif;">
<h3 style="margin: 0 0 8px 0; color: #1e3a8a; font-size: 18px; font-weight: 700;">৮. মাস্টার্স কোর্সের সিজিপিএ স্কেল কি ভিন্ন?</h3>
<p style="margin: 0; color: #334155; font-size: 16px; line-height: 1.8;">
না, মাস্টার্স ফাইনাল বা প্রিলিমিনারিতেও একই ৪.০০ স্কেল ব্যবহৃত হয়। মাস্টার্স ফাইনালে সাধারণত ৩২ থেকে ৩৬ ক্রেডিট সম্পন্ন করতে হয়।
</p>
</div>

<!-- FAQ 9 -->
<div class="htbd-faq-item" style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 18px 20px; margin-bottom: 14px; font-family: 'SolaimanLipi', sans-serif;">
<h3 style="margin: 0 0 8px 0; color: #1e3a8a; font-size: 18px; font-weight: 700;">৯. হেল্পট্রিকবিডি সিজিপিএ ক্যালকুলেটর কি অফলাইনে কাজ করে?</h3>
<p style="margin: 0; color: #334155; font-size: 16px; line-height: 1.8;">
হ্যাঁ, একবার পেজটি লোড হয়ে গেলে কোনো ইন্টারনেট সংযোগ ছাড়াও এটি ক্লায়েন্ট-সাইড জাভাস্ক্রিপ্ট দ্বারা সম্পূর্ণ অফলাইনে মসৃণভাবে গণনা সম্পন্ন করতে পারে।
</p>
</div>

<!-- FAQ 10 -->
<div class="htbd-faq-item" style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 18px 20px; margin-bottom: 14px; font-family: 'SolaimanLipi', sans-serif;">
<h3 style="margin: 0 0 8px 0; color: #1e3a8a; font-size: 18px; font-weight: 700;">১০. ব্রাউজার রিফ্রেশ করলে কি আমার ইনপুট করা রেজাল্ট মুছে যাবে?</h3>
<p style="margin: 0; color: #334155; font-size: 16px; line-height: 1.8;">
না! আমাদের ক্যালকুলেটরে লোকাল স্টোরেজ (LocalStorage) অটো-সেভ ব্যবস্থা রয়েছে। ফলে পেজ বন্ধ বা রিফ্রেশ করলেও আপনার ইনপুট করা রেজাল্ট সম্পূর্ণ নিরাপদ সংরক্ষিত থাকবে।
</p>
</div>

<!-- FAQ 11 -->
<div class="htbd-faq-item" style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 18px 20px; margin-bottom: 25px; font-family: 'SolaimanLipi', sans-serif;">
<h3 style="margin: 0 0 8px 0; color: #1e3a8a; font-size: 18px; font-weight: 700;">১১. লেটার গ্রেড ছাড়া কি সরাসরি দশমিক বা কাস্টম পয়েন্ট দিয়ে সিজিপিএ হিসাব করা যায়?</h3>
<p style="margin: 0; color: #334155; font-size: 16px; line-height: 1.8;">
হ্যাঁ! আমাদের ক্যালকুলেটরে প্রতিটি বিষয়ের জন্য লেটার গ্রেডের পাশাপাশি "পয়েন্ট (GP)" ঘর রয়েছে। আপনি চাইলে লেটার গ্রেড ড্রপডাউন স্পর্শ না করেই যেকোনো ফ্র্যাকশনাল বা সুনির্দিষ্ট পয়েন্ট (যেমন: ৩.৫৫, ৩.১২, ২.৮৫ ইত্যাদি) সরাসরি লিখে মুহূর্তেই সঠিক সিজিপিএ গণনা করতে পারবেন।
</p>
</div>

<!-- Author Attribution Box -->
<div class="htbd-author-box" style="display: flex; align-items: center; gap: 18px; margin: 40px 0 25px 0; padding: 20px 24px; background: #f8fafc; border: 1px solid #e2e8f0; border-left: 5px solid #1e3a8a; border-radius: 10px; font-family: 'SolaimanLipi', Arial, sans-serif;">
  <img src="https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/author/faruk_sir.webp" 
       alt="ফারুক স্যার (মো. ওমর ফারুক)" 
       class="htbd-author-avatar" 
       width="75" height="75" 
       loading="lazy" 
       style="width: 75px !important; height: 75px !important; min-width: 75px !important; max-width: 75px !important; border-radius: 50% !important; object-fit: cover !important; border: 2px solid #2563eb !important; flex-shrink: 0 !important; display: block !important; margin: 0 !important; box-shadow: 0 2px 6px rgba(0,0,0,0.08) !important;" />
  <div class="htbd-author-info" style="flex: 1 1 auto; min-width: 0;">
    <h4 style="margin: 0 0 4px 0; color: #1e3a8a; font-size: 18px; font-weight: 700; line-height: 1.3;">ফারুক স্যার (মো. ওমর ফারুক)</h4>
    <div class="htbd-author-meta" style="font-size: 13px; color: #64748b; margin-bottom: 6px; font-weight: 600;">শিক্ষাবিদ ও অ্যাকাডেমিক গবেষক | প্রতিষ্ঠাতা, HelpTrickBD</div>
    <p class="htbd-author-bio" style="font-size: 14px; color: #334155; line-height: 1.6; margin: 0;">
      জাতীয় বিশ্ববিদ্যালয় ও উচ্চশিক্ষা অ্যাকাডেমিক পাঠ্যক্রম পর্যালোচনায় দীর্ঘ এক দশকের অভিজ্ঞতাসম্পন্ন একজন অ্যাকাডেমিক মেন্টর ও শিক্ষা গবেষক।
    </p>
  </div>
</div>

<!-- ========================================================================== -->
<!-- EMBEDDED JAVASCRIPT LOGIC ENGINE (VANILLA JS, ZERO EXTERNAL DEPENDENCIES)  -->
<!-- ========================================================================== -->
<script>
(function() {{
  // ---------------------------------------------------------------------------
  // BLOGGER HTML ENTITY SCRUBBER & DECODER
  // ---------------------------------------------------------------------------
  function _bn(str) {{
    if (!str || typeof str !== 'string') return str;
    if (str.indexOf('&') === -1) return str;
    const txt = document.createElement('textarea');
    txt.innerHTML = str;
    return txt.value;
  }}

  function scrubEntities(root) {{
    if (!root) return;
    const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, null, false);
    let node;
    while ((node = walker.nextNode())) {{
      if (node.nodeValue && node.nodeValue.indexOf('&#') !== -1) {{
        node.nodeValue = _bn(node.nodeValue);
      }}
    }}
  }}

  // 1. SYLLABUS DATABASE
  const SYLLABUS = {syllabus_json_str};

  // Grade point mapping
  const GRADE_SCALE = {{
    "A+": 4.00,
    "A": 3.75,
    "A-": 3.50,
    "B+": 3.25,
    "B": 3.00,
    "B-": 2.75,
    "C+": 2.50,
    "C": 2.25,
    "D": 2.00,
    "F": 0.00
  }};

  // State
  let currentProgram = 'honours'; // honours, degree, masters
  let currentMode = 'mode-year';

  // DOM Elements
  const progBtns = document.querySelectorAll('.htbd-prog-btn');
  const tabBtns = document.querySelectorAll('.htbd-tab-btn');
  const modePanels = document.querySelectorAll('.htbd-mode-panel');

  const dashGaugeCircle = document.getElementById('dash-gauge-circle');
  const dashCgpaVal = document.getElementById('dash-cgpa-val');
  const dashDivisionBadge = document.getElementById('dash-division-badge');
  const dashTotalCredits = document.getElementById('dash-total-credits');
  const dashTotalPoints = document.getElementById('dash-total-points');
  const dashProgramBadge = document.getElementById('dash-program-badge');
  const dashTrendLine = document.getElementById('dash-trend-line');

  // Program switching (Clean Class Toggle, Zero Inline Style Pollution)
  progBtns.forEach(btn => {{
    btn.addEventListener('click', () => {{
      progBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      currentProgram = btn.dataset.prog;
      updateProgramUI();
      calculateYearMode();
    }});
  }});

  function updateProgramUI() {{
    const y3Card = document.querySelector('.htbd-year-card[data-year="3"]');
    const y4Card = document.querySelector('.htbd-year-card[data-year="4"]');

    if (currentProgram === 'honours') {{
      dashProgramBadge.textContent = _bn('স্নাতক (সম্মান)');
      if (y3Card) y3Card.style.display = 'block';
      if (y4Card) y4Card.style.display = 'block';
    }} else if (currentProgram === 'degree') {{
      dashProgramBadge.textContent = _bn('ডিগ্রি (পাস)');
      if (y3Card) y3Card.style.display = 'block';
      if (y4Card) y4Card.style.display = 'none';
    }} else if (currentProgram === 'masters') {{
      dashProgramBadge.textContent = _bn('মাস্টার্স');
      if (y3Card) y3Card.style.display = 'none';
      if (y4Card) y4Card.style.display = 'none';
    }}
  }}

  // Tab switching (Clean Class Toggle, Zero Inline Style Pollution)
  tabBtns.forEach(btn => {{
    btn.addEventListener('click', () => {{
      tabBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      currentMode = btn.dataset.mode;
      modePanels.forEach(p => p.style.display = 'none');
      const targetPanel = document.getElementById('panel-' + currentMode);
      if (targetPanel) targetPanel.style.display = 'block';

      if (currentMode === 'mode-year') calculateYearMode();
      if (currentMode === 'mode-subject') calculateSubjectMode();
      if (currentMode === 'mode-target') calculateTargetMode();
      if (currentMode === 'mode-improvement') calculateImprovementMode();
    }});
  }});

  // ---------------------------------------------------------------------------
  // MODE 1: YEAR-WISE CALCULATION
  // ---------------------------------------------------------------------------
  const yearCards = document.querySelectorAll('.htbd-year-card');

  yearCards.forEach(card => {{
    const range = card.querySelector('.htbd-yr-range');
    const input = card.querySelector('.htbd-yr-gpa');
    const credit = card.querySelector('.htbd-yr-credit');

    range.addEventListener('input', () => {{
      input.value = parseFloat(range.value).toFixed(2);
      calculateYearMode();
    }});

    input.addEventListener('input', () => {{
      let raw = input.value.trim();
      if (raw === '') {{
        range.value = 0;
      }} else {{
        let val = parseFloat(raw) || 0;
        if (val > 4) val = 4;
        if (val < 0) val = 0;
        range.value = val;
      }}
      calculateYearMode();
    }});

    credit.addEventListener('input', calculateYearMode);
  }});

  function calculateYearMode() {{
    let totalPoints = 0;
    let totalCredits = 0;
    let yearGpas = [];

    yearCards.forEach(card => {{
      const year = parseInt(card.dataset.year);
      if (currentProgram === 'degree' && year > 3) return;
      if (currentProgram === 'masters' && year > 2) return;

      const input = card.querySelector('.htbd-yr-gpa');
      const credit = card.querySelector('.htbd-yr-credit');
      const rawVal = input.value.trim();

      if (rawVal !== '') {{
        const gpa = parseFloat(rawVal);
        const cr = parseFloat(credit.value) || 0;
        if (!isNaN(gpa) && cr > 0) {{
          totalPoints += (gpa * cr);
          totalCredits += cr;
          yearGpas.push(gpa);
          return;
        }}
      }}
      yearGpas.push(null); // not entered
    }});

    const cgpa = totalCredits > 0 ? (totalPoints / totalCredits) : 0;
    updateDashboard(cgpa, totalCredits, totalPoints, yearGpas);
    saveState();
  }}

  document.getElementById('btn-reset-year').addEventListener('click', () => {{
    yearCards.forEach(card => {{
      card.querySelector('.htbd-yr-gpa').value = '';
      card.querySelector('.htbd-yr-range').value = 0;
    }});
    calculateYearMode();
  }});

  // ---------------------------------------------------------------------------
  // DASHBOARD UPDATER (PURE CSS BADGES & GAUGE ACCURACY)
  // ---------------------------------------------------------------------------
  function getDivisionText(cgpa, credits) {{
    if (credits === 0 || cgpa === 0) return _bn('পয়েন্ট বা গ্রেড ইনপুট দিন');
    if (cgpa >= 3.00) return _bn('First Class (১ম শ্রেণি)');
    if (cgpa >= 2.25) return _bn('Second Class (২য় শ্রেণি)');
    if (cgpa >= 2.00) return _bn('Third Class (৩য় শ্রেণি)');
    return _bn('নট প্রমোটেড / ডিগ্রি অপ্রাপ্ত');
  }}

  function updateDashboard(cgpa, credits, points, gpaTrend) {{
    const formattedCgpa = cgpa.toFixed(2);
    dashCgpaVal.textContent = formattedCgpa;
    dashTotalCredits.textContent = credits;
    dashTotalPoints.textContent = points.toFixed(2);

    // Update Circular Gauge
    const circumference = 314.16;
    const progress = Math.min(Math.max(cgpa / 4.00, 0), 1);
    const offset = circumference - (progress * circumference);
    dashGaugeCircle.style.strokeDashoffset = offset;

    // Remove old badge classes
    dashDivisionBadge.className = 'htbd-badge';

    let strokeColor = '#2563eb';
    const divText = getDivisionText(cgpa, credits);
    dashDivisionBadge.textContent = _bn(divText);
    scrubEntities(dashDivisionBadge);

    if (credits === 0 || cgpa === 0) {{
      strokeColor = '#94a3b8';
      dashDivisionBadge.classList.add('htbd-badge-empty');
      dashGaugeCircle.style.strokeDashoffset = circumference;
    }} else if (cgpa >= 3.00) {{
      strokeColor = '#15803d'; // Emerald
      dashDivisionBadge.classList.add('htbd-badge-first');
    }} else if (cgpa >= 2.25) {{
      strokeColor = '#2563eb'; // Blue
      dashDivisionBadge.classList.add('htbd-badge-second');
    }} else if (cgpa >= 2.00) {{
      strokeColor = '#d97706'; // Amber
      dashDivisionBadge.classList.add('htbd-badge-third');
    }} else {{
      strokeColor = '#dc2626'; // Red
      dashDivisionBadge.classList.add('htbd-badge-fail');
    }}

    dashGaugeCircle.style.stroke = strokeColor;

    // Update Trend Graph (Only plots valid entered years)
    if (gpaTrend && gpaTrend.length >= 2) {{
      const xCoords = [20, 70, 120, 170];
      let validPoints = [];

      gpaTrend.forEach((val, i) => {{
        if (i < xCoords.length) {{
          const circle = document.getElementById('p' + (i + 1));
          if (val !== null && !isNaN(val)) {{
            const y = 50 - (Math.min(Math.max(val / 4.00, 0), 1) * 40);
            validPoints.push(xCoords[i] + ',' + y);
            if (circle) {{
              circle.setAttribute('cy', y);
              circle.style.opacity = '1';
            }}
          }} else {{
            if (circle) {{
              circle.setAttribute('cy', 50);
              circle.style.opacity = '0.25';
            }}
          }}
        }}
      }});

      if (dashTrendLine) {{
        if (validPoints.length >= 2) {{
          dashTrendLine.setAttribute('points', validPoints.join(' '));
          dashTrendLine.style.opacity = '1';
        }} else if (validPoints.length === 1) {{
          dashTrendLine.setAttribute('points', validPoints[0] + ' ' + validPoints[0]);
          dashTrendLine.style.opacity = '0.5';
        }} else {{
          dashTrendLine.setAttribute('points', '20,50 70,50 120,50 170,50');
          dashTrendLine.style.opacity = '0.2';
        }}
      }}
    }}
  }}

  // ---------------------------------------------------------------------------
  // MODE 2: COURSE-WISE DETAILED GPA
  // ---------------------------------------------------------------------------
  const coursesContainer = document.getElementById('courses-container');
  const btnAddCourse = document.getElementById('btn-add-course');
  const btnResetCourses = document.getElementById('btn-reset-courses');
  const btnLoadSyllabus = document.getElementById('btn-load-syllabus');
  const selDept = document.getElementById('sel-dept');
  const selYear = document.getElementById('sel-year');

  function createCourseRow(code = '', name = '', credit = 4, selectedGrade = '', exactPoint = '') {{
    const row = document.createElement('div');
    row.className = 'htbd-course-row';

    let initialPoint = '';
    if (exactPoint !== null && exactPoint !== '' && !isNaN(exactPoint)) {{
      initialPoint = parseFloat(exactPoint).toFixed(2);
    }} else if (selectedGrade && GRADE_SCALE[selectedGrade] !== undefined) {{
      initialPoint = GRADE_SCALE[selectedGrade].toFixed(2);
    }}

    const displayName = name ? code + ' - ' + name : code;
    const cOpts = [[4,'৪ ক্রেডিট'],[3,'৩ ক্রেডিট'],[2,'২ ক্রেডিট'],[0,'নন-ক্রেডিট']]
      .map(([v,t]) => `<option value="${{v}}" ${{credit === v ? 'selected' : ''}}>${{t}}</option>`).join('');
    const gOpts = [['','-- গ্রেড --'],['A+','A+ (4.00)'],['A','A (3.75)'],['A-','A- (3.50)'],
      ['B+','B+ (3.25)'],['B','B (3.00)'],['B-','B- (2.75)'],['C+','C+ (2.50)'],['C','C (2.25)'],['D','D (2.00)'],['F','F (0.00)']]
      .map(([v,t]) => `<option value="${{v}}" ${{selectedGrade === v ? 'selected' : ''}}>${{t}}</option>`).join('');

    row.innerHTML = `
      <div class="cr-top">
        <div class="cr-name">
          <input type="text" class="c-name" value="${{displayName}}"
            placeholder="কোর্স কোড ও নাম"
            style="width:100%;box-sizing:border-box;padding:7px 10px;border:1px solid #cbd5e1;border-radius:6px;font-size:13.5px;" />
        </div>
        <div class="cr-del-wrap">
          <button type="button" class="btn-del-course" title="কোর্স মুছুন">×</button>
        </div>
      </div>
      <div class="cr-controls">
        <div class="cr-col cr-col-credit">
          <span class="cr-label">ক্রেডিট</span>
          <select class="c-credit" style="width:100%;box-sizing:border-box;padding:7px 4px;border:1px solid #cbd5e1;border-radius:6px;font-size:13px;text-align:center;">
            ${{cOpts}}
          </select>
        </div>
        <div class="cr-col cr-col-grade">
          <span class="cr-label">লেটার গ্রেড</span>
          <select class="c-grade" style="width:100%;box-sizing:border-box;padding:7px 4px;border:1px solid #cbd5e1;border-radius:6px;font-size:13px;font-weight:700;">
            ${{gOpts}}
          </select>
        </div>
        <div class="cr-col cr-col-point">
          <span class="cr-label">পয়েন্ট (GP)</span>
          <input type="number" class="c-point"
            min="0.00" max="4.00" step="0.01"
            value="${{initialPoint}}"
            placeholder="0.00"
            style="width:100%;box-sizing:border-box;padding:7px 4px;border:1.5px solid #94a3b8;border-radius:6px;font-size:14px;font-weight:700;text-align:center;"
            title="পয়েন্ট টাইপ করলে গ্রেড অটো-সিলেক্ট হবে" />
        </div>
      </div>
    `;

    const cCredit = row.querySelector('.c-credit');
    const cGrade  = row.querySelector('.c-grade');
    const cPoint  = row.querySelector('.c-point');
    const btnDel  = row.querySelector('.btn-del-course');

    // Grade dropdown -> Point input (Sync)
    cGrade.addEventListener('change', () => {{
      const gr = cGrade.value;
      if (gr && GRADE_SCALE[gr] !== undefined) {{
        cPoint.value = GRADE_SCALE[gr].toFixed(2);
      }} else if (gr === '') {{
        cPoint.value = '';
      }}
      calculateSubjectMode();
    }});

    // Point input -> Auto Select matching Letter Grade
    const syncPointToGrade = () => {{
      const rawVal = cPoint.value.trim();
      if (rawVal === '') {{
        cGrade.value = '';
        calculateSubjectMode();
        return;
      }}
      let p = parseFloat(rawVal);
      if (isNaN(p)) {{
        cGrade.value = '';
        calculateSubjectMode();
        return;
      }}
      if (p > 4.00) p = 4.00;
      if (p < 0.00) p = 0.00;

      let g = 'F';
      if      (p >= 4.00) g = 'A+';
      else if (p >= 3.75) g = 'A';
      else if (p >= 3.50) g = 'A-';
      else if (p >= 3.25) g = 'B+';
      else if (p >= 3.00) g = 'B';
      else if (p >= 2.75) g = 'B-';
      else if (p >= 2.50) g = 'C+';
      else if (p >= 2.25) g = 'C';
      else if (p >= 2.00) g = 'D';

      cGrade.value = g;
      calculateSubjectMode();
    }};

    cPoint.addEventListener('input', syncPointToGrade);
    cPoint.addEventListener('keyup', syncPointToGrade);
    cPoint.addEventListener('change', syncPointToGrade);

    cCredit.addEventListener('change', calculateSubjectMode);
    btnDel.addEventListener('click', () => {{
      row.remove();
      calculateSubjectMode();
    }});

    coursesContainer.appendChild(row);
  }}

  function calculateSubjectMode() {{
    const rows = document.querySelectorAll('.htbd-course-row');
    let totalPoints = 0;
    let totalCredits = 0;

    rows.forEach(r => {{
      const cr = parseFloat(r.querySelector('.c-credit').value) || 0;
      const rawVal = r.querySelector('.c-point').value.trim();

      if (rawVal !== '') {{
        const gp = parseFloat(rawVal);
        if (!isNaN(gp) && cr > 0) {{
          totalPoints += (cr * gp);
          totalCredits += cr;
        }}
      }}
    }});

    const gpa = totalCredits > 0 ? (totalPoints / totalCredits) : 0;
    updateDashboard(gpa, totalCredits, totalPoints, [gpa, gpa, gpa, gpa]);
  }}

  btnAddCourse.addEventListener('click', () => {{
    const count = document.querySelectorAll('.htbd-course-row').length + 1;
    const name = 'কোর্স ' + (count < 10 ? '০' : '') + count;
    createCourseRow(name, '', 4, '', '');
    calculateSubjectMode();
  }});

  btnResetCourses.addEventListener('click', () => {{
    coursesContainer.innerHTML = '';
    createCourseRow('কোর্স ০১', '', 4, '', '');
    createCourseRow('কোর্স ০২', '', 4, '', '');
    createCourseRow('কোর্স ০৩', '', 4, '', '');
    createCourseRow('কোর্স ০৪', '', 4, '', '');
    createCourseRow('কোর্স ০৫', '', 4, '', '');
    createCourseRow('কোর্স ০৬', '', 4, '', '');
    calculateSubjectMode();
  }});

  // Load syllabus on click
  btnLoadSyllabus.addEventListener('click', () => {{
    const dept = selDept.value;
    const year = selYear.value;

    if (SYLLABUS[dept] && SYLLABUS[dept].years && SYLLABUS[dept].years[year]) {{
      coursesContainer.innerHTML = '';
      const list = SYLLABUS[dept].years[year];
      list.forEach(c => {{
        createCourseRow(c.code, c.name, c.credit, '', '');
      }});
      calculateSubjectMode();
    }} else {{
      alert('এই বিভাগের জন্য কাস্টম কোর্স যোগ করুন।');
    }}
  }});

  // Smart Paste Parser
  const smartPasteBox = document.getElementById('smart-paste-box');
  const btnOpenSmartPaste = document.getElementById('btn-open-smart-paste');
  const btnCancelPaste = document.getElementById('btn-cancel-paste');
  const btnParsePaste = document.getElementById('btn-parse-paste');
  const smartPasteInput = document.getElementById('smart-paste-input');

  btnOpenSmartPaste.addEventListener('click', () => {{
    smartPasteBox.style.display = 'block';
  }});

  btnCancelPaste.addEventListener('click', () => {{
    smartPasteBox.style.display = 'none';
  }});

  btnParsePaste.addEventListener('click', () => {{
    const raw = smartPasteInput.value;
    if (!raw.trim()) return;

    const pattern = /(\\d{{6}})\\s*[-:\\s]*\\s*([A-DF][+-]?|\\d+(?:\\.\\d+)?)/gi;
    let match;
    let found = 0;

    coursesContainer.innerHTML = '';
    while ((match = pattern.exec(raw)) !== null) {{
      const code = match[1];
      const valStr = match[2].trim().toUpperCase();
      const credit = (code === '221109') ? 0 : 4; // non credit english check

      const numVal = parseFloat(valStr);
      if (!isNaN(numVal) && numVal <= 4.00) {{
        let matchedGrade = 'custom';
        for (const [g, val] of Object.entries(GRADE_SCALE)) {{
          if (Math.abs(val - numVal) < 0.001) {{
            matchedGrade = g;
            break;
          }}
        }}
        createCourseRow(code, '', credit, matchedGrade, numVal);
      }} else {{
        createCourseRow(code, '', credit, valStr);
      }}
      found++;
    }}

    if (found > 0) {{
      smartPasteBox.style.display = 'none';
      smartPasteInput.value = '';
      calculateSubjectMode();
      alert(found + 'টি কোর্সের গ্রেড ও পয়েন্ট সফলভাবে অটো-ফিল করা হয়েছে!');
    }} else {{
      alert('সঠিক রেজাল্ট ফরম্যাট শনাক্ত করা যায়নি। অনুগ্রহ করে কোড ও গ্রেড বা পয়েন্ট (যেমন: 221901 A অথবা 221901 3.75) পেস্ট করুন।');
    }}
  }});

  // ---------------------------------------------------------------------------
  // MODE 3: TARGET FIRST CLASS PLANNER
  // ---------------------------------------------------------------------------
  const selCompletedYears = document.getElementById('target-completed-years');
  const inputCurrentCgpa = document.getElementById('target-current-cgpa');
  const selGoalCgpa = document.getElementById('target-goal-cgpa');
  const targetReqGpa = document.getElementById('target-req-gpa');
  const targetBadge = document.getElementById('target-badge');
  const targetAdvice = document.getElementById('target-advice');

  selCompletedYears.addEventListener('change', calculateTargetMode);
  inputCurrentCgpa.addEventListener('input', calculateTargetMode);
  selGoalCgpa.addEventListener('change', calculateTargetMode);

  function calculateTargetMode() {{
    const completed = parseInt(selCompletedYears.value) || 2;
    const current = parseFloat(inputCurrentCgpa.value) || 2.75;
    const goal = parseFloat(selGoalCgpa.value) || 3.00;
    const remaining = 4 - completed;

    const totalRequired = (goal * 4) - (current * completed);
    const reqGpa = remaining > 0 ? (totalRequired / remaining) : goal;

    targetReqGpa.textContent = reqGpa > 0 ? reqGpa.toFixed(2) : '0.00';

    targetBadge.className = 'htbd-badge';

    if (reqGpa <= 3.10) {{
      targetBadge.classList.add('htbd-target-easy');
      targetBadge.textContent = 'সহজসাধ্য ও বাস্তবসম্মত';
      targetAdvice.textContent = 'আপনার কাঙ্ক্ষিত ফলাফল অর্জন করা বেশ সহজ। নিয়মিত ক্লাসের পড়া শেষ করলেই আপনি ফার্স্ট ক্লাস নিশ্চিত করতে পারবেন।';
    }} else if (reqGpa <= 3.45) {{
      targetBadge.classList.add('htbd-target-medium');
      targetBadge.textContent = 'সম্ভব, নিয়মিত অধ্যবসায় প্রয়োজন';
      targetAdvice.textContent = 'বাকি বর্ষগুলোর প্রতিটি বিষয়ে কমপক্ষে B+ বা A- গ্রেড পেতে হবে। ইনকোর্স ও ব্যবহারিকে পুরো নম্বর তোলার চেষ্টা করুন।';
    }} else if (reqGpa <= 3.85) {{
      targetBadge.classList.add('htbd-target-hard');
      targetBadge.textContent = 'চ্যালেঞ্জিং, কঠোর প্রস্তুতি লাগবে';
      targetAdvice.textContent = 'আপনাকে প্রতিটি বিষয়ে A বা A+ গ্রেড পেতে হবে। প্রয়োজনে পূর্ববর্তী বছরের C বা D পাওয়া বিষয়ে মানোন্নয়ন পরীক্ষা দেওয়ার পরামর্শ রইল।';
    }} else {{
      targetBadge.classList.add('htbd-target-impossible');
      targetBadge.textContent = 'অসম্ভব (মানোন্নয়ন পরীক্ষা দিন)';
      targetAdvice.textContent = 'গাণিতিকভাবে ৪.০০ এর বেশি জিপিএ তোলা অসম্ভব। পূর্ববর্তী বর্ষগুলোর খারাপ হওয়া বিষয়ের মানোন্নয়ন (Improvement) পরীক্ষা দেওয়া ছাড়া ৩.০০ স্পর্শ করা সম্ভব নয়।';
    }}
  }}

  // ---------------------------------------------------------------------------
  // MODE 4: IMPROVEMENT SIMULATOR
  // ---------------------------------------------------------------------------
  const impCurrentGpa = document.getElementById('imp-current-gpa');
  const impNewGpa = document.getElementById('imp-new-gpa');
  const impDeltaGpa = document.getElementById('imp-delta-gpa');
  const impCoursesList = document.getElementById('imp-courses-list');
  const btnAddImpCourse = document.getElementById('btn-add-imp-course');

  function createImpRow(name = '', oldGp = '', newGp = '') {{
    const row = document.createElement('div');
    row.className = 'imp-course-row';

    const oldVal = (oldGp !== '' && !isNaN(oldGp)) ? parseFloat(oldGp).toFixed(2) : '';
    const newVal = (newGp !== '' && !isNaN(newGp)) ? parseFloat(newGp).toFixed(2) : '';

    row.innerHTML = `
      <div class="imp-top">
        <div class="imp-name-wrap">
          <input type="text" class="imp-name" placeholder="কোর্স নাম / কোড" value="${{name}}" style="padding: 7px 10px; border: 1px solid #cbd5e1; border-radius: 6px; font-size: 13px; box-sizing: border-box; width: 100%;" />
        </div>
        <div class="imp-del-wrap">
          <button type="button" class="btn-del-imp" title="মুছুন">×</button>
        </div>
      </div>
      <div class="imp-bottom">
        <div class="imp-col imp-col-old">
          <span class="imp-label">পূর্বের পয়েন্ট (GP)</span>
          <input type="number" class="imp-old-gp" min="0.00" max="4.00" step="0.01" value="${{oldVal}}" placeholder="2.00" style="padding: 7px 4px; border: 1px solid #cbd5e1; border-radius: 6px; font-size: 13.5px; font-weight: 700; text-align: center; box-sizing: border-box; width: 100%;" title="পূর্বের গ্রেড পয়েন্ট" />
        </div>
        <div class="imp-col imp-col-new">
          <span class="imp-label">টার্গেট পয়েন্ট (সর্বোচ্চ ৩.২৫)</span>
          <input type="number" class="imp-new-gp" min="0.00" max="3.25" step="0.01" value="${{newVal}}" placeholder="3.25" style="padding: 7px 4px; border: 1px solid #86efac; border-radius: 6px; font-size: 13.5px; font-weight: 700; color: #15803d; text-align: center; box-sizing: border-box; width: 100%;" title="প্রত্যাশিত নতুন পয়েন্ট (সর্বোচ্চ ৩.২৫)" />
        </div>
      </div>
    `;

    row.querySelector('.imp-old-gp').addEventListener('input', calculateImprovementMode);
    row.querySelector('.imp-new-gp').addEventListener('input', calculateImprovementMode);
    row.querySelector('.btn-del-imp').addEventListener('click', () => {{
      row.remove();
      calculateImprovementMode();
    }});

    impCoursesList.appendChild(row);
  }}

  impCurrentGpa.addEventListener('input', calculateImprovementMode);
  if (btnAddImpCourse) {{
    btnAddImpCourse.addEventListener('click', () => {{
      const count = document.querySelectorAll('.imp-course-row').length + 1;
      createImpRow('কোর্স ' + (count < 10 ? '০' : '') + count, '', '');
      calculateImprovementMode();
    }});
  }}

  function calculateImprovementMode() {{
    const currentGpa = parseFloat(impCurrentGpa.value) || 2.65;
    const defaultCredits = 32;
    let oldPoints = currentGpa * defaultCredits;
    let gainedPoints = 0;

    const impRows = document.querySelectorAll('.imp-course-row');
    impRows.forEach(r => {{
      const oldRaw = r.querySelector('.imp-old-gp').value.trim();
      const newRaw = r.querySelector('.imp-new-gp').value.trim();

      if (oldRaw !== '' && newRaw !== '') {{
        const oldGp = parseFloat(oldRaw) || 0;
        let newGp = parseFloat(newRaw) || 0;
        if (newGp > 3.25) newGp = 3.25; // NU B+ ordinance cap
        const cr = 4; // standard 4 credit
        if (newGp > oldGp) {{
          gainedPoints += (newGp - oldGp) * cr;
        }}
      }}
    }});

    const updatedPoints = oldPoints + gainedPoints;
    const finalGpa = updatedPoints / defaultCredits;
    const delta = finalGpa - currentGpa;

    impNewGpa.textContent = finalGpa.toFixed(2);
    impDeltaGpa.textContent = (delta >= 0 ? '+' : '') + delta.toFixed(2) + ' GPA';
  }}

  // ---------------------------------------------------------------------------
  // OFFICIAL ACADEMIC TRANSCRIPT & 1-PAGE PDF PRINT ENGINE
  // ---------------------------------------------------------------------------
  const btnPrint = document.getElementById('btn-print-transcript');
  const transcriptModal = document.getElementById('htbd-transcript-modal');
  const btnCloseModal = document.getElementById('btn-close-modal');
  const btnTriggerPdfPrint = document.getElementById('btn-trigger-pdf-print');

  const modalInpName = document.getElementById('modal-inp-name');
  const modalInpCollege = document.getElementById('modal-inp-college');
  const modalInpSession = document.getElementById('modal-inp-session');

  const certStudentName = document.getElementById('cert-student-name');
  const certCollegeName = document.getElementById('cert-college-name');
  const certRegSession = document.getElementById('cert-reg-session');
  const certProgramName = document.getElementById('cert-program-name');
  const certTotalCredits = document.getElementById('cert-total-credits');
  const certTotalPoints = document.getElementById('cert-total-points');
  const certCgpa = document.getElementById('cert-cgpa');
  const certDivision = document.getElementById('cert-division');
  const certTableBody = document.getElementById('cert-table-body');
  const certFootCredits = document.getElementById('cert-foot-credits');
  const certFootCgpa = document.getElementById('cert-foot-cgpa');
  const certFootPoints = document.getElementById('cert-foot-points');
  const certRefNo = document.getElementById('cert-ref-no');
  const certIssueDate = document.getElementById('cert-issue-date');

  // Open Modal & Populate Certificate
  btnPrint.addEventListener('click', () => {{
    populateCertificateData();
    transcriptModal.style.display = 'block';
    document.body.style.overflow = 'hidden'; // prevent bg scroll
  }});

  // Open Modal & Populate Certificate
  btnPrint.addEventListener('click', () => {{
    populateCertificateData();
    scrubEntities(document.getElementById('htbd-transcript-modal'));
    transcriptModal.style.display = 'block';
    document.body.style.overflow = 'hidden'; // prevent bg scroll
  }});

  // Close Modal
  function closeModal() {{
    transcriptModal.style.display = 'none';
    document.body.style.overflow = '';
  }}
  btnCloseModal.addEventListener('click', closeModal);
  transcriptModal.addEventListener('click', (e) => {{
    if (e.target === transcriptModal) closeModal();
  }});

  // Live Input Sync
  modalInpName.addEventListener('input', () => {{
    certStudentName.textContent = modalInpName.value.trim() || _bn('পরীক্ষার্থী (Examinee)');
    scrubEntities(certStudentName);
  }});
  modalInpCollege.addEventListener('input', () => {{
    certCollegeName.textContent = modalInpCollege.value.trim() || _bn('জাতীয় বিশ্ববিদ্যালয় অধিভুক্ত কলেজ');
    scrubEntities(certCollegeName);
  }});
  modalInpSession.addEventListener('input', () => {{
    certRegSession.textContent = modalInpSession.value.trim() || _bn('২০২০-২১ (নিয়মিত)');
    scrubEntities(certRegSession);
  }});

  // Pure deterministic Bengali numeral and date converter
  function toBnDigits(num) {{
    const bnDigits = ['০', '১', '২', '৩', '৪', '৫', '৬', '৭', '৮', '৯'];
    return String(num).replace(/[0-9]/g, d => _bn(bnDigits[d]));
  }}

  function getBnDateString(date) {{
    const bnMonths = ['জানুয়ারি', 'ফেব্রুয়ারি', 'মার্চ', 'এপ্রিল', 'মে', 'জুন', 'জুলাই', 'আগস্ট', 'সেপ্টেম্বর', 'অক্টোবর', 'নভেম্বর', 'ডিসেম্বর'];
    const day = toBnDigits(date.getDate());
    const month = _bn(bnMonths[date.getMonth()]);
    const year = toBnDigits(date.getFullYear());
    return _bn(day + ' ' + month + ', ' + year);
  }}

  function populateCertificateData() {{
    const now = new Date();
    const dateFormatted = getBnDateString(now);
    const randomRef = 'Ref: NU-' + now.getFullYear() + '-' + Math.floor(10000 + Math.random() * 90000);
    certRefNo.textContent = _bn(randomRef);
    certIssueDate.textContent = _bn('তারিখ: ' + dateFormatted);

    // Student identity
    certStudentName.textContent = modalInpName.value.trim() || _bn('পরীক্ষার্থী (Examinee)');
    certCollegeName.textContent = modalInpCollege.value.trim() || _bn('জাতীয় বিশ্ববিদ্যালয় অধিভুক্ত কলেজ');
    certRegSession.textContent = modalInpSession.value.trim() || _bn('২০২০-২১ (নিয়মিত)');

    // Degree Name
    let progName = _bn('স্নাতক (সম্মান) চার বছর');
    if (currentProgram === 'degree') progName = _bn('ডিগ্রি (পাস) তিন বছর');
    else if (currentProgram === 'masters') progName = _bn('মাস্টার্স রেগুলার / প্রিলিমিনারি');
    certProgramName.textContent = _bn(progName);

    // CGPA & Metrics
    const cgpa = parseFloat(dashCgpaVal.textContent) || 0;
    const totalCredits = dashTotalCredits.textContent;
    const totalPoints = dashTotalPoints.textContent;
    const divText = getDivisionText(cgpa, parseFloat(totalCredits) || 0);

    certTotalCredits.textContent = totalCredits;
    certTotalPoints.textContent = totalPoints;
    certCgpa.textContent = cgpa.toFixed(2);
    certDivision.textContent = _bn(divText);

    certFootCredits.textContent = totalCredits;
    certFootCgpa.textContent = cgpa.toFixed(2);
    certFootPoints.textContent = totalPoints;

    // Table Rows
    certTableBody.innerHTML = '';
    const yearLabels = {{
      '1': {{ bn: _bn('১ম বর্ষ বার্ষিক পরীক্ষা'), en: '1st Year Final Examination' }},
      '2': {{ bn: _bn('২য় বর্ষ বার্ষিক পরীক্ষা'), en: '2nd Year Final Examination' }},
      '3': {{ bn: _bn('৩য় বর্ষ বার্ষিক পরীক্ষা'), en: '3rd Year Final Examination' }},
      '4': {{ bn: _bn('৪র্থ বর্ষ বার্ষিক পরীক্ষা'), en: '4th Year Final Examination' }}
    }};

    if (currentMode === 'mode-year') {{
      let rowIdx = 1;
      yearCards.forEach(card => {{
        const yr = card.dataset.year;
        if (currentProgram === 'degree' && parseInt(yr) > 3) return;
        if (currentProgram === 'masters' && parseInt(yr) > 2) return;

        const rawGpa = card.querySelector('.htbd-yr-gpa').value.trim();
        const gpa = rawGpa !== '' ? parseFloat(rawGpa).toFixed(2) : '0.00';
        const cr = card.querySelector('.htbd-yr-credit').value || '32';
        const pts = (parseFloat(gpa) * parseFloat(cr)).toFixed(2);

        let lg = 'F';
        const pNum = parseFloat(gpa);
        if      (pNum >= 4.00) lg = 'A+';
        else if (pNum >= 3.75) lg = 'A';
        else if (pNum >= 3.50) lg = 'A-';
        else if (pNum >= 3.25) lg = 'B+';
        else if (pNum >= 3.00) lg = 'B';
        else if (pNum >= 2.75) lg = 'B-';
        else if (pNum >= 2.50) lg = 'C+';
        else if (pNum >= 2.25) lg = 'C';
        else if (pNum >= 2.00) lg = 'D';

        const yInfo = yearLabels[yr] || {{ bn: toBnDigits(yr) + 'ম বর্ষ বার্ষিক পরীক্ষা', en: yr + 'th Year Final Examination' }};
        const examTitle = yInfo.bn + ' (' + yInfo.en + ')';
        const rowBnIdx = toBnDigits(rowIdx < 10 ? '0' + rowIdx : rowIdx);

        const tr = document.createElement('tr');
        tr.style.background = (rowIdx % 2 === 0) ? '#f8fafc' : '#ffffff';
        tr.innerHTML = `
          <td style="border: 1px solid #cbd5e1; padding: 5px 6px; text-align: center;">${{rowBnIdx}}</td>
          <td style="border: 1px solid #cbd5e1; padding: 5px 8px; font-weight: 600;">${{examTitle}}</td>
          <td style="border: 1px solid #cbd5e1; padding: 5px 6px; text-align: center;">${{cr}}</td>
          <td style="border: 1px solid #cbd5e1; padding: 5px 6px; text-align: center; font-weight: 700; color: #1e3a8a;">${{lg}}</td>
          <td style="border: 1px solid #cbd5e1; padding: 5px 6px; text-align: center; font-weight: 700;">${{gpa}}</td>
          <td style="border: 1px solid #cbd5e1; padding: 5px 6px; text-align: center; font-weight: 600;">${{pts}}</td>
        `;
        certTableBody.appendChild(tr);
        rowIdx++;
      }});
    }} else {{
      const rows = document.querySelectorAll('.htbd-course-row');
      let rowIdx = 1;
      rows.forEach(r => {{
        const rowBnIdx = toBnDigits(rowIdx < 10 ? '0' + rowIdx : rowIdx);
        const name = r.querySelector('.c-name').value.trim() || ('কোর্স ' + rowBnIdx);
        const cr = r.querySelector('.c-credit').value;
        const gr = r.querySelector('.c-grade').value || '-';
        const rawGp = r.querySelector('.c-point').value.trim();
        const gp = rawGp !== '' ? parseFloat(rawGp).toFixed(2) : '0.00';
        const pts = (parseFloat(cr) * parseFloat(gp)).toFixed(2);

        const tr = document.createElement('tr');
        tr.style.background = (rowIdx % 2 === 0) ? '#f8fafc' : '#ffffff';
        tr.innerHTML = `
          <td style="border: 1px solid #cbd5e1; padding: 5px 6px; text-align: center;">${{rowBnIdx}}</td>
          <td style="border: 1px solid #cbd5e1; padding: 5px 8px; font-weight: 600;">${{name}}</td>
          <td style="border: 1px solid #cbd5e1; padding: 5px 6px; text-align: center;">${{cr}}</td>
          <td style="border: 1px solid #cbd5e1; padding: 5px 6px; text-align: center; font-weight: 700; color: #1e3a8a;">${{gr}}</td>
          <td style="border: 1px solid #cbd5e1; padding: 5px 6px; text-align: center; font-weight: 700;">${{gp}}</td>
          <td style="border: 1px solid #cbd5e1; padding: 5px 6px; text-align: center; font-weight: 600;">${{pts}}</td>
        `;
        certTableBody.appendChild(tr);
        rowIdx++;
      }});
    }}
    scrubEntities(document.getElementById('htbd-transcript-modal'));
  }}

  // ---------------------------------------------------------------------------
  // ISOLATED IFRAME PRINT ENGINE (GUARANTEED 1-PAGE A4 PDF, ZERO OVERFLOW)
  // ---------------------------------------------------------------------------
  btnTriggerPdfPrint.addEventListener('click', () => {{
    const paper = document.getElementById('htbd-certificate-paper');
    if (!paper) return;
    scrubEntities(paper);

    // Create an invisible, isolated iframe
    const iframe = document.createElement('iframe');
    iframe.style.position = 'fixed';
    iframe.style.right = '0';
    iframe.style.bottom = '0';
    iframe.style.width = '0';
    iframe.style.height = '0';
    iframe.style.border = '0';
    iframe.style.visibility = 'hidden';
    document.body.appendChild(iframe);

    const doc = iframe.contentWindow.document;
    doc.open();
    doc.write(`<!DOCTYPE html>
<html lang="bn">
<head>
  <meta charset="utf-8">
  <title>NU_Academic_Transcript_2026</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Bengali:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://fonts.maateen.me/solaiman-lipi/font.css">
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
    @page {{
      size: A4 portrait;
      margin: 8mm 10mm;
    }}
    * {{
      box-sizing: border-box;
      -webkit-print-color-adjust: exact !important;
      print-color-adjust: exact !important;
      font-family: 'SolaimanLipi', 'Noto Sans Bengali', Arial, sans-serif !important;
    }}
    body {{
      margin: 0;
      padding: 0;
      background: #ffffff !important;
      color: #0c2340 !important;
      font-family: 'SolaimanLipi', 'Noto Sans Bengali', Arial, sans-serif !important;
    }}
    #htbd-certificate-paper {{
      width: 100% !important;
      max-width: 100% !important;
      box-shadow: none !important;
      padding: 16px !important;
      border: 3px solid #1e3a8a !important;
      border-radius: 6px !important;
    }}
    .htbd-cert-inner-frame {{
      border: 1.5px solid #b45309 !important;
      padding: 14px 16px !important;
    }}
    table {{
      page-break-inside: avoid;
    }}
  </style>
</head>
<body>
  ${{paper.outerHTML}}
</body>
</html>`);
    doc.close();

    // Trigger Print once styles and fonts are 100% loaded
    const triggerPrint = () => {{
      iframe.contentWindow.focus();
      iframe.contentWindow.print();
      setTimeout(() => iframe.remove(), 4000);
    }};

    if (doc.fonts && doc.fonts.ready) {{
      doc.fonts.ready.then(() => {{
        setTimeout(triggerPrint, 250);
      }}).catch(() => {{
        setTimeout(triggerPrint, 600);
      }});
    }} else {{
      setTimeout(triggerPrint, 700);
    }}
  }});

  // Copy Summary
  document.getElementById('btn-copy-summary').addEventListener('click', () => {{
    const cgpa = dashCgpaVal.textContent;
    const div = dashDivisionBadge.innerText;
    const cr = dashTotalCredits.textContent;
    const text = `জাতীয় বিশ্ববিদ্যালয় সিজিপিএ ক্যালকুলেটর রেজাল্ট:\n• সিজিপিএ: ${{cgpa}} / 4.00\n• মূল্যায়ন: ${{div}}\n• মোট ক্রেডিট: ${{cr}}\nহিসাব করুন: https://www.helptrickbd.com/p/nu-cgpa-calculator.html`;

    navigator.clipboard.writeText(text).then(() => {{
      alert('রেজাল্ট সামারি কপি হয়েছে!');
    }});
  }});

  // ---------------------------------------------------------------------------
  // LOCALSTORAGE PERSISTENCE
  // ---------------------------------------------------------------------------
  function saveState() {{
    const data = {{
      program: currentProgram,
      years: []
    }};
    yearCards.forEach(c => {{
      data.years.push({{
        gpa: c.querySelector('.htbd-yr-gpa').value,
        credit: c.querySelector('.htbd-yr-credit').value
      }});
    }});
    try {{
      localStorage.setItem('htbd_nu_cgpa_data', JSON.stringify(data));
    }} catch (e) {{}}
  }}

  function loadState() {{
    try {{
      const raw = localStorage.getItem('htbd_nu_cgpa_data');
      if (raw) {{
        const data = JSON.parse(raw);
        if (data.years && data.years.length) {{
          data.years.forEach((item, i) => {{
            if (yearCards[i]) {{
              if (item.gpa) {{
                yearCards[i].querySelector('.htbd-yr-gpa').value = item.gpa;
                yearCards[i].querySelector('.htbd-yr-range').value = item.gpa;
              }}
              if (item.credit) {{
                yearCards[i].querySelector('.htbd-yr-credit').value = item.credit;
              }}
            }}
          }});
        }}
      }}
    }} catch (e) {{}}
  }}

  // Initial Boot
  scrubEntities(document.getElementById('htbd-nu-cgpa-app'));
  scrubEntities(document.getElementById('htbd-transcript-modal'));
  loadState();
  if (btnResetCourses) btnResetCourses.click(); // load empty initial course rows
  createImpRow('কোর্স ০১', '', '');
  createImpRow('কোর্স ০২', '', '');
  calculateYearMode();
  calculateTargetMode();
  calculateImprovementMode();
  scrubEntities(document.getElementById('htbd-nu-cgpa-app'));
  scrubEntities(document.getElementById('htbd-transcript-modal'));

}})();
</script>

<!-- ========================================================================== -->
<!-- JSON-LD SCHEMA MICRODATA: BlogPosting & FAQPage                            -->
<!-- ========================================================================== -->
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "জাতীয় বিশ্ববিদ্যালয় সিজিপিএ ক্যালকুলেটর ও গ্রেডিং গাইড ২০২৬",
  "description": "জাতীয় বিশ্ববিদ্যালয় অনার্স, ডিগ্রি পাস ও মাস্টার্স শিক্ষার্থীদের জন্য আধুনিক সিজিপিএ ক্যালকুলেটর ২০২৬। ডিপার্টমেন্ট সিলেবাস অটো-লোড, স্মার্ট রেজাল্ট পেস্ট পার্সার, টার্গেট ফার্স্ট ক্লাস প্ল্যানার ও প্রাতিষ্ঠানিক ১-পাতা A4 ট্রান্সক্রিপ্ট প্রিন্ট সুবিধা।",
  "image": "https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/posts/nu_cgpa_calculator_honours_degree_masters_2026.webp",
  "datePublished": "2026-10-03T14:30:00+06:00",
  "dateModified": "2026-10-03T16:50:00+06:00",
  "author": {{
    "@type": "Person",
    "name": "ফারুক স্যার (মো. ওমর ফারুক)",
    "jobTitle": "শিক্ষাবিদ ও অ্যাকাডেমিক গবেষক",
    "url": "https://www.helptrickbd.com/p/about-us.html"
  }},
  "publisher": {{
    "@type": "Organization",
    "name": "HelpTrickBD",
    "url": "https://www.helptrickbd.com/",
    "logo": {{
      "@type": "ImageObject",
      "url": "https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/logo/helptrickbd_logo.webp"
    }}
  }},
  "mainEntityOfPage": {{
    "@type": "WebPage",
    "@id": "https://www.helptrickbd.com/p/nu-cgpa-calculator.html"
  }}
}}
</script>

<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{
      "@type": "Question",
      "name": "অনার্স ১ম থেকে ৪র্থ বর্ষ পর্যন্ত মোট ক্রেডিট কত?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "জাতীয় বিশ্ববিদ্যালয়ের চার বছর মেয়াদি অনার্স কোর্সে সাধারণত প্রতি বর্ষে ৩২ ক্রেডিট করে ৪ বছরে সর্বমোট ১২৮ ক্রেডিট সম্পন্ন করতে হয়।"
      }}
    }},
    {{
      "@type": "Question",
      "name": "সিজিপিএ কত পেলে ১ম শ্রেণি বা ফার্স্ট ক্লাস পাওয়া যায়?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "জাতীয় বিশ্ববিদ্যালয়ের নিয়ম অনুযায়ী ফাইনাল সিজিপিএ ৩.০০ (CGPA 3.00) বা তার বেশি অর্জন করলে তা প্রথম শ্রেণি (First Class) হিসেবে গণ্য হয়।"
      }}
    }},
    {{
      "@type": "Question",
      "name": "অনার্স ২য় বর্ষের ইংরেজি আবশ্যিক ফেল করলে কি প্রমোশন আটকে যাবে?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "না, ইংরেজি আবশ্যিক বিষয়ে ফেল করলেও অন্য প্রধান ৩টি বিষয়ে পাস থাকলে ৩য় বর্ষে প্রমোশন দেওয়া হবে। তবে অনার্স শেষ করার পূর্বে অবশ্যই এই নন-ক্রেডিট বিষয়ে পাস করতে হবে।"
      }}
    }},
    {{
      "@type": "Question",
      "name": "ইমপ্রুভমেন্ট পরীক্ষা দিলে সর্বোচ্চ কত গ্রেড পাওয়া যায়?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "জাতীয় বিশ্ববিদ্যালয়ের অর্ডিন্যান্স অনুযায়ী মানোন্নয়ন পরীক্ষায় কোনো বিষয়ে ৯০ নম্বর পেলেও সর্বোচ্চ B+ গ্রেড (গ্রেড পয়েন্ট ৩.২৫) প্রদান করা হয়।"
      }}
    }},
    {{
      "@type": "Question",
      "name": "কোনো বর্ষে এফ (F) গ্রেড থাকলে কি সিজিপিএ হিসাব করা সম্ভব?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "হ্যাঁ, তবে F গ্রেডের গ্রেড পয়েন্ট হলো ০.০০। এটি মোট ক্রেডিটের সাথে যুক্ত হয়ে গড় সিজিপিএ ব্যাপকভাবে হ্রাস করে। পরবর্তী বর্ষে পরীক্ষা দিয়ে F গ্রেড ক্লিয়ার করলে নতুন গ্রেড পয়েন্ট যুক্ত হয়ে সিজিপিএ বৃদ্ধি পাবে।"
      }}
    }},
    {{
      "@type": "Question",
      "name": "লেটার গ্রেড ছাড়া কি সরাসরি দশমিক বা কাস্টম পয়েন্ট দিয়ে সিজিপিএ হিসাব করা যায়?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "হ্যাঁ, হেল্পট্রিকবিডি ক্যালকুলেটরে প্রতিটি বিষয়ের জন্য লেটার গ্রেডের পাশাপাশি সরাসরি পয়েন্ট (GP) ঘর রয়েছে। আপনি যেকোনো ফ্র্যাকশনাল বা সুনির্দিষ্ট পয়েন্ট সরাসরি লিখে নির্ভুল সিজিপিএ গণনা করতে পারবেন।"
      }}
    }}
  ]
}}
</script>
'''

    with open(HTML_PATH, "w", encoding="utf-8") as f:
        f.write(html_content)

    meta = {
        "title": "জাতীয় বিশ্ববিদ্যালয় সিজিপিএ ক্যালকুলেটর ও গ্রেডিং গাইড ২০২৬",
        "english_slug": "nu-cgpa-calculator",
        "type": "page",
        "category": "National University",
        "labels": ["National University", "Education Guide", "Tools"],
        "status": "draft",
        "meta_description": "জাতীয় বিশ্ববিদ্যালয় অনার্স, ডিগ্রি পাস ও মাস্টার্স শিক্ষার্থীদের জন্য আধুনিক সিজিপিএ ক্যালকুলেটর ২০২৬। ডিপার্টমেন্ট সিলেবাস অটো-লোড, স্মার্ট রেজাল্ট পেস্ট পার্সার, টার্গেট ফার্স্ট ক্লাস প্ল্যানার ও প্রাতিষ্ঠানিক ১-পাতা A4 ট্রান্সক্রিপ্ট প্রিন্ট সুবিধা।",
        "search_description": "জাতীয় বিশ্ববিদ্যালয় সিজিপিএ ক্যালকুলেটর ২০২৬: অনার্স ও ডিগ্রি জিপিএ হিসাব, টার্গেট প্ল্যানার এবং ১-পাতা A4 ট্রান্সক্রিপ্ট প্রিন্ট সুবিধা।",
        "hero_banner": "https://cdn.jsdelivr.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/images/posts/nu_cgpa_calculator_honours_degree_masters_2026.webp",
        "word_count": len(html_content.split())
    }

    with open(META_PATH, "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)

    print("=" * 70)
    print("NU CGPA CALCULATOR MASTER PAGE GENERATED SUCCESSFULLY!")
    print(f"HTML Output: {HTML_PATH}")
    print(f"Meta Output: {META_PATH}")
    print(f"Approx Word Count: {meta['word_count']}")
    print("=" * 70)

if __name__ == "__main__":
    generate_page()
