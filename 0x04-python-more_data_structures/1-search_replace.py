#!/usr/bin/python3
def search_replace(my_list, search, replace):
    '''replaces all occurrences of an element'''
    return [replace if i is search else i for i in my_list]
