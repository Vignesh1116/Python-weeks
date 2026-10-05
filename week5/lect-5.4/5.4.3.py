#  create a matrix multiplication function using numpy

import numpy as np

def matrix_multiply(A, B):
    return np.multiply(A, B)


A = [[1,2,3], [4,5,6], [7,8,9]]
B = [[1,2,1], [3,1,7], [6,2,3]]

print(matrix_multiply(A, B))

# pip install numpy