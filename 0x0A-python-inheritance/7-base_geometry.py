#!/usr/bin/python3
"""
Contains the classeGeometry
"""


class BaseGeometry:
    """A class with publimethods area and integer_validator"""
    def area(self):
        """raises an exception whenlled"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates that value is aner greater than 0"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
