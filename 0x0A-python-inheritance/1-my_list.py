#!/usr/bin/python3
"""
containsist class
"""


class MyList(list):
    """a subclass  list"""
    def __init__(self):
        """initiali the object"""
        super().__init__()

    def print_sorted(self):
        """prints tsorted list"""
        print(sorted(self))
