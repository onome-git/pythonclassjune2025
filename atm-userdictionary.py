users = {
    "onome": {"password": "love123", "balance": 400},
    "antione": {"password": "abc456", "balance": 200},
    "negar": {"password": "abc456", "balance": 200}
}



def NationalBank_atm():
    print("Welcome to National Bank ATM")

    # Login phase
    username = input("Enter username: ")

    if username not in users:
        print("User does not exist.")
        return  # exit the function

    password = input("Enter password: ")

    if users[username]["password"] != password:
        print("Incorrect password.")
        return

    print("Login successful!")
    balance = users[username]["balance"]

    while True:
        print(f"\nCurrent balance: ${balance}")
        print("Choose an option:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Invest")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            amount = float(input("Amount to deposit: "))
            balance += amount
            print(f"Deposited ${amount}. New balance: ${balance}")
        elif choice == "2":
            amount = float(input("Amount to withdraw: "))
            if amount > balance:
                print("Insufficient funds.")
            else:
                balance -= amount
                print(f"Withdrawn ${amount}. New balance: ${balance}")
        elif choice == "3":
            print(f"Your current balance is: ${balance}")
        elif choice == "4":
            invest_amount = float(input("Amount to invest: "))
            profit = invest_amount * 0.5
            balance += profit
            print(f"You earned ${profit} profit from investment!")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

    # Save balance back to dictionary
    users[username]["balance"] = balance

# Run the ATM
NationalBank_atm()