num=123
op=num%10
num=num//10

while num>0:
    digit=num%10
    op=op*10+digit
    num=num//10

print(op)    