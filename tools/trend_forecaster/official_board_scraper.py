#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/trend_forecaster/official_board_scraper.py
-------------------------------------------------
Helptrickbd Official Government & University Notice Board Scraper.

Directly scrapes official notice portals and retrieves:
- Official Notice Titles
- Official Notice Dates
- Direct Official PDF Download Links (.pdf)

Monitored Official Portals:
1. National University (nu.ac.bd) -> Honours 1st-4th, Masters, Degree, MPhil
2. Dhaka Education Board (dhakaeducationboard.gov.bd) -> SSC, HSC, Routine, Fee
3. Bangladesh Technical Education Board (bteb.gov.bd) -> Diploma in Engineering
4. Bangladesh Public Service Commission (bpsc.gov.bd) -> BCS Preliminary & Written
5. Directorate of Primary Education (dpe.gov.bd / portals) -> Primary Scholarship & Exams

Zero-emoji compliance (Rule 12).
"""

import os
import sys
import re
import ssl
import json
import urllib.request
from datetime import datetime

try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

SSL_CTX = ssl.create_default_context()
SSL_CTX.check_hostname = False
SSL_CTX.verify_mode = ssl.CERT_NONE

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "bn-BD,bn;q=0.9,en-US;q=0.8,en;q=0.7"
}


def clean_html_text(text):
    clean = re.sub(r'<[^>]+>', ' ', text)
    clean = re.sub(r'&nbsp;', ' ', clean)
    clean = re.sub(r'\s+', ' ', clean)
    return clean.strip(' "“‘\'\r\n\t')


def scrape_national_university_notices(limit=15):
    """
    Directly scrapes National University (nu.ac.bd) official notice repository.
    Extracts notice titles and exact uploads/notices/*.pdf download links.
    """
    url = "https://www.nu.ac.bd/"
    notices = []
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, context=SSL_CTX, timeout=12) as r:
            html = r.read().decode("utf-8", errors="ignore")

        pattern = r'<a[^>]+href=["\']([^"\']*uploads/notices/[^"\']+)["\'][^>]*>(.*?)</a>'
        matches = re.findall(pattern, html, re.DOTALL | re.IGNORECASE)

        seen = set()
        for link, text in matches:
            clean = clean_html_text(text)
            if clean and len(clean) > 10 and clean not in seen:
                seen.add(clean)
                full_link = link if link.startswith("http") else "https://www.nu.ac.bd/" + link.lstrip("/")
                
                # Extract date from filename if present (e.g. pub_date_30092026.pdf)
                date_match = re.search(r'pub_date_(\d{2})(\d{2})(\d{4})', link, re.IGNORECASE)
                if date_match:
                    d, m, y = date_match.groups()
                    pub_date = f"{y}-{m}-{d}"
                else:
                    pub_date = datetime.now().strftime("%Y-%m-%d")

                notices.append({
                    "source": "জাতীয় বিশ্ববিদ্যালয় (NU Official)",
                    "title": clean,
                    "pdf_url": full_link,
                    "pub_date": pub_date,
                    "category": "অনার্স ও মাস্টার্স"
                })
                if len(notices) >= limit:
                    break
    except Exception as e:
        print(f"[-] NU Notice Scraper ত্রুটি: {e}")

    return notices


def scrape_dhaka_board_notices(limit=10):
    """
    Scrapes Dhaka Education Board official announcements and PDFs.
    """
    url = "https://dhakaeducationboard.gov.bd/"
    notices = []
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, context=SSL_CTX, timeout=10) as r:
            html = r.read().decode("utf-8", errors="ignore")

        # Scan for PDFs and notice anchors
        pattern = r'<a[^>]+href=["\']([^"\']+\.pdf)["\'][^>]*>(.*?)</a>'
        matches = re.findall(pattern, html, re.DOTALL | re.IGNORECASE)

        seen = set()
        for link, text in matches:
            clean = clean_html_text(text)
            if clean and len(clean) > 8 and clean not in seen:
                seen.add(clean)
                full_link = link if link.startswith("http") else "https://dhakaeducationboard.gov.bd/" + link.lstrip("/")
                notices.append({
                    "source": "ঢাকা শিক্ষা বোর্ড (Official)",
                    "title": clean,
                    "pdf_url": full_link,
                    "pub_date": datetime.now().strftime("%Y-%m-%d"),
                    "category": "মাধ্যমিক ও উচ্চমাধ্যমিক"
                })
                if len(notices) >= limit:
                    break

        # Also check for urgent modal notice if present
        if "জরুরি গণবিজ্ঞপ্তি" in html and "modal" in html:
            modal_text_match = re.search(r'জরুরি গণবিজ্ঞপ্তি.*?তারিখঃ\s*([০-৯0-9/]+)', html, re.DOTALL)
            date_str = modal_text_match.group(1) if modal_text_match else ""
            notices.insert(0, {
                "source": "ঢাকা শিক্ষা বোর্ড (Official Notice)",
                "title": f"জরুরি গণবিজ্ঞপ্তি: নাম, বয়স ও তথ্য সংশোধন বিষয়ক সতর্কবার্তা (তারিখ: {date_str})",
                "pdf_url": "https://dhakaeducationboard.gov.bd/",
                "pub_date": datetime.now().strftime("%Y-%m-%d"),
                "category": "বোর্ড নির্দেশনা"
            })
    except Exception as e:
        print(f"[-] Dhaka Board Notice Scraper ত্রুটি: {e}")

    return notices


def scrape_bteb_notices(limit=8):
    """
    Scrapes Bangladesh Technical Education Board official notice portal.
    """
    url = "http://www.bteb.gov.bd/site/view/notices"
    notices = []
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, context=SSL_CTX, timeout=10) as r:
            html = r.read().decode("utf-8", errors="ignore")

        pattern = r'<a[^>]+href=["\']([^"\']+)["\'][^>]*>(.*?)</a>'
        matches = re.findall(pattern, html, re.DOTALL | re.IGNORECASE)
        seen = set()
        for link, text in matches:
            clean = clean_html_text(text)
            if any(k in clean for k in ["ডিপ্লোমা", "পরীক্ষা", "রুটিন", "ফরম পূরণ", "ভর্তি", "বিজ্ঞপ্তি", "ফলাফল"]):
                if len(clean) > 12 and clean not in seen:
                    seen.add(clean)
                    full_link = link if link.startswith("http") else "http://www.bteb.gov.bd" + link
                    notices.append({
                        "source": "কারিগরি শিক্ষা বোর্ড (BTEB Official)",
                        "title": clean,
                        "pdf_url": full_link,
                        "pub_date": datetime.now().strftime("%Y-%m-%d"),
                        "category": "পলিটেকনিক ও কারিগরি"
                    })
                    if len(notices) >= limit:
                        break
    except Exception as e:
        print(f"[-] BTEB Notice Scraper ত্রুটি: {e}")

    return notices


def scrape_bmeb_notices(limit=8):
    """
    Scrapes Bangladesh Madrasah Education Board (bmeb.gov.bd) official notices & PDFs.
    """
    url = "http://www.bmeb.gov.bd/"
    notices = []
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, context=SSL_CTX, timeout=10) as r:
            html = r.read().decode("utf-8", errors="ignore")

        pattern = r'<a[^>]+href=["\']([^"\']+)["\'][^>]*>(.*?)</a>'
        matches = re.findall(pattern, html, re.DOTALL | re.IGNORECASE)
        seen = set()
        for link, text in matches:
            clean = clean_html_text(text)
            if any(k in clean for k in ["দাখিল", "আলim", "আলিম", "পরীক্ষা", "রুটিন", "ফরম পূরণ", "বিজ্ঞপ্তি", "ফলাফল"]):
                if len(clean) > 12 and clean not in seen:
                    seen.add(clean)
                    full_link = link if link.startswith("http") else "http://www.bmeb.gov.bd" + link
                    notices.append({
                        "source": "মাদ্রাসা শিক্ষা বোর্ড (BMEB Official)",
                        "title": clean,
                        "pdf_url": full_link,
                        "pub_date": datetime.now().strftime("%Y-%m-%d"),
                        "category": "দাখিল ও আলিম"
                    })
                    if len(notices) >= limit:
                        break
    except Exception as e:
        print(f"[-] BMEB Notice Scraper ত্রুটি: {e}")

    return notices


def scrape_ntrca_notices(limit=6):
    """
    Scrapes NTRCA (Non-Government Teachers Registration and Certification Authority).
    """
    url = "http://www.ntrca.gov.bd/"
    notices = []
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, context=SSL_CTX, timeout=10) as r:
            html = r.read().decode("utf-8", errors="ignore")

        pattern = r'<a[^>]+href=["\']([^"\']+)["\'][^>]*>(.*?)</a>'
        matches = re.findall(pattern, html, re.DOTALL | re.IGNORECASE)
        seen = set()
        for link, text in matches:
            clean = clean_html_text(text)
            if any(k in clean for k in ["শিক্ষক", "নিবন্ধন", "বিজ্ঞপ্তি", "রুটিন", "পরীক্ষা", "ফলাফল", "ভাইভা", "সিলেবাস"]):
                if len(clean) > 12 and clean not in seen:
                    seen.add(clean)
                    full_link = link if link.startswith("http") else "http://www.ntrca.gov.bd" + link
                    notices.append({
                        "source": "এনটিআরসিএ (NTRCA Official)",
                        "title": clean,
                        "pdf_url": full_link,
                        "pub_date": datetime.now().strftime("%Y-%m-%d"),
                        "category": "শিক্ষক নিবন্ধন"
                    })
                    if len(notices) >= limit:
                        break
    except Exception as e:
        print(f"[-] NTRCA Notice Scraper ত্রুটি: {e}")

    return notices


def scrape_du_7college_notices(limit=6):
    """
    Scrapes Dhaka University Affiliated 7 Colleges official portal.
    """
    url = "https://7college.du.ac.bd/"
    notices = []
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, context=SSL_CTX, timeout=10) as r:
            html = r.read().decode("utf-8", errors="ignore")

        pattern = r'<a[^>]+href=["\']([^"\']+)["\'][^>]*>(.*?)</a>'
        matches = re.findall(pattern, html, re.DOTALL | re.IGNORECASE)
        seen = set()
        for link, text in matches:
            clean = clean_html_text(text)
            if any(k in clean for k in ["পরীক্ষা", "রুটিন", "ফরম পূরণ", "বিজ্ঞপ্তি", "অনার্স", "মাস্টার্স", "রেজাল্ট"]):
                if len(clean) > 10 and clean not in seen:
                    seen.add(clean)
                    full_link = link if link.startswith("http") else "https://7college.du.ac.bd/" + link.lstrip("/")
                    notices.append({
                        "source": "ঢাবি অধিভুক্ত ৭ কলেজ (7 College Official)",
                        "title": clean,
                        "pdf_url": full_link,
                        "pub_date": datetime.now().strftime("%Y-%m-%d"),
                        "category": "৭ কলেজ অনার্স ও মাস্টার্স"
                    })
                    if len(notices) >= limit:
                        break
    except Exception as e:
        print(f"[-] 7 College Notice Scraper ত্রুটি: {e}")

    return notices


def fetch_all_official_board_notices():
    """
    Consolidates notices directly from all official education portals.
    """
    all_notices = []
    
    # 1. National University
    all_notices.extend(scrape_national_university_notices(limit=10))

    # 2. Dhaka Education Board
    all_notices.extend(scrape_dhaka_board_notices(limit=6))

    # 3. BTEB Technical Board
    all_notices.extend(scrape_bteb_notices(limit=6))

    # 4. BMEB Madrasah Education Board
    all_notices.extend(scrape_bmeb_notices(limit=6))

    # 5. NTRCA Teachers Registration
    all_notices.extend(scrape_ntrca_notices(limit=6))

    # 6. DU 7 Colleges
    all_notices.extend(scrape_du_7college_notices(limit=4))

    return all_notices


if __name__ == "__main__":
    print("=" * 72)
    print("  HELPTRICKBD OFFICIAL BOARD NOTICE & PDF SCRAPER")
    print("=" * 72)
    notices = fetch_all_official_board_notices()
    print(f"[*] মোট {len(notices)}টি অফিসিয়াল নোটিশ ও PDF সফলভাবে সংগৃহীত হয়েছে:\n")
    for idx, n in enumerate(notices, 1):
        print(f"{idx}. [{n['source']}] {n['title']}")
        print(f"   PDF: {n['pdf_url']}")
        print(f"   তারিখ: {n['pub_date']}\n")
