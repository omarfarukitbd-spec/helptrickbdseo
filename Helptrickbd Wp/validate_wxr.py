import xml.etree.ElementTree as ET
import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

WORKSPACE_DIR = "d:/android/Project/Helptrickbd Wp"

files_to_check = [
    ("helptrickbd_part1_posts_01_to_45.xml", 45),
    ("helptrickbd_part2_posts_46_to_90.xml", 45),
    ("helptrickbd_part3_posts_91_to_134.xml", 44),
    ("helptrickbd_wp_import_all_134.xml", 134),
    ("helptrickbd_wp_import.xml", 134)
]

print("=== Starting XML Syntax & Integrity Validation ===\n")

all_passed = True
total_validated_items = 0

for filename, expected_count in files_to_check:
    filepath = os.path.join(WORKSPACE_DIR, filename)
    print(f"Checking {filename}...")
    if not os.path.exists(filepath):
        print(f"  ❌ File not found: {filepath}")
        all_passed = False
        continue
        
    try:
        tree = ET.parse(filepath)
        root = tree.getroot()
        channel = root.find("channel")
        if channel is None:
            print("  ❌ No <channel> element found!")
            all_passed = False
            continue
            
        items = channel.findall("item")
        actual_count = len(items)
        if actual_count != expected_count:
            print(f"  ❌ Item count mismatch: expected {expected_count}, got {actual_count}")
            all_passed = False
            continue
            
        # Verify first and last item in this file
        first_title = items[0].find("title").text
        first_id = items[0].find("{http://wordpress.org/export/1.2/}post_id").text
        last_title = items[-1].find("title").text
        last_id = items[-1].find("{http://wordpress.org/export/1.2/}post_id").text
        
        # Check that content:encoded is present and non-empty in all items
        empty_content_count = 0
        jump_break_count = 0
        total_content_len = 0
        for it in items:
            content_elem = it.find("{http://purl.org/rss/1.0/modules/content/}encoded")
            if content_elem is None or not content_elem.text or len(content_elem.text.strip()) == 0:
                empty_content_count += 1
            else:
                total_content_len += len(content_elem.text)
                if "<!--more-->" in content_elem.text:
                    jump_break_count += 1
                    
        if empty_content_count > 0:
            print(f"  ❌ Found {empty_content_count} items with empty content!")
            all_passed = False
            continue
            
        print(f"  ✅ VALID WXR 1.2 XML! Count: {actual_count}/{expected_count}")
        print(f"     First: ID {first_id} - '{first_title[:35]}...'")
        print(f"     Last:  ID {last_id} - '{last_title[:35]}...'")
        print(f"     Avg content size: {total_content_len // actual_count:,} chars | Jump breaks: {jump_break_count}")
        
    except ET.ParseError as pe:
        print(f"  ❌ XML Parse Error in {filename}: {pe}")
        all_passed = False
    except Exception as e:
        print(f"  ❌ Unexpected error in {filename}: {e}")
        all_passed = False
    print()

if all_passed:
    print("🎉 ALL XML IMPORT FILES ARE 100% VALID AND PRODUCTION READY!")
else:
    print("❌ VALIDATION FAILED! Check errors above.")
    sys.exit(1)
