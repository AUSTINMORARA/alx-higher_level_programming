#!/usr/bin/python3
'''Square class defination'''


class Square:
    '''Square class declaration'''

    def __init__(self, size=0):
        '''Square initialization

        Args:
            size:size of square
        '''
        self.size = size

    @property
    def size(self):
        '''Retrieves size of the square'''
        return self.__size

    @size.setter
    def size(self, value):
        '''Sets size of the square

            Args:
                value: to be evaluated
            Raises:
                TypeError:If value is not an integer
                ValueErroe:If value is less than 0
        '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        '''Calculates the area of the square.'''
        return self.__size * self.__size

    def my_print(self):
        '''Creates square with # character'''
        for i in range(self.__size):
            [print("#", end="") for j in range(self.__size)]
            print('\n')
        if self.__size == 0:
            print()
