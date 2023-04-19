README.md

Python Test Driven Development
This repository contains Python functions developed using Test Driven Development methodology. Each function is designed to accomplish a specific task and is tested with multiple test cases to ensure its correctness.

Tasks
0. Integers addition
Function to add two integers.

File: 0-add_integer.py
Test file: tests/0-add_integer.txt

1. Divide a matrix
Function to divide all elements of a matrix by a given number.

File: 2-matrix_divided.py
Test file: tests/2-matrix_divided.txt
2. Say my name
Function to print the full name based on given first and last names.

File: 3-say_my_name.py
Test file: tests/3-say_my_name.txt
3. Print square
Function to print a square with the character #.

File: 4-print_square.py
Test file: tests/4-print_square.txt
4. Text indentation
Function to print a text with 2 new lines after each of these characters: ., ? and :.

File: 5-text_indentation.py
Test file: tests/5-text_indentation.txt
5. Max integer - Unittest
Unittests for a function that finds the max integer in a list.

File: 6-max_integer.py
Test file: tests/6-max_integer_test.py
6. Matrix multiplication
Function to multiply 2 matrices.

File: 100-matrix_mul.py
Test file: tests/100-matrix_mul.txt
7. Lazy matrix multiplication
Function to multiply 2 matrices using the NumPy module.

File: 101-lazy_matrix_mul.py
Test file: tests/101-lazy_matrix_mul.txt
Usage
To run the test cases for each function, execute the following command:

bash
Copy code
python3 -m doctest -v ./tests/<test_file_name>
Replace <test_file_name> with the name of the test file you want to run.

For example, to run the test cases for 0-add_integer.py, run:

bash
Copy code
python3 -m doctest -v ./tests/0-add_integer.txt
Repository
GitHub repository: alu-higher_level_programming
Directory: python-test_driven_development
Author
Your Name (aristote-code)
