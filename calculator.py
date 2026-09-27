import ast
import operator


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


def subtraction(a, b):
    """Perform subtraction of two numbers."""
    return a - b


def multiplication(a, b):
    """Perform multiplication of two numbers."""
    return a * b


def division(a, b):
    """Perform division while preventing division by zero."""
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b


def evaluate_expression(expression):
    """Evaluate an arithmetic expression using PEMDAS."""

    allowed_operators = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.Pow: operator.pow,
        ast.USub: operator.neg,
        ast.UAdd: operator.pos
    }

    def calculate(node):
        if isinstance(node, ast.Constant):
            if isinstance(node.value, (int, float)):
                return node.value
            raise ValueError("Invalid value.")

        if isinstance(node, ast.BinOp):
            operator_function = allowed_operators.get(type(node.op))

            if operator_function is None:
                raise ValueError("Invalid operator.")

            left = calculate(node.left)
            right = calculate(node.right)

            if isinstance(node.op, ast.Div) and right == 0:
                raise ZeroDivisionError

            return operator_function(left, right)

        if isinstance(node, ast.UnaryOp):
            operator_function = allowed_operators.get(type(node.op))

            if operator_function is None:
                raise ValueError("Invalid operator.")

            return operator_function(calculate(node.operand))

        raise ValueError("Invalid expression.")

    tree = ast.parse(expression, mode="eval")

    return calculate(tree.body)


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
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                result = subtraction(a, b)
                print("Subtraction Result:", result)
            except ValueError:
                print("Error: Invalid input. Please enter numbers.")

        elif choice == "3":
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                result = multiplication(a, b)
                print("Multiplication Result:", result)
            except ValueError:
                print("Error: Invalid input. Please enter numbers.")

        elif choice == "4":
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))

                if b == 0:
                    print("Error: Cannot divide by zero.")
                else:
                    result = division(a, b)
                    print("Division Result:", result)

            except ValueError:
                print("Error: Invalid input. Please enter numbers.")

        elif choice == "5":
            expression = input(
                "Enter expression (example: 2 + 3 * 4): "
            )

            try:
                result = evaluate_expression(expression)
                print("PEMDAS Result:", result)

            except ZeroDivisionError:
                print("Error: Cannot divide by zero.")

            except (ValueError, SyntaxError):
                print("Error: Invalid expression.")

        elif choice == "6":
            print("Thank you for using Calculator Master!")
            break

        else:
            print("Error: Invalid menu choice. Please select 1-6.")


if __name__ == "__main__":
    calculator()