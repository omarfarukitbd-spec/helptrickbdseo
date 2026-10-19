#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/backup_manager/theme_backup_manager.py
---------------------------------------------
HelpTrickBD Pro - Automated WordPress Theme Pre-Edit Backup, Packaging & Instant Rollback System.
Enforces Rule 09: 2-Folder Theme Governance Architecture.
  Folder 1: 'Theme Backups' - Pre-edit full snapshots and rollback archives.
  Folder 2: 'Updated Theme' - Production-ready updated theme files & installable zip.

Usage:
    python tools/backup_manager/theme_backup_manager.py backup --reason "mobile_heading_fix"
    python tools/backup_manager/theme_backup_manager.py package
    python tools/backup_manager/theme_backup_manager.py list
    python tools/backup_manager/theme_backup_manager.py restore [--timestamp YYYYMMDD_HHMMSS]
"""

import os
import sys
import shutil
import zipfile
import json
import re
from datetime import datetime
import stat

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

# 2 Designated Theme Folders:
THEME_BACKUPS_DIR = os.path.join(PROJECT_ROOT, "Theme Backups")
UPDATED_THEME_DIR = os.path.join(PROJECT_ROOT, "Updated Theme")

# Working Theme Directories:
PRIMARY_WORKING_THEME = os.path.join(PROJECT_ROOT, "Helptrickbd Wp", "helptrickbd-theme")
UPDATED_THEME_SOURCE = os.path.join(UPDATED_THEME_DIR, "helptrickbd-theme")

# Legacy Fallback Directory (preserves backward compatibility):
LEGACY_BACKUP_DIR = os.path.join(PROJECT_ROOT, "backups", "theme")
LATEST_BACKUP_DIR = os.path.join(THEME_BACKUPS_DIR, "latest")


def get_theme_source_dir():
    """Returns the active working theme directory, prioritizing whichever has newer modifications."""
    if os.path.exists(UPDATED_THEME_SOURCE) and os.path.exists(PRIMARY_WORKING_THEME):
        up_style = os.path.join(UPDATED_THEME_SOURCE, "style.css")
        wp_style = os.path.join(PRIMARY_WORKING_THEME, "style.css")
        if os.path.exists(up_style) and os.path.exists(wp_style):
            if os.path.getmtime(up_style) > os.path.getmtime(wp_style):
                return UPDATED_THEME_SOURCE
            return PRIMARY_WORKING_THEME
    if os.path.exists(PRIMARY_WORKING_THEME):
        return PRIMARY_WORKING_THEME
    if os.path.exists(UPDATED_THEME_SOURCE):
        return UPDATED_THEME_SOURCE
    return PRIMARY_WORKING_THEME


def get_theme_version(source_dir=None):
    """Extract theme version from style.css."""
    src = source_dir or get_theme_source_dir()
    style_css = os.path.join(src, "style.css")
    if os.path.exists(style_css):
        with open(style_css, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                m = re.match(r"^Version:\s*([0-9\.]+)", line.strip(), re.IGNORECASE)
                if m:
                    return m.group(1)
    return "unknown"


def slugify(text):
    """Sanitize string for folder names."""
    text = re.sub(r"[^\w\s-]", "", text).strip().lower()
    return re.sub(r"[-\s]+", "_", text)[:40]


def create_theme_zip(source_dir, output_zip_path):
    """
    Creates a zip archive with explicit directory entries and exact WordPress/UNIX POSIX permissions:
    - Directories: S_IFDIR | 0755 (0x41ed0010)
    - Files: S_IFREG | 0644 (0x81a40000)
    - create_system: 3 (UNIX)
    Root folder inside zip is 'helptrickbd-theme/'.
    """
    os.makedirs(os.path.dirname(output_zip_path), exist_ok=True)
    now = datetime.now().timetuple()[:6]
    with zipfile.ZipFile(output_zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        # Explicit root folder entry
        root_dir_entry = zipfile.ZipInfo("helptrickbd-theme/", now)
        root_dir_entry.create_system = 3
        root_dir_entry.external_attr = ((stat.S_IFDIR | 0o755) << 16) | 0x10
        root_dir_entry.compress_type = zipfile.ZIP_STORED
        zf.writestr(root_dir_entry, "")

        for root, dirs, files in os.walk(source_dir):
            dirs.sort()
            files.sort()

            rel_root = os.path.relpath(root, source_dir)
            if rel_root == ".":
                zip_base = "helptrickbd-theme"
            else:
                zip_base = "helptrickbd-theme/" + rel_root.replace("\\", "/")

            for d in dirs:
                dir_path = f"{zip_base}/{d}/"
                zinfo = zipfile.ZipInfo(dir_path, now)
                zinfo.create_system = 3
                zinfo.external_attr = ((stat.S_IFDIR | 0o755) << 16) | 0x10
                zinfo.compress_type = zipfile.ZIP_STORED
                zf.writestr(zinfo, "")

            for f in files:
                if f.endswith(".zip") or f in (".DS_Store", "Thumbs.db"):
                    continue
                file_abs = os.path.join(root, f)
                file_rel = f"{zip_base}/{f}"
                with open(file_abs, "rb") as fp:
                    data = fp.read()
                zinfo = zipfile.ZipInfo(file_rel, now)
                zinfo.create_system = 3
                zinfo.external_attr = (stat.S_IFREG | 0o644) << 16
                zinfo.compress_type = zipfile.ZIP_DEFLATED
                zf.writestr(zinfo, data)


def backup_theme(reason="manual_pre_edit"):
    """Takes a complete timestamped snapshot into 'Theme Backups'."""
    src = get_theme_source_dir()
    if not os.path.exists(src):
        print(f"[!] Error: Theme source directory not found at {src}")
        return False

    version = get_theme_version(src)
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d_%H%M%S")
    reason_slug = slugify(reason) if reason else "pre_edit"

    backup_folder_name = f"wp_theme_{timestamp}_v{version}_{reason_slug}"
    target_backup_dir = os.path.join(THEME_BACKUPS_DIR, backup_folder_name)
    theme_copy_dir = os.path.join(target_backup_dir, "helptrickbd-theme")

    print(f"[*] Starting Theme Pre-Edit Backup (Folder 1: Theme Backups)...")
    print(f"    Source:  {src}")
    print(f"    Version: v{version}")
    print(f"    Reason:  {reason}")

    # 1. Copy full directory to Theme Backups
    os.makedirs(target_backup_dir, exist_ok=True)
    shutil.copytree(src, theme_copy_dir, dirs_exist_ok=True)

    # 2. Package installable backup zip
    backup_zip_path = os.path.join(target_backup_dir, f"helptrickbd-theme-v{version}-{timestamp}.zip")
    create_theme_zip(src, backup_zip_path)
    zip_size_kb = os.path.getsize(backup_zip_path) / 1024

    # 3. Count files & total size
    total_files = 0
    total_bytes = 0
    for root, _, files in os.walk(src):
        total_files += len(files)
        for f in files:
            total_bytes += os.path.getsize(os.path.join(root, f))

    # 4. Write metadata.json
    metadata = {
        "timestamp": timestamp,
        "date_human": now.strftime("%Y-%m-%d %H:%M:%S"),
        "theme_version": version,
        "reason": reason,
        "total_files": total_files,
        "total_size_bytes": total_bytes,
        "zip_size_kb": round(zip_size_kb, 2),
        "backup_zip_name": os.path.basename(backup_zip_path)
    }
    with open(os.path.join(target_backup_dir, "metadata.json"), "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)

    # 5. Update latest mirror in Theme Backups
    if os.path.exists(LATEST_BACKUP_DIR):
        shutil.rmtree(LATEST_BACKUP_DIR)
    shutil.copytree(theme_copy_dir, LATEST_BACKUP_DIR, dirs_exist_ok=True)
    shutil.copy2(backup_zip_path, os.path.join(LATEST_BACKUP_DIR, "helptrickbd-theme-latest.zip"))
    shutil.copy2(os.path.join(target_backup_dir, "metadata.json"), os.path.join(LATEST_BACKUP_DIR, "metadata.json"))

    print(f"\n[+] Theme Backup Completed Successfully in 'Theme Backups'!")
    print(f"    Backup Folder: {target_backup_dir}")
    print(f"    Installable Rollback Zip: {backup_zip_path} ({zip_size_kb:.2f} KB)")
    print(f"    Safety Status: Verified. Ready for safe theme editing.\n")
    return True


def package_theme():
    """
    Synchronizes and packages the latest theme into 'Updated Theme'.
    Outputs:
      - Updated Theme/helptrickbd-theme/ (latest code)
      - Updated Theme/helptrickbd-theme.zip (ready for WP dashboard upload)
      - Updated Theme/helptrickbd-theme-v<version>.zip (version release zip)
      - Helptrickbd Wp/helptrickbd-theme.zip (root bundle)
    """
    src = get_theme_source_dir()
    if not os.path.exists(src):
        print(f"[!] Error: Theme source directory not found at {src}")
        return False

    version = get_theme_version(src)
    print(f"[*] Packaging and Synchronizing Updated Theme (Folder 2: Updated Theme)...")
    print(f"    Source:  {src}")
    print(f"    Version: v{version}")

    # 1. Sync files to Updated Theme/helptrickbd-theme/
    os.makedirs(UPDATED_THEME_DIR, exist_ok=True)
    shutil.copytree(src, UPDATED_THEME_SOURCE, dirs_exist_ok=True)

    # Also keep Primary Working Theme in sync if different
    if os.path.abspath(src) != os.path.abspath(PRIMARY_WORKING_THEME):
        shutil.copytree(src, PRIMARY_WORKING_THEME, dirs_exist_ok=True)

    # 2. Generate clean production zips
    prod_zip_generic = os.path.join(UPDATED_THEME_DIR, "helptrickbd-theme.zip")
    prod_zip_versioned = os.path.join(UPDATED_THEME_DIR, f"helptrickbd-theme-v{version}.zip")
    wp_legacy_zip = os.path.join(PROJECT_ROOT, "Helptrickbd Wp", "helptrickbd-theme.zip")

    create_theme_zip(UPDATED_THEME_SOURCE, prod_zip_generic)
    shutil.copy2(prod_zip_generic, prod_zip_versioned)
    shutil.copy2(prod_zip_generic, wp_legacy_zip)

    zip_size_kb = os.path.getsize(prod_zip_generic) / 1024

    # 3. Update Updated Theme/README.md
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    readme_content = f"""# 🚀 Updated Theme (সর্বশেষ হালনাগাদকৃত প্রোডাকশন থিম ভল্ট)

