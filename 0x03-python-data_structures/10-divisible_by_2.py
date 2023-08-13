#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    if len(my_list != 0):
        new_list = my_list[:]
    else:
        return None

    for x in len(new_list) - 1:
        if x % 2 == 0:
            return True
        return False
    return new_list
