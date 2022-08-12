#!/usr/bin/python3
"""
This module implements a Square object
that inherits from rectangle class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square implementation and initialization"""

    def __init__(self, size: int, x=0, y=0, id=None):
        """initialization of the square object
        """
        super().__init__(size, size, x, y, id)
        self.__size = size

    @property
    def size(self) -> int:
        """size getter function
        """
        return self.__size

    @size.setter
    def size(self, value: int):
        """size setter function
        """
        self.__size = value
        self.width = self.height = value

    def __str__(self) -> str:
        """string representation"""
        id = self.id
        size = self.__size
        x = self.x
        y = self.y
        return "[Square] ({}) {}/{} - {}".format(id, x, y, size)

    def update(self, *args, **kwargs):
        """update arguments using arguments"""
        attr = ['id', 'size', 'x', 'y']
        if args:
            for at, numb in zip(attr, args):
                setattr(self, at, numb)
        elif kwargs:
            for key, value in kwargs.items():
                if key in attr:
                    setattr(self, key, value)

    def to_dictionary(self) -> dict:
        """square to dictionary"""
        id = self.id
        size = self.__size
        x = self.x
        y = self.y
        return {'id': id, 'x': x, 'size': size, 'y': y}
