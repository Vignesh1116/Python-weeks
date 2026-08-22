# find the factorial of a number using while loop, take number n as input

num=int(input("Enter the number:"))
fact=1
number=1

while number<=num:
    fact=fact*number
    number+=1

print(fact)    
