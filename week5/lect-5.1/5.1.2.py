# create a function named `sub` that takes three parameters as 
# input and  returns
#  their the minimum difference among the three


def sub(a=10, b=20, c=15):
    diff1 = abs(a - b) # 10-20=10
    diff2 = abs(a - c) # 10 -15=5
    diff3 = abs(b - c) # 20-15=5
    
    return min(diff1, diff2, diff3)

print(sub())