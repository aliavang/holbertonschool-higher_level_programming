#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
"""
from sys import argv
save = __import__('7-save_to_json_file').save_to_json_file
load = __import__('8-load_from_json_file').load_from_json_file

list = []
l = len(argv)
try:
    load("add_item.json")
except:
    pass
for arg in range(1, l):
    list.append(argv[arg])
save(list, "add_item.json")
