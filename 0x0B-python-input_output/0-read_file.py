#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
"""


def read_file(filename=""):
    """Read text file and print to stdout

    python3 -c 'print(__import__("my_module").my_function.__doc__)'
    python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
    """
    with open(filename, 'r') as f:
        read_file = f.read()
        print(read_file)
    f.closed
