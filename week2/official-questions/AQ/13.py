# Accept three non-negative real numbers as input from the user. If the three numbers form the sides of a triangle, print True . If not, print False.

a = float(input())
b = float(input())
c = float(input())

print(a + b > c and a + c > b and b + c > a)