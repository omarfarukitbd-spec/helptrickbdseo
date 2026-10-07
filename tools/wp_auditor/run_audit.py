#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/wp_auditor/run_audit.py
------------------------------
Command-line runner for the HelpTrickBD WordPress 360-Degree Site Auditor.

Usage:
  python tools/wp_auditor/run_audit.py [--limit 10]
  python tools/wp_auditor/run_audit.py --all
"""

import os
import sys
import argparse

try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.wp_auditor.wp_auditor_core import WordPressSiteAuditor

def main():
    parser = argparse.ArgumentParser(description="HelpTrickBD WordPress 360 Site Auditor")
    parser.add_argument("--limit", type=int, default=10, help="Number of posts to audit (default: 10)")
    parser.add_argument("--all", action="store_true", help="Audit all published posts across the site")
    parser.add_argument("--output-md", type=str, default=os.path.join(PROJECT_ROOT, "reports", "wp_full_site_audit_report.md"), help="Path to Markdown report")
    parser.add_argument("--output-json", type=str, default=os.path.join(PROJECT_ROOT, "reports", "wp_full_site_audit_report.json"), help="Path to JSON data file")

    args = parser.parse_args()
    limit = None if args.all else args.limit

    auditor = WordPressSiteAuditor()
    results = auditor.audit_site(limit=limit)
    auditor.export_reports(results, output_md=args.output_md, output_json=args.output_json)

if __name__ == "__main__":
    main()
