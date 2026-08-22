# Write a program to find the highest common factor (HCF) of two numbers.

a=int(input()) # 10
b=int(input()) # 12
hcf=1
for i in range(1,min(a,b)+1): # 1,10
    if a%i==0 and b%i==0: # 
        hcf=i
print(hcf)  

