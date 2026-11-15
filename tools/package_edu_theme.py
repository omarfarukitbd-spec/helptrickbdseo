#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/package_edu_theme.py
Packages HelpTrickBD EduPortal (helptrickbd-edu) into WordPress installable ZIP archive
with 100% UNIX POSIX attributes and syncs to Updated Theme/.
"""

import os
import shutil
import zipfile
import time
import stat

def package_edu_theme():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    source_dir = os.path.join(base_dir, 'Helptrickbd Wp', 'helptrickbd-edu')
    dest_dir = os.path.join(base_dir, 'Updated Theme', 'helptrickbd-edu')
    zip_dest = os.path.join(base_dir, 'Updated Theme', 'helptrickbd-edu.zip')
    zip_ver_dest = os.path.join(base_dir, 'Updated Theme', 'helptrickbd-edu-v1.0.0.zip')

    if not os.path.exists(source_dir):
        print(f"❌ Error: Theme directory not found at {source_dir}")
        return False

    os.makedirs(os.path.join(base_dir, 'Updated Theme'), exist_ok=True)

    # 1. Sync source files to Updated Theme/helptrickbd-edu/
    print(f"[*] Syncing source files to {dest_dir}...")
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
    shutil.copytree(source_dir, dest_dir)
    print("   ✅ Sync completed.")

    # 2. Package installable ZIP
    print(f"[*] Building WordPress installable ZIP at {zip_dest}...")
    now = time.localtime()[:6]

    with zipfile.ZipFile(zip_dest, 'w', zipfile.ZIP_DEFLATED) as z:
        # Root directory entry
        root_zinfo = zipfile.ZipInfo('helptrickbd-edu/', now)
        root_zinfo.create_system = 3  # UNIX
        root_zinfo.external_attr = ((stat.S_IFDIR | 0o755) << 16) | 0x10
        root_zinfo.compress_type = zipfile.ZIP_STORED
        z.writestr(root_zinfo, '')

        # Walk directory
        for root, dirs, files in os.walk(source_dir):
            dirs.sort()
            files.sort()

            for d in dirs:
                dir_full = os.path.join(root, d)
                rel_dir = 'helptrickbd-edu/' + os.path.relpath(dir_full, source_dir).replace('\\', '/') + '/'
                d_zinfo = zipfile.ZipInfo(rel_dir, now)
                d_zinfo.create_system = 3
                d_zinfo.external_attr = ((stat.S_IFDIR | 0o755) << 16) | 0x10
                d_zinfo.compress_type = zipfile.ZIP_STORED
                z.writestr(d_zinfo, '')

            for f in files:
                if f.endswith('.zip') or f in ('.DS_Store', 'Thumbs.db'):
                    continue
                file_full = os.path.join(root, f)
                rel_file = 'helptrickbd-edu/' + os.path.relpath(file_full, source_dir).replace('\\', '/')
                f_zinfo = zipfile.ZipInfo(rel_file, now)
                f_zinfo.create_system = 3
                f_zinfo.external_attr = ((stat.S_IFREG | 0o644) << 16) | 0x20
                with open(file_full, 'rb') as fp:
                    z.writestr(f_zinfo, fp.read())

    # Copy versioned zip
    shutil.copyfile(zip_dest, zip_ver_dest)
    zip_size = os.path.getsize(zip_dest) / 1024
    print(f"   🎉 Successfully built {zip_dest} ({zip_size:.2f} KB)")
    print(f"   🎉 Versioned copy: {zip_ver_dest}")
    return True

if __name__ == '__main__':
    package_edu_theme()
