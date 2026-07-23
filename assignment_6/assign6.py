# Assignment 6 - ATM Machine

balance = 1000.0  # Initial balance

print("===== ATM MACHINE =====")
print("1. Check Balance")
print("2. Deposit")
print("3. Withdraw")
print("4. Exit")

choice = int(input("Enter your choice (1-4): "))

if choice == 1:
    print("Your balance is:", balance)

elif choice == 2:
    amount = float(input("Enter amount to deposit: "))
    balance = balance + amount
    print("Deposit successful!")
    print("New balance:", balance)

elif choice == 3:
    amount = float(input("Enter amount to withdraw : "))

    if amount <= balance:
        balance = balance - amount
        print("Withdrawal successful!")
        print("Remaining balance:", balance)
    else:
        print("Insufficient funds!")
        print("You cannot withdraw more than your balance.")

elif choice == 4:
    print("Thank you for using our ATM.")

else:
    print("Invalid choice! ")
