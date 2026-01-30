class DynamicProperties:
    """
    The DynamicProperties class allows dynamic addition of properties to an instance
    at runtime. Property values are stored in an internal dictionary, and access to
    them is provided through automatically generated getters and setters.
    """

    def __init__(self) -> None:
        self._properties = {}

    def add_property(self, name: str, value: object) -> None:
        """
        Dynamically adds a new property to the object.
        """

        def getter(self) -> object:
            """
            Getter for the dynamic property.
            """
            return self._properties[name]

        def setter(self, val: object) -> None:
            """
            Setter for the dynamic property.
            """
            self._properties[name] = val

        self._properties[name] = value
        setattr(self.__class__, name, property(getter, setter))


obj = DynamicProperties()
obj.add_property('name', 'default_name')
print(obj.name)  # default_name
obj.name = "Python"
print(obj.name)  # Python
