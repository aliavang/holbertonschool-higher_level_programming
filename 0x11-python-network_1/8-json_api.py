#!/usr/bin/python3
"""
Takes in a letter and sends a POST request with the letter as a parameter
"""
import requests
import sys


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        val = ""
    else:
        val = sys.argv[1]
    q = {'q': val}
    url = 'http://0.0.0.0:5000/search_user'
    r = requests.post(url, data=q)
    if r.json():
        print("[{}] {}".format(r.json().get('id'), r.json().get('name')))
    elif not r.json():
        print("No result")
    else:
        print("Not a valid JSON")
