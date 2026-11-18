"""
InternCircle Project 01: Interactive Calculator & Unit Converter

A beginner-friendly command-line application using:
- Functions
- if/elif conditionals
- while loops
- try/except input validation
- A dictionary for conversion factors
"""

# Keep conversion factors in one place so they are easy to update.
CONVERSION_FACTORS = {
    "km_to_miles": 0.621371,
    "kg_to_pounds": 2.20462,
}

# Currency conversion is an extra feature.
# Enter the current exchange rate when the program asks for it.
def read_number(prompt):
    """Keep asking until the user enters a valid number."""
    while True:
        user_input = input(prompt).strip()
        try:
            return float(user_input)
        except ValueError:
            print("Please enter a valid number, for example 12 or 3.5.")


def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Return the difference between two numbers."""
    return a - b


def multiply(a, b):
    """Return the product of two numbers."""
    return a * b


def divide(a, b):
    """Divide two numbers, handling division by zero safely."""
    if b == 0:
        return "Cannot divide by zero."
    return a / b


def km_to_miles(kilometers):
    """Convert kilometers to miles."""
    return kilometers * CONVERSION_FACTORS["km_to_miles"]


def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return celsius * 9 / 5 + 32


def kg_to_pounds(kilograms):
    """Convert kilograms to pounds."""
    return kilograms * CONVERSION_FACTORS["kg_to_pounds"]


def unit_converter():
    """Display the unit conversion menu and perform a conversion."""
    while True:
        print("\n--- UNIT CONVERTER ---")
        print("1. Kilometers to Miles")
        print("2. Celsius to Fahrenheit")
        print("3. Kilograms to Pounds")
        print("4. Back to Main Menu")

        choice = input("Choose a conversion (1-4): ").strip()

        if choice == "1":
            value = read_number("Enter distance in kilometers: ")
            print(f"{value:g} km = {km_to_miles(value):.4f} miles")
        elif choice == "2":
            value = read_number("Enter temperature in Celsius: ")
            print(f"{value:g} C = {celsius_to_fahrenheit(value):.2f} F")
        elif choice == "3":
            value = read_number("Enter weight in kilograms: ")
            print(f"{value:g} kg = {kg_to_pounds(value):.4f} pounds")
        elif choice == "4":
            break
        else:
            print("Please choose an option from 1 to 4.")


def currency_converter():
    """Extra feature: convert between INR and USD using a rate entered by the user."""
    print("\n--- EXTRA: CURRENCY CONVERTER ---")
    print("1. INR to USD")
    print("2. USD to INR")
    choice = input("Choose a conversion (1-2): ").strip()

    if choice not in ("1", "2"):
        print("Please choose 1 or 2.")
        return

    amount = read_number("Enter amount: ")
    if amount < 0:
        print("Amount cannot be negative.")
        return

    rate = read_number("Enter current INR value for 1 USD: ")
    if rate <= 0:
        print("Exchange rate must be greater than zero.")
        return

    if choice == "1":
        print(f"INR {amount:.2f} = USD {amount / rate:.2f}")
    else:
        print(f"USD {amount:.2f} = INR {amount * rate:.2f}")

    print("Note: The exchange rate is supplied by the user; it is not fetched live.")


def get_two_numbers():
    """Read two numbers for an arithmetic operation."""
    first = read_number("Enter the first number: ")
    second = read_number("Enter the second number: ")
    return first, second


def main():
    """Run the main menu until the user chooses to quit."""
    while True:
        print("\n========================================")
        print("  INTERACTIVE CALCULATOR & UNIT CONVERTER")
        print("========================================")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Convert Units")
        print("6. Quit")
        print("7. Extra: Currency Converter")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            a, b = get_two_numbers()
            print("Result:", add(a, b))
        elif choice == "2":
            a, b = get_two_numbers()
            print("Result:", subtract(a, b))
        elif choice == "3":
            a, b = get_two_numbers()
            print("Result:", multiply(a, b))
        elif choice == "4":
            a, b = get_two_numbers()
            print("Result:", divide(a, b))
        elif choice == "5":
            unit_converter()
        elif choice == "6":
            print("Thank you for using the calculator. Goodbye!")
            break
        elif choice == "7":
            currency_converter()
        else:
            print("Please pick a number from 1 to 7.")


if __name__ == "__main__":
    main()
