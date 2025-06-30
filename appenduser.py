users = {
    "onome": {"password": "love123", "balance": 400},
    "antione": {"password": "abc456", "balance": 200},
    "negar": {"password": "abc456", "balance": 200}
}


roles = {
    "admin": ["alice", "bob"],
    "guest": ["charlie"]
}

def sign_up():     #
    print("=== Sign Up ===")
    username = input("Choose a username: ")
    if username in users:
        print("Username already exists. Try another one.")
        return
    password = input("Create a password: ")
    try:
        balance = float(input("Enter starting balance: "))
    except ValueError:
        print("Invalid balance. Must be a number.")
        return
    users[username] = {"password": password, "balance": balance}
    print(f"User '{username}' registered successfully!")

    # Ask user to choose a role and append to roles dictionary
    print("Assign role to user (admin/guest):")
    role = input("Enter role: ").lower()
    if role in roles:
        roles[role].append(username)
        print(f"User '{username}' added to role '{role}'.")
    else:
        print("Role not found. User not added to any role.")

def NationalBank_atm():
    print("Welcome to National Bank ATM")
    while True:
        print("\nMenu:")
        print("1. Login")
        print("2. Sign Up")
        print("3. Show roles")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            username = input("Enter username: ")
            if username not in users:
                print("User does not exist.")
                continue
            password = input("Enter password: ")
            if users[username]["password"] != password:
                print("Incorrect password.")
                continue

            print("Login successful!")
            balance = users[username]["balance"]

            while True:
                print(f"\nCurrent balance: ${balance}")
                print("Choose an option:")
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Check Balance")
                print("4. Invest")
                print("5. Logout")

                atm_choice = input("Enter choice: ")

                if atm_choice == "1":
                    try:
                        amount = float(input("Amount to deposit: "))
                        balance += amount
                        print(f"Deposited ${amount}. New balance: ${balance}")
                    except ValueError:
                        print("Invalid amount.")
                elif atm_choice == "2":
                    try:
                        amount = float(input("Amount to withdraw: "))
                        if amount > balance:
                            print("Insufficient funds.")
                        else:
                            balance -= amount
                            print(f"Withdrawn ${amount}. New balance: ${balance}")
                    except ValueError:
                        print("Invalid amount.")
                elif atm_choice == "3":
                    print(f"Your current balance is: ${balance}")
                elif atm_choice == "4":
                    try:
                        invest_amount = float(input("Amount to invest: "))
                        profit = invest_amount * 0.5
                        balance += profit
                        print(f"You earned ${profit} profit from investment!")
                    except ValueError:
                        print("Invalid amount.")
                elif atm_choice == "5":
                    print("Logging out...\n")
                    users[username]["balance"] = balance
                    break
                else:
                    print("Invalid choice. Try again.")
        elif choice == "2":
            sign_up()
        elif choice == "3":
            print("\nRoles and users:")
            for role, members in roles.items():
                print(f"{role}: {members}")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

NationalBank_atm()
