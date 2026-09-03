num=123
op=num%10 #3
num=num//10 #123//10=12

while num>0:   #12>0           1>0       0>0
    digit=num%10  #12%10=2      1%10=1
    op=op*10+digit #3*10+2=32    32*10+1=321
    num=num//10 #12//10=1    1//10=0

print(op)    