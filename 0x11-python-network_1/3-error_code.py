#!/usr/bin/python3
"""
Send a request and display response body.
"""
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from sys import argv


if (__name__ == "__main__"):
    url = argv[1]

    request = Request(url)

    try:
        with urlopen(request) as response:
            print(response.read().decode())
    except HTTPError as ex:
        print(f"Error code: {ex.code}")
