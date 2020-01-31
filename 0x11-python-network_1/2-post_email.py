#!/usr/bin/python3
"""
Send URL and email address as POST request to URL and displays response
"""
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    with urllib.request.urlopen(url) as response:
        html = response.info()
        print("Your email is: {}".format(html.get("email")))
