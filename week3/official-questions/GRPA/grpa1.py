#calculate n 35
n=3
sum=0
for i in range(1,n+1):
    rev_sum=0
    for j in range(1,i+1):
        rev_sum+=j
    sum+=rev_sum
    print(sum)   
    
     

