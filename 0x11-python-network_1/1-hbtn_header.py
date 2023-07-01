#!/usr/bin/python3
"""Script sends URL, request URL and display Request-Id variable found"""
import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        html = response.info()
        print(html.get("X-Request-Id"))
