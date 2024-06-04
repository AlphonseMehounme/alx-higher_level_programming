#!/usr/bin/python3
"""
  This module send requests to url and print the result
"""
import requests


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    resp = requests.get(url).text
    print(f"Body response:\n\t- type: {type(resp)}\n\t- content: {resp}")
