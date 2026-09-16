#  create a function that returns the average of the elements present in the list

def swap(m,i,j,dim=0):

    if dim == 0:
        m[i],m[j] = m[j],m[i]

    elif dim == 1:
        for row in m:
            row[i],row[j] = row[j],row[i]
    return m      
m = [[1,2,3],[4,5,6],[7,8,9]]

print(swap(m,0,2))
