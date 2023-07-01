#!/usr/bin/python3
"""Script sends post request to passed URL with the email as a parameter"""


if __name__ == "__main__":
    import requests
    import sys

    res = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(res.text)
