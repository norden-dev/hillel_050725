from typing import Any


class MyClass:
    def __init__(self, value: str) -> None:
        self.value = value

    def say_hello(self) -> str:
        return f"Hello, {self.value}"


def analyze_object(obj: Any) -> None:
    """
    Analyze a given object and print information about it.
    """
    print(f"Type of object: {type(obj)}\n")
    print("Attributes and methods:\n")

    attributes = dir(obj)

    for attr_name in attributes:
        if attr_name.startswith("__"):
            continue

        attr_value = getattr(obj, attr_name)
        print(f"- {attr_name}: {type(attr_value)}")


obj = MyClass("World")
analyze_object(obj)
