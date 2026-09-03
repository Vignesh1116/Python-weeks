# Write a program to print the first and last digits of a number without converting it to string.

num = int(input("Enter a number: ")) #121

# Last digit
last = num % 10 #121%10 = 1

# First digit
first = num  #121
while first >= 10: #121>=10  ,12>=10 , 1>=10
    first = first // 10 #121//10 = 12 , 12//10 = 1

print("First digit:", first)
print("Last digit:", last)