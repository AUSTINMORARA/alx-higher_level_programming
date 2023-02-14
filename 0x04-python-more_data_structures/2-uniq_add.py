#!/usr/bin/python3
def uniq_add(my_list=[]):
    '''adds all unique integers in a list'''
    s = 0
    for i in my_list:
       set (s += i)
    return s
