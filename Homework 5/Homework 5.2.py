from typing import Any


class Calculator:
    def add(self, a: int, b: int) -> int:
        """Return the sum of two numbers."""
        return a + b

    def subtract(self, a: int, b: int) -> int:
        """Return the difference between two numbers."""
        return a - b


def call_function(obj: Any, method_name: str, *args: Any) -> Any:
    """
    Dynamically call a method of an object by its name.
    """
    method = getattr(obj, method_name)
    return method(*args)


calc = Calculator()
print(call_function(calc, "add", 10, 5))
print(call_function(calc, "subtract", 10, 5))
