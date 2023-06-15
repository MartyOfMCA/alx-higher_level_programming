#!/usr/bin/python3

def roman_to_int(roman_string):
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    sum = 0
    roman_value = 0

    if not roman_string or type(roman_string) is not str:
        return (0)

    for index in range(0, len(roman_string), 1):
        roman_value = roman[roman_string[index].upper()]
        if (index > 0):
            if (roman[roman_string.upper()[index - 1]] < roman_value):
                sum -= (roman[roman_string.upper()[index - 1]] * 2)
        sum += roman_value

    return (sum)
