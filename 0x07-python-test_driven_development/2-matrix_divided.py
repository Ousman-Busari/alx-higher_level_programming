#!/usr/bin/python3
"""
This module contains a function that divides
all elements of a matrix.The matrix must be a list of list of int/float

The name of fucntion is matrix_divided
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by the parameter div,
    rounds the results to decimal places, adds them to a new
    matrix of equal dimension.
    Returns the new matrix
    """
    new_matrix = []
    if type(matrix[0]) is list:
        size = len(matrix[0])

    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    for i in range(len(matrix)):
        inner_list = []
        if type(matrix[i]) is not list:
            raise TypeError('matrix must be a matrix (list of lists) of '
                            'integers/floats')
        if size != len(matrix[i]):
            raise TypeError('Each row of the matrix must have the same size')
        for j in range(len(matrix[i])):
            if type(matrix[i][j]) is not int and\
               type(matrix[i][j]) is not float:
                raise TypeError('matrix must be a matrix (list of lists) of '
                                'integers/floats')
            if div != float('inf'):
                inner_list.append(round(matrix[i][j] / div, 2))
            else:
                inner_list.append(0.0)
        new_matrix.append(inner_list)

    return new_matrix
