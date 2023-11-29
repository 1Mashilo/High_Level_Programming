#!/usr/bin/python3
"""
Prints the ASCII alphabet in lowercase on the same line.

This code snippet uses a for loop to iterate through the range of
Unicode code points corresponding to lowercase letters ('a' to 'z').
It prints each letter sequentially on the same line without line breaks.

The 'chr()' function is used to convert the code points into characters.

"""
for i in range(ord('a'), ord('z') + 1):
    print('{:c}'.format(i), end='')