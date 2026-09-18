#!/usr/bin/env python3
"""
tools/social_broadcaster/whatsapp_helper.py
HelpTrickBD Safe 1-Click WhatsApp Channel Broadcast Helper.

Copies formatted human-feel copy to clipboard and opens WhatsApp Channel
for seamless 1-click broadcast without any ban or restriction risk.
Strictly zero-emoji compliant.
"""

import sys
import subprocess
import webbrowser
import urllib.parse
from typing import Dict, Any

try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass


class WhatsAppHelper:
    """Zero-risk 1-click broadcaster for WhatsApp Channel."""

    def __init__(self, channel_link: str = "https://whatsapp.com/channel/0029Vb956jgCHDyrx1wkUh2a"):
        self.channel_link = channel_link.strip()

    def copy_to_clipboard(self, text: str) -> bool:
        """Copies text to Windows clipboard via native clip command."""
        try:
            process = subprocess.Popen(
                ["clip"],
                stdin=subprocess.PIPE,
                close_fds=True,
                shell=True
            )
            process.communicate(input=text.encode("utf-16"))
            return True
        except Exception:
            return False

    def open_channel_window(self) -> bool:
        """Opens the WhatsApp Channel URL in the default browser."""
        try:
            webbrowser.open(self.channel_link)
            return True
        except Exception:
            return False

    def trigger_broadcast(self, text: str) -> Dict[str, Any]:
        """Executes the safe 1-click broadcast flow: copies text & opens channel."""
        clipboard_ok = self.copy_to_clipboard(text)
        browser_ok = self.open_channel_window()

        return {
            "success": True,
            "clipboard_copied": clipboard_ok,
            "browser_opened": browser_ok,
            "message": "হোয়াটসঅ্যাপ চ্যানেলের জন্য ফরম্যাটেড টেক্সট ক্লিপবোর্ডে কপি করা হয়েছে এবং চ্যানেলের লিংক ব্রাউজারে ওপেন করা হয়েছে।"
        }
