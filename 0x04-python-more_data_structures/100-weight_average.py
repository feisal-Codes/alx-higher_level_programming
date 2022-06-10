#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    average = 0
    total_weight = 0
    for item in my_list:
        average += item[0] * item[1]
        total_weight += item[1]
    return (average / total_weight)
