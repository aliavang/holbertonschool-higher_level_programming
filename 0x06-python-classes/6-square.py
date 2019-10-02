#!/usr/bin/python3
class Square:
    """Create class Square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize fields of class Square"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Retrieve size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set value of size if valid value"""
        if not type(value) == int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Retrieve position of square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set position of square"""
        if not type(value) == tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not len(value) == 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not type(value[0]) == int and not type(value[1]) == int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 and value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value[0:2]

    def area(self):
        """Find area of Square of x size"""
        return self.__size * self.__size

    def my_print(self):
        """Print square of x size"""
        if self.__size == 0:
            print("")
            return
        for y in range(self.__position[1]):
            print("")
        for r in range(self.__size):
            for z in range(self.position[0]):
                print(" ", end="")
            for c in range(self.__size):
                print("#", end="")
            print("")
