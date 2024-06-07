#!/usr/bin/python3
"""
This module takes your GitHub credentials (username and password) and
uses the GitHub API to display your id
"""
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/users/" + sys.argv[1]
    headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": "Bearer " + sys.argv[2],
            "X-GitHub-Api-Version": "2022-11-28"
            }
    resp = requests.get(url, headers)
    print(resp.json()['id'])
