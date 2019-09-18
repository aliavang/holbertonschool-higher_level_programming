#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a, tuple_b = tuple_a[:2], tuple_b[:2]
    len_a, len_b = len(tuple_a), len(tuple_b)
    if len_a == 1:
        tuple_a += (0, )
    elif len_a == 0:
        tuple_a += (0, 0)
    elif len_b == 1:
        tuple_b += (0, )
    elif len_b == 0:
        tuple_b += (0, 0)
    tuple_c = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return tuple_c
