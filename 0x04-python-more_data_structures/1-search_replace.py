#!/usr/bin/python3
def search_replace(my_list, search, replace):
    '''replaces all occurrences of an element'''
    new = []
    for i in my_list:
        if i == search:
            i = replace
            new.append(i)
        else:
            new.append(i)
    return new
