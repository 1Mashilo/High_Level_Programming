def islower(c):
    """
    Check for lowercase characters.

    Args:
        c (str): The character to check.

    Returns:
        bool: True if the character is lowercase, False otherwise.
    """
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False

# Test cases
print(islower('a'))
print(islower('Z'))
print(islower('1'))
print(islower('z'))