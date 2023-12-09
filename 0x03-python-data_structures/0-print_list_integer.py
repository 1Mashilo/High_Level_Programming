#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """
    Print each integer in the given list.

    Args:
        my_list (list): A list of integers.

    Returns:
        None
    """
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))
