n, p = int(input()), int(input())
S = ''
for i in range(1, n + 1):
    S += str(i)
# Assume that p is less than or equal to len(S)
print(S[p - 1])
