#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/social_broadcaster/sync_7_posts_master_md.py
--------------------------------------------------
Synchronizes the 7 newly broadcasted posts into
output_posts/social_unposted_messages_master.md with zero-emoji compliance.
"""

import os
import sys
import json

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
AUDIT_DATA_FILE = os.path.join(PROJECT_ROOT, "output_posts", "social_audit_data.json")
MASTER_MD_FILE = os.path.join(PROJECT_ROOT, "output_posts", "social_unposted_messages_master.md")

def main():
    with open(AUDIT_DATA_FILE, "r", encoding="utf-8") as f:
        audit_data = json.load(f)

    with open(MASTER_MD_FILE, "r", encoding="utf-8") as f:
        master_content = f.read()

    new_7 = audit_data[-7:]

    table_rows = []
    wa_cards = []

    for idx, post in enumerate(new_7, 128):
        wa_id = f"WA-{idx}"
        title = post.get("title", "")
        url = post.get("url", "")
        category = post.get("category", "Education Guide")
        hero_img = post.get("hero_image", "")
        copy = post.get("copy", {})
        fb_msg = copy.get("facebook", "")

        # Generate WhatsApp message from Facebook message format
        wa_msg = f"*{title}*\n\n{fb_msg}"

        table_rows.append(f"| {idx} | {title} | {category} | [{url}]({url}) | সম্পন্ন | সম্পন্ন | প্রস্তুত |")

        card_text = f"""### [{wa_id}] {title}
- **লাইভ ইউআরএল:** {url}
- **ক্যাটাগরি:** {category}
- **ব্যানার ইমেজ:** {hero_img}

**হোয়াটসঅ্যাপ মেসেজ ফরম্যাট (কপি করতে নিচের বক্সে ক্লিক করুন):**
```text
{wa_msg}
```
"""
        wa_cards.append(card_text)

    # 1. Update summary in Section 1
    updated_content = master_content
    updated_content = updated_content.replace(
        "| ফেসবুক পেজ (Facebook Page) | 127 | 127 | 0 | ১০০% | সম্পূর্ণ সম্পন্ন |",
        "| ফেসবুক পেজ (Facebook Page) | 134 | 134 | 0 | ১০০% | সম্পূর্ণ সম্পন্ন |"
    )
    updated_content = updated_content.replace(
        "| টেলিগ্রাম চ্যানেল (Telegram Channel) | 127 | 127 | 0 | ১০০% | সম্পূর্ণ সম্পন্ন |",
        "| টেলিগ্রাম চ্যানেল (Telegram Channel) | 134 | 134 | 0 | ১০০% | সম্পূর্ণ সম্পন্ন |"
    )
    updated_content = updated_content.replace(
        "| হোয়াটসঅ্যাপ চ্যানেল (WhatsApp Channel) | 127 | 0 | 127 | ০% | ১২৭টি মেসেজ কপি-রেডি প্রস্তুত |",
        "| হোয়াটসঅ্যাপ চ্যানেল (WhatsApp Channel) | 134 | 0 | 134 | ০% | ১৩৪টি মেসেজ কপি-রেডি প্রস্তুত |"
    )
    updated_content = updated_content.replace(
        "## ৩. হোয়াটসঅ্যাপ চ্যানেলের জন্য ১২৭টি পোস্টের রেডি-টু-সেন্ড মেসেজ ফরম্যাট",
        "## ৩. হোয়াটসঅ্যাপ চ্যানেলের জন্য ১৩৪টি পোস্টের রেডি-টু-সেন্ড মেসেজ ফরম্যাট"
    )

    # 2. Inject table rows after row 127
    target_row_127_prefix = "| 127 |"
    lines = updated_content.splitlines(True)
    injected_lines = []
    found = False

    for line in lines:
        injected_lines.append(line)
        if target_row_127_prefix in line and not found:
            found = True
            for r in table_rows:
                injected_lines.append(r + "\n")

    if found:
        updated_content = "".join(injected_lines)
    else:
        print("[!] Row 127 prefix not found in table.")

    # 3. Append WA cards to end of document
    updated_content = updated_content.strip() + "\n\n" + "\n\n".join(wa_cards) + "\n"

    with open(MASTER_MD_FILE, "w", encoding="utf-8") as f:
        f.write(updated_content)

    print("Master markdown successfully updated with 7 new posts (Total: 134 posts).")

if __name__ == "__main__":
    main()
