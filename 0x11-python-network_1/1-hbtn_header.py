#!/usr/bin/python3
"""
  Send request to provided url
"""
import urllib.request
import sys


url = sys.argv[1]
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    headers = response.getheaders()
    for header in headers:
        if header[0] == 'X-Request-Id':
            print(header[1])
    #print("Body response:")
    #print(f"\t- type: {type(response_bytes)}")
    #print(f"\t- content: {response_bytes}")
    #print(f"\t- utf8 content: {response_bytes.decode('utf-8')}")
