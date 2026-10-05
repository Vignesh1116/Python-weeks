# Problem-7

# Create a dictionary D with the following structure:

#     key: numbers from 1 to 100, endpoints included
#     value: set of factors of key

# Using this information, find a pair of numbers in the range

# [1,100][1,100] that have the most number of factors in common. If there are multiple pairs, store all such pairs as a list of tuples.


D = {}

# create dictionary of factors
for i in range(1,101):
    s = set()
    for j in range(1,i+1):
        if i % j == 0:
            s.add(j)
    D[i] = s

max_common = 0
pairs = []

# find pairs with maximum common factors
for a in range(1,101):
    for b in range(a+1,101):
        common = D[a] & D[b]

        if len(common) > max_common:
            max_common = len(common)
            pairs = [(a,b)]

        elif len(common) == max_common:
            pairs.append((a,b))

print(pairs)
