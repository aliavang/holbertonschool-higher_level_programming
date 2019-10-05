#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
"""


def matrix_divided(matrix, div):
    """Divide matrix by passed divider

    python3 -c 'print(__import__("my_module").my_function.__doc__)'
    """

    if not isinstance(matrix, list) and isinstance(matrix, int):
        raise TypeError("matrix must be a matrix (list of lists) of integers/
        floats")
    if not isinstance(matrix, list) and isinstance(matrix, float):
        raise TypeError("matrix must be a matrix (list of lists) of integers/
        floats")
    if not len
