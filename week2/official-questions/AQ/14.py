# Accept four distinct integers as input from the user. Print in ascending order if the four numbers have been entered in ascending order, and print not in ascending order otherwise.

a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a < b < c < d:
    print("in ascending order")
else:
    print("not in ascending order")
