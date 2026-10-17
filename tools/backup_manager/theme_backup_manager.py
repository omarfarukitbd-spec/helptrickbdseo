#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/backup_manager/theme_backup_manager.py
---------------------------------------------
HelpTrickBD Pro - Automated WordPress Theme Pre-Edit Backup & Instant Rollback System.
Enforces Rule 09: Always take a full snapshot & installable zip of the active theme
before modifying any theme file.

Usage:
    python tools/backup_manager/theme_backup_manager.py backup --reason "mobile_heading_fix"
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

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
THEME_DIR = os.path.join(PROJECT_ROOT, "Helptrickbd Wp", "helptrickbd-theme")
BACKUP_BASE_DIR = os.path.join(PROJECT_ROOT, "backups", "theme")
LATEST_DIR = os.path.join(BACKUP_BASE_DIR, "latest")

def get_theme_version():
    """Extract theme version from style.css."""
    style_css = os.path.join(THEME_DIR, "style.css")
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
    Creates a zip archive with explicit directory entries and UNIX POSIX permissions (0755/0644).
    Root folder inside zip is 'helptrickbd-theme/'.
    """
    os.makedirs(os.path.dirname(output_zip_path), exist_ok=True)
    with zipfile.ZipFile(output_zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        # Explicit root folder entry
        root_dir_entry = zipfile.ZipInfo("helptrickbd-theme/")
        root_dir_entry.external_attr = 0o755 << 16 | 0o040000
        root_dir_entry.date_time = datetime.now().timetuple()[:6]
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
                zinfo = zipfile.ZipInfo(dir_path)
                zinfo.external_attr = 0o755 << 16 | 0o040000
                zinfo.date_time = datetime.now().timetuple()[:6]
                zf.writestr(zinfo, "")

            for f in files:
                if f.endswith(".zip") or f == ".DS_Store":
                    continue
                file_abs = os.path.join(root, f)
                file_rel = f"{zip_base}/{f}"
                with open(file_abs, "rb") as fp:
                    data = fp.read()
                zinfo = zipfile.ZipInfo(file_rel)
                zinfo.external_attr = 0o644 << 16 | 0o100000
                zinfo.date_time = datetime.now().timetuple()[:6]
                zf.writestr(zinfo, data)

def backup_theme(reason="manual_pre_edit"):
    """Takes a complete timestamped snapshot of helptrickbd-theme."""
    if not os.path.exists(THEME_DIR):
        print(f"[!] Error: Theme directory not found at {THEME_DIR}")
        return False

    version = get_theme_version()
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d_%H%M%S")
    reason_slug = slugify(reason) if reason else "pre_edit"
    
    backup_folder_name = f"wp_theme_{timestamp}_v{version}_{reason_slug}"
    target_backup_dir = os.path.join(BACKUP_BASE_DIR, backup_folder_name)
    theme_copy_dir = os.path.join(target_backup_dir, "helptrickbd-theme")

    print(f"[*] Starting Theme Pre-Edit Backup...")
    print(f"    Source:  {THEME_DIR}")
    print(f"    Version: v{version}")
    print(f"    Reason:  {reason}")

    # 1. Copy full directory
    os.makedirs(target_backup_dir, exist_ok=True)
    shutil.copytree(THEME_DIR, theme_copy_dir, dirs_exist_ok=True)

    # 2. Package installable backup zip
    backup_zip_path = os.path.join(target_backup_dir, f"helptrickbd-theme-v{version}-{timestamp}.zip")
    create_theme_zip(THEME_DIR, backup_zip_path)
    zip_size_kb = os.path.getsize(backup_zip_path) / 1024

    # 3. Count files & total size
    total_files = 0
    total_bytes = 0
    for root, _, files in os.walk(THEME_DIR):
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

    # 5. Update latest mirror
    if os.path.exists(LATEST_DIR):
        shutil.rmtree(LATEST_DIR)
    shutil.copytree(theme_copy_dir, LATEST_DIR, dirs_exist_ok=True)
    # copy zip and metadata to latest as well
    shutil.copy2(backup_zip_path, os.path.join(LATEST_DIR, "helptrickbd-theme-latest.zip"))
    shutil.copy2(os.path.join(target_backup_dir, "metadata.json"), os.path.join(LATEST_DIR, "metadata.json"))

    print(f"\n[+] Theme Backup Completed Successfully!")
    print(f"    Backup Folder: {target_backup_dir}")
    print(f"    Installable Zip: {backup_zip_path} ({zip_size_kb:.2f} KB)")
    print(f"    Latest Snapshot: {LATEST_DIR}")
    print(f"    Safety Status: Ready for safe editing.\n")
    return True

def list_backups():
    """Lists all available theme backups."""
    if not os.path.exists(BACKUP_BASE_DIR):
        print(f"[!] No backups found in {BACKUP_BASE_DIR}")
        return

    backups = []
    for item in os.listdir(BACKUP_BASE_DIR):
        full_path = os.path.join(BACKUP_BASE_DIR, item)
        if os.path.isdir(full_path) and item.startswith("wp_theme_"):
            meta_path = os.path.join(full_path, "metadata.json")
            if os.path.exists(meta_path):
                with open(meta_path, "r", encoding="utf-8") as f:
                    meta = json.load(f)
                    backups.append((item, meta))
            else:
                backups.append((item, {"date_human": "N/A", "reason": "No metadata", "theme_version": "N/A"}))

    backups.sort(key=lambda x: x[0], reverse=True)

    print("\n======================================================================")
    print(" [*] HELPTRICKBD PRO - WORDPRESS THEME BACKUP REPOSITORY")
    print("======================================================================")
    if not backups:
        print(" [!] No WordPress theme backups found yet.")
    else:
        for i, (name, meta) in enumerate(backups, 1):
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
    if not target_identifier or target_identifier.lower() == "latest":
        if os.path.exists(LATEST_DIR):
            source_dir = LATEST_DIR
        else:
            print("[!] Latest backup directory does not exist.")
            return False
    else:
        # Search by folder name or timestamp
        for item in os.listdir(BACKUP_BASE_DIR):
            if target_identifier in item:
                cand = os.path.join(BACKUP_BASE_DIR, item, "helptrickbd-theme")
                if os.path.exists(cand):
                    source_dir = cand
                    break

    if not source_dir or not os.path.exists(source_dir):
        print(f"[!] Could not locate valid backup matching: {target_identifier}")
        return False

    # Safety: Take temporary emergency snapshot before overwriting
    temp_safety = os.path.join(BACKUP_BASE_DIR, "_pre_restore_safety_backup")
    if os.path.exists(THEME_DIR):
        if os.path.exists(temp_safety):
            shutil.rmtree(temp_safety)
        shutil.copytree(THEME_DIR, temp_safety)

    print(f"[*] Restoring theme from: {source_dir}")
    print(f"    Target: {THEME_DIR}")

    # Copy files
    for root, _, files in os.walk(source_dir):
        rel = os.path.relpath(root, source_dir)
        dest_root = os.path.join(THEME_DIR, rel)
        os.makedirs(dest_root, exist_ok=True)
        for f in files:
            if f.endswith(".zip") or f == "metadata.json":
                continue
            shutil.copy2(os.path.join(root, f), os.path.join(dest_root, f))

    # Regenerate primary theme zip
    zip_out = os.path.join(PROJECT_ROOT, "Helptrickbd Wp", "helptrickbd-theme.zip")
    create_theme_zip(THEME_DIR, zip_out)

    print(f"[+] Theme successfully restored!")
    print(f"    Live files restored in: {THEME_DIR}")
    print(f"    Re-packaged installable zip: {zip_out}\n")
    return True

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="HelpTrickBD Theme Pre-Edit Backup & Rollback Tool")
    subparsers = parser.add_subparsers(dest="command")

    # backup
    backup_p = subparsers.add_parser("backup", help="Create a pre-edit theme backup")
    backup_p.add_argument("--reason", default="pre_edit_safety_snapshot", help="Reason or description of upcoming edits")

    # list
    subparsers.add_parser("list", help="List all theme backups")

    # restore
    restore_p = subparsers.add_parser("restore", help="Restore theme from backup")
    restore_p.add_argument("--timestamp", default="latest", help="Backup timestamp or folder name (default: latest)")

    args = parser.parse_args()

    if args.command == "backup":
        backup_theme(args.reason)
    elif args.command == "list":
        list_backups()
    elif args.command == "restore":
        restore_theme(args.timestamp)
    else:
        # Default behavior if no argument: backup
        backup_theme("default_snapshot")
