Read Me
This directory contains Python programs to demonstrate concepts related to object-oriented programming in Python.

Files
0-lookup.py - A Python function that returns the list of available attributes and methods of an object.
1-my_list.py - A Python class MyList that inherits from list. It has a public instance method print_sorted that prints the list, but sorted in ascending order.
2-is_same_class.py - A Python function that returns True if the object is exactly an instance of the specified class; otherwise False.
3-is_kind_of_class.py - A Python function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class; otherwise False.
4-inherits_from.py - A Python function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class; otherwise False.
5-base_geometry.py - An empty Python class BaseGeometry.
6-base_geometry.py - A Python class BaseGeometry that has a public instance method area that raises an Exception with the message area() is not implemented.
7-base_geometry.py - A Python class BaseGeometry that has a public instance method integer_validator that validates that the input value is an integer and greater than 0.
8-rectangle.py - A Python class Rectangle that inherits from BaseGeometry. It has a private instance attributes width and height. It has a public instance method area that returns the area of the rectangle. It implements the __str__ method that prints, and __repr__ that returns, the following rectangle description: [Rectangle] <width>/<height>
9-rectangle.py - A Python class Rectangle that inherits from BaseGeometry. It has a private instance attributes width and height. It has a public instance method area that returns the area of the rectangle. It implements the __str__ method that prints, and __repr__ that returns, the following rectangle description: [Rectangle] <width>/<height>
10-square.py - A Python class Square that inherits from Rectangle. It has a private instance attribute size. It has a public instance method area that returns the area of the square. It implements the __str__ method that prints, and __repr__ that returns, the following square description: [Square] <size>/<size>.
Usage
Each file can be run independently to test the functionality of the classes and functions.

For example:

css
Copy code
$ python3 0-main.py
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'my_attr1', 'my_meth']
['__abs__', '__add__', '__and__', '__bool__', '__ceil__',