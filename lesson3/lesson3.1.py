a = float(input("Введіть перше число: "))
operation = input("Введіть дію (+, -, *, /): ")
b = float(input("Введіть друге число: "))

if operation == "+":
    print("Результат:", a + b)
elif operation == "-":
    print("Результат:", a - b)
elif operation == "*":
    print("Результат:", a * b)
elif operation == "/":
    if b == 0:
        print("Помилка: ділення на нуль неможливе!")
    else:
        print("Результат:", a / b)
else:
    print("Невідома операція!")
