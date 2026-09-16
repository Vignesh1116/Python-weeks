n, p = int(input()), int(input()) # n = 4, p = 1
S = ''
for i in range(1, n + 1): # 1,2,3,4
    S += str(i) # 1234
# Assume that p is less than or equal to len(S)
print(S[p - 1])
