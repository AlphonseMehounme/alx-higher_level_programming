#!/usr/bin/python3
"""
This module takes 2 arguments and prints the last 10 commit from a repo
"""
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/" + sys.argv[2] + "/" + sys.argv[1] + "/commits"
    headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": "Bearer",
            "X-GitHub-Api-Version": "2022-11-28"
          }
    com = requests.get(url, headers)
    for i in range(-1, -10, -1):
        print(com.json()[i]['sha'])
    print(com.status_code)
