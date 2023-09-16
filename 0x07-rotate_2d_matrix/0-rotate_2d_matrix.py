#!/usr/bin/python3
# a python code to rotate a 2d matrix by 90 degrees

def rotate_2d_matrix(matrix):
    """
    This is the main function
    """
    n = len(matrix)
    
    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row to get the clockwise rotation
    for i in range(n):
        matrix[i] = matrix[i][::-1]
