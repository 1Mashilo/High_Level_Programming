#!/usr/bin/python3

def square_matrix_map(matrix=[]):
    """
    Calculate the square of each element in a matrix using `map`.

    Args:
        matrix (list, optional): The input matrix (list of lists). Defaults to an empty list.

    Returns:
        list: A new matrix of the same size as the input matrix, where each element is the square of the corresponding
              element in the input matrix.
    """

    return (list(map(lambda x: list(map(lambda y: y**2, x)), matrix))) 