#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return (list(map(lambda inner_list=[]:
                     list(map(lambda x: x * x, inner_list)), matrix)))
