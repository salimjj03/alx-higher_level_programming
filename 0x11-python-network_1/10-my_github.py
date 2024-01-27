#!/usr/bin/python3
""" THis model  takes in a URL, sends a request
to the URL and displays the:wq
value of the X-Request-Id variable f
ound in the header of the response. """

import requests
from sys import argv

if __name__ == "__main__":
    url = 'https://api.github.com/users/{}'.format(argv[1])
    req = requests.get(url, auth=(argv[1], argv[2])).json()

    print(req.get('id'))
