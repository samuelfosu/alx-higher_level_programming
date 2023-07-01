#!/usr/bin/python3
"""Script that send a post request to http://0.0.0.0:5000/search_user"""


if __name__ == "__main__":
    import requests
    import sys

    res = requests.get('https://api.github.com/user',
                       auth=(sys.argv[1], sys.argv[2]))
    print(res.json().get('id'))
