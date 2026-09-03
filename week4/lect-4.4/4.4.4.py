## generate a list of 15 numbers random numbers from 1 to 15 and sort it
## print all the numbers from 1 to 15 , which are not in the generated list

import random
l=[]
for i in range(15):
    l.append(random.randint(1,15))
l.sort()
print(l)
for i in range(1,15):
    if i not in l:
        print(i)