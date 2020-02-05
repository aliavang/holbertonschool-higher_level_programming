#!/usr/bin/python3
"""
Send request to URL and display error code
"""
import urllib.request
from urllib.error import HTTPError
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read()
            print("{}".format(html.decode('utf-8')))
    except urllib.error.HTTPError as e:
            print("Error code: {}".format(e.code))
