#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """
    Add two tuples element-wise.

    Args:
        tuple_a (tuple, optional): The first tuple to be added. Defaults to an empty tuple (0, 0).
        tuple_b (tuple, optional): The second tuple to be added. Defaults to an empty tuple (0, 0).

    Returns:
        tuple: A new tuple containing the sum of elements from the input tuples.

    Example:
        >>> result = add_tuple((1, 2), (3, 4))
        >>> print(result)
        (4, 6)
        
        >>> result = add_tuple((1,), (3, 4))
        >>> print(result)
        (4, 4)
        
        >>> result = add_tuple((), (3, 4))
        >>> print(result)
        (3, 4)
        
        >>> result = add_tuple((), ())
        >>> print(result)
        (0, 0)
    """
    
    if len(tuple_a) < 2:
        if len(tuple_a) == 0:
            tuple_a = (0, 0)
        else:
            tuple_a = (tuple_a[0], 0)
    
    if len(tuple_b) < 2:
        if len(tuple_b) == 0:
            tuple_b = (0, 0)
        else:
            tuple_b = (tuple_b[0], 0)

    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
