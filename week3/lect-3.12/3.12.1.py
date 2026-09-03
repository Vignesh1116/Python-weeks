# write a code to find whether the given number is prime or not

num=int(input("Enter the Number:"))#6

flag=0

if num<=1:
    print("Not a Prime")
else:
    for i in range(2,num):#2,3,4,5
        if num % i == 0:#6%2==0
            flag=1
            break  

    if flag == 0:
        print("Prime")      
    else:
        print("Not a prime")    