from typing import Callable


def operation_calculator(operation: str) ->Callable[[int | float, int | float], int | float | str]:
    """Return a function to perform arithmetic operations"""

    def calculator(number1: int | float, number2: int | float) -> int | float | str:
        """Performs calculations between two values"""
        if operation == "+":
            return number1 + number2
        elif operation == "-":
            return number1 - number2
        elif operation == "*":
            return number1 * number2
        elif operation == "/":
            return number1 / number2 if number2 != 0 else "Помилка ділення на нуль"
        else:
            return "Невідома операція"

    return calculator


adding = operation_calculator("+")
substraction = operation_calculator("-")
multiplication = operation_calculator("*")
division = operation_calculator("/")
print(adding(5, 2))
print(substraction(5, 2))
print(multiplication(5, 2))
print(division(5, 2))
