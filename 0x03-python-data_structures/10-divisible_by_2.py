#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    if len(my_list) != 0:
        new_list = my_list[:]
    else:
        return None

    for x in new_list:
        if x % 2 == 0:
            new_list.replace(True)
        new_list.replace(False)
    return new_list
