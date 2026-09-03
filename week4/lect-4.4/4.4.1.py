## Generate a list of 1000 random numbers between 1 and 1000, and sort the list
# after sorting, print the smallest, second smallest, largest and second largest number in the list

import random
l=[]

for i in range(1000):
    l.append(random.randint(1,1000))

l.sort()
print(l)

print(l[0])
print(l[1])
print(l[-1])
print(l[-2])