#!/usr/bin/env python3
"""
HelpTrickBD 1-Click Authenticator
Listens on localhost:8080 and captures the token once the user clicks the auth link.
"""

import os
import sys

try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ["https://www.googleapis.com/auth/blogger"]
CREDENTIALS_FILE = os.path.join(os.path.dirname(__file__), "client_secrets.json")
TOKEN_FILE = os.path.join(os.path.dirname(__file__), "blogger_token.json")

def authenticate():
    if not os.path.exists(CREDENTIALS_FILE):
        print(f"[ERROR] client_secrets.json not found: {CREDENTIALS_FILE}")
        return False
    
    flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
    print("\n" + "="*70)
    print("  [READY] Listening on http://localhost:8080 for Google authorization callback...")
    print("="*70 + "\n")
    creds = flow.run_local_server(port=8080, open_browser=False)
    with open(TOKEN_FILE, "w") as token:
        token.write(creds.to_json())
    print("\n🎉 [SUCCESS] Authentication completed! blogger_token.json saved successfully!\n")
    return True

if __name__ == "__main__":
    authenticate()
