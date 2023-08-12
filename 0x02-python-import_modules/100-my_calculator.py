#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    argv = sys.argv
    if len(argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(argv[1])
    op = argv[2]
    b = int(argv[3])

    op = {"+": add, "-": sub, "*": mul, "/": div}
    if argv[2] not in list(op.keys()):
        print("Unknown operator. Available operators: +, -, *, /")
        sys.exit(1)

    print("{} {} {} = {]".format(a, op, b, op(a, b)))
