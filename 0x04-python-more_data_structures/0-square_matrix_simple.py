#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    
    """
    Compute the square value of all integers in a two-dimensional matrix.

    Args:
        matrix (list of lists): The input matrix, a list of lists where each inner list represents a row.

    Returns:
        list of lists: A new matrix of the same size as the input matrix, where each value is the square
        of the corresponding input value. The original matrix is not modified.
    """

    new_matrix = matrix.copy()

    for i in range(len(matrix)):
        new_matrix[i] = list(map(lambda x: x**2, matrix[i]))

    return new_matrix

