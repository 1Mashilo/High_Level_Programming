#!/usr/bin/python3
def print_uppercase_line(input_str):
    """
    Print the input string in uppercase followed by a new line.
    
    Without importing modules or using `str.upper()` or `str.isupper()`.

    Args:
        input_str (str): The string to be printed in uppercase.

    Returns:
        None
    """
    for c in input_str:
        if ord(c) >= 97 and ord(c) <= 122:
            c = chr(ord(c) - 32)
        print("{}".format(c), end="")
    print("")
