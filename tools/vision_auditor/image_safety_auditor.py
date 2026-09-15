#!/usr/bin/env python3
"""
tools/vision_auditor/image_safety_auditor.py
HelpTrickBD Visual Asset & Core Web Vitals Image Safety Auditor.

Performs a comprehensive automated audit across all images in the project and post HTMLs:
1. File Format & Weight Check: Strictly audits against the 10-20 KB WebP standard.
2. Aspect Ratio & Dimensions Check: Verifies 16:9 hero banners (1200x675) and social cards (1200x630).
3. Image SEO & Accessibility Check: Validates alt tags, title tags, <figure>, <figcaption>, and loading="lazy".
4. Visual Quality & Contrast: Detects corrupted, washed out, or completely dark images.
5. Auto-Optimization & Fix Hook: Automatically invokes webp_compressor to convert non-compliant images to 10-20 KB WebP.
"""

import os
import sys
import glob
import math
import argparse
from typing import List, Dict, Tuple
from PIL import Image, ImageStat
from bs4 import BeautifulSoup

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

from tools.image_optimizer.webp_compressor import compress_to_target_webp


class ImageSafetyAuditor:
    def __init__(self, target_min_kb: float = 10.0, target_max_kb: float = 20.0):
        self.target_min_kb = target_min_kb
        self.target_max_kb = target_max_kb
        self.asset_results: List[Dict] = []
        self.html_results: List[Dict] = []

    def audit_image_file(self, file_path: str) -> Dict:
        """Audits a single image file on disk."""
        rel_path = os.path.relpath(file_path, PROJECT_ROOT)
        size_bytes = os.path.getsize(file_path)
        size_kb = size_bytes / 1024.0
        ext = os.path.splitext(file_path)[1].lower()

        status = "PASS"
        issues = []

        # Check format
        is_webp = (ext == ".webp")
        if not is_webp:
            issues.append(f"Format is {ext.upper()}, not WebP")

        # Check target size (10-20 KB)
        if size_kb > self.target_max_kb:
            status = "FAIL" if size_kb > 50 else "WARNING"
            issues.append(f"Oversized ({size_kb:.1f} KB > {self.target_max_kb} KB limit)")
        elif size_kb < self.target_min_kb and is_webp:
            issues.append(f"Undersized ({size_kb:.1f} KB < {self.target_min_kb} KB min, may lack detail)")

        # Image dimension and contrast check
        width, height = 0, 0
        ratio = 0.0
        brightness = 0.0
        try:
            with Image.open(file_path) as img:
                width, height = img.size
                ratio = round(width / height, 2) if height > 0 else 0
                
                # Check 16:9 ratio (tolerance 1.70 - 1.85) or 1.91 (1200x630 OG)
                is_16_9 = 1.70 <= ratio <= 1.85
                is_og = 1.88 <= ratio <= 1.95
                if not (is_16_9 or is_og):
                    issues.append(f"Non-standard aspect ratio ({ratio}:1, expected 16:9 [1.78] or OG [1.90])")

                # Brightness / Contrast check
                grayscale = img.convert("L")
                stat = ImageStat.Stat(grayscale)
                brightness = stat.mean[0]
                if brightness < 15:
                    status = "FAIL"
                    issues.append("Image is almost pitch black (brightness < 15)")
                elif brightness > 245:
                    status = "FAIL"
                    issues.append("Image is completely blown out / blank white (brightness > 245)")

        except Exception as e:
            status = "FAIL"
            issues.append(f"Corrupted or unreadable image: {e}")

        result = {
            "path": rel_path,
            "filename": os.path.basename(file_path),
            "size_kb": round(size_kb, 2),
            "format": ext.replace(".", "").upper(),
            "dimensions": f"{width}x{height}",
            "aspect_ratio": ratio,
            "brightness": round(brightness, 1),
            "status": status,
            "issues": issues
        }
        return result

    def scan_asset_directories(self, dirs: List[str]):
        """Scans specified asset folders for image files."""
        extensions = ("*.jpg", "*.jpeg", "*.png", "*.webp")
        for d in dirs:
            abs_dir = os.path.join(PROJECT_ROOT, d)
            if not os.path.exists(abs_dir):
                continue
            for ext in extensions:
                for file_path in glob.glob(os.path.join(abs_dir, "**", ext), recursive=True):
                    res = self.audit_image_file(file_path)
                    self.asset_results.append(res)

    def audit_html_post_images(self, html_path: str) -> List[Dict]:
        """Audits all img tags inside an article HTML for SEO, lazy loading, and semantic structure."""
        rel_path = os.path.relpath(html_path, PROJECT_ROOT)
        with open(html_path, "r", encoding="utf-8") as f:
            content = f.read()

        soup = BeautifulSoup(content, "html.parser")
        images = soup.find_all("img")
        post_img_results = []

        for idx, img in enumerate(images):
            src = img.get("src", "")
            alt = img.get("alt", "").strip()
            title = img.get("title", "").strip()
            loading = img.get("loading", "").lower()
            parent = img.parent.name if img.parent else ""

            issues = []
            status = "PASS"

            # 1. Alt tag check
            if not alt:
                status = "FAIL"
                issues.append("Missing alt tag (Critical for Google Image SEO & Accessibility)")
            elif len(alt) < 10:
                status = "WARNING"
                issues.append(f"Short generic alt tag ('{alt}')")

            # 2. Lazy loading check
            if loading != "lazy" and idx > 0: # First image (hero) can be eager, subsequent must be lazy
                issues.append("Missing loading='lazy' (Negatively impacts Core Web Vitals LCP/INP)")
                if status == "PASS":
                    status = "WARNING"

            # 3. Semantic figure check
            if parent != "figure":
                issues.append("Not enclosed in semantic <figure> / <figcaption> tags")
                if status == "PASS":
                    status = "WARNING"

            # 4. WebP extension in URL
            if src and not (".webp" in src.lower() or "bp.blogspot.com" in src.lower()):
                issues.append("Image source does not reference modern WebP format")

            post_img_results.append({
                "post": rel_path,
                "img_index": idx + 1,
                "src": src[:60] + "..." if len(src) > 60 else src,
                "alt": alt,
                "has_title": bool(title),
                "loading": loading or "none",
                "in_figure": (parent == "figure"),
                "status": status,
                "issues": issues
            })

        self.html_results.extend(post_img_results)
        return post_img_results

    def generate_markdown_report(self, output_file: str = "image_safety_audit_report.md") -> str:
        """Generates an executive Markdown report of all audited visual assets."""
        report_path = os.path.join(PROJECT_ROOT, output_file)

        total_assets = len(self.asset_results)
        total_html_imgs = len(self.html_results)

        passed_assets = sum(1 for a in self.asset_results if a["status"] == "PASS")
        warn_assets = sum(1 for a in self.asset_results if a["status"] == "WARNING")
        fail_assets = sum(1 for a in self.asset_results if a["status"] == "FAIL")

        passed_html = sum(1 for h in self.html_results if h["status"] == "PASS")
        warn_html = sum(1 for h in self.html_results if h["status"] == "WARNING")
        fail_html = sum(1 for h in self.html_results if h["status"] == "FAIL")

        lines = [
            "# 📸 HelpTrickBD Visual Asset & Core Web Vitals Image Safety Audit",
            f"**Audit Date:** ২০২৬ সংস্করণ | **Target WebP Standard:** {self.target_min_kb} - {self.target_max_kb} KB",
            f"**Total Local Assets Scanned:** {total_assets} | **Post Embedded Images:** {total_html_imgs}\n",
            "---",
            "## 📊 Executive Summary Scorecard\n",
            "| Asset Type | Total Inspected | 🟢 Passed | 🟡 Warning | 🔴 Needs Fix | Compliance % |",
            "| :--- | :---: | :---: | :---: | :---: | :---: |",
            f"| **Disk Media Assets (`assets/images`)** | {total_assets} | {passed_assets} | {warn_assets} | {fail_assets} | {(passed_assets/total_assets*100 if total_assets else 100):.1f}% |",
            f"| **Post HTML Images (`<img>` tags)** | {total_html_imgs} | {passed_html} | {warn_html} | {fail_html} | {(passed_html/total_html_imgs*100 if total_html_imgs else 100):.1f}% |\n",
            "---",
            "## 🖼️ Local Media Assets Detailed Audit\n",
            "| File Path | Format | Size (KB) | 10-20KB Compliant? | Dimensions | Ratio | Status | Issues / Notes |",
            "| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |"
        ]

        for a in self.asset_results:
            is_compliant = "✅ Yes" if (self.target_min_kb <= a["size_kb"] <= self.target_max_kb and a["format"] == "WEBP") else "❌ No"
            status_icon = "🟢" if a["status"] == "PASS" else ("🟡" if a["status"] == "WARNING" else "🔴")
            issue_str = ", ".join(a["issues"]) if a["issues"] else "Optimal WebP asset"
            lines.append(f"| `{a['path']}` | {a['format']} | {a['size_kb']} KB | {is_compliant} | {a['dimensions']} | {a['aspect_ratio']}:1 | {status_icon} {a['status']} | {issue_str} |")

        lines.extend([
            "\n---",
            "## 🔍 Post HTML Embedded Images Audit (Semantic SEO & CWV)\n",
            "| Post File | Img # | Alt Tag | Lazy Load | In `<figure>` | Status | Remediation Required |",
            "| :--- | :---: | :--- | :---: | :---: | :---: | :--- |"
        ])

        for h in self.html_results:
            status_icon = "🟢" if h["status"] == "PASS" else ("🟡" if h["status"] == "WARNING" else "🔴")
            alt_preview = f"'{h['alt'][:35]}...'" if len(h['alt']) > 35 else f"'{h['alt']}'"
            lazy_icon = "✅" if h["loading"] == "lazy" else "⚠️ Missing"
            fig_icon = "✅" if h["in_figure"] else "⚠️ Missing"
            issue_str = ", ".join(h["issues"]) if h["issues"] else "100% SEO compliant"
            lines.append(f"| `{h['post']}` | #{h['img_index']} | {alt_preview} | {lazy_icon} | {fig_icon} | {status_icon} {h['status']} | {issue_str} |")

        lines.extend([
            "\n---",
            "## 💡 Actionable Recommendations for 100% Core Web Vitals Compliance",
            "1. **Compress Non-WebP Banners:** Run `python tools/image_optimizer/webp_compressor.py -i <IMAGE_PATH>` on all PNG/JPG banners to convert them into 10–20 KB WebP.",
            "2. **Add `loading='lazy'`:** Ensure every image below the fold contains `loading='lazy'` to maximize Largest Contentful Paint (LCP) speed.",
            "3. **Semantic `<figure>` Wrapping:** Wrap content images with `<figure>` and `<figcaption>` with descriptive Bengali captions for AdSense editorial credit and Google Image search ranking."
        ])

        with open(report_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))

        return report_path


