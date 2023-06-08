#!/usr/bin/python3
import sys

def print_arguments(argv):
	num_arguments = len(argv)
	if num_arguments == 0:
		print("0 arguments.")
		print(".")
	elif num_arguments == 1:
		print("1 argument:")
		print("1:", argv[0])
	else:
		print(num_arguments, "arguments:")
		for i, arg in enumerate(argv, start=1):
			print(i, ":", arg)

print_arguments(sys.argv[1:])
