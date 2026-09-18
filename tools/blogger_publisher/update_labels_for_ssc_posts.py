import os
import sys
import json
import time

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tools.blogger_publisher.publisher import get_authenticated_service, BLOG_ID

# Target posts to update with the new labels
TARGET_POST_IDS = [
    # Live Posts from English 2nd Paper
    {"id": "5074244725044328705", "name": "Post 02: Substitution Table"},
    {"id": "4513403598587272029", "name": "Post 03: Right Form of Verbs"},
    # Scheduled Posts
    {"id": "4210603287369740506", "name": "Post 10: Changing Sentences"},
    {"id": "6576972447245567621", "name": "Post 11: Tag Questions"},
    {"id": "848541826459702618",  "name": "Post 12: Suffix & Prefix"},
    {"id": "7959520177371215724", "name": "Post 13: Preposition & Gap Filling"},
    {"id": "2728520994420779689", "name": "Post 14: Connectors & Punctuation"},
    {"id": "2819164478523778841", "name": "Post 15: Writing Part"},
    {"id": "9216323938062929290", "name": "Post 16: Model Test & Board Question"},
    {"id": "7160657224948521919", "name": "Post 17: Master Golden Post"}
]

NEW_LABELS = ["Education Guide", "SSC Suggestion", "Dakhil Suggestion"]

def update_post_labels():
    print("=" * 75)
    print("UPDATING LABELS ON BLOGGER FOR SSC ENGLISH 2ND PAPER POSTS")
    print(f"Target Labels: {NEW_LABELS}")
    print("=" * 75)

    service = get_authenticated_service()
    if not service:
        print("[ERROR] Could not authenticate Blogger API.")
        sys.exit(1)

    success_count = 0
    for item in TARGET_POST_IDS:
        post_id = item["id"]
        post_name = item["name"]
        print(f"\n[*] Processing {post_name} (ID: {post_id})...")

        try:
            # Fetch existing post (view='ADMIN' required for SCHEDULED posts)
            existing = service.posts().get(blogId=BLOG_ID, postId=post_id, view="ADMIN").execute()
            current_labels = existing.get("labels", [])
            published_time = existing.get("published")
            status = existing.get("status")

            # Merge labels uniquely while preserving order
            merged_labels = list(dict.fromkeys(current_labels + ["SSC Suggestion", "Dakhil Suggestion"]))
            # Ensure "Education Guide" is present
            if "Education Guide" not in merged_labels:
                merged_labels.insert(0, "Education Guide")

            patch_body = {
                "labels": merged_labels,
                "published": published_time
            }

            updated = service.posts().patch(
                blogId=BLOG_ID,
                postId=post_id,
                body=patch_body
            ).execute()

            print(f"    [OK] Labels updated: {updated.get('labels')} | Status: {updated.get('status')}")
            success_count += 1
            # Delay to protect against API rate limits
            time.sleep(4)

        except Exception as e:
            print(f"    [ERROR] Failed to update {post_id}: {e}")
            time.sleep(5)

    print("\n" + "=" * 75)
    print(f"[OK] Completed: {success_count}/{len(TARGET_POST_IDS)} posts updated successfully.")
    print("=" * 75)

if __name__ == "__main__":
    update_post_labels()