def main():
    parser = argparse.ArgumentParser(description="HelpTrickBD Visual Asset & Image Safety Auditor")
    parser.add_argument("--scan_assets", action="store_true", default=True, help="Scan assets directory")
    parser.add_argument("--scan_posts", action="store_true", default=True, help="Scan post HTMLs in output_posts")
    parser.add_argument("--auto_fix", action="store_true", help="Auto-compress flagged images to 10-20KB WebP")
    parser.add_argument("--output", "-o", type=str, default="image_safety_audit_report.md", help="Output Markdown report")

    args = parser.parse_args()

    print("\n=======================================================")
    print("  HelpTrickBD Visual Asset & Image Safety Auditor")
    print("=======================================================")

    auditor = ImageSafetyAuditor(target_min_kb=10.0, target_max_kb=20.0)

    if args.scan_assets:
        print("[*] Scanning media asset folders...")
        auditor.scan_asset_directories(["assets/images", "assets"])

    if args.scan_posts:
        print("[*] Scanning output posts for embedded image tags...")
        post_files = glob.glob(os.path.join(PROJECT_ROOT, "output_posts", "**", "*.html"), recursive=True)
        for pf in post_files:
            auditor.audit_html_post_images(pf)

    report_path = auditor.generate_markdown_report(args.output)
    print(f"\n[+] Image Safety & Quality Audit completed successfully!")
    print(f"[+] Detailed Markdown Report: {report_path}")

    # If auto-fix requested
    if args.auto_fix:
        print("\n[*] Running Auto-Fix: Compressing non-compliant images to 10-20 KB WebP...")
        fixed_count = 0
        for asset in auditor.asset_results:
            if asset["format"] != "WEBP" or asset["size_kb"] > 20.0:
                full_path = os.path.join(PROJECT_ROOT, asset["path"])
                base, _ = os.path.splitext(full_path)
                out_webp = f"{base}.webp"
                try:
                    compress_to_target_webp(full_path, out_webp, target_min_kb=10.0, target_max_kb=20.0)
                    fixed_count += 1
                    print(f"  [⚡ Fixed] {asset['path']} -> {os.path.basename(out_webp)} ({os.path.getsize(out_webp)/1024:.1f} KB)")
                except Exception as e:
                    print(f"  [!] Failed to auto-fix {asset['path']}: {e}")
        print(f"[+] Total images optimized: {fixed_count}")


if __name__ == "__main__":
    main()
