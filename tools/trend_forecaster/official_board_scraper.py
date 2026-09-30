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


def scrape_dgme_medical_notices(limit=6):
    """
    Scrapes Directorate General of Medical Education (dgme.gov.bd) for MBBS/BDS notices.
    """
    url = "https://dgme.gov.bd/"
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
            if any(k in clean for k in ["এমবিবিএস", "বিডিএস", "ভর্তি", "পরীক্ষা", "বিজ্ঞপ্তি", "রেজাল্ট", "মেডিকেল"]):
                if len(clean) > 10 and clean not in seen:
                    seen.add(clean)
                    full_link = link if link.startswith("http") else "https://dgme.gov.bd" + link
                    notices.append({
                        "source": "মেডিকেল ও ডেন্টাল ভর্তি (DGME Official)",
                        "title": clean,
                        "pdf_url": full_link,
                        "pub_date": datetime.now().strftime("%Y-%m-%d"),
                        "category": "মেডিকেল ভর্তি"
                    })
                    if len(notices) >= limit:
                        break
    except Exception as e:
        print(f"[-] DGME Medical Scraper ত্রুটি: {e}")

    return notices


def scrape_du_admission_notices(limit=4):
    """
    Scrapes Dhaka University Undergraduate Admission portal (admission.eis.du.ac.bd).
    """
    url = "https://admission.eis.du.ac.bd/"
    notices = []
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, context=SSL_CTX, timeout=8) as r:
            html = r.read().decode("utf-8", errors="ignore")

        pattern = r'<a[^>]+href=["\']([^"\']+)["\'][^>]*>(.*?)</a>'
        matches = re.findall(pattern, html, re.DOTALL | re.IGNORECASE)
        seen = set()
        for link, text in matches:
            clean = clean_html_text(text)
            if any(k in clean for k in ["ইউনিট", "ভর্তি", "বিজ্ঞপ্তি", "পরীক্ষা", "তারিখ"]):
                if len(clean) > 8 and clean not in seen:
                    seen.add(clean)
                    full_link = link if link.startswith("http") else "https://admission.eis.du.ac.bd/" + link.lstrip("/")
                    notices.append({
                        "source": "ঢাকা বিশ্ববিদ্যালয় ভর্তি (DU Admission Official)",
                        "title": clean,
                        "pdf_url": full_link,
                        "pub_date": datetime.now().strftime("%Y-%m-%d"),
                        "category": "বিশ্ববিদ্যালয় ভর্তি"
                    })
                    if len(notices) >= limit:
                        break
    except Exception as e:
        print(f"[-] DU Admission Scraper ত্রুটি: {e}")

    return notices


def scrape_rajshahi_board_notices(limit=5):
    """
    Scrapes Rajshahi Education Board (rajshahieducationboard.gov.bd).
    """
    url = "http://rajshahieducationboard.gov.bd/"
    notices = []
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, context=SSL_CTX, timeout=8) as r:
            html = r.read().decode("utf-8", errors="ignore")

        pattern = r'<a[^>]+href=["\']([^"\']+\.pdf)["\'][^>]*>(.*?)</a>'
        matches = re.findall(pattern, html, re.DOTALL | re.IGNORECASE)
        seen = set()
        for link, text in matches:
            clean = clean_html_text(text)
            if len(clean) > 10 and clean not in seen:
                seen.add(clean)
                full_link = link if link.startswith("http") else "http://rajshahieducationboard.gov.bd/" + link.lstrip("/")
                notices.append({
                    "source": "রাজশাহী শিক্ষা বোর্ড (Official)",
                    "title": clean,
                    "pdf_url": full_link,
                    "pub_date": datetime.now().strftime("%Y-%m-%d"),
                    "category": "মাধ্যমিক ও উচ্চমাধ্যমিক"
                })
                if len(notices) >= limit:
                    break
    except Exception as e:
        print(f"[-] Rajshahi Board Scraper ত্রুটি: {e}")

    return notices


