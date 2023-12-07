#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    """
    Delete key-value pairs from a dictionary where the value matches the specified value.

    Args:
        a_dictionary (dict): The input dictionary.
        value: The value to be matched for deletion.

    Returns:
        dict: The modified dictionary after deleting matching key-value pairs.
    """
    list_keys = list(a_dictionary.keys())

    for value_dic in list_keys:
        if value == a_dictionary.get(value_dic):
            del a_dictionary[value_dic]

    return a_dictionary
