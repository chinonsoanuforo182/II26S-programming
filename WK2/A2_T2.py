print("Program starting.")

brand = input("Insert car brand: ")
model = input("Insert car model: ")

# Using sep and end in two print commands
print("Car brand is", f"\"{brand}\"", sep=" ", end=" ")
print("and the model is", f"'{model}'.", sep=" ")

print("Program ending.")
