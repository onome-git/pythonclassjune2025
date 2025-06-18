print("Hello World")
print([1,2,3,4,5,6,7,8,9,10])
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum is:", a + b)
import random
print("Random number:", random.randint(1, 100))
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
import random
 
print(" Welcome to the Guessing Game!")
secret_number = random.randint(1, 10)
attempts = 3
import random
 
print(" Welcome to the Guessing Game!")
secret_number = random.randint(1, 10)
attempts = 3
 
while attempts > 0:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == secret_number:
        print("🎉 Correct! You win!")
        break
    else:
        attempts -= 1
        if guess < secret_number:
            print("Too low!")
        else:
            print("Too high!")
 
        if attempts > 0:
            print(f"Try again! {attempts} attempts left.")
        else:
            print(f" Out of tries! The number was {secret_number}")
       