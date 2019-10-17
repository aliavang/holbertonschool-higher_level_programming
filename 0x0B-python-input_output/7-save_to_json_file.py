#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
"""


def save_to_json_file(my_obj, filename):
    """Write object to a text file using JSON representation

    python3 -c 'print(__import__("my_module").my_function.__doc__)'
    python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
    """
    import json
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
