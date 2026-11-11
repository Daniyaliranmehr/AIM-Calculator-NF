from functions import add, sub, multiply, division, power, mod, maximum


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
    elif operator == "*":
        result = multiply(number1, number2)
    elif operator == "/":
        result = division(number1, number2)
    elif operator == "**":
        result = power(number1, number2)
    elif operator == "%":
        result = mod(number1, number2)
    elif operator == "max":
        result = maximum(number1, number2)
   
    print(f"Result: {result}")


if __name__ == "__main__":
    main()
    