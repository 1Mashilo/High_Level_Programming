def pow(a, b):
    """
    Return the result of raising 'a' to the power of 'b'.

    Args:
        a (int): The base number.
        b (int): The exponent.

    Returns:
        int: The result of 'a' raised to the power of 'b'.
    """
    return (a ** b)

# Test cases
result1 = pow(2, 3)
# Expected output: 8 (2^3)
print("Result 1:", result1)

result2 = pow(5, 2)
# Expected output: 25 (5^2)
print("Result 2:", result2)

result3 = pow(3, 0)
# Expected output: 1 (Any number raised to the power of 0 is 1)
print("Result 3:", result3)
