#!/usr/bin/python3

import sys

if (__name__ == "__main__"):
    sum = 0
    argv_count = - 1

    for arg in sys.argv:
        argv_count += 1
        if (argv_count == 0):
            continue
        sum += int(arg)
    print(sum)
