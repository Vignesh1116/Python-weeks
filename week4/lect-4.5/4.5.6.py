# create a python code to sort the list using while loop
l=[9,3,7,1,6,3,4]

t=True 
while t:
    t=False
    for i in range(len(l)-1): #0 1 2 3 4 5
        if l[i]>l[i+1]:     #9>3   #3>7 7>1 1>6 6>3 5>4
            l[i],l[i+1]=l[i+1],l[i] #9,3=3,9 / 7,1 = 1,7 6,3=3,6 4,5
            t=True
print(l)


# 