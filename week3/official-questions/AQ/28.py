# Two numbers n1 and n2 are said to be the same if they have an equal number of digits in them. 
# Write a program to check whether n1 and n2 are the same. 
# n1 and n2 are positive integers entered by the user without converting the 
# number to string.

# Program to check if two numbers have the same number of digits

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

# Count digits in n1
count1 = 0
while n1 > 0:
    n1 //= 10   # remove last digit
    count1 += 1 # increase counter

# Count digits in n2
count2 = 0
while n2 > 0:
    n2 //= 10
    count2 += 1

# Compare counts
if count1 == count2:
    print("SAME")
else:
    print("NOT SAME")
