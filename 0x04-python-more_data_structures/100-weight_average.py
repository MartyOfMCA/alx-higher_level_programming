#!/usr/bin/python3

def weight_average(my_list=[]):
    dividend = 0
    divisor = 0

    if (not my_list):
        return (0)

    for item in my_list:
        dividend += (tuple(item)[0] * tuple(item)[1])
        divisor += tuple(item)[1]

    return (dividend / divisor)
