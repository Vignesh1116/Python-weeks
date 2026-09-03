## Generate a list of 100 random numbers between 1 and 1000, and sort the list
##  create another list even, and add all the even numbers to this even list and print the list
## similarly create another list odd, and add all the odd numbers to this odd list and print the list

import random
l=[]
even=[]
odd=[]

for i in range(100):
    l.append(random.randint(1,1000))
l.sort()
print(l)

for i in l:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)