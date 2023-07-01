#!/usr/bin/python3
"""Script that sends request to URL and displays response (decoded in utf-8)."""
from urllib import request, error
import sys


if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as reponse:
            body = response.read()
            print(body.decode("utf-8"))
    except error.HTTPError as err:
        print("Error code: {}" .format(err.code))
