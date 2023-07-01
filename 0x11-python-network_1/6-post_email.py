#!/usr/bin/python3
"""Script sends post request to passed URL with the email as a parameter"""
import requests
import sys


if __name__ == "__main__":
    try:
        r = requests.get(sys.argv[1])
        print(r.headers["X-Request-Id"])
    except:
        pass
