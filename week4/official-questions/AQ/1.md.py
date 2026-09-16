x = int(input()) #10 #4
count=0

for i in range(1,x+1): # 1,11
    if x % i ==0: #10%1=0 , 10%2=0, 10%5=0, 10%10=0
        count+=1 #1,2,3,4
print(count) #4

if int(x**0.5)*int(x**0.5) == x: #10**0.5 =3.16 * 3.16 == 9.98 == 10
    print("perfect square")
else:
    print("Not perfect square")    