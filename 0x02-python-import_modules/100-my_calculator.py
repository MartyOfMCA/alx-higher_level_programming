#!/usr/bin/python3

from sys import argv
from calculator_1 import add, div, mul, sub

if (__name__ == "__main__"):
    argc = len(argv) - 1
    fmt = ""
    op1 = 0
    op2 = 0
    result = 0
    opcode = ""

    if (argc == 3):
        op1 = int(argv[1])
        opcode = argv[2]
        op2 = int(argv[3])

        fmt = "{:d} {} {:d} = ".format(op1, opcode, op2)

        if (opcode == "+"):
            result = add(op1, op2)
        elif (opcode == "-"):
            result = sub(op1, op2)
        elif (opcode == "*"):
            result = mul(op1,  op2)
        elif (opcode == "/"):
            result = div(op1, op2)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)

        fmt += "{:d}".format(result)
        print(fmt)
    else:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)
