#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dictionary2 = {}
    for i in a_dictionary:
        dictionary2[i] = a_dictionary[i] * 2
    return dictionary2
