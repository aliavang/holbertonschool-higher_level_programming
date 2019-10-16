#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
"""


class MyList(list):
    """
    python3 -c 'print(__import__("my_module").MyClass.__doc__)'
    """
    pass

    def print_sorted(self):
        """Print sorted list

        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
        """
        sort_list = sorted(self)
        print(sort_list)
