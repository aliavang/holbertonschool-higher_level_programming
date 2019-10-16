#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
"""

def inherits_from(obj, a_class):
    """Return True if object is an instance that inherited from specified\
    class, otherwise False

    python3 -c 'print(__import__("my_module").my_function.__doc__)'
    python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
    """
    if issubclass(type(obj), a_class) and not type(obj) == a_class:
        return True
    else:
        return False
