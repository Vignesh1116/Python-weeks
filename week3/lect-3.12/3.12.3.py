
emp_id = input("Enter the employee id:")

while emp_id != "-1":
    Trade = int(input("Enter the amount:"))
    profit_loss=0

    while Trade != 0:
        profit_loss=profit_loss+Trade
        Trade = int(input("Enter the amount:"))
    print(profit_loss)
    emp_id = input("Enter the employee id:")