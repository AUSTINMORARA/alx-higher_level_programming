#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    set_in = set()
    dif = set_1.symmetric_difference(set_2)
    for i in dif:
        set_in.add(i)
    return set_in