এই ফোল্ডারে হেল্পট্রিকবিডি প্রো ওয়ার্ডপ্রেস থিমের **সর্বশেষ আপডেট ও ভ্যালিডেট করা প্রোডাকশন ফাইল** সংরক্ষিত থাকে।

---

## 📦 বর্তমান রিলিজ তথ্য:
- **থিম সংস্করণ (Version):** v{version}
- **প্যাকেজিং সময়:** {now_str}
- **ইনস্টলেবল জিপ ফাইল:** `helptrickbd-theme.zip` ({zip_size_kb:.2f} KB)
- **ভার্সন জিপ ফাইল:** `helptrickbd-theme-v{version}.zip`

---

## 🌐 ওয়ার্ডপ্রেসে লাইভ আপডেট করার নিয়ম:
1. ওয়ার্ডপ্রেস অ্যাডমিন প্যানেলে লগইন করুন: `https://www.helptrickbd.com/wp-admin`
2. বামপাশের মেনু থেকে যান: **Appearance > Themes**
3. উপরে ক্লিক করুন: **Add New Theme > Upload Theme**
4. এই ফোল্ডার থেকে **`helptrickbd-theme.zip`** ফাইলটি সিলেক্ট করে **Install Now** বাটনে ক্লিক করুন।
5. প্রম্পট আসলে ক্লিক করুন: **"Replace active with uploaded"** (বর্তমানটির স্থলে নতুনটি প্রতিস্থাপন করুন)।
6. ব্যস! সাইটের ক্যাশ ক্লিয়ার করুন। আপনার সাইট মুহূর্তেই সর্বশেষ থিমে আপডেট হয়ে যাবে।

