#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/wp_publisher/test_wp_connection.py
-----------------------------------------
Diagnostic tool to verify WordPress REST API availability and authentication status.

Usage:
  python tools/wp_publisher/test_wp_connection.py
"""

import os
import sys
import json

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.wp_publisher.publisher import WordPressPublisher

def run_test():
    print("=" * 65)
    print("HELPTRICKBD WORDPRESS REST API DIAGNOSTIC CHECK")
    print("=" * 65)

    pub = WordPressPublisher()
    config = pub.config
    print(f"Target Site URL : {config.get('wp_url')}")
    print(f"WordPress User  : {config.get('wp_user')}")
    print(f"App Password    : {'[CONFIGURED]' if config.get('wp_app_password') else '[NOT SET - PLEASE CONFIGURE]'}")
    print(f"Default Status  : {config.get('default_status')}")
    print("-" * 65)

    if not config.get("wp_app_password"):
        print("[WARNING] Application Password is not configured in config.json.")
        print("To generate one:")
        print("1. Log in to WordPress Admin (https://www.helptrickbd.com/wp-admin/)")
        print("2. Go to Users > Profile")
        print("3. Scroll to 'Application Passwords', enter name (e.g. 'HelpTrickBD-Bot'), and click 'Add New Application Password'")
        print("4. Paste the 24-character generated password into tools/wp_publisher/config.json")
        print("-" * 65)

    print("[*] Testing WordPress REST API endpoint...")
    result = pub.test_connection()

    if result.get("success"):
        print(f"[SUCCESS] Connected to WordPress REST API!")
        print(f"User ID   : {result.get('user_id')}")
        print(f"Username  : {result.get('username')}")
        print(f"Roles     : {', '.join(result.get('roles', []))}")
    else:
        status_code = result.get("status_code", "N/A")
        print(f"[FAILED] Could not authenticate (Status: {status_code})")
        print(f"Details : {result.get('error', 'Unknown error')}")

    print("=" * 65)

if __name__ == "__main__":
    run_test()
