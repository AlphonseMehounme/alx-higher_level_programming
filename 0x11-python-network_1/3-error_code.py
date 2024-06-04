#!/usr/bin/python3
"""
This module that takes in a URL, sends a request to the URL and displays the
body of the response (decoded in utf-8)
"""
import urllib.request
import sys
import urllib.error


if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            response_bytes = response.read()
            print(response_bytes.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
