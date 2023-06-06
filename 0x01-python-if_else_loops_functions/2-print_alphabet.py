#!/usr/bin/python3
#2-print_alphabet.py

"""prints the ASCII alphabet, in lowercase, not followed by a new line."""
for letters in range(97, 123):
    print("{}".format(chr(letters)), end="")
