# write a function is_present that takes a list of numbers and a number n as arguments and returns True if n is present in the list, otherwise False.

l=[1,2,3,4,5,6,7,8,9,10]

def is_present(l,n):

    if n in l:
        return True
    else:
        return False

print(is_present(l,5))
print(is_present(l,15))            