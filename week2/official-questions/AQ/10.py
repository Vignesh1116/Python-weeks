# Problem-10:

# Accept an integer x as input from the user. If the number is even, print even . If the number is odd, print odd.

x=int(input("Enter the number:"))

last_digit = abs(x)%10

digits=["zero","one","two","three","four","five","six","seven","eight","nine"]

print(digits[last_digit])