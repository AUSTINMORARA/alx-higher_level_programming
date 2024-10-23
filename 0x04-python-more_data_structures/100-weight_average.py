#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list and len(my_list):
        num = 0
        denominator = 0
        for t in mylist:
            num += (t[0] * t[1])
            denominator += (t[1])
        return (num/denominator)
    return (0)
