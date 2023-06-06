#!/usr/bin/python3

step = 1
seeds = range(0, 9, 1)
increments = range(step, 10, 1)

for seed in seeds:
    for increment in increments:
        if (seed < 8 and increment < 10):
            print("{}{}, ".format(seed, increment), end="")
            continue
        print("{}{}".format(seed, increment))
    step += 1
    increments = range(step, 10, 1)
