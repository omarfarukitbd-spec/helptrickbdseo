import os
import sys
import json
import re
import requests

sys.stdout.reconfigure(encoding='utf-8')

with open('tools/wp_publisher/config.json', 'r', encoding='utf-8') as f:
    cfg = json.load(f)

auth = (cfg['wp_user'], cfg['wp_app_password'])
base_url = cfg['wp_url'].rstrip('/')

# 1. Update Post 1: Primary Scholarship
p1_html_path = 'output_posts/primary-scholarship-exam-routine-2026.html'
with open(p1_html_path, 'r', encoding='utf-8') as f:
    p1_content = f.read()

# Replace PDF link with WordPress hosted official PDF
p1_new_pdf = 'https://www.helptrickbd.com/wp-content/uploads/2026/10/primary_scholarship_policy_routine_2026.pdf'
p1_content_updated = re.sub(
    r'https://cdn\.jsdelivr\.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/pdf/primary/[^\s"\'#]+',
    p1_new_pdf,
    p1_content
)
with open(p1_html_path, 'w', encoding='utf-8') as f:
    f.write(p1_content_updated)
print(f"Updated {p1_html_path} with official PDF URL.")

# 2. Update Post 2: NU Degree 1st Year
p2_html_path = 'output_posts/nu-degree-1st-year-rescheduled-routine-2026.html'
with open(p2_html_path, 'r', encoding='utf-8') as f:
    p2_content = f.read()

p2_new_pdf = 'https://www.helptrickbd.com/wp-content/uploads/2026/10/nu_degree_1st_year_rescheduled_routine_notice.pdf'
p2_content_updated = re.sub(
    r'https://cdn\.jsdelivr\.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/pdf/nu/[^\s"\'#]+',
    p2_new_pdf,
    p2_content
)
with open(p2_html_path, 'w', encoding='utf-8') as f:
    f.write(p2_content_updated)
print(f"Updated {p2_html_path} with official PDF URL.")

# 3. Update Post 3: SSC 2027 Test Exam & Form Fill Up
p3_html_path = 'output_posts/ssc-2027-test-exam-form-fill-up-guide.html'
with open(p3_html_path, 'r', encoding='utf-8') as f:
    p3_content = f.read()

p3_new_pdf = 'https://www.helptrickbd.com/wp-content/uploads/2026/10/ssc_2027_form_fill_up_notice_dhaka_board.pdf'
p3_content_updated = re.sub(
    r'https://cdn\.jsdelivr\.net/gh/omarfarukitbd-spec/helptrickbdseo@main/assets/pdf/ssc/[^\s"\'#]+',
    p3_new_pdf,
    p3_content
)
with open(p3_html_path, 'w', encoding='utf-8') as f:
    f.write(p3_content_updated)
print(f"Updated {p3_html_path} with official PDF URL.")

print("\nAll HTML files updated with authentic official PDF URLs hosted on HelpTrickBD!")
