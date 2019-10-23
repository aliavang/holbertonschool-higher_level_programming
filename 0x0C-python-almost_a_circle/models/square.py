#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """python3 -c 'print(__import__("my_module").MyClass.__doc__)'"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize square

        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
        """
        super().__init__(size, size, x, y)

    def __str__(self):
        """Return information on square in string format

        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
        """
        return "[Square] ({}) {}/{} - {}".\
            format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Return value of size

        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
        """
        return self.width

    @size.setter
    def size(self, value):
        """Set value of size

        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update attributes of square

        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
        """
        if args is not None:
            for arg in range(len(args)):
                if arg == 0:
                    self.id = args[0]
                elif arg == 1:
                    self.size = args[1]
                elif arg == 2:
                    self.x = args[2]
                elif arg == 3:
                    self.y = args[3]
        if kwargs is not None:
            for k, it in kwargs.items():
                setattr(self, k, it)

    def to_dictionary(self):
        """Return dictionary representation of square

        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
        """
        return {'id': self.id, 'size': self.height, 'x': self.x, 'y': self.y}
