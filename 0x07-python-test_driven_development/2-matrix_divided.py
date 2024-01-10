#!/usr/bin/python3

def matrix_divided(matrix, divisor):
    """
    Divide all elements in the matrix by the given divisor.

    Args:
        matrix (list of lists): The matrix to be divided.
        divisor (int or float): The divisor.

    Returns:
        list of lists: A new matrix representing the division of elements.
        
    Raises:
        TypeError: If matrix is not a list of lists of integers/floats, or if the
            divisor is not an integer or float.
        ZeroDivisionError: If the divisor is 0.
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_length = None
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if row_length is None:
            row_length = len(row)
        elif row_length != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        for value in row:
            if not isinstance(value, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not isinstance(divisor, (int, float)):
        raise TypeError("divisor must be a number")

    if divisor == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(value / divisor, 2) for value in row] for row in matrix]
