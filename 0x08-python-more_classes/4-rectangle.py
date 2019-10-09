#!/usr/bin/python3
class Rectangle:
    """Rectangle class with width and height"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Retrieve height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Retrieve area of rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Return perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return string of rectangle"""
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string
        else:
            for h in range(self.__height):
                for w in range(self.__width):
                    string += "#"
                string += "\n"
            return string[: -1]

    def __repr__(self):
        """Return string of rectangle in repr format"""
        return "Rectangle({}, {})".format(self.__width, self.__height)
