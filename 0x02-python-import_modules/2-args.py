#!/usr/bin/python3

import sys

if (__name__ == "__main__"):
    argc = len(sys.argv)
    argv_count = 1

    print("{} {}".format(argc - 1, "argument" + (":" if argc - 1 == 1
          else "s:" if argc - 1 > 1 else "s.")))
    for index in range(argv_count, argc, 1):
        print("{}: {}".format(argv_count, sys.argv[index]))
        argv_count += 1
