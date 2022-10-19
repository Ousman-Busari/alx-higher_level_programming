#!/usr/bin/python3
"""
This module contains a function that mutiplies two matrixes
The matrixes must be a list of list of int/float

The name of function is matrix_mul
"""

def matrix_mul(m_a, m_b):
    """
    Multiplies two matrixes when the number of column in the first matrix
    is equal to the number of rows in the second matrix,
    adds the results to a new matrix.
    Returns the new matrix
    """
    if type(m_a) is not list:
        raise TypeError('m_a must be a list')
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")

    if type(m_b) is not list:
        raise TypeError('m_b must be a list')
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")


    for i in m_a:
        if type(i) is not list:
            raise TypeError('m_a must be a list of lists')
        if len(i) == 0:
            raise ValueError("m_a can't be empty")
        if len(i) != len(m_a[0]):
            raise TypeError('each row of m_a must be of the same size')
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError('m_a should contain only integers or floats')

    m_a_avg_len = len(m_a[0])

    for i in m_b:
        if type(i) is not list:
            raise TypeError('m_b must be a list of lists')
        if len(i) == 0:
            raise ValueError("m_b can't be empty")
        if len(i) != len(m_b[0]):
            raise TypeError('each row of m_b must be of the same size')
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError('m_b should contain only integers or floats')

    m_b_avg_len = len(m_b[0])

    # checking if the two matrixes can be multiplied
    if m_a_avg_len != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    new_matrix = []
    for i in range(len(m_a)):
        new_list = []
        j = 0
        while j < m_b_avg_len:
            col_by_row = 0
            k = 0
            mul = 0
            while k < len(m_b):
                mul += m_a[i][k] * m_b[k][j]
                k += 1
            col_by_row += mul
            new_list.append(col_by_row)
            j += 1
        new_matrix.append(new_list)
    return new_matrix

#print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
#print(matrix_mul([[1, 2]], [[3, 4], [5, 6]]))
