def add(a,b): return a+b
def subtract(a,b): return a-b
def multiply(a,b): return a*b
def divide(a,b): return "Cannot divide by zero" if b==0 else a/b

while True:
    try:
        x, y = float(input("First number: ")), float(input("Second number: "))
    except ValueError:
        print("Enter valid numbers."); continue

    op = input("Choose (+, -, *, /): ")
    if op == "+": print("Result:", add(x,y))
    elif op == "-": print("Result:", subtract(x,y))
    elif op == "*": print("Result:", multiply(x,y))
    elif op == "/": print("Result:", divide(x,y))
    else: print("Invalid operation")

    if input("Another? (yes/no): ").lower() != "yes":
        print("Bye!"); break