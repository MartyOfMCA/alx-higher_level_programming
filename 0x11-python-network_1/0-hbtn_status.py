#!/usr/bin/python3
"""
Fetches data from a URL.
"""
from urllib.request import Request, urlopen


if (__name__ == "__main__"):
    url = "https://alx-intranet.hbtn.io/status"

    request = Request(url)
    with urlopen(request) as response:
        contents = response.read()
        print("Body response:")
        print(f"\t- type: {type(contents)}")
        print(f"\t- content: {contents}")
        print(f"\t- utf8 content: {contents.decode()}")
