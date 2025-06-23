def weather_forecast():
    while True:
        weather = input("What is the state of the weather today?? (Type 'exit' to quit): ").strip().lower()

        if weather == "exit" or weather == "quit":
            print("Goodbye! Stay safe out there.")
            break
        elif weather == "hot":
            print("It's burning, I need lots of cold water to stay hydrated.")
        elif weather == "cold":
            print("It’s cool today. Wao, I'm happy!")
        elif weather == "rainy":
            print("Everywhere is wet and flooded! Time to carry an umbrella.")
        else:
            print("Sorry, didn’t get you. Please try again with 'hot', 'cold', or 'rainy'.")

weather_forecast()