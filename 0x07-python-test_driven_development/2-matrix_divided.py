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

    for i in matrix:
        inner_list = []
        if type(i) is not list:
            raise TypeError('matrix must be a matrix (list of lists) of '\
                            'integers/floats')
        if size != len(i):
            raise TypeError('Each row of the matrix must have the same size')
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError('matrix must be a matrix (list of lists) of '\
                                'integers/floats')
            inner_list.append(round(j / div, 2))
        new_matrix.append(inner_list)

    return new_matrix
