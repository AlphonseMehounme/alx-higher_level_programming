#!/usr/bin/python3
"""
    Matrix divided modume
    This module has the matrix divided function
"""


def matrix_divided(matrix, div):
    """Function matrix_divided

       Function that divise matrix

       Args:
         @matrix : Matrix to divise
         @div : Matrix to divise by

       Return:
         Return the matrix divided
    """
    if type(matrix) != list:
        raise TypeError("matrix must be a matrix (list of lists) of"
              "integers/floats")
    for m in matrix:
        if type(m) != list:
            raise TypeError("matrix must be a matrix (list of lists) of"
                  "integers/floats")
        for i in m:
            if type(i) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of"
                      "integers/floats")
        size = len(matrix[0])
        if len(m) != size:
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    rows = len(matrix)
    cols = len(matrix[0])
    newmatrix = [[0] * cols for _ in range(rows)]
    for j in range(rows):
        for k in range(cols):
            newmatrix[j][k] = round(matrix[j][k] / div, 2)
    return newmatrix
