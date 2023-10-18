
def add_integer(a, b):
    """
    Return the addition of two numbers.

    Args:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int: The sum of a and b as an integer.

    Raises:
        TypeError: If either a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return a + b
