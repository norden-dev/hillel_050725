while True:
    number1 = int(input("Enter a first number: "))
    operation = input("Enter operation (+, -, *, /): ")
    number2 = int(input("Enter a second number: "))

    if operation == "+":
        result = number1 + number2
        print("Result:", result)
    elif operation == "-":
        result = number1 - number2
        print("Result:", result)
    elif operation == "*":
       result = number1 * number2
       print("Result:", result)
    elif operation == "/":
        if number2 != 0:
            result = number1 / number2
            print("Result:", result)
        else:
            print("Error")
    else:
        print("Unknown operation")
    continue_calc = input("yes y если продолжить")
    if continue_calc not in('yes', 'y'):
        break


