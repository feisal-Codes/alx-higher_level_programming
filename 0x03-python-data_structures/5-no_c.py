#!/usr/bin/python3
def no_c(my_string):
    a = ""
    for i in my_string:
        if i not in "cC":
            a += i
    return a
