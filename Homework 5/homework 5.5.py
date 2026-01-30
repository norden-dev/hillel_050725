class MutableClass:
    """
    A class that allows dynamic addition and removal of attributes at runtime.
    """

    def add_attribute(self, name: str, value: object) -> None:
        """
        Add a new attribute to the instance.
        """
        setattr(self, name, value)

    def remove_attribute(self, name: str) -> None:
        """
        Remove an attribute from the instance.

        """
        delattr(self, name)


obj = MutableClass()

obj.add_attribute("name", "Python")
print(obj.name)  # Python

obj.remove_attribute("name")
print(obj.name)  # Виникне помилка, атрибут видалений
