import os
import sys
import json
import time
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.blogger_publisher.publisher import get_authenticated_service, BLOG_ID

HTML_FILE = os.path.join(PROJECT_ROOT, "content", "drafts", "post-17-ssc-golden-master.html")
META_FILE = os.path.join(PROJECT_ROOT, "content", "drafts", "post-17-ssc-golden-master_metadata.json")

def schedule_golden_master(sched_time="2026-09-19T11:30:00+06:00", readable_time="আজ সকাল ১১:৩০ BST"):
    print("=" * 75)
    print("HELPTRICKBD BLOGGER SCHEDULE ENGINE - SSC ENGLISH 2ND PAPER MASTER GOLDEN POST")
    print("=" * 75)

    service = get_authenticated_service()
    if not service:
        print("[ERROR] Failed to authenticate Blogger API v3.")
        sys.exit(1)

    with open(META_FILE, "r", encoding="utf-8") as f:
        meta = json.load(f)
    with open(HTML_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    slug = meta["slug"]
    full_title = meta["title"]
    label = meta.get("labels", ["Education Guide"])[0] if isinstance(meta.get("labels"), list) else meta.get("labels", "Education Guide")

    print(f"\n[Master Golden Post]")
    print(f"       Title:          {full_title}")
    print(f"       Slug:           {slug}")
    print(f"       Category Label: {label}")
    print(f"       Schedule Time:  {readable_time} ({sched_time})")

    # STEP 1: Mint clean English permalink with future scheduled time
    body = {
        "kind": "blogger#post",
        "blog": {"id": BLOG_ID},
        "title": slug,
        "content": content,
        "labels": [label],
        "published": sched_time
    }

    try:
        print("\n       [*] Step 1: Minting clean English permalink on Blogger (Scheduled)...")
        result = service.posts().insert(blogId=BLOG_ID, body=body, isDraft=False).execute()
        post_id = result.get("id")
        initial_url = result.get("url")
        status = result.get("status")
        print(f"       [OK] Post Minted! ID: {post_id} | Status: {status}")
        print(f"           Minted URL: {initial_url}")

        time.sleep(3)

        # STEP 2: Update title to full academic title (preserving schedule time)
        print("       [*] Step 2: Updating post title to full academic title...")
        patch_body = {
            "title": full_title,
            "published": sched_time
        }
        updated = service.posts().patch(blogId=BLOG_ID, postId=post_id, body=patch_body).execute()
        final_url = updated.get("url")
        final_status = updated.get("status")
        print(f"       [OK] Academic Title Updated Successfully!")
        print(f"           Final Live URL: {final_url} | Status: {final_status}")

        record = {
            "id": post_id,
            "title": full_title,
            "published": sched_time,
            "url": final_url,
            "status": final_status,
            "labels": [label]
        }

        # Save record
        record_path = os.path.join(PROJECT_ROOT, "output_posts", "scheduled_golden_master_post.json")
        with open(record_path, "w", encoding="utf-8") as out_f:
            json.dump(record, out_f, ensure_ascii=False, indent=2)
        print(f"\n[OK] Record saved to {record_path}")
        return record

    except Exception as e:
        print(f"       [ERROR] Scheduling failed: {e}")
        return None

if __name__ == "__main__":
    schedule_golden_master()
