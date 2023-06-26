#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    result = 0

    for increment in range(0, list_length, 1):
        result = 0
        try:
            result = my_list_1[increment] / my_list_2[increment]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(result)

    return (new_list)
