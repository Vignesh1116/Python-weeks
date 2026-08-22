num = int(input("Enter the number:"))

for i in range(2,num):
    is_prime = True

    for j in range(2,i):
        if j % i == 0:
            is_prime = False
            break

    if is_prime:
        print(i,end=" ")    