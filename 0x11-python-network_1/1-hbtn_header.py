#!/usr/bin/python3
"""
  Send request to provided url
  Get URL from commmand Line 
  And print the value of X-Request-ID
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
