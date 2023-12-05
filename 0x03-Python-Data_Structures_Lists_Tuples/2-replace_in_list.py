#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """
    Replace an element in a list at a specific position.

    Args:
        my_list (list): The list in which to replace the element.
        idx (int): The index at which to replace the element.
        element: The new element to be placed at the specified index.

    Returns:
        The modified list after the replacement.
    """
    if 0 <= idx < len(my_list):
        my_list[idx] = element
    return my_list
