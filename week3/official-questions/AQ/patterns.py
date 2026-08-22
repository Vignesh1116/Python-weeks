# for i in range (5):
#     print(5*"*")

# for i in range(1,6):
#     print(i*"*")    

# for i in range(5,0,-1):
#     print(i*"*")    

op=''
for i in range(1,6):
    op+=str(i)+""
    print(op)

# for i in range(1,6):
#     print(i*'*')
# for i in range(5,0,-1):
#     print(i*"*")    

# for i in range(1,6):
#     print(" "*(5-i)+"*"*i)


# a= [1,1,2,2,3,3,3,5,5,5,4]

# freq={}

# for i in a:
#     if i in freq:
#         freq[i]+=1
#     else:
#         freq[i]=1
# print(freq)     
       
# num = int(input("Enter a number: "))#123
# total = 0

# # while num > 0:           #123>0       12>0         1>0
# #     digit = num % 10     #3            2             1
# #     total = total+ digit #0=0+3=3     3+2=5        5+1=6
# #     num //= 10           #123//10=12   12//10=1      1//10=0

# # print("Sum of digits =", total)


# num=int(input())
# temp=num
# total=0
# n=len(str(num))
# while num>0:
#     digit=num%10
#     total+=digit**n
#     num//=10

# if total == temp:
#     print("Armstrong")
# else:
#     print("not armstrong")   


    #without using looping find 2 power value

n=int(input())
num=2**n
print(num)

#permutations of string 

import itertools

s = "abc"
perms = itertools.permutations(s)

for p in perms:
    print("".join(p))

    #find the palindromic substring

# s = "ababa"
# n = len(s)          
# palindromic_substrings = []
# for i in range(n):
#     for j in range(i + 1, n + 1):
#         substring = s[i:j]
#         if substring == substring[::-1]:
#             palindromic_substrings.append(substring)
# print(set(palindromic_substrings))

#find the trailing number of zeros

num = 45000
count = 0

while num % 10 == 0:
    count += 1
    num //= 10

print(count)



