#!/usr/bin/python3
"""list 10 commits (from the most recent to oldest) of
the repository “rails” by the user “rails”
"""
import requests
import sys


if __name__ == "__main__":
    url = "https://api.github.com//repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    r = requests.get(url)
    commits = r.json()

    try:
        for i, obj in enumerate(commits):
            if i == 10:
                    break
            if type(obj) is dict:
                name = obj.get('commit').get('author').get('name')
                print("{}: {}".format(obj.get('sha'), name))
    except ValueError as invalid_json:
        pass