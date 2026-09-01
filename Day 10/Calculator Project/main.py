def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operator = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    first_number = float(input("Enter the first number: \n"))

    should_accumulate = True

    while should_accumulate:

        for symbol in operator:
            print(symbol)

        operator_symbol = input("Enter the operator of your choice:\n")

        second_number = float(input("Enter the second number:\n"))

        answer = operator[operator_symbol](first_number, second_number)

        print(f"{first_number} {operator_symbol} {second_number} = {answer}")

        choice = input(
            f"Type 'y' to continue calculating with {answer}, "
            f"or type 'n' to start a new calculation: "
        )

        if choice == "y":
            first_number = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()


calculator()