#!/usr/bin/python3

"""
Script to demonstrate the print_reversed_list_integer function.

Usage:
    Run this script to import the print_reversed_list_integer function
    from the 3-print_reversed_list_integer module and call it with a predefined list.
"""

print_reversed_list_integer = __import__('3-print_reversed_list_integer').print_reversed_list_integer

my_list = [1, 2, 3]
print_reversed_list_integer(my_list)
