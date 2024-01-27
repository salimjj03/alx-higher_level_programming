#!/usr/bin/python3
""" THis model  takes in a URL, sends a request
to the URL and displays the:wq
value of the X-Request-Id variable f
ound in the header of the response. """

import requests
from sys import argv


if __name__ == "__main__":
    with requests.get(argv[1]) as r:
        if r.status_code >= 400:
            print("Error code: {}".format(r.status_code))
        else:
            print(r.text)
