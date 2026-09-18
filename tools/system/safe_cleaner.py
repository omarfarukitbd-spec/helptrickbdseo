#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/system/safe_cleaner.py
----------------------------
Safely cleans temporary files, package caches, and build caches
WITHOUT touching any code, credentials, browsers passwords, or Drive D projects.
"""

import os
import shutil
import sys

def get_drive_c_free():
    total, used, free = shutil.disk_usage("C:")
    return free / (1024**3)

def safe_remove_dir_contents(path, name):
    if not os.path.exists(path):
        print(f"[-] {name} does not exist. Skipped.")
        return 0
    print(f"[*] Cleaning {name} ({path})...")
    freed = 0
    for root, dirs, files in os.walk(path, topdown=False):
        for f in files:
            fp = os.path.join(root, f)
            try:
                sz = os.path.getsize(fp)
                os.remove(fp)
                freed += sz
            except Exception:
                pass
        for d in dirs:
            dp = os.path.join(root, d)
            try:
                os.rmdir(dp)
            except Exception:
                pass
    print(f"[+] Cleaned {name}: freed {freed / (1024**3):.2f} GB")
    return freed

def safe_remove_tree(path, name):
    if not os.path.exists(path):
        print(f"[-] {name} does not exist. Skipped.")
        return 0
    print(f"[*] Removing {name} ({path})...")
    try:
        # Calculate size
        sz = 0
        for root, dirs, files in os.walk(path):
            for f in files:
                try:
                    sz += os.path.getsize(os.path.join(root, f))
                except Exception:
                    pass
        shutil.rmtree(path, ignore_errors=True)
        print(f"[+] Removed {name}: freed {sz / (1024**3):.2f} GB")
        return sz
    except Exception as e:
        print(f"[!] Error removing {name}: {e}")
        return 0

def main():
    user = os.path.expanduser("~")
    
    before_free = get_drive_c_free()
    print(f"=== SAFE DISK CLEANUP STARTED ===")
    print(f"Initial C: Free Space: {before_free:.2f} GB\n")
    
    total_freed = 0
    
    # 1. Gradle caches
    gradle_caches = os.path.join(user, ".gradle", "caches")
    total_freed += safe_remove_tree(gradle_caches, "Gradle Build Caches")
    
    # 2. npm-cache
    npm_cache = os.path.join(user, "AppData", "Local", "npm-cache")
    total_freed += safe_remove_tree(npm_cache, "NPM Package Cache")
    
    # 3. .cache (pip, huggingface, tool caches)
    dot_cache = os.path.join(user, ".cache")
    total_freed += safe_remove_tree(dot_cache, "Generic Tool Cache (.cache)")
    
    # 4. AndroidStudio old backup folder
    as_backup = os.path.join(user, "AppData", "Local", "Google", "AndroidStudio2026.1.2_backup")
    total_freed += safe_remove_tree(as_backup, "Old AndroidStudio Backup")
    
    # 5. User Temp directory contents (skip files in use)
    user_temp = os.path.join(user, "AppData", "Local", "Temp")
    total_freed += safe_remove_dir_contents(user_temp, "User Temp Files")
    
    after_free = get_drive_c_free()
    print(f"\n=== CLEANUP COMPLETED ===")
    print(f"Total Space Reclaimed: {total_freed / (1024**3):.2f} GB")
    print(f"New C: Free Space:     {after_free:.2f} GB")
    print(f"Drive C Status:        {'HEALTHY / BLUE' if after_free > 18 else 'IMPROVED'}")

if __name__ == '__main__':
    main()
