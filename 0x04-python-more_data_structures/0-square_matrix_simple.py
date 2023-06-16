#!/usr/bin/python3
def square_matrix_simple(matrix):
    # Create a new matrix of the same size as the input matrix
    result = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    
    # Compute the square of each element in the input matrix and store it in the result matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result[i][j] = matrix[i][j] ** 2
    
    return result