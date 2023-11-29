#!/usr/bin/python3

"""
    Check for lowercase characters.

    Args:
        c (str): The character to check.

    Returns:
         bool: True if the character is lowercase, False otherwise.
"""
def islower(c):


    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False