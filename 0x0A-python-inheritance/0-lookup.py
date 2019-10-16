#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
"""


def lookup(obj):
    """Return list of available attributes and methods

    python3 -c 'print(__import__("my_module").my_function.__doc__)'
    python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
    """
    return dir(obj)
