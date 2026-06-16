# ==========================================
# ADVANCED POWER CALCULATOR
# ==========================================

import math

history = []

def power_calculation():
    try:
        base = float(input("Enter Base Number: "))
        exponent = float(input("Enter Exponent: "))

        result = base ** exponent

        print("\nResult:")
        print(f"{base} ^ {exponent} = {result}")

        history.append(
            f"Power: {base}^{exponent} = {result}"
        )

    except ValueError:
        print("Invalid Input!")

def square_root():
    try:
        num = float(input("Enter Number: "))

        if num < 0:
            print("Cannot calculate square root of negative numbers.")
            return

        result = math.sqrt(num)

        print(f"Square Root = {result}")

        history.append(
            f"Square Root: √{num} = {result}"
        )

    except ValueError:
        print("Invalid Input!")

def logarithm():
    try:
        num = float(input("Enter Number: "))

        if num <= 0:
            print("Logarithm only works for positive numbers.")
            return

        result = math.log10(num)

        print(f"log10({num}) = {result}")

        history.append(
            f"Log10: {num} = {result}"
        )

    except ValueError:
        print("Invalid Input!")

def percentage():
    try:
        value = float(input("Enter Value: "))
        total = float(input("Enter Total: "))

        result = (value / total) * 100

        print(f"Percentage = {result:.2f}%")

        history.append(
            f"Percentage: {value}/{total} = {result:.2f}%"
        )

    except ValueError:
        print("Invalid Input!")
    except ZeroDivisionError:
        print("Total cannot be zero.")

def compound_interest():
    try:
        principal = float(input("Principal Amount: "))
        rate = float(input("Annual Interest Rate (%): "))
        years = float(input("Number of Years: "))
        times = int(input("Compounded Per Year: "))

        amount = principal * (
            (1 + (rate / 100) / times)
            ** (times * years)
        )

        interest = amount - principal

        print("\n----- RESULT -----")
        print(f"Final Amount : {amount:.2f}")
        print(f"Interest Earned : {interest:.2f}")

        history.append(
            f"Compound Interest: Amount={amount:.2f}"
        )

    except ValueError:
        print("Invalid Input!")

def show_history():
    print("\n===== HISTORY =====")

    if len(history) == 0:
        print("No calculations yet.")
    else:
        for i, item in enumerate(history, start=1):
            print(f"{i}. {item}")

def clear_history():
    history.clear()
    print("History Cleared.")

def display_menu():
    print("\n")
    print("=" * 40)
    print("      ADVANCED POWER CALCULATOR")
    print("=" * 40)
    print("1. Power Calculation")
    print("2. Square Root")
    print("3. Logarithm (Base 10)")
    print("4. Percentage")
    print("5. Compound Interest")
    print("6. Show History")
    print("7. Clear History")
    print("8. Exit")
    print("=" * 40)

def main():
    print("\nWelcome to the Advanced Calculator!")

    while True:
        display_menu()

        choice = input("Select Option (1-8): ")

        if choice == "1":
            power_calculation()

        elif choice == "2":
            square_root()

        elif choice == "3":
            logarithm()

        elif choice == "4":
            percentage()

        elif choice == "5":
            compound_interest()

        elif choice == "6":
            show_history()

        elif choice == "7":
            clear_history()

        elif choice == "8":
            print("\nThank You For Using The Calculator!")
            break

        else:
            print("Invalid Choice. Try Again.")

if __name__ == "__main__":
    main()