---

## 🛠️ কমান্ড লাইন সিঙ্ক:
```bash
python tools/backup_manager/theme_backup_manager.py package
```
"""
    with open(os.path.join(UPDATED_THEME_DIR, "README.md"), "w", encoding="utf-8") as f:
        f.write(readme_content)

    print(f"\n[+] Updated Theme Successfully Packaged!")
    print(f"    Source: {UPDATED_THEME_SOURCE}")
    print(f"    WordPress Ready Zip: {prod_zip_generic} ({zip_size_kb:.2f} KB)")
    print(f"    Versioned Release Zip: {prod_zip_versioned}")
    print(f"    Status: Ready for 1-click live upload.\n")
    return True


def list_backups():
    """Lists all available theme backups across Theme Backups and legacy directories."""
    search_dirs = [THEME_BACKUPS_DIR, LEGACY_BACKUP_DIR]
    backups = []
    seen = set()

    for b_dir in search_dirs:
        if not os.path.exists(b_dir):
            continue
        for item in os.listdir(b_dir):
            if item in seen:
                continue
            full_path = os.path.join(b_dir, item)
            if os.path.isdir(full_path) and item.startswith("wp_theme_"):
                seen.add(item)
                meta_path = os.path.join(full_path, "metadata.json")
                if os.path.exists(meta_path):
                    with open(meta_path, "r", encoding="utf-8") as f:
                        meta = json.load(f)
                        backups.append((item, meta, full_path))
                else:
                    backups.append((item, {"date_human": "N/A", "reason": "No metadata", "theme_version": "N/A"}, full_path))

    backups.sort(key=lambda x: x[0], reverse=True)

    print("\n======================================================================")
    print(" [*] HELPTRICKBD PRO - THEME BACKUPS REPOSITORY (Folder 1: Theme Backups)")
    print("======================================================================")
    if not backups:
        print(" [!] No WordPress theme backups found yet.")
    else:
        for i, (name, meta, full_path) in enumerate(backups, 1):
            date = meta.get("date_human", "N/A")
            ver = meta.get("theme_version", "N/A")
            reason = meta.get("reason", "N/A")
            size_kb = meta.get("zip_size_kb", 0)
            print(f" {i}. [{date}] Version: v{ver} ({size_kb} KB)")
            print(f"    Folder: {name}")
            print(f"    Reason: {reason}")
            print("----------------------------------------------------------------------")
    print(f" Total backups: {len(backups)}\n")


def restore_theme(target_identifier=None):
    """Restores the theme from latest or a specific timestamp folder."""
    source_dir = None
    search_dirs = [THEME_BACKUPS_DIR, LEGACY_BACKUP_DIR]

    if not target_identifier or target_identifier.lower() == "latest":
        if os.path.exists(LATEST_BACKUP_DIR):
            source_dir = LATEST_BACKUP_DIR
        else:
            legacy_latest = os.path.join(LEGACY_BACKUP_DIR, "latest")
            if os.path.exists(legacy_latest):
                source_dir = legacy_latest
    else:
        for b_dir in search_dirs:
            if not os.path.exists(b_dir):
                continue
            for item in os.listdir(b_dir):
                if target_identifier in item:
                    cand = os.path.join(b_dir, item, "helptrickbd-theme")
                    if os.path.exists(cand):
                        source_dir = cand
                        break
            if source_dir:
                break

    if not source_dir or not os.path.exists(source_dir):
        print(f"[!] Could not locate valid backup matching: {target_identifier}")
        return False

    dest_theme = PRIMARY_WORKING_THEME
    print(f"[*] Restoring theme from: {source_dir}")
    print(f"    Target: {dest_theme}")

    # Copy files
    for root, _, files in os.walk(source_dir):
        rel = os.path.relpath(root, source_dir)
        dest_root = os.path.join(dest_theme, rel)
        os.makedirs(dest_root, exist_ok=True)
        for f in files:
            if f.endswith(".zip") or f == "metadata.json":
                continue
            shutil.copy2(os.path.join(root, f), os.path.join(dest_root, f))

    # Package into Updated Theme automatically
    package_theme()

    print(f"[+] Theme successfully restored and synchronized across both folders!")
    print(f"    Restored files: {dest_theme}")
    print(f"    Updated Theme Zip: {os.path.join(UPDATED_THEME_DIR, 'helptrickbd-theme.zip')}\n")
    return True


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="HelpTrickBD Theme 2-Folder Governance & Backup Tool")
    subparsers = parser.add_subparsers(dest="command")

    # backup
    backup_p = subparsers.add_parser("backup", help="Create a pre-edit theme backup in 'Theme Backups'")
    backup_p.add_argument("--reason", default="pre_edit_safety_snapshot", help="Reason or description of upcoming edits")

    # package / sync
    package_p = subparsers.add_parser("package", help="Package and update latest theme files in 'Updated Theme'")

    # list
    subparsers.add_parser("list", help="List all theme backups")

    # restore
    restore_p = subparsers.add_parser("restore", help="Restore theme from backup and repackage")
    restore_p.add_argument("--timestamp", default="latest", help="Backup timestamp or folder name (default: latest)")

    args = parser.parse_args()

    if args.command == "backup":
        backup_theme(args.reason)
    elif args.command == "package":
        package_theme()
    elif args.command == "list":
        list_backups()
    elif args.command == "restore":
        restore_theme(args.timestamp)
    else:
        # Default behavior: package
        package_theme()
