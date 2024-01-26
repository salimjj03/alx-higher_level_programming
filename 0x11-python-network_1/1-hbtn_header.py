#!/usr/bin/python3
""" THis model  takes in a URL, sends a request
to the URL and displays the:wq
value of the X-Request-Id variable f
ound in the header of the response. """

from sys import argv
from urllib.request import urlopen


with urlopen(argv[1]) as response:
    h = response.headers.get("X-Request-Id")
    print(h)
