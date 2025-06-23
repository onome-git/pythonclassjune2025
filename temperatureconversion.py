def celcius_to_farenheit(celsius):
    farenheit = (celsius * 9/5) + 32
    return farenheit
celsius = float(input("Enter temperature in Celsius: "))
farenheit = celcius_to_farenheit(celsius)
print(f"Temperature in Fahrenheit: {farenheit}")
