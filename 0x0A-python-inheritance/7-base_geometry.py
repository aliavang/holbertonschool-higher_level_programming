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
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate value

        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
        """
        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
