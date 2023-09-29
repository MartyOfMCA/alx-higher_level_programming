#!/usr/bin/python3
"""
Send a request to a URL and print the value
of the header variable X-Request-Id.
"""
from urllib.request import Request, urlopen
from sys import argv


if (__name__ == "__main__"):
    url = argv[1]

    request = Request(url)

    with urlopen(request) as response:
        print(response.getheader("X-Request-Id"))
