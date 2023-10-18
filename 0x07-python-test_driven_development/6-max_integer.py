
def max_integer(integer_list=[]):
    """
    Find and return the maximum integer in a list of integers.

    Args:
        integer_list (list, optional): The list of integers. Defaults to an empty list.

    Returns:
        int: The maximum integer in the list.
        None: If the list is empty.
    """
    
    if len(integer_list) == 0:
        return None
    max_value = integer_list[0]
    for number in integer_list:
        if number > max_value:
            max_value = number
    return max_value
