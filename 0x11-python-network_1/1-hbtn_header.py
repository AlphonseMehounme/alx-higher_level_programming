#!/usr/bin/python3
"""
This module Send request to provided url from commmand Line and print the
value of X-Request-ID header to standard output
Usage : ./1-hbtn_header.py https://alx-intranet.hbtn.io
"""
import urllib.request
import sys


if '__name__' == '__main__':
    """
      Main section that uses the provided URL to send request and print value
      of X-Request-ID header to ouptut
    """
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        headers = response.getheaders()
        for header in headers:
            if header[0] == 'X-Request-Id':
                print(header[1])
