#!/usr/bin/python3
"""
This module takes in a URL and an email, sends a POST request to the passed
URL with the email as a parameter, and displays the body of the response
(decoded in utf-8)
"""
import sys
import urllib.parse
import urllib.request


data = {'email': sys.argv[2]}
url = sys.argv[1]
data = urllib.parse.urlencode(data).encode('ascii')
req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as response:
    response_bytes = response.read()
    print(response_bytes.decode('utf-8'))
