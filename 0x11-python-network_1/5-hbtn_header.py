#!/usr/bin/python3
"""
Send request and print the header variable
X-Request-Id for the request.
"""
from requests import get
from sys import argv


if (__name__ == "__main__"):
    url = argv[1]

    with get(url) as response:
        print(response.headers.get("X-Request-Id"))
