#!/usr/bin/env python3

def print_matrix_integer(matrix=[[]]):
    i = 0
    for row in matrix:
        j = 0
        while j < 3:
            if j == 2:
                print("{:d}".format(matrix[i][j]))
            else:
                print("{:d} ".format(matrix[i][j]), end="")
            j += 1
        i += 1
