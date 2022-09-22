#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    av = sys.argv
    ac = len(av)
    if ac != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if ac == 4:
        a = int(av[1])
        b = int(av[3])
        if av[2] == "+":
            result = add(a, b)
        elif av[2] == "-":
            result = sub(a, b)
        elif av[2] == "*":
            result = mul(a, b)
        elif av[2] == "/":
            result = div(a, b)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
        print(result)
