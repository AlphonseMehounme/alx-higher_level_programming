#!/usr/bin/python3
"""
This module takes in a URL, sends a request to the URL and displays the value
of the variable X-Request-Id in the response header
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    headers = requests.get(url).headers
    if headers.get('X-Request-Id'):
        print(headers.get('X-Request-Id'))
