#!/usr/bin/python3
""" THis model  takes in a URL, sends a request
to the URL and displays the:wq
value of the X-Request-Id variable f
ound in the header of the response. """

from sys import argv
from urllib.request import urlopen
from urllib.parse import urlencode
import urllib.request
from urllib.error import HTTPError


if __name__ == "__main__":
    r = urllib.request.Request(argv[1])
    try:
        with urlopen(r) as response:
            print(response.read().decode("utf-8"))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
