#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def run_deep_live_audit():
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
        # Viewport: Mobile 390x844 (iPhone 14 / Pixel standard)
        driver.set_window_size(390, 844)
        driver.get('https://www.helptrickbd.com')
        time.sleep(3)

        # 1. Find single post link
        post_link = driver.execute_script("""
            const a = document.querySelector('.n-lead-title a, .n-post-title a, .n-hero-lead a');
            return a ? a.href : null;
        """)
        print(f"[*] Found sample post link: {post_link}")

        # 2. Detailed Homepage Audit
        hp_report = driver.execute_script("""
            const report = {
                title: document.title,
                viewportWidth: window.innerWidth,
                bodyWidth: document.body.offsetWidth,
                hasHorizontalScroll: document.documentElement.scrollWidth > window.innerWidth,
                scrollWidth: document.documentElement.scrollWidth,
                elementsTouchingEdge: [],
                headerSections: {},
                issues: []
            };

            // Check if page has horizontal scroll
            if (report.hasHorizontalScroll) {
                report.issues.push({
                    type: 'HORIZONTAL_SCROLL',
                    detail: `Page scrollWidth is ${report.scrollWidth}px, wider than viewport ${report.viewportWidth}px`
                });
            }

            // Inspect Masthead
            const masthead = document.querySelector('.n-masthead');
            const wordmark = document.querySelector('.n-brand-wordmark');
            const subdomain = document.querySelector('.n-brand-subdomain');
            const tagline = document.querySelector('.n-brand-tagline');
            const topbar = document.querySelector('.n-topbar, .n-dateline');
            const navbar = document.querySelector('.n-nav');
            const ticker = document.querySelector('.n-ticker');
            const container = document.querySelector('.ht-container');

            if (topbar) {
                const cs = window.getComputedStyle(topbar);
                report.headerSections.topbar = {
                    padding: cs.padding,
                    margin: cs.margin,
                    display: cs.display,
                    flexWrap: cs.flexWrap
                };
            }

            if (masthead) {
                const cs = window.getComputedStyle(masthead);
                report.headerSections.masthead = {
                    padding: cs.padding,
                    margin: cs.margin,
                    borderBottom: cs.borderBottom
                };
            }

            if (wordmark) {
                const a = wordmark.querySelector('a');
                const cs = window.getComputedStyle(wordmark);
                report.headerSections.wordmark = {
                    text: a ? a.innerText.trim() : wordmark.innerText.trim(),
                    fontSize: cs.fontSize,
                    lineHeight: cs.lineHeight,
                    margin: cs.margin
                };
            }

            if (subdomain) {
                const cs = window.getComputedStyle(subdomain);
                report.headerSections.subdomain = {
                    text: subdomain.innerText.trim(),
                    display: cs.display,
                    fontSize: cs.fontSize,
                    color: cs.color,
                    margin: cs.margin
                };
            }

            if (tagline) {
                const cs = window.getComputedStyle(tagline);
                report.headerSections.tagline = {
                    text: tagline.innerText.trim(),
                    fontSize: cs.fontSize,
                    color: cs.color,
                    margin: cs.margin
                };
            }

            if (navbar) {
                const cs = window.getComputedStyle(navbar);
                const searchTrigger = navbar.querySelector('.n-nav-search-trigger span');
                report.headerSections.navbar = {
                    padding: cs.padding,
                    height: navbar.offsetHeight,
                    searchSpanText: searchTrigger ? searchTrigger.innerText : null
                };
            }

            if (ticker) {
                const cs = window.getComputedStyle(ticker);
                const rect = ticker.getBoundingClientRect();
                report.headerSections.ticker = {
                    width: rect.width,
                    left: rect.left,
                    right: rect.right,
                    margin: cs.margin,
                    borderRadius: cs.borderRadius
                };
                if (rect.left === 0 && rect.right === window.innerWidth) {
                    report.issues.push({
                        type: 'TICKER_FULL_BLEED',
                        detail: 'Ticker has 0 horizontal margin and touches screen edges directly without container padding'
                    });
                }
            }

            // Check container padding
            if (container) {
                const cs = window.getComputedStyle(container);
                report.headerSections.container = {
                    paddingLeft: cs.paddingLeft,
                    paddingRight: cs.paddingRight,
                    width: container.offsetWidth
                };
                if (parseFloat(cs.paddingLeft) < 8 || parseFloat(cs.paddingRight) < 8) {
                    report.issues.push({
                        type: 'CONTAINER_ZERO_PADDING',
                        detail: `Container padding is left: ${cs.paddingLeft}, right: ${cs.paddingRight}. Content touches screen edge.`
                    });
                }
            }

            // Check sections padding & cards
            const sections = document.querySelectorAll('section');
            sections.forEach(sec => {
                const cs = window.getComputedStyle(sec);
                const rect = sec.getBoundingClientRect();
                if (parseFloat(cs.paddingLeft) === 0 && parseFloat(cs.paddingRight) === 0 && (rect.left === 0)) {
                    report.elementsTouchingEdge.push({
                        tag: sec.tagName,
                        className: sec.className,
                        padding: cs.padding
                    });
                }
            });

            // Check Search input placeholder for 'Ctrl+K' on mobile
            const searchInputs = document.querySelectorAll('input[type=\"search\"], .n-nav-search-trigger, .ht-search-trigger');
            searchInputs.forEach(el => {
                const text = el.innerText || el.getAttribute('placeholder') || '';
                if (text.includes('Ctrl+K') || text.includes('Ctrl')) {
                    report.issues.push({
                        type: 'KEYBOARD_SHORTCUT_ON_MOBILE',
                        detail: `Found desktop shortcut '${text.trim()}' visible in mobile view`
                    });
                }
            });

            return report;
        """)

        print("\n=== HOMEPAGE MOBILE AUDIT ===")
        print(json.dumps(hp_report, indent=2, ensure_ascii=False))

        # 3. Capture Single Post Mobile Audit if post_link found
        sp_report = {}
        if post_link:
            print(f"\n[*] Navigating to Single Post: {post_link}...")
            driver.get(post_link)
            time.sleep(3)

            sp_screenshot = os.path.join(output_dir, 'live_mobile_single_post_390.png')
            driver.save_screenshot(sp_screenshot)
            print(f"   ✅ Saved single post mobile screenshot: {sp_screenshot}")

            sp_report = driver.execute_script("""
                const rep = {
                    title: document.title,
                    scrollWidth: document.documentElement.scrollWidth,
                    viewportWidth: window.innerWidth,
                    hasHorizontalScroll: document.documentElement.scrollWidth > window.innerWidth,
                    articlePadding: null,
                    featuredImage: null,
                    fontSizeH1: null,
                    issues: []
                };

                const article = document.querySelector('article, .n-single-article, .htbd-article');
                if (article) {
                    const cs = window.getComputedStyle(article);
                    rep.articlePadding = cs.padding;
                }

                const h1 = document.querySelector('h1, .entry-title, .n-article-title');
                if (h1) {
                    const cs = window.getComputedStyle(h1);
                    rep.fontSizeH1 = cs.fontSize;
                    rep.lineHeightH1 = cs.lineHeight;
                    const rect = h1.getBoundingClientRect();
                    if (rect.left < 8) {
                        rep.issues.push({
                            type: 'TITLE_TOUCHING_EDGE',
                            detail: `H1 title touches screen edge (left: ${rect.left}px)`
                        });
                    }
                }

                const featImg = document.querySelector('.n-article-banner img, .wp-post-image, .entry-thumbnail img');
                if (featImg) {
                    const rect = featImg.getBoundingClientRect();
                    const cs = window.getComputedStyle(featImg);
                    rep.featuredImage = {
                        width: rect.width,
                        borderRadius: cs.borderRadius
                    };
                }

                return rep;
            """)
            print("\n=== SINGLE POST MOBILE AUDIT ===")
            print(json.dumps(sp_report, indent=2, ensure_ascii=False))

        full_results = {
            'homepage': hp_report,
            'singlePost': sp_report
        }
        with open(os.path.join(output_dir, 'live_mobile_deep_audit.json'), 'w', encoding='utf-8') as f:
            json.dump(full_results, f, indent=2, ensure_ascii=False)

    finally:
        driver.quit()

if __name__ == '__main__':
    run_deep_live_audit()
