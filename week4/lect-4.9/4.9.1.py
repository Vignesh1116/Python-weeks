# create the below matrix A and B with python
# A = 1 2 3
#     4 5 6
#     7 8 9 
# 
# B = 1 2 1
#     6 2 3
#     4 2 1 
#' 
# multiply these two matrices using for loops

# Create Matrix A
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Create Matrix B
B = [
    [1, 2, 1],
    [6, 2, 3],
    [4, 2, 1]
]

# Create result matrix (3x3) filled with 0
result = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# Multiply matrices using for loops
for i in range(len(A)):          # rows of A
    for j in range(len(B[0])):   # columns of B
        for k in range(len(B)):  # columns of A / rows of B
            result[i][j] += A[i][k] * B[k][j]

# Print result
for row in result:
    print(row)