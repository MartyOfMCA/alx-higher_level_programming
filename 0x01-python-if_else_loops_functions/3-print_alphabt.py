#!/usr/bin/python3

iterator = range(97, (97 + 26), 1)

for index in iterator:
    if (index == 101 or index == 113):
        continue
    print("{}".format(chr(index)), end="")
