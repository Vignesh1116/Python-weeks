# create the below matrix A and B with python
# A = 1 2 3
#     4 5 6
#     7 8 9 
# 
# B = 1 2 1
#     6 2 3
#     4 2 1 
# 
# 

# Create matrices A and B
A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

B = [[1, 2, 1],
     [6, 2, 3],
     [4, 2, 1]]

# Initialize result matrix C with zeros
C = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]

# Calculate the sum of matrices A and B
for i in range(len(A)):
    for j in range(len(A[0])):
        C[i][j] = A[i][j] + B[i][j]

# Print the resulting matrix C
for row in C:
    print(row)


