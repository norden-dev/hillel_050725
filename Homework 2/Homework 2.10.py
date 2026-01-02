from typing import Callable, Tuple


def create_product(name: str, price: float, quantity: int) -> Tuple[Callable[[], str], Callable[[float], str]]:
    """Creates a product with the specified parameters and returns functions to retrieve information and update the price. """
    product = {
        "name": name,
        "price": price,
        "quantity": quantity
    }

    def get_info() -> str:
        """Returns product information."""
        return f"Продукт: {product['name']}, Ціна: {product['price']}, Кількість: {product['quantity']}"

    def set_price(new_price: float) -> str:
        """Updates the product price. """
        product["price"] = new_price
        return f"Ціна за {product['name']} була оновлена до {product['price']}."

    return get_info, set_price


get_info, set_price = create_product("Backpack", 1000, 10)
print(get_info())
print(set_price(1200))
print(get_info())
