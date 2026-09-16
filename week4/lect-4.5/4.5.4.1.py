## write a python code to print the maximum element of the list, using for loop

l=[1,44,22,11,23,36,49,28,31,8,54,54]

max=0 #0 1 44 49  54

for i in l: 
    if i>max: #1>0 44>1  22>44 11>44  49>44 28>49 54>49 54>54
        max=i # 1   44     49    54

print(max)
