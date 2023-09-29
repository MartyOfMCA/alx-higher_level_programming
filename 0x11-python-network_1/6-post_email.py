#!/usr/bin/python3
"""
Send a POST request with an email added
to the request body.
"""
from requests import post
from sys import argv


if (__name__ == "__main__"):
    url = argv[1]
    email = argv[2]

    data = {"email": email}

    with post(url, data) as response:
        print(response.text)
