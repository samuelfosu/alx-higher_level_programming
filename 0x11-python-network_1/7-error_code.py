#!/usr/bin/python3
"""Script sends URL and displays the body"""


if __name__ == "__main__":
    import requests
    import sys

    res = requests.get(sys.argv[1])

    if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))
    else:
        print(res.text)
