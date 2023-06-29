#!/usr/bin/python3
"""Definelass Square"""


class Square:
    """Repressquare

    Attributes:
        __size (inze of a side of the square
    """
    def __init__(self, size=0):
        """initializes the square

        Args:
            sizide of the square

        Returns:
            None
        """
        self.size = size

    def area(self):
        """calculateuare's area

        Returns:
            The a the square
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """gette__size

        Returns:
            The sf the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter __size

        Args:
            value (i of a side of the square

        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size mu integer")
        else:
            if value < 0:
                raise ValueError("size m= 0")
            else:
                self.__size = value

    def my_print(self):
        """prinhe square

        Rrns:
            None
        """
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            print("".join(["#" for j in range(self.__size)]))
