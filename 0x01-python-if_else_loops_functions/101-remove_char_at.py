#!/usr/bin/python3
def remove_char_at(str, n):
    """
    Create a copy of the string without the character at position n.

    Args:
        str (str): The input string.
        n (int): The position of the character to remove.

    Returns:
        str: A new string with the character at position n removed.
        If n is negative, the original string is returned.
    """
    if n < 0:

        return str
    else:

        return str[:n] + str[n + 1:]