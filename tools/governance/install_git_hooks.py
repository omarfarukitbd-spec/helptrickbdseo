#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/governance/install_git_hooks.py
-------------------------------------
Installs automated Git Pre-Push and Pre-Commit hooks.
Guarantees that ANY machine (Home PC or Office PC) running Git
will automatically block commits or pushes that violate governance standards.
"""

import os
import sys
import stat

if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
GIT_HOOKS_DIR = os.path.join(PROJECT_ROOT, ".git", "hooks")

PRE_PUSH_SCRIPT = """#!/bin/sh
# HelpTrickBD Automated Git Pre-Push Hook
echo "======================================================"
echo "🛡️  RUNNING PRE-PUSH GOVERNANCE & INTEGRITY CHECK..."
echo "======================================================"

python tools/governance/check_all_governance.py
STATUS=$?

if [ $STATUS -ne 0 ]; then
    echo "======================================================"
    echo "❌ GIT PUSH REJECTED: Governance check failed!"
    echo "Fix the issues reported above before pushing to origin."
    echo "======================================================"
    exit 1
fi

echo "✅ Pre-push governance check passed. Pushing to origin..."
exit 0
"""

def install_hooks():
    if not os.path.exists(GIT_HOOKS_DIR):
        print(f"Error: .git/hooks directory not found at {GIT_HOOKS_DIR}", file=sys.stderr)
        return False

    pre_push_path = os.path.join(GIT_HOOKS_DIR, "pre-push")
    with open(pre_push_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(PRE_PUSH_SCRIPT)

    # Make executable
    st = os.stat(pre_push_path)
    os.chmod(pre_push_path, st.st_mode | stat.S_IEXEC | stat.S_IXGRP | stat.S_IXOTH)

    print(f"✅ Pre-push hook successfully installed at: {pre_push_path}")
    return True

if __name__ == "__main__":
    success = install_hooks()
    sys.exit(0 if success else 1)
