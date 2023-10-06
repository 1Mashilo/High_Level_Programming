def swap_variables(a, b):
    """
    Swap the values of two variables.

    Args:
        a: The first variable.
        b: The second variable.

    Returns:
        tuple: A tuple containing the values of the variables after swapping.

    Example:
        >>> a = 89
        >>> b = 10
        >>> a, b = swap_variables(a, b)
        >>> print("a={:d} - b={:d}".format(a, b))
        a=10 - b=89
    """
    a, b = b, a
    return a, b

a = 89
b = 10
a, b = swap_variables(a, b)
print("a={:d} - b={:d}".format(a, b))
