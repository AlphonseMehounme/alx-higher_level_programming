#!/usr/bin/python3
"""
  Send request to provided URL
"""
import sys
import urllib.request


url = sys.argv[1]
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    headers = response.getheaders()
    for header in headers:
        if header[0] == 'X-Request-Id':
            print(header[1])
