#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
"""

class BaseGeometry:
    """
    python3 -c 'print(__import__("my_module").MyClass.__doc__)'
    """
    def area(self):
        """Return area of the geometry

        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
        """
        raise Execption("area() is not implemented")
