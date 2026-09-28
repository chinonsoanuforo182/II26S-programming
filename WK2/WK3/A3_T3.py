print("Program starting.")
print("This is a program with simple menu, where you can choose which operation the program performs.")

# Prompt for username
name = input("Before the menu, please insert your name: ")

# Print menu
print("\nOptions:")
print("1 - Print welcome message")
print("0 - Exit")

choice = input("Your choice: ")

# Perform actions based on user choice
if choice == "1":
    print(f"Welcome {name}!")
elif choice == "0":
    print("Exiting...")
else:
    print("Unknown option.")

print("\nProgram ending.")

