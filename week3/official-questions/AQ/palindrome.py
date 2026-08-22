num=input()
rev=''

for i in num:
    rev=i+rev
if rev == num:
    print("Palindrome")
else:
    print("Not palindrome")        

#without using looping find 2cube power value

n=int(input())
result=2**n     
print(result)

#permutations of a string

import itertools

s = "abc"
perms = itertools.permutations(s)

for p in perms:
    print("".join(p))

#matrix 90 degree left rotation

