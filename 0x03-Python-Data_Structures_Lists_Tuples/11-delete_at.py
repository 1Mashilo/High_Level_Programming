def delete_at(my_list=[], idx=0):
    """
    Delete an item at a specific position in a list.

    Args:
        my_list (list, optional): The list from which to delete an item. Defaults to an empty list.
        idx (int, optional): The index of the item to be deleted. Defaults to 0.

    Returns:
        list: The modified list after deleting the item, or the original list if the index is out of range.

    Example:
        >>> my_list = [10, 20, 30, 40, 50]
        >>> delete_at(my_list, 2)
        >>> print(my_list)
        [10, 20, 40, 50]

        >>> delete_at(my_list, 10)
        >>> print(my_list)
        [10, 20, 40, 50]
    """
    if idx >= 0 and idx < len(my_list):
        del my_list[idx]
    return my_list
