#!/usr/bin/python3
"""
takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import sys
import requests
import requests.exceptions


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    q = ""
    if len(sys.argv) > 1:
        q = sys.argv[1]
    data = {"q": q}
    resp = requests.post(url, data)
    try:
        js = resp.json()
        if js == {}:
            print("No result")
        else:
            print(f"[{js['id']}] {js['name']}")
    except requests.exceptions.JSONDecodeError:
        print("Not a valid JSON")
