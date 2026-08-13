marks=int(input("Enter the marks:"))

if marks<0:
    print("invalid input")
elif marks<=100:
    print("A")
elif marks>=80 and marks<90:
    print("B")
elif marks>=70 and marks<80:
    print("C")
elif marks>=60 and marks<70:
    print("D")
elif marks<60:
    print("E")
else:
    print("Invalid input")                     