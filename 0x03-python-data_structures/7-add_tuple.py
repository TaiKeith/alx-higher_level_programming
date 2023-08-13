#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):

    new_tuple = ()
    for i in range(2):
        if i >= len(tuple_a):
            a = 0
        else:
            a = tuple_a[i]
        if i >= len(tuple_b):
            b = 0
        else:
            b = tuple_b[i]

        if (i == 0):
            new_tuple = (a + b)
        else:
            new_tuple = (new_tuple, a + b)
    return new_tuple
