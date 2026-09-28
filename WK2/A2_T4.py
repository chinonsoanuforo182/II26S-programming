print("Program starting.")
print("Estimate how many minutes you spent on programming...\n")

# Prompt user for each task
t1 = int(input("A1_T1: "))
t2 = int(input("A1_T2: "))
t3 = int(input("A1_T3: "))
t4 = int(input("A1_T4: "))
t5 = int(input("A1_T5: "))
t6 = int(input("A1_T6: "))
t7 = int(input("A1_T7: "))

# Calculate total
total = t1 + t2 + t3 + t4 + t5 + t6 + t7

# Calculate average (two decimals)
average = round(total / 7, 2)

# Rounded integer average
average_int = int(round(total / 7, 0))

print(f"\nIn total you spent {total} minutes on programming.")
print(f"Average per task was {average} min and same rounded to the nearest integer {average_int} min.\n")

print("Program ending.")
