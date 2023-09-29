#!/usr/bin/python3
"""
Send a POST request with a letter added
as a parameter.
"""
from requests import post
from sys import argv


if (__name__ == "__main__"):
    url = "http://0.0.0.0:5000/search_user"
    letter = argv[1] if (len(argv) == 2) else ""
    data = {"q": letter}

    with post(url, data) as response:
        content_type = response.headers.get("Content-type")

        if (content_type == "application/json"):
            json = eval(response.text)

            if (json != {}):
                print(f"[{json.get('id')}] {json.get('name')}")
            else:
                print("No result")
        else:
            print("Not a valid JSON")
