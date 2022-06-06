#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    isdivisible = []
    for i in my_list:
        isdivisible.append(i % 2 == 0)
    return isdivisible
