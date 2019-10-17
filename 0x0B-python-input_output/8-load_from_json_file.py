#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
"""


def load_from_json_file(filename):
    """Create object from a JSON file

    python3 -c 'print(__import__("my_module").my_function.__doc__)'
    python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
    """
    import json
    with open(filename, 'r') as f:
        return json.load(f)
