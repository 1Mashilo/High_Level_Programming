#!/usr/bin/python3

def sum_unique_integers(input_list=[]):
    """
    Calculate the sum of unique integers in the input list.

    This function takes a list of integers and returns the sum of unique integers.
    Each unique integer is included only once in the summation, even if it appears
    multiple times in the input list.

    Args:
        input_list (list): A list of integers to find the sum of unique elements.

    Returns:
        int: The sum of unique integers in the input list.

    """
    unique_integers = set()

    for integer in input_list:
        if integer not in unique_integers:
            unique_integers.add(integer)

    sum_of_unique = 0

    for unique_integer in unique_integers:
        sum_of_unique += unique_integer

    return sum_of_unique
