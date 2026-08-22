# write a code to find whether the given number is prime or not

num=int(input("Enter the Number:"))

flag=0

if num<=1:
    print("Not a Prime")
else:
    for i in range(2,num):
        if num % i == 0:
            flag=1
            break  

    if flag == 0:
        print("Prime")      
    else:
        print("Not a prime")    