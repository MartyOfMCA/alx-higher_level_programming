#!/usr/bin/python3

import sys
from calculator_1 import add, div, mul, sub

if (__name__ == "__main__"):
    argc = len(sys.argv) - 1
    fmt = ""
    op1 = 0
    op2 = 0
    result = 0
    opcode = ""

    if (argc == 3):
        op1 = int(sys.argv[1])
        opcode = sys.argv[2]
        op2 = int(sys.argv[3])

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
            sys.exit(1)

        fmt += "{:d}".format(result)
        print(fmt)
    else:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        sys.exit(1)
