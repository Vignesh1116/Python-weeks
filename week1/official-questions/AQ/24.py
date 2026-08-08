# Accept a two digit number as input and print the sum of its digits. What about a three digit number?

num=int(input())
sum=0
sum+=num%10
print(sum)
sum+=num//10
print(sum)