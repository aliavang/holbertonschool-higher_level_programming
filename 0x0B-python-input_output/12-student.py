#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
"""


class Student:
    """python3 -c 'print(__import__("my_module").MyClass.__doc__)'"""
    def __init__(self, first_name, last_name, age):
        """Initialize

        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve dictionary representation of Student

        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        python3 -c 'print(__import__("my_module").MyClass.my_function.\
        __doc__)'
        """
        d = {}
        if attrs is None:
            return self.__dict__
        for s in attrs:
            for k, i in self.__dict__.items():
                if k == s:
                    d[k] = i
        return d
