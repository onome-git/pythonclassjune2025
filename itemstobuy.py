def calculate_discount(subtotal):
    return subtotal * 0.10  # 10% discount

def calculate_tax(amount):
    return amount * 0.05  # 5% tax

# Step 1: Ask how many items the user wants to buy
num_items = int(input("How many items do you want to buy? "))

items = []  # to store each item's details
subtotal = 0

# Step 2: Collect item details
for i in range(num_items):
    print()
    name = input(f"Enter name of item {i+1}: ")
    price = float(input(f"Enter price of {name}: "))
    quantity = int(input(f"Enter quantity of {name}: "))
    
    total_price = price * quantity
    subtotal += total_price

    # Save details
    items.append((name, quantity, total_price))

# Step 3: Calculate discount and tax
discount = calculate_discount(subtotal)
after_discount = subtotal - discount
tax = calculate_tax(after_discount)
total = after_discount + tax

# Step 4: Print the receipt
print("\nReceipt:")
for name, quantity, total_price in items:
    print(f"- {name} x{quantity} = ${total_price:.2f}")

print(f"\nSubtotal: ${subtotal:.2f}")
print(f"Discount applied: -${discount:.2f}")
print(f"Tax (5%): ${tax:.2f}")
print(f"Total: ${total:.2f}")