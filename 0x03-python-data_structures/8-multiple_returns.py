#!/usr/bin/python3


def multiple_returns(sentence):
    res_tuple = ()
    if len(sentence) == 0:
        res_tuple = len(sentence), None
    else:
        res_tuple = len(sentence), sentence[0]

    return res_tuple
