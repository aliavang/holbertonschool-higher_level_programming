#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
"""


def is_kind_of_class(obj, a_class):
    """Return True if object is an instance or if the object is an instance\
    of a class that inherited from the specified class, otherwise False

    python3 -c 'print(__import__("my_module").my_function.__doc__)'
    python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
    """
    return isinstance(obj, a_class)
