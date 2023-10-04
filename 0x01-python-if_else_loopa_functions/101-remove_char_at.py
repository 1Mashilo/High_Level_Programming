def remove_char_at(str, n):
    """
    Create a copy of the string without the character at position n.

    Args:
        str (str): The input string.
        n (int): The position of the character to remove.

    Returns:
        str: A new string with the character at position n removed. If n is negative, the original string is returned.
    """
    if n < 0:
        
        return str
    else:
        
        return str[:n] + str[n + 1:]




def remove_char_at_test():
    """
    Test the remove_char_at function with a sample test case.
    """
    # Test case 1: Removing the character at position 2 from "Hello"
    result = remove_char_at("Hello", 2)
    expected_output = "Helo"
    if result == expected_output:
        print("Test Case 1 Passed!")
    else:
        print("Test Case 1 Failed. Expected:", expected_output)
        print("Actual:", result)

   