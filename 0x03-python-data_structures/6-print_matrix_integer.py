#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for rown in row:
            print("{:d}".format(rown), end='')
            print(" ".format(), end='')
        print("")
