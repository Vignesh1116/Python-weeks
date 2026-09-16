x=[4,5,6]
y=[1,2,3]

def greater(x,y):

    for i in range(len(x)):
        if x[i]<=y[i]:
            return False
        return True

print(greater(x,y))