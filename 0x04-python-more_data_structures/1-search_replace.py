#!/usr/bin/python3

def search_replace(my_list, search, replace):
    i = 0
    n = len(my_list)

    while i < n:
        if my_list[i] == search:
            my_list[i] = replace
        i += 1 
