#!/usr/bin/python3
""" This module defines a class 'Square' """


class Square:
    """ Definition of a square by its size. """

    def __init__(self, size=0):
        """ Initialize size attribute with validation."""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
