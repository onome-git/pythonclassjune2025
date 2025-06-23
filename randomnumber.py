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
            print(f" Out of tries! The number was {secret_number}.")