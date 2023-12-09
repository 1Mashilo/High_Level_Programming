#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """
    Replace an element in a copied list at a specific position.

    Args:
        my_list (list): The original list in which to create a copy and replace the element.
        idx (int): The index at which to replace the element.
        element: The new element to be placed at the specified index.

    Returns:
        list: A new list that is a copy of the original list with the specified element replaced.

    Note:
        - If the index is out of range (negative or greater than the list length minus one),
          the original list is returned without modifications.
    """
    if idx < 0 or idx > (len(my_list) - 1):
        return my_list

    copy = [x for x in my_list]
    copy[idx] = element
    return copy
