print("Program starting.")

# Prompt user for two words
word1 = input("Insert first word: ")
word2 = input("Insert second word: ")

# Calculate lengths
len1 = len(word1)
len2 = len(word2)

# Print lengths
print(f"1st word is {len1} characters long.")
print(f"2nd word is {len2} characters long.")

# Concatenate the words
compound = word1 + word2

# Print compound word with single quotes
print(f"Words together makes one closed compound '{compound}'.")

print("Program ending.")
