#!/usr/bin/python3
import numpy

def lazy_matrix_mul(matrix_a, matrix_b):
    """
    Perform matrix multiplication using NumPy.

    Args:
        matrix_a (list of lists): The first matrix to multiply.
        matrix_b (list of lists): The second matrix to multiply.

    Returns:
        list of lists: The result of the matrix multiplication.
    """
    return numpy.matmul(matrix_a, matrix_b)
