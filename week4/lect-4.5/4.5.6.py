# create a python code to sort the list using while loop
l=[9,3,7,1,6,3,4]

t=True
while t:
    t=False
    for i in range(len(l)-1):
        if l[i]>l[i+1]:
            l[i],l[i+1]=l[i+1],l[i]
            t=True
print(l)