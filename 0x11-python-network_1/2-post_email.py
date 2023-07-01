#!/usr/bin/python3
"""Script that sends request to URL and displays response (decoded in utf-8)."""
from urllib import request, parse
import sys


if __name__ == "__main__":
    value = ("email": sys.argv[2])
    data = parse.urlencode(values)
    data = data.encode("ascii")
    req = request.Request(sys.argv[1], data)
    with request.urlopen(req) as response:
        body = response.read()
        print(body.decode("utf-8"))
