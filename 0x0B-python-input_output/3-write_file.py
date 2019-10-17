#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
"""


def write_file(filename="", text=""):
    """Write a string to text and return number of characters written

    python3 -c 'print(__import__("my_module").my_function.__doc__)'
    python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
    """
    c_count = 0
    with open(filename, 'w') as f:
        c_count = f.write(text)
    return c_count
