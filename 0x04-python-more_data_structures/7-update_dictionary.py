#!/usr/bin/python3

def update_dictionary(dictionary, key, value):
    """
    Replace or add a key/value pair in a dictionary.

    Args:
        dictionary (dict): The dictionary to be updated.
        key (str): The key to be added or updated.
        value: The value to be associated with the key.

    Returns:
        dict: The updated dictionary.
    """
    dictionary[key] = value
    return dictionary

