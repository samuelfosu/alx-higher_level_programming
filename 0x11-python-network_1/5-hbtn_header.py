#!/usr/bin/python3
"""Script sends URL request and displays X-Request-Id"""
import requests
import sys


if __name__ == "__main__":
    try:
        r = requests.get(sys.argv[1])
        print(r.headers['X-Request-Id'])
    except:
        pass
