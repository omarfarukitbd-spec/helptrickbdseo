#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/governance/agent_permission_gate.py
-----------------------------------------
Interactive and Programmatic User Permission Gate for Helptrickbd SEO.
Enforces the Strict User Permission Matrix defined in:
.agents/rules/00_AGENT_CONSTITUTION.md

Restricted Actions that ALWAYS require explicit user confirmation:
1. add_label: Adding a new label/category to Blogger.
2. delete_post: Deleting a post from Blogger live or draft.
3. modify_permalink: Changing an existing live permalink.
4. replace_thumbnail: Overwriting an original author thumbnail.
5. translate_language: Translating an English post to Bengali or vice versa.
6. publish_live: Final live publishing to Blogger.
"""

import sys
import argparse

# Ensure utf-8 output encoding for Windows terminals
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# Restricted actions registry with Bengali/English explanations
RESTRICTED_ACTIONS = {
    "add_label": {
        "title": "Adding or Modifying Blogger Labels (লেবেল সংযোজন বা পরিবর্তন)",
        "why": "Uncontrolled labels dilute AdSense category balance, triggering 'Low Value Content' or 'Under Construction' rejection.",
        "prompt": "Did the user explicitly approve this specific label in the chat?"
    },
    "delete_post": {
        "title": "Deleting a Blogger Post (ব্লগার পোস্ট মুছে ফেলা)",
        "why": "Deleting live posts creates instant 404 dead links, destroys backlinks, and drops Google ranking.",
        "prompt": "Did the user give explicit permission to delete this post?"
    },
    "modify_permalink": {
        "title": "Modifying a Live Permalink / URL (লাইভ পারমালিঙ্ক পরিবর্তন)",
        "why": "Altering live URLs permanently breaks existing Google index entries, backlinks, and social shares.",
        "prompt": "Did the user explicitly confirm modifying this live URL?"
    },
    "replace_thumbnail": {
        "title": "Replacing Original Author Thumbnail (মৌলিক থাম্বনেইল প্রতিস্থাপন)",
        "why": "Author's original graphics must be preserved. Overwriting authentic graphics harms brand identity.",
        "prompt": "Did the user explicitly ask to replace this existing original thumbnail?"
    },
    "translate_language": {
        "title": "Cross-Language Translation (পোস্টের মূল ভাষা পরিবর্তন)",
        "why": "English articles have global high-RPM keyword intent. Translating them to Bengali (or vice versa) is strictly forbidden.",
        "prompt": "Has the user explicitly commanded to change the post's language?"
    },
    "publish_live": {
        "title": "Final Live Publishing to Blogger (ব্লগারে লাইভ পাবলিশ)",
        "why": "Publishing unverified drafts can push broken images, thin content, or missing jump breaks directly to production.",
        "prompt": "Has pre_flight_checker.py passed with 0 errors AND has the user approved live publishing?"
    }
}

def verify_gate(action_name, details="", user_confirmed=False):
    if action_name not in RESTRICTED_ACTIONS:
        print(f"[PERMISSION GATE] Action '{action_name}' is not restricted. Proceeding.")
        return True

    info = RESTRICTED_ACTIONS[action_name]
    print("\n" + "="*70)
    print(f"[STOP GATE] USER PERMISSION REQUIRED: {info['title']}")
    print("="*70)
    print(f"Action Details : {details}")
    print(f"Why Restricted : {info['why']}")
    print(f"Gate Check     : {info['prompt']}")
    print("-" * 70)

    if user_confirmed:
        print("RESULT: USER PERMISSION VERIFIED. PROCEEDING.")
        print("="*70 + "\n")
        return True
    else:
        print("RESULT: ACCESS DENIED / GATE HALTED.")
        print("STOP! The agent MUST ask the user for explicit permission before executing this action.")
        print("="*70 + "\n")
        return False

def main():
    parser = argparse.ArgumentParser(description="User Permission Gate for Autonomous AI Agents")
    parser.add_argument("action", choices=list(RESTRICTED_ACTIONS.keys()), help="Name of restricted action")
    parser.add_argument("--details", "-d", default="General request", help="Specific details of the action")
    parser.add_argument("--confirmed", "-c", action="store_true", help="Flag indicating user gave explicit consent in chat")
    args = parser.parse_args()

    allowed = verify_gate(args.action, args.details, args.confirmed)
    sys.exit(0 if allowed else 1)

if __name__ == "__main__":
    main()
