0x07. Python - Test-driven development

Python Unit Tests TDD

Tasks

0. Integers addition

mandatory

Write a function that adds 2 integers.

Prototype: def add_integer(a, b=98):a and b must be integers or floats, otherwise raise a TypeError exception with the message a must be an integer or b must be an integera and b must be first casted to integers if they are floatReturns an integer: the addition of a and bYou are not allowed to import any module

1. Divide a matrix

mandatory

Write a function that divides all elements of a matrix.

Prototype: def matrix_divided(matrix, div):matrix must be a list of lists of integers or floats, otherwise raise a TypeError exception with the message matrix must be a matrix (list of lists) of integers/floatsEach row of the matrix must be of the same size, otherwise raise a TypeError exception with the message Each row of the matrix must have the same sizediv must be a number (integer or float), otherwise raise a TypeError exception with the message div must be a numberdiv can’t be equal to 0, otherwise raise a ZeroDivisionError exception with the message division by zeroAll elements of the matrix should be divided by div, rounded to 2 decimal placesReturns a new matrixYou are not allowed to import any module

2. Say my name

mandatory

Write a function that prints My name is <first name> <last name>

Prototype: def say_my_name(first_name, last_name=""):first_name and last_name must be strings otherwise, raise a TypeError exception with the message first_name must be a string or last_name must be a stringYou are not allowed to import any module

3. Print square

mandatory

Write a function that prints a square with the character #.

Prototype: def print_square(size):size is the size length of the squaresize must be an integer, otherwise raise a TypeError exception with the message size must be an integerif size is less than 0, raise a ValueError exception with the message size must be >= 0if size is a float and is less than 0, raise a TypeError exception with the message size must be an integerYou are not allowed to import any module

4. Text indentation

mandatory

Write a function that prints a text with 2 new lines after each of these characters: ., ? and :

Prototype: def text_indentation(text):text must be a string, otherwise raise a TypeError exception with the message text must be a stringThere should be no space at the beginning or at the end of each printed lineYou are not allowed to import any module

5. Max integer - Unittest

mandatory

Since the beginning you have been creating “Interactive tests”. For this exercise, you will add Unittests.

In this task, you will write unittests for the function def max_integer(list=[]):.

Your test file should be inside a folder testsYou have to use the unittest moduleYour test file should be python files (extension: .py)Your test file should be executed by using this command: python3 -m unittest tests.6-max_integer_testAll tests you make must be passable by the function belowWe strongly encourage you to work together on test cases, so that you don’t miss any edge case

6. Matrix multiplication

#advanced

Write a function that multiplies 2 matrices:

Read: Matrix multiplication - only Matrix product (two matrices)

Prototype: def matrix_mul(m_a, m_b):

m_a and m_b must be validated with these requirements in this order

m_a and m_b must be an list of lists of integers or floats:

if m_a or m_b is not a list: raise a TypeError exception with the message m_a must be a list or m_b must be a listif m_a or m_b is not a list of lists: raise a TypeError exception with the message m_a must be a list of lists or m_b must be a list of listsif m_a or m_b is empty (it means: = [] or = [[]]): raise a ValueError exception with the message m_a can't be empty or m_b can't be emptyif one element of those list of lists is not an integer or a float: raise a TypeError exception with the message m_a should contain only integers or floats or m_b should contain only integers or floatsif m_a or m_b is not a rectangle (all ‘rows’ should be of the same size): raise a TypeError exception with the message each row of m_a must be of the same size or each row of m_b must be of the same size

If m_a and m_b can’t be multiplied: raise a ValueError exception with the message m_a and m_b can't be multiplied

You are not allowed to import any module

7. Lazy matrix multiplication

#advanced

Write a function that multiplies 2 matrices by using the module NumPy

To install it: pip3 install numpy==1.15.0

Prototype: def lazy_matrix_mul(m_a, m_b):Test cases should be the same as 100-matrix_mul but with new exception type/message

8. CPython #3: Python Strings

#advanced


Create a function that prints Python strings.

Prototype: void print_python_string(PyObject *p);Format: see exampleIf p is not a valid string, print an error message (see example)Read: Unicode HOWTO

