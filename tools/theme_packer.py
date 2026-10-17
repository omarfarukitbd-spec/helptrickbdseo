"""
HelpTrickBD Pro - WordPress Theme Packaging Utility
Creates 100% Linux/UNIX and WordPress-compliant theme ZIP archives with proper
directory structures and POSIX permissions (0755 for dirs, 0644 for files).
"""

import os
import zipfile
import time

def package_theme():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    theme_dir = os.path.join(base_dir, 'Helptrickbd Wp', 'helptrickbd-theme')
    zip_path = os.path.join(base_dir, 'Helptrickbd Wp', 'helptrickbd-theme.zip')

    if not os.path.exists(theme_dir):
        print(f"Error: Theme directory not found at {theme_dir}")
        return False

    now = time.localtime()[:6]
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as z:
        # 1. Root directory entry: helptrickbd-theme/
        root_zinfo = zipfile.ZipInfo('helptrickbd-theme/', now)
        root_zinfo.create_system = 3  # UNIX
        root_zinfo.external_attr = (0o755 << 16) | 0x10  # drwxr-xr-x
        z.writestr(root_zinfo, '')

        # 2. Walk directory structure
        for root, dirs, files in os.walk(theme_dir):
            # Write directory entries with 0755
            for d in dirs:
                dir_full = os.path.join(root, d)
                rel_dir = os.path.relpath(dir_full, os.path.dirname(theme_dir)).replace('\\', '/') + '/'
                d_zinfo = zipfile.ZipInfo(rel_dir, now)
                d_zinfo.create_system = 3  # UNIX
                d_zinfo.external_attr = (0o755 << 16) | 0x10  # drwxr-xr-x
                z.writestr(d_zinfo, '')

            # Write file entries with 0644
            for f in files:
                file_full = os.path.join(root, f)
                rel_file = os.path.relpath(file_full, os.path.dirname(theme_dir)).replace('\\', '/')
                with open(file_full, 'rb') as fp:
                    data = fp.read()
                f_zinfo = zipfile.ZipInfo(rel_file, now)
                f_zinfo.create_system = 3  # UNIX
                f_zinfo.external_attr = 0o644 << 16  # -rw-r--r--
                z.writestr(f_zinfo, data)

    size_kb = os.path.getsize(zip_path) / 1024
    print(f"Theme packaged successfully: {zip_path} ({size_kb:.2f} KB)")
    return True

if __name__ == '__main__':
    package_theme()
