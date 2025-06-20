name = "Onome"
job = "Cloud architect"
salary = "$90,000"
location = "Montreal"

print(f"I, {name}, from {location}, working as a {job}, with the salary of {salary}, would love to work in cloud and AI.")

n = int(input("Enter how many Fibonacci numbers to print: "))
a = 0
b = 1
for i in range(n):
    print(a)
    next = a + b
    a = b
    b = next

print("Welcome to NATIONAL Bank")
print("1. Fixed deposit:100")
print("2. Withdrawal limit:300")
print("3. Stock market fund (Minimum):200")
print("4. Crypto Basket")
choice = input("Choose an investment option (1-4): ")