#!/usr/bin/env python3
"""
HelpTrickBD 1-Click Blogger OAuth Authenticator
Generates the authorization link, listens on localhost:8080,
and saves `blogger_token.json` for autonomous post updating.
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

def generate_auth_url():
    if not os.path.exists(CREDENTIALS_FILE):
        print(f"[ERROR] client_secrets.json not found in: {CREDENTIALS_FILE}")
        return None
    flow = InstalledAppFlow.from_client_secrets_file(
        CREDENTIALS_FILE,
        SCOPES,
        redirect_uri="http://localhost:8080/"
    )
    auth_url, _ = flow.authorization_url(
        access_type="offline",
        include_granted_scopes="true",
        prompt="consent"
    )
    print("\n" + "="*70)
    print("  🔗 GOOGLE AUTHENTICATION LINK:")
    print("="*70)
    print(auth_url)
    print("="*70 + "\n")
    return auth_url

if __name__ == "__main__":
    generate_auth_url()
