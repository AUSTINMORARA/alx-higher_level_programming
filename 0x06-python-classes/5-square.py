#!/usr/bin/python3
'''
Square class defination
'''


class Square:
    '''Square class declaration'''

    def __init__(self, size=0):
        '''Class initialization
            Args:
                size:size of square
        '''
        self.__size = size

    @property
    def size(self):
        '''Retrieves size'''
        return self.__size

    @size.setter
    def size(self, value):
        '''size setter
            Args:
                value: to be evaluated
        '''
        if isinstance(value, int) is not True:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        '''Calculates the area of a square.'''
        return self.__size * self.__size

    def my_print(self):
        '''Creates square with "#"'''
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print('\n')
        if self.__size == 0:
            print("")
