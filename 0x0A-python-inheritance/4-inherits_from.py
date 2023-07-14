#!/usr/bin/python3
"""
Contains the inction
"""


def inherits_from(obj, a_class):
    """returns true if obj is  of a_class, otherwise false"""
    return(issubclass(type(obj), a_class) and type(obj) != a_class)
