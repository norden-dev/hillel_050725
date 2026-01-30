from typing import Type, Any


def analyze_inheritance(cls: Type[Any]) -> None:
    """
    Analyze a class and print the methods it inherits from its base classes.
    """
    print(f"Class {cls.__name__} inherits:\n")

    for name in dir(cls):
        attr = getattr(cls, name)

        if not callable(attr) or name.startswith("__"):
            continue

        for base in cls.__mro__:
            if name in base.__dict__:
                if base is not cls:
                    print(f"- {name} from {base.__name__}")
                break


class Parent:
    def parent_method(self):
        pass


class Child(Parent):
    def child_method(self):
        pass
