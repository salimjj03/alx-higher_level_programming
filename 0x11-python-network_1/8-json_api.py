#!/usr/bin/python3
""" THis model  takes in a URL, sends a request
to the URL and displays the:wq
value of the X-Request-Id variable f
ound in the header of the response. """

import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) > 1:
        if argv[1].isdigit():
            print("Not a valid JSON")
            exit()
        d = {"q": argv[1]}
    else:
        d = {"q": ""}
    with requests.post("http://0.0.0.0:5000/search_user", d) as r:
        js = r.json()
        if js:
            print("[{}] {}".format(js.get("id"), js.get("name")))
        else:
            print("No result")
