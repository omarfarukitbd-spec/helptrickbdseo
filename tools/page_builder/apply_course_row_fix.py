#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
apply_course_row_fix.py
-----------------------
Replace createCourseRow function with mobile-responsive + point-to-grade sync version.
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')

TARGET = r"e:\Helptrickbd\tools\page_builder\build_nu_cgpa_calculator_page.py"

with open(TARGET, "r", encoding="utf-8") as f:
    content = f.read()

# Locate function boundaries
func_start = content.find('  function createCourseRow(')
func_end_marker = '    coursesContainer.appendChild(row);\n  }}\n\n  function calculateSubjectMode'
func_end_idx = content.find(func_end_marker, func_start)
assert func_end_idx != -1, "End of createCourseRow not found!"
func_end_idx += len('    coursesContainer.appendChild(row);\n  }}')

print(f"Found function: chars {func_start} to {func_end_idx}")

NEW_FUNC = r"""  function createCourseRow(code = '', name = '', credit = 4, selectedGrade = '', exactPoint = null) {{
    const row = document.createElement('div');
    row.className = 'htbd-course-row';

    let initialPoint = '';
    if (exactPoint !== null && exactPoint !== '' && !isNaN(exactPoint)) {{
      initialPoint = parseFloat(exactPoint).toFixed(2);
    }} else if (selectedGrade && GRADE_SCALE[selectedGrade] !== undefined) {{
      initialPoint = GRADE_SCALE[selectedGrade].toFixed(2);
    }}

    const displayName = name ? code + ' - ' + name : code;
    const cOpts = [[4,'\u09ea \u0995\u09cd\u09b0\u09c7\u09a1\u09bf\u099f'],[3,'\u09e9 \u0995\u09cd\u09b0\u09c7\u09a1\u09bf\u099f'],[2,'\u09e8 \u0995\u09cd\u09b0\u09c7\u09a1\u09bf\u099f'],[0,'\u09a8\u09a8-\u0995\u09cd\u09b0\u09c7\u09a1\u09bf\u099f']]
      .map(([v,t]) => `<option value="${{v}}" ${{credit === v ? 'selected' : ''}}>${{t}}</option>`).join('');
    const gOpts = [['','-- \u0997\u09cd\u09b0\u09c7\u09a1 --'],['A+','A+ (4.00)'],['A','A (3.75)'],['A-','A- (3.50)'],
      ['B+','B+ (3.25)'],['B','B (3.00)'],['B-','B- (2.75)'],['C+','C+ (2.50)'],['C','C (2.25)'],['D','D (2.00)'],['F','F (0.00)']]
      .map(([v,t]) => `<option value="${{v}}" ${{selectedGrade === v ? 'selected' : ''}}>${{t}}</option>`).join('');

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
            placeholder="\u099f\u09be\u0987\u09aa \u0995\u09b0\u09c1\u09a8"
            style="width:100%;box-sizing:border-box;padding:6px 4px;border:1.5px solid #94a3b8;border-radius:4px;font-size:13px;font-weight:700;text-align:center;color:#0f172a;background:#f8fafc;"
            title="\u09aa\u09af\u09bc\u09c7\u09a8\u09cd\u099f \u099f\u09be\u0987\u09aa \u0995\u09b0\u09b2\u09c7 \u0997\u09cd\u09b0\u09c7\u09a1 \u0985\u099f\u09cb-\u09b8\u09bf\u09b2\u09c7\u0995\u09cd\u099f \u09b9\u09ac\u09c7" />
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

    // Grade dropdown -> Point input (one-way sync with visual feedback)
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

content = content[:func_start] + NEW_FUNC + content[func_end_idx:]

with open(TARGET, "w", encoding="utf-8") as f:
    f.write(content)

print("DONE - createCourseRow replaced successfully")
print(f"Total chars: {len(content)}")
