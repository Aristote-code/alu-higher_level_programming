#!/usr/bin/python3

''' Integer addition exception of float'''


def add_integer(a, b=98):
    ''' A function that adds Integers with an exception of float'''
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
