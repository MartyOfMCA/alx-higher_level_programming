#!/usr/bin/python3
"""
Send a POST request with an email added
to request body.
"""
from urllib.request import Request, urlopen
from urllib import parse
from sys import argv


if (__name__ == "__main__"):
    url = argv[1]
    email = argv[2]
    data = {"email": email}

    encoded_data = parse.urlencode(data).encode("ascii")
    request = Request(url, encoded_data)

    with urlopen(request) as response:
        print(response.read().decode())
