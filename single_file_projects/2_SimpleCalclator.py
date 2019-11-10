import sys

while True:
    try:

        a = float(input("Enter a number (or a letter to exit): "))
        operator = input("Enter the operator: ")
        b = float(input("Enter a number (or a letter to exit): "))
        if operator == '+':
            result = a + b
            print(result)

        elif operator == '-':
            result = a - b
            print(result)

        elif operator == '*':
            result = a * b
            print(result)

        elif operator == '/':
            try:
                result = a / b
                print(result)
            except ZeroDivisionError:
                print("You can't devide by zero!")
        else:
            print("Unexpected input.\nChoose an operator from one of those: +, -, *, / next time.")

    except ValueError:
        sys.exit(0)
        break