# -*- coding: utf-8 -*-
import os, sys, shutil, zipfile, time, stat, re

def get_theme_version(style_path):
    if not os.path.exists(style_path):
        return '1.0.0'
    with open(style_path, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            m = re.match(r'^[ \t]*Version:[ \t]*(.+)$', line, re.I)
            if m:
                return m.group(1).strip()
    return '1.0.0'

def package():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    source_dir = os.path.join(base_dir, 'Helptrickbd Wp', 'helptrickbd-edu')
    dest_dir = os.path.join(base_dir, 'Updated Theme', 'helptrickbd-edu')
    style_path = os.path.join(source_dir, 'style.css')
    ver = get_theme_version(style_path)
    print(f'Detected Theme Version: {ver}')

    updated_theme_dir = os.path.join(base_dir, 'Updated Theme')
    os.makedirs(updated_theme_dir, exist_ok=True)

    # 1. Sync source files to Updated Theme/helptrickbd-edu/
    print(f'[*] Syncing source to {dest_dir}...')
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
    shutil.copytree(source_dir, dest_dir)
    print('   [OK] Directory sync completed.')

    # 2. Package installable ZIP
    zip_dest = os.path.join(updated_theme_dir, 'helptrickbd-edu.zip')
    zip_ver_dest = os.path.join(updated_theme_dir, f'helptrickbd-edu-v{ver}.zip')

    for zp in [zip_dest, zip_ver_dest]:
        if os.path.exists(zp):
            try:
                os.remove(zp)
            except Exception:
                pass

    print(f'[*] Building WordPress installable ZIP at {zip_dest}...')
    now = time.localtime()[:6]

    with zipfile.ZipFile(zip_dest, 'w', zipfile.ZIP_DEFLATED) as z:
        # Root directory entry
        root_zinfo = zipfile.ZipInfo('helptrickbd-edu/', now)
        root_zinfo.create_system = 3
        root_zinfo.external_attr = ((stat.S_IFDIR | 0o755) << 16) | 0x10
        root_zinfo.compress_type = zipfile.ZIP_STORED
        z.writestr(root_zinfo, '')

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

    # Copy versioned zip in Updated Theme
    shutil.copyfile(zip_dest, zip_ver_dest)
    print(f'   [OK] Created {zip_dest} ({os.path.getsize(zip_dest)/1024:.1f} KB)')
    print(f'   [OK] Created {zip_ver_dest} ({os.path.getsize(zip_ver_dest)/1024:.1f} KB)')

    # Also copy to Desktop for convenience
    desktop_dir = os.path.expanduser(r'~\Desktop')
    if os.path.exists(desktop_dir):
        desk_main = os.path.join(desktop_dir, 'helptrickbd-edu.zip')
        desk_ver = os.path.join(desktop_dir, f'helptrickbd-edu-v{ver}.zip')
        try:
            shutil.copyfile(zip_dest, desk_main)
            shutil.copyfile(zip_dest, desk_ver)
            print(f'   [OK] Copied to Desktop: {desk_ver}')
        except Exception as e:
            print(f'   [WARN] Could not copy to desktop: {e}')

if __name__ == '__main__':
    package()
