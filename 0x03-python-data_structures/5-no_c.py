#!/usr/bin/python3

def no_c(my_string):
    """
    Remove all occurrences of the characters 'c' and 'C' from a string.

    Args:
        my_string (str): The input string from which to remove 'c' and 'C'.

    Returns:
        str: A new string with all 'c' and 'C' characters removed.

    Example:
        >>> no_c("Chocolate")
        'hocolate'

        >>> no_c("Coffee")
        'offee'
    """
    copy = [x for x in my_string if x != 'c' and x != 'C']
    return "".join(copy)
