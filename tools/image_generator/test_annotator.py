#!/usr/bin/env python3
"""
Test script generating a sample annotated tutorial step image.
"""

import os
from PIL import Image, ImageDraw, ImageFont
from tutorial_annotator import annotate_screenshot, annotate_with_html

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
RAW_UI_PATH = os.path.join(PROJECT_ROOT, "assets", "images", "tutorials", "raw_ui_sample.png")
SAMPLE_OUT = os.path.join(PROJECT_ROOT, "assets", "images", "tutorials", "sample_annotated_step1.png")

# Create a clean mock browser window interface (1000x580)
w, h = 1000, 580
ui = Image.new("RGB", (w, h), "#f8fafc")
draw = ImageDraw.Draw(ui)

# Browser header bar
draw.rectangle([0, 0, w, 44], fill="#1e293b")
draw.ellipse([14, 16, 26, 28], fill="#ef4444")
draw.ellipse([34, 16, 46, 28], fill="#f59e0b")
draw.ellipse([54, 16, 66, 28], fill="#10b981")
draw.rounded_rectangle([90, 8, 700, 36], radius=6, fill="#334155")
draw.text((110, 14), "https://eservices.dhakaeducationboard.gov.bd/name-age-correction", fill="#94a3b8")

# Portal Navbar
draw.rectangle([0, 44, w, 110], fill="#ffffff")
draw.text((40, 68), "DHAKA EDUCATION BOARD - E-SERVICES PORTAL", fill="#0f172a")

# Main Form Container
draw.rounded_rectangle([40, 130, w - 40, h - 40], radius=12, fill="#ffffff", outline="#e2e8f0", width=1)
draw.text((70, 160), "Application Form: Name & Age Correction (Online)", fill="#1e40af")

# Form fields mock
draw.text((70, 205), "Examination:", fill="#475569")
draw.rounded_rectangle([70, 230, 450, 275], radius=6, outline="#cbd5e1", fill="#f8fafc", width=1)
draw.text((90, 244), "SSC / Dakhil / Equivalent", fill="#1e293b")

draw.text((500, 205), "Passing Year:", fill="#475569")
draw.rounded_rectangle([500, 230, 880, 275], radius=6, outline="#cbd5e1", fill="#f8fafc", width=1)
draw.text((520, 244), "2024", fill="#1e293b")

draw.text((70, 305), "Roll Number:", fill="#475569")
draw.rounded_rectangle([70, 330, 450, 375], radius=6, outline="#cbd5e1", fill="#f8fafc", width=1)
draw.text((90, 344), "142857", fill="#1e293b")

draw.text((500, 305), "Registration No:", fill="#475569")
draw.rounded_rectangle([500, 330, 880, 375], radius=6, outline="#cbd5e1", fill="#f8fafc", width=1)
draw.text((520, 344), "1115283940", fill="#1e293b")

# Action Button to CLICK (Target)
btn_x1, btn_y1, btn_x2, btn_y2 = 70, 430, 380, 485
draw.rounded_rectangle([btn_x1, btn_y1, btn_x2, btn_y2], radius=8, fill="#2563eb")
draw.text((105, 448), "Find Record & Proceed to Form", fill="#ffffff")

# Secondary button
draw.rounded_rectangle([410, 430, 520, 485], radius=8, outline="#cbd5e1", fill="#ffffff")
draw.text((440, 448), "Reset", fill="#64748b")

ui.save(RAW_UI_PATH)

# Now Annotate this UI screenshot with Chrome Headless (with Hind Siliguri):
annotated_path = annotate_with_html(
    image_path=RAW_UI_PATH,
    target_box=(btn_x1, btn_y1, btn_x2, btn_y2),
    step_number=1,
    action_label="এই বাটনে ক্লিক করুন",
    output_filename="sample_annotated_step1.png",
    color="#dc2626"
)

print(f"Sample Annotated Screenshot created at: {annotated_path}")
