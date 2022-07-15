#!/usr/bin/python3
"""
This module implements a Rectangle object
that inherits from the base class
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle initialization, implementation using diff methods
    """

    def __init__(self, width: int, height: int, x=0, y=0, id=None):
        """initialization of the values
        """
        super().__init__(id)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def __str__(self) -> str:
        """string representation after override
        """
        return "[Rectangle] ({}) {}/{} - {}/{}" \
            .format(self.id, self.x, self.y, self.width, self.height)

    def check_type_value(self, name:  str, value: object, greater_equal=False):
        """type and value validation function
        """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if not greater_equal:
            if value <= 0:
                raise ValueError("{} must be > 0".format(name))
        else:
            if value < 0:
                raise ValueError("{} must be >= 0".format(name))

    @property
    def width(self) -> int:
        """width getter function using a property
        """
        return self.__width

    @width.setter
    def width(self, width: int):
        """width setter function a property setter
        """
        self.check_type_value('width', width)
        self.__width = width

    @property
    def height(self) -> int:
        """height getter function using a property
        """
        return self.__height

    @height.setter
    def height(self, height: int):
        """height setter function using a property setter
        """
        self.check_type_value('height', height)
        self.__height = height

    @property
    def x(self) -> int:
        """x getter function using a property
        """
        return self.__x

    @x.setter
    def x(self, x: int):
        """x setter using a property setter
        """
        self.check_type_value('x', x, True)
        self.__x = x

    @property
    def y(self) -> int:
        """y getter function using a property
        """
        return self.__y

    @y.setter
    def y(self, y: int):
        """y setter function using a property setter
        """
        self.check_type_value('y', y, True)
        self.__y = y

    def area(self) -> int:
        """area of the rectangle
        """
        return self.__width * self.__height

    def display(self):
        """prints rectangle in a # pattern
        """
        print('\n'*self.__y, end='')
        for l in range(self.__height):
            print(' '*self.__x + '#'*self.__width)

    def update(self, *args, **kwargs):
        """update rectangle attributes with diff arguments
        """

        values = (self.id, self.__width, self.__height, self.__x, self.__y)
        if args != ():
            self.id, self.__width, self.__height, self.__x, self.__y = \
                args + values[len(args):len(values)]
        elif kwargs:
            for (name, value) in kwargs.items():
                setattr(self, name, value)

    def to_dictionary(self) -> int:
        """rectangle to dictionary
        """

        return {
            'x': self.__x, 'y': self.__y, 'id': self.id,
            'height': self.__height, 'width': self.__width}
