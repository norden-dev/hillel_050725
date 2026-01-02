subscribers = []


def subscribe(name: str) -> str:
    """Adds a subscriber """
    subscribers.append(name)

    def confirm_subscription() -> str:
        """Confirms the subscription."""
        return f"Підписка підтверджена для {name}"

    return confirm_subscription()


def unsubscribe(name: str) -> str:
    """Removes a subscriber"""
    if name in subscribers:
        subscribers.remove(name)
        return f"{name} Успішно відписаний"
    else:
        return f"Підписника з ім'ям '{name}' не знайдено"


print(subscribe("Олена"))
print(subscribe("Ігор"))
print(subscribers)
print(unsubscribe("Ігор"))
print(subscribers)
