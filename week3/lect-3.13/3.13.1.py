## write a code for the below test cases

# print until you find @ in the string, using break statement
# TestCase 1
INPUT="abcd@gmail.com"
# OUTPUT:
'''
a
b
c
d
'''

text="abcd@gmail.com"

for i in text:
    if i == "@":
        break
    print(i)