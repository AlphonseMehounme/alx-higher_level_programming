#!/usr/bin/python3
"""
This module takes in a URL, sends a request to the URL and displays the body
of the response.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    resp = requests.get(url)
    if resp.status_code >= 400:
        print("Error code:", resp.status_code)
    else:
        print(resp.text)
