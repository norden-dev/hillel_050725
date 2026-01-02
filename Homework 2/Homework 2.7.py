total_expense = 0


def add_expense(value: str|float) -> None:
    """adds expense"""
    global total_expense
    total_expense += value


def get_expense() -> None:
    """gets expense"""
    print(f"Загальна сума витрат: {total_expense}")



print("Вітаємо у Вашому особистому менеджері витрат!")
print("\nВи можете обрати одну з дій:")
print("+ - додати суму витрат;")
print("= - подивитись загальну суму витрат;")
print("інший ключ - завершення програми.")

while True:
    action = input("\nОберіть бажану дію: ")

    if action == "+":
        expense = int(input("Введіть суму витрат: "))
        add_expense(expense)
    elif action == "=":
        get_expense()
    else:
        break
