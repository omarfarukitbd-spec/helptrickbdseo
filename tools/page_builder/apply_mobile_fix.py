#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
apply_mobile_fix.py
-------------------
Applies mobile responsive + point-to-grade auto-sync fix to build script.
"""

import re

TARGET = r"e:\Helptrickbd\tools\page_builder\build_nu_cgpa_calculator_page.py"

with open(TARGET, "r", encoding="utf-8") as f:
    content = f.read()

# ============================================================
# FIX 1: Replace CSS style block with mobile-responsive version
# ============================================================
OLD_CSS = """<style>
/* Full-Width Canvas for NU CGPA Calculator Page (Hides sidebar and gives 100% width) */
.static_page #feed-view, .item-view #feed-view, #feed-view {{
  width: 100% !important;
  max-width: 100% !important;
  float: none !important;
}}
.static_page #sidebar-container, .item-view #sidebar-container, #sidebar-container {{
  display: none !important;
}}
.htbd-calc-grid {{
  display: grid;
  grid-template-columns: 1.15fr 0.85fr;
  gap: 24px;
}}
@media (max-width: 880px) {{
  .htbd-calc-grid {{
    grid-template-columns: 1fr;
  }}
}}
</style>"""

NEW_CSS = """<style>
/* Full-Width Canvas for NU CGPA Calculator Page */
.static_page #feed-view, .item-view #feed-view, #feed-view {{
  width: 100% !important;
  max-width: 100% !important;
  float: none !important;
}}
.static_page #sidebar-container, .item-view #sidebar-container, #sidebar-container {{
  display: none !important;
}}
.htbd-calc-grid {{
  display: grid;
  grid-template-columns: 1.15fr 0.85fr;
  gap: 24px;
}}
@media (max-width: 880px) {{
  .htbd-calc-grid {{
    grid-template-columns: 1fr;
  }}
}}
/* ===== COURSE ROW: DESKTOP (5-column grid via CSS class) ===== */
.htbd-course-row {{
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  padding: 8px 10px;
  display: grid;
  grid-template-columns: 2.4fr 0.85fr 1.3fr 1fr 36px;
  gap: 6px;
  align-items: center;
}}
.htbd-course-header {{
  display: grid;
  grid-template-columns: 2.4fr 0.85fr 1.3fr 1fr 36px;
  gap: 6px;
  padding: 6px 10px;
  background: #e2e8f0;
  border-radius: 6px;
  font-size: 12.5px;
  font-weight: 700;
  color: #334155;
  margin-bottom: 8px;
}}
/* ===== COURSE ROW: MOBILE (stacked, name on top, controls in a row) ===== */
@media (max-width: 600px) {{
  #htbd-nu-cgpa-app {{
    padding: 14px 10px;
    border-radius: 10px;
  }}
  .htbd-course-header {{
    display: none !important;
  }}
  .htbd-course-row {{
    display: block;
    padding: 10px 12px;
    border-left: 4px solid #2563eb;
  }}
  .htbd-course-row .cr-name {{
    display: block;
    margin-bottom: 8px;
  }}
  .htbd-course-row .cr-name input {{
    width: 100%;
    box-sizing: border-box;
    font-size: 14px;
    font-weight: 600;
  }}
  .htbd-course-row .cr-controls {{
    display: grid;
    grid-template-columns: 1fr 1fr 1fr 36px;
    gap: 6px;
    align-items: end;
  }}
  .htbd-course-row .cr-label {{
    display: block;
    font-size: 9.5px;
    font-weight: 700;
    color: #64748b;
    text-transform: uppercase;
    margin-bottom: 2px;
    letter-spacing: 0.3px;
  }}
  .htbd-course-row .cr-controls select,
  .htbd-course-row .cr-controls input[type="number"] {{
    width: 100%;
    box-sizing: border-box;
    font-size: 12px;
  }}
  .htbd-calc-grid {{
    gap: 16px;
  }}
  .htbd-tab-btn {{
    min-width: 110px !important;
    font-size: 13px !important;
    padding: 9px 10px !important;
  }}
}}
/* ===== POINT <-> GRADE SYNC VISUAL FEEDBACK ===== */
.c-point.gp-synced {{
  border-color: #22c55e !important;
  background: #f0fdf4 !important;
  transition: all 0.3s ease;
}}
.c-grade.grade-synced {{
  border-color: #2563eb !important;
  background: #eff6ff !important;
  transition: all 0.3s ease;
}}
</style>"""

assert OLD_CSS in content, "CSS block not found!"
content = content.replace(OLD_CSS, NEW_CSS, 1)
print("✅ Fix 1: Mobile responsive CSS injected")

# ============================================================
# FIX 2: Replace static course header div with CSS class
# ============================================================
OLD_HEADER = '''        <div style="display: grid; grid-template-columns: 2.2fr 0.9fr 1.2fr 1fr 34px; gap: 6px; padding: 6px 10px; background: #e2e8f0; border-radius: 6px; font-size: 12.5px; font-weight: 700; color: #334155; margin-bottom: 8px;">
          <div>코스 코드 및 名前</div>'''

# use a robust search for the course header div
HEADER_OLD_PATTERN = (
    '        <div style="display: grid; grid-template-columns: 2.2fr 0.9fr 1.2fr 1fr 34px;'
    ' gap: 6px; padding: 6px 10px; background: #e2e8f0; border-radius: 6px; font-size: 12.5px;'
    ' font-weight: 700; color: #334155; margin-bottom: 8px;">'
)

HEADER_NEW_START = '        <div class="htbd-course-header">'

if HEADER_OLD_PATTERN in content:
    content = content.replace(HEADER_OLD_PATTERN, HEADER_NEW_START, 1)
    print("✅ Fix 2: Course header div replaced with CSS class")
else:
    print("⚠️  Fix 2: Header pattern not found (may already be fixed)")

# ============================================================
# FIX 3: Replace createCourseRow JS function with mobile-aware version
# ============================================================
OLD_FUNC_START = "  function createCourseRow(code = '', name = '', credit = 4, selectedGrade = '', exactPoint = null) {{"
OLD_FUNC_END = "    coursesContainer.appendChild(row);\n  }}"

# Find start and end
start_idx = content.find(OLD_FUNC_START)
end_idx = content.find(OLD_FUNC_END, start_idx)
assert start_idx != -1, "createCourseRow function start not found!"
assert end_idx != -1, "createCourseRow function end not found!"
end_idx += len(OLD_FUNC_END)  # include the closing }}

NEW_FUNC = """  function createCourseRow(code = '', name = '', credit = 4, selectedGrade = '', exactPoint = null) {{
    const row = document.createElement('div');
    row.className = 'htbd-course-row';

    let initialPoint = '';
    if (exactPoint !== null && exactPoint !== '' && !isNaN(exactPoint)) {{
      initialPoint = parseFloat(exactPoint).toFixed(2);
    }} else if (selectedGrade && GRADE_SCALE[selectedGrade] !== undefined) {{
      initialPoint = GRADE_SCALE[selectedGrade].toFixed(2);
    }}

    const displayName = name ? code + ' - ' + name : code;
    const cOpts = [
      [4, '\u09ea \u0995\u09cd\u09b0\u09c7\u09a1\u09bf\u099f'],
      [3, '\u09e9 \u0995\u09cd\u09b0\u09c7\u09a1\u09bf\u099f'],
      [2, '\u09e8 \u0995\u09cd\u09b0\u09c7\u09a1\u09bf\u099f'],
      [0, '\u09a8\u09a8-\u0995\u09cd\u09b0\u09c7\u09a1\u09bf\u099f']
    ].map(([v,t]) => `<option value="${{v}}" ${{credit === v ? 'selected' : ''}}>${{t}}</option>`).join('');

    const gOpts = [
      ['', '-- \u0997\u09cd\u09b0\u09c7\u09a1 --'],
      ['A+','A+ (4.00)'],['A','A (3.75)'],['A-','A- (3.50)'],
      ['B+','B+ (3.25)'],['B','B (3.00)'],['B-','B- (2.75)'],
      ['C+','C+ (2.50)'],['C','C (2.25)'],['D','D (2.00)'],['F','F (0.00)']
    ].map(([v,t]) => `<option value="${{v}}" ${{selectedGrade === v ? 'selected' : ''}}>${{t}}</option>`).join('');

    row.innerHTML = `
      <div class="cr-name">
        <input type="text" class="c-name" value="${{displayName}}"
          placeholder="\u0995\u09cb\u09b0\u09cd\u09b8 \u0995\u09cb\u09a1 \u0993 \u09a8\u09be\u09ae"
          style="width:100%;box-sizing:border-box;padding:6px 8px;border:1px solid #cbd5e1;border-radius:4px;font-size:13px;" />
      </div>
      <div class="cr-controls">
        <div>
          <span class="cr-label">\u0995\u09cd\u09b0\u09c7\u09a1\u09bf\u099f</span>
          <select class="c-credit" style="width:100%;box-sizing:border-box;padding:6px 2px;border:1px solid #cbd5e1;border-radius:4px;font-size:13px;text-align:center;">
            ${{cOpts}}
          </select>
        </div>
        <div>
          <span class="cr-label">\u09b2\u09c7\u099f\u09be\u09b0 \u0997\u09cd\u09b0\u09c7\u09a1</span>
          <select class="c-grade" style="width:100%;box-sizing:border-box;padding:6px 2px;border:1px solid #cbd5e1;border-radius:4px;font-size:12.5px;font-weight:700;color:#1e3a8a;">
            ${{gOpts}}
          </select>
        </div>
        <div>
          <span class="cr-label">\u09aa\u09af\u09bc\u09c7\u09a8\u09cd\u099f (GP)</span>
          <input type="number" class="c-point"
            min="0.00" max="4.00" step="0.01"
            value="${{initialPoint}}"
            placeholder="\u09a4\u09be\u0987\u09aa \u0995\u09b0\u09c1\u09a8"
            style="width:100%;box-sizing:border-box;padding:6px 4px;border:1.5px solid #94a3b8;border-radius:4px;font-size:13px;font-weight:700;text-align:center;color:#0f172a;background:#f8fafc;"
            title="\u09aa\u09af\u09bc\u09c7\u09a8\u09cd\u099f \u099f\u09be\u0987\u09aa \u0995\u09b0\u09b2\u09c7 \u09b2\u09c7\u099f\u09be\u09b0 \u0997\u09cd\u09b0\u09c7\u09a1 \u0985\u099f\u09cb-\u09b8\u09bf\u09b2\u09c7\u0995\u09cd\u099f \u09b9\u09ac\u09c7" />
        </div>
        <div style="text-align:center;padding-top:2px;">
          <span class="cr-label" style="visibility:hidden;">X</span>
          <button type="button" class="btn-del-course"
            style="background:#fee2e2;color:#ef4444;border:none;width:30px;height:30px;border-radius:6px;cursor:pointer;font-size:16px;font-weight:bold;display:block;">\xd7</button>
        </div>
      </div>
    `;

    const cCredit = row.querySelector('.c-credit');
    const cGrade  = row.querySelector('.c-grade');
    const cPoint  = row.querySelector('.c-point');

    // Grade dropdown -> Point input (one-way sync)
    cGrade.addEventListener('change', () => {{
      const gr = cGrade.value;
      if (gr && GRADE_SCALE[gr] !== undefined) {{
        cPoint.value = GRADE_SCALE[gr].toFixed(2);
        cPoint.classList.add('gp-synced');
        setTimeout(() => cPoint.classList.remove('gp-synced'), 700);
      }} else if (gr === '') {{
        cPoint.value = '';
      }}
      calculateSubjectMode();
    }});

    // Point input -> Grade dropdown (auto-select matching letter grade!)
    cPoint.addEventListener('input', () => {{
      const rawVal = cPoint.value.trim();
      if (rawVal === '') {{
        cGrade.value = '';
        calculateSubjectMode();
        return;
      }}
      let p = parseFloat(rawVal);
      if (isNaN(p)) {{ cGrade.value = ''; calculateSubjectMode(); return; }}
      if (p > 4.00) p = 4.00;
      if (p < 0.00) p = 0.00;

      // NU official grading scale
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
      cGrade.classList.add('grade-synced');
      setTimeout(() => cGrade.classList.remove('grade-synced'), 700);
      calculateSubjectMode();
    }});

    cCredit.addEventListener('change', calculateSubjectMode);
    row.querySelector('.btn-del-course').addEventListener('click', () => {{
      row.remove();
      calculateSubjectMode();
    }});

    coursesContainer.appendChild(row);
  }}"""

content = content[:start_idx] + NEW_FUNC + content[end_idx:]
print("✅ Fix 3: createCourseRow replaced with mobile-aware + sync version")

# ============================================================
# WRITE BACK
# ============================================================
with open(TARGET, "w", encoding="utf-8") as f:
    f.write(content)

print(f"\\n✅ All fixes applied! File saved.")
print(f"Total chars: {len(content)}")
