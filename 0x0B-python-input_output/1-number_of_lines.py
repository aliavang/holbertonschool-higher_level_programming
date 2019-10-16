#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
"""


def number_of_lines(filename=""):
    """Return number of lines of a text file

    python3 -c 'print(__import__("my_module").my_function.__doc__)'
    python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
    """
    line_count = 0
    with open(filename, 'r') as f:
        for l in f:
            line_count += 1
    return line_count
