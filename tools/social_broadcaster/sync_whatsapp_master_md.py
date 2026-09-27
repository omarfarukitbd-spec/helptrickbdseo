#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/social_broadcaster/sync_whatsapp_master_md.py
---------------------------------------------------
Synchronizes the 15 newly broadcasted SSC Bangla 1st Paper posts into
output_posts/social_unposted_messages_master.md with ready-to-send, zero-AI,
high-engagement WhatsApp message cards ([WA-113] to [WA-127]).
"""

import os
import sys
import json
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
AUDIT_DATA_FILE = os.path.join(PROJECT_ROOT, "output_posts", "social_audit_data.json")
MASTER_MD_FILE = os.path.join(PROJECT_ROOT, "output_posts", "social_unposted_messages_master.md")

def main():
    if not os.path.exists(AUDIT_DATA_FILE) or not os.path.exists(MASTER_MD_FILE):
        print("[!] Required files not found.")
        return

    with open(AUDIT_DATA_FILE, "r", encoding="utf-8") as f:
        audit_data = json.load(f)

    with open(MASTER_MD_FILE, "r", encoding="utf-8") as f:
        master_content = f.read()

    # The 15 newest posts are at the beginning of audit_data (index 0 to 14)
    # Let's order them in natural chronological sequence for WhatsApp: WA-113 to WA-127
    new_15 = audit_data[:15]
    # Reverse so they go from Master Pillar / Part 1 -> CQ Banks -> Model Test
    new_15_ordered = list(reversed(new_15))

    # Build new table rows for Section 2
    table_rows = []
    # Build new WhatsApp cards for Section 3
    wa_cards = []

    for idx, post in enumerate(new_15_ordered, 113):
        wa_id = f"WA-{idx}"
        title = post.get("title", "")
        url = post.get("url", "")
        category = post.get("category", "এসএসসি ও দাখিল স্টাডি গাইড")
        hero_img = post.get("hero_image", "")
        copy = post.get("copy", {})
        wa_msg = copy.get("whatsapp", "")

        # Table row: | 113 | Title | Category | URL | সম্পন্ন | সম্পন্ন | প্রস্তুত |
        table_rows.append(f"| {idx} | {title} | {category} | [{url}]({url}) | সম্পন্ন | সম্পন্ন | প্রস্তুত |")

        # WhatsApp card
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

    # 1. Update Section 1 summary numbers
    updated_content = master_content
    updated_content = updated_content.replace(
        "| ফেসবুক পেজ (Facebook Page) | 112 | 112 | 0 | ১০০% | সম্পূর্ণ সম্পন্ন |",
        "| ফেসবুক পেজ (Facebook Page) | 127 | 127 | 0 | ১০০% | সম্পূর্ণ সম্পন্ন |"
    )
    updated_content = updated_content.replace(
        "| টেলিগ্রাম চ্যানেল (Telegram Channel) | 112 | 112 | 0 | ১০০% | সম্পূর্ণ সম্পন্ন |",
        "| টেলিগ্রাম চ্যানেল (Telegram Channel) | 127 | 127 | 0 | ১০০% | সম্পূর্ণ সম্পন্ন |"
    )
    updated_content = updated_content.replace(
        "| হোয়াটসঅ্যাপ চ্যানেল (WhatsApp Channel) | 112 | 0 | 112 | ০% | ১১২টি মেসেজ কপি-রেডি প্রস্তুত |",
        "| হোয়াটসঅ্যাপ চ্যানেল (WhatsApp Channel) | 127 | 0 | 127 | ০% | ১২৭টি মেসেজ কপি-রেডি প্রস্তুত |"
    )
    updated_content = updated_content.replace(
        "## ৩. হোয়াটসঅ্যাপ চ্যানেলের জন্য ১১২টি পোস্টের রেডি-টু-সেন্ড মেসেজ ফরম্যাট",
        "## ৩. হোয়াটসঅ্যাপ চ্যানেলের জন্য ১২৭টি পোস্টের রেডি-টু-সেন্ড মেসেজ ফরম্যাট"
    )

    # 2. Inject table rows before Section 3
    target_table_end = "| 112 | আধুনিক রাষ্ট্রচিন্তা ২০১৯ সালের প্রশ্নের নির্ভুল উত্তরমালা ও সমাধান (২০২৬) | সাধারণ জ্ঞান, প্রবন্ধ ও অন্যান্য | [https://www.helptrickbd.com/2024/11/modern-political-thought-answer-sheet-2019-pdf.html](https://www.helptrickbd.com/2024/11/modern-political-thought-answer-sheet-2019-pdf.html) | সম্পন্ন | সম্পন্ন | বাকি |\n"
    if target_table_end in updated_content:
        replacement_table = target_table_end + "\n".join(table_rows) + "\n"
        updated_content = updated_content.replace(target_table_end, replacement_table)
    else:
        print("[!] Target table row not found for injection.")

    # 3. Append WA cards to the end of the file
    updated_content = updated_content.strip() + "\n\n" + "\n\n".join(wa_cards) + "\n"

    with open(MASTER_MD_FILE, "w", encoding="utf-8") as f:
        f.write(updated_content)

    print(f"Successfully injected 15 new WhatsApp post cards ([WA-113] to [WA-127]) into {MASTER_MD_FILE}!")

if __name__ == "__main__":
    main()
