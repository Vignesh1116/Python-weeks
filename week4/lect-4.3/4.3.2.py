# create a list of 20 random integers between 1 and 10, generated using random library

import random
l=[]

for i in range(20):
    l.append(random.randint(1,10))
print(l)    