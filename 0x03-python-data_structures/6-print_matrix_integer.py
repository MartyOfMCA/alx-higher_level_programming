#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    rows, cols = 0, 0

    rows = len(matrix)
    for row in range(0, rows):
        cols = len(matrix[row])
        for col in range(0, cols):
            print("{:d}".format(matrix[row][col]), end="")
            if (col < (cols - 1)):
                print(" ", end="")
        print()
    return (None)
