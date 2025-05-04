# Simple Micro-Project=>  ATM Management System without Database and GUI

# function for checking_balance
def check_balance(balance):
    return balance

# funtion for deposit
def deposit(balance,deposit_amount):
    balance+=deposit_amount
    return balance
    
# function for withdraw
def withdraw(balance,withdraw_amount):
    balance+=withdraw_amount
    return balance


while True:
    balance= 55000

    what_operation=input("Enter \"deposit\" , \"withdraw\" , \"check\" , \"exit\" : ").lower().strip()

    if what_operation == "deposit":
        deposit_amount = int(input("Enter deposit amount: "))
        balance = deposit(balance, deposit_amount)  # Update balance
        print("Now Balance is ", balance)
        

    elif what_operation == "withdraw":
        withdraw_amount = int(input("Enter withdraw amount: "))
        if withdraw_amount <= balance:  # Check for sufficient funds
            balance = withdraw(balance, withdraw_amount)  # Update balance
            print("Now Balance is ", balance)
        else:
            print("Insufficient funds.")

    elif what_operation=="check":
        # call check fuction
        print(check_balance(balance))

    elif what_operation=="exit":
        print("Exiting Program...")
        print("Done")
        break

    else:
        print("Invalid Input")
        break









