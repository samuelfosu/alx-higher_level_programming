#!/usr/bin/python3
""Script that sends request to URL and displays response (decoded in utf-8)."""


if __name__ == "__main__":
    import urllib.request
    import urllib.error
    import sys

    req = urllib.request.Request(sys.argv[1])

    try:
        with urllib.request.urlopen(req) as res:
            print(res.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
