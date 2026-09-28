print("Program starting.")
print("Welcome to the unit converter program!")
print("Follow the menu instructions below.\n")

# Main menu
print("Options:")
print("1 - Length")
print("2 - Weight")
print("0 - Exit")

choice = input("Your choice: ")

# ---------------- LENGTH MENU ----------------
if choice == "1":
    print("\nLength options:")
    print("1 - Meters to kilometers")
    print("2 - Kilometers to meters")
    print("0 - Exit")

    length_choice = input("Your choice: ")

    # Meters → Kilometers
    if length_choice == "1":
        meters = float(input("Insert meters: "))
        km = meters / 1000
        print(f"{meters:.1f} m is {km:.1f} km")

    # Kilometers → Meters
    elif length_choice == "2":
        km = float(input("Insert kilometers: "))
        meters = km * 1000
        print(f"{km:.1f} km is {meters:.1f} m")

    elif length_choice == "0":
        print("Exiting...")
    else:
        print("Unknown option.")

# ---------------- WEIGHT MENU ----------------
elif choice == "2":
    print("\nWeight options:")
    print("1 - Grams to pounds")
    print("2 - Pounds to grams")
    print("0 - Exit")

    weight_choice = input("Your choice: ")

    # Grams → Pounds (1 gram = 0.00220462 pounds)
    if weight_choice == "1":
        grams = float(input("Insert grams: "))
        pounds = grams * 0.00220462
        print(f"{grams:.1f} g is {pounds:.1f} lb")

    # Pounds → Grams (1 pound = 453.592 grams)
    elif weight_choice == "2":
        pounds = float(input("Insert pounds: "))
        grams = pounds * 453.592
        print(f"{pounds:.1f} lb is {grams:.1f} g")

    elif weight_choice == "0":
        print("Exiting...")
    else:
        print("Unknown option.")

# ---------------- EXIT ----------------
elif choice == "0":
    print("Exiting...")

# ---------------- UNKNOWN ----------------
else:
    print("Unknown option.")

print("\nProgram ending.")
