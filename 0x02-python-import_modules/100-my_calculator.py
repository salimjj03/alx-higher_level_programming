#!/usr/bin/python3
def calc():
    from sys import argv, exit
    from calculator_1 import sub, add, mul, div
    a = int(argv[1])
    operator = argv[2]
    b = int(argv[3])
    if len(argv) != 4:
        print("./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if operator == '+':
        result = add(a, b)
    elif operator == '-':
        result = sub(a, b)
    elif operator == '*':
        result = mul(a, b)
    elif operator == '/':
        result = div(a, b)
    elif operator not in '/-+*':
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print(f"{a} {operator} {b} '=' {result}")


if  __name__ == "__main__":
    calc()
