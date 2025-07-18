#ask  user  pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 1

# Outer while loop for rows
while row <= size:
    # Inner for loop for columns
    for col in range(1, size + 1):
        print("*", end="")

    # Move to next line after each row
    print()

    # Increment row counter
    row += 1
