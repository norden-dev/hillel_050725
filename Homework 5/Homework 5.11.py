from typing import Any, Dict, Tuple, Type


class LimitedAttributesMeta(type):
    """Metaclass that limits the number of attributes a class can have."""

    max_attrs: int = 3

    def __new__(
            mcs: Type["LimitedAttributesMeta"],
            name: str,
            bases: Tuple[type, ...],
            cls_dict: Dict[str, Any],
    ) -> type:
        """Creates a new class and checks the number of user-defined attributes."""
        attrs = [attr for attr in cls_dict if not attr.startswith("__")]

        if len(attrs) > mcs.max_attrs:
            raise TypeError(
                f"Клас {name} не може мати більше {mcs.max_attrs} атрибутів."
            )

        return super().__new__(mcs, name, bases, cls_dict)


class LimitedClass(metaclass=LimitedAttributesMeta):
    attr1 = 1
    attr2 = 2
    attr3 = 3
    # attr4 = 4  # Викличе помилку

obj = LimitedClass()
