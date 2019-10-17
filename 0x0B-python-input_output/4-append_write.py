#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
"""


def append_write(filename="", text=""):
    """Append string to end of text file

    python3 -c 'print(__import__("my_module").my_function.__doc__)'
    python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
    """
    with open(filename, 'a') as f:
        c_count = f.write(text)
        return c_count
