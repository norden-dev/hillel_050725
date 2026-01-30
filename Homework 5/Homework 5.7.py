import functools
import types
from typing import Type, Callable, Any


def log_methods(cls: Type[Any]) -> Type[Any]:
    """
    Class decorator that wraps all methods of a class with a logging layer.

    """
    for name, attr in cls.__dict__.items():

        if isinstance(attr, types.FunctionType):
            setattr(cls, name, _wrap(attr, name))

        elif isinstance(attr, staticmethod):
            setattr(cls, name, staticmethod(_wrap(attr.__func__, name)))

        elif isinstance(attr, classmethod):
            setattr(cls, name, classmethod(_wrap(attr.__func__, name)))

    return cls


def _wrap(func: Callable[..., Any], name: str) -> Callable[..., Any]:
    """
    Create a wrapper around a function to log its calls.

    """

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        printable_args = args[1:] if args else args
        print(f"Logging: {name} called with {printable_args}")
        return func(*args, **kwargs)

    return wrapper


@log_methods
class MyClass:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b


obj = MyClass()
obj.add(5, 3)  # Logging: add called with (5, 3)
obj.subtract(5, 3)  # Logging: subtract called with (5, 3)
