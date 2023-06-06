#!/usr/bin/python3

def fizzbuzz():
    iterator = range(1, 101, 1)
    text = ""

    for index in iterator:
        if (index % 3 == 0 or index % 5 == 0):
            if (index % 3 == 0 and index % 5 == 0):
                text = "FizzBuzz"
            elif (index % 3 == 0):
                text = "Fizz"
            else:
                text = "Buzz"
            print("{} ".format(text), end="")
        else:
            print("{} ".format(index), end="")
