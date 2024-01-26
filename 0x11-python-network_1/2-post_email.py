#!/usr/bin/python3
""" THis model  takes in a URL, sends a request
to the URL and displays the:wq
value of the X-Request-Id variable f
ound in the header of the response. """

from sys import argv
from urllib.request import urlopen
from urllib.parse import urlencode
import urllib.request


if __name__ == "__main__":
    da = {"email": argv[2]}
    d = urlencode(da).encode("utf-8")
    r = urllib.request.Request(argv[1], data=d, method="POST")
    with urlopen(r) as response:
        h = response.read().decode("utf-8")
        print(h)
