#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def capture_screenshots():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    html_path = os.path.join(base_dir, 'tools', 'preview_edu_portal.html')
    output_dir = os.path.join(base_dir, 'docs', 'images')
    os.makedirs(output_dir, exist_ok=True)

    file_url = f"file:///{html_path.replace(os.sep, '/')}"

    opts = Options()
    opts.add_argument('--headless')
    opts.add_argument('--disable-gpu')
    opts.add_argument('--no-sandbox')
    opts.add_argument('--hide-scrollbars')

    driver = webdriver.Chrome(options=opts)

    try:
        # 1. Desktop 1440px
        print(f"[*] Navigating to {file_url} (Desktop 1440px)...")
        driver.set_window_size(1440, 1080)
        driver.get(file_url)
        time.sleep(2)
        total_height = driver.execute_script("return document.body.parentNode.scrollHeight")
        driver.set_window_size(1440, total_height)
        time.sleep(1)
        desktop_img = os.path.join(output_dir, 'edu_portal_desktop_1440.png')
        driver.save_screenshot(desktop_img)
        print(f"   ✅ Saved desktop screenshot: {desktop_img} ({os.path.getsize(desktop_img) / 1024:.1f} KB)")

        # 2. Mobile 390px
        print(f"[*] Navigating to {file_url} (Mobile 390px)...")
        driver.set_window_size(390, 844)
        driver.get(file_url)
        time.sleep(2)
        total_height_m = driver.execute_script("return document.body.parentNode.scrollHeight")
        driver.set_window_size(390, total_height_m)
        time.sleep(1)
        mobile_img = os.path.join(output_dir, 'edu_portal_mobile_390.png')
        driver.save_screenshot(mobile_img)
        print(f"   ✅ Saved mobile screenshot: {mobile_img} ({os.path.getsize(mobile_img) / 1024:.1f} KB)")

    finally:
        driver.quit()

if __name__ == '__main__':
    capture_screenshots()
