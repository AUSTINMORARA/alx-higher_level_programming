#!/usr/bin/python3

def common_elements(set_1, set_2):
    empty = set()
    #could use set_1.intersection(set_2)
    for i in set_1:
        for j in set_2:
            if i == j:
                empty.add(i)
    return empty
