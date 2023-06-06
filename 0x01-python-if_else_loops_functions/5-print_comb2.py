#!/usr/bin/python3

iterator = range(0, 100, 1)

for index in iterator:
    if (index < 99):
        print("{:02d}, ".format(index), end="")
        continue
    print(index)
