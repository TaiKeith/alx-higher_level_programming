#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    if len(my_list) != 0:
        return None

    new_list = []

    for x in my_list:
        if x % 2 == 0:
            new_list.append(True)
        new_list.append(False)
    return new_list
