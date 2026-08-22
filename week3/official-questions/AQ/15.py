# Write a code to accept a string as input and determine if it is a palindrome or not.


s=input()                #123
rev=""
for i in s:
    rev=i+rev          # 1+0=1
                         # 2+1=21
                        # 3+21=321
if s==rev:
    print("Palindrome")
else:
    print("Not a palindrome")
