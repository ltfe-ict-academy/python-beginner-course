"""Simple calculator."""

print("Welcome to the simple calculator! Enter exit to quit.")

while True:
    number_01 = input("Enter number one: ")
    if number_01.lower() == "exit":
        break

    number_02 = input("Enter number two: ")
    if number_02.lower() == "exit":
        break

    operation_sign = input("Enter operation sign [+,-,*,/]: ")
    if operation_sign.lower() == "exit":
        break

    number_01 = float(number_01)
    number_02 = float(number_02)
    result = None
    if operation_sign == "+":
        result = number_01 + number_02
    elif operation_sign == "-":
        result = number_01 - number_02
    elif operation_sign == "*":
        result = number_01 * number_02
    elif operation_sign == "/":
        result = number_01 / number_02
    else:
        print("Wrong operation sign!")

    if result is not None:
        print(f"Result {number_01}{operation_sign}{number_02}={result}")
