'''
create three functions that take a list as input 
1) to return the first element of the list
2) to return the last element of the list
3) to return the sum of values returned from the above two functions 
'''

def first(lst):
    return lst[0]

def second(lst):
    return lst[-1]

def sum(lst):
    return first(lst) + second(lst)

n = [1,2,3,4,5,6,7,8]

print(first(n))
print(second(n))
print(sum(n))