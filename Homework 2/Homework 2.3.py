discount = 0.1


def create_order(price: float, is_vip: bool) -> float:
    """Calculates the final price"""
    global discount
    final_price = price * (1 - discount)

    def apply_additional_discount(vip_discount: float) -> None:
        """Calculates the final price with additional discount"""
        nonlocal final_price
        final_price *= (1 - vip_discount)

    if is_vip:
        apply_additional_discount(0.05)

    return final_price


print(create_order(1000, is_vip=False))
print(create_order(1000, is_vip=True))
