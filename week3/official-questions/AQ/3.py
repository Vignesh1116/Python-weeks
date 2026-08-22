# Write a program to accept the positive integer n from the user and print the average of all number's factorial

# from 1 to n .

# for i in range (5,0,-1):

#   space = " " * (5-i)
#   stars=  i * "*"
#   print(space+stars)
 
n = int(input("Enter the number:"))

fact=1
total=0
avg=0

for i  in range(1,n+1):
    fact=fact*i
    total=total+fact
    avg=total/i

print(fact)
print(total)
print(avg)    