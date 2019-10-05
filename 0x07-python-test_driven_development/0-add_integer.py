#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
"""


def add_integer(a, b=98):
    """Return sum of a and b
    python3 -c 'print(__import__("my_module").my_function.__doc__)'
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a, b = int(a), int(b)
    return a + b
