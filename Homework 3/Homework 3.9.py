class Product:
    """
    Represents a product using explicit getter and setter methods
    to control access to the price attribute.
    """

    def __init__(self, name: str, price: float):
        self.name = name
        self.set_price(price)

    def get_price(self) -> float:
        """
        Returns the current price of the product.
        """
        return self.__price

    def set_price(self, new_price: float) -> None:
        """
        Sets a new price for the product with validation.
        """
        if new_price < 0:
            raise ValueError("Price cannot be less than zero")
        self.__price = new_price


class ProductWithProperty:
    """
    Represents a product using the @property decorator
    to manage access to the price attribute.
    """

    def __init__(self, name: str, price: float):
        self.name: str = name
        self.price: float = price

    @property
    def price(self) -> float:
        """
        Returns the current price of the product.
        """
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """
        Sets a new price for the product with validation.
        """
        if new_price < 0:
            raise ValueError("Price cannot be less than zero")
        self.__price = new_price


class Descriptor:
    """
    Descriptor that controls access to a price attribute
    and validates assigned values.
    """

    def __set_name__(self, owner, name: str) -> None:
        self.name: str = "_" + name

    def __get__(self, instance, owner) -> float:
        """
        Returns the stored value from the instance.
        """
        return instance.__dict__[self.name]

    def __set__(self, instance, value: float) -> None:
        """
        Sets a value on the instance with validation.
        """
        if value < 0:
            raise ValueError("Value cannot be less than zero")
        instance.__dict__[self.name] = value


class CurrencyDescriptor:
    """
    Descriptor that controls the currency and performs
    price conversion when the currency changes.
    """

    RATES = {
        "USD": 1.0,
        "EUR": 0.9
    }

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        value = value.upper()

        if value not in self.RATES:
            raise ValueError("Unsupported currency")

        old_currency = instance.__dict__.get(self.name, value)

        if "_price" in instance.__dict__:
            price_in_usd = instance.price / self.RATES[old_currency]
            instance._price = price_in_usd * self.RATES[value]

        instance.__dict__[self.name] = value


class ProductWithDescriptor:
    """
    Represents a product that uses a descriptor
    to manage the price attribute.
    """

    price = Descriptor()
    currency = CurrencyDescriptor()

    def __init__(self, name: str, price: float, currency: str):
        self.name = name
        self.currency = currency
        self.price = price


product1 = ProductWithDescriptor("backpack", 90, "eur")
product2 = ProductWithDescriptor('backpack', 100, "usd")
print(product1.price)
product1.currency = "USD"
print(product1.price)

product3 = ProductWithProperty("backpack2", 100)
product4 = Product("backpack3", 800)
