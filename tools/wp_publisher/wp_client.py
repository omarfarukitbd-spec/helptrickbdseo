#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/wp_publisher/wp_client.py
--------------------------------
Robust, authenticated HTTP client for WordPress 6.7+ REST API.
Authenticates using WordPress Application Passwords via Basic Auth.
Supports automatic retries for transient HTTP errors and rate limits.
"""

import os
import sys
import base64
import json
import time
import requests
from typing import Optional, Dict, Any

class WordPressClient:
    def __init__(self, base_url: str, username: str, app_password: str, timeout: int = 30):
        self.base_url = base_url.rstrip("/")
        self.api_url = f"{self.base_url}/wp-json/wp/v2"
        self.timeout = timeout
        self.username = username
        self.app_password = app_password.strip()

        # Build Basic Auth header
        token = base64.b64encode(f"{self.username}:{self.app_password}".encode("utf-8")).decode("utf-8")
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Basic {token}",
            "User-Agent": "HelpTrickBD-AutoPublisher/1.0 (+https://www.helptrickbd.com)",
            "Accept": "application/json"
        })

    def request(self, method: str, endpoint: str, max_retries: int = 3, **kwargs) -> requests.Response:
        """
        Executes an HTTP request to the WordPress REST API endpoint with retry logic.
        endpoint can be relative (e.g. 'posts') or a full URL.
        """
        if endpoint.startswith("http://") or endpoint.startswith("https://"):
            url = endpoint
        elif endpoint.startswith("/wp-json/"):
            url = f"{self.base_url}{endpoint}"
        elif endpoint.startswith("/"):
            url = f"{self.api_url}{endpoint}"
        else:
            url = f"{self.api_url}/{endpoint}"

        kwargs.setdefault("timeout", self.timeout)

        for attempt in range(1, max_retries + 1):
            try:
                response = self.session.request(method, url, **kwargs)
                
                # Check for rate limiting
                if response.status_code == 429 and attempt < max_retries:
                    wait_time = int(response.headers.get("Retry-After", 3))
                    time.sleep(wait_time)
                    continue

                # Check for transient server errors
                if response.status_code in (502, 503, 504) and attempt < max_retries:
                    time.sleep(2 * attempt)
                    continue

                return response

            except (requests.ConnectionError, requests.Timeout) as e:
                if attempt == max_retries:
                    raise
                time.sleep(2 * attempt)

        raise requests.RequestException(f"Failed to execute request to {url} after {max_retries} attempts.")

    def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None, **kwargs) -> requests.Response:
        return self.request("GET", endpoint, params=params, **kwargs)

    def post(self, endpoint: str, json: Optional[Dict[str, Any]] = None, **kwargs) -> requests.Response:
        return self.request("POST", endpoint, json=json, **kwargs)

    def delete(self, endpoint: str, params: Optional[Dict[str, Any]] = None, **kwargs) -> requests.Response:
        return self.request("DELETE", endpoint, params=params, **kwargs)
