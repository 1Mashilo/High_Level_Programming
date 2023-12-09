
#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """
    Find all multiples of 2 in a list and return a list of Boolean values.

    Args:
        my_list (list, optional): The list of integers in which to find multiples of 2.
                                 Defaults to an empty list.

    Returns:
        list of bool: A list of Boolean values where each element indicates whether the
                      corresponding element in the input list is divisible by 2.

    Example:
        >>> result1 = divisible_by_2([1, 2, 3, 4, 5])
        >>> print(result1)
        [False, True, False, True, False]

        >>> result2 = divisible_by_2([])
        >>> print(result2)
        []
    """
    multiples = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            multiples.append(True)
        else:
            multiples.append(False)

    return multiples
