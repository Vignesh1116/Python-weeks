# Construct the following sets in Python:

#     A is a set of the first 100 positive integers divisible by 3
#     B is a set of the first 100 positive integers divisible by 5.

# Using Python's set notation, find the set of all integers that are:

#     divisible by both 3 and 5
#     divisible by 3 or 5
#     divisible by 3 but not divisible by 5
#     divisible by 5 but not divisible by 3

# Note that each bullet corresponds to a separate set.

# A: first 100 positive integers divisible by 3
A = {x for x in range(1,101) if x % 3 == 0}

# B: first 100 positive integers divisible by 5
B = {x for x in range(1,101) if x % 5 == 0}

# divisible by both 3 and 5
print(A & B)

# divisible by 3 or 5
print(A | B)

# divisible by 3 but not divisible by 5
print(A - B)

# divisible by 5 but not divisible by 3
print(B - A)