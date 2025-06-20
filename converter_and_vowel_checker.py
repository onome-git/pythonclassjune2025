# Temperature Converter: Celsius to Fahrenheit
def convert_temperature(output_file):
    print("=== Temperature Converter (Celsius to Fahrenheit) ===")
    try:
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        result = f"{celsius}°C is equal to {fahrenheit:.2f}°F\n"
        print(result)
        output_file.write("Temperature Conversion:\n")
        output_file.write(result + "\n")
    except ValueError:
        print("Please enter a valid number.\n")
        output_file.write("Invalid temperature input.\n\n")

# Vowel Checker: Check if word starts with a vowel
def check_vowel_start(output_file):
    print("=== Vowel Checker ===")
    word = input("Enter a word: ").strip().lower()
    if not word:
        print("No word entered.\n")
        output_file.write("No word entered.\n\n")
        return
    if word[0] in "aeiou":
        result = f"'{word}' starts with a vowel.\n"
    else:
        result = f"'{word}' does NOT start with a vowel.\n"
    print(result)
    output_file.write("Vowel Check:\n")
    output_file.write(result + "\n")

# Main program
def main():
    with open("results.txt", "w") as f:
        while True:
            print("Choose an option:")
            print("1. Convert Celsius to Fahrenheit")
            print("2. Check if a word starts with a vowel")
            print("3. Exit")

            choice = input("Enter 1, 2, or 3: ").strip()
            print()
            if choice == "1":
                convert_temperature(f)
            elif choice == "2":
                check_vowel_start(f)
            elif choice == "3":
                print("Goodbye!")
                f.write("User exited the program.\n")
                break
            else:
                print("Invalid choice. Please try again.\n")
                f.write("Invalid menu choice.\n\n")

main()
