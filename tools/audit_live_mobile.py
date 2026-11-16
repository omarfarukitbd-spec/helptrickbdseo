#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def audit_live_site():
    output_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'docs', 'live_audit')
    os.makedirs(output_dir, exist_ok=True)

    opts = Options()
    opts.add_argument('--headless')
    opts.add_argument('--disable-gpu')
    opts.add_argument('--no-sandbox')
    opts.add_argument('--ignore-certificate-errors')
    opts.add_argument('--user-agent=Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36')

    driver = webdriver.Chrome(options=opts)

    try:
        url = "https://www.helptrickbd.com"
        print(f"[*] Navigating to {url} (Mobile 390x844)...")
        driver.set_window_size(390, 844)
        driver.get(url)
        time.sleep(4)

        # 1. Capture Above-the-fold mobile screenshot
        atf_img = os.path.join(output_dir, 'live_mobile_atf_390.png')
        driver.save_screenshot(atf_img)
        print(f"   ✅ Saved live mobile ATF screenshot: {atf_img}")

        # 2. Capture Full-page mobile screenshot
        total_height = driver.execute_script("return Math.max(document.body.scrollHeight, document.documentElement.scrollHeight)")
        driver.set_window_size(390, total_height)
        time.sleep(1)
        full_img = os.path.join(output_dir, 'live_mobile_full_390.png')
        driver.save_screenshot(full_img)
        print(f"   ✅ Saved live mobile full screenshot: {full_img}")

        # Reset viewport for inspection
        driver.set_window_size(390, 844)

        # 3. Comprehensive DOM & Layout Audit Script
        audit_js = """
        const results = {
            viewport: { width: window.innerWidth, height: window.innerHeight },
            overflowElements: [],
            headerComponents: {},
            containerPaddings: {},
            typographyIssues: [],
            layoutObservations: []
        };

        // Check horizontal overflow
        const docWidth = document.documentElement.offsetWidth;
        const allElements = document.querySelectorAll('*');
        allElements.forEach(el => {
            const rect = el.getBoundingClientRect();
            if (rect.right > docWidth + 2) {
                results.overflowElements.push({
                    tag: el.tagName,
                    class: el.className,
                    id: el.id,
                    right: rect.right,
                    width: rect.width,
                    text: el.innerText ? el.innerText.substring(0, 40) : ''
                });
            }
        });

        // Inspect header components
        const dateline = document.querySelector('.n-dateline, .n-topbar, header');
        const masthead = document.querySelector('.n-masthead, .n-masthead-inner');
        const brandWordmark = document.querySelector('.n-brand-wordmark');
        const subdomain = document.querySelector('.n-brand-subdomain');
        const tagline = document.querySelector('.n-brand-tagline');
        const nav = document.querySelector('.n-nav, .n-nav-inner');
        const ticker = document.querySelector('.n-ticker, .n-ticker-inner');
        const container = document.querySelector('.ht-container');

        if (masthead) {
            const cs = window.getComputedStyle(masthead);
            results.headerComponents.masthead = {
                padding: cs.padding,
                margin: cs.margin,
                width: cs.width,
                textAlign: cs.textAlign
            };
        }
        if (brandWordmark) {
            const cs = window.getComputedStyle(brandWordmark);
            results.headerComponents.brandWordmark = {
                text: brandWordmark.innerText,
                fontSize: cs.fontSize,
                fontWeight: cs.fontWeight,
                lineHeight: cs.lineHeight,
                margin: cs.margin,
                padding: cs.padding
            };
        }
        if (subdomain) {
            const cs = window.getComputedStyle(subdomain);
            results.headerComponents.subdomain = {
                text: subdomain.innerText,
                display: cs.display,
                fontSize: cs.fontSize,
                color: cs.color,
                margin: cs.margin
            };
        }
        if (tagline) {
            const cs = window.getComputedStyle(tagline);
            results.headerComponents.tagline = {
                text: tagline.innerText,
                fontSize: cs.fontSize,
                color: cs.color,
                margin: cs.margin,
                lineHeight: cs.lineHeight
            };
        }
        if (container) {
            const cs = window.getComputedStyle(container);
            results.containerPaddings = {
                paddingLeft: cs.paddingLeft,
                paddingRight: cs.paddingRight,
                maxWidth: cs.maxWidth,
                width: cs.width
            };
        }
        if (ticker) {
            const cs = window.getComputedStyle(ticker);
            const rect = ticker.getBoundingClientRect();
            results.headerComponents.ticker = {
                width: rect.width,
                margin: cs.margin,
                padding: cs.padding,
                borderRadius: cs.borderRadius
            };
        }
        if (nav) {
            const rect = nav.getBoundingClientRect();
            results.headerComponents.navbar = {
                width: rect.width,
                height: rect.height,
                scrollWidth: nav.scrollWidth
            };
        }

        // Check cards / lead story margins
        const leadStory = document.querySelector('.n-lead-story, .n-lead-hero-grid, .n-section-lead');
        if (leadStory) {
            const cs = window.getComputedStyle(leadStory);
            results.headerComponents.leadStory = {
                padding: cs.padding,
                margin: cs.margin,
                width: leadStory.getBoundingClientRect().width
            };
        }

        return results;
        """

        audit_data = driver.execute_script(audit_js)
        print("\n=== AUDIT RESULTS JSON ===")
        print(json.dumps(audit_data, indent=2, ensure_ascii=False))

        # Save audit report to json
        json_path = os.path.join(output_dir, 'live_audit_data.json')
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(audit_data, f, indent=2, ensure_ascii=False)
        print(f"\n   ✅ Saved audit data: {json_path}")

    finally:
        driver.quit()

if __name__ == '__main__':
    audit_live_site()