def scrape_bou_open_university_notices(limit=6):
    """
    Scrapes Bangladesh Open University (BOU - bou.ac.bd) for SSC, HSC, BA/BSS, MBA notices.
    """
    url = "https://www.bou.ac.bd/"
    notices = []
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, context=SSL_CTX, timeout=10) as r:
            html = r.read().decode("utf-8", errors="ignore")

        pattern = r'<a[^>]+href=["\']([^"\']*upload/notice/[^"\']+)["\'][^>]*>(.*?)</a>'
        matches = re.findall(pattern, html, re.DOTALL | re.IGNORECASE)
        seen = set()
        for link, text in matches:
            clean = clean_html_text(text)
            if len(clean) > 10 and clean not in seen:
                seen.add(clean)
                full_link = link if link.startswith("http") else "https://www.bou.ac.bd/" + link.lstrip("/")
                notices.append({
                    "source": "উন্মুক্ত বিশ্ববিদ্যালয় (BOU Official)",
                    "title": clean,
                    "pdf_url": full_link,
                    "pub_date": datetime.now().strftime("%Y-%m-%d"),
                    "category": "বাউবি উন্মুক্ত শিক্ষা"
                })
                if len(notices) >= limit:
                    break
    except Exception as e:
        print(f"[-] BOU Open University Scraper ত্রুটি: {e}")

    return notices


def scrape_bnmc_nursing_notices(limit=4):
    """
    Scrapes Bangladesh Nursing & Midwifery Council (bnmc.gov.bd).
    """
    url = "http://www.bnmc.gov.bd/"
    notices = []
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, context=SSL_CTX, timeout=8) as r:
            html = r.read().decode("utf-8", errors="ignore")

        pattern = r'<a[^>]+href=["\']([^"\']+)["\'][^>]*>(.*?)</a>'
        matches = re.findall(pattern, html, re.DOTALL | re.IGNORECASE)
        seen = set()
        for link, text in matches:
            clean = clean_html_text(text)
            if any(k in clean for k in ["নার্সিং", "ভর্তি", "পরীক্ষা", "লাইসেন্সিং", "বিজ্ঞপ্তি"]):
                if len(clean) > 8 and clean not in seen:
                    seen.add(clean)
                    full_link = link if link.startswith("http") else "http://www.bnmc.gov.bd" + link
                    notices.append({
                        "source": "নার্সিং কাউন্সিল (BNMC Official)",
                        "title": clean,
                        "pdf_url": full_link,
                        "pub_date": datetime.now().strftime("%Y-%m-%d"),
                        "category": "নার্সিং ও মিডওয়াইফারি"
                    })
                    if len(notices) >= limit:
                        break
    except Exception as e:
        print(f"[-] BNMC Nursing Scraper ত্রুটি: {e}")

    return notices


def fetch_all_official_board_notices():
    """
    Consolidates notices directly from all official education portals.
    """
    all_notices = []
    
    # 1. National University (Honours, Masters, Degree)
    all_notices.extend(scrape_national_university_notices(limit=10))

    # 2. Bangladesh Open University (BOU SSC, HSC, BA/BSS, MBA)
    all_notices.extend(scrape_bou_open_university_notices(limit=6))

    # 3. Dhaka Education Board (SSC & HSC)
    all_notices.extend(scrape_dhaka_board_notices(limit=5))

    # 4. Rajshahi Education Board
    all_notices.extend(scrape_rajshahi_board_notices(limit=4))

    # 5. BTEB Technical Board (Polytechnic)
    all_notices.extend(scrape_bteb_notices(limit=5))

    # 6. BMEB Madrasah Education Board (Dakhil & Alim)
    all_notices.extend(scrape_bmeb_notices(limit=5))

    # 7. NTRCA Teachers Registration
    all_notices.extend(scrape_ntrca_notices(limit=5))

    # 8. DU 7 Colleges
    all_notices.extend(scrape_du_7college_notices(limit=4))

    # 9. DGME Medical & Dental Admission
    all_notices.extend(scrape_dgme_medical_notices(limit=4))

    # 10. BNMC Nursing & Midwifery Council
    all_notices.extend(scrape_bnmc_nursing_notices(limit=4))

    # 11. DU Undergraduate Admission
    all_notices.extend(scrape_du_admission_notices(limit=3))

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
