print ("Program stating")
name = input("What is your name: John")

First = float(input("enter a floating point number: 3.1"))
Second = float(input("enter a second floating point number: 5.3"))
 
print(f"{name} you entered {First} and {Second}")

product = First * Second
rounded_product = round(product, 2)

print(f"Multiplying {First} and {Second} will result in product {rounded_product}")
print("program ending")
