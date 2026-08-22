n = int(input())

if n<0:
    print("Not defined")
elif n == 0:
    print(1)
else:
    fact=1
    num=1

    while num<=n:
        fact=fact*num
        num+=1
    print(fact)                