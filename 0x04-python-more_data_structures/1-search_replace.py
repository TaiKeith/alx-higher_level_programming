#!/usr/bin/python3

def search_replace(my_list, search, replace):
    def search_search(num):
        return num if num != search else replace
    return list(map(search_search, my_list)) 
