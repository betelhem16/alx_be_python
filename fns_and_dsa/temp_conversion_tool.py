FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    return CELSIUS_TO_FAHRENHEIT_FACTOR * celsius + 32

def main():
    try:
        
        value = float(input("Enter the temperature to convert: "))
        
        choice = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if choice == 'F':
            converted = convert_to_celsius(value)
            print(f"{value}°F is {converted}°C")
        elif choice == 'C':
            converted = convert_to_fahrenheit(value)
            print(f"{value}°C is {converted}°F")
        else:
            print("Invalid unit. Please enter 'C' or 'F'.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == '__main__':
    main()


