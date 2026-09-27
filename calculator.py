def show_menu():
    print("\n===== CALCULATOR MASTER =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")


def calculator():
    while True:
        show_menu()

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            print("Addition feature will be added.")

        elif choice == "2":
            print("Subtraction feature will be added.")

        elif choice == "3":
            print("Multiplication feature will be added.")

        elif choice == "4":
            print("Division feature will be added.")

        elif choice == "5":
            print("Thank you for using Calculator Master!")
            break

        else:
            print("Error: Invalid menu choice. Please select 1-5.")


if __name__ == "__main__":
    calculator()