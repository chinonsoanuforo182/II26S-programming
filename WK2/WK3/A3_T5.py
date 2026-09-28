print("Program starting.\n")

print("Options:")
print("1 - Celsius to Fahrenheit")
print("2 - Fahrenheit to Celsius")
print("0 - Exit")

choice = input("Your choice: ")

# Celsius → Fahrenheit
if choice == "1":
    celsius = float(input("Insert the amount of Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    fahrenheit_rounded = round(fahrenheit, 1)
    print(f"{celsius:.1f} °C equals to {fahrenheit_rounded:.1f} °F")

# Fahrenheit → Celsius
elif choice == "2":
    fahrenheit = float(input("Insert the amount of Fahrenheit: "))
    celsius = (fahrenheit - 32) / 1.8
    celsius_rounded = round(celsius, 1)
    print(f"{fahrenheit:.1f} °F equals to {celsius_rounded:.1f} °C")

# Exit
elif choice == "0":
    print("Exiting...")

# Unknown option
else:
    print("Unknown option.")

print("\nProgram ending.")
