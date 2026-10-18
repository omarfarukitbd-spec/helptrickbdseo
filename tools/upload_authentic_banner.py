import os
import sys
import json
import requests

sys.stdout.reconfigure(encoding='utf-8')

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.wp_publisher.publisher import WordPressPublisher

publisher = WordPressPublisher()
banner_path = os.path.join(PROJECT_ROOT, "assets", "images", "posts", "ntrca_school_level_assistant_teacher_syllabus_2026.webp")

print(f"[*] Uploading authentic banner: {banner_path} ({os.path.getsize(banner_path)} bytes)...")
media_id = publisher.upload_featured_image(
    file_path=banner_path,
    alt_text="NTRCA স্কুল পর্যায় সিলেবাস 2026 সহকারী শিক্ষক পূর্ণাঙ্গ সিলেবাস ও মানবণ্টন",
    title="NTRCA স্কুল পর্যায় সিলেবাস 2026"
)

if media_id:
    print(f"[SUCCESS] Uploaded authentic featured image! Media ID: {media_id}")
    # Get media URL
    res = requests.get(f"{publisher.client.base_url}/wp-json/wp/v2/media/{media_id}", auth=publisher.client.auth)
    if res.status_code == 200:
        url = res.json().get('source_url')
        print(f"[*] Media URL: {url}")
        with open('tools/latest_media.json', 'w', encoding='utf-8') as f:
            json.dump({'media_id': media_id, 'url': url}, f, indent=2)
else:
    print("[ERROR] Failed to upload featured image!")
    sys.exit(1)
