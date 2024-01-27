#!/usr/bin/python3
""" THis model  takes in a URL, sends a request
to the URL and displays the:wq
value of the X-Request-Id variable f
ound in the header of the response. """

import requests


if __name__ == "__main__":
    with requests.get("https://alx-intranet.hbtn.io/status") as r:
        print("Body response:$")
        print("\t- type: {}".format(type(r.text)))
        print("\t- content: {}".format(r.text))
