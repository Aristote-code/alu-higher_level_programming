#!/usr/bin/python3

''' Integer addition exception of float'''

def add_integer(a, b=98):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a and b must be integers or floats")

    return (int(a) + int(b))

