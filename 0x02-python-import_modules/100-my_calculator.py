#!/usr/bin/python3
def calc():
    from sys import argv, exit
    from calculator_1 import sub, add, mul, div
    if len(argv) != 4:
        print("./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    operator = argv[2]
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
