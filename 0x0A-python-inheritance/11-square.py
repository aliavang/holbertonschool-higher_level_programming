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
        if not type(value) == int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """
    python3 -c 'print(__import__("my_module").MyClass.__doc__)'
    """

    def __init__(self, width, height):
        """Initialize

        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return area of Rectangle

        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
        """
        return self.__width * self.__height

    def __str__(self):
        h_count = 0
        w_count = 0
        for w in range(self.__width):
            w_count += 1
        for h in range(self.__height):
            h_count += 1
        return "[Rectange] {:d}/{:d}".format(w_count, h_count)

class Square(Rectangle):
    """
    python3 -c 'print(__import__("my_module").MyClass.__doc__)'
    """

    def __init__(self, size):
        """Initialize

        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
        """
        BaseGeometry.integer_validator(self, "size", size)
        self.__size = size

    def area(self):
        """Return area of Square

        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
        """
        return self.__size * self.__size

    def __str__(self):
        """Return string of square

        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
        """
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
