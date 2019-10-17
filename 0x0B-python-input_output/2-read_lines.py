#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
"""


def read_lines(filename="", nb_lines=0):
    """Read n lines of a file and print to stdout

    python3 -c 'print(__import__("my_module").my_function.__doc__)'
    python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
    """
    i = 0
    with open(filename, 'r') as f:
        if nb_lines <= 0:
            print(f.read())
        for l in f:
            if i < nb_lines:
                print(l, end="")
            else:
                break
            i += 1
