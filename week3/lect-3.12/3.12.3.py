
emp_id = input("Enter the employee id:") #1

while emp_id != "-1":
    Trade = int(input("Enter the amount:"))#1000
    profit_loss=0

    while Trade != 0:#1000!=0  2000!=0 0!=0
        profit_loss=profit_loss+Trade #0+1000=1000  / 1000+2000=3000
        Trade = int(input("Enter the amount:"))#2000 0
    print(profit_loss)
    emp_id = input("Enter the employee id:")