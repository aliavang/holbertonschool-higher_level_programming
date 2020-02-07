#!/usr/bin/python3
"""
Send a request to the URL and display error code
"""
import requests
import sys


if __name__ == '__main__':
    r = requests.get(sys.argv[1])
    try:
        r.raise_for_status()
        print(r.text)
    except Exception as e:
        print("Error code: {}".format(r.status_code))
