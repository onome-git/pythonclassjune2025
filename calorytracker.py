 
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

# def calculate_meal_calories(meal_name):
    print(f"\nEnter food items for {meal_name} (type 'done' when finished):")
    total = 0
    while True:
        item = input(">> ").strip().lower()
        if item == "done":
            break
        try:
            parts = item.split()
            if len(parts) < 2:
                print("Please use format like '2 egg' or '100g nutella'")
                continue

            quantity_raw = parts[0]
            food_name = " ".join(parts[1:])

            # Handle 'g' (e.g., 100g)
            if "g" in quantity_raw:
                quantity = float(quantity_raw.replace("g", ""))
            else:
                quantity = float(quantity_raw)

            if food_name not in calorie_chart:
                print(f"Food item '{food_name}' not recognized. Try again.")
                continue

            calories_per_unit = calorie_chart[food_name]
            total += quantity * calories_per_unit

        except ValueError:
            print("Invalid number format. Example: '2 egg' or '100g nutella'")
        except Exception as e:
            print(f"Unexpected error: {e}")

    print(f"Total calories for {meal_name}: {total:.2f} kcal")
    return total    