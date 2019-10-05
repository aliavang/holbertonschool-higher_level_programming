#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
"""


def text_indentation(text):
    """Print two new newline after a '.', '?', ':'

    python3 -c 'print(__import__("my_module").my_function.__doc__)'
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    else:
        c = 0
        while c < len(text):
            print("{:s}".format(text[c]), end="")
            if text[c] == '.' or text[c] == '?' or text[c] == ':':
                print("\n")
                c += 1
            c += 1
