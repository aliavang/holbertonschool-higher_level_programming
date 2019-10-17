#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
"""


def class_to_json(obj):
    """Return dictionary description for JSON serialized object

    python3 -c 'print(__import__("my_module").my_function.__doc__)'
    python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
    """
    return obj.__dict__
