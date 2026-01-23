class UnknownOperationError(Exception):
    """
    Exception raised when an unsupported arithmetic operation is provided.
    """


def calk() -> None:
    """Simple console calculator that performs basic arithmetic operations."""
    try:
        num1: float = float(input("Enter first number: "))
        operation: str = input("Enter operation (+, -, *, /): ")
        num2: float = float(input("Enter second number: "))

        if operation == "+":
            result: float = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                raise ZeroDivisionError("Division by zero is not supported!")
            result = num1 / num2
        else:
            raise UnknownOperationError("Unknown operation! Type only +, -, *, or /.")

        print(f"Result: {result}")

    except ValueError:
        print("Error: Please enter a valid number.")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    except UnknownOperationError as e:
        print(f"Error: {e}")
    except OverflowError:
        print("Error: Number overflow.")
    except Exception as e:
        print(f"Unexpected error: {e}")


calk()
