#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import shutil
from datetime import datetime

try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
theme_file = os.path.join(PROJECT_ROOT, "Helptrickbd theme code.xml")

# 1. Backup
ts = datetime.now().strftime("%Y%m%d_%H%M%S")
backup_dir = os.path.join(PROJECT_ROOT, "backups")
os.makedirs(backup_dir, exist_ok=True)
backup_file = os.path.join(backup_dir, f"Helptrickbd_theme_code_backup_{ts}.xml")
shutil.copy(theme_file, backup_file)
print(f"[OK] Backup saved: {backup_file}")

with open(theme_file, "r", encoding="utf-8") as f:
    content = f.read()

target = """/* 6. Post Body Typography and Readability */
  .post-body p {
    font-size: 18px !important;
    line-height: 1.85 !important;
    color: #202124 !important;
  }"""

replacement = """/* 6. Post Body Typography, Lists & Readability */
  .post-body p,
  .entry-content p {
    font-size: 18px !important;
    line-height: 1.85 !important;
    color: #202124 !important;
    margin-bottom: 18px !important;
  }

  .post-body ol, 
  .post-body ul,
  .entry-content ol,
  .entry-content ul {
    margin: 18px 0 24px 0 !important;
    padding-left: 28px !important;
  }

  .post-body ol li, 
  .post-body ul li,
  .entry-content ol li,
  .entry-content ul li {
    font-size: 17.5px !important;
    line-height: 1.85 !important;
    color: #24292f !important;
    margin-bottom: 14px !important;
    padding-bottom: 4px !important;
  }

  /* Distinct Question & Answer spacing inside lists */
  .post-body ol li strong,
  .post-body ul li strong,
  .entry-content ol li strong,
  .entry-content ul li strong {
    display: inline-block !important;
    margin-bottom: 5px !important;
    color: #0f172a !important;
    font-size: 18px !important;
  }

  .post-body ol li em,
  .post-body ul li em,
  .entry-content ol li em,
  .entry-content ul li em {
    font-style: normal !important;
    color: #0369a1 !important;
    font-weight: 600 !important;
  }"""

if target in content:
    content = content.replace(target, replacement, 1)
    with open(theme_file, "w", encoding="utf-8") as f:
        f.write(content)
    print("[OK] Successfully updated Helptrickbd theme code.xml with enhanced list & question/answer spacing!")
else:
    print("[!] Target string not found in Helptrickbd theme code.xml!")
