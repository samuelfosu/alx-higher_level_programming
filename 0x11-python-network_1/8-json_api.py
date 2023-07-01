#!/usr/bin/python3
"""Script sends a POST request to http://0.0.0.0:5000/search_user"""


if __name__ == "__main__":
    import requests
    import sys

    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    res = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        res_dict = res.json()
        if res_dict == {}:
            print('No result')
        else:
            print("[{}] {}".format(res_dict.get("id"), res_dict.get("name")))
    except ValueError:
        print("Not a valid JSON")
