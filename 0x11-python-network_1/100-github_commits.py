#!/usr/bin/python3
"""
Print the top 10 commit history from a
users repository.
"""
from requests import get
from sys import argv


if (__name__ == "__main__"):
    repo = argv[1]
    owner = argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits?per_page=10"
    count = 0

    with get(url) as response:
        data = eval(response.text.replace("false", "False")
                    .replace("true", "True")
                    .replace("null", "\"\""))
        for record in data:
            commit = record.get("commit")
            print(f"{record.get('sha')}: "
                  f"{commit.get('author').get('name')}")
            count += 1
