
# write a python script for the below test case,
# Note the input will be of 5 characters long,


# testcase 1
'''
INPUT : 'gokul'
OUTPUT : 'hplvm'
'''

# testcase 2
'''
INPUT: 'abcde'
OUTPUT: 'bcdef'
'''

# solution:

a="abcdefghijklmnopqrstuvwxyz"

b="abcde"
c=""

for i in b:
    c+=a[a.index(i)+1]
print(c)


  