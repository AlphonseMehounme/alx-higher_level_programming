#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for i in range(len(matrix)):
        new = new + [list(map(lambda x: x*x, matrix[i]))]
    return new
