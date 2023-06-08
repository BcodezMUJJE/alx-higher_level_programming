#!/usr/bin/python3
# assign values to variables
a = 10
b = 5
# Import the calculation function from calculator_1
from calculator_1 import add, sub, mul, div
print("{} + {} = {}".format(a, b, add(a, b)))
print("{} - {} = {}".format(a, b, sub(a, b)))
print("{} / {} = {}".format(a, b, div(a, b)))
print("{} * {} = {}".format(a, b, mul(a, b)))
