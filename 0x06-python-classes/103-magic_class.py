#!/usr/bin/python3
"""DefinesicClass"""
import math


class MagicClass:
    """This repcircle"""
    def __init__(self, radius=0):
        """Initialiic Class"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radiusbe a number')
        self.__radius = radius

    def area(self):
        """Calculaes tf the circle"""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """Calculates theference of the circle"""
        return 2 * math.pi * self.__radius
