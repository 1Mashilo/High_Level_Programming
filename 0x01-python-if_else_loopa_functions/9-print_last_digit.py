def print_last_digit(number):

    """Print the last digit of a number and return it."""
    S
    print(abs(number) % 10, end="")
    return (abs(number) % 10)

# Test case 1: Positive number with multiple digits
result = print_last_digit(12345)
print("\nResult:", result)

# Test case 2: Negative number with multiple digits
result = print_last_digit(-6789)
print("\nResult:", result)

# Test case 3: Single-digit positive number
result = print_last_digit(7)
print("\nResult:", result)