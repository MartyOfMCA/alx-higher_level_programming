#!/usr/bin/python3
"""
Print the response status for a request.
"""
from requests import get


if (__name__ == "__main__"):
    url = "https://alx-intranet.hbtn.io/status"

    with get(url) as response:
        print("Body response:")
        print(f"\t- type: {type(response.text)}")
        print(f"\t- content: {response.text}")
