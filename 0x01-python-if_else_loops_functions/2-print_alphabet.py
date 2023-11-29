#!/usr/bin/python3
"""
Prints lowercase letters from 'a' to 'z' in a single line.

This code snippet uses a for loop to iterate through the
range of Unicode code points
corresponding to lowercase letters ('a' to 'z'). It prints
each letter sequentially in a single line.

The 'chr()' function is used to convert the code points into
characters, and the 'end=""' argument
in the 'print()' function ensures that the letters are
printed on the same line without line breaks.

"""
for i in range(ord('a'), ord('z') + 1):
    print('{:c}'.format(i), end='')