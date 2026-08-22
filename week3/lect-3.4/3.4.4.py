num=int(input())
n=num
reverse=0

while num>0:
    digit=num%10
    reverse=reverse*10+digit
    num=num//10

print(reverse)

if n == reverse:
    print("palindrome")
else:
    print("not palindrome")        