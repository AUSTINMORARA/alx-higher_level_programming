#!/usr/bin/python3
def uniq_add(my_list=0):
    '''adds all unique integers in a list'''
    set_it = set(my_list)
   
    sm = 0
    for i in set_it:
        sm += i
    return sm
