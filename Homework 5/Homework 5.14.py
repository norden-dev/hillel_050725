from typing import Any, Dict, Type


class TypeCheckedMeta(type):
    """
    Metaclass that enforces runtime type checking for attributes
    based on their type annotations.
    """

    def __new__(
            mcs: Type["TypeCheckedMeta"],
            name: str,
            bases: tuple[type, ...],
            namespace: Dict[str, Any],
    ) -> Type:
        """
        Create a new class and inject a custom __setattr__ method
        that validates attribute types at runtime.
        """

        cls = super().__new__(mcs, name, bases, namespace)

        all_annotations: Dict[str, Any] = {}
        for base in reversed(cls.__mro__):
            all_annotations.update(getattr(base, "__annotations__", {}))

        def __setattr__(self: Any, key: str, value: Any) -> None:
            """
            Validate the type of the assigned value against the
            expected type from annotations before setting the attribute.
            """
            if key in all_annotations:
                expected_type = all_annotations[key]
                if not isinstance(value, expected_type):
                    raise TypeError(
                        f"For attribute '{key}' expected type "
                        f"'{expected_type.__name__}', but got "
                        f"'{type(value).__name__}'."
                    )

            object.__setattr__(self, key, value)

        cls.__setattr__ = __setattr__

        return cls


class Person(metaclass=TypeCheckedMeta):
    name: str = ""
    age: int = 0


p = Person()
p.name = "John"  # Все добре
p.age = "30"  # Викличе помилку, очікується int
