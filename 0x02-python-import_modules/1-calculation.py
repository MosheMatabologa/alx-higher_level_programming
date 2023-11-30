#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

def perform_operation(a, b, operation):
    result = operation(a, b)
    print("{:d} {} {:d} = {:d}".format(a, operation.__name__, b, result))

if __name__ == "__main__":
    a = 10
    b = 5

    perform_operation(a, b, add)
    perform_operation(a, b, sub)
    perform_operation(a, b, mul)
    perform_operation(a, b, div)
