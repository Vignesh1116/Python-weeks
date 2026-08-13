# take year of birth (YOB) as input,
# print the current age of the person and also print if the person is eligible to vote or not


# HINT : subtract current year from YOB

YOB=int(input())
age=2025-YOB
print(age)
if age>18:
    print("eligible to vote")
else:
    print("not eligible")    