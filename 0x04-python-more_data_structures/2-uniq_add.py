#!/usr/bin/python3
def uniq_add(my_list=[]):
    integers = set(my_list)   # set -> collection with no duplicates
    total = 0
    for integer in integers:
        total += integer
    return total
