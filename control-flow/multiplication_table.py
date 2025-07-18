# Multiplication Table Generator
print("Multiplication Table Generator")

# Get user input
number = int(input("Enter a number to generate its multiplication table: "))

# Generate and print the multiplication table from 1 to 50
print(f"Multiplication table for {number}:")
for i in range(1, 11):
    product = number * i
    print(f"{number} * {i} = {product}")
