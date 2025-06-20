 
calorie_chart = {
    "egg": 70,
    "carrot": 20,
    "nutella": 1.0,  # per gram, since 100g = 100kcal
    "toast": 80,
    "banana": 90,
    "chicken breast": 1.65,  # per gram
    "rice": 200,
    "apple": 95,
    "milk": 120,
    "yogurt": 1.0  # per gram
}

# Function to parse items like "2 eggs" or "100g Nutella"
def calculate_meal_calories(meal_name):
    print(f"\nEnter food items for {meal_name} (type 'done' when finished):")
    total = 0
    while True:
        item = input(">> ").strip().lower()
        if item == "done":
            break
        try:
            quantity, *name_parts = item.split()
            quantity = quantity.replace("g", "")
            quantity = float(quantity)
            food_name = " ".join(name_parts)
            if food_name not in calorie_chart:
                print("Item not recognized. Try again.")
                continue
            cal_value = calorie_chart[food_name]
            if food_name in ["nutella", "chicken breast", "yogurt"]:
                total += quantity * cal_value
            else:
                total += quantity * cal_value
        except:
            print("Invalid input format. Example: '2 eggs' or '100g Nutella'")
    print(f"Total calories for {meal_name}: {total:.2f} kcal")
    return total

# Main program
def main():
    print("Welcome to the Calorie Tracker!")
    breakfast = calculate_meal_calories("breakfast")
    lunch = calculate_meal_calories("lunch")
    dinner = calculate_meal_calories("dinner")

    daily_total = breakfast + lunch + dinner
    print(f"\nTotal calories for the day: {daily_total:.2f} kcal")

