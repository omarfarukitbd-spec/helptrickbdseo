#!/usr/bin/env python3
"""
HelpTrickBD - Native GEO & AEO Audit Tool
Direct interface for the GEO Audit Toolkit (.agents/skills/geo-audit-toolkit).
Runs multi-LLM Generative Engine Optimization audits across ChatGPT, Google AI Overviews,
Perplexity, Claude, and Mistral.
"""

import os
import sys

try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SKILL_DIR = os.path.join(PROJECT_ROOT, ".agents", "skills", "geo-audit-toolkit")

if SKILL_DIR not in sys.path:
    sys.path.insert(0, SKILL_DIR)

if __name__ == "__main__":
    from scripts.run_audit import _main
    
    # Default to https://www.helptrickbd.com/ if no URL specified
    if len(sys.argv) == 1:
        sys.argv.append("https://www.helptrickbd.com/")
        sys.argv.extend(["--max-pages", "5"])
        print("[*] No target URL provided. Auditing default: https://www.helptrickbd.com/ (max 5 pages)...")

    _main()
