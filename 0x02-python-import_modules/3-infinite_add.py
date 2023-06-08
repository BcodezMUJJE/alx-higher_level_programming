#!/usr/bin/python3
import sys

def calculate_sum(argv):
    total_sum = 0
    for arg in argv:
        total_sum += int(arg)
    return total_sum

result = calculate_sum(sys.argv[1:])
print(result)
