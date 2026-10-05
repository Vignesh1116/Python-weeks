# create a function that takes two list as input and return their dot products as output

'''
sample test case
l1=[1,2,3]
l2=[4,5,6]
dot_product(l1,l2)

# ans : 32
'''

def dot_product(l1, l2):
    result = 0

    for i in range(3): #3 0,1,2
        result += l1[i] * l2[i]

    return result


l1 = [1, 2, 3]
l2 = [4, 5, 6]

print(dot_product(l1, l2))