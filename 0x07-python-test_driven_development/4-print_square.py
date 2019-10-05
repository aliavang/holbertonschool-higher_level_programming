#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
"""

def print_square(size):
    """Print a square of specified size

    python3 -c 'print(__import__("my_method").my_function.__doc__)'
    """

    if not isinstance(size, int) or isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        for row in range(size):
            for col in range(size):
                print("#", end="")
            print("")
