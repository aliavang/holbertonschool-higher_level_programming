#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
"""


def error_raise(num):
    """Raise error depending on number that is passed to function"""

    if num == 1:
        raise TypeError("matrix must be a matrix (list of lists) of\
        integers/floats")
    elif num == 2:
        raise TypeError("Each row of the matrix must have the same size")
    elif num == 3:
        raise TypeError("div must be a number")
    elif num == 4:
        raise ZeroDivisionError("division by zero")

def matrix_divided(matrix, div):
    """Divide matrix by passed divider

    python3 -c 'print(__import__("my_module").my_function.__doc__)'
    """

    if not isinstance(div, (float, int)):
        error_raise(3)
    elif div <= 0:
        error_raise(4)
    if not isinstance(matrix, list):
        error_raise(1)
    for row in matrix:
        """
        if not isinstance(matrix[row], int)\
           or not isinstance(matrix[row], float):
            error_raise(1)
        """
        for ele in row:
            print("{:d}".format(matrix[row][ele]))
