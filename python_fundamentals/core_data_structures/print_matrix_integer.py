#!/usr/bin/env python3

def print_matrix_integer(matrix=[[]]):
    i = 0
    k = 0
    for column in matrix[0]:
        k += 1
    for row in matrix:
        j = 0
        while j < k:
            if j == k - 1:
                print("{:d}".format(matrix[i][j]))
            else:
                print("{:d} ".format(matrix[i][j]), end="")
            j += 1
        i += 1
    if i == 1 and j == 1 and k == 1:
        print("")
