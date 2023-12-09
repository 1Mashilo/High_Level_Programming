#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """
    Print a matrix of integers.

    Args:
        matrix (list of lists): The matrix to be printed, where each inner list represents a row.
    """
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j != 0:
                print(" ", end='')
            print("{:d}".format(matrix[i][j]), end='')
        print()
