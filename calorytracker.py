 
# Calorie tracker program

# Define calorie data (calories per unit or per gram)
calorie_chart = {
    "egg": 70,
    "carrot": 20,
    "nutella": 1.0,  # per gram
    "toast": 80,
    "banana": 90,
    "chicken breast": 1.65,  # per gram
    "rice": 200,
    "apple": 95,
    "milk": 120,
    "yogurt": 1.0  # per gram
}

def calculate_meal_calories(meal_name):
    print(f"\nEnter food items for {meal_name} (type 'done' when finished):")
    total = 0

    while True:
        item = input(">> ").strip().lower()

        if item == "done":
            break

        parts = item.split()
        if len(parts) < 2:
            print("Use format like '2 egg' or '100g nutella'")
            continue

        quantity_text = parts[0]
        food_name = " ".join(parts[1:])

        try:
            if "g" in quantity_text:
                quantity = float(quantity_text.replace("g", ""))
            else:
                quantity = float(quantity_text)
        except ValueError:
            print("Please enter a valid number for quantity.")
            continue

        if food_name not in calorie_chart:
            print(f"'{food_name}' not recognized. Try again.")
            continue

        calories = quantity * calorie_chart[food_name]
        total += calories

    print(f"Total calories for {meal_name}: {total:.2f} kcal")
    return total

def main():
    print("Welcome to the Calorie Tracker!")

    breakfast = calculate_meal_calories("breakfast")
    lunch = calculate_meal_calories("lunch")
    dinner = calculate_meal_calories("dinner")

    daily_total = breakfast + lunch + dinner
    print(f"\nTotal calories for the day: {daily_total:.2f} kcal")

main()
