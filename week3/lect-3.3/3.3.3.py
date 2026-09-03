# find the factorial of a number using while loop, take number n as input

num=int(input("Enter the number:")) #5
fact=1
number=1

while number<=num: #1<=5    2<=5   3<=5   4<=5   5<=5 6<=5
    fact=fact*number # 1*1=1 1*2=2  2*3=6  6*4=24 24*5=120
    number+=1 # 2 3 4 5 6

print(fact)    
