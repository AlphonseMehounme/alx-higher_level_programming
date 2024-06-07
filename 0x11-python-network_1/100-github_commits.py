#!/usr/bin/python3
"""
This module takes 2 arguments and prints the last 10 commit from a repo
"""
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/" + sys.argv[2] + "/" + sys.argv[1] +\
            "/commits"
    headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": "Bearer",
            "X-GitHub-Api-Version": "2022-11-28"
          }
    coms = requests.get(url, headers).json()
    i = 0
    for com in coms:
        if i < 10:
            print(f"{com['sha']}: {com['commit']['author']['name']}")
