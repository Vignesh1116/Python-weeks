n=int(input("Enter the numbers: "))

for i in range(n,0,-1):
    for j in range(i,0,-1): # 5 4 3 2 1 / 4 3 2 1
        print(j , end=" ")
    for j in range(2,i+1): # 2 3 4 5 / 2 3 4
         print(j, end=" ")
    print()         
    



# 5 4 3 2 1 2 3 4 5
#    4 3 2 1 2 3 4