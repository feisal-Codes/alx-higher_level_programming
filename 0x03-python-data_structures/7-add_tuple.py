#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    empty = (0, 0)
    tuple_c = ()
    tuple1 = tuple_a + empty
    tuple2 = tuple_b + empty
    tuple_c = tuple1[0] + tuple2[0], tuple1[1] + tuple2[1]
    return tuple_c
