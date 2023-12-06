#!/usr/bin/python3

def delete_key_from_dictionarya(dictionary, key):
    """
    Delete a key from a dictionary, if it exists.

    Args:
        dictionary (dict): The dictionary from which to delete the key.
        key (str): The key to be deleted.

    Returns:
        dict: The updated dictionary after key deletion.
    """
    if key in dictionary:
        del dictionary[key]
   return dictionary
