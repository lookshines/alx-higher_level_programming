#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = []
    tuple_1 = tuple_a + (0, 0)
    tuple_2 = tuple_b + (0, 0)
    for i in range(0, len(tuple_a)):
        new_tuple.append(tuple_1[i] + tuple_2[i])
    new_tuple = tuple(new_tuple)
    return new_tuple
