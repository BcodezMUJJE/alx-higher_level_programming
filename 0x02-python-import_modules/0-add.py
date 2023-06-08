#!/usr/bin/python3
# Assign values to variables
a = 1
b = 2
# Import the add function from add_0.py
from add_0 import add
# Perform the addition and print answer
answer = add(a, b)
print("{} + {} = {}".format(a, b, answer))
