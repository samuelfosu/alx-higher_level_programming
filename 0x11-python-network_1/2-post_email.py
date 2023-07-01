#!/usr/bin/python3
"""Script that sends request to URL and displays response (decoded in utf-8)."""


if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    data = urllib.parse.urlencode({'email': sys.argv[2]}).encode('utf-8')
    req = urllib.request.Request(sys.argv[1], data)

    with urllib.request.urlopen(req) as res:
        print(res.read().decode('utf-8'))
