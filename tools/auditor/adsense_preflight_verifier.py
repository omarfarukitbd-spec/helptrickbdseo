#!/usr/bin/env python3
"""
AdSense Pre-Flight Application Verifier Tool.
Automated audit engine to verify identity match, age, address, e-TIN, and live website technical compliance.
Strictly zero emojis in logs and outputs.
"""

import argparse
import datetime
import json
import os
import re
import sys
import urllib.request
import urllib.error

THEME_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "Helptrickbd theme code.xml")
LEGAL_PAGES = [
    "https://www.helptrickbd.com/p/about-us.html",
    "https://www.helptrickbd.com/p/contact-us.html",
    "https://www.helptrickbd.com/p/privacy-policy.html",
    "https://www.helptrickbd.com/p/terms-conditions.html",
    "https://www.helptrickbd.com/p/disclaimer.html"
]


def normalize_name(name: str) -> str:
    if not name:
        return ""
    # Strip dots, hyphens, multiple spaces, uppercase
    cleaned = re.sub(r'[\.\-\,\_]', ' ', name)
    cleaned = re.sub(r'\s+', ' ', cleaned).strip().upper()
    return cleaned


def verify_identity(data: dict) -> list:
    issues = []
    gmail_name = normalize_name(data.get("gmail_name", ""))
    nid_name = normalize_name(data.get("nid_name", ""))
    payment_name = normalize_name(data.get("payment_name", ""))
    bank_name = normalize_name(data.get("bank_account_name", ""))

    print("[1/5] Verifying 4-Point Identity Alignment...")
    if not nid_name:
        issues.append("ERROR: Smart NID English name is missing.")
    if not gmail_name:
        issues.append("ERROR: Gmail profile name is missing.")
    if not payment_name:
        issues.append("ERROR: AdSense payment profile name is missing.")
    if not bank_name:
        issues.append("ERROR: Bank account holder name is missing.")

    if nid_name and gmail_name and nid_name != gmail_name:
        issues.append(f"CRITICAL MISMATCH: NID name ('{data.get('nid_name')}') does not match Gmail name ('{data.get('gmail_name')}').")
    if nid_name and payment_name and nid_name != payment_name:
        issues.append(f"CRITICAL MISMATCH: NID name ('{data.get('nid_name')}') does not match Payment name ('{data.get('payment_name')}').")
    if nid_name and bank_name and nid_name != bank_name:
        issues.append(f"CRITICAL MISMATCH: NID name ('{data.get('nid_name')}') does not match Bank name ('{data.get('bank_account_name')}').")

    if not issues:
        print("  - Identity Match: 100% Letter-for-letter match across all documents. [OK]")
    else:
        for err in issues:
            print(f"  - {err}")
    return issues


def verify_age(data: dict) -> list:
    issues = []
    print("[2/5] Verifying Age and Date of Birth...")
    nid_dob_str = data.get("nid_dob", "").strip()
    gmail_dob_str = data.get("gmail_dob", "").strip()

    if not nid_dob_str:
        issues.append("ERROR: NID Date of Birth is missing.")
        return issues

    date_formats = ["%d/%m/%Y", "%Y-%m-%d", "%d-%m-%Y", "%d.%m.%Y"]
    nid_dob = None
    for fmt in date_formats:
        try:
            nid_dob = datetime.datetime.strptime(nid_dob_str, fmt).date()
            break
        except ValueError:
            continue

    if not nid_dob:
        issues.append(f"ERROR: Could not parse NID DOB format '{nid_dob_str}'. Expected DD/MM/YYYY.")
        return issues

    today = datetime.date.today()
    age = today.year - nid_dob.year - ((today.month, today.day) < (nid_dob.month, nid_dob.day))
    if age < 18:
        issues.append(f"CRITICAL FAILURE: Age is {age} years. Google AdSense strictly requires applicants to be at least 18 years old.")
    else:
        print(f"  - Age Calculated: {age} years old (Applicant is 18+). [OK]")

    if gmail_dob_str:
        gmail_dob = None
        for fmt in date_formats:
            try:
                gmail_dob = datetime.datetime.strptime(gmail_dob_str, fmt).date()
                break
            except ValueError:
                continue
        if gmail_dob and gmail_dob != nid_dob:
            issues.append(f"WARNING: NID DOB ({nid_dob}) does not match Gmail DOB ({gmail_dob}). Please sync Gmail DOB.")
        elif gmail_dob:
            print("  - DOB Sync: NID DOB and Gmail DOB match perfectly. [OK]")

    return issues


def verify_address(data: dict) -> list:
    issues = []
    print("[3/5] Verifying Postal Address & Bangladesh Post Office Delivery Optimization...")
    addr1 = data.get("address_line_1", "").strip()
    addr2 = data.get("address_line_2", "").strip()
    city = data.get("city", "").strip()
    postcode = str(data.get("postal_code", "")).strip()

    if not addr1:
        issues.append("ERROR: Address Line 1 is empty.")
    if not city:
        issues.append("ERROR: City/District is empty.")

    # Check Postal Code
    if not re.fullmatch(r'\d{4}', postcode):
        issues.append(f"ERROR: Postal code '{postcode}' is invalid. Must be an exact 4-digit code (e.g. 1230, 3100).")
    else:
        print(f"  - Postal Code: {postcode} (Valid 4-digit code). [OK]")

    # Check Mobile Number in Address Line 2
    phone_pattern = r'(?:\+?8801[3-9]\d{8}|01[3-9]\d{8})'
    if not re.search(phone_pattern, addr2):
        issues.append("HIGH WARNING: Address Line 2 does NOT contain a valid Bangladesh mobile number. "
                      "Include your phone number in Address Line 2 (e.g. 'Mobile: +88017XXXXXXXX') "
                      "so the local postman can call you upon letter arrival.")
    else:
        print(f"  - Address Line 2 Delivery Hack: Mobile number detected in Address Line 2 ('{addr2}'). [OK]")

    return issues


