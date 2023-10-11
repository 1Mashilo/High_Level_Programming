

def safe_print_division(dividend, divisor):
    """
    Calculate the division of two numbers and print the result.

    Args:
        dividend (float or int): The number to be divided.
        divisor (float or int): The number to divide by.

    Returns:
        float or int or None: The result of the division or None if an exception occurs.
    """
    try:
        result = dividend / divisor 
    except (TypeError, ZeroDivisionError):
        result = None 
    finally:
        print(f"Inside result: {result}") 
    return result
