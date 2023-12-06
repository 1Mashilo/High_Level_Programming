#!/usr/bin/python3

def count_keys_in_dictionary(input_dict):
    """
    Count and return the number of keys in a dictionary.

    Args:
        input_dict (dict): The dictionary for which to count keys.

    Returns:
        int: The number of keys in the dictionary.
    """
    key_count = 0
    keys_list = list(input_dict.keys())

    for key in keys_list:
        key_count += 1

    return key_count
