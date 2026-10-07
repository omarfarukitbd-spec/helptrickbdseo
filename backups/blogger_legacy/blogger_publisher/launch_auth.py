#!/usr/bin/env python3
"""
HelpTrickBD 100% Reliable OAuth Authenticator
Writes the exact login link to `tools/blogger_publisher/login_link.txt`,
listens for the Google redirect on an open port, and saves `blogger_token.json`.
"""

import os
import sys
import wsgiref.simple_server
from google_auth_oauthlib.flow import InstalledAppFlow, _WSGIRequestHandler, _RedirectWSGIApp

try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

SCOPES = ["https://www.googleapis.com/auth/blogger"]
CREDENTIALS_FILE = os.path.join(os.path.dirname(__file__), "client_secrets.json")
TOKEN_FILE = os.path.join(os.path.dirname(__file__), "blogger_token.json")
LINK_FILE = os.path.join(os.path.dirname(__file__), "login_link.txt")

def authenticate():
    flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
    wsgi_app = _RedirectWSGIApp("🎉 সফল হয়েছে! পোস্ট আপডেটের অনুমোদন সম্পন্ন হয়েছে। এই ট্যাবটি এখন বন্ধ করতে পারেন।")
    
    # Bind to free port
    local_server = wsgiref.simple_server.make_server(
        "localhost", 0, wsgi_app, handler_class=_WSGIRequestHandler
    )
    port = local_server.server_port
    flow.redirect_uri = f"http://localhost:{port}/"

    auth_url, _ = flow.authorization_url(access_type="offline", prompt="consent")

    with open(LINK_FILE, "w", encoding="utf-8") as lf:
        lf.write(auth_url)

    print("\n" + "="*70, flush=True)
    print("  🔗 GOOGLE AUTHENTICATION LINK:", flush=True)
    print("="*70, flush=True)
    print(auth_url, flush=True)
    print("="*70 + "\n", flush=True)
    print(f"[*] Server listening on port {port}. Waiting for authorization in browser...", flush=True)

    local_server.handle_request()

    # Extract code and fetch token
    authorization_response = wsgi_app.last_request_uri.replace("http:", "https:")
    flow.fetch_token(authorization_response=authorization_response)
    creds = flow.credentials

    with open(TOKEN_FILE, "w") as token:
        token.write(creds.to_json())

    print("\n🎉 [SUCCESS] blogger_token.json তৈরি হয়েছে! এখন সরাসরি লাইভ ব্লগারে আপডেট হবে।\n", flush=True)
    return creds

if __name__ == "__main__":
    authenticate()
