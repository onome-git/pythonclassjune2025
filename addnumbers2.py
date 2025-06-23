def add_numbers(current_sum, number):
    return current_sum + number

total_sum = 0  # Start with 0

while True:
    try:
        number = int(input("Input a number: "))
        total_sum = add_numbers(total_sum, number)
    except ValueError:
        print("Please enter a valid number.")
        continue  # Go back to the beginning of the loop

    validation = input("Do you want to enter another number? (Yes/No): ")
    if validation.lower() == "yes":
        continue
    else:
        print("Final Sum:", total_sum)
        print("Bye Bye!!")
        break