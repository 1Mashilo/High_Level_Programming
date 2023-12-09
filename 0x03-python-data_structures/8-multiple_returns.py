#!/usr/bin/python3

def multiple_returns(sentence):
    """
    Returns the length of a string and its first character.

    Args:
        sentence (str): The input string for which to calculate the length and first character.

    Returns:
        tuple: A tuple containing two elements:
            - The length of the input string.
            - The first character of the input string.

    Example:
        >>> result1 = multiple_returns("Hello, World!")
        >>> print(result1)
        (13, 'H')

        >>> result2 = multiple_returns("")
        >>> print(result2)
        (0, None)
    """

    if sentence == "":
        return (0, None)
    
    return (len(sentence), sentence[0])
