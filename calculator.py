def show_menu():
    print("\n===== CALCULATOR MASTER =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. PEMDAS Expression")
    print("6. Exit")


def addition(a, b):
    """Perform addition of two numbers."""
    return a + b


def calculator():
    while True:
        show_menu()

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                result = addition(a, b)
                print("Addition Result:", result)
            except ValueError:
                print("Error: Invalid input. Please enter numbers.")

        elif choice == "2":
            print("Subtraction feature will be added.")

        elif choice == "3":
            print("Multiplication feature will be added.")

        elif choice == "4":
            print("Division feature will be added.")

        elif choice == "5":
            print("PEMDAS feature will be added.")

        elif choice == "6":
            print("Thank you for using Calculator Master!")
            break

        else:
            print("Error: Invalid menu choice. Please select 1-6.")


if __name__ == "__main__":
    calculator()