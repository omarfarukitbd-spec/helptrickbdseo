#!/usr/bin/env python3
"""
HelpTrickBD Smart Scheduling Optimizer
Calculates the peak traffic publication window for educational content in Bangladesh:
Target: Exactly between 7:00 PM and 8:30 PM BST (19:00 - 20:30 UTC+6).

Features:
- Natural Minute Jitter (e.g. 19:18, 19:42, 20:12) to avoid robotic bot detection patterns.
- Multi-post Day Staggering (automatically allocates 1 post per day during prime time).
- Outputs RFC 3339 string formatted for Blogger API v3 (`published` / `updated`).

Usage:
    python scheduler_optimizer.py --days-ahead 0
    python scheduler_optimizer.py --batch-count 3
"""

import argparse
import datetime
import random
import sys

try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

# BST is UTC+6
BST_OFFSET = datetime.timezone(datetime.timedelta(hours=6))

# User's strict requirement: 7:00 PM - 8:30 PM (19:00 - 20:30)
WINDOW_START_HOUR = 19
WINDOW_START_MINUTE = 5
WINDOW_END_HOUR = 20
WINDOW_END_MINUTE = 25


def calculate_optimal_post_time(days_ahead=0):
    """
    Returns an RFC 3339 formatted publication datetime within 19:00 - 20:30 BST.
    """
    now_bst = datetime.datetime.now(BST_OFFSET)
    target_date = now_bst.date() + datetime.timedelta(days=days_ahead)

    # Randomize minute between 19:05 and 20:25 for natural variation
    total_minutes = random.randint(19 * 60 + WINDOW_START_MINUTE, 20 * 60 + WINDOW_END_MINUTE)
    target_hour = total_minutes // 60
    target_minute = total_minutes % 60
    target_second = random.randint(10, 50)

    target_dt = datetime.datetime(
        target_date.year,
        target_date.month,
        target_date.day,
        target_hour,
        target_minute,
        target_second,
        tzinfo=BST_OFFSET
    )

    # If scheduled for today but the window has already passed, push to tomorrow
    if days_ahead == 0 and target_dt <= now_bst:
        return calculate_optimal_post_time(days_ahead=1)

    rfc3339_str = target_dt.isoformat()
    readable_bst = target_dt.strftime("%d %B %Y, %I:%M:%S %p (BST / বাংলাদেশ সময়)")

    return {
        "rfc3339": rfc3339_str,
        "readable": readable_bst,
        "date": target_date.strftime("%Y-%m-%d"),
        "time": f"{target_hour:02d}:{target_minute:02d}:{target_second:02d}"
    }


def generate_batch_schedule(count=1):
    """Generates scheduled publication slots for N posts, 1 post per day at prime time."""
    slots = []
    for day in range(count):
        slot = calculate_optimal_post_time(days_ahead=day)
        slots.append(slot)
    return slots


def main():
    parser = argparse.ArgumentParser(description="HelpTrickBD Peak-Time Scheduler (7:00 PM - 8:30 PM BST)")
    parser.add_argument("--days-ahead", type=int, default=0, help="Number of days in future (0 = today)")
    parser.add_argument("--batch-count", type=int, default=1, help="Number of posts to schedule across consecutive days")

    args = parser.parse_args()

    if args.batch_count > 1:
        print(f"\n[*] Generating Prime Schedule for {args.batch_count} Articles (Strict Window: 7:00 PM - 8:30 PM BST):")
        slots = generate_batch_schedule(args.batch_count)
        for idx, s in enumerate(slots, 1):
            print(f"  Post #{idx}: {s['readable']}")
            print(f"           RFC3339: {s['rfc3339']}\n")
    else:
        slot = calculate_optimal_post_time(args.days_ahead)
        print(f"\n[OK] Optimal Publication Slot (Strict 7:00 PM - 8:30 PM BST):")
        print(f"  Human Time: {slot['readable']}")
        print(f"  RFC 3339:   {slot['rfc3339']}\n")


if __name__ == "__main__":
    main()
