# create a function to do matrix multiplication 

'''
testcase:

A=[[1,2,3],[4,5,6],[7,8,9]]
B=[[1,2,1],[3,1,7],[6,2,3]]
output:
[[25,10,24],[55,25,57],[85,40,90]]

'''

def matrix_multiply(A, B):
    result = []

    for i in range(len(A)):
        row = []

        for j in range(len(B[0])):
            total = 0

            for k in range(len(B)):
                total += A[i][k] * B[k][j]

            row.append(total) # [25,10,24],[55,25,57],[85,40,90]

        result.append(row) #[[25,10,24],[55,25,57],[85,40,90]]

    return result


A = [[1,2,3], [4,5,6], [7,8,9]]
B = [[1,2,1], [3,1,7], [6,2,3]]

print(matrix_multiply(A, B))