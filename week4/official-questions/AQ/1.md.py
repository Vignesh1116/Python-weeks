x = int(input())
count=0

for i in range(1,x+1):
    if x % i ==0:
        count+=1
print(count)

if int(x**0.5)*int(x**0.5) == x:
    print("perfect square")
else:
    print("Not perfect square")    