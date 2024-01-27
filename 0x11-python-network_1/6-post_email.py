#!/usr/bin/python3
""" THis model  takes in a URL, sends a request
to the URL and displays the:wq
value of the X-Request-Id variable f
ound in the header of the response. """

import requests
from sys import argv


if __name__ == "__main__":
    d = {"email": argv[2]}
    with requests.post(argv[1], data=d) as r:
        print(r.text)
