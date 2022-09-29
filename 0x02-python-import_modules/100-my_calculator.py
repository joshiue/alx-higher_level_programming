#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    num_arg = len(argv[1:])
    if num_arg != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    sign = ['+', '-', '*', '/']
    if argv[2] not in sign:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    num1 = int(argv[1])
    num2 = int(argv[3])
    op = argv[2]
    if op == "+":
        print("{:d} + {:d} = {:d}".format(num1, num2, add(num1, num2)))
    if op == "-":
        print("{:d} - {:d} = {:d}".format(num1, num2, sub(num1, num2)))
    if op == "*":
        print("{:d} * {:d} = {:d}".format(num1, num2, mul(num1, num2)))
    if op == "/":
        print("{:d} / {:d} = {:d}".format(num1, num2, div(num1, num2)))
