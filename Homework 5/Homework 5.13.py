from typing import Any, Dict, Tuple, Type


class AutoMethodMeta(type):
    """
    Metaclass that automatically generates getter and setter methods
    for each non-callable class attribute.
    """

    def __new__(
        mcs: Type["AutoMethodMeta"],
        name: str,
        bases: Tuple[type, ...],
        namespace: Dict[str, Any]
    ) -> Type:
        """
        Create a new class and inject automatically generated
        getter and setter methods into its namespace.

        """

        attrs = [
            key for key, value in namespace.items()
            if not key.startswith("__") and not callable(value)
        ]

        for attr in attrs:
            get_name = f"get_{attr}"
            set_name = f"set_{attr}"

            if get_name not in namespace:
                def getter(self: Any, attr: str = attr) -> Any:
                    """
                    Return the value of the specified instance attribute.
                    """
                    return getattr(self, attr)

                namespace[get_name] = getter

            if set_name not in namespace:
                def setter(self: Any, value: Any, attr: str = attr) -> None:
                    """
                    Set a new value for the specified instance attribute.
                    """
                    setattr(self, attr, value)

                namespace[set_name] = setter

        return super().__new__(mcs, name, bases, namespace)


class Person(metaclass=AutoMethodMeta):
    name = "John"
    age = 30


p = Person()
print(p.get_name())  # John
p.set_age(31)
print(p.get_age())  # 31
