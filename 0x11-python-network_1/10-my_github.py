#!/usr/bin/python3
"""
Print the Github id for a particular user.
This script accepts the Github username
and password (Personal Access Token).
"""
from requests import get
from sys import argv


if (__name__ == "__main__"):
    username = argv[1]
    token = argv[2]
    url = f"https://api.github.com/users/{username}"
    header = {"Authorization": f"Token {token}"}

    with get(url, headers=header) as response:
        json = response.text.replace("true", "True")\
                .replace("false", "False")\
                .replace("null", "\"\"")
        print(eval(json).get("id"))
