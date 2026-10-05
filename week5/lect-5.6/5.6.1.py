#  create a recursive function to return the sum  numbers from 1 to n, take  n as an argument

def sum_n(n):
    if n == 0:
        return 0

    return n + sum_n(n - 1)


print(sum_n(5))