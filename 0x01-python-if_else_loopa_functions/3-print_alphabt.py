#!/usr/bin/python3
"""
Prints the lowercase alphabet, excluding 'q' and 'e', in a single
line followed by a new line.

This program uses a for loop to iterate through
the ASCII values of lowercase letters (from 'a' to 'z').
Within the loop, it checks if the current
letter is not 'q' and not 'e' using an if condition.
If the condition is met, it prints the letter using the 'print' function
with the 'end' argument set to an empty string to avoid line breaks.

The result is the lowercase alphabet printed in a single line,
excluding 'q' and 'e', followed by a new line.

"""
for letter in range(97, 123):
    if chr(letter) != 'q' and chr(letter) != 'e':
        print("{}".format(chr(letter)), end="")
print()
