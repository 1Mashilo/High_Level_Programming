#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    """
    Print an integer with "{:d}.format()" and handle exceptions.

    If a TypeError or ValueError occurs, an error message is printed to standard error.

    Args:
        value (int): The integer to print.

    Returns:
        bool: True if the integer is printed successfully, False if there's an exception.
    """
    try:  
        print(f"{value:d}")
        return True 

    except (TypeError, ValueError):

        print(f"Exception: {sys.exc_info()[1]}", file=sys.stderr)
        return False