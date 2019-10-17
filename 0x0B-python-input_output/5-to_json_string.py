#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
"""


def to_json_string(my_obj):
    """Return JSON representation of object

    python3 -c 'print(__import__("my_module").my_function.__doc__)'
    python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
    """
    import json
    return json.dumps(my_obj)
