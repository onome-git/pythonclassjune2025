def smart_atm():
    balance = 100  # Set initial balance
  
    print("Welcome to the Smart ATM!")
    print(f"Your current balance is: ${balance}")

    while True:
        print("\nChoose an option:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Invest")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            balance += amount
            print(f"${amount} deposited!")
            print("Great job growing your savings!")

        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            if amount <= balance:
                balance -= amount
                print(f"${amount} withdrawn!")
            else:
                print("Not enough money!")

        elif choice == "3":
            print(f"Balance: ${balance}")

        elif choice == "4":
            amount = float(input("Enter amount to invest: "))
            if amount <= balance:
                profit = amount * 0.1
                balance += profit
                print(f"You earned ${profit:.2f} profit!")
                print(f"New balance: ${balance:.2f}")
            else:
                print("Not enough money to invest!")

        elif choice == "5":
            print("Thanks for using Smart ATM. Bye!")
            break

        else:
            print("Invalid choice.")

# Call the function
smart_atm()