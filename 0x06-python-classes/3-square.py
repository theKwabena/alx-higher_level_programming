#!/usr/bin/python3
"""Defin class Square"""


class Square:
    """Reprs a square

    Attributes:
        __sizesize of a side of the square
    """
    def __init__(self, size=0):
        """initis the square

        Args:
            size (ize of a side of the square

        Returs:
            None
        """
        if type(size) is not int:
            raise TypeError("size mu an integer")
        else:
            if size < 0:
                raise ValueError("size m be >= 0")
            else:
                self.__size = size

    def area(self):
        """calcs the square's area

        Rets:
            The aof the square
        """
        return (self.__size) ** 2
