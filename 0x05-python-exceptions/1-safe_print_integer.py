#!/usr/bin/python3

def safe_print_integer(value):
    """
    Print an integer with "{:d}".format() and handle exceptions.

    Args:
        value (int): The integer to print.

    Returns:
        bool: True if the integer is printed successfully, False if there's an exception.
    """
    try:
        print(f"{value:d}")

        return True 

    except (TypeError, ValueError):
       
        return False 

