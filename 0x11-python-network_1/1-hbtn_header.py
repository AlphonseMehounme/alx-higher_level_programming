#!/usr/bin/python3
"""
  Send request
"""
import urllib.request


req = urllib.request.Request("https://alx-intranet.hbtn.io/status")
with urllib.request.urlopen(req) as response:
    response_bytes = response.read()
    print("Body response:")
    print(f"\t- type: {type(response_bytes)}")
    print(f"\t- content: {response_bytes}")
    print(f"\t- utf8 content: {response_bytes.decode('utf-8')}")
