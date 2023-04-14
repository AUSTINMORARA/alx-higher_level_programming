#!/usr/bin/python3
"""MyList Module"""


class MyList(list):
    """List class"""

    def __init__(self):
        """initiate my class"""
        super().__init__()

    def print_sorted(self):
        """instance method that prints list"""
        print(sorted(list))