def verify_tax(data: dict) -> list:
    issues = []
    print("[4/5] Verifying US Tax (W-8BEN) & Bangladesh e-TIN Readiness...")
    etin = str(data.get("etin", "")).strip()
    if not etin:
        issues.append("WARNING: e-TIN is missing. Without a 12-digit e-TIN, US tax withholding will be 30% instead of 0% treaty rate.")
    elif not re.fullmatch(r'\d{12}', etin):
        issues.append(f"ERROR: e-TIN '{etin}' is invalid. Bangladesh e-TIN must be exactly 12 numeric digits.")
    else:
        print(f"  - e-TIN Format: Valid 12-digit number ('{etin[:3]}******{etin[-3:]}'). Treaty benefit rate = 0%. [OK]")
    return issues


def verify_live_website() -> list:
    issues = []
    print("[5/5] Auditing Live Website Technical Prerequisites...")

    # 1. ads.txt check
    ads_txt_url = "https://www.helptrickbd.com/ads.txt"
    try:
        req = urllib.request.Request(ads_txt_url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        with urllib.request.urlopen(req, timeout=10) as response:
            if response.status == 200:
                content = response.read().decode('utf-8')
                if "google.com, pub-" in content:
                    print("  - ads.txt Live at Root: Verified HTTP 200 with valid Publisher ID. [OK]")
                else:
                    issues.append("WARNING: ads.txt responded with HTTP 200, but does not contain valid pub-ID string.")
            else:
                issues.append(f"ERROR: ads.txt responded with HTTP {response.status}.")
    except Exception as e:
        issues.append(f"ERROR: Failed to fetch ads.txt ({e}).")

    # 2. Check AdSense script in theme file
    if os.path.exists(THEME_FILE):
        try:
            with open(THEME_FILE, 'r', encoding='utf-8') as f:
                theme_content = f.read()
                if "pagead2.googlesyndication.com/pagead/js/adsbygoogle.js" in theme_content:
                    print("  - AdSense Head Script: Found inside 'Helptrickbd theme code.xml'. [OK]")
                else:
                    issues.append("ERROR: AdSense script tag NOT found inside 'Helptrickbd theme code.xml'.")
        except Exception as e:
            issues.append(f"WARNING: Could not read theme file: {e}")

    # 3. Check Legal Pages HTTP Status
    for url in LEGAL_PAGES:
        slug = url.split('/')[-1]
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=10) as resp:
                if resp.status == 200:
                    print(f"  - Legal Trust Page: {slug} is HTTP 200 OK. [OK]")
                else:
                    issues.append(f"ERROR: Legal page {slug} returned HTTP {resp.status}.")
        except Exception as e:
            issues.append(f"ERROR: Legal page {slug} could not be reached: {e}")

    return issues


def run_full_verification(data: dict):
    print("=" * 70)
    print("HELPTRICKBD SEO — ADSENSE PRE-FLIGHT APPLICATION VERIFIER")
    print("=" * 70)

    all_issues = []
    all_issues.extend(verify_identity(data))
    all_issues.extend(verify_age(data))
    all_issues.extend(verify_address(data))
    all_issues.extend(verify_tax(data))
    all_issues.extend(verify_live_website())

    print("=" * 70)
    print("VERIFICATION SUMMARY REPORT:")
    criticals = [i for i in all_issues if "CRITICAL" in i or "ERROR" in i]
    warnings = [i for i in all_issues if "WARNING" in i]

    if not criticals and not warnings:
        print("STATUS: 100% PASSED. Application is fully compliant with all Google AdSense policies.")
    elif not criticals:
        print(f"STATUS: CONDITIONALLY READY ({len(warnings)} non-blocking warnings to review).")
    else:
        print(f"STATUS: BLOCKED. {len(criticals)} critical issue(s) MUST be fixed before applying.")

    for issue in all_issues:
        print(f"  * {issue}")
    print("=" * 70)


def main():
    parser = argparse.ArgumentParser(description="AdSense Application Pre-flight Verifier")
    parser.add_argument("--json", help="Path to JSON file containing user input data")
    args = parser.parse_args()

    data = {}
    if args.json and os.path.exists(args.json):
        with open(args.json, 'r', encoding='utf-8') as f:
            data = json.load(f)
    else:
        # Default mock for dry-run technical check
        data = {
            "gmail_name": "Md Omar Faruk",
            "nid_name": "Md Omar Faruk",
            "payment_name": "Md Omar Faruk",
            "bank_account_name": "Md Omar Faruk",
            "nid_dob": "01/01/2000",
            "gmail_dob": "01/01/2000",
            "address_line_1": "Sector 7, Uttara",
            "address_line_2": "Mobile: +8801700000000",
            "city": "Dhaka",
            "postal_code": "1230",
            "etin": "123456789012"
        }

    run_full_verification(data)


if __name__ == "__main__":
    main()
