# A three digit number is called a sandwich number if the difference between its first and last digit is equal to its middle digit. Accept a three digit number as input and print sandwich if the number is a sandwich number. Print plain if the number is not a sandwich number. For example, 123 and 853 are sandwich numbers.

n = int(input("Enter a three-digit number: "))

first = n // 100
middle = (n // 10) % 10
last = n % 10

if abs(first - last) == middle:
    print("sandwich")
else:
    print("plain")
