def max_integer(my_list=[]):
    """
    Find the largest integer in a list.

    Args:
        my_list (list, optional): The list of integers in which to find the largest integer. 
                                 Defaults to an empty list.

    Returns:
        int or None: The largest integer in the list, or None if the list is empty.

    Example:
        >>> result1 = max_integer([10, 20, 5, 30])
        >>> print(result1)
        30

        >>> result2 = max_integer([])
        >>> print(result2)
        None
    """
    if len(my_list) == 0:
        return None

    big = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > big:
            big = my_list[i]

    return big
