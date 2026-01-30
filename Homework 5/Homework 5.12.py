from typing import Any, Dict, Tuple, Type


class LoggingMeta(type):
    """
    Metaclass that automatically adds logging for attribute access
    and modification on class instances.
    """

    def __new__(
        mcs: Type[type],
        name: str,
        bases: Tuple[type, ...],
        namespace: Dict[str, Any]
    ) -> Type:
        """
        Create a new class and inject logging behavior into
        __getattribute__ and __setattr__ methods.
        """
        cls: Type = super().__new__(mcs, name, bases, namespace)

        orig_getattribute = (
            cls.__getattribute__
            if "__getattribute__" in namespace
            else object.__getattribute__
        )
        orig_setattr = (
            cls.__setattr__
            if "__setattr__" in namespace
            else object.__setattr__
        )

        def __getattribute__(self: Any, attr: str) -> Any:
            """
            Intercept attribute access and log it.

            """
            if not attr.startswith("__"):
                print(f"Logging: accessed '{attr}'")
            return orig_getattribute(self, attr)

        def __setattr__(self: Any, attr: str, value: Any) -> None:
            """
            Intercept attribute assignment and log it.
            """
            if not attr.startswith("__"):
                print(f"Logging: modified '{attr}'")
            orig_setattr(self, attr, value)

        cls.__getattribute__ = __getattribute__
        cls.__setattr__ = __setattr__

        return cls


class MyClass(metaclass=LoggingMeta):
    def __init__(self, name):
        self.name = name


obj = MyClass("Python")
print(obj.name)  # Logging: accessed 'name'
obj.name = "New Python"  # Logging: modified 'name'
