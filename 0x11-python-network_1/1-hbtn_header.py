#!/usr/bin/python3
"""
  This module Send request to provided url from commmand Line and print the
  value of X-Request-ID header to output
"""
import urllib.request
import sys


if '__name__': '__main__':
    """
      Main section
    """
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        headers = response.getheaders()
        for header in headers:
            if header[0] == 'X-Request-Id':
                print(header[1])
