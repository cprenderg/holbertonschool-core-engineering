#!/usr/bin/env python3
"""Module that contains rectangle class"""


from base_geometry import BaseGeometry


class Rectangle(BaseGeometry):
    """Insides of a rectangle class"""

    def __init__(self, width=0, height=0):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
