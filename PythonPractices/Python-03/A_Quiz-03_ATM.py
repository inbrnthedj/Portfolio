# ATM Withdrawal 
user_choice = "Withdraw Cash"
if user_choice == "Withdraw Cash":
    amount = int(input("Enter the amount to withdraw: "))
    if amount % 10 == 0:
        print("Amount dispensed: ", amount)
    else:
        print("Please enter a multiple of 10.")
else:
    print("Thank you for using the ATM.")