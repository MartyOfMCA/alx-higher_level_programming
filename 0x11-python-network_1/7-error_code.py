#!/usr/bin/python3
"""
Send a request and display response body
handling any exceptions that might happen.
"""
from requests import get
from sys import argv


if (__name__ == "__main__"):
    url = argv[1]

    with get(url) as response:
        if (response.status_code >= 400):
            print(f"Error code: {response.status_code}")
        else:
            print(response.text)
