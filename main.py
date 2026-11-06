from functions import add, sub


def main():
    expression = input("Expression: ")
    items = expression.split()

    operator = items[1]
    number1 = float(items[0])
    number2 = float(items[-1])

    if operator == "+":
        result = add(number1, number2)
    elif operator == "-":
        result = sub(number1, number2)

    print(f"Result: {result}")


if __name__ == "__main__":
    main()
    