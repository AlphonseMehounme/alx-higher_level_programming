#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sq = lambda x: x*x
    new = []
    for i in range(len(matrix)):
        new = new + [list(map(sq, matrix[i]))]
    return new
