#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Represuare

    Attri
        __size (i a side of the square
    """
    def __init__(self, size=0):
        """initithe square

        Args:
            sizesize of a side of the square

        Returns:
            None
        """
        self.size = size

    def area(self):
        """calculuare's area

        Returns:
            The ahe square
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """getter of __size

        Returns:
            The  square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter of __size

        Args:
            vathe size of a size of the square

        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size  an integer")
        else:
            if value < 0:
                raise ValueError("sizebe >= 0")
            else:
                self.__size = value
