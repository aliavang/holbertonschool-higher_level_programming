#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
"""


def from_json_string(my_str):
    """Return object represented by JSON string

    python3 -c 'print(__import__("my_module").my_function.__doc__)'
    python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
    """
    import json
    return json.loads(my_str)
